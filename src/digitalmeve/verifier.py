from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple, Union


def verify_identity(identity: Union[str, Path]) -> bool:
    """
    Minimal identity check used by tests.
    Empty string = invalid, any non-empty = valid.
    """
    if identity is None:
        return False
    return str(identity).strip() != ""


def _as_dict(proof: Any) -> Optional[Dict[str, Any]]:
    """Accept dict or JSON string and return a dict, else None."""
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
    Returns (True, {}) if valid, (False, {"error": "<reason>"}) otherwise.
    """
    obj = _as_dict(proof)
    if not isinstance(obj, dict):
        return False, {"error": "Invalid proof"}

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
        return False, {"error": "Missing required keys"}

    subject = obj.get("subject")
    if not isinstance(subject, dict):
        return False, {"error": "Missing required keys"}

    subj_required: Iterable[str] = ("filename", "size", "hash_sha256")
    if any(k not in subject for k in subj_required):
        return False, {"error": "Missing required keys"}

    # Optional issuer check
    if expected_issuer is not None and obj.get("issuer") != expected_issuer:
        return False, {"error": "Issuer mismatch"}

    # Hash must equal subject.hash_sha256
    if obj.get("hash") != subject.get("hash_sha256"):
        return False, {"error": "Hash mismatch"}

    return True, {}
