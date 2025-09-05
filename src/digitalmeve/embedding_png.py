from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

from PIL import Image, PngImagePlugin


_MEVE_KEY = "MEVE_Proof"


def _minify_json(obj: Dict[str, Any]) -> str:
    """Retourne un JSON minifié (UTF-8, sans espaces inutiles)."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def embed_proof_png(
    in_path: Path | str,
    proof: Dict[str, Any],
    out_path: Optional[Path | str] = None,
) -> Path:
    """
    Embarque la preuve MEVE dans un PNG via un chunk iTXt (clé 'MEVE_Proof').

    - in_path : image PNG source
    - proof   : dict MEVE
    - out_path: destination (par défaut <in_path>.meve.png)

    Retourne le chemin du PNG écrit.
    """
    src = Path(in_path)
    if out_path is None:
        dst = src.with_suffix(src.suffix)
        dst = dst.with_name(src.stem + ".meve" + src.suffix)  # foo.png -> foo.meve.png
    else:
        dst = Path(out_path)

    if not src.exists():
        raise FileNotFoundError(f"PNG introuvable: {src}")

    payload = _minify_json(proof)

    with Image.open(str(src)) as im:
        # On reconstruit les metas pour garantir l’écriture du iTXt
        pnginfo = PngImagePlugin.PngInfo()
        # On ajoute nos métadonnées existantes si présentes
        for k, v in im.info.items():
            # Pillow attend des str pour iTXt; on ignore les objets non sérialisables
            if isinstance(v, (str, bytes)):
                try:
                    pnginfo.add_text(k, v if isinstance(v, str) else v.decode("utf-8", "ignore"))
                except Exception:
                    pass

        # Ajoute la preuve MEVE (iTXt)
        pnginfo.add_text(_MEVE_KEY, payload)

        # Sauvegarde : Pillow réécrit un PNG propre avec nos iTXt
        im.save(str(dst), pnginfo=pnginfo)

    return dst


def extract_proof_png(in_path: Path | str) -> Dict[str, Any]:
    """
    Extrait la preuve MEVE (JSON) depuis un PNG (chunk iTXt 'MEVE_Proof').
    Retourne un dict Python.
    Lève KeyError si la clé n’est pas présente ou JSONDecodeError si invalide.
    """
    src = Path(in_path)
    if not src.exists():
        raise FileNotFoundError(f"PNG introuvable: {src}")

    with Image.open(str(src)) as im:
        raw = im.info.get(_MEVE_KEY, None)

    if raw is None:
        raise KeyError("Aucune preuve MEVE trouvée dans le PNG (iTXt 'MEVE_Proof').")

    if isinstance(raw, bytes):
        raw = raw.decode("utf-8", errors="strict")

    return json.loads(str(raw))
