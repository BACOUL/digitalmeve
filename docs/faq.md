# FAQ — DigitalMeve

> Frequently asked questions about the **.meve** format, the CLI, and verification.

## What is a .meve.json file?
A **sidecar JSON** that contains the proof of existence and integrity of a document:
- `issued_at`: UTC ISO-8601 timestamp (Z)
- `hash_sha256`: file fingerprint
- `issuer` + `status`: Personal / Pro / Official
- minimal metadata (filename, size)

## Does DigitalMeve store my documents?
**No.** Neither the CLI nor the MVP API store your files. Only the hash and minimal metadata are processed in memory to generate the proof.

## How do I verify a proof?
- **CLI**: `digitalmeve verify path/to/file.meve.json`
- **Web** (beta coming soon): drag & drop the proof into the *Verify* page.

## Is the original file required for verification?
For **full integrity check**, yes: the `hash_sha256` is recalculated on the original file and compared to the proof.  
For **inspection** (metadata, issuer, date…), the sidecar `.meve.json` alone is enough.

## Difference between *Personal*, *Pro*, and *Official*?
- **Personal**: self-certification (existence only).
- **Pro**: verified professional email (magic link).
- **Official**: verified institution/domain via **DNS TXT**.

The **status** is always **calculated** by the verifier; it is never self-declared.

## Is this a legally qualified electronic signature?
**No.** `.meve` establishes **existence & integrity proof**, not a qualified signature (per eIDAS). It’s complementary.

## What happens if I modify the document after generation?
Verification will fail: the `hash_sha256` will no longer match.

## Can I include custom metadata?
Yes: via CLI (`--meta key=value`) or API. Metadata is **optional** and **free-form**, but avoid sensitive data.

## Will the format evolve?
Yes. The **MEVE/1** schema is versioned and public (`schemas/meve-1.schema.json`). Future versions will remain as **backward-compatible** as possible.

## Can I publish my proof publicly?
Yes. (Phase 2) A **transparency log** will allow periodic publication of Merkle roots. In the meantime, you can share the `.meve.json`.

## How to report a vulnerability?
See **SECURITY.md**. Use the provided email/PGP key. Thank you!
