# DigitalMeve — Official Verification (Spec Draft)

## 🎯 Goal

Issue `.MEVE` with official provenance (university, court, administration, notary, etc.).

---

## 🔒 Trust Mechanism

- DNS ownership of the organization’s domain  
- Optional: Org signing key (Ed25519) stored server-side (HSM/KeyVault)  

---

## 🛠 Minimal Official Flow (MVP+2)

1. Org admin requests verification for `org.tld`.  
2. DigitalMeve generates a unique token (challenge), e.g. `meve-verify=<nonce>`.  
3. Admin adds a DNS TXT record at `_meve.org.tld`.  
4. Verifier resolves DNS and validates the challenge.  
5. DigitalMeve issues `.MEVE` with:  
   - Status: **Official**  
   - Issuer: org name / domain  
   - Certified: DigitalMeve (dns)  
   - Signature: Ed25519  
   - (Optional) Co-sign with Org key and embed `Org-Signature` field  

---

## ♻ Revocation / Rotation

- DNS record removal → downgrade new proofs to **Pro**  
- Org key rotation → include **Key-ID** in proofs  

---

## 👁 Display

The public verifier shows a green **Official** badge with the verified domain (e.g. `university.edu`).  

---

## 📌 Notes

- No legal guarantee is implied.  
- `.MEVE` ties the content hash to a verified issuer at a given time.
