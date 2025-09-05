from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

from PIL import Image, PngImagePlugin

# Clé de métadonnée où l’on stocke la preuve
_MEVE_KEY = "meve_proof"


def _minify(obj: Dict[str, Any]) -> str:
    """JSON compact (utf-8, sans espaces)."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def embed_proof_png(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Embarque la preuve MEVE dans un PNG via un chunk iTXt/tEXt (_MEVE_KEY).

    - in_path : PNG source
    - proof   : dict MEVE (sera minifié en JSON)
    - out_path: destination ; si None, écrit à côté en suffixant '.meve.png'

    Retourne le chemin du fichier de sortie.
    """
    src = Path(in_path)
    if out_path is None:
        out = src.with_name(src.stem + ".meve.png")
    else:
        out = Path(out_path)

    img = Image.open(src)
    pnginfo = PngImagePlugin.PngInfo()

    # Conserver les éventuelles clés texte existantes
    # (selon Pillow, les textes existants sont dans img.info.get('parameters'))
    # On recopie simplement ce qui est présent dans img.text si disponible
    try:
        if hasattr(img, "text") and isinstance(img.text, dict):
            for k, v in img.text.items():
                if isinstance(k, str) and isinstance(v, str):
                    pnginfo.add_text(k, v)
    except Exception:
        pass  # best-effort

    # Ajoute la preuve MEVE minifiée
    pnginfo.add_text(_MEVE_KEY, _minify(proof))

    # Sauvegarde avec métadonnées
    img.save(out, pnginfo=pnginfo)
    img.close()
    return out


def extract_proof_png(path: Union[str, Path]) -> Dict[str, Any]:
    """
    Extrait la preuve MEVE depuis un PNG (clé _MEVE_KEY).
    Renvoie le dict JSON ; ValueError si absent ou invalide.
    """
    p = Path(path)
    img = Image.open(p)

    # Pillow expose les textes via .text (dict) sur PNG
    text_map = {}
    try:
        if hasattr(img, "text") and isinstance(img.text, dict):
            text_map = img.text
        else:
            # fallback: certaines versions exposent via info
            # (pas toujours fiable pour iTXt)
            info = getattr(img, "info", {}) or {}
            # clé exacte si déjà présente
            if _MEVE_KEY in info and isinstance(info[_MEVE_KEY], str):
                text_map[_MEVE_KEY] = info[_MEVE_KEY]
    finally:
        img.close()

    if _MEVE_KEY not in text_map:
        raise ValueError("No MEVE proof found in PNG metadata")

    raw = text_map[_MEVE_KEY]
    try:
        return json.loads(raw)
    except Exception as e:  # pragma: no cover
        raise ValueError(f"Invalid MEVE proof JSON in PNG: {e}") from e
