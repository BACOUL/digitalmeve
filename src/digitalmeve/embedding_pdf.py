# src/digitalmeve/embedding_png.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Union

from PIL import Image, PngImagePlugin

_MEVE_PNG_KEY = "meve_proof"


def embed_proof_png(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Union[str, Path],
) -> Path:
    """
    Intègre la preuve MEVE dans un PNG via un chunk texte (iTXt) sous la clé 'meve_proof'.
    - Copie le PNG d'entrée vers out_path en conservant les métadonnées texte existantes.
    - Ajoute/écrase la clé 'meve_proof' avec un JSON minifié.

    Retourne: Path(out_path)
    """
    p_in = Path(in_path)
    p_out = Path(out_path)

    with Image.open(p_in) as im:
        pnginfo = PngImagePlugin.PngInfo()

        # Conserver les métadonnées texte existantes (si présentes)
        # en évitant de dupliquer notre clé.
        info = getattr(im, "info", {}) or {}
        for k, v in info.items():
            if k == _MEVE_PNG_KEY:
                continue
            # Pillow peut stocker des bytes -> décoder si possible
            if isinstance(v, bytes):
                try:
                    v = v.decode("utf-8")
                except Exception:
                    # on saute les entrées non décodables
                    continue
            if isinstance(v, str):
                pnginfo.add_text(k, v)

        payload = json.dumps(proof, ensure_ascii=False, separators=(",", ":"))
        pnginfo.add_text(_MEVE_PNG_KEY, payload)

        # Sauvegarde avec nos métadonnées
        im.save(p_out, pnginfo=pnginfo)

    return p_out


def extract_proof_png(in_path: Union[str, Path]) -> Dict[str, Any] | None:
    """
    Extrait la preuve MEVE depuis un PNG (clé iTXt 'meve_proof').
    Retourne le dict de preuve ou None si absent/illisible.
    """
    p = Path(in_path)
    with Image.open(p) as im:
        data = getattr(im, "info", {}).get(_MEVE_PNG_KEY)
        if data is None:
            return None

        if isinstance(data, bytes):
            try:
                data = data.decode("utf-8")
            except Exception:
                return None

        try:
            return json.loads(data)
        except Exception:
            return None
