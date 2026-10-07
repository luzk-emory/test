#!/bin/bash
# Setup script for the Claude Code cloud environment (paste into the environment's "Setup script" field).
# Installs LaTeX (notes, handouts, beamer slides) and the Python packages the check scripts need.
set -e
export DEBIAN_FRONTEND=noninteractive
(apt-get update -qq && apt-get install -y -qq --no-install-recommends \
   texlive-latex-base texlive-latex-recommended texlive-latex-extra \
   texlive-fonts-recommended texlive-pictures poppler-utils) &
pip install -q numpy scipy scikit-learn openpyxl &
wait
pdflatex --version | head -1
