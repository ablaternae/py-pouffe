# =============================================================================
#
# =============================================================================


from . import __options__ as o
from .__about__ import *
from .__meta__ import Meta
from .__options__ import Options

# from .http import *
# from .http import server as http_server

try:
    tmp = o.options
    # options
except (AttributeError, NameError) as exc:
    options = o.Options().from_object(o)
    # sys.modules['poufdb.__options__'].options = options


__all__ = ("Meta", "options")
