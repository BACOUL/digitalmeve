from __future__ import annotations

import json
from base64 import b64encode
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, Optional, Union

_MEVE_VERSION = "1.0"
_PREVIEW_BYTES = 128  # Nombre d’octets pour l’aperçu


def _file_sha256(path: Path) -> str:
    """Calcule le hash SHA-256 hexadécimal du fichier."""
    h = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _preview_b64(path: Path, limit: int = _PREVIEW_BYTES) -> str:
    """Retourne un aperçu base64 des premiers octets du fichier."""
    try:
        with path.open("rb") as f:
            head = f.read(limit)
        return b64encode(head).decode("ascii")
    except Exception:
        # L’aperçu est optionnel ; si erreur, on renvoie vide
        return ""


def generate_meve(
    file_path: Union[str, Path],
    outdir: Optional[Union[str, Path]] = None,
    issuer: str = "Personal",
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Génère une preuve MEVE minimale pour un fichier donné.

    Parameters
    ----------
    file_path : str | Path
        Fichier à certifier.
    outdir : str | Path | None, optional
        Répertoire pour écrire le fichier `.meve.json`.
    issuer : str, default "Personal"
        Identité de l’émetteur.
    metadata : dict | None
        Métadonnées additionnelles.

    Returns
    -------
    dict
        Preuve MEVE complète.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"file not found: {path}")

    # Calculs
    content_hash = _file_sha256(path)
    preview = _preview_b64(path)
    ts = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    # Structure de preuve
    proof: Dict[str, Any] = {
        "meve_version": _MEVE_VERSION,
        "issuer": issuer,
        "issued_at": ts,
        "timestamp": ts,
        "metadata": metadata or {},
        "subject": {
            "filename": path.name,
            "size": path.stat().st_size,
            "hash_sha256": content_hash,
        },
        "hash": content_hash,
        "preview_b64": preview,
        # Champs avancés (vides par défaut pour compatibilité schéma)
        "verified_domain": "",
        "key_id": "",
        "signature": "",
        "doc_ref": "",
    }

    # Écriture optionnelle sur disque
    if outdir is not None:
        out = Path(outdir)
        out.mkdir(parents=True, exist_ok=True)
        outfile = out / f"{path.name}.meve.json"
        with outfile.open("w", encoding="utf-8") as f:
            json.dump(proof, f, ensure_ascii=False, separators=(",", ":"))

    return proof
