diff --git a/src/digitalmeve/generator.py b/src/digitalmeve/generator.py
index 0000000..0000001 100644
--- a/src/digitalmeve/generator.py
+++ b/src/digitalmeve/generator.py
@@ -1,6 +1,6 @@
 from __future__ import annotations
 
-from base64 import b64encode
+from base64 import b64encode
 from datetime import datetime, timezone
 from hashlib import sha256
 from pathlib import Path
@@ -73,6 +73,7 @@ def generate_meve(
     preview = _preview_b64(path)
-    ts = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
+    ts = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
 
     proof: Dict[str, Any] = {
         "meve_version": _MEVE_VERSION,
         "issuer": issuer,
-        "timestamp": ts,
+        "timestamp": ts,
         "metadata": metadata or {},
         "subject": {
             "filename": path.name,
             "size": path.stat().st_size,
             "hash_sha256": content_hash,
         },
         # duplication utile et demandée par les tests
         "hash": content_hash,
         "preview_b64": preview,
+        # Champs avancés optionnels (présents mais vides par défaut)
+        # — seront renseignés par les niveaux Pro/Official plus tard.
+        "verified_domain": "",
+        "key_id": "",
+        "signature": "",
+        "doc_ref": "",
     }
 
     # écriture optionnelle du sidecar
     if outdir is not None:
         out = Path(outdir)
         out.mkdir(parents=True, exist_ok=True)
         outfile = out / f"{path.name}.meve.json"
 
         import json
         with outfile.open("w", encoding="utf-8") as f:
             json.dump(proof, f, ensure_ascii=False, separators=(",", ":"), indent=None)
 
     return proof
