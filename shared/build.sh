#!/bin/bash
# Build a document and its answer key into ./build/ (run from a meeting folder).
#   ../../shared/build.sh notes             -> build/notes.pdf, build/notes-key.pdf
#   ../../shared/build.sh handout-H1-iv     -> build/handout-H1-iv.pdf, ...-key.pdf
#   ../../shared/build.sh slides nokey      -> build/slides.pdf only
f=$1; mkdir -p build
for i in 1 2; do pdflatex -interaction=nonstopmode -output-directory=build "$f.tex" > build/$f.console; done
grep -E "^!|undefined" build/$f.log || echo "ok  build/$f.pdf"
if [ "$2" != "nokey" ]; then
  for i in 1 2; do pdflatex -interaction=nonstopmode -output-directory=build -jobname "$f-key" "\def\KEY{}\input{$f}" > build/$f-key.console; done
  grep -E "^!|undefined" build/$f-key.log || echo "ok  build/$f-key.pdf"
fi
