# 🛡 DigitalMeve — Verification Guide

---

## 1. Overview

DigitalMeve provides a **fast and universal** way to verify the authenticity of any `.meve` proof.  
Verification ensures:

- **Integrity** → the document has not been tampered with (SHA-256 validation).  
- **Timestamp** → the proof contains a valid UTC timestamp.  
- **Issuer** → the identity level (Personal, Pro, Official) matches expectations.  

---

## 2. Verification Methods

### 2.1 Local verification (Python SDK)

Install DigitalMeve:

```bash
pip install digitalmeve

Example usage:

from digitalmeve import verify_meve

ok, info = verify_meve("sample.txt.meve.json", expected_issuer="Personal")

if ok:
    print("✅ Proof valid:", info)
else:
    print("❌ Invalid proof:", info)


---

2.2 Web verification (coming soon)

Drag & drop your .meve.json file into the DigitalMeve Web Verifier.

The verifier runs locally in your browser — no data is uploaded.



---

2.3 API verification (for Pro/Official users)

A REST API will be available for integrations:

POST /api/v1/verify
Content-Type: application/json

{
  "proof": { ... }
}

Response example:

{
  "valid": true,
  "issuer": "Pro",
  "timestamp": "2025-08-30T12:34:56Z",
  "hash": "b94d27b9934d3e08..."
}


---

3. Error Handling

Standard error cases:

Issuer mismatch → {"error": "Issuer mismatch", "expected": "..."}

Hash mismatch → {"error": "Hash mismatch"}

Missing keys → {"error": "Missing required keys", "missing": [...]}

Invalid proof → {"error": "Invalid file: ..."}



---

4. Next Steps

Learn how to generate proofs → Generator Guide

See formal rules → Specification

Review security model → Security



---

✍️ Maintained under DigitalMeve.
