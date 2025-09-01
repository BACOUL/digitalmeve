
# 🌍 DigitalMeve — The .MEVE Standard

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)  
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=PyPI&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![Python](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve/month)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Description  

**DigitalMeve** — The `.MEVE` Standard: Certified Digital Memory.  

The first universal format to **prove, certify, and verify** the authenticity of any digital document.  
DigitalMeve introduces `.meve` (Memory Verified), a lightweight, universal file to **timestamp, hash, and certify** any document.  

---

## 📑 Table of Contents  

- [🚀 Vision](#-vision)  
- [🔑 Levels of Certification](#-levels-of-certification)  
- [📂 Format Specification — MEVE/1](#-format-specification--meve1)  
- [⚙️ Quickstart](#️-quickstart)  
  - [CLI](#cli)  
  - [Python API](#python-api)  
- [🛡 Security](#-security)  
- [📊 Use Cases](#-use-cases)  
- [📜 Roadmap](#-roadmap)  
- [📢 Communication](#-communication)  
- [⚖ License](#-license)  
- [🛠 Contributing](#-contributing)  
- [✅ Status](#-status)  
- [📚 Documentation](#-documentation)  
- [🌟 Final Goal](#-final-goal)  

---

## 🚀 Vision  

**DigitalMeve** creates a new certification format: **`.meve` (Memory Verified)**.  
In **2 seconds**, `.meve` proves:  

1. The existence of a document at a given time.  
2. Its integrity (via SHA-256).  
3. The authenticity of its issuer (Personal, Pro, Official).  

👉 The ambition: make `.meve` the **“PDF of digital proof”**.  

---

## 🔑 Levels of Certification  

- **Personal** → Self-certification (existence only).  
- **Pro** → Email verified (real professional identity).  
- **Official** → DNS verified / institution (official certification).  

⚡ Certification is **computed automatically** by DigitalMeve → impossible to fake.  

---

## 📂 Format Specification — MEVE/1  

Example of `.meve.json` structure:  

```json
{
  "meve_version": "1.0",
  "issuer": "Personal",
  "timestamp": "2025-09-01T12:34:56Z",
  "subject": {
    "filename": "document.pdf",
    "size": 1048576,
    "hash_sha256": "..."
  },
  "hash": "...",
  "preview_b64": "...",
  "metadata": {}
}


---

⚙️ Quickstart

CLI

# Generate proof
digitalmeve generate mydoc.pdf --out out/

# Verify proof
digitalmeve verify out/mydoc.pdf.meve.json

Python API

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

proof = generate_meve("mydoc.pdf", outdir="out", issuer="DigitalMeve Demo")
ok, info = verify_meve("out/mydoc.pdf.meve.json", expected_issuer="DigitalMeve Demo")

print("Valid:", ok)
print("Details:", info)


---

🛡 Security

Tamper-proof: if the file changes, hash changes → .meve invalid.

Metadata embedding or .meve.json sidecar.

Scalable: works for very large files.

Detection: instant fraud detection.



---

📊 Use Cases

🧑‍💻 Individuals

Proof of creation (art, photos, manuscripts).

Timestamp for private agreements.

Insurance evidence (videos, photos).


👔 Professionals

Certified invoices, quotes, contracts.

Proof of authorship (designs, code).

Intellectual property pre-proof.


🏛 Institutions

Universities → certified diplomas.

Governments → official documents.

Courts & notaries → contracts, rulings.



---

📜 Roadmap

Phase 1 (MVP, 1–2 months)

Generator .meve (site + script).

Verifier .meve (drag & drop site).

SHA-256 hash + UTC timestamp + Ed25519 signature.


Phase 2 (6 months)

Pro email verification.

Official DNS verification.

Export certified PDF with DigitalMeve footer.

Public API for third-party integration.


Phase 3 (1–2 years)

International standardization (ISO/AFNOR).

ERP / CRM / University integrations.

Large-scale adoption.



---

📢 Communication

Slogan:
👉 “DigitalMeve — Trust in every file.”

Pitch:
“Your documents, certified and verifiable in 2 seconds, anywhere in the world.”

Channels:

Landing page (Framer).

Explainer videos (EN/FR).

Live demo (upload → verify).

LinkedIn / YouTube / Twitter campaigns.



---

⚖ License

This repository is licensed under the MIT License.
See LICENSE.


---

🛠 Contributing

We welcome contributions!

Open issues for bugs or feature requests.

Submit pull requests with clear commits.

Follow CONTRIBUTING.md.



---

✅ Status

Current version: 1.7.0

Release page: Releases

Tests: 



---

📚 Documentation

Specification

Security

Examples

Roadmap

Generator Guide

Verification Guide



---

🌟 Final Goal

Make .MEVE the universal format of digital certification:

Free for individuals.

Subscription/API for professionals.

License for institutions.


DigitalMeve — Trust in every file.

---
