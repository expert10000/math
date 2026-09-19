#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv
from collections import defaultdict, Counter
from pathlib import Path

DECISIONS = {
    # Exact/defensible semantic links from the reviewed Tier-2 packet.
    "SOLSEM-77DFFE6671A1": {
        "decision": "ACCEPT",
        "target_problem_id": "IMP-DL-E1F1BB4192-P011",
        "candidate_rank": "2",
        "note": "Solution constructs a minimal free resolution inductively; candidate 2 is the explicit minimal-resolution existence problem."
    },
    "SOLSEM-510F83E5FDD3": {
        "decision": "ACCEPT",
        "target_problem_id": "IMP-DL-9DE2876887-P002",
        "candidate_rank": "1",
        "note": "Solution proves the meromorphic-at-infinity/rational-function part of the displayed two-part problem."
    },

    # These are reader-facing exposition/support proofs, not dossier problems needing linkage.
    "SOLSEM-33A097330A55": {
        "decision": "NOT_A_PROBLEM",
        "target_problem_id": "",
        "candidate_rank": "",
        "note": "Answer-like summary after the chapter conclusion; no actual problem statement precedes it."
    },
    "SOLSEM-F23AA3472752": {
        "decision": "NOT_A_PROBLEM",
        "target_problem_id": "",
        "candidate_rank": "",
        "note": "Proof of the proposition that submodules of finitely generated modules over Noetherian rings are finitely generated; support theorem/proof, not a problem."
    },

    # The exact statement exists, but the current scanner did not isolate it as a clean problem row.
    "SOLSEM-8BD310C9A992": {
        "decision": "NEEDS_STRUCTURAL_RESCAN",
        "target_problem_id": "",
        "candidate_rank": "",
        "note": "Exact local question compares quotients by distinct real linear factors with irreducible real quadratics; current top candidate is a later oversized base-change block."
    },
    "SOLSEM-F0C1695725CA": {
        "decision": "NEEDS_STRUCTURAL_RESCAN",
        "target_problem_id": "",
        "candidate_rank": "",
        "note": "Exact Exercise 9.3 is present locally, but it is swallowed by an oversized multi-exercise problem row."
    },
    "SOLSEM-94664AFC5677": {
        "decision": "NEEDS_STRUCTURAL_RESCAN",
        "target_problem_id": "",
        "candidate_rank": "",
        "note": "Exact local question asks why k[s,t]/(s-a,t-b) is k rather than k×k; current candidate is a later explanatory example, not the original statement."
    },
    "SOLSEM-DE60695D66E5": {
        "decision": "NEEDS_STRUCTURAL_RESCAN",
        "target_problem_id": "",
        "candidate_rank": "",
        "note": "Solution is Part (c), vanishing of Ext maps for a minimal exact sequence; the exact Part (c) theorem is not represented by the current top-three candidates."
    },
    "SOLSEM-7723F82AC385": {
        "decision": "NEEDS_STRUCTURAL_RESCAN",
        "target_problem_id": "",
        "candidate_rank": "",
        "note": "Exact PV integral problem immediately precedes its solution, but the scanner missed it; all ranked candidates are different problems."
    },
}

TERMINAL_NONPROBLEM = {"RESOLVED_NOT_A_PROBLEM"}

def read_tsv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]

def write_tsv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k:row.get(k,"") for k in fields})

def extend(fields, extras):
    out=list(fields)
    for x in extras:
        if x not in out: out.append(x)
    return out

