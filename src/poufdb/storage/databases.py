# =============================================================================
#
# =============================================================================


import sys
from types import ModuleType
from typing import Any, Callable, Iterable, Mapping
from .options import tripcode as hash, SQLITE_PRAGMAS
import ujson as json

import sortedcontainers
from typing import Any, Callable, Iterable, Mapping, List

Containers = sortedcontainers
Collection = sortedcontainers.SortedDict
Document = json


class Databases(ModuleType):
    """Databases (docs collections) List."""

    _collection: Collection = []

    def __repr__(self) -> str:
        import pprint

        return (
            "<module Pouf.Databases: "
            + pprint.pformat(self.__dir__(), indent=2)
            + ">"
        )
        # return "Databases [" + ", ".join([f"'{d}'" for d in dir(self)]) + "]"

    def __dir__(self) -> list:
        return list(
            filter(
                lambda k: not isinstance(self[k], (Callable, ModuleType)),
                filter(
                    lambda k: not k.startswith("__"), self._collection.keys()
                ),
            )
        )

    def __getitem__(self, name: str) -> Any:
        return getattr(self, str(name), None)

    def __setitem__(self, name: str, value: Any = None) -> Any:
        return setattr(self, str(name), value)

    # https://docs.peewee-orm.com/en/latest/peewee/database.html#setting-the-database-at-run-time

    @classmethod
    def create(cls, dbname: str):
        return cls().init(dbname, pragmas=SQLITE_PRAGMAS)

    pass


sys.modules[__name__].__class__ = Databases


__all__ = ()