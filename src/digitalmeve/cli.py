import sys
import argparse
import json
from pathlib import Path

from digitalmeve.generator import generate_proof
from digitalmeve.verifier import verify_proof
from digitalmeve.utils import _write_json_file, pretty_print


def _cmd_generate(args: argparse.Namespace) -> int:
    src = Path(args.input)
    if not src.exists():
        print(f"error: input file {src} not found", file=sys.stderr)
        return 1

    proof = generate_proof(src)

    # si --outdir est donné, le proof.json va là-bas
    if args.outdir:
        outdir = Path(args.outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        sidecar = outdir / f"{src.name}.meve.json"
    else:
        sidecar = Path(f"{src}.meve.json")

    # rendre le chemin ABSOLU
    sidecar = sidecar.resolve()

    try:
        _write_json_file(sidecar, proof)
    except Exception as e:
        print(f"error: cannot write proof: {e}", file=sys.stderr)
        return 2

    # imprime le chemin absolu (lu par les tests)
    print(str(sidecar))
    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    src = Path(args.input)
    sidecar = Path(f"{src}.meve.json")

    if not sidecar.exists():
        print(f"error: proof file {sidecar} not found", file=sys.stderr)
        return 1

    try:
        with open(sidecar, "r", encoding="utf-8") as f:
            proof = json.load(f)
    except Exception as e:
        print(f"error: cannot read proof: {e}", file=sys.stderr)
        return 2

    valid = verify_proof(src, proof)
    if not valid:
        print("INVALID")
        return 3

    print("VALID")
    return 0


def _cmd_inspect(args: argparse.Namespace) -> int:
    sidecar = Path(args.input)

    if not sidecar.exists():
        print(f"error: proof file {sidecar} not found", file=sys.stderr)
        return 1

    try:
        with open(sidecar, "r", encoding="utf-8") as f:
            proof = json.load(f)
    except Exception as e:
        print(f"error: cannot read proof: {e}", file=sys.stderr)
        return 2

    pretty_print(proof)
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="command")

    g = sub.add_parser("generate")
    g.add_argument("input", help="input file")
    g.add_argument("--outdir", help="output directory")
    g.set_defaults(func=_cmd_generate)

    v = sub.add_parser("verify")
    v.add_argument("input", help="input file")
    v.set_defaults(func=_cmd_verify)

    i = sub.add_parser("inspect")
    i.add_argument("input", help="proof file (.meve.json)")
    i.set_defaults(func=_cmd_inspect)

    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
