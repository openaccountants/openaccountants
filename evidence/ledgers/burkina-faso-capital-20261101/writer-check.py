#!/usr/bin/env python3
"""Reproduce source-anchor, shape, migration and preservation checks, not legal review."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
R=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent;S=R.parent/'sources'
sys.path.insert(0,str(R/'scripts'));import skill_checks
sha=lambda x:hashlib.sha256(x).hexdigest()
b=json.loads((E/'preservation-baseline.json').read_text());migration=json.loads((E/'old-topic-destinations.json').read_text());addition=json.loads((E/'readme-addition.json').read_text());checked=[]
for x in b['files']:
 p=R/x['path'];d=p.read_bytes() if p.exists() else subprocess.check_output(['git','show','HEAD:'+x['path']],cwd=R)
 if x['path']==addition['path']:
  assert d.decode().endswith(addition['append_exact']);d=d[:-len(addition['append_exact'].encode())]
 if x['path']=='skills/burkina-faso/bf-corporate-tax.md':
  t=d.decode();m=migration['permitted_corporate_changes'];assert t.count(m['new_exact'])==1
  t=t.replace(m['new_exact'],m['old_exact'],1).replace('version: 1.2\n','version: 1.1\n',1).replace(m['H1_after'],m['H1_before'],1);d=t.encode()
 assert sha(d)==x['sha256'],x['path'];checked.append(x['path'])
shape={}
for slug in ['bf-investment-income','bf-corporate-tax']:
 p=R/'skills/burkina-faso'/f'{slug}.md';shape[slug]=skill_checks.run_all(str(p));assert all(not v for v in shape[slug].values()),shape[slug]
text=(R/'skills/burkina-faso/bf-investment-income.md').read_text();fm=text.split('---',2)[1]
for key in ['review_status:','trust_label:','license:','reviewed_by:','reviewed_on:']:
 assert key not in fm,key
assert 'openaccountants-cta-block' not in text
rows=json.loads((E/'bf-investment-income.json').read_text());assert len(rows)==60;pages=(S/'cgi-2026-raw.txt').read_text().split('\f');norm=lambda s:re.sub(r'\s+','',s).casefold();quote_checks=[]
for x in rows:
 for k in ['id','section','rule','act','article','printed_page','official_url','quote_fr','read_date','source_sha256']:assert x.get(k),[x['id'],k]
 assert x['source_sha256']==sha((S/'cgi-2026.pdf').read_bytes())
 nums=x['printed_page'] if isinstance(x['printed_page'],list) else [x['printed_page']];t=norm(' '.join(pages[n-1] for n in nums))
 for key in ['quote_fr','additional_quote_fr']:
  if x.get(key):assert norm(x[key]) in t,[x['id'],key]
 quote_checks.append({'row':x['id'],'anchor_in_cited_pages':True})
for x in json.loads((E/'source-identities.json').read_text()):
 assert sha((S/x['file']).read_bytes())==x['sha256'],x['file']
 for f in x.get('cached_reader_files',[]):assert sha((S/f['file']).read_bytes())==f['sha256'],f['file']
result={'immutable_predecessor':b['immutable_commit'],'shape_checks':shape,'new_ledger_rows':len(rows),'quote_checks':quote_checks,'source_identity_checks':'pass','preservation':{'old_guide_bodies_exact_except_two_migrated_corporate_rows':True,'old_Guide_count':len([p for p in checked if p.startswith('skills/') and not p.endswith('README.md')]),'prior_evidence_blob_count':len([p for p in checked if p.startswith('evidence/')]),'README_append_only':True,'checked_files':checked},'law_verification':'Not inferred from these mechanical checks; pending fresh independent source review.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
