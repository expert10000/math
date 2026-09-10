#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

VOLUMES = [
    ("I",    "vol01_linear_algebra",              18, "VOLUME01_FREEZE_MANIFEST.sha256"),
    ("II",   "vol02_real_analysis",               25, "VOLUME02_FREEZE_MANIFEST.sha256"),
    ("III",  "vol03_fourier_distributions_pde",   28, "VOLUME03_FREEZE_MANIFEST.sha256"),
    ("IV",   "vol04_complex_analysis",             31, "VOLUME04_FREEZE_MANIFEST.sha256"),
    ("V",    "vol05_commutative_algebra",          28, "VOLUME05_FREEZE_MANIFEST.sha256"),
    ("VI",   "vol06_algebraic_geometry",           49, "VOLUME06_FREEZE_MANIFEST.sha256"),
    ("VII",  "vol07_differential_geometry",        42, "VOLUME07_FREEZE_MANIFEST.sha256"),
    ("VIII", "vol08_algebraic_topology",           35, "VOLUME08_FREEZE_MANIFEST.sha256"),
]

# These files are global metadata/evidence that can legitimately be rewritten
# after an earlier volume was frozen without changing that volume's mathematics.
# The audit may refresh only these hashes in an older manifest.
SHARED_MUTABLE = {
    "editorial/CHAPTER_STATUS.tsv",
    "editorial/SOURCE_MIGRATION.tsv",
    "reports/series/BUILD_I_VIII.tsv",
    "reports/series/BUILD_I_VIII.md",
}

BLOCKING_LOG_PHRASES = (
    "latex warning: there were undefined references",
    "there were undefined citations",
    "multiply defined",
)

class AuditError(RuntimeError):
    pass

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def run(*args: str, cwd: Path | None = None, capture: bool = False) -> str:
    p = subprocess.run(
        list(args),
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=capture,
        encoding="utf-8",
        errors="replace",
    )
    if p.returncode:
        if capture:
            if p.stdout:
                print(p.stdout, end="")
            if p.stderr:
                print(p.stderr, end="", file=sys.stderr)
        raise AuditError(f"Command failed ({p.returncode}): {' '.join(args)}")
    return p.stdout if capture else ""

def read_status(repo: Path):
    p = repo / "editorial/CHAPTER_STATUS.tsv"
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def resolve_manifest_path(repo: Path, vol: Path, rel: str) -> tuple[Path, str]:
    rel = rel.strip().replace("\\", "/")
    repo_candidate = repo / rel
    vol_candidate = vol / rel
    if repo_candidate.exists():
        return repo_candidate, repo_candidate.relative_to(repo).as_posix()
    if vol_candidate.exists():
        return vol_candidate, vol_candidate.relative_to(repo).as_posix()
    # Prefer the apparent convention in the diagnostic.
    if rel.startswith("books/") or rel.startswith("editorial/") or rel.startswith("shared/") or rel.startswith("reports/"):
        return repo_candidate, rel
    return vol_candidate, (vol / rel).relative_to(repo).as_posix()

def parse_manifest(manifest: Path):
    rows = []
    for raw in manifest.read_text(encoding="utf-8-sig").splitlines():
        if not raw.strip():
            continue
        parts = raw.split(None, 1)
        if len(parts) != 2 or not re.fullmatch(r"[0-9a-fA-F]{64}", parts[0]):
            raise AuditError(f"Malformed manifest row in {manifest}: {raw}")
        rows.append([parts[0].lower(), parts[1].strip().replace("\\", "/")])
    if not rows:
        raise AuditError(f"Empty freeze manifest: {manifest}")
    return rows

def write_manifest(manifest: Path, rows):
    manifest.write_text(
        "\n".join(f"{h}  {rel}" for h, rel in rows) + "\n",
        encoding="utf-8",
    )

def verify_manifest(repo: Path, vol: Path, manifest: Path, allow_shared_refresh: bool):
    rows = parse_manifest(manifest)
    findings = []
    changed = False
    for row in rows:
        expected, raw_rel = row
        p, repo_rel = resolve_manifest_path(repo, vol, raw_rel)
        if not p.exists():
            findings.append({
                "path": repo_rel,
                "status": "MISSING",
                "expected": expected,
                "actual": "MISSING",
                "repair": "NO",
            })
            continue
        actual = sha(p)
        if actual == expected:
            continue
        if allow_shared_refresh and repo_rel in SHARED_MUTABLE:
            row[0] = actual
            changed = True
            findings.append({
                "path": repo_rel,
                "status": "REFRESHED_SHARED_METADATA",
                "expected": expected,
                "actual": actual,
                "repair": "YES",
            })
        else:
            findings.append({
                "path": repo_rel,
                "status": "DRIFT",
                "expected": expected,
                "actual": actual,
                "repair": "NO",
            })
    if changed:
        write_manifest(manifest, rows)
    return rows, findings, changed

