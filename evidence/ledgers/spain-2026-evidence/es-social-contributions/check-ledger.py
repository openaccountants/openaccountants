from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];g=R/'skills/international/spain/es-social-contributions.md';b=g.read_text();checks=[]
def c(n,a,e):
 assert a==e,(n,a,e);checks.append(dict(name=n,actual=str(a),expected=str(e),pass_check=True))
c('frozen Guide',hashlib.sha256(g.read_bytes()).hexdigest(),'b731e75c8c2dce0e947a2ae7d3cc9a688c02e7880ef738585c323047192e9c85')
for z in json.loads((P/'actual-read-quotes.json').read_text()):c(z['source']+' exact quote '+str(z['LF_start']),z['quote'] in ('\n'.join((P/z['reader']).read_text().split('\n')[z['LF_start']-1:z['LF_end']]).replace('\f','\n') if z.get('line_convention') else '\n'.join((P/z['reader']).read_text().splitlines()[z['LF_start']-1:z['LF_end']])),True)
for z in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:c(z['key']+' '+k,hashlib.sha256((P/z[k]).read_bytes()).hexdigest(),z[k+'_sha256'])
c('exact current wording',all(z['wording'] in b for z in json.loads((P/'claim-rows.json').read_text())),True)
c('2 original examples',b.count('```oa-check'),2)
c('RETA numerator',(10000+1200)*F(93,100),10416);c('calendar day monthly',F(10416,180)*30,1736);c('31.50 derived',sum([F('28.30'),F('1.30'),F('0.90'),F('0.10'),F('0.90')]),F('31.50'));c('ordinary full month',1200*F('0.315'),378)
c('published3month',3*F('88.64'),F('265.92'));c('diagnosticMEI',F('950.98')*F('.009'),F('8.55882'));c('diagnostic nearestcent',round(F('950.98')*F('.009'),2),F('8.56'));c('diagnostic3month',(80+F('8.56'))*3,F('265.68'));c('difference',F('265.92')-F('265.68'),F('.24'))
c('SMI full extras',F(17094,12),F('1424.50'));c('group1 parttime',80*F('11.98'),F('958.40'));c('AT parttime minimum',80*F('8.58'),F('686.40'))
c('solidarity slice1',min(6000-F('5101.20'),F('510.12')),F('510.12'));c('solidarity slice2',6000-F('5611.32'),F('388.68'));c('employer solidarity',round(F('510.12')*F('.0096'),2)+round(F('388.68')*F('.0104'),2),F('8.94'));c('employee solidarity',round(F('510.12')*F('.0019'),2)+round(F('388.68')*F('.0021'),2),F('1.79'))
c('house employerCC',round(970*F('.236')*F('.8'),2),F('183.14'));c('house unemp',round(970*F('.055')*F('.2'),2),F('10.67'));c('house employee',round(970*F('.047'),2)+round(970*F('.0155'),2)+round(970*F('.0015'),2),F('62.09'))
c('IPREM sixth uplift',600*F(7,6),700);c('no child floor',700*F('.80'),560);c('no child cap',700*F('1.75'),1225);c('one child floor',700*F('1.07'),749);c('one child cap',700*2,1400);c('two child cap',700*F('2.25'),1575);c('interest annual',10000*F('.0325')*F('1.25'),F('406.25'));c('interest73days',10000*F('.0325')*F('1.25')*F(73,365),F('81.25'));c('settlement refund income',max(1100-800,0),300)
c('all old units routed',any('TOPIC-MAPPING GAP' in z['destination'] for z in json.loads((P/'old-topics.json').read_text())),False)

r=subprocess.run(['/usr/bin/python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,capture_output=True,text=True,env={**__import__('os').environ,'PYTHONPATH':'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'});(P/'oa-output.txt').write_text(r.stdout+r.stderr);c('actual 2 oa',r.returncode,0)
(P/'ledger-check-results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(len(checks),'writer ledger assertions passed')
