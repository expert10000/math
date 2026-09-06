#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json
from pathlib import Path

TARGETS = {
    "VI": {
        "source_file": "books/vol06_algebraic_geometry/chapters/ch41_divisor_class_groups/figures/figure_07.tex",
        "classification": "CONFIRMED_TIKZ_WIDTH_OVERFLOW",
        "repair_action": "tighten TikZ node geometry and constrain explanatory node width",
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"

    warnings_path = reports / "POST_PEDAGOGY_REPROOF_LAYOUT_WARNINGS.tsv"
    triage_path = reports / "V12_RC1_RENDER_TRIAGE.tsv"
    if not warnings_path.exists() or not triage_path.exists():
        raise SystemExit("Missing v1.2 RC rendered proof inputs.")

    warnings = read_tsv(warnings_path)
    severe = [r for r in warnings if float(r.get("overfull_pt") or 0) >= 20.0]
    if len(severe) != 3:
        raise SystemExit(f"Expected exactly 3 residual >=20pt findings, found {len(severe)}.")
    if {r["volume"] for r in severe} != {"VI", "VII", "VIII"}:
        raise SystemExit("Residual >=20pt findings are not exactly VI/VII/VIII.")

    low_text_rows = [r for r in read_tsv(triage_path) if r.get("finding_type") == "LOW_TEXT_PAGE"]
    if len(low_text_rows) != 10:
        raise SystemExit(f"Expected 10 low-text triage rows, found {len(low_text_rows)}.")
    nonintentional = [r for r in low_text_rows if not r.get("classification","").startswith("LIKELY_INTENTIONAL")]
    if nonintentional:
        raise SystemExit("One or more low-text pages are not classified as intentional structural/frontmatter pages.")

    rows = []
    for r in severe:
        t = TARGETS[r["volume"]]
        src = repo / t["source_file"]
        if not src.exists():
            raise SystemExit(f"Missing residual source target: {t['source_file']}")
        rows.append({
            "volume": r["volume"],
            "kind": r["kind"],
            "overfull_pt": r["overfull_pt"],
            "severity": r["severity"],
            "source_file": t["source_file"],
            "classification": t["classification"],
            "repair_action": t["repair_action"],
        })

    rows.sort(key=lambda r: ("VI","VII","VIII").index(r["volume"]))
    write_tsv(
        reports / "V12_RC1_RESIDUAL_LAYOUT_TRIAGE.tsv",
        rows,
        ["volume","kind","overfull_pt","severity","source_file","classification","repair_action"],
    )

    obj = {
        "schema": 1,
        "status": "PASS",
        "candidate": "v1.2-rc1",
        "residual_ge_20pt": len(rows),
        "residual_volumes": [r["volume"] for r in rows],
        "largest_overfull_pt": max(float(r["overfull_pt"]) for r in rows),
        "low_text_pages_reviewed": len(low_text_rows),
        "low_text_pages_classified_intentional": len(low_text_rows),
        "source_targets": [r["source_file"] for r in rows],
        "blocking": [],
    }
    (reports / "V12_RC1_RESIDUAL_LAYOUT_TRIAGE.json").write_text(
        json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    md = [
        "# v1.2 RC1 residual layout triage",
        "",
        "**Status:** PASS",
        "",
        f"- Residual overfull boxes >=20pt: **{len(rows)}**.",
        f"- Largest residual: **{obj['largest_overfull_pt']:.5f}pt**.",
        f"- Low-text review pages: **{len(low_text_rows)}**, all classified as intentional structural/frontmatter pages.",
        "",
        "## Confirmed residuals",
        "",
    ]
    for r in rows:
        md.append(
            f"- **Volume {r['volume']}** — {float(r['overfull_pt']):.5f}pt — "
            f"`{r['source_file']}` — {r['repair_action']}."
        )
    md += [
        "",
        "No further shared/global typography change is proposed. The repair scope is exactly the three local source constructs above.",
        "",
    ]
    (reports / "V12_RC1_RESIDUAL_LAYOUT_TRIAGE.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(obj, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