def chapter_include_count(vol: Path) -> int:
    book = (vol / "book.tex").read_text(encoding="utf-8-sig", errors="replace")
    return len(re.findall(
        r"(?m)^[ \t]*\\include\{chapters/ch\d\d_[^}]+/chapter\}",
        book
    ))

def clean_build(vol: Path):
    run("latexmk", "-C", "book.tex", cwd=vol)
    run(
        "latexmk", "-pdf", "-interaction=nonstopmode",
        "-halt-on-error", "-file-line-error", "book.tex", cwd=vol
    )
    pdf = vol / "book.pdf"
    log = vol / "book.log"
    if not pdf.exists() or not log.exists():
        raise AuditError(f"Missing PDF/log after build: {vol}")
    low = log.read_text(encoding="utf-8", errors="replace").lower()
    bad = [x for x in BLOCKING_LOG_PHRASES if x in low]
    if bad:
        raise AuditError(f"Blocking LaTeX warning(s) in {vol}: {bad}")
    return pdf

def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--repair-shared-metadata", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"
    status_rows = read_status(repo)

    expected_total = sum(v[2] for v in VOLUMES)
    if len(status_rows) != expected_total:
        raise AuditError(
            f"Expected {expected_total} total CHAPTER_STATUS rows, found {len(status_rows)}."
        )

    rows = []
    manifest_findings = []
    failures = []

    # First manifest pass: detect mathematical drift before doing any build work.
    for roman, dirname, expected_chapters, manifest_name in VOLUMES:
        vol = repo / "books" / dirname
        if not vol.exists():
            failures.append(f"{roman}: missing volume directory {vol}")
            continue

        status = [r for r in status_rows if r.get("volume") == roman]
        frozen = sum(1 for r in status if r.get("status") == "FROZEN")
        complete = sum(1 for r in status if r.get("next_action") == "COMPLETE")
        includes = chapter_include_count(vol)

        manifest = vol / "freeze" / manifest_name
        if not manifest.exists():
            failures.append(f"{roman}: missing freeze manifest {manifest}")
            continue

        mrows, findings, changed = verify_manifest(
            repo, vol, manifest, args.repair_shared_metadata
        )
        for f in findings:
            f["volume"] = roman
            manifest_findings.append(f)
            if f["status"] in ("MISSING", "DRIFT"):
                failures.append(f"{roman}: manifest {f['status']} {f['path']}")

        if len(status) != expected_chapters:
            failures.append(
                f"{roman}: status rows {len(status)} != expected {expected_chapters}"
            )
        if frozen != expected_chapters or complete != expected_chapters:
            failures.append(
                f"{roman}: expected all {expected_chapters} rows FROZEN/COMPLETE; "
                f"found frozen={frozen} complete={complete}"
            )
        if includes != expected_chapters:
            failures.append(
                f"{roman}: active includes {includes} != expected {expected_chapters}"
            )

        rows.append({
            "volume": roman,
            "volume_dir": dirname,
            "chapters_expected": expected_chapters,
            "status_rows": len(status),
            "frozen_rows": frozen,
            "complete_rows": complete,
            "active_includes": includes,
            "manifest_entries": len(mrows),
            "manifest_shared_metadata_refreshes": sum(
                1 for f in findings if f["status"] == "REFRESHED_SHARED_METADATA"
            ),
            "manifest_status": "PASS" if not any(
                f["status"] in ("MISSING", "DRIFT") for f in findings
            ) else "FAIL",
            "build_status": "NOT_RUN",
            "pdf": "",
            "bytes": "",
            "sha256": "",
        })

    if failures:
        for msg in failures:
            print("BLOCK:", msg)
        raise AuditError("Pre-build I-VIII freeze-manifest/status audit failed.")

    # Clean-build all eight volumes.
    build_inventory = []
    by_volume = {r["volume"]: r for r in rows}
    for roman, dirname, expected_chapters, manifest_name in VOLUMES:
        vol = repo / "books" / dirname
        print(f"\nBUILD {roman} - {dirname}")
        pdf = clean_build(vol)
        rel_pdf = pdf.relative_to(repo).as_posix()
        digest = sha(pdf)
        b = pdf.stat().st_size
        rec = by_volume[roman]
        rec["build_status"] = "PASS"
        rec["pdf"] = rel_pdf
        rec["bytes"] = str(b)
        rec["sha256"] = digest
        build_inventory.append({
            "volume": roman,
            "volume_dir": dirname,
            "target": "book.tex",
            "kind": "canonical",
            "status": "PASS",
            "pdf": rel_pdf,
            "bytes": str(b),
            "sha256": digest,
            "error": "-",
        })

    # Refresh canonical build inventory.
    write_tsv(
        reports / "BUILD_I_VIII.tsv",
        build_inventory,
        ["volume", "volume_dir", "target", "kind", "status", "pdf", "bytes", "sha256", "error"],
    )
    md = [
        "# I-VIII Canonical Build Inventory",
        "",
        "- PASS: **8**",
        "- FAIL: **0**",
        "- NO_WRAPPER: **0**",
        "",
        "| Volume | Target | Status | Detail |",
        "|---|---|---|---|",
    ]
    for r in build_inventory:
        md.append(f"| {r['volume']} | book.tex | PASS | {r['pdf']} |")
    (reports / "BUILD_I_VIII.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # A build-inventory refresh is itself shared release evidence. If any older
    # manifest tracks it, allow that metadata-only hash to refresh now.
    for roman, dirname, expected_chapters, manifest_name in VOLUMES:
        vol = repo / "books" / dirname
        manifest = vol / "freeze" / manifest_name
        _, findings, _ = verify_manifest(
            repo, vol, manifest, args.repair_shared_metadata
        )
        for f in findings:
            if f["status"] in ("MISSING", "DRIFT"):
                failures.append(f"{roman}: post-build manifest {f['status']} {f['path']}")
            if f["status"] == "REFRESHED_SHARED_METADATA":
                # Avoid duplicate report rows if already recorded in pre-pass.
                key = (roman, f["path"], f["actual"])
                existing = {
                    (x["volume"], x["path"], x["actual"])
                    for x in manifest_findings
                    if x["status"] == "REFRESHED_SHARED_METADATA"
                }
                if key not in existing:
                    f["volume"] = roman
                    manifest_findings.append(f)

    if failures:
        for msg in failures:
            print("BLOCK:", msg)
        raise AuditError("Post-build I-VIII freeze-manifest audit failed.")

    # Final report outputs.
    write_tsv(
        reports / "REVIEWED_FREEZE_BUILD_AUDIT_I_VIII.tsv",
        rows,
        [
            "volume", "volume_dir", "chapters_expected", "status_rows",
            "frozen_rows", "complete_rows", "active_includes", "manifest_entries",
            "manifest_shared_metadata_refreshes", "manifest_status", "build_status",
            "pdf", "bytes", "sha256",
        ],
    )
    write_tsv(
        reports / "REVIEWED_FREEZE_MANIFEST_FINDINGS_I_VIII.tsv",
        manifest_findings,
        ["volume", "path", "status", "expected", "actual", "repair"],
    )

    summary = {
        "status": "PASS",
        "volumes": 8,
        "canonical_chapters": expected_total,
        "all_status_rows_frozen_complete": True,
        "all_freeze_manifests_verified": True,
        "all_canonical_builds_passed": True,
        "shared_metadata_hashes_refreshed": sum(
            1 for f in manifest_findings
            if f["status"] == "REFRESHED_SHARED_METADATA"
        ),
        "mathematical_source_drift": 0,
        "missing_manifest_paths": 0,
    }
    (reports / "REVIEWED_FREEZE_BUILD_AUDIT_I_VIII.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )

    out = [
        "# I-VIII Reviewed Freeze and Canonical Build Audit",
        "",
        "**Result: PASS**",
        "",
        f"- Canonical volumes: **8**",
        f"- Canonical chapters/status rows: **{expected_total}**",
        "- All chapter rows: **FROZEN / COMPLETE**",
        "- All active chapter include counts: **PASS**",
        "- All eight freeze manifests: **PASS**",
        "- Mathematical-source manifest drift: **0**",
        "- Missing manifest paths: **0**",
        "- Clean canonical PDF builds: **8 / 8 PASS**",
        f"- Shared-metadata manifest hashes refreshed: **{summary['shared_metadata_hashes_refreshed']}**",
        "",
        "## Interpretation",
        "",
        "The audit distinguishes immutable mathematical-source drift from mutable",
        "series metadata. Canonical chapter/source drift is always blocking. A stale",
        "hash for explicitly shared metadata such as the global chapter-status or",
        "build inventory may be refreshed only when `--repair-shared-metadata` is used,",
        "and every such refresh is recorded in the manifest-findings TSV.",
        "",
        "The PDF SHA-256 values in the build inventory describe this clean toolchain run.",
        "Source freeze manifests are the authoritative frozen-source evidence; PDF bytes",
        "are not assumed to be reproducible across different TeX installations.",
    ]
    (reports / "REVIEWED_FREEZE_BUILD_AUDIT_I_VIII.md").write_text(
        "\n".join(out) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2))
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AuditError as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
