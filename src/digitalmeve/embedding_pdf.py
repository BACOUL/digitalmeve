*** /dev/null
--- a/src/digitalmeve/embedding_png.py
@@
+"""
+Embedding / extraction d'une preuve MEVE dans un PNG via Pillow.
+
+Technique : on stocke la preuve JSON minifiée dans un champ texte PNG
+(`meve_proof`) à l'aide de `PngInfo`. C'est lisible par n'importe quel outil
+qui préserve les metadata PNG.
+"""
+
+from __future__ import annotations
+
+from pathlib import Path
+import json
+from typing import Any, Dict, Optional
+
+from PIL import Image, PngImagePlugin
+
+MEVE_TEXT_KEY = "meve_proof"
+
+
+def _to_path(p: str | Path) -> str:
+    """Normalise en str pour Pillow / disque."""
+    return str(p if isinstance(p, Path) else Path(p))
+
+
+def embed_proof_png(in_path: str | Path, proof: Dict[str, Any], out_path: str | Path) -> Path:
+    """
+    Écrit `proof` dans un PNG en tant que texte `meve_proof`.
+
+    - `in_path` : image source (PNG)
+    - `proof`   : dict JSON-serializable
+    - `out_path`: fichier PNG de sortie
+    Retourne `Path(out_path)`.
+    """
+    src = _to_path(in_path)
+    dst = Path(_to_path(out_path))
+
+    # JSON compact (pas d'espaces) pour limiter la taille.
+    payload = json.dumps(proof, separators=(",", ":"))
+
+    with Image.open(src) as im:
+        # On reconstruit un PngInfo et on y met notre entrée.
+        pnginfo = PngImagePlugin.PngInfo()
+        # Conserver d'éventuels textes existants si Pillow les expose.
+        for k, v in (im.info or {}).items():
+            if isinstance(v, str) and k != MEVE_TEXT_KEY:
+                pnginfo.add_text(k, v)
+        pnginfo.add_text(MEVE_TEXT_KEY, payload)
+
+        # Sauvegarde : Pillow écrasera/créera le fichier de sortie.
+        im.save(_to_path(dst), format="PNG", pnginfo=pnginfo)
+
+    return dst
+
+
+def extract_proof_png(path: str | Path) -> Optional[Dict[str, Any]]:
+    """
+    Lit un PNG et tente d'extraire `meve_proof`.
+    Retourne le dict si présent, sinon `None`.
+    """
+    with Image.open(_to_path(path)) as im:
+        raw = (im.info or {}).get(MEVE_TEXT_KEY)
+        if not raw:
+            return None
+        try:
+            return json.loads(raw)
+        except json.JSONDecodeError:
+            return None
