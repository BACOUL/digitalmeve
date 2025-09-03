from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .generator import generate_meve
from .verifier import verify_meve
from .utils import format_identity


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # digitalmeve generate <path> <identity>
    p_gen = sub.add_parser("generate")
    p_gen.add_argument("path", type=Path)
    p_gen.add_argument("identity")

    # digitalmeve verify <path>
    p_ver = sub.add_parser("verify")
    p_ver.add_argument("path", type=Path)

    # digitalmeve inspect <proof.json>
    p_ins = sub.add_parser("inspect")
    p_ins.add_argument("proof", type=Path)

    # ✅ Fix: afficher l’aide si aucune commande
    if argv is None or len(argv) == 0:
        parser.print_help(sys.stdout)
        return 0

    args = parser.parse_args(argv)

    if args.cmd == "generate":
        identity = format_identity(args.identity)
        proof = generate_meve(args.path, identity)
        sys.stdout.write(json.dumps(proof, ensure_ascii=False))
        return 0

    if args.cmd == "verify":
        ok = verify_meve(args.path)
        sys.stdout.write("VALID\n" if ok else "INVALID\n")
        return 0 if ok else 1

    if args.cmd == "inspect":
        try:
            raw = args.proof.read_text(encoding="utf-8")
            if not raw.strip():
                data = {"error": "empty file"}
            else:
                data = json.loads(raw)
        except Exception:
            data = {"error": "invalid json"}
        sys.stdout.write(json.dumps(data, ensure_ascii=False))
        return 0

    return 1
