from pathlib import Path
import json,hashlib,sys
O=Path(__file__).parent;D=O.parent/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29';mode=sys.argv[1]
if mode=='quotes':
 q=list(json.loads((D/'own-actual-read-quotes.json').read_text()).values());lo,hi=map(int,sys.argv[2:4])
 for i,x in enumerate(q[lo-1:hi],lo):
  for t in ['raw','reader']:
   rp=x.get(t+'_path',x.get('path') if t=='raw' else None);rh=x.get(t+'_sha256',x.get('sha256') if t=='raw' else None);assert hashlib.sha256(Path(rp).read_bytes()).hexdigest()==rh
  a,b=x['native_LF'];span='\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:b]);assert x['exact_quote']in span,x['id']
  print('QUOTE',i,x['id'],x['article'],x.get('url',x.get('official_url')),'ACTUAL',x['reader_path'],f'nativeLF{a}–{b}',x['reader_sha256'],'\n'+x['exact_quote']+'\n')
elif mode=='diff':print((D/'support'/(sys.argv[2]+'.diff')).read_text())
