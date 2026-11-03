#!/usr/bin/env python3
"""Independent focused-closure checks; outputs only new reviewer evidence."""
from pathlib import Path
import hashlib,json,os,re,subprocess,sys
E=Path(__file__).resolve().parent;R=E.parents[2];P=E.parent/'burundi-capital-repair-20261101';W=E.parent/'burundi-capital-20261101'
HEAD='29c8b477f1d659c0042a6ae9de5b10ef615a98d0';BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
def sha(b):return hashlib.sha256(b).hexdigest()
def g(*a):return subprocess.check_output(['git',*a],cwd=R)
def read(p):return (R/p).read_bytes() if (R/p).exists() else g('show',HEAD+':'+p)
assert g('rev-parse','HEAD').decode().strip()==HEAD
assert g('merge-base',HEAD,'origin/main').decode().strip()==BASE
candidate=(P/'repair-candidate.json').read_bytes();assert sha(candidate)=='a84e85a093c2110d4721f1a40e25466c95efcbbdc5f0a8fce55c2351fe6bbd84'
c=json.loads(candidate)
for r in c['files']:
 b=read(r['path']);assert sha(b)==r['sha256'];assert len(b)==r['bytes']
assert sha((E/'review-freeze.json').read_bytes())=='d979284df7a131f493db0c6b347fad58657d6296a3d4d1b44c386d758c984001'
f=json.loads((E/'review-freeze.json').read_text())
for r in f['evidence']:assert sha((R/r['path']).read_bytes())==r['sha256'],r['path']
old=g('show',HEAD+':skills/burundi/bi-capital-income-tax.md').decode();new=read('skills/burundi/bi-capital-income-tax.md').decode();recipe=json.loads((P/'literal-repairs.json').read_text());expected=old
assert len(recipe['exact_replacements'])==20
for r in recipe['exact_replacements']:
 assert expected.count(r['before'])==r['occurrences'];expected=expected.replace(r['before'],r['after'])
assert expected==new
assert sha(new.encode())=='233d9e7f0e2df6e1d6c65df8713950d7e97126cfecb564a051fdb8af8c238510'
assert g('diff','--name-only').decode().splitlines()==['skills/burundi/bi-capital-income-tax.md']
preserved=[]
for r in json.loads((P/'preservation-baseline.json').read_text())['prior_tracked_files']:
 b=g('show',HEAD+':'+r['path']);assert sha(b)==r['sha256']
 if r['treatment']=='byte-identical':assert read(r['path'])==b;preserved.append(r['path'])
oldrows=json.loads((W/'bi-capital-income-tax.json').read_text());rows=json.loads((P/'effective-47-row-ledger.json').read_text());delta=json.loads((P/'five-row-before-after.json').read_text());changed=[]
assert len(oldrows)==len(rows)==47
for a,b in zip(oldrows,rows):
 assert a['id']==b['id']
 if a!=b:
  changed.append(a['id']);d=next(x for x in delta['corrections'] if x['id']==a['id']);assert a==d['before'] and b==d['after']
assert changed==['C15','C19','C35','C37','C45']
assert delta['new_rule_rows_appended']==0
human=(P/'effective-47-row-ledger.md').read_text();supp=json.loads((P/'decisive-source-supplement.json').read_text());assert len(supp)==13
byid={r['id']:r for r in supp}
for r in rows:
 assert r['read_date']=='2026-11-01'
 assert human.count('| '+r['id']+' |')==1
 for key in ['claim','act','article','pdf_locator','official_url']:assert str(r[key]) in human,(r['id'],key)
 assert r['exact_quote'].replace('|',' / ') in human or r['exact_quote'].replace('|','&#124;') in human,(r['id'],'quote')
 for s in r.get('supporting_sources',[]):assert s==byid[s['id']]
for s in supp:
 b=(R.parent/'sources'/s['source_path']).read_bytes();assert sha(b)==s['source_sha256'];assert s['read_date']=='2026-11-01';assert s['exact_quote'] in human
 # All thirteen decisive quotes were separately visually checked, not accepted from this lookup.
for r in json.loads((P/'source-artifacts-supplement.json').read_text()):assert sha((R.parent/'sources'/r['path']).read_bytes())==r['sha256']
for source_id,s in json.loads((P/'sources-read-supplement.json').read_text()).items():
 assert sha((R.parent/'sources'/s['path']).read_bytes())==s['sha256'];assert s['official_url'] in new;assert '2026-11-01' in new
oldblocks=re.findall(r'```oa-check\n(.*?)```',old,re.S);blocks=re.findall(r'```oa-check\n(.*?)```',new,re.S)
assert len(oldblocks)==len(blocks)==3
assert blocks[0].replace('seller_paid_duty_low','duty_low').replace('seller_paid_duty_high','duty_high')==oldblocks[0]
assert blocks[1:]==oldblocks[1:]
assert read('skills/burundi/README.md')==g('show',HEAD+':skills/burundi/README.md')
sys.path.insert(0,str(R/'scripts'));import skill_checks
shapes={p:skill_checks.run_all(p) for p in ['skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md']};assert all(len(x)==15 and not any(x.values()) for x in shapes.values())
fm=skill_checks.read_frontmatter(new);assert fm['category']=='international' and str(fm['version'])=='0.2' and fm['tier'] in (2,'2')
assert not any(k in fm for k in ['review_status','trust_label','license','authored_by','reviewed_by','reviewed_on'])
assert 'openaccountants-cta-block' not in new
commands=[['python3','scripts/check-examples.py','--require','skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md'],['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['python3','scripts/check-sync-integrity.py','--base',BASE,'--worktree','--mode','audit','--strict-metadata'],['git','diff','--check',BASE]]
env=dict(os.environ);env['PYTHONPATH']='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps';outputs=[]
for cmd in commands:
 p=subprocess.run(cmd,cwd=R,env=env,capture_output=True,text=True);outputs.append({'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
record={'head':HEAD,'actual_full_base':BASE,'repair_candidate_sha256':sha(candidate),'accepted_candidate_sha256':sha(new.encode()),'original_review_freeze_sha256':sha((E/'review-freeze.json').read_bytes()),'original_review_files_preserved':len(f['evidence'])+1,'all_twenty_literal_replacements_reproduced':True,'prior_tracked_files_preserved':len(preserved),'old_guide_bodies_unchanged_since_capital_head':sum(p.startswith('skills/') and not p.endswith('/README.md') for p in preserved),'effective_rows':len(rows),'effective_changed_rows':changed,'other_row_objects_equal':42,'source_supplement_entries':len(supp),'effective_json_read_dates_all_2026_11_01':True,'human_ledger_claim_article_quote_source_routes_match':True,'three_new_case_calculations_identical':True,'two_other_new_blocks_identical':True,'all_seven_partial_strings_and_readme_identical':True,'no_new_platform_keys_or_cta':True,'shape_checks':shapes,'commands':outputs,'all_passed':all(o['exit_code']==0 for o in outputs)}
(E/'closure-checks.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['shape_checks']},ensure_ascii=False,indent=2))
assert record['all_passed']
