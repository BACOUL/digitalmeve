from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

import pikepdf


_MEVE_KEY = "/MEVE_Proof"


def _minify_json(obj: Dict[str, Any]) -> str:
    """Retourne un JSON **minifié** et UTF-8 (sans échappements inutiles)."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def embed_proof_pdf(
    in_path: Path | str,
    proof: Dict[str, Any],
    out_path: Optional[Path | str] = None,
) -> Path:
    """
    Embarque la preuve MEVE dans les métadonnées PDF (docinfo) sous la clé /MEVE_Proof.
    - in_path : PDF source
    - proof   : dict MEVE
    - out_path: destination (par défaut <in_path>.meve.pdf)
    Retourne le chemin du PDF écrit.
    """
    src = Path(in_path)
    if out_path is None:
        dst = src.with_suffix(src.suffix)  # garde .pdf
        dst = dst.with_name(src.stem + ".meve" + src.suffix)  # foo.pdf -> foo.meve.pdf
    else:
        dst = Path(out_path)

    if not src.exists():
        raise FileNotFoundError(f"PDF introuvable: {src}")

    payload = _minify_json(proof)

    with pikepdf.Pdf.open(str(src)) as pdf:
        # docinfo peut être immuable : on reconstruit un Dictionary modifiable
        info = pikepdf.Dictionary(pdf.docinfo)
        info[_MEVE_KEY] = payload
        pdf.docinfo = info
        pdf.save(str(dst))

    return dst


def extract_proof_pdf(in_path: Path | str) -> Dict[str, Any]:
    """
    Extrait la preuve MEVE (JSON) depuis les métadonnées PDF (/MEVE_Proof).
    Retourne un dict Python.
    Lève KeyError si la clé n’est pas présente ou JSONDecodeError si invalide.
    """
    src = Path(in_path)
    if not src.exists():
        raise FileNotFoundError(f"PDF introuvable: {src}")

    with pikepdf.Pdf.open(str(src)) as pdf:
        raw = pdf.docinfo.get(_MEVE_KEY, None)

    if raw is None:
        raise KeyError("Aucune preuve MEVE trouvée dans le PDF (/MEVE_Proof).")

    if isinstance(raw, bytes):
        raw = raw.decode("utf-8", errors="strict")

    # Certaines versions peuvent renvoyer un pikepdf.String
    raw_str = str(raw)
    return json.loads(raw_str)
