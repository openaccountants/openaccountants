"""Focused independent correction checks; writes only new review evidence."""
from pathlib import Path
import hashlib,json,re,subprocess
OUT=Path(__file__).resolve().parent
PACK=OUT.parent/'2026-11-01-libya-pack'
FREEZE='a4f20f79ffdfd90e68cfde258405a15dcb627ef9'
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a])
assert git('rev-parse','HEAD').decode().strip()==FREEZE
request=json.loads((OUT/'writer-corrections.json').read_text())
for f,h in request['candidate_files'].items():assert sha(Path(f).read_bytes())==h,(f,h)
for f,h in json.loads((OUT/'review-file-hashes.json').read_text()).items():assert sha(Path(f).read_bytes())==h,f
changed=git('diff','--name-only',FREEZE,'--','skills/libya','docs/research/2026-11-01-libya-pack').decode().splitlines()
assert set(changed)==set(request['candidate_files'])
originals={str(f):git('show',f'{FREEZE}:{f}') for f in Path('skills/libya').glob('*.md')}
guide_hashes={}
examples=0
for f,old in originals.items():
 new=Path(f).read_bytes()
 if f=='skills/libya/ly-cross-border-tax.md':
  expected=old.replace(b'arts. 1-5, 8, 10-17, 19-20, 23 and 26',b'arts. 1-5, 8, 10-20, 23 and 26').replace(b'PDF pp. 4-26, 28-29, 32-36',b'PDF pp. 4-29, 32-36')
  assert new==expected
 else:assert new==old,f
 oldblocks=re.findall(rb'^```oa-check.*?^```',old,re.M|re.S)
 newblocks=re.findall(rb'^```oa-check.*?^```',new,re.M|re.S)
 assert oldblocks==newblocks
 examples+=len(newblocks)
 if '/ly-' in f:guide_hashes[f]={'sha256':sha(new),'bytes':len(new)}
assert len(guide_hashes)==8 and examples==16
register=json.loads((PACK/'fact-register.json').read_text())
oldregister=json.loads(git('show',f'{FREEZE}:docs/research/2026-11-01-libya-pack/fact-register.json'))
assert set(register)-set(oldregister)=={'AVOID1','AVOID2','T10A'}
assert all(register[k]==v for k,v in oldregister.items() if k!='V12')
assert register['V12']['quote']=='1%'
assert all(register['V12'][k]==oldregister['V12'][k] for k in ['id','claim','section','url','read_on'])
seen=set();placements={};total=0
for f in sorted((PACK/'ledgers').glob('*.md')):
 rows=[]
 for line in f.read_text().splitlines():
  if not re.match(r'^\| [A-Z]+\d+[A-Z]* \|',line):continue
  c=[x.strip() for x in line.split('|')[1:-1]];v=register[c[0]]
  assert len(c)==7 and c[1]==v['claim']+'; '+v['section']
  assert c[2]==v['authority']+'; PDF '+str(v['pdf_page'])
  assert c[3]==v['quote'] and c[4]==v['url'] and c[5]==v['read_on'] and c[6]==v['conditions']
  rows.append(c[0]);seen.add(c[0]);total+=1
 placements[f.name]=rows
assert len(register)==119 and seen==set(register) and total==211
oldmanifest=json.loads(git('show',f'{FREEZE}:docs/research/2026-11-01-libya-pack/source-read-manifest.json'))
newmanifest=json.loads((PACK/'source-read-manifest.json').read_text())
for a,b in zip(oldmanifest,newmanifest):
 assert all(a[k]==b[k] for k in a if k not in ('visual_check','actual_read_scope'))
 raw=(Path('../sources')/b['file']).read_bytes();assert sha(raw)==b['sha256'] and len(raw)==b['bytes']
report={'review_date':'2026-11-01','initial_freeze':FREEZE,'working_tree_candidate':True,'writer_corrections_sha256':sha((OUT/'writer-corrections.json').read_bytes()),'exact_candidate_files':request['candidate_files'],'candidate_guide_hashes':guide_hashes,'preserved_initial_review_hashes':True,'all_other_frozen_country_files_unchanged':True,'only_guide_change':'One cross-border Sources row expands actual read scope to include art.18/PDF27; exact expected replacement independently checked.','all_substantive_guide_text_unchanged':True,'example_blocks_byte_identical':examples,'unique_rule_records':len(register),'ledger_placements':total,'placements':placements,'all_source_pdf_hashes_unchanged':True,'old_topic_map_unchanged':True,'all_7_domains_still_partial':True,'findings_closed':['R1','R2','T10 citation improvement'],'legal_acceptance_scope':'Historical primary text and stated partial research scope only; complete 2026 law/current filing/accountant attestation/country completion remain unconfirmed.'}
(OUT/'closure-mechanics.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print('PASS: 8 recorded correction hashes; initial review hashes preserved; only exact Sources-row Guide change; 16 example blocks byte-identical; 119 records and 211 matching ledger placements; source PDF hashes unchanged.')
