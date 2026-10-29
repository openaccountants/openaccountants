from pathlib import Path
import json,hashlib,sys,re
O=Path(__file__).parent;B=O.parent/'germany-ledger-writer-B-2026-10-29';slug=sys.argv[1];mode=sys.argv[2];lo,hi=map(int,sys.argv[3:5]);rows=json.loads((B/'support'/slug/'rows.json').read_text());H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
if mode=='claims':
 for n,r in enumerate(rows[lo-1:hi],lo):print(f'ROW{n} nativeLF{r["LF_start"]}–{r["LF_end"]} SECTION '+r['section']+' ANCHORS '+','.join(r['source_quote_ids'])+'\n'+r['wording']+'\n')
elif mode in ['quotes','newquotes']:
 bank=json.loads((B/'used-source-read-scopes.json').read_text());ids=list(dict.fromkeys(k for r in rows for k in r['source_quote_ids']));
 if mode=='newquotes':ids=[r['id'] for r in json.loads((O/(slug+'-quote-reuse-plan.json')).read_text())if 'pending_direct_read'in r]
 for n,k in enumerate(ids[lo-1:hi],lo):
  q=bank[k];assert H(q['raw_path'])==q['raw_sha256'];assert H(q['reader_path'])==q['reader_sha256'];a,b=q['native_LF'];span='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert q['exact_quote']in span,k;print(f'QUOTE{n} '+k+' '+q['act_article']+' '+q['official_url']+'\n'+q['reader_path']+f' nativeLF{a}–{b} SHA'+q['reader_sha256']+'\n'+q['exact_quote']+'\n')
else:raise ValueError(mode)
