# =============================================================================
#
# =============================================================================

# from hashlib import sha256

import sortedcontainers

from poufdb.options import hash, hash10, triphash

Containers = sortedcontainers
Collection = sortedcontainers.SortedDict


UUID_MAX_COUNT = 1000  #   aka LIMIT
