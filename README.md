

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

The first universal format to **prove, certify, and verify** the authenticity of any digital file.  
`.meve` = **Memory Verified** → timestamp + hash + issuer certification.  

---

## 📑 Table of Contents  

- [🚀 Vision](#-vision)  
- [🔑 Levels of Certification](#-levels-of-certification)  
- [📂 Format Specification — MEVE/1](#-format-specification--meve1)  
- [⚙️ Usage](#️-usage)  
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

DigitalMeve creates a universal certification format: **`.meve` (Memory Verified)**.  

It proves in **2 seconds**:  
1. The existence of a document at a given date.  
2. Its integrity (SHA-256).  
3. The authenticity of the issuer.  

**Goal** → Make `.meve` the **“PDF of digital proof”**.  

---

## 🔑 Levels of Certification  

- **Personal** → Self-certification (existence only).  
- **Pro** → Email verified (real professional identity).  
- **Official** → DNS verified / institutional certification.  

⚡ Always computed automatically, never declared manually → impossible to fake.  

---

## 📂 Format Specification — MEVE/1  

Example of `.meve.json`:  

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

⚙️ Usage

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

Tamper-proof: any file change breaks the hash.

Metadata embedding or sidecar .meve.json.

Scalable: handles very large files.

Fraud detection: instant verification.



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

Governments → official docs.

Courts & notaries → contracts, rulings.



---

📜 Roadmap

Phase 1 (MVP): generator + verifier + hashing ✅

Phase 2: Pro email verification + certified PDF export

Phase 3: Official DNS verification + standardization



---

📢 Communication

Slogan:
👉 “DigitalMeve — Trust in every file.”

Pitch:
“Your documents, certified and verifiable in 2 seconds, anywhere.”

Channels:

Landing page (Framer).

Explainer videos.

Live demo.

LinkedIn / YouTube / Twitter.



---

⚖ License

MIT License. See LICENSE.


---

🛠 Contributing

Open issues for bugs/features.

Submit PRs with clear commits.

Follow CONTRIBUTING.md.



---

✅ Status

Current version: 1.7.0

Releases

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

📸 (Screenshots and diagrams to be added here)

---
