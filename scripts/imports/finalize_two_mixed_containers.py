#!/usr/bin/env python3
from __future__ import annotations

import argparse, csv, hashlib, re, shutil
from collections import defaultdict
from pathlib import Path

TARGET_FAMILIES={"RSF-004","RSF-008"}
LINE_RANGE_RE=re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
COMMENT_RE=re.compile(r"(?<!\\)%.*$")
HEADING_RE=re.compile(r"^\s*\\(?P<level>section|subsection|subsubsection)\*?\{(?P<title>[^{}]+)\}\s*$",re.I)
OBJECT_TITLE_RE=re.compile(
    r"^\s*(?P<kind>Problem|Exercise|Example|Question|Task|Challenge)\b"
    r"(?:\s+(?P<number>[A-Za-z0-9][A-Za-z0-9.()_\-/]*))?\s*[:.\-]?\s*(?P<rest>.*)$",
    re.I
)
BOLD_PROBLEM_RE=re.compile(r"^\s*\\textbf\{\s*(?:Problem|Exercise|Question|Task|Challenge)\s*[.:]?\s*\}\s*$",re.I)
TERMINALS=[
    re.compile(r"^\s*\\begin\{(?:solution|answer|proofsolution|proof)\*?\}",re.I),
    re.compile(r"^\s*\\(?:section|subsection|subsubsection|paragraph|subparagraph)\*?\{\s*(?:Solution|Answer|Proof)\s*[.:]?\s*\}\s*$",re.I),
    re.compile(r"^\s*\\textbf\{\s*(?:Solution|Answer|Proof)\s*[.:]?\s*\}\s*$",re.I),
    re.compile(r"^\s*\\emph\{\s*(?:Solution|Answer|Proof)\s*[.:]?\s*\}\s*$",re.I),
    re.compile(r"^\s*(?:Solution|Answer|Proof)\s*[.:]\s*$",re.I),
]
LEVEL={"section":1,"subsection":2,"subsubsection":3}
RESET_VALUES={
    "duplicate_group":"",
    "canonical_match_type":"UNREVIEWED","canonical_problem_id":"","canonical_volume":"","canonical_chapter":"",
    "target_volume":"UNCLASSIFIED","target_chapter":"UNCLASSIFIED","target_section":"UNCLASSIFIED",
    "mapping_confidence":"UNCLASSIFIED","migration_status":"UNREVIEWED","migration_commit":"",
    "review_status":"NEEDS_EDITORIAL_REVIEW","has_hint":"NO","has_solution":"NO","solution_id":"",
    "local_solution_ids":"","propagated_solution_ids":"","solution_link_status":"NO_SOLUTION_LINKED",
}
TERMINAL_STATUSES={"RESOLVED_NOT_A_PROBLEM","MISSING_COMPANION_STATEMENT"}

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
    for e in extras:
        if e not in out:out.append(e)
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
    text=re.split(r"(?im)^\s*(?:\\textbf\{)?(?:Solution|Answer|Hint)\}?\s*[:.]",text,maxsplit=1)[0]
    lines=[strip_comment(x) for x in text.splitlines()]
    text="\n".join(lines)
    text=re.sub(r"\\label\{[^}]+\}"," ",text)
    text=re.sub(r"\\begin\{(?:problem|exercise|example|question|task|challenge)\*?\}(?:\[[^\]]*\])?"," ",text,flags=re.I)
    text=re.sub(r"\\end\{(?:problem|exercise|example|question|task|challenge)\*?\}"," ",text,flags=re.I)
    text=re.sub(r"\\(?:section|subsection|subsubsection|paragraph)\*?\{\s*(?:Problem|Exercise|Example|Question|Task|Challenge)[^}]*\}"," ",text,flags=re.I)
    text=re.sub(r"^\s*\\item(?:\[[^\]]+\])?\s*","",text,flags=re.I)
    text=re.sub(r"^\s*(?:\\textbf\{)?(?:Problem|Exercise|Example|Question|Task|Challenge)(?:\s+[A-Za-z0-9][A-Za-z0-9.()_\-/]*)?\}?\s*[:.]\s*","",text,flags=re.I)
    text=re.sub(r"\s+"," ",text).strip()
    return text

