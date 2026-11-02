import pathlib, subprocess, re, json, hashlib, importlib.util, sys
from decimal import Decimal
ROOT=pathlib.Path('/Users/michaelcutajar/.codex/visualizations/2026/10/23/01a16914-3f96-7d32-a5e0-df503863dadf/andorra-continuation/country')
OUT=ROOT.parent/'review'
sys.path.insert(0,str(ROOT/'scripts'))
from frontmatter_yaml import load_frontmatter
spec=importlib.util.spec_from_file_location('examples',ROOT/'scripts/check-examples.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
CAND='32d4e3e8c3121fa37fa7648b5343116dacd08cc4';BASE='5254033fda891adceb3c98aec1f508e3b21f85f5';MERGE='43a766a09b91b45392ee0522e5f69d9e2e6306b2'
def show(commit,path):return subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=ROOT)
def sha(x):return hashlib.sha256(x).hexdigest()
files=sorted((ROOT/'skills/international/andorra').glob('*.md'))
protected=['name','depends_on','authored_by','trust_label','review_status','license','drafted_by','approved_by','validation_status','validated','reviewed_by','reviewed_on','verified_by']
records=[];oldblocks={};allblocks=[]
for p in files:
 rel=str(p.relative_to(ROOT));old=show(BASE,rel);new=show(CAND,rel);merged=show(MERGE,rel)
 oldt=old.decode();newt=new.decode()
 oldfm=load_frontmatter(oldt.split('---',2)[1]);newfm=load_frontmatter(newt.split('---',2)[1])
 if isinstance(oldfm,tuple):oldfm=oldfm[0]
 if isinstance(newfm,tuple):newfm=newfm[0]
 of=oldt.split('<!-- openaccountants-cta-block -->',1);nf=newt.split('<!-- openaccountants-cta-block -->',1)
 record={'path':rel,'original_sha256':sha(old),'candidate_sha256':sha(new),'original_archive_byte_exact':old==(ROOT/'skills/research/andorra-2026/original'/f'{p.stem}.txt').read_bytes(),'main_merge_unchanged':old==merged,'old_bytes':len(old),'new_bytes':len(new),'shrink_percent':round((1-len(new)/len(old))*100,2),'protected_fields_unchanged':{k:oldfm.get(k)==newfm.get(k) for k in protected},'cta_unchanged':len(of)==len(nf) and (len(of)==1 or of[1]==nf[1]),'old_control_count':len(m.BLOCK_RE.findall(oldt)),'new_control_count':len(m.BLOCK_RE.findall(newt))}
 records.append(record)
 for b in m.BLOCK_RE.findall(oldt):oldblocks[m.parse_block(b)['name']]=b
 for b in m.BLOCK_RE.findall(newt):allblocks.append((rel,b))
for rel in ['skills/research/andorra-2026/corporate-supplementary-controls.md','skills/research/andorra-2026/nonresident-supplementary-controls.md','skills/research/andorra-2026/continuation-controls.md']:
 for b in m.BLOCK_RE.findall(show(CAND,rel).decode()):allblocks.append((rel,b))
results=[];preserved=[]
for rel,txt in allblocks:
 b=m.parse_block(txt);values=dict(b['inputs'])
 for key,expr in b['steps']:values[key]=m.evaluate(expr,values)
 results.append({'file':rel,'name':b['name'],'inputs':{k:str(v) for k,v in b['inputs'].items()},'computed':{k:str(values[k]) for k in b['expected']},'expected':{k:str(v) for k,v in b['expected'].items()},'pass':not m.run_block(b)})
 if b['name'] in oldblocks:preserved.append({'name':b['name'],'location':rel,'byte_exact_block':oldblocks[b['name']]==txt})
coverage=subprocess.run([sys.executable,'scripts/coverage-report.py','--json'],cwd=ROOT,capture_output=True,text=True)
cov=json.loads(coverage.stdout)
ad=[r for r in cov['rows'] if r['code']=='AD'][0]
(OUT/'coverage-andorra.json').write_text(json.dumps({'exit_code':coverage.returncode,'generated_on':cov['generated_on'],'andorra':ad},indent=2)+'\n')
(OUT/'computations.json').write_text(json.dumps({'candidate':CAND,'total_controls':len(results),'all_pass':all(r['pass'] for r in results),'controls':results},indent=2)+'\n')
(OUT/'preservation.json').write_text(json.dumps({'candidate':CAND,'baseline':BASE,'merge':MERGE,'files':records,'preserved_original_controls':preserved,'all_original_oa_checks_preserved':set(oldblocks)=={x['name'] for x in preserved},'lost_substantive_topic_groups_identified':1,'pending_restorations':['Resident movable-capital withholding and elected EUR3000 reduction, original income section5.9'],'lost_content_restored_by_reviewer':0,'restoration_note':'Reviewer was instructed not to edit Guides. Writer must restore the identified method; the restoration count must be updated only after checking the actual fixed text.'},indent=2)+'\n')
print(json.dumps({'controls':len(results),'pass':all(r['pass'] for r in results),'original_controls':len(oldblocks),'all_preserved':len(preserved)==len(oldblocks) and all(r['byte_exact_block'] for r in preserved),'example_counts':{pathlib.Path(r['path']).name:r['new_control_count'] for r in records},'preservation_checks_pass':all(r['original_archive_byte_exact'] and r['main_merge_unchanged'] and r['cta_unchanged'] and all(r['protected_fields_unchanged'].values()) for r in records),'shrinks':{pathlib.Path(r['path']).name:r['shrink_percent'] for r in records},'AD':ad},indent=2))
