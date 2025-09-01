# 📑 DigitalMeve — MEVE/1 Specification (Draft)

---

## 1. Purpose

`.meve` provides a **portable, human-readable proof** for any digital file:

- **Existence** at time T (UTC timestamp)  
- **Integrity** of the exact bytes (SHA-256)  
- **Issuer linkage** (Personal / Pro / Official), computed automatically by the verifier  

---

## 2. Minimal JSON (MEVE/1)

```json
{
  "meve_version": "1.0",
  "issuer": "Personal",
  "hash": "<sha256 of the file>",
  "preview_b64": "<optional base64 preview of first bytes>",
  "subject": {
    "filename": "sample.pdf",
    "size": 12345,
    "hash_sha256": "<sha256 of the file>"
  },
  "timestamp": "2025-08-30T12:34:56Z",
  "metadata": {}
}

Required fields

meve_version (string) → currently "1.0"

issuer (string) → logical issuer name

hash (string) → SHA-256 of file bytes (must equal subject.hash_sha256)

preview_b64 (string, optional) → base64 preview (first bytes)

subject (object)

filename (string) → original filename

size (integer) → size in bytes

hash_sha256 (string) → SHA-256 of file


timestamp (string, ISO 8601 UTC)

metadata (object, can be empty)



---

3. Levels of Certification (computed by verifier)

Personal → default self-certification

Pro → verified email/domain account (future)

Official → DNS / institution verified (future)


> The level is always computed by the verifier — never user-declared.




---

4. Generation Rules (reference)

Do not modify the original file; always produce a sidecar *.meve.json.

Compute SHA-256 on the full byte stream.

Include a small base64 preview (~64–128 bytes).

Use datetime.now(timezone.utc).isoformat() → UTC timestamp with Z.



---

5. Verification Rules (reference)

Given a dict or path to *.meve.json, the verifier MUST:

1. Parse JSON → must be an object.


2. Check presence of required root keys.


3. Ensure subject contains: filename, size, hash_sha256.


4. Verify hash == subject.hash_sha256.


5. If expected_issuer provided → enforce equality.


6. Return (ok: true, info: dict) on success, otherwise (ok: false, {"error": "...", ...}).



Standard error messages

Missing keys → {"error": "Missing required keys", "missing": [...]}

Issuer mismatch → {"error": "Issuer mismatch", "expected": "..."}

Hash mismatch → {"error": "Hash mismatch"}

Invalid JSON/file → {"error": "Invalid file: <details>"}



---

6. Embedding vs Sidecar

Recommended (MVP) → keep the file untouched; generate filename.ext.meve.json.

Future → embed proof inside metadata (PDF/XMP, PNG tEXt, EXIF).



---

7. Compatibility

Parsers must ignore unknown fields (forward extensibility).

meve_version controls major format changes (e.g., "2.0").



---

8. Security Notes

Any byte change → different SHA-256 → verification fails.

Existence proof ≠ legal identity.

Identity verification comes from Pro/Official flows.

UTC timestamp; optional future trusted timestamp authority (TSA).


👉 See Security Model for full threat model.


---

9. Examples

Concrete usage available in Examples.

digitalmeve verify contract.pdf.meve.json
✔ Valid — hash and issuer verified


---

✍️ Draft version: MEVE/1.0
Maintained under DigitalMeve.

---
