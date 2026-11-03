#!/usr/bin/env python3
"""Independent immutable-candidate and preservation verification; no network or writes outside this evidence directory."""
from pathlib import Path
import hashlib,json,subprocess,sys
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[3]; E=Path(__file__).resolve().parent
BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'; HEAD='f2ae4ea5b9463c5e959b2e3e44147e49facafbed'; CONTENT='296a542f79277b98bd02cb00831b1517a5c2ff34'
def git(*args):return subprocess.check_output(['git',*args],cwd=R)
def raw(commit,path):return git('show',f'{commit}:{path}')
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(commit,p):
 b=raw(commit,p);return dict(path=p,blob=git('rev-parse',f'{commit}:{p}').decode().strip(),sha256=sha(b),bytes=len(b))
allbase=git('ls-tree','-r','--name-only',BASE).decode().splitlines()
oldguides=[p for p in allbase if p.startswith('skills/burundi/') and p.endswith('.md') and not p.endswith('/README.md')]
oldproof=[p for p in allbase if p.startswith('evidence/ledgers/burundi-')]
assert len(oldguides)==8 and len(oldproof)==14,(oldguides,oldproof)
preserved=[]
for p in oldguides+oldproof:
 a=identity(BASE,p);b=identity(HEAD,p);assert a==b,p
 exists=(R/p).exists()
 if exists:assert sha((R/p).read_bytes())==a['sha256'],p+' worktree drift'
 preserved.append(dict(**a,result='byte-identical at frozen head',worktree='byte-identical' if exists else 'not materialised in sparse checkout; Git blob checked'))
P='skills/burundi/bi-property-transactions.md'; body=raw(HEAD,P).decode(); assert raw(CONTENT,P)==raw(HEAD,P)
sys.path.insert(0,str(R/'scripts'));import skill_checks
fm=skill_checks.read_frontmatter(body); shape=skill_checks.run_checks(P,body,fm)
assert len(shape)==15 and not any(shape.values()),shape
for k in ['review_status','license','authored_by','trust_label','drafted_by','approved_by','validation_status','validated','reviewed_by','reviewed_on','verified_by']:
 assert k not in fm,k
assert 'openaccountants-cta-block' not in body
# Direct independent enumeration, not the writer's preservation manifest.
changes=git('diff','--name-status',BASE,HEAD,'--','skills/burundi').decode().splitlines()
assert changes==['M\tskills/burundi/README.md','A\t'+P],changes
oldreadme=raw(BASE,'skills/burundi/README.md').decode(); newreadme=raw(HEAD,'skills/burundi/README.md').decode()
assert oldreadme.split('---',2)[1]==newreadme.split('---',2)[1], 'seven partial classifications or routing changed'
ledgerpath='evidence/ledgers/burundi-property-20261101/bi-property-transactions.json'; ledger=json.loads(raw(HEAD,ledgerpath))
assert [x['id'] for x in ledger]==['P%02d'%i for i in range(1,67)]
sourceids=json.loads(raw(HEAD,'evidence/ledgers/burundi-property-20261101/source-identities.json'))
sources=[]
for k,s in sourceids.items():
 b=(R.parent/'sources'/s['path']).read_bytes(); assert sha(b)==s['sha256'] and len(b)==s['bytes']
 sources.append(dict(id=k,path=s['path'],sha256=sha(b),bytes=len(b),official_url=s['url']))
commands=[]
for args in [['python3','scripts/check-examples.py','--require',P],['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['python3','scripts/check-sync-integrity.py','--base',BASE,'--mode','audit','--strict-metadata'],['git','diff','--check',BASE,HEAD]]:
 p=subprocess.run(args,cwd=R,capture_output=True,text=True);commands.append(dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,commands[-1]
result=dict(base=BASE,frozen_head=HEAD,content_commit=CONTENT,guide=identity(HEAD,P),ledger=identity(HEAD,ledgerpath),ledger_rows=66,shape_checks=shape,preservation=preserved,old_guides_preserved=8,prior_evidence_preserved=14,replaced_old_body_units=0,country_skill_diff=changes,readme_frontmatter_unchanged=True,platform_owned_keys_added=[],manual_cta_added=False,source_bytes=sources,commands=commands)
(E/'mechanical-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(result='pass',shape_checks=len(shape),ledger_rows=66,old_guides=8,prior_evidence=14,replaced_old_body_units=0,commands=commands),indent=2))
