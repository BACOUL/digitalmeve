from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import json
import pikepdf


MEVE_DOCINFO_KEY = "meve_proof"  # clé légère dans Info (XMP possible plus tard)


def embed_proof_pdf(in_path: Path | str, proof: Dict[str, Any], out_path: Path | str | None = None) -> Path:
    """
    Embarque la preuve JSON (minifiée) dans les métadonnées PDF (Info).
    - in_path: PDF source
    - proof: dict JSON sérialisable
    - out_path: destination; si None, écrit à côté sous <name>.meve.pdf
    """
    in_path = Path(in_path)
    if out_path is None:
        out_path = in_path.with_suffix(".meve.pdf")
    out_path = Path(out_path)

    payload = json.dumps(proof, separators=(",", ":"), ensure_ascii=False)

    with pikepdf.Pdf.open(in_path) as pdf:
        info = pdf.docinfo or pikepdf.Dictionary()
        info[MEVE_DOCINFO_KEY] = pikepdf.String(payload)
        pdf.docinfo = info
        pdf.save(str(out_path))

    return out_path


def extract_proof_pdf(path: Path | str) -> Optional[Dict[str, Any]]:
    """
    Extrait la preuve depuis les métadonnées PDF (Info[MEVE_DOCINFO_KEY]).
    Retourne dict ou None si absent/invalide.
    """
    path = Path(path)
    try:
        with pikepdf.Pdf.open(path) as pdf:
            info = pdf.docinfo or {}
            raw = info.get(MEVE_DOCINFO_KEY)
            if not raw:
                return None
            if isinstance(raw, pikepdf.String):
                raw = str(raw)
            return json.loads(raw)
    except Exception:
        return None


def is_meve_pdf(path: Path | str) -> bool:
    """
    Heuristique rapide : existe et suffix .meve.pdf OU présence de la clé Info.
    """
    p = Path(path)
    if not p.exists():
        return False
    if p.name.endswith(".meve.pdf"):
        return True
    try:
        with pikepdf.Pdf.open(p) as pdf:
            info = pdf.docinfo or {}
            return MEVE_DOCINFO_KEY in info
    except Exception:
        return False
