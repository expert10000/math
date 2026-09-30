#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, re
from collections import Counter
from pathlib import Path

TARGETS = {
    'CP-II-0086','CP-II-0108','CP-II-0127','CP-II-0249',
    'CP-II-0303','CP-II-0310','CP-II-0322','CP-II-0395',
    'CP-II-0434','CP-II-0508','CP-II-0523','CP-II-0544',
    'CP-II-0545','CP-II-0547','CP-II-0551','CP-II-0569',
}
EXPECTED_C_REWRITE = 0
EXPECTED_D_BLOCKING = 0


def window(text: str, pid: str) -> str:
    starts=list(re.finditer(r"\\begin\{problem\}\[(CP-II-\d{4})\]",text))
    i=next((i for i,m in enumerate(starts) if m.group(1)==pid),None)
    if i is None: raise ValueError(pid)
    a=starts[i].start(); b=starts[i+1].start() if i+1<len(starts) else len(text)
    return text[a:b]


def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',required=True,type=Path); args=ap.parse_args()
    repo=args.repo.resolve(); base=repo/'books'/'companion_problems_solutions'
    chapter=base/'chapters'/'part02_volume_ii'/'chapter.tex'
    audit=base/'metadata'/'PART_II_SOLUTION_QUALITY_AUDIT.tsv'
    prov=base/'metadata'/'PART_II_C_REWRITE_R1_PROVENANCE.tsv'
    errors=[]
    for p in (chapter,audit,prov):
        if not p.exists(): errors.append(f'missing required file: {p}')
    if errors:
        print('COMPANION PART II C_REWRITE R1 VALIDATION FAILED'); [print('  -',e) for e in errors]; return 1
    text=chapter.read_text(encoding='utf-8')
    sigs={
      'CP-II-0086':('principal-value','order exactly'),
      'CP-II-0108':('narrower and narrower spikes','continuity alone'),
      'CP-II-0127':('supports escape to infinity','global weighted Schwartz'),
      'CP-II-0249':('compact Hausdorff space is normal',),
      'CP-II-0303':(r'\ge\frac14','open cover with no finite subcover'),
      'CP-II-0310':('vertical fibers',r'\mathbb R^n/\mathbb Z^n'),
      'CP-II-0322':('Runge',),
      'CP-II-0395':('Hahn--Banach','weakly compact'),
      'CP-II-0434':('irrational','Heine--Borel'),
      'CP-II-0508':('forward boundary hit','moving the base point'),
      'CP-II-0523':('finite limit at infinity','Heine--Cantor'),
      'CP-II-0544':(r'\sin(x^3)','fixed amplitude'),
      'CP-II-0545':('every convergent sequence is Cauchy','Cauchy in'),
      'CP-II-0547':('Every Banach space','An open interval'),
      'CP-II-0551':("Riesz's lemma",'unit ball cannot be compact'),
      'CP-II-0569':('fundamental theorem of calculus','higher-order finite differences'),
    }
    for pid in TARGETS:
        try: w=window(text,pid)
        except ValueError: errors.append(f'{pid}: missing'); continue
        if re.search(r"\\begin\{(?:enumerate|itemize|description)\*?\}",w):
            errors.append(f'{pid}: legacy list environment survived')
        if re.search(r'(^|\s)\\item(?:\[|\s|$)',w,re.M):
            errors.append(f'{pid}: legacy item survived')
        wn=re.sub(r'\s+', ' ', w.lower()).strip()
        for sig in sigs[pid]:
            sn=re.sub(r'\s+', ' ', sig.lower()).strip()
            if sn not in wn:
                errors.append(f'{pid}: signature missing: {sig}')
    with audit.open('r',encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    by={r.get('companion_problem_id',''):r for r in rows}
    for pid in sorted(TARGETS):
        r=by.get(pid)
        if not r: errors.append(f'{pid}: missing audit row'); continue
        if r.get('quality_status')!='A_STRONG': errors.append(f"{pid}: expected A_STRONG, got {r.get('quality_status')}")
        if r.get('priority')!='P3': errors.append(f"{pid}: expected P3, got {r.get('priority')}")
    counts=Counter(r.get('quality_status','') for r in rows)
    if len(rows)!=570:
        errors.append(f'audit rows: expected 570, got {len(rows)}')
    if counts.get('C_REWRITE',0)!=EXPECTED_C_REWRITE:
        errors.append(
            f"C_REWRITE: expected {EXPECTED_C_REWRITE}, "
            f"got {counts.get('C_REWRITE',0)}"
        )
    if counts.get('D_BLOCKING',0)!=EXPECTED_D_BLOCKING:
        errors.append(
            f"D_BLOCKING: expected {EXPECTED_D_BLOCKING}, "
            f"got {counts.get('D_BLOCKING',0)}"
        )

    # If the pre-R1 backup is present, prove the 16 intended R1 targets
    # transitioned from C_REWRITE to A_STRONG. Later editorial batches may
    # legitimately change non-target rows, so their historical statuses are not frozen.
    backup = audit.with_name(audit.name + '.before_part02_c_rewrite_r1.bak')
    if backup.exists():
        with backup.open('r',encoding='utf-8-sig',newline='') as f:
            brows=list(csv.DictReader(f,delimiter='\t'))
        bby={r.get('companion_problem_id',''):r for r in brows}
        if len(brows)!=570:
            errors.append(f'pre-R1 backup audit rows: expected 570, got {len(brows)}')
        for pid in sorted(TARGETS):
            old=bby.get(pid)
            row=by.get(pid)

            if old is None:
                errors.append(f'{pid}: missing from pre-R1 backup audit')
                continue

            if old.get('quality_status')!='C_REWRITE':
                errors.append(
                    f"{pid}: pre-R1 status expected C_REWRITE, "
                    f"got {old.get('quality_status')}"
                )

            if row is None:
                errors.append(f'{pid}: missing current audit row')
            elif row.get('quality_status')!='A_STRONG':
                errors.append(
                    f"{pid}: current status expected A_STRONG, "
                    f"got {row.get('quality_status')}"
                )
    with prov.open('r',encoding='utf-8-sig',newline='') as f:
        prows=list(csv.DictReader(f,delimiter='\t'))
    pids={r.get('companion_problem_id','') for r in prows}
    if pids!=TARGETS: errors.append(f'R1 provenance IDs mismatch: {sorted(pids)}')
    if errors:
        print('COMPANION PART II C_REWRITE R1 VALIDATION FAILED')
        for e in errors: print('  -',e)
        return 1
    print('COMPANION PART II C_REWRITE R1 VALIDATION PASSED')
    print('  thematic section: Metric and Topological Foundations')
    print('  repaired C_REWRITE rows: 16')
    print('  all 16 targets: A_STRONG / P3')
    print(f"  A_STRONG: {counts.get('A_STRONG',0)}")
    print(f"  B_POLISH: {counts.get('B_POLISH',0)}")
    print(f"  C_REWRITE: {counts.get('C_REWRITE',0)}")
    print(f"  D_BLOCKING: {counts.get('D_BLOCKING',0)}")
    return 0

if __name__=='__main__': raise SystemExit(main())
