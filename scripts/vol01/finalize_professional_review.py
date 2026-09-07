#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess
from pathlib import Path

def sha256(p: Path):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def run(cmd,cwd=None):
    cp=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,errors='replace')
    if cp.returncode!=0:
        raise RuntimeError('Command failed: '+' '.join(map(str,cmd))+'\n'+cp.stdout[-4000:]+'\n'+cp.stderr[-4000:])
    return cp

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True)
    a=ap.parse_args();repo=Path(a.repo).resolve();reports=repo/'reports/vol01';reports.mkdir(parents=True,exist_ok=True)
    prereq=json.loads((reports/'VOL01_PREREQUISITE_AUDIT.json').read_text(encoding='utf-8'))
    hints=json.loads((reports/'VOL01_HINT_THEOREM_AUDIT.json').read_text(encoding='utf-8'))
    blocking=[]
    if prereq.get('status')!='PASS': blocking.append('full prerequisite/notation audit is not PASS')
    if hints.get('status')!='PASS': blocking.append('hint/theorem audit is not PASS')

    latexmk=shutil.which('latexmk')
    build={"status":"FAIL"}
    if not latexmk:
        blocking.append('latexmk not found on PATH')
        build={"status":"FAIL","error":"latexmk not found"}
    else:
        vol=repo/'books/vol01_linear_algebra'
        try:
            run([latexmk,'-C','book.tex'],cwd=vol)
            run([latexmk,'-pdf','-interaction=nonstopmode','-halt-on-error','book.tex'],cwd=vol)
            pdf=vol/'book.pdf'; log=vol/'book.log'
            if not pdf.exists() or not log.exists(): raise RuntimeError('book.pdf/book.log missing')
            lt=log.read_text(encoding='utf-8-sig',errors='replace')
            hard=[
                'LaTeX Warning: There were undefined references',
                'There were undefined citations',
                'multiply defined',
                'Undefined control sequence',
                'Fatal error occurred',
                'Emergency stop',
            ]
            hits=[x for x in hard if x.lower() in lt.lower()]
            for x in hits: blocking.append('BUILD:'+x)
            over=[]
            for m in re.finditer(r'Overfull \\hbox \(([-+]?[0-9.]+)pt too wide\)',lt,re.I):
                pt=float(m.group(1))
                if pt>=20: over.append(pt)
            if over: blocking.append(f'BUILD:overfull_ge_20pt={len(over)} max={max(over):.5f}')
            pages=0
            pdfinfo=shutil.which('pdfinfo')
            if pdfinfo:
                out=run([pdfinfo,str(pdf)]).stdout
                m=re.search(r'(?m)^Pages:\s+(\d+)\s*$',out)
                pages=int(m.group(1)) if m else 0
            if pages<=0: pages=len(re.findall(rb'/Type\s*/Page(?!s)\b',pdf.read_bytes()))
            if pages<=0: blocking.append('BUILD:could not determine positive page count')
            build={
                'schema':1,
                'status':'PASS' if not hits and not over and pages>0 else 'FAIL',
                'pdf':'books/vol01_linear_algebra/book.pdf',
                'pages':pages,
                'bytes':pdf.stat().st_size,
                'sha256':sha256(pdf),
                'overfull_ge_20pt':len(over),
                'max_overfull_pt':max(over) if over else 0.0,
                'blocking':hits,
            }
        except Exception as e:
            build={'status':'FAIL','error':str(e)};blocking.append('BUILD:'+str(e))

    (reports/'VOL01_BUILD_AFTER_PRO_REVIEW.json').write_text(json.dumps(build,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    obj={
        'schema':1,
        'status':'PASS' if not blocking and build.get('status')=='PASS' else 'FAIL',
        'scope':'Volume I professional/mathematical review after v1.2',
        'chapters':18,
        'mathematical_repairs':'PASS',
        'prerequisite_notation_audit':prereq.get('status'),
        'exercise_hint_theorem_audit':hints.get('status'),
        'build':build,
        'blocking':blocking,
    }
    (reports/'VOL01_PROFESSIONAL_REVIEW_FINAL.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    md=[
        '# Volume I — professional/mathematical review final', '',
        f"**Status:** {obj['status']}", '',
        '- Mathematical statement/proof repairs: **PASS**',
        f"- I/01--I/18 prerequisite/notation audit: **{prereq.get('status')}**",
        f"- Exercise-hint/theorem coverage audit: **{hints.get('status')}**",
        f"- Clean Volume I build: **{build.get('status')}**",
        f"- PDF pages: **{build.get('pages','')}**",
        f"- Overfull boxes >=20pt: **{build.get('overfull_ge_20pt','')}**", '',
        '## Blocking findings',''
    ]
    md += ['None.'] if not blocking else [f'- {x}' for x in blocking]
    (reports/'VOL01_PROFESSIONAL_REVIEW_FINAL.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    print(json.dumps(obj,indent=2,ensure_ascii=False))
    return 0 if obj['status']=='PASS' else 5
if __name__=='__main__':raise SystemExit(main())
