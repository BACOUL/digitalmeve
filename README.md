
# 🌍 DigitalMeve — The .MEVE Standard

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://static.pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/BACOUL/digitalmeve/blob/main/LICENSE)

---

## 📖 Overview

**DigitalMeve** defines the universal format **`.meve`** (*Memory Verified*):  
a lightweight, human-readable proof that confirms:

- the **existence** of a document at a given time,  
- the **integrity** of the file (**SHA-256**),  
- the **authenticity** of the issuer (**Personal / Pro / Official**).  

**Goal:** make `.meve` the *“PDF of digital proof”* worldwide.  

---

## 🚀 Project status

- Version: **1.7.0 (MVP)**  
- ✅ Core generator & verifier published to PyPI  
- ✅ CI/CD (quality, tests, publish)  
- ✅ Docs & policies (MIT, Contributing, Security)  
- 🚧 Next: JSON Schema validation, FastAPI minimal API, Framer demo site  

Changelog → [CHANGELOG.md](https://github.com/BACOUL/digitalmeve/blob/main/CHANGELOG.md)  

---

## 🗂 Repository Tree

.github/                 CI workflows (quality, tests, publish) docs/                    Documentation (specs, guides, roadmap, security) examples/                Usage examples schema/                  JSON Schemas (MEVE/1) ← planned in v1.8 src/digitalmeve/         Core library (generator / verifier) tests/                   Unit & integration tests

.editorconfig .flake8 .gitignore .pre-commit-config.yaml CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE MAINTAINERS.md MANIFEST.in Makefile README.md ROADMAP.md SECURITY.md mkdocs.yml pyproject.toml requirements.txt

---

## ⚡ Quick start

```bash
pip install digitalmeve

from digitalmeve import generate_meve, verify_meve

# Generate a proof
meve_path = generate_meve(
    file_path="examples/sample.pdf",
    issuer="john.doe@example.com",
    meta={"purpose": "contract-v1"},
)

# Verify a proof
result = verify_meve(meve_path)
print(result.valid, result.level, result.timestamp_iso)

Guides:

Generator Guide

Verification Guide


Short example .meve.json:

{
  "status": "Personal",
  "issuer": "john.doe@example.com",
  "issued_at": "2025-09-01T12:34:56Z",
  "hash_sha256": "8f9c1b3c...e7a",
  "meta": {"filename": "contract-v1.pdf", "size": 58231, "mime": "application/pdf"},
  "id": "meve-0a92f3"
}


---

📚 Documentation

Overview

API Usage

Generator Guide

Verification Guide

Specification

Security

Examples

Pro Verification (email)

Official Verification (DNS)

Roadmap (docs)

Roadmap (root)


> MkDocs site (future): https://bacoul.github.io/digitalmeve/




---

📝 MEVE/1 — Field Summary (Draft)

Field	Meaning / Notes

status	Personal | Pro | Official
issuer	Email or domain
certified	self | email | dns (how authenticity was proven)
issued_at	ISO-8601 UTC timestamp
hash_sha256	Document integrity hash
schema_hash	Hash of the schema/manifest (future)
key_id	Public key id (future)
id	Short MEVE proof id
signature	Ed25519 signature (future)
meta	Filename, size (bytes), MIME type
doc_len	Document length in bytes (future)
verified_domain	Populated when DNS is verified (future)
doc_ref	Internal reference / pointer (optional)


Full specification → specification.md


---

🔑 Certification Levels

Personal → self-certification (existence only)

Pro → identity verified via email

Official → DNS-verified institution


⚡ The level is always computed automatically by the verifier.


---

🛡 Security & Trust

Tamper-proof: any change invalidates the proof

SHA-256 integrity hashing

Embedded metadata or sidecar .meve.json

Instant fraud detection (hash mismatch)

Clear error messages

Offline verification (CLI/WASM planned)

HSM/KMS key storage (planned)

Transparency log (Merkle root) (planned)


Details → security.md


---

🎨 Product UX

Status badges: Personal / Pro / Official

Drag-and-drop verification (demo planned)

Export JSON proof

Shareable badge “Sealed with DigitalMeve” (planned)

Free tier size limit (e.g., 25–50 MB) (planned)



---

⚖ Legal

GDPR: no documents stored, only hashes

eIDAS/ESIGN: .meve = proof of existence & integrity, not a qualified signature

Terms: no illegal content; MEVE ≠ notary



---

📊 Use Cases

Individuals: authorship, timestamped photos/videos, personal evidence

Professionals: certified invoices/contracts, IP pre-proof

Institutions: diplomas, court judgments, official documents



---

💰 Business Model

Free → individuals

Pro → subscription (API, dashboard)

Official → licensing/SLA (DNS verification, institutions)



---

🔧 API Preview (Planned)

POST /generate → upload file + issuer → returns .meve.json (file not stored)

POST /verify → submit proof JSON → returns { ok, level, issuer, timestamp }

Stack: FastAPI + Docker (Railway / Render / Cloud Run)



---

🗺 Roadmap

Phase 1 (MVP, v1.7) → generator, verifier, CI/CD, PyPI ✅

Phase 2 (~6 months) → email/DNS verification, schema validation, PDF export, SaaS API 🚧

Phase 3 (1–2 years) → standardization (ISO/AFNOR), ERP/CRM integrations, adoption 🎯


30-day MVP checklist:

[x] Structured repo & packaging

[x] Generator + tests

[x] Verifier + tests

[x] CI/CD workflows

[ ] Framer landing + demo

[ ] Spec & product docs polish

[ ] Bilingual FAQ (EN/FR)

[ ] First comms (video + socials)


Roadmap docs → roadmap.md


---

🛠 Development

Local checks:

pre-commit run --all-files
pytest -q

Contributing

Code of Conduct

Security Policy

Maintainers

Support



---

📦 Releases & CI/CD

Current version: 1.7.0 (PyPI)

Workflow: version bump → tag → GitHub Actions → publish

Changelog → CHANGELOG.md


Workflows:

Quality

Tests

Publish



---

⚖ License

MIT → LICENSE



---

✍️ Maintained by the DigitalMeve Team.

---
