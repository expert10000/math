#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

LINE_RANGE_RE = re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
COMMENT_RE = re.compile(r"(?<!\\)%.*$")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_'-]{2,}")
MATH_CMD_RE = re.compile(r"\\[A-Za-z]+")
MATH_ATOM_RE = re.compile(r"(?<![A-Za-z])(?:[A-Za-z](?:_[A-Za-z0-9{}]+|\^[A-Za-z0-9{}]+)?|[0-9]+(?:\.[0-9]+)?)(?![A-Za-z])")
EXERCISE_NUM_RE = re.compile(r"(?:Exercise|Problem|Question|Task|Example)\s*([0-9]+(?:\.[0-9]+)*(?:\s*\([a-z]\))?)", re.I)

STOP = {
    "the","and","for","that","with","from","this","then","show","prove","let","suppose",
    "such","all","there","have","has","are","was","were","into","over","under","where",
    "which","when","each","some","any","its","can","may","will","one","two","three",
    "also","thus","hence","therefore","using","given","define","defined","consider",
    "solution","proof","answer","exercise","problem","example","question","task",
    "section","subsection","textbf","textit","begin","end","item","left","right",
}

SUBJECT_TOKENS = {
    "analysis","real","complex","geometry","differential","algebraic","topology",
    "commutative","algebra","linear","number","numbers","functions","series",
    "measure","probability","functional","calculus",
}

def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]

def write_tsv(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore"
        )
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})

def safe_lines(path: Path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:
            return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError:
            pass
    return path.read_text(encoding="utf-8", errors="replace").splitlines()

def parse_range(s):
    m = LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)), int(m.group(2))) if m else None

def source_text(srcroot: Path, rel: str, line_range: str):
    rr = parse_range(line_range)
    p = srcroot / rel
    if not rr or not p.exists():
        return ""
    lines = safe_lines(p)
    a,b = rr
    return "\n".join(lines[max(0,a-1):min(len(lines),b)])

def clean_tex(text: str):
    text = "\n".join(COMMENT_RE.sub("",x) for x in text.splitlines())
    text = re.sub(r"\\begin\{[^}]+\}|\\end\{[^}]+\}", " ", text)
    text = re.sub(r"\\(?:section|subsection|subsubsection|paragraph)\*?\{([^{}]*)\}", r" \1 ", text)
    text = re.sub(r"\\(?:textbf|textit|emph)\{([^{}]*)\}", r" \1 ", text)
    text = text.replace("{"," ").replace("}"," ")
    text = re.sub(r"\s+"," ",text).strip()
    return text

def lexical_tokens(text: str):
    toks=[]
    for w in WORD_RE.findall(clean_tex(text).lower()):
        if w not in STOP and len(w) >= 3:
            toks.append(w)
    return toks

def math_tokens(text: str):
    out=[]
    for cmd in MATH_CMD_RE.findall(text):
        c=cmd[1:].lower()
        if c not in {"begin","end","text","textbf","textit","emph","left","right","big","bigg"}:
            out.append("\\"+c)
    for atom in MATH_ATOM_RE.findall(text):
        a=re.sub(r"\s+","",atom.lower())
        if a not in {"a","an","i"}:
            out.append(a)
    return out

def filename_family(path: str):
    stem = Path(path).stem.lower()
    stem = re.sub(r"\s*\(\d+\)\s*$","",stem)
    stem = re.sub(r"\s*-\s*copy$","",stem)
    bits = re.split(r"[^a-z0-9]+",stem)
    ignore={"theory","of","merged","exercises","full","corrected","professional","copy","v1","v2","v3","v4"}
    return {b for b in bits if b and b not in ignore}

def subject_family(path: str):
    fam=filename_family(path)
    return fam & SUBJECT_TOKENS

def normalize_number(s: str):
    s=(s or "").strip().lower()
    s=re.sub(r"\s+","",s)
    s=s.strip(".:")
    return s

def inferred_number(row):
    n=normalize_number(row.get("source_problem_number",""))
    if n:
        return n
    for field in ("source_heading","statement_excerpt"):
        m=EXERCISE_NUM_RE.search(row.get(field,"") or "")
        if m:
            return normalize_number(m.group(1))
    return ""

def build_idf(candidate_units):
    df=Counter()
    N=len(candidate_units)
    for c in candidate_units:
        toks=set(c["_lex"])
        for t in toks:
            df[t]+=1
    return {t: math.log((N+1)/(n+1))+1.0 for t,n in df.items()}

