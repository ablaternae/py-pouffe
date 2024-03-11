# =============================================================================
#
# =============================================================================


from . import __options__ as o
from .__about__ import *
from .__meta__ import Meta
from .__options__ import Options

# from .http import *
# from .http import server as http_server
import sys

try:
    print('TRY ---')
    print(__name__)
    # print(sys.modules[__name__])
    print(hasattr(sys.modules[__name__], 'options'))
    print(hasattr(sys.modules['poufdb.__options__'], 'options'))
    print(hasattr(o, 'options'))
    print(sys.modules['poufdb.__options__'].Options)
    print(sys.modules[__name__].dir())
    print('options' in sys.modules['poufdb'].vars())
    print(options)
    options
except (AttributeError, NameError) as exc:
    print('except', exc)
    options = o.Options().from_object(o)
    sys.modules['poufdb.__options__'].options = options


__all__ = ("Meta", "options")
