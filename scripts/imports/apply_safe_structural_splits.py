#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import shutil
import re
from collections import defaultdict, Counter
from pathlib import Path

LINE_RANGE_RE = re.compile(r"L?(\d+)\s*-\s*L?(\d+)")

# Fields that must not be inherited blindly from the oversized parent.
RESET_VALUES = {
    "duplicate_group": "",
    "canonical_match_type": "UNREVIEWED",
    "canonical_problem_id": "",
    "canonical_volume": "",
    "canonical_chapter": "",
    "target_volume": "UNCLASSIFIED",
    "target_chapter": "UNCLASSIFIED",
    "target_section": "UNCLASSIFIED",
    "mapping_confidence": "UNCLASSIFIED",
    "migration_status": "UNREVIEWED",
    "migration_commit": "",
    "review_status": "NEEDS_EDITORIAL_REVIEW",
    "has_hint": "NO",
    "has_solution": "NO",
    "solution_id": "",
    "local_solution_ids": "",
    "propagated_solution_ids": "",
    "solution_link_status": "NO_SOLUTION_LINKED",
}

def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]

def write_tsv(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=fields,
            delimiter="\t",
            lineterminator="\n",
            extrasaction="ignore",
        )
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})

def extend(fields, extras):
    out = list(fields)
    for x in extras:
        if x not in out:
            out.append(x)
    return out

def parse_range(s):
    m = LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)), int(m.group(2))) if m else None

def split_ids(s):
    return [x for x in (s or "").split(";") if x]

def generated_problem_id(candidate):
    rr = parse_range(candidate["proposed_line_range"])
    start = rr[0] if rr else 0
    sid = candidate.get("source_id") or "IMP"
    return f"{sid}-R{start:06d}-{candidate['statement_hash'][:8].upper()}"

def solution_start(row):
    rr = parse_range(row.get("solution_line_range", ""))
    return rr[0] if rr else None

def unique_number_match(link, children):
    num = (link.get("source_problem_number") or "").strip()
    if not num:
        return None
    matches = [
        c for c in children
        if (c.get("source_problem_number") or "").strip() == num
    ]
    return matches[0] if len(matches) == 1 else None

def same_file_preceding_match(link, children, old_source_file):
    # Conservative locality rule:
    # solution must be in same file and fall after exactly one child and before
    # the next child marker.
    if link.get("solution_source_file", "") != old_source_file:
        return None
    s = solution_start(link)
    if s is None:
        return None

    cs = sorted(children, key=lambda c: parse_range(c["proposed_line_range"])[0])
    hits = []
    for i, c in enumerate(cs):
        a, b = parse_range(c["proposed_line_range"])
        next_a = parse_range(cs[i+1]["proposed_line_range"])[0] if i+1 < len(cs) else None
        if s > b and (next_a is None or s < next_a):
            hits.append(c)
    return hits[0] if len(hits) == 1 else None

def replace_candidate_parent_ids(candidate_string, child_map):
    out = []
    seen = set()
    for pid in split_ids(candidate_string):
        repl = child_map.get(pid, [pid])
        for x in repl:
            if x not in seen:
                out.append(x)
                seen.add(x)
    return ";".join(out)

def recompute_solution_flags(ledger, links):
    by_id = {r["problem_id"]: r for r in ledger}
    local_solutions = defaultdict(set)
    local_hints = defaultdict(set)

    for s in links:
        pid = s.get("linked_problem_id", "")
        if pid not in by_id:
            continue
        kind = (s.get("solution_kind") or "").upper()
        if kind == "SOLUTION":
            local_solutions[pid].add(s["solution_id"])
        elif kind == "HINT":
            local_hints[pid].add(s["solution_id"])

    sols_by_hash = defaultdict(set)
    hints_by_hash = defaultdict(set)
    for r in ledger:
        h = r.get("statement_hash", "")
        if not h:
            continue
        pid = r["problem_id"]
        sols_by_hash[h].update(local_solutions.get(pid, set()))
        hints_by_hash[h].update(local_hints.get(pid, set()))

    for r in ledger:
        pid = r["problem_id"]
        h = r.get("statement_hash", "")
        local = sorted(local_solutions.get(pid, set()))
        group = sorted(sols_by_hash.get(h, set())) if h else []
        propagated = [x for x in group if x not in local]
        all_solutions = local + propagated

        r["has_solution"] = "YES" if all_solutions else "NO"
        r["solution_id"] = ";".join(all_solutions)
        r["has_hint"] = "YES" if (local_hints.get(pid) or hints_by_hash.get(h)) else "NO"
        r["local_solution_ids"] = ";".join(local)
        r["propagated_solution_ids"] = ";".join(propagated)

        if local:
            r["solution_link_status"] = "LOCAL_OR_COMPANION_LINKED"
        elif propagated:
            r["solution_link_status"] = "EXACT_DUPLICATE_PROPAGATED"
        else:
            r["solution_link_status"] = "NO_SOLUTION_LINKED"

