diff --git a/src/digitalmeve/__init__.py b/src/digitalmeve/__init__.py
index 0000000..0000000 100644
--- a/src/digitalmeve/__init__.py
+++ b/src/digitalmeve/__init__.py
@@ -1,12 +1,23 @@
-from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401
-from .embedding_png import embed_proof_png, extract_proof_png  # noqa: F401
-from .generator import generate_meve  # noqa: F401
-from .verifier import verify_meve  # noqa: F401
-
-__all__ = [
-    "generate_meve",
-    "verify_meve",
-    "embed_proof_pdf",
-    "extract_proof_pdf",
-    "embed_proof_png",
-    "extract_proof_png",
-]
+"""
+DigitalMeve public API.
+Ne pas importer embedding_png ici si le module n’existe pas.
+"""
+
+from .generator import generate_meve  # noqa: F401
+from .verifier import verify_meve  # noqa: F401
+from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401
+
+__all__ = ["generate_meve", "verify_meve", "embed_proof_pdf", "extract_proof_pdf"]
+
+# Import PNG seulement si présent (optionnel)
+try:  # pragma: no cover
+    from .embedding_png import embed_proof_png, extract_proof_png  # type: ignore  # noqa: F401
+
+    __all__ += ["embed_proof_png", "extract_proof_png"]
+except Exception:
+    # Pas de module PNG → on n’expose rien côté PNG
+    pass
