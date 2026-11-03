#!/usr/bin/env python3
from pathlib import Path
import json,os,subprocess,sys
E=Path(__file__).resolve().parent;R=E.parents[2]
phase=sys.argv[1] if len(sys.argv)>1 else 'precommit'
assert phase in ('precommit','committed')
env=dict(os.environ);env['PYTHONPATH']='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps'
def g(*a):return subprocess.check_output(['git',*a],cwd=R).decode().strip()
base=g('merge-base','HEAD','origin/main');head=g('rev-parse','HEAD')
commands=[['python3','evidence/ledgers/burundi-capital-20261101/writer-check.py'],['python3','scripts/check-examples.py','--require','skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md']]
if phase=='committed':
 commands+=[['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['python3','scripts/check-sync-integrity.py','--base',base,'--mode','audit','--strict-metadata']]
commands += [['git','diff','--check',base,'HEAD'] if phase=='committed' else ['git','diff','--check']]
record={'phase':phase,'head':head,'actual_full_merge_base':base,'actual_origin_main':g('rev-parse','origin/main'),'commands':[],'all_passed':False}
output=E/(phase+'-validation.json')
for cmd in commands:
 result=subprocess.run(cmd,cwd=R,env=env,capture_output=True,text=True)
 row={'command':cmd,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr};record['commands'].append(row)
 output.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'command':cmd,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr},ensure_ascii=False))
 if result.returncode:sys.exit(result.returncode)
record['all_passed']=True;output.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
