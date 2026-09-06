#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
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


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def page_count(pdf: Path) -> int:
    try:
        return len(re.findall(rb"/Type\s*/Page(?!s)\b", pdf.read_bytes()))
    except Exception:
        return 0


def write_tsv(path: Path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def git_head(repo: Path) -> str:
    cp = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8", errors="replace",
    )
    return cp.stdout.strip() if cp.returncode == 0 else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"

    audit = json.loads((reports / "SERIES_PEDAGOGY_AUDIT.json").read_text(encoding="utf-8-sig"))
    cross = json.loads((reports / "SERIES_PEDAGOGY_CROSS_VOLUME.json").read_text(encoding="utf-8-sig"))
    blockers = []
    observations = []

    if audit.get("status") != "PASS":
        blockers.append("series pedagogy audit is not PASS")
    if cross.get("status") != "PASS":
        blockers.append("cross-volume pedagogy reconciliation is not PASS")
    if int(cross.get("chapters", 0)) != 256:
        blockers.append(f"cross-volume chapter count={cross.get('chapters')} != 256")
    if int(cross.get("duplicate_active_label_groups", 0)) != 0:
        blockers.append("cross-volume duplicate active labels are present")

    release_rows = []
    for roman, num, title, dirname, expected in VOLUMES:
        volume_root = repo / "books" / dirname
        pdf = volume_root / "book.pdf"
        log = volume_root / "book.log"
        book = volume_root / "book.tex"
        recon = reports / f"VOLUME{num:02d}_EXAMPLE_EXERCISE_RECONCILIATION.json"
        hashes = reports / f"VOLUME{num:02d}_EXAMPLE_EXERCISE_HASHES.tsv"

        missing = [p for p in (pdf, log, book, recon, hashes) if not p.exists()]
        if missing:
            blockers.append(f"{roman}: missing freeze inputs: " + ", ".join(p.relative_to(repo).as_posix() for p in missing))
            continue

        log_text = log.read_text(encoding="utf-8", errors="replace")
        fatal_patterns = [
            "Fatal error occurred",
            "Emergency stop",
            "! LaTeX Error",
            "Undefined control sequence",
            "There were undefined references",
            "There were undefined citations",
            "multiply defined",
        ]
        hits = [p for p in fatal_patterns if p.lower() in log_text.lower()]
        if hits:
            blockers.append(f"{roman}: build-log blocking signatures: {', '.join(hits)}")

        recon_data = json.loads(recon.read_text(encoding="utf-8-sig"))
        old_pdf_sha = str((recon_data.get("pdf") or {}).get("sha256") or "").lower()
        fresh_pdf_sha = sha256_file(pdf)
        if old_pdf_sha and old_pdf_sha != fresh_pdf_sha:
            observations.append(
                f"{roman}: rebuilt PDF SHA-256 differs from the per-volume reconciliation snapshot; "
                "the fresh series-freeze hash supersedes it for this release"
            )

        release_rows.append({
            "volume": roman,
            "title": title,
            "chapters": expected,
            "pdf_path": pdf.relative_to(repo).as_posix(),
            "pdf_bytes": pdf.stat().st_size,
            "pdf_pages": page_count(pdf),
            "pdf_sha256": fresh_pdf_sha,
            "matches_volume_reconciliation_pdf_sha256": "YES" if old_pdf_sha == fresh_pdf_sha else "NO",
            "book_tex_sha256": sha256_file(book),
            "volume_reconciliation_sha256": sha256_file(recon),
            "volume_hash_ledger_sha256": sha256_file(hashes),
        })

    if len(release_rows) != 8:
        blockers.append(f"release rows={len(release_rows)}, expected=8")

    fields = [
        "volume", "title", "chapters", "pdf_path", "pdf_bytes", "pdf_pages", "pdf_sha256",
        "matches_volume_reconciliation_pdf_sha256", "book_tex_sha256",
        "volume_reconciliation_sha256", "volume_hash_ledger_sha256",
    ]
    release_path = reports / "SERIES_PEDAGOGY_RELEASE_HASHES.tsv"
    write_tsv(release_path, release_rows, fields)

    source_manifest_sha = sha256_file(reports / "SERIES_PEDAGOGY_HASHES.tsv")
    counts_manifest_sha = sha256_file(reports / "SERIES_PEDAGOGY_COUNTS.tsv")
    audit_sha = sha256_file(reports / "SERIES_PEDAGOGY_AUDIT.json")
    cross_sha = sha256_file(reports / "SERIES_PEDAGOGY_CROSS_VOLUME.json")
    release_sha = sha256_file(release_path)

    aggregate_material = "\n".join(
        f"{r['volume']}\t{r['pdf_sha256']}\t{r['book_tex_sha256']}\t"
        f"{r['volume_reconciliation_sha256']}\t{r['volume_hash_ledger_sha256']}"
        for r in release_rows
    ).encode("utf-8")
    aggregate_release_sha = hashlib.sha256(aggregate_material).hexdigest()

    status = "PASS" if not blockers else "FAIL"
    result = {
        "schema": 1,
        "status": status,
        "scope": "Whole-series pedagogy integration freeze, Volumes I-VIII",
        "git_base_before_freeze_commit": git_head(repo),
        "volumes": len(release_rows),
        "chapters": 256,
        "series_totals": cross.get("series_totals", {}),
        "pdfs": release_rows,
        "evidence_hashes": {
            "series_pedagogy_counts_sha256": counts_manifest_sha,
            "series_pedagogy_hashes_sha256": source_manifest_sha,
            "series_pedagogy_audit_sha256": audit_sha,
            "series_pedagogy_cross_volume_sha256": cross_sha,
            "series_pedagogy_release_hashes_sha256": release_sha,
            "aggregate_release_sha256": aggregate_release_sha,
        },
        "blocking": blockers,
        "observations": observations,
    }
    (reports / "SERIES_PEDAGOGY_FREEZE.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    md = [
        "# Whole-series pedagogy integration freeze — Volumes I–VIII",
        "",
        f"**Result:** {status}",
        "",
        "- volumes: **8**",
        "- canonical chapters: **256**",
        f"- rebuilt PDFs recorded: **{len(release_rows)} / 8**",
        f"- aggregate release SHA-256: `{aggregate_release_sha}`",
        "",
        "## Release PDFs",
        "",
    ]
    for row in release_rows:
        md.append(
            f"- **{row['volume']}** — {row['title']}: "
            f"`{row['pdf_sha256']}` ({row['pdf_bytes']} bytes, {row['pdf_pages']} pages)"
        )
    md += ["", "## Evidence hashes", ""]
    for key, value in result["evidence_hashes"].items():
        md.append(f"- `{key}`: `{value}`")
    md += ["", "## Blocking findings", ""]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    md += ["", "## Observations", ""]
    md += [f"- {x}" for x in observations] if observations else ["None."]
    (reports / "SERIES_PEDAGOGY_FREEZE.md").write_text(
        "\n".join(md).rstrip() + "\n", encoding="utf-8"
    )

    print(json.dumps({
        "status": status,
        "volumes": len(release_rows),
        "chapters": 256,
        "aggregate_release_sha256": aggregate_release_sha,
        "blocking": blockers,
    }, indent=2))
    return 0 if status == "PASS" else 13


if __name__ == "__main__":
    raise SystemExit(main())
