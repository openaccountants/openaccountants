"""Run unchanged repository validator against the pinned base and current worktree.
The stock CLI compares committed HEAD only; before committing it otherwise checks zero files.
No validator rule is changed. Exact CLI is also run after the batch commit.
"""
import importlib.util,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(root/'scripts'))
spec=importlib.util.spec_from_file_location('mali_validator',root/'scripts/validate-guides.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
base='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
def changed():
 return subprocess.check_output(['git','diff','--name-only','--no-renames','--diff-filter=d',base],cwd=root,text=True).splitlines()
m.changed_files_vs_main=changed
m.main()
