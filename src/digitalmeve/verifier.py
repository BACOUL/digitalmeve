from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple, Union


def verify_identity(identity: Union[str, Path]) -> bool:
    """
    Vérification minimale de l'identité utilisée par les tests.
    Chaîne vide -> False ; toute chaîne non vide -> True.
    """
    if identity is None:
        return False
    return str(identity).strip() != ""


def _as_dict(proof: Any) -> Optional[Dict[str, Any]]:
    """
    Accepte :
      - un dict (retourné tel quel)
      - une chaîne JSON
      - un chemin de fichier (Path ou str) pointant vers un JSON
    Retourne un dict ou None si l'entrée n'est pas exploitable.
    """
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


def verify_meve(
    proof: Any,
    *,
    expected_issuer: Optional[str] = None,
) -> Tuple[bool, Dict[str, Any]]:
    """
    Valide la structure d'une preuve .meve.

    Retourne :
      - (True, <dict de la preuve>) si valide
      - (False, {"error": "<raison>"}) sinon
    """
    obj = _as_dict(proof)
    if not isinstance(obj, dict):
        return False, {"error": "Invalid proof"}

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

    if expected_issuer is not None and obj.get("issuer") != expected_issuer:
        return False, {"error": "Issuer mismatch"}

    if obj.get("hash") != subject.get("hash_sha256"):
        return False, {"error": "Hash mismatch"}

    # Exemple : validation de schéma (si ajoutée plus tard)
    try:
        # schema_validate(obj)   # <- placeholder futur
        pass
    except Exception as e:
        msg = f"Schema validation failed: {e}"
        return False, {"error": msg}

    return True, obj
