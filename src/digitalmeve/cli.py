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
    """Parse --meta key=value items into a dict."""
    meta: Dict[str, str] = {}
    for kv in items or []:
        if "=" not in kv:
            print(
                f"[error] invalid --meta '{kv}', expected key=value",
                file=sys.stderr,
            )
            sys.exit(EXIT_ERR)
        key, val = kv.split("=", 1)
        meta[key.strip()] = val.strip()
    return meta


def _call_generate(
    file: Path,
    issuer: str,
    outdir: Path | None,
    meta: Dict[str, str] | None,
) -> Any:
    """
    Call generate_meve with backward compatibility:
    try with meta/outdir; on TypeError, retry without meta.
    """
    kwargs: Dict[str, Any] = {"file_path": file, "issuer": issuer}
    if outdir is not None:
        kwargs["outdir"] = outdir
    if meta:
        kwargs["meta"] = meta
    try:
        return generate_meve(**kwargs)  # type: ignore[arg-type]
    except TypeError:
        kwargs.pop("meta", None)
        return generate_meve(**kwargs)  # type: ignore[arg-type]


def _load_json_file(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"input not found: {path}")
    text = path.read_text(encoding="utf-8")
    return json.loads(text)


def _print_json(obj: Any) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=2))


# ------------------------- subcommands -------------------------


def _cmd_generate(args: argparse.Namespace) -> int:
    try:
        file = Path(args.file)
        outdir = Path(args.outdir) if args.outdir else None
        meta = _parse_meta(args.meta)

        result = _call_generate(
            file=file,
            issuer=args.issuer,
            outdir=outdir,
            meta=meta,
        )

        # Accept both behaviors:
        # - result is a dict (proof JSON)
        # - result is a path to a written .meve.json
        if isinstance(result, (str, Path)):
            proof_path = Path(result)
            proof = _load_json_file(proof_path)
            _print_json(proof)
        else:
            _print_json(result)
        return EXIT_OK

    except Exception as exc:  # pragma: no cover
        _print_json({"ok": False, "error": str(exc)})
        return EXIT_ERR


def _cmd_verify(args: argparse.Namespace) -> int:
    try:
        target = Path(args.input)

        # Prefer passing the loaded JSON; if verifier needs a path, fallback.
        try:
            payload = _load_json_file(target)
            res = verify_meve(  # type: ignore[arg-type]
                payload,
                expected_issuer=args.expected_issuer,
            )
        except Exception:
            res = verify_meve(  # type: ignore[arg-type]
                target,
                expected_issuer=args.expected_issuer,
            )

        ok: bool
        info: Any

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
        proof = _load_json_file(proof_path)

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


# --------------------------- argparse --------------------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="digitalmeve",
        description="DigitalMeve — generate and verify .meve proofs",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    # generate
    pg = sub.add_parser(
        "generate",
        help="Generate a .meve proof for a file",
    )
    pg.add_argument("file", help="Source document path")
    pg.add_argument(
        "--issuer",
        required=True,
        help="Issuer identity (email or domain)",
    )
    pg.add_argument(
        "--outdir",
        default=None,
        help="Output directory for <name>.meve.json",
    )
    pg.add_argument(
        "--meta",
        nargs="*",
        metavar="key=value",
        help="Optional metadata (repeatable): author=John version=1",
    )
    pg.set_defaults(func=_cmd_generate)

    # verify
    pv = sub.add_parser(
        "verify",
        help="Verify a .meve proof",
    )
    pv.add_argument("input", help="Path to .meve.json file")
    pv.add_argument(
        "--expected-issuer",
        default=None,
        help="Optional expected issuer",
    )
    pv.set_defaults(func=_cmd_verify)

    # inspect
    pi = sub.add_parser(
        "inspect",
        help="Print a human-readable summary of a .meve proof",
    )
    pi.add_argument("input", help="Path to .meve.json file")
    pi.set_defaults(func=_cmd_inspect)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
