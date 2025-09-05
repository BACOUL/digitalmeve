from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Union
import shutil


def embed_proof_png(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Stub d’embed pour PNG.

    Pour l’instant, on ne modifie pas l’image : on se contente de copier
    le fichier source vers la destination afin que l’API existe et que les
    imports des tests passent. L’implémentation iTXt arrivera plus tard.

    Retourne le chemin du fichier de sortie.
    """
    src = Path(in_path)
    if not src.exists():
        raise FileNotFoundError(f"file not found: {src}")

    if out_path is None:
        out = src.with_name(src.stem + ".meve.png")
    else:
        out = Path(out_path)

    # Copie binaire simple (placeholder)
    shutil.copy2(src, out)
    return out


def extract_proof_png(path: Union[str, Path]) -> Dict[str, Any]:
    """
    Stub d’extraction pour PNG.

    Non implémenté pour l’instant (prévu via chunk iTXt).
    On lève une NotImplementedError si jamais appelé.
    """
    raise NotImplementedError("PNG MEVE extraction not implemented yet")
