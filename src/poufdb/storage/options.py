# =============================================================================
#
# =============================================================================

# from hashlib import sha256

import sortedcontainers

import information_schema

from ..options import hash, tripcode

Containers = sortedcontainers
Collection = sortedcontainers.SortedDict


UUID_MAX_COUNT = 1000  #   aka LIMIT

SQLITE_PRAGMAS = (
    ("cache_size", -1024 * 64),  # 64MB page-cache.
    ("journal_mode", "wal"),  # Use WAL-mode (you should always use this!).
    # ("foreign_keys", 1),  # Enforce foreign-key constraints.
)

DATABASE_EXTENSION = ".db"
DATABASE_DIRECTORY = information_schema["STORAGE_DATA_DIR"]


STORAGE = information_schema.to_object("STORAGE_", lowercase=1)
ENGINES = information_schema["ENGINES"] = information_schema.to_dict("STORAGE_ENGINE_")
