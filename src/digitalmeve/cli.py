# src/digitalmeve/cli.py
import argparse
from pathlib import Path

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_proof
from digitalmeve.utils import pretty_print


def main():
    parser = argparse.ArgumentParser(prog="digitalmeve")
    sub = parser.add_subparsers(dest="command", required=True)

    # ---- generate ----
    p_gen = sub.add_parser("generate", help="Génère une preuve MEVE")
    p_gen.add_argument("--issuer", required=True, help="Identité de l'émetteur")
    p_gen.add_argument("--outdir", type=Path, required=True, help="Répertoire de sortie")

    # ---- verify ----
    p_ver = sub.add_parser("verify", help="Vérifie une preuve MEVE")
    p_ver.add_argument("path", type=Path, help="Fichier de preuve à vérifier")

    # ---- inspect ----
    p_ins = sub.add_parser("inspect", help="Affiche une preuve lisible")
    p_ins.add_argument("path", type=Path, help="Fichier de preuve à inspecter")

    args = parser.parse_args()

    if args.command == "generate":
        proof = generate_meve(issuer=args.issuer, outdir=args.outdir)
        pretty_print(proof)
    elif args.command == "verify":
        result = verify_proof(args.path)
        pretty_print(result)
    elif args.command == "inspect":
        data = args.path.read_text(encoding="utf-8")
        print(data)


if __name__ == "__main__":
    main()
