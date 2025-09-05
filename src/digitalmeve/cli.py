# src/digitalmeve/cli.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import click

from .generator import generate_meve
from .verifier import verify_meve
from .embedding_pdf import embed_proof_pdf, extract_proof_pdf
from .embedding_png import embed_proof_png, extract_proof_png


# ----------------------------
# Helpers
# ----------------------------
def _infer_out_path_meve(input_path: Path) -> Path:
    """Return <stem>.meve.<suffix> (e.g. invoice.pdf -> invoice.meve.pdf)."""
    return input_path.with_name(f"{input_path.stem}.meve{input_path.suffix}")


def _write_json_sidecar(for_path: Path, proof: Dict[str, Any]) -> Path:
    """Write <filename>.meve.json next to the file."""
    sidecar = for_path.with_name(f"{for_path.name}.meve.json")
    sidecar.write_text(json.dumps(proof, indent=2, ensure_ascii=False), encoding="utf-8")
    return sidecar


def _load_and_maybe_extract(path: Path) -> Dict[str, Any]:
    """
    Load a proof:
      - If *.meve.json -> load JSON
      - If *.pdf/*.png (with embedded proof) -> extract
      - Else -> try to read text -> json
    """
    suffix = path.suffix.lower()
    if suffix == ".json":
        return json.loads(path.read_text(encoding="utf-8"))

    if suffix == ".pdf":
        proof = extract_proof_pdf(path)
        if proof is None:
            raise click.ClickException("No embedded proof found in PDF.")
        return proof

    if suffix == ".png":
        proof = extract_proof_png(path)
        if proof is None:
            raise click.ClickException("No embedded proof found in PNG.")
        return proof

    # Fallback: try JSON from file
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise click.ClickException(f"Unsupported input for verify/inspect: {path}") from exc


# ----------------------------
# CLI
# ----------------------------
@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    """DigitalMeve — .MEVE generator & verifier (CLI)."""
    pass


@cli.command("generate")
@click.argument("input_file", type=click.Path(path_type=Path, exists=True, dir_okay=False))
@click.option("--issuer", required=True, help='Issuer label (e.g. "Personal" or "Alice").')
@click.option(
    "--also-json",
    is_flag=True,
    default=False,
    help="Also write a sidecar <output>.meve.json next to the generated file.",
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
      - For others -> only JSON sidecar if --also-json is provided
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

    # 3) Other formats: only JSON sidecar (when requested)
    if also_json:
        # Sidecar named from original file (not *.meve.ext because no embedding)
        sidecar = input_file.with_name(f"{input_file.name}.meve.json")
        if outdir:
            sidecar = (Path(outdir).resolve() / sidecar.name)
        sidecar.write_text(json.dumps(proof, indent=2, ensure_ascii=False), encoding="utf-8")
        click.echo(f"Wrote sidecar → {sidecar}")
    else:
        raise click.ClickException(
            "Embedding supported only for PDF/PNG. Use --also-json to write a sidecar for other formats."
        )


@cli.command("verify")
@click.argument("proof_path", type=click.Path(path_type=Path, exists=True, dir_okay=False))
@click.option(
    "--expected-issuer",
    default=None,
    help='Optional expected issuer to enforce (e.g. "Alice").',
)
def cmd_verify(proof_path: Path, expected_issuer: Optional[str]) -> None:
    """
    Verify a proof from:
      - *.meve.json (sidecar)
      - *.pdf/*.png with embedded proof
      - or a JSON file containing the proof
    """
    proof_path = proof_path.resolve()
    proof = _load_and_maybe_extract(proof_path)

    ok, info = verify_meve(proof, expected_issuer=expected_issuer)
    if not ok:
        click.echo(json.dumps({"ok": False, **info}, ensure_ascii=False))
        raise SystemExit(1)

    click.echo(json.dumps({"ok": True, "proof": info}, ensure_ascii=False))


@cli.command("inspect")
@click.argument("proof_path", type=click.Path(path_type=Path, exists=True, dir_okay=False))
def cmd_inspect(proof_path: Path) -> None:
    """
    Human-friendly summary of a proof (works with *.meve.json or embedded PDF/PNG).
    """
    proof_path = proof_path.resolve()
    proof = _load_and_maybe_extract(proof_path)

    issuer = proof.get("issuer")
    status = proof.get("status")
    certified = proof.get("certified")
    issued_at = proof.get("issued_at") or proof.get("timestamp")
    subject = proof.get("subject") or {}
    filename = subject.get("filename")
    size = subject.get("size")
    hash_sha256 = subject.get("hash_sha256")

    summary = {
        "issuer": issuer,
        "status": status,
        "certified": certified,
        "issued_at": issued_at,
        "subject": {
            "filename": filename,
            "size": size,
            "hash_sha256": hash_sha256,
        },
    }
    click.echo(json.dumps(summary, indent=2, ensure_ascii=False))


# ----------------------------
# Entry point
# ----------------------------
def main() -> None:  # pragma: no cover
    cli()


if __name__ == "__main__":  # pragma: no cover
    main()
