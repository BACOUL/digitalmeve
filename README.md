
# 🌍 DigitalMeve — The .MEVE Standard

> The universal way to **certify** and **verify** the authenticity of your documents.

[![Quality](.github/badges/quality.svg)](.github/workflows/quality.yml)
[![Tests](.github/badges/tests.svg)](.github/workflows/tests.yml)
[![Publish](.github/badges/publish.svg)](.github/workflows/publish.yml)
[![Coverage](https://codecov.io/gh/BACOUL/digitalmeve/branch/main/graph/badge.svg)](https://codecov.io/gh/BACOUL/digitalmeve)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Quick links**:  
> • [Overview](docs/overview.md) • [Specification](docs/specification.md) • [Generator Guide](docs/generator-guide.md) • [Verifier Guide](docs/verification-guide.md) • [API Usage](docs/API_USAGE.md) • [Examples](docs/examples.md) • [Security](SECURITY.md) • [Roadmap](docs/roadmap.md)

---

## 📑 Table of Contents

1. [Overview](#overview)  
2. [Quick Installation](#quick-installation)  
3. [CLI Usage](#cli-usage)  
4. [Python Usage](#python-usage)  
5. [Features](#features)  
6. [Schema & Format](#schema--format)  
7. [Reproducible Examples](#reproducible-examples)  
8. [Certification Levels](#certification-levels)  
9. [Security](#security)  
10. [Web Integration (preview)](#web-integration-preview)  
11. [Development & Contribution](#development--contribution)  
12. [License](#license)

---

## Overview

**DigitalMeve** defines the `.meve` format to prove **existence**, **integrity** (SHA-256), **timestamp** (UTC) and **issuer** of any file.  
The format is **open**, **portable** (sidecar `.meve.json`) and **machine-verifiable** (JSON Schema).

---

## Quick Installation

```bash
pip install digitalmeve

> Requires Python 3.10+




---

CLI Usage

Generate a proof

digitalmeve generate path/to/file.pdf --issuer "Alice"

Creates a sidecar file.pdf.meve.json.

For PDF/PNG, also creates an embedded copy (e.g. file.meve.pdf).


Verify a proof

# From a sidecar
digitalmeve verify path/to/file.pdf.meve.json --expected-issuer "Alice"

# Or from the original file (tries embedded first, then sidecar)
digitalmeve verify path/to/file.pdf --expected-issuer "Alice"

Inspect (print JSON)

digitalmeve inspect path/to/file.pdf.meve.json


---

Python Usage

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

proof = generate_meve("mydoc.pdf", issuer="Alice")
ok, info = verify_meve(proof, expected_issuer="Alice")
print(ok, info["subject"]["hash_sha256"])

More examples: docs/API_USAGE.md


---

Features

🔐 SHA-256 hashing → guarantees file integrity

🕒 UTC timestamp (ISO-8601)

🧾 JSON Schema validation (schemas/meve-1.schema.json)

🧳 Sidecar .meve.json → works for any file type

🧩 CLI & Python API

🤖 CI/CD ready (GitHub Actions for tests, quality, publish)



---

Schema & Format

Official schema: schemas/meve-1.schema.json

Guides:

Specification

Generator Guide

Verifier Guide




---

Reproducible Examples

Scripts:

examples/make_examples.sh → generate proofs

examples/verify_examples.sh → verify proofs


Docs: docs/examples.md



---

Certification Levels

Personal → self-certification (existence only)

Pro → verified professional (email check)

Official → DNS / institutional verification



---

Security

Policy: SECURITY.md

Vulnerability disclosure: security@digitalmeve.com (response ≤72h)

Details on hashing, schema, Pro/Official verification, keys: see SECURITY.md



---

Web Integration (preview)

Planned FastAPI endpoints:

POST /generate → returns .meve.json (and/or embedded)

POST /verify → returns { ok, info }
See api/app.py and workflow API (build & smoke).



---

Development & Contribution

Guide: CONTRIBUTING.md

Code of Conduct: CODE_OF_CONDUCT.md

Governance: GOVERNANCE.md • Maintainers: MAINTAINERS.md



---

License

MIT

---

