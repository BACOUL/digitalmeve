*** Begin Patch
*** Add File: src/digitalmeve/embedding_png.py
+from __future__ import annotations
+
+from pathlib import Path
+from typing import Any, Dict, Optional
+import json
+
+from PIL import Image, PngImagePlugin
+
+# Clé unique (non standard) pour stocker la preuve dans un chunk iTXt.
+_MEVE_KEY = "meve_proof"
+
+
+def _minified_json(data: Dict[str, Any]) -> str:
+    """Retourne un JSON minifié et UTF-8 (ensure_ascii=False) pour économiser de la place."""
+    return json.dumps(data, separators=(",", ":"), ensure_ascii=False)
+
+
+def embed_proof_png(
+    in_path: Path | str,
+    proof: Dict[str, Any],
+    out_path: Path | str | None = None,
+) -> Path:
+    """
+    Intègre une preuve .MEVE (dict) dans un PNG via un chunk iTXt.
+
+    - in_path : chemin du PNG source
+    - proof   : dict JSON-serializable de la preuve
+    - out_path: chemin de sortie (par défaut, <in>.meve.png)
+    """
+    src = Path(in_path)
+    if out_path is None:
+        out_path = src.with_suffix(".meve.png")
+    dst = Path(out_path)
+
+    # Ouvre l'image et prépare les métadonnées PNG
+    with Image.open(src) as im:
+        info = PngImagePlugin.PngInfo()
+
+        # Conserver les autres clés texte existantes si présentes
+        # (img.info ne contient que quelques champs textuels ; on recopie par prudence)
+        for k, v in im.info.items():
+            try:
+                # Certaines valeurs ne sont pas sérialisables en texte (ex: bKGD, tIME, etc.)
+                if isinstance(v, str):
+                    info.add_text(k, v)
+            except Exception:
+                # On ignore silencieusement ce qui n'est pas du texte
+                pass
+
+        # Ajoute la preuve minifiée dans un iTXt
+        info.add_text(_MEVE_KEY, _minified_json(proof))
+
+        # Sauvegarde assortie des métadonnées
+        im.save(dst, pnginfo=info)
+
+    return dst
+
+
+def extract_proof_png(in_path: Path | str) -> Optional[Dict[str, Any]]:
+    """
+    Extrait la preuve .MEVE embarquée dans un PNG (si présente), sinon None.
+    """
+    src = Path(in_path)
+    with Image.open(src) as im:
+        raw = im.info.get(_MEVE_KEY)
+        if not raw:
+            return None
+        try:
+            return json.loads(raw)
+        except Exception:
+            # Chunk présent mais non décodable en JSON
+            return None
+
*** End Patch
