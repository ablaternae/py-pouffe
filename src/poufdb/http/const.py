# =============================================================================
#
# =============================================================================

DB_NOT_FOUND = {"error": "not_found", "reason": "Database does not exist."}

DB_EXISTS = {
    "error": "file_exists",
    "reason": "The database could not be created, the file already exists.",
}

SUCCESS = {"ok": True}

SESSION = {"ok": True, "userCtx": {"name": None, "roles": ["_admin"]}}

TOO_MANY_UUIDS = {"error": "bad_request", "reason": "count parameter too large"}
