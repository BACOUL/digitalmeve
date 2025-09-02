# 🌍 DigitalMeve — The .MEVE Standard

👉 *The first global platform to certify and verify the authenticity of your documents.*

[![Quality](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/quality.yml)
[![Tests](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/tests.yml)
[![Publish](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/BACOUL/digitalmeve/actions/workflows/publish.yml)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)](https://github.com/BACOUL/digitalmeve)
[![PyPI - Version](https://img.shields.io/pypi/v/digitalmeve.svg?label=DigitalMeve&logo=pypi)](https://pypi.org/project/digitalmeve/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/digitalmeve.svg?logo=python&label=Python)](https://pypi.org/project/digitalmeve/)
[![Downloads](https://pepy.tech/badge/digitalmeve)](https://pepy.tech/project/digitalmeve)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 2. 🚀 Patches Snapshot (already implemented)

DigitalMeve already includes a strong foundation:

- ✅ **Core library**: `generator.py` + `verifier.py`  
- ✅ **CLI**: `digitalmeve generate / verify / inspect`  
- ✅ **Tests**: `pytest` passing on Python 3.10 → 3.12  
- ✅ **Official Schema**: [`schemas/meve-1.schema.json`](schemas/meve-1.schema.json)  
- ✅ **CI/CD GitHub Actions**:  
  - [tests.yml](.github/workflows/tests.yml) (unit tests)  
  - [quality.yml](.github/workflows/quality.yml) (lint, ruff, black)  
  - [publish.yml](.github/workflows/publish.yml) (PyPI via OIDC)  
- ✅ **Quality**: linting, pre-commit hooks, coverage badge  
- ✅ **Docs**: overview, specification, guides, roadmap, security, API usage  
- ✅ **Examples**: real sample files + reproducible scripts (`examples/make_examples.sh`)  
- ✅ **Governance**: [LICENSE](LICENSE), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md)  

---

### 🔑 Main commands

```bash
# Generate a .meve.json proof
digitalmeve generate path/to/file.pdf --issuer "Alice"

# Verify a proof
digitalmeve verify file.pdf.meve.json --expected-issuer "Alice"

# Inspect a proof (human-readable summary)
digitalmeve inspect file.pdf.meve.json
