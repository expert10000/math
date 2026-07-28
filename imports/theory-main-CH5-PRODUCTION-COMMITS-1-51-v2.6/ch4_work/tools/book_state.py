#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
states = []
for p in sorted((root / "chapters").glob("chapter*/CHAPTER_STATE.json")):
    states.append(json.loads(p.read_text(encoding="utf-8")))

complete_sections = sum(len(c["sections"]) for c in states)
lines = [
    "# Book State",
    "",
    "This file is generated from chapter-local `CHAPTER_STATE.json` files.",
    "",
    "## Current build",
    "",
    f"- Modular chapters included: {len(states)}",
    f"- Completed modular sections: {complete_sections}",
    "- Master file: `main.tex`",
    "- Bibliography: `references.bib`",
    "- Glossary: `glossary/entries.tex`",
    "- Index: enabled",
    "",
    "## Chapters",
    "",
]
for c in states:
    lines.append(f"### Chapter {c['chapter']}: {c['title']}")
    lines.append(f"- Canonical file: `{c['canonical_file']}`")
    lines.append(f"- Sections: {len(c['sections'])}")
    lines.append("")
(root / "BOOK_STATE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(root / "BOOK_STATE.md")
