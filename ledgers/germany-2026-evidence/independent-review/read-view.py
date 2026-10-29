from pathlib import Path
import json,hashlib,sys
O=Path(__file__).parent;F=json.loads((O/'country-freeze.json').read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();slug=sys.argv[1];kind=sys.argv[2];lo=int(sys.argv[3]);hi=int(sys.argv[4]);z=next(p for p in F['pairs']if p['slug']==slug)
if z['writer']!='A':raise SystemExit('Aviewonly; other writer formats need their exact adapters, not assumptions')
D=Path(z['ledger_path']).parent.parent/'support'/slug
if kind in ['claims','compactclaims']:
 data=json.loads((D/'claim-rows.json').read_text())
 last=None
 for n,r in enumerate(data[lo-1:hi],lo):
  rel=(r['section'],tuple(r['anchors']),r['kind'])
  if kind=='claims' or rel!=last: print('SECTION '+r['section']+' ANCHORS '+','.join(r['anchors'])+' CLASS '+r['kind'])
  print(f'ROW{n} nativeGuideLF{r["lf"]} '+r['wording'])
  last=rel
elif kind in ['quotes','newquotes']:
 bank={}
 for p in (D.parent.parent/'sources').glob('*.identity.json'):
  t=json.loads(p.read_text());bank[t['id']]=t
 data=json.loads((D/'actual-read-quotes.json').read_text())
 if kind=='newquotes':data=[r['source']for r in json.loads((O/(slug+'-quote-reuse-plan.json')).read_text())if 'pending_direct_read'in r]
 for n,q in enumerate(data[lo-1:hi],lo):
  s=bank[q['source']];rp=Path(s['reader_path']);raw=Path(s['raw_path']);assert H(rp)==q['reader_sha256']==s['reader_sha256']and H(raw)==q['raw_sha256']==s['raw_sha256'];a=q.get('LF_start',q.get('paragraph'));b=q.get('LF_end',a);span='\n'.join(rp.read_text().split('\n')[a-1:b]);assert q['exact_quote']in span,q['id'];print(f'QUOTE{n} '+q['id']+' '+q['article']+'\n'+q['url']+f'\nACTUALREADER {rp} literalLF{a}–{b} SHA{q["reader_sha256"]}\n'+q['exact_quote']+'\n')
else:raise SystemExit('Unknown view')
