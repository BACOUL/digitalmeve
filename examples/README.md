# 📂 DigitalMeve — Examples

This folder contains **example files** and their corresponding **.meve proofs**, as well as helper scripts to regenerate and verify them.

---

## 📌 Structure

examples/ ├── files/       # input demo files (PDF, JPG, etc.) ├── proofs/      # generated .meve proofs (.json) ├── make_examples.sh   # script to generate example proofs ├── verify_examples.sh # script to verify all example proofs └── README.md    # this file

---

## 🛠 Usage

### 1. Generate proofs for example files

Run:

```bash
./make_examples.sh

This will create .meve.json proofs in the proofs/ folder for each file inside files/.


---

2. Verify all generated proofs

Run:

./verify_examples.sh

This will check all .meve.json files inside proofs/ and show whether they are valid.


---

📖 Documentation

For detailed examples and explanation of the proof structure, see:

Examples Guide

Specification

Verification Guide



---

✅ With these scripts, anyone can generate and verify live examples of DigitalMeve proofs in just a few seconds.
