# =============================================================================
#
# =============================================================================


import sys

from . import options
from .__about__ import *
from .utils import Config

# from .http import *
# from .http import server as http_server
# from .storage import info

# print(hasattr(sys.modules[__name__], "config"))

if not hasattr(sys.modules[__name__], "config"):
    config = Config().from_object(options)

# print(config)

# __all__ = ("Meta", "Options", "defaults")
