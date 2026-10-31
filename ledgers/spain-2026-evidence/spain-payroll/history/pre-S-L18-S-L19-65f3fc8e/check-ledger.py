from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];g=R/'skills/international/spain/spain-payroll.md';b=g.read_text();checks=[]
def c(n,a,e):
 assert a==e,(n,a,e);checks.append(dict(name=n,actual=str(a),expected=str(e),pass_check=True))
c('frozen Guide',hashlib.sha256(g.read_bytes()).hexdigest(),'89de80b5558648018020a803fd139685ac92d4908d6f72b1007e84626598d77a')
for z in json.loads((P/'actual-read-quotes.json').read_text()):c(z['source']+' exact quote '+str(z['LF_start']),z['quote'] in '\n'.join(((P/z['reader']).read_text().split('\n') if z.get('line_convention') else (P/z['reader']).read_text().splitlines())[z['LF_start']-1:z['LF_end']]),True)
for z in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:c(z['key']+' '+k,hashlib.sha256((P/z[k]).read_bytes()).hexdigest(),z[k+'_sha256'])
c('exact current wording',all(z['wording'] in b for z in json.loads((P/'claim-rows.json').read_text())),True)
for k,call in [('algoRED20','RED20 = REDONDEAR1 (RED20)'),('algoDesc','MINDESG = REDONDEAR1 (MINDESG)'),('algoDesc3','MINDES3= REDONDEAR1 (MINDES3)'),('algoAS65','65AS = REDONDEAR1 (65AS)'),('algoAS75','75AS = REDONDEAR1 (75AS)'),('algoDISDES','DISDES = REDONDEAR1 (DISDES)'),('algoDISAS','DISAS = REDONDEAR1 (DISAS)'),('algoASISDES','ASISDES = REDONDEAR1 (ASISDES)'),('algoASISAS','ASISAS = REDONDEAR1 (ASISAS)'),('algoNormal','MINOPAGO = TRUNCAR (MINOPAGO)'),('algoNormal','TIPO = TRUNCAR (TIPO)'),('algoAnnual','IMPORTE = REDONDEAR1 (IMPORTE)'),('algoReg','TIPOREG = TRUNCAR (TIPOREG)'),('algoReg','MINOPAGO = TRUNCAR (MINOPAGO)'),('algoRegAnnual','IMPORTE = REDONDEAR1 (IMPORTE)'),('algoGuard','TIPOREG = TRUNCAR (TIPOREG)')]:
 c('native named call '+k+call,any(call in z['quote'] for z in json.loads((P/'quotes.json').read_text())[k]),True)
c('2 original examples',b.count('```oa-check'),2)
def T(x):
 out=F(0)
 for lo,hi,r in [(0,12450,'.19'),(12450,20200,'.24'),(20200,35200,'.30'),(35200,60000,'.37'),(60000,300000,'.45'),(300000,10**12,'.47')]:out+=max(0,min(x,hi)-lo)*F(r)
 return out
c('employee derived percentage',F('.047')+F('.0155')+F('.001')+F('.0015'),F('.065'));c('annual employee',30000*F('.065'),1950);c('base',30000-1950-2000,26050);c('T base',T(26050),F('5980.50'));c('T minimum',T(5550),F('1054.50'));c('quota',T(26050)-T(5550),4926);c('annual rate',F(4926,30000)*100,F('16.42'));c('monthly tax',2500*F('.1642'),F('410.50'));c('net',2500-F('162.50')-F('410.50'),1927);c('employer components',2500*sum(map(F,['.236','.055','.002','.006','.0075','.015'])),F('803.75'));c('employer cost',2500+F('803.75'),F('3303.75'))
c('rise base',36000-2340-2000,31660);c('rise quota',T(31660)-T(5550),6609);c('remaining quota',6609-2463,4146);c('truncated rate',int(F(4146,21000)*10000)*F(1,100),F('19.74'));c('monthly revised tax',3500*F('.1974'),F('690.90'));c('monthly revised net',3500-F('227.50')-F('690.90'),F('2581.60'));c('projected withholding',2463+6*F('690.90'),F('6608.40'))
reduction_R=F('21008.84')-F('2194.78');red=F('2364.34')-F('1.14')*(reduction_R-F('17673.52'));c('RED20 unrounded',red,F('1064.1244'));rounded=round(red,2);c('RED20 rounded',rounded,F('1064.12'));base=reduction_R-2000-rounded;c('separator base',base,F('15749.94'));quota=T(base)-T(5550);c('separator quota',quota,F('2102.9856'));c('separator cap',F('.43')*(F('21008.84')-15876),F('2207.1212'));c('proper rate10.01',int(quota/F('21008.84')*10000)*F(1,100),F('10.01'));wrong=T(reduction_R-2000-red)-T(5550);c('unrounded wrong10',int(wrong/F('21008.84')*10000)*F(1,100),10)
from decimal import Decimal,ROUND_HALF_UP
c('specified half-cent upwards',Decimal('0.005').quantize(Decimal('.01'),rounding=ROUND_HALF_UP),Decimal('.01'));c('rate truncation example',int(F('17.85964523')*100)*F(1,100),F('17.85'))
c('FOGASA published daily reconstruction',round(2*(F('40.70')+2*F(1221,365)),2),F('94.78'));c('FOGASA wagecap',F('94.78')*120,F('11373.60'));c('FOGASA indemnitycap',F('94.78')*365,F('34594.70'));c('SMI 12pay',F(17094,12),F('1424.50'));c('all old units routed',any('TOPIC-MAPPING GAP' in z['destination'] for z in json.loads((P/'old-topics.json').read_text())),False)

r=subprocess.run(['/usr/bin/python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,capture_output=True,text=True,env={**__import__('os').environ,'PYTHONPATH':'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'});(P/'oa-output.txt').write_text(r.stdout+r.stderr);c('actual 2 oa',r.returncode,0)
(P/'ledger-check-results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(len(checks),'writer ledger assertions passed')
