#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DigitalMeve CLI (MVP)
Commands:
  - generate <file> [--issuer "Alice"] [--outdir DIR]
  - verify <proof.json> [--expected-issuer "Alice"]
  - inspect <proof.json>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


# ---------- utils ----------

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )


def _sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_json_file(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"proof file not found: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"proof file is empty: {path}")
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"invalid JSON in {path}: {e}") from e


def _write_json_file(path: Path, data: Dict[str, Any]) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


# ---------- core ----------

def _build_proof_for_file(src: Path, issuer: str) -> Dict[str, Any]:
    return {
        "meve_version": "1.0",
        "issued_at": _now_iso(),
        "issuer": issuer,
        "hash": _sha256_of_file(src),
        "metadata": {},
    }


def _cmd_generate(args: argparse.Namespace) -> int:
    src = Path(args.file)
    if not src.exists():
        print(f"error: input file not found: {src}", file=sys.stderr)
        return 2

    issuer = args.issuer or "test@example.com"
    proof = _build_proof_for_file(src, issuer)

    # si --outdir est donné, le proof.json va là-bas
    if args.outdir:
        outdir = Path(args.outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        sidecar = outdir / f"{src.name}.meve.json"
    else:
        sidecar = Path(f"{src}.meve.json")

    try:
        _write_json_file(sidecar, proof)
    except Exception as e:
        print(f"error: cannot write proof: {e}", file=sys.stderr)
        return 2

    print(str(sidecar))
    return 0


def _cmd_inspect(args: argparse.Namespace) -> int:
    path = Path(args.proof)
    try:
        proof = _read_json_file(path)
    except (FileNotFoundError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    print(json.dumps(proof, indent=2, ensure_ascii=False))
    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    path = Path(args.proof)
    try:
        proof = _read_json_file(path)
    except (FileNotFoundError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    required = ["meve_version", "issued_at", "issuer", "hash"]
    missing = [k for k in required if k not in proof]
    if missing:
        print(f"invalid proof: missing fields: {', '.join(missing)}", file=sys.stderr)
        return 1

    if args.expected_issuer and proof.get("issuer") != args.expected_issuer:
        print(
            "invalid proof: issuer mismatch "
            f"(expected {args.expected_issuer}, got {proof.get('issuer')})",
            file=sys.stderr,
        )
        return 1

    sib = _guess_sibling_file(path)
    if sib and sib.exists():
        actual = _sha256_of_file(sib)
        if actual != proof.get("hash"):
            print("invalid proof: hash mismatch", file=sys.stderr)
            return 1

    print("OK")
    return 0


def _guess_sibling_file(proof_path: Path) -> Path | None:
    name = proof_path.name
    if name.endswith(".meve.json"):
        sibling = name[: -len(".meve.json")]
        return proof_path.with_name(sibling)
    return None


# ---------- argparse ----------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="digitalmeve", add_help=True)
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate", help="generate a .meve.json proof")
    g.add_argument("file", help="path to the input file")
    g.add_argument("--issuer", default=None, help="issuer name, e.g. 'Alice'")
    g.add_argument("--outdir", default=None, help="directory to save proof file")
    g.set_defaults(func=_cmd_generate)

    v = sub.add_parser("verify", help="verify a .meve.json proof")
    v.add_argument("proof", help="path to the proof JSON")
    v.add_argument(
        "--expected-issuer",
        default=None,
        help="optional issuer to enforce",
    )
    v.set_defaults(func=_cmd_verify)

    i = sub.add_parser("inspect", help="pretty-print a proof JSON")
    i.add_argument("proof", help="path to the proof JSON")
    i.set_defaults(func=_cmd_inspect)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
