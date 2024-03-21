# =============================================================================
#
# =============================================================================


from datetime import datetime
from typing import Any, Dict, List, Union

import ujson as json
from playhouse.apsw_ext import (
    SQL,
    APSWDatabase,
    AutoField,
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    IntegerField,
    Model,
    PrimaryKeyField,
    TextField,
)
from playhouse.fields import PickleField
from playhouse.hybrid import hybrid_method, hybrid_property
from playhouse.sqlite_ext import JSONField

from ..options import tripcode as hash

Database = APSWDatabase
RealField = FloatField
database = Database(None)


class BaseModel(Model):
    """
    JSON Object:

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

    id = AutoField(column_name="_rowid_", primary_key=True)
    # пробуем привязаться к системному полю

    _id = CharField(index=True, max_length=255, null=False, unique=False)
    # (string) – Document ID

    _rev = CharField(index=True, null=False, unique=True)
    # (string) – Revision MVCC token

    _deleted = BooleanField(default=False)
    # – Deletion flag. Available if document was removed

    # _attachments = BlobField(null=True)
    # (object) – Attachment’s stubs. Available if document has any attachments
    # сделать ссылку на таблицу IntegerField(att_id) -> _attachments(id, blob)
    # отдельная таблица с односторонним ключом (оттуда) по ид+ревизия
    # отдельная таблица id, Array[doc_id], hash_att(unique index), blob (zipped blob?)

    _data = PickleField(column_name="_data", index=False, null=True, unique=False)
    # добавленное поле
    # проверить с типом JSONField

    _timestamp = FloatField(index=True, null=False, unique=False)
    # добавленное поле

    # calculated cells #

    @hybrid_property
    def _conflicts(self) -> List[str]:
        # (array) – List of conflicted revisions. Available if requested with conflicts=true query parameter
        return ret

    @hybrid_property
    def _deleted_conflicts(self) -> List[str]:
        # (array) – List of deleted conflicted revisions. Available if requested with deleted_conflicts=true query parameter
        return ret

    @hybrid_property
    def _local_seq(self) -> str:
        # (string) – Document’s update sequence in current database. Available if requested with local_seq=true query parameter
        # не будет реализовано, потому что не понятно что делает
        return ret

    @hybrid_property
    def _revs_info(self) -> List[str | object]:
        # (array) – List of objects with information about local revisions and their status. Available if requested with open_revs query parameter
        return ret

    @hybrid_property
    def _revisions(self) -> List[str] | object:
        # (object) – List of local revision tokens without. Available if requested with revs=true query parameter
        return ret

    class Meta:
        database = database
        only_save_dirty = True

        hash = hash

        pass

    def save(self, *args, **kwargs):
        # this is a create operation, set the date_created field
        # if self._get_pk_value() is None:
        #    self.date_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #        print(
        #            self,
        #            self.id,
        #            self.get_id(),
        #            not self.id,
        #            self.create_time,
        # [e for e in self.select().dicts()],
        #        )

        self._timestamp = datetime.now()

        return super().save(*args, **kwargs)

    pass


__all__ = ("Database", "Model", "BaseModel")
