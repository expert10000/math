#!/usr/bin/env python3
"""Validate the active Volume I--VIII TeX graph after a canonical build.

The checker is deliberately dependency-free so that a clean checkout needs only
Python 3 and the TeX tools already required for the build.  It writes transient
reports under build/ by default; release evidence is handled separately.
"""
from __future__ import annotations

import argparse
import json
import platform
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

VOLUMES = (
    ("I", "vol01_linear_algebra"),
    ("II", "vol02_real_analysis"),
    ("III", "vol03_fourier_distributions_pde"),
    ("IV", "vol04_complex_analysis"),
    ("V", "vol05_commutative_algebra"),
    ("VI", "vol06_algebraic_geometry"),
    ("VII", "vol07_differential_geometry"),
    ("VIII", "vol08_algebraic_topology"),
)

LOG_CHECKS = {
    "undefined_references": re.compile(r"(?:LaTeX Warning: (?:Reference|Citation).+undefined|There were undefined (?:references|citations))", re.I),
    "duplicate_labels": re.compile(r"(?:Label .+ multiply defined|multiply-defined|multiply defined)", re.I),
    "missing_assets": re.compile(r"(?:LaTeX Warning: File|Package \S+ Error: File).+(?:not found|not exist)", re.I),
    # An undefined TeX control sequence is the practical compiler-level
    # detection boundary for undefined notation/macros.
    "undefined_notation_or_macro": re.compile(r"Undefined control sequence", re.I),
    "fatal_tex_error": re.compile(r"^! .+", re.M),
}
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|pageref|eqref|autoref|cref|Cref)\{([^}]+)\}")
WORKFLOW_PATTERNS = {
    "protected chapter": re.compile(r"\bprotected chapter\b", re.I),
    "legacy problem": re.compile(r"\blegacy problem\b", re.I),
    "legacy-corpus boundary": re.compile(r"\blegacy-corpus boundary\b", re.I),
    "mapped legacy manuscripts": re.compile(r"\bmapped legacy manuscripts?\b", re.I),
    "source audit": re.compile(r"\bsource audit\b", re.I),
    "migration map": re.compile(r"\bmigration map\b", re.I),
    "post-volume audit": re.compile(r"\bpost-VIII/35\b", re.I),
    "reconstruction invariant": re.compile(r"\breconstruction invariant\b", re.I),
    "retained corpus rules": re.compile(r"\bretained corpus rules?\b", re.I),
    "canonical solved layer": re.compile(r"\bcanonical solved (?:problem|layer)\b", re.I),
    "canonical complex-analysis chain": re.compile(r"\bcanonical complex-analysis chain\b", re.I),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def uncomment(text: str) -> str:
    return re.sub(r"(?<!\\)%.*$", "", text, flags=re.M)


def resolve_tex(root: Path, including: Path, raw: str) -> Path | None:
    raw_path = Path(raw.replace("/", "\\"))
    candidates = (root / raw_path, including.parent / raw_path)
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
        if not candidate.suffix:
            with_suffix = candidate.with_suffix(".tex")
            if with_suffix.is_file():
                return with_suffix.resolve()
    return None


def tex_graph(root: Path) -> tuple[list[Path], list[str]]:
    entry = root / "book.tex"
    queue = [entry.resolve()]
    seen: set[Path] = set()
    files: list[Path] = []
    missing: list[str] = []
    while queue:
        current = queue.pop()
        if current in seen:
            continue
        seen.add(current)
        files.append(current)
        text = uncomment(read_text(current))
        for raw in INPUT_RE.findall(text):
            target = resolve_tex(root, current, raw.strip())
            if target is None:
                try:
                    source = current.relative_to(root).as_posix()
                except ValueError:
                    source = current.as_posix()
                missing.append(f"{source} -> {raw}")
            elif target.suffix.lower() == ".tex":
                queue.append(target)
    return sorted(files), sorted(set(missing))


def command_version(command: list[str]) -> str:
    try:
        result = subprocess.run(command, text=True, capture_output=True, check=False, timeout=15)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "unavailable"
    text = (result.stdout or result.stderr).strip().splitlines()
    return text[0] if text else f"exit {result.returncode}"


def git_head(repo: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return "unavailable"


def check_volume(repo: Path, volume: str, dirname: str) -> dict:
    root = repo / "books" / dirname
    graph, missing_inputs = tex_graph(root)
    labels: dict[str, list[str]] = defaultdict(list)
    references: list[tuple[str, str]] = []
    for path in graph:
        text = uncomment(read_text(path))
        rel = path.relative_to(repo).as_posix()
        for label in LABEL_RE.findall(text):
            labels[label].append(rel)
        for group in REF_RE.findall(text):
            for label in group.split(","):
                if label.strip():
                    references.append((rel, label.strip()))
    duplicate_labels = {label: paths for label, paths in labels.items() if len(paths) > 1}
    missing_references = [f"{path} -> {label}" for path, label in references if label not in labels]

    log = root / "book.log"
    log_findings: dict[str, list[str]] = {}
    if not log.is_file():
        log_findings["missing_build_log"] = [log.relative_to(repo).as_posix()]
    else:
        log_text = read_text(log)
        for name, pattern in LOG_CHECKS.items():
            hits = pattern.findall(log_text)
            if hits:
                log_findings[name] = [str(hit) for hit in hits]

    findings = {
        "missing_inputs": missing_inputs,
        "duplicate_labels": sorted(duplicate_labels),
        "missing_references": sorted(set(missing_references)),
        **log_findings,
    }
    findings = {key: value for key, value in findings.items() if value}
    return {
        "volume": volume,
        "directory": dirname,
        "active_tex_files": len(graph),
        "labels": len(labels),
        "references": len(references),
        "status": "PASS" if not findings else "FAIL",
        "findings": findings,
    }


def reader_facing_check(repo: Path) -> tuple[str, list[str]]:
    """Reject operational workflow language, but allow approved scholarly terms.

    C02 deliberately introduces a source/provenance policy in front matter and
    C06 uses "proof dossier" as a pedagogical form.  A single-word blacklist
    would reject both approved uses, so this C08 gate checks the unambiguous
    operational phrases that must not reach rendered book pages.
    """
    findings: list[str] = []
    active_files: set[Path] = set()
    for _, dirname in VOLUMES:
        graph, _ = tex_graph(repo / "books" / dirname)
        active_files.update(graph)
    for path in sorted(active_files):
        if "legacy_problem_audit" in path.as_posix().lower():
            continue
        text = uncomment(read_text(path))
        rel = path.relative_to(repo).as_posix()
        for line_number, line in enumerate(text.splitlines(), 1):
            for name, pattern in WORKFLOW_PATTERNS.items():
                if pattern.search(line):
                    findings.append(f"{rel}:{line_number}: {name}: {line.strip()}")
    return ("PASS" if not findings else "FAIL", findings)


def write_reports(report_dir: Path, report: dict) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "document-qa.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Canonical document QA", "",
        f"**Result:** {report['status']}", "",
        f"- Commit: `{report['commit']}`",
        f"- Generated: {report['generated_at']}",
        f"- Python: {report['environment']['python']}",
        f"- latexmk: {report['environment']['latexmk']}",
        f"- pdflatex: {report['environment']['pdflatex']}", "",
        "| Volume | Status | Active TeX files | Labels | References |",
        "|---|---|---:|---:|---:|",
    ]
    for volume in report["volumes"]:
        lines.append(f"| {volume['volume']} | {volume['status']} | {volume['active_tex_files']} | {volume['labels']} | {volume['references']} |")
    lines += ["", "## Findings", ""]
    for volume in report["volumes"]:
        if not volume["findings"]:
            continue
        lines.append(f"### Volume {volume['volume']}")
        lines.append("")
        for name, values in volume["findings"].items():
            lines.append(f"- {name}: {len(values)}")
    lines += ["", f"- reader-facing workflow vocabulary: {report['reader_facing']['status']}", ""]
    if report["reader_facing"]["findings"]:
        lines += [f"- {item}" for item in report["reader_facing"]["findings"]]
    (report_dir / "document-qa.md").write_text("\n".join(lines), encoding="utf-8")
    (report_dir / "latex-environment.json").write_text(json.dumps(report["environment"], indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--report-dir", type=Path, default=None)
    args = parser.parse_args()
    repo = args.repo.resolve()
    report_dir = (args.report_dir or repo / "build" / "qa").resolve()
    volumes = [check_volume(repo, volume, dirname) for volume, dirname in VOLUMES]
    reader_status, reader_findings = reader_facing_check(repo)
    environment = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "latexmk": command_version(["latexmk", "-v"]),
        "pdflatex": command_version(["pdflatex", "--version"]),
    }
    report = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "commit": git_head(repo),
        "status": "PASS" if all(v["status"] == "PASS" for v in volumes) and reader_status == "PASS" else "FAIL",
        "environment": environment,
        "volumes": volumes,
        "reader_facing": {"status": reader_status, "findings": reader_findings},
    }
    write_reports(report_dir, report)
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
