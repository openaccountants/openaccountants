from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];g=R/'skills/international/spain/es-estimated-tax.md';b=g.read_text();checks=[]
def c(n,a,e):
 assert a==e,(n,a,e);checks.append(dict(name=n,actual=str(a),expected=str(e),pass_check=True))
c('frozen Guide',hashlib.sha256(g.read_bytes()).hexdigest(),'6272215a56c4f293e025101af322b2215e578f0284a63ccdbd959ba5f8f290eb')
for z in json.loads((P/'actual-read-quotes.json').read_text()):c(z['source']+' exact quote '+str(z['LF_start']),z['quote'] in '\n'.join(((P/z['reader']).read_text().split('\n') if z.get('line_convention') else (P/z['reader']).read_text().splitlines())[z['LF_start']-1:z['LF_end']]),True)
for z in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:c(z['key']+' '+k,hashlib.sha256((P/z[k]).read_bytes()).hexdigest(),z[k+'_sha256'])
c('exact current wording',all(z['wording'] in b for z in json.loads((P/'claim-rows.json').read_text())),True)
c('2 original examples',b.count('```oa-check'),2);c('Q2 net',30000-10000,20000);c('Q2 advance',20000*F(20,100)-1500-500,2000);c('Q1 reduction carry',max(0,-3000)*F(20,100)-100,-100);c('Q2 with reduction and unused credit',1500*F(20,100)-100-100,100);c('Ceuta rate',F(20,100)*(1-F(60,100)),F(8,100));c('ordinary module rate3',F(3,100),F('0.03'))
r=subprocess.run(['/usr/bin/python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,capture_output=True,text=True,env={**__import__('os').environ,'PYTHONPATH':'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'});(P/'oa-output.txt').write_text(r.stdout+r.stderr);c('actual 2 oa',r.returncode,0)
(P/'ledger-check-results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(len(checks),'writer ledger assertions passed')
