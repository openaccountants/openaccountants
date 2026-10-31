from pathlib import Path
import json,re,hashlib
from decimal import Decimal as D
from fractions import Fraction as F
p=Path('ledgers/spain-2026-evidence/es-foral-income-tax');rows=json.loads((p/'rows.json').read_text());scopes=[];bad=[];cache={}
for z in rows:
 rp=Path(z['reader'])
 if str(rp)not in cache:
  t=rp.read_text();a=[];coords=[]
  for k,m in enumerate(re.finditer(r'\S+',t)):
   if a:a.append(' ');coords.append(m.start())
   a.extend(m.group());coords.extend(range(m.start(),m.end()))
  cache[str(rp)]=(t,''.join(a),coords)
 t,n,coords=cache[str(rp)];q=re.sub(r'^\[…\] | \[…\]$','',z['quote']);i=n.find(q)
 if i<0:bad.append(z['id']);continue
 scopes.append(dict(row=z['id'],url=z['url'],provision=z['provision'],raw_sha256=z['raw_sha256'],reader=str(rp),reader_sha256=hashlib.sha256(rp.read_bytes()).hexdigest(),LF_start=t.count('\n',0,coords[i])+1,LF_end=t.count('\n',0,coords[i+len(q)-1])+1,read_on='2026-10-28',scope='Selected exact quotation actually read; intervening pages/full document are not claimed. Saved-source reuse, not fresh acquisition.'))
(p/'actual-source-read-scopes.json').write_text(json.dumps(dict(rows=scopes,unmatched=bad,method='Native reader LF; whitespace-only joined quotation; row deduplication is permitted for identical selected reads; raw immutable.'),ensure_ascii=False,indent=2)+'\n')

print('scopes',len(scopes),'unmatched',bad)
