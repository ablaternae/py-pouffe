# =============================================================================
#
# =============================================================================

import sys

from flask import Flask

from .. import options
from ..__about__ import *

# from ..options import APP_DEBUG, HTTP_HOST, HTTP_PORT
print("flask options", options)
app = Flask(__name__)
# app.debug = True не работает, при перезагрузке падает процесс EOFError: Ran out of input


@app.route("/")
async def index():
    return (
        {
            # name(): "Welcome!",
            name(): summary(),
            "uuid": uuid(),
            "id": id(),
            "version": version(),
            "python_version": sys.version,
            "features": [],
            "vendor": vendor(),
        },
        200,
    )


@app.route("/_all_dbs")
@app.route("/_session")
@app.route("/_utils")  #   static / admin oanel
@app.route("/_uuids")
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
    host = options.HTTP_HOST if host is None else host
    port = options.HTTP_PORT if port is None else port
    threaded = True

    print("OPTIONS HTTP_PORT", port, host)
    print("OPTIONS ", options)
    # для мультипроцессинга нужна обертка в обычную функцию
    app.run(host=host, port=port, threaded=threaded, **kwargs)


__all__ = ("app", "start")
