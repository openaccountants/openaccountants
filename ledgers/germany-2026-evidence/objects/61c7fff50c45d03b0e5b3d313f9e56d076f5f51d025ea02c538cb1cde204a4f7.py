from pathlib import Path
import json,hashlib,sys
O=Path(__file__).parent;A=O.parent/'germany-ledger-writer-2026-10-28';B=O.parent/'germany-ledger-writer-B-2026-10-29';slug=sys.argv[1];norm=lambda s:' '.join(s.split());H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();prior=[]
for s in ['de-income-tax','de-self-employed-income-tax','de-employee-income-tax','de-partners-and-part-year','de-corporate-tax','leaving-germany-exit-tax','de-uk-employer-first-hire','de-non-resident-tax','de-vat-annual-and-special-schemes','germany-einvoice','de-crypto-tax','germany-to-switzerland-cross-border-tax','de-treaty-withholding-rates','germany-transfer-pricing']:
 for i,x in enumerate(json.loads((A/'support'/s/'actual-read-quotes.json').read_text()),1):prior.append((s,i,x))
bankB=json.loads((B/'used-source-read-scopes.json').read_text())
for s in ['de-trade-tax','de-einkommensteuer-freelancer','germany-vat-return','de-capital-gains','de-social-contributions','de-payroll-benefits','de-payroll']:
 rows=json.loads((B/'support'/s/'rows.json').read_text());ids=list(dict.fromkeys(k for r in rows for k in r['source_quote_ids']))
 for i,k in enumerate(ids,1):
  x=bankB[k];prior.append((s,i,{'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'exact_quote':x['exact_quote'],'url':x['official_url']}))
bank={json.loads(p.read_text())['id']:json.loads(p.read_text())for p in(A/'sources').glob('*.identity.json')};quotes=json.loads((A/'support'/slug/'actual-read-quotes.json').read_text());out=[]
for n,q in enumerate(quotes,1):
 x=bank[q['source']];assert H(x['raw_path'])==q['raw_sha256'];assert H(x['reader_path'])==q['reader_sha256'];a=q.get('LF_start',q.get('paragraph'));b=q.get('LF_end',a);assert q['exact_quote'] in '\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:b]);m=[(s,i,z)for s,i,z in prior if z['raw_sha256']==q['raw_sha256'] and z['url']==q['url'] and norm(q['exact_quote'])in norm(z['exact_quote'])];r={'row':n,'id':q['id'],'source':q,'reader_path':x['reader_path'],'raw_path':x['raw_path'],'native_LF':[a,b]}
 if m:r['actual_read_bridge']={'guide':m[0][0],'quote_row':m[0][1],'conditions':'Same original raw+official URL; entire selected quote is exact prior quotation words with whitespace/formfeed joining only. Current reader/native membership separately verified; not a full rawbody reading claim.'}
 else:r['pending_direct_read']=True
 out.append(r)
(O/(slug+'-quote-reuse-plan.json')).write_text(json.dumps(out,indent=2)+'\n');print('TOTAL',len(out),'BRIDGES',sum('actual_read_bridge'in r for r in out));print('NEW',[(r['row'],r['id'])for r in out if 'pending_direct_read'in r])
