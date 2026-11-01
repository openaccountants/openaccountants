#!/usr/bin/env python3
"""Independent mechanical and predecessor identity audit; does not certify law."""
from pathlib import Path
import datetime,hashlib,json,os,re,subprocess
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
FROZEN='416ec514979330e5980061eda4a38ab2cdef6e4a'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(b):return hashlib.sha256(b).hexdigest()
subprocess.run(['git','merge-base','--is-ancestor',FROZEN,'HEAD'],cwd=ROOT,check=True)
closure=json.loads((OUT/'closure-candidate-manifest.json').read_text())
frozen_files={}
for path,expected_hash in closure['files'].items():
 b=(ROOT/path).read_bytes();assert sha(b)==expected_hash;assert b==git('show',f'{FROZEN}:{path}')
 frozen_files[path]=expected_hash
ids=json.loads((OUT/'predecessor-identities.json').read_text());maptext=(OUT/'old-topics.md').read_text()
maprows={}
for line in maptext.splitlines():
 m=re.match(r'\| (skills/chad/[^ ]+) `([0-9a-f]+)` L(\d+) \| (.*?) \| (.*?) \|$',line)
 if m:
  path,blob,n,old,dest=m.groups();key=(path,int(n));assert key not in maprows
  maprows[key]=(blob,old,dest)
results={};alltopics=[]
platform=('review_status','trust_label','license','authored_by','verified_by','reviewed_by','reviewed_on','drafted_by','approved_by','validation_status','validated')
for path,expected in ids.items():
 old=git('show',f'{BASE}:{path}');new=(ROOT/path).read_bytes()
 assert sha(old)==expected['sha256']
 assert git('rev-parse',f'{BASE}:{path}').decode().strip()==expected['git_blob']
 oldtext=old.decode();newtext=new.decode()
 for key in platform:
  assert [l for l in oldtext.split('---',2)[1].splitlines() if l.startswith(key+':')]==[l for l in newtext.split('---',2)[1].splitlines() if l.startswith(key+':')],(path,key)
 for key in ('name','jurisdiction'):
  assert [l for l in oldtext.split('---',2)[1].splitlines() if l.startswith(key+':')]==[l for l in newtext.split('---',2)[1].splitlines() if l.startswith(key+':')],(path,key)
 oldbody=oldtext.split('---',2)[2].split('<!-- openaccountants-cta-block -->')[0]
 topics=[]
 for n,line in enumerate(oldbody.splitlines(),1):
  if not line.strip():continue
  row=maprows.get((path,n));assert row is not None,(path,n,'missing mapping')
  blob,item,dest=row;assert blob==expected['git_blob'];assert item==line.replace('|','&#124;'),(path,n,item,line)
  assert dest.strip();topics.append({'body_line':n,'original':line.strip(),'destination':dest})
  alltopics.append((path,n))
 cta_old=oldtext.split('<!-- openaccountants-cta-block -->',1)
 cta_new=newtext.split('<!-- openaccountants-cta-block -->',1)
 cta_same=len(cta_old)==len(cta_new) and (len(cta_old)==1 or cta_old[1]==cta_new[1])
 assert cta_same,path
 results[path]={'old_sha256':sha(old),'new_sha256':sha(new),'unchanged':old==new,'cta_preserved':cta_same,'platform_metadata_preserved':True,'old_editorial_lines':len(topics),'topics':topics}
assert set(maprows)==set(alltopics),'unmatched mapping rows'
# Prior import scope is fixed; no acceptance is extended.
imp='skills/chad/td-import-exemption-eligibility.md';assert results[imp]['unchanged']
files=sorted(str(p.relative_to(ROOT)) for p in (ROOT/'skills/chad').glob('*.md') if p.name!='README.md' and p.name!='td-import-exemption-eligibility.md')
env=dict(os.environ,PYTHONPATH='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps')
commands=[]
for argv in [['python3','scripts/skill_checks.py',*files],['python3','scripts/check-examples.py','--require',*files],['python3','scripts/check-sync-integrity.py','--base',BASE,'--head',FROZEN,'--mode','audit','--strict-metadata'],['git','diff','--check',BASE,FROZEN]]:
 p=subprocess.run(argv,cwd=ROOT,env=env,text=True,capture_output=True)
 commands.append({'argv':argv,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
history=[p for p in git('ls-tree','-r','--name-only',BASE,'evidence/ledgers').decode().splitlines() if '/chad-' in p]
for p in history:assert git('show',f'{BASE}:{p}')==(ROOT/p).read_bytes(),p
result={'prior_chad_evidence_files_preserved':history,'prior_evidence_count':len(history),'reviewed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'immutable_base':BASE,'frozen_candidate':FROZEN,'frozen_files':frozen_files,'predecessors':results,'total_predecessor_editorial_lines':len(alltopics),'commands':commands}
(OUT/'mechanical-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'old_editorial_lines':len(alltopics),'predecessor_files':len(results),'commands':[c['returncode'] for c in commands]}))
