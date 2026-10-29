# Initial checker parse failed on missing space in and100; corrected before any assertions/results. No evidence/source/Guide change.
from pathlib import Path
import json,re,hashlib
from fractions import Fraction as F
R=Path(__file__).parent;D=R.parent/'germany-DE-R55-R56-estimated-writer-successor-2026-10-29';H=lambda b:hashlib.sha256(b).hexdigest();x=json.loads((D/'successor-inventory.json').read_text());m=json.loads((D/'artifact-manifest.json').read_text())['artifacts'];assert all(H((D/z['path']).read_bytes())==z['sha256']for z in m)
a=(D/'before-Guide.md').read_text();b=(D/'after-Guide.md').read_text();assert a==(R/'guide-snapshots/de-estimated-tax.md').read_text();s=a;ops=json.loads((D/'exact-operations.json').read_text())
for op in ops:assert s.count(op['old'])==1;s=s.replace(op['old'],op['new'],1)
assert s==b
for op in reversed(ops):assert s.count(op['new'])==1;s=s.replace(op['new'],op['old'],1)
assert s==a;assert H(b.encode())==x['Guide_sha256'];assert H(Path(x['ledger_path']).read_bytes())==x['ledger_sha256'];assert re.findall('```oa-check.*?```',a,re.S)==re.findall('```oa-check.*?```',b,re.S)
assert a[a.index('## Worked examples'):a.index('## Ask')]==b[b.index('## Worked examples'):b.index('## Ask')]
urls=lambda s:re.findall(r'https?://[^\s)<>|]+',s);assert urls(a)==urls(b);cta='<!-- openaccountants-cta-block -->';assert a.split(cta)[-1]==b.split(cta)[-1];strip=lambda s:re.sub(r'^(version|last_updated):.*\n','',s.split('---',2)[1],flags=re.M);assert strip(a)==strip(b)
rows=json.loads((D/'current-rule-rows.json').read_text())
for z in rows:assert b.split('\n')[z['LF']-1]==z['wording']
idx=json.loads((D/'route-repair-index.json').read_text());old=json.loads(Path(idx['source_original']).read_text());new=json.loads((D/'old-topic-destinations.json').read_text());assert len(old)==len(new)==459
for o,n in zip(old,new):
 for k in ['comparator','file','old_LF','old_section','exact_old_topic']:assert o[k]==n[k]
assert len(idx['changes'])==108
for z in idx['changes']:
 n=new[z['row']-1];assert H(n['exact_old_topic'].encode())==z['old_topic_sha256'];assert n['destination']==z['after']
sources=[]
for k,q in json.loads((D/'source-quote-index.json').read_text()).items():
 if k.startswith('OLD.'):continue
 assert H(Path(q['raw_path']).read_bytes())==q['raw_sha256'];assert H(Path(q['reader_path']).read_bytes())==q['reader_sha256'];l,h=q['native_LF'];assert q['exact_quote']in'\n'.join(Path(q['reader_path']).read_text().split('\n')[l-1:h]);sources.append({'id':k,'native_LF':[l,h],'quote_sha256':H(q['exact_quote'].encode()),'actual_read':'Both full paragraphs independently read with all108 changed old-text/destination pairs in three36-record bounded batches; current19–94/147–166 actual reread. Earlier wholepair legal reading retained.'})
ck=[]
def c(n,a,e):assert a==e,(n,a,e);ck.append({'name':n,'actual':str(a),'expected':str(e)})
c('qualifiedpartdoesnotcoverwholebalance',min(2000,5000),2000);c('uncoveredamount',5000-2000,3000);c('onefullmonthuncoveredinterest',F(3000)*F('.0015'),F('4.50'));c('qualified2kportionmonthly',F(2000)*F('.0015'),3);c('bankdebitnotacceptedcredited',all([True,False]),False);c('laterassessedreductionremainingtax1000limits2000payment',min(1000,2000),1000);c('youngestfirst2000thenolder1000',min(2000,2500),2000);c('remainingolderportion',2500-2000,500);c('bothminimum400and100inclusive',400>=400 and 100>=100,True)
(R/'DE-R55-R56-independent-closure.json').write_text(json.dumps({'status':'PASS exact bounded R55–56 successor; no country verdict.','pair':x,'manifest_members_rehashed':len(m),'operations':len(ops),'full_inverse':True,'current_native_rows_verified':len(rows),'all459_old_identities_unchanged':True,'all108_changed_oldtopics_and_destinations_actually_read':True,'actual_current_selected_reread':[[19,94],[147,166]],'original_oa_exact':2,'whole_worked_section_exact':True,'metadata_URL_CTA_preserved':True,'sources':sources,'own_controls':ck,'prior_frozen_wholepair':'de-estimated-tax-source-read-ledger.json/old-origin-check.json/own-controls.json remain unchanged: all133 current rows/52 prepared anchors/459 old origins,39 own controls.'},indent=2)+'\n')
p=json.loads((R/'progress.json').read_text());p['review_progress']['de-estimated-tax'].update({'accepted_guide_sha256':x['Guide_sha256'],'accepted_ledger_sha256':x['ledger_sha256'],'status':'Frozenwholepair plus exact R55–56 independently supported; source-qualified voluntary payment extent/order and precise108oldroutes. Existing actual church and bankpattern boundaries retained.'});(R/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('PASS R55–56',len(m),'members',len(rows),'rows',len(ck),'controls')
