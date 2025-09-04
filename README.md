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

## 📑 Table of Contents

1. [Overview](#1-overview)  
2. [🚀 Patches Snapshot](#2--patches-snapshot-already-implemented)  
3. [📖 TL;DR](#3--tl-dr)  
4. [🔧 Quickstart](#4--unified-quickstart-install--cli--python)  
5. [✨ Features](#5--features-highlights)  
6. [📚 Documentation](#6--documentation)  
7. [🧪 Examples](#7--examples-runnable)  
8. [🔑 Certification Levels](#8--certification-levels)  
9. [🛡 Security](#9--security)  
10. [📊 Use Cases](#10--use-cases)  
11. [🚀 Roadmap](#11--roadmap-snapshot)  
12. [🌐 Web Integration](#12--web-integration-planned)  
13. [💻 Development & Contribution](#13--development--contribution)  
14. [📦 Releases](#14--releases)  
15. [⚖ License](#15--license)  

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
- ✅ **Official Schema**: [`schemas/meve-1.schema.json`](schemas/meve-1.schema.json)
- ✅ **CI/CD GitHub Actions**:
  - [tests.yml](.github/workflows/tests.yml)
  - [quality.yml](.github/workflows/quality.yml)
  - [publish.yml](.github/workflows/publish.yml)
- ✅ **Docs**: overview, specification, guides, roadmap, security, API usage
- ✅ **Examples**: reproducible scripts (`examples/make_examples.sh`)
- ✅ **Governance**: [LICENSE](LICENSE), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md)

---

## 3. 📖 TL;DR

DigitalMeve defines the universal format `.meve` (Memory Verified) to timestamp, hash, and certify digital documents.  
👉 Goal: make `.meve` the **“PDF of digital proof”**.

Why `.meve`? **Existence** (file existed), **Integrity** (SHA-256), **Authenticity** (issuer visible), **Metadata** (optional), **Portable** (sidecar JSON).

---

## 4. 🔧 Unified Quickstart (Install + CLI + Python)

```bash
# Install
pip install digitalmeve

# CLI
digitalmeve generate path/to/file.pdf --issuer "Alice"
digitalmeve verify path/to/file.pdf.meve.json --issuer "Alice"
digitalmeve inspect path/to/file.pdf.meve.json
