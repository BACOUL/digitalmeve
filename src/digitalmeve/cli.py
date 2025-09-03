from __future__ import annotations

import argparse
import sys
import json  # ✅ ajouté
from pathlib import Path

from .generator import generate_proof
from .verifier import verify_meve


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # ---- generate ----
    p_gen = sub.add_parser("generate")
    p_gen.add_argument("file", type=Path)

    # ---- verify ----
    p_ver = sub.add_parser("verify")
    p_ver.add_argument("proof", type=Path)

    # ---- inspect ----
    p_ins = sub.add_parser("inspect")
    p_ins.add_argument("proof", type=Path)

    args = parser.parse_args(argv)

    if args.cmd == "generate":
        proof = generate_proof(args.file)
        outfile = args.file.with_suffix(args.file.suffix + ".meve.json")
        outfile.write_text(json.dumps(proof, indent=2))  # ✅ JSON valide
        print(outfile)
        return 0

    if args.cmd == "verify":
        ok, _ = verify_meve(args.proof)
        print("OK" if ok else "FAIL")
        return 0 if ok else 1

    if args.cmd == "inspect":
        text = args.proof.read_text(encoding="utf-8")
        print(text)
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
