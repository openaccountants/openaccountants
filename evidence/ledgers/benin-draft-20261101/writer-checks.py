#!/usr/bin/env python3
"""Reproducible local writer checks. This is not independent source review."""
from pathlib import Path
import hashlib, json, os, re, subprocess, sys
ROOT=Path(__file__).resolve().parents[3]
BASE='a7888d0d6c1f7cb0fed13d8d3f6b7e05f1d12297'
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scripts'))
from frontmatter_yaml import load_frontmatter

def git(*args): return subprocess.run(['git',*args],cwd=ROOT,capture_output=True,check=True).stdout

def fm(t): return load_frontmatter(t.split('---',2)[1])
paths=sorted((ROOT/'skills/benin').glob('bj-*.md'))
results={}
for p in paths:
 data=fm(p.read_text()); assert data['jurisdiction']=='BJ' and type(data['tax_year']) is int and data['tax_year']==2026
 assert data['tier']==2 and not data.get('verified_by') and not data.get('reviewed_by')
results['strict_metadata']={'guides':len(paths),'passed':True}
legacy={}
oldmap=(ROOT/'evidence/ledgers/benin-old-topics.md').read_text()
for rel in git('ls-tree','-r','--name-only',BASE,'skills/benin').decode().splitlines():
 p=ROOT/rel
 if not p.name.startswith('bj-'):continue
 old=git('show',f'{BASE}:{rel}'); new=p.read_bytes();a=fm(old.decode());b=fm(new.decode())
 for key in ['review_status','trust_label','license']:
  assert a.get(key)==b.get(key),(p.name,key)
 marker=b'<!-- openaccountants-cta-block -->'
 assert old.split(marker,1)[1]==new.split(marker,1)[1],p.name
 topics=[line for line in old.decode().split('<!-- openaccountants-cta-block -->',1)[0].splitlines() if line.startswith('#') or re.match(r'^- \*\*',line)]
 for topic in topics:assert f'{p.name}: {topic}' in oldmap,(p.name,topic)
 legacy[p.name]={'baseline_sha256':hashlib.sha256(old).hexdigest(),'topics':len(topics),'cta_and_platform_metadata_unchanged':True,'old_bytes':len(old),'new_bytes':len(new)}
results['legacy_preservation']=legacy
# Every map target exists and every target section is real.
for line in oldmap.splitlines():
 if not line.startswith('| bj-'):continue
 target=line.split('|')[2].strip();fn,anchor=target.split('#',1)
 text=(ROOT/'skills/benin'/fn).read_text()
 anchors={re.sub(r'[^a-z0-9 -]','',x.lower()).replace(' ','-') for x in re.findall(r'^## (.*)$',text,re.M)}
 assert anchor in anchors,target
results['legacy_topic_count']=sum(x['topics'] for x in legacy.values())
results['ledger_rows']={p.name:len(re.findall(r'^\| \d+ \|',p.read_text(),re.M)) for p in (ROOT/'evidence/ledgers').glob('bj-*.md')}
assert len(results['ledger_rows'])==8
# All primary CGI quotes are literal after typography and whitespace normalisation.
# This check reads private full source text without copying it into Git.
cgi_path=ROOT.parent/'sources/cgi2026.txt'
def norm(s):return re.sub(r'\s+',' ',s.replace('’',"'").replace('À','A').replace('«','').replace('»','')).strip().casefold()
if cgi_path.exists():
 cgi=norm(cgi_path.read_text()); checked=0
 for p in (ROOT/'evidence/ledgers').glob('bj-*.md'):
  for line in p.read_text().splitlines():
   if re.match(r'^\| \d+ \|',line) and '6adcbd46ab83b_' in line:
    quote=line.split('|')[6].strip().strip('«» ')
    assert norm(quote) in cgi,(p.name,quote)
    checked+=1
 results['cgi_literal_quotes']={'checked':checked,'passed':True}
else:results['cgi_literal_quotes']={'skipped':'private source absent; not an independent source reread'}
commands=[['python3','scripts/skill_checks.py',*[str(p.relative_to(ROOT)) for p in paths]],['python3','scripts/check-examples.py','--require',*[str(p.relative_to(ROOT)) for p in paths]],['python3',str((HERE/'pinned-validation.py').relative_to(ROOT))],['git','diff','--check'],['git','diff','--cached','--check']]
results['commands']=[]
for cmd in commands:
 r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
 results['commands'].append({'argv':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
results['passed']=all(r['exit_code']==0 for r in results['commands'])
(HERE/'check-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':results['passed'],'guides':len(paths),'legacy_topics':results['legacy_topic_count'],'ledger_rows':sum(results['ledger_rows'].values()),'commands':[(r['argv'][:2],r['exit_code']) for r in results['commands']]},indent=2))
sys.exit(0 if results['passed'] else 1)
