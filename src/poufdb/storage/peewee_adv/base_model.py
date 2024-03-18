# =============================================================================
#
# =============================================================================

from playhouse.apsw_ext import *
from playhouse.hybrid import hybrid_method, hybrid_property
from playhouse.sqlite_ext import JSONField

Database = APSWDatabase
RealField = FloatField


class BaseModel(Model):
    """
    Response JSON Object:

    _id (string) – Document ID
    _rev (string) – Revision MVCC token
    _deleted (boolean) – Deletion flag. Available if document was removed
    _attachments (object) – Attachment’s stubs. Available if document has any attachments
    _conflicts (array) – List of conflicted revisions. Available if requested with conflicts=true query parameter
    _deleted_conflicts (array) – List of deleted conflicted revisions. Available if requested with deleted_conflicts=true query parameter
    _local_seq (string) – Document’s update sequence in current database. Available if requested with local_seq=true query parameter
    _revs_info (array) – List of objects with information about local revisions and their status. Available if requested with open_revs query parameter
    _revisions (object) – List of local revision tokens without. Available if requested with revs=true query parameter
    """

    # _rowid_ = AutoField()

    _id = CharField()
    # (string) – Document ID
    _rev = CharField()
    # (string) – Revision MVCC token
    _deleted = BooleanField(default=False)
    # – Deletion flag. Available if document was removed
    _attachments = BlobField()
    # сделать ссылку на файл? (object) – Attachment’s stubs. Available if document has any attachments

    _conflicts = JSONField()  #   вычисляемое
    # (array) – List of conflicted revisions. Available if requested with conflicts=true query parameter

    _deleted_conflicts = JSONField()  #   вычисляемое
    # (array) – List of deleted conflicted revisions. Available if requested with deleted_conflicts=true query parameter

    _local_seq = CharField()  # не будет реализовано
    # (string) – Document’s update sequence in current database. Available if requested with local_seq=true query parameter

    _revs_info = JSONField()  #   вычисляемое
    # (array) – List of objects with information about local revisions and their status. Available if requested with open_revs query parameter

    _revisions = JSONField()  #   вычисляемое
    # (object) – List of local revision tokens without. Available if requested with revs=true query parameter

    class Meta:
        # database = database
        ...

    pass


__all__ = ("Database", "Model", "BaseModel")
