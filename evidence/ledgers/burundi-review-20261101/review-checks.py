from pathlib import Path
import collections, hashlib, importlib.util, json, os, re, subprocess, sys, unicodedata
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
BASE='8935b6fc3a7ff0f773334a45a67448f1efe37b19'
HEAD='124f6a7a00cbf173ddcd91a4c0ee81e5aa0f25bf'
os.chdir(ROOT)
sys.path.insert(0,str(ROOT/'scripts'))
import skill_checks
from frontmatter_yaml import load_frontmatter

def git(*args):
 return subprocess.check_output(['git',*args],text=True).strip()
def sha(b): return hashlib.sha256(b).hexdigest()
def fm(b): return load_frontmatter(b.decode().split('---',2)[1])
assert git('rev-parse','HEAD')==HEAD
candidate=json.loads((ROOT.parent/'candidate-checks.json').read_text())
assert sha((ROOT.parent/'sources/capture-manifest.json').read_bytes())=='1441f65ac42f1c00ddeb4807aaa2ee087b4fabbd1ad044c114a85c12119a85d5'
manifest=json.loads((ROOT.parent/'sources/capture-manifest.json').read_text())
source_hashes={}
def walk(obj):
 if isinstance(obj,list):
  for x in obj: walk(x)
 elif isinstance(obj,dict):
  if obj.get('sha256') and obj.get('name'):
   names=[obj.get('file',''),obj['name']+'.pdf',obj['name']+'.html',obj['name']+'.png']
   existing=next((ROOT.parent/'sources'/n for n in names if n and (ROOT.parent/'sources'/n).is_file()),None)
   if existing:
    assert sha(existing.read_bytes())==obj['sha256'],str(existing)
    source_hashes[existing.name]=obj['sha256']
  for value in obj.values():
   if isinstance(value,(dict,list)): walk(value)
walk(manifest)
paths=sorted(str(x) for x in Path('skills/burundi').glob('bi-*.md'))
platform=['review_status','license','authored_by','trust_label','drafted_by','approved_by','validation_status','validated','verified_by','reviewed_by','reviewed_on']
results={'base':BASE,'head':HEAD,'guides':{},'source_manifest_sha256':sha((ROOT.parent/'sources/capture-manifest.json').read_bytes()),'source_files_hash_checked':source_hashes,'runs':[]}
for p in paths:
 data=Path(p).read_bytes(); meta=fm(data)
 assert sha(data)==candidate['files'][p]
 check=skill_checks.run_all(p)
 ledger=Path('evidence/ledgers')/Path(p).name
 rows=[x for x in ledger.read_text().splitlines() if re.match(r'^\| \d+ \|',x)]
 old=subprocess.run(['git','show',f'{BASE}:{p}'],capture_output=True).stdout
 preserved=None; cta=None
 if old:
  om=fm(old)
  preserved={k:meta.get(k)==om.get(k) and (k in meta)==(k in om) for k in platform}
  marker=b'<!-- openaccountants-cta-block -->'
  cta=old[old.index(marker):]==data[data.index(marker):]
 else:
  assert not any(k in meta for k in platform)
 results['guides'][p]={'sha256':sha(data),'description_words':len(meta['description'].split()),'tier':meta['tier'],'version':str(meta['version']),'ledger_rows':len(rows),'shape_failures':{k:v for k,v in check.items() if v},'platform_fields_preserved':preserved,'cta_suffix_exact':cta}
 assert not any(check.values())
 assert 80<=len(meta['description'].split())<=150
 assert meta['tier']==2
 if preserved is not None: assert all(preserved.values()) and cta
for p,h in candidate['files'].items(): assert sha(Path(p).read_bytes())==h
old_topics=[]
for p in paths:
 old=subprocess.run(['git','show',f'{BASE}:{p}'],capture_output=True,text=True).stdout
 old_topics += [(Path(p).stem,m) for m in re.findall(r'^- \*\*(.*?)\*\*',old,re.M)]
map_text=Path('evidence/ledgers/bi-old-topic-destinations.md').read_text()
mapped=re.findall(r'^\| \d+ \| (bi-[^:]+): (.*?) \|',map_text,re.M)
assert collections.Counter(old_topics)==collections.Counter(mapped)
results['old_topic_labels']=len(old_topics)
results['ledger_rows']=sum(x['ledger_rows'] for x in results['guides'].values())
assert results['ledger_rows']==114 and len(old_topics)==65
commands=[['python3','scripts/check-examples.py','--require',*paths],['python3','scripts/check-sync-integrity.py','--repo',str(ROOT),'--base',BASE,'--head',HEAD,'--mode','audit','--strict-metadata']]
for cmd in commands:
 r=subprocess.run(cmd,text=True,capture_output=True)
 results['runs'].append({'argv':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 assert r.returncode==0
# Pin the existing validator's path and add/delete discovery to the frozen base;
# never depend on a moving origin/main and never rewrite a validation script.
spec=importlib.util.spec_from_file_location('review_validator',ROOT/'scripts/validate-guides.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
v.changed_files_vs_main=lambda: git('diff','--name-only',f'{BASE}..{HEAD}').splitlines()
changes=git('diff','--name-status',f'{BASE}..{HEAD}').splitlines()
added={x.split('\t')[1] for x in changes if x.startswith('A\t')}
deleted={x.split('\t')[1] for x in changes if x.startswith('D\t')}
v.added_and_deleted_vs_main=lambda:(added,deleted)
import contextlib,io
buf=io.StringIO();sys.argv=['validate-guides.py','--changed-only','--no-index-check']
with contextlib.redirect_stdout(buf): v.main()
results['runs'].append({'argv':['validate-guides.py','--changed-only','--no-index-check'],'scope_override':f'exact {BASE}..{HEAD} via import, no tracked script edits','exit_code':0,'stdout':buf.getvalue()})
(OUT/'mechanical-checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'head':HEAD,'guides':len(paths),'ledger_rows':results['ledger_rows'],'old_topics':results['old_topic_labels'],'checks':'passed','report':str(OUT/'mechanical-checks.json')},indent=2))
