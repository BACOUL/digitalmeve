# API Usage — DigitalMeve

This page shows how to generate and verify a minimal `.meve` proof (in-memory) and how to persist the proof as a sidecar JSON file.

## Generate (in-memory)

```python
from digitalmeve.core import generate_meve

meve = generate_meve("path/to/file.pdf")  # returns a dict
print(meve["subject"]["filename"], meve["subject"]["hash_sha256"])

Verify (in-memory dict)

from digitalmeve.core import verify_meve

ok, info = verify_meve(meve, expected_issuer="Personal")
assert ok is True
print(info["subject"]["size"])

Generate sidecar .meve.json on disk

from pathlib import Path
from digitalmeve.core import generate_meve

outdir = Path("out")
outdir.mkdir(exist_ok=True)
meve = generate_meve("data/sample.pdf", outdir=outdir, issuer="DigitalMeve Test Suite")
# writes: out/sample.pdf.meve.json

Verify from a sidecar file

from digitalmeve.core import verify_meve

ok, info = verify_meve("out/sample.pdf.meve.json", expected_issuer="DigitalMeve Test Suite")
print(ok, info["subject"]["filename"])

> Notes

Changing one byte in the original file will change hash_sha256 and verification will fail.

For large files or formats without stable metadata, use sidecar .meve.json.

Levels: Personal (self), Pro (email verified), Official (DNS verified).




---

# 2) Exemples exécutables

## a) Script Python simple

**Fichier :** `examples/generate_and_verify.py`

```python
from pathlib import Path
from digitalmeve.core import generate_meve, verify_meve

def main():
    # Prepare sample data
    samples = Path("examples/_data")
    samples.mkdir(parents=True, exist_ok=True)
    f = samples / "hello.txt"
    f.write_text("hello meve\n", encoding="utf-8")

    # 1) In-memory generation
    meve = generate_meve(f)
    print("Generated (in-memory):", meve["subject"]["filename"], meve["issuer"])

    # 2) Persist sidecar .meve.json
    outdir = samples / "out"
    outdir.mkdir(exist_ok=True)
    meve2 = generate_meve(f, outdir=outdir, issuer="DigitalMeve Test Suite")
    sidecar = outdir / f"{f.name}.meve.json"
    print("Sidecar written:", sidecar.exists(), sidecar)

    # 3) Verify in-memory dict
    ok, info = verify_meve(meve, expected_issuer="Personal")
    print("Verify in-memory:", ok, info["subject"]["hash_sha256"][:12])

    # 4) Verify from file
    ok2, info2 = verify_meve(sidecar, expected_issuer="DigitalMeve Test Suite")
    print("Verify sidecar:", ok2, info2["subject"]["filename"])

if __name__ == "__main__":
    main()

b) Mini démo CLI

Fichier : examples/cli_demo.sh

#!/usr/bin/env bash
set -euo pipefail

PY=${PY:-python}

# Create sample
mkdir -p examples/_data examples/_data/out
echo "hello meve" > examples/_data/hello.txt

# In Python: generate + verify
$PY - <<'PYCODE'
from pathlib import Path
from digitalmeve.core import generate_meve, verify_meve
p = Path("examples/_data/hello.txt")
out = p.parent / "out"
out.mkdir(exist_ok=True)
m = generate_meve(p, outdir=out, issuer="DigitalMeve Test Suite")
print("Wrote:", (out / (p.name + ".meve.json")))
ok, info = verify_meve(out / (p.name + ".meve.json"), expected_issuer="DigitalMeve Test Suite")
print("Verify:", ok, info["subject"]["hash_sha256"][:12])
PYCODE

echo "✅ Done."
