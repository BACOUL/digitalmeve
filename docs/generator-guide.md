# ⚙️ MEVE — Generator Guide (Developer)

This guide explains how to generate `.meve.json` proof files with **DigitalMeve**.

---

## 🚀 1) Quick Start (Python)

```python
from digitalmeve.core import generate_meve

meve = generate_meve("myfile.pdf", issuer="My Company")
print(meve)

Result (dict example):

{
  "meve_version": "1.0",
  "issuer": "My Company",
  "timestamp": "2025-08-30T12:00:00Z",
  "metadata": {},
  "subject": {
    "filename": "myfile.pdf",
    "size": 12345,
    "hash_sha256": "abcdef123456..."
  },
  "hash": "abcdef123456...",
  "preview_b64": "..."
}


---

💾 2) Output File (Sidecar)

By default, generate_meve only returns a Python dict.
To persist the proof on disk:

meve = generate_meve("myfile.pdf", outdir="out", issuer="My Company")

This creates:

out/myfile.pdf.meve.json


---

🔎 3) Fields Explanation

meve_version → current spec version ("1.0")

issuer → issuer name (Personal, Pro, or Official)

timestamp → UTC ISO8601 timestamp

metadata → free key-value pairs (optional)

subject → description of the certified file:

filename → original filename

size → file size in bytes

hash_sha256 → SHA-256 hash of the file content


hash → same as subject.hash_sha256 (shortcut)

preview_b64 → base64 preview of the first bytes of the file



---

⚠️ 4) Error Handling

File not found → FileNotFoundError

Permission denied → OSError

Unsupported input type → TypeError if not str or Path



---

✅ 5) Best Practices

Always generate the .meve.json immediately after finalizing a document.

Store the .meve.json in the same folder as the original file.

For Pro/Official issuers, use the verified identity flow (coming soon).

Never modify a .meve.json manually — any change invalidates the proof.



---

📚 Next: Verification Guide
📖 Full Spec: Specification
