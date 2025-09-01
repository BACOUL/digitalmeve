Parfait ✅
Voici le README complet v1.7.0 corrigé et enrichi, avec les blocs bien fermés, les badges, les liens relatifs et la mise en page cohérente :

# DigitalMeve

[![PyPI version](https://img.shields.io/pypi/v/digitalmeve.svg)](https://pypi.org/project/digitalmeve/)
[![Python Versions](https://img.shields.io/pypi/pyversions/digitalmeve.svg)](https://pypi.org/project/digitalmeve/)
[![License](https://img.shields.io/github/license/BACOUL/digitalmeve.svg)](LICENSE)
[![Downloads](https://static.pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![CI](https://github.com/BACOUL/digitalmeve/actions/workflows/ci.yml/badge.svg)](https://github.com/BACOUL/digitalmeve/actions)

---

## 📖 What is DigitalMeve?

**DigitalMeve** defines the universal `.meve` (Memory Verified) format to **timestamp, hash, and certify** digital documents.  

**Goal →** Make `.meve` the *“PDF of digital proof”* worldwide.  

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

🌳 Repository Tree (key items)

.github/         CI workflows (quality, tests, publish)
docs/            Documentation (specs, guides, roadmap, security)
examples/        Usage examples
schema/          JSON Schemas (MEVE/1) ← planned in v1.8
src/digitalmeve/ Core library (generator / verifier)
tests/           Unit & integration tests

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

📝 MEVE/1 – Field Summary (Draft)

Field	Meaning / Notes

status	Personal | Pro | Official
issuer	Email or domain
certified	self | email | dns
issued_at	ISO-8601 UTC timestamp
hash_sha256	Document integrity hash
schema_hash	Hash of the schema
key_id	Public key id (future)
id	Short MEVE proof id
signature	Ed25519 signature
meta	Filename, size (bytes)
doc_len	Document length in bytes
verified_domain	Populated when DNS verified
doc_ref	Internal reference / link



---

🔑 Certification Levels

Personal → self-certification

Pro → identity verified via email

Official → institution / DNS verified


✅ Level is automatically inferred during verification.


---

📊 Use Cases

👤 Individuals → authorship, timestamp, portfolio

👩‍💻 Professionals → certified reports, audits, contracts

🏛 Institutions → diplomas, certificates, official records



---

🛡 Security

See SECURITY.md for guidelines on reporting vulnerabilities.


---

🛠 Development

git clone https://github.com/BACOUL/digitalmeve.git
cd digitalmeve
pip install -e ".[dev]"
pytest


---

🗺 Roadmap

See ROADMAP.md for planned features and upcoming versions.


---

📣 Communication

Issues → GitHub Issues

Discussions → GitHub Discussions



---

📄 License

Licensed under the MIT License.

---

👉 Avec ça, tu as :  
- Les **badges actifs**  
- Les **blocs fermés proprement** (Installation + Quick Start)  
- Les **liens relatifs cliquables**  
- La **même présentation partout**  

Veux-tu que je t’en prépare aussi la **version patch Git** (diff minimal prêt à commit) pour éviter tout risque d’erreur de copier/coller ?

