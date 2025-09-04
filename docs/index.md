# 🌍 DigitalMeve — Documentation Index

Welcome to **DigitalMeve**, the `.MEVE` (Memory Verified) standard for timestamping, hashing, and certifying digital content.

---

## 📖 Introduction

DigitalMeve introduces a lightweight, universal format `.meve` that proves in less than 2 seconds:

- The existence of a file at a given time  
- The integrity of its content (via **SHA-256**)  
- The authenticity of the issuer (*Personal*, *Pro*, *Official*)  

---

## 📦 Installation

```bash
pip install digitalmeve


---

⚡ Quick Start

from digitalmeve.core import generate_meve, verify_meve

# Generate a proof
proof = generate_meve("contract.pdf", issuer="Personal")

# Verify it
ok, info = verify_meve(proof, expected_issuer="Personal")
print(ok, info["subject"]["filename"])


---

📚 Documentation Map

Overview → high-level intro to DigitalMeve

Specification → full format details (.MEVE/1)

Generator Guide → how to create .meve.json proofs

Verification Guide → how to check proofs locally

Pro Verification → email-verified identity (Pro)

Official Verification → DNS/org verified issuers

Examples → concrete usage samples



---

🔑 Certification Levels

Personal → self-certification (free)

Pro → verified professional (email/domain)

Official → verified institutions (DNS/org key)



---

🛡 Security

Tamper-proof (hash mismatch invalidates)

Works offline (local verify)

Transparency logs planned for rotation/revocation



---

🚀 Roadmap

Phase 1 (MVP) → generator + verifier

Phase 2 → Pro/Official onboarding, PDF export, API

Phase 3 → International standardization + SaaS integrations



---

📢 Final Goal

Make .MEVE the universal format of digital certification:

Free for individuals

Subscription for professionals

Institutional license for official issuers


👉 DigitalMeve — Trust in every file.

---
