from pathlib import Path
import hashlib,json,subprocess,re,collections
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/spain-closeout-2026-10-31');R=W/'repository';E=R/'ledgers/spain-closeout-20261031';O=W/'review/final-checkpoint'
h=lambda b:hashlib.sha256(b).hexdigest()
hf=lambda p:h(p.read_bytes())
def git(*args):return subprocess.check_output(['git',*args],cwd=R)
def old(p,ref):return git('show',ref+':'+p)
c=json.loads((E/'checkpoint.json').read_text());base=c['original_base'];latest=c['latest_main_checked']
pins=json.loads((R/'ledgers/spain-2026-evidence/independent-review/final-22-pair-pins.json').read_text());oldpairs={p['slug']:p for p in pins['pairs']}
assert len(c['pairs'])==len(oldpairs)==22
changed={'es-foral-income-tax':'a4','es-foral-non-resident-tax':'a1-gross'}
checks={'reviewed_on':'2026-10-31','original_base':base,'latest_main_checked':latest,'pairs':[]}
for p in c['pairs']:
 q=oldpairs[p['slug']];x={'slug':p['slug'],'guide_sha256':hf(R/p['guide_path']),'ledger_sha256':hf(R/p['ledger_path'])}
 for k in ('guide','ledger'):
  assert x[k+'_sha256']==p[k+'_sha256'];assert (R/p[k+'_path']).stat().st_size==p[k+'_bytes']
  assert h(old(p[k+'_path'],base))==q[k+'_sha256']
  assert old(p[k+'_path'],latest)==old(p[k+'_path'],base)
 if p['slug'] in changed:
  m=json.loads((W/'review'/changed[p['slug']]/'manifest.json').read_text())
  assert x['guide_sha256']==m['candidate_guide_sha256'];assert x['ledger_sha256']==m['candidate_ledger_sha256']
  assert (R/p['ledger_path']).read_bytes().startswith(old(p['ledger_path'],base));x['verdict']='EXACT_APPROVED_DELTA_AND_ORIGINAL_LEDGER_PREFIX'
 else:
  assert all(x[k+'_sha256']==q[k+'_sha256'] for k in ('guide','ledger'));x['verdict']='UNCHANGED_SEALED_PAIR'
 checks['pairs'].append(x)
assert len(c['unchanged_other_spain_files'])==26
allspain={str(p.relative_to(R)) for p in (R/'skills/international/spain').iterdir() if p.is_file()}
expected=allspain-{'skills/international/spain/README.md',*(p['guide_path'] for p in c['pairs'] if p['slug'] in changed)}
assert expected==set(c['unchanged_other_spain_files'])
for p,sha in c['unchanged_other_spain_files'].items():
 assert hf(R/p)==sha==h(old(p,base));assert old(p,latest)==old(p,base)
checks['unchanged_other_spain_files']=c['unchanged_other_spain_files']
oldreview='ledgers/spain-2026-evidence/independent-review/'
tracked=git('ls-tree','-r','--name-only',base,'--',oldreview).decode().splitlines()
assert tracked
for p in tracked:assert (R/p).read_bytes()==old(p,base)==old(p,latest)
assert not git('diff','--name-only',base,'--',oldreview).strip()
checks['original_sealed_review_files_unchanged']=len(tracked)
archive=E/'baseline-country-status.txt';assert archive.read_bytes()==old('skills/international/spain/README.md',base)
assert hf(archive)==c['baseline_country_status_sha256']
public_copies={'scope-review':['scope-review.md','scope-matrix.json','manifest.json'],'a4-independent-review':[p.name for p in (W/'review/a4').iterdir() if p.is_file()],'a1-gross-independent-review':[p.name for p in (W/'review/a1-gross').iterdir() if p.is_file()],'a1-net-rejection':[p.name for p in (W/'review/a1').iterdir() if p.is_file()],'residual-crypto':['report.md','source-checks.json','verdict.json','manifest.json']}
localdirs={'scope-review':W/'review','a4-independent-review':W/'review/a4','a1-gross-independent-review':W/'review/a1-gross','a1-net-rejection':W/'review/a1','residual-crypto':W/'review/residual-crypto'}
checks['preserved_review_copies']={}
for d,files in public_copies.items():
 for f in files:assert (E/d/f).read_bytes()==(localdirs[d]/f).read_bytes()
 checks['preserved_review_copies'][d]={f:hf(E/d/f) for f in files}
