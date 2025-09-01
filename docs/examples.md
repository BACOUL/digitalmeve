# 📂 Examples of MEVE Usage

This document shows practical examples of how `.MEVE` proofs are generated, structured, and verified.

---

## 📝 Example 1 — Basic File Proof

**Input file**: `contract.pdf`

**Generated proof** (`contract.pdf.meve.json`):

```json
{
  "meve_version": "1.0",
  "issuer": "Personal",
  "timestamp": "2025-08-30T12:00:00Z",
  "subject": {
    "filename": "contract.pdf",
    "size": 52344,
    "hash_sha256": "abcd1234..."
  },
  "hash": "abcd1234...",
  "metadata": {}
}

Verification (CLI):

digitalmeve verify contract.pdf.meve.json
✔ Valid — hash and issuer verified


---

🏞 Example 2 — With Metadata

Input file: photo.jpg

Generated proof snippet:

{
  "subject": {
    "filename": "photo.jpg",
    "size": 238900,
    "hash_sha256": "efgh5678..."
  },
  "metadata": {
    "location": "Paris",
    "author": "Alice"
  }
}

Metadata is optional and can include arbitrary key/value pairs.


---

👔 Example 3 — Professional Certification

Issuer: DigitalMeve Pro Test Suite

Proof includes:

{
  "issuer": "alice@company.com",
  "issuer_level": "Pro",
  "certified": "DigitalMeve (email)",
  "signature": "..."
}

Verified email → issuer level = Pro

Standard JSON with extra field "issuer_level": "Pro"



---

✅ These examples show how .MEVE can be used for personal proofs, enriched proofs with metadata, and professional-level certifications.
