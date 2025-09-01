
# 🌍 DigitalMeve — The .MEVE Standard

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Description

**DigitalMeve** defines the universal format **`.meve`** (*Memory Verified*) to **timestamp, hash, and certify** any digital document.

🎯 **Mission**: make `.meve` the **“PDF of digital proof”**.

---

## 📦 Installation

```bash
pip install digitalmeve

> Requirement: Python 3.10+




---

⚡ Quick Start

Generate a .meve proof for a file and verify it:

from digitalmeve import generate_meve, verify_meve

# 1) Generate
meve_path = generate_meve(
    file_path="examples/sample.pdf",
    issuer="john.doe@example.com",   # or domain for OFFICIAL
    meta={"purpose": "draft-contract-v1"}
)
print("MEVE created:", meve_path)

# 2) Verify
result = verify_meve(meve_path)
assert result.valid
print(
    "valid:", result.valid,
    "| level:", result.level,         # PERSONAL / PRO / OFFICIAL
    "| algo:", result.hash_algo,      # SHA-256
    "| ts:", result.timestamp_iso
)

➡️ More details: Generator Guide • Verification Guide


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

Roadmap (docs) • Roadmap (root)



---

🔑 Certification Levels

PERSONAL → self-certification (existence proof only).

PRO → identity verified via email (real professional).

OFFICIAL → identity verified via DNS (institution / domain).


☑️ Certification level is always computed automatically by the verifier.


---

🛡 Security

Tamper-proof: any modification invalidates the .meve.

Strong hashing: SHA-256 by default.

Metadata embedding: inline (JSON) or sidecar .meve.json for large files.

Fraud detection: instant hash mismatch detection.


Details: Security • SECURITY.md


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

Courts → contracts, judgments, evidence.



---

🛠 Development

Run local checks:

pre-commit run --all-files
pytest -q

Project policies & guides:

CONTRIBUTING.md

CODE_OF_CONDUCT.md

SECURITY.md

MAINTAINERS.md

SUPPORT.md




---

📦 Releases & CI/CD

Current version: 1.7.0

Published automatically to PyPI

Workflow: version bump → tag → GitHub Actions → PyPI publish

Changelog: CHANGELOG.md


Workflows: Quality • Tests • Publish (see badges above).


---

🚀 Vision

A lightweight, human-readable format, verifiable in 2 seconds, recognized worldwide to prove:

1. The existence of a document at a given time,


2. The integrity of the document (hash),


3. The authenticity of the issuer (Personal / Pro / Official).



Slogan
👉 “DigitalMeve — The first global platform to certify and verify the authenticity of your documents.”

Pitch
“Your documents, certified and verifiable in 2 seconds, anywhere in the world.”


---

⚖ License

Distributed under the MIT License — see LICENSE.


---