scope=json.loads((E/'scope-review/scope-matrix.json').read_text());assert scope['counts']=={'A':4,'B':33,'C':36};assert len(scope['matrix'])==73
checks['preserved_scope_counts']=scope['counts'];assert c['partial_domains']==['IT-IND'];assert c['open_findings']==['A2','A3'];assert set(c['resolved_method_gaps'])=={'A1','A4'}
checks['status']={'partial_domains':c['partial_domains'],'open_findings':c['open_findings'],'resolved_method_gaps':c['resolved_method_gaps'],'country_complete':False,'close_issue391':False,'accountant_attestation':False}
for k,f in [('country_readme_sha256',R/'skills/international/spain/README.md'),('owners_sha256',R/'OWNERS.md'),('source_receipts_sha256',E/'source-receipts.json')]:assert c[k]==hf(f)
readme=(R/'skills/international/spain/README.md').read_text();cover=(E/'README.md').read_text()
assert re.search(r'partial:\n  IT-IND:',readme);assert 'stays open' in readme and '#391' in readme;assert 'not country-complete' in cover
broken=[];links=[]
for file in [R/'skills/international/spain/README.md',E/'README.md',R/'skills/international/spain/es-foral-income-tax.md',R/'skills/international/spain/es-foral-non-resident-tax.md']:
 for target in re.findall(r'\]\(([^)]+)\)',file.read_text()):
  if re.match(r'\w+:|#',target):continue
  target=target.split('#')[0];dest=(file.parent/target).resolve();links.append({'file':str(file.relative_to(R)),'target':target,'exists':dest.exists()})
  if not dest.exists():broken.append(links[-1])
assert not broken;checks['local_markdown_links']=links
owners=(R/'OWNERS.md').read_text();prior=old('OWNERS.md',base).decode()
def countryrows(s):return {m.group(1):m.group(0) for m in re.finditer(r'^\| ([A-Z]{2}) \|.*$',s,re.M)}
a,b=countryrows(prior),countryrows(owners);assert a.keys()==b.keys();assert [k for k in a if a[k]!=b[k]]==['ES']
assert 'Claude: 32 jurisdictions. ChatGPT: 23.' in owners
allowed_old=[a['ES'],'**Claude: 33 jurisdictions. ChatGPT: 22.** A country allocation covers every topic, including existing skills. One active writer per country.']
allowed_new=[b['ES'],'**Claude: 32 jurisdictions. ChatGPT: 23.** A country allocation covers every topic, including existing skills. One active writer per country.']
minus=[];plus=[]
for line in git('diff',base,'--','OWNERS.md').decode().splitlines():
 if line.startswith('---') or line.startswith('+++'):continue
 if line.startswith('-'):minus.append(line[1:])
 if line.startswith('+'):plus.append(line[1:])
assert set(minus)==set(allowed_old);assert len(plus)==3;assert set(allowed_new).issubset(plus);assert any(p.startswith('- **Spain closeout (31 October):') for p in plus)
assert old('OWNERS.md',base)==old('OWNERS.md',latest)
counts=collections.Counter('ChatGPT' if line.split('|')[3].strip().startswith('ChatGPT') else 'Claude' for line in b.values());assert counts=={'Claude':32,'ChatGPT':23}
checks['owners_actual_table_counts']=dict(counts)
checks['owners_change_scope']={'only_country_row_changed':'ES','other_changes':'ownership totals and Spain handover bullet only','non_ES_rows_unchanged':len(a)-1,'totals':'32 Claude / 23 ChatGPT'}
receipts=json.loads((E/'source-receipts.json').read_text());assert len(receipts)==13;checks['source_archives']=[]
for s in receipts:
 p=E/s['archive_path'];assert p.stat().st_size==s['bytes'];assert hf(p)==s['sha256'];assert p.read_bytes()==(W/s['archive_path']).read_bytes();assert p.read_bytes().startswith(b'%PDF');assert s['exit']==0
 checks['source_archives'].append({k:s[k] for k in ('key','url','archive_path','sha256','bytes')})
