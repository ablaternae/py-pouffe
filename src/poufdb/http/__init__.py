# =============================================================================
#
# =============================================================================


from types import ModuleType

import information_schema

from . import const, flask, flask_async

HTTP = information_schema.to_object("HTTP_", lowercase=1)
HTTP.CONST = const

SERVERS = information_schema["HTTP_SERVERS"] = information_schema.to_dict(
    "HTTP_SERVER_", lowercase=0
)

print("HTTP ==", HTTP, dir(information_schema), SERVERS)
server = ModuleType(__name__ + ".server")


def get_server(kind: str = None) -> ModuleType:
    """

    :param kind: kind of http server, defaults in information_schema["HTTP_SERVERS"]
    :type kind: str, optional
    :return: ModuleType
    :raise: ImportError

    """
    if kind is None:
        if "DEFAULT" in SERVERS:
            kind = SERVERS["DEFAULT"]

    from importlib import import_module

    server = import_module("." + kind, __name__)

    return server


server = get_server()

__all__ = ("const", "server", "HTTP", "get_server")
# __all__ = ("app", "const", "server", "options")
