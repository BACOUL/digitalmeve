diff --git a/src/digitalmeve/cli.py b/src/digitalmeve/cli.py
index 1111111..2222222 100644
--- a/src/digitalmeve/cli.py
+++ b/src/digitalmeve/cli.py
@@ -1,8 +1,10 @@
 from __future__ import annotations
 
 import json
+import logging
 import sys
 from pathlib import Path
 from typing import Any, Dict, Optional
 
 import click
@@
 from .verifier import verify_meve
@@
 # Helpers
 # --------------------------------------------------------------------------- #
 
+logger = logging.getLogger("digitalmeve.cli")
+if not logger.handlers:
+    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
 
 def _read_json_file(path: Path) -> Optional[Dict[str, Any]]:
-    try:
-        text = path.read_text(encoding="utf-8")
-        if not text.strip():
-            return None
-        return json.loads(text)
-    except Exception:
-        return None
+    try:
+        text = path.read_text(encoding="utf-8")
+    except Exception as e:
+        logger.debug("Failed to read %s: %s", path, e)
+        return None
+    if not text.strip():
+        return None
+    try:
+        return json.loads(text)
+    except Exception as e:
+        logger.debug("Invalid JSON in %s: %s", path, e)
+        return None
 
 
 def _sidecar_candidates(path: Path) -> list[Path]:
@@
-    try:
-        cands.append(path.with_suffix(path.suffix + ".meve.json"))
-    except Exception:
-        pass
-    try:
-        cands.append(path.with_suffix(".meve.json"))
-    except Exception:
-        pass
+    try:
+        cands.append(path.with_suffix(path.suffix + ".meve.json"))
+    except Exception as e:
+        logger.debug("with_suffix(%s + .meve.json) failed for %s: %s", path.suffix, path, e)
+    try:
+        cands.append(path.with_suffix(".meve.json"))
+    except Exception as e:
+        logger.debug("with_suffix(.meve.json) failed for %s: %s", path, e)
@@
 def _write_sidecars(
     path: Path,
     proof: Dict[str, Any],
     outdir: Optional[Path],
 ) -> list[Path]:
@@
-    try:
-        outs.append((base / path.name).with_suffix(path.suffix + ".meve.json"))
-    except Exception:
-        pass
+    try:
+        outs.append((base / path.name).with_suffix(path.suffix + ".meve.json"))
+    except Exception as e:
+        logger.debug("sidecar keep-ext failed for %s: %s", path, e)
 
-    try:
-        outs.append((base / path.name).with_suffix(".meve.json"))
-    except Exception:
-        pass
+    try:
+        outs.append((base / path.name).with_suffix(".meve.json"))
+    except Exception as e:
+        logger.debug("sidecar replace-ext failed for %s: %s", path, e)
@@
     payload = json.dumps(proof, ensure_ascii=False, separators=(",", ":"))
     for o in uniq:
         o.write_text(payload, encoding="utf-8")
     return uniq
