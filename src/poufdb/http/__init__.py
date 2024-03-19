# =============================================================================
#
# =============================================================================


from types import ModuleType

import information_schema

from . import const, flask, flask_async

# from .const import *


HTTP = information_schema.to_object("HTTP_", lowercase=1)
HTTP.CONST = const

print("HTTP ==", HTTP, dir(information_schema))

server = ModuleType(__name__ + ".server")


def get_server(kind=HTTP.driver) -> ModuleType:
    #

    if kind == HTTP.driver_flask:
        server = flask

    if kind == HTTP.driver_flask_async:
        server = flask_async

    return server


server = get_server()

__all__ = ("const", "server", "HTTP", "get_server")
# __all__ = ("app", "const", "server", "options")
