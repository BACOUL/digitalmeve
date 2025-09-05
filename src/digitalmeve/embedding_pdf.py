from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

from PIL import Image, PngImagePlugin

__all__ = ["embed_proof_png", "extract_proof_png"]

_TEXT_KEY = "meve_proof"  # iTXt key


def _to_path(p: Union[str, Path]) -> Path:
    return p if isinstance(p, Path) else Path(p)


def embed_proof_png(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Optional[Union[str, Path]] = None,
) -> Path:
    """Embed the JSON proof into a PNG via an iTXt chunk."""
    src = _to_path(in_path)
    out = (
        _to_path(out_path) if out_path is not None else src.with_suffix(".embedded.png")
    )

    proof_json = json.dumps(proof, separators=(",", ":"), ensure_ascii=False)

    with Image.open(src) as im:
        info = PngImagePlugin.PngInfo()
        # Preserve existing textual metadata
        if hasattr(im, "info"):
            for k, v in im.info.items():
                try:
                    info.add_text(str(k), str(v))
                except Exception:
                    pass
        info.add_text(_TEXT_KEY, proof_json)
        im.save(out, pnginfo=info)

    return out


def extract_proof_png(in_path: Union[str, Path]) -> Optional[Dict[str, Any]]:
    """Extract the JSON proof from a PNG iTXt chunk, if present."""
    src = _to_path(in_path)
    with Image.open(src) as im:
        payload = getattr(im, "info", {}).get(_TEXT_KEY)
        if not payload:
            return None
        try:
            return json.loads(str(payload))
        except Exception:
            return None
