from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];g=R/'skills/international/spain/es-capital-gains.md';b=g.read_text();checks=[]
def c(n,a,e):
 assert a==e,(n,a,e);checks.append(dict(name=n,actual=str(a),expected=str(e),pass_check=True))
c('frozen Guide',hashlib.sha256(g.read_bytes()).hexdigest(),'e7e697ce9c7d64dc0ffb0a717894a49c4a6e25cd94890c7249b272d4e2e4fb38')
for z in json.loads((P/'actual-read-quotes.json').read_text()):c(z['source']+' exact quote '+str(z['LF_start']),z['quote'] in '\n'.join((P/z['reader']).read_text().splitlines()[z['LF_start']-1:z['LF_end']]),True)
for z in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:c(z['key']+' '+k,hashlib.sha256((P/z[k]).read_bytes()).hexdigest(),z[k+'_sha256'])
c('exact current wording',all(z['wording'] in b for z in json.loads((P/'claim-rows.json').read_text())),True)
c('2 original examples',b.count('```oa-check'),2);c('transfer',20000-100,19900);c('basis',10000+50,10050);c('gain',19900-10050,9850);c('tax',6000*F(19,100)+3850*F(21,100),F('1948.50'));c('admitted loss',10000-2000,8000);c('cross offset',min(8000,10000*F(25,100)),2500);c('carry',8000-2500,5500);c('savingsbase',10000-2500,7500);c('secondtax',6000*F(19,100)+1500*F(21,100),1455);c('unlisted floor',3000/F(20,100),15000);c('unlisted gain',15000-5000,10000);c('rights basis',10000-2000,8000);c('rights gain',15000-8000,7000);c('annuity clamp',10000*min(30000,60000,240000)/30000,10000);c('annuity partial',10000*15000/30000,5000)
for rate,half in [(19,F('9.5')),(21,F('10.5')),(23,F('11.5')),(27,F('13.5')),(30,F(15))]:c('combinedrate'+str(rate),half*2,rate)
for full,half in [(0,0),(1140,570),(10380,5190),(44880,22440),(71880,35940)]:c('combinedopeningquota'+str(full),half*2,full)
r=subprocess.run(['/usr/bin/python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,capture_output=True,text=True,env={**__import__('os').environ,'PYTHONPATH':'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'});(P/'oa-output.txt').write_text(r.stdout+r.stderr);c('actual 2 oa',r.returncode,0)
(P/'ledger-check-results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(len(checks),'writer ledger assertions passed')
