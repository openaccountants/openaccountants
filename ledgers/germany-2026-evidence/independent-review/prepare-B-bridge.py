from pathlib import Path
import json,hashlib,re,sys
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');A=O.parent/'germany-ledger-writer-2026-10-28';B=O.parent/'germany-ledger-writer-B-2026-10-29';norm=lambda s:' '.join(s.split());H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
prior=[]
for slug in ['de-income-tax','de-self-employed-income-tax','de-employee-income-tax','de-partners-and-part-year','de-corporate-tax','leaving-germany-exit-tax','de-uk-employer-first-hire','de-non-resident-tax','de-vat-annual-and-special-schemes','germany-einvoice','de-crypto-tax','germany-to-switzerland-cross-border-tax','de-treaty-withholding-rates','germany-transfer-pricing','germany-payroll']:
 for n,x in enumerate(json.loads((A/'support'/slug/'actual-read-quotes.json').read_text()),1):prior.append((slug,n,x))
slug=sys.argv[1];rows=json.loads((B/'support'/slug/'rows.json').read_text());bank=json.loads((B/'used-source-read-scopes.json').read_text());
for prev in ['de-trade-tax','de-einkommensteuer-freelancer','germany-vat-return','de-capital-gains','de-social-contributions','de-payroll-benefits']:
 for n,k in enumerate(dict.fromkeys(k for r in json.loads((B/'support'/prev/'rows.json').read_text())for k in r['source_quote_ids']),1):
  q=bank[k];prior.append((prev,n,{**q,'url':q['official_url']}))
ids=list(dict.fromkeys(k for r in rows for k in r['source_quote_ids']));out=[]
for n,k in enumerate(ids,1):
 q=bank[k];assert H(q['raw_path'])==q['raw_sha256'];assert H(q['reader_path'])==q['reader_sha256'];a,b=q['native_LF'];assert q['exact_quote']in '\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);m=[(s,i,x)for s,i,x in prior if x['raw_sha256']==q['raw_sha256'] and norm(q['exact_quote'])in norm(x['exact_quote']) and x['url']==q['official_url']]
 r={'row':n,'id':k,'source':q}
 if m:r['actual_read_bridge']={'guide':m[0][0],'quote_row':m[0][1],'conditions':'Exact original raw+official URL and quotation words; normalisation only joins extracted whitespace/formfeeds. Current independent literal reader span membership separately checked, not source-wide read.'}
 else:r['pending_direct_read']=True
 out.append(r)
(O/(slug+'-quote-reuse-plan.json')).write_text(json.dumps(out,indent=2)+'\n');print('total',len(ids),'bridge',sum('actual_read_bridge'in r for r in out));print('NEW',[(r['row'],r['id'])for r in out if 'pending_direct_read'in r])
