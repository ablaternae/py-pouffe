# =============================================================================
#
# =============================================================================

import os
from hashlib import sha256 as sha
from os import linesep as CRLF
from os.path import basename, dirname, realpath

hash = lambda x: sha(str(x).encode("utf-8")).hexdigest()

from environs import Env

env = Env()
env.read_env(override=True)


WORK_DIR = os.getcwd()

APP_DEBUG = env.bool("APP_DEBUG", False)
APP_ENV = env.str("APP_ENV", "dev")

HTTP_HOST = env.str("HTTP_HOST", "127.0.0.1")
HTTP_HOST = env.str("HTTP_HOST", "0.0.0.0")
HTTP_PORT = env.int("HTTP_PORT", 5984)
HTTP_URL = env.str("HTTP_URL", "")

SOURCE_URL = ""
DATA_DIR = realpath(env.str("DATA_DIR", os.path.join(WORK_DIR, "_data")))

ADMIN_PANEL = env.bool("ADMIN_PANEL", False)
ADMIN_URL = ""
ADMIN_PORT = "8084"
