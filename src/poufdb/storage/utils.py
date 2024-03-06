# =============================================================================
#
# =============================================================================

# from hashlib import sha256

import sortedcontainers

Containers = sortedcontainers
Collection = sortedcontainers.SortedDict

# hash = lambda x: sha256(str(x).encode("utf-8")).hexdigest()

MAX_UUIDS = 1000
UUID_MAX_COUNT = 1000  #   aka LIMIT