def split_ids(s):
    return [x for x in (s or "").split(";") if x]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--apply", action="store_true")
    args=ap.parse_args()
    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"

    df, decisions=read_tsv(inv/"ORPHAN_SEMANTIC_REVIEW_DECISIONS.tsv")
    rf, rankings=read_tsv(inv/"ORPHAN_SEMANTIC_CANDIDATE_RANKINGS.tsv")
    of, orphan_units=read_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv")
    lf, links=read_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv")
    pf, ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")
    sf, sem=read_tsv(inv/"SEMANTIC_PROBLEM_UNITS.tsv")

    dby={r["orphan_semantic_unit_id"]:r for r in decisions}
    oby={r["orphan_semantic_unit_id"]:r for r in orphan_units}
    lby={r["solution_id"]:r for r in links}
    pby={r["problem_id"]:r for r in ledger}

    rank_by=defaultdict(dict)
    for r in rankings:
        rank_by[r["orphan_semantic_unit_id"]][r.get("rank","")]=r

    errors=[]
    audit=[]
    rescan=[]
    nonproblem=[]

    for uid,choice in DECISIONS.items():
        if uid not in oby:
            errors.append(f"{uid}: no longer present in ORPHAN_SEMANTIC_UNITS.tsv")
            continue
        mids=split_ids(oby[uid].get("member_solution_ids",""))
        members=[lby[x] for x in mids if x in lby]
        if len(members)!=len(mids):
            errors.append(f"{uid}: member solution IDs missing")
            continue
        if any(m.get("linked_problem_id") for m in members):
            errors.append(f"{uid}: already linked; refusing stale Tier-2 decision")
            continue

        target=choice["target_problem_id"]
        if choice["decision"]=="ACCEPT":
            if target not in pby:
                errors.append(f"{uid}: target problem {target} missing")
                continue
            rr=rank_by.get(uid,{}).get(choice["candidate_rank"])
            if not rr or rr.get("representative_problem_id")!=target:
                errors.append(f"{uid}: reviewed candidate rank/target changed")
                continue

        row={
            "orphan_semantic_unit_id":uid,
            "decision":choice["decision"],
            "candidate_rank":choice["candidate_rank"],
            "target_problem_id":target,
            "member_solution_count":len(members),
            "member_solution_ids":";".join(mids),
            "note":choice["note"],
            "apply_status":"PENDING" if not args.apply else "APPLIED",
        }
        audit.append(row)
        if choice["decision"]=="NEEDS_STRUCTURAL_RESCAN":
            rescan.append(row.copy())
        elif choice["decision"]=="NOT_A_PROBLEM":
            nonproblem.append(row.copy())

    write_tsv(inv/"TIER2_EDITORIAL_RESOLUTION_PLAN.tsv",
              ["orphan_semantic_unit_id","decision","candidate_rank","target_problem_id",
               "member_solution_count","member_solution_ids","note","apply_status"], audit)
    write_tsv(inv/"STRUCTURAL_RESCAN_QUEUE.tsv",
              ["orphan_semantic_unit_id","decision","candidate_rank","target_problem_id",
               "member_solution_count","member_solution_ids","note","apply_status"], rescan)
    write_tsv(inv/"NONPROBLEM_SOLUTION_BLOCKS.tsv",
              ["orphan_semantic_unit_id","decision","candidate_rank","target_problem_id",
               "member_solution_count","member_solution_ids","note","apply_status"], nonproblem)

    md=["# Tier-2 editorial resolution plan","",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- Decisions: **{len(audit)}**",
        f"- Validation errors: **{len(errors)}**",""]
    for r in audit:
        md += [f"## {r['orphan_semantic_unit_id']}",
               f"- Decision: **{r['decision']}**",
               f"- Target: `{r['target_problem_id'] or '—'}`",
               f"- Source solution blocks: **{r['member_solution_count']}**",
               f"- Note: {r['note']}",""]
    if errors:
        md += ["## Errors",""]+[f"- {e}" for e in errors]
    (inv/"TIER2_EDITORIAL_RESOLUTION_PLAN.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    if errors:
        print("TIER2 EDITORIAL VALIDATION FAILED")
        for e in errors: print(" -",e)
        return 1
    if not args.apply:
        print("TIER2 EDITORIAL DRY RUN PASSED: accept=2 not_a_problem=2 structural_rescan=5")
        return 0

    lf=extend(lf,["editorial_resolution_status","editorial_resolution_method","editorial_note"])
    accepted_blocks=0; nonproblem_blocks=0; rescan_blocks=0
    for uid,choice in DECISIONS.items():
        mids=split_ids(oby[uid].get("member_solution_ids",""))
        for sid in mids:
            s=lby[sid]
            s["editorial_note"]=choice["note"]
            if choice["decision"]=="ACCEPT":
                s["linked_problem_id"]=choice["target_problem_id"]
                s["link_status"]="LINKED_EDITORIAL_TIER2"
                s["reconciliation_status"]="RESOLVED_EDITORIAL_TIER2"
                s["reconciliation_method"]="TIER2_MANUAL_CONTENT_REVIEW"
                s["reconciliation_confidence"]="HIGH"
                s["editorial_resolution_status"]="APPLIED_LINK"
                s["editorial_resolution_method"]="TIER2_MANUAL_CONTENT_REVIEW"
                accepted_blocks+=1
            elif choice["decision"]=="NOT_A_PROBLEM":
                s["reconciliation_status"]="RESOLVED_NOT_A_PROBLEM"
                s["reconciliation_method"]="TIER2_MANUAL_CONTENT_REVIEW"
                s["reconciliation_confidence"]="HIGH"
                s["editorial_resolution_status"]="TERMINAL_NONPROBLEM"
                s["editorial_resolution_method"]="TIER2_MANUAL_CONTENT_REVIEW"
                nonproblem_blocks+=1
            elif choice["decision"]=="NEEDS_STRUCTURAL_RESCAN":
                s["reconciliation_status"]="NEEDS_STRUCTURAL_RESCAN"
                s["reconciliation_method"]="TIER2_MANUAL_CONTENT_REVIEW"
                s["reconciliation_confidence"]="HIGH"
                s["editorial_resolution_status"]="QUEUED_STRUCTURAL_RESCAN"
                s["editorial_resolution_method"]="TIER2_MANUAL_CONTENT_REVIEW"
                rescan_blocks+=1

    # Recompute ledger solution availability, propagated across exact statement hashes.
    ledger_by_id={r["problem_id"]:r for r in ledger}
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
            sols_by_hash[h].update(sol_by_pid.get(pid,set()))
            hints_by_hash[h].update(hint_by_pid.get(pid,set()))

    pf=extend(pf,["local_solution_ids","propagated_solution_ids","solution_link_status"])
    for r in ledger:
        pid=r["problem_id"]; h=r.get("statement_hash","")
        local=sorted(sol_by_pid.get(pid,set()))
        group=sorted(sols_by_hash.get(h,set())) if h else []
        prop=[x for x in group if x not in local]
        allsol=local+prop
        r["has_solution"]="YES" if allsol else "NO"
        r["solution_id"]=";".join(allsol)
        r["has_hint"]="YES" if (hint_by_pid.get(pid) or hints_by_hash.get(h)) else "NO"
        r["local_solution_ids"]=";".join(local)
        r["propagated_solution_ids"]=";".join(prop)
        r["solution_link_status"]="LOCAL_OR_COMPANION_LINKED" if local else ("EXACT_DUPLICATE_PROPAGATED" if prop else "NO_SOLUTION_LINKED")

    sf=extend(sf,["aggregate_solution_ids","aggregate_hint_ids","solution_availability"])
    for r in sem:
        h=r.get("statement_hash","")
        r["aggregate_solution_ids"]=";".join(sorted(sols_by_hash.get(h,set())))
        r["aggregate_hint_ids"]=";".join(sorted(hints_by_hash.get(h,set())))
        r["solution_availability"]="YES" if sols_by_hash.get(h) else "NO"

    # Remaining unresolved source blocks: exclude terminal non-problem resolutions,
    # retain structural-rescan blocks explicitly.
    stmt_hash_by_pid={r["problem_id"]:r.get("statement_hash","") for r in ledger}
    remaining=[]
    for s in links:
        if s.get("linked_problem_id"): continue
        status=s.get("reconciliation_status") or s.get("link_status") or "UNRESOLVED"
        if status in TERMINAL_NONPROBLEM:
            continue
        cand=split_ids(s.get("candidate_problem_ids",""))
        hashes=sorted({stmt_hash_by_pid.get(x,"") for x in cand if stmt_hash_by_pid.get(x,"")})
        remaining.append({
            "solution_id":s.get("solution_id",""),
            "solution_semantic_unit_id":s.get("solution_semantic_unit_id",""),
            "solution_kind":s.get("solution_kind",""),
            "solution_source_file":s.get("solution_source_file",""),
            "solution_line_range":s.get("solution_line_range",""),
            "source_problem_number":s.get("source_problem_number",""),
            "status":status,
            "candidate_problem_ids":s.get("candidate_problem_ids",""),
            "candidate_statement_hashes":";".join(hashes),
            "editorial_action":"STRUCTURAL_RESCAN" if status=="NEEDS_STRUCTURAL_RESCAN" else
                               ("REVIEW_NUMBERING_MISMATCH" if status=="UNRESOLVED_NUMBERING_MISMATCH" else
                                ("CHOOSE_AMONG_DISTINCT_STATEMENTS" if cand else "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN"))
        })
    write_tsv(inv/"REMAINING_ORPHANS.tsv",
              ["solution_id","solution_semantic_unit_id","solution_kind","solution_source_file",
               "solution_line_range","source_problem_number","status","candidate_problem_ids",
               "candidate_statement_hashes","editorial_action"],remaining)

    groups=defaultdict(list)
    for r in remaining:
        groups[r.get("solution_semantic_unit_id") or r["solution_id"]].append(r)
    orphan_out=[]
    for key,members in sorted(groups.items()):
        hs=set(); pids=set(); statuses=set()
        for r in members:
            hs.update(split_ids(r["candidate_statement_hashes"]))
            pids.update(split_ids(r["candidate_problem_ids"]))
            statuses.add(r["status"])
        action="STRUCTURAL_RESCAN" if "NEEDS_STRUCTURAL_RESCAN" in statuses else (
            "CHOOSE_AMONG_DISTINCT_STATEMENTS" if len(hs)>1 else
            ("LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN" if len(hs)==0 else "RECHECK_EQUIVALENCE_RULE"))
        orphan_out.append({
            "orphan_semantic_unit_id":key,
            "member_count":len(members),
            "member_solution_ids":";".join(sorted(r["solution_id"] for r in members)),
            "source_files":";".join(sorted({r["solution_source_file"] for r in members})),
            "statuses":";".join(sorted(statuses)),
            "candidate_problem_ids":";".join(sorted(pids)),
            "candidate_statement_hashes":";".join(sorted(hs)),
            "distinct_candidate_statement_count":len(hs),
            "editorial_action":action,
        })
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv",
              ["orphan_semantic_unit_id","member_count","member_solution_ids","source_files","statuses",
               "candidate_problem_ids","candidate_statement_hashes","distinct_candidate_statement_count","editorial_action"],orphan_out)

    write_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv",lf,links)
    write_tsv(inv/"PROBLEM_LEDGER.tsv",pf,ledger)
    write_tsv(inv/"SEMANTIC_PROBLEM_UNITS.tsv",sf,sem)

    applied=[dict(r,apply_status="APPLIED") for r in audit]
    write_tsv(inv/"TIER2_EDITORIAL_RESOLUTION_AUDIT.tsv",
              ["orphan_semantic_unit_id","decision","candidate_rank","target_problem_id",
               "member_solution_count","member_solution_ids","note","apply_status"],applied)

    bystatus=Counter(r["status"] for r in remaining)
    sm=["# Tier-2 editorial reconciliation — applied","",
        "- Accepted semantic links: **2 units**",
        f"- Accepted source solution blocks: **{accepted_blocks}**",
        "- Terminal non-problem/support units: **2**",
        f"- Terminal non-problem source blocks: **{nonproblem_blocks}**",
        "- Structural-rescan units queued: **5**",
        f"- Structural-rescan source blocks: **{rescan_blocks}**",
        f"- Remaining unresolved semantic units: **{len(orphan_out)}**",
        f"- Remaining unresolved source blocks: **{len(remaining)}**","",
        "## Remaining by status",""]
    sm += [f"- {k}: **{v}**" for k,v in sorted(bystatus.items())]
    (inv/"TIER2_EDITORIAL_RESOLUTION_SUMMARY.md").write_text("\n".join(sm)+"\n",encoding="utf-8")
    print(f"TIER2 EDITORIAL APPLIED: linked_units=2 nonproblem_units=2 structural_rescan_units=5 remaining_units={len(orphan_out)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
