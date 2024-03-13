# =============================================================================
#
# =============================================================================

from playhouse.apsw_ext import *

Database = APSWDatabase


class BaseModel(Model):
    class Meta:
        database = database


from ..meta import Meta

print(Meta().from_mapping(locals()))

__all__ = ("Database", "Model", "BaseModel")
