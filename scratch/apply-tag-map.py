#!/usr/bin/env python3
"""
Apply the corrected standards tag map to content/learn/**/*.md

Usage (from repo root, with tagmap.py and this file present):
    python apply-tag-map.py --dry-run
    python apply-tag-map.py

Rewrites only the `standards:` line in each module's front matter.
Everything else in the file is untouched.
"""
import re, sys, glob, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tagmap import MAP

dry = "--dry-run" in sys.argv
changed = skipped = missing = 0

for path in sorted(glob.glob("content/learn/**/*.md", recursive=True)):
    if path.endswith("_index.md"):
        continue
    text = open(path, encoding="utf-8").read()
    fm = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not fm:
        continue
    mid = re.search(r'^id:\s*"?([A-Z]+-\d+)"?', fm.group(1), re.M)
    if not mid or mid.group(1) not in MAP:
        missing += 1
        print(f"  SKIP (no map entry): {path}")
        continue
    codes = MAP[mid.group(1)][0]
    new_line = "standards: [" + ", ".join(f'"{c}"' for c in codes) + "]"
    block = fm.group(1)
    if re.search(r"^standards:.*$", block, re.M):
        new_block = re.sub(r"^standards:.*$", new_line, block, count=1, flags=re.M)
    else:
        new_block = block + "\n" + new_line
    if new_block == block:
        skipped += 1
        continue
    out = text[: fm.start(1)] + new_block + text[fm.end(1) :]
    if not dry:
        open(path, "w", encoding="utf-8", newline="\n").write(out)
    changed += 1
    print(f"  {mid.group(1):<11} -> {', '.join(codes)}")

print(f"\n{'[dry run] would update' if dry else 'updated'}: {changed} | unchanged: {skipped} | unmapped: {missing}")
