from __future__ import annotations

from base64 import b64encode
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Dict, Optional, Any, Union


_MEVE_VERSION = "1.0"
_PREVIEW_BYTES = 128  # petite empreinte lisible pour debug/aperçu


def _file_sha256(path: Path) -> str:
    """Return the hexadecimal SHA-256 digest for the file at `path`."""
    h = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _preview_b64(path: Path, limit: int = _PREVIEW_BYTES) -> str:
    """
    Return a base64 preview of the first `limit` bytes of the file.

    Parameters
    ----------
    path : pathlib.Path
        Path to the file.
    limit : int, default 128
        Number of bytes to read for the preview.

    Returns
    -------
    str
        Base64-encoded string of the first bytes. Returns empty string
        if reading fails (preview is optional).
    """
    try:
        with path.open("rb") as f:
            head = f.read(limit)
        return b64encode(head).decode("ascii")
    except Exception:
        # l’aperçu est optionnel ; en cas de souci on renvoie une chaîne vide
        return ""


def generate_meve(
    file_path: Union[str, Path],
    outdir: Optional[Union[str, Path]] = None,
    issuer: str = "Personal",
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Generate a minimal MEVE proof (as dict) for the given file.

    What it does
    ------------
    - Reads the file, computes a SHA-256 hash and a base64 preview.
    - Builds a dict with keys required by the test suite:
        * meve_version, issuer, issued_at, metadata
        * subject: { filename, size, hash_sha256 }
        * hash (duplicate of subject.hash_sha256)
        * preview_b64 (base64 preview of first bytes)
    - Optionally writes a sidecar JSON `<filename>.meve.json` into `outdir`.

    Parameters
    ----------
    file_path : str | pathlib.Path
        Path to the input file.
    outdir : str | pathlib.Path | None, optional
        If provided, the proof is also written as JSON file in this directory.
    issuer : str, default "Personal"
        Issuer string to include in the proof.
    metadata : dict | None, optional
        Optional metadata to embed in the proof.

    Returns
    -------
    dict
        The MEVE proof structure. Even if written to disk, the dict
        is always returned.

    Notes
    -----
    - `hash` and `subject.hash_sha256` always match.
    - `issued_at` is ISO 8601 in UTC (with "Z").
    - The preview is informational only, it is not part of verification.
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
        "issued_at": ts,           # champ requis par le schéma + tests
        "timestamp": ts,           # conservé pour compatibilité future
        "metadata": metadata or {},
        "subject": {
            "filename": path.name,
            "size": path.stat().st_size,
            "hash_sha256": content_hash,
        },
        # duplication utile et demandée par les tests
        "hash": content_hash,
        "preview_b64": preview,
    }

    # écriture optionnelle du sidecar
    if outdir is not None:
        out = Path(outdir)
        out.mkdir(parents=True, exist_ok=True)
        outfile = out / f"{path.name}.meve.json"

        import json
        with outfile.open("w", encoding="utf-8") as f:
            json.dump(proof, f, ensure_ascii=False, separators=(",", ":"), indent=None)

    return proof
