from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .generator import generate_proof
from .verifier import verify_meve


def _read_stdin_text() -> str:
    try:
        return sys.stdin.read()
    except Exception as e:
        sys.stderr.write(f"stdin read error: {e}\n")
        sys.exit(1)


def cmd_generate(args: argparse.Namespace) -> int:
    metadata = None
    if args.metadata:
        try:
            metadata = json.loads(args.metadata)
        except Exception:
            sys.stderr.write("Invalid JSON in --metadata\n")
            return 1

    proof = generate_proof(
        args.file,
        outdir=args.outdir,
        issuer=args.issuer,
        metadata=metadata,
    )
    # Sortie JSON **valide** sur stdout (compacte)
    print(json.dumps(proof, ensure_ascii=False))
    return 0


def cmd_inspect(_: argparse.Namespace) -> int:
    try:
        text = _read_stdin_text()
        obj = json.loads(text)
    except Exception as e:
        sys.stderr.write(f"Invalid input JSON: {e}\n")
        return 1

    print(json.dumps(obj, ensure_ascii=False, indent=2))
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    # Si --file est fourni on lit le fichier, sinon on lit stdin
    if args.file:
        try:
            data = Path(args.file).read_text(encoding="utf-8")
        except Exception as e:
            sys.stderr.write(f"Cannot read file: {e}\n")
            return 1
    else:
        data = _read_stdin_text()

    try:
        obj = json.loads(data)
    except Exception as e:
        sys.stderr.write(f"Invalid input JSON: {e}\n")
        return 1

    ok, info = verify_meve(obj, expected_issuer=args.issuer)
    print(json.dumps({"valid": ok, "info": info}, ensure_ascii=False, indent=2))
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # generate
    p_gen = sub.add_parser("generate", help="Generate a MEVE proof")
    p_gen.add_argument("file", help="File to generate proof for")
    p_gen.add_argument("--issuer", default="Personal")
    p_gen.add_argument("--outdir", help="Optional output directory")
    p_gen.add_argument(
        "--metadata",
        help="Optional metadata as JSON string",
    )
    p_gen.set_defaults(func=cmd_generate)

    # inspect
    p_ins = sub.add_parser(
        "inspect",
        help="Read proof JSON from stdin and pretty-print",
    )
    p_ins.set_defaults(func=cmd_inspect)

    # verify (facultatif mais utile)
    p_ver = sub.add_parser(
        "verify",
        help="Verify proof from --file or stdin",
    )
    p_ver.add_argument("--file", help="Proof file (.json). If absent, use stdin")
    p_ver.add_argument("--issuer", help="Expected issuer")
    p_ver.set_defaults(func=cmd_verify)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    rc = args.func(args)
    sys.exit(rc)


if __name__ == "__main__":
    main()
