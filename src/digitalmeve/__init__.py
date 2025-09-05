"""
DigitalMeve package init: expose l’API publique sans casser si PNG n’est pas encore implémenté.
"""

# Version "best effort" (utile pour tests/version)
try:
    from importlib.metadata import PackageNotFoundError, version  # type: ignore
    try:
        __version__ = version("digitalmeve")
    except PackageNotFoundError:
        __version__ = "0.0.0"
except Exception:  # pragma: no cover
    __version__ = "0.0.0"

# PDF : toujours présent
from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401

# PNG : optionnel tant que le module n’existe pas
try:  # pragma: no cover
    from .embedding_png import embed_proof_png, extract_proof_png  # type: ignore  # noqa: F401
except Exception:  # pragma: no cover
    embed_proof_png = None  # type: ignore[assignment]
    extract_proof_png = None  # type: ignore[assignment]

__all__ = [
    "embed_proof_pdf",
    "extract_proof_pdf",
    "embed_proof_png",
    "extract_proof_png",
    "__version__",
]
