
# 🌍 DigitalMeve — The .MEVE Standard

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/BACOUL/digitalmeve/blob/main/LICENSE)

---

## 📖 What is DigitalMeve?

**DigitalMeve** defines the universal format `.meve` (*Memory Verified*):  
a lightweight, human-readable file that proves in **2 seconds**:

1. The existence of a document at a given date.  
2. The integrity of the document (via SHA-256 hash).  
3. The authenticity of the issuer (Personal, Pro, Official).  

🎯 Goal: make `.meve` the **“PDF of digital proof”** worldwide.  

---

## 📚 Documentation

- [Overview](https://github.com/BACOUL/digitalmeve/blob/main/docs/overview.md)  
- [API Usage](https://github.com/BACOUL/digitalmeve/blob/main/docs/API_USAGE.md)  
- [Generator Guide](https://github.com/BACOUL/digitalmeve/blob/main/docs/generator-guide.md)  
- [Verification Guide](https://github.com/BACOUL/digitalmeve/blob/main/docs/verification-guide.md)  
- [Specification](https://github.com/BACOUL/digitalmeve/blob/main/docs/specification.md)  
- [Security](https://github.com/BACOUL/digitalmeve/blob/main/docs/security.md)  
- [Examples](https://github.com/BACOUL/digitalmeve/blob/main/docs/examples.md)  
- [Pro Verification](https://github.com/BACOUL/digitalmeve/blob/main/docs/PRO.md)  
- [Official Verification](https://github.com/BACOUL/digitalmeve/blob/main/docs/OFFICIAL.md)  
- [Roadmap (docs)](https://github.com/BACOUL/digitalmeve/blob/main/docs/roadmap.md) • [Roadmap (root)](https://github.com/BACOUL/digitalmeve/blob/main/ROADMAP.md)

---

## ⚡ Quick Start

Generate and verify a `.meve` proof in Python:

```python
from digitalmeve import generate_meve, verify_meve

# 1) Generate
meve_path = generate_meve(
    file_path="examples/sample.pdf",
    issuer="john.doe@example.com",
    meta={"purpose": "contract-v1"}
)

# 2) Verify
result = verify_meve(meve_path)
print(result.valid, result.level, result.timestamp_iso)

➡️ Generator Guide
➡️ Verification Guide


---

🔑 Certification Levels

Personal → self-certification (existence proof only).

Pro → email-verified identity.

Official → DNS-verified institution/domain.


☑️ The level is automatically computed by the verifier (never self-declared).


---

📊 Use Cases

👤 Individuals → authorship, timestamped photos/videos, personal evidence
👔 Professionals → certified invoices, contracts, IP pre-proof
🏛 Institutions → diplomas, court judgments, official documents


---

🛠 Development

Run local checks:

pre-commit run --all-files
pytest -q

Contributing

Code of Conduct

Security Policy



---

🚀 Vision

A universal proof format, as simple and portable as PDF, but for existence & authenticity.

Slogan
👉 DigitalMeve — The first global platform to certify and verify the authenticity of your documents.

Pitch
Your documents, certified and verifiable in 2 seconds, anywhere in the world.


---

⚖ License

Distributed under the MIT License → LICENSE


---

✍️ Maintained by DigitalMeve Team • Repo → https://github.com/BACOUL/digitalmeve

---

# 📄 `LINKS.md` (backup avec toutes les URLs en clair)

```markdown
# 🔗 DigitalMeve — Links Backup

This file contains all important links in raw format (no Markdown)  
to avoid copy-paste issues with some editors.

---

## 📚 Documentation

Overview → https://github.com/BACOUL/digitalmeve/blob/main/docs/overview.md  
API Usage → https://github.com/BACOUL/digitalmeve/blob/main/docs/API_USAGE.md  
Generator Guide → https://github.com/BACOUL/digitalmeve/blob/main/docs/generator-guide.md  
Verification Guide → https://github.com/BACOUL/digitalmeve/blob/main/docs/verification-guide.md  
Specification → https://github.com/BACOUL/digitalmeve/blob/main/docs/specification.md  
Security → https://github.com/BACOUL/digitalmeve/blob/main/docs/security.md  
Examples → https://github.com/BACOUL/digitalmeve/blob/main/docs/examples.md  
Pro Verification → https://github.com/BACOUL/digitalmeve/blob/main/docs/PRO.md  
Official Verification → https://github.com/BACOUL/digitalmeve/blob/main/docs/OFFICIAL.md  
Roadmap (docs) → https://github.com/BACOUL/digitalmeve/blob/main/docs/roadmap.md  
Roadmap (root) → https://github.com/BACOUL/digitalmeve/blob/main/ROADMAP.md  

---

## 📦 Project

Repo → https://github.com/BACOUL/digitalmeve  
PyPI → https://pypi.org/project/digitalmeve/  
Downloads → https://pepy.tech/project/digitalmeve  
License → https://github.com/BACOUL/digitalmeve/blob/main/LICENSE  
Contributing → https://github.com/BACOUL/digitalmeve/blob/main/CONTRIBUTING.md  
Code of Conduct → https://github.com/BACOUL/digitalmeve/blob/main/CODE_OF_CONDUCT.md  
Security Policy → https://github.com/BACOUL/digitalmeve/blob/main/SECURITY.md  

---

## 🛠 CI/CD Workflows

Quality → https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml  
Tests → https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml  
Publish → https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml


---

