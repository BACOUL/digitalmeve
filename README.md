
# 🌍 DigitalMeve — The .MEVE Standard

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[![Security Policy](https://img.shields.io/badge/Security-Policy-blue)](SECURITY.md)
---

## 📑 Table of Contents
- [Vision](#-vision)  
- [Certification Levels](#-certification-levels)  
- [Format Specification](#-format-specification)
- [🔒 Security Policy](SECURITY.md)
- [💬 Support](SUPPORT.md)
- [Use Cases](#-use-cases)  
- [Business Model](#-business-model)  
- [Legal & Compliance](#-legal--compliance)  
- [Roadmap](#-roadmap)  
- [Documentation](#-documentation)  
- [Contributing](#-contributing)  
- [License](#-license)  
- [Status](#-status)  

---

## 🚀 Vision  

DigitalMeve introduces **`.meve` (Memory Verified)**:  
A lightweight and universal proof format ensuring in **2 seconds**:  
1. Existence of a file at a given time.  
2. Integrity of its exact bytes (SHA-256).  
3. Authenticity of the issuer (Personal / Pro / Official).  

**Goal** → make `.meve` the **“PDF of digital proof”** worldwide.  

---

## 🔑 Certification Levels  

- **Personal** → Self-certification (existence proof only).  
- **Pro** → Verified email identity (professional / company).  
- **Official** → Verified DNS / institutional domain.  

⚡ Levels are **computed automatically** by the verifier (never user-declared).  

---

## 📂 Format Specification  

See full spec → [docs/specification.md](./docs/specification.md)  

Minimal `.meve.json` structure:  
```json
{
  "meve_version": "1.0",
  "issuer": "Personal",
  "timestamp": "2025-08-30T12:34:56Z",
  "subject": {
    "filename": "sample.pdf",
    "size": 12345,
    "hash_sha256": "abcd1234..."
  },
  "hash": "abcd1234...",
  "metadata": {},
  "preview_b64": "..."
}


---

🛡 Security

Tamper-proof → any byte change invalidates the hash.

Verifier → works offline, CLI or browser (no forced upload).

Transparency log → prevents backdating (future).

Fallback → .meve.json sidecar for large files (>50MB).


More details → docs/security.md


---

📊 Use Cases

Individuals

Proof of authorship (art, manuscripts).

Timestamp for personal agreements.

Insurance evidence (photos/videos).


Professionals

Certified invoices, contracts, designs.

Intellectual property pre-proof.

Legal & compliance archives.


Institutions

Universities → certified diplomas.

Governments → official documents.

Courts / notaries → judgments & contracts.


Examples → docs/examples.md


---

💰 Business Model

Free → Individuals (Personal level).

Pro (paid) → Email/domain verified (API, dashboard).

Official (licensed) → Institutions (DNS, SLA).


KPIs → verifications/day, invalid proofs detected, verified domains, TTFV (Time-to-first-verify).


---

⚖ Legal & Compliance

eIDAS / ESIGN → .meve = integrity & existence proof, not a qualified e-signature.

RGPD/GDPR → no storage of documents, only minimal metadata.

CGU/AUP → no illegal or harmful content.



---

🗺 Roadmap

See docs/roadmap.md

Phase 1 (MVP) → generator + verifier, SHA-256, timestamp.

Phase 2 → Pro email verification, Official DNS verification, certified PDF export.

Phase 3 → International standardization, ERP/CRM/university integration.



---

📚 Documentation

Overview

Specification

Security

Examples

Generator Guide

Verification Guide

Pro Verification

Official Verification



---

🛠 Contributing

See → CONTRIBUTING.md

Open issues for bugs or features.

Submit PRs with tests & lint passing.

Follow coding standards (Black, Flake8, pytest).



---

⚖ License

Licensed under the MIT License.
See LICENSE.


---

✅ Status

Current version: 1.7.0

Release page: Releases

Tests: 



---

✍️ DigitalMeve — “The PDF of Digital Proof”

