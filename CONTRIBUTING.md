# Contribuer à DigitalMeve

Merci de votre intérêt ! Pour contribuer :

# Contributing to DigitalMeve

Thanks for your interest! Please read this guide before opening an issue or PR.

## Setup
- Python 3.10+ recommended.
- Clone, then:  
  ```bash
  pip install -r requirements-dev.txt
  pre-commit install

Run all checks: pre-commit run --all-files && pytest -q


Branching & PR

Branch name: feat/<topic>, fix/<topic>, or docs/<topic>.

Keep PRs small, with clear description and tests.

CI must be green (lint + tests) before review.


Coding style

Black + Flake8 (max line length = 88).

Type hints where practical.

Tests with pytest, put them in tests/.


Releases

Bump version in pyproject.toml & src/digitalmeve/__init__.py.

Create a tag vX.Y.Z → publish workflow handles PyPI.


## Flux de contribution
1. Ouvrez une **issue** si vous proposez une nouvelle fonctionnalité ou signalez un bug.
2. **Forkez** le dépôt puis créez une branche : `git checkout -b feature/ma-feature`
3. Écrivez du code **clair** + **tests** dans `tests/`.
4. Vérifiez que la **CI est verte** (lint, format, tests).
5. Ouvrez une **Pull Request** vers `main` (remplissez le template).

## Standards
- Python **3.10+**
- **pytest** pour les tests (`pytest -q`)
- **ruff** (lint) : `ruff check .`
- **black** (format) : `black .` (ligne 100 max)

## Commit & PR
- Messages de commit clairs : `feat: …`, `fix: …`, `docs: …`, `chore: …`
- Une PR = un sujet. Ajoutez captures/logs si pertinent.

## Sécurité
- Ne joignez **jamais** de documents sensibles aux issues/PR.
- Pour signaler une vulnérabilité : voir `SECURITY.md`.

Merci ! 🙏
