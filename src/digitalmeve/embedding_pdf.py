# src/digitalmeve/embedding_pdf.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

import pikepdf

__all__ = ["embed_proof_pdf", "extract_proof_pdf"]

# Clé sous laquelle on stocke la preuve dans les métadonnées PDF (DocInfo)
MEVE_PDF_KEY = "/MeveProof"


def _to_path(p: str | Path) -> Path:
    return p if isinstance(p, Path) else Path(p)


def embed_proof_pdf(
    in_path: str | Path, proof: Dict[str, Any], out_path: str | Path
) -> Path:
    """
    Écrit la preuve JSON (minifiée) dans DocInfo du PDF.
    Retourne le Path(out_path).
    """
    src = _to_path(in_path)
    dst = _to_path(out_path)

    payload = json.dumps(proof, separators=(",", ":"))

    with pikepdf.open(src) as pdf:
        info = pdf.docinfo  # type: ignore[assignment]
        info[MEVE_PDF_KEY] = payload
        pdf.save(dst)

    return dst


def extract_proof_pdf(path: str | Path) -> Optional[Dict[str, Any]]:
    """
    Lit la preuve depuis DocInfo. Retourne un dict ou None.
    """
    p = _to_path(path)
    with pikepdf.open(p) as pdf:
        info = pdf.docinfo or {}
        raw = (
            info.get(MEVE_PDF_KEY)
            or info.get("/MEVE_PROOF")
            or info.get("/meve_proof")
            or info.get("/Meve")
        )

    if raw is None:
        return None

    try:
        return json.loads(str(raw))
    except Exception:
        return None
