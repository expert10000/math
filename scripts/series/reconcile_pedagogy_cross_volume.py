#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

VOLUMES = [
    ("I", 1, "vol01_linear_algebra", 18),
    ("II", 2, "vol02_real_analysis", 25),
    ("III", 3, "vol03_fourier_distributions_pde", 28),
    ("IV", 4, "vol04_complex_analysis", 31),
    ("V", 5, "vol05_commutative_algebra", 28),
    ("VI", 6, "vol06_algebraic_geometry", 49),
    ("VII", 7, "vol07_differential_geometry", 42),
    ("VIII", 8, "vol08_algebraic_topology", 35),
]
EXPECTED_SERIES_CHAPTERS = 256
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
EXERCISE_RE = re.compile(r"\\begin\{exercise\}(?:\[[^\]]*\])?(.*?)\\end\{exercise\}", re.S)
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path: Path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        cut = None
        for i, ch in enumerate(line):
            if ch != "%":
                continue
            bs = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                bs += 1
                j -= 1
            if bs % 2 == 0:
                cut = i
                break
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)


def resolve_tex(current: Path, target: str, volume_root: Path, repo: Path):
    raw = Path(target)
    candidates = [current.parent / raw, volume_root / raw, repo / raw]
    for candidate in candidates:
        for q in (candidate, candidate.with_suffix(".tex") if candidate.suffix == "" else candidate):
            try:
                q = q.resolve()
            except Exception:
                pass
            if q.exists() and q.is_file():
                return q
    return None


def active_volume_tex_graph(repo: Path, volume_root: Path):
    book = volume_root / "book.tex"
    if not book.exists():
        return []
    seen = set()
    stack = [book.resolve()]
    while stack:
        p = stack.pop()
        if p in seen or not p.exists():
            continue
        seen.add(p)
        text = strip_comments(p.read_text(encoding="utf-8-sig", errors="replace"))
        for target in INPUT_RE.findall(text):
            q = resolve_tex(p, target, volume_root, repo)
            if q is not None and q not in seen:
                stack.append(q)
    vr = volume_root.resolve()
    return sorted(
        [p for p in seen if p == book.resolve() or vr in p.parents],
        key=lambda p: p.as_posix(),
    )


def git_blob(repo: Path, rel: str):
    cp = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", f"HEAD:{rel}"],
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8", errors="replace",
    )
    return cp.stdout.strip() if cp.returncode == 0 else ""


def normalize_prompt(body: str) -> str:
    body = re.sub(r"\\label\{[^}]+\}", " ", body)
    body = re.sub(r"\s+", " ", strip_comments(body)).strip()
    return body


