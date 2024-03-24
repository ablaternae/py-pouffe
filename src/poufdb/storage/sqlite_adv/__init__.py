# =============================================================================
#
# =============================================================================

from .base_model import BaseModel, Database, Model, database


class Document(BaseModel):
    pass


__all__ = ("BaseModel", "Database", "Document", "Model", "database")
