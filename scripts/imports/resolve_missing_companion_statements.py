#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv
from collections import defaultdict
from pathlib import Path

DECISIONS = {
    "SOLSEM-32533806C6A4": {
        "source_number": "4.1",
        "member_solution_ids": [
            "IMP-DL-AE41E61130-S001",
            "IMP-M2-22F064D6B8-S001",
        ],
        "reason": "No matching Exercise 4.1 statement was found in the imported statement corpus. Ranked hits are examples or mathematically adjacent exercises, not the source statement.",
    },
    "SOLSEM-561D796840F3": {
        "source_number": "4.2",
        "member_solution_ids": [
            "IMP-DL-AE41E61130-S002",
            "IMP-M2-22F064D6B8-S002",
        ],
        "reason": "No matching Exercise 4.2 statement was found in the imported statement corpus. Ranked hits are unrelated despite lexical overlap.",
    },
    "SOLSEM-8C64B3E5FE56": {
        "source_number": "4.3",
        "member_solution_ids": [
            "IMP-DL-AE41E61130-S003",
            "IMP-M2-22F064D6B8-S003",
        ],
        "reason": "No matching Exercise 4.3 refinement/upper-lower-sum statement was found in the imported statement corpus.",
    },
    "SOLSEM-C8093323C4B4": {
        "source_number": "4.4",
        "member_solution_ids": [
            "IMP-DL-AE41E61130-S004",
            "IMP-M2-22F064D6B8-S004",
        ],
        "reason": "No matching Exercise 4.4 finite-set characteristic-function statement was found. Nearby indicator-function examples are not the exercise statement.",
    },
}

TERMINAL_STATUSES = {
    "RESOLVED_NOT_A_PROBLEM",
    "MISSING_COMPANION_STATEMENT",
}

def read_tsv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]

def write_tsv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t",
                           lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})

def extend(fields, extras):
    out = list(fields)
    for e in extras:
        if e not in out:
            out.append(e)
    return out

def split_ids(s):
    return [x for x in (s or "").split(";") if x]

