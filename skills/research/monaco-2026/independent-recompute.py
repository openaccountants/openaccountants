from decimal import Decimal as D, ROUND_HALF_UP, ROUND_CEILING
import json,re,subprocess
from pathlib import Path
root=Path('/private/tmp/oa-monaco-finish-2026-10-25')
Q=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
checks={}
checks['mc-income-tax']=[{'receipts':D(60000)+D(2000),'monaco_personal_tax':D(0)},{'days':D(170)+D(160)+D(35),'margin':D(170)-max(D(160),D(35)),'shortfall':D(183)-D(170)}]
checks['mc-company-formation']=[{'initial_minimum':D(15000),'remaining':D(30000)-D(15000)},{'quarter':D(300000)/4,'initial_minimum':max(D(300000)/4,D(150000)),'remaining':D(300000)-D(150000)}]
checks['mc-corporate-income-tax']=[{'tax':D(100000)/4,'advance':D(80000)/4/5,'balance':D(100000)/4-D(80000)/4/5*4},{'used':min(D(2000000),D(1000000)+(D(2000000)-D(1000000))/2),'tax':(D(2000000)-D(1500000))/4,'remaining_loss':D(2000000)-D(1500000)}]
checks['mc-cross-border']=[{'gross':D(9000)+D(1000),'credit':min(D(1000),D(10000)/4),'monaco_after':D(10000)/4-D(1000)},{'credit':min(D(3000),D(10000)/4),'monaco_after':D(10000)/4-D(2500),'uncredited':D(3000)-D(2500)}]
checks['mc-transfer-pricing']=[{'adjustment':D(100)*(D(1000)-D(800)),'extra_isb':D(20000)/4},{'addback':D(10000)-D(6000),'extra_isb':D(4000)/4}]
checks['monaco-vat']=[{'net':D(12000)/D('1.2'),'output':D(12000)-D(12000)/D('1.2'),'payable':D(2000)-D(600)},{'output':D(2000)/5,'input_credit':D(400)/2,'payable':D(400)-D(200)}]
def payroll(pay,ccss_cap,car_cap,car_rate,cmrc_cap):
 ccss=Q(min(pay,ccss_cap)*D('.1345'));car_er=Q(min(pay,car_cap)*car_rate);car_ee=Q(min(pay,car_cap)*D('.0685'))
 ue=Q(min(pay,D(16020))*D('.04'));uw=Q(min(pay,D(16020))*D('.024'));a=min(pay,cmrc_cap);b=max(D(0),min(pay,8*cmrc_cap)-cmrc_cap)
 cmrc=a*D('.1002')+b*D('.2429');er=ccss+car_er+ue+Q(cmrc*D('.6'));ee=car_ee+uw+Q(cmrc*D('.4'))
 return {'ta':a,'tb':b,'employer':er,'employee':ee,'cash_net':pay-ee,'cost_before_insurance':pay+er}
checks['mc-payroll-social']=[payroll(D(3000),D(10000),D(6276),D('.0839'),D(4067)),payroll(D(12000),D(9800),D(6112),D('.0833'),D(3971))]
for slug,results in checks.items():
 text=subprocess.check_output(['git','show','970e4d40:skills/international/monaco/'+slug+'.md'],cwd=root,text=True)
 blocks=re.findall(r'```oa-check\n(.*?)```',text,re.S);assert len(blocks)==2
 for i,(block,calc) in enumerate(zip(blocks,results),1):
  exp=block.split('expected:\n')[1]
  expected={k:D(v) for k,v in re.findall(r'^  (\w+): (\d+(?:\.\d+)?)$',exp,re.M)}
  for k,v in expected.items():assert abs(v-calc[k])<D('.001'),(slug,i,k,v,calc[k])
print('All 14 candidate oa-check expected maps independently matched:')
print(json.dumps(checks,default=str,indent=2))
print('Independent substantive boundary calculations:')
for t in [D(125000),D('125000.01'),D(1000000),D(1125000),D(3500000)]:
 n=((max(t-D(125000),D(0)))/D(125000)).to_integral_value(rounding=ROUND_CEILING)
 print('Executive service T',t,'additional bands',n,'ceiling',D(67680)*(1+D('.75')*min(n,7)+D('.8')*max(n-7,0)))
for ecb in ['2.40','2.65','2.90']:print('ECB',ecb,'BdF',D(ecb)+2,'Monaco ceiling',D(ecb)+4)
print('Finance net5m EBITDA10m cap',max(D(3000000),D(10000000)*D('.3')),'disallowed',D(2000000))
print('Thin capital net1.2m EBITDA8m cap',max(D(1000000),D(8000000)*D('.1')),'disallowed',D(200000),'eligible carry',D(200000)/3)
for h in ['.20','.35','.50']:
 rate=D('.2') if D(h)<D('.35') else D('.1') if D(h)<D('.5') else D('.05');q=min(D(100000)*rate,D(12000));print('Participation holding',h,'capped quota',q,'deduction',D(100000)-q)
up=lambda x:x.quantize(D('.01'),rounding=ROUND_CEILING)
a=up(D('.816'));t=up(D(2)/3);coef=up(a*t);print('VAT coefficients',a,t,coef,'VAT1000 recovery',D(1000)*coef)
print('Annual fixed-asset adjustment',D(20000)*(D('.6')-D('.8'))/5,'building',D(20000)*(D('.6')-D('.8'))/20)
print('Fuel VAT100 passenger petrol/diesel recovery',D(100)*D('.8'),'gas/LPG',D(100)*D('.5'))
print('CCSS/CAR 2025 monthly/yearly',D(9800)*12,D(6112)*12,'2026 October',D(10000)*12,D(6276)*12)
print('CMRC upper B',D(3971)*8,D(4067)*8)
print('Jan/Jun adult169h minima',D('12.02')*169,D('12.31')*169)
