

# 🌍 DigitalMeve — The .MEVE Standard

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![Python](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **DigitalMeve — The first global platform to analyze and certify the authenticity of your documents.**  
> *“.MEVE is to proof what PDF is to documents.”*

---

## 📚 Table of Contents

- [About](#about)
- [Vision](#vision)
- [Levels of Certification](#levels-of-certification)
- [Specification — MEVE/1](#specification--meve1)
- [Install](#install)
- [Quick Start](#quick-start)
  - [Python API](#python-api)
  - [Command Line](#command-line)
- [API Reference (short)](#api-reference-short)
- [Project Structure](#project-structure)
- [Security](#security)
- [UX & Product](#ux--product)
- [Legal & Compliance](#legal--compliance)
- [Use Cases](#use-cases)
- [Business Model](#business-model)
- [Communication](#communication)
- [Roadmap](#roadmap)
- [30-Day Plan (MVP)](#30-day-plan-mvp)
- [Status](#status)
- [Contributing](#contributing)
- [License](#license)
- [More Docs](#more-docs)

---

## About

**DigitalMeve** defines **`.MEVE` (Memory Verified)** — a compact, human-readable proof that certifies a file’s **existence**, **integrity** and **issuer authenticity** in seconds, with **offline verification**.

---

## Vision

A single, universal proof format anyone can verify in under 2 seconds.  
Goal: make `.MEVE` the **global standard** for digital certification.

---

## Levels of Certification

- **Personal** — self-certified (existence proof).
- **Pro** — email-verified identity.
- **Official** — DNS/domain or institutional verification.

> The level is **computed by the verifier** (never self-declared) to prevent fraud.

---

## Specification — MEVE/1

The canonical manifest is a compact JSON (stable key order, UTF-8).  
Current generator returns:

```json
{
  "meve_version": "1.0",
  "issuer": "Personal",
  "timestamp": "2025-01-01T12:34:56Z",
  "metadata": {},
  "subject": {
    "filename": "document.pdf",
    "size": 123456,
    "hash_sha256": "..."
  },
  "hash": "...",
  "preview_b64": "..."
}

hash duplicates subject.hash_sha256 for convenience.

preview_b64 is a short Base64 preview for debugging/UX.

Optional sidecar: <filename>.meve.json (no change to the source file).


Design notes for future fields (Pro/Official issuers) live under docs/: Status, Key_ID, Signature (Ed25519), Schema_Hash, Verified_Domain, Doc-Len, Doc-Ref.


---

Install

pip install digitalmeve

Python ≥ 3.10 recommended.


---

Quick Start

Python API

from pathlib import Path
from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve, verify_identity

# 1) Generate a .MEVE proof, optionally write a sidecar JSON
proof = generate_meve(
    file_path="samples/invoice.pdf",
    outdir="out",                 # -> writes invoice.pdf.meve.json
    issuer="Personal",            # "Personal" | "Pro" | "Official"
    metadata={"purpose": "demo"}  # arbitrary metadata
)

# 2) Verify the proof (dict or path to .meve.json)
ok, info = verify_meve(proof, expected_issuer="Personal")
assert ok is True
assert info["subject"]["filename"] == "invoice.pdf"

# 3) Identity helper
assert verify_identity("ABC123") is True

Command Line

The CLI modules run everywhere (no console script needed):

# Generate
python -m digitalmeve.cli.generate path/to/file.pdf --issuer Personal --out out/

# Verify
python -m digitalmeve.cli.verify out/file.pdf.meve.json --issuer Personal


---

API Reference (short)

# src/digitalmeve/generator.py
def generate_meve(
    file_path: str | Path,
    outdir: str | Path | None = None,
    issuer: str = "Personal",
    metadata: dict | None = None,
) -> dict:
    """Return a MEVE/1 proof and optionally write <name>.meve.json"""

# src/digitalmeve/verifier.py
def verify_meve(meve: dict | str | Path, expected_issuer: str | None = None) -> tuple[bool, dict]:
    """Validate structure + content hash; returns (ok, info_or_error)"""

def verify_identity(identity: str) -> bool:
    """Simple helper used by tests/examples"""


---

Project Structure

.
├─ docs/                     # specifications & design notes (in progress)
├─ examples/                 # usage samples
├─ src/
│  └─ digitalmeve/
│     ├─ generator.py        # MEVE proof generator
│     ├─ verifier.py         # MEVE verifier
│     └─ cli/
│        ├─ generate.py      # python -m digitalmeve.cli.generate
│        └─ verify.py        # python -m digitalmeve.cli.verify
├─ tests/                    # pytest suite (green on CI)
├─ README.md  CHANGELOG.md  ROADMAP.md  SECURITY.md  CONTRIBUTING.md
└─ pyproject.toml  mkdocs.yml  LICENSE  Makefile

Quick links:

src/digitalmeve/generator.py · src/digitalmeve/verifier.py

src/digitalmeve/cli/ · examples/ · tests/

docs/ · ROADMAP.md · SECURITY.md · CONTRIBUTING.md



---

Security

Tamper-evident: any change to the source file invalidates the proof.

Offline verification: works without network access.

Transparency-ready: design compatible with Merkle-root logging.

Sidecar support: .meve.json avoids touching original files.

Clear errors: invalid structure, missing keys, issuer mismatch, hash mismatch, etc.


Future work: Ed25519 signatures, key rotation & revocation list, transparency log publishing.


---

UX & Product

Status badges: Personal (grey), Pro (blue), Official (green).

Drag-and-drop web verifier (planned) + simple CLI.

Exportable JSON proof; short Base64 preview for visual inspection.

Sensible free limits (e.g., 25–50 MB) and guidance on large files.



---

Legal & Compliance

GDPR-friendly: the project does not store user documents.

eIDAS/ESIGN note: .MEVE is a proof of existence/integrity, not a qualified e-signature.

Anti-confusion: .MEVE is not a notary/INPI replacement.
See also: SECURITY.md and LICENSE.



---

Use Cases

Individuals: authorship, photo/video evidence, timestamping drafts.
Professionals: invoices, quotes, contracts, IP pre-proof.
Institutions: diplomas, rulings, official communications.


---

Business Model

Free: personal proofs with quotas.

Pro: subscription (volume, API, dashboard).

Official: institutional licensing (DNS/domain verification, SLA).



---

Communication

Slogan: “DigitalMeve — The first global platform to analyze and certify the authenticity of your documents.”
Channels: landing page (EN/FR), short explainers, live demos, LinkedIn/Twitter/YouTube.


---

Roadmap

Phase 1 (MVP — active)

✅ Python generator & verifier (src/digitalmeve/)

✅ CI: linting, tests, publish

🚧 Web demo (drag-and-drop)

🚧 Docs site (mkdocs)


Phase 2 (≈6 months)

Email verification (Pro)

DNS verification (Official)

Certified PDF export

Public API & integrations


Phase 3 (1–2 years)

Standardization (ISO/AFNOR)

ERP/CRM/University integrations

Broad adoption



---

30-Day Plan (MVP)

[x] GitHub repo & structure

[x] Python API + tests (green)

[x] CI/CD (quality, tests, publish)

[ ] Landing page EN/FR & FAQ

[ ] Live demo & tutorials

[ ] Initial communication & beta users



---

Status

Current version: 1.7.0

Changelog · Releases · PyPI



---

Contributing

Issues and PRs are welcome!
Please read CONTRIBUTING.md and follow the code style.
Run pre-commit locally, then pytest before submitting.


---

License

MIT — see LICENSE.


---

More Docs

docs/ (specification & guides; in progress)

examples/

ROADMAP.md · SECURITY.md

mkdocs.yml


**Notes on links**
- All **internal anchors** now match GitHub’s exact IDs (e.g., `#30-day-plan-mvp` ✅).
- All **file/folder links** point to paths that exist in your repo (`docs/`, `examples/`, `src/digitalmeve/...`, `tests/`, `ROADMAP.md`, etc.).

If any specific file inside `docs/` is not yet created (e.g., `specification.md`), we safely link to the **folder** so the link is still valid today. When you add `docs/specification.md`, we can point directly to it.

