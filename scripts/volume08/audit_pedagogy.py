#!/usr/bin/env python3
"""Read-only Volume VIII preservation audit, with optional NEW external output.

Exit 0: structural source checks passed (pedagogy still HOLD).
Exit 1: structural/invocation failure. Exit 2 with --strict: readiness is HOLD.
No builds, release updates or freeze actions are performed.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.dont_write_bytecode=True
from pedagogy_core import AuditError, load_json, report_markdown, source_audit

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--stage',type=int,choices=(1,2,3),required=True)
    p.add_argument('--strict',action='store_true',help='Return exit 2 while pedagogical readiness is HOLD')
    p.add_argument('--output',type=Path,help='NEW directory outside repository for JSON and Markdown reports; never overwritten')
    args=p.parse_args(); root=Path(__file__).resolve().parent
    repo=args.repo.resolve()
    banks=[load_json(root/n) for n in ('hints_01_17.json','hints_18_35.json') if (root/n).is_file()]
    report=source_audit(repo,load_json(root/'pedagogy_plan.json'),args.stage,banks,load_json(root/'protected_findings.json'))
    if args.output:
        out=args.output.resolve()
        if out.is_relative_to(repo) or out.exists():
            raise AuditError('--output must be a new directory outside the repository')
        out.mkdir(parents=True)
        (out/'audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
        (out/'audit.md').write_text(report_markdown(report),encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('stage','structural_source_status','pedagogy_readiness','counts_from_active_source','curated_hint_coverage','duplicate_labels','unresolved_static_references','canonical_pdf_build','freeze_executed')},indent=2))
    for failure in report['structural_failures']: print('BLOCK: '+failure,file=sys.stderr)
    if report['structural_source_status']!='PASS': return 1
    return 2 if args.strict else 0
if __name__=='__main__':
    try: raise SystemExit(main())
    except (AuditError,OSError,ValueError,KeyError) as exc:
        print('AUDIT STOPPED: '+str(exc),file=sys.stderr); raise SystemExit(1)
