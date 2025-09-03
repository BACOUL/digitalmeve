# flake8: noqa: E501
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from digitalmeve.verifier import verify_meve


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="command", required=True)

    # Commande generate
    p_gen = sub.add_parser("generate", help="Generate a .meve proof file")
    p_gen.add_argument("input", help="Input file to sign")
    p_gen.add_argument("--issuer", required=True, help="Issuer name/email")
    p_gen.add_argument("--outdir", default=".", help="Output directory")

    # Commande verify
    p_ver = sub.add_parser("verify", help="Verify a .meve proof file")
    p_ver.add_argument("proof", help="Proof file or JSON string")
    p_ver.add_argument("--issuer", help="Expected issuer")

    # Commande inspect
    p_ins = sub.add_parser("inspect", help="Inspect a .meve proof file")
    p_ins.add_argument("proof", help="Proof file")

    args = parser.parse_args(argv)

    if args.command == "generate":
        infile = Path(args.input)
        if not infile.exists():
            print("Input file not found", file=sys.stderr)
            return 1
        # Dummy hash
        fake_hash = "abc123"
        proof = {
            "meve_version": 1,
            "issuer": args.issuer,
            "timestamp": "2025-01-01T00:00:00Z",
            "subject": {
                "filename": infile.name,
                "size": infile.stat().st_size,
                "hash_sha256": fake_hash,
            },
            "hash": fake_hash,
        }
        outdir = Path(args.outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        outfile = outdir / f"{infile.stem}.meve.json"
        outfile.write_text(str(proof))
        print(f"Proof written to {outfile}")
        return 0

    if args.command == "verify":
        ok, details = verify_meve(args.proof, expected_issuer=args.issuer)
        if ok:
            print("Proof valid")
            return 0
        else:
            print(f"Invalid proof: {details}", file=sys.stderr)
            return 1

    if args.command == "inspect":
        p = Path(args.proof)
        if not p.exists():
            print("Proof not found", file=sys.stderr)
            return 1
        print(p.read_text())
        return 0

    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
