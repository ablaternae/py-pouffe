# =============================================================================
#
# =============================================================================


from .. import defaults
from . import information_schema as info
from . import options, utils

print(defaults)

STORAGE = defaults.get_namespace("STORAGE_", lowercase=1)

print(STORAGE)

if STORAGE.driver == STORAGE.driver_peewee:
    from . import peewee as engine

if STORAGE.driver == STORAGE.driver_peewee_async:
    from . import peewee as engine

__all__ = ("info", "engine")
