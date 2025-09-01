Parfait 🙌 merci pour la confirmation.
Voici le README complet enrichi v1.7.0 avec :

✅ Badges dynamiques absolus

✅ Version indiquée dans le titre

✅ Tous les liens docs en relatif cliquable

✅ Structure cohérente (v9 enrichie + homogénéisée)



---

# 🌍 DigitalMeve — The .MEVE Standard (v1.7.0)

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 What is DigitalMeve?

**DigitalMeve** defines the universal **`.meve`** (*Memory Verified*) format.  
A `.meve` file certifies in **2 seconds**:

1. 📌 The **existence** of a document at a specific time  
2. 🔐 The **integrity** of the document (via SHA-256)  
3. ✅ The **authenticity** of the issuer (Personal / Pro / Official)  

👉 **Goal** → Make `.meve` the *“PDF of digital proof”* worldwide.  

---

## 📦 Installation

```bash
pip install digitalmeve


---

⚡ Quick Start

from digitalmeve import generate_meve, verify_meve

# 1) Generate a proof
meve_path = generate_meve(
    file_path="examples/sample.pdf",
    issuer="john.doe@example.com",
    meta={"purpose": "contract"}
)

# 2) Verify the proof
result = verify_meve(meve_path)
print(result.valid, result.issuer, result.hash)

📘 Guides

Generator Guide

Verification Guide



---

📚 Documentation

📘 Overview

⚙️ API Usage

🏗 Generator Guide

🔍 Verification Guide

📑 Specification

🛡 Security

🧩 Examples

📧 Pro Verification (email)

🌐 Official Verification (DNS)

🗺 Roadmap (docs)

🗺 Roadmap (root)


📜 Changelog → CHANGELOG.md


---

📂 Repository Tree

.github/                 → Workflows CI/CD (quality, tests, publish)
docs/                    → Documentation (specifications, guides…)
examples/                → Usage examples
schema/                  → JSON Schemas (MEVE/1) ← planned in v1.8
src/digitalmeve/         → Core library (generator / verifier)
tests/                   → Unit & integration tests

.editorconfig
.flake8
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MAINTAINERS.md
MANIFEST.in
Makefile
README.md
ROADMAP.md
SECURITY.md
mkdocs.yml
pyproject.toml
requirements.txt


---

📝 MEVE/1 — Field Summary (Draft)

Field	Meaning / Notes

status	Personal ｜ Pro ｜ Official
issuer	Email or domain
certified	self ｜ email ｜ dns
issued_at	ISO-8601 UTC timestamp
hash_sha256	Document integrity hash
schema_hash	Hash of the schema used
key_id	Public key id (future use)
id	Short MEVE proof id
signature	Ed25519 signature (planned)
meta	Filename, size (bytes), purpose, …
doc_len	Document length in bytes
verified_domain	Populated when DNS-verified
doc_ref	Internal reference / cross-link


📑 Full specification → Specification


---

🔑 Certification Levels

🟦 Personal → self-certification (existence proof only)

🟨 Pro → identity verified via email

🟩 Official → DNS-verified institution


✔ The certification level is always computed automatically.


---

🧩 Use Cases

👤 Individuals

Proof of authorship (art, photos, manuscripts)

Timestamped evidence (insurance, agreements)


💼 Professionals

Certified invoices, contracts, designs

Intellectual property pre-proof


🏛 Institutions

Universities → certified diplomas

Governments → official documents

Courts → legal contracts, judgments



---

🛡 Security

🔐 Tamper-proof: any modification invalidates the proof

⚡ Offline verification (CLI / WASM planned)

📦 Sidecar .meve.json for large files

🌳 Transparency log (Merkle root, planned)

🛑 Explicit error messages


See SECURITY.md


---

🛠 Development

🐍 Requires Python 3.10+

Run checks locally:


pre-commit run --all-files
pytest -q

📖 Contributing Guide

🤝 Code of Conduct

🛡 Security Policy

👥 Maintainers



---

🚀 Roadmap

✅ Implemented

.meve generator (CLI + Python API)

.meve verifier (CLI + Python API)

PyPI packaging & publish workflow

Unit & integration tests (pytest + CI)

Quality checks (flake8, pre-commit)

Legal docs (LICENSE, SECURITY, CONTRIBUTING, CoC)


🚧 Next

Pro verification (email)

Official verification (DNS)

Ed25519 signing + key management

Transparency log (Merkle root)

API backend (FastAPI) + dashboard

Certified PDF export


📌 Full roadmap → ROADMAP.md


---

📢 Communication

Slogan EN:
👉 “DigitalMeve — The first global platform to certify and verify the authenticity of your documents.”

Pitch:
💬 “Your documents, certified and verifiable in 2 seconds, anywhere in the world.”


---

⚖ License

This repository is licensed under the MIT License.
See LICENSE for details.


---

✍️ Maintained by the DigitalMeve Team

---

✅ Avec cette version tu as :  
- Les **badges dynamiques** (qualité, tests, publish, PyPI, downloads, license)  
- La **version** dans le titre  
- Les **liens docs relatifs** (donc cliquables sur GitHub)  
- Une structure enrichie et homogène  

👉 Tu veux que je t’en génère aussi directement le fichier `README.md` prêt à déposer dans ton repo ?

