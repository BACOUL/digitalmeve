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
    # dict direct
    if isinstance(proof, dict):
        return proof

    # chemin de fichier ?
    if isinstance(proof, (str, Path)):
        p = Path(proof)
        if p.exists() and p.is_file():
            try:
                text = p.read_text(encoding="utf-8")
                return json.loads(text)
            except Exception:
                return None
        # sinon tenter de parser comme JSON inline
        try:
            return json.loads(str(proof))
        except Exception:
            return None

    # bytes -> JSON
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

    # Clés obligatoires au niveau racine
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

    # Vérification optionnelle de l'émetteur
    if expected_issuer is not None and obj.get("issuer") != expected_issuer:
        return False, {"error": "Issuer mismatch"}

    # Cohérence du hash
    if obj.get("hash") != subject.get("hash_sha256"):
        return False, {"error": "Hash mismatch"}

    # ✅ Succès : renvoyer le dict complet (les tests l'utilisent)
    return True, obj
