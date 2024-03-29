# =============================================================================
#
# http proxy to sql
#
# official api https://docs.couchdb.org/en/stable/api/index.html
# base api https://www.tutorialspoint.com/couchdb/couchdb_http_api.htm
# client https://couchdb-python.readthedocs.io/en/latest/client.html#server
#
# =============================================================================

"""
https://www.tutorialspoint.com/couchdb/couchdb_http_api.htm

GET − This format is used to get a specific item. To get different items, you have to send specific url patterns. In CouchDB using this GET request, we can get static items, database documents and configuration, and statistical information in the form of JSON documents (in most cases).

HEAD − The HEAD method is used to get the HTTP header of a GET request without the body of the response.

POST − Post request is used to upload data. In CouchDB using POST request, you can set values, upload documents, set document values, and can also start certain administration commands.

PUT − Using PUT request, you can create new objects, databases, documents, views and design documents.

DELETE − Using DELETE request, you can delete documents, views, and design documents.

COPY − Using COPY method, you can copy documents and objects.
"""
"""
Response headers

Content-type − This header specifies the MIME type of the data returned by the server. For most request, the returned MIME type is text/plain.

Cache-control − This header suggests the client about treating the information sent by the server. CouchDB mostly returns the must-revalidate, which indicates that the information should be revalidated if possible.

Content-length − This header returns the length of the content sent by the server, in bytes.

Etag − This header is used to show the revision for a document, or a view.
"""


import gzip
import sys
from typing import Any, Dict, Iterable, List, Union

from flask import Flask, Response, abort, make_response, request, session

from .. import storage
from ..__about__ import *
from ..storage import engine
from . import const

app = Flask(__name__)
# app.debug = True не работает, при перезагрузке падает процесс EOFError: Ran out of input


async def response(
    content: Union[str, dict, list], status=None, headers=None
) -> Response:
    if not status:
        status = const.status.OK
    if not headers:
        headers = {}

    resp = make_response(content, status, headers)

    if isinstance(content, (List, Dict, Iterable)):
        resp.content_type = const.CONTENT_JSON
    elif isinstance(content, str):
        resp.content_type = const.CONTENT_HTML
    else:
        abort(500, "Unknown content")
    return resp


@app.before_request
async def event_before() -> None | Response:
    print(
        "before ==>",
        # dir(request),
        # dict(request.args),
        request.path,
        request.script_root,
        request.url_root,
    )

    func = request.path.lower().replace("/", "")
    print(func)

    if not func.startswith("_"):
        return

    if hasattr(storage, func):
        try:
            resp = await response(
                {**storage.func.__call__(**request.args), **const.SUCCESS}
            )
        except Exception as exc:
            resp = await response(const.BAD_REQUEST, 500)

    return


@app.after_request
async def event_after_latest(response: Response) -> Response:

    if request.method not in ("GET", "POST"):
        return response

    # https://stackoverflow.com/questions/30165475/how-to-compress-minimize-size-of-json-jsonify-with-flask-in-python
    # accept_encoding = request.headers.get("Accept-Encoding", "")
    accept_encoding = request.accept_encodings
    # print(accept_encoding, response.status_code)
    response_data = response.get_data()
    len_data = len(response_data)

    if (
        response.status_code < 200
        or response.status_code > 299
        or response.direct_passthrough
        or len_data < const.MINIMUM_DEFLATE_SIZE
        or "gzip" not in accept_encoding.lower()
        or "Content-Encoding" in response.headers
    ):
        return response

    content = gzip.compress(response_data, compresslevel=const.GZIP_COMPRESS_LEVEL)
    response.set_data(content)
    response.headers["Content-Encoding"] = "gzip"
    response.headers["Content-Length"] = len(content)

    return response


@app.route("/", methods=["POST", "GET"])
async def index():

    # @after_this_request
    # def func(response: Response) -> Response:
    #    return response

    return await response(
        {
            # name(): "Welcome!",
            name(): summary(),
            "uuid": uuid(),
            "id": id(),
            "version": version(),
            "python_version": sys.version,
            "features": [],
            "vendor": vendor(),
            # "author": author(),
        },
        const.status.OK,
    )


@app.route("/_all_dbs/")
@app.route("/_session/")
@app.route("/_utils/")  #   static / admin oanel
@app.route("/_uuids/")
async def no_answer():
    return {}, 501


@app.route("/<db>/", methods=["POST"])  #   create
# return {"ok":true,"id":"c6e2f3d7f8d0c91ce7938e9c0800131c","rev":"1-abadd48a09c270047658dbc38dc8a892"} # 32 символа sha1
# couch даёт служебные поля с подчеркиванием _id _rev _deleted
@app.route("/<db>/", methods=["GET"])  #   read
@app.route("/<db>/", methods=["PUT"])  #   update / insert or update
@app.route("/<db>/", methods=["DELETE"])  # delete / NB: mark as *delete*
# как работает удаление https://habr.com/ru/articles/139325/


@app.route("/<db>/")
@app.route("/<db>/_all_docs")  #   select * limit MAX_UUIDS
async def no_db(db=None):
    from ..storage import engine

    # print(engine.db.create())

    return f"DB Error {str(db)}, 405 Method Not Allowed", 405


@app.route("/{db}/_design/{field??}/_view/{view_name??}")
async def not_found():
    return f"http error 406 Not Acceptable", 406


"""
CouchDB на самом деле не завязан ни на какой конкретный язык, 
а использует абстракцию в виде View-сервера. Т.е. вы просто подключаете view-сервер 
для вашего любимого языка программирования и пишите map() и reduce() например на Python, 
пользуясь его его богатой стандартной библиотекой.

По большому счёту, никто не мешает вам при добавлении нового документа прямо из map() 
осуществить геокодинг адреса вашего добавляемого в базу клиента с помощью внешнего 
сервиса (Google Maps API например) и посчитать для него геоиндекс другой внешней библиотекой. 
Или просто проиндексировать документ с помощью Sphinx, получив ещё и супербыстрый 
полнотекстовый индекс вашей БД. В общем, простор для творчества ограничен только фантазией.

Если нужно больше скорости, то все view-функции можно переписать на C, воспользовавшись фактом, 
что интерфейс view-сервера прост как лопата, а view в CouchDB — это точно такой же документ, 
а точнее design-документ со специальным ID. Поэтому ему совсем не обязательно содержать 
непосредственно код функций — можно положить туда в том числе любой идентификатор, 
который будет понятен вашему view-серверу. Заметно, что это идейное единство данных и 
инструкций по их обработке в виде точно таких же данных сродни идеологии Lisp.

https://habr.com/ru/articles/101251/
"""


def start(host=None, port=None, **kwargs):
    """для мультипроцессинга нужна обертка в обычную функцию"""

    host = config.HTTP_HOST if host is None else host
    port = config.HTTP_PORT if port is None else port
    threaded = True

    # print("OPTIONS HTTP_PORT", port, host)
    # print("OPTIONS ", config)

    app.run(host=host, port=port, threaded=threaded, **kwargs)


__all__ = ("app", "start")
