#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, re
from collections import Counter, defaultdict
from pathlib import Path

TARGETS={"RSF-004","RSF-008"}
LINE_RANGE_RE=re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
COMMENT_RE=re.compile(r"(?<!\\)%.*$")

BOUNDARIES=[
    ("SECTION",re.compile(r"^\s*\\(?:section|subsection|subsubsection)\*?\{([^{}]+)\}\s*$",re.I)),
    ("PARAGRAPH",re.compile(r"^\s*\\paragraph\*?\{([^{}]+)\}\s*$",re.I)),
    ("BOLD",re.compile(r"^\s*\\textbf\{([^{}]+)\}\s*$",re.I)),
    ("EMPH",re.compile(r"^\s*\\emph\{([^{}]+)\}\s*$",re.I)),
    ("ITEM",re.compile(r"^\s*\\item(?:\[[^\]]+\])?\s*(.*)$",re.I)),
    ("PLAIN_DIRECTIVE",re.compile(
        r"^\s*((?:Show|Prove|Compute|Find|Determine|Evaluate|Verify|Establish|Deduce|Classify|Construct|Describe|Decide|Explain|Give)\b.*)$",
        re.I)),
]
TERMINALS=[
    re.compile(r"^\s*\\begin\{(?:solution|answer|proofsolution|proof)\*?\}",re.I),
    re.compile(r"^\s*\\(?:section|subsection|subsubsection|paragraph|subparagraph)\*?\{\s*(?:Solution|Answer|Proof)\s*[.:]?\s*\}\s*$",re.I),
    re.compile(r"^\s*\\textbf\{\s*(?:Solution|Answer|Proof)\s*[.:]?\s*\}\s*$",re.I),
    re.compile(r"^\s*\\emph\{\s*(?:Solution|Answer|Proof)\s*[.:]?\s*\}\s*$",re.I),
    re.compile(r"^\s*(?:Solution|Answer|Proof)\s*[.:]\s*$",re.I),
]

KEYWORDS=re.compile(
    r"\b(problem|exercise|question|task|challenge|example|show|prove|compute|find|determine|evaluate|verify|establish|deduce|classify|construct|describe|decide|explain)\b",
    re.I
)

def read_tsv(path):
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        r=csv.DictReader(f,delimiter="\t")
        return list(r.fieldnames or []),[dict(x) for x in r]

def write_tsv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader()
        for row in rows:w.writerow({k:row.get(k,"") for k in fields})

def parse_range(s):
    m=LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)),int(m.group(2))) if m else None

