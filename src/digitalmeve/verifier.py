from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple, Union


# ---------------------------
# Public API (imported by tests)
# ---------------------------

def verify_identity(path: Union[str, Path]) -> Tuple[bool, Dict[str, Any]]:
    """
    Trivial identity check used by smoke tests.

    Returns:
        (ok, info)
        - ok=False and {"error": "invalid file"} if path is empty, a directory,
          or does not exist.
        - ok=True otherwise.
    """
    if not path:
        return False, {"error": "invalid file"}
    p = Path(path)
    if not p.exists() or p.is_dir():
        return False, {"error": "invalid file"}
    return True, {"path": str(p)}


def verify_meve(
    proof: Any,
    *,
    expected_issuer: Optional[str] = None,
) -> Tuple[bool, Dict[str, Any]]:
    """
    Validate a .meve proof structure (dict).

    Required top-level keys:
      - meve_version (str)
      - issuer (str)
      - timestamp (str)
      - subject (dict with filename/size/hash_sha256)
      - hash (str)  # must equal subject.hash_sha256

    Args:
        proof: The candidate proof (should be a dict).
        expected_issuer: If provided, must match proof["issuer"].

    Returns:
        (ok, info)
        - On failure, ok=False and info={"error": "..."} where the message is one
          of:
            * "Missing required keys"
            * "issuer mismatch"
            * "hash mismatch"
            * "invalid proof"
        - On success, ok=True and a small normalized payload is returned.
    """
    # Must be a mapping
    if not isinstance(proof, dict):
        return False, {"error": "invalid proof"}

    required: Iterable[str] = (
        "meve_version",
        "issuer",
        "timestamp",
        "subject",
        "hash",
    )
    if any(k not in proof for k in required):
        # NOTE: Capital M is important for the tests
        return False, {"error": "Missing required keys"}

    subject = proof.get("subject")
    if not isinstance(subject, dict):
        return False, {"error": "invalid proof"}

    subj_required: Iterable[str] = ("filename", "size", "hash_sha256")
    if any(k not in subject for k in subj_required):
        return False, {"error": "Missing required keys"}

    # issuer check (exact string compare)
    if expected_issuer is not None and proof.get("issuer") != expected_issuer:
        return False, {"error": "issuer mismatch"}

    # hash check: top-level hash must mirror subject.hash_sha256
    if proof.get("hash") != subject.get("hash_sha256"):
        return False, {"error": "hash mismatch"}

    # All good — return a compact normalized view
    return True, {
        "issuer": proof["issuer"],
        "meve_version": proof["meve_version"],
        "filename": subject["filename"],
        "size": subject["size"],
        "hash": proof["hash"],
        "timestamp": proof["timestamp"],
    }
