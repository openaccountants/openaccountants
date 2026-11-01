#!/usr/bin/env python3
"""Read-only frozen review checks; outputs only in this review directory."""
from pathlib import Path
import hashlib,json,os,re,subprocess,sys
E=Path(__file__).resolve().parent;R=E.parents[2];W=E.parent/'burundi-capital-20261101'
HEAD='29c8b477f1d659c0042a6ae9de5b10ef615a98d0';BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8';OLD='eae2a469563bc2417596ddfca2db9c43a813a290'
def g(*a):return subprocess.check_output(['git',*a],cwd=R)
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return (R/p).read_bytes() if (R/p).exists() else g('show',HEAD+':'+p)
assert g('rev-parse','HEAD').decode().strip()==HEAD
assert g('merge-base',HEAD,'origin/main').decode().strip()==BASE
sys.path.insert(0,str(R/'scripts'));import skill_checks
checks={p:skill_checks.run_all(p) for p in ['skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md']}
assert all(len(v)==15 and not any(v.values()) for v in checks.values())
transform=json.loads((W/'permitted-old-guide-transform.json').read_text());old=g('show',OLD+':'+transform['path']);assert old==(W/'predecessor-bi-income-tax.md.txt').read_bytes()
expected=old.decode()
for t in transform['exact_replacements']:
 assert expected.count(t['before'])==1;expected=expected.replace(t['before'],t['after'])
assert read(transform['path'])==expected.encode()
kept=[]
for row in json.loads((W/'preservation-baseline.json').read_text())['files']:
 b=g('show',OLD+':'+row['path']);assert sha(b)==row['sha256'];assert g('rev-parse',OLD+':'+row['path']).decode().strip()==row['blob']
 if row['treatment']=='byte-identical':
  assert read(row['path'])==b;kept.append({**row,'review_result':'exact frozen and working bytes match'})
units=json.loads((W/'old-topic-destinations.json').read_text())['all_current_old_guide_body_units'];assert len(units)==294
all_old=[]
for p in g('ls-tree','-r','--name-only',OLD,'skills/burundi').decode().splitlines():
 if not p.endswith('.md') or p.endswith('/README.md'):continue
 text=g('show',OLD+':'+p).decode();parts=re.split(r'\n\s*\n',text.split('---',2)[2])
 for i,t in enumerate(parts,1):
  if t.strip():all_old.append((p,i,t))
# Independently check every claimed old block and its actual destination, then full-file literal transform proves completeness.
reviewed=[]
for row in units:
 p=row['path'];t=row['old_text'];assert sha(t.encode())==row['sha256'];assert t in g('show',OLD+':'+p).decode()
 current=read(p).decode();status='preserved exact'
 if t not in current:
  found=[]
  for rep in transform['exact_replacements']:
   if rep['before'].strip() in t:
    new=t.replace(rep['before'].strip(),rep['after'].strip());assert new in current;found.append(rep)
  assert found,row;status='permitted H1 version or exact single-rate migration'
 reviewed.append({**row,'independent_destination_result':status})
(E/'old-topic-review.json').write_text(json.dumps({'old_commit':OLD,'all_294_destinations_checked':True,'units':reviewed},ensure_ascii=False,indent=2)+'\n')
source=[]
for row in json.loads((W/'source-artifacts.json').read_text()):
 b=(R.parent/'sources'/row['path']).read_bytes();assert sha(b)==row['sha256'];source.append({**row,'review_hash_result':'match'})
new=read('skills/burundi/bi-capital-income-tax.md').decode();fm=skill_checks.read_frontmatter(new)
assert 'openaccountants-cta-block' not in new
assert not any(k in fm for k in ['review_status','trust_label','license','authored_by','reviewed_by','reviewed_on'])
# Whole old bytes replay preserves original CTA and platform keys without introducing/removing any.
md=read('skills/burundi/README.md').decode();oldmd=g('show',OLD+':skills/burundi/README.md').decode();assert md.split('partial:\n',1)[1].split('\n---',1)[0]==oldmd.split('partial:\n',1)[1].split('\n---',1)[0]
env=dict(os.environ);env['PYTHONPATH']='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps'
commands=[['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['python3','scripts/check-sync-integrity.py','--base',BASE,'--mode','audit','--strict-metadata'],['python3','scripts/check-examples.py','--require','skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md'],['git','diff','--check',BASE,HEAD]]
outputs=[]
for cmd in commands:
 p=subprocess.run(cmd,cwd=R,env=env,capture_output=True,text=True);outputs.append({'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
record={'head':HEAD,'content_commit':'084e8cf0f0bb8b1efe4561f8c35b1040f19dc94c','actual_full_base':BASE,'old_predecessor':OLD,'shape_checks':checks,'preservation':kept,'preserved_guide_bodies':sum(r['path'].startswith('skills/') for r in kept),'preserved_evidence':sum(r['path'].startswith('evidence/') for r in kept),'old_individual_sha256':sha(old),'current_individual_sha256':sha(read(transform['path'])),'capital_guide_sha256':sha(new.encode()),'294_old_unit_destinations':'pass','seven_partial_strings':'exact','source_artifacts':source,'commands':outputs,'all_requested_commands_passed':all(p['exit_code']==0 for p in outputs),'template_category_finding':{'actual':fm['category'],'required':'international','authority':'docs/skill-template.md Required keys and Category vocabulary, new files'},'incidental_invocation':{'command':'python3 scripts/validate-guides.py --help','outcome':'Script has no help switch; it ran full-tree validation and reported stale index.json and llms-full.txt. No files changed. Required changed-only no-index run is recorded separately.'}}
(E/'mechanical-checks.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k in ['head','actual_full_base','preserved_guide_bodies','preserved_evidence','capital_guide_sha256','commands','all_requested_commands_passed','template_category_finding']},ensure_ascii=False,indent=2))
