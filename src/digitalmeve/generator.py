diff --git a/src/digitalmeve/generator.py b/src/digitalmeve/generator.py
index f719a50..abcd123 100644
--- a/src/digitalmeve/generator.py
+++ b/src/digitalmeve/generator.py
@@ -1,5 +1,6 @@
 from __future__ import annotations
 
+import json
 from base64 import b64encode
 from datetime import datetime, timezone
 from hashlib import sha256
@@ -73,22 +74,18 @@ def generate_meve(
     if outdir is not None:
         out = Path(outdir)
         out.mkdir(parents=True, exist_ok=True)
         outfile = out / f"{path.name}.meve.json"
-        import json
         with outfile.open("w", encoding="utf-8") as f:
-            json.dump(
-                proof, f, ensure_ascii=False, separators=(",", ":"), indent=None
-            )
+            json.dump(proof, f, ensure_ascii=False, separators=(",", ":"), indent=None)
 
     if also_json and outdir is None:
         outfile = path.with_name(f"{path.name}.meve.json")
-        import json
         with outfile.open("w", encoding="utf-8") as f:
-            json.dump(
-                proof, f, ensure_ascii=False, separators=(",", ":"), indent=None
-            )
+            json.dump(proof, f, ensure_ascii=False, separators=(",", ":"), indent=None)
 
     return proof
