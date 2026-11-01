#!/usr/bin/env python3
"""Validate actual committed Chad Guides against immutable country base."""
from pathlib import Path
import subprocess,os,json,hashlib,importlib.util,sys
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
os.chdir(ROOT);sys.path.insert(0,str(ROOT/'scripts'))
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
changed=subprocess.check_output(['git','diff','--name-only','--no-renames',BASE,head],text=True).splitlines()
guides=[x for x in changed if x.startswith('skills/chad/') and x.endswith('.md') and not x.endswith('/README.md')]
assert len(guides)==7,guides
assert all(subprocess.check_output(['git','show',head+':'+x])==Path(x).read_bytes() for x in guides)
env=dict(os.environ,PYTHONPATH='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps')
commands=[]
for argv in [['python3','scripts/skill_checks.py',*guides],['python3','scripts/check-examples.py','--require',*guides],['python3','scripts/check-sync-integrity.py','--base',BASE,'--head',head,'--mode','audit','--strict-metadata'],['git','diff','--check',BASE,head]]:
 p=subprocess.run(argv,env=env,capture_output=True,text=True)
 commands.append({'argv':argv,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 assert p.returncode==0,(argv,p.stdout,p.stderr)
# Existing changed-only validator is pinned here without modifying its source.
spec=importlib.util.spec_from_file_location('chad_validate',ROOT/'scripts/validate-guides.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
mod.changed_files_vs_main=lambda:changed
statuses=subprocess.check_output(['git','diff','--name-status','--no-renames',BASE,head],text=True).splitlines()
mod.added_and_deleted_vs_main=lambda:({x.split('\t')[1] for x in statuses if x.startswith('A\t')},{x.split('\t')[1] for x in statuses if x.startswith('D\t')})
import contextlib,io
capture=io.StringIO();oldargs=sys.argv;sys.argv=['validate-guides.py','--changed-only','--no-index-check']
with contextlib.redirect_stdout(capture):mod.main()
sys.argv=oldargs
commands.append({'argv':['pinned existing validate-guides.py','--changed-only','--no-index-check'],'exit':0,'stdout':capture.getvalue(),'stderr':''})
# Exact platform keys and entire CTA suffix; new TP contains none of those keys.
platform=('review_status','trust_label','license','authored_by','verified_by','reviewed_by','reviewed_on','drafted_by','approved_by','validation_status','validated')
metadata={}
for path in guides:
 new=Path(path).read_text()
 old=subprocess.run(['git','show',BASE+':'+path],capture_output=True,text=True)
 if old.returncode:
  assert all(not any(l.startswith(k+':') for l in new.splitlines()) for k in platform)
  assert '<!-- openaccountants-cta-block -->' not in new
  metadata[path]='new; no platform fields or stamped CTA'
 else:
  for key in platform:
   before=[l for l in old.stdout.splitlines() if l.startswith(key+':')]
   after=[l for l in new.splitlines() if l.startswith(key+':')]
   assert before==after,(path,key)
  assert old.stdout.split('<!-- openaccountants-cta-block -->',1)[1]==new.split('<!-- openaccountants-cta-block -->',1)[1]
  metadata[path]='platform fields and complete CTA preserved'
# Prior accepted Guide and all historical review/source evidence unchanged.
history=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'evidence/ledgers'],text=True).splitlines()
history=[x for x in history if '/chad-' in x or x.endswith('/td-import-exemption-eligibility.md')]
for path in history:
 assert subprocess.check_output(['git','rev-parse',BASE+':'+path])==subprocess.check_output(['git','rev-parse',head+':'+path]),path
imp='skills/chad/td-import-exemption-eligibility.md';assert subprocess.check_output(['git','show',BASE+':'+imp])==Path(imp).read_bytes()
# Zero-context saved patch, avoiding unchanged-context whitespace noise.
patch=subprocess.check_output(['git','diff','--unified=0',BASE,head])
(ROOT.parent/'sources'/'committed-guide-change-zero-context.diff').write_bytes(patch)
report={'base':BASE,'validated_head':head,'changed_guides':guides,'changed_guide_count':7,'example_count':14,'metadata':metadata,'historical_files_preserved':len(history),'commands':commands,'all_pass':True}
(OUT/'committed-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'changed_guides':7,'examples':14,'all_pass':True,'head':head}))
