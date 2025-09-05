*** Begin Patch
*** Update File: src/digitalmeve/cli.py
@@
 from __future__ import annotations
 
 import json
 from pathlib import Path
-from typing import Any, Dict, Optional, Tuple
+from typing import Any, Dict, Optional
 
 import click
 
 from .generator import generate_meve
 from .verifier import verify_meve
@@
 @cli.command("generate")
 @click.argument("input_file", type=click.Path(path_type=Path, exists=True, dir_okay=False))
 @click.option("--issuer", required=True, help='Issuer label (e.g. "Personal" or "Alice").')
 @click.option(
     "--also-json",
     is_flag=True,
     default=False,
-    help="Also write a sidecar <output>.meve.json next to the generated file.",
+    help="Also write a sidecar <output>.meve.json next to the generated file (PDF/PNG).",
 )
 @click.option(
     "--outdir",
     type=click.Path(path_type=Path, file_okay=False),
     default=None,
     help="Optional output directory. Defaults to input folder.",
 )
 def cmd_generate(input_file: Path, issuer: str, also_json: bool, outdir: Optional[Path]) -> None:
     """
     Generate a .meve proof for INPUT_FILE and embed it when possible.
 
     Output:
       - For PDF  -> <name>.meve.pdf
       - For PNG  -> <name>.meve.png
-      - For others -> only JSON sidecar if --also-json is provided
+      - For others -> JSON sidecar is ALWAYS written by default
     """
     input_file = input_file.resolve()
     target_dir = (outdir or input_file.parent).resolve()
 
     # 1) Build the proof dict in memory
     proof = generate_meve(str(input_file), issuer=issuer)
 
     # 2) Embed depending on file type
     suffix = input_file.suffix.lower()
     if suffix == ".pdf":
         out_path = target_dir / _infer_out_path_meve(input_file).name
         out_path = embed_proof_pdf(input_file, proof, out_path)
         click.echo(f"Embedded MEVE → {out_path}")
         if also_json:
             sidecar = _write_json_sidecar(out_path, proof)
             click.echo(f"Wrote sidecar → {sidecar}")
         return
 
     if suffix == ".png":
         out_path = target_dir / _infer_out_path_meve(input_file).name
         out_path = embed_proof_png(input_file, proof, out_path)
         click.echo(f"Embedded MEVE → {out_path}")
         if also_json:
             sidecar = _write_json_sidecar(out_path, proof)
             click.echo(f"Wrote sidecar → {sidecar}")
         return
 
-    # 3) Other formats: only JSON sidecar (when requested)
-    if also_json:
-        # Sidecar named from original file (not *.meve.ext because no embedding)
-        sidecar = input_file.with_name(f"{input_file.name}.meve.json")
-        if outdir:
-            sidecar = (Path(outdir).resolve() / sidecar.name)
-        sidecar.write_text(json.dumps(proof, indent=2, ensure_ascii=False), encoding="utf-8")
-        click.echo(f"Wrote sidecar → {sidecar}")
-    else:
-        raise click.ClickException(
-            "Embedding supported only for PDF/PNG. Use --also-json to write a sidecar for other formats."
-        )
+    # 3) Other formats: ALWAYS write a JSON sidecar (default behavior)
+    sidecar = input_file.with_name(f"{input_file.name}.meve.json")
+    if outdir:
+        sidecar = (Path(outdir).resolve() / sidecar.name)
+    sidecar.write_text(json.dumps(proof, indent=2, ensure_ascii=False), encoding="utf-8")
+    click.echo(f"Wrote sidecar → {sidecar}")
*** End Patch
