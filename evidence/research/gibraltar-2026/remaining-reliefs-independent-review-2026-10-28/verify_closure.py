from pathlib import Path
import json,hashlib,re,subprocess
C=Path(__file__).resolve().parents[4]
O=Path(__file__).resolve().parent/'closure-6f53123a'
O.mkdir(exist_ok=True)
BASE='933e6993fe5305609c849551765a27ba9a116e8b'
PIN='6f53123a0306500efec732d97e42abc5ef764388'
R='skills/research/gibraltar-2026/remaining-reliefs-2026-10-28/'
G='skills/international/gibraltar/gi-individual-income-tax.md'
def raw(rev,path):return subprocess.check_output(['git','show',rev+':'+path],cwd=C)
def text(rev,path):return raw(rev,path).decode()
def j(rev,path):return json.loads(raw(rev,path))
def sha(b):return hashlib.sha256(b).hexdigest()
def write(name,d):(O/name).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
a=j(BASE,R+'ledger.json');b=j(PIN,R+'ledger.json')
changed=subprocess.check_output(['git','diff','--name-only',BASE,PIN],cwd=C,text=True).splitlines()
expected={G,'skills/international/gibraltar/README.md',R+'ledger.json',R+'ledgers/gi-individual-income-tax.md',R+'relief-controls.md',R+'writer-section-repair.json',R+'review-provenance-repair.json'}
assert set(changed)==expected
locations=[]
guide=text(PIN,G)
for x,y in zip(a['rows'],b['rows']):
    if not x['id'].startswith('REL-'):
        assert x==y
        continue
    assert {k:v for k,v in x.items() if k not in ['guide_section','new_anchor']}=={k:v for k,v in y.items() if k not in ['guide_section','new_anchor']}
    ident=y['id'];section=y['guide_section'];anchor=y['new_anchor']
    assert section==('Sources' if ident=='REL-14' else 'The base')
    sectiontext=guide.split('## '+section+'\n',1)[1].split('\n## ',1)[0]
    assert (anchor in sectiontext if ident=='REL-14' else '### '+anchor+'\n' in sectiontext)
    locations.append({'id':ident,'canonical_H2':section,'anchor':anchor,'verified_in_own_section':True,'rule_and_source_fields_exact':True})
assert len(locations)==14
assert a['source_proofs']==b['source_proofs'] and len(b['source_proofs'])==93
assert a['old_paragraph_map']==b['old_paragraph_map']
assert {k:v for k,v in a.items() if k not in ['rows','status','guide_sha256']}=={k:v for k,v in b.items() if k not in ['rows','status','guide_sha256']}
md_before=text(BASE,R+'ledgers/gi-individual-income-tax.md');md_after=text(PIN,R+'ledgers/gi-individual-income-tax.md')
for x,y in zip(a['rows'],b['rows']):
    if not x['id'].startswith('REL-'):continue
    old='| '+x['id']+' | '+x['guide_section']+': '
    new='| '+y['id']+' | '+y['guide_section']+' > '+y['new_anchor']+': '
    assert md_before.count(old)==1
    md_before=md_before.replace(old,new)
assert md_before==md_after
provenance=j(PIN,R+'review-provenance-repair.json')
old=provenance['guide_only_replacement']['old'];new=provenance['guide_only_replacement']['new']
assert text(BASE,G).count(old)==1
assert text(BASE,G).replace(old,new)==guide
assert sha(raw(BASE,G))==provenance['guide_sha256_before']
assert sha(raw(PIN,G))==provenance['guide_sha256_after']==b['guide_sha256']
assert text(BASE,R+'relief-controls.md').replace('# Assumed certified relief calculations, unreviewed additions','# Assumed certified relief calculation controls',1)==text(PIN,R+'relief-controls.md')
# Check README changes are confined to two provenance paragraphs; frontmatter and all other paragraphs exact.
rb=text(BASE,'skills/international/gibraltar/README.md');rn=text(PIN,'skills/international/gibraltar/README.md')
bp=rb.split('\n\n');np=rn.split('\n\n');assert len(bp)==len(np)
readme_deltas=[{'old':x,'new':y} for x,y in zip(bp,np) if x!=y]
assert len(readme_deltas)==2
assert all(x['old'].startswith(('The reviewed continuation is published','1. The ordinary corporate')) for x in readme_deltas)
assert rb.split('---',2)[1]==rn.split('---',2)[1]
# Every old paragraph destination still resolves, and prior unrelated accepted files remain unchanged.
resolved=[]
for p in b['old_paragraph_map']:
    chunks=[v.strip() for v in re.split(r'\n\s*\n',guide)]
    assert any(sha(v.encode())==p['current_sha256'] for v in chunks)
    resolved.append(p['id'])
