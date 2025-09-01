# 🛡 DigitalMeve

[![PyPI version](https://img.shields.io/pypi/v/digitalmeve)](https://pypi.org/project/digitalmeve/)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Security](https://img.shields.io/badge/security-monitored-brightgreen)](SECURITY.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

DigitalMeve defines the **.meve format (Memory Verified)** to **hash, timestamp, and certify** any digital content.

---

## 📖 Table of Contents
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Use Cases](#-use-cases)
- [Documentation](#-documentation)
- [Security](#-security)
- [Business Model](#-business-model)
- [Roadmap](#-roadmap)
- [Legal & Compliance](#-legal--compliance)

---

## ⚙️ Installation
```bash
pip install digitalmeve


---

🚀 Quick Start

Generate proof:

from digitalmeve.core import generate_meve
meve = generate_meve("contract.pdf")
print(meve["subject"]["hash_sha256"])

Verify proof:

from digitalmeve.core import verify_meve
ok, info = verify_meve("contract.pdf.meve.json", expected_issuer="Personal")
print(ok, info)

👉 Full examples → docs/examples.md


---

📊 Use Cases

Individuals → authorship proof, timestamp agreements.

Professionals → contracts, invoices, IP protection.

Institutions → universities (certified diplomas), courts/notaries (judgments).



---

📚 Documentation

Overview

Specification

Verification Guide

Generator Guide

Security Model

Roadmap



---

🔐 Security

Tamper-proof → any byte change detected.

Verifier works offline (CLI & SDK).

Transparency log (planned).


👉 More details → docs/security.md
👉 Security Policy


---

💰 Business Model

Free → Individuals (Personal level).

Pro (paid) → Verified email/domain.

Official (licensed) → Institutions.


KPIs: verifications/day, invalid proofs ratio.


---

🛣 Roadmap

See docs/roadmap.md


---

⚖️ Legal & Compliance

eIDAS / ESIGN → .meve ensures integrity + timestamp.

GDPR → no personal content stored, only hashes.



---

✍️ Maintained under DigitalMeve
