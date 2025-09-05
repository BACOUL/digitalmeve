# API Usage — DigitalMeve

This page shows how to **generate** and **verify** a minimal `.meve` proof in memory, and how to **persist** the proof as a sidecar JSON file.

---

## Generate (in memory)

```python
from digitalmeve.generator import generate_meve

meve = generate_meve("path/to/file.pdf")  # returns a dict
print(meve["subject"]["filename"], meve["subject"]["hash_sha256"])


---

Verify (in-memory dict)

from digitalmeve.verifier import verify_meve

ok, info = verify_meve(meve, expected_issuer="Personal")
assert ok is True
print(info["subject"]["size"])


---

Generate sidecar .meve.json on disk

import json
from pathlib import Path
from digitalmeve.generator import generate_meve

outdir = Path("out")
outdir.mkdir(exist_ok=True)

proof = generate_meve("path/to/file.pdf")
(outdir / "file.pdf.meve.json").write_text(
    json.dumps(proof, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

print("Proof saved:", outdir / "file.pdf.meve.json")


---

✅ With these steps you can:

Generate a .meve proof in memory

Verify the proof directly

Or persist it as a .meve.json sidecar file for later verification
