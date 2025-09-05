from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

import pikepdf

# Clé dans les Document Info PDF
_MEVE_INFO_KEY = "/MEVE_PROOF"


def _minify(obj: Dict[str, Any]) -> str:
    """JSON compact (utf-8, sans espaces)."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def embed_proof_pdf(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Embarque la preuve MEVE dans un PDF via Document Info (_MEVE_INFO_KEY).

    - in_path : PDF source
    - proof   : dict MEVE (sera minifié en JSON)
    - out_path: destination ; si None, écrit à côté en suffixant '.meve.pdf'

    Retourne le chemin du fichier de sortie.
    """
    src = Path(in_path)
    if not src.exists():
        raise FileNotFoundError(f"file not found: {src}")

    if out_path is None:
        out = src.with_name(src.stem + ".meve.pdf")
    else:
        out = Path(out_path)

    with pikepdf.open(str(src)) as pdf:
        info = pdf.docinfo or pikepdf.Dictionary()
        info[_MEVE_INFO_KEY] = _minify(proof)
        pdf.docinfo = info
        pdf.save(str(out))

    return out


def extract_proof_pdf(path: Union[str, Path]) -> Dict[str, Any]:
    """
    Extrait la preuve MEVE depuis un PDF (clé _MEVE_INFO_KEY).
    Renvoie le dict JSON ; ValueError si absent ou invalide.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"file not found: {p}")

    with pikepdf.open(str(p)) as pdf:
        info = pdf.docinfo or {}
        raw = info.get(_MEVE_INFO_KEY)

    if not raw:
        raise ValueError("No MEVE proof found in PDF metadata")

    if isinstance(raw, bytes):
        raw = raw.decode("utf-8", errors="strict")

    if not isinstance(raw, str):
        raise ValueError("Invalid MEVE proof type in PDF metadata")

    try:
        return json.loads(raw)
    except Exception as e:  # pragma: no cover
        raise ValueError(f"Invalid MEVE proof JSON in PDF: {e}") from e
