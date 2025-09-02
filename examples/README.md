# 📂 DigitalMeve — Examples

This folder contains **reproducible examples** of `.meve.json` proofs.

---

## 1. Contract Proof
Input file: `contract.pdf`  
Generated proof: [`contract.pdf.meve.json`](contract.pdf.meve.json)

Command used:
```bash
digitalmeve generate examples/contract.pdf --issuer "demo@digitalmeve.test" --outdir examples/

Verification:

digitalmeve verify examples/contract.pdf.meve.json --expected-issuer "demo@digitalmeve.test"


---

2. Photo Proof

Input file: photo.jpg
Generated proof: photo.jpg.meve.json

Command used:

digitalmeve generate examples/photo.jpg --issuer "alice@example.com" --outdir examples/


---

3. Diploma Proof

Input file: diploma.pdf
Generated proof: diploma.pdf.meve.json

Command used:

digitalmeve generate examples/diploma.pdf --issuer "university@example.org" --outdir examples/


---

🔄 Re-generate all proofs

You can re-generate all example proofs with:

bash scripts/make_examples.sh
