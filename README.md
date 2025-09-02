# 🌍 DigitalMeve — The .MEVE Standard

👉 *The first global platform to certify and verify the authenticity of your documents.*

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)](https://github.com/BACOUL/digitalmeve)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 2. 🚀 Patches Snapshot (already implemented)

DigitalMeve already includes a strong foundation:

- ✅ **Core library**: `generator.py` + `verifier.py`  
- ✅ **CLI**: `digitalmeve generate / verify / inspect`  
- ✅ **Tests**: `pytest` passing on Python 3.10 → 3.12  
- ✅ **Official Schema**: [`schemas/meve-1.schema.json`](schemas/meve-1.schema.json)  
- ✅ **CI/CD GitHub Actions**:  
  - [tests.yml](.github/workflows/tests.yml) (unit tests)  
  - [quality.yml](.github/workflows/quality.yml) (lint, ruff, black)  
  - [publish.yml](.github/workflows/publish.yml) (PyPI via OIDC)  
- ✅ **Quality**: linting, pre-commit hooks, coverage badge  
- ✅ **Docs**: overview, specification, guides, roadmap, security, API usage  
- ✅ **Examples**: real sample files + reproducible scripts (`examples/make_examples.sh`)  
- ✅ **Governance**: [LICENSE](LICENSE), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md)  

---

### 🔑 Main commands

# Generate a .meve.json proof
digitalmeve generate path/to/file.pdf --issuer "Alice"

# Verify a proof
digitalmeve verify file.pdf.meve.json --expected-issuer "Alice"

# Inspect a proof (human-readable summary)
digitalmeve inspect file.pdf.meve.json

3. 📖 Description / TL;DR

DigitalMeve defines the universal format `.meve` (Memory Verified) to timestamp, hash, and certify digital documents.  
👉 The goal: make `.meve` the “PDF of digital proof” worldwide.

Why `.meve`?

- **Existence** → prove a file existed at a given date.  
- **Integrity** → SHA-256 hash, any change = invalid.  
- **Authenticity** → issuer is always visible (Personal / Pro / Official).  
- **Metadata** → optional key/values (author, project, contract ID…).  
- **Portable** → lightweight JSON sidecar (file.pdf.meve.json).  

🔧 Quick Usage (CLI & Python)

# CLI usage
digitalmeve generate mydoc.pdf --issuer "Alice"
digitalmeve verify mydoc.pdf.meve.json --expected-issuer "Alice"
digitalmeve inspect mydoc.pdf.meve.json

# Python usage
from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

proof = generate_meve("mydoc.pdf", issuer="Alice")
ok, info = verify_meve("mydoc.pdf.meve.json", expected_issuer="Alice")
print(ok, info)

✅ With .meve, you can prove existence, integrity, and authenticity of any digital file in seconds.

## 4. 📦 Installation

