#!/usr/bin/env python3
"""
Prüft, ob alle .md Dateien im Ordner docs/ auch in mkdocs.yml unter nav: eingetragen sind.
"""
import os
import glob
import re

docs_dir = "/home/thorsten/dokument/docs"
mkdocs_file = "/home/thorsten/dokument/mkdocs.yml"

nav_paths = set()

with open(mkdocs_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    # Match lines like "- Somethings: path/to/file.md"
    match = re.search(r':\s+([A-Za-z0-9_\-/\.äöüÄÖÜß]+\.md)\b', line)
    if match:
        nav_paths.add(match.group(1).strip())
    else:
        # Match lines like "- path/to/file.md"
        match_simple = re.search(r'^\s*-\s+([A-Za-z0-9_\-/\.äöüÄÖÜß]+\.md)\b', line)
        if match_simple:
            nav_paths.add(match_simple.group(1).strip())

all_md_files = glob.glob(f"{docs_dir}/**/*.md", recursive=True)
rel_md_files = {os.path.relpath(f, docs_dir) for f in all_md_files}

orphaned = rel_md_files - nav_paths

if orphaned:
    print(f"⚠️ Gefundene verwaiste Dateien ({len(orphaned)}):")
    for f in sorted(orphaned):
        print(f"  - docs/{f}")
else:
    print(f"✅ Alle {len(rel_md_files)} Markdown-Dateien sind ordnungsgemäß in mkdocs.yml registriert!")
