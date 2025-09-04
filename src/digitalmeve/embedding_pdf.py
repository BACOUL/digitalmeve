diff --git a/src/digitalmeve/embedding_pdf.py b/src/digitalmeve/embedding_pdf.py
--- a/src/digitalmeve/embedding_pdf.py
+++ b/src/digitalmeve/embedding_pdf.py
@@
-# (ancien code)
+from __future__ import annotations
+
+import json
+from pathlib import Path
+
+import pikepdf
+from pikepdf import Name, Pdf, String
+
+
+MEVE_INFO_KEY = Name("/MEVE")  # clé standardisée pour stocker la preuve
+
+
+def embed_proof_pdf(src_pdf: str | Path, proof: dict, out_pdf: str | Path) -> None:
+    """
+    Emballe la preuve JSON dans les métadonnées Info du PDF sous la clé /MEVE.
+    Note: avec pikepdf, on modifie pdf.docinfo *en place* (pas d'affectation d'un dict).
+    """
+    src_pdf = str(src_pdf)
+    out_pdf = str(out_pdf)
+    with Pdf.open(src_pdf) as pdf:
+        info = pdf.docinfo
+        info[MEVE_INFO_KEY] = String(json.dumps(proof, ensure_ascii=False))
+        pdf.save(out_pdf)
+
+
+def extract_proof_pdf(pdf_path: str | Path) -> dict | None:
+    """
+    Récupère et désérialise la preuve stockée sous /MEVE.
+    Renvoie None si absente ou invalide.
+    """
+    pdf_path = str(pdf_path)
+    with Pdf.open(pdf_path) as pdf:
+        raw = pdf.docinfo.get(MEVE_INFO_KEY)
+        if raw is None:
+            return None
+        try:
+            return json.loads(str(raw))
+        except Exception:
+            return None
