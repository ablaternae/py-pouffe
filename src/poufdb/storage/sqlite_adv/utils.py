# =============================================================================
#
# =============================================================================

import os
from types import ModuleType
from typing import Any, Callable, Iterable, List, Mapping

from ..options import DATABASE_DIRECTORY, DATABASE_EXTENSION, ENGINES, STORAGE


def get_db_list(data_dir: str = None) -> Iterable:
    if not data_dir or not os.path.isdir(data_dir):
        data_dir = DATABASE_DIRECTORY

    ret = (
        f
        for f in os.scandir(data_dir)
        if f.is_file(follow_symlinks=False) and str(f).endswith(DATABASE_EXTENSION)
    )
    print(ret)
