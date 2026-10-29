from pathlib import Path
import json,hashlib,re
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');D=O.parent/'germany-DE-R09-corporate-rounding-writer-successor-2026-10-29';P=O.parent/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();inv=json.loads((D/'successor-inventory.json').read_text());res={};m=json.loads((D/'artifact-manifest.json').read_text())['artifacts'];assert all(H(D/x['path'])==x['sha256'] for x in m)
for slug,opf in [('de-corporate-tax','exact-operations.json'),('de-trade-tax','R10-exact-operations.json')]:
 a=(D/'before'/f'{slug}.md').read_text();b=(D/'after'/f'{slug}.md').read_text();assert a==(P/'after'/f'{slug}.md').read_text();ops=json.loads((D/opf).read_text());s=a
 for op in ops:assert s.count(op['old'])==1;s=s.replace(op['old'],op['new'],1)
 assert s==b
 for op in reversed(ops):assert s.count(op['new'])==1;s=s.replace(op['new'],op['old'],1)
 assert s==a;assert H(D/'after'/f'{slug}.md')==inv[slug]['Guide_sha256'];assert H(Path(inv[slug]['ledger_path']))==inv[slug]['ledger_sha256']
 assert re.findall('```oa-check.*?```',a,re.S)==re.findall('```oa-check.*?```',b,re.S)
 assert a.split('---',2)[1].replace('version: 0.3','version: 0.4').replace('version: 1.2','version: 1.3')==b.split('---',2)[1]
 rows=json.loads((D/'support'/('rows.json' if slug=='de-corporate-tax' else 'trade-rows.json')).read_text())
 for x in rows:l,h=x['native_LF'];assert '\n'.join(b.split('\n')[l-1:h])==x['wording']
 res[slug]={**inv[slug],'exact_operations':len(ops),'full_inverse':True,'native_rows_checked':len(rows),'original_oa_exact':2,'tax_source_numerical_delta':'Only corporate new assessed-rounding sentence and stipulated separator; trade no rule/number change'}
x=list(json.loads((D/'own-actual-read-quotes.json').read_text()).values())[0];assert H(Path(x['raw_path']))==x['raw_sha256'];assert H(Path(x['reader_path']))==x['reader_sha256'];assert x['exact_quote'] in Path(x['reader_path']).read_text().split('\n')[6]
controls=[{'input_taxable':v,'unrounded_15pct':str(v*15/100),'positive_assessed_KSt':(v*15)//100}for v in [10001,10006,10007,10000]];assert [x['positive_assessed_KSt']for x in controls]==[1500,1500,1501,1500]
(O/'DE-R09-R10-independent-closure.json').write_text(json.dumps({'status':'PASS bounded exact R09/R10 deltas only. Corporate whole-pair reading is complete; trade whole-pair reading is still pending. No country verdict.','members_rehashed':len(m),'pairs':res,'source_read_reuse':'KStG31(1) full nativeLF7 independently actually read as corporatequote24; exact raw/reader/quote identities matched','own_positive_rounding_controls':controls},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress']['de-corporate-tax']['status']='Exact R07/R08/R09 successors independently supported; whole frozen229 units/120quotes+all source changed deltas read. Country ordinary-limit disposition later.';p['review_progress']['de-corporate-tax']['accepted_guide_sha256']=inv['de-corporate-tax']['Guide_sha256'];p['review_progress']['de-corporate-tax']['accepted_ledger_sha256']=inv['de-corporate-tax']['ledger_sha256'];(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('boundedPASS27manifest/2inverse/4roundcontrols')
