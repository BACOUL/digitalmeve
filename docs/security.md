# 🔒 DigitalMeve — Security Model

This document describes what `.MEVE` guarantees, what it does **not** guarantee, and the threat model with mitigations.

---

## ✅ What MEVE Proves

- **Existence** of a file at a given point in time (**UTC timestamp**).  
- **Integrity** of the file content (**SHA-256 hash**).  
- **Issuer linkage** (Personal / Pro / Official) — automatically computed by the verifier.  

---

## ❌ What MEVE Does *Not* Prove

- The **civil/legal identity** of a person (unless verified Pro/Official flows are used).  
- The **truthfulness of the content**; MEVE certifies **bytes**, not meaning.  

---

## ⚠️ Threats & Mitigations

- **Tampering** → any byte change results in a different SHA-256 → verification fails.  
- **Visual tricks** → verifier always checks raw content bytes, not rendering.  
- **Large files (>50 MB)** → use sidecar `*.meve.json` instead of metadata embedding.  
- **Clock issues** → all timestamps stored in **UTC ISO-8601**; future option: trusted timestamp authority.  
- **Key management (future)** → Pro/Official issuers will use dedicated signing keys and revocation lists.  

---

## 📣 Responsible Disclosure

We take security seriously. Please report vulnerabilities privately:

- 📧 Email: `security@digitalmeve.example`  
- ⏱ Expected first response: **≤ 72h**  

⚠️ **Do not disclose vulnerabilities publicly** before a fix or mitigation is available.  

---

## 🗂 Scope

- Core library: `/src/digitalmeve`  
- Reference verifier & generator  
- CI workflows: `.github/workflows`  

---

## 🔐 Privacy

- The verifier **never stores document content**.  
- Only the **hash** and minimal **metadata** appear in proofs.  
- No centralized storage: proofs remain under the user’s control.  

---

👉 For technical details, see [Specification](SPECIFICATION.md).  
👉 For adoption roadmap, see [Roadmap](ROADMAP.md).
