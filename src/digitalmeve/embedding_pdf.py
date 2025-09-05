from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

import pikepdf
from pikepdf import Name

__all__ = ["embed_proof_pdf", "extract_proof_pdf"]

_KEY = "/MeveProof"  # entrée Info (docinfo) qui stocke la preuve JSON


def _p(p: Union[str, Path]) -> Path:
    return p if isinstance(p, Path) else Path(p)


def embed_proof_pdf(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Embedde une preuve .meve (dict) dans un PDF via le dictionnaire Info (docinfo).
    Retourne le chemin du PDF de sortie.
    """
    src = _p(in_path)
    out = _p(out_path) if out_path is not None else src.with_suffix(".embedded.pdf")

    proof_json = json.dumps(proof, ensure_ascii=False, separators=(",", ":"))

    with pikepdf.Pdf.open(str(src)) as pdf:
        # docinfo est un mapping nom -> valeur ; on écrit sous /MeveProof
        try:
            pdf.docinfo[_KEY] = proof_json
        except Exception:
            # au cas où il faille remplacer entièrement docinfo
            info = dict(pdf.docinfo) if pdf.docinfo is not None else {}
            info[Name(_KEY)] = proof_json
            pdf.docinfo = info  # type: ignore[assignment]
        pdf.save(str(out))

    return out


def extract_proof_pdf(in_path: Union[str, Path]) -> Optional[Dict[str, Any]]:
    """
    Lit la preuve JSON depuis le champ Info (/MeveProof). Retourne dict ou None.
    """
    src = _p(in_path)
    with pikepdf.Pdf.open(str(src)) as pdf:
        value = None
        try:
            # accès direct string ou objet pikepdf
            value = pdf.docinfo.get(_KEY)  # type: ignore[union-attr]
        except Exception:
            value = None

        if not value:
            return None

        # normaliser en str
        if isinstance(value, bytes):
            value = value.decode("utf-8", "ignore")
        value = str(value)

        try:
            return json.loads(value)
        except Exception:
            return None
