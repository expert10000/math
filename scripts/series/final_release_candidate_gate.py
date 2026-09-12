#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

VOLUMES = [
    ("I", 1, "Linear Algebra", "vol01_linear_algebra", 18),
    ("II", 2, "Real Analysis and Topological Foundations", "vol02_real_analysis", 25),
    ("III", 3, "Measure, Fourier Analysis, Distributions and PDE", "vol03_fourier_distributions_pde", 28),
    ("IV", 4, "Complex Analysis and Riemann Surfaces", "vol04_complex_analysis", 31),
    ("V", 5, "Commutative Algebra and Homological Methods", "vol05_commutative_algebra", 28),
    ("VI", 6, "Algebraic Geometry and Sheaf Theory", "vol06_algebraic_geometry", 49),
    ("VII", 7, "Differential, Riemannian and Hyperbolic Geometry", "vol07_differential_geometry", 42),
    ("VIII", 8, "Algebraic Topology", "vol08_algebraic_topology", 35),
]
EXPECTED_CHAPTERS = 256
BLOCKING_LOG_PHRASES = (
    "latex warning: there were undefined references",
    "there were undefined citations",
    "multiply defined",
    "! latex error",
    "! emergency stop",
)
OVERFULL_RE = re.compile(r"Overfull \\[hv]box \\(([-+]?\\d+(?:\\.\\d+)?)pt too (?:wide|high)\\)", re.I)


def run(repo: Path, label: str, script: str, *extra: str) -> dict:
    cmd = [sys.executable, str(repo / script), "--repo", str(repo), *extra]
    print(f"\n=== {label} ===")
    print("$", " ".join(cmd))
    cp = subprocess.run(cmd, cwd=repo, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if cp.stdout:
        print(cp.stdout, end="" if cp.stdout.endswith("\n") else "\n")
    if cp.stderr:
        print(cp.stderr, end="" if cp.stderr.endswith("\n") else "\n", file=sys.stderr)
    return {"label": label, "command": cmd, "returncode": cp.returncode}


def git(repo: Path, *args: str) -> str:
    cp = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True, encoding="utf-8", errors="replace")
    if cp.returncode:
        raise RuntimeError(cp.stderr.strip() or f"git {' '.join(args)} failed")
    return cp.stdout.strip()


