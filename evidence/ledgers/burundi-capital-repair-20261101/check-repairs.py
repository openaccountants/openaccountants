#!/usr/bin/env python3
"""Check only the explicit R1–R4 working candidate and preserved frozen inputs."""
from pathlib import Path
import hashlib,json,subprocess,sys,re
E=Path(__file__).resolve().parent;R=E.parents[2];W=E.parent/'burundi-capital-20261101';BASE='29c8b477f1d659c0042a6ae9de5b10ef615a98d0'
def g(*a):return subprocess.check_output(['git',*a],cwd=R)
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return (R/p).read_bytes() if (R/p).exists() else g('show',BASE+':'+p)
assert g('rev-parse','HEAD').decode().strip()==BASE,'No commit permitted before focused closure'
baseline=json.loads((E/'preservation-baseline.json').read_text());literal=json.loads((E/'literal-repairs.json').read_text())
old=g('show',BASE+':skills/burundi/bi-capital-income-tax.md');assert sha(old)==literal['original_guide_sha256'];expected=old.decode()
for row in literal['exact_replacements']:
 assert expected.count(row['before'])==row['occurrences'],row
 expected=expected.replace(row['before'],row['after'])
new=read('skills/burundi/bi-capital-income-tax.md');assert new==expected.encode();assert sha(new)==literal['result_guide_sha256']
kept=[]
for row in baseline['prior_tracked_files']:
 oldbytes=g('show',BASE+':'+row['path']);assert sha(oldbytes)==row['sha256'];assert g('rev-parse',BASE+':'+row['path']).decode().strip()==row['git_blob']
 if row['treatment']=='byte-identical':assert read(row['path'])==oldbytes,row['path'];kept.append(row['path'])
for row in baseline['review_files']:assert sha((R/row['path']).read_bytes())==row['sha256'],row['path']
assert sha(read('evidence/ledgers/burundi-capital-review-20261101/review-freeze.json'))==baseline['review_freeze_sha256']
oldrows=json.loads((W/'bi-capital-income-tax.json').read_text());newrows=json.loads((E/'effective-47-row-ledger.json').read_text());delta=json.loads((E/'five-row-before-after.json').read_text())
changed={'C15','C19','C35','C37','C45'};assert len(oldrows)==len(newrows)==47
for before,after in zip(oldrows,newrows):
 assert before['id']==after['id']
 if before['id'] not in changed:assert before==after
 else:
  d=next(x for x in delta['corrections'] if x['id']==before['id']);assert before==d['before'];assert after==d['after']
assert len(delta['corrections'])==5 and delta['new_rule_rows_appended']==0
for row in json.loads((E/'source-artifacts-supplement.json').read_text()):assert sha((R.parent/'sources'/row['path']).read_bytes())==row['sha256'],row['path']
# Exact old-Guide migration is unchanged, including all platform keys and CTA bytes.
t=json.loads((W/'permitted-old-guide-transform.json').read_text());pre=g('show',t['base']+':'+t['path']);assert pre==(W/'predecessor-bi-income-tax.md.txt').read_bytes();replay=pre.decode()
for rep in t['exact_replacements']:assert replay.count(rep['before'])==1;replay=replay.replace(rep['before'],rep['after'])
assert replay.encode()==read(t['path'])
# No numbers or calculations changed: case1 only renames payer-identifying input variables.
oldblocks=re.findall(r'```oa-check\n(.*?)```',old.decode(),re.S);blocks=re.findall(r'```oa-check\n(.*?)```',new.decode(),re.S);assert len(oldblocks)==len(blocks)==3
assert blocks[0].replace('seller_paid_duty_low','duty_low').replace('seller_paid_duty_high','duty_high')==oldblocks[0]
assert blocks[1:]==oldblocks[1:]
sys.path.insert(0,str(R/'scripts'));import skill_checks
checks={p:skill_checks.run_all(p) for p in ['skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md']}
assert all(len(v)==15 and not any(v.values()) for v in checks.values()),checks
fm=skill_checks.read_frontmatter(new.decode());assert fm['category']=='international';assert str(fm['version'])=='0.2';assert fm['tier'] in ('2',2)
assert not any(k in fm for k in ['review_status','trust_label','license','authored_by','reviewed_by','reviewed_on'])
assert 'openaccountants-cta-block' not in new.decode()
# Seven partial declarations and README are preserved, not status-promoted.
assert read('skills/burundi/README.md')==g('show',BASE+':skills/burundi/README.md')
print(json.dumps({'result':'pass','candidate_sha256':sha(new),'frozen_head_unchanged':BASE,'literal_replacements':len(literal['exact_replacements']),'prior_tracked_files_unchanged':len(kept),'old_guide_bodies_unchanged_since_frozen_capital_head':sum(p.startswith('skills/burundi/') and p!='skills/burundi/README.md' for p in kept),'review_files_unchanged':len(baseline['review_files']),'original_47_rows_preserved':True,'effective_corrected_rows':sorted(changed),'effective_other_rows_equal':42,'new_rule_rows':0,'three_original_case_calculations_unchanged':True,'shape_checks':checks,'seven_partial_strings_and_readme_unchanged':True},ensure_ascii=False,indent=2))
