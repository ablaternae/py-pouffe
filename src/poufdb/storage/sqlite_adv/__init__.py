# =============================================================================
#
# =============================================================================


from .base_model import BaseModel, Database, Model, database
from .utils import *


class Document(BaseModel):
    pass


__all__ = ("BaseModel", "Database", "Document", "Model", "database")
