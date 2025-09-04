# 📖 Glossary — DigitalMeve

Key terms used in the `.meve` standard.

---

## .meve.json (sidecar)
JSON file adjacent to the original document containing the DigitalMeve proof.

---

## Hash SHA-256
256-bit cryptographic fingerprint of the file.
A single bit changed ⇒ completely different hash.

---

## Timestamp (`issued_at` / `timestamp`)
UTC ISO-8601 date/time (`YYYY-MM-DDThh:mm:ssZ`) written in the proof at generation time.

---

## Issuer
Declared identity of the emitter (free text).
The associated status (*Personal / Pro / Official*) is always calculated by the verifier.

---

## Status
- **Personal** → self-certification
- **Pro** → verified email
- **Official** → verified institution/domain

---

## Certified
Certification method:
- `self`
- `email`
- `dns`

---

## Preview (`preview_b64`)
Base64 preview of a few initial bytes.
Informational only (not used in verification).

---

## Subject
Block describing the certified object:
- `filename`
- `size`
- `hash_sha256`

---

## Schema (MEVE/1)
Public JSON schema describing the minimal proof structure.
Reference: [schemas/meve-1.schema.json](../schemas/meve-1.schema.json)

---

## Transparency Log (Phase 2)
Append-only log of hashes periodically published (Merkle roots) to strengthen immutability.

---

## Ed25519 (Phase 2)
Modern elliptic curve signature scheme.
Used to sign proofs on the server side (Pro/Official).
