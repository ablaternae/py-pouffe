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
Collection = sortedcontainers.SortedList
Document = json
Register = sortedcontainers.SortedDict

from .utils import dbname_normalize, get_db_connect


class Database(ModuleType):
    """Databases (docs collections) List."""

    _register: Register = Register()
    _current_db: str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._current_db = dbname_normalize(args[0])

        # if not dbname in self:
        self[self._current_db] = get_db_connect(self._current_db)

        print(self._register.keys())
        print(self._current_db in self._register.keys())

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
        return list(self._register)

    def __getitem__(self, name: str) -> Any:
        return self._register[str(name)] if str(name) in self._register else None

    def __setitem__(self, name: str, value: Any = None) -> Any:
        return self._register.setdefault(str(name), value)

    # https://docs.peewee-orm.com/en/latest/peewee/database.html#setting-the-database-at-run-time

    @classmethod
    def create(cls, dbname: str):
        """create or open dbname"""
        return cls().__init__(dbname, pragmas=SQLITE_PRAGMAS)

    @classmethod
    def read(cls, dbname: str):
        """read info about dbname"""
        return cls()

    @classmethod
    def update(cls, dbname: str):
        """ update WHAT ?"""
        return cls()

    @classmethod
    def delete(cls, dbname: str):
        """
        remove db-file to %data_dir%/_backups/dbname-%Y-%M-%d-%m-%i
        if isset STORAGE_DELETE_BACKUPS
        """
        return True

    pass


sys.modules[__name__].__class__ = Database


__all__ = ()
