from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

import click

from .generator import generate_meve
from .verifier import verify_meve
from .embedding_pdf import embed_proof_pdf, extract_proof_pdf
from .embedding_png import embed_proof_png, extract_proof_png


# -------- Helpers ------------------------------------------------------------


def _read_json_file(path: Path) -> Optional[Dict[str, Any]]:
    try:
        text = path.read_text(encoding="utf-8")
        return json.loads(text)
    except Exception:
        return None


def _find_sidecar_for(path: Path) -> Optional[Path]:
    """Ex.: /tmp/file.pdf -> /tmp/file.pdf.meve.json (s'il existe)."""
    sidecar = path.with_suffix(path.suffix + ".meve.json")
    return sidecar if sidecar.exists() else None


def _maybe_extract_embedded(path: Path) -> Optional[Dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_proof_pdf(path)
    if suffix == ".png":
        return extract_proof_png(path)
    return None


def _write_sidecar(path: Path, proof: Dict[str, Any], outdir: Optional[Path]) -> Path:
    if outdir:
        outdir.mkdir(parents=True, exist_ok=True)
        out = (outdir / path.name).with_suffix(path.suffix + ".meve.json")
    else:
        out = path.with_suffix(path.suffix + ".meve.json")
    out.write_text(json.dumps(proof, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return out


# -------- CLI ----------------------------------------------------------------


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    """DigitalMeve command-line interface."""


@cli.command("generate")
@click.argument("file", type=click.Path(path_type=Path, exists=True, dir_okay=False))
@click.option("--issuer", type=str, required=False, help="Issuer name to embed in the proof.")
@click.option(
    "--also-json",
    "also_json",
    is_flag=True,
    default=False,
    help="Also write a .meve.json sidecar next to the file.",
)
@click.option(
    "--outdir",
    type=click.Path(path_type=Path, file_okay=False, dir_okay=True),
    required=False,
    help="Directory where to write outputs (sidecar and/or embedded copy).",
)
def cmd_generate(file: Path, issuer: Optional[str], also_json: bool, outdir: Optional[Path]) -> None:
    """
    Generate a MEVE proof for FILE.
    - PDF/PNG: embed proof into a new file (.meve.pdf/.meve.png). Optionally write a sidecar.
    - Others: only write sidecar (use --also-json or nothing will be produced silently).
    """
    proof = generate_meve(file, issuer=issuer)

    suffix = file.suffix.lower()
    produced_anything = False

    # 1) Embed for supported formats
    if suffix == ".pdf":
        embed_proof_pdf(file, proof, out_path=None if outdir is None else outdir / (file.stem + ".meve.pdf"))
        produced_anything = True
    elif suffix == ".png":
        embed_proof_png(file, proof, out_path=None if outdir is None else outdir / (file.stem + ".meve.png"))
        produced_anything = True

    # 2) Sidecar if requested
    if also_json or not produced_anything:
        _write_sidecar(file, proof, outdir)
        produced_anything = True

    if not produced_anything:
        # Ne devrait pas arriver, mais on garde un message clair.
        click.echo(
            "Error: Embedding supported only for PDF/PNG. Use --also-json to write a sidecar for other formats.",
            err=True,
        )
        sys.exit(1)


@cli.command("verify")
@click.argument("file", type=click.Path(path_type=Path, exists=True, dir_okay=False))
@click.option("--expected-issuer", type=str, required=False, help="Expected issuer.")
def cmd_verify(file: Path, expected_issuer: Optional[str]) -> None:
    """
    Verify FILE by extracting an embedded proof or falling back to a .meve.json sidecar.
    Exit code 0 on success, 1 on failure.
    """
    # 1) embedded?
    proof = _maybe_extract_embedded(file)

    # 2) otherwise sidecar?
    if proof is None:
        sidecar = _find_sidecar_for(file)
        if sidecar is not None:
            proof = _read_json_file(sidecar)

    if proof is None:
        click.echo("Error: No proof found (neither embedded nor sidecar).", err=True)
        sys.exit(1)

    ok, info = verify_meve(proof, expected_issuer=expected_issuer)
    if ok:
        # Pas de bruit : succès = code 0, rien à stdout (les tests ne lisent pas un JSON ici).
        sys.exit(0)

    # Échec → message clair + code 1
    click.echo(f"Error: {info.get('error', 'Invalid proof')}", err=True)
    sys.exit(1)


@cli.command("inspect")
@click.argument("file", type=click.Path(path_type=Path, exists=True, dir_okay=False))
def cmd_inspect(file: Path) -> None:
    """
    Print the MEVE proof for FILE to stdout as **pure JSON**.
    1) Try embedded proof (PDF/PNG), else
    2) Try sidecar `<file>.meve.json`.
    """
    proof = _maybe_extract_embedded(file)
    if proof is None:
        sidecar = _find_sidecar_for(file)
        if sidecar is not None:
            proof = _read_json_file(sidecar)

    if proof is None:
        click.echo("Error: No proof found (neither embedded nor sidecar).", err=True)
        sys.exit(1)

    # IMPORTANT: sortie stricte JSON (pas de texte avant/après) pour éviter JSONDecodeError dans les tests.
    sys.stdout.write(json.dumps(proof, ensure_ascii=False, separators=(",", ":")))
    sys.stdout.flush()


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
