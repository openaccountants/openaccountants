#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,os,re,subprocess
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
HEAD='d91f12a172626fb9c4ee9ee69f860dd410856492';OLD='0a85c3bd65f4dc30edf9319cf52d04c395a1d305';BASE='db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(b):return hashlib.sha256(b).hexdigest()
assert git('rev-parse','HEAD').decode().strip()==HEAD
repair=json.loads((ROOT/'evidence/ledgers/chad-repair-1/writer-repair.json').read_text())
updated={}
for name,wanted in repair['after_sha256'].items():
 b=(ROOT/name).read_bytes(); updated[name]={'sha256':sha(b),'matches_frozen_commit':b==git('show',f'{HEAD}:{name}'),'matches_repair_receipt':sha(b)==wanted};assert b==git('show',f'{HEAD}:{name}') and sha(b)==wanted
unchanged_names=['skills/chad/README.md','evidence/ledgers/chad-old-topics.md','evidence/ledgers/chad-draft-20261101/candidate-manifest.json','evidence/ledgers/chad-draft-20261101/source-record.json']
unchanged_names+=list(json.loads((ROOT/'evidence/ledgers/chad-draft-20261101/source-record.json').read_text())['legacy_sha256'])
unchanged_names=[f'skills/chad/{name}' if '/' not in name else name for name in unchanged_names]
unchanged={}
for name in unchanged_names:
 b=(ROOT/name).read_bytes(); unchanged[name]={'sha256':sha(b),'matches_original_candidate':b==git('show',f'{OLD}:{name}')};assert b==git('show',f'{OLD}:{name}')
path='skills/chad/td-import-exemption-eligibility.md'; new=(ROOT/path).read_text();old=git('show',f'{OLD}:{path}').decode()
examples=lambda text:re.findall(r'```oa-check\n.*?\n```',text,re.S)
assert examples(new)==examples(old) and len(examples(new))==2
sources={}
for name in ['arrete-135-review-20261101.pdf','finance-law-review-20261101.pdf']:
 p=ROOT/'../sources'/name;sources[name]={'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'private_path':str(p.resolve())}
assert sources['finance-law-review-20261101.pdf']['sha256']=='7bc46241a7c7586d9eece4fb5c95a6587ba637732480b7b4c8cfbf31112d7fd2'
assert sources['arrete-135-review-20261101.pdf']['sha256']=='f92a1e4568b8ac1fead585400209de4ec327a18bd5a9728e1687f59c05758f5a'
env=dict(os.environ,PYTHONPATH='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps')
commands=[['python3','evidence/ledgers/chad-review-closure-1/pinned-validation.py'],['python3','scripts/skill_checks.py',path],['python3','scripts/check-examples.py','--require',path],['git','status','--short']]
results=[]
for argv in commands:
 p=subprocess.run(argv,cwd=ROOT,env=env,text=True,capture_output=True);results.append({'argv':argv,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0
result={'candidate_commit':HEAD,'original_candidate':OLD,'pinned_base':BASE,'reviewed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'updated_files':updated,'unchanged_files':unchanged,'both_oa_check_blocks_unchanged':True,'private_sources':sources,'commands':results,'decision':'Original P1 closed. Accept only the defined non-wheat eligibility working paper scope, with all wheat held and all wider filing/law matters unresolved.'}
(OUT/'check-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Pinned candidate/repair hashes matched; 10 preserved files matched original; 2 examples unchanged; all 3 validation commands passed.')
