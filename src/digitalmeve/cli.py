# src/digitalmeve/cli.py
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .generator import generate_meve
from .verifier import verify_meve


def _cmd_generate(args: argparse.Namespace) -> int:
    try:
        proof = generate_meve(
            file_path=Path(args.file),
            outdir=Path(args.outdir) if args.outdir else None,
            issuer=args.issuer,
        )
    except Exception as exc:  # pragma: no cover
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(proof, ensure_ascii=False, indent=2))
    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    target = Path(args.input)
    try:
        ok, info = verify_meve(target, expected_issuer=args.expected_issuer)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1

    print(json.dumps({"ok": ok, "info": info}, ensure_ascii=False, indent=2))
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="digitalmeve",
        description="DigitalMeve — générer et vérifier des preuves .meve",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    pg = sub.add_parser("generate", help="Générer une preuve .meve pour un fichier")
    pg.add_argument("file", help="Fichier source")
    pg.add_argument("--issuer", default="Personal", help="Nom de l’émetteur")
    pg.add_argument(
        "--outdir",
        default=None,
        help="Dossier de sortie pour écrire <nom>.meve.json (optionnel)",
    )
    pg.set_defaults(func=_cmd_generate)

    pv = sub.add_parser("verify", help="Vérifier une preuve .meve")
    pv.add_argument("input", help="Fichier .meve.json (ou JSON lisible)")
    pv.add_argument("--expected-issuer", default=None, help="Émetteur attendu")
    pv.set_defaults(func=_cmd_verify)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


# Wrappers pratiques pour des commandes séparées
def main_generate() -> int:  # pragma: no cover
    parser = build_parser()
    args = parser.parse_args(["generate", *sys.argv[1:]])
    return _cmd_generate(args)


def main_verify() -> int:  # pragma: no cover
    parser = build_parser()
    args = parser.parse_args(["verify", *sys.argv[1:]])
    return _cmd_verify(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
