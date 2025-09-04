# 🌍 DigitalMeve — Overview

DigitalMeve defines the universal **`.meve` (Memory Verified)** format to **prove, certify, and verify** the authenticity of any digital document.

---

## 📂 What is a `.meve` file?

A `.meve` file is a lightweight, human-readable JSON container that includes:

- ✅ The **cryptographic hash** of the original document (SHA-256)
- ⏱️ A trusted **timestamp** (UTC ISO 8601)
- 🔏 A **digital signature** from the issuer (Ed25519)
- 🗂️ Optional **metadata** (filename, author, tags…)

---

## 🔑 Why DigitalMeve?

- 🌐 **Universal & interoperable** — works across files, apps, and platforms
- ⏱️ **Fast** — proof generated in under 2 seconds
- 🔐 **Secure** — tamper-proof integrity check (hash + signature)
- 🤝 **Simple** — lightweight JSON, easy to read and verify locally

---

## 🔒 Certification Levels

- **Personal** → self-issued proof (free)
- **Pro** → verified professional (email/domain)
- **Official** → verified organization (DNS/org key)

---

## 📚 Next Steps

- 👉 See [Specification](SPECIFICATION.md) for the formal `.MEVE/1` structure
- 👉 See [Examples](EXAMPLES.md) for concrete use cases and sample proofs
- 👉 See [Generator Guide](GENERATOR_GUIDE.md) to create proofs yourself

---

## 🌟 Final Goal

**DigitalMeve aims to become the “PDF of digital proof”** —
free for individuals, subscription for professionals,
and trusted licenses for institutions.
