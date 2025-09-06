# 📂 Examples of MEVE Usage

This page shows how `.meve.json` proofs are generated, structured, and verified, in line with the public schema [`schemas/meve-1.schema.json`](../schemas/meve-1.schema.json).

---

## 📝 Example 1 — Basic File Proof

**Input file:** `contract.pdf`  

**Command:**

digitalmeve generate examples/contract.pdf --outdir examples --issuer "Personal"

Generated proof (contract.pdf.meve.json):

{
  "meve_version": "1.0",
  "status": "Personal",
  "certified": "self",
  "issuer": "Personal",
  "issued_at": "2025-09-02T12:00:00Z",
  "timestamp": "2025-09-02T12:00:00Z",
  "subject": {
    "filename": "contract.pdf",
    "size": 52344,
    "hash_sha256": "abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234"
  },
  "hash_sha256": "abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234",
  "meta": {}
}

Verification (CLI):

digitalmeve verify examples/contract.pdf.meve.json

Expected output:

{"ok": true, ...}

> ℹ️ Note: timestamp is kept for backward compatibility. The schema uses issued_at as the canonical field.




---

🏞 Example 2 — With Metadata

Input file: photo.jpg

Command:

digitalmeve generate examples/photo.jpg --outdir examples --issuer "Personal"

Generated proof (excerpt):

{
  "status": "Personal",
  "certified": "self",
  "issuer": "Personal",
  "issued_at": "2025-09-02T12:00:00Z",
  "subject": {
    "filename": "photo.jpg",
    "size": 238900,
    "hash_sha256": "efef...5678"
  },
  "hash_sha256": "efef...5678",
  "meta": {
    "title": "River at dusk",
    "author": "Alice",
    "location": "Paris"
  }
}

> Metadata is optional and can include arbitrary key/value pairs under the meta object.




---

👔 Example 3 — Professional (mock)

For Pro issuers (email confirmed), the verifier will compute:

"status": "Pro",
"certified": "email"

Example snippet (illustrative):

{
  "status": "Pro",
  "certified": "email",
  "issuer": "alice@company.com",
  "issued_at": "2025-09-02T12:00:00Z",
  "hash_sha256": "9a9a...1111"
}

> ⚠️ In the current MVP, Pro/Official elevation is mocked in docs.
Production flow will add email/DNS checks and optional signature fields (key_id, signature, verified_domain).




---

🔁 Regenerate all examples

Use the helper script:

cd examples
./make_examples.sh

This calls the CLI for each supported file and writes <file>.meve.json sidecars next to sources.

---

