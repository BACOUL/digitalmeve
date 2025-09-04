
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

## 1. Overview

DigitalMeve provides a **fast and universal** way to verify the authenticity of any `.meve` proof.

Verification ensures:

- **Integrity** → the document has not been tampered with (SHA-256 validation).
- **Timestamp** → the proof contains a valid UTC timestamp.
- **Issuer** → the identity level (Personal, Pro, Official) matches expectations.

---

## 2. 🚀 Patches Snapshot (already implemented)

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

## 3. 📖 Description / TL;DR

DigitalMeve defines the universal format `.meve` (Memory Verified) to timestamp, hash, and certify digital documents.  
👉 The goal: make `.meve` the “PDF of digital proof” worldwide.

Why `.meve`?

- **Existence** → prove a file existed at a given date.
- **Integrity** → SHA-256 hash, any change = invalid.
- **Authenticity** → issuer is always visible (Personal / Pro / Official).
- **Metadata** → optional key/values (author, project, contract ID…).
- **Portable** → lightweight JSON sidecar (file.pdf.meve.json).

---

## 4. 🔧 Quick Usage (CLI & Python)

### CLI

```bash
# Generate a .meve.json proof
digitalmeve generate path/to/file.pdf --issuer "Alice"

# Verify a proof
digitalmeve verify path/to/file.pdf.meve.json --issuer "Alice"

# Inspect a proof (human-readable summary)
digitalmeve inspect path/to/file.pdf.meve.json

Python

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

proof = generate_meve("mydoc.pdf", issuer="Alice")
ok, info = verify_meve(proof, expected_issuer="Alice")
print(ok, info["subject"]["hash_sha256"])

✅ With .meve, you can prove existence, integrity, and authenticity of any digital file in seconds.


---

5. 📦 Installation

Requires Python 3.10+.

pip install digitalmeve


---

6. ✨ Features (Highlights)

SHA-256 hashing → guarantees file integrity.

Timestamp (UTC ISO-8601) → proof of existence at a given time.

Issuer levels → Personal / Pro / Official.

JSON Schema validation → machine-verifiable against schemas/meve-1.schema.json.

Metadata embedding → free-form key/values (author, project, notes…).

Sidecar .meve.json → scalable for any file type or size.

CLI & Python API → generate, verify, inspect in seconds.

CI/CD ready → tested with GitHub Actions.



---

7. 📚 Documentation

Overview

Specification

Generator Guide

Verification Guide

API Usage

Security

Examples

Pro Verification

Official Verification

Roadmap

FAQ

Glossary


Schema Reference: MEVE/1 JSON Schema


---

8. 🧪 Examples (runnable)

Scripts included:

./examples/make_examples.sh → generate sample proofs (invoice, photo, diploma).

./examples/verify_examples.sh → verify all generated proofs.


Resources:

Examples folder

Examples Guide



---

9. 🔑 Certification Levels

Personal → self-certification (existence proof only).

Pro → email verified (identity linked to a real professional).

Official → DNS/institution verified.


⚡ The level is computed by the verifier — impossible to forge.


---

10. 🛡 Security (Essentials)

Hashing (SHA-256) → unique, tamper-proof fingerprint.

Immutability → any change invalidates the proof.

Schema validation → validated against MEVE/1 JSON Schema.

Pro verification → email magic-link.

Official verification → TXT challenge _meve.<domain>.

Verification key (Ed25519-ready) → key_id + signature are supported.

Transparency-ready → compatible with future transparency logs.

Disclosure & contact → see SECURITY.md.



---

11. 📊 Use Cases

Individuals

Proof of authorship (artworks, photos, manuscripts).

Timestamped evidence.


Professionals

Certified invoices, contracts, designs.

API integration for automated workflows.


Institutions

Universities → certified diplomas.

Governments → official documents and tenders.

Courts & notaries → legal archives.



---

12. 🚀 Roadmap (snapshot)

Phase 1 — MVP (now)

Generator & Verifier (CLI + PyPI)

GitHub CI/CD Workflows

JSON Schema v1


Phase 2 — 6 months

Pro verification (email magic link)

Official verification (DNS challenge)

Certified PDF export

Public API SaaS


Phase 3 — 1–2 years

Standardization & integrations

Transparency log (Merkle root)


See details → docs/roadmap.md


---

13. 🌐 Web Integration (planned)

API endpoints (future):

POST /api/generate → upload file + issuer → returns .meve.json.

POST /api/verify → submit proof JSON → returns { ok, info }.



---

14. 📦 Releases

Current version: 1.7.1-dev

Published automatically to PyPI

Version bump → tag → GitHub Actions → PyPI publish

Changelog → CHANGELOG.md



---

15. ⚖ License

MIT — see LICENSE.

> NB : pas d’espaces en fin de ligne et **une seule** ligne vide à la fin.

---

