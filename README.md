
# 🌍 DigitalMeve — The .MEVE Standard

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/BACOUL/digitalmeve/blob/main/LICENSE)

---

## 📖 What is DigitalMeve?

**DigitalMeve** defines the universal format **`.meve`** (Memory Verified) to **timestamp, hash, and certify** digital documents.

**Goal** → Make `.meve` the **“PDF of digital proof”** worldwide.

---

## 📦 Installation

```bash
pip install digitalmeve


---

📚 Documentation

Current (GitHub)

Overview

API Usage

Generator Guide

Verification Guide

Specification

Security

Examples

Pro Verification

Official Verification

Roadmap (docs)

Roadmap (root)


Future (MkDocs site)

👉 DigitalMeve Documentation (soon)


---

🗂 Repository Tree

.github/                 CI workflows (quality, tests, publish)
docs/                    Documentation (specs, guides, roadmap, security)
examples/                Usage examples
schema/                  JSON Schemas (MEVE/1) ← planned in v1.8
src/digitalmeve/         Core library (generator / verifier)
tests/                   Unit & integration tests

.editorconfig
.flake8
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MAINTAINERS.md
MANIFEST.in
Makefile
README.md
ROADMAP.md
SECURITY.md
mkdocs.yml
pyproject.toml
requirements.txt


---

✅ Already Implemented

.meve generator (Python CLI)
→ SHA-256 hash + UTC timestamp + issuer + base64 preview.
→ Saved as .meve.json sidecar.

.meve verifier (Python CLI)
→ Validates structure + hash + expected issuer.

Packaging & PyPI publishing
→ pyproject.toml, requirements.txt, MANIFEST.in.

Unit tests (pytest)
→ Automated with GitHub Actions (3.10, 3.11, 3.12).

Code quality
→ .flake8, pre-commit, linting.

Docs & legal
→ LICENSE, CODE_OF_CONDUCT.md, CONTRIBUTING.md, SECURITY.md.



---

🚧 Next Steps

Email verification (Pro level).

DNS TXT challenge verification (Official level).

Ed25519 signatures and key management.

Transparency log (Merkle root).

Certified PDF export with DigitalMeve footer.

Public API (upload → verify).

Dashboard (history, exports, webhooks).

SaaS integrations (ERP, CRM, universities).

Standardization (ISO/AFNOR).



---

🔑 Certification Levels

Personal → self-certification (existence proof only).

Pro → email-verified identity.

Official → DNS-verified institution.


⚡ Certification level is always computed automatically by the verifier.


---

🛡 Security

Tamper-proof: any change in the file invalidates the .meve.

Metadata embedding (JSON or sidecar).

Scalable: .meve.json sidecar for large files.

Fraud detection: instant hash mismatch detection.

Transparency log (future).



---

📊 Use Cases

👤 Individuals

Proof of authorship (art, photos, manuscripts).

Timestamped evidence (insurance, agreements).


👔 Professionals

Certified invoices, contracts, designs.

Intellectual property pre-proof.


🏛 Institutions

Universities → certified diplomas.

Governments → official documents.

Courts → legal contracts, judgments.



---

🛠 Development

Requires Python 3.10+

Run checks locally:

pre-commit run --all-files
pytest -q

Contribution guide → CONTRIBUTING.md

Code of Conduct → CODE_OF_CONDUCT.md

Security policy → SECURITY.md



---

📦 Releases

Current version: 1.7.0

Published automatically to PyPI

Workflow: version bump → tag → GitHub Actions → PyPI publish



---

📢 Communication

Slogan:
👉 “DigitalMeve — The first global platform to certify and verify the authenticity of your documents.”

Pitch:
“Your documents, certified and verifiable in 2 seconds, anywhere in the world.”


---

⚖ License

This repository is licensed under the MIT License.
See LICENSE for details.


---

✍️ Maintained by the DigitalMeve Team.


