from __future__ import annotations

from .generator import generate_meve, generate_proof  # noqa: F401
from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401
from .embedding_png import embed_proof_png, extract_proof_png  # noqa: F401
from .verifier import verify_identity, verify_meve  # noqa: F401

# IMPORTANT: gardez cette version alignée avec pyproject.toml
__version__ = "1.7.1-dev"

__all__ = [
    "generate_meve",
    "generate_proof",
    "embed_proof_pdf",
    "extract_proof_pdf",
    "embed_proof_png",
    "extract_proof_png",
    "verify_identity",
    "verify_meve",
    "__version__",
]
