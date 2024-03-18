# =============================================================================
#
# =============================================================================

import sys

from flask import Flask

from .. import options
from ..__about__ import *

app = Flask(__name__)


@app.route("/")
def index():
    return (
        {
            # name(): summary(),
            name(): "Welcome!",
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
def no_answer():
    return {}, 501


@app.route("/<db>/", methods=["POST"])  #   create
@app.route("/<db>/", methods=["GET"])  #   read
@app.route("/<db>/", methods=["PUT"])  #   update / insert or update
@app.route("/<db>/", methods=["DELETE"])  # delete / NB: mark as *delete*
@app.route("/<db>/_all_docs")  #   select * limit MAX_UUIDS
@app.route("/<db>/<path:p>/")
def no_db(db=None, p=None):
    return f"DB Error {str(db)}, 501 Not Implemented Yet", 501


def start(host=None, port=None, **kwargs):
    host = options.HTTP_HOST if host is None else host
    port = options.HTTP_PORT if port is None else port
    threaded = False

    app.run(host=host, port=port, threaded=threaded, **kwargs)


__all__ = ("app", "start")