def tfidf_cosine(a_tokens,b_tokens,idf):
    ca=Counter(a_tokens); cb=Counter(b_tokens)
    common=set(ca)&set(cb)
    if not common:
        return 0.0
    dot=sum(ca[t]*idf.get(t,1.0)*cb[t]*idf.get(t,1.0) for t in common)
    na=math.sqrt(sum((v*idf.get(t,1.0))**2 for t,v in ca.items()))
    nb=math.sqrt(sum((v*idf.get(t,1.0))**2 for t,v in cb.items()))
    return dot/(na*nb) if na and nb else 0.0

def jaccard(a,b):
    a=set(a); b=set(b)
    if not a or not b:
        return 0.0
    return len(a&b)/len(a|b)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    args=ap.parse_args()

    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"
    srcroot=repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"

    required=[
        inv/"PROBLEM_LEDGER.tsv",
        inv/"PROBLEM_SOLUTION_LINKS.tsv",
        inv/"STRUCTURAL_REBUILD_CANDIDATES_V3.tsv",
        inv/"POST_SPLIT_LINK_REVIEW.tsv",
    ]
    missing=[str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit("Missing required files:\n  " + "\n  ".join(missing))

    _,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")
    _,links=read_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv")
    _,candidates=read_tsv(inv/"STRUCTURAL_REBUILD_CANDIDATES_V3.tsv")
    _,review_rows=read_tsv(inv/"POST_SPLIT_LINK_REVIEW.tsv")

    # Require the safe split to be applied, not merely dry-run.
    active_ids={r["problem_id"] for r in ledger}
    safe_plan_path=inv/"SAFE_STRUCTURAL_SPLIT_PLAN.tsv"
    if safe_plan_path.exists():
        _,safe_plan=read_tsv(safe_plan_path)
        still_active=[r["current_problem_id"] for r in safe_plan if r["current_problem_id"] in active_ids]
        if still_active:
            raise SystemExit(
                f"Safe structural split appears not to be applied: {len(still_active)} superseded parents are still active."
            )

    link_by_id={r["solution_id"]:r for r in links}

    # Target every post-split review row, collapsed by semantic solution unit.
    target_members=defaultdict(list)
    for rr in review_rows:
        sid=rr.get("solution_id","")
        link=link_by_id.get(sid,{})
        unit=(link.get("solution_semantic_unit_id") or link.get("solution_hash") or sid)
        row=dict(rr)
        row["_unit"]=unit
        row["_link"]=link
        target_members[unit].append(row)

    # Build a global statement candidate pool from v3 explicit segments plus current ledger rows.
    pool_by_hash=defaultdict(list)

    for c in candidates:
        h=c.get("statement_hash","")
        if not h:
            continue
        row={
            "statement_hash":h,
            "representative_problem_id":"",
            "source_file":c.get("source_file",""),
            "source_line_range":c.get("proposed_line_range",""),
            "source_problem_number":c.get("source_problem_number",""),
            "source_heading":c.get("source_heading",""),
            "statement_excerpt":c.get("statement_excerpt",""),
            "candidate_origin":"STRUCTURAL_V3",
        }
        pool_by_hash[h].append(row)

    for r in ledger:
        h=r.get("statement_hash","")
        if not h:
            continue
        row={
            "statement_hash":h,
            "representative_problem_id":r.get("problem_id",""),
            "source_file":r.get("source_file",""),
            "source_line_range":r.get("source_line_range",""),
            "source_problem_number":r.get("source_problem_number",""),
            "source_heading":r.get("source_heading",""),
            "statement_excerpt":"",
            "candidate_origin":"ACTIVE_LEDGER",
        }
        pool_by_hash[h].append(row)

    candidate_units=[]
    for h,members in pool_by_hash.items():
        # Prefer an active-ledger representative, else first explicit segment.
        rep=next((m for m in members if m["candidate_origin"]=="ACTIVE_LEDGER"),members[0])
        full_text=source_text(srcroot,rep["source_file"],rep["source_line_range"])
        statement_text=full_text if full_text else rep.get("statement_excerpt","")
        unit={
            "statement_hash":h,
            "representative_problem_id":rep.get("representative_problem_id",""),
            "representative_source_file":rep["source_file"],
            "representative_line_range":rep["source_line_range"],
            "source_problem_number":inferred_number(rep),
            "source_heading":rep.get("source_heading",""),
            "statement_text":statement_text,
            "statement_excerpt":clean_tex(statement_text)[:900],
            "equivalent_source_files":";".join(sorted({m["source_file"] for m in members})),
            "equivalent_problem_ids":";".join(sorted({m["representative_problem_id"] for m in members if m.get("representative_problem_id")})),
            "member_count":len(members),
        }
        unit["_lex"]=lexical_tokens(statement_text)
        unit["_math"]=math_tokens(statement_text)
        unit["_fam"]=filename_family(rep["source_file"])
        unit["_subject"]=subject_family(rep["source_file"])
        candidate_units.append(unit)

    idf=build_idf(candidate_units)

    rankings=[]
    decisions=[]
    packet=["# Companion statement recovery review packet",""]

    for unit,members in sorted(target_members.items()):
        # Representative solution row.
        rep=members[0]
        link=rep["_link"]
        solution_text=source_text(
            srcroot,
            link.get("solution_source_file",rep.get("solution_source_file","")),
            link.get("solution_line_range",rep.get("solution_line_range","")),
        )
        slex=lexical_tokens(solution_text)
        smath=math_tokens(solution_text)
        sfam=filename_family(link.get("solution_source_file",rep.get("solution_source_file","")))
        ssub=subject_family(link.get("solution_source_file",rep.get("solution_source_file","")))
        nums={normalize_number(m.get("source_problem_number","")) for m in members if normalize_number(m.get("source_problem_number",""))}

        scored=[]
        for c in candidate_units:
            cnum=normalize_number(c.get("source_problem_number",""))
            num_exact=1.0 if cnum and cnum in nums else 0.0

            lex=tfidf_cosine(slex,c["_lex"],idf)
            mathj=jaccard(smath,c["_math"])

            famj=jaccard(sfam,c["_fam"])
            subj=1.0 if ssub and c["_subject"] and (ssub & c["_subject"]) else 0.0

            # Number is useful but deliberately capped below content evidence.
            score=(
                0.46*lex +
                0.24*mathj +
                0.12*num_exact +
                0.10*famj +
                0.08*subj
            )

            # Strong penalty for clearly different high-level subjects.
            if ssub and c["_subject"] and not (ssub & c["_subject"]):
                score *= 0.72

            scored.append((score,lex,mathj,num_exact,famj,subj,c))

        scored.sort(key=lambda x:x[0],reverse=True)
        top=scored[:8]
        top_score=top[0][0] if top else 0.0
        second=top[1][0] if len(top)>1 else 0.0
        margin=top_score-second

        # Editorial triage, not auto-linking.
        if top and top_score>=0.48 and margin>=0.10 and (top[0][1]>=0.20 or top[0][2]>=0.10):
            rec="STRONG_REVIEW"
        elif top and top_score>=0.32 and margin>=0.05:
            rec="CONTENT_MATCH_REVIEW"
        elif top and top[0][3] == 1.0 and top_score < 0.32:
            rec="NUMBER_ONLY_WEAK"
        else:
            rec="NO_GOOD_MATCH"

        decisions.append({
            "solution_semantic_unit_id":unit,
            "member_solution_count":len(members),
            "member_solution_ids":";".join(sorted(m.get("solution_id","") for m in members)),
            "source_problem_numbers":";".join(sorted(nums)),
            "top_statement_hash":top[0][6]["statement_hash"] if top else "",
            "top_representative_problem_id":top[0][6]["representative_problem_id"] if top else "",
            "top_source_file":top[0][6]["representative_source_file"] if top else "",
            "top_source_line_range":top[0][6]["representative_line_range"] if top else "",
            "top_score":f"{top_score:.4f}",
            "second_score":f"{second:.4f}",
            "margin":f"{margin:.4f}",
            "recommendation":rec,
            "editorial_decision":"PENDING",
        })

        packet += [
            f"## {unit}",
            f"- Solution members: **{len(members)}**",
            f"- Solution IDs: `{';'.join(sorted(m.get('solution_id','') for m in members))}`",
            f"- Source number(s): `{';'.join(sorted(nums)) or '—'}`",
            f"- Solution source: `{link.get('solution_source_file',rep.get('solution_source_file',''))}` {link.get('solution_line_range',rep.get('solution_line_range',''))}",
            f"- Solution excerpt: {clean_tex(solution_text)[:1000]}",
            f"- Recommendation: **{rec}**",
            "",
        ]

        for rank,(score,lex,mathj,num_exact,famj,subj,c) in enumerate(top[:5],1):
            rankings.append({
                "solution_semantic_unit_id":unit,
                "rank":rank,
                "statement_hash":c["statement_hash"],
                "representative_problem_id":c["representative_problem_id"],
                "source_file":c["representative_source_file"],
                "source_line_range":c["representative_line_range"],
                "source_problem_number":c["source_problem_number"],
                "score":f"{score:.4f}",
                "lexical_tfidf":f"{lex:.4f}",
                "math_jaccard":f"{mathj:.4f}",
                "number_exact":f"{num_exact:.1f}",
                "family_jaccard":f"{famj:.4f}",
                "subject_match":f"{subj:.1f}",
                "equivalent_source_files":c["equivalent_source_files"],
                "equivalent_problem_ids":c["equivalent_problem_ids"],
                "statement_excerpt":c["statement_excerpt"],
            })

            packet += [
                f"### Candidate {rank} — score {score:.4f}",
                f"- Representative problem: `{c['representative_problem_id'] or '—'}`",
                f"- Source: `{c['representative_source_file']}` {c['representative_line_range']}",
                f"- Source number: `{c['source_problem_number'] or '—'}`",
                f"- Evidence: lexical={lex:.4f}, math={mathj:.4f}, number={num_exact:.1f}, family={famj:.4f}, subject={subj:.1f}",
                f"- Equivalent problem IDs: `{c['equivalent_problem_ids'] or '—'}`",
                f"- Statement excerpt: {c['statement_excerpt'][:1000]}",
                "",
            ]

        packet += [
            f"**Top margin:** {margin:.4f}",
            "**Editorial decision:** `PENDING`",
            "",
            "---",
            "",
        ]

    ranking_fields=[
        "solution_semantic_unit_id","rank","statement_hash","representative_problem_id",
        "source_file","source_line_range","source_problem_number","score","lexical_tfidf",
        "math_jaccard","number_exact","family_jaccard","subject_match",
        "equivalent_source_files","equivalent_problem_ids","statement_excerpt",
    ]
    decision_fields=[
        "solution_semantic_unit_id","member_solution_count","member_solution_ids",
        "source_problem_numbers","top_statement_hash","top_representative_problem_id",
        "top_source_file","top_source_line_range","top_score","second_score","margin",
        "recommendation","editorial_decision",
    ]

    write_tsv(inv/"COMPANION_STATEMENT_CANDIDATE_RANKINGS.tsv",ranking_fields,rankings)
    write_tsv(inv/"COMPANION_STATEMENT_RECOVERY_DECISIONS.tsv",decision_fields,decisions)
    (inv/"COMPANION_STATEMENT_RECOVERY_PACKET.md").write_text("\n".join(packet)+"\n",encoding="utf-8")

    rec_counts=Counter(r["recommendation"] for r in decisions)
    summary=[
        "# Companion statement recovery audit",
        "",
        "This pass is review-only. It does not change any problem/solution links.",
        "",
        f"- Post-split review source rows: **{len(review_rows)}**",
        f"- Collapsed semantic solution units: **{len(target_members)}**",
        f"- Unique statement candidates searched: **{len(candidate_units)}**",
        f"- Ranked candidate rows emitted: **{len(rankings)}**",
        "",
        "## Recommendation counts",
        f"- STRONG_REVIEW: **{rec_counts['STRONG_REVIEW']}**",
        f"- CONTENT_MATCH_REVIEW: **{rec_counts['CONTENT_MATCH_REVIEW']}**",
        f"- NUMBER_ONLY_WEAK: **{rec_counts['NUMBER_ONLY_WEAK']}**",
        f"- NO_GOOD_MATCH: **{rec_counts['NO_GOOD_MATCH']}**",
        "",
        "Number matching is deliberately only 12% of the score; mathematical-content evidence dominates.",
        "Review `COMPANION_STATEMENT_RECOVERY_PACKET.md` before any link is applied.",
    ]
    (inv/"COMPANION_STATEMENT_RECOVERY_SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

    print(
        "COMPANION STATEMENT RECOVERY AUDIT COMPLETE: "
        f"review_rows={len(review_rows)} semantic_units={len(target_members)} "
        f"candidates={len(candidate_units)} strong={rec_counts['STRONG_REVIEW']} "
        f"content_review={rec_counts['CONTENT_MATCH_REVIEW']} "
        f"number_only={rec_counts['NUMBER_ONLY_WEAK']} no_match={rec_counts['NO_GOOD_MATCH']}"
    )
    return 0

if __name__=="__main__":
    raise SystemExit(main())
