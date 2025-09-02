#!/usr/bin/env python3
"""
DigitalMeve CLI

Subcommands:
  - generate  : create a .meve proof (embedded by default)
  - verify    : verify a .meve proof (sidecar JSON or embedded)
  - inspect   : print a human-readable summary of a proof JSON

New:
  --also-json on "generate" writes an additional sidecar JSON file
  alongside the embedded certified output (e.g. file.meve.pdf AND file.pdf.meve.json)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve
from digitalmeve.utils import load_json, pretty_print  # if you don't have these, remove & inline


def _cmd_generate(args: argparse.Namespace) -> int:
    in_path = Path(args.file)
    if not in_path.exists():
        print(f"error: input file not found: {in_path}", file=sys.stderr)
        return 2

    # Generate proof; embedded output path is returned by generator.
    result = generate_meve(
        str(in_path),
        issuer=args.issuer,
        metadata=_parse_kv_meta(args.meta),
        also_json=args.also_json,  # <- NEW
    )

    # Be quiet to preserve existing tests unless verbose requested.
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
    # Keep output minimal to avoid breaking existing tests
    if args.json:
        import json

        print(json.dumps({"ok": ok, "info": info}, ensure_ascii=False))
    else:
        status = "✅ VALID" if ok else "❌ INVALID"
        print(status)
        if args.verbose:
            pretty_print(info) if "pretty_print" in globals() else print(info)
    return 0 if ok else 1


def _cmd_inspect(args: argparse.Namespace) -> int:
    # Inspect expects a JSON proof path and prints a human readable summary
    proof = load_json(args.proof) if "load_json" in globals() else _load_json_fallback(args.proof)
    # Keep the keys expected by tests (issued_at, issuer, meve_version, hash, metadata…)
    pretty_print(proof) if "pretty_print" in globals() else print(proof)
    return 0


def _load_json_fallback(path: str):
    import json

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


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
    gen = sub.add_parser("generate", help="Generate a .meve proof (embedded by default)")
    gen.add_argument("file", help="Input file (e.g. contract.pdf)")
    gen.add_argument("--issuer", help='Issuer name/email (e.g. "alice@acme.com")', default="Personal")
    gen.add_argument(
        "--meta",
        metavar="k=v",
        nargs="*",
        help="Optional metadata pairs (repeatable): --meta author=Alice project=Test",
    )
    gen.add_argument(
        "--also-json",
        action="store_true",
        help="Also write sidecar JSON proof (*.meve.json) in addition to embedded output",
    )
    gen.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    gen.set_defaults(func=_cmd_generate)

    # verify
    ver = sub.add_parser("verify", help="Verify a proof (sidecar JSON or embedded file)")
    ver.add_argument(
        "input",
        help="Either a *.meve.json sidecar OR an embedded certified file (e.g. file.meve.pdf)",
    )
    ver.add_argument("--expected-issuer", help="Optional issuer to enforce")
    ver.add_argument("--json", action="store_true", help="Print JSON result")
    ver.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    ver.set_defaults(func=_cmd_verify)

    # inspect
    ins = sub.add_parser("inspect", help="Show a human-readable summary of a proof JSON")
    ins.add_argument("proof", help="Path to *.meve.json")
    ins.set_defaults(func=_cmd_inspect)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
