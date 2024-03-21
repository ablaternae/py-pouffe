# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:01:41 2024

@author: vs
"""

# =============================================================================
#
# =============================================================================


from datetime import datetime
from typing import Any, Dict, List, Union
from types import ModuleType, SimpleNamespace
from typing import Any, Callable, Iterable, Mapping

import ujson as json

from playhouse.apsw_ext import (
    SQL,
    APSWDatabase,
    AutoField,
    BlobField,
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    IntegerField,
    Model,
    PrimaryKeyField,
    TextField,
)
from playhouse.fields import PickleField
from playhouse.hybrid import hybrid_method, hybrid_property
from playhouse.sqlite_ext import JSONField

from ..options import tripcode as hash, SQLITE_PRAGMAS

RealField = FloatField


class Database(APSWDatabase):
    # https://docs.peewee-orm.com/en/latest/peewee/database.html#setting-the-database-at-run-time

    @classmethod
    def create(cls, dbname: str):
        return cls().init(dbname, pragmas=SQLITE_PRAGMAS)

    pass
