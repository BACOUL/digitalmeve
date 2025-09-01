# Security Policy

We take security seriously. Thank you for helping keep DigitalMeve, its users, and the ecosystem safe.

## Supported Versions

| Version  | Status        |
|----------|---------------|
| 1.7.x    | ✔ Supported   |
| < 1.7.0  | ✖ End-of-life |

We backport only critical fixes.

## How to Report a Vulnerability

**Please do not open public Issues for security reports.**

Use one of these private channels:

1. **GitHub Security Advisory** (preferred)  
   - Go to the repository’s **Security** tab → **Advisories** → **Report a vulnerability**.

2. **Email**  
   - Send details to **security@digitalmeve.com** (PGP optional).  
   - Include: affected version(s), environment, steps to reproduce, PoC, impact, and any suggested mitigations.

We will acknowledge receipt within **3 business days** and keep you informed of progress.

## Disclosure Policy

- We follow **coordinated disclosure**:
  - We validate, develop a fix, and prepare a release.
  - We credit reporters (unless you prefer anonymity).
  - We may request a short embargo until patches are available.

## Hardening Notes

- No user documents are stored by the project; proofs are generated locally.
- Verification can run **offline**; no network dependency for core validation.
- Design is compatible with: transparency logs (Merkle roots), key rotation, revocation lists.
- Sidecar `.meve.json` avoids modifying original files; large files supported.

## Development Security Hygiene

- Mandatory CI checks: lint, tests, packaging.
- `pre-commit` hooks recommended for contributors.
- Dependencies are pinned via `pyproject.toml`; supply chain checks run in CI.

Thank you for responsibly disclosing security issues. 🙏