def rebuild_semantic_units(ledger):
    groups = defaultdict(list)
    for r in ledger:
        if r.get("statement_hash"):
            groups[r["statement_hash"]].append(r)

    rows = []
    for h, members in sorted(groups.items()):
        members = sorted(members, key=lambda r: r["problem_id"])
        rep = members[0]
        sols = sorted({
            x
            for r in members
            for x in split_ids(r.get("solution_id", ""))
        })
        hints = sorted({
            x
            for r in members
            for x in split_ids(r.get("hint_id", ""))
        })
        rows.append({
            "statement_hash": h,
            "semantic_problem_id": f"SEM-{h[:12].upper()}",
            "representative_problem_id": rep["problem_id"],
            "member_count": len(members),
            "member_problem_ids": ";".join(r["problem_id"] for r in members),
            "source_files": ";".join(sorted({r.get("source_file", "") for r in members})),
            "source_collections": ";".join(sorted({r.get("source_collection", "") for r in members})),
            "problem_types": ";".join(sorted({r.get("problem_type", "") for r in members if r.get("problem_type", "")})),
            "source_problem_numbers": ";".join(sorted({r.get("source_problem_number", "") for r in members if r.get("source_problem_number", "")})),
            "aggregate_solution_ids": ";".join(sols),
            "aggregate_hint_ids": ";".join(hints),
            "solution_availability": "YES" if sols else "NO",
            "review_status": "NEEDS_EDITORIAL_REVIEW",
        })
    return rows

