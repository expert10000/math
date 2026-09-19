#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,re,shutil
from collections import defaultdict
from pathlib import Path

LINE_RANGE_RE=re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
COMMENT_RE=re.compile(r"(?<!\\)%.*$")
TERMINAL_STATUSES={"RESOLVED_NOT_A_PROBLEM","MISSING_COMPANION_STATEMENT"}

EXISTING_LINKS={
    "SOLSEM-F0C1695725CA":"IMP-DL-20E278E436-R002160-7EC1330C",
    "SOLSEM-2ECC5725FBED":"IMP-DL-D4351A3BBD-P032",
    "SOLSEM-A3E4B3F720CA":"IMP-DL-15679DEE8D-P004",
}

RECOVERY_SPECS={
    "SOLSEM-7723F82AC385":{
        "source_file":"Downloads/theory-of-complex-analysis-gamma.tex",
        "start_contains":r"\section*{Problem}",
        "must_follow":"operatorname{PV}",
        "end_contains":r"\section*{Background}",
        "problem_type":"PROBLEM","source_problem_number":"",
        "label":"principal-value cosine integral",
    },
    "SOLSEM-94664AFC5677":{
        "source_file":"Downloads/theory-of-commutative-algebra-12.tex",
        "start_contains":r"\subsection{Why \(k[s,t]/(s-a,t-b)\cong k\) and not \(k\times k\)}",
        "end_contains":"The reason is that the ideal",
        "problem_type":"PROBLEM","source_problem_number":"",
        "label":"why point quotient is k rather than k x k",
    },
    "SOLSEM-DE60695D66E5":{
        "source_file":"Downloads/theory-of-commutative-algebra-9.tex",
        "start_contains":r"\subsection{Part (c): vanishing of the induced maps in \(\Ext\)}",
        "end_contains":r"\textbf{Proof.}",
        "problem_type":"PROBLEM","source_problem_number":"14(c)",
        "label":"minimal presentation Ext maps vanish",
    },
    "SOLSEM-8BD310C9A992":{
        "source_file":"Downloads/theory-of-commutative-algebra-12.tex",
        "start_contains":r"\subsection{Irreducible quadratic factors over \(\mathbb{R}\) and why the quotient is not the same as for real linear factors}",
        "end_contains":r"\subsubsection{The basic comparison in one variable}",
        "problem_type":"PROBLEM","source_problem_number":"",
        "label":"real linear versus irreducible quadratic quotient comparison",
    },
    "SOLSEM-75628998F7B0":{
        "source_file":"Downloads/theory-of-analysis-FD2.tex",
        "start_contains":r"\subsection*{Exercise 4.5 (Inhomogeneous Helmholtz Equation in $\mathbb{R}^3$)}",
        "end_contains":r"\subsection*{Solution to Exercise 4.5}",
        "problem_type":"EXERCISE","source_problem_number":"4.5",
        "label":"inhomogeneous Helmholtz equation",
    },
    "SOLSEM-AD6A0593A50F":{
        "source_file":"Downloads/theory-of-geometry-2.tex",
        "start_contains":r"\subsection*{Problem}",
        "must_follow":"torsion",
        "end_contains":r"\subsection*{Theory}",
        "problem_type":"PROBLEM","source_problem_number":"1",
        "label":"torsion formula and nonuniqueness when curvature vanishes",
    },
}

RESET_VALUES={
    "duplicate_group":"",
    "canonical_match_type":"UNREVIEWED","canonical_problem_id":"","canonical_volume":"","canonical_chapter":"",
    "target_volume":"UNCLASSIFIED","target_chapter":"UNCLASSIFIED","target_section":"UNCLASSIFIED",
    "mapping_confidence":"UNCLASSIFIED","migration_status":"UNREVIEWED","migration_commit":"",
    "review_status":"NEEDS_EDITORIAL_REVIEW","has_hint":"NO","has_solution":"NO","solution_id":"",
    "local_solution_ids":"","propagated_solution_ids":"","solution_link_status":"NO_SOLUTION_LINKED",
}

def read_tsv(path):
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        r=csv.DictReader(f,delimiter="\t")
        return list(r.fieldnames or []),[dict(x) for x in r]

def write_tsv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader()
        for r in rows:w.writerow({k:r.get(k,"") for k in fields})

