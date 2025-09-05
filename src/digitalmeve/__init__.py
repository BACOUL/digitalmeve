"""DigitalMeve — The .MEVE Standard"""

# Garder la version alignée avec pyproject.toml
__version__ = "1.7.1-dev"

from .core import generate_meve  # noqa: F401
from .verifier import verify_identity  # noqa: F401
from .utils import format_identity  # noqa: F401

# Exposer (si présents) les helpers d’embedding
try:
    from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401
except Exception:  # module/fonctions absents en dev ?
    pass

try:
    from .embedding_png import embed_proof_png, extract_proof_png  # noqa: F401
except Exception:
    pass
