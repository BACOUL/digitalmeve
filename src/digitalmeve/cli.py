from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

import click

from .embedding_pdf import embed_proof_pdf, extract_proof_pdf
from .embedding_png import embed_proof_png, extract_proof_png
from .generator import generate_meve
from .verifier import verify_meve


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _read_json_file(path: Path) -> Optional[Dict[str, Any]]:
    try:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return None
        return json.loads(text)
    except Exception:
        return None


def _sidecar_candidates(path: Path) -> list[Path]:
    """
    Tente plusieurs conventions de sidecar, dans l'ordre :
      A) file.ext.meve.json
      B) file.meve.json
      C) <str(path)>.meve.json
      D) path.parent / (path.name + ".meve.json")
      E) path.parent / (path.stem + ".meve.json")
    """
    cands: list[Path] = []
    try:
        cands.append(path.with_suffix(path.suffix + ".meve.json"))
    except Exception:
        pass
    try:
        cands.append(path.with_suffix(".meve.json"))
    except Exception:
        pass
    cands.append(Path(str(path) + ".meve.json"))
    cands.append(path.parent / (path.name + ".meve.json"))
    cands.append(path.parent / (path.stem + ".meve.json"))

    seen: set[str] = set()
    uniq: list[Path] = []
    for p in cands:
        key = str(p)
        if key not in seen:
            seen.add(key)
            uniq.append(p)
    return uniq


def _find_sidecar_for(path: Path) -> Optional[Path]:
    for cand in _sidecar_candidates(path):
        if cand.exists():
            return cand
    return None


def _maybe_extract_embedded(path: Path) -> Optional[Dict[str, Any]]:
    sfx = path.suffix.lower()
    if sfx == ".pdf":
        return extract_proof_pdf(path)
    if sfx == ".png":
        return extract_proof_png(path)
    return None


def _write_sidecars(path: Path, proof: Dict[str, Any], outdir: Optional[Path]) -> list[Path]:
    """
    Écrit jusqu’à deux variantes quand elles diffèrent :
      - file.ext.meve.json
      - file.meve.json
    """
    base = (outdir or path.parent)
    base.mkdir(parents=True, exist_ok=True)

    outs: list[Path] = []

    try:
        a = (base / path.name).with_suffix(path.suffix + ".meve.json")
        outs.append(a)
    except Exception:
        a = None

    try:
        b = (base / path.name).with_suffix(".meve.json")
        if a is None or str(b) != str(a):
            outs.append(b)
    except Exception:
        pass

    payload = json.dumps(proof, ensure_ascii=False, separators=(",", ":"))
    for o in outs:
        o.write_text(payload, encoding="utf-8")
    return outs


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


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
    help="Also write a .meve.json sidecar (in --outdir if provided).",
)
@click.option(
    "--outdir",
    type=click.Path(path_type=Path, file_okay=False, dir_okay=True),
    required=False,
    help="Directory for outputs (sidecar and/or embedded copy).",
)
def cmd_generate(file: Path, issuer: Optional[str], also_json: bool, outdir: Optional[Path]) -> None:
    """
    Generate a MEVE proof for FILE.
    - PDF/PNG: embed proof into .meve.pdf/.meve.png.
    - Tous formats : un sidecar est TOUJOURS écrit à côté du fichier source.
    - Si --also-json est fourni, on écrit un sidecar supplémentaire dans --outdir.
    """
    proof = generate_meve(file, issuer=issuer)

    # 1) Embedding si supporté
    suffix = file.suffix.lower()
    if suffix == ".pdf":
        dst = None if outdir is None else (outdir / (file.stem + ".meve.pdf"))
        embed_proof_pdf(file, proof, out_path=dst)
    elif suffix == ".png":
        dst = None if outdir is None else (outdir / (file.stem + ".meve.png"))
        embed_proof_png(file, proof, out_path=dst)

    # 2) Sidecar TOUJOURS à côté du fichier source (robuste pour les tests/outils)
    _write_sidecars(file, proof, outdir=None)

    # 3) Optionnel : sidecar supplémentaire dans --outdir si demandé
    if also_json and outdir is not None:
        _write_sidecars(file, proof, outdir=outdir)


@cli.command("verify")
@click.argument("file", type=click.Path(path_type=Path, exists=True, dir_okay=False))
@click.option("--expected-issuer", type=str, required=False, help="Expected issuer.")
def cmd_verify(file: Path, expected_issuer: Optional[str]) -> None:
    """
    Verify FILE (embedded first, then sidecar). Exit code 0 on success, 1 on failure.
    """
    proof = _maybe_extract_embedded(file)
    if proof is None:
        sc = _find_sidecar_for(file)
        if sc is not None:
            proof = _read_json_file(sc)

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
    Print the MEVE proof (pure JSON on stdout).
    1) Try embedded proof (PDF/PNG)
    2) Else sidecar (multiple naming conventions)
    """
    proof = _maybe_extract_embedded(file)
    if proof is None:
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
