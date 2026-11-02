#!/usr/bin/env python3
"""Run repository validator against the requested frozen base, without mutating refs."""
from pathlib import Path
import importlib.util, subprocess, sys
ROOT=Path(__file__).resolve().parents[3]
BASE='db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6'
sys.path.insert(0,str(ROOT/'scripts'))
spec=importlib.util.spec_from_file_location('validate_guides',ROOT/'scripts/validate-guides.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def git(*args):
 return subprocess.run(['git',*args],cwd=ROOT,text=True,capture_output=True,check=True).stdout
# Staged + unstaged compared with pinned base. Before running, all candidate files
# must be tracked/staged. No files are modified by this adapter.
changed=git('diff','--name-only','--diff-filter=d',BASE).splitlines()
status=git('diff','--name-status','--no-renames',BASE).splitlines()
added={x.split('\t')[1] for x in status if x.startswith('A\t')}
deleted={x.split('\t')[1] for x in status if x.startswith('D\t')}
m.changed_files_vs_main=lambda:changed
m.added_and_deleted_vs_main=lambda:(added,deleted)
def us_deletions(errors):
 for path in deleted:
  if path.startswith('packages/us-federal/'):errors.append(f'hand-authored file deleted vs {BASE}: {path}')
m.check_us_federal_deletions=us_deletions
sys.argv=['validate-guides.py','--changed-only','--no-index-check']
print(f'Pinned base: {BASE}; comparison includes candidate working tree')
m.main()
