# tests/test_embed_pdf.py
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pikepdf

from digitalmeve.embedding_pdf import embed_proof_pdf, extract_proof_pdf


def _iso8601_z_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def test_pdf_embed_and_extract(tmp_path: Path):
    # 1) créer un petit PDF de test
    src_pdf = tmp_path / "sample.pdf"
    with pikepdf.Pdf.new() as pdf:
        pdf.pages.append(pikepdf.Page(width=200, height=200))
        pdf.save(str(src_pdf))

    assert src_pdf.exists()

    # 2) preuve minimale (compatible générateur actuel)
    proof = {
        "meve_version": "1.0",
        "issuer": "Personal",
        "issued_at": _iso8601_z_now(),
        "timestamp": _iso8601_z_now(),
        "metadata": {},
        "subject": {
            "filename": src_pdf.name,
            "size": src_pdf.stat().st_size,
            "hash_sha256": "deadbeef" * 8,  # valeur factice pour le test
        },
        "hash": "deadbeef" * 8,
        "preview_b64": "",
    }

    # 3) embed → produit sample.meve.pdf
    out_pdf = embed_proof_pdf(src_pdf, proof)
    assert out_pdf.exists()
    assert out_pdf.name == "sample.meve.pdf"

    # 4) extract → doit retrouver la même preuve (au moins les champs clés)
    extracted = extract_proof_pdf(out_pdf)
    assert isinstance(extracted, dict)
    assert extracted["issuer"] == proof["issuer"]
    assert extracted["meve_version"] == "1.0"

    # 5) robustesse : si on enlève la métadonnée, extract -> None
    # (on simule en sauvegardant un PDF sans /MeveProof)
    no_meta = tmp_path / "no_meta.pdf"
    with pikepdf.Pdf.open(str(out_pdf)) as pdf2:
        info = pdf2.docinfo
        if "/MeveProof" in info:
            del info["/MeveProof"]
        pdf2.docinfo = info
        pdf2.save(str(no_meta))

    assert extract_proof_pdf(no_meta) is None
