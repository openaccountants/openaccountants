from pathlib import Path
import json,hashlib
R=Path(__file__).parent;D=R.parent/'germany-root-rental-ledger-2026-10-29';norm=lambda s:' '.join(s.split());H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();prior=[]
for f in R.glob('*-quote-reuse-plan.json'):
 if f.name=='de-rental-income-quote-reuse-plan.json':continue
 slug=f.name[:-len('-quote-reuse-plan.json')]
 if not(R/(slug+'-source-read-ledger.json')).exists():continue
 for x in json.loads(f.read_text()):
  q=x['source'];prior.append({'guide':slug,'row':x['row'],'raw':q.get('raw_sha256'),'url':q.get('url',q.get('official_url')),'quote':q.get('exact_quote')})
# First PIT direct-reading ledger predates quote-plan convention: source in existing verified completed guide A originals.
A=R.parent/'germany-ledger-writer-2026-10-28'
for slug in ['de-income-tax','de-self-employed-income-tax','de-employee-income-tax','de-partners-and-part-year','de-corporate-tax','leaving-germany-exit-tax']:
 for n,q in enumerate(json.loads((A/'support'/slug/'actual-read-quotes.json').read_text()),1):prior.append({'guide':slug,'row':n,'raw':q['raw_sha256'],'url':q['url'],'quote':q['exact_quote']})
ids={x['source_id']:x for x in json.loads((D/'source-identities.json').read_text())};out=[]
for n,q in enumerate(json.loads((D/'source-quotes.json').read_text()),1):
 s=ids[q['source_id']];assert H(s['path'])==s['sha256'];assert H(s['reader_path'])==q['reader_sha256'];a,b=q['reader_native_LF'];assert q['exact_original_language_quote']in'\n'.join(Path(s['reader_path']).read_text().split('\n')[a-1:b]);z={'row':n,'id':q['id'],'source':q,'identity':s}
 matches=[x for x in prior if x['raw']==q['source_sha256']and x['url']==q['official_url']and norm(q['exact_original_language_quote'])in norm(x['quote'])]
 if matches:z['actual_read_bridge']={'guide':matches[0]['guide'],'quote_row':matches[0]['row'],'conditions':'Same original raw/officialURL and full quote words; only whitespace/formfeed joining. Existing completed source-read receipt required; current native membership separately verified. No whole-source reading inference.'}
 else:z['pending_direct_read']=True
 out.append(z)
(R/'de-rental-income-quote-reuse-plan.json').write_text(json.dumps(out,indent=2)+'\n');print('TOTAL',len(out),'BRIDGE',sum('actual_read_bridge'in x for x in out));print('NEW',[(x['row'],x['id'])for x in out if 'pending_direct_read'in x])
