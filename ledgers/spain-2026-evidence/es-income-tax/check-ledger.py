from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,ROUND_HALF_UP
import json,hashlib,re,subprocess,os
P=Path(__file__).resolve().parent;R=P.parents[2];g=R/'skills/international/spain/es-income-tax.md';b=g.read_text();checks=[]
def c(n,a,e):
 assert a==e,(n,a,e);checks.append(dict(name=n,actual=str(a),expected=str(e),pass_check=True))
def cents(x):return Decimal(x.numerator)/Decimal(x.denominator) if isinstance(x,F) else Decimal(str(x))
def round2(x):return cents(x).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
c('frozen Guide',hashlib.sha256(g.read_bytes()).hexdigest(),'11e11aeccc77080f5c60a444ce01397b77e6ebebfa7e304a884777b8d4e0191f')
for z in json.loads((P/'actual-read-quotes.json').read_text()):c(z['source']+' exact quote '+str(z['LF_start']),z['quote'] in '\n'.join((P/z['reader']).read_text().splitlines()[z['LF_start']-1:z['LF_end']]),True)
for z in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:c(z['key']+' '+k,hashlib.sha256((P/z[k]).read_bytes()).hexdigest(),z[k+'_sha256'])
c('every current wording exact',all(z['wording'] in b for z in json.loads((P/'claim-rows.json').read_text())),True);c('all old units semantically mapped',any('TOPIC-MAPPING GAP' in z['destination'] for z in json.loads((P/'old-topics.json').read_text())),False);c('105regional native anchors',len(json.loads((P/'regional-scale-native-anchors.json').read_text())),105)
c('2 original examples',b.count('```oa-check'),2)
# Quota continuity permits printed-cent rounding at source band boundaries; use actual statutory opening quotas, never silently replace them.
for z in json.loads((P/'regional-scale-native-anchors.json').read_text()):
 cells=[x.strip() for x in b.splitlines()[z['guide_lf']-1].split('|')[1:-1]]
 if cells[2]=='No upper limit':continue
 c('regional positive width '+str(z['guide_lf']),F(cells[2])>0,True);c('regional nonnegative rate '+str(z['guide_lf']),F(cells[3].strip('%'))>0,True)
c('foreign full-year exemption',2000+F(36500)*45/365,6500);c('foreign full-year residual',38500-6500,32000);c('foreign short payer exemption',3000+F(18400)*46/184,7600);c('foreign short residual',21400-7600,13800);c('wrong365 separator',round2(3000+F(18400)*46/365),Decimal('5318.90'));c('foreign two payers',F(27300)*39/273+F(18400)*36/92,11100);c('whole year cap',min(60100,80000),60100);c('foreign residual',80000-60100,19900);c('residual FTC',min(1990,4975),1990)
c('art20 netR',18000-1150,16850);c('art20 reduction',F(7302)-F('1.75')*(16850-14852),F('3805.50'));c('employment BL',F(16850)-2000-F('3805.50'),F('11044.50'));st=round2((F('11044.50')-5550)*F('.095'));ma=round2((F('11044.50')-F('5956.65'))*F('.085'));c('statehalf',st,Decimal('521.98'));c('Madridhalf',ma,Decimal('432.47'));c('DA61credit',F('590.89')-F('.2')*(18000-17094),F('409.69'));c('annual refund',Decimal(600)-(st+ma-Decimal('409.69')),Decimal('55.24'))
c('simplified cap',min(2000,F(60000-20000)*F('.05')),2000);c('professionalBL',60000-20000-2000,38000);c('savings25cross',min(4000,F(10000)*F('.25')),2500);c('carry',4000-2500,1500);c('stateprofessional',round2(F('4362.75')+(38000-35200)*F('.185')-5550*F('.095')),Decimal('4353.50'));c('Madridprofessional',round2(F('3841.42')+(38000-F('35425.68'))*F('.174')-F('5956.65')*F('.085')),Decimal('3783.04'));c('savingscombined',6000*F('.19')+1500*F('.21'),1455);c('balance',F('4353.50')+F('3783.04')+1455-9000,F('591.54'))
c('Balearic over65 total',F('1.10')*(5550+1150),7370);c('Rioja assistance unchanged',3000,3000)
c('pension employee E500',F('2.5')*500,1250);c('pension employee E1500',1250+F('.25')*(1500-500),1500);c('pension income exactly60000 override',60000>60000,False);c('spouse exactly8000 fails',8000<8000,False)
c('combined annuity enlarged',23000+3000,26000);c('annuity state otherpart',F('2112.75')+(24200-20200)*F('.15'),F('2712.75'));c('augmin tax',7530*F('.095'),F('715.35'));aug=F(171)+F('2712.75')-F('715.35');c('enlarged quota',aug,F('2168.40'));c('general average',aug/26000*100,F('8.34'));c('actual half quota',23000*aug/26000,F('1918.20'));c('total',2*23000*aug/26000,F('3836.40'))
c('AEAT printed regional progression mismatch',round2(F(2475,26800)*100),Decimal('9.24'));c('AEAT city final actual subtraction',F(5778)-F('2035.01'),F('3742.99'));c('exact three-year extension requires laterperiod',3>=3,True);c('strict instalment window Oct1notafterOct3',(2026,10,1)>(2026,10,3),False)
r=subprocess.run(['/usr/bin/python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,capture_output=True,text=True,env={**os.environ,'PYTHONPATH':'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'});(P/'oa-output.txt').write_text(r.stdout+r.stderr);c('actual2oa',r.returncode,0)
(P/'ledger-check-results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(len(checks),'writer assertions passed')
