# =============================================================================
#
# =============================================================================

from .base_model import BaseModel, Database
from .database import Database


def db(dbname: str) -> dict:
    #

    def create():
        return 111

    pass


__all__ = ("Database", "Model", "BaseModel")
