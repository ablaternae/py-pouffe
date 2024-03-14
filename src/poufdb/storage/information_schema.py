# =============================================================================
#
# =============================================================================

from playhouse.dataset import DataSet

from .. import defaults
from . import DATA_DIR

information_schema = DataSet("sqlite:///:memory:")
server = information_schema["default"].update(defaults)

server.update(defaults)
information_schema.freeze(server.all(), format="csv", filename="information_schema.csv")
