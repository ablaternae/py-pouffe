# =============================================================================
#
# =============================================================================


import sys

import information_schema

from . import __about__, options
from .__about__ import *

defaults = information_schema.from_object(options)
information_schema.from_object(__about__)

from .http import *
from .storage import *

__all__ = ("Meta", "Options", "defaults")