def shash(text):
    n=normalize_statement(text)
    return hashlib.sha256(n.encode()).hexdigest() if n else ""

def is_terminal(line):
    x=strip_comment(line)
    return any(p.search(x) for p in TERMINALS)

def heading(line):
    m=HEADING_RE.match(strip_comment(line))
    if not m:return None
    return m.group("level").lower(),m.group("title").strip()

def next_nonblank(lines,i,limit):
    for j in range(i+1,min(limit,i+8)):
        if strip_comment(lines[j]).strip():
            return j,strip_comment(lines[j]).strip()
    return None,None

def is_statement_heading(line):
    h=heading(line)
    return bool(h and h[1].strip().lower()=="statement")

def find_objects(lines,a,b):
    # a,b 1-based inclusive
    starts=[]
    for lineno in range(a,b+1):
        h=heading(lines[lineno-1])
        if h:
            lev,title=h
            mt=OBJECT_TITLE_RE.match(title)
            if mt:
                starts.append({
                    "start":lineno,"level":LEVEL[lev],"kind":mt.group("kind").upper(),
                    "number":(mt.group("number") or "").strip(),"heading":title,
                    "origin":"EXPLICIT_OBJECT_HEADING",
                })
                continue

            # Implicit problem: a section/subsection immediately introducing a Statement heading.
            idx=lineno-1
            nj,nline=next_nonblank(lines,idx,b)
            if nj is not None and is_statement_heading(lines[nj]):
                starts.append({
                    "start":lineno,"level":LEVEL[lev],"kind":"PROBLEM","number":"",
                    "heading":title,"origin":"HEADING_FOLLOWED_BY_STATEMENT",
                })
                continue

        if BOLD_PROBLEM_RE.match(strip_comment(lines[lineno-1])):
            # Only add standalone bold problem if not already inside an explicit object start on same/previous line.
            if not starts or starts[-1]["start"] < lineno-1:
                starts.append({
                    "start":lineno,"level":4,"kind":"PROBLEM","number":"",
                    "heading":strip_comment(lines[lineno-1]).strip(),"origin":"BOLD_OBJECT_MARKER",
                })

    # Deduplicate starts.
    by={}
    for s in starts:by.setdefault(s["start"],s)
    return [by[k] for k in sorted(by)]

def segment_object(lines,obj,next_obj_start,parent_end):
    start=obj["start"]
    hard_end=(next_obj_start-1) if next_obj_start else parent_end

    # Problem/exercise/question/task objects stop at their Solution/Answer/Proof.
    if obj["kind"]!="EXAMPLE":
        for j in range(start+1,hard_end+1):
            if is_terminal(lines[j-1]):
                return start,max(start,j-1)

    # Worked examples stop at next same/higher-level structural heading, even if it
    # is summary/theory/context, so they do not swallow exposition.
    if obj["kind"]=="EXAMPLE":
        for j in range(start+1,hard_end+1):
            h=heading(lines[j-1])
            if h and LEVEL[h[0]]<=obj["level"]:
                return start,max(start,j-1)

    return start,hard_end

def generated_id(source_id,start,h):
    return f"{source_id or 'IMP'}-F2R{start:06d}-{h[:8].upper()}"

def solution_start(r):
    rr=parse_range(r.get("solution_line_range",""))
    return rr[0] if rr else None

def unique_number_match(link,children):
    num=(link.get("source_problem_number") or "").strip()
    if not num:return None
    ms=[c for c in children if (c.get("source_problem_number") or "").strip()==num]
    return ms[0] if len(ms)==1 else None

def same_file_preceding_match(link,children,src):
    if link.get("solution_source_file","")!=src:return None
    s=solution_start(link)
    if s is None:return None
    cs=sorted(children,key=lambda c:parse_range(c["proposed_line_range"])[0])
    hits=[]
    for i,c in enumerate(cs):
        aa,bb=parse_range(c["proposed_line_range"])
        nxt=parse_range(cs[i+1]["proposed_line_range"])[0] if i+1<len(cs) else None
        if s>bb and (nxt is None or s<nxt):hits.append(c)
    return hits[0] if len(hits)==1 else None

