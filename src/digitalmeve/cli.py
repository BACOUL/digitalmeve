import argparse
import sys
from pathlib import Path
import json

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve   # ✅ correction ici
from digitalmeve.utils import pretty_print


def _cmd_generate(args: argparse.Namespace) -> int:
    src = Path(args.input)
    if not src.exists():
        print(f"error: input file {src} not found", file=sys.stderr)
        return 1

    proof = generate_meve(src)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(proof, f, indent=2)
    else:
        pretty_print(proof)

    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    proof_file = Path(args.input)
    if not proof_file.exists():
        print(f"error: proof file {proof_file} not found", file=sys.stderr)
        return 1

    with open(proof_file, "r", encoding="utf-8") as f:
        proof = json.load(f)

    ok = verify_meve(proof)   # ✅ correction ici
    if not ok:
        print("❌ Verification failed", file=sys.stderr)
        return 1

    print("✅ Verification succeeded")
    return 0


def _cmd_inspect(args: argparse.Namespace) -> int:
    proof_file = Path(args.input)
    if not proof_file.exists():
        print(f"error: proof file {proof_file} not found", file=sys.stderr)
        return 1

    with open(proof_file, "r", encoding="utf-8") as f:
        proof = json.load(f)

    pretty_print(proof)
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="command", required=True)

    p_gen = sub.add_parser("generate", help="Generate proof from input")
    p_gen.add_argument("input", help="Input file")
    p_gen.add_argument("-o", "--output", help="Output file (JSON proof)")
    p_gen.set_defaults(func=_cmd_generate)

    p_ver = sub.add_parser("verify", help="Verify a proof file")
    p_ver.add_argument("input", help="Proof file (JSON)")
    p_ver.set_defaults(func=_cmd_verify)

    p_ins = sub.add_parser("inspect", help="Inspect a proof file")
    p_ins.add_argument("input", help="Proof file (JSON)")
    p_ins.set_defaults(func=_cmd_inspect)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
