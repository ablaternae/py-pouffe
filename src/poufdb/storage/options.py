# =============================================================================
#
# =============================================================================

# from hashlib import sha256

import sortedcontainers

from .. import options

# import hash, hash10, triphash

Containers = sortedcontainers
Collection = sortedcontainers.SortedDict


UUID_MAX_COUNT = 1000  #   aka LIMIT

SQLITE_PRAGMAS = (
    ("cache_size", -1024 * 64),  # 64MB page-cache.
    ("journal_mode", "wal"),  # Use WAL-mode (you should always use this!).
    ("foreign_keys", 1),  # Enforce foreign-key constraints.
)
