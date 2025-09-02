#!/usr/bin/env bash
# Regenerate .meve.json proofs for any sample files in ./examples
# It will skip existing .meve / .meve.json files and generate sidecars next to sources.

set -euo pipefail

EXAMPLES_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "==> Scanning ${EXAMPLES_DIR}"

# All candidate sources (add/adjust extensions if you add more examples)
mapfile -t SOURCES < <(find "$EXAMPLES_DIR" -maxdepth 1 -type f \
  \( -iname "*.pdf" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.txt" -o -iname "*.docx" \) \
  -printf "%f\n")

if [ ${#SOURCES[@]} -eq 0 ]; then
  echo "No source files found (pdf/jpg/png/txt/docx). Nothing to do."
  exit 0
fi

echo "==> Generating DigitalMeve proofs..."
for f in "${SOURCES[@]}"; do
  src="${EXAMPLES_DIR}/${f}"
  echo " - ${f}"
  digitalmeve generate "$src" --outdir "$EXAMPLES_DIR" --issuer "Example"
done

echo "==> Done. Proofs written as <file>.meve.json in ${EXAMPLES_DIR}"
