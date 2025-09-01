
# 🌍 DigitalMeve — The .MEVE Standard

Quality → https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml  
Tests → https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml  
Publish → https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml  
PyPI → https://pypi.org/project/digitalmeve/  
Python Versions → https://pypi.org/project/digitalmeve/  
Downloads → https://pepy.tech/project/digitalmeve  
License MIT → https://github.com/BACOUL/digitalmeve/blob/main/LICENSE  

---

## 📖 What is DigitalMeve?

**DigitalMeve** defines the universal format `.meve` (*Memory Verified*):  
a lightweight, human-readable file that proves in **2 seconds**:

1. The existence of a document at a given date.  
2. The integrity of the document (via SHA-256 hash).  
3. The authenticity of the issuer (Personal, Pro, Official).  

🎯 Goal: make `.meve` the **“PDF of digital proof”** worldwide.  

---

## 📂 Example of a `.meve.json`

```json
{
  "status": "Personal",
  "issuer": "john.doe@example.com",
  "issued_at": "2025-09-01T12:34:56Z",
  "hash_sha256": "8f9c1b3c...e7a",
  "meta": {
    "filename": "contract-v1.pdf",
    "size": 58231,
    "mime": "application/pdf"
  },
  "preview_b64": "JVBERi0xLjQKJ....",
  "id": "meve-0a92f3"
}


---

⚡ Quick Start

Generate and verify a .meve proof in Python:

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

➡️ Generator Guide → https://github.com/BACOUL/digitalmeve/blob/main/docs/generator-guide.md
➡️ Verification Guide → https://github.com/BACOUL/digitalmeve/blob/main/docs/verification-guide.md


---

📚 Documentation

📌 Current (GitHub)

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

🚀 Future (MkDocs site)

Overview → https://bacoul.github.io/digitalmeve/overview/
API Usage → https://bacoul.github.io/digitalmeve/api_usage/
Generator Guide → https://bacoul.github.io/digitalmeve/generator-guide/
Verification Guide → https://bacoul.github.io/digitalmeve/verification-guide/
Specification → https://bacoul.github.io/digitalmeve/specification/
Security → https://bacoul.github.io/digitalmeve/security/
Examples → https://bacoul.github.io/digitalmeve/examples/
Pro Verification → https://bacoul.github.io/digitalmeve/pro/
Official Verification → https://bacoul.github.io/digitalmeve/official/
Roadmap → https://bacoul.github.io/digitalmeve/roadmap/


---

📌 Project Status (v1.7.0)

✅ Core generator (generate_meve) — hash, timestamp, metadata
✅ Core verifier (verify_meve) — integrity + issuer check
✅ PyPI package published → https://pypi.org/project/digitalmeve/
✅ CI/CD (tests, quality, publish)
✅ Documentation & governance (MIT, CONTRIBUTING, SECURITY)

🚧 Next steps:

JSON Schema validation (schema/meve-1.schema.json)

Minimal API backend (FastAPI)

Framer landing site + demo



---

📑 MEVE/1 Specification (draft)

Field	Description

status	Personal | Pro | Official
issuer	Identity (email or domain)
issued_at	UTC timestamp (ISO 8601)
hash_sha256	Document integrity hash
id	Short MEVE ID
meta	Filename • Size • Mime type
preview_b64	Base64 preview of first bytes


Full spec → https://github.com/BACOUL/digitalmeve/blob/main/docs/specification.md


---

🔑 Certification Levels

Personal → self-certification (existence proof only).

Pro → email-verified identity.

Official → DNS-verified institution/domain.


☑️ The level is automatically computed by the verifier (never self-declared).


---

🌐 API (coming soon)

POST /generate → upload file + issuer → returns .meve.json.
POST /verify → submit proof → returns { ok, level, issuer, timestamp }.


---

🛣 Roadmap

Phase 1 (MVP) → generator, verifier, CI/CD, PyPI (done)

Phase 2 (6 months) → email/DNS verification, PDF export, SaaS API (planned)

Phase 3 (1–2 years) → ISO/AFNOR standardization, ERP/CRM integrations, adoption (goal)



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

Contributing → https://github.com/BACOUL/digitalmeve/blob/main/CONTRIBUTING.md
Code of Conduct → https://github.com/BACOUL/digitalmeve/blob/main/CODE_OF_CONDUCT.md
Security Policy → https://github.com/BACOUL/digitalmeve/blob/main/SECURITY.md


---

🚀 Vision

A universal proof format, as simple and portable as PDF, but for existence & authenticity.

Slogan
👉 DigitalMeve — The first global platform to certify and verify the authenticity of your documents.

Pitch
Your documents, certified and verifiable in 2 seconds, anywhere in the world.


---

⚖ License

Distributed under the MIT License → https://github.com/BACOUL/digitalmeve/blob/main/LICENSE


---

✍️ Maintained by DigitalMeve Team •
