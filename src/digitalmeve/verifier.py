from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple

__all__ = ["verify_identity", "verify_proof", "verify_meve"]


def verify_identity(identity: Any) -> bool:
    """Validation minimale d'identité utilisée par les tests."""
    if identity is None:
        return False
    return str(identity).strip() != ""


def _as_dict(proof: Any) -> Optional[Dict[str, Any]]:
    """Convertit une 'preuve' en dict Python (dict, str JSON, chemin de fichier, bytes)."""
    if isinstance(proof, dict):
        return proof

    if isinstance(proof, (str, Path)):
        p = Path(proof)
        if p.exists() and p.is_file():
            try:
                text = p.read_text(encoding="utf-8")
                return json.loads(text)
            except Exception:
                return None
        try:
            return json.loads(str(proof))
        except Exception:
            return None

    if isinstance(proof, (bytes, bytearray)):
        try:
            return json.loads(proof.decode("utf-8"))
        except Exception:
            return None

    return None


def _missing_keys(obj: Dict[str, Any], keys: Iterable[str]) -> list[str]:
    return [k for k in keys if k not in obj]


def verify_proof(
    proof: Any,
    *,
    expected_issuer: Optional[str] = None,
) -> Tuple[bool, Dict[str, Any]]:
    """Valide la structure et la cohérence d'une preuve .meve."""
    obj = _as_dict(proof)
    if not isinstance(obj, dict):
        return False, {"error": "Invalid proof"}

    required_top: Iterable[str] = ("meve_version", "issuer", "timestamp", "subject", "hash")
    if _missing_keys(obj, required_top):
        return False, {"error": "Missing required keys"}

    subject = obj.get("subject")
    if not isinstance(subject, dict):
        return False, {"error": "Missing required keys"}

    if _missing_keys(subject, ("filename", "size", "hash_sha256")):
        return False, {"error": "Missing required keys"}

    if expected_issuer is not None and obj.get("issuer") != expected_issuer:
        return False, {"error": "Issuer mismatch"}

    if obj.get("hash") != subject.get("hash_sha256"):
        return False, {"error": "Hash mismatch"}

    # Placeholder pour une validation de schéma future
    try:
        pass
    except Exception as exc:  # pragma: no cover
        return False, {"error": f"Schema validation failed: {exc}"}

    return True, obj


# ✅ Alias demandé par les tests
verify_meve = verify_proof
