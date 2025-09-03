# src/digitalmeve/verifier.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple, Union

__all__ = ["verify_proof"]


def _as_dict(proof: Any) -> Optional[Dict[str, Any]]:
    """
    Convertit une 'preuve' vers un dict Python.

    Accepte :
      - dict            -> renvoyé tel quel
      - str/Path        -> si fichier JSON existant, on le lit ;
                           sinon on tente json.loads sur la chaîne
      - bytes/bytearray -> décodé en UTF-8 puis json.loads

    Retourne le dict ou None si l'entrée n'est pas exploitable.
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


def _missing_keys(obj: Dict[str, Any], keys: Iterable[str]) -> list[str]:
    """Retourne la liste des clés manquantes dans obj."""
    return [k for k in keys if k not in obj]


def verify_proof(
    proof: Any,
    *,
    expected_issuer: Optional[str] = None,
) -> Tuple[bool, Dict[str, Any]]:
    """
    Valide la structure et la cohérence d'une preuve .meve.

    Paramètres
    ----------
    proof : Any
        La preuve (dict, chemin de fichier JSON, chaîne JSON, ou bytes).
    expected_issuer : Optional[str]
        Si fourni, la preuve doit avoir le même 'issuer'.

    Retour
    ------
    (ok, info) : Tuple[bool, Dict[str, Any]]
        - ok=True  -> info contient la preuve normalisée (dict)
        - ok=False -> info={"error": "<raison lisible>"}
    """
    obj = _as_dict(proof)
    if not isinstance(obj, dict):
        return False, {"error": "Invalid proof"}

    # Champs de premier niveau requis
    required_top: Iterable[str] = (
        "meve_version",
        "issuer",
        "timestamp",
        "subject",
        "hash",
    )
    missing_top = _missing_keys(obj, required_top)
    if missing_top:
        return False, {"error": "Missing required keys"}

    # Sujet attendu : { filename, size, hash_sha256 }
    subject = obj.get("subject")
    if not isinstance(subject, dict):
        return False, {"error": "Missing required keys"}

    required_subject: Iterable[str] = ("filename", "size", "hash_sha256")
    if _missing_keys(subject, required_subject):
        return False, {"error": "Missing required keys"}

    # Vérification émetteur attendu
    if expected_issuer is not None and obj.get("issuer") != expected_issuer:
        return False, {"error": "Issuer mismatch"}

    # Cohérence des empreintes : hash global == subject.hash_sha256
    if obj.get("hash") != subject.get("hash_sha256"):
        return False, {"error": "Hash mismatch"}

    # Ici on pourrait brancher une vraie validation de schéma JSON.
    # On garde un try/except pour rester compatible si on l'active plus tard.
    try:
        # schema_validate(obj)  # placeholder futur
        pass
    except Exception as exc:  # pragma: no cover
        return False, {"error": f"Schema validation failed: {exc}"}

    return True, obj
