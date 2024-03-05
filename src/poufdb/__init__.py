# SPDX-FileCopyrightText: 2024-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT

from hashlib import sha256

from . import options
from .__about__ import *
from .http import *
from .http import server

hash = lambda x: sha256(str(x).encode("utf-8")).hexdigest()

# sha((str(os.lstat(os.path.dirname(__file__)))).encode("utf-8")).hexdigest()
