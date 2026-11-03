#!/usr/bin/env python3
"""Writer arithmetic/shape/preservation checks, not independent source review."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
root=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(root/'scripts'))
import skill_checks
out=Path(__file__).resolve().parent
base=json.loads((out/'preservation-baseline.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=root)
checks=[]
for f in base['files']:
 b=git('show','HEAD:'+f['path']);assert sha(b)==f['sha256'],f['path']
 p=root/f['path']
 if p.exists():assert sha(p.read_bytes())==f['sha256'],f['path']
 checks.append({'path':f['path'],'sha256':f['sha256'],'preserved':True})
source_rows=json.loads((out/'source-identities.json').read_text())
for s in source_rows:
 for f in s['captures']:
  p=root/f['path'];assert sha(p.read_bytes())==f['sha256'];assert p.stat().st_size==f['bytes']
norm=lambda s:re.sub(r'\s+',' ',s).strip()
rows=json.loads((out/'mg-annual-property-tax.json').read_text())
for row in rows:
 text=norm((root/row['cached_text']).read_text())
 for q in row['exact_french_quotes']:assert norm(q) in text,(row['id'],q)
path='skills/madagascar/mg-annual-property-tax.md'
text=(root/path).read_text();shape=skill_checks.run_all(path)
assert len(shape)==15;assert not any(shape.values()),shape
front=skill_checks.read_frontmatter(text)
for forbidden in ['license','review_status','trust_label','reviewed_by','reviewed_on','verified_by','authored_by']:
 assert forbidden not in front,forbidden
assert 'openaccountants-cta-block' not in text
receipt=json.loads((out/'readme-addition.json').read_text())
old=git('show',receipt['base_commit']+':'+receipt['path'])
assert sha(old)==receipt['before_sha256']
assert (root/receipt['path']).read_bytes()==old+receipt['literal_append'].encode()
assert text.count('```oa-check')==2
result=subprocess.run([sys.executable,'scripts/check-examples.py','--require',path],cwd=root,capture_output=True,text=True)
assert result.returncode==0,result.stdout+result.stderr
print(json.dumps({'classification':'Writer checks only; no independent source review or accountant attestation','base_commit':base['base_commit'],'preserved_files':checks,'ledger_rows':len(rows),'quote_substring_check':'All quote anchors found after whitespace normalization; not a substitute for reading conditions','source_capture_count':sum(len(s['captures']) for s in source_rows),'shape_checks':shape,'worked_cases':{'exit':result.returncode,'stdout':result.stdout},'new_guide_sha256':sha((root/path).read_bytes()),'readme_additive_only':True},indent=2))
