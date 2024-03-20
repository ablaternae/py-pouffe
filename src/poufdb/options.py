# =============================================================================
#
# =============================================================================


import os

# from hashlib import sha256 as sha
# sha1 is faster than sha256 apprx 1/3 and just shorter
from hashlib import sha1 as sha

try:
    from tripcode import tripcode
except:
    pass


from environs import Env

env = Env()
env.read_env(override=True)


WORK_DIR = os.getcwd()
CRLF = os.linesep


APP_ENV = env.str("APP_ENV", "dev")
APP_DEBUG = env.bool("APP_DEBUG", False)

HTTP_HOST = env.str("HTTP_HOST", "0.0.0.0")
HTTP_HOST = env.str("HTTP_HOST", "127.0.59.84")
HTTP_PORT = env.int("HTTP_PORT", 5984)
HTTP_SERVER_FLASK = "flask"
HTTP_SERVER_FLASK_ASYNC = "flask_async"
HTTP_SERVER_FASTAPI = "fastapi"

HTTP_SERVER_DEFAULT = env.str("HTTP_SERVER", HTTP_SERVER_FLASK_ASYNC)

# HTTP_URL = env.str("HTTP_URL", "")

HTTP_ADMIN_PANEL = env.bool("ADMIN_PANEL", False)
HTTP_ADMIN_PORT = "8084"
HTTP_ADMIN_URL = ""


STORAGE_DATA_DIR = os.path.realpath(
    env.str("DATA_DIR", os.path.join(WORK_DIR, "_data"))
)
STORAGE_ENGINE_SQLITE = "sqlite"
STORAGE_ENGINE_SQLITE_ASYNC = "sqlite_async"
STORAGE_ENGINE_SQLITE_ADVANCED = "sqlite_adv"

STORAGE_ENGINE_DEFAULT = env.str(
    "STORAGE_ENGINE", STORAGE_ENGINE_SQLITE_ADVANCED
)


hash = lambda x: sha(str(x).encode("utf-8")).hexdigest()
hash10 = triphash = lambda x: hash(x)[:10]
if not ("tripcode" in globals() or "tripcode" in locals()):
    tripcode = hash10
