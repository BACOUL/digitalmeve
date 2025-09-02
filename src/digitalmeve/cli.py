#!/usr/bin/env python3
"""
DigitalMeve CLI
Subcommands:
  - generate  : create a .meve proof (embedded by default)
  - verify    : verify a .meve proof (sidecar JSON or embedded)
  - inspect   : print a human-readable summary of a proof JSON

New:
  --also-json on "generate" writes an additional sidecar JSON file
  alongside the embedded certified output (e.g. file.meve.pdf AND
  file.pdf.meve.json)
"""
from __future__ import annotations

import argparse
import sys
import json
from pathlib import Path
from typing import Optional

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve


def _cmd_generate(args: argparse.Namespace) -> int:
    in_path = Path(args.file)
    if not in_path.exists():
        print(f"error: input file not found: {in_path}", file=sys.stderr)
        return 2

    result = generate_meve(
        str(in_path),
        issuer=args.issuer,
        metadata=_parse_kv_meta(args.meta),
        also_json=args.also_json,
    )

    if args.verbose:
        out_path = result.get("embedded_path")
        sidecar = result.get("sidecar_path")
        print("✅ Generated proof")
        if out_path:
            print(f" • embedded: {out_path}")
        if sidecar:
            print(f" • sidecar : {sidecar}")

    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    target = args.input
    ok, info = verify_meve(target, expected_issuer=args.expected_issuer)
    if args.json:
        print(json.dumps({"ok": ok, "info": info}, ensure_ascii=False))
    else:
        status = "✅ VALID" if ok else "❌ INVALID"
        print(status)
        if args.verbose:
            print(json.dumps(info, indent=2, ensure_ascii=False))
    return 0 if ok else 1


def _cmd_inspect(args: argparse.Namespace) -> int:
    with open(args.proof, "r", encoding="utf-8") as f:
        proof = json.load(f)
    print(json.dumps(proof, indent=2, ensure_ascii=False))
    return 0


def _parse_kv_meta(pairs: list[str] | None) -> Optional[dict]:
    if not pairs:
        return None
    meta = {}
    for item in pairs:
        if "=" not in item:
            continue
        k, v = item.split("=", 1)
        meta[k.strip()] = v.strip()
    return meta


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="digitalmeve", description="DigitalMeve CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    # generate
    gen = sub.add_parser("generate", help="Generate a .meve proof")
    gen.add_argument("file", help="Input file (e.g. contract.pdf)")
    gen.add_argument(
        "--issuer",
        help='Issuer name/email (e.g. "alice@acme.com")',
        default="Personal",
    )
    gen.add_argument(
        "--meta",
        metavar="k=v",
        nargs="*",
        help="Optional metadata pairs: --meta author=Alice project=Test",
    )
    gen.add_argument(
        "--also-json",
        action="store_true",
        help="Also write sidecar JSON proof (*.meve.json)",
    )
    gen.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    gen.set_defaults(func=_cmd_generate)

    # verify
    ver = sub.add_parser("verify", help="Verify a proof")
    ver.add_argument(
        "input",
        help="Either a *.meve.json sidecar OR an embedded certified file",
    )
    ver.add_argument("--expected-issuer", help="Optional issuer to enforce")
    ver.add_argument("--json", action="store_true", help="Print JSON result")
    ver.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    ver.set_defaults(func=_cmd_verify)

    # inspect
    ins = sub.add_parser("inspect", help="Show a summary of a proof JSON")
    ins.add_argument("proof", help="Path to *.meve.json")
    ins.set_defaults(func=_cmd_inspect)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
