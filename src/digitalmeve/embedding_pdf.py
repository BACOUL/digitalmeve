# src/digitalmeve/embedding_pdf.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

import pikepdf

# Clé simple dans le PDF Info (lisible par pikepdf et conservée par la plupart des outils)
MEVE_KEY = "/MeveProof"


def _to_str_path(p: str | Path) -> str:
    return str(p if isinstance(p, Path) else Path(p))


def embed_proof_pdf(in_path: str | Path, proof: Dict[str, Any], out_path: str | Path) -> Path:
    """
    Écrit la preuve JSON minifiée dans les metadata (docinfo) du PDF sous la clé MEVE_KEY.
    Retourne Path(out_path).
    """
    src = _to_str_path(in_path)
    dst = Path(_to_str_path(out_path))

    payload = json.dumps(proof, separators=(",", ":"))

    # Ouvre le PDF source, insère/écrase la clé, sauvegarde vers le fichier de sortie
    with pikepdf.open(src) as pdf:
        info = pdf.docinfo or pikepdf.Dictionary()
        info[MEVE_KEY] = pikepdf.String(payload)
        pdf.docinfo = info
        pdf.save(_to_str_path(dst))

    return dst


def extract_proof_pdf(path: str | Path) -> Optional[Dict[str, Any]]:
    """
    Lit la clé MEVE_KEY depuis les metadata du PDF et retourne le dict, ou None si absent/illisible.
    """
    with pikepdf.open(_to_str_path(path)) as pdf:
        try:
            info = pdf.docinfo
            if not info or MEVE_KEY not in info:
                return None
            raw = str(info[MEVE_KEY])
        except Exception:
            return None

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None
