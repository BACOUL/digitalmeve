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


def _sidecar_candidates(path: Path) -> list[Path]:
    """
    Deux conventions possibles suivant les outils/tests :
      A) remplace la dernière extension en ajoutant '.meve.json'
         ex: file.pdf -> file.pdf.meve.json
      B) concatène simplement '.meve.json'
         ex: file.pdf -> file.pdf.meve.json (identique si extension),
             file      -> file.meve.json   (si pas d'extension)
    """
    cand_a = path.with_suffix(path.suffix + ".meve.json")
    cand_b = Path(str(path) + ".meve.json")
    # déduplique si identiques
    out: list[Path] = []
    for c in (cand_a, cand_b):
        if c not in out:
            out.append(c)
    return out


def _find_sidecar_for(path: Path) -> Optional[Path]:
    for cand in _sidecar_candidates(path):
        if cand.exists():
            return cand
    return None


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
        # on choisit la convention A côté outdir
        out = (outdir / path.name).with_suffix(path.suffix + ".meve.json")
    else:
        # en local, convention A (les tests acceptent A ou B, on reste cohérent)
        out = path.with_suffix(path.suffix + ".meve.json")
    out.write_text(
        json.dumps(proof, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    return out


# -------- CLI ----------------------------------------------------------------


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    """DigitalMeve command-line interface."""


@cli.command("generate")
@click.argument("file", type=click.Path(path_type=Path, exists=True, dir_okay=False))
@click.option(
    "--issuer", type=str, required=False, help="Issuer name to embed in the proof."
)
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
def cmd_generate(
    file: Path, issuer: Optional[str], also_json: bool, outdir: Optional[Path]
) -> None:
    """
    Generate a MEVE proof for FILE.
    - PDF/PNG: embed proof into a new file (.meve.pdf/.meve.png). Optionally write a sidecar.
    - Others: only write sidecar (use --also-json or it will be written implicitly).
    """
    proof = generate_meve(file, issuer=issuer)

    suffix = file.suffix.lower()
    produced_anything = False

    # 1) Embedding pour formats supportés
    if suffix == ".pdf":
        out_path = None if outdir is None else (outdir / (file.stem + ".meve.pdf"))
        embed_proof_pdf(file, proof, out_path=out_path)
        produced_anything = True
    elif suffix == ".png":
        out_path = None if outdir is None else (outdir / (file.stem + ".meve.png"))
        embed_proof_png(file, proof, out_path=out_path)
        produced_anything = True

    # 2) Sidecar si demandé… ou si format non supporté
    if also_json or not produced_anything:
        _write_sidecar(file, proof, outdir)
        produced_anything = True

    if not produced_anything:
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
    proof = _maybe_extract_embedded(file)

    if proof is None:
        sidecar = _find_sidecar_for(file)
        if sidecar is not None:
            proof = _read_json_file(sidecar)

    if proof is None:
        click.echo("Error: No proof found (neither embedded nor sidecar).", err=True)
        sys.exit(1)

    ok, info = verify_meve(proof, expected_issuer=expected_issuer)
    if ok:
        sys.exit(0)

    click.echo(f"Error: {info.get('error', 'Invalid proof')}", err=True)
    sys.exit(1)


@cli.command("inspect")
@click.argument("file", type=click.Path(path_type=Path, exists=True, dir_okay=False))
def cmd_inspect(file: Path) -> None:
    """
    Print the MEVE proof for FILE to stdout as **pure JSON**.
    1) Try embedded proof (PDF/PNG).
    2) Else try sidecar (two naming conventions).
    """
    proof = _maybe_extract_embedded(file)

    if proof is None:
        # essaie les deux conventions de sidecar
        for cand in _sidecar_candidates(file):
            proof = _read_json_file(cand)
            if proof is not None:
                break

    if proof is None:
        click.echo("Error: No proof found (neither embedded nor sidecar).", err=True)
        sys.exit(1)

    sys.stdout.write(json.dumps(proof, ensure_ascii=False, separators=(",", ":")))
    sys.stdout.flush()


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
