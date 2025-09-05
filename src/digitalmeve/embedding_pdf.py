# src/digitalmeve/embedding_pdf.py
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Union
import json

import pikepdf


_MEVE_KEY = "/MEVE_Proof"  # clé Info où l'on stocke la preuve JSON minifiée


def _json_minified(obj: Dict[str, Any]) -> str:
    """JSON minifié, UTF-8 friendly (pour docinfo)."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def embed_proof_pdf(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Embarque `proof` dans le PDF via le dictionnaire Info (clé _MEVE_KEY).
    Retourne le chemin du PDF de sortie.
    """
    src = Path(in_path)
    if not src.exists():
        raise FileNotFoundError(f"file not found: {src}")

    out = Path(out_path) if out_path is not None else src.with_name(src.stem + ".meve.pdf")

    proof_str = _json_minified(proof)

    # Ouvre, met à jour le docinfo, sauvegarde
    with pikepdf.open(str(src)) as pdf:
        info = pdf.docinfo or pikepdf.Dictionary()
        info[pikepdf.Name(_MEVE_KEY)] = proof_str
        pdf.docinfo = info
        pdf.save(str(out))

    return out


def extract_proof_pdf(path: Union[str, Path]) -> Dict[str, Any]:
    """
    Extrait la preuve depuis le PDF (docinfo[_MEVE_KEY]) et la retourne en dict.
    Lève KeyError si la clé n’est pas trouvée ou JSONDecodeError si invalide.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"file not found: {p}")

    with pikepdf.open(str(p)) as pdf:
        info = pdf.docinfo or {}
        raw = info.get(pikepdf.Name(_MEVE_KEY))
        if raw is None:
            raise KeyError("MEVE proof not found in PDF docinfo")
        # pikepdf renvoie un PdfString; conversion en str puis JSON
        return json.loads(str(raw))
