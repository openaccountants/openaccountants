from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];g=R/'skills/international/spain/spain-crypto-tax.md';b=g.read_text();checks=[]
def c(n,a,e):
 assert a==e,(n,a,e);checks.append(dict(name=n,actual=str(a),expected=str(e),pass_check=True))
c('frozen Guide',hashlib.sha256(g.read_bytes()).hexdigest(),'1cb9ca63c95f0f6a88daa41443c1237e133d058bc12e6c82bca48911a4a6748c')
for z in json.loads((P/'actual-read-quotes.json').read_text()):c(z['source']+' exact quote '+str(z['LF_start']),z['quote'] in '\n'.join((P/z['reader']).read_text().splitlines()[z['LF_start']-1:z['LF_end']]),True)
for z in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:c(z['key']+' '+k,hashlib.sha256((P/z[k]).read_bytes()).hexdigest(),z[k+'_sha256'])
c('exact current wording',all(z['wording'] in b for z in json.loads((P/'claim-rows.json').read_text())),True)
c('2 original examples',b.count('```oa-check'),2)
c('sale basis',25000+150,25150);c('net proceeds',55000-200,54800);c('sale gain',54800-25150,29650)
def tax(n):return F(19,100)*min(n,6000)+F(21,100)*max(0,n-6000)
c('sale tax',tax(29650),F('6106.50'));c('FIFO cost',12000+2*F(10000,5),16000);c('swap value',max(45600,44000),45600);c('swap gain',45600-16000,29600);c('remaining cost',3*F(10000,5),6000);c('disposal basket',29600-33000,-3400);c('offset',min(3400,10000*F(25,100)),2500);c('savings base',10000-2500,7500);c('carried',3400-2500,900);c('tax basket',tax(7500),1455)
c('mixed fee evidenced60%',100*F(60,100),60);c('mixed fee evidenced40%',100*F(40,100),40);c('fee ledger nonduplication',3940+40+960,4940);c('received swap basis with own acquisition fee',5000+40,5040);c('conditional same asset released plus new gain',500-4000,-3500)
c('exact50k initial exclusion',50000>50000,False);c('50001 triggers initial',50001>50000,True);c('selfcustody excluded',50001,150001-100000);c('exact20k later increase',20000>20000,False)
c('all old units semantically routed',any('TOPIC-MAPPING GAP' in z['destination'] for z in json.loads((P/'old-topics.json').read_text())),False)

r=subprocess.run(['/usr/bin/python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,capture_output=True,text=True,env={**__import__('os').environ,'PYTHONPATH':'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'});(P/'oa-output.txt').write_text(r.stdout+r.stderr);c('actual 2 oa',r.returncode,0)
(P/'ledger-check-results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(len(checks),'writer ledger assertions passed')
