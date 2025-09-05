diff --git a/src/digitalmeve/verifier.py b/src/digitalmeve/verifier.py
index 0000000..0000000 100644
--- a/src/digitalmeve/verifier.py
+++ b/src/digitalmeve/verifier.py
@@ -1,10 +1,16 @@
 from __future__ import annotations

 import json
 from pathlib import Path
 from typing import Any, Dict, Iterable, Optional, Tuple

+# Extraction des preuves embarquées (PDF/PNG)
+try:
+    from .embedding_pdf import extract_proof_pdf
+except Exception:  # pragma: no cover
+    extract_proof_pdf = None  # type: ignore
+try:
+    from .embedding_png import extract_proof_png
+except Exception:  # pragma: no cover
+    extract_proof_png = None  # type: ignore
+

 def verify_identity(identity: str | Path | None) -> bool:
     """
@@ -19,6 +25,48 @@ def verify_identity(identity: str | Path | None) -> bool:
     return str(identity).strip() != ""


+def verify_file(
+    path: str | Path,
+    *,
+    expected_issuer: Optional[str] = None,
+) -> Tuple[bool, Dict[str, Any]]:
+    """
+    Vérifie un fichier contenant une preuve .meve :
+      - JSON (sidecar) : *.meve.json ou *.json
+      - PDF embarqué   : *.pdf ou *.meve.pdf
+      - PNG embarqué   : *.png ou *.meve.png
+    Retourne (ok, info|{"error": "..."}).
+    """
+    p = Path(path)
+    if not p.exists():
+        return False, {"error": "File not found"}
+
+    name = p.name.lower()
+    suf = p.suffix.lower()
+
+    # 1) Sidecar JSON
+    if suf == ".json" or name.endswith(".meve.json"):
+        proof = _as_dict(p)
+        return verify_meve(proof, expected_issuer=expected_issuer)
+
+    # 2) PDF embarqué
+    if suf == ".pdf" or name.endswith(".meve.pdf"):
+        if extract_proof_pdf is None:
+            return False, {"error": "PDF extraction unavailable"}
+        try:
+            proof = extract_proof_pdf(p)  # type: ignore[misc]
+            return verify_meve(proof, expected_issuer=expected_issuer)
+        except Exception as e:  # pragma: no cover
+            return False, {"error": f"PDF extraction failed: {e}"}
+
+    # 3) PNG embarqué
+    if suf == ".png" or name.endswith(".meve.png"):
+        if extract_proof_png is None:
+            return False, {"error": "PNG extraction unavailable"}
+        try:
+            proof = extract_proof_png(p)  # type: ignore[misc]
+            return verify_meve(proof, expected_issuer=expected_issuer)
+        except Exception as e:  # pragma: no cover
+            return False, {"error": f"PNG extraction failed: {e}"}
+
+    return False, {"error": f"Unsupported file type: {suf}"}
+
 def _as_dict(proof: Any) -> Optional[Dict[str, Any]]:
     """
     Accepte :
       - un dict (retourné tel quel)
@@ -95,3 +143,4 @@ def verify_meve(
         return False, {"error": msg}  # noqa: E501

     return True, obj
+