def run_external(repo: Path, label: str, cmd: list[str], cwd: Path | None = None) -> dict:
    print(f"\n=== {label} ===")
    print("$", " ".join(cmd))
    cp = subprocess.run(
        cmd, cwd=str(cwd or repo), text=True, capture_output=True,
        encoding="utf-8", errors="replace"
    )
    if cp.stdout:
        print(cp.stdout, end="" if cp.stdout.endswith("\n") else "\n")
    if cp.stderr:
        print(cp.stderr, end="" if cp.stderr.endswith("\n") else "\n", file=sys.stderr)
    return {"label": label, "command": cmd, "returncode": cp.returncode}


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Run the final Volume I-VIII release-candidate gate.")
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports" / "series"
    reports.mkdir(parents=True, exist_ok=True)

    required_scripts = [
        "scripts/series/audit_i_viii.py",
        "scripts/series/audit_reviewed_freezes_i_viii.py",
        "scripts/series/refresh_current_pdf_inventory.py",
        "scripts/series/verify_series_build.py",
        "scripts/series/reconcile_i_viii_release.py",
        "scripts/series/audit_pedagogy_i_viii.py",
        "scripts/series/refresh_volume02_professional_review_freeze.py",
        "scripts/series/refresh_volume08_shared_macros_freeze_hash.py",
    ]
    missing = [p for p in required_scripts if not (repo / p).exists()]
    if missing:
        raise SystemExit("Missing required series tooling: " + ", ".join(missing))

    head_before = git(repo, "rev-parse", "HEAD")
    status_rows = read_tsv(repo / "editorial" / "CHAPTER_STATUS.tsv")
    blockers: list[str] = []
    if len(status_rows) != EXPECTED_CHAPTERS:
        blockers.append(f"CHAPTER_STATUS rows={len(status_rows)} expected={EXPECTED_CHAPTERS}")
    if sum(r.get("status") == "FROZEN" for r in status_rows) != EXPECTED_CHAPTERS:
        blockers.append("not all 256 chapter rows are FROZEN")
    if sum(r.get("next_action") == "COMPLETE" for r in status_rows) != EXPECTED_CHAPTERS:
        blockers.append("not all 256 chapter rows are COMPLETE")
    for roman, _, _, dirname, expected in VOLUMES:
        book = repo / "books" / dirname / "book.tex"
        if not book.exists():
            blockers.append(f"Volume {roman}: missing book.tex")
        if len([r for r in status_rows if r.get("volume") == roman]) != expected:
            blockers.append(f"Volume {roman}: chapter ledger count mismatch")
    if blockers:
        raise SystemExit("Pre-gate structural blockers:\n- " + "\n- ".join(blockers))

    commands = []
    commands.append(run(repo, "Global status/path/encoding audit", "scripts/series/audit_i_viii.py"))
    # Volume II received professional-review source changes after its previous
    # numerical-guidance freeze.  Rebuild and freeze that exact current state
    # (25 numbered chapters + one intentional unnumbered topology interlude)
    # before asking the cross-volume reviewed-freeze audit to verify all eight.
    commands.append(run(
        repo,
        "Refresh Volume II professional-review freeze",
        "scripts/series/refresh_volume02_professional_review_freeze.py",
    ))

    # Volume VIII's September 10 freeze manifest contains a stale byte hash for
    # shared/macros.tex even though that shared file is Git-clean at the pinned
    # source base and has not changed since August 31. Refresh only that one row,
    # and only after the helper verifies the shared file is Git-clean.
    commands.append(run(
        repo,
        "Refresh Volume VIII shared-macros freeze hash",
        "scripts/series/refresh_volume08_shared_macros_freeze_hash.py",
    ))
    commands.append(run(
        repo,
        "Volume VIII native freeze audit",
        "books/vol08_algebraic_topology/freeze/AUDIT_VOLUME08_FREEZE.py",
    ))

    # Remove prior reviewed-freeze reports so a failed current run can never
    # be misread as PASS from stale evidence.
    for stale in (
        "REVIEWED_FREEZE_BUILD_AUDIT_I_VIII.json",
        "REVIEWED_FREEZE_BUILD_AUDIT_I_VIII.md",
        "REVIEWED_FREEZE_BUILD_AUDIT_I_VIII.tsv",
        "REVIEWED_FREEZE_MANIFEST_FINDINGS_I_VIII.tsv",
    ):
        p = repo / "reports/series" / stale
        if p.exists():
            p.unlink()

    commands.append(run(repo, "Reviewed freeze verification + clean canonical builds", "scripts/series/audit_reviewed_freezes_i_viii.py", "--repair-shared-metadata"))
    commands.append(run(repo, "Refresh canonical PDF inventory", "scripts/series/refresh_current_pdf_inventory.py"))
    commands.append(run(repo, "Verify I-VIII canonical builds", "scripts/series/verify_series_build.py"))
    commands.append(run(repo, "Pedagogy consistency audit", "scripts/series/audit_pedagogy_i_viii.py"))

    # Volume VI has a native edition-controlled solution layer.  The global
    # reconciliation intentionally requires a fresh full-solutions PDF/log, so
    # build that canonical release evidence before the final reconciliation.
    vol6 = repo / "books" / "vol06_algebraic_geometry"
    clean = run_external(
        repo,
        "Clean Volume VI full-solutions edition",
        ["latexmk", "-C", "book_full_solutions.tex"],
        cwd=vol6,
    )
    commands.append(clean)
    if clean["returncode"] == 0:
        commands.append(run_external(
            repo,
            "Build Volume VI full-solutions edition",
            ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "book_full_solutions.tex"],
            cwd=vol6,
        ))
    else:
        commands.append({
            "label": "Build Volume VI full-solutions edition",
            "command": ["latexmk", "-pdf", "book_full_solutions.tex"],
            "returncode": 99,
        })

    commands.append(run(repo, "Full I-VIII release reconciliation", "scripts/series/reconcile_i_viii_release.py"))
    failed = [x for x in commands if x["returncode"] != 0]
    if failed:
        blockers.extend(f"{x['label']} returned {x['returncode']}" for x in failed)

    build_rows = [r for r in read_tsv(reports / "BUILD_I_VIII.tsv") if r.get("target") == "book.tex" and r.get("kind") == "canonical"]
    build_index = {r.get("volume"): r for r in build_rows}
    layout_rows = []
    for roman, _, title, dirname, _ in VOLUMES:
        log = repo / "books" / dirname / "book.log"
        pdf = repo / "books" / dirname / "book.pdf"
        log_text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
        lower = log_text.lower()
        phrase_hits = [p for p in BLOCKING_LOG_PHRASES if p in lower]
        widths = [float(x) for x in OVERFULL_RE.findall(log_text)]
        ge20 = [x for x in widths if x >= 20.0]
        br = build_index.get(roman, {})
        status = "PASS"
        reasons = []
        if br.get("status") != "PASS":
            status = "FAIL"; reasons.append(f"build={br.get('status','MISSING')}")
        if not pdf.exists():
            status = "FAIL"; reasons.append("book.pdf missing")
        if not log.exists():
            status = "FAIL"; reasons.append("book.log missing")
        if phrase_hits:
            status = "FAIL"; reasons.append("blocking LaTeX warning/error")
        if ge20:
            status = "FAIL"; reasons.append(f">=20pt overfull boxes={len(ge20)}")
        if status == "FAIL":
            blockers.append(f"Volume {roman}: " + "; ".join(reasons))
        layout_rows.append({
            "volume": roman,
            "title": title,
            "build_status": br.get("status", "MISSING"),
            "pdf_exists": "YES" if pdf.exists() else "NO",
            "log_exists": "YES" if log.exists() else "NO",
            "blocking_log_phrases": len(phrase_hits),
            "overfull_boxes": len(widths),
            "overfull_ge_20pt": len(ge20),
            "max_overfull_pt": f"{max(widths):.3f}" if widths else "0.000",
            "status": status,
        })

    write_tsv(
        reports / "FINAL_RC_LAYOUT_I_VIII.tsv",
        layout_rows,
        ["volume", "title", "build_status", "pdf_exists", "log_exists", "blocking_log_phrases", "overfull_boxes", "overfull_ge_20pt", "max_overfull_pt", "status"],
    )

    evidence = {
        "global_audit": load_json(reports / "GLOBAL_I_VIII_AUDIT.json"),
        "reviewed_freeze_build_audit": load_json(reports / "REVIEWED_FREEZE_BUILD_AUDIT_I_VIII.json"),
        "build_verification": load_json(reports / "SERIES_BUILD_VERIFICATION.json"),
        "series_reconciliation": load_json(reports / "GLOBAL_SERIES_RECONCILIATION.json"),
    }
    for name, obj in evidence.items():
        if obj.get("status") != "PASS":
            blockers.append(f"{name} status={obj.get('status','MISSING')}")

    status = "PASS" if not blockers else "FAIL"
    summary = {
        "schema": 1,
        "status": status,
        "gate": "FINAL_VOLUME_I_VIII_RELEASE_CANDIDATE",
        "source_commit": head_before,
        "volumes": 8,
        "chapters": EXPECTED_CHAPTERS,
        "frozen_complete_rows": sum(r.get("status") == "FROZEN" and r.get("next_action") == "COMPLETE" for r in status_rows),
        "canonical_builds_pass": sum(r.get("status") == "PASS" for r in build_rows),
        "layout_volumes_pass": sum(r["status"] == "PASS" for r in layout_rows),
        "overfull_ge_20pt_total": sum(int(r["overfull_ge_20pt"]) for r in layout_rows),
        "commands": commands,
        "evidence_status": {k: v.get("status", "MISSING") for k, v in evidence.items()},
        "blocking": blockers,
    }
    (reports / "FINAL_RELEASE_CANDIDATE_GATE_I_VIII.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md = [
        "# Final Volume I-VIII Release-Candidate Gate",
        "",
        f"**Result: {status}**",
        "",
        f"- Source commit entering gate: `{head_before}`",
        f"- Canonical volumes: **8 / 8**",
        f"- Canonical chapters: **{EXPECTED_CHAPTERS} / {EXPECTED_CHAPTERS} FROZEN / COMPLETE**",
        f"- Clean canonical builds: **{summary['canonical_builds_pass']} / 8 PASS**",
        f"- Layout/log gate: **{summary['layout_volumes_pass']} / 8 PASS**",
        f"- Overfull boxes >=20pt: **{summary['overfull_ge_20pt_total']}**",
        "",
        "## Gate components",
        "",
    ]
    for x in commands:
        md.append(f"- {'PASS' if x['returncode']==0 else 'FAIL'} — {x['label']}")
    md += ["", "## Per-volume layout/build status", "", "| Volume | Build | >=20pt | Max overfull | Gate |", "|---|---|---:|---:|---|"]
    for r in layout_rows:
        md.append(f"| {r['volume']} | {r['build_status']} | {r['overfull_ge_20pt']} | {r['max_overfull_pt']}pt | {r['status']} |")
    md += ["", "## Blockers", ""]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    (reports / "FINAL_RELEASE_CANDIDATE_GATE_I_VIII.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if status == "PASS" else 4


if __name__ == "__main__":
    raise SystemExit(main())
