#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, re, hashlib
from pathlib import Path
from collections import Counter

LINE_RANGE_RE = re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
HEADING_RE = re.compile(
    r"\\(?:section|subsection|subsubsection)\*?\{(?:Problem|Exercise|Example)\b[^}]*\}",
    re.I
)
PLAIN_RE = re.compile(r"(?mi)^\s*(?:Problem|Exercise|Example)\s+[A-Za-z0-9.()_-]+")
SOLUTION_RE = re.compile(
    r"\\begin\{solution\}|\\(?:section|subsection|subsubsection)\*?\{Solution\}|\\textbf\{Solution\.?\}",
    re.I
)
HINT_RE = re.compile(r"\\textit\{Hint:?}|\\paragraph\{Hint\}|\\subsection\*?\{Hint\}", re.I)

KNOWN_RESCANS = [
    {
        "orphan_semantic_unit_id": "SOLSEM-8BD310C9A992",
        "source_file": "Downloads/theory-of-commutative-algebra-12.tex",
        "start_anchor": r"\subsection{Irreducible quadratic factors over \(\mathbb{R}\) and why the quotient is not the same as for real linear factors}",
        "end_anchor": r"\subsubsection{The basic comparison in one variable}",
        "kind": "PROBLEM_LIKE_QUESTION",
        "note": "Recover the natural question preceding the comparison; current candidate is a later oversized block."
    },
    {
        "orphan_semantic_unit_id": "SOLSEM-F0C1695725CA",
        "source_file": "Downloads/theory-of-real-analysis.tex",
        "start_anchor": r"\subsection*{Exercise 9.3}",
        "end_anchor": r"\paragraph{Background.}",
        "kind": "EXERCISE",
        "note": "Recover exact Exercise 9.3 statement."
    },
    {
        "orphan_semantic_unit_id": "SOLSEM-94664AFC5677",
        "source_file": "Downloads/theory-of-commutative-algebra-12.tex",
        "start_anchor": r"\subsection{Why \(k[s,t]/(s-a,t-b)\cong k\) and not \(k\times k\)}",
        "end_anchor": r"\subsubsection{The evaluation map}",
        "kind": "PROBLEM_LIKE_QUESTION",
        "note": "Recover exact local question about one point versus product ring."
    },
    {
        "orphan_semantic_unit_id": "SOLSEM-DE60695D66E5",
        "source_file": "Downloads/theory-of-commutative-algebra-9.tex",
        "start_anchor": r"\subsection{Part (c): vanishing of the induced maps in \(\Ext\)}",
        "end_anchor": r"\textbf{Proof.}",
        "kind": "PROBLEM_PART",
        "note": "Recover Part (c) statement/theorem before proof."
    },
    {
        "orphan_semantic_unit_id": "SOLSEM-7723F82AC385",
        "source_file": "Downloads/theory-of-complex-analysis-gamma.tex",
        "start_anchor": r"\section*{Problem}",
        "end_anchor": r"\section*{Background}",
        "kind": "PROBLEM",
        "note": "Recover exact principal-value integral problem."
    },
]

def read_tsv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r=csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]

def write_tsv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields, delimiter="\t",
                         lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k:row.get(k,"") for k in fields})

def safe_lines(path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:
            return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError:
            pass
    return path.read_text(encoding="utf-8", errors="replace").splitlines()

def parse_range(s):
    m=LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)),int(m.group(2))) if m else None

def strip_tex(s):
    s=re.sub(r"(?<!\\)%.*$"," ",s,flags=re.M)
    s=re.sub(r"\\(?:begin|end)\{[^}]+\}"," ",s)
    s=re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?(?:\{([^{}]*)\})?",lambda m:" "+(m.group(1) or "")+" ",s)
    s=re.sub(r"\s+"," ",s).strip()
    return s

def excerpt(s,n=900):
    s=strip_tex(s)
    return s if len(s)<=n else s[:n-1]+"…"

def sha(s):
    return hashlib.sha256(re.sub(r"\s+"," ",strip_tex(s)).lower().encode()).hexdigest()

