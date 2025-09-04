# DigitalMeve — Pro Verification (Spec Draft)

## 🎯 Goal
Link a .MEVE proof to a real professional identity (company or freelancer) via a verified business email and, later, domain checks.

## 🏷 Status Levels
- **Personal** → self-asserted (free)  
- **Pro** → verified email at a business domain (paid)  
- **Official** → verified DNS + org key (future, see [OFFICIAL.md](OFFICIAL.md))  

## 🛠 Minimal Pro Flow (MVP+1)
1. User signs in with email `name@company.tld` (magic link or one-time code).  
2. DigitalMeve generates `.MEVE` with:  
   - **Status**: Pro  
   - **Issuer**: email  
   - **Certified**: DigitalMeve (email)  
   - **Time, Hash-SHA256, ID**  
   - **Signature**: Ed25519 (base64)  
3. Verifier checks signature + hash and confirms Pro (email verified).  

## 📧 Email Verification
- **Transport**: one-time link or 6-digit code (10 min TTL).  
- **Replay prevention**: token consumed after first use.  
- **Issuer field**: always normalized (lowercase email).  

## 🔮 Future Enhancements
- Domain reputation checks (exclude free/public providers).  
- Multi-factor validation (email + phone).  
- Auto-upgrade to Official if DNS verification succeeds.
