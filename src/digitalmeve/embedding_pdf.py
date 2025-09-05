# src/digitalmeve/embedding_pdf.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

import pikepdf


__all__ = ["embed_proof_pdf", "extract_proof_pdf"]

# Clé docinfo utilisée pour stocker la preuve JSON minifiée
_DOCINFO_KEY = "/MeveProof"


def _to_path(p: Union[str, Path]) -> Path:
    return p if isinstance(p, Path) else Path(p)


def embed_proof_pdf(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Intègre la preuve JSON dans les métadonnées PDF (Info/XMP) via docinfo.

    - in_path : PDF source
    - proof   : dict JSON (sera minifié)
    - out_path: PDF de sortie ; si None, écrit à côté avec suffixe ".embedded.pdf"

    Retourne le Path du PDF écrit.
    """
    src = _to_path(in_path)
    if out_path is None:
        out = src.with_suffix(".embedded.pdf")
    else:
        out = _to_path(out_path)

    # Minifier le JSON pour diminuer la taille et rester stable
    proof_json = json.dumps(proof, separators=(",", ":"), ensure_ascii=False)

    with pikepdf.Pdf.open(str(src)) as pdf:
        # Copier l'info existant pour ne rien perdre
        info = pikepdf.Dictionary(pdf.docinfo) if pdf.docinfo is not None else pikepdf.Dictionary()
        # Écrire sous une clé custom
        info[_DOCINFO_KEY] = proof_json
        pdf.docinfo = info
        pdf.save(str(out))

    return out


def extract_proof_pdf(in_path: Union[str, Path]) -> Optional[Dict[str, Any]]:
    """
    Extrait la preuve JSON stockée dans les métadonnées PDF (docinfo).
    Retourne un dict si présent et valide, sinon None.
    """
    src = _to_path(in_path)
    with pikepdf.Pdf.open(str(src)) as pdf:
        if pdf.docinfo is None:
            return None
        raw = pdf.docinfo.get(_DOCINFO_KEY)
        if not raw:
            return None
        try:
            # pikepdf peut renvoyer un Object ; on force en str avant json.loads
            return json.loads(str(raw))
        except Exception:
            return None
