from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];g=R/'skills/international/spain/es-modelo-111.md';b=g.read_text();checks=[]
def c(n,a,e):
 assert a==e,(n,a,e);checks.append(dict(name=n,actual=str(a),expected=str(e),pass_check=True))
c('frozen Guide',hashlib.sha256(g.read_bytes()).hexdigest(),'cacfed2ef3bd58be9ef879b9a644b51426e5218656c53f074cee93ae5fe7e982')
for z in json.loads((P/'actual-read-quotes.json').read_text()):c(z['source']+' exact quote '+str(z['LF_start']),z['quote'] in '\n'.join((P/z['reader']).read_text().splitlines()[z['LF_start']-1:z['LF_end']]),True)
for z in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:c(z['key']+' '+k,hashlib.sha256((P/z[k]).read_bytes()).hexdigest(),z[k+'_sha256'])
c('exact current wording',all(z['wording'] in b for z in json.loads((P/'claim-rows.json').read_text())),True)
c('2 original examples',b.count('```oa-check'),2);c('VAT',1000*F(21,100),210);c('withheld',1000*F(15,100),150);c('cash',1000+210-150,1060);c('payer outflow',1060+150,1210)
c('salary cash gross',2500*3,7500);c('salary withholding',F('410.50')*3,F('1231.50'));c('professional fees',1000+500+2000,3500);c('professional withheld',(1000+500)*F(7,100)+2000*F(15,100),405);c('total remittance',F('1231.50')+405,F('1636.50'));c('complementary',F('1636.50')-1500,F('136.50'))
r=subprocess.run(['/usr/bin/python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,capture_output=True,text=True,env={**__import__('os').environ,'PYTHONPATH':'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'});(P/'oa-output.txt').write_text(r.stdout+r.stderr);c('actual 2 oa',r.returncode,0)
(P/'ledger-check-results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(len(checks),'writer ledger assertions passed')
