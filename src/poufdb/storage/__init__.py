# =============================================================================
#
# =============================================================================


from types import ModuleType

import information_schema

from . import options, peewee, peewee_adv  # , utils  # , const,


STORAGE = information_schema.to_object("STORAGE_", lowercase=1)
ENGINES = information_schema["ENGINES"] = information_schema.to_dict(
    "STORAGE_ENGINE_"
)

print("ENGINES ==", ENGINES)
print("STORAGE", STORAGE)

engine = ModuleType(__name__ + ".engine")
info = {}


def get_engine(kind: str = None) -> ModuleType:
    """

    :param kind: kind of DB storage engines, defaults in information_schema["STORAGE_ENGINES"]
    :type kind: str, optional
    :return: ModuleType
    :raise: ImportError

    """
    if kind is None:
        if "DEFAULT" in ENGINES:
            kind = ENGINES["DEFAULT"]

    from importlib import import_module

    engine = import_module("." + kind, __name__)

    return engine


engine = get_engine()


__all__ = ("info", "engine", "get_engine", "ENGINES")
