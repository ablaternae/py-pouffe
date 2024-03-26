# =============================================================================
#
# =============================================================================


from http import HTTPStatus as status

DB_NOT_FOUND = {"error": "not_found", "reason": "Database does not exist."}

DB_EXISTS = {
    "error": "file_exists",
    "reason": "The database could not be created, the file already exists.",
}

SUCCESS = {"ok": True}

SESSION = {"ok": True, "userCtx": {"name": None, "roles": ["_admin"]}}

TOO_MANY_UUIDS = {"error": "bad_request", "reason": "count parameter too large"}

HEADER_JSON = {"Content-Type": "application/json"}

CONTENT_HTML = "text/html; charset=utf-8"
CONTENT_JSON = "application/json; charset=utf-8"

MINIMUM_DEFLATE_SIZE = 2
MINIMUM_DEFLATE_SIZE = 2048
GZIP_COMPRESS_LEVEL = 6
