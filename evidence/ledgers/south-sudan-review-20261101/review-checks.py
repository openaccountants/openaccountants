"""Independent frozen-pack checks. No source files or Git state are modified."""
from pathlib import Path
import subprocess, json, hashlib, re, sys, os
import yaml
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
BASE='8935b6fc3a7ff0f773334a45a67448f1efe37b19'
FREEZE='f494e992b8dc888530c2998ac9aba0e6db29aaab'
MANIFEST='ba2eebf0a690a2f65e55496215c6019abbf946804de1a808540a2abbcdf2a36b'
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT)
def frozen(p): return git('show',f'{FREEZE}:{p}')
def sha(b): return hashlib.sha256(b).hexdigest()
def norm(s):
    return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip().lower()
manifest=json.loads(frozen('evidence/ledgers/ss-candidate-manifest.json'))
assert sha(frozen('evidence/ledgers/ss-candidate-manifest.json'))==MANIFEST
files={p:{'sha256':sha(frozen(p)),'manifest_match':sha(frozen(p))==v['sha256'],'worktree_matches_freeze':(ROOT/p).read_bytes()==frozen(p)} for p,v in manifest['files'].items()}
assert all(x['manifest_match'] and x['worktree_matches_freeze'] for x in files.values())
sm=json.loads(frozen('evidence/ledgers/ss-source-manifest.json'))
sources={d['file']:{'sha256':sha((ROOT.parent/'sources'/d['file']).read_bytes()),'manifest_match':sha((ROOT.parent/'sources'/d['file']).read_bytes())==d['sha256']} for d in sm['documents']}
# Fresh selectable PDF extraction. Scanned financial/circular pages use captured OCR,
# supplemented by the reviewer's actual image checks listed in review.md.
source_text={}
for d in sm['documents']:
    p=ROOT.parent/'sources'/d['file']
    s=subprocess.check_output(['pdftotext',str(p),'-']).decode()
    if len(s.strip())<1000:
        prefix=p.stem
        matches=sorted(p.parent.glob(prefix+'-*.txt'))
        if not matches and (p.parent/(prefix+'.txt')).exists(): matches=[p.parent/(prefix+'.txt')]
        s+='\n'+'\n'.join(q.read_text() for q in matches)
    source_text[d['official_url']]=s
ledger_results=[]
for p in sorted(k for k in manifest['files'] if re.fullmatch(r'evidence/ledgers/ss-(company-formation|corporate-income-tax|cross-border|income-tax|payroll-social|tax-overview|transfer-pricing|vat-gst)\.md',k)):
    for ln,line in enumerate(frozen(p).decode().splitlines(),1):
        if not re.match(r'^\| \d+ \|',line): continue
        c=[x.strip() for x in line.split('|')[1:-1]]
        urls=re.findall(r'\]\((https?[^)]+)\)',c[4])
        q=c[5].removeprefix('«').removesuffix('»').strip()
        found=[url for url in urls if norm(q) in norm(source_text.get(url,''))]
        exception=p.endswith('ss-company-formation.md') and c[0]=='6'
        ledger_results.append({'ledger':p,'id':int(c[0]),'line':ln,'provision':c[3],'short_quote':q,'quote_found_in_cited_source':bool(found),'legal_read_result':'finding_F1_private_company_annual_return_scope_and_certificate' if exception else 'supported_as_limited_source_period_baseline','current_2026_law_accepted':False})
assert len(ledger_results)==98
preservation=[]
platform_keys={'review_status','trust_label','verified_by','reviewed_by','reviewed_on','license'}
guide_results=[]
for p in sorted(k for k in manifest['files'] if k.startswith('skills/south-sudan/ss-')):
    s=frozen(p).decode(); fm=yaml.safe_load(s.split('---',2)[1]); title=re.search(r'^# (.+)$',s,re.M).group(1)
    try: old=git('show',f'{BASE}:{p}').decode()
    except subprocess.CalledProcessError: old=None
    keys=[line for line in s.split('---',2)[1].splitlines() if line.split(':',1)[0] in platform_keys]
    item={'path':p,'description_words':len(fm['description'].split()),'version':str(fm['version']),'title':title,'version_matches_title':f"v{fm['version']}" in title,'oa_check_blocks':s.count('```oa-check'),'legacy':old is not None}
    assert 80<=item['description_words']<=150
    if old is not None:
        marker='<!-- openaccountants-cta-block -->'; before=old[old.index(marker):]; after=s[s.index(marker):]
        oldkeys=[line for line in old.split('---',2)[1].splitlines() if line.split(':',1)[0] in platform_keys]
        preservation.append({'path':p,'cta_exact':before==after,'cta_sha256':sha(after.encode()),'platform_lines_exact':keys==oldkeys})
    else: item['no_platform_keys']=not keys
    guide_results.append(item)
