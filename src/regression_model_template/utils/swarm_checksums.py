"""Deterministic canonical JSON SHA-256 checksum utilities."""

import hashlib
import json
from typing import Any


def sha256_canonical_json(payload: dict[str, Any]) -> str:
    """Return a deterministic lowercase hex SHA-256 digest for a JSON-serializable dict."""
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
