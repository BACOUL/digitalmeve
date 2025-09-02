import json
from pathlib import Path

import pytest
import jsonschema

from digitalmeve.generator import generate_meve


# Charger le schéma une fois
schema_path = Path(__file__).resolve().parent.parent / "schemas" / "meve-1.schema.json"
with schema_path.open("r", encoding="utf-8") as f:
    SCHEMA = json.load(f)


def test_generated_proof_matches_schema(tmp_path):
    # Créer un fichier temporaire
    test_file = tmp_path / "hello.txt"
    test_file.write_text("hello world")

    # Générer une preuve
    proof = generate_meve(test_file)

    # Validation stricte
    jsonschema.validate(instance=proof, schema=SCHEMA)


def test_invalid_proof_fails():
    bad_proof = {"issuer": "X"}  # volontairement incomplet
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad_proof, schema=SCHEMA)
