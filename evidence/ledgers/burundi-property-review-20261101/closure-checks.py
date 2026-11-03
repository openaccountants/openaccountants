#!/usr/bin/env python3
"""Independently validate the uncommitted R1–R4 candidate against immutable writer and review history."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent;W=R/'evidence/ledgers/burundi-property-20261101'
H='f2ae4ea5b9463c5e959b2e3e44147e49facafbed';B='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
def g(*a):return subprocess.check_output(['git',*a],cwd=R)
def old(p):return g('show',H+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def current(p):return (R/p).read_bytes()
receipt=json.loads((W/'repair-candidate.json').read_text())
for x in receipt['files']:assert sha(current(x['path']))==x['sha256'],x['path']
p='skills/burundi/bi-property-transactions.md';before=old(p).decode();after=current(p).decode()
repairs=json.loads((W/'reviewer-repairs.json').read_text())
replayed=before
for c in repairs['changes']:
 assert c['path']==p
 assert replayed.count(c['before'])==1,c['finding']
 replayed=replayed.replace(c['before'],c['after'],1)
assert replayed==after,'Candidate contains changes beyond literal repairs'
assert before.split('---',2)[1]==after.split('---',2)[1], 'Frontmatter substantive metadata changed'
section=lambda s:s.split('## Two worked examples that recompute\n',1)[1].split('## Ask the client first',1)[0]
assert section(before)==section(after)
blocks=lambda s:re.findall(r'^```oa-check\n.*?^```',s,re.M|re.S)
assert len(blocks(after))==4 and blocks(before)==blocks(after)
l='evidence/ledgers/burundi-property-20261101/bi-property-transactions.json';oldrows=json.loads(old(l));rows=json.loads(current(l))
assert len(oldrows)==66 and len(rows)==72 and oldrows==rows[:66]
assert [x['id'] for x in rows[66:]]==['P67','P68','P69','P70','P71','P72']
h='evidence/ledgers/burundi-property-20261101/ledgers/bi-property-transactions.md';assert current(h).startswith(old(h))
# Compare actual source identities and repaired row evidence to those identities.
sourceids=json.loads(old('evidence/ledgers/burundi-property-20261101/source-identities.json'));sourcechecks=[]
for k,s in sourceids.items():
 b=(R.parent/'sources'/s['path']).read_bytes();assert sha(b)==s['sha256'];sourcechecks.append(dict(id=k,sha256=sha(b),bytes=len(b)))
for row in rows[66:]:
 assert row['read_date']=='2026-11-01'
 assert any(row['source_sha256']==s['sha256'] and row['official_url']==s['url'] for s in sourceids.values())
 for key in ['section','act','article','official_url','exact_quote','read_date','source_sha256','pdf_locator','source_read_scope']:assert row[key]
# Re-read scope disclosures and repairs are specific and no genuine hold removed.
for claim in ['94, 103–104','207, 215, 217, 226–227','108–109, 226, 235, 237','broader interpretation of the exact BIF 100,000,000']:
 assert claim in after,claim
oldhold=before.split('Not yet confirmed: ',1)[1].split(' An indexed',1)[0]
newhold=after.split('Not yet confirmed: ',1)[1].split(' An indexed',1)[0]
assert oldhold.replace('construction implementing order and permit forms;','construction implementing order and permit forms, including broader interpretation of the exact BIF 100,000,000 permit-insurance condition and current required insurance evidence;')==newhold
pres=[]
allbase=g('ls-tree','-r','--name-only',B).decode().splitlines()
paths=[x for x in allbase if (x.startswith('skills/burundi/') and x.endswith('.md') and not x.endswith('/README.md')) or x.startswith('evidence/ledgers/burundi-')]
assert len(paths)==22
for path in paths:
 b=g('show',B+':'+path);assert old(path)==b
 exists=(R/path).exists()
 if exists:assert current(path)==b
 pres.append(dict(path=path,sha256=sha(b),git_blob=g('rev-parse',B+':'+path).decode().strip(),worktree='identical' if exists else 'sparse absent; immutable Git identity checked'))
assert current('skills/burundi/README.md')==old('skills/burundi/README.md')
oldproof=[x for x in g('ls-tree','-r','--name-only',H,'--','evidence/ledgers/burundi-property-20261101').decode().splitlines() if x not in [l,h]]
for path in oldproof:assert current(path)==old(path),path
initial=json.loads((E/'review-freeze.json').read_text())
for x in initial['files']:assert sha(current(x['path']))==x['sha256'],x['path']+' initial review overwritten'
sys.path.insert(0,str(R/'scripts'));import skill_checks
shape=skill_checks.run_checks(p,after,skill_checks.read_frontmatter(after));assert len(shape)==15 and not any(shape.values())
fm=skill_checks.read_frontmatter(after)
for k in ['review_status','license','authored_by','trust_label','drafted_by','approved_by','validation_status','validated','reviewed_by','reviewed_on','verified_by']:assert k not in fm
assert 'openaccountants-cta-block' not in after
commands=[]
for args in [['python3','scripts/check-examples.py','--require',p],['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['python3','scripts/check-sync-integrity.py','--base',B,'--mode','audit','--strict-metadata'],['git','diff','--check']]:
 r=subprocess.run(args,cwd=R,capture_output=True,text=True);commands.append(dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr));assert r.returncode==0,commands[-1]
result=dict(result='pass',frozen_writer_head=H,base=B,guide_sha256=sha(current(p)),repair_candidate_sha256=sha((W/'repair-candidate.json').read_bytes()),precise_guide_repair_replay=True,frontmatter_unchanged=True,original_ledger_objects_preserved=66,new_ledger_rows=6,total_ledger_rows=72,human_ledger_original_exact_prefix=True,original_four_case_section_preserved=True,oa_check_blocks_preserved=4,prior_files=pres,old_guides_preserved=8,prior_evidence_preserved=14,replaced_old_units=0,frozen_property_evidence_preserved=len(oldproof),initial_review_files_preserved=len(initial['files']),initial_review_receipt_sha256=sha((E/'review-freeze.json').read_bytes()),readme_unchanged=True,source_bytes=sourcechecks,shape_checks=shape,commands=commands)
(E/'closure-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['prior_files','commands','shape_checks','source_bytes']},indent=2))
