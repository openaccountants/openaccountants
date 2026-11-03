#!/usr/bin/env python3
"""Writer's reproducible preservation and shape checks; no law verification implied."""
import hashlib,json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'scripts'))
import skill_checks
b=json.loads((E/'preservation-baseline.json').read_text());a=json.loads((E/'readme-addition.json').read_text());checked=[]
for x in b['files']:
 p=R/x['path']
 data=p.read_bytes() if p.exists() else subprocess.check_output(['git','show','HEAD:'+x['path']],cwd=R)
 if x['path']==a['path']:
  assert data.decode().endswith(a['append_exact']);data=data[:-len(a['append_exact'].encode())]
 assert hashlib.sha256(data).hexdigest()==x['sha256'],x['path']
 checked.append({'path':x['path'],'reading':'working file' if p.exists() else 'HEAD blob; sparse absent'})
g=R/'skills/burkina-faso/bf-company-property-tax.md';checks=skill_checks.run_all(str(g));assert all(not v for v in checks.values()),checks
rows=json.loads((E/'bf-company-property-tax.json').read_text());assert len(rows)==30
for row in rows:
 assert all(row.get(k) for k in ['id','section','rule','act','article','printed_page','official_url','quote_fr','read_date','source_sha256'])
print(json.dumps({'preservation':'pass','old_guides':10,'prior_evidence_files':102,'README_append_only':True,'shape_checks':checks,'ledger_rows':len(rows),'checked_files':checked},indent=2))
