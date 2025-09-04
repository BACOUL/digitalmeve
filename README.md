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
DigitalMeve defines the universal format **`.meve`** (Memory Verified) to **timestamp, hash, and certify** digital documents.
**Goal:** make `.meve` the *“PDF of digital proof”*.

**Verification ensures**
- **Integrity** → SHA-256 validation (any change = invalid)
- **Timestamp** → UTC ISO-8601 (`issued_at`)
- **Issuer** → Personal / Pro / Official (computed by the verifier)

---

## 2. 🚀 Patches Snapshot (already implemented)
- ✅ Core library: `generator.py` + `verifier.py`
- ✅ CLI: `digitalmeve generate / verify / inspect`
- ✅ Tests: `pytest` on Python 3.10 → 3.12
- ✅ Official Schema: [`schemas/meve-1.schema.json`](schemas/meve-1.schema.json)
- ✅ CI/CD: [tests](.github/workflows/tests.yml) · [quality](.github/workflows/quality.yml) · [publish](.github/workflows/publish.yml)
- ✅ Quality: linting, pre-commit hooks, coverage badge
- ✅ Docs: overview, specification, guides, roadmap, security, API usage
- ✅ Examples: real samples + scripts (`examples/make_examples.sh`)
- ✅ Governance: [LICENSE](LICENSE) · [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md) · [CONTRIBUTING](CONTRIBUTING.md) · [SECURITY](SECURITY.md)

---

## 3. 📖 TL;DR
**Why `.meve`?**
Existence (prove a file existed), Integrity (SHA-256), Authenticity (visible issuer), Metadata (optional), Portable (sidecar `file.ext.meve.json`).

---

## 4. 🔧 Unified Quickstart (Install + CLI + Python)
```bash
# Install
pip install digitalmeve

# --- CLI -------------------------------------------------
# Generate a .meve.json proof
digitalmeve generate path/to/file.pdf --issuer "Alice"

# Verify a proof
digitalmeve verify path/to/file.pdf.meve.json --issuer "Alice"

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

SHA-256 hashing · UTC timestamp (issued_at)

Issuer levels → Personal / Pro / Official

JSON Schema validation → schemas/meve-1.schema.json

Metadata (free-form key/values)

Sidecar .meve.json (scales for any file type)

CLI & Python API (generate / verify / inspect)

CI/CD ready (GitHub Actions)



---

6. 📚 Documentation

Overview · Specification · Generator Guide · Verification Guide

API Usage · Security · Examples

Pro · Official · Roadmap · FAQ · Glossary


Schema Reference: MEVE/1 JSON Schema


---

7. 🧪 Examples (runnable)

Scripts:

examples/make_examples.sh → generate sample proofs (invoice, photo, diploma)

examples/verify_examples.sh → verify all generated proofs


Resources: examples/ · Examples Guide


---

8. 🔑 Certification Levels

Personal → self-certification (existence proof only)

Pro → email verified (professional identity)

Official → DNS/institution verified


> The level is computed by the verifier — not self-declared.




---

9. 🛡 Security (Essentials)

Tamper-evident (SHA-256) · Schema validation

Pro verification (email magic-link) · Official verification (DNS TXT _meve.<domain>)

Ed25519-ready (key_id, signature) · Transparency-ready (future logs)

See SECURITY.md for disclosure & contact



---

10. 📊 Use Cases

Individuals (authorship, evidence) · Professionals (invoices, contracts, automation) · Institutions (diplomas, tenders, archives)


---

11. 🚀 Roadmap (snapshot)

Phase 1 (MVP): generator + verifier, CI, schema v1

Phase 2 (≤6 months): Pro/Official onboarding, certified PDF export, public API

Phase 3 (1–2 years): standardization, integrations, transparency log
Full details → docs/roadmap.md



---

12. 🌐 Web Integration (planned)

Future endpoints:

POST /api/generate → returns .meve.json

POST /api/verify → returns { ok, info }



---

13. 📦 Releases

Current version: 1.7.1-dev · published to PyPI.
Workflow: version bump → tag → GitHub Actions → PyPI. See CHANGELOG.md.


---

14. ⚖ License

MIT — see LICENSE.
