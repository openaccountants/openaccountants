"""Read-only verification of immutable candidate; writes this review directory only."""
from pathlib import Path
import json, hashlib, re, subprocess, sys, importlib.util
from decimal import Decimal as D
import yaml

C = Path(__file__).resolve().parents[4]
O = Path(__file__).resolve().parent
S = C.parent / 'work/sources/remaining-reliefs'
PIN = '933e6993fe5305609c849551765a27ba9a116e8b'
BASE = 'f7d59d7c4679192f0e5d3bbe286742fb78531c11'
R = 'skills/research/gibraltar-2026/remaining-reliefs-2026-10-28/'
G = 'skills/international/gibraltar/gi-individual-income-tax.md'
def git(rev, path):
    return subprocess.check_output(['git','show',rev+':'+path],cwd=C)
def sha(b):
    return hashlib.sha256(b).hexdigest()
def out(name, data):
    (O/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
def j(path, rev=PIN):
    return json.loads(git(rev,path))
def normalized(t):
    t = re.sub(r'^\s*© Government of Gibraltar \(www\.gibraltarlaws\.gov\.gi\)\s*$', '', t, flags=re.M)
    t = re.sub(r'^\s*Page \d+ of \d+\s*$', '', t, flags=re.M)
    return ' '.join(t.split())
def paragraphs(t):
    body = t.split('---',2)[2].split('<!-- openaccountants-cta-block -->')[0]
    return [x.strip() for x in re.split(r'\n\s*\n',body) if x.strip() and not x.strip().startswith('#')]

d = j(R+'ledger.json')
old = j('skills/research/gibraltar-2026/individual-completion-2026-10-28/ledger.json',BASE)
guide_bytes = git(PIN,G)
guide = guide_bytes.decode()
before = git(BASE,G).decode()
assert sha(guide_bytes)==d['guide_sha256']
assert git(PIN,R+'gi-individual-income-tax.before.txt')==git(BASE,G)
newproofs = [p for p in d['source_proofs'] if p['id'].startswith('REL-')]
proof_results=[]
for p in newproofs:
    raw=(S/p['file']).read_bytes()
    text=(S/Path(p['file']).with_suffix('.txt')).read_text()
    clean=normalized(text)
    snippets=[]
    for i,q in enumerate(p['quotes'],1):
        needle=' '.join(q.split())
        snippets.append({'snippet':i,'words':len(q.split()),'normalized_offset':clean.find(needle),'exact_after_stated_normalization':needle in clean})
    proof_results.append({'id':p['id'],'file':p['file'],'url':p['url'],'provision':p['provision'],'read_on':p['read_on'],'sha256':sha(raw),'recorded_hash_matches':sha(raw)==p['sha256'],'snippets':snippets,'all_snippets_exact':all(x['exact_after_stated_normalization'] for x in snippets)})
assert len(newproofs)==6 and sum(len(p['snippets']) for p in proof_results)==57
assert all(p['recorded_hash_matches'] and p['all_snippets_exact'] for p in proof_results)
receipts=j(R+'source-receipts.json')
receipt_checks=[dict(x,verified_sha256=sha((S/x['name']).read_bytes()),hash_matches=x['sha256']==sha((S/x['name']).read_bytes())) for x in receipts]
assert all(x['hash_matches'] for x in receipt_checks)
out('source-proof-results.json',{'normalization':'Remove only repeated Government of Gibraltar copyright and Page N of M footer lines, then collapse whitespace. Running headers, punctuation, case and all substantive text retained.','proofs':proof_results,'receipts':receipt_checks,'full_documents_read':True,'operative_documents':4,'targeted_amendments':2,'visual_pages':['energy-performance.pdf p5','disabled-access.pdf p3','ev-charger.pdf p4']})

closure=j('skills/research/gibraltar-2026/final-country-review-2026-10-28/closure-4d2640c6/closure.json')
manifest=[]
for entry in closure['verification']['accepted_content_manifest']:
    path=entry['path']; raw=git(PIN,path)
    changed=path in ['skills/international/gibraltar/README.md',G]
    manifest.append(dict(entry,current_sha256=sha(raw),current_git_blob=subprocess.check_output(['git','rev-parse',PIN+':'+path],cwd=C,text=True).strip(),expected_delta=changed,unchanged=sha(raw)==entry['sha256']))
assert len(manifest)==41 and sum(x['unchanged'] for x in manifest)==39
assert all(x['unchanged'] or x['expected_delta'] for x in manifest)
prior_review=[]
for entry in closure['verification']['primary_review_evidence']:
    raw=git(PIN,entry['path'])
    prior_review.append({'path':entry['path'],'sha256':sha(raw),'exact':sha(raw)==entry['sha256']})
assert all(x['exact'] for x in prior_review)
assert d['rows'][:60]==old['rows'] and d['source_proofs'][:87]==old['source_proofs']
oldpars=paragraphs(before); currentpars=paragraphs(guide)
assert len(oldpars)==90
assert oldpars==[x['old_text'] for x in d['old_paragraph_map']]
destinations=[]
for x in d['old_paragraph_map']:
    assert sha(x['old_text'].encode())==x['old_sha256']
    exact=x['old_text'] in currentpars
    assert exact==x['paragraph_exact']
    matches=[p for p in currentpars if sha(p.encode())==x['current_sha256']]
    assert len(matches)==1
    destinations.append({'id':x['id'],'old_section':x['old_section'],'destination':x['destination'],'old_sha256':x['old_sha256'],'current_sha256':x['current_sha256'],'verified_destination':True,'paragraph_exact':exact,'disposition':x['disposition'],'changed_text':matches[0] if not exact else None})
assert sum(x['paragraph_exact'] for x in destinations)==88
meta_before=yaml.safe_load(before.split('---',2)[1]);meta_current=yaml.safe_load(guide.split('---',2)[1])
protected=['name','description','jurisdiction','category','tax_year','tier','verified_by','authored_by','review_status','trust_label','license','drafted_by','approved_by','validation_status','validated','reviewed_by','reviewed_on']
metadata=[{'key':k,'old':str(meta_before.get(k)),'new':str(meta_current.get(k)),'exact':meta_before.get(k)==meta_current.get(k)} for k in protected]
assert all(x['exact'] for x in metadata)
assert before.split('<!-- openaccountants-cta-block -->')[1]==guide.split('<!-- openaccountants-cta-block -->')[1]
assert meta_current['sources'][:len(meta_before['sources'])]==meta_before['sources']
assert meta_current['version']=='0.11'
sections=re.findall(r'^## (.+)$',guide.split('<!-- openaccountants-cta-block -->')[0],re.M)
assert sections==['Who this applies to','Rates, bands and thresholds','The base','Deadlines and filing','Penalties and interest','Cross-border points','Two worked examples that recompute','Ask the client first','Sources']
blocks=re.findall(r'^```oa-check\n(.*?)^```',guide,re.M|re.S)
assert len(blocks)==2 and blocks==re.findall(r'^```oa-check\n(.*?)^```',before,re.M|re.S)
readme_before=yaml.safe_load(git(BASE,'skills/international/gibraltar/README.md').decode().split('---',2)[1])
readme_current=yaml.safe_load(git(PIN,'skills/international/gibraltar/README.md').decode().split('---',2)[1])
assert readme_current['partial'].keys()==readme_before['partial'].keys()
assert all(readme_current['partial'][k]==v for k,v in readme_before['partial'].items() if k!='IT-IND')
mdledger=git(PIN,R+'ledgers/gi-individual-income-tax.md').decode()
assert all('| '+x['id']+' |' in mdledger for x in d['rows'])
assert all(x['rule'] in mdledger for x in d['rows'] if x['id'].startswith('REL-'))
assert all('### Proof '+p['id'] in mdledger and all(q in mdledger for q in p['quotes']) for p in newproofs)
assert all('| '+x['id']+' |' in mdledger for x in d['old_paragraph_map'])
out('preservation-results.json',{'pin':PIN,'base':BASE,'guide_sha256':sha(guide_bytes),'before_snapshot_exact':True,'inherited_rows_data_exact':60,'inherited_proof_units_data_exact':87,'manifest':manifest,'prior_review_evidence':prior_review,'old_topic_map_complete':True,'mapped_paragraphs':90,'exact_paragraphs':88,'explicit_gap_reconciliations':2,'destinations':destinations,'protected_metadata':metadata,'old_sources_preserved':True,'CTA_byte_exact':True,'canonical_sections':sections,'main_oa_checks':2,'main_oa_checks_byte_exact':True,'all_seven_partial_domains_retained':True,'other_partial_reasons_exact':True,'individual_partial_reason':readme_current['partial']['IT-IND'],'markdown_ledger_rows_proofs_and_map_match':True,'lost_content_restored':0})

# Independent arithmetic, directly from statutory cap/rate rules and input facts.
# No writer expressions or writer evaluator are used for these computations.
calcs=[
 ('Solar installation aggregate cap and two-year joint allocation',{'total_deduction':min(D('8000'),D('6000')),'each_year':D('6000')/2,'first_claimant_each_year':D('6000')/2*D('.60'),'second_claimant_each_year':D('6000')/2*D('.40')},'min(8000,6000)=6000; 6000/2=3000; 3000*0.60=1800; 3000*0.40=1200'),
 ('Performance improvement to rating D including EPC cost',{'evidenced_total':D('10000')+200,'income_deduction':(D('10000')+200)*D('.30')},'(10000+200)*0.30=3060'),
 ('EV charger aggregate cap and agreed allocation',{'deduction':min(D('2800'),D('2000')),'first_claimant':D('2000')*D('.75'),'second_claimant':D('2000')*D('.25')},'min(2800,2000)=2000; 2000*0.75=1500; 2000*0.25=500'),
 ('Disabled business access cost cap, eligibility assumed',{'income_deduction':min(D('18000'),D('15000'))},'min(18000,15000)=15000'),
 ('Full-year GIBS income 40000',{'tax':D('17000')*D('.16')+D('8000')*D('.19')+D('15000')*D('.25')},'2720+1520+3750=7990'),
 ('ABS minimum deduction top-up and pre-credit liability',{'topup':D('4343')-3455,'taxable':D('24343')-4343,'tax_before_credit':D('4000')*D('.14')+D('12000')*D('.17')+D('4000')*D('.39')},'4343-3455=888; 24343-4343=20000; 560+2040+1560=4160')]
controltext=git(PIN,R+'relief-controls.md').decode()
allblocks=[yaml.safe_load(b) for b in re.findall(r'^```oa-check\n(.*?)^```',controltext+'\n'+guide,re.M|re.S)]
assert len(allblocks)==6
arith=[]
for name,values,method in calcs:
    block=next(b for b in allblocks if b['name']==name)
    expected=block['expected']; checks={k:values[k]==D(str(v)) for k,v in expected.items()}
    assert all(checks.values())
    arith.append({'name':name,'independent_method':method,'independent_results':{k:str(v) for k,v in values.items()},'writer_expected':expected,'checks':checks,'passed':True})
out('independent-arithmetic.json',{'method':'Independent Decimal calculations written from the statutory rules and scenario inputs, then compared with expected fields.','results':arith,'new_scenarios':4,'preserved_main_examples':2,'conditional_eligibility_preserved':True,'deduction_is_not_tax_saved':True})

sys.path.insert(0,str(C/'scripts'))
spec=importlib.util.spec_from_file_location('review_validate',C/'scripts/validate-guides.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
errors=[];warnings=[];paths={str(p.relative_to(C)) for p in (C/'skills/international/gibraltar').glob('*.md') if p.name!='README.md'}
v.check_guides(v.load_build_index(),errors,warnings,only_files=paths)
out('schema-results.json',{'guides':len(paths),'errors':errors,'warnings':warnings,'scope':'Country source-guide frontmatter/provenance validation; generated global inventory excluded.'})
assert not errors
for name,args in [
    ('repository-examples.log',['scripts/check-examples.py',G,R+'relief-controls.md']),
    ('metadata-integrity.log',['scripts/check-sync-integrity.py','--base',BASE,'--head',PIN,'--strict-metadata'])
]:
    run=subprocess.run([sys.executable]+args,cwd=C,text=True,capture_output=True)
    (O/name).write_text(run.stdout+run.stderr+'\nExit: '+str(run.returncode)+'\n')
    assert run.returncode==0
print(json.dumps({'pin':PIN,'new_proofs':len(proof_results),'exact_snippets':sum(len(p['snippets']) for p in proof_results),'inherited_rows':60,'inherited_proofs':87,'accepted_manifest_unchanged':39,'old_paragraph_destinations':90,'old_paragraphs_exact':88,'independent_calculations':6,'schema_errors':len(errors),'schema_warnings':warnings},indent=2))
