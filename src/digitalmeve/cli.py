diff --git a/src/digitalmeve/cli.py b/src/digitalmeve/cli.py
index f4b2c3d..9a7f6e1 100644
--- a/src/digitalmeve/cli.py
+++ b/src/digitalmeve/cli.py
@@ -4,6 +4,7 @@ import argparse
 import json
 import sys
 from pathlib import Path
+from typing import Optional, List
 
 from .generator import generate_meve
 from .verifier import verify_meve
@@ -12,7 +13,7 @@ from .verifier import verify_meve
 # -------- utils -----------------------------------------------------------
 
-def _read_text_from_optional_file(path_arg: str | None) -> str:
+def _read_text_from_optional_file(path_arg: Optional[str]) -> str:
     """
     Si path_arg est None ou '-', lit depuis stdin.
     Sinon lit le fichier en UTF-8 et retourne le contenu.
@@ -116,7 +117,7 @@ def build_parser() -> argparse.ArgumentParser:
     return parser
 
 
-def main(argv: list[str] | None = None) -> int:
+def main(argv: Optional[List[str]] = None) -> int:
     parser = build_parser()
     args = parser.parse_args(argv)
     return args.func(args)