prior=j(PIN,'skills/research/gibraltar-2026/final-country-review-2026-10-28/closure-4d2640c6/closure.json')
manifest=[]
for p in prior['verification']['accepted_content_manifest']:
    if p['path'] in [G,'skills/international/gibraltar/README.md']:continue
    assert sha(raw(PIN,p['path']))==p['sha256']
    manifest.append(p['path'])
assert len(manifest)==39
for p in prior['verification']['primary_review_evidence']:
    assert sha(raw(PIN,p['path']))==p['sha256']
assert len(re.findall(r'^```oa-check\n',guide,re.M))==2
assert len(re.findall(r'^## ',guide.split('<!-- openaccountants-cta-block -->')[0],re.M))==9
write('checks.json',{'reviewed_initial_head':BASE,'repair_head':PIN,'changed_files':changed,'all_other_tracked_files_byte_exact':True,'corrected_locations':locations,'all_74_rule_fields_unchanged':True,'all_93_proof_units_data_exact':True,'inherited_60_rows_data_exact':True,'old_90_paragraph_map_data_exact':True,'all_90_destinations_still_resolve':True,'markdown_only_14_location_prefixes_changed':True,'guide_only_single_provenance_paragraph_changed':True,'guide_sha256':b['guide_sha256'],'guide_protected_metadata_CTA_tax_content_arithmetic_exact':True,'control_only_title_changed':True,'readme_only_two_provenance_paragraphs_changed':True,'readme_frontmatter_including_all_partial_reasons_exact':True,'readme_changes':readme_deltas,'other_39_accepted_manifest_blobs_exact':True,'prior_independent_review_archived_evidence_exact':True,'main_H2s':9,'main_oa_checks':2})
write('closure.json',{'review_type':'Bounded independent repair closure','read_on':'2026-10-28','initial_review_head':BASE,'accepted_head':PIN,'accepted':True,'open_findings':[],'closed_findings':['GI-REL-01'],'scope':'Fourteen new relief row locations corrected and one neutral Guide review-provenance paragraph, two README provenance paragraphs and supplementary title reviewed. The 933e6993 substantive source/arithmetic acceptance is carried forward because all tax content, proof units, inputs, calculations and inherited evidence remain exact.','guide_version':'0.11','guide_sha256':b['guide_sha256'],'new_rows_accepted':14,'new_proof_units_accepted':6,'exact_snippets_accepted':57,'independent_arithmetic':'Four new conditional scenarios and both preserved main examples previously independently recomputed; all arithmetic content unchanged.','inherited_accepted_scope_preserved':True,'prior_39_unaffected_manifest_files_exact':True,'country_complete':False,'professional_attestation':False,'tier_promoted':False,'not_claimed':['Actual client eligibility or certificate approval','Complete relief schedule or country coverage','ABS/GIBS interaction resolution','No general claim limitation','Retrospective disabled-access gap-period acceptance','Publication, CI, merge or deployment at this repair pin'],'verification':'checks.json','reviewer_actions':{'writer_edits':False,'guide_edits':False,'commits':False,'pushes':False,'external_messages':False,'live_transactions':False,'source_research_reopened':False}})
print('Accepted bounded repair '+PIN+'; 14 actual anchors verified; no open findings.')
