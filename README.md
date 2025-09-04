
---

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
- ✅ **Official Schema**: `schemas/meve-1.schema.json`
- ✅ **CI/CD GitHub Actions**: tests, quality (ruff/black), publish (PyPI via OIDC)
- ✅ **Quality**: linting, pre-commit hooks, coverage badge
- ✅ **Docs**: overview, specification, guides, roadmap, security, API usage
- ✅ **Examples**: real sample files + reproducible scripts (`examples/make_examples.sh`)
- ✅ **Governance**: `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`

---

## 3. 📖 TL;DR

DigitalMeve defines the universal format `.meve` (Memory Verified) to timestamp, hash, and certify digital documents.  
👉 Goal: make `.meve` the “PDF of digital proof”.

Why `.meve`?
- **Existence** → proof a file existed at a given date.
- **Integrity** → SHA-256 hash, any change = invalid.
- **Authenticity** → issuer is always visible (Personal / Pro / Official).
- **Metadata** → optional key/values (author, project, notes…).
- **Portable** → sidecar `file.pdf.meve.json`.

---

## 4. 🔧 Unified Quickstart (Install + CLI + Python)

```bash
# Install
pip install digitalmeve

# --- CLI -------------------------------------------------
# Generate a .meve.json proof
digitalmeve generate path/to/file.pdf --issuer "Alice"

# Verify a proof
digitalmeve verify path/to/file.pdf.meve.json --expected-issuer "Alice"

# Inspect a proof (human-readable summary)
digitalmeve inspect path/to/file.pdf.meve.json

# --- Python ----------------------------------------------
from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

proof = generate_meve("mydoc.pdf", issuer="Alice")
ok, info = verify_meve(proof, expected_issuer="Alice")
print(ok, info["subject"]["hash_sha256"])

✅ With .meve, you can prove existence, integrity, and authenticity in seconds.


---

5. ✨ Features (Highlights)

SHA-256 hashing → guarantees file integrity

Timestamp (UTC ISO-8601) → proof of existence at a given time

Issuer levels → Personal / Pro / Official

JSON Schema validation → machine-verifiable against schemas/meve-1.schema.json

Metadata embedding → free-form key/values (author, project, notes…)

Sidecar .meve.json → scalable for any file type or size

CLI & Python API → generate, verify, inspect in seconds

CI/CD ready → GitHub Actions (tests, quality, publish)



---

6. 📚 Documentation

Overview — introduction to .meve

Generator Guide — how to create proofs

Verification Guide — how to validate proofs

Specification — formal rules of the format

Security — guarantees and threat model

Roadmap — upcoming features

Examples

Pro

Official

FAQ

Glossary



---

7. 🧪 Examples

Scripts: examples/make_examples.sh (generate) and examples/verify_examples.sh (verify).
Resources: examples/ folder and docs/examples.md.


---

8. 🔑 Certification Levels

Personal → self-certification (existence proof only)

Pro → email verified (identity linked to a real professional)

Official → DNS/institution verified


The level is computed by the verifier — not self-declared.


---

9. 🛡 Security

Hashing (SHA-256) and immutability: any change invalidates the proof

Schema validation (MEVE/1)

Pro verification (email magic-link)

Official verification (DNS TXT _meve.<domain>)

Ed25519-ready (key_id, signature)

Transparency-ready (future transparency logs)


See SECURITY.md for disclosure & contact.


---

10. 📊 Use Cases

Individuals → authorship, evidence

Professionals → invoices, contracts, automation

Institutions → diplomas, tenders, archives



---

11. 🚀 Roadmap

Phase 1 (MVP): generator + verifier, CI, schema v1

Phase 2 (≤6 months): Pro/Official onboarding, PDF export, public API

Phase 3 (1–2 years): standardization, integrations, transparency log



---

12. 🌐 Web Integration (planned)

POST /api/generate → returns .meve.json

POST /api/verify → returns { ok, info }



---

13. 📦 Releases

Current version: 1.7.1-dev — Published automatically to PyPI.
Workflow: version bump → tag → Actions → PyPI. See CHANGELOG.md.


---

14. ⚖ License

MIT — see LICENSE.

---
