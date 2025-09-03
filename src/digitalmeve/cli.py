from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .generator import generate_meve
from .verifier import verify_meve


def _resolve_outfile(src: Path, outdir: Path | None) -> Path:
    """Construit le chemin du .meve.json en respectant --outdir si fourni."""
    base = src.name  # ex: sample.txt
    target = Path(outdir) if outdir else src.parent
    target.mkdir(parents=True, exist_ok=True)
    return (target / base).with_suffix(src.suffix + ".meve.json")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # ---- generate ----
    p_gen = sub.add_parser("generate", help="Generate a .meve proof (JSON)")
    p_gen.add_argument("file", type=Path, help="Input file to certify")
    p_gen.add_argument("--issuer", type=str, default=None, help="Issuer identity (e.g. email)")
    p_gen.add_argument("--outdir", type=Path, default=None, help="Output directory for the .meve.json")

    # ---- verify ----
    p_ver = sub.add_parser("verify", help="Verify a .meve proof")
    p_ver.add_argument("proof", type=Path, help="Path to *.meve.json")
    p_ver.add_argument("--expected-issuer", type=str, default=None, help="Optional expected issuer")

    # ---- inspect ----
    p_ins = sub.add_parser("inspect", help="Print a .meve proof (raw JSON)")
    p_ins.add_argument("proof", type=Path, help="Path to *.meve.json")

    args = parser.parse_args(argv)

    if args.cmd == "generate":
        proof = generate_meve(args.file, issuer=args.issuer)
        outfile = _resolve_outfile(args.file, args.outdir)
        outfile.write_text(json.dumps(proof, ensure_ascii=False, indent=2))
        # Le test lit le chemin depuis stdout
        print(outfile)
        return 0

    if args.cmd == "verify":
        ok, _info = verify_meve(args.proof, expected_issuer=args.expected_issuer)
        print("OK" if ok else "FAIL")
        return 0 if ok else 1

    if args.cmd == "inspect":
        # IMPORTANT : renvoyer exactement le JSON du fichier, sans ajout
        sys.stdout.write(args.proof.read_text(encoding="utf-8"))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
