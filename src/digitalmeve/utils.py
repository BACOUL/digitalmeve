diff --git a/src/digitalmeve/utils.py b/src/digitalmeve/utils.py
index 074b2d4..a9a63f1 100644
--- a/src/digitalmeve/utils.py
+++ b/src/digitalmeve/utils.py
@@ -1,16 +1,16 @@
 # src/digitalmeve/utils.py
 from __future__ import annotations
 
-from pathlib import Path
-from typing import Optional, Union, Mapping, Any
 import json
 import sys
+from pathlib import Path
+from typing import Any, Mapping
 
 
 __all__ = [
     "format_identity",
     "load_json",
     "pretty_print",
 ]
 
 
-def load_json(path: Union[str, Path]) -> Any:
+def load_json(path: str | Path) -> Any:
     """
     Charge un fichier JSON (UTF-8) et renvoie l'objet Python.
     Laisse remonter les exceptions (FileNotFoundError, JSONDecodeError)
@@ -29,16 +29,16 @@ def pretty_print(data: Any) -> None:
     Utilisé par la commande `inspect` du CLI.
     """
     json.dump(data, sys.stdout, indent=2, ensure_ascii=False)
     print()  # flush avec un saut de ligne
 
 
-def format_identity(value: Optional[Union[str, Path, Mapping]]) -> str:
+def format_identity(value: str | Path | Mapping | None) -> str:
     """
     - str  -> retourne la string telle quelle
     - Path -> retourne le nom du fichier (sans extension) en MAJUSCULES
     - dict -> si clé 'identity' présente, on la renvoie
     - autres / None -> lève AttributeError
     """
     if isinstance(value, Path):
         return value.stem.upper()
     if isinstance(value, str):
         return value
     if isinstance(value, Mapping) and "identity" in value:
         return str(value["identity"])
     raise AttributeError("invalid identity")
