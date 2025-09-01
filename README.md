
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

**DigitalMeve** defines the universal format **`.meve`** (Memory Verified) to **timestamp, hash and certify** any digital content.  

✔ Existence proof (UTC timestamp)  
✔ Integrity proof (SHA-256 hash)  
✔ Issuer proof (Personal / Pro / Official)  

👉 Goal: make `.meve` the **“PDF of digital proof”** worldwide.  

---

## 📦 Installation  

```bash
pip install digitalmeve


---

📑 Table of Contents

🚀 Vision

🔑 Certification Levels

📂 Format Specification

🛡 Security

📊 Use Cases

📜 Roadmap

📚 Documentation

🛠 Contributing

⚖ License

✅ Status



---

🚀 Vision

A lightweight, universal file format proving in 2 seconds:

1. The existence of a file at a given date.


2. Its integrity (hash SHA-256).


3. The authenticity of its issuer.




---

🔑 Certification Levels

Personal → self-certification (free, existence only).

Pro → verified professional email (paid).

Official → verified DNS / institution (green badge).


⚡ Levels are automatically computed by the verifier, never self-declared.


---

📂 Format Specification

Example of .meve.json:

{
  "meve_version": "1.0",
  "issuer": "Personal",
  "timestamp": "2025-08-30T12:34:56Z",
  "subject": {
    "filename": "contract.pdf",
    "size": 52344,
    "hash_sha256": "abcd1234..."
  },
  "hash": "abcd1234...",
  "metadata": {},
  "preview_b64": "..."
}

📖 Full spec → Specification


---

🛡 Security

Tamper-proof → any byte change invalidates the proof.

Verifier-first → runs locally (CLI / Python / browser WASM).

Transparency log → prevents backdating.

Sidecar JSON → scalable for large files (>50 MB).


📖 Details → Security


---

📊 Use Cases

👤 Individuals

Proof of authorship (art, manuscripts).

Insurance evidence (photos/videos).

Personal agreements.


👔 Professionals

Certified invoices & contracts.

Intellectual property pre-proof.

Developer code signing.


🏛 Institutions

Diplomas & academic records.

Legal contracts & court decisions.

Official documents.


📖 See → Examples


---

📜 Roadmap

Phase 1 (MVP, ✅ in progress)

.meve Generator (Python CLI + SDK).

.meve Verifier (CLI, web prototype).

SHA-256 + timestamp + issuer.


Phase 2 (next 6 months)

Pro email verification.

Official DNS verification.

Certified PDF export.

Public API.


Phase 3 (1–2 years)

International standardization (ISO/AFNOR).

ERP/CRM/university integrations.

Open-source desktop/mobile verifier.


📖 Full roadmap → Roadmap


---

📚 Documentation

Overview

API Usage

Generator Guide

Verification Guide

Specification

Security

Examples

Pro Verification

Official Verification



---

🛠 Contributing

We welcome contributions!

See Contributing

Follow Code of Conduct

Report issues → Bug report

Suggest features → Feature request



---

⚖ License

This repository is licensed under the MIT License.
See LICENSE.


---

✅ Status

Current version: 1.7.0

Releases: GitHub Releases

PyPI: digitalmeve



---

🌟 DigitalMeve — Trust in every file.

---

