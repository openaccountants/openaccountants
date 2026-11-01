#!/usr/bin/env python3
"""Verify accepted repairs plus exactly permitted status changes, never alter historical evidence."""
from pathlib import Path
import json,hashlib,subprocess,sys,re
E=Path(__file__).resolve().parent;R=E.parents[2];HEAD='29c8b477f1d659c0042a6ae9de5b10ef615a98d0'
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
def read(p):return (R/p).read_bytes() if (R/p).exists() else git('show','HEAD:'+p)
baseline=json.loads((E/'preservation-baseline.json').read_text());status=json.loads((E/'status-application.json').read_text());permission=json.loads(read(status['permission_path']))
assert sha(read(status['permission_path']))==status['permission_sha256'];assert sha(read(status['closure_path']))==status['closure_sha256']
assert len(permission['files'])==2;assert sum(len(f['replacements']) for f in permission['files'])==5
literal=json.loads(read('evidence/ledgers/burundi-capital-repair-20261101/literal-repairs.json'))
original=git('show',HEAD+':skills/burundi/bi-capital-income-tax.md');accepted=original.decode()
for change in literal['exact_replacements']:
 assert accepted.count(change['before'])==change['occurrences'];accepted=accepted.replace(change['before'],change['after'])
assert sha(accepted.encode())==literal['result_guide_sha256']=='233d9e7f0e2df6e1d6c65df8713950d7e97126cfecb564a051fdb8af8c238510'
for row in permission['files']:
 before=accepted if row['path'].endswith('bi-capital-income-tax.md') else git('show',HEAD+':'+row['path']).decode()
 assert sha(before.encode())==row['before_sha256']
 for change in row['replacements']:
  assert before.count(change['before'])==change['required_occurrences'];before=before.replace(change['before'],change['after'])
 assert read(row['path'])==before.encode();assert sha(read(row['path']))==row['after_sha256']
preserved=[]
for row in baseline['files']:
 if not row['status_change_permitted']:
  assert sha(read(row['path']))==row['sha256'],row['path'];preserved.append(row['path'])
assert sha(read('evidence/ledgers/burundi-capital-review-20261101/review-freeze.json'))=='d979284df7a131f493db0c6b347fad58657d6296a3d4d1b44c386d758c984001'
W=E.parent/'burundi-capital-20261101';C=E.parent/'burundi-capital-repair-20261101'
a=json.loads((W/'bi-capital-income-tax.json').read_text());b=json.loads((C/'effective-47-row-ledger.json').read_text());delta=json.loads((C/'five-row-before-after.json').read_text())
assert len(a)==len(b)==47;ids={'C15','C19','C35','C37','C45'}
for old,new in zip(a,b):
 if old['id'] in ids:
  change=next(c for c in delta['corrections'] if c['id']==old['id']);assert change['before']==old and change['after']==new
 else:assert old==new
# Keep the old individual migration exact, including protected platform keys and suffix.
t=json.loads((W/'permitted-old-guide-transform.json').read_text());old=git('show',t['base']+':'+t['path']);assert old==(W/'predecessor-bi-income-tax.md.txt').read_bytes();replay=old.decode()
for change in t['exact_replacements']:assert replay.count(change['before'])==1;replay=replay.replace(change['before'],change['after'])
assert read(t['path'])==replay.encode()
md=read('skills/burundi/README.md').decode();oldmd=git('show',HEAD+':skills/burundi/README.md').decode();assert md.split('partial:\n',1)[1].split('\n---',1)[0]==oldmd.split('partial:\n',1)[1].split('\n---',1)[0]
new=read('skills/burundi/bi-capital-income-tax.md').decode();sys.path.insert(0,str(R/'scripts'));import skill_checks
checks={p:skill_checks.run_all(p) for p in ['skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md']};assert all(len(v)==15 and not any(v.values()) for v in checks.values()),checks
fm=skill_checks.read_frontmatter(new);assert fm['category']=='international';assert str(fm['version'])=='0.2';assert fm['tier'] in ('2',2);assert 80<=len(fm['description'].split())<=150
assert not any(k in fm for k in ['review_status','trust_label','license','authored_by','reviewed_by','reviewed_on']);assert 'openaccountants-cta-block' not in new
assert re.findall(r'```oa-check\n(.*?)```',accepted,re.S)==re.findall(r'```oa-check\n(.*?)```',new,re.S)
source_count=0
for p in [W/'source-artifacts.json',C/'source-artifacts-supplement.json']:
 for s in json.loads(p.read_text()):assert sha((R.parent/'sources'/s['path']).read_bytes())==s['sha256'];source_count+=1
print(json.dumps({'result':'pass','guide_sha256':sha(new.encode()),'readme_sha256':sha(md.encode()),'exact_status_literals':5,'accepted_repair_literals':len(literal['exact_replacements']),'preserved_files':len(preserved),'preserved_old_guide_bodies':sum(p.startswith('skills/burundi/') for p in preserved),'original_47_rows_and_review_evidence_preserved':True,'effective_rows':47,'corrected_ids':sorted(ids),'other_equal_rows':42,'source_artifact_hashes_checked':source_count,'all_seven_partial_strings_exact':True,'shape_checks':checks,'description_words':len(fm['description'].split())},ensure_ascii=False,indent=2))
