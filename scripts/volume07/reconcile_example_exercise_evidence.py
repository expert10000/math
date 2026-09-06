#!/usr/bin/env python3
import argparse
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

REPORT_DIR = Path("reports/series")
VOL_DIR = Path("books/vol07_differential_geometry")
BASELINE_REL = REPORT_DIR / "VOLUME07_EXAMPLE_EXERCISE_BASELINE.json"
AUDIT_REL = REPORT_DIR / "VOLUME07_EXAMPLE_EXERCISE_AUDIT.json"
BALANCE_REL = REPORT_DIR / "VOLUME07_EXAMPLE_EXERCISE_BALANCE_AUDIT.json"

LABEL_RE = re.compile(r"\\label\{([^}]+)\}")

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def count_env(text: str, env: str) -> int:
    return len(re.findall(rf"\\begin\{{{re.escape(env)}\}}", text))

def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    cp = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )
    if check and cp.returncode:
        raise RuntimeError(
            f"git {' '.join(args)} failed ({cp.returncode}):\n{cp.stderr}"
        )
    return cp

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--log", required=True)
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    pdf = Path(args.pdf).resolve()
    log = Path(args.log).resolve()
    out = repo / REPORT_DIR
    out.mkdir(parents=True, exist_ok=True)

    blockers = []
    observations = []
    rows = []
    hash_rows = []
    all_labels = []

    baseline_path = repo / BASELINE_REL
    audit_path = repo / AUDIT_REL
    balance_path = repo / BALANCE_REL

    if not baseline_path.exists():
        blockers.append("BASELINE_MISSING")
        baseline = {"chapters": []}
    else:
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))

    audit = {}
    if not audit_path.exists():
        blockers.append("EXPANSION_AUDIT_MISSING")
    else:
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        if audit.get("status") != "PASS":
            blockers.append(f"EXPANSION_AUDIT_STATUS:{audit.get('status')}")
        if audit.get("stage") != 5:
            blockers.append(f"EXPANSION_AUDIT_STAGE:{audit.get('stage')}!=5")
        if audit.get("expanded_count") != 42:
            blockers.append(
                f"EXPANSION_AUDIT_EXPANDED_COUNT:{audit.get('expanded_count')}!=42"
            )

    balance = {}
    if not balance_path.exists():
        blockers.append("BALANCE_AUDIT_MISSING")
    else:
        balance = json.loads(balance_path.read_text(encoding="utf-8"))
        if balance.get("status") != "PASS":
            blockers.append(f"BALANCE_AUDIT_STATUS:{balance.get('status')}")
        if balance.get("canonical_chapter_sources_modified") not in (0, None):
            blockers.append("BALANCE_AUDIT_CANONICAL_DRIFT")

    chapters = baseline.get("chapters", [])
    if len(chapters) != 42:
        blockers.append(f"BASELINE_CHAPTER_COUNT:{len(chapters)}!=42")

    added_totals = {
        "examples": 0,
        "exercises": 0,
        "hints": 0,
        "solutions": 0,
    }
    composed_totals = {
        "examples": 0,
        "exercises": 0,
        "hints": 0,
        "problems": 0,
        "solutions": 0,
        "labels": 0,
    }

    for item in chapters:
        code = item["chapter"]
        canonical_rel = item["path"]
        canonical = repo / canonical_rel
        expansion = canonical.parent / "pedagogy_expansion.tex"
        expansion_rel = expansion.relative_to(repo).as_posix()

        if not canonical.exists():
            blockers.append(f"{code}:CANONICAL_MISSING:{canonical_rel}")
            continue
        if not expansion.exists():
            blockers.append(f"{code}:EXPANSION_MISSING:{expansion_rel}")
            continue

        # Git-object protection is line-ending invariant.
        tracked_blob = git(repo, "rev-parse", f"HEAD:{canonical_rel}").stdout.strip()
        expected_blob = item.get("protected_git_blob_sha1")
        if tracked_blob != expected_blob:
            blockers.append(
                f"{code}:PROTECTED_GIT_BLOB_DRIFT:{tracked_blob}!={expected_blob}"
            )
        wt = git(repo, "diff", "--quiet", "HEAD", "--", canonical_rel, check=False)
        if wt.returncode == 1:
            blockers.append(f"{code}:PROTECTED_WORKTREE_DRIFT")
        elif wt.returncode not in (0, 1):
            blockers.append(f"{code}:PROTECTED_WORKTREE_CHECK_ERROR")

        ctext = canonical.read_text(encoding="utf-8-sig")
        etext = expansion.read_text(encoding="utf-8-sig")

        cc = {
            "examples": count_env(ctext, "example"),
            "exercises": count_env(ctext, "exercise"),
            "hints": count_env(ctext, "hint"),
            "problems": count_env(ctext, "problem"),
            "solutions": count_env(ctext, "solution"),
        }
        ec = {
            "examples": count_env(etext, "example"),
            "exercises": count_env(etext, "exercise"),
            "hints": count_env(etext, "hint"),
            "solutions": count_env(etext, "solution"),
        }

        expected_expansion = {
            "examples": 3,
            "exercises": 16,
            "hints": 16,
            "solutions": 16,
        }
        if ec != expected_expansion:
            blockers.append(f"{code}:EXPANSION_COUNTS:{ec}!={expected_expansion}")

        n = int(code.split("/")[1])
        marker = f"VII{n:02d}"
        if (
            f"% BEGIN VOL07-EXPANSION {marker}" not in etext
            or f"% END VOL07-EXPANSION {marker}" not in etext
        ):
            blockers.append(f"{code}:EXPANSION_BOUNDARY_MARKERS")

        labels = LABEL_RE.findall(ctext) + LABEL_RE.findall(etext)
        all_labels.extend(labels)

        composed = {
            "examples": cc["examples"] + ec["examples"],
            "exercises": cc["exercises"] + ec["exercises"],
            "hints": cc["hints"] + ec["hints"],
            "problems": cc["problems"],
            "solutions": cc["solutions"] + ec["solutions"],
            "labels": len(labels),
        }

        # Canonical corpus already passed its own exact hint/solution audit.
        # Keep a diagnostic here as a second independent check.
        if cc["exercises"] != cc["hints"]:
            blockers.append(
                f"{code}:CANONICAL_EXERCISE_HINT_IMBALANCE:"
                f"{cc['exercises']}!={cc['hints']}"
            )
        if cc["solutions"] != cc["exercises"] + cc["problems"]:
            blockers.append(
                f"{code}:CANONICAL_SOLUTION_COVERAGE:"
                f"{cc['solutions']}!={cc['exercises'] + cc['problems']}"
            )

        for k in added_totals:
            added_totals[k] += ec[k]
        for k in composed_totals:
            composed_totals[k] += composed[k]

        cbytes = canonical.read_bytes()
        ebytes = expansion.read_bytes()
        composed_sha = sha256_bytes(
            b"VOL07-COMPOSED\0" + cbytes + b"\0PEDAGOGY\0" + ebytes
        )

        row = {
            "chapter": code,
            "canonical_examples": cc["examples"],
            "canonical_exercises": cc["exercises"],
            "canonical_hints": cc["hints"],
            "canonical_problems": cc["problems"],
            "canonical_solutions": cc["solutions"],
            "expansion_examples": ec["examples"],
            "expansion_exercises": ec["exercises"],
            "expansion_hints": ec["hints"],
            "expansion_solutions": ec["solutions"],
            "composed_examples": composed["examples"],
            "composed_exercises": composed["exercises"],
            "composed_hints": composed["hints"],
            "composed_problems": composed["problems"],
            "composed_solutions": composed["solutions"],
            "composed_labels": composed["labels"],
        }
        rows.append(row)

        hash_rows.append(
            {
                "chapter": code,
                "canonical_path": canonical_rel,
                "canonical_sha256": sha256_file(canonical),
                "protected_git_blob_sha1": expected_blob,
                "pedagogy_path": expansion_rel,
                "pedagogy_sha256": sha256_file(expansion),
                "composed_sha256": composed_sha,
            }
        )

    expected_added = {
        "examples": 126,
        "exercises": 672,
        "hints": 672,
        "solutions": 672,
    }
    if added_totals != expected_added:
        blockers.append(f"ADDED_TOTALS:{added_totals}!={expected_added}")

    for label, n in Counter(all_labels).items():
        if n > 1:
            blockers.append(f"DUPLICATE_COMPOSED_LABEL:{label}:{n}")

    # Ensure book.tex wires all 42 pedagogy layers.
    book = repo / VOL_DIR / "book.tex"
    if not book.exists():
        blockers.append("BOOK_TEX_MISSING")
    else:
        btext = book.read_text(encoding="utf-8-sig")
        wire_count = btext.count("VOL07-PEDAGOGY VII/")
        if wire_count != 42:
            blockers.append(f"BOOK_PEDAGOGY_WIRING:{wire_count}!=42")
        for i in range(1, 43):
            if f"VOL07-PEDAGOGY VII/{i:02d}" not in btext:
                blockers.append(f"BOOK_PEDAGOGY_WIRING_MISSING:VII/{i:02d}")

    # Build/PDF evidence.
    pdfinfo = {
        "path": (pdf.relative_to(repo).as_posix()
                 if pdf.exists() and repo in pdf.parents else str(pdf)),
        "bytes": pdf.stat().st_size if pdf.exists() else None,
        "sha256": sha256_file(pdf) if pdf.exists() else None,
    }
    if not pdf.exists():
        blockers.append("PDF_MISSING")

    logtext = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    if not log.exists():
        blockers.append("LOG_MISSING")
    fatal_patterns = [
        "Fatal error occurred",
        "Emergency stop",
        "! LaTeX Error",
        "!  ==> Fatal error",
        "Undefined control sequence",
    ]
    for pat in fatal_patterns:
        if pat in logtext:
            blockers.append(f"TEX_FATAL:{pat}")
    if "There were undefined references" in logtext:
        blockers.append("UNDEFINED_REFERENCES")
    if "There were undefined citations" in logtext:
        blockers.append("UNDEFINED_CITATIONS")
    if "multiply defined" in logtext.lower():
        blockers.append("MULTIPLY_DEFINED_LABELS")
    if "Rerun to get cross-references right" in logtext:
        blockers.append("RERUN_WARNING_AFTER_BUILD")

    # Existing corpus audit is generated by AUDIT_VOLUME07.ps1. Validate its JSON
    # before the launcher restores the generated report files to HEAD.
    corpus_json = repo / "editorial/VOLUME_VII_CORPUS_AUDIT.json"
    corpus_status = None
    if corpus_json.exists():
        try:
            corpus = json.loads(corpus_json.read_text(encoding="utf-8-sig"))
            corpus_status = corpus.get("result")
            if corpus_status != "PASS":
                blockers.append(f"CORPUS_AUDIT_STATUS:{corpus_status}")
        except Exception as exc:
            blockers.append(f"CORPUS_AUDIT_JSON:{exc}")
    else:
        blockers.append("CORPUS_AUDIT_JSON_MISSING")

    tracked = git(repo, "ls-files", "scripts/volume07").stdout.splitlines()
    cache = [
        x for x in tracked
        if "/__pycache__/" in x or x.endswith(".pyc")
    ]
    if cache:
        blockers.extend(f"TRACKED_PYTHON_CACHE:{x}" for x in cache)

    status = "PASS" if not blockers else "FAIL"
    result = {
        "schema": 2,
        "status": status,
        "volume": "VII",
        "architecture": "split-pedagogy-layer",
        "chapter_count": len(rows),
        "added_totals": added_totals,
        "expected_added_totals": expected_added,
        "composed_totals": composed_totals,
        "chapters": rows,
        "pdf": pdfinfo,
        "upstream_audits": {
            "expansion": {
                "status": audit.get("status"),
                "stage": audit.get("stage"),
                "expanded_count": audit.get("expanded_count"),
            },
            "balance": {
                "status": balance.get("status"),
                "canonical_chapter_sources_modified":
                    balance.get("canonical_chapter_sources_modified"),
            },
            "corpus": {"status": corpus_status},
        },
        "tracked_python_cache": cache,
        "blocking": blockers,
        "observations": observations,
    }

    (out / "VOLUME07_EXAMPLE_EXERCISE_RECONCILIATION.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )

    count_fields = [
        "chapter",
        "canonical_examples", "canonical_exercises", "canonical_hints",
        "canonical_problems", "canonical_solutions",
        "expansion_examples", "expansion_exercises", "expansion_hints",
        "expansion_solutions",
        "composed_examples", "composed_exercises", "composed_hints",
        "composed_problems", "composed_solutions", "composed_labels",
    ]
    with (out / "VOLUME07_EXAMPLE_EXERCISE_COUNTS.tsv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        w = csv.DictWriter(f, fieldnames=count_fields, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    hash_fields = [
        "chapter", "canonical_path", "canonical_sha256",
        "protected_git_blob_sha1", "pedagogy_path", "pedagogy_sha256",
        "composed_sha256",
    ]
    with (out / "VOLUME07_EXAMPLE_EXERCISE_HASHES.tsv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        w = csv.DictWriter(f, fieldnames=hash_fields, delimiter="\t")
        w.writeheader()
        w.writerows(hash_rows)

    md = [
        "# Volume VII pedagogy reconciliation after example/exercise expansion",
        "",
        f"**Result:** {status}",
        "",
        "## Architecture",
        "",
        "- canonical chapter sources: protected and unchanged",
        "- pedagogy additions: chapter-local `pedagogy_expansion.tex` layers",
        "- composed evidence: canonical source + pedagogy layer",
        "",
        "## Added pedagogy totals",
        "",
        f"- worked examples: **{added_totals['examples']}**",
        f"- exercises: **{added_totals['exercises']}**",
        f"- hints: **{added_totals['hints']}**",
        f"- complete solutions: **{added_totals['solutions']}**",
        "",
        "## Composed Volume VII totals",
        "",
    ]
    for key, value in composed_totals.items():
        md.append(f"- {key}: **{value}**")
    md += [
        "",
        "## Upstream audits",
        "",
        f"- expansion audit: **{audit.get('status')}**, stage `{audit.get('stage')}`",
        f"- balance audit: **{balance.get('status')}**",
        f"- corpus audit: **{corpus_status}**",
        "",
        "## Canonical PDF",
        "",
        f"- path: `{pdfinfo['path']}`",
        f"- bytes: `{pdfinfo['bytes']}`",
        f"- SHA-256: `{pdfinfo['sha256']}`",
        "",
        "## Protection and hygiene",
        "",
        f"- reconciled chapters: **{len(rows)} / 42**",
        f"- duplicate composed labels: **{sum(1 for _, n in Counter(all_labels).items() if n > 1)}**",
        f"- tracked Python cache files: **{len(cache)}**",
        "",
        "## Blocking findings",
        "",
    ]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (out / "VOLUME07_EXAMPLE_EXERCISE_RECONCILIATION.md").write_text(
        "\n".join(md) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(
        {
            "status": status,
            "chapter_count": len(rows),
            "added_totals": added_totals,
            "composed_totals": composed_totals,
            "pdf": pdfinfo,
            "blocking": blockers,
        },
        indent=2,
    ))
    return 0 if status == "PASS" else 13

if __name__ == "__main__":
    raise SystemExit(main())
