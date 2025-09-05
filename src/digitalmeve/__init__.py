"""
DigitalMeve public API.
"""

from .generator import generate_meve  # noqa: F401
from .verifier import verify_meve  # noqa: F401

# PDF embedding (présent dans le projet)
from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401

__all__ = [
    "generate_meve",
    "verify_meve",
    "embed_proof_pdf",
    "extract_proof_pdf",
]

# PNG embedding (optionnel) : on n'exporte que si le module existe
try:  # pragma: no cover
    from .embedding_png import embed_proof_png, extract_proof_png  # type: ignore  # noqa: F401

    __all__ += ["embed_proof_png", "extract_proof_png"]
except Exception:
    pass
