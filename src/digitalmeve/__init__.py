*** Begin Patch
*** Update File: src/digitalmeve/__init__.py
@@
-from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401
-# from .embedding_png import embed_proof_png, extract_proof_png  # noqa: F401
-__version__ = "1.7.1-dev"
+"""
+DigitalMeve public API surface.
+
+On n’exporte ici que les symboles stables nécessaires aux usages
+classiques (lib Python, CLI, API web). Les modules d’embedding (PDF/PNG)
+ne sont pas importés ici pour éviter les erreurs d’import côté API.
+"""
+
+from .generator import generate_meve  # noqa: F401
+from .verifier import verify_meve  # noqa: F401
+
+__all__ = ["__version__", "generate_meve", "verify_meve"]
+__version__ = "1.7.1-dev"
*** End Patch
