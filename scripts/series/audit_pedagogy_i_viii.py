#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
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
EXPECTED_SERIES_CHAPTERS = 256
COUNT_KEYS = ("examples", "exercises", "hints", "problems", "solutions", "labels")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def derive_totals(data: dict) -> dict:
    if isinstance(data.get("composed_totals"), dict):
        src = data["composed_totals"]
    elif isinstance(data.get("totals"), dict):
        src = data["totals"]
    else:
        src = {}
        for row in data.get("chapters", []):
            split = "composed_examples" in row
            for key in COUNT_KEYS:
                field = f"composed_{key}" if split else key
                src[key] = int(src.get(key, 0)) + int(row.get(field, 0) or 0)
    return {k: int(src.get(k, 0) or 0) for k in COUNT_KEYS}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"
    reports.mkdir(parents=True, exist_ok=True)

    blockers = []
    observations = []
    volume_rows = []
    series_totals = {k: 0 for k in COUNT_KEYS}
    total_chapters = 0

    for roman, num, title, dirname, expected_chapters in VOLUMES:
        recon_rel = Path(f"reports/series/VOLUME{num:02d}_EXAMPLE_EXERCISE_RECONCILIATION.json")
        counts_rel = Path(f"reports/series/VOLUME{num:02d}_EXAMPLE_EXERCISE_COUNTS.tsv")
        hashes_rel = Path(f"reports/series/VOLUME{num:02d}_EXAMPLE_EXERCISE_HASHES.tsv")
        recon = repo / recon_rel
        counts = repo / counts_rel
        hashes = repo / hashes_rel

        if not recon.exists():
            blockers.append(f"{roman}: missing {recon_rel.as_posix()}")
            continue
        try:
            data = json.loads(recon.read_text(encoding="utf-8-sig"))
        except Exception as exc:
            blockers.append(f"{roman}: invalid reconciliation JSON: {exc}")
            continue

        status = data.get("status")
        chapter_count = int(data.get("chapter_count", len(data.get("chapters", []))) or 0)
        recon_blocking = data.get("blocking") or []
        architecture = data.get("architecture", "direct-chapter")

        if status != "PASS":
            blockers.append(f"{roman}: reconciliation status={status!r}")
        if recon_blocking:
            blockers.append(f"{roman}: reconciliation blocking findings={len(recon_blocking)}")
        if chapter_count != expected_chapters:
            blockers.append(f"{roman}: reconciliation chapter_count={chapter_count}, expected={expected_chapters}")

        chapter_codes = [r.get("chapter", "") for r in data.get("chapters", [])]
        if len(chapter_codes) != expected_chapters:
            blockers.append(f"{roman}: chapter rows={len(chapter_codes)}, expected={expected_chapters}")
        if len(set(chapter_codes)) != len(chapter_codes):
            blockers.append(f"{roman}: duplicate chapter codes in reconciliation")
        bad_prefix = [c for c in chapter_codes if not c.startswith(roman + "/")]
        if bad_prefix:
            blockers.append(f"{roman}: chapter-code prefix mismatch ({len(bad_prefix)})")

        totals = derive_totals(data)
        for key in COUNT_KEYS:
            series_totals[key] += totals[key]
        total_chapters += chapter_count

        counts_rows = []
        hashes_rows = []
        if not counts.exists():
            blockers.append(f"{roman}: missing {counts_rel.as_posix()}")
        else:
            counts_rows = read_tsv(counts)
            if len(counts_rows) != expected_chapters:
                blockers.append(f"{roman}: counts ledger rows={len(counts_rows)}, expected={expected_chapters}")

        if not hashes.exists():
            blockers.append(f"{roman}: missing {hashes_rel.as_posix()}")
        else:
            hashes_rows = read_tsv(hashes)
            if len(hashes_rows) != expected_chapters:
                blockers.append(f"{roman}: hash ledger rows={len(hashes_rows)}, expected={expected_chapters}")

        pdf = data.get("pdf") or {}
        pdf_sha = str(pdf.get("sha256") or "").lower()
        pdf_bytes = int(pdf.get("bytes") or 0)
        if not HEX64.match(pdf_sha):
            blockers.append(f"{roman}: reconciliation PDF SHA-256 missing/invalid")
        if pdf_bytes <= 0:
            blockers.append(f"{roman}: reconciliation PDF byte count missing/invalid")

        legacy_obs = data.get("legacy_observations") or []
        if legacy_obs:
            observations.append(f"{roman}: {len(legacy_obs)} legacy pedagogy observations preserved by its PASS reconciliation")

        volume_rows.append({
            "volume": roman,
            "number": num,
            "title": title,
            "directory": dirname,
            "architecture": architecture,
            "expected_chapters": expected_chapters,
            "reconciled_chapters": chapter_count,
            "reconciliation_status": status,
            "reconciliation_sha256": sha256_file(recon),
            "counts_rows": len(counts_rows),
            "hash_rows": len(hashes_rows),
            "examples": totals["examples"],
            "exercises": totals["exercises"],
            "hints": totals["hints"],
            "problems": totals["problems"],
            "solutions": totals["solutions"],
            "labels": totals["labels"],
            "pdf_evidence_sha256": pdf_sha,
            "pdf_evidence_bytes": pdf_bytes,
            "legacy_observations": len(legacy_obs),
        })

    if len(volume_rows) != 8:
        blockers.append(f"series: reconciled volume rows={len(volume_rows)}, expected=8")
    if total_chapters != EXPECTED_SERIES_CHAPTERS:
        blockers.append(f"series: reconciled chapters={total_chapters}, expected={EXPECTED_SERIES_CHAPTERS}")

    status = "PASS" if not blockers else "FAIL"
    result = {
        "schema": 1,
        "status": status,
        "scope": "Volumes I-VIII pedagogy reconciliation",
        "expected_volumes": 8,
        "reconciled_volumes": len(volume_rows),
        "expected_chapters": EXPECTED_SERIES_CHAPTERS,
        "reconciled_chapters": total_chapters,
        "series_totals": series_totals,
        "volumes": volume_rows,
        "blocking": blockers,
        "observations": observations,
    }

    (reports / "SERIES_PEDAGOGY_AUDIT.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    md = [
        "# Series pedagogy reconciliation audit — Volumes I–VIII",
        "",
        f"**Result:** {status}",
        "",
        f"- reconciled volumes: **{len(volume_rows)} / 8**",
        f"- reconciled chapters: **{total_chapters} / {EXPECTED_SERIES_CHAPTERS}**",
        "",
        "## Composed pedagogy totals",
        "",
    ]
    for key in COUNT_KEYS:
        md.append(f"- {key}: **{series_totals[key]}**")
    md += ["", "## Per-volume evidence", ""]
    for row in volume_rows:
        md.append(
            f"- **{row['volume']}** — {row['title']}: "
            f"{row['reconciled_chapters']} chapters; "
            f"reconciliation **{row['reconciliation_status']}**; "
            f"architecture `{row['architecture']}`."
        )
    md += ["", "## Blocking findings", ""]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    md += ["", "## Preserved observations", ""]
    md += [f"- {x}" for x in observations] if observations else ["None."]
    (reports / "SERIES_PEDAGOGY_AUDIT.md").write_text(
        "\n".join(md).rstrip() + "\n", encoding="utf-8"
    )

    print(json.dumps({
        "status": status,
        "volumes": len(volume_rows),
        "chapters": total_chapters,
        "series_totals": series_totals,
        "blocking": blockers,
    }, indent=2))
    return 0 if status == "PASS" else 11


if __name__ == "__main__":
    raise SystemExit(main())