def rebuild_remaining_orphans(links, ledger):
    statement_hash_by_pid = {r["problem_id"]: r.get("statement_hash","") for r in ledger}
    remaining = []
    for s in links:
        if s.get("linked_problem_id"):
            continue
        status = s.get("reconciliation_status") or s.get("link_status") or "UNRESOLVED"
        if status in TERMINAL_STATUSES:
            continue
        pids = split_ids(s.get("candidate_problem_ids",""))
        hashes = sorted({
            statement_hash_by_pid.get(pid,"")
            for pid in pids
            if statement_hash_by_pid.get(pid,"")
        })
        if status == "NEEDS_STRUCTURAL_RESCAN":
            action = "STRUCTURAL_RESCAN"
        elif status == "NEEDS_POST_SPLIT_RECONCILIATION":
            action = "RELINK_AFTER_SAFE_STRUCTURAL_SPLIT"
        elif status == "UNRESOLVED_NUMBERING_MISMATCH":
            action = "REVIEW_NUMBERING_MISMATCH"
        elif pids:
            action = "CHOOSE_AMONG_DISTINCT_STATEMENTS"
        else:
            action = "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN"
        remaining.append({
            "solution_id": s.get("solution_id",""),
            "solution_semantic_unit_id": s.get("solution_semantic_unit_id",""),
            "solution_kind": s.get("solution_kind",""),
            "solution_source_file": s.get("solution_source_file",""),
            "solution_line_range": s.get("solution_line_range",""),
            "source_problem_number": s.get("source_problem_number",""),
            "status": status,
            "candidate_problem_ids": s.get("candidate_problem_ids",""),
            "candidate_statement_hashes": ";".join(hashes),
            "editorial_action": action,
        })

    groups = defaultdict(list)
    for r in remaining:
        key = r.get("solution_semantic_unit_id") or r["solution_id"]
        groups[key].append(r)

    units = []
    for key, members in sorted(groups.items()):
        hashes=set(); pids=set(); statuses=set(); actions=set()
        for r in members:
            hashes.update(split_ids(r.get("candidate_statement_hashes","")))
            pids.update(split_ids(r.get("candidate_problem_ids","")))
            statuses.add(r.get("status",""))
            actions.add(r.get("editorial_action",""))
        if "RELINK_AFTER_SAFE_STRUCTURAL_SPLIT" in actions:
            action="RELINK_AFTER_SAFE_STRUCTURAL_SPLIT"
        elif "STRUCTURAL_RESCAN" in actions:
            action="STRUCTURAL_RESCAN"
        elif len(hashes)>1:
            action="CHOOSE_AMONG_DISTINCT_STATEMENTS"
        elif len(hashes)==0:
            action="LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN"
        else:
            action="RECHECK_EQUIVALENCE_RULE"
        units.append({
            "orphan_semantic_unit_id": key,
            "member_count": len(members),
            "member_solution_ids": ";".join(sorted(r["solution_id"] for r in members)),
            "source_files": ";".join(sorted({r["solution_source_file"] for r in members})),
            "statuses": ";".join(sorted(statuses)),
            "candidate_problem_ids": ";".join(sorted(pids)),
            "candidate_statement_hashes": ";".join(sorted(hashes)),
            "distinct_candidate_statement_count": len(hashes),
            "editorial_action": action,
        })
    return remaining, units

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()

    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"

    required = [
        inv/"PROBLEM_LEDGER.tsv",
        inv/"PROBLEM_SOLUTION_LINKS.tsv",
        inv/"COMPANION_STATEMENT_RECOVERY_DECISIONS.tsv",
    ]
    missing=[str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit("Missing required files:\n  " + "\n  ".join(missing))

    pfields, ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")
    lfields, links=read_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv")
    _, recovery=read_tsv(inv/"COMPANION_STATEMENT_RECOVERY_DECISIONS.tsv")

    rec_by_unit={r["solution_semantic_unit_id"]:r for r in recovery}
    link_by_id={r["solution_id"]:r for r in links}
    errors=[]
    audit=[]

    for unit,decision in DECISIONS.items():
        rr=rec_by_unit.get(unit)
        if not rr:
            errors.append(f"{unit}: missing from companion recovery decisions")
            continue

        members=decision["member_solution_ids"]
        actual=set(split_ids(rr.get("member_solution_ids","")))
        if actual != set(members):
            errors.append(f"{unit}: member solution set changed: {sorted(actual)}")
            continue

        for sid in members:
            s=link_by_id.get(sid)
            if not s:
                errors.append(f"{unit}: solution {sid} missing from link table")
                continue
            if s.get("linked_problem_id"):
                errors.append(f"{unit}: solution {sid} is already linked to {s.get('linked_problem_id')}")
            if (s.get("source_problem_number") or "").strip() != decision["source_number"]:
                errors.append(f"{unit}: {sid} source number changed")

        audit.append({
            "solution_semantic_unit_id":unit,
            "source_problem_number":decision["source_number"],
            "member_solution_count":len(members),
            "member_solution_ids":";".join(members),
            "companion_recovery_recommendation":rr.get("recommendation",""),
            "top_candidate_problem_id":rr.get("top_representative_problem_id",""),
            "top_candidate_source_file":rr.get("top_source_file",""),
            "top_score":rr.get("top_score",""),
            "margin":rr.get("margin",""),
            "editorial_disposition":"MISSING_COMPANION_STATEMENT",
            "reason":decision["reason"],
            "apply_status":"APPLIED" if args.apply else "PENDING",
        })

    afields=[
        "solution_semantic_unit_id","source_problem_number","member_solution_count",
        "member_solution_ids","companion_recovery_recommendation","top_candidate_problem_id",
        "top_candidate_source_file","top_score","margin","editorial_disposition",
        "reason","apply_status"
    ]
    write_tsv(inv/"MISSING_COMPANION_STATEMENT_PLAN.tsv",afields,audit)

    md=["# Missing companion statement resolution","",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- Semantic solution units: **{len(audit)}**",
        f"- Source solution blocks: **{sum(int(r['member_solution_count']) for r in audit)}**",
        f"- Validation errors: **{len(errors)}**",""]
    for r in audit:
        md += [
            f"## {r['solution_semantic_unit_id']} — Exercise {r['source_problem_number']}",
            f"- Disposition: **{r['editorial_disposition']}**",
            f"- Solution IDs: `{r['member_solution_ids']}`",
            f"- Highest-ranked corpus candidate: `{r['top_candidate_problem_id'] or '—'}`",
            f"- Reason: {r['reason']}",
            ""
        ]
    if errors:
        md += ["## Errors",""] + [f"- {e}" for e in errors]
    (inv/"MISSING_COMPANION_STATEMENT_PLAN.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    if errors:
        print("MISSING COMPANION STATEMENT VALIDATION FAILED")
        for e in errors:
            print(" -",e)
        return 1

    if not args.apply:
        print("MISSING COMPANION STATEMENT DRY RUN PASSED: units=4 blocks=8")
        return 0

    lfields=extend(lfields,[
        "previous_candidate_problem_ids",
        "editorial_resolution_status",
        "editorial_resolution_method",
        "editorial_note",
    ])

    changed=0
    for unit,decision in DECISIONS.items():
        for sid in decision["member_solution_ids"]:
            s=link_by_id[sid]
            if s.get("candidate_problem_ids"):
                s["previous_candidate_problem_ids"]=s.get("candidate_problem_ids","")
            s["candidate_problem_ids"]=""
            s["reconciliation_status"]="MISSING_COMPANION_STATEMENT"
            s["reconciliation_method"]="COMPANION_CORPUS_CONTENT_AUDIT"
            s["reconciliation_confidence"]="HIGH"
            s["editorial_resolution_status"]="TERMINAL_MISSING_STATEMENT"
            s["editorial_resolution_method"]="COMPANION_CORPUS_CONTENT_AUDIT"
            s["editorial_note"]=decision["reason"]
            s["link_status"]="UNLINKED_MISSING_STATEMENT"
            changed+=1

    remaining, units = rebuild_remaining_orphans(links, ledger)

    write_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv",lfields,links)
    write_tsv(inv/"MISSING_COMPANION_STATEMENTS.tsv",afields,
              [dict(r,apply_status="APPLIED") for r in audit])

    rem_fields=[
        "solution_id","solution_semantic_unit_id","solution_kind","solution_source_file",
        "solution_line_range","source_problem_number","status","candidate_problem_ids",
        "candidate_statement_hashes","editorial_action"
    ]
    unit_fields=[
        "orphan_semantic_unit_id","member_count","member_solution_ids","source_files",
        "statuses","candidate_problem_ids","candidate_statement_hashes",
        "distinct_candidate_statement_count","editorial_action"
    ]
    write_tsv(inv/"REMAINING_ORPHANS.tsv",rem_fields,remaining)
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv",unit_fields,units)

    summary=[
        "# Missing companion statements — applied",
        "",
        "- Semantic solution units resolved terminally: **4**",
        "- Duplicate/source solution blocks preserved: **8**",
        "- Forced problem links created: **0**",
        f"- Remaining active orphan source blocks: **{len(remaining)}**",
        f"- Remaining active orphan semantic units: **{len(units)}**",
        "",
        "The four Exercise 4.1–4.4 solution families remain preserved with full provenance, "
        "but are removed from active orphan ranking because the corresponding statements are "
        "not present in the imported corpus.",
    ]
    (inv/"MISSING_COMPANION_STATEMENT_SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")
    print(f"MISSING COMPANION STATEMENTS APPLIED: units=4 blocks={changed} remaining_units={len(units)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
