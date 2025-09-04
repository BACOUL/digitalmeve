from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from .generator import generate_meve
from .verifier import verify_meve


# -------- utils -----------------------------------------------------------

def _read_text_from_optional_file(path_arg: Optional[str]) -> str:
    """
    Si path_arg est None ou '-', lit depuis stdin.
    Sinon lit le fichier en UTF-8 et retourne le contenu.
    """
    if path_arg in (None, "-"):
        return sys.stdin.read()
    p = Path(path_arg)
    return p.read_text(encoding="utf-8")


# -------- commandes -------------------------------------------------------

def cmd_generate(args: argparse.Namespace) -> int:
    """
    Génère une preuve MEVE sur stdout.
    Écrit éventuellement un sidecar JSON si --outdir est fourni.
    """
    try:
        proof = generate_meve(
            file_path=args.file,
            outdir=args.outdir,
            issuer=args.issuer,
            metadata=None,
            also_json=args.also_json,
        )
    except Exception as e:  # pragma: no cover
        sys.stderr.write(f"{e}\n")
        return 1

    print(json.dumps(proof, ensure_ascii=False, indent=2))
    return 0


def cmd_inspect(args: argparse.Namespace) -> int:
    """
    Lit un JSON (fichier ou stdin) et l’affiche enrichi avec :
    - issuer (copié)
    - hash_prefix (les 12 premiers caractères de 'hash')
    - level = "file"
    """
    text = _read_text_from_optional_file(args.file)
    try:
        obj = json.loads(text)
    except Exception as e:
        sys.stderr.write(f"Invalid input JSON: {e}\n")
        return 1

    out = dict(obj)
    h = str(obj.get("hash", ""))
    out["issuer"] = obj.get("issuer")
    out["hash_prefix"] = h[:12]
    out["level"] = "file"

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    """
    Vérifie une preuve MEVE. Retourne 0 si OK, 1 sinon.
    """
    text = _read_text_from_optional_file(args.file)
    try:
        obj = json.loads(text)
    except Exception as e:
        sys.stderr.write(f"Invalid input JSON: {e}\n")
        return 1

    ok, _detail = verify_meve(obj, expected_issuer=args.expected_issuer)
    return 0 if ok else 1


# -------- parser / main ---------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="command", metavar="{generate,inspect,verify}")
    sub.required = True

    # generate
    p_gen = sub.add_parser("generate", help="Create a .meve proof")
    p_gen.add_argument("file", help="Input file to prove")
    p_gen.add_argument(
        "--outdir",
        default=None,
        help="Write sidecar JSON in this directory (optional).",
    )
    p_gen.add_argument(
        "--issuer",
        default="Personal",
        help="Issuer name/email for the proof (default: Personal).",
    )
    p_gen.add_argument(
        "--also-json",
        action="store_true",
        help="Also write <file>.meve.json next to the file when no --outdir.",
    )
    p_gen.set_defaults(func=cmd_generate)

    # inspect
    p_ins = sub.add_parser("inspect", help="Inspect a .meve JSON")
    p_ins.add_argument(
        "file",
        nargs="?",
        help="Path to JSON or '-' for stdin (default: stdin).",
    )
    p_ins.set_defaults(func=cmd_inspect)

    # verify
    p_ver = sub.add_parser("verify", help="Verify a .meve proof")
    p_ver.add_argument(
        "file",
        nargs="?",
        help="Path to JSON or '-' for stdin (default: stdin).",
    )
    p_ver.add_argument(
        "--issuer",
        dest="expected_issuer",
        default=None,
        help="Expected issuer to match (optional).",
    )
    p_ver.set_defaults(func=cmd_verify)

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