DigitalMeve is available on [PyPI](https://pypi.org/project/digitalmeve/) and requires **Python 3.10+**.  
Install it with:
pip install digitalmeve

## 5. ⚡ Quickstart (CLI)

After installing, you can immediately generate and verify `.meve` proofs using the CLI.

Generate a proof:
digitalmeve generate path/to/file.pdf --issuer "Alice"

digitalmeve verify path/to/file.pdf.meve.json --expected-issuer "Alice"

digitalmeve inspect path/to/file.pdf.meve.json


## 6. ✨ Features (Highlights)

- **SHA-256 hashing** → guarantees file integrity.  
- **Timestamp (UTC ISO-8601)** → proof of existence at a given time.  
- **Issuer levels** →  
  - *Personal*: self-certification.  
  - *Pro*: email verified.  
  - *Official*: DNS/institution verified.  
- **JSON Schema validation** → all proofs are machine-verifiable against [`schemas/meve-1.schema.json`](schemas/meve-1.schema.json).  
- **Metadata embedding** → free-form key/values (author, project, notes…).  
- **Sidecar `.meve.json` files** → scalable for any file type or size.  
- **CLI & Python API** → generate, verify, inspect proofs in seconds.  
- **CI/CD ready** → tested with GitHub Actions (tests, quality, PyPI publish).

## 7. 📚 Documentation

- [Overview](docs/overview.md)  
- [Specification](docs/specification.md)  
- [Generator Guide](docs/generator-guide.md)  
- [Verification Guide](docs/verification-guide.md)  
- [API Usage](docs/API_USAGE.md)  
- [Security](docs/security.md)  
- [Examples](docs/examples.md)  
- [Pro Verification](docs/PRO.md)  
- [Official Verification](docs/OFFICIAL.md)  
- [Roadmap](docs/roadmap.md)  
- [FAQ](docs/faq.md)  
- [Glossary](docs/glossary.md)  

**Schema Reference:** [`MEVE/1 JSON Schema`](schemas/meve-1.schema.json)  

## 8. 🧪 Examples (runnable)

DigitalMeve provides reproducible examples to demonstrate `.meve` proofs in action.  

Scripts included:  
- `./examples/make_examples.sh` → generate sample proofs (invoice, photo, diploma).  
- `./examples/verify_examples.sh` → verify all generated proofs.  

Resources:  
- [Examples folder](examples/)  
- [Examples Guide](docs/examples.md)

## 9. 🔑 Certification Levels

DigitalMeve defines three levels of certification:

- **Personal** → self-certification (existence proof only).  
- **Pro** → email verified (identity linked to a real professional).  
- **Official** → DNS verified / institution (official certification).  

⚡ Certification level is always computed automatically by the verifier — impossible to forge.

## 10. 🛡 Security (Essentials)

- **Hashing (SHA-256)** → ensures the file’s fingerprint is unique and tamper-proof.  
- **Immutability** → any change in the original file immediately invalidates the `.meve` proof.  
- **Schema validation** → every proof is checked against the official [MEVE/1 JSON Schema](schemas/meve-1.schema.json).  
- **Sidecar JSON** → `.meve.json` proofs are stored separately, scalable for large files and non-intrusive.  
- **Pro verification (email)** → issuer identity verified via magic-link workflow (no password).  
- **Official verification (DNS)** → TXT challenge on `_meve.<domain>` binds proofs to a verified domain/institution.  
- **Verification key (Ed25519-ready)** → proofs are designed to carry `key_id` (public key reference) and `signature` (Ed25519).  
  - Public key = **verification key** used by verifiers; private key stored securely (HSM/KMS).  
  - Offline verification: `signature` is checked against the file hash + proof manifest using the public key (`key_id`).  
- **Transparency-ready** → compatible with future transparency logs (Merkle tree roots periodically published).  
- **Disclosure & contact** → security guidance and reporting process in [SECURITY.md](SECURITY.md).

## 11. 📊 Use Cases

- **🧑 Individuals**  
  - Proof of authorship (artworks, photos, manuscripts, ideas).  
  - Timestamped evidence (insurance claims, personal agreements).  

- **👔 Professionals**  
  - Certified invoices, contracts, and designs.  
  - Intellectual property pre-proof and audits.  
  - API integration for automated workflows.  

- **🏛 Institutions**  
  - Universities → certified diplomas and transcripts.  
  - Governments → official documents, tenders, and policies.  
  - Courts & notaries → legal contracts, rulings, and certified archives.

## 12. 🚀 Roadmap (snapshot)

**Phase 1 — MVP (30 days)**  
✅ Generator & Verifier (CLI + PyPI)  
✅ GitHub CI/CD Workflows  
✅ JSON Schema v1  
🚧 FAQ + Glossary  
🚧 Examples + scripts  

**Phase 2 — 6 months**  
- Pro verification (email magic link)  
- Official verification (DNS challenge)  
- Certified PDF export  
- Public API SaaS  

**Phase 3 — 1–2 years**  
- International standardization  
- ERP/CRM integrations  
- Transparency log (Merkle root)  
- Broad adoption across industries  

📖 Full details → [docs/roadmap.md](docs/roadmap.md)

## 13. 🌐 Web Integration (planned)

Future API endpoints (for Framer integration and external apps):

- **POST /api/generate** → upload file + issuer → returns `.meve.json` (not stored).  
- **POST /api/verify** → submit proof JSON → returns `{ ok, info }`.  

🔗 Schema reference → [schemas/meve-1.schema.json](schemas/meve-1.schema.json)  
📦 PyPI package → [DigitalMeve on PyPI](https://pypi.org/project/digitalmeve/)

## 14. 📦 Releases

- Current version: **1.7.1-dev**  
- Published automatically to [PyPI](https://pypi.org/project/digitalmeve/)  
- Workflow: version bump → tag → GitHub Actions → PyPI publish  
- Full changelog available in [CHANGELOG.md](CHANGELOG.md)

## 15. ⚖ License

This project is licensed under the **MIT License**.  
See the full text in [LICENSE](LICENSE).
