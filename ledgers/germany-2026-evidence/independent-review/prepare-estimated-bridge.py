from pathlib import Path
import json,hashlib
O=Path(__file__).parent;A=O.parent/'germany-ledger-writer-2026-10-28';B=O.parent/'germany-ledger-writer-B-2026-10-29';D=O.parent/'germany-root-estimated-ledger-2026-10-29';norm=lambda s:' '.join(s.split());H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();prior=[]
for s in ['de-income-tax','de-self-employed-income-tax','de-employee-income-tax','de-partners-and-part-year','de-corporate-tax','leaving-germany-exit-tax','de-uk-employer-first-hire','de-non-resident-tax','de-vat-annual-and-special-schemes','germany-einvoice','de-crypto-tax','germany-to-switzerland-cross-border-tax']:
 for i,q in enumerate(json.loads((A/'support'/s/'actual-read-quotes.json').read_text()),1):prior.append((s,i,q))
bankB=json.loads((B/'used-source-read-scopes.json').read_text())
for s in ['de-trade-tax','de-einkommensteuer-freelancer','germany-vat-return','de-capital-gains']:
 rows=json.loads((B/'support'/s/'rows.json').read_text());ids=list(dict.fromkeys(k for r in rows for k in r['source_quote_ids']))
 for i,k in enumerate(ids,1):
  q=bankB[k];prior.append((s,i,{'raw_sha256':q['raw_sha256'],'url':q['official_url'],'exact_quote':q['exact_quote']}))
qs=json.loads((D/'source-quotes.json').read_text());bank={y['id']:y for y in json.loads((D/'source-identities.json').read_text())};out=[]
for i,q in enumerate(qs,1):
 r={'row':i,'source':q}
 if 'reader' in q:
  z=bank[q['source']];rp=D/q['reader'];assert H(rp)==q['reader_sha256'];assert H(D/z['raw'])==q['raw_sha256'];a,b=q['native_LF'];assert q['exact_quote']in'\n'.join(rp.read_text().split('\n')[a-1:b]);r['identity']=z
  m=[(s,n,x)for s,n,x in prior if x['raw_sha256']==q['raw_sha256']and x['url']==q['url']and norm(q['exact_quote'])in norm(x['exact_quote'])]
  if m:r['actual_read_bridge']={'guide':m[0][0],'quote_row':m[0][1],'scope':'Exact same raw/URL/complete selected quotation words with whitespace joining only; current paragraph-native membership independently checked. Not a source-wide reading or whole-rule PASS.'}
  else:r['pending_direct_read']=True
 else:r['pending_observation_read']=True
 out.append(r)
(O/'de-estimated-tax-quote-reuse-plan.json').write_text(json.dumps(out,indent=2)+'\n');print('TOTAL',len(out),'BRIDGES',sum('actual_read_bridge'in r for r in out));print('NEW',[(r['row'],r['source']['id'])for r in out if 'pending_direct_read'in r or'pending_observation_read'in r])
