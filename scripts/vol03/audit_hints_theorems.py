#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

EXPECTED = {"chapters": 28, "problems": 336, "exercises": 672, "hints": 672, "solutions": 1008}
CLASSIFICATIONS = {"proved", "proved earlier", "standard external theorem", "proof sketch", "preview only"}
REQUIRED = {
    4: ["monotone convergence", "fatou", "dominated convergence"],
    5: ["tonelli", "fubini"],
    6: ["completeness"],
    7: ["holder", "minkowski"],
    8: ["egorov", "vitali"],
    9: ["dirichlet", "fejer"],
    10: ["young", "approximate identit"],
    11: ["inversion"],
    13: ["plancherel", "parseval"],
    14: ["schwartz"],
    16: ["distributional derivative"],
    17: ["support", "singular"],
    18: ["tempered distribution"],
    19: ["fourier transform", "distribution"],
    20: ["weak derivative"],
    21: ["sobolev", "poincare"],
    22: ["density", "mollif"],
    23: ["lax", "milgram"],
    24: ["fundamental solution"],
    25: ["green"],
    26: ["sturm", "liouville"],
    27: ["maximum principle"],
    28: ["spectral", "transform"],
}
TRIPLE = re.compile(
    r"\\begin\{exercise\}(?:\[([^\]\n]*)\])?(.*?)\\end\{exercise\}\s*"
    r"\\begin\{hint\}(.*?)\\end\{hint\}\s*"
    r"\\begin\{solution\}(.*?)\\end\{solution\}", re.S)
THEOREM = re.compile(r"\\begin\{theorem\}(?:\[([^\]\n]*)\])?(.*?)\\end\{theorem\}", re.S)
LABEL = re.compile(r"\\label\{([^}]+)\}")
REF = re.compile(r"\\(?:ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}")
STOP = {"the","and","for","with","that","this","from","into","use","apply","show","prove","give","state","find","chapter","exercise","solution","then","where","when"}

