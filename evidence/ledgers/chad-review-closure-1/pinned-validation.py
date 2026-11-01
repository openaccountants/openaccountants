#!/usr/bin/env python3
"""Run existing changed-only validator with its diff pinned, without moving Git refs."""
from pathlib import Path
import importlib.util, subprocess, sys
ROOT=Path(__file__).resolve().parents[3]
BASE='db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6'
HEAD='d91f12a172626fb9c4ee9ee69f860dd410856492'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==HEAD
sys.path.insert(0,str(ROOT/'scripts'))
spec=importlib.util.spec_from_file_location('pinned_validate',ROOT/'scripts/validate-guides.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT,text=True)
changed=git('diff','--name-only','--no-renames','--diff-filter=d',f'{BASE}...{HEAD}').splitlines()
status=git('diff','--name-status','-M90%',f'{BASE}...{HEAD}').splitlines()
added={line.split('\t')[1] for line in status if line.startswith('A\t')}
deleted={line.split('\t')[1] for line in status if line.startswith('D\t')}
v.changed_files_vs_main=lambda: changed
v.added_and_deleted_vs_main=lambda: (added,deleted)
def pinned_us_federal_deletions(errors):
    for name in sorted(deleted):
        if name.startswith('packages/us-federal/'):
            errors.append(f'pinned-base deletion of hand-authored us-federal file: {name}')
v.check_us_federal_deletions=pinned_us_federal_deletions
print(f'Pinned diff: {BASE}...{HEAD}')
sys.argv=['scripts/validate-guides.py','--changed-only','--no-index-check']
v.main()
