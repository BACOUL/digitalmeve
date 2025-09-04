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

## Table of Contents

1. [Overview](#1-overview)
2. [Patches Snapshot](#2--patches-snapshot-already-implemented)
3. [TL;DR](#3--tldr)
4. [Quickstart (Install + CLI + Python)](#4--quickstart-install--cli--python)
5. [Features](#5--features-highlights)
6. [Documentation](#6--documentation)
7. [Examples](#7--examples-runnable)
8. [Certification Levels](#8--certification-levels)
9. [Security](#9--security-essentials)
10. [Use Cases](#10--use-cases)
11. [Roadmap](#11--roadmap-snapshot)
12. [Web Integration (planned)](#12--web-integration-planned)
13. [Development](#13--development-contribute)
14. [Releases](#14--releases)
15. [License](#15--license)

---

## 1. Overview

DigitalMeve provides a **fast and universal** way to certify & verify digital files using `.meve` proofs.

Verification ensures:
- **Integrity** → the document has not been tampered with (SHA-256).
- **Timestamp** → the proof contains a valid UTC ISO-8601 timestamp.
- **Issuer** → identity level (Personal / Pro / Official) is explicit and checkable.

---

## 2. 🚀 Patches Snapshot (already implemented)

- ✅ **Core library**: `generator.py` + `verifier.py`
- ✅ **CLI**: `digitalmeve generate / verify / inspect`
- ✅ **Tests**: `pytest` passing on Python 3.10 → 3.12
- ✅ **Official Schema**: [`schemas/meve-1.schema.json`](schemas/meve-1.schema.json)
- ✅ **CI/CD GitHub Actions**:
  - [tests.yml](.github/workflows/tests.yml) (unit tests)
  - [quality.yml](.github/workflows/quality.yml) (ruff, black)
  - [publish.yml](.github/workflows/publish.yml) (PyPI via OIDC)
- ✅ **Quality**: linting, pre-commit hooks, coverage badge
- ✅ **Docs**: overview, specification, guides, roadmap, security, API usage
- ✅ **Examples**: reproducible scripts (`examples/make_examples.sh`)
- ✅ **Governance**: [LICENSE](LICENSE), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md)

**Main CLI commands**
```bash
# Generate a .meve.json proof
digitalmeve generate path/to/file.pdf --issuer "Alice"

# Verify a proof
digitalmeve verify path/to/file.pdf.meve.json --issuer "Alice"

# Inspect a proof (human-readable summary)
digitalmeve inspect path/to/file.pdf.meve.json


---

3. 📖 TL;DR

DigitalMeve defines the universal format .meve (Memory Verified) to timestamp, hash, and certify digital documents.
Goal: make .meve the “PDF of digital proof.”

Why .meve? Existence (file existed), Integrity (SHA-256), Authenticity (issuer level), Metadata (optional), Portable (sidecar file.ext.meve.json).


---

4. 🔧 Quickstart (Install + CLI + Python)

# 1) Install (Python 3.10+)
pip install digitalmeve

# 2) CLI — generate / verify / inspect
digitalmeve generate path/to/file.pdf --issuer "Alice"
digitalmeve verify path/to/file.pdf.meve.json --issuer "Alice"
digitalmeve inspect path/to/file.pdf.meve.json

# 3) Python API — minimal usage
from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

proof = generate_meve("mydoc.pdf", issuer="Alice")
ok, info = verify_meve(proof, expected_issuer="Alice")
print(ok, info["subject"]["hash_sha256"])


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


Schema reference: MEVE/1 JSON Schema


---

7. 🧪 Examples (runnable)

Scripts:

./examples/make_examples.sh → generate sample proofs (invoice, photo, diploma)

./examples/verify_examples.sh → verify all generated proofs


Resources: examples/ · docs/examples.md


---

8. 🔑 Certification Levels

Personal → self-certification (existence only)

Pro → email verified (identity linked to a real professional)

Official → DNS/institution verified


⚡ The level is computed by the verifier — not self-declared.


---

9. 🛡 Security (Essentials)

Hashing (SHA-256) → tamper-evident; any change invalidates the proof

Schema validation (MEVE/1)

Pro verification → email magic-link

Official verification → DNS TXT _meve.<domain>

Ed25519-ready → key_id, signature fields (design)

Transparency-ready → compatible with future transparency logs

Disclosure & contact → see SECURITY.md



---

10. 📊 Use Cases

Individuals → authorship, timestamped evidence

Professionals → certified invoices/contracts, automation

Institutions → diplomas, tenders, legal archives



---

11. 🚀 Roadmap (snapshot)

Phase 1 (MVP) → generator + verifier, CI, schema v1

Phase 2 (≤6 months) → Pro/Official onboarding, certified PDF export, public API

Phase 3 (1–2 years) → standardization, integrations, transparency log


Details → docs/roadmap.md


---

12. 🌐 Web Integration (planned)

Future endpoints (Framer integration & external apps):

POST /api/generate → upload file + issuer → returns .meve.json

POST /api/verify → submit proof JSON → returns { ok, info }



---

13. 🧩 Development (contribute)

Dev quickstart:

pre-commit run --all-files
pytest -q

Guides & policies:
CONTRIBUTING.md · CODE_OF_CONDUCT.md · SECURITY.md


---

14. 📦 Releases

Current version: 1.7.1-dev

Auto-publish to PyPI (Trusted Publisher / OIDC)

Flow: version bump → tag → Actions → PyPI

Changelog: CHANGELOG.md



---

15. ⚖ License

MIT — see LICENSE.

> Housekeeping: no trailing spaces; exactly one blank line at end of file.



Tu peux maintenant coller ça dans `README.md`.
Si tu veux, je peux ensuite te proposer une petite variante avec **Table des matières cliquable** générée automatiquement (compatible GitHub/PyPI) ou ajouter un **badge de couverture automatique**.
