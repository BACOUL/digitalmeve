# src/digitalmeve/embedding_pdf.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

import pikepdf


# Clé utilisée dans les métadonnées Document Info du PDF
_DOCINFO_KEY = "/MeveProof"


def _minified_json(d: Dict[str, Any]) -> str:
    """JSON compact (UTF-8) pour stockage en métadonnées."""
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))


def embed_proof_pdf(
    in_path: Union[str, Path],
    proof: Dict[str, Any],
    out_path: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Intègre la preuve .meve (dict) dans les métadonnées PDF (Document Info).
    - Écrit la clé /MeveProof avec un JSON minifié.
    - Si out_path n'est pas fourni, crée <name>.meve.pdf à côté du fichier source.
    Retourne le chemin du PDF certifié.
    """
    src = Path(in_path)
    if not src.exists():
        raise FileNotFoundError(src)

    # Nom de sortie par défaut : document.meve.pdf
    if out_path is None:
        out_path = src.with_name(f"{src.stem}.meve.pdf")
    out = Path(out_path)

    # Ouverture + écriture Document Info
    with pikepdf.Pdf.open(str(src)) as pdf:
        info = pdf.docinfo or pikepdf.Dictionary()
        info[_DOCINFO_KEY] = _minified_json(proof)
        pdf.docinfo = info
        pdf.save(str(out))

    return out


def extract_proof_pdf(in_path: Union[str, Path]) -> Optional[Dict[str, Any]]:
    """
    Extrait et retourne la preuve (.meve) depuis les métadonnées PDF.
    Si absente ou invalide → retourne None.
    """
    src = Path(in_path)
    if not src.exists():
        raise FileNotFoundError(src)

    with pikepdf.Pdf.open(str(src)) as pdf:
        info = pdf.docinfo or {}
        raw = info.get(_DOCINFO_KEY)
        if not raw:
            return None
        try:
            return json.loads(str(raw))
        except Exception:
            return None
