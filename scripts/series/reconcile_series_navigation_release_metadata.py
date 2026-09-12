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

CANDIDATE = "v1.3-rc1"
RELEASE_DIR = "theory_of_mathematics_i_viii_v1.3-rc1"
VOLUMES = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII")


def run(repo: Path, label: str, script: str, *extra: str) -> None:
    cmd = [sys.executable, str(repo / script), "--repo", str(repo), *extra]
    print(f"\n=== {label} ===")
    print("$", " ".join(cmd))
    cp = subprocess.run(cmd, cwd=repo, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if cp.stdout:
        print(cp.stdout, end="" if cp.stdout.endswith("\n") else "\n")
    if cp.stderr:
        print(cp.stderr, end="" if cp.stderr.endswith("\n") else "\n", file=sys.stderr)
    if cp.returncode:
        raise SystemExit(f"{label} failed with exit code {cp.returncode}")


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


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def replace_section(path: Path, heading: str, body: str) -> None:
    text = path.read_text(encoding="utf-8-sig", errors="replace") if path.exists() else ""
    block = heading + "\n\n" + body.rstrip() + "\n"
    rx = re.compile(r"(?ms)^" + re.escape(heading) + r"\n.*?(?=^## |\Z)")
    if rx.search(text):
        text = rx.sub(block, text)
    else:
        text = text.rstrip() + "\n\n" + block
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")



def preserve_volume02_professional_review_navigation(repo: Path) -> None:
    vol = repo / "books" / "vol02_real_analysis"
    landing = vol / "LANDING.md"
    nav = vol / "MATHEMATICAL_NAVIGATION.md"

    if landing.exists():
        text = landing.read_text(encoding="utf-8-sig", errors="replace")
        text = text.replace(
            "**Chapter architecture:** 25 chapters",
            "**Chapter architecture:** 25 numbered chapters + 1 unnumbered general-topology interlude",
        )
        marker = "- ✓ **II/07 — Connectedness and Path Connectedness** — `FROZEN` / `COMPLETE`"
        interlude = "- ↪ **General Topological Spaces** — unnumbered professional-review interlude"
        if marker in text and interlude not in text:
            text = text.replace(marker, marker + "\n" + interlude, 1)
        landing.write_text(text, encoding="utf-8")

    if nav.exists():
        text = nav.read_text(encoding="utf-8-sig", errors="replace")
        bullet = (
            "- **General Topological Spaces (interlude)** → **VII/01 — Topological Manifolds** — "
            "General topology, subspaces, products, homeomorphisms, separation, and countability "
            "clarify which later manifold constructions are purely topological."
        )
        if bullet not in text:
            anchor = (
                "- **II/05 — Metric Spaces and Continuity** → **VII/01 — Topological Manifolds** — "
                "Metric-space continuity prepares the topology underlying manifolds."
            )
            if anchor in text:
                text = text.replace(anchor, anchor + "\n" + bullet, 1)
            else:
                text = text.rstrip() + "\n\n## Professional-review topology interlude\n\n" + bullet + "\n"
        nav.write_text(text, encoding="utf-8")

def latest_path_commit(repo: Path, rel: str) -> str:
    cp = subprocess.run(["git", "-C", str(repo), "log", "-1", "--format=%H", "--", rel], text=True, capture_output=True, encoding="utf-8", errors="replace")
    return cp.stdout.strip() if cp.returncode == 0 else ""


def main() -> int:
    ap = argparse.ArgumentParser(description="Reconcile cross-volume navigation and series release metadata.")
    ap.add_argument("--repo", required=True)
    ap.add_argument("--gate-commit", default="")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports" / "series"
    release = repo / "release"
    books = repo / "books"

    gate_path = reports / "FINAL_RELEASE_CANDIDATE_GATE_I_VIII.json"
    if not gate_path.exists():
        raise SystemExit("Final release-candidate gate report is missing.")
    gate = load_json(gate_path)
    if gate.get("status") != "PASS":
        raise SystemExit("Final release-candidate gate is not PASS.")

    gate_commit = args.gate_commit or git(repo, "rev-parse", "HEAD")

    # Order matters: generate_navigation rewrites base LANDING/SERIES_NAVIGATION;
    # build_cross_volume_navigation then restores curated mathematical bridges.
    run(repo, "Regenerate canonical navigation/metadata inventory", "scripts/series/generate_navigation.py", "--build-inventory", str(reports / "BUILD_I_VIII.tsv"))
    run(repo, "Regenerate curated cross-volume mathematical navigation", "scripts/series/build_cross_volume_navigation.py")
    preserve_volume02_professional_review_navigation(repo)
    run(
        repo,
        "Refresh Volume II navigation hash in professional-review freeze",
        "scripts/series/refresh_volume02_professional_review_freeze.py",
        "--metadata-only",
    )
    run(repo, "Refresh release dashboard/master manifest", "scripts/series/generate_release_dashboard.py")

    nav_summary = load_json(reports / "CROSS_VOLUME_NAVIGATION_SUMMARY.json")
    if nav_summary.get("status") != "PASS":
        raise SystemExit("Cross-volume navigation summary is not PASS.")

    master = read_tsv(release / "SERIES_MASTER_MANIFEST.tsv")
    blockers = []
    if len(master) != 8:
        blockers.append(f"SERIES_MASTER_MANIFEST rows={len(master)} expected=8")
    seen = {r.get("volume") for r in master}
    if seen != set(VOLUMES):
        blockers.append(f"volume set mismatch: {sorted(seen)}")
    not_released = [r.get("volume") for r in master if r.get("readiness") != "RELEASED"]
    if not_released:
        blockers.append("not RELEASED: " + ", ".join(not_released))
    if any(r.get("build_status") != "PASS" for r in master):
        blockers.append("one or more series master-manifest build rows are not PASS")
    if blockers:
        raise SystemExit("Release metadata reconciliation blocked:\n- " + "\n- ".join(blockers))

    freeze_commits = {}
    freeze_files = {}
    for r in master:
        v = r["volume"]
        n = VOLUMES.index(v) + 1
        # Resolve directory from canonical master manifest source titles by the known series layout.
        dirs = sorted((repo / "books").glob(f"vol{n:02d}_*"))
        if len(dirs) != 1:
            raise SystemExit(f"Volume {v}: expected one books/vol{n:02d}_* directory, found {len(dirs)}")
        rel = dirs[0].relative_to(repo).as_posix()
        release_doc = f"{rel}/freeze/RELEASE_VOLUME{n:02d}.md"
        manifest = f"{rel}/freeze/VOLUME{n:02d}_FREEZE_MANIFEST.sha256"
        freeze_files[v] = {"release_doc": release_doc, "freeze_manifest": manifest}
        freeze_commits[v] = latest_path_commit(repo, release_doc)

    # Add the release-candidate pointers only after the generators finish: the
    # generic navigation generator rewrites SERIES_NAVIGATION.md from scratch.
    replace_section(
        books / "SERIES_NAVIGATION.md",
        "## Release-candidate state",
        f"Canonical release candidate: **{CANDIDATE}**.\n\n"
        f"The final I-VIII gate is **PASS** for all 8 volumes / 256 chapters. "
        f"Machine-readable release metadata is in `../release/SERIES_RELEASE_METADATA.json`; "
        f"the canonical release package will be written to `../release/{RELEASE_DIR}/` by the release commit.",
    )
    replace_section(
        release / "README.md",
        "## Current canonical candidate",
        f"- Candidate: **Theory of Mathematics I-VIII {CANDIDATE}**\n"
        f"- Final I-VIII release-candidate gate: **PASS**\n"
        f"- Volumes / chapters: **8 / 256**\n"
        f"- Canonical builds: **8 / 8 PASS**\n"
        f"- Cross-volume navigation reconciliation: **PASS**\n"
        f"- Metadata: `SERIES_RELEASE_METADATA.json`\n"
        f"- Target package directory: `{RELEASE_DIR}/`",
    )

    nav_files = [
        books / "SERIES_NAVIGATION.md",
        books / "CROSS_VOLUME_MATHEMATICAL_NAVIGATION.md",
        books / "CROSS_VOLUME_REFERENCE_AUDIT.tsv",
        books / "VOLUME_METADATA_AUDIT.tsv",
        reports / "CROSS_VOLUME_CHAPTER_BRIDGES.tsv",
        reports / "CROSS_VOLUME_DEPENDENCY_MAP.tsv",
        reports / "CROSS_VOLUME_NAVIGATION_SUMMARY.json",
        release / "README.md",
        release / "SERIES_MASTER_MANIFEST.tsv",
        release / "SERIES_RELEASE_DASHBOARD.md",
        release / "SERIES_RELEASE_READINESS.json",
    ]
    nav_hashes = {p.relative_to(repo).as_posix(): sha(p) for p in nav_files if p.exists()}

    metadata = {
        "schema": 1,
        "series": "Theory of Mathematics I-VIII",
        "candidate": CANDIDATE,
        "release_directory": f"release/{RELEASE_DIR}",
        "previous_final_release": "v1.2",
        "gate_status": gate.get("status"),
        "gate_source_commit": gate.get("source_commit"),
        "gate_commit": gate_commit,
        "metadata_source_commit": git(repo, "rev-parse", "HEAD"),
        "volumes": 8,
        "chapters": 256,
        "released_rows": sum(r.get("readiness") == "RELEASED" for r in master),
        "build_pass_rows": sum(r.get("build_status") == "PASS" for r in master),
        "cross_volume_navigation": nav_summary,
        "volume_freeze_commits": freeze_commits,
        "volume_freeze_files": freeze_files,
        "navigation_release_hashes": nav_hashes,
        "blocking": [],
        "status": "PASS",
    }
    (release / "SERIES_RELEASE_METADATA.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    summary = {
        "schema": 1,
        "status": "PASS",
        "candidate": CANDIDATE,
        "gate_commit": gate_commit,
        "series_master_rows": len(master),
        "released": sum(r.get("readiness") == "RELEASED" for r in master),
        "build_pass": sum(r.get("build_status") == "PASS" for r in master),
        "volume_edges": nav_summary.get("volume_edges"),
        "chapter_bridges": nav_summary.get("chapter_bridges"),
        "cross_volume_chapter_bridges": nav_summary.get("cross_volume_chapter_bridges"),
        "navigation_sidecars": nav_summary.get("volume_navigation_sidecars"),
        "metadata_file": "release/SERIES_RELEASE_METADATA.json",
        "blocking": [],
    }
    (reports / "SERIES_NAVIGATION_RELEASE_RECONCILIATION.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (reports / "SERIES_NAVIGATION_RELEASE_RECONCILIATION.md").write_text(
        "# Series Navigation and Release-Metadata Reconciliation\n\n"
        "**Result: PASS**\n\n"
        f"- Candidate: **{CANDIDATE}**\n"
        f"- Final gate commit: `{gate_commit}`\n"
        f"- Release-ready volumes: **{summary['released']} / 8**\n"
        f"- Canonical build PASS rows: **{summary['build_pass']} / 8**\n"
        f"- Curated volume edges: **{summary['volume_edges']}**\n"
        f"- Curated chapter bridges: **{summary['chapter_bridges']}**\n"
        f"- Per-volume mathematical navigation sidecars: **{summary['navigation_sidecars']} / 8**\n"
        "- Generic navigation, curated mathematical navigation, dashboard, and machine-readable metadata now agree.\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
