from pathlib import Path
import json,re,subprocess,hashlib
import yaml
K=Path(__file__).resolve().parent;C=K.parents[3];B=C.parent;S=B/'work/sources';G=C/'skills/international/gibraltar/gi-corporate-tax.md';BASE='b98e7f01d8d5468e0ad4a99a09d03392244d1ab6';SPLIT='43206e9939b3d2add9de213897fbec30aafa9c36'
def git(*args):return subprocess.check_output(['git',*args],cwd=C)
def sha(b):return hashlib.sha256(b).hexdigest()
def norm(t):return re.sub(r'\s+',' ',t).strip()
def clean(t):return norm('\n'.join(x for x in t.splitlines() if not re.match(r'^\s*(?:© Government of Gibraltar|Page \d+ of \d+|2010-21\s+Income Tax|Income Tax\s+2010-21)',x)))
def paragraphs(text):
 body=text.split('---',2)[2].split('<!-- openaccountants-cta-block -->')[0];head='Title';out=[]
 for p in re.split(r'\n\s*\n',body.strip()):
  if p.startswith('#'):
   if p.startswith('## '):head=p.lstrip('#').strip()
   elif p.startswith('### '):head=head.split(' > ')[0]+' > '+p.lstrip('#').strip()
   continue
  out.append((head,p))
 return out
j=json.loads((K/'ledger.json').read_text());current=G.read_text();before=(K/'gi-corporate-tax.before.txt').read_text();assert before.encode()==git('show',BASE+':'+str(G.relative_to(C)))
old=paragraphs(before);cur=paragraphs(current);arch=(K/'preserved-corporate-controls.md').read_text();maps=[]
changed={3:('Earlier source reads and completed corporate reviews','Earlier read dates retained; actual new ledger/read scope and independent-acceptance limit recorded.'),96:('If required payments on account will exceed','Unverified CT4-field limit narrowed by the sourced procedure; statutory decision/surcharge conditions retained.'),110:('Earlier source reads are preserved','Earlier source date preserved; actual new read scopes distinguished.')}
for i,(head,p) in enumerate(old,1):
 match=[(h,q) for h,q in cur if q==p]
 if match:dest='Guide: '+match[0][0];q=p;why='Full original paragraph byte-exact'
 elif p in arch:dest='Research: preserved-corporate-controls.md';q=p;why='Full original executable block/context byte-exact in supplement'
 else:
  assert i in changed,(i,p[:120]);prefix,why=changed[i];match=[(h,q) for h,q in cur if q.startswith(prefix)];assert len(match)==1,(i,prefix);dest='Guide: '+match[0][0];q=match[0][1]
 maps.append({'id':f'CORP-P{i:03}','old_heading':head,'old_paragraph_sha256':sha(p.encode()),'actual_old_anchor':norm(p)[:180],'destination':dest,'current_paragraph_sha256':sha(q.encode()),'full_paragraph_exact_in_guide':bool([1 for h,z in cur if z==p]),'full_paragraph_exact_in_guide_or_archive':p==q,'disposition':why})
assert len(maps)==113 and sum(m['full_paragraph_exact_in_guide_or_archive'] for m in maps)==110
j['old_paragraph_map']=maps
src={
'https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf':clean((S/'income-tax-act-20260323.txt').read_text()),
'https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf':clean((S/'rates-tax-rules-20240701.txt').read_text()),
'https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force':norm((S/'uk-gibraltar-treaty-official.txt').read_text()),
'https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate':norm((S/'corporate/corporate-current.txt').read_text()),
'https://www.gibraltar.gov.gi/contacts/income-tax-office-76':norm((S/'corporate/ito-contacts-current.txt').read_text()),
'https://www.gibraltar.gov.gi/new/sites/default/files/1/01/guidance_on_business_entertainment_expenditure.pdf':norm((S/'corporate/business-entertainment.txt').read_text()),
'https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Corporate/Schedule%2010%20Table%20-%20Payments%20on%20Account%20-%202022%20to%202033.pdf':norm((S/'corporate/payments-allocation-2022-2033.txt').read_text()),
'https://www.gibraltar.gov.gi/new/sites/default/files/HMGoG_Documents/CT4%20-%20Claim%20to%20reduce%20payments%20on%20account%20for%20an%20accounting%20period.xls':norm(' '.join(str(c['value']) for sh in json.loads((S/'ct4-payments-reduction-cells.json').read_text()) for c in sh['cells']))}
rows=j['rows']+j['inherited_source_matched_rows'];assert len(rows)==118 and len({r['id'] for r in rows})==118
for r in rows:
 assert r['read_on']=='2026-10-28' and r['url'] in src
 assert all(norm(q) in src[r['url']] for q in r['quotes']),(r['id'],r['provision'])
for r in j['inherited_rule_queue']:
 assert r['id'] in {x['id'].split('.')[0] for x in j['inherited_source_matched_rows']}
