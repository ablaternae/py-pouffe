# =============================================================================
#
# =============================================================================

from hashlib import sha256

import sortedcontainers

Containers = sortedcontainers
Collection = sortedcontainers.SortedDict

hash = lambda x: sha256(str(x).encode("utf-8")).hexdigest()
