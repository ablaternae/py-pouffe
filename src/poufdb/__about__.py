# SPDX-FileCopyrightText: 2024-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT

__version__ = "0.2.2a5"


from importlib.metadata import metadata
from uuid import uuid1

meta = metadata(__name__.split(".")[0]).json
# здесь хак: name должно быть имя пакета, а не модуля


__author__ = meta["author_email"] or ""
__license__ = meta["license_expression"] or ""
__summary__ = meta["summary"] or ""
__description__ = meta["description"] or ""
__url__ = meta["project_url"] or ""

__id__ = str(uuid1())


def id():
    return __id__


def name():
    return meta["name"]


def author():
    return __author__


def version():
    return __version__


def license():
    return __license__


def summary():
    return __summary__


def description():
    return __description__


__all__ = (
    "__id__",
    # "__name__",
    "__author__",
    "__version__",
    "__license__",
    "__summary__",
    "id",
    "name",
    "author",
    "version",
    "license",
    "summary",
    "description",
    "meta",
)
