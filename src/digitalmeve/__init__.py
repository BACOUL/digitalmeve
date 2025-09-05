-from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401
-from .embedding_png import embed_proof_png, extract_proof_png  # noqa: F401
-
-__all__ = [
-    "embed_proof_pdf",
-    "extract_proof_pdf",
-    "embed_proof_png",
-    "extract_proof_png",
-]
+from .embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401
+
+# Les fonctions PNG sont optionnelles tant que le module n’est pas présent.
+try:  # pragma: no cover
+    from .embedding_png import embed_proof_png, extract_proof_png  # type: ignore  # noqa: F401
+except Exception:  # pragma: no cover
+    embed_proof_png = None  # type: ignore
+    extract_proof_png = None  # type: ignore
+
+__all__ = [
+    "embed_proof_pdf",
+    "extract_proof_pdf",
+    "embed_proof_png",
+    "extract_proof_png",
+]
