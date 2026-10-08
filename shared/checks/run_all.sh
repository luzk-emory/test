#!/bin/bash
# Re-run every arithmetic check. Each script prints one line per claim; this prints only problems.
cd "$(dirname "$0")"
for s in notes*_check.py handoutH*_check.py slides*_check.py; do
  out=$(python3 "$s" 2>&1)
  bad=$(echo "$out" | grep -E "MISMATCH \||^FLAG |\[BAD\]|\[FAIL\]|\[WARN\]|Traceback")
  if [ -n "$bad" ]; then echo "### $s"; echo "$bad"; else echo "ok  $s"; fi
done
