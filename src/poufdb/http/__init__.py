#
#
#


from .. import options
from . import const

HTTP = options.get_namespace("HTTP_", lowercase=1)

print(HTTP)

if HTTP.driver == HTTP.driver_flask:
    from . import flask as server

if HTTP.driver == HTTP.driver_flask_async:
    from . import flask_async as server

__all__ = ("const", "server")
# __all__ = ("app", "const", "server", "options")
