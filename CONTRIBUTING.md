# 🤝 Contributing to DigitalMeve

Thank you for your interest in contributing!
Please read this guide before opening an issue or pull request.

---

## 🛠️ Setup

- Python **3.10+** recommended.
- Clone the repository:
  ```bash
  git clone https://github.com/BACOUL/digitalmeve.git
  cd digitalmeve

Install dependencies:

pip install -r requirements-dev.txt

Install git hooks:

pre-commit install

Run all checks locally before committing:

pre-commit run --all-files && pytest -q



---

🌱 Branching & Pull Requests

Branch naming convention:

feat/<name> → new feature

fix/<name> → bug fix

docs/<name> → documentation


Keep PRs small and focused.

Each PR should include:

Clear description of the change

Tests (if applicable)

Updated docs (if needed)



✅ CI must be green (lint + tests) before review.


---

🎨 Coding Standards

Formatting: Black (line length = 88)

Linting: Ruff

ruff check .

Type hints: use them where practical

Tests: pytest → put tests in tests/



---

🚀 Releases

1. Bump version in:

pyproject.toml

src/digitalmeve/__init__.py



2. Commit with message:

chore(release): vX.Y.Z


3. Tag the release:

git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z


4. The publish workflow will handle build & upload to PyPI.




---

✅ Pull Request Checklist

Before submitting a PR, make sure:

[ ] Code is formatted with Black

[ ] Lint passes with Ruff

[ ] All tests pass with pytest

[ ] Docs / README updated if relevant

[ ] CI (tests + quality + publish) is green



---

🔒 Security

Never attach sensitive documents in issues/PRs.

To report a vulnerability, please use SECURITY.md.



---

🙌 Thanks!

Your contributions make DigitalMeve better.
We welcome new ideas, bug reports, documentation improvements, and code changes!

---