def rebuild_remaining_orphans(links, ledger):
    statement_hash_by_pid = {
        r["problem_id"]: r.get("statement_hash", "")
        for r in ledger
    }
    remaining = []
    for s in links:
        if s.get("linked_problem_id"):
            continue

        status = (
            s.get("reconciliation_status")
            or s.get("link_status")
            or "UNRESOLVED"
        )

        # Explicit terminal support/nonproblem blocks are not open orphans.
        if status in {"RESOLVED_NOT_A_PROBLEM"}:
            continue

        pids = split_ids(s.get("candidate_problem_ids", ""))
        hashes = sorted({
            statement_hash_by_pid.get(pid, "")
            for pid in pids
            if statement_hash_by_pid.get(pid, "")
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
            "solution_id": s.get("solution_id", ""),
            "solution_semantic_unit_id": s.get("solution_semantic_unit_id", ""),
            "solution_kind": s.get("solution_kind", ""),
            "solution_source_file": s.get("solution_source_file", ""),
            "solution_line_range": s.get("solution_line_range", ""),
            "source_problem_number": s.get("source_problem_number", ""),
            "status": status,
            "candidate_problem_ids": s.get("candidate_problem_ids", ""),
            "candidate_statement_hashes": ";".join(hashes),
            "editorial_action": action,
        })

    groups = defaultdict(list)
    for r in remaining:
        key = r.get("solution_semantic_unit_id") or r["solution_id"]
        groups[key].append(r)

    units = []
    for key, members in sorted(groups.items()):
        hashes = set()
        pids = set()
        statuses = set()
        actions = set()

        for r in members:
            hashes.update(split_ids(r.get("candidate_statement_hashes", "")))
            pids.update(split_ids(r.get("candidate_problem_ids", "")))
            statuses.add(r.get("status", ""))
            actions.add(r.get("editorial_action", ""))

        if "RELINK_AFTER_SAFE_STRUCTURAL_SPLIT" in actions:
            action = "RELINK_AFTER_SAFE_STRUCTURAL_SPLIT"
        elif "STRUCTURAL_RESCAN" in actions:
            action = "STRUCTURAL_RESCAN"
        elif len(hashes) > 1:
            action = "CHOOSE_AMONG_DISTINCT_STATEMENTS"
        elif len(hashes) == 0:
            action = "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN"
        else:
            action = "RECHECK_EQUIVALENCE_RULE"

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
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    repo = args.repo.resolve()
    inv = repo / "imports" / "problem_inventory"

    qfields, quality = read_tsv(inv / "STRUCTURAL_SUPERSESSION_QUALITY_V3.tsv")
    cfields, candidates = read_tsv(inv / "STRUCTURAL_REBUILD_CANDIDATES_V3.tsv")
    pfields, ledger = read_tsv(inv / "PROBLEM_LEDGER.tsv")
    lfields, links = read_tsv(inv / "PROBLEM_SOLUTION_LINKS.tsv")

    safe_rows = [
        r for r in quality
        if r.get("repair_class") == "SAFE_SPLIT_PREVIEW"
    ]
    safe = {r["current_problem_id"]: r for r in safe_rows}

    # Locked expectations from the user's reviewed v3 result.
    EXPECTED_SAFE_CONTAINERS = 75
    EXPECTED_CHILDREN = 667

    errors = []
    if len(safe_rows) != EXPECTED_SAFE_CONTAINERS:
        errors.append(
            f"SAFE container count changed: expected {EXPECTED_SAFE_CONTAINERS}, got {len(safe_rows)}"
        )

    cand_by_id = {r["candidate_id"]: r for r in candidates}
    ledger_by_id = {r["problem_id"]: r for r in ledger}

    child_pairs_by_old = {}
    old_to_newids = {}
    all_new_ids = set()
    total_children = 0

    plan = []
    for oldid, q in safe.items():
        old = ledger_by_id.get(oldid)
        if not old:
            errors.append(f"{oldid}: current ledger row missing")
            continue

        cids = split_ids(q.get("child_candidate_ids", ""))
        children = []
        for cid in cids:
            c = cand_by_id.get(cid)
            if not c:
                errors.append(f"{oldid}: child candidate {cid} missing")
                continue

            if oldid not in split_ids(c.get("containing_current_problem_ids", "")):
                errors.append(
                    f"{oldid}: candidate {cid} is no longer contained by parent"
                )
            children.append(c)

        if len(children) < 2:
            errors.append(f"{oldid}: SAFE split has fewer than two child rows")
            continue

        # Re-check v3 safety criteria.
        spans = [int(c.get("line_span") or 0) for c in children]
        if any(x >= 250 for x in spans):
            errors.append(f"{oldid}: child >=250 lines found in SAFE split")
        if max(spans or [0]) >= 250:
            errors.append(f"{oldid}: max child span no longer safe")

        pairs = []
        newids = []
        for c in children:
            nid = generated_problem_id(c)
            if nid in all_new_ids:
                errors.append(f"{oldid}: duplicate generated child ID {nid}")
            if nid in ledger_by_id and nid != oldid:
                errors.append(f"{oldid}: generated child ID collides with existing ledger row {nid}")
            all_new_ids.add(nid)
            pairs.append((c, nid))
            newids.append(nid)

        child_pairs_by_old[oldid] = pairs
        old_to_newids[oldid] = newids
        total_children += len(pairs)

        plan.append({
            "current_problem_id": oldid,
            "source_file": old.get("source_file", ""),
            "current_line_range": old.get("source_line_range", ""),
            "current_line_span": q.get("current_line_span", ""),
            "child_count": len(pairs),
            "new_problem_ids": ";".join(newids),
            "child_line_ranges": ";".join(c["proposed_line_range"] for c, _ in pairs),
            "median_child_span": q.get("median_child_span", ""),
            "max_child_span": q.get("max_child_span", ""),
            "coverage_ratio": q.get("coverage_ratio", ""),
            "repair_class": q.get("repair_class", ""),
        })

    if total_children != EXPECTED_CHILDREN:
        errors.append(
            f"replacement child count changed: expected {EXPECTED_CHILDREN}, got {total_children}"
        )

    # Ensure no two safe parents overlap in the same physical source.
    parents_by_source = defaultdict(list)
    for oldid in safe:
        old = ledger_by_id.get(oldid)
        rr = parse_range(old.get("source_line_range", "")) if old else None
        if old and rr:
            parents_by_source[old.get("source_file", "")].append((oldid, rr))

    for src, rows in parents_by_source.items():
        rows = sorted(rows, key=lambda x: x[1][0])
        for i in range(len(rows)-1):
            a = rows[i]
            b = rows[i+1]
            if a[1][1] >= b[1][0]:
                errors.append(
                    f"{src}: overlapping SAFE parent rows {a[0]} and {b[0]}"
                )

    new_pfields = extend(
        pfields,
        [
            "structural_status",
            "supersedes_problem_id",
            "structural_repair_note",
        ],
    )
    new_lfields = extend(
        lfields,
        [
            "previous_linked_problem_id",
            "structural_relink_status",
            "structural_relink_method",
        ],
    )

    # Build repaired shadow ledger.
    shadow_ledger = []
    superseded_rows = []

    for r0 in ledger:
        oldid = r0["problem_id"]
        if oldid not in child_pairs_by_old:
            shadow_ledger.append(dict(r0))
            continue

        pairs = child_pairs_by_old[oldid]
        archived = dict(r0)
        archived["superseded_by_problem_ids"] = ";".join(nid for _, nid in pairs)
        archived["supersession_reason"] = "SAFE_STRUCTURAL_SPLIT_V3"
        superseded_rows.append(archived)

        for c, nid in pairs:
            nr = dict(r0)
            for k, v in RESET_VALUES.items():
                if k in nr or k in new_pfields:
                    nr[k] = v

            nr["problem_id"] = nid
            nr["source_id"] = c.get("source_id", nr.get("source_id", ""))
            nr["source_collection"] = c.get("source_collection", nr.get("source_collection", ""))
            nr["source_file"] = c.get("source_file", nr.get("source_file", ""))
            nr["source_line_range"] = c["proposed_line_range"]
            if "source_location" in new_pfields:
                nr["source_location"] = c["proposed_line_range"]
            nr["source_problem_number"] = c.get("source_problem_number", "")
            nr["source_heading"] = c.get("source_heading", "")
            nr["problem_type"] = c.get("detected_type", "")
            nr["statement_hash"] = c["statement_hash"]
            nr["structural_status"] = "ACTIVE_RESEGMENTED"
            nr["supersedes_problem_id"] = oldid
            nr["structural_repair_note"] = (
                "Explicit child segment from v3 SAFE_SPLIT_PREVIEW."
            )
            old_notes = nr.get("notes", "")
            nr["notes"] = (
                (old_notes + " | ") if old_notes else ""
            ) + f"Structurally resegmented from {oldid}."
            shadow_ledger.append(nr)

    shadow_by_id = {r["problem_id"]: r for r in shadow_ledger}

    # Build shadow solution links.
    shadow_links = []
    post_split_review = []
    relinked_count = 0
    old_links_cleared = 0
    candidate_lists_rewritten = 0

    for s0 in links:
        s = dict(s0)
        s.setdefault("previous_linked_problem_id", "")
        s.setdefault("structural_relink_status", "")
        s.setdefault("structural_relink_method", "")

        # Rewrite candidate lists anywhere they still point to superseded parent IDs.
        old_candidates = s.get("candidate_problem_ids", "")
        new_candidates = replace_candidate_parent_ids(old_candidates, old_to_newids)
        if new_candidates != old_candidates:
            s["candidate_problem_ids"] = new_candidates
            candidate_lists_rewritten += 1

        old_link = s.get("linked_problem_id", "")
        if old_link in child_pairs_by_old:
            old_parent = ledger_by_id[old_link]
            children = [
                dict(c, new_problem_id=nid)
                for c, nid in child_pairs_by_old[old_link]
            ]

            chosen = unique_number_match(s, children)
            method = ""
            if chosen:
                method = "UNIQUE_SOURCE_NUMBER"
            else:
                chosen = same_file_preceding_match(
                    s,
                    children,
                    old_parent.get("source_file", ""),
                )
                if chosen:
                    method = "SAME_FILE_NEAREST_PRECEDING_CHILD"

            s["previous_linked_problem_id"] = old_link

            if chosen:
                s["linked_problem_id"] = chosen["new_problem_id"]
                s["structural_relink_status"] = "RELINKED"
                s["structural_relink_method"] = method
                relinked_count += 1
            else:
                s["linked_problem_id"] = ""
                s["structural_relink_status"] = "NEEDS_POST_SPLIT_RECONCILIATION"
                s["structural_relink_method"] = ""
                s["reconciliation_status"] = "NEEDS_POST_SPLIT_RECONCILIATION"
                s["candidate_problem_ids"] = ";".join(
                    nid for _, nid in child_pairs_by_old[old_link]
                )
                old_links_cleared += 1
                post_split_review.append({
                    "solution_id": s.get("solution_id", ""),
                    "previous_linked_problem_id": old_link,
                    "solution_source_file": s.get("solution_source_file", ""),
                    "solution_line_range": s.get("solution_line_range", ""),
                    "source_problem_number": s.get("source_problem_number", ""),
                    "candidate_problem_ids": s.get("candidate_problem_ids", ""),
                    "review_action": "RELINK_AFTER_SAFE_STRUCTURAL_SPLIT",
                })

        shadow_links.append(s)

    # Reject dangling direct links.
    for s in shadow_links:
        pid = s.get("linked_problem_id", "")
        if pid and pid not in shadow_by_id:
            errors.append(
                f"{s.get('solution_id','')}: dangling linked_problem_id {pid}"
            )

    recompute_solution_flags(shadow_ledger, shadow_links)
    semantic_units = rebuild_semantic_units(shadow_ledger)
    remaining_orphans, orphan_units = rebuild_remaining_orphans(
        shadow_links,
        shadow_ledger,
    )

    plan_fields = [
        "current_problem_id",
        "source_file",
        "current_line_range",
        "current_line_span",
        "child_count",
        "new_problem_ids",
        "child_line_ranges",
        "median_child_span",
        "max_child_span",
        "coverage_ratio",
        "repair_class",
    ]
    write_tsv(inv / "SAFE_STRUCTURAL_SPLIT_PLAN.tsv", plan_fields, plan)

    write_tsv(
        inv / "PROBLEM_LEDGER_SAFE_SPLIT_SHADOW.tsv",
        new_pfields,
        shadow_ledger,
    )
    write_tsv(
        inv / "PROBLEM_SOLUTION_LINKS_SAFE_SPLIT_SHADOW.tsv",
        new_lfields,
        shadow_links,
    )

    superseded_fields = extend(
        pfields,
        ["superseded_by_problem_ids", "supersession_reason"],
    )
    write_tsv(
        inv / "SUPERSEDED_STRUCTURAL_ROWS_PREVIEW.tsv",
        superseded_fields,
        superseded_rows,
    )

    write_tsv(
        inv / "POST_SPLIT_LINK_REVIEW.tsv",
        [
            "solution_id",
            "previous_linked_problem_id",
            "solution_source_file",
            "solution_line_range",
            "source_problem_number",
            "candidate_problem_ids",
            "review_action",
        ],
        post_split_review,
    )

    semantic_fields = [
        "statement_hash",
        "semantic_problem_id",
        "representative_problem_id",
        "member_count",
        "member_problem_ids",
        "source_files",
        "source_collections",
        "problem_types",
        "source_problem_numbers",
        "aggregate_solution_ids",
        "aggregate_hint_ids",
        "solution_availability",
        "review_status",
    ]
    write_tsv(
        inv / "SEMANTIC_PROBLEM_UNITS_SAFE_SPLIT_SHADOW.tsv",
        semantic_fields,
        semantic_units,
    )

    remaining_fields = [
        "solution_id",
        "solution_semantic_unit_id",
        "solution_kind",
        "solution_source_file",
        "solution_line_range",
        "source_problem_number",
        "status",
        "candidate_problem_ids",
        "candidate_statement_hashes",
        "editorial_action",
    ]
    write_tsv(
        inv / "REMAINING_ORPHANS_SAFE_SPLIT_SHADOW.tsv",
        remaining_fields,
        remaining_orphans,
    )

    orphan_fields = [
        "orphan_semantic_unit_id",
        "member_count",
        "member_solution_ids",
        "source_files",
        "statuses",
        "candidate_problem_ids",
        "candidate_statement_hashes",
        "distinct_candidate_statement_count",
        "editorial_action",
    ]
    write_tsv(
        inv / "ORPHAN_SEMANTIC_UNITS_SAFE_SPLIT_SHADOW.tsv",
        orphan_fields,
        orphan_units,
    )

    old_count = len(ledger)
    new_count = len(shadow_ledger)
    child_rows = total_children
    semantic_count = len(semantic_units)

    summary = [
        "# Safe structural split",
        "",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- SAFE parent rows selected: **{len(safe_rows)}**",
        f"- Parent rows superseded: **{len(superseded_rows)}**",
        f"- Child problem rows created: **{child_rows}**",
        f"- Master/shadow ledger row count: **{old_count} → {new_count}**",
        f"- Net ledger increase: **{new_count-old_count:+d}**",
        f"- Existing direct solution/hint links relinked uniquely: **{relinked_count}**",
        f"- Existing direct links cleared for explicit post-split review: **{old_links_cleared}**",
        f"- Candidate-problem lists rewritten away from superseded parents: **{candidate_lists_rewritten}**",
        f"- Post-split link-review rows: **{len(post_split_review)}**",
        f"- Semantic statement units after split: **{semantic_count}**",
        f"- Remaining orphan source blocks after split: **{len(remaining_orphans)}**",
        f"- Remaining orphan semantic units after split: **{len(orphan_units)}**",
        f"- Validation errors: **{len(errors)}**",
        "",
        "Only the 75 rows classified `SAFE_SPLIT_PREVIEW` are superseded.",
        "All `REVIEW_SPLIT_PREVIEW` and `INSUFFICIENT_SEGMENTATION` rows remain unchanged.",
    ]

    if errors:
        summary += ["", "## Validation errors", ""]
        summary += [f"- {e}" for e in errors]

    (inv / "SAFE_STRUCTURAL_SPLIT_SUMMARY.md").write_text(
        "\n".join(summary) + "\n",
        encoding="utf-8",
    )

    if errors:
        print("SAFE STRUCTURAL SPLIT VALIDATION FAILED")
        for e in errors:
            print(" -", e)
        return 1

    print(
        "SAFE STRUCTURAL SPLIT DRY RUN PASSED: "
        f"parents={len(safe_rows)} children={child_rows} "
        f"ledger={old_count}->{new_count} relinked={relinked_count} "
        f"review_links={old_links_cleared}"
    )

    if not args.apply:
        print(
            "No master files changed. Inspect SAFE_STRUCTURAL_SPLIT_SUMMARY.md, "
            "POST_SPLIT_LINK_REVIEW.tsv, and the shadow ledger; then rerun with --apply."
        )
        return 0

    # Freeze pre-split master files once.
    pre_files = [
        "PROBLEM_LEDGER.tsv",
        "PROBLEM_SOLUTION_LINKS.tsv",
        "SEMANTIC_PROBLEM_UNITS.tsv",
        "REMAINING_ORPHANS.tsv",
        "ORPHAN_SEMANTIC_UNITS.tsv",
    ]
    for name in pre_files:
        src = inv / name
        dst = inv / name.replace(".tsv", "_PRE_SAFE_STRUCTURAL_SPLIT.tsv")
        if src.exists() and not dst.exists():
            shutil.copy2(src, dst)

    # Promote shadow files to authoritative master files.
    write_tsv(inv / "PROBLEM_LEDGER.tsv", new_pfields, shadow_ledger)
    write_tsv(inv / "PROBLEM_SOLUTION_LINKS.tsv", new_lfields, shadow_links)
    write_tsv(inv / "SEMANTIC_PROBLEM_UNITS.tsv", semantic_fields, semantic_units)
    write_tsv(inv / "REMAINING_ORPHANS.tsv", remaining_fields, remaining_orphans)
    write_tsv(inv / "ORPHAN_SEMANTIC_UNITS.tsv", orphan_fields, orphan_units)
    write_tsv(
        inv / "SUPERSEDED_STRUCTURAL_ROWS.tsv",
        superseded_fields,
        superseded_rows,
    )

    print(
        "SAFE STRUCTURAL SPLIT APPLIED: "
        f"parents={len(safe_rows)} children={child_rows} ledger={old_count}->{new_count}"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
