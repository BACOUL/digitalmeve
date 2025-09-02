diff --git a/tests/test_schema.py b/tests/test_schema.py
@@
-import json
-import pathlib
+import json
+from pathlib import Path
 
-def _load_schema():
-    with open("meve-1.schema.json") as f:
-        return json.load(f)
+def _load_schema():
+    """Charge le schéma depuis schemas/meve-1.schema.json (chemin robuste)."""
+    repo_root = Path(__file__).resolve().parents[1]
+    candidates = [
+        repo_root / "schemas" / "meve-1.schema.json",
+        # fallback éventuel si quelqu’un l’a mis ailleurs :
+        repo_root / "src" / "digitalmeve" / "schemas" / "meve-1.schema.json",
+    ]
+    for p in candidates:
+        if p.exists() and p.is_file():
+            with p.open(encoding="utf-8") as f:
+                return json.load(f)
+    raise FileNotFoundError(
+        "meve-1.schema.json introuvable. Place-le dans ./schemas/meve-1.schema.json"
+    )
