# 🔐 Security Policy — DigitalMeve

## Supported Versions

| Version   | Supported |
|-----------|-----------|
| 1.7.x     | ✅ Yes    |
| < 1.7     | ❌ No     |

We only provide **security patches** for the latest stable release.

---

## Reporting a Vulnerability

If you discover a security vulnerability, **please report it responsibly**:

- Email: [security@digitalmeve.com](mailto:security@digitalmeve.com)  
- Expected first response: **within 72 hours**  
- Do **not** disclose publicly until a fix or mitigation is available.  

We follow **responsible disclosure practices**: early contact, private fix, coordinated release.

---

## Scope

Covered by this policy:

- Core library (`/src/digitalmeve`)
- Reference CLI & API
- Official documentation (`/docs`)
- GitHub workflows (`.github/workflows`)

Not in scope:

- Third-party forks
- Unofficial integrations

---

## Best Practices for Users

- Always use the **latest release** from PyPI.  
- Verify `.meve.json` proofs with the **official verifier**.  
- Never modify `.meve.json` manually.  
- For sensitive integrations, run verification **offline** (no data upload).  

---

✍️ Maintained under DigitalMeve Security Team.