def clean_comments(s: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", s)

def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\\([A-Za-z]+)", r" \1 ", s)
    s = re.sub(r"[^A-Za-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip().casefold()

def words(s: str) -> set[str]:
    return {w for w in fold(s).split() if len(w) >= 3 and w not in STOP and not w.isdigit()}

def similarity(a: set[str], b: set[str]) -> float:
    return 0.0 if not a or not b else len(a & b) / len(a | b)

def classify(block: str) -> str | None:
    f = fold(block)
    if "proved earlier" in f:
        return "proved earlier"
    if "standard theorem" in f or ("standard" in f and "deferred" in f) or ("full proof" in f and "deferred" in f):
        return "standard external theorem"
    if "proof sketch" in f:
        return "proof sketch"
    if r"\begin{proof}" in block:
        return "proved"
    if "preview" in f:
        return "preview only"
    return None

def write_tsv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", required=True); args = ap.parse_args()
    repo = Path(args.repo).resolve(); volume = repo / "books/vol03_fourier_distributions_pde"; reports = repo / "reports/vol03"
    reports.mkdir(parents=True, exist_ok=True)
    chapters = sorted((volume / "chapters").glob("ch*/chapter.tex"))
    blocking, warnings, hint_rows, theorem_rows, all_hint_records = [], [], [], [], []
    totals = Counter(); chapter_texts = {}
    if len(chapters) != 28: blocking.append(f"expected 28 chapter files, found {len(chapters)}")
    for n, path in enumerate(chapters, 1):
        text = clean_comments(path.read_text(encoding="utf-8-sig", errors="replace")); chapter_texts[n] = text
        counts = {env: len(re.findall(r"\\begin\{" + env + r"\}", text)) for env in ("problem","exercise","hint","solution")}
        totals.update(counts)
        actual = tuple(counts[x] for x in ("problem","exercise","hint","solution"))
        if actual != (12,24,24,36): blocking.append(f"III/{n:02d}: expected 12/24/24/36, found {actual}")
        triples = list(TRIPLE.finditer(text))
        if len(triples) != 24: blocking.append(f"III/{n:02d}: expected 24 exercise/hint/solution triples, found {len(triples)}")
        for k,m in enumerate(triples,1):
            title=(m.group(1) or "").strip(); ex=m.group(2).strip(); hint=m.group(3).strip(); sol=m.group(4).strip(); lm=LABEL.search(ex)
            label = lm.group(1) if lm else f"III/{n:02d}-E{k:02d}-NO-LABEL"
            if not lm: blocking.append(f"III/{n:02d} exercise {k}: missing label")
            all_hint_records.append({"chapter":f"III/{n:02d}","ordinal":k,"label":label,"title":title,"hint":hint,"exwords":words(title+" "+ex),"hintwords":words(hint),"solwords":words(sol),"line":text[:m.start()].count("\n")+1})
        for k,m in enumerate(THEOREM.finditer(text),1):
            title=(m.group(1) or "").strip(); body=m.group(2).strip(); lm=LABEL.search(body); label=lm.group(1) if lm else f"III/{n:02d}-T{k:02d}-NO-LABEL"
            coverage=classify(body)
            if coverage is None:
                blocking.append(f"{label}: theorem has no honest proof-scope classification"); coverage="preview only"
            theorem_rows.append({"chapter":f"III/{n:02d}","ordinal":k,"label":label,"theorem":title,"classification":coverage,"proof_environment":"yes" if r"\begin{proof}" in body else "no","source_line":text[:m.start()].count("\n")+1,"body_sha256":hashlib.sha256(body.encode()).hexdigest()})
    normalized = Counter(fold(r["hint"]) for r in all_hint_records)
    by_chapter = {}
    for r in all_hint_records: by_chapter.setdefault(r["chapter"], []).append(r)
    for chapter, rows in by_chapter.items():
        for i, rec in enumerate(rows):
            h=rec["hintwords"]; own=similarity(h, rec["solwords"]); neighbor=0.0
            if i: neighbor=max(neighbor, similarity(h, rows[i-1]["solwords"]))
            if i+1<len(rows): neighbor=max(neighbor, similarity(h, rows[i+1]["solwords"]))
            status="PASS"; notes=[]; compact=fold(rec["hint"])
            if not rec["hint"].strip(): status="FAIL"; notes.append("empty hint")
            if compact in {"use definition","use theorem","apply theorem","apply result","compute directly"}: status="FAIL"; notes.append("generic-only hint")
            if neighbor>=0.55 and neighbor>own+0.40 and own<0.20: status="FAIL"; notes.append("possible neighboring-solution contamination")
            dup=normalized[compact]
            if dup>=4: warnings.append(f"{rec['label']}: normalized hint appears {dup} times"); notes.append(f"duplicate-hint diagnostic={dup}")
            if status=="FAIL": blocking.append(f"{rec['label']}: " + "; ".join(notes))
            hint_rows.append({"chapter":rec["chapter"],"ordinal":rec["ordinal"],"label":rec["label"],"title":rec["title"],"source_line":rec["line"],"hint_sha256":hashlib.sha256(rec["hint"].encode()).hexdigest(),"hint_words":len(compact.split()),"own_solution_similarity":f"{own:.4f}","nearest_neighbor_solution_similarity":f"{neighbor:.4f}","duplicate_hint_count":dup,"status":status,"hint":" ".join(rec["hint"].split()),"notes":" | ".join(notes) if notes else "-"})
    family_rows=[]
    for n, needles in REQUIRED.items():
        text=fold(chapter_texts.get(n,""))
        for needle in needles:
            ok=needle in text; family_rows.append({"chapter":f"III/{n:02d}","family":needle,"status":"PASS" if ok else "FAIL"})
            if not ok: blocking.append(f"III/{n:02d}: missing required theorem family {needle}")
    labels=[]; refs=[]; malformed=[]; todos=[]
    for path in [volume/"book.tex", *chapters]:
        text=clean_comments(path.read_text(encoding="utf-8-sig",errors="replace")); labels.extend(LABEL.findall(text))
        for group in REF.findall(text): refs.extend(x.strip() for x in group.split(",") if x.strip())
        for line_no,line in enumerate(text.splitlines(),1):
            if re.search(r"\b(?:TODO|FIXME|TBD)\b",line,re.I): todos.append(f"{path.relative_to(repo)}:{line_no}")
            if re.search(r"\\begin\{(?:exercise|problem|theorem|example)\}\[",line) and "]" not in line: malformed.append(f"{path.relative_to(repo)}:{line_no}")
    duplicate_labels=sorted(k for k,v in Counter(labels).items() if v>1); missing_refs=sorted(set(refs)-set(labels))
    blocking += [f"duplicate label: {x}" for x in duplicate_labels] + [f"missing reference: {x}" for x in missing_refs] + [f"malformed optional title: {x}" for x in malformed] + [f"unresolved marker: {x}" for x in todos]
    if len(hint_rows)!=672: blocking.append(f"expected 672 hint rows, found {len(hint_rows)}")
    for key,expected in (("problem",336),("exercise",672),("hint",672),("solution",1008)):
        if totals[key]!=expected: blocking.append(f"expected {expected} {key}s, found {totals[key]}")
    write_tsv(reports/"VOL03_HINT_RECONCILIATION.tsv", hint_rows, ["chapter","ordinal","label","title","source_line","hint_sha256","hint_words","own_solution_similarity","nearest_neighbor_solution_similarity","duplicate_hint_count","status","hint","notes"])
    write_tsv(reports/"VOL03_THEOREM_COVERAGE.tsv", theorem_rows, ["chapter","ordinal","label","theorem","classification","proof_environment","source_line","body_sha256"])
    obj={"schema":1,"status":"PASS" if not blocking else "FAIL","scope":"Volume III III/01-III/28 hint reconciliation and theorem coverage","chapters_checked":len(chapters),"current_source_counts":{"problems":totals["problem"],"exercises":totals["exercise"],"hints":totals["hint"],"solutions":totals["solution"]},"hints_reviewed":len(hint_rows),"hint_status_counts":dict(Counter(r["status"] for r in hint_rows)),"theorems_classified":len(theorem_rows),"theorem_classification_counts":dict(Counter(r["classification"] for r in theorem_rows)),"required_family_checks":family_rows,"duplicate_labels":duplicate_labels,"missing_refs":missing_refs,"malformed_optional_titles":malformed,"todo_markers":todos,"warnings":warnings,"blocking":blocking}
    (reports/"VOL03_HINT_THEOREM_AUDIT.json").write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume III — hint and theorem audit","",f"**Status:** {obj['status']}","",f"- Chapters checked: **{len(chapters)}/28**",f"- Hints reconciled: **{len(hint_rows)}/672**",f"- Theorems classified: **{len(theorem_rows)}**",f"- Duplicate labels: **{len(duplicate_labels)}**",f"- Missing references: **{len(missing_refs)}**","","The historical 224-hint v1.0 inventory is not used as the current-source baseline.","","## Blocking findings","",*( ["None."] if not blocking else [f"- {x}" for x in blocking])]
    (reports/"VOL03_HINT_THEOREM_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    recon=["# Volume III — hint/theorem reconciliation","","The professional-review source contains **672 exercise/hint pairs** (28 chapters × 24 exercises).","","`VOL03_HINT_RECONCILIATION.tsv` gives one stable row for every hint.","","`VOL03_THEOREM_COVERAGE.tsv` classifies every theorem environment using the allowed proof-scope vocabulary.","",f"Final audit status: **{obj['status']}**."]
    (reports/"VOL03_HINT_THEOREM_RECONCILIATION.md").write_text("\n".join(recon)+"\n",encoding="utf-8")
    print(json.dumps(obj,indent=2,ensure_ascii=False)); return 0 if obj["status"]=="PASS" else 5

if __name__ == "__main__": raise SystemExit(main())
