# =============================================================================
#
# =============================================================================


from . import __options__ as options
from .__about__ import *
from .__meta__ import Meta
from .__options__ import Options

# from .http import *
# from .http import server as http_server

try:
    defaults = options.defaults
    # options
except (AttributeError, NameError) as exc:
    defaults = Options().from_object(options)


__all__ = ("Meta", "Options", "options", "defaults")
