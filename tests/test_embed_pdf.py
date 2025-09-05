from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pikepdf

from digitalmeve.embedding_pdf import embed_proof_pdf, extract_proof_pdf


def test_pdf_embed_and_extract(tmp_path: Path) -> None:
    # 1) Create a tiny valid PDF (blank) just to have a container
    src_pdf = tmp_path / "sample.pdf"
    with pikepdf.Pdf.new() as pdf:
        pdf.save(str(src_pdf))
    assert src_pdf.exists()

    # 2) Minimal proof to embed
    issued_at = (
        datetime(2025, 1, 1, tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
    )
    proof = {
        "meve_version": "1.0",
        "issued_at": issued_at,
        "issuer": "Personal",
        "status": "Personal",
        "certified": "self",
        "hash_sha256": "00" * 32,
        "subject": {
            "filename": "sample.pdf",
            "size": 0,
            "hash_sha256": "00" * 32,
        },
    }

    # 3) Embed then extract from the PDF
    out_pdf = tmp_path / "sample.embedded.pdf"
    embed_proof_pdf(src_pdf, proof, out_pdf)
    assert out_pdf.exists()

    extracted = extract_proof_pdf(out_pdf)
    assert isinstance(extracted, dict)

    # 4) Key checks
    for key in ("meve_version", "issued_at", "issuer", "status", "certified"):
        assert extracted.get(key) == proof[key]
