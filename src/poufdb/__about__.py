# =============================================================================
#
# =============================================================================


__version__ = "0.2.5a9"


from importlib.metadata import metadata
from uuid import uuid1

from .__options__ import hash

meta = metadata(__name__.split(".")[0]).json
# здесь хак: name должно быть имя пакета, а не модуля


__author__ = meta["author_email"] or ""
__license__ = meta["license_expression"] or ""
__summary__ = meta["summary"] or ""
__description__ = meta["description"] or ""
__url__ = meta["project_url"] or ""

__vendor__ = "ablaternae.github.io/py-pouffe"
__uuid__ = str(uuid1())
__id__ = hash(f"{__vendor__}:{__uuid__}")


def id():
    return __id__


def uuid():
    return __uuid__


def vendor():
    return __vendor__


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
    "uuid",
    "name",
    "author",
    "version",
    "license",
    "summary",
    "vendor",
    "description",
    "meta",
)
