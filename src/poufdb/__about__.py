# =============================================================================
#
# =============================================================================


__version__ = "0.2.5a15"


from importlib.metadata import metadata
from uuid import uuid1

from .options import hash

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


id = lambda: __id__
uuid = lambda: __uuid__
vendor = lambda: __vendor__
name = lambda: meta["name"]
author = lambda: __author__
version = lambda: __version__
license = lambda: __license__
summary = lambda: __summary__
description = lambda: __description__


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
