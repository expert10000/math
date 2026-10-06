from __future__ import annotations
import argparse, csv, re
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    chapter=repo/"books/companion_problems_solutions/chapters/part07_volume_vii/chapter.tex"
    atlas=repo/"books/companion_problems_solutions/metadata/PART_VII_MIGRATION_ATLAS.tsv"
    if not chapter.exists(): raise SystemExit(f"missing: {chapter}")
    if not atlas.exists(): raise SystemExit(f"missing: {atlas}")
    text=chapter.read_text(encoding="utf-8")
    with atlas.open(encoding="utf-8-sig", newline="") as f:
        rows=list(csv.DictReader(f, delimiter="\t"))
    ids=[r["companion_problem_id"] for r in rows]
    problems=re.findall(r"\\begin\{problem\}\[(CP-VII-\d{4})\s+---", text)
    solutions=len(re.findall(r"\\begin\{solution\}", text))
    expected=[f"CP-VII-{i:04d}" for i in range(1,len(ids)+1)]
    assert ids == expected, "IDs not contiguous"
    assert problems == ids, "chapter problem order differs from atlas"
    assert solutions == len(ids), f"solution count {solutions} != problem count {len(ids)}"
    assert "Editorial hold:" not in text, "editorial solution holds remain"
    chapters={r["main_text_chapter"] for r in rows}
    missing=[f"VII/{i:02d}" for i in range(1,43) if f"VII/{i:02d}" not in chapters]
    assert not missing, f"missing chapter coverage: {missing}"
    labels=re.findall(r"\\label\{([^}]+)\}", text)
    assert len(labels)==len(set(labels)), "duplicate labels"
    print("COMPANION PART VII VALIDATION PASSED")
    print(f"  reader-facing problems: {len(ids)}")
    print(f"  solutions: {solutions}")
    print("  editorial holds: 0")
    print("  main-text coverage: VII/01--VII/42")
    print("  labels unique: true")

if __name__=="__main__":
    main()
