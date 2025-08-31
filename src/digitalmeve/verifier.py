"""
Verifier module for DigitalMeve.

Provides `verify_meve` and `verify_identity` functions to check the validity
and authenticity of a `.meve` proof dictionary or JSON sidecar file.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, Tuple, Union


def verify_identity(value: str) -> bool:
    """
    Very simple identity check used in tests.

    Returns True if the provided string is non-empty and alphanumeric.
    """
    return isinstance(value, str) and value.isalnum()


def verify_meve(
    proof: Union[Dict[str, Any], str, Path],
    expected_issuer: str | None = None,
) -> Tuple[bool, Dict[str, Any]]:
    """
    Verify a `.meve` proof.

    Args:
        proof: A dictionary already loaded, or a path/str to a `.json` file.
        expected_issuer: Optional string; if provided, issuer must match.

    Returns:
        (ok, info) tuple:
          - ok: bool, True if verification passes
          - info: dict with either the normalized proof or an {"error": "..."}.
    """
    # Load from file if string or Path
    if isinstance(proof, (str, Path)):
        try:
            data = json.loads(Path(proof).read_text(encoding="utf-8"))
        except Exception as e:
            return False, {"error": f"invalid json: {e}"}
    elif isinstance(proof, dict):
        data = proof
    else:
        return False, {"error": "invalid proof type"}

    required_keys = {"meve_version", "issuer", "timestamp", "metadata", "subject"}
    if not required_keys.issubset(data.keys()):
        return False, {"error": "missing required keys"}

    if expected_issuer and data.get("issuer") != expected_issuer:
        return False, {"error": "issuer mismatch"}

    return True, data
