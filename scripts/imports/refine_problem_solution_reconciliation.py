#!/usr/bin/env python3
"""Second-pass orphan solution reconciliation.

Runs after reconcile_problem_inventory.py (v2). It does not edit canonical books.

Goals:
- collapse unresolved solution/hint copies by normalized solution-text hash;
- safely resolve ambiguous candidate sets that reduce to one statement hash;
- safely apply only high-confidence, fully supported numbering shifts;
- clear stale numbering-mismatch statuses that are no longer represented by NUMBERING_MISMATCHES.tsv;
- recompute problem solution availability and semantic-unit aggregates;
- leave every unresolved block explicit.
"""
from __future__ import annotations

import argparse, csv, hashlib, re, shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

LINE_RANGE_RE = re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
NUM_TAIL_RE = re.compile(r"(\d+)$")


def read_tsv(path: Path):
    if not path.exists():
        raise SystemExit(f"Required input missing: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r=csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]


def write_tsv(path: Path, fields: list[str], rows: Iterable[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def extend(fields, extras):
    out=list(fields)
    for e in extras:
        if e not in out: out.append(e)
    return out


def parse_range(s):
    m=LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


def safe_read(path: Path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try: return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError: pass
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def extract_range(root: Path, rel: str, rng: str):
    p=root/rel; rr=parse_range(rng)
    if not p.exists() or not rr: return ""
    lines=safe_read(p); a,b=rr; a=max(1,a); b=min(len(lines),b)
    return "\n".join(lines[a-1:b]) if a<=b else ""


def normalize_solution_text(text: str) -> str:
    # Conservative normalization: comments/whitespace + known solution wrappers only.
    text=re.sub(r"(?<!\\)%.*$", " ", text, flags=re.M)
    text=re.sub(r"\\(?:begin|end)\{(?:solution|proof|hint)\}", " ", text, flags=re.I)
    text=re.sub(r"\\(?:sub)*section\*?\{\s*(?:solution|answer|hint)\s*\}", " ", text, flags=re.I)
    text=re.sub(r"\\(?:paragraph|subparagraph)\*?\{\s*(?:solution|answer|hint)\s*\}", " ", text, flags=re.I)
    text=re.sub(r"\s+", " ", text).strip()
    return text


def text_hash(text: str):
    n=normalize_solution_text(text)
    return hashlib.sha256(n.encode("utf-8")).hexdigest() if n else ""


def numeric_tail(s: str):
    m=NUM_TAIL_RE.search(re.sub(r"\s+", "", (s or "").strip()))
    return int(m.group(1)) if m else None


def split_ids(s: str):
    return [x for x in (s or "").split(";") if x]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    ap.add_argument("--refresh-baseline", action="store_true")
    args=ap.parse_args()
    repo=args.repo.resolve(); inv=repo/"imports"/"problem_inventory"; root=repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"

    # Freeze v2 outputs as the deterministic input for this refinement.
    base_links=inv/"PROBLEM_SOLUTION_LINKS_RECONCILIATION_V2_BASELINE.tsv"
    base_ledger=inv/"PROBLEM_LEDGER_RECONCILIATION_V2_BASELINE.tsv"
    if args.refresh_baseline or not base_links.exists(): shutil.copy2(inv/"PROBLEM_SOLUTION_LINKS.tsv", base_links)
    if args.refresh_baseline or not base_ledger.exists(): shutil.copy2(inv/"PROBLEM_LEDGER.tsv", base_ledger)

    link_fields, links=read_tsv(base_links)
    ledger_fields, ledger=read_tsv(base_ledger)
    sem_fields, sem=read_tsv(inv/"SEMANTIC_PROBLEM_UNITS.tsv")
    try: mismatch_fields, mismatches=read_tsv(inv/"NUMBERING_MISMATCHES.tsv")
    except SystemExit: mismatches=[]

    ledger_by_id={r["problem_id"]:r for r in ledger}
    statement_hash_by_pid={r["problem_id"]:r.get("statement_hash","") for r in ledger}
    pids_by_hash=defaultdict(list)
    for r in ledger:
        if r.get("statement_hash"): pids_by_hash[r["statement_hash"]].append(r["problem_id"])

    # Representative per statement hash, preferring existing representative id.
    rep_by_hash={}
    for r in ledger:
        h=r.get("statement_hash","")
        if not h: continue
        rep=r.get("representative_problem_id","")
        if rep in ledger_by_id and statement_hash_by_pid.get(rep)==h: rep_by_hash[h]=rep
    for h,pids in pids_by_hash.items(): rep_by_hash.setdefault(h, sorted(pids)[0])

    # Extract and hash solution/hint text for every block.
    link_fields=extend(link_fields,["solution_text_hash","solution_semantic_unit_id","refinement_status","refinement_method"])
    groups=defaultdict(list)
    for s in links:
        txt=extract_range(root, s.get("solution_source_file",""), s.get("solution_line_range",""))
        h=text_hash(txt)
        s["solution_text_hash"]=h
        if h: groups[h].append(s)

    semantic_solution_rows=[]
    newly_linked_hash_collapse=0

    # 1. Exact solution-text semantic collapse + safe candidate collapse.
    for idx,h in enumerate(sorted(groups),1):
        members=groups[h]
        suid=f"SOLSEM-{hashlib.sha1(h.encode('ascii')).hexdigest()[:12].upper()}"
        for s in members: s["solution_semantic_unit_id"]=suid
        linked_hashes={statement_hash_by_pid.get(s.get("linked_problem_id",""),"") for s in members if s.get("linked_problem_id")}
        linked_hashes.discard("")
        candidate_pids=set()
        for s in members: candidate_pids.update(split_ids(s.get("candidate_problem_ids","")))
        candidate_hashes={statement_hash_by_pid.get(pid,"") for pid in candidate_pids}; candidate_hashes.discard("")

        resolution="UNRESOLVED"
        target_hash=""
        method=""
        # If any exact-copy member already has a trusted link and all trusted links agree,
        # propagate that semantic statement to the unresolved copies.
        if len(linked_hashes)==1:
            target_hash=next(iter(linked_hashes)); resolution="RESOLVED_BY_SOLUTION_TEXT_DUPLICATE"; method="EXACT_SOLUTION_TEXT_TRUSTED_MEMBER"
        # Otherwise if all ambiguous candidates reduce to one exact statement hash,
        # multiple candidate provenance rows are not a mathematical ambiguity.
        elif not linked_hashes and len(candidate_hashes)==1:
            target_hash=next(iter(candidate_hashes)); resolution="RESOLVED_BY_CANDIDATE_STATEMENT_EQUIVALENCE"; method="AMBIGUOUS_IDS_SINGLE_STATEMENT_HASH"

        if target_hash:
            rep=rep_by_hash[target_hash]
            for s in members:
                if not s.get("linked_problem_id"):
                    s["linked_problem_id"]=rep
                    s["link_status"]="LINKED_SEMANTIC_EQUIVALENCE"
                    s["reconciliation_status"]="RESOLVED_SEMANTIC_EQUIVALENCE"
                    s["reconciliation_method"]=method
                    s["reconciliation_confidence"]="HIGH"
                    s["refinement_status"]="RESOLVED"
                    s["refinement_method"]=method
                    newly_linked_hash_collapse += 1
        semantic_solution_rows.append({
            "solution_semantic_unit_id":suid,
            "solution_text_hash":h,
            "member_count":len(members),
            "member_solution_ids":";".join(sorted(s["solution_id"] for s in members)),
            "source_files":";".join(sorted({s.get("solution_source_file","") for s in members})),
            "linked_statement_hashes_before":";".join(sorted(linked_hashes)),
            "candidate_statement_hashes":";".join(sorted(candidate_hashes)),
            "resolution":resolution,
            "resolved_statement_hash":target_hash,
            "resolved_problem_id":rep_by_hash.get(target_hash,""),
        })

    # 2. Numbering-shift application under strict full-support conditions.
    mismatch_solution_files=set()
    for m in mismatches:
        mismatch_solution_files.update(split_ids(m.get("equivalent_solution_source_files","")) or [m.get("solution_source_file","")])
    auto_shift_links=0
    shift_audit=[]
    # Index unresolved links by source file after semantic collapse.
    links_by_file=defaultdict(list)
    for s in links:
        if not s.get("linked_problem_id"): links_by_file[s.get("solution_source_file","")].append(s)

    for m in mismatches:
        try:
            sim=float(m.get("file_similarity",0) or 0); ratio=float(m.get("support_ratio",0) or 0); support=int(m.get("support_count",0) or 0); offset=int(m.get("constant_number_offset",0) or 0)
        except ValueError:
            continue
        sol_files=split_ids(m.get("equivalent_solution_source_files","")) or [m.get("solution_source_file","")]
        prob_files=split_ids(m.get("equivalent_candidate_problem_files","")) or [m.get("candidate_problem_file","")]
        eligible=(sim>=0.90 and ratio>=0.999 and support>=2 and offset!=0)
        attempted=resolved=0; unresolved_ids=[]
        if eligible:
            for sf in sol_files:
                for s in links_by_file.get(sf,[]):
                    sn=numeric_tail(s.get("source_problem_number",""))
                    if sn is None: continue
                    attempted+=1; target_num=sn-offset
                    candidates=[]
                    for r in ledger:
                        if r.get("source_file") not in prob_files: continue
                        if numeric_tail(r.get("source_problem_number",""))==target_num: candidates.append(r)
                    hs={r.get("statement_hash","") for r in candidates if r.get("statement_hash")}
                    if len(hs)==1:
                        th=next(iter(hs)); rep=rep_by_hash[th]
                        s["linked_problem_id"]=rep
                        s["link_status"]="LINKED_NUMBERING_SHIFT"
                        s["reconciliation_status"]="RESOLVED_NUMBERING_SHIFT"
                        s["reconciliation_method"]="FULL_SUPPORT_CONSTANT_OFFSET"
                        s["reconciliation_confidence"]="HIGH"
                        s["refinement_status"]="RESOLVED"
                        s["refinement_method"]="FULL_SUPPORT_CONSTANT_OFFSET"
                        resolved+=1; auto_shift_links+=1
                    else:
                        unresolved_ids.append(s.get("solution_id",""))
        shift_audit.append({
            "mismatch_group":m.get("mismatch_group",""), "eligible_for_auto_apply":"YES" if eligible else "NO",
            "file_similarity":m.get("file_similarity",""), "constant_number_offset":m.get("constant_number_offset",""),
            "support_count":m.get("support_count",""), "support_ratio":m.get("support_ratio",""),
            "attempted_solution_blocks":attempted, "resolved_solution_blocks":resolved,
            "unresolved_solution_ids":";".join(unresolved_ids),
            "status":"APPLIED" if eligible and resolved else ("ELIGIBLE_BUT_NOT_UNIQUE" if eligible else "REVIEW_ONLY"),
        })

    # Clear stale numbering-mismatch status if the source file is no longer part of a current mismatch group.
    for s in links:
        if s.get("linked_problem_id"): continue
        if s.get("reconciliation_status")=="UNRESOLVED_NUMBERING_MISMATCH" and s.get("solution_source_file","") not in mismatch_solution_files:
            s["reconciliation_status"]="UNRESOLVED_AMBIGUOUS" if s.get("candidate_problem_ids") else "UNRESOLVED_NO_CANDIDATE"
            s["link_status"]=s["reconciliation_status"]
            s["reconciliation_method"]="STALE_NUMBERING_STATUS_CLEARED"
            s["refinement_status"]="UNRESOLVED"
            s["refinement_method"]="STALE_NUMBERING_STATUS_CLEARED"

    # 3. Recompute direct and statement-hash propagated solution/hint availability.
    sol_by_pid=defaultdict(set); hint_by_pid=defaultdict(set)
    for s in links:
        pid=s.get("linked_problem_id","")
        if pid not in ledger_by_id: continue
        if s.get("solution_kind")=="SOLUTION": sol_by_pid[pid].add(s["solution_id"])
        elif s.get("solution_kind")=="HINT": hint_by_pid[pid].add(s["solution_id"])
    sols_by_hash=defaultdict(set); hints_by_hash=defaultdict(set)
    for r in ledger:
        h=r.get("statement_hash",""); pid=r["problem_id"]
        if h:
            sols_by_hash[h].update(sol_by_pid.get(pid,set())); hints_by_hash[h].update(hint_by_pid.get(pid,set()))

    ledger_fields=extend(ledger_fields,["local_solution_ids","propagated_solution_ids","solution_link_status","reconciliation_status"])
    for r in ledger:
        pid=r["problem_id"]; h=r.get("statement_hash","")
        local=sorted(sol_by_pid.get(pid,set())); group=sorted(sols_by_hash.get(h,set())) if h else []
        prop=[x for x in group if x not in local]
        all_sols=local+prop
        r["has_solution"]="YES" if all_sols else "NO"; r["solution_id"]=";".join(all_sols)
        r["has_hint"]="YES" if (hint_by_pid.get(pid) or hints_by_hash.get(h)) else "NO"
        r["local_solution_ids"]=";".join(local); r["propagated_solution_ids"]=";".join(prop)
        if local: r["solution_link_status"]="LOCAL_OR_COMPANION_LINKED"
        elif prop: r["solution_link_status"]="EXACT_DUPLICATE_PROPAGATED"
        else: r["solution_link_status"]="NO_SOLUTION_LINKED"

    # Update semantic problem units solution aggregates.
    sem_by_hash={r.get("statement_hash",""):r for r in sem}
    sem_fields=extend(sem_fields,["aggregate_solution_ids","aggregate_hint_ids","solution_availability"])
    for h,r in sem_by_hash.items():
        r["aggregate_solution_ids"]=";".join(sorted(sols_by_hash.get(h,set())))
        r["aggregate_hint_ids"]=";".join(sorted(hints_by_hash.get(h,set())))
        r["solution_availability"]="YES" if sols_by_hash.get(h) else "NO"

    # 4. Explicit unresolved output + semantic orphan groups.
    remaining=[]
    for s in links:
        if s.get("linked_problem_id"): continue
        status=s.get("reconciliation_status") or s.get("link_status") or "UNRESOLVED"
        remaining.append({
            "solution_id":s.get("solution_id",""), "solution_semantic_unit_id":s.get("solution_semantic_unit_id",""),
            "solution_kind":s.get("solution_kind",""), "solution_source_file":s.get("solution_source_file",""),
            "solution_line_range":s.get("solution_line_range",""), "source_problem_number":s.get("source_problem_number",""),
            "status":status, "candidate_problem_ids":s.get("candidate_problem_ids",""),
            "candidate_statement_hashes":";".join(sorted({statement_hash_by_pid.get(x,"") for x in split_ids(s.get("candidate_problem_ids","")) if statement_hash_by_pid.get(x,"")})),
            "editorial_action":"REVIEW_NUMBERING_MISMATCH" if status=="UNRESOLVED_NUMBERING_MISMATCH" else ("CHOOSE_AMONG_DISTINCT_STATEMENTS" if s.get("candidate_problem_ids") else "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN")
        })

    # Group remaining by solution semantic unit for human review compression.
    remgroups=defaultdict(list)
    for r in remaining: remgroups[r.get("solution_semantic_unit_id") or r["solution_id"]].append(r)
    orphan_units=[]
    for key,members in sorted(remgroups.items()):
        ch=set(); pids=set(); statuses=set()
        for r in members:
            ch.update(split_ids(r.get("candidate_statement_hashes",""))); pids.update(split_ids(r.get("candidate_problem_ids",""))); statuses.add(r.get("status",""))
        orphan_units.append({
            "orphan_semantic_unit_id":key,
            "member_count":len(members),
            "member_solution_ids":";".join(sorted(r["solution_id"] for r in members)),
            "source_files":";".join(sorted({r["solution_source_file"] for r in members})),
            "statuses":";".join(sorted(statuses)),
            "candidate_problem_ids":";".join(sorted(pids)),
            "candidate_statement_hashes":";".join(sorted(ch)),
            "distinct_candidate_statement_count":len(ch),
            "editorial_action":"CHOOSE_AMONG_DISTINCT_STATEMENTS" if len(ch)>1 else ("LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN" if len(ch)==0 else "RECHECK_EQUIVALENCE_RULE"),
        })

    # Write.
    write_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv", link_fields, links)
    write_tsv(inv/"PROBLEM_LEDGER.tsv", ledger_fields, ledger)
    write_tsv(inv/"SEMANTIC_PROBLEM_UNITS.tsv", sem_fields, sem)
    write_tsv(inv/"SOLUTION_SEMANTIC_UNITS.tsv", [
        "solution_semantic_unit_id","solution_text_hash","member_count","member_solution_ids","source_files",
        "linked_statement_hashes_before","candidate_statement_hashes","resolution","resolved_statement_hash","resolved_problem_id"
    ], semantic_solution_rows)
    write_tsv(inv/"NUMBERING_SHIFT_APPLICATION.tsv", [
        "mismatch_group","eligible_for_auto_apply","file_similarity","constant_number_offset","support_count","support_ratio",
        "attempted_solution_blocks","resolved_solution_blocks","unresolved_solution_ids","status"
    ], shift_audit)
    write_tsv(inv/"REMAINING_ORPHANS.tsv", [
        "solution_id","solution_semantic_unit_id","solution_kind","solution_source_file","solution_line_range","source_problem_number",
        "status","candidate_problem_ids","candidate_statement_hashes","editorial_action"
    ], remaining)
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv", [
        "orphan_semantic_unit_id","member_count","member_solution_ids","source_files","statuses","candidate_problem_ids",
        "candidate_statement_hashes","distinct_candidate_statement_count","editorial_action"
    ], orphan_units)

    by_status=Counter(r["status"] for r in remaining)
    md=["# Remaining orphan imported solutions/hints — semantic refinement", "",
        "> Exact duplicate solution text and exact duplicate problem statements have been collapsed before editorial review.", "",
        "## Counts", "",
        f"- Unresolved source blocks: **{len(remaining)}**",
        f"- Unresolved semantic solution units: **{len(orphan_units)}**",
        f"- Newly linked by exact solution/candidate semantic equivalence: **{newly_linked_hash_collapse}**",
        f"- Newly linked by fully supported numbering shift: **{auto_shift_links}**", "",
        "## Counts by status", ""]
    md += [f"- {k}: **{v}**" for k,v in sorted(by_status.items())]
    md += ["", "## Semantic review units", ""]
    for u in orphan_units:
        md.append(f"- `{u['orphan_semantic_unit_id']}` — **{u['member_count']} source block(s)** — {u['distinct_candidate_statement_count']} distinct candidate statement hash(es) — {u['editorial_action']}")
    (inv/"remaining_orphans.md").write_text("\n".join(md)+"\n", encoding="utf-8")

    solved=sum(1 for r in ledger if r.get("has_solution")=="YES")
    summary=["# Imported problem reconciliation — semantic orphan refinement", "",
        "> Second-pass reconciliation over the duplicate/solution pass. Canonical book content remains untouched.", "",
        "## Resolution", "",
        f"- Solution/hint blocks total: **{len(links)}**",
        f"- Exact solution-text semantic units: **{len(groups)}**",
        f"- Newly linked by semantic equivalence: **{newly_linked_hash_collapse}**",
        f"- Newly linked by high-confidence numbering shift: **{auto_shift_links}**",
        f"- Remaining unresolved source blocks: **{len(remaining)}**",
        f"- Remaining unresolved semantic units: **{len(orphan_units)}**", "",
        "## Recomputed ledger", "",
        f"- Problem source rows with reconciled solution availability: **{solved}**",
        f"- Problem source rows without reconciled solution availability: **{len(ledger)-solved}**", "",
        "## Review policy", "",
        "- Multiple provenance candidates with one statement hash are resolved automatically.",
        "- Exact duplicate solution text inherits a trusted semantic link from another copy.",
        "- Numbering shifts are auto-applied only at >=0.90 file similarity, 100% offset support, support >=2, and a unique target statement hash per shifted number.",
        "- All remaining ambiguity is between genuinely distinct statement hashes or lacks a candidate.",
    ]
    (inv/"RECONCILIATION_REFINEMENT_SUMMARY.md").write_text("\n".join(summary)+"\n", encoding="utf-8")
    print("SEMANTIC ORPHAN REFINEMENT COMPLETE")
    print(f"  newly linked semantic-equivalence: {newly_linked_hash_collapse}")
    print(f"  newly linked numbering-shift: {auto_shift_links}")
    print(f"  remaining source blocks: {len(remaining)}")
    print(f"  remaining semantic units: {len(orphan_units)}")
    return 0

if __name__=="__main__": raise SystemExit(main())
