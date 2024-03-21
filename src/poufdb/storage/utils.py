# =============================================================================
#
# =============================================================================


from ..options import hash, tripcode
from .options import DATABASE_DIRECTORY, DATABASE_EXTENSION
import os
import information_schema

import sortedcontainers
from typing import Any, Callable, Iterable, Mapping, List

Containers = sortedcontainers
Collection = sortedcontainers.SortedList
Document = sortedcontainers.SortedDict


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


def get_db_list(data_dir: str = None) -> Iterable:
    if not data_dir or not os.path.isdir(data_dir):
        data_dir = DATABASE_DIRECTORY

    ret = (
        f
        for f in os.scandir(data_dir)
        if f.is_file(follow_symlinks=False)
        and str(f).endswith(DATABASE_EXTENSION)
    )
    print(ret)


get_db_list()


__all__ = (
    "hash",
    "tripcode",
    "make_snake_case",
    "make_camel_case",
    "get_db_list",
    "DATABASE_DIRECTORY",
    "DATABASE_EXTENSION",
)
