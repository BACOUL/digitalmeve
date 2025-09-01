
# 🌍 DigitalMeve — The `.meve` Standard (v1.7.0)

[![PyPI](https://img.shields.io/pypi/v/digitalmeve.svg?label=PyPI%20package&logo=pypi)](https://pypi.org/project/digitalmeve/)
![Python](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![Security](https://img.shields.io/badge/security-policy-green)](https://github.com/BACOUL/digitalmeve/blob/main/SECURITY.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/BACOUL/digitalmeve/blob/main/LICENSE)

**DigitalMeve** defines the **`.meve` (Memory Verified)** format to **hash, timestamp, and certify** any digital file — fast ⚡, secure 🔐, and universal 🌍.

---

## Table of contents

- [What is `.meve`?](#what-is-meve)
- [Installation](#installation)
- [Quick start](#quick-start)
  - [Python SDK](#python-sdk)
  - [CLI usage](#cli-usage)
- [Documentation](#documentation)
- [Specification (MEVE/1)](#specification-meve1)
- [Security model](#security-model)
- [Issuer levels](#issuer-levels)
- [Project status](#project-status)
- [CI/CD & Publishing](#cicd--publishing)
- [Development](#development)
- [Project layout](#project-layout)
- [Roadmap](#roadmap)
- [Contributing & Code of conduct](#contributing--code-of-conduct)
- [License](#license)
- [Contact](#contact)

---

## What is `.meve`?

A portable, human-readable proof that ties a file to:

1. **Existence** at time *T* (UTC timestamp)  
2. **Integrity** of the **exact bytes** (SHA-256)  
3. **Issuer linkage** (Personal / Pro / Official) — **computed by the verifier**, never user-declared

**Goal:** make `.meve` the “**PDF of digital proof**”.

---

## Installation

```bash
pip install digitalmeve

Supported Python: 3.10, 3.11, 3.12
Platforms: Linux, macOS, Windows (CPython)


---

Quick start

Python SDK

from digitalmeve.core import generate_meve, verify_meve

# Generate an in-memory proof (and optionally write sidecar JSON)
proof = generate_meve("contract.pdf", issuer="Personal", outdir="out")
print(proof["subject"]["hash_sha256"])  # SHA-256 of the file

# Verify (path or dict)
ok, info = verify_meve("out/contract.pdf.meve.json", expected_issuer="Personal")
print("✅ Valid" if ok else "❌ Invalid", info)

Sidecar output: out/contract.pdf.meve.json

CLI usage

(Temporary reference CLIs kept at repository root)

# Generate a proof
python cli_generate.py path/to/file.pdf --out out --issuer Personal

# Verify a proof
python cli_verify.py out/file.pdf.meve.json --expected Personal


---

Documentation

Overview

API Usage

Generator Guide

Verification Guide

Specification

Security

Examples

Pro verification (email)

Official verification (DNS)

Roadmap



---

Specification (MEVE/1)

Minimal JSON (reference):

{
  "meve_version": "1.0",
  "issuer": "Personal",
  "timestamp": "2025-08-30T12:34:56Z",
  "metadata": {},
  "subject": {
    "filename": "sample.pdf",
    "size": 12345,
    "hash_sha256": "abcd1234..."
  },
  "hash": "abcd1234...",
  "preview_b64": "..."
}

Rules: SHA-256 over the full byte stream, UTC ISO-8601 timestamp, strict JSON, sidecar *.meve.json preferred.
➡️ Details: docs/specification.md


---

Security model

Tamper-proof: any byte change ⇒ different hash ⇒ verification fails

Verifier runs offline (no upload)

Transparency log & key management planned

Large files → prefer sidecar JSON
➡️ Details: docs/security.md



---

Issuer levels

Personal → self-asserted (free)

Pro → verified email/domain (paid) — MVP+1

Official → DNS/institution verified (licensed) — MVP+2


The level is computed by the verifier, not user-declared.
➡️ PRO.md • OFFICIAL.md


---

Project status

Current library version: 1.7.0

MEVE spec revision: MEVE/1 (meve_version: "1.0")

Test matrix: Python 3.10 / 3.11 / 3.12

CI: lint + unit tests + smoke, on PRs and pushes to main



---

CI/CD & Publishing

Workflows (see .github/workflows/):

✅ tests.yml — pytest on 3.10–3.12 + flake8 lint

✅ quality.yml — lightweight flake8 (PR signal)

✅ smoke.yml — fast sanity check

✅ publish.yml — PyPI publish on GitHub Release → Published using Trusted Publisher (OIDC)

✅ release-drafter.yml — drafts release notes from merged PRs


Release flow (maintainers)

1. Bump version in:

pyproject.toml

src/digitalmeve/__init__.py



2. Merge to main (CI must be green)


3. Create GitHub Release with tag vX.Y.Z


4. publish.yml builds sdist/wheel & publishes to PyPI (OIDC, no secrets)




---

Development

# Clone
git clone https://github.com/BACOUL/digitalmeve.git
cd digitalmeve

# Create venv (example)
python -m venv .venv && . .venv/bin/activate

# Install
python -m pip install -U pip
pip install -e .
pip install -r requirements-dev.txt

# Pre-commit (format/lint/hooks)
pre-commit install
pre-commit run --all-files

# Tests
pytest -q

Style & tools

Formatter: black (88 cols)

Lint: flake8

Tests: pytest

Hooks: pre-commit (see .pre-commit-config.yaml)



---

Project layout

digitalmeve/
├─ src/digitalmeve/           # core library
│  ├─ __init__.py
│  ├─ core.py                 # generator
│  └─ verifier.py             # verifier
├─ cli_generate.py            # reference CLI (gen)
├─ cli_verify.py              # reference CLI (verify)
├─ docs/                      # full documentation
├─ tests/                     # pytest suite
├─ .github/workflows/         # CI/CD
├─ pyproject.toml             # package metadata
├─ Makefile                   # convenience tasks
└─ SECURITY.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, ROADMAP.md, CHANGELOG.md


---

Roadmap

High-level milestones are tracked in
➡️ docs/roadmap.md


---

Contributing & Code of conduct

Contributing guide

Code of conduct

Security policy


Issue templates & PR template are provided under
➡️ .github/ISSUE_TEMPLATE/ & .github/PULL_REQUEST_TEMPLATE.md


---

License

Licensed under the MIT License.
➡️ LICENSE


---

Contact

DigitalMeve Core Team — contact@digitalmeve.com
Security: security@digitalmeve.com

---

Si tu veux, je peux aussi préparer un **CHANGES/CHANGELOG précis pour 1.7.0** et un petit **badge “Made for Framer site”**. Dis-moi et je te le fournis en patch direct.

