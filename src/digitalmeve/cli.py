# src/digitalmeve/cli.py
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

from .generator import generate_meve
from .verifier import verify_meve

EXIT_OK = 0
EXIT_ERR = 1


def _parse_meta(items: list[str] | None) -> Dict[str, str]:
    meta: Dict[str, str] = {}
    for kv in items or []:
        if "=" not in kv:
            print(f"[error] invalid --meta '{kv}', expected key=value", file=sys.stderr)
            sys.exit(EXIT_ERR)
        k, v = kv.split("=", 1)
        meta[k.strip()] = v.strip()
    return meta


def _call_generate(file: Path, issuer: str, outdir: Path | None, meta: Dict[str, str] | None) -> Any:
    """Call generate_meve in a backward-compatible way (meta optional)."""
    kwargs: Dict[str, Any] = {"file_path": file, "issuer": issuer}
    if outdir is not None:
        kwargs["outdir"] = outdir
    if meta:
        kwargs["meta"] = meta
    try:
        return generate_meve(**kwargs)  # type: ignore[arg-type]
    except TypeError:
        # Fallback if older generate_meve doesn't support meta/outdir keywords
        kwargs.pop("meta", None)
        return generate_meve(**kwargs)  # type: ignore[arg-type]


def _load_proof_from_path_or_json_file(p: Path) -> Dict[str, Any]:
    if not p.exists():
        raise FileNotFoundError(f"input not found: {p}")
    # Always treat as JSON file on disk
    text = p.read_text(encoding="utf-8")
    return json.loads(text)


def _print_json(obj: Any) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=2))


def _cmd_generate(args: argparse.Namespace) -> int:
    try:
        file = Path(args.file)
        outdir = Path(args.outdir) if args.outdir else None
        meta = _parse_meta(args.meta)
        res = _call_generate(file=file, issuer=args.issuer, outdir=outdir, meta=meta)
        # Accept both behaviors:
        # - res is a dict (proof JSON) -> print it
        # - res is a path to a written .meve.json -> load & print the JSON
        if isinstance(res, (str, Path)):
            proof_path = Path(res)
            proof = json.loads(proof_path.read_text(encoding="utf-8"))
            _print_json(proof)
        else:
            _print_json(res)
        return EXIT_OK
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return EXIT_ERR


def _cmd_verify(args: argparse.Namespace) -> int:
    try:
        target = Path(args.input)
        # Load file JSON and pass to verify_meve (or path if your verifier expects a path)
        try:
            payload = _load_proof_from_path_or_json_file(target)
            res = verify_meve(payload, expected_issuer=args.expected_issuer)  # type: ignore[arg-type]
        except Exception:
            # Fall back: pass the path directly (if your verifier expects a path)
            res = verify_meve(target, expected_issuer=args.expected_issuer)  # type: ignore[arg-type]

        # res may be a tuple (ok, info) or dict-like
        ok = None
        info = None
        if isinstance(res, tuple) and len(res) == 2:
            ok, info = bool(res[0]), res[1]
        elif isinstance(res, dict):
            ok = bool(res.get("ok") or res.get("valid") or res.get("success"))
            info = res
        else:
            ok = True
            info = res

        _print_json({"ok": bool(ok), "info": info})
        return EXIT_OK if ok else EXIT_ERR
    except Exception as exc:  # pragma: no cover
        _print_json({"ok": False, "error": str(exc)})
        return EXIT_ERR


def _cmd_inspect(args: argparse.Namespace) -> int:
    try:
        proof_path = Path(args.input)
        proof = _load_proof_from_path_or_json_file(proof_path)
        # Normalize common fields
        status = proof.get("status") or proof.get("Status")
        issuer = proof.get("issuer") or proof.get("Issuer")
        issued_at = proof.get("issued_at") or proof.get("Issued_at")
        h = (proof.get("hash_sha256") or proof.get("Hash-SHA256") or "")[:16]
        meta = proof.get("meta") or {}
        name = meta.get("name") or meta.get("filename") or ""
        size = meta.get("size") or meta.get("length") or ""
        mime = meta.get("mime") or meta.get("content_type") or ""

        summary = {
            "file": proof_path.name,
            "level": status,
            "issuer": issuer,
            "issued_at": issued_at,
            "hash_prefix": f"{h}…",
            "doc": {"name": name, "size": size, "mime": mime},
        }
        _print_json(summary)
        return EXIT_OK
    except Exception as exc:  # pragma: no cover
        _print_json({"ok": False, "error": str(exc)})
        return EXIT_ERR


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="digitalmeve",
        description="DigitalMeve — generate and verify .meve proofs",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    # generate
    pg = sub.add_parser("generate", help="Generate a .meve proof for a file")
    pg.add_argument("file", help="Source document path")
    pg.add_argument("--issuer", required=True, help="Issuer identity (email or domain)")
    pg.add_argument("--outdir", default=None, help="Output directory for <name>.meve.json")
    pg.add_argument(
        "--meta",
        nargs="*",
        metavar="key=value",
        help="Optional metadata (repeatable): author=John version=1",
    )
    pg.set_defaults(func=_cmd_generate)

    # verify
    pv = sub.add_parser("verify", help="Verify a .meve proof")
    pv.add_argument("input", help="Path to .meve.json file")
    pv.add_argument("--expected-issuer", default=None, help="Optional expected issuer")
    pv.set_defaults(func=_cmd_verify)

    # inspect
    pi = sub.add_parser("inspect", help="Print a human-readable summary of a .meve proof")
    pi.add_argument("input", help="Path to .meve.json file")
    pi.set_defaults(func=_cmd_inspect)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
