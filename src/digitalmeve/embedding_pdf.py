from __future__ import annotations

import json
from pathlib import Path

from pikepdf import Name, Pdf, String

# We store the proof JSON under the Info dictionary key /MEVE
MEVE_INFO_KEY = Name("/MEVE")


def embed_proof_pdf(src_pdf: str | Path, proof: dict, out_pdf: str | Path) -> None:
    """
    Embed the MEVE proof (as JSON) into the PDF Info dictionary under /MEVE.

    Notes:
    - With pikepdf, mutate pdf.docinfo *in place*; do not assign a new dict.
    - The value must be a pikepdf.String (or convertible).
    """
    src_pdf = str(src_pdf)
    out_pdf = str(out_pdf)

    with Pdf.open(src_pdf) as pdf:
        info = pdf.docinfo
        info[MEVE_INFO_KEY] = String(json.dumps(proof, ensure_ascii=False))
        pdf.save(out_pdf)


def extract_proof_pdf(pdf_path: str | Path) -> dict | None:
    """
    Extract and deserialize the proof stored under /MEVE.
    Returns None if missing or invalid JSON.
    """
    pdf_path = str(pdf_path)

    with Pdf.open(pdf_path) as pdf:
        raw = pdf.docinfo.get(MEVE_INFO_KEY)
        if raw is None:
            return None
        try:
            return json.loads(str(raw))
        except Exception:
            return None
