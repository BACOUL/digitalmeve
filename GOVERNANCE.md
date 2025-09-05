# Governance — DigitalMeve

## Maintainer
- **@BACOUL** (Jeason Bacoul) — final authority on technical and release decisions.

## Decision Making
- Technical changes (features, dependencies, architecture) are decided by the maintainer.
- Pull Requests must pass CI (quality + tests) and are merged after review.
- Security fixes are prioritized and may be merged with expedited review.

## Contributions
- Everyone is welcome to open issues and PRs.
- PRs should stay focused, include tests (when applicable), and update docs if needed.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for coding standards and release flow.

## Releases
- Versioning: [Semantic Versioning](https://semver.org/).
- Source of truth: `pyproject.toml` and `src/digitalmeve/__init__.py`.
- Only the maintainer publishes to PyPI (via GitHub Actions / OIDC).

## Security
- Report vulnerabilities to **security@digitalmeve.com** (see [SECURITY.md](SECURITY.md)).
- Security issues may be handled privately until a fix is available.

## Changes to Governance
- This document may evolve to include additional maintainers or a steering group as the project grows.