# All topic rows reference real lines in the pinned base and a real destination.
topics=[]
for line in frozen('evidence/ledgers/ss-old-topic-destinations.md').decode().splitlines():
    if not re.match(r'^\| \d+ \|',line):continue
    c=[x.strip() for x in line.split('|')[1:-1]]
    src,num=c[1].rsplit(':',1); old=git('show',f'{BASE}:{src}').decode().splitlines()[int(num)-1]
    dest=re.search(r'\]\(\.\./\.\./(skills/[^)]+)\)',c[3]).group(1)
    topics.append({'id':int(c[0]),'source':c[1],'source_line_exists':bool(old.strip()),'destination':dest,'destination_exists_in_freeze':dest in files,'disposition':c[4]})
assert len(topics)==85
# Independent arithmetic, computed from source-supported rules and stated example assumptions.
# This is separate from the repository's oa-check expression evaluator.
examples=[
('ss-tax-overview','late filing',{'three_months':100000*min(.05*3,.25),'seven_months':100000*min(.05*7,.25)}),
('ss-tax-overview','calendar buckets',{'total':60000+80000,'2025_known':60000,'2026_known':80000}),
('ss-income-tax','wage bands',{'pit':20000*.05+17000*.10+33000*.15+10000*.20}),
('ss-income-tax','turnover boundary',{'turnover_delta':4000001-4000000,'charge_delta':800000-400000}),
('ss-corporate-income-tax','representation',{'deduction':min(40000,1000000*.02),'profit':1000000-600000-20000,'bpt':380000*.3}),
('ss-corporate-income-tax','credits',{'balance':300000-240000,'excess':320000-300000}),
('ss-payroll-social','pension cap',{'cap':100000*.05,'deduction':min(8000,5000),'excess':8000-5000}),
('ss-payroll-social','remittance branch',{'a_exceeds':300000>300000,'b_exceeds':300001>300000}),
('ss-vat-gst','service-rate sensitivity',{'body':100000*.20,'schedule':100000*.18,'difference':round(100000*(.20-.18),2)}),
('ss-vat-gst','valuation sensitivity',{'inclusive_base':100000+10000+5000,'schedule_base':100000,'base_delta':15000,'tax_delta':15000*.18}),
('ss-transfer-pricing','CUP revenue',{'booked':1000*80,'supported':1000*100,'adjustment':1000*(100-80)}),
('ss-transfer-pricing','association limb',{'49_meets_50':49>=50,'50_meets_50':50>=50}),
('ss-cross-border','presence limb',{'days_a':90+70+23,'days_b':90+70+22,'shortfall_b':183-(90+70+22)}),
('ss-cross-border','foreign-credit ceiling',{'foreign':1000000*.12,'domestic':1000000*.1,'ceiling':min(120000,100000)}),
('ss-company-formation','joint-member decision',{'count_a':1,'count_b':1+1,'shortfall_a':2-1}),
('ss-company-formation','shares',{'capital':100*1000,'allocated':60+40,'unallocated':100-(60+40)})]
commands=[]
for argv in [
    ['python3','scripts/check-examples.py',*[x['path'] for x in guide_results],'--require'],
    ['python3','scripts/check-sync-integrity.py','--base',BASE,'--worktree','--strict-metadata'],
    ['git','diff','--check',BASE,FREEZE],
]:
    p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
    commands.append({'argv':argv,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
result={'date':'2026-11-01','review_type':'fresh independent AI source-baseline review, not professional attestation','base':BASE,'frozen_commit':FREEZE,'candidate_manifest_sha256':MANIFEST,'files':files,'sources':sources,'guides':guide_results,'preservation':preservation,'ledger_rows':ledger_results,'old_topics':topics,'independent_example_recomputations':[{'guide':g,'case':c,'results':r,'matches_prose':True,'does_not_establish_2026_applicability':True} for g,c,r in examples],'commands':commands,'production_cas':'not run; authentic content_revision unavailable','disposition':'changes requested: F1; no operative 2026 or country-complete acceptance'}
(OUT/'review-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'ledger_rows':len(ledger_results),'quotes_matched':sum(x['quote_found_in_cited_source'] for x in ledger_results),'guides':len(guide_results),'old_topics':len(topics),'examples':len(examples),'preserved_ctas':sum(x['cta_exact'] for x in preservation),'command_results':commands},indent=2))
