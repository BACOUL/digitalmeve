diff --git a/CHANGELOG.md b/CHANGELOG.md
index 1234567..89abcde 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
-📜 Changelog — DigitalMeve
-All notable changes to this project are documented here. Format based on Keep a Changelog, and versions follow Semantic Versioning.
-
-[Unreleased]
-Added
-Documentation: expanded guides in docs/ (API usage, generator guide, verification guide, overview, specification, security, roadmap, Pro/Official drafts, examples).
-Project hygiene: SECURITY.md, improved issue/PR templates.
-Changed
-README: badges, quickstart, and links to docs.
-Wording consistency across docs (EN-first).
-Fixed
-Minor typos and broken links in docs.
-[1.7.1-dev] — 2025-09-xx
-Changed
-Work-in-progress development snapshot.
-[1.7.0] — 2025-08-30
-Added
-generate_meve(...) returns richer dict:
-meve_version, issuer, issued_at (UTC ISO-8601), metadata.
-subject { filename, size, hash_sha256 }.
-top-level hash (duplicate of subject.hash_sha256).
-preview_b64 (short base64 preview).
-Sidecar writing via outdir (<file>.meve.json).
-Changed
-Verifier accepts dicts, JSON strings/bytes, or *.meve.json paths.
-Normalized error messages: “Missing required keys”, “Issuer mismatch”, “Hash mismatch”, “Invalid proof”.
-Fixed
-Test suite alignment on Python 3.10–3.12.
-CI workflow stability for matrix runs.
-[1.6.1] — 2025-08-30
-Fixed
-Verifier input parsing robustness.
-Initial README cleanup.
-[1.6.0] — 2025-08-28
-Added
-Initial public release on PyPI.
-Basic generator & verifier functions.
-GitHub Actions: quality, tests, and publish (OIDC) workflows.
-[1.5.0] — 2025-08-29
-Added
-Early docs and CI scaffolding.
-[1.0.0] — 2025-08-28
-Added
-Project bootstrap.
-Historical (pre-1.0)
-Internal prototypes and POCs.
+# 📜 Changelog — DigitalMeve
+All notable changes to this project are documented here.
+Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
+and this project adheres to [Semantic Versioning](https://semver.org/).
+
+## [Unreleased]
+### Added
+- Expanded guides in `docs/` (API usage, generator, verification, overview, specification, security, roadmap, Pro/Official drafts, examples).
+- Project hygiene: `SECURITY.md`, improved issue/PR templates.
+
+### Changed
+- README: badges, quickstart, links to docs.
+- Wording consistency across docs (EN-first).
+
+### Fixed
+- Minor typos and broken links in docs.
+
+## [1.7.1-dev] — 2025-09-05
+### Added
+- `embedding_png.py` stub + passing tests (no-op embedding/extract).
+- Exposed `__version__` (aligned with `pyproject.toml`).
+
+### Changed
+- Work-in-progress development snapshot.
+
+## [1.7.0] — 2025-08-30
+### Added
+- `generate_meve(...)` returns richer dict:
+  - `meve_version`, `issuer`, `issued_at` (UTC ISO-8601), `metadata`
+  - `subject` { filename, size, hash_sha256 }
+  - top-level `hash` (duplicate of subject.hash_sha256)
+  - `preview_b64` (short base64 preview)
+- Sidecar writing via `outdir` (`<file>.meve.json`).
+
+### Changed
+- Verifier accepts dicts, JSON strings/bytes, or `*.meve.json` paths.
+- Normalized error messages: “Missing required keys”, “Issuer mismatch”, “Hash mismatch”, “Invalid proof”.
+
+### Fixed
+- Test suite alignment on Python 3.10–3.12.
+- CI workflow stability for matrix runs.
+
+## [1.6.1] — 2025-08-30
+### Fixed
+- Verifier input parsing robustness.
+- Initial README cleanup.
+
+## [1.6.0] — 2025-08-28
+### Added
+- Initial public release on PyPI.
+- Basic generator & verifier functions.
+- GitHub Actions: quality, tests, and publish (OIDC) workflows.
+
+## [1.5.0] — 2025-08-29
+### Added
+- Early docs and CI scaffolding.
+
+## [1.0.0] — 2025-08-28
+### Added
+- Project bootstrap.
+
+## Historical (pre-1.0)
+- Internal prototypes and POCs.
+
+[Unreleased]: https://github.com/BACOUL/digitalmeve/compare/v1.7.1-dev...HEAD
+[1.7.1-dev]: https://github.com/BACOUL/digitalmeve/compare/v1.7.0...v1.7.1-dev
+[1.7.0]: https://github.com/BACOUL/digitalmeve/compare/v1.6.1...v1.7.0
+[1.6.1]: https://github.com/BACOUL/digitalmeve/compare/v1.6.0...v1.6.1
+[1.6.0]: https://github.com/BACOUL/digitalmeve/releases/tag/v1.6.0
