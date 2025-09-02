from __future__ import annotations

from base64 import b64encode
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Dict, Optional, Any, Union

import json

_MEVE_VERSION = "1.0"
_PREVIEW_BYTES = 128  # petite empreinte lisible pour debug/aperçu


def _file_sha256(path: Path) -> str:
    """Retourne le SHA-256 hexadécimal du fichier donné."""
    h = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _preview_b64(path: Path, limit: int = _PREVIEW_BYTES) -> str:
    """
    Retourne une prévisualisation base64 des premiers octets du fichier.
    Si erreur → chaîne vide (aperçu optionnel).
    """
    try:
        with path.open("rb") as f:
            head = f.read(limit)
        return b64encode(head).decode("ascii")
    except Exception:
        return ""


def generate_meve(
    file_path: Union[str, Path],
    outdir: Optional[Union[str, Path]] = None,
    issuer: str = "Personal",
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Génère une preuve MEVE minimale (dict) pour le fichier donné.

    Champs générés :
    - meve_version
    - issuer
    - issued_at (UTC ISO 8601, "Z")
    - metadata
    - subject: { filename, size, hash_sha256 }
    - hash (copie de subject.hash_sha256)
    - preview_b64 (facultatif, pour debug)
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"file not found: {path}")

    # calculs
    content_hash = _file_sha256(path)
    preview = _preview_b64(path)
    ts = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    proof: Dict[str, Any] = {
        "meve_version": _MEVE_VERSION,
        "issuer": issuer,
        "issued_at": ts,   # ✅ seule source de temps
        "metadata": metadata or {},
        "subject": {
            "filename": path.name,
            "size": path.stat().st_size,
            "hash_sha256": content_hash,
        },
        "hash": content_hash,
        "preview_b64": preview,
    }

    # écriture optionnelle du sidecar
    if outdir is not None:
        out = Path(outdir)
        out.mkdir(parents=True, exist_ok=True)
        outfile = out / f"{path.name}.meve.json"
        with outfile.open("w", encoding="utf-8") as f:
            json.dump(proof, f, ensure_ascii=False, separators=(",", ":"), indent=None)

    return proof
