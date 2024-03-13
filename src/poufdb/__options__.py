# =============================================================================
#
# =============================================================================


import os

# from hashlib import sha1 as sha #   sha1 faster sha256 apprx 1/3
from hashlib import sha256 as sha

from os.path import basename, dirname, realpath

from .__meta__ import Meta

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

HTTP_HOST = env.str("HTTP_HOST", "127.0.0.1")
HTTP_HOST = env.str("HTTP_HOST", "0.0.0.0")
HTTP_PORT = env.int("HTTP_PORT", 5984)
HTTP_DRIVER_FLASK = "flask"
HTTP_DRIVER_FLASK_ASYNC = "flask_async"
HTTP_DRIVER_FASTAPI = "fastapi"
HTTP_DRIVER = HTTP_DRIVER_FLASK_ASYNC

# HTTP_URL = env.str("HTTP_URL", "")

HTTP_ADMIN_PANEL = env.bool("ADMIN_PANEL", False)
HTTP_ADMIN_PORT = "8084"
HTTP_ADMIN_URL = ""


STORAGE_DATA_DIR = realpath(env.str("DATA_DIR", os.path.join(WORK_DIR, "_data")))
STORAGE_DRIVER_SQLITE = "sqlite"
STORAGE_DRIVER_SQLITE_ASYNC = "sqlite_async"

STORAGE_DRIVER = STORAGE_DRIVER_SQLITE_ASYNC


hash = lambda x: sha(str(x).encode("utf-8")).hexdigest()
hash10 = triphash = lambda x: hash(x)[:10]
if not "tripcode" in locals():
    tripcode = hash10


class Options(Meta):
    pass


# class Options(Meta):
#    __singleton__: bool = False
#
#    def __init__(self, *args, **kwargs):
#        print('SINGLETON', type(self), type(self).__singleton__)
#
#        if not type(self).__singleton__:
#            super().__init__(*args, **kwargs)
#            type(self).__singleton__ = True
