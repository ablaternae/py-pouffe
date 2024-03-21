# =============================================================================
#
# =============================================================================


import sys
from types import ModuleType
from typing import Any, Callable, Iterable, List, Mapping

import sortedcontainers
import ujson as json

from .options import SQLITE_PRAGMAS

Containers = sortedcontainers
Collection = sortedcontainers.SortedDict
Document = json

from .utils import dbname_normalize, get_db_connect


class Database(ModuleType):
    """Databases (docs collections) List."""

    _collection: Collection = Collection()
    _current_db: str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._current_db = dbname_normalize(args[0])

        # if not dbname in self:
        self[self._current_db] = get_db_connect(self._current_db)

        print(self._collection.keys())
        print(self._current_db in self._collection.keys())

        ...

    def __call__(self, *args, **kwargs):
        raise TypeError(
            "`databases` module is not callable. Use class `Database( name: str )` instead"
        )

    def __repr__(self) -> str:
        import pprint

        return f"Pouf.Databases <module:{__name__}> " + pprint.pformat(
            self.__dir__(), indent=2
        )
        # return "Databases [" + ", ".join([f"'{d}'" for d in dir(self)]) + "]"

    def __dir__(self) -> list:
        return list(self._collection)

    def __getitem__(self, name: str) -> Any:
        return self._collection[str(name)] if str(name) in self._collection else None

    def __setitem__(self, name: str, value: Any = None) -> Any:
        return self._collection.setdefault(str(name), value)

    # https://docs.peewee-orm.com/en/latest/peewee/database.html#setting-the-database-at-run-time

    @classmethod
    def create(cls, dbname: str):
        return cls().init(dbname, pragmas=SQLITE_PRAGMAS)

    pass


sys.modules[__name__].__class__ = Database


__all__ = ()