for review in ['a1-gross','a4']:
 d=json.loads((W/'review'/review/'independent-checks.json').read_text())
 if review=='a1-gross':targets=d['support_target_hashes']
 else:targets={k:v['sha256'] for k,v in d['support_files'].items()}
 for p,sha in targets.items():assert hf(E/p)==sha
checks['approved_support_hashes_still_match']=True
v=json.loads((E/'validation-schemas.json').read_text());assert v['changed2_errors']==v['changed2_warnings']==[];assert v['preexisting_unchanged_failure'] is True
assert v['all22_schema_and_mechanical_errors']==['skills/international/spain/es-irpf-deductions.md: (h) no_em_dash: 7 em dash(es)']
assert v['baseline_deductions_sha256']==hf(R/'skills/international/spain/es-irpf-deductions.md')==h(old('skills/international/spain/es-irpf-deductions.md',base))
assert '49 oa-check' in (E/'validation-examples.txt').read_text();assert '0 failures' in (E/'validation-examples.txt').read_text()
assert 'Ran 149 tests' in (E/'validation-unit-tests.txt').read_text();assert (E/'validation-unit-tests.txt').read_text().rstrip().endswith('OK')
note=(E/'validation-environment-note.txt').read_text();assert all(t in note for t in ['1 failure, 7 errors','TMPDIR=/private/tmp','RUNNER_TEMP=/private/tmp','No source or test file was changed'])
checks['validation']={'new_checks_this_seal':'identity, preservation, packaging and recorded-result consistency; no blind whole-pack legal or test rerun','prior_independent_delta_examples':'A1 original2, A4 original2 plus all5 linked controls recomputed/passed in exact delta reviews','writer_recorded_results':v,'writer_unit_tests':'149 pass after recorded macOS temporary-path/CI variable correction; initial1failure7errors preserved in note','does_not_claim_full22_mechanical_green':True}
changedpaths=git('diff','--name-only',base).decode().splitlines();allowed={'OWNERS.md','skills/international/spain/README.md',*(p[k+'_path'] for p in c['pairs'] if p['slug'] in changed for k in ('guide','ledger'))}
assert all(p in allowed or p.startswith('ledgers/spain-closeout-20261031/') for p in changedpaths)
checks['tracked_change_scope_pass']=True;checks['untracked_outside_batch']=git('ls-files','--others','--exclude-standard').decode().splitlines();checks['excluded_from_verdict']=['untracked resp.txt','future integration/commit/PR checks; preserve these exact reviewed hashes after integration']
checks['resolved_findings']=[{'id':'F-FINAL-01','status':'RESOLVED','description':'Checkpoint initially retained baseline byte counts for2changed pairs despite correct candidate hashes. Writer corrected exactly4byte fields; all new sizes now independently verified. No Guide, ledger, status or source bytes changed.'}]
checks['open_publication_findings']=[]
checks['verdict']='PASS_FOR_ONE_ACCURATELY_PARTIAL_COUNTRY_CHECKPOINT_ONLY'
(O/'independent-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'verdict':checks['verdict'],'pair_count':len(c['pairs']),'unchanged_pairs':20,'other_spain_files':26,'old_sealed_files':len(tracked),'source_archives':len(receipts),'local_links':len(links),'checkpoint_sha256':hf(E/'checkpoint.json'),'README_sha256':hf(R/'skills/international/spain/README.md'),'OWNERS_sha256':hf(R/'OWNERS.md'),'cover_sha256':hf(E/'README.md'),'untracked':checks['untracked_outside_batch']},indent=2))
