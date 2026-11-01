from pathlib import Path
import hashlib,json,os,re,subprocess,sys
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
os.chdir(ROOT)
sys.path.insert(0,str(ROOT/'scripts'))
import skill_checks
from frontmatter_yaml import load_frontmatter
BASE='8935b6fc3a7ff0f773334a45a67448f1efe37b19'
OLD='124f6a7a00cbf173ddcd91a4c0ee81e5aa0f25bf'
HEAD='e42a4f145ce4393878310853027150dfaec193af'
def git(*a): return subprocess.check_output(['git',*a],text=True).strip()
def sha(b):return hashlib.sha256(b).hexdigest()
def oldbytes(p): return subprocess.check_output(['git','show',f'{OLD}:{p}'])
def meta(b):return load_frontmatter(b.decode().split('---',2)[1])
assert git('rev-parse','HEAD')==HEAD
repair=json.loads(Path('evidence/ledgers/burundi-repair-1/repair.json').read_text())
preservation=json.loads(Path('evidence/ledgers/burundi-repair-1/preservation-and-checks.json').read_text())
results={'base':BASE,'original_candidate':OLD,'repair_candidate':HEAD,'verdict':'limited-source-faithful-acceptance','guides':{},'evidence_preserved':{},'changed_ledger_rows':{},'runs':[]}
for p,h in {**preservation['initial_review_sha256'],**preservation['preserved_writer_evidence']}.items():
 assert sha(Path(p).read_bytes())==h,p
 results['evidence_preserved'][p]=h
manifest=Path('../sources/capture-manifest.json').read_bytes()
assert sha(manifest)=='1441f65ac42f1c00ddeb4807aaa2ee087b4fabbd1ad044c114a85c12119a85d5'
results['source_capture_manifest_sha256']=sha(manifest)
platform=['review_status','license','authored_by','trust_label','drafted_by','approved_by','validation_status','validated','verified_by','reviewed_by','reviewed_on']
marker=b'<!-- openaccountants-cta-block -->'
for p,h in repair['after_guide_sha256'].items():
 b=Path(p).read_bytes();o=oldbytes(p);fm=meta(b);om=meta(o)
 assert sha(b)==h and sha(o)==repair['before_guide_sha256'][p]
 assert fm['description']==om['description']
 assert all((k in fm)==(k in om) and fm.get(k)==om.get(k) for k in platform)
 assert re.findall(rb'```oa-check.*?```',b,re.S)==re.findall(rb'```oa-check.*?```',o,re.S)
 text=b.decode();title=re.search(r'^# .*$',text,re.M).group()
 assert title.endswith('v'+str(fm['version']))
 assert '**General reference only.**' in text.split('## Who this applies to')[0]
 if marker in o:
  assert b[b.index(marker):]==o[o.index(marker):]
  cta=True
 else:
  assert marker not in b and not any(k in fm for k in platform)
  cta=None
 checks=skill_checks.run_all(p);assert not any(checks.values())
 results['guides'][p]={'sha256':h,'description_words':len(fm['description'].split()),'version':str(fm['version']),'shape_checks':len(checks),'shape_failures':{},'example_blocks_unchanged':True,'platform_fields_preserved':True,'cta_suffix_exact':cta,'opening_notice':True}
ledgers=sorted(Path('evidence/ledgers').glob('bi-*.md'))
count=0
for p in ledgers:
 if p.name=='bi-old-topic-destinations.md':continue
 rows={int(re.match(r'^\| (\d+) \|',x).group(1)):x for x in p.read_text().splitlines() if re.match(r'^\| \d+ \|',x)}
 olds={int(re.match(r'^\| (\d+) \|',x).group(1)):x for x in oldbytes(str(p)).decode().splitlines() if re.match(r'^\| \d+ \|',x)}
 count+=len(rows)
 changed=[i for i,row in rows.items() if row!=olds.get(i)]
 if changed:results['changed_ledger_rows'][str(p)]={'changed_existing':[i for i in changed if i in olds],'new':[i for i in changed if i not in olds]}
results['total_physical_ledger_rows']=count;assert count==116
# No content was removed from or added to the legacy destination map or pack scope.
for p in ['evidence/ledgers/bi-old-topic-destinations.md','skills/burundi/README.md']:
 assert Path(p).read_bytes()==oldbytes(p),p
 results['evidence_preserved'][p]=sha(Path(p).read_bytes())
commands=[['python3','evidence/ledgers/burundi-repair-1/pinned-validation.py'],['python3','scripts/check-examples.py','--require',*sorted(repair['after_guide_sha256'])],['python3','scripts/check-sync-integrity.py','--base',BASE,'--head',HEAD,'--mode','audit','--strict-metadata'],['git','diff','--check',f'{OLD}..{HEAD}']]
for cmd in commands:
 r=subprocess.run(cmd,capture_output=True,text=True)
 results['runs'].append({'argv':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 assert r.returncode==0,r.stdout+r.stderr
results['reviewer_correction']={'article':'procedure law art.32','original_review_wrong_physical_page':12,'correct_physical_and_printed_page':13,'method':'Actual p.13 image independently viewed; p.12 continuation and source OCR page marker cross-checked. Exact quote is une durée de dix ans. Original review files preserved unchanged.'}
(OUT/'closure-checks.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'repair_candidate':HEAD,'guides':len(results['guides']),'physical_ledger_rows':count,'changed_ledger_rows':results['changed_ledger_rows'],'checks':'all passed'},indent=2))
