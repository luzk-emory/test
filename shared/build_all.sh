#!/bin/bash
# Rebuild every set of notes, handout and key, then the combined PDFs in pdf/.
# Run from the repository root:  bash shared/build_all.sh
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"
for d in meetings/m*; do cp shared/coursenotes.sty "$d/"; done      # keep style copies in sync
(cd shared && mkdir -p build && pdflatex -interaction=nonstopmode -output-directory=build notation.tex >/dev/null)
ALL=(shared/build/notation.pdf); KEYS=(shared/build/notation.pdf)
for d in meetings/m*; do
  for f in notes $(cd "$d" && ls handout-*.tex 2>/dev/null | sed 's/\.tex$//'); do
    (cd "$d" && bash ../../shared/build.sh "$f")
    ALL+=("$d/build/$f.pdf"); KEYS+=("$d/build/$f-key.pdf")
  done
done
pdfunite "${ALL[@]}" pdf/notes-all.pdf; pdfunite "${KEYS[@]}" pdf/notes-keys.pdf
cp shared/build/notation.pdf pdf/notation.pdf
echo "combined: $(pdfinfo pdf/notes-all.pdf | grep Pages)"
