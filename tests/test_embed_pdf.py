diff --git a/tests/test_embed_pdf.py b/tests/test_embed_pdf.py
index 1111111..2222222 100644
--- a/tests/test_embed_pdf.py
+++ b/tests/test_embed_pdf.py
@@ -1,9 +1,7 @@
 from __future__ import annotations

 from datetime import datetime, timezone
 from pathlib import Path

-import pikepdf
-from pikepdf import Page
+import pikepdf

 from digitalmeve.embedding_pdf import embed_proof_pdf, extract_proof_pdf

@@ -21,10 +19,9 @@ def test_pdf_embed_and_extract(tmp_path: Path):
     # 1) créer un petit PDF de test
     src_pdf = tmp_path / "sample.pdf"
-    with pikepdf.Pdf.new() as pdf:
-        pdf.pages.append(Page.blank(width=200, height=200))
-        pdf.save(str(src_pdf))
+    # NB: Sur la version CI de pikepdf, Page.blank n'existe pas.
+    # Un PDF vide suffit pour tester l'embed/extract de docinfo.
+    with pikepdf.Pdf.new() as pdf:
+        pdf.save(str(src_pdf))

     assert src_pdf.exists()
