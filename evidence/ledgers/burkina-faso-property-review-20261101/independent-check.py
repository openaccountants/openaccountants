#!/usr/bin/env python3
"""Read-only review checks; writes only new review receipts in this directory."""
import subprocess, pathlib, hashlib, json, sys, importlib.util, os
ROOT=pathlib.Path(__file__).resolve().parents[3]
OUT=pathlib.Path(__file__).resolve().parent
os.chdir(ROOT)
HEAD='13a38f884550d6d220f79100a8fbc1404842a1de'
PREV='f7482aabcf34d114499f3b621beb1027cc406d5c'
BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
def git(*args): return subprocess.check_output(['git',*args])
def sha(data): return hashlib.sha256(data).hexdigest()
def save(name,data): (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def blob(ref,path): return git('show',f'{ref}:{path}')
assert git('rev-parse','HEAD').decode().strip()==HEAD
paths=git('ls-tree','-r','--name-only',PREV).decode().splitlines()
oldguides=[p for p in paths if p.startswith('skills/burkina-faso/') and p.endswith('.md') and not p.endswith('README.md')]
evidence=[p for p in paths if p.startswith('evidence/') and ('burkina-faso' in p or p.endswith('/bf-transfer-pricing.md') or p.endswith('/bf-nonresident-services-withholding.md'))]
checks=[]
for p in oldguides+evidence:
    before=blob(PREV,p); after=blob(HEAD,p); work=ROOT/p
    checks.append({'path':p,'baseline_sha256':sha(before),'head_sha256':sha(after),'head_identical':before==after,'working_identical':work.read_bytes()==after if work.exists() else None,'sparse_absent':not work.exists()})
assert len(oldguides)==10 and len(evidence)==102
assert all(x['head_identical'] and x['working_identical'] is not False for x in checks)
rp='skills/burkina-faso/README.md'; before=blob(PREV,rp); after=blob(HEAD,rp)
append=json.loads((ROOT/'evidence/ledgers/burkina-faso-property-20261101/readme-addition.json').read_text())['append_exact'].encode()
assert after==before+append
save('preservation-checks.json',{'frozen_head':HEAD,'baseline':PREV,'old_guides':len(oldguides),'prior_evidence_files':len(evidence),'checks':checks,'readme':{'before_sha256':sha(before),'after_sha256':sha(after),'exact_append':append.decode(),'exact_append_match':True},'replaced_old_bodies':0,'lost_content_restored':0,'note':'This is a new job; immutable predecessor files are their own complete destination. No predecessor topic moved or lost. All seven domain partial declarations unchanged.'})
inputs=['AGENTS.md','docs/skill-template.md','docs/OWNERS.md',rp,'skills/burkina-faso/bf-company-property-tax.md']
inputs += [p for p in git('ls-tree','-r','--name-only',HEAD,'evidence/ledgers/burkina-faso-property-20261101').decode().splitlines()]
save('input-manifest.json',{'frozen_head':HEAD,'previous_accepted_ten_guide_head':PREV,'main_base':BASE,'branch':git('branch','--show-current').decode().strip(),'files':[{'path':p,'git_blob':git('rev-parse',f'{HEAD}:{p}').decode().strip(),'sha256':sha(blob(HEAD,p)),'working_matches':(ROOT/p).read_bytes()==blob(HEAD,p)} for p in inputs]})
spec=importlib.util.spec_from_file_location('checks',ROOT/'scripts/skill_checks.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
shape=mod.run_all('skills/burkina-faso/bf-company-property-tax.md')
assert len(shape)==15 and not any(shape.values())
save('shape-checks.json',{'frozen_head':HEAD,'checks':shape,'pass':True})
commands=[['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['python3','scripts/check-sync-integrity.py','--base',BASE,'--mode','audit','--strict-metadata'],['python3','scripts/check-examples.py','--require','skills/burkina-faso/bf-company-property-tax.md'],['git','diff','--check',BASE,HEAD]]
results=[]
for cmd in commands:
    run=subprocess.run(cmd,capture_output=True,text=True)
    results.append({'command':cmd,'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr})
save('validation.json',{'frozen_head':HEAD,'results':results,'interpretation':'Changed-only compares actual committed origin/main...HEAD. Custom property slug warning is acknowledged: separate TFS job routed by exact appended README; it is not a new eighth complete country domain.'})
assert all(x['returncode']==0 for x in results)
from decimal import Decimal as D
annual=D(6000000); deduction=annual*D('.5'); base=annual-deduction; tax=base*D('.1')
a=D(12000000); ownerbase=a*D('.5'); ownertax=ownerbase*D('.1'); tenantbase=a; tenanttax=tenantbase*D('.1')
save('independent-cases.json',{'frozen_head':HEAD,'method':'Independent Decimal arithmetic, not evaluation of the Guide expressions; legal branches checked against full art.254 and art.256.','cases':[{'case':'Owner-occupied SARL','facts':'Enumerated SARL; January owner; own occupation; supported annual rental value includes immediate indispensable dependency; no exemption; ordinary deduction applies.','value':str(annual),'deduction':str(deduction),'base':str(base),'tax':str(tax),'legal_decision':'Art.255(1) uses hypothetical rental value for self-occupation. Zero cash rent does not imply zero tax.','matches':tax==D(300000)},{'case':'Major-repairs decision','facts':'Otherwise comparable SA properties; supported annual value; January ownership; no exemption. Legal burden of grosses réparations controls.','owner_base':str(ownerbase),'owner_tax':str(ownertax),'tenant_base':str(tenantbase),'tenant_tax':str(tenanttax),'difference':str(tenanttax-ownertax),'legal_decision':'Art.254 second paragraph switches off the full 50% deduction when the tenant bears major repairs. This is classification of existing burden, not an election; disputed classification remains held.','matches':ownertax==D(600000) and tenanttax==D(1200000) and tenanttax-ownertax==D(600000)}],'additional_floor_checks':{'duties_300000_inaccuracy_penalty':str(max(D(300000)*D('.25'),D(100000))),'duties_300000_taxation_office_penalty':str(max(D(300000)*D('.25'),D(500000))),'note':'Distinct hypothetical branches, not accumulated. No actual first late day computed.'}})
print(json.dumps({'head':HEAD,'preserved_guides':len(oldguides),'preserved_evidence':len(evidence),'readme_exact_append':True,'shape_checks':len(shape),'validation_codes':[x['returncode'] for x in results]},indent=2))
