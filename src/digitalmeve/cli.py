from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .generator import generate_meve
from .verifier import verify_meve
from .utils import format_identity


def _dump_json(path: Path, data: dict) -> None:
    """Écrit un JSON lisible et valide en UTF-8."""
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="digitalmeve",
        description="DigitalMeve proof tool",
        add_help=True,
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # digitalmeve generate <path> [identity] --issuer --outdir
    p_gen = sub.add_parser("generate", help="Generate a .meve proof (JSON)")
    p_gen.add_argument("path", type=Path)
    # identité positionnelle optionnelle (compat)
    p_gen.add_argument("identity", nargs="?", default=None)
    p_gen.add_argument(
        "--issuer",
        help="issuer email/name (override identity)",
        default=None,
    )
    p_gen.add_argument(
        "--outdir",
        type=Path,
        help="output directory for the generated proof",
        default=None,
    )

    # digitalmeve verify <path>
    p_ver = sub.add_parser("verify", help="Verify a .meve proof (JSON file)")
    p_ver.add_argument("path", type=Path)

    # digitalmeve inspect <proof.json>
    p_ins = sub.add_parser("inspect", help="Inspect a .meve proof file")
    p_ins.add_argument("proof", type=Path)

    args = parser.parse_args(argv)

    if args.cmd == "generate":
        # identité : --issuer > identity positionnelle
        raw_identity = args.issuer if args.issuer else args.identity
        identity = format_identity(raw_identity)

        proof = generate_meve(args.path, identity)

        outdir = args.outdir if args.outdir else args.path.parent
        outdir.mkdir(parents=True, exist_ok=True)

        out_name = f"{args.path.name}.meve.json"
        out_path = outdir / out_name

        _dump_json(out_path, proof)
        # Imprime le chemin pour que les tests puissent le récupérer
        sys.stdout.write(str(out_path))
        return 0

    if args.cmd == "verify":
        ok, _ = verify_meve(args.path)
        sys.stdout.write("VALID\n" if ok else "INVALID\n")
        return 0 if ok else 1

    if args.cmd == "inspect":
        try:
            raw = args.proof.read_text(encoding="utf-8")
            data = json.loads(raw) if raw.strip() else {"error": "empty file"}
        except Exception:
            data = {"error": "invalid json"}
        sys.stdout.write(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