def row_counts(row: dict):
    split = "composed_examples" in row
    def get(k):
        return int(row.get(f"composed_{k}" if split else k, 0) or 0)
    def added(k):
        return int(row.get(f"expansion_{k}", 0) or 0)
    return {
        "examples": get("examples"),
        "exercises": get("exercises"),
        "hints": get("hints"),
        "problems": get("problems"),
        "solutions": get("solutions"),
        "labels": get("labels"),
        "added_examples": added("examples"),
        "added_exercises": added("exercises"),
        "added_hints": added("hints"),
        "added_solutions": added("solutions"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"

    audit_path = reports / "SERIES_PEDAGOGY_AUDIT.json"
    if not audit_path.exists():
        raise SystemExit("SERIES_PEDAGOGY_AUDIT.json missing; run commit 1 audit first.")
    audit = json.loads(audit_path.read_text(encoding="utf-8-sig"))
    if audit.get("status") != "PASS":
        raise SystemExit("Series pedagogy audit is not PASS.")

    blockers = []
    observations = []
    count_rows = []
    hash_rows = []
    labels = defaultdict(list)
    prompts = defaultdict(list)
    active_tex_files = 0

    for roman, num, dirname, expected in VOLUMES:
        recon = reports / f"VOLUME{num:02d}_EXAMPLE_EXERCISE_RECONCILIATION.json"
        hashes = reports / f"VOLUME{num:02d}_EXAMPLE_EXERCISE_HASHES.tsv"
        data = json.loads(recon.read_text(encoding="utf-8-sig"))
        architecture = data.get("architecture", "direct-chapter")

        chapters = data.get("chapters", [])
        if len(chapters) != expected:
            blockers.append(f"{roman}: reconciliation chapter rows={len(chapters)}, expected={expected}")

        for row in chapters:
            c = row_counts(row)
            count_rows.append({
                "volume": roman,
                "chapter": row.get("chapter", ""),
                "architecture": architecture,
                **c,
            })

        hrows = read_tsv(hashes)
        if len(hrows) != expected:
            blockers.append(f"{roman}: hash ledger rows={len(hrows)}, expected={expected}")
        for hrow in hrows:
            canonical_path = hrow.get("canonical_path") or hrow.get("path") or ""
            canonical_sha = (hrow.get("canonical_sha256") or hrow.get("sha256") or "").lower()
            pedagogy_path = hrow.get("pedagogy_path") or ""
            pedagogy_sha = (hrow.get("pedagogy_sha256") or "").lower()
            protected_blob = hrow.get("protected_git_blob_sha1") or ""
            composed_sha = hrow.get("composed_sha256") or ""
            chapter = hrow.get("chapter", "")

            cp = repo / canonical_path if canonical_path else None
            canonical_ok = bool(cp and cp.exists() and sha256_file(cp) == canonical_sha)
            if not canonical_ok:
                blockers.append(f"{chapter}: canonical SHA-256 mismatch or file missing")

            pedagogy_ok = ""
            if pedagogy_path:
                pp = repo / pedagogy_path
                pedagogy_ok = "YES" if pp.exists() and sha256_file(pp) == pedagogy_sha else "NO"
                if pedagogy_ok != "YES":
                    blockers.append(f"{chapter}: pedagogy SHA-256 mismatch or file missing")

            blob_ok = ""
            if protected_blob and canonical_path:
                blob_ok = "YES" if git_blob(repo, canonical_path) == protected_blob else "NO"
                if blob_ok != "YES":
                    blockers.append(f"{chapter}: protected Git blob drift")

            hash_rows.append({
                "volume": roman,
                "chapter": chapter,
                "canonical_path": canonical_path or "-",
                "canonical_sha256": canonical_sha or "-",
                "canonical_verified": "YES" if canonical_ok else "NO",
                "protected_git_blob_sha1": protected_blob or "-",
                "protected_git_blob_verified": blob_ok or "-",
                "pedagogy_path": pedagogy_path or "-",
                "pedagogy_sha256": pedagogy_sha or "-",
                "pedagogy_verified": pedagogy_ok or "-",
                "composed_sha256": composed_sha or "-",
            })

        volume_root = repo / "books" / dirname
        graph = active_volume_tex_graph(repo, volume_root)
        active_tex_files += len(graph)
        for p in graph:
            rel = p.relative_to(repo).as_posix()
            text = strip_comments(p.read_text(encoding="utf-8-sig", errors="replace"))
            for lab in LABEL_RE.findall(text):
                labels[lab].append(rel)
            for body in EXERCISE_RE.findall(text):
                prompt = normalize_prompt(body)
                if prompt:
                    prompts[prompt].append(rel)

    if len(count_rows) != EXPECTED_SERIES_CHAPTERS:
        blockers.append(f"master count rows={len(count_rows)}, expected={EXPECTED_SERIES_CHAPTERS}")
    if len(hash_rows) != EXPECTED_SERIES_CHAPTERS:
        blockers.append(f"master hash rows={len(hash_rows)}, expected={EXPECTED_SERIES_CHAPTERS}")
    if len({r["chapter"] for r in count_rows}) != EXPECTED_SERIES_CHAPTERS:
        blockers.append("master count ledger has duplicate/missing chapter codes")
    if len({r["chapter"] for r in hash_rows}) != EXPECTED_SERIES_CHAPTERS:
        blockers.append("master hash ledger has duplicate/missing chapter codes")

    duplicate_labels = {
        lab: paths for lab, paths in labels.items()
        if len(paths) > 1
    }
    if duplicate_labels:
        blockers.append(f"duplicate active labels across series={len(duplicate_labels)}")

    duplicate_prompts = []
    for prompt, paths in prompts.items():
        uniq = sorted(set(paths))
        if len(uniq) > 1:
            duplicate_prompts.append({
                "prompt": prompt,
                "occurrences": len(paths),
                "files": uniq,
            })
    duplicate_prompts.sort(key=lambda x: (-x["occurrences"], x["prompt"]))
    if duplicate_prompts:
        observations.append(
            f"exact normalized exercise-prompt duplicate groups={len(duplicate_prompts)}; "
            "reported for editorial review, not blocking by itself"
        )

    count_fields = [
        "volume", "chapter", "architecture",
        "examples", "exercises", "hints", "problems", "solutions", "labels",
        "added_examples", "added_exercises", "added_hints", "added_solutions",
    ]
    write_tsv(reports / "SERIES_PEDAGOGY_COUNTS.tsv", count_rows, count_fields)

    hash_fields = [
        "volume", "chapter", "canonical_path", "canonical_sha256", "canonical_verified",
        "protected_git_blob_sha1", "protected_git_blob_verified",
        "pedagogy_path", "pedagogy_sha256", "pedagogy_verified", "composed_sha256",
    ]
    write_tsv(reports / "SERIES_PEDAGOGY_HASHES.tsv", hash_rows, hash_fields)

    series_totals = {}
    for key in ("examples", "exercises", "hints", "problems", "solutions", "labels",
                "added_examples", "added_exercises", "added_hints", "added_solutions"):
        series_totals[key] = sum(int(r[key]) for r in count_rows)

    status = "PASS" if not blockers else "FAIL"
    result = {
        "schema": 1,
        "status": status,
        "scope": "Cross-volume pedagogy evidence, Volumes I-VIII",
        "chapters": len(count_rows),
        "hash_rows": len(hash_rows),
        "active_tex_files_scanned": active_tex_files,
        "active_unique_labels": len(labels),
        "duplicate_active_label_groups": len(duplicate_labels),
        "duplicate_active_labels": [
            {"label": lab, "files": paths}
            for lab, paths in sorted(duplicate_labels.items())
        ],
        "exact_duplicate_prompt_groups": len(duplicate_prompts),
        "duplicate_prompts": duplicate_prompts[:100],
        "series_totals": series_totals,
        "blocking": blockers,
        "observations": observations,
    }
    (reports / "SERIES_PEDAGOGY_CROSS_VOLUME.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    md = [
        "# Cross-volume pedagogy evidence reconciliation — Volumes I–VIII",
        "",
        f"**Result:** {status}",
        "",
        f"- chapter rows: **{len(count_rows)} / {EXPECTED_SERIES_CHAPTERS}**",
        f"- hash rows: **{len(hash_rows)} / {EXPECTED_SERIES_CHAPTERS}**",
        f"- active TeX files scanned: **{active_tex_files}**",
        f"- active unique labels: **{len(labels)}**",
        f"- duplicate active label groups: **{len(duplicate_labels)}**",
        f"- exact duplicate normalized exercise-prompt groups: **{len(duplicate_prompts)}**",
        "",
        "## Series totals",
        "",
    ]
    for key, value in series_totals.items():
        md.append(f"- {key}: **{value}**")
    md += ["", "## Duplicate-label audit", ""]
    if duplicate_labels:
        for lab, paths in sorted(duplicate_labels.items()):
            md.append(f"- `{lab}` — " + ", ".join(f"`{p}`" for p in paths))
    else:
        md.append("None.")
    md += ["", "## Exercise-prompt duplication review", ""]
    if duplicate_prompts:
        for item in duplicate_prompts[:25]:
            preview = item["prompt"][:180]
            md.append(f"- {item['occurrences']} occurrences: `{preview}`")
    else:
        md.append("None.")
    md += ["", "## Blocking findings", ""]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    md += ["", "## Observations", ""]
    md += [f"- {x}" for x in observations] if observations else ["None."]
    (reports / "SERIES_PEDAGOGY_CROSS_VOLUME.md").write_text(
        "\n".join(md).rstrip() + "\n", encoding="utf-8"
    )

    print(json.dumps({
        "status": status,
        "chapters": len(count_rows),
        "hash_rows": len(hash_rows),
        "duplicate_labels": len(duplicate_labels),
        "duplicate_prompts": len(duplicate_prompts),
        "series_totals": series_totals,
        "blocking": blockers,
    }, indent=2))
    return 0 if status == "PASS" else 12


if __name__ == "__main__":
    raise SystemExit(main())
