from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Union


# ---------------------------
# Public API (imported by tests)
# ---------------------------

def verify_identity(path: Union[str, Path]) -> bool:
    """
    Very small sanity check used by tests.
    Returns True for an existing file path, False otherwise.
    """
    if not path:
        return False
    p = Path(path)
    if not p.exists() or p.is_dir():
        return False
    return True


def _as_dict(proof: Any) -> Optional[Dict[str, Any]]:
    """Accept either a dict or a JSON string and return a dict, else None."""
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
) -> bool:
    """
    Validate a .meve proof structure.

    Required top-level keys:
      - meve_version (str)
      - issuer (str)
      - timestamp (str)
      - subject (dict with filename/size/hash_sha256)
      - hash (str)  # must equal subject.hash_sha256

    Returns:
        True if valid, False otherwise.
    """
    obj = _as_dict(proof)
    if not isinstance(obj, dict):
        return False

    required: Iterable[str] = (
        "meve_version",
        "issuer",
        "timestamp",
        "subject",
        "hash",
    )
    if any(k not in obj for k in required):
        return False

    subject = obj.get("subject")
    if not isinstance(subject, dict):
        return False

    subj_required: Iterable[str] = ("filename", "size", "hash_sha256")
    if any(k not in subject for k in subj_required):
        return False

    if expected_issuer is not None and obj.get("issuer") != expected_issuer:
        return False

    if obj.get("hash") != subject.get("hash_sha256"):
        return False

    return True