def safe_lines(path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError:pass
    return path.read_text(encoding="utf-8",errors="replace").splitlines()

def strip_comment(s): return COMMENT_RE.sub("",s)

def is_terminal(line):
    x=strip_comment(line)
    return any(p.search(x) for p in TERMINALS)

def compact(text,n=800):
    x=re.sub(r"\s+"," ",text).strip()
    return x if len(x)<=n else x[:n-1]+"…"

def extract_boundary(line):
    x=strip_comment(line)
    for kind,p in BOUNDARIES:
        m=p.search(x)
        if m:
            label=(m.group(1) if m.groups() else x).strip()
            return kind,label
    return None

def candidate_boundary(kind,label):
    # High recall, but still only a suggestion.
    if kind=="PLAIN_DIRECTIVE":
        return True
    if kind=="ITEM":
        return bool(KEYWORDS.search(label))
    return bool(KEYWORDS.search(label))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    args=ap.parse_args()

    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"
    srcroot=repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"

    _,summary=read_tsv(inv/"REVIEW_SPLIT_MERGED_RESEGMENTATION_SUMMARY.tsv")
    _,segments=read_tsv(inv/"REVIEW_SPLIT_MERGED_RESEGMENTATION_CANDIDATES.tsv")
    _,families=read_tsv(inv/"REVIEW_SPLIT_UNIQUE_FAMILIES.tsv")
    _,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")

    rows=[r for r in summary if r["review_family_id"] in TARGETS and r.get("promotion_verdict")=="STILL_REVIEW_REQUIRED"]
    if {r["review_family_id"] for r in rows} != TARGETS:
        raise SystemExit(f"Expected STILL_REVIEW_REQUIRED families {sorted(TARGETS)}, got {[r['review_family_id'] for r in rows]}")

    fam_by={r["review_family_id"]:r for r in families}
    ledger_by={r["problem_id"]:r for r in ledger}
    seg_by=defaultdict(list)
    for s in segments:
        if s["review_family_id"] in TARGETS:
            seg_by[s["review_family_id"]].append(s)

    residual_rows=[]
    boundary_rows=[]
    packet=["# Final two residual structural audit",""]

    for r in sorted(rows,key=lambda x:x["review_family_id"]):
        fid=r["review_family_id"]
        fam=fam_by[fid]
        pid=r["representative_problem_id"]
        parent=ledger_by.get(pid)
        if not parent:
            raise SystemExit(f"{fid}: representative parent {pid} is not active.")
        pr=parse_range(parent["source_line_range"])
        src=r["representative_source_file"]
        lines=safe_lines(srcroot/src)
        segs=sorted(seg_by[fid],key=lambda s:int(s["segment_index"]))

        # Residuals = oversized merged segments plus uncovered parent gaps >=80 lines.
        regions=[]
        for s in segs:
            rr=parse_range(s["proposed_line_range"])
            if int(s["line_span"])>=120:
                regions.append(("OVERSIZED_SEGMENT",s["segment_index"],rr))

        intervals=[parse_range(s["proposed_line_range"]) for s in segs]
        cursor=pr[0]
        gap_index=0
        for rr in intervals:
            if rr[0]>cursor:
                ga,gb=cursor,rr[0]-1
                if gb-ga+1>=80:
                    gap_index+=1
                    regions.append(("UNCOVERED_GAP",f"G{gap_index}",(ga,gb)))
            cursor=max(cursor,rr[1]+1)
        if cursor<=pr[1] and pr[1]-cursor+1>=80:
            gap_index+=1
            regions.append(("UNCOVERED_GAP",f"G{gap_index}",(cursor,pr[1])))

        packet += [
            f"## {fid} — {pid}",
            f"- Source: `{src}`",
            f"- Parent: `{parent['source_line_range']}`",
            f"- Merged segments: **{len(segs)}**",
            f"- Residual regions audited: **{len(regions)}**",
            ""
        ]

        for rtype,rid,rr in regions:
            a,b=rr
            text="\n".join(lines[a-1:b])
            terms=[]
            boundaries=[]
            for lineno in range(a,b+1):
                line=lines[lineno-1]
                if is_terminal(line):
                    terms.append((lineno,line.strip()))
                hit=extract_boundary(line)
                if hit:
                    kind,label=hit
                    is_cand=candidate_boundary(kind,label)
                    boundaries.append((lineno,kind,label,is_cand))
                    if is_cand:
                        boundary_rows.append({
                            "review_family_id":fid,
                            "representative_problem_id":pid,
                            "source_file":src,
                            "region_type":rtype,
                            "region_id":str(rid),
                            "region_line_range":f"L{a}-L{b}",
                            "boundary_line":lineno,
                            "boundary_kind":kind,
                            "boundary_label":label,
                            "candidate_problem_boundary":"YES",
                        })

            # Heuristic residual diagnosis.
            cand_count=sum(1 for x in boundaries if x[3])
            if cand_count>=2:
                diagnosis="MULTIPLE_MISSED_PROBLEM_BOUNDARIES"
            elif cand_count==1 and terms:
                diagnosis="LIKELY_SINGLE_MISSED_BOUNDARY"
            elif cand_count==1:
                diagnosis="ONE_POSSIBLE_BOUNDARY"
            elif terms:
                diagnosis="LONG_SINGLE_PROBLEM_OR_EXPOSITION_WITH_TERMINALS"
            else:
                diagnosis="EXPOSITION_OR_NESTED_STRUCTURE"

            residual_rows.append({
                "review_family_id":fid,
                "representative_problem_id":pid,
                "source_file":src,
                "region_type":rtype,
                "region_id":str(rid),
                "region_line_range":f"L{a}-L{b}",
                "line_span":b-a+1,
                "candidate_problem_boundaries":cand_count,
                "terminal_markers":len(terms),
                "diagnosis":diagnosis,
            })

            packet += [
                f"### {rtype} {rid} — L{a}-L{b} ({b-a+1} lines)",
                f"- Candidate problem boundaries: **{cand_count}**",
                f"- Terminal markers: **{len(terms)}**",
                f"- Diagnosis: **{diagnosis}**",
                f"- Region excerpt: {compact(text)}",
                "",
            ]
            if boundaries:
                packet += ["#### Candidate/internal headings",""]
                for lineno,kind,label,is_cand in boundaries[:40]:
                    flag="CANDIDATE" if is_cand else "context"
                    packet += [f"- L{lineno} `{kind}` [{flag}]: `{compact(label,250)}`"]
                if len(boundaries)>40:
                    packet += [f"- … {len(boundaries)-40} more headings omitted."]
                packet += [""]
            if terms:
                packet += ["#### Terminal markers",""]
                for lineno,line in terms[:20]:
                    packet += [f"- L{lineno}: `{compact(line,220)}`"]
                packet += [""]

        packet += ["---",""]

    write_tsv(inv/"FINAL_TWO_RESIDUAL_REGIONS.tsv",
              ["review_family_id","representative_problem_id","source_file","region_type","region_id",
               "region_line_range","line_span","candidate_problem_boundaries","terminal_markers","diagnosis"],
              residual_rows)
    write_tsv(inv/"FINAL_TWO_RESIDUAL_BOUNDARY_CANDIDATES.tsv",
              ["review_family_id","representative_problem_id","source_file","region_type","region_id",
               "region_line_range","boundary_line","boundary_kind","boundary_label","candidate_problem_boundary"],
              boundary_rows)
    (inv/"FINAL_TWO_RESIDUAL_AUDIT_PACKET.md").write_text("\n".join(packet)+"\n",encoding="utf-8")

    diag=Counter(r["diagnosis"] for r in residual_rows)
    sm=[
        "# Final two residual audit summary","",
        f"- Families audited: **2**",
        f"- Residual regions: **{len(residual_rows)}**",
        f"- Candidate missed problem boundaries: **{len(boundary_rows)}**","",
        "## Residual diagnoses",
    ]
    for k,v in sorted(diag.items()):
        sm += [f"- {k}: **{v}**"]
    sm += ["",
        "This pass is review-only. It isolates only the remaining problematic regions inside RSF-004 and RSF-008."
    ]
    (inv/"FINAL_TWO_RESIDUAL_AUDIT_SUMMARY.md").write_text("\n".join(sm)+"\n",encoding="utf-8")

    print(f"FINAL TWO RESIDUAL AUDIT COMPLETE: regions={len(residual_rows)} candidate_boundaries={len(boundary_rows)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
