from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];g=R/'skills/international/spain/es-rental-income.md';b=g.read_text();checks=[]
def c(n,a,e):
 assert a==e,(n,a,e);checks.append(dict(name=n,actual=str(a),expected=str(e),pass_check=True))
c('frozen Guide',hashlib.sha256(g.read_bytes()).hexdigest(),'c54193fb3920e8c416c777bd86caa82f319f7ff4eef2ae7d76ce1eeda059e57a')
for z in json.loads((P/'actual-read-quotes.json').read_text()):c(z['source']+' exact quote '+str(z['LF_start']),z['quote'] in '\n'.join((P/z['reader']).read_text().splitlines()[z['LF_start']-1:z['LF_end']]),True)
for z in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:c(z['key']+' '+k,hashlib.sha256((P/z[k]).read_bytes()).hexdigest(),z[k+'_sha256'])
c('exact current wording',all(z['wording'] in b for z in json.loads((P/'claim-rows.json').read_text())),True)
c('2 original examples',b.count('```oa-check'),2);c('building basis',max(150000*F(80,100),100000*F(80,100)),120000);c('depreciation',120000*F(3,100),3600);c('example1 net',12000-2000-1000-3600,5400);c('example1 taxable',5400*(1-F(50,100)),2700);c('example2 cappedcost',min(4000,6000),4000);c('example2 carry',6000-4000,2000);c('example2 signednet',4000-4000-800-1200,-2000);c('B positive',1200-200,1000);c('B taxable',1000*(1-F(100,100)),0);c('relative credit rate',F(19,100)*(1-F(60,100)),F('0.076'));c('successive60then30',10000*(1-F(60,100))*(1-F(30,100)),2800);c('irregular capped',400000-F(30,100)*min(400000,300000),310000)
r=subprocess.run(['/usr/bin/python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,capture_output=True,text=True,env={**__import__('os').environ,'PYTHONPATH':'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'});(P/'oa-output.txt').write_text(r.stdout+r.stderr);c('actual 2 oa',r.returncode,0)
(P/'ledger-check-results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(len(checks),'writer ledger assertions passed')
