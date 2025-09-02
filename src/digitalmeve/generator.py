from __future__ import annotations

from base64 import b64encode
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Dict, Optional, Any, Union


_MEVE_VERSION = "1.0"
_PREVIEW_BYTES = 128  # small readable preview for debug


def _file_sha256(path: Path) -> str:
    h = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _preview_b64(path: Path, limit: int = _PREVIEW_BYTES) -> str:
    try:
        with path.open("rb") as f:
            head = f.read(limit)
        return b64encode(head).decode("ascii")
    except Exception:
        return ""  # preview is optional


def _iso8601_z_now() -> str:
    # ISO-8601 UTC with trailing Z and **no microseconds**
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def generate_meve(
    file_path: Union[str, Path],
    outdir: Optional[Union[str, Path]] = None,
    issuer: str = "Personal",
    metadata: Optional[Dict[str, Any]] = None,
    also_json: bool = False,
) -> Dict[str, Any]:
    """
    Generate a minimal MEVE proof (as dict) for the given file.

    Keys produced:
      - meve_version, issuer, issued_at (ISO-8601 Z, no micros), metadata
      - subject: { filename, size, hash_sha256 }
      - hash (duplicate of subject.hash_sha256)
      - preview_b64 (optional)
      - timestamp (kept for backward-compat, same as issued_at)
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"file not found: {path}")

    content_hash = _file_sha256(path)
    preview = _preview_b64(path)
    issued_at = _iso8601_z_now()

    proof: Dict[str, Any] = {
        "meve_version": _MEVE_VERSION,
        "issuer": issuer,
        "issued_at": issued_at,   # <-- requis par les tests
        "timestamp": issued_at,   # compat
        "metadata": metadata or {},
        "subject": {
            "filename": path.name,
            "size": path.stat().st_size,
            "hash_sha256": content_hash,
        },
        "hash": content_hash,
        "preview_b64": preview,
    }

    # Écriture éventuelle d'un sidecar JSON
    if outdir is not None:
        out = Path(outdir)
        out.mkdir(parents=True, exist_ok=True)
        outfile = out / f"{path.name}.meve.json"
        import json
        with outfile.open("w", encoding="utf-8") as f:
            json.dump(proof, f, ensure_ascii=False, separators=(",", ":"), indent=None)

    if also_json and outdir is None:
        outfile = path.with_name(f"{path.name}.meve.json")
        import json
        with outfile.open("w", encoding="utf-8") as f:
            json.dump(proof, f, ensure_ascii=False, separators=(",", ":"), indent=None)

    return proof
