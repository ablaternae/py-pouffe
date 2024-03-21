# =============================================================================
#
# =============================================================================


import os
from types import ModuleType
from typing import Any, Callable, Iterable, List, Mapping

import information_schema

from ..options import hash, tripcode
from .options import DATABASE_DIRECTORY, DATABASE_EXTENSION, ENGINES, STORAGE

try:
    from setuptools.extern.jaraco.text import WordSet

    def make_snake_case(s):
        return WordSet.parse(s).lowered().underscore_separated()

    def make_camel_case(s):
        return WordSet.parse(s).camel_case()  # headless_camel_case()

except ImportError:
    from peewee import make_snake_case

    def make_camel_case(s):
        import re

        return re.sub(r"\w+", lambda m: m.group(0).capitalize(), s)


engine = ModuleType(__name__ + ".engine")


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

    engine = import_module(".." + kind, __name__)

    return engine


engine = get_engine()


def get_db_list(data_dir: str = None) -> Iterable:
    if not data_dir or not os.path.isdir(data_dir):
        data_dir = DATABASE_DIRECTORY

    ret = (
        f
        for f in os.scandir(data_dir)
        if f.is_file(follow_symlinks=False) and str(f).endswith(DATABASE_EXTENSION)
    )
    print(ret)


print("get_db_list", get_db_list())


def dbname_normalize(dbname: str):
    return make_snake_case(dbname)


def get_db_connect(dbname: str):
    dbname = make_snake_case(dbname)
    dbfile = os.path.join(DATABASE_DIRECTORY, dbname + DATABASE_EXTENSION)
    print(dbfile)

    # db = engine.Database(None)
    db = engine.database
    db.init(dbfile)
    db.connect(reuse_if_open=True)
    return db


__all__ = (
    "hash",
    "tripcode",
    "make_snake_case",
    "make_camel_case",
    "get_db_list",
    "DATABASE_DIRECTORY",
    "DATABASE_EXTENSION",
)
