# 🌍 DigitalMeve — The .MEVE Standard

👉 *The first global platform to certify and verify the authenticity of your documents.*

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)](https://codecov.io/gh/BACOUL/digitalmeve)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


## 📑 Table of Contents

1. [Overview](#overview)
2. [🚀 Patches Snapshot](#patches)
3. [📖 TL;DR](#tldr)
4. [🔧 Quickstart](#quickstart)
5. [✨ Features](#features)
6. [📚 Documentation](#documentation)
7. [🧪 Examples](#examples)
8. [🔑 Certification Levels](#certification-levels)
9. [🛡 Security](#security)
10. [📊 Use Cases](#use-cases)
11. [🚀 Roadmap](#roadmap)
12. [🌐 Web Integration](#web-integration)
13. [💻 Development & Contribution](#development)
14. [📦 Releases](#releases)
15. [⚖ License](#license)

---

<a id="overview"></a>
## 1. Overview

**DigitalMeve** provides a **fast and universal** way to verify the authenticity of any `.meve` proof.

Verification ensures:
- **Integrity** → the document has not been tampered with (SHA-256 validation).
- **Timestamp** → the proof contains a valid UTC timestamp.
- **Issuer** → the identity level (Personal, Pro, Official) matches expectations.

---

<a id="patches"></a>
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

<a id="tldr"></a>
## 3. 📖 TL;DR

**DigitalMeve** defines the universal format `.meve` (Memory Verified) to timestamp, hash, and certify digital documents.

👉 Goal: make `.meve` the **“PDF of digital proof”**.

Why `.meve`?
- **Existence** → the file existed at a given time.
- **Integrity** → SHA-256 hash guarantees no tampering.
- **Authenticity** → issuer is visible.
- **Metadata** → optional custom key/values.
- **Portable** → sidecar `.meve.json` works with any file type.
