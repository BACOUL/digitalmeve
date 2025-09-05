# src/digitalmeve/embedding_png.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

from PIL import Image, PngImagePlugin

# Clé texte dans les métadonnées PNG (chunk tEXt / iTXt)
MEVE_PNG_KEY = "meve_proof"


def _as_path(p: str | Path) -> Path:
    return p if isinstance(p, Path) else Path(p)


def embed_proof_png(
    in_path: str | Path, proof: Dict[str, Any], out_path: str | Path
) -> Path:
    """
    Écrit la preuve JSON minifiée dans un chunk texte du PNG sous la clé MEVE_PNG_KEY.
    Retourne Path(out_path).
    """
    src = _as_path(in_path)
    dst = _as_path(out_path)

    payload = json.dumps(proof, separators=(",", ":"))

    img = Image.open(src)
    img.load()  # s'assure que l'image est chargée avant ré-écriture

    # Conserver les métadonnées existantes + ajouter notre clé
    meta = PngImagePlugin.PngInfo()
    for k, v in (img.info or {}).items():
        if k == MEVE_PNG_KEY:
            continue
        if isinstance(v, bytes):
            try:
                v = v.decode("utf-8", "ignore")
            except Exception:
                v = str(v)
        meta.add_text(k, str(v))
    meta.add_text(MEVE_PNG_KEY, payload)

    img.save(dst, "PNG", pnginfo=meta)
    return dst


def extract_proof_png(path: str | Path) -> Optional[Dict[str, Any]]:
    """
    Lit la clé MEVE_PNG_KEY depuis les métadonnées PNG et retourne le dict, ou None si absent/illisible.
    """
    img = Image.open(_as_path(path))
    info = img.info or {}

    raw = (
        info.get(MEVE_PNG_KEY)
        or info.get("MeveProof")
        or info.get("MEVE_PROOF")
        or info.get("meve_proof")
    )
    if raw is None:
        return None

    if isinstance(raw, bytes):
        try:
            raw = raw.decode("utf-8")
        except Exception:
            return None

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None
