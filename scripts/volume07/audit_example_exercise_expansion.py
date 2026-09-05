#!/usr/bin/env python3
import argparse, hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASELINE = ROOT / "reports/series/VOLUME07_EXAMPLE_EXERCISE_BASELINE.json"
VOL = ROOT / "books/vol07_differential_geometry"

def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()

def expansion_path(chapter_path: str) -> Path:
    p = Path(chapter_path)
    return ROOT / p.parent / "pedagogy_expansion.tex"

def expected(stage: int, n: int) -> bool:
    if stage <= 1:
        return False
    if stage == 2:
        return n <= 11
    if stage == 3:
        return n <= 19
    if stage == 4:
        return n <= 30
    return n <= 42

def counts(text: str):
    return {
        "examples": text.count(r"\begin{example}"),
        "exercises": text.count(r"\begin{exercise}"),
        "hints": text.count(r"\begin{hint}"),
        "solutions": text.count(r"\begin{solution}"),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", type=int, required=True, choices=range(1, 8))
    args = ap.parse_args()
    data = json.loads(BASELINE.read_text(encoding="utf-8"))
    failures = []
    rows = []
    for item in data["chapters"]:
        n = int(item["chapter"].split("/")[1])
        source = ROOT / item["path"]
        got = git_blob_sha1(source.read_bytes())
        if got != item["protected_git_blob_sha1"]:
            failures.append(f'{item["chapter"]}: protected chapter drift {got}')
        ep = expansion_path(item["path"])
        should = expected(args.stage, n) if args.stage <= 5 else True
        if should and not ep.exists():
            failures.append(f'{item["chapter"]}: missing pedagogy expansion')
            continue
        if not should and ep.exists():
            failures.append(f'{item["chapter"]}: expansion exists before scheduled stage')
            continue
        c = {"examples":0,"exercises":0,"hints":0,"solutions":0}
        if ep.exists():
            text = ep.read_text(encoding="utf-8")
            c = counts(text)
            if c != {"examples":3,"exercises":16,"hints":16,"solutions":16}:
                failures.append(f'{item["chapter"]}: bad expansion counts {c}')
            labels = re.findall(r"\\label\{([^}]+)\}", text)
            if len(labels) != len(set(labels)):
                failures.append(f'{item["chapter"]}: duplicate labels inside expansion')
            code = f'VII{n:02d}'
            if f'% BEGIN VOL07-EXPANSION {code}' not in text or f'% END VOL07-EXPANSION {code}' not in text:
                failures.append(f'{item["chapter"]}: missing expansion boundary markers')
        rows.append({"chapter": item["chapter"], **c})
    status = "PASS" if not failures else "FAIL"
    print(json.dumps({"status":status,"stage":args.stage,"chapters":rows,"failures":failures}, indent=2))
    return 0 if status == "PASS" else 9

if __name__ == "__main__":
    raise SystemExit(main())
