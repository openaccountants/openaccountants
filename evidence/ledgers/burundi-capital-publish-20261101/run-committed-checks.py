#!/usr/bin/env python3
from pathlib import Path
import json,os,subprocess,sys
E=Path(__file__).resolve().parent;R=E.parents[2]
env=dict(os.environ);env['PYTHONPATH']='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps'
def git(*a):return subprocess.check_output(['git',*a],cwd=R).decode().strip()
base=git('merge-base','HEAD','origin/main');head=git('rev-parse','HEAD')
record={'validation_kind':'actual committed changed-only scope; no index generation','content_commit':head,'actual_full_merge_base':base,'actual_origin_main':git('rev-parse','origin/main'),'commands':[],'all_passed':False}
commands=[['python3','evidence/ledgers/burundi-capital-publish-20261101/check-publish.py'],['python3','scripts/check-examples.py','--require','skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md'],['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['python3','scripts/check-sync-integrity.py','--base',base,'--mode','audit','--strict-metadata'],['git','diff','--check',base,'HEAD']]
for cmd in commands:
 p=subprocess.run(cmd,cwd=R,env=env,capture_output=True,text=True);row={'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr};record['commands'].append(row);(E/'committed-validation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(json.dumps(row,ensure_ascii=False))
 if p.returncode:sys.exit(p.returncode)
record['all_passed']=True;(E/'committed-validation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