assert len(j['inherited_rule_queue'])==93 and sum(len(r['quotes']) for r in rows)==372
assert len(j['nonrule_original_paragraph_ids'])==12 and len(j['original_executable_paragraph_ids'])==8
assert len(set(j['nonrule_original_paragraph_ids'])|set(j['original_executable_paragraph_ids'])|{q['id'] for q in j['inherited_rule_queue']})==113
# Regenerate destination table from the actual current map, retaining all source/rule text.
canon=K/'ledgers/gi-corporate-tax.md';md=canon.read_text();start=md.index('| Original ID |');end=md.index('\n## Nonrule and executable accounting',start)
ls=['| Original ID | Original section | Actual original content anchor | Current destination / preservation |','|---|---|---|---|']
for m in maps:ls.append('| '+' | '.join(v.replace('|','\\|') for v in [m['id'],m['old_heading'],m['actual_old_anchor'],m['destination']+'; '+m['disposition']])+' |')
md=md[:start]+'\n'.join(ls)+'\n'+md[end:];md=md.replace('in ledger.json','in [ledger.json](../ledger.json)');canon.write_text(md)
for r in rows:
 assert r['rule'].replace('|','\\|') in md,r['id']
 for q in r['quotes']:assert q.replace('|','\\|') in md,(r['id'],q)
(K/'ledger.json').write_text(json.dumps(j,indent=2)+'\n')
marker='<!-- openaccountants-cta-block -->';assert before[before.index(marker):]==current[current.index(marker):]
a=yaml.safe_load(before.split('---',2)[1]);b=yaml.safe_load(current.split('---',2)[1]);mutable={'description','last_updated','version','sources'};assert {k:v for k,v in a.items() if k not in mutable}=={k:v for k,v in b.items() if k not in mutable}
H=['Who this applies to','Rates, bands and thresholds','The base','Deadlines and filing','Penalties and interest','Cross-border points','Two worked examples that recompute','Ask the client first','Sources'];assert re.findall(r'^## (.+)$',current.split(marker)[0],re.M)==H
pat=re.compile(r'```oa-check\n.*?```',re.S);assert len(pat.findall(current))==2 and len(pat.findall(arch))==6
chosen=[C/'skills/research/gibraltar-2026/ordinary-completion-2026-10-28/interest-controls.md',C/'skills/research/gibraltar-2026/ordinary-completion-2026-10-28/exit-controls.md',K/'ct4-controls.md',K/'preserved-corporate-controls.md',K/'rent-control.md',K.parent/'individual-completion-2026-10-28/preserved-individual-controls.md',K.parent/'individual-completion-2026-10-28/ordinary-deduction-controls.md']
allblocks=[]
for p in list((C/'skills/international/gibraltar').glob('gi-*.md'))+chosen:allblocks+=pat.findall(p.read_text())
oldblocks=[]
for p in git('ls-tree','-r','--name-only',SPLIT,'skills/international/gibraltar').decode().splitlines():
 if p.endswith('.md'):oldblocks+=pat.findall(git('show',SPLIT+':'+p).decode())
assert len(oldblocks)==47 and all(x in allblocks for x in oldblocks);assert len(allblocks)==58
for p in ['skills/international/gibraltar/gi-connected-party-pricing-and-interest.md','skills/international/gibraltar/gi-foreign-tax-relief.md']:
 assert (C/p).read_bytes()==git('show',BASE+':'+p)
historical=[]
for p in git('ls-tree','-r','--name-only',SPLIT,'docs/research').decode().splitlines():
 if 'gibraltar' in p:assert (C/p).read_bytes()==git('show',SPLIT+':'+p);historical.append(p)
prior=[]
for p in git('ls-tree','-r','--name-only',BASE,'skills/research/gibraltar-2026/ordinary-completion-2026-10-28').decode().splitlines():
 assert (C/p).read_bytes()==git('show',BASE+':'+p);prior.append(p)
res={'phase':'Full corporate writer ledger complete; current country review pending','guide_version':b['version'],'guide_sha256':sha(G.read_bytes()),'canonical_ledger_sha256':sha(canon.read_bytes()),'rule_rows':118,'quote_snippets_source_matched':372,'original_paragraph_map':113,'original_paragraphs_exact_across_guide_archive':110,'explicit_old_paragraph_reconciliations':3,'inherited_legal_derived_paragraphs_covered':93,'nonrule_paragraphs_accounted':12,'original_control_paragraphs_accounted':8,'remaining_inherited_writer_entries':0,'canonical_h2_count':9,'main_corporate_controls':2,'original_corporate_controls_archived':6,'calculation_blocks_across_current_pack_and_selected_supplements':58,'original_country_controls_preserved':47,'historical_research_byte_exact':len(historical),'prior_accepted_research_byte_exact':len(prior),'corporate_cta_exact':True,'protected_metadata_exact':True,'prior_accepted_financing_foreign_methods_exact':True,'new_independent_acceptance':False,'published':False,'country_complete':False}
(K/'writer-complete-audit.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
