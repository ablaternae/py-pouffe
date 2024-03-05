# =============================================================================
#
# =============================================================================

import sys

from flask import Flask

from ..__about__ import *
from ..options import APP_DEBUG, HTTP_HOST, HTTP_PORT

app = Flask(__name__)
# app.debug = True не работает, при перезагрузке падает процесс EOFError: Ran out of input


@app.route("/")
async def index():
    return (
        {
            name(): "Welcome!",
            "version": version(),
            "python_version": sys.version,
            "id": id(),
            # "uuid": request.app.state.server_id.hex,
            "features": [],
            "author": author(),
            # "vendor": {"name": "Marten de Vries"},
        },
        200,
    )


@app.route("/_all_dbs")
@app.route("/_session")
@app.route("/_utils")  #   static admin oanel
@app.route("/_uuids")
async def no_answer():
    return {}, 501


@app.route("/<db>/", methods=["PUT"])
@app.route("/<db>/", methods=["DELETE"])
@app.route("/<db>/")
async def no_db(db=None):
    return str(db), 501


def start():
    # для мультипроцессинга нужна обертка в обычную функцию
    app.run(host=HTTP_HOST, port=HTTP_PORT, threaded=True)


__all__ = ("app", "start")
