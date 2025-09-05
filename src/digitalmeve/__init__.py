"""
DigitalMeve — public API.
"""

from .generator import generate_meve  # noqa: F401
from .verifier import verify_meve  # noqa: F401
from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401

# Version exposée (attendue par les tests)
__version__ = "1.7.1-dev"

__all__ = [
    "generate_meve",
    "verify_meve",
    "embed_proof_pdf",
    "extract_proof_pdf",
    "__version__",
]

# PNG : si le module est présent, on expose aussi (les tests l’importent)
try:  # pragma: no cover
    from .embedding_png import embed_proof_png, extract_proof_png  # type: ignore # noqa: F401

    __all__ += ["embed_proof_png", "extract_proof_png"]
except Exception:
    # Si indisponible, on ne casse pas l’import du package
    pass
