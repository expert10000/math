#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json
from pathlib import Path

TARGETS = {
    "VI": {
        "source_file": "books/vol06_algebraic_geometry/chapters/ch41_divisor_class_groups/chapter.tex",
        "classification": "CONFIRMED_BOXED_CLASS_GROUP_SUMMARY_OVERFLOW",
        "repair_action": "reflow the quadric-cone class-group summary into three aligned rows",
    },
    "VII": {
        "source_file": "books/vol07_differential_geometry/chapters/ch10_orientation_and_integration/chapter.tex",
        "classification": "CONFIRMED_BOXED_DISPLAY_OVERFLOW",
        "repair_action": "reflow the boxed orientation/integration summary onto two aligned rows",
    },
    "VIII": {
        "source_file": "books/vol08_algebraic_topology/chapters/ch35_lefschetz_theory/chapter.tex",
        "classification": "CONFIRMED_LONG_ARROW_CHAIN_OVERFLOW",
        "repair_action": "reflow the canonical arc into two aligned display rows",
    },
}

def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    reports=repo/"reports/series"

    warnings=read_tsv(reports/"POST_PEDAGOGY_REPROOF_LAYOUT_WARNINGS.tsv")
    severe=[r for r in warnings if float(r.get("overfull_pt") or 0) >= 20.0]
    if len(severe)!=3 or {r["volume"] for r in severe}!={"VI","VII","VIII"}:
        raise SystemExit(f"Expected exactly the VI/VII/VIII residual queue; got {[(r.get('volume'),r.get('overfull_pt')) for r in severe]}")

    prior=read_tsv(reports/"V12_RC1_RENDER_TRIAGE.tsv")
    low=[r for r in prior if r.get("finding_type")=="LOW_TEXT_PAGE"]
    if len(low)!=10:
        raise SystemExit(f"Expected 10 low-text review rows, found {len(low)}")
    if any(not r.get("classification","").startswith("LIKELY_INTENTIONAL") for r in low):
        raise SystemExit("A low-text page remains unclassified.")

    rows=[]
    for r in severe:
        t=TARGETS[r["volume"]]
        if not (repo/t["source_file"]).exists():
            raise SystemExit("Missing corrected residual target: "+t["source_file"])
        rows.append({
            "volume":r["volume"],"kind":r["kind"],"overfull_pt":r["overfull_pt"],
            "severity":r["severity"],"source_file":t["source_file"],
            "classification":t["classification"],"repair_action":t["repair_action"],
        })
    rows.sort(key=lambda r:("VI","VII","VIII").index(r["volume"]))
    write_tsv(reports/"V12_RC1_RESIDUAL_LAYOUT_TRIAGE.tsv",rows,
              ["volume","kind","overfull_pt","severity","source_file","classification","repair_action"])
    obj={
        "schema":2,"status":"PASS","candidate":"v1.2-rc1",
        "correction":"VI residual source attribution corrected from figure_07.tex to ch41 chapter.tex after clean affected-volume verification",
        "residual_ge_20pt":3,"residual_volumes":["VI","VII","VIII"],
        "largest_overfull_pt":max(float(r["overfull_pt"]) for r in rows),
        "low_text_pages_reviewed":10,"low_text_pages_classified_intentional":10,
        "source_targets":[r["source_file"] for r in rows],"blocking":[],
    }
    (reports/"V12_RC1_RESIDUAL_LAYOUT_TRIAGE.json").write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=[
        "# v1.2 RC1 residual layout triage — corrected source attribution","",
        "**Status:** PASS","",
        "- Residual overfull boxes >=20pt: **3**.",
        "- Low-text review pages: **10**, all classified as intentional structural/frontmatter pages.",
        "- The original VI attribution to `figure_07.tex` was disproved by the first affected-volume rebuild.",
        "- The unchanged `29.45859pt` warning resolves to the boxed quadric-cone class-group summary in `VI/41 chapter.tex`.",
        "","## Corrected residuals","",
    ]
    for r in rows:
        md.append(f"- **Volume {r['volume']}** — {float(r['overfull_pt']):.5f}pt — `{r['source_file']}` — {r['repair_action']}.")
    (reports/"V12_RC1_RESIDUAL_LAYOUT_TRIAGE.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(obj,indent=2,ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
