#!/usr/bin/env python3
"""Check the exact prior Burundi content and source identities; no live writes."""
from pathlib import Path
import hashlib,importlib.util,json,subprocess,sys
R=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'scripts'));import skill_checks
P=R/'skills/burundi/bi-property-transactions.md'
def h(b):return hashlib.sha256(b).hexdigest()
def g(*a):return subprocess.check_output(['git',*a],cwd=R)
base=json.loads((E/'preservation-baseline.json').read_text()); preserved=[]
for row in base['files']:
 p=row['path'];before=g('show',base['base_commit']+':'+p)
 assert h(before)==row['sha256'],p+' baseline mismatch'
 assert g('rev-parse',base['base_commit']+':'+p).decode().strip()==row['blob'],p+' blob mismatch'
 if p!='skills/burundi/README.md':
  actual=(R/p).read_bytes() if (R/p).exists() else g('show','HEAD:'+p)
  assert h(actual)==row['sha256'],p+' preservation mismatch';preserved.append(p)
text=P.read_text();fm=skill_checks.read_frontmatter(text);checks=skill_checks.run_checks(str(P),text,fm)
assert len(checks)==15,checks
assert not any(checks.values()),checks
assert all(x not in fm for x in ['review_status','trust_label','license','reviewed_by','reviewed_on','authored_by'])
assert 'openaccountants-cta-block' not in text
ledger=json.loads((E/'bi-property-transactions.json').read_text());assert len(ledger)==66
for row in ledger:
 for key in ['section','act','article','official_url','exact_quote','read_date','source_sha256','pdf_locator','source_read_scope']:
  assert row.get(key),f'{row["id"]} missing {key}'
raw=[]
for source in json.loads((E/'source-identities.json').read_text()).values():
 p=R.parent/'sources'/source['path']
 if p.exists():assert h(p.read_bytes())==source['sha256'];raw.append(source['path'])
print(json.dumps(dict(result='pass',prior_files_preserved=len(preserved),old_guides_preserved=sum(x.startswith('skills/burundi/') for x in preserved),prior_evidence_preserved=sum(x.startswith('evidence/') for x in preserved),shape_checks=checks,ledger_rows=len(ledger),actual_source_bytes_checked=raw,new_guides=1,replaced_body_units=0),indent=2))
