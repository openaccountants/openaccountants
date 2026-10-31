from pathlib import Path
import importlib.util,sys,json,contextlib,io
P=Path(__file__).parent.resolve();repo=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain');sys.path.insert(0,str(repo/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
v=load('validate_guides',repo/'scripts/validate-guides.py');bi=load('build_index',repo/'scripts/build-index.py');files=[str(P/'proposed-v1.4.md')];bi.guide_files=lambda:files
errors=[];warnings=[];s=io.StringIO()
with contextlib.redirect_stdout(s):v.check_guides(bi,errors,warnings,only_files=set(files))
r={'scope':'Actual Spain repository check_guides routine against one private candidate absolute path only; no current live Guide or package-wide validation/generation.','stdout':s.getvalue(),'errors':errors,'warnings':warnings};(P/'private-validator-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));assert not errors
ex=load('check_examples',repo/'scripts/check-examples.py');count,fail=ex.check_file(files[0]);r={'scope':'Actual repository oa-check runner against private candidate','files':1,'blocks':count,'failures':fail};(P/'private-example-runner-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r));assert count==2 and not fail
