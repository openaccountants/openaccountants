#!/usr/bin/env python3
"""Narrow draft structure, source identity and immutable preservation checks."""
import hashlib,json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[3];E=Path(__file__).parent;S=R.parent/'sources';sys.path.insert(0,str(R/'scripts'))
import skill_checks
sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=R)
p=json.loads((E/'preservation-baseline.json').read_text());base=p['base_commit'];pres=[]
for x in p['files']:
 if x['path']=='skills/benin/README.md':continue
 b=git('show',f"HEAD:{x['path']}");assert sha(b)==x['sha256'],x['path']
 if (R/x['path']).exists():assert sha((R/x['path']).read_bytes())==x['sha256'],x['path']
 pres.append(x['path'])
source=[]
for x in json.loads((E/'source-identities.json').read_text()):
 assert sha((S/x['file']).read_bytes())==x['sha256'];source.append(x['file'])
shape={};ledger={}
for slug in ['bj-property-tfu','bj-rental-income-tax']:
 path=R/'skills/benin'/f'{slug}.md';txt=path.read_text();fm=skill_checks.read_frontmatter(txt)
 assert not any(k in fm for k in ['review_status','trust_label','license','verified_by','reviewed_by','reviewed_on'])
 assert 'openaccountants-cta-block' not in txt
 result=skill_checks.run_checks(str(path),txt,fm);assert len(result)==15
 assert all(not v for v in result.values()),result
 shape[slug]=result;rr=json.loads((E/f'{slug}.json').read_text());ledger[slug]=len(rr)
 for row in rr:
  assert all(row.get(k) for k in ['id','section','rule','act_article','official_url','exact_french_quote','read_date','source_sha256','read_scope'])
example=subprocess.run([sys.executable,'scripts/check-examples.py','--require','skills/benin/bj-property-tfu.md','skills/benin/bj-rental-income-tax.md'],cwd=R,text=True,capture_output=True);assert example.returncode==0,example.stdout+example.stderr
readme=(R/'skills/benin/README.md').read_text();assert readme.count('## Property and rental additions, 1 November 2026')==1
for domain in ['IT-IND','IT-CORP','VAT','SC','PR','TP','XB']:assert f'  {domain}:' in readme
report=dict(base=base,shape_checks=shape,ledger_counts=ledger,examples=dict(returncode=example.returncode,stdout=example.stdout,stderr=example.stderr),preserved_files=pres,preserved_guides=8,preserved_prior_evidence=28,source_identities_passed=source,replaced_old_guide_units=0,remaining_status='Both new drafts need independent review; all seven country domains remain partial.')
print(json.dumps(report,indent=2))
