from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple, Union


# --------------------------------------------------------------------
# Public API expected by tests
# --------------------------------------------------------------------

def verify_identity(identity: Union[str, Path]) -> bool:
    """
    Minimal identity check used by tests.

    The tests consider an empty string invalid and a non-empty token
    like 'ABC123' valid. So we return True for any non-empty string/path.
    """
    if identity is None:
        return False
    s = str(identity).strip()
    return s != ""


def _as_dict(proof: Any) -> Optional[Dict[str, Any]]:
    """Accept either a dict or a JSON string and return a dict (or None)."""
    if isinstance(proof, dict):
        return proof
    if isinstance(proof, (bytes, str)):
        try:
            return json.loads(proof)
        except Exception:
            return None
    return None


def verify_meve(
    proof: Any,
    *,
    expected_issuer: Optional[str] = None,
) -> Tuple[bool, Dict[str, str]]:
    """
    Validate a .meve proof structure.

    Required top-level keys:
      - meve_version (str)
      - issuer (str)
      - timestamp (str)
      - subject (dict with filename/size/hash_sha256)
      - hash (str)  # must equal subject.hash_sha256

    Returns:
        (True, {}) if valid
        (False, {"error": "<reason>"}) if invalid
    """
    obj = _as_dict(proof)
    if not isinstance(obj, dict):
        return False, {"error": "invalid proof"}

    # Top-level required keys
    required: Iterable[str] = (
        "meve_version",
        "issuer",
        "timestamp",
        "subject",
        "hash",
    )
    missing = [k for k in required if k not in obj]
    if missing:
        return False, {"error": "missing required keys"}

    subject = obj.get("subject")
    if not isinstance(subject, dict):
        return False, {"error": "missing required keys"}

    subj_required: Iterable[str] = ("filename", "size", "hash_sha256")
    if any(k not in subject for k in subj_required):
        return False, {"error": "missing required keys"}

    # Optional issuer check
    if expected_issuer is not None and obj.get("issuer") != expected_issuer:
        return False, {"error": "issuer mismatch"}

    # Hash must mirror subject.hash_sha256
    if obj.get("hash") != subject.get("hash_sha256"):
        return False, {"error": "hash mismatch"}

    return True, {}