def replace_candidates(s,mapping):
    out=[];seen=set()
    for pid in split_ids(s):
        for x in mapping.get(pid,[pid]):
            if x not in seen:seen.add(x);out.append(x)
    return ";".join(out)

def recompute_solution_flags(ledger,links):
    byid={r["problem_id"]:r for r in ledger}
    sols=defaultdict(set);hints=defaultdict(set)
    for s in links:
        pid=s.get("linked_problem_id","")
        if pid not in byid:continue
        k=(s.get("solution_kind") or "").upper()
        if k=="SOLUTION":sols[pid].add(s["solution_id"])
        elif k=="HINT":hints[pid].add(s["solution_id"])
    sh=defaultdict(set);hh=defaultdict(set)
    for r in ledger:
        h=r.get("statement_hash","")
        if h:
            sh[h].update(sols.get(r["problem_id"],set()));hh[h].update(hints.get(r["problem_id"],set()))
    for r in ledger:
        pid=r["problem_id"];h=r.get("statement_hash","")
        local=sorted(sols.get(pid,set()));group=sorted(sh.get(h,set())) if h else []
        prop=[x for x in group if x not in local];allsol=local+prop
        r["has_solution"]="YES" if allsol else "NO";r["solution_id"]=";".join(allsol)
        r["has_hint"]="YES" if (hints.get(pid) or hh.get(h)) else "NO"
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
        if status in TERMINAL_STATUSES:continue
        pids=split_ids(s.get("candidate_problem_ids",""));hs=sorted({hby.get(x,"") for x in pids if hby.get(x,"")})
        if status=="NEEDS_STRUCTURAL_RESCAN":action="STRUCTURAL_RESCAN"
        elif status=="NEEDS_POST_SPLIT_RECONCILIATION":action="RELINK_AFTER_FINAL_TWO_REPAIR"
        elif status=="UNRESOLVED_NUMBERING_MISMATCH":action="REVIEW_NUMBERING_MISMATCH"
        elif pids:action="CHOOSE_AMONG_DISTINCT_STATEMENTS"
        else:action="LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN"
        rem.append({
            "solution_id":s.get("solution_id",""),"solution_semantic_unit_id":s.get("solution_semantic_unit_id",""),
            "solution_kind":s.get("solution_kind",""),"solution_source_file":s.get("solution_source_file",""),
            "solution_line_range":s.get("solution_line_range",""),"source_problem_number":s.get("source_problem_number",""),
            "status":status,"candidate_problem_ids":s.get("candidate_problem_ids",""),
            "candidate_statement_hashes":";".join(hs),"editorial_action":action,
        })
    gg=defaultdict(list)
    for r in rem:gg[r.get("solution_semantic_unit_id") or r["solution_id"]].append(r)
    units=[]
    for k,m in sorted(gg.items()):
        hs=set();pids=set();sts=set();acts=set()
        for r in m:
            hs.update(split_ids(r["candidate_statement_hashes"]));pids.update(split_ids(r["candidate_problem_ids"]))
            sts.add(r["status"]);acts.add(r["editorial_action"])
        if "RELINK_AFTER_FINAL_TWO_REPAIR" in acts:action="RELINK_AFTER_FINAL_TWO_REPAIR"
        elif "STRUCTURAL_RESCAN" in acts:action="STRUCTURAL_RESCAN"
        elif len(hs)>1:action="CHOOSE_AMONG_DISTINCT_STATEMENTS"
        elif not hs:action="LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN"
        else:action="RECHECK_EQUIVALENCE_RULE"
        units.append({
            "orphan_semantic_unit_id":k,"member_count":len(m),"member_solution_ids":";".join(sorted(r["solution_id"] for r in m)),
            "source_files":";".join(sorted({r["solution_source_file"] for r in m})),"statuses":";".join(sorted(sts)),
            "candidate_problem_ids":";".join(sorted(pids)),"candidate_statement_hashes":";".join(sorted(hs)),
            "distinct_candidate_statement_count":len(hs),"editorial_action":action,
        })
    return rem,units

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()

    repo=args.repo.resolve();inv=repo/"imports"/"problem_inventory";srcroot=repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"

    _,fams=read_tsv(inv/"REVIEW_SPLIT_UNIQUE_FAMILIES.tsv")
    _,members=read_tsv(inv/"REVIEW_SPLIT_FAMILY_MEMBERS.tsv")
    pfields,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")
    lfields,links=read_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv")

    tf=[r for r in fams if r["review_family_id"] in TARGET_FAMILIES]
    if {r["review_family_id"] for r in tf}!=TARGET_FAMILIES:
        raise SystemExit("Final-two family metadata missing.")

    ledger_by={r["problem_id"]:r for r in ledger}
    mem_by=defaultdict(list)
    for r in members:
        if r["review_family_id"] in TARGET_FAMILIES:mem_by[r["review_family_id"]].append(r)

    errors=[];parent_pairs={};plan=[];objects_preview=[];newids=set()

    for fam in tf:
        fid=fam["review_family_id"]
        for m in mem_by[fid]:
            pid=m["problem_id"]
            if pid not in ledger_by:
                errors.append(f"{fid}/{pid}: parent no longer active");continue
            parent=ledger_by[pid];pr=parse_range(parent["source_line_range"]);src=parent["source_file"]
            path=srcroot/src
            if not path.exists():
                errors.append(f"{fid}/{pid}: source missing {src}");continue
            lines=safe_lines(path)
            objs=find_objects(lines,*pr)
            pairs=[]
            for i,obj in enumerate(objs):
                next_start=objs[i+1]["start"] if i+1<len(objs) else None
                a,b=segment_object(lines,obj,next_start,pr[1])
                text="\n".join(lines[a-1:b]);h=shash(text)
                if not h:continue
                span=b-a+1
                if span>=250:
                    errors.append(f"{fid}/{pid}: object {obj['heading']} remains {span} lines")
                nid=generated_id(parent.get("source_id",""),a,h)
                if nid in newids:errors.append(f"{fid}/{pid}: generated ID collision {nid}")
                newids.add(nid)
                c={
                    "review_family_id":fid,"parent_problem_id":pid,"source_id":parent.get("source_id",""),
                    "source_collection":parent.get("source_collection",""),"source_file":src,
                    "object_origin":obj["origin"],"detected_type":obj["kind"],
                    "source_problem_number":obj["number"],"source_heading":obj["heading"],
                    "proposed_line_range":f"L{a}-L{b}","line_span":span,"statement_hash":h,
                }
                pairs.append((c,nid));objects_preview.append(dict(c,new_problem_id=nid))
            if not pairs:
                errors.append(f"{fid}/{pid}: no final objects found")
            parent_pairs[pid]=pairs
            plan.append({
                "review_family_id":fid,"parent_problem_id":pid,"source_file":src,
                "parent_line_range":parent["source_line_range"],"object_count":len(pairs),
                "new_problem_ids":";".join(n for _,n in pairs),
                "object_line_ranges":";".join(c["proposed_line_range"] for c,_ in pairs),
                "max_object_span":max((int(c["line_span"]) for c,_ in pairs),default=0),
            })

    mapping={p:[n for _,n in pairs] for p,pairs in parent_pairs.items()}
    new_pfields=extend(pfields,["structural_status","supersedes_problem_id","structural_repair_note","review_family_id"])
    new_lfields=extend(lfields,["previous_linked_problem_id","structural_relink_status","structural_relink_method"])

    shadow=[];superseded=[]
    for r0 in ledger:
        pid=r0["problem_id"]
        if pid not in parent_pairs:
            shadow.append(dict(r0));continue
        pairs=parent_pairs[pid]
        ar=dict(r0);ar["superseded_by_problem_ids"]=";".join(n for _,n in pairs);ar["supersession_reason"]="FINAL_TWO_MIXED_CONTAINER_REPAIR";superseded.append(ar)
        for c,nid in pairs:
            nr=dict(r0)
            for k,v in RESET_VALUES.items():
                if k in nr or k in new_pfields:nr[k]=v
            nr["problem_id"]=nid;nr["source_id"]=c["source_id"];nr["source_collection"]=c["source_collection"]
            nr["source_file"]=c["source_file"];nr["source_line_range"]=c["proposed_line_range"]
            if "source_location" in new_pfields:nr["source_location"]=c["proposed_line_range"]
            nr["source_problem_number"]=c["source_problem_number"];nr["source_heading"]=c["source_heading"]
            nr["problem_type"]=c["detected_type"];nr["statement_hash"]=c["statement_hash"]
            nr["structural_status"]="ACTIVE_FINAL_TWO_RESEGMENTED";nr["supersedes_problem_id"]=pid
            nr["review_family_id"]=c["review_family_id"]
            nr["structural_repair_note"]="Final source-structural repair: actual problem/example headings retained; explanatory glue omitted."
            shadow.append(nr)

    shadow_ids={r["problem_id"] for r in shadow};shadow_links=[];relinked=0;review_links=0;rewritten=0;link_review=[]
    for s0 in links:
        s=dict(s0);s.setdefault("previous_linked_problem_id","");s.setdefault("structural_relink_status","");s.setdefault("structural_relink_method","")
        oldc=s.get("candidate_problem_ids","");newc=replace_candidates(oldc,mapping)
        if newc!=oldc:s["candidate_problem_ids"]=newc;rewritten+=1
        old=s.get("linked_problem_id","")
        if old in parent_pairs:
            parent=ledger_by[old];children=[dict(c,new_problem_id=n) for c,n in parent_pairs[old]]
            chosen=unique_number_match(s,children);method="UNIQUE_SOURCE_NUMBER" if chosen else ""
            if not chosen:
                chosen=same_file_preceding_match(s,children,parent["source_file"])
                if chosen:method="SAME_FILE_NEAREST_PRECEDING_OBJECT"
            s["previous_linked_problem_id"]=old
            if chosen:
                s["linked_problem_id"]=chosen["new_problem_id"];s["structural_relink_status"]="RELINKED";s["structural_relink_method"]=method;relinked+=1
            else:
                s["linked_problem_id"]="";s["structural_relink_status"]="NEEDS_POST_SPLIT_RECONCILIATION";s["reconciliation_status"]="NEEDS_POST_SPLIT_RECONCILIATION"
                s["candidate_problem_ids"]=";".join(mapping[old]);review_links+=1
                link_review.append({
                    "solution_id":s.get("solution_id",""),"previous_linked_problem_id":old,
                    "solution_source_file":s.get("solution_source_file",""),"solution_line_range":s.get("solution_line_range",""),
                    "source_problem_number":s.get("source_problem_number",""),"candidate_problem_ids":s["candidate_problem_ids"],
                    "review_action":"RELINK_AFTER_FINAL_TWO_REPAIR",
                })
        if s.get("linked_problem_id") and s["linked_problem_id"] not in shadow_ids:
            errors.append(f"{s.get('solution_id','')}: dangling link {s['linked_problem_id']}")
        shadow_links.append(s)

    recompute_solution_flags(shadow,shadow_links);sem=rebuild_semantic(shadow);rem,units=rebuild_orphans(shadow_links,shadow)

    write_tsv(inv/"FINAL_TWO_REPAIR_OBJECTS.tsv",
              ["review_family_id","parent_problem_id","source_id","source_collection","source_file","object_origin",
               "detected_type","source_problem_number","source_heading","proposed_line_range","line_span","statement_hash","new_problem_id"],
              objects_preview)
    write_tsv(inv/"FINAL_TWO_REPAIR_PLAN.tsv",
              ["review_family_id","parent_problem_id","source_file","parent_line_range","object_count","new_problem_ids","object_line_ranges","max_object_span"],plan)
    write_tsv(inv/"PROBLEM_LEDGER_FINAL_TWO_SHADOW.tsv",new_pfields,shadow)
    write_tsv(inv/"PROBLEM_SOLUTION_LINKS_FINAL_TWO_SHADOW.tsv",new_lfields,shadow_links)
    write_tsv(inv/"FINAL_TWO_REPAIR_LINK_REVIEW.tsv",
              ["solution_id","previous_linked_problem_id","solution_source_file","solution_line_range","source_problem_number","candidate_problem_ids","review_action"],link_review)

    supfields=extend(pfields,["superseded_by_problem_ids","supersession_reason"])
    write_tsv(inv/"FINAL_TWO_REPAIR_SUPERSEDED_PREVIEW.tsv",supfields,superseded)
    semfields=["statement_hash","semantic_problem_id","representative_problem_id","member_count","member_problem_ids","source_files","source_collections","problem_types","source_problem_numbers","aggregate_solution_ids","aggregate_hint_ids","solution_availability","review_status"]
    remfields=["solution_id","solution_semantic_unit_id","solution_kind","solution_source_file","solution_line_range","source_problem_number","status","candidate_problem_ids","candidate_statement_hashes","editorial_action"]
    unitfields=["orphan_semantic_unit_id","member_count","member_solution_ids","source_files","statuses","candidate_problem_ids","candidate_statement_hashes","distinct_candidate_statement_count","editorial_action"]
    write_tsv(inv/"SEMANTIC_PROBLEM_UNITS_FINAL_TWO_SHADOW.tsv",semfields,sem)
    write_tsv(inv/"REMAINING_ORPHANS_FINAL_TWO_SHADOW.tsv",remfields,rem)
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS_FINAL_TWO_SHADOW.tsv",unitfields,units)

    objcount=sum(len(v) for v in parent_pairs.values())
    summary=[
        "# Final two mixed-container repair","",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- Families repaired: **{len(tf)}**",
        f"- Parent rows superseded: **{len(parent_pairs)}**",
        f"- Final problem/example objects created: **{objcount}**",
        f"- Ledger rows: **{len(ledger)} → {len(shadow)}**",
        f"- Direct links relinked uniquely: **{relinked}**",
        f"- Links requiring post-repair review: **{review_links}**",
        f"- Candidate lists rewritten: **{rewritten}**",
        f"- Remaining orphan semantic units: **{len(units)}**",
        f"- Validation errors: **{len(errors)}**","",
        "Explanatory sections such as `Theory for Problem ...`, summaries, diagrams, and solution/proof regions are not emitted as problem objects.",
        "Explicit worked examples remain valid `EXAMPLE` objects and are stopped before the next same/higher-level heading.",
    ]
    if errors:summary+=["","## Validation errors",""]+[f"- {e}" for e in errors]
    (inv/"FINAL_TWO_REPAIR_SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

    if errors:
        print("FINAL TWO REPAIR VALIDATION FAILED")
        for e in errors:print(" -",e)
        return 1

    print(f"FINAL TWO REPAIR DRY RUN PASSED: parents={len(parent_pairs)} objects={objcount} ledger={len(ledger)}->{len(shadow)} relinked={relinked} review_links={review_links}")
    if not args.apply:
        print("No master files changed. Inspect FINAL_TWO_REPAIR_SUMMARY.md, FINAL_TWO_REPAIR_OBJECTS.tsv, and link review.")
        return 0

    for name in ("PROBLEM_LEDGER.tsv","PROBLEM_SOLUTION_LINKS.tsv","SEMANTIC_PROBLEM_UNITS.tsv","REMAINING_ORPHANS.tsv","ORPHAN_SEMANTIC_UNITS.tsv"):
        src=inv/name;dst=inv/name.replace(".tsv","_PRE_FINAL_TWO_REPAIR.tsv")
        if src.exists() and not dst.exists():shutil.copy2(src,dst)

    write_tsv(inv/"PROBLEM_LEDGER.tsv",new_pfields,shadow)
    write_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv",new_lfields,shadow_links)
    write_tsv(inv/"SEMANTIC_PROBLEM_UNITS.tsv",semfields,sem)
    write_tsv(inv/"REMAINING_ORPHANS.tsv",remfields,rem)
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv",unitfields,units)
    write_tsv(inv/"FINAL_TWO_REPAIR_SUPERSEDED_ROWS.tsv",supfields,superseded)
    print(f"FINAL TWO REPAIR APPLIED: parents={len(parent_pairs)} objects={objcount} remaining_units={len(units)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
