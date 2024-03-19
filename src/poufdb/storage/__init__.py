# =============================================================================
#
# =============================================================================


from types import ModuleType

# print(__name__, defaults)
import information_schema

from . import options, peewee, peewee_adv, utils  # , const,

STORAGE = information_schema.to_object("STORAGE_", lowercase=1)
information_schema['ENGINES'] = ENGINES = information_schema.to_dict("STORAGE_DRIVER_")

print('ENGINES ==', ENGINES)
print('STORAGE', STORAGE)

engine = ModuleType(__name__ + ".engine")
info = {}


def get_engine(kind=STORAGE.driver) -> ModuleType:
    #

    if kind == STORAGE.driver_sqlite:
        ENGINES['default'] = ENGINES['SQLITE']
        engine = peewee

    if kind == STORAGE.driver_sqlite_advanced:
        ENGINES['default'] = ENGINES['SQLITE_ADVANCED']
        engine = peewee_adv

    return engine


engine = get_engine()


__all__ = ("info", "engine", "get_engine", "ENGINES")
