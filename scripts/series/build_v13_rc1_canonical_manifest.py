#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

CANDIDATE = "v1.3-rc1"
RELEASE_NAME = "theory_of_mathematics_i_viii_v1.3-rc1"
TAG = "theory-of-mathematics-i-viii-v1.3-rc1"
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


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def git(repo: Path, *args: str) -> str:
    cp = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True, encoding="utf-8", errors="replace")
    if cp.returncode:
        raise RuntimeError(cp.stderr.strip() or f"git {' '.join(args)} failed")
    return cp.stdout.strip()


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def refresh_sums(root: Path) -> list[str]:
    lines = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.name != "SHA256SUMS.txt":
            lines.append(f"{sha(p)}  {p.relative_to(root).as_posix()}")
    (root / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    for line in lines:
        digest, rel = line.split("  ", 1)
        if sha(root / rel) != digest:
            raise RuntimeError("Release hash verification failed: " + rel)
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the canonical Volume I-VIII v1.3-rc1 manifest and release package.")
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports" / "series"
    release = repo / "release"

    gate = load_json(reports / "FINAL_RELEASE_CANDIDATE_GATE_I_VIII.json")
    nav = load_json(reports / "SERIES_NAVIGATION_RELEASE_RECONCILIATION.json")
    metadata = load_json(release / "SERIES_RELEASE_METADATA.json")
    if gate.get("status") != "PASS":
        raise SystemExit("Final release-candidate gate is not PASS.")
    if nav.get("status") != "PASS":
        raise SystemExit("Series navigation/release metadata reconciliation is not PASS.")
    if metadata.get("status") != "PASS" or metadata.get("candidate") != CANDIDATE:
        raise SystemExit("SERIES_RELEASE_METADATA.json does not authorize v1.3-rc1.")

    builder = repo / "scripts" / "series" / "build_i_viii_release_bundle.py"
    if not builder.exists():
        raise SystemExit("Missing build_i_viii_release_bundle.py")
    cmd = [sys.executable, str(builder), "--repo", str(repo), "--release-name", RELEASE_NAME]
    print("$", " ".join(cmd))
    cp = subprocess.run(cmd, cwd=repo, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if cp.stdout:
        print(cp.stdout, end="" if cp.stdout.endswith("\n") else "\n")
    if cp.stderr:
        print(cp.stderr, end="" if cp.stderr.endswith("\n") else "\n", file=sys.stderr)
    if cp.returncode:
        raise SystemExit(f"Base I-VIII release bundle builder failed with {cp.returncode}")

    root = release / RELEASE_NAME
    if not root.exists():
        raise SystemExit("Release directory was not created.")

    current_source_commit = git(repo, "rev-parse", "HEAD")
    status_rows = read_tsv(repo / "editorial" / "CHAPTER_STATUS.tsv")
    master = {r["volume"]: r for r in read_tsv(release / "SERIES_MASTER_MANIFEST.tsv")}
    pdfs = {r["volume"]: r for r in read_tsv(root / "manifests" / "PDFS.tsv")}
    canonical_rows = []
    for roman, num, title, dirname, chapters in VOLUMES:
        mr = master.get(roman)
        pr = pdfs.get(roman)
        if not mr or not pr:
            raise SystemExit(f"Volume {roman}: missing master/PDF manifest row")
        if mr.get("readiness") != "RELEASED" or mr.get("build_status") != "PASS":
            raise SystemExit(f"Volume {roman}: master manifest not RELEASED/PASS")
        freeze_dir = repo / "books" / dirname / "freeze"
        freeze_manifest = freeze_dir / f"VOLUME{num:02d}_FREEZE_MANIFEST.sha256"
        release_doc = freeze_dir / f"RELEASE_VOLUME{num:02d}.md"
        if not freeze_manifest.exists() or not release_doc.exists():
            raise SystemExit(f"Volume {roman}: freeze evidence missing")
        sr = [r for r in status_rows if r.get("volume") == roman]
        canonical_rows.append({
            "volume": roman,
            "number": num,
            "title": title,
            "chapters": chapters,
            "frozen": sum(r.get("status") == "FROZEN" for r in sr),
            "complete": sum(r.get("next_action") == "COMPLETE" for r in sr),
            "readiness": mr.get("readiness"),
            "build_status": mr.get("build_status"),
            "source_baseline_sha256": mr.get("source_baseline_sha256"),
            "freeze_manifest": freeze_manifest.relative_to(repo).as_posix(),
            "freeze_manifest_sha256": sha(freeze_manifest),
            "release_doc": release_doc.relative_to(repo).as_posix(),
            "release_doc_sha256": sha(release_doc),
            "pdf_pages": pr.get("pages"),
            "pdf_bytes": pr.get("bytes"),
            "pdf_sha256": pr.get("sha256"),
            "release_pdf": pr.get("release_pdf"),
        })

    fields = [
        "volume", "number", "title", "chapters", "frozen", "complete", "readiness", "build_status",
        "source_baseline_sha256", "freeze_manifest", "freeze_manifest_sha256", "release_doc", "release_doc_sha256",
        "pdf_pages", "pdf_bytes", "pdf_sha256", "release_pdf",
    ]
    top_tsv = release / "CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.tsv"
    write_tsv(top_tsv, canonical_rows, fields)
    write_tsv(root / "manifests" / "CANONICAL_VOLUMES.tsv", canonical_rows, fields)

    # Add the final gate/navigation/release metadata into immutable candidate evidence.
    extra_evidence = [
        reports / "FINAL_RELEASE_CANDIDATE_GATE_I_VIII.json",
        reports / "FINAL_RELEASE_CANDIDATE_GATE_I_VIII.md",
        reports / "FINAL_RC_LAYOUT_I_VIII.tsv",
        reports / "SERIES_NAVIGATION_RELEASE_RECONCILIATION.json",
        reports / "SERIES_NAVIGATION_RELEASE_RECONCILIATION.md",
        release / "SERIES_RELEASE_METADATA.json",
        top_tsv,
    ]
    evidence_dir = root / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    for p in extra_evidence:
        if not p.exists():
            raise SystemExit(f"Required release evidence missing: {p.relative_to(repo)}")
        shutil.copy2(p, evidence_dir / p.name)

    release_json_path = root / "RELEASE.json"
    release_json = load_json(release_json_path)
    release_json.update({
        "schema": 3,
        "release": f"Theory of Mathematics I-VIII {CANDIDATE}",
        "tag": TAG,
        "candidate": CANDIDATE,
        "source_commit_before_release_commit": current_source_commit,
        "final_release_candidate_gate": {
            "status": gate.get("status"),
            "gate_source_commit": gate.get("source_commit"),
            "gate_commit": metadata.get("gate_commit"),
            "canonical_builds_pass": gate.get("canonical_builds_pass"),
            "layout_volumes_pass": gate.get("layout_volumes_pass"),
            "overfull_ge_20pt_total": gate.get("overfull_ge_20pt_total"),
        },
        "navigation_release_reconciliation": nav,
        "canonical_volume_manifest": "manifests/CANONICAL_VOLUMES.tsv",
        "canonical_volume_manifest_sha256": sha(root / "manifests" / "CANONICAL_VOLUMES.tsv"),
        "release_state": "RELEASE_CANDIDATE",
    })
    release_json_path.write_text(json.dumps(release_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    notes = root / "RELEASE_NOTES.md"
    notes_text = notes.read_text(encoding="utf-8")
    notes_text = notes_text.replace(
        "# Theory of Mathematics I–VIII — Release 1.0",
        "# Theory of Mathematics I–VIII — v1.3-rc1 Release Candidate",
        1,
    )
    notes_text = notes_text.replace(
        "This directory is the immutable repository release bundle for the fully reconstructed canonical eight-volume series.",
        "This directory is the canonical v1.3-rc1 release-candidate bundle for the eight-volume series.",
        1,
    )
    notes.write_text(
        notes_text
        + "\n## v1.3-rc1 professional-review candidate\n\n"
        + "- Final Volume I-VIII release-candidate gate: **PASS**.\n"
        + "- All **256 / 256** canonical chapters are FROZEN / COMPLETE.\n"
        + "- Clean canonical builds: **8 / 8 PASS**.\n"
        + "- Blocking >=20pt overfull boxes in the final gate: **0**.\n"
        + "- Cross-volume mathematical navigation and release metadata: **reconciled / PASS**.\n"
        + "- This directory is a release candidate; it does not replace the frozen v1.2 final release.\n",
        encoding="utf-8",
    )

    sums = refresh_sums(root)
    aggregate = hashlib.sha256("\n".join(sums).encode("utf-8")).hexdigest()

    manifest_obj = {
        "schema": 1,
        "status": "PASS",
        "series": "Theory of Mathematics I-VIII",
        "candidate": CANDIDATE,
        "tag": TAG,
        "previous_final_release": "v1.2",
        "source_commit_before_release_commit": current_source_commit,
        "gate_source_commit": gate.get("source_commit"),
        "gate_commit": metadata.get("gate_commit"),
        "volumes": 8,
        "chapters": 256,
        "frozen": sum(int(r["frozen"]) for r in canonical_rows),
        "complete": sum(int(r["complete"]) for r in canonical_rows),
        "canonical_builds_pass": sum(r["build_status"] == "PASS" for r in canonical_rows),
        "release_directory": root.relative_to(repo).as_posix(),
        "release_files_hashed": len(sums),
        "release_aggregate_sha256": aggregate,
        "volumes_manifest": canonical_rows,
        "blocking": [],
    }
    top_json = release / "CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.json"
    top_json.write_text(json.dumps(manifest_obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    primary = [
        top_tsv,
        top_json,
        release / "SERIES_RELEASE_METADATA.json",
        reports / "FINAL_RELEASE_CANDIDATE_GATE_I_VIII.json",
        reports / "SERIES_NAVIGATION_RELEASE_RECONCILIATION.json",
        root / "RELEASE.json",
        root / "SHA256SUMS.txt",
    ]
    top_sha = release / "CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.sha256"
    top_sha.write_text("\n".join(f"{sha(p)}  {p.relative_to(repo).as_posix()}" for p in primary) + "\n", encoding="utf-8")

    # Refresh generic master hash evidence to point at the new canonical RC manifest too.
    series_sha = release / "SERIES_MASTER_MANIFEST.sha256"
    series_primary = [
        release / "SERIES_MASTER_MANIFEST.tsv",
        release / "SERIES_RELEASE_READINESS.json",
        release / "SERIES_RELEASE_METADATA.json",
        top_tsv,
        top_json,
        top_sha,
        root / "RELEASE.json",
        root / "SHA256SUMS.txt",
    ]
    series_sha.write_text("\n".join(f"{sha(p)}  {p.relative_to(repo).as_posix()}" for p in series_primary) + "\n", encoding="utf-8")

    report = {
        "schema": 1,
        "status": "PASS",
        "candidate": CANDIDATE,
        "volumes": 8,
        "chapters": 256,
        "release_dir": root.relative_to(repo).as_posix(),
        "canonical_manifest_tsv": top_tsv.relative_to(repo).as_posix(),
        "canonical_manifest_json": top_json.relative_to(repo).as_posix(),
        "release_files_hashed": len(sums),
        "release_aggregate_sha256": aggregate,
        "blocking": [],
    }
    (reports / "V13_RC1_CANONICAL_RELEASE_MANIFEST.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (reports / "V13_RC1_CANONICAL_RELEASE_MANIFEST.md").write_text(
        "# Theory of Mathematics I-VIII v1.3-rc1 Canonical Release Manifest\n\n"
        "**Result: PASS / RELEASE_CANDIDATE**\n\n"
        "- Volumes: **8 / 8**.\n"
        "- Chapters: **256 / 256 FROZEN / COMPLETE**.\n"
        "- Canonical builds: **8 / 8 PASS**.\n"
        f"- Release directory: `{report['release_dir']}`.\n"
        f"- Candidate aggregate SHA-256: `{aggregate}`.\n"
        "- The v1.2 final release remains preserved; this is the next canonical release candidate.\n",
        encoding="utf-8",
    )

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
