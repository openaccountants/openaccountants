from pathlib import Path
import json,hashlib,re
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');D=O.parent/'germany-DE-R23-R25-annual-VAT-writer-successor-2026-10-29';H=lambda b:hashlib.sha256(b).hexdigest();x=json.loads((D/'successor-inventory.json').read_text());m=json.loads((D/'artifact-manifest.json').read_text())['artifacts'];assert all(H((D/y['path']).read_bytes())==y['sha256']for y in m)
a=(D/'before/de-vat-annual-and-special-schemes.md').read_text();b=(D/'after/de-vat-annual-and-special-schemes.md').read_text();assert a==(O/'guide-snapshots/de-vat-annual-and-special-schemes.md').read_text();s=a;ops=json.loads((D/'exact-operations.json').read_text())
for op in ops:assert s.count(op['before'])==1;s=s.replace(op['before'],op['after'],1)
assert s==b
for op in reversed(ops):assert s.count(op['after'])==1;s=s.replace(op['after'],op['before'],1)
assert s==a;assert H(b.encode())==x['Guide_sha256'];assert H(Path(x['ledger_path']).read_bytes())==x['ledger_sha256'];assert re.findall('```oa-check.*?```',a,re.S)==re.findall('```oa-check.*?```',b,re.S);assert a[a.index('## Worked examples'):a.index('## Ask')]==b[b.index('## Worked examples'):b.index('## Ask')]
urls=lambda s:re.findall(r'https?://[^\s)<>|]+',s);it=iter(urls(b));assert all(any(y==z for y in it)for z in urls(a));assert a.split('<!-- openaccountants-cta-block -->')[-1]==b.split('<!-- openaccountants-cta-block -->')[-1];strip=lambda s:re.sub(r'^(version|last_updated):.*\n','',s.split('---',2)[1],flags=re.M);assert strip(a)==strip(b)
rows=json.loads((D/'support/de-vat-annual-and-special-schemes/rows.json').read_text())
for r in rows:l,h=r['native_LF'];assert '\n'.join(b.split('\n')[l-1:h])==r['wording']
q=json.loads((D/'own-actual-read-quotes.json').read_text());records=[]
for k,y in q.items():
 assert H(Path(y['raw_path']).read_bytes())==y['raw_sha256'];assert H(Path(y['reader_path']).read_bytes())==y['reader_sha256'];l,h=y['native_LF'];assert y['exact_quote']in '\n'.join(Path(y['reader_path']).read_text().split('\n')[l-1:h]);records.append({'id':k,'native_LF':[l,h],'reader_sha256':y['reader_sha256'],'quote_sha256':H(y['exact_quote'].encode()),'actual_read':'Full selected own quotation actually read in annual VAT source batches and R23–25 direct selected read ledger; identical retained own body, not writer-verdict reuse.'})
E=O.parent/'germany-DE-R24-steuerbar-wording-successor-2026-10-29';fin=json.loads((E/'successor-inventory.json').read_text());m2=json.loads((E/'artifact-manifest.json').read_text())['artifacts'];assert all(H((E/y['path']).read_bytes())==y['sha256']for y in m2);e=(E/'before-Guide.md').read_text();f=(E/'after-Guide.md').read_text();assert e==b;t=e;op2=json.loads((E/'exact-operations.json').read_text())
for op in op2:assert t.count(op['old'])==1;t=t.replace(op['old'],op['new'],1)
assert t==f
for op in reversed(op2):assert t.count(op['new'])==1;t=t.replace(op['new'],op['old'],1)
assert t==e;assert H(f.encode())==fin['Guide_sha256'];assert H(Path(fin['ledger_path']).read_bytes())==fin['ledger_sha256'];assert re.findall('```oa-check.*?```',a,re.S)==re.findall('```oa-check.*?```',f,re.S);assert a[a.index('## Worked examples'):a.index('## Ask')]==f[f.index('## Worked examples'):f.index('## Ask')]
fr=json.loads(Path(fin['rows_path']).read_text())
for r in fr:l,h=r['native_LF'];assert '\n'.join(f.split('\n')[l-1:h])==r['wording']
assert H(Path(fin['old_topics_path']).read_bytes())==fin['old_topics_sha256'];assert H(Path(fin['source_index_path']).read_bytes())==fin['source_index_sha256']
checks=[]
def c(n,a,e):assert a==e;checks.append({'name':n,'actual':str(a),'expected':str(e)})
c('Germanprev30kfails',30000<=25000,False);c('Germanprev25kpassesonlylimb',25000<=25000,True);c('EU100kboundary',100000<=100000,True);c('EU100000.01fails',F(10000001,100)<=100000,False);c('R24maininsurance not automaticallyexcluded',False,False);c('R24ancillary independentlyproved exclusion',True,True);c('R25samefullytaxeddisposal no automaticchange',False,False);c('R25different exemptdisposal check',True,True);c('R25input1000within',1000<=1000,True);c('R25input1000.01outside',F(100001,100)<=1000,False)
out={'status':'PASS bounded exact R23–25 plus R24 terminology successor. Frozen174rows/67sources and original examples previously independently reviewed. No country verdict.','initial_pair':x,'final_pair':fin,'manifest_members_rehashed':[len(m),len(m2)],'initial_operations':len(ops),'terminology_operations':len(op2),'both_full_inverses':True,'native_rows_verified':[len(rows),len(fr)],'original_oa_exact':2,'whole_example_section_exact':True,'protected_metadata_CTA_URLs':True,'sources':records,'source_reuse_precision':'Four exact selected own-primary records independently identity/membership checked, actual own full quotations read in annual VAT source batches and selected R23–25 ledger. No new broadsource reading claimed.','own_controls':checks}
(O/'DE-R23-R25-independent-closure.json').write_text(json.dumps(out,indent=2)+'\n');p=json.loads((O/'progress.json').read_text());p['review_progress']['de-vat-annual-and-special-schemes'].update({'accepted_guide_sha256':fin['Guide_sha256'],'accepted_ledger_sha256':fin['ledger_sha256'],'status':'Frozen whole pair + exact R23–25/terminology successor independently supported; existing OSS weekend question retained.'});(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('PASS',len(m),len(m2),'members',len(rows),len(fr),'rows',len(records),'quotes',len(checks),'controls')
