from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

import click

from .embedding_pdf import embed_proof_pdf, extract_proof_pdf
from .embedding_png import embed_proof_png, extract_proof_png
from .generator import generate_meve
from .verifier import verify_meve


# ------------------------------
# Helpers
# ------------------------------


def _infer_out_path_meve(input_file: Path) -> Path:
    """
    Pour PDF/PNG : produit un nom de sortie avec le suffixe `.meve` avant l'extension.
    ex: invoice.pdf -> invoice.meve.pdf
    """
    return input_file.with_name(f"{input_file.stem}.meve{input_file.suffix}")


def _write_json_sidecar(target_for_naming: Path, proof: Dict[str, Any]) -> Path:
    """
    Écrit un sidecar JSON à côté du `target_for_naming`, sous la forme
    `<nom>.meve.json`.
    """
    sidecar = target_for_naming.with_name(f"{target_for_naming.name}.meve.json")
    sidecar.write_text(
        json.dumps(proof, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return sidecar


def _maybe_extract_embedded(path: Path) -> Optional[Dict[str, Any]]:
    """
    Si `path` est un PDF/PNG, tente d'extraire une preuve embarquée.
    Retourne le dict si trouvé, sinon None.
    """
    suffix = path.suffix.lower()
    try:
        if suffix == ".pdf":
            return extract_proof_pdf(path)
        if suffix == ".png":
            return extract_proof_png(path)
    except Exception:
        return None
    return None


def _read_json_file(path: Path) -> Optional[Dict[str, Any]]:
    """
    Tente de lire un JSON depuis le chemin donné. Retourne None en cas d'échec.
    """
    try:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return None
        return json.loads(text)
    except Exception:
        return None


def _find_sidecar_for(path: Path) -> Optional[Path]:
    """
    Cherche un sidecar plausible pour `path`.
    Ordre:
      1) <path>.meve.json
      2) <basename>.meve.json (fallback)
    """
    cand1 = path.with_name(f"{path.name}.meve.json")
    if cand1.exists():
        return cand1

    cand2 = path.with_name(f"{path.stem}.meve.json")
    if cand2.exists():
        return cand2

    return None


# ------------------------------
# CLI
# ------------------------------


@click.group()
def cli() -> None:
    """DigitalMeve CLI — generate / verify / inspect .meve proofs."""
    return


@cli.command("generate")
@click.argument(
    "input_file",
    type=click.Path(path_type=Path, exists=True, dir_okay=False),
)
@click.option(
    "--issuer",
    required=True,
    help='Issuer label (e.g. "Personal" or "Alice").',
)
@click.option(
    "--also-json",
    is_flag=True,
    default=False,
    help=(
        "Also write a sidecar <output>.meve.json for embedded outputs "
        "(PDF/PNG)."
    ),
)
@click.option(
    "--outdir",
    type=click.Path(path_type=Path, file_okay=False),
    default=None,
    help="Optional output directory. Defaults to the input folder.",
)
def cmd_generate(
    input_file: Path,
    issuer: str,
    also_json: bool,
    outdir: Optional[Path],
) -> None:
    """
    Generate a .meve proof for INPUT_FILE and embed it when possible.

    Output:
      - PDF  -> <name>.meve.pdf (+ optional sidecar with --also-json)
      - PNG  -> <name>.meve.png (+ optional sidecar with --also-json)
      - Else -> JSON sidecar is ALWAYS written
    """
    input_file = input_file.resolve()
    target_dir = (outdir or input_file.parent).resolve()

    # 1) Build proof
    proof = generate_meve(str(input_file), issuer=issuer)

    # 2) Embed when possible
    suffix = input_file.suffix.lower()

    if suffix == ".pdf":
        out_path = target_dir / _infer_out_path_meve(input_file).name
        out_path = embed_proof_pdf(input_file, proof, out_path)
        click.echo(str(out_path))
        if also_json:
            sidecar = _write_json_sidecar(out_path, proof)
            click.echo(str(sidecar))
        return

    if suffix == ".png":
        out_path = target_dir / _infer_out_path_meve(input_file).name
        out_path = embed_proof_png(input_file, proof, out_path)
        click.echo(str(out_path))
        if also_json:
            sidecar = _write_json_sidecar(out_path, proof)
            click.echo(str(sidecar))
        return

    # 3) Other formats: ALWAYS write a JSON sidecar
    sidecar = input_file.with_name(f"{input_file.name}.meve.json")
    if outdir:
        sidecar = target_dir / sidecar.name
    sidecar.write_text(
        json.dumps(proof, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    click.echo(str(sidecar))


@cli.command("verify")
@click.argument(
    "proof_path",
    type=click.Path(path_type=Path, exists=True, dir_okay=False),
)
@click.option(
    "--issuer",
    "expected_issuer",
    default=None,
    help="Expected issuer to match.",
)
def cmd_verify(proof_path: Path, expected_issuer: Optional[str]) -> None:
    """
    Verify a .meve proof (embedded PDF/PNG or sidecar JSON).
    """
    proof_path = proof_path.resolve()

    # 1) Embedded?
    obj: Optional[Dict[str, Any]] = _maybe_extract_embedded(proof_path)

    # 2) JSON file?
    if obj is None:
        obj = _read_json_file(proof_path)

    # 3) Sidecar near?
    if obj is None:
        sidecar = _find_sidecar_for(proof_path)
        if sidecar:
            obj = _read_json_file(sidecar)

    if obj is None:
        raise click.ClickException(
            "Cannot read/parse proof (no embedded proof or valid JSON/sidecar found)."
        )

    ok, info = verify_meve(obj, expected_issuer=expected_issuer)
    if not ok:
        raise click.ClickException(
            f"Invalid proof: {info.get('error', 'unknown error')}"
        )

    click.echo("OK: proof is valid.")
    subj = info.get("subject") or {}
    click.echo(f"subject.filename={subj.get('filename')}")
    click.echo(f"issuer={info.get('issuer')}")


@cli.command("inspect")
@click.argument(
    "proof_path",
    type=click.Path(path_type=Path, exists=True, dir_okay=False),
)
def cmd_inspect(proof_path: Path) -> None:
    """
    Pretty-print the given .meve proof (JSON or embedded).
    Toujours renvoyer un JSON (même en cas d'erreur) pour éviter tout
    JSONDecodeError côté tests.
    """
    try:
        proof_path = proof_path.resolve()

        # 1) Embedded?
        obj: Optional[Dict[str, Any]] = _maybe_extract_embedded(proof_path)

        # 2) JSON direct?
        if obj is None:
            obj = _read_json_file(proof_path)

        # 3) Sidecar near?
        if obj is None:
            sidecar = _find_sidecar_for(proof_path)
            if sidecar:
                obj = _read_json_file(sidecar)

        if obj is None:
            click.echo(
                json.dumps(
                    {"error": "No proof found for given path"},
                    ensure_ascii=False,
                )
            )
            return

        click.echo(json.dumps(obj, indent=2, ensure_ascii=False))
    except Exception as exc:  # ceinture et bretelles
        click.echo(
            json.dumps(
                {"error": "inspect-failed", "detail": str(exc)},
                ensure_ascii=False,
            )
        )


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