def extend(fields,extras):
    out=list(fields)
    for x in extras:
        if x not in out:out.append(x)
    return out

def parse_range(s):
    m=LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)),int(m.group(2))) if m else None

def split_ids(s):return [x for x in (s or "").split(";") if x]

def safe_lines(path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError:pass
    return path.read_text(encoding="utf-8",errors="replace").splitlines()

def strip_comment(s):return COMMENT_RE.sub("",s)

def normalize_statement(text):
    text=re.sub(r"\\begin\{(?:solution|answer|proofsolution|hint|hints)\}.*?\\end\{(?:solution|answer|proofsolution|hint|hints)\}"," ",text,flags=re.I|re.S)
    text=re.split(r"(?im)^\s*(?:\\noindent\s*)?(?:\\textbf\{)?(?:Solution|Answer|Hint)\}?\s*[:.]",text,maxsplit=1)[0]
    text="\n".join(strip_comment(x) for x in text.splitlines())
    text=re.sub(r"\\label\{[^}]+\}"," ",text)
    text=re.sub(r"\\begin\{(?:problem|exercise|example|question|task|challenge)\*?\}(?:\[[^\]]*\])?"," ",text,flags=re.I)
    text=re.sub(r"\\end\{(?:problem|exercise|example|question|task|challenge)\*?\}"," ",text,flags=re.I)
    text=re.sub(r"\\(?:section|subsection|subsubsection|paragraph)\*?\{\s*(?:Problem|Exercise|Example|Question|Task|Challenge)[^}]*\}"," ",text,flags=re.I)
    text=re.sub(r"\s+"," ",text).strip()
    return text

def shash(text):
    n=normalize_statement(text)
    return hashlib.sha256(n.encode()).hexdigest() if n else ""

def locate(lines,spec):
    starts=[]
    for i,line in enumerate(lines,1):
        if spec["start_contains"] in line:
            if spec.get("must_follow"):
                window="\n".join(lines[i-1:min(len(lines),i+25)])
                if spec["must_follow"] not in window:
                    continue
            starts.append(i)
    if len(starts)!=1:
        raise ValueError(f"{spec['source_file']}: expected one start for {spec['label']}, found {starts}")
    a=starts[0]
    end_hits=[]
    for j in range(a+1,len(lines)+1):
        if spec["end_contains"] in lines[j-1]:
            end_hits.append(j)
            break
    if not end_hits:
        raise ValueError(f"{spec['source_file']}: end marker not found for {spec['label']}")
    b=end_hits[0]-1
    while b>=a and not lines[b-1].strip(): b-=1
    return a,b

def generated_id(source_id,start,h):
    return f"{source_id or 'IMP'}-ORR{start:06d}-{h[:8].upper()}"

def recompute_solution_flags(ledger,links):
    byid={r["problem_id"]:r for r in ledger};sols=defaultdict(set);hints=defaultdict(set)
    for s in links:
        pid=s.get("linked_problem_id","")
        if pid not in byid:continue
        kind=(s.get("solution_kind") or "").upper()
        if kind=="SOLUTION":sols[pid].add(s["solution_id"])
        elif kind=="HINT":hints[pid].add(s["solution_id"])
    sols_h=defaultdict(set);hints_h=defaultdict(set)
    for r in ledger:
        h=r.get("statement_hash","")
        if h:
            sols_h[h].update(sols.get(r["problem_id"],set()));hints_h[h].update(hints.get(r["problem_id"],set()))
    for r in ledger:
        pid=r["problem_id"];h=r.get("statement_hash","")
        local=sorted(sols.get(pid,set()));grp=sorted(sols_h.get(h,set())) if h else []
        prop=[x for x in grp if x not in local];allsol=local+prop
        r["has_solution"]="YES" if allsol else "NO"
        r["solution_id"]=";".join(allsol)
        r["has_hint"]="YES" if (hints.get(pid) or hints_h.get(h)) else "NO"
        r["local_solution_ids"]=";".join(local);r["propagated_solution_ids"]=";".join(prop)
        r["solution_link_status"]="LOCAL_OR_COMPANION_LINKED" if local else ("EXACT_DUPLICATE_PROPAGATED" if prop else "NO_SOLUTION_LINKED")

def rebuild_semantic(ledger):
    g=defaultdict(list)
    for r in ledger:
        if r.get("statement_hash"):g[r["statement_hash"]].append(r)
    out=[]
    for h,m in sorted(g.items()):
        m=sorted(m,key=lambda r:r["problem_id"]);rep=m[0]
        sols=sorted({x for r in m for x in split_ids(r.get("solution_id",""))})
        hints=sorted({x for r in m for x in split_ids(r.get("hint_id",""))})
        out.append({
            "statement_hash":h,"semantic_problem_id":f"SEM-{h[:12].upper()}","representative_problem_id":rep["problem_id"],
            "member_count":len(m),"member_problem_ids":";".join(r["problem_id"] for r in m),
            "source_files":";".join(sorted({r.get("source_file","") for r in m})),
            "source_collections":";".join(sorted({r.get("source_collection","") for r in m})),
            "problem_types":";".join(sorted({r.get("problem_type","") for r in m if r.get("problem_type","")})),
            "source_problem_numbers":";".join(sorted({r.get("source_problem_number","") for r in m if r.get("source_problem_number","")})),
            "aggregate_solution_ids":";".join(sols),"aggregate_hint_ids":";".join(hints),
            "solution_availability":"YES" if sols else "NO","review_status":"NEEDS_EDITORIAL_REVIEW",
        })
    return out

def rebuild_orphans(links,ledger):
    hby={r["problem_id"]:r.get("statement_hash","") for r in ledger};rem=[]
    for s in links:
        if s.get("linked_problem_id"):continue
        status=s.get("reconciliation_status") or s.get("link_status") or "UNRESOLVED"
        if status in TERMINAL_STATUSES or status.startswith("RESOLVED_"):continue
        pids=split_ids(s.get("candidate_problem_ids",""));hs=sorted({hby.get(x,"") for x in pids if hby.get(x,"")})
        rem.append({
            "solution_id":s.get("solution_id",""),"solution_semantic_unit_id":s.get("solution_semantic_unit_id",""),
            "solution_kind":s.get("solution_kind",""),"solution_source_file":s.get("solution_source_file",""),
            "solution_line_range":s.get("solution_line_range",""),"source_problem_number":s.get("source_problem_number",""),
            "status":status,"candidate_problem_ids":s.get("candidate_problem_ids",""),
            "candidate_statement_hashes":";".join(hs),
            "editorial_action":"CHOOSE_AMONG_DISTINCT_STATEMENTS" if pids else "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN",
        })
    gg=defaultdict(list)
    for r in rem:gg[r.get("solution_semantic_unit_id") or r["solution_id"]].append(r)
    units=[]
    for k,m in sorted(gg.items()):
        pids=sorted({x for r in m for x in split_ids(r["candidate_problem_ids"])})
        hs=sorted({x for r in m for x in split_ids(r["candidate_statement_hashes"])})
        units.append({
            "orphan_semantic_unit_id":k,"member_count":len(m),
            "member_solution_ids":";".join(sorted(r["solution_id"] for r in m)),
            "source_files":";".join(sorted({r["solution_source_file"] for r in m})),
            "statuses":";".join(sorted({r["status"] for r in m})),
            "candidate_problem_ids":";".join(pids),"candidate_statement_hashes":";".join(hs),
            "distinct_candidate_statement_count":len(hs),
            "editorial_action":"CHOOSE_AMONG_DISTINCT_STATEMENTS" if hs else "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN",
        })
    return rem,units

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()

    repo=args.repo.resolve();inv=repo/"imports"/"problem_inventory";srcroot=repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"
    pfields,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")
    lfields,links=read_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv")

    lby={r["problem_id"]:r for r in ledger}
    hash_to_ids=defaultdict(list)
    for r in ledger:
        if r.get("statement_hash"):hash_to_ids[r["statement_hash"]].append(r["problem_id"])

    errors=[];recover_rows=[];targets=dict(EXISTING_LINKS)
    new_pfields=extend(pfields,["structural_status","structural_repair_note","orphan_recovery_unit_id"])

    for uid,target in EXISTING_LINKS.items():
        if target not in lby:errors.append(f"{uid}: existing target not active: {target}")

    for uid,spec in RECOVERY_SPECS.items():
        p=srcroot/spec["source_file"]
        if not p.exists():
            errors.append(f"{uid}: missing source {spec['source_file']}");continue
        lines=safe_lines(p)
        try:a,b=locate(lines,spec)
        except Exception as e:
            errors.append(f"{uid}: {e}");continue
        text="\n".join(lines[a-1:b])
        h=shash(text)
        existing=hash_to_ids.get(h,[])
        if existing:
            target=sorted(existing)[0]
            targets[uid]=target
            recover_rows.append({
                "orphan_semantic_unit_id":uid,"action":"USE_EXISTING_HASH_EQUIVALENT",
                "problem_id":target,"source_file":spec["source_file"],"source_line_range":f"L{a}-L{b}",
                "problem_type":spec["problem_type"],"source_problem_number":spec["source_problem_number"],
                "statement_hash":h,"label":spec["label"],
            })
            continue

        templates=[r for r in ledger if r.get("source_file","")==spec["source_file"]]
        if not templates:
            errors.append(f"{uid}: no ledger template for source {spec['source_file']}");continue
        tmpl=min(templates,key=lambda r:abs((parse_range(r.get("source_line_range","")) or (a,a))[0]-a))
        nr=dict(tmpl)
        for k,v in RESET_VALUES.items():
            if k in nr or k in new_pfields:nr[k]=v
        nid=generated_id(tmpl.get("source_id",""),a,h)
        if nid in lby:
            errors.append(f"{uid}: generated ID collision {nid}");continue
        nr["problem_id"]=nid
        nr["source_file"]=spec["source_file"]
        nr["source_line_range"]=f"L{a}-L{b}"
        if "source_location" in new_pfields:nr["source_location"]=nr["source_line_range"]
        nr["source_problem_number"]=spec["source_problem_number"]
        nr["source_heading"]=lines[a-1].strip()
        nr["problem_type"]=spec["problem_type"]
        nr["statement_hash"]=h
        # A recovered statement has a new hash and therefore begins as its
        # own semantic representative. Do not inherit reconciliation identity
        # from the nearby template row.
        nr["representative_problem_id"]=nid
        nr["duplicate_role"]="UNIQUE_STATEMENT"
        if "reconciliation_status" in new_pfields:
            nr["reconciliation_status"]="UNIQUE_STATEMENT"
        nr["structural_status"]="ACTIVE_TARGETED_ORPHAN_STATEMENT_RECOVERY"
        nr["structural_repair_note"]="Recovered exact source statement after structural freeze for orphan solution reconciliation."
        nr["orphan_recovery_unit_id"]=uid
        ledger.append(nr);lby[nid]=nr;hash_to_ids[h].append(nid);targets[uid]=nid
        recover_rows.append({
            "orphan_semantic_unit_id":uid,"action":"RECOVER_NEW_STATEMENT",
            "problem_id":nid,"source_file":spec["source_file"],"source_line_range":f"L{a}-L{b}",
            "problem_type":spec["problem_type"],"source_problem_number":spec["source_problem_number"],
            "statement_hash":h,"label":spec["label"],
        })

    expected=set(EXISTING_LINKS)|set(RECOVERY_SPECS)
    if set(targets)!=expected:
        errors.append(f"Target set mismatch: have {sorted(targets)}, expected {sorted(expected)}")

    new_lfields=extend(lfields,["previous_linked_problem_id","reconciliation_status","editorial_decision","editorial_rationale"])
    shadow_links=[];linked_units=set();linked_blocks=0
    for s0 in links:
        s=dict(s0)
        uid=s.get("solution_semantic_unit_id","")
        if uid in targets:
            target=targets[uid]
            s["previous_linked_problem_id"]=s.get("linked_problem_id","")
            s["linked_problem_id"]=target
            s["candidate_problem_ids"]=target
            s["reconciliation_status"]="RESOLVED_SOURCE_GROUNDED_EDITORIAL_LINK"
            s["editorial_decision"]="ACCEPT"
            s["editorial_rationale"]="Source-grounded P2/P3 review: solution matches exact current or recovered source statement."
            linked_units.add(uid);linked_blocks+=1
        shadow_links.append(s)

    for uid in expected:
        if uid not in linked_units:errors.append(f"{uid}: no solution-link blocks updated")

    recompute_solution_flags(ledger,shadow_links)
    sem=rebuild_semantic(ledger)
    rem,units=rebuild_orphans(shadow_links,ledger)

    write_tsv(inv/"P2_P3_EDITORIAL_RESOLUTION_PLAN.tsv",
              ["orphan_semantic_unit_id","action","problem_id","source_file","source_line_range",
               "problem_type","source_problem_number","statement_hash","label"],recover_rows)
    write_tsv(inv/"PROBLEM_LEDGER_P2_P3_RESOLUTION_SHADOW.tsv",new_pfields,ledger)
    write_tsv(inv/"PROBLEM_SOLUTION_LINKS_P2_P3_RESOLUTION_SHADOW.tsv",new_lfields,shadow_links)

    semfields=["statement_hash","semantic_problem_id","representative_problem_id","member_count","member_problem_ids",
               "source_files","source_collections","problem_types","source_problem_numbers","aggregate_solution_ids",
               "aggregate_hint_ids","solution_availability","review_status"]
    remfields=["solution_id","solution_semantic_unit_id","solution_kind","solution_source_file","solution_line_range",
               "source_problem_number","status","candidate_problem_ids","candidate_statement_hashes","editorial_action"]
    unitfields=["orphan_semantic_unit_id","member_count","member_solution_ids","source_files","statuses",
                "candidate_problem_ids","candidate_statement_hashes","distinct_candidate_statement_count","editorial_action"]
    write_tsv(inv/"SEMANTIC_PROBLEM_UNITS_P2_P3_RESOLUTION_SHADOW.tsv",semfields,sem)
    write_tsv(inv/"REMAINING_ORPHANS_P2_P3_RESOLUTION_SHADOW.tsv",remfields,rem)
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS_P2_P3_RESOLUTION_SHADOW.tsv",unitfields,units)

    summary=[
        "# P2/P3 source-grounded editorial resolution","",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- Units resolved: **{len(linked_units)} / 9**",
        f"- Existing current targets linked: **{len(EXISTING_LINKS)}**",
        f"- Recovery specs processed: **{len(RECOVERY_SPECS)}**",
        f"- New statement rows recovered: **{sum(1 for r in recover_rows if r['action']=='RECOVER_NEW_STATEMENT')}**",
        f"- Existing hash-equivalent recovered targets reused: **{sum(1 for r in recover_rows if r['action']=='USE_EXISTING_HASH_EQUIVALENT')}**",
        f"- Solution/hint blocks linked: **{linked_blocks}**",
        f"- Active orphan semantic units after resolution: **{len(units)}**",
        f"- Validation errors: **{len(errors)}**","",
        "Decisions are based on exact source statement/solution fit, not ranking score alone."
    ]
    if errors:summary+=["","## Validation errors",""]+[f"- {e}" for e in errors]
    (inv/"P2_P3_EDITORIAL_RESOLUTION_SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

    if errors:
        print("P2/P3 EDITORIAL RESOLUTION VALIDATION FAILED")
        for e in errors:print(" -",e)
        return 1

    print(f"P2/P3 EDITORIAL RESOLUTION DRY RUN PASSED: units={len(linked_units)} new_statements={sum(1 for r in recover_rows if r['action']=='RECOVER_NEW_STATEMENT')} remaining_units={len(units)}")
    if not args.apply:
        print("No master files changed.")
        return 0

    for name in ("PROBLEM_LEDGER.tsv","PROBLEM_SOLUTION_LINKS.tsv","SEMANTIC_PROBLEM_UNITS.tsv","REMAINING_ORPHANS.tsv","ORPHAN_SEMANTIC_UNITS.tsv"):
        src=inv/name;dst=inv/name.replace(".tsv","_PRE_P2_P3_EDITORIAL_RESOLUTION.tsv")
        if src.exists() and not dst.exists():shutil.copy2(src,dst)

    write_tsv(inv/"PROBLEM_LEDGER.tsv",new_pfields,ledger)
    write_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv",new_lfields,shadow_links)
    write_tsv(inv/"SEMANTIC_PROBLEM_UNITS.tsv",semfields,sem)
    write_tsv(inv/"REMAINING_ORPHANS.tsv",remfields,rem)
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv",unitfields,units)

    print(f"P2/P3 EDITORIAL RESOLUTION APPLIED: units={len(linked_units)} remaining_units={len(units)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
