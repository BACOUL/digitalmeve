# 🏆 Competitive Landscape — DigitalMeve vs Alternatives

This document compares **DigitalMeve** with existing solutions for document verification and certification.  
Goal: show why `.meve` is a **universal, open, and future-proof** standard.

---

## 🔑 Criteria for comparison

1. **Integrity** → Detect tampering (hash / cryptographic guarantees)  
2. **Timestamp** → Prove existence at a given time  
3. **Identity** → Associate a real issuer identity (Personal / Pro / Official)  
4. **Ease of Use** → Accessibility for non-technical users  
5. **Cost** → Free or costly (recurring fees, blockchain gas, etc.)  
6. **Transparency** → Open-source, auditable, interoperable  

---

## 📊 Comparative Table

| Solution               | Integrity (Hash) | Timestamp | Identity | Ease of Use | Cost | Transparency |
|-------------------------|-----------------|-----------|----------|--------------|------|--------------|
| **DigitalMeve**         | ✅ (SHA-256)    | ✅ (UTC ISO-8601) | ✅ Personal / Pro / Official | ✅ CLI · API · Web | Free (Personal) | ✅ Open-source |
| Blockchain notarization | ✅              | ✅ (block time)  | ❌ (pseudo-anonymous) | ❌ (wallets, gas fees) | 💰 Gas fees | Partial |
| DocuSign / AdobeSign    | ❌              | ❌               | ✅ (email/contract identity) | ✅ UI-friendly | 💰 Subscription | ❌ Closed-source |
| PGP/GPG Signatures      | ✅              | ❌               | ✅ (if key trusted) | ❌ (complex UX) | Free | ❌ Poor adoption |
| Hash in ZIP/Sidecar     | ✅              | ❌               | ❌ | ⚠️ Basic (manual) | Free | ❌ Not standardized |

---

## 🚀 Why DigitalMeve wins

- **Universal** → works with *any* file (PDF, PNG, TXT, binaries).  
- **Certified levels** → issuer can be Personal, Pro (email-verified), or Official (DNS/institution).  
- **Accessible** → CLI, Python API, and planned Web API.  
- **Lightweight** → no blockchain, no heavy infra, no proprietary lock-in.  
- **Open** → schema-based, easy to integrate in external systems.  
- **Future-ready** → designed for transparency logs and interoperability.

---

## 📚 References

- [schemas/meve-1.schema.json](../schemas/meve-1.schema.json)  
- [docs/specification.md](specification.md)  
- [docs/overview.md](overview.md)  
- [docs/examples.md](examples.md)  

---

✅ Next step: integrate a simplified **Comparison Table** into the **website** (landing page section “Why DigitalMeve?”).
