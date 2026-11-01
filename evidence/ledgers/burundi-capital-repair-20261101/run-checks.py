#!/usr/bin/env python3
from pathlib import Path
import subprocess,os,json,sys
E=Path(__file__).resolve().parent;R=E.parents[2]
env=dict(os.environ);env['PYTHONPATH']='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps'
base=subprocess.check_output(['git','merge-base','HEAD','origin/main'],cwd=R).decode().strip()
commands=[['python3','evidence/ledgers/burundi-capital-repair-20261101/check-repairs.py'],['python3','scripts/check-examples.py','--require','skills/burundi/bi-capital-income-tax.md','skills/burundi/bi-income-tax.md'],['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['python3','scripts/check-sync-integrity.py','--base',base,'--worktree','--mode','audit','--strict-metadata'],['git','diff','--check',base]]
r={'status':'uncommitted working candidate; not a committed-validation receipt','frozen_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip(),'actual_full_merge_base':base,'commands':[],'all_passed':False}
for cmd in commands:
 p=subprocess.run(cmd,cwd=R,env=env,capture_output=True,text=True);out={'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr};r['commands'].append(out);(E/'working-candidate-checks.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
 if p.returncode:sys.exit(p.returncode)
r['all_passed']=True;(E/'working-candidate-checks.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
