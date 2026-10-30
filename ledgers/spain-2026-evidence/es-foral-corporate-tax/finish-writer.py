from pathlib import Path
import json,re,hashlib
from decimal import Decimal as D
from fractions import Fraction as F
p=Path('ledgers/spain-2026-evidence/es-foral-corporate-tax');rows=json.loads((p/'rows.json').read_text());scopes=[];bad=[];cache={}
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
checks={}
def check(k,a,b):checks[k]={'actual':str(a),'expected':str(b),'pass':a==b};assert a==b,k
check('monetary-index-cost',D(100000)*D('1.071'),D(107100));check('monetary-index-depreciation',D(3000)*D('1.040')+D(3000)*D('1.020'),D(6180));check('monetary-deduction',D(107100)-D(6180)-D(94000),D(6920));check('monetary-disposal',D(56000)-D(6920),D(49080));check('monetary-cap',min(D(6920),D(5000)),D(5000));check('bad-debt-closing-ceiling',(D(500000)-D(100000)-D(50000))*D('.01'),D(3500));check('bad-debt-addition',D(3500)-D(2000),D(1500));check('domestic-dividend-base',D(10000)*D('.5'),D(5000));check('domestic-dividend-quota',D(5000)*D('.24'),D(1200));check('micro-netbase',D(100000)*D('.85'),D(85000));check('Bizkaia-environmental-credit',(D(100000)-D(20000)*D('.76'))*D('.35'),D(29680));check('AG-environmental-credit',(D(100000)-D(20000))*D('.35'),D(28000));check('BG-surcharge',sum(D(x)*D('.24')*D(a)for x,a in [(15000,'.01'),(25000,'.02'),(25000,'.03'),(50000,'.04')]),D(816));check('BG-increased-quota',D(190000)*D('.24')+D(816),D(46416));t=F(24,100);M=F(76000);E=F(190000);remaining=E-F(135000);S=F(0);admitted=[]
for w,a in [(M*F(15,100),F(1,100)),(M*F(25,100),F(2,100)),(M*F(25,100),F(3,100)),(None,F(4,100))]:
 v=min(remaining,w/(1-t-a*t))if w is not None else remaining;remaining-=v;S+=v*t*a;admitted.append(v)
check('A-exact-feedback',S,F(29432841,111746));check('A-excess-reconciliation',sum(admitted),F(55000));check('A-displayed-quota',(D(45600)+D(S.numerator)/D(S.denominator)).quantize(D('.01')),D('45863.39'));check('2026-AG-hire',D(7000)*D('1.1'),D(7700));check('2026-AG-special-hire',D(7700)*2,D(15400));check('pension-below-threshold-preferred',D(1000)*D('.1'),D(100));check('pension-below-threshold-other',D(1000)*D('.05'),D(50));check('minimum-credit-available',D(24000)-max(D(17000),D(24000)-D(8000)),D(7000));check('232-boundary-equal',D(36000)>D(36000),False);check('232-next-cent',D('36000.01')>D(36000),True)
(p/'writer-separating-controls.json').write_text(json.dumps(checks,indent=2)+'\n');print('scopes',len(scopes),'unmatched',bad,'controls',len(checks))
