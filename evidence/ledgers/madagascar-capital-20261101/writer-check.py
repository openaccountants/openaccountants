#!/usr/bin/env python3
"""Check the new capital-income candidate, exact old blobs, quote anchors and metadata."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scripts'))
import skill_checks
from frontmatter_yaml import load_frontmatter
sha=lambda b:hashlib.sha256(b).hexdigest()
b=json.loads((HERE/'preservation-baseline.json').read_text())
for x in b['files']:
 current=subprocess.check_output(['git','show','HEAD:'+x['path']],cwd=ROOT)
 assert sha(current)==x['sha256'],x['path']
 p=ROOT/x['path']
 if p.exists():assert sha(p.read_bytes())==x['sha256'],x['path']
p=ROOT/'skills/madagascar/mg-capital-income.md';t=p.read_text();fm=load_frontmatter(t.split('---',2)[1])
assert 80<=len(fm['description'].split())<=150
for key in ['license','review_status','trust_label','authored_by','reviewed_by','reviewed_on']:assert key not in fm,key
assert 'openaccountants-cta-block' not in t
checks=skill_checks.run_checks(str(p),t,fm);assert len(checks)==15 and not any(checks.values()),checks
rows=json.loads((HERE/'mg-capital-income.json').read_text())
for x in rows:
 source=(ROOT/x['cached_text']).read_text();norm=re.sub(r'\s+',' ',source)
 assert sha((ROOT/x['cached_pdf']).read_bytes())==x['pdf_sha256'],x['id']
 for q in x['exact_french_quotes']:assert re.sub(r'\s+',' ',q) in norm,(x['id'],q)
 assert x['section'] and x['article'] and x['official_url'] and x['printed_page']
subprocess.run([sys.executable,'scripts/check-examples.py','--require',str(p.relative_to(ROOT))],cwd=ROOT,check=True)
print(json.dumps({'source_rule_rows':len(rows),'shape_checks':len(checks),'shape_problems':checks,'prior_guides_unchanged':b['guide_count'],'prior_evidence_blobs_unchanged':len(b['files'])-b['guide_count'],'new_guide_sha256':sha(p.read_bytes()),'old_topic_rule':'All prior introductions/headings/bullets/tables/frontmatter/CTA remain at identical old Guide blobs; no old Guide rewrite.'},indent=2))
