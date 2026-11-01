"""Read-only checks of the frozen candidate; writes only this review directory."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import yaml
BASE='aec6ba04066bb69d1168c8028ba11dd65cb90505'
FREEZE='a4f20f79ffdfd90e68cfde258405a15dcb627ef9'
OUT=Path(__file__).resolve().parent
PACK=Path('docs/research/2026-11-01-libya-pack')
def git(*args):return subprocess.check_output(['git',*args])
def sha(b):return hashlib.sha256(b).hexdigest()
assert git('rev-parse','HEAD').decode().strip()==FREEZE
platform={'review_status','license','authored_by','trust_label','drafted_by','approved_by','validation_status','validated','verified_by','reviewed_by','reviewed_on'}
report={'base':BASE,'freeze':FREEZE,'guides':{},'old_topics':[],'sources':[],'ledger_placements':{},'scope':git('diff','--name-status',BASE).decode().splitlines()}
manifest=json.loads((PACK/'candidate-guide-hashes.json').read_text())
oldhashes=json.loads((PACK/'old-hashes.json').read_text())
opening='> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person\'s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.'
legacy_count=0
for f in sorted(Path('skills/libya').glob('ly-*.md')):
 b=f.read_bytes();s=b.decode();fm=yaml.safe_load(s.split('---',2)[1]);n=len(fm['description'].split())
 assert sha(b)==manifest[str(f)]['sha256'] and len(b)==manifest[str(f)]['bytes']
 assert 80<=n<=150 and fm['jurisdiction']=='LY' and fm['tax_year']==2026 and fm['tier']==2
 assert str(fm['version'])=='1.0' and re.search(r'^# .* v1\.0$',s,re.M)
 assert opening in s and s.index(opening)<s.index('## Who this applies to')
 assert all(k not in fm for k in ['reviewed_by','reviewed_on','verified_by'])
 result=subprocess.run(['git','show',f'{BASE}:{f}'],capture_output=True)
 row={'sha256':sha(b),'bytes':len(b),'description_words':n,'opening_exact':True,'title_version_matches':True}
 if result.returncode==0:
  legacy_count+=1;ob=result.stdout;os=ob.decode();of=yaml.safe_load(os.split('---',2)[1])
  assert sha(ob)==oldhashes[str(f)]['sha256']
  keys={k for k in platform if k in of}
  assert keys=={k for k in platform if k in fm}
  for k in keys:
   assert re.search(r'^'+k+':.*$',os,re.M)[0]==re.search(r'^'+k+':.*$',s,re.M)[0]
  marker='<!-- openaccountants-cta-block -->'
  assert os[os.index(marker):].encode()==s[s.index(marker):].encode()
  assert str(fm['last_updated'])>str(of['last_updated']) and len(b)>=len(ob)*0.75
  row.update(legacy=True,old_sha256=sha(ob),platform_lines_exact=True,cta_exact=True,old_bytes=len(ob),shrinkage_over_25pct=False)
 else:
  assert not(platform & set(fm)) and '<!-- openaccountants-cta-block -->' not in s
  row.update(legacy=False,no_platform_fields_or_cta=True)
 report['guides'][str(f)]=row
assert legacy_count==6 and len(report['guides'])==8
readme=yaml.safe_load(Path('skills/libya/README.md').read_text().split('---',2)[1])
assert set(readme['partial'])==set(readme['applicable'])=={'IT-IND','IT-CORP','VAT','SC','PR','TP','XB'}
assert readme['not_applicable']=={}
report['all_7_domains_partial']=True
register=json.loads((PACK/'fact-register.json').read_text());seen=set();total=0
for f in sorted((PACK/'ledgers').glob('*.md')):
 rows=[]
 for ln,line in enumerate(f.read_text().splitlines(),1):
  if not re.match(r'^\| [A-Z]+\d+ \|',line):continue
  c=[x.strip() for x in line.split('|')[1:-1]];v=register[c[0]]
  assert len(c)==7 and c[1]==v['claim']+'; '+v['section']
  assert c[2]==v['authority']+'; PDF '+str(v['pdf_page'])
  assert c[3]==v['quote'] and c[4]==v['url'] and c[5]==v['read_on'] and c[6]==v['conditions']
  rows.append({'id':c[0],'line':ln});seen.add(c[0]);total+=1
 report['ledger_placements'][f.name]=rows
assert len(register)==116 and seen==set(register) and total==208
report['distinct_ledger_records']=len(register);report['ledger_placements_total']=total
mapped={}
for line in (PACK/'old-topic-destination-map.md').read_text().splitlines():
 if not line.startswith('| skills/libya/'):continue
 c=[x.strip() for x in line.split('|')[1:-1]]
 key=(c[0],int(c[1]));assert key not in mapped;mapped[key]=c
for file,row in report['guides'].items():
 if not row['legacy']:continue
 original=git('show',f'{BASE}:{file}').decode().split('<!-- openaccountants-cta-block -->')[0]
 for ln,line in enumerate(original.splitlines(),1):
  if not line.startswith('- **'):continue
  c=mapped[(file,ln)];assert c[3]==line
  report['old_topics'].append({'file':file,'line':ln,'topic':c[2],'destination':c[4],'treatment':c[5],'verbatim_original_matches':True})
assert len(report['old_topics'])==len(mapped)==66
for f in json.loads((PACK/'source-read-manifest.json').read_text()):
 b=(Path('../sources')/f['file']).read_bytes()
 assert sha(b)==f['sha256'] and len(b)==f['bytes']
 report['sources'].append({'file':f['file'],'official_url':f['official_url'],'sha256':sha(b),'bytes':len(b)})
tracked=git('ls-files','skills/libya','docs/research/2026-11-01-libya-pack').decode().splitlines()
report['frozen_content_hashes']={f:sha(Path(f).read_bytes()) for f in tracked}
assert all(git('show',f'{FREEZE}:{f}')==Path(f).read_bytes() for f in tracked)
(OUT/'mechanical-results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print('PASS: frozen tracked content unchanged; 8 hashes; 6 legacy metadata/CTA matches; 2 new clean; 116 unique ledger records; 208 placements; 66 exact old-bullet/line matches; 5 source hashes; all 7 domains partial.')
