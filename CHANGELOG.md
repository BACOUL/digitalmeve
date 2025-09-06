diff --git a/CHANGELOG.md b/CHANGELOG.md
index 0000000..0000001 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -1,34 +1,48 @@
 📜 Changelog — DigitalMeve
 All notable changes to this project are documented here. Format based on Keep a Changelog, and versions follow Semantic Versioning.

 [Unreleased]
 Added
 Documentation: expanded guides in /docs/ (API usage, generator guide, verification guide, overview, specification, security, roadmap, Pro/Official drafts, examples).
 Project hygiene: SECURITY.md, improved issue/PR templates.
 Changed
 README: badges, quickstart, and links to docs.
 Wording consistency across docs (EN-first).
 Fixed
 Minor typos and broken links in docs.
-[1.7.1-dev] — 2025-09-xx
-Changed
-Work-in-progress development snapshot.
+
+[1.7.1] — 2025-09-06
+### Added
+- Documentation: expanded guides in `/docs/` (API usage, generator guide, verification guide, overview, specification, security, roadmap, Pro/Official drafts, examples).
+- Project hygiene: `SECURITY.md`, improved issue/PR templates.
+
+### Changed
+- README: badges, quickstart, and links to docs.
+- Wording consistency across docs (EN-first).
+
+### Fixed
+- Minor typos and broken links in docs.

 [1.7.0] — 2025-08-30
 Added
 generate_meve(...) returns richer dict:
 meve_version, issuer, issued_at (UTC ISO-8601), metadata.
 subject { filename, size, hash_sha256 }.
 Top-level hash (duplicate of subject.hash_sha256).
 preview_b64 (short base64 preview).
 Sidecar writing via outdir (<file>.meve.json).
 Changed
 Verifier accepts dicts, JSON strings/bytes, or *.meve.json paths.
 Normalized error messages:
 “Missing required keys”
 “Issuer mismatch”
 “Hash mismatch”
 “Invalid proof”
 Fixed
 Test suite alignment on Python 3.10–3.12.
 CI workflow stability for matrix runs.