def find_anchor(lines, anchor, start=0):
    target=anchor.strip()
    for i in range(start,len(lines)):
        if lines[i].strip()==target:
            return i
    return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    args=ap.parse_args()
    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"
    srcroot=repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"

    _,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")
    audit=[]; flagged=[]
    counters=Counter()
    for r in ledger:
        rr=parse_range(r.get("source_line_range",""))
        if not rr:
            counters["missing_range"]+=1
            continue
        a,b=rr; span=max(0,b-a+1)
        p=srcroot/r.get("source_file","")
        if not p.exists():
            counters["missing_source"]+=1
            continue
        lines=safe_lines(p)
        text="\n".join(lines[max(0,a-1):min(len(lines),b)])
        hcount=len(HEADING_RE.findall(text))+len(PLAIN_RE.findall(text))
        scount=len(SOLUTION_RE.findall(text))
        hintcount=len(HINT_RE.findall(text))
        reasons=[]
        if span>=250: reasons.append("SPAN_GE_250")
        elif span>=120: reasons.append("SPAN_GE_120")
        if hcount>=3: reasons.append("MULTIPLE_PROBLEM_HEADINGS")
        if scount>=2: reasons.append("MULTIPLE_SOLUTION_MARKERS")
        if hcount>=2 and span>=60: reasons.append("LIKELY_MULTI_OBJECT")
        severity=("HIGH" if ("SPAN_GE_250" in reasons or "MULTIPLE_PROBLEM_HEADINGS" in reasons or "MULTIPLE_SOLUTION_MARKERS" in reasons)
                  else ("MEDIUM" if reasons else "OK"))
        row={
            "problem_id":r.get("problem_id",""),
            "source_file":r.get("source_file",""),
            "source_line_range":r.get("source_line_range",""),
            "line_span":span,
            "problem_heading_markers":hcount,
            "solution_markers":scount,
            "hint_markers":hintcount,
            "severity":severity,
            "flags":";".join(reasons),
            "source_heading":r.get("source_heading",""),
            "statement_hash":r.get("statement_hash",""),
        }
        audit.append(row)
        if severity!="OK":
            flagged.append(row)
            counters[severity]+=1

    audit.sort(key=lambda x:(0 if x["severity"]=="HIGH" else 1 if x["severity"]=="MEDIUM" else 2,
                             -int(x["line_span"]),x["problem_id"]))
    flagged.sort(key=lambda x:(0 if x["severity"]=="HIGH" else 1,-int(x["line_span"]),x["problem_id"]))
    fields=["problem_id","source_file","source_line_range","line_span","problem_heading_markers",
            "solution_markers","hint_markers","severity","flags","source_heading","statement_hash"]
    write_tsv(inv/"STRUCTURAL_INTEGRITY_AUDIT.tsv",fields,audit)
    write_tsv(inv/"STRUCTURAL_REPAIR_QUEUE.tsv",fields,flagged)

    # Known five recoveries: preview only, no ledger mutation.
    recovered=[]
    for spec in KNOWN_RESCANS:
        p=srcroot/spec["source_file"]
        if not p.exists():
            recovered.append({**spec,"status":"SOURCE_MISSING","proposed_line_range":"","statement_hash":"","statement_excerpt":""})
            continue
        lines=safe_lines(p)
        si=find_anchor(lines,spec["start_anchor"])
        ei=find_anchor(lines,spec["end_anchor"],(si+1 if si is not None else 0))
        if si is None or ei is None or ei<=si:
            recovered.append({**spec,"status":"ANCHOR_NOT_FOUND","proposed_line_range":"","statement_hash":"","statement_excerpt":""})
            continue
        # include start heading, stop before end anchor
        text="\n".join(lines[si:ei])
        recovered.append({
            **spec,
            "status":"RECOVERED_PREVIEW",
            "proposed_line_range":f"L{si+1}-L{ei}",
            "statement_hash":sha(text),
            "statement_excerpt":excerpt(text),
        })
    rfields=["orphan_semantic_unit_id","source_file","kind","status","proposed_line_range",
             "statement_hash","statement_excerpt","note"]
    write_tsv(inv/"KNOWN_STRUCTURAL_RESCAN_PREVIEW.tsv",rfields,recovered)

    high=sum(1 for r in flagged if r["severity"]=="HIGH")
    med=sum(1 for r in flagged if r["severity"]=="MEDIUM")
    span250=sum(1 for r in flagged if "SPAN_GE_250" in r["flags"])
    multip=sum(1 for r in flagged if "MULTIPLE_PROBLEM_HEADINGS" in r["flags"])
    multis=sum(1 for r in flagged if "MULTIPLE_SOLUTION_MARKERS" in r["flags"])
    recovered_ok=sum(1 for r in recovered if r["status"]=="RECOVERED_PREVIEW")

    sm=["# Imported problem structural-integrity audit","",
        "This is review-only. It does not modify `PROBLEM_LEDGER.tsv`.","",
        "## Global ledger segmentation",
        f"- Ledger rows inspected: **{len(audit)}**",
        f"- Flagged rows: **{len(flagged)}**",
        f"- High severity: **{high}**",
        f"- Medium severity: **{med}**",
        f"- Spans >=250 lines: **{span250}**",
        f"- Rows with >=3 problem/exercise/example headings: **{multip}**",
        f"- Rows with >=2 solution markers: **{multis}**","",
        "## Known Tier-2 structural recoveries",
        f"- Recovery previews found: **{recovered_ok}/5**","",
        "Review `STRUCTURAL_REPAIR_QUEUE.tsv` before any global repair. "
        "Review `KNOWN_STRUCTURAL_RESCAN_PREVIEW.tsv` before merging the five targeted statements."]
    (inv/"STRUCTURAL_INTEGRITY_SUMMARY.md").write_text("\n".join(sm)+"\n",encoding="utf-8")

    md=["# Known structural rescan preview",""]
    for r in recovered:
        md += [f"## {r['orphan_semantic_unit_id']}",
               f"- Source: `{r['source_file']}` {r['proposed_line_range'] or '—'}",
               f"- Kind: **{r['kind']}**",
               f"- Status: **{r['status']}**",
               f"- Excerpt: {r['statement_excerpt'] or '—'}",
               f"- Note: {r['note']}",""]
    (inv/"KNOWN_STRUCTURAL_RESCAN_PREVIEW.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(f"STRUCTURAL INTEGRITY AUDIT COMPLETE: ledger={len(audit)} flagged={len(flagged)} high={high} medium={med} recoveries={recovered_ok}/5")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
