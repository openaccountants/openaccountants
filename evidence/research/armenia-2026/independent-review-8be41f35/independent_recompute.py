from decimal import Decimal as D
from pathlib import Path
import json
r=[]
def case(name,values,expect):
 got={k:D(str(v)) for k,v in values.items()}; want={k:D(str(v)) for k,v in expect.items()};r.append({'name':name,'actual':{k:str(v) for k,v in got.items()},'expected':{k:str(v) for k,v in want.items()},'pass':got==want})
case('CIT bridge',{'current':D(30000000)+500000+3000000-4000000,'tax':D(24500000)*D('.18'),'balance':D(24500000)*D('.18')-3000000},{'current':29500000,'tax':4410000,'balance':1410000})
case('CIT losses',{'use2021':8000000,'use2023':10000000-8000000,'remain2023':6000000-(10000000-8000000),'taxable':0},{'use2021':8000000,'use2023':2000000,'remain2023':4000000,'taxable':0})
case('XB royalty',{'tax':D(10000000)/10,'net':D(10000000)*D('.9')},{'tax':1000000,'net':9000000})
case('XB foreign credit',{'total':D(50000000)*D('.18'),'cap':D(30000000)*D('.18'),'balance':D(20000000)*D('.18'),'ineligible':7000000-D(30000000)*D('.18')},{'total':9000000,'cap':5400000,'balance':3600000,'ineligible':1600000})
case('PIT salary',{'tax':D(1000000)/5},{'tax':200000})
case('PIT rent',{'basic':D(72000000)/10,'extra':D(72000000-60000000)/10,'total':D(72000000)/10+D(72000000-60000000)/10,'balance':D(72000000-60000000)/10},{'basic':7200000,'extra':1200000,'total':8400000,'balance':1200000})
case('Payroll300k',{'PIT':D(300000)/5,'pension':D(300000)/20,'net':300000-D(300000)/5-D(300000)/20-1000-4800},{'PIT':60000,'pension':15000,'net':219200})
case('Payroll health entry',{'before':250000-D(250000)/5-D(250000)/20-1000,'after':250000-D(250000)/5-D(250000)/20-1000-4800},{'before':186500,'after':181700})
case('Pension two limbs',{'lower':D(300000)/20,'upper':D(600000)/10-25000},{'lower':15000,'upper':35000})
case('Health continuing funding',{'funding':4800+6000},{'funding':10800})
case('VAT output input',{'output':D(5000000)/5,'input':600000+200000,'pay':D(5000000)/5-600000-200000,'zero_credit':800000},{'output':1000000,'input':800000,'pay':200000,'zero_credit':800000})
case('VAT import paid timing',{'base':10000000+1000000,'tax':D(11000000)/5,'Sept':0,'Oct':D(11000000)/5},{'base':11000000,'tax':2200000,'Sept':0,'Oct':2200000})
case('TP CUP',{'charged':10000*10000,'benchmark':10000*12000,'difference':10000*(12000-10000)},{'charged':100000000,'benchmark':120000000,'difference':20000000})
a=list(map(D,['.02','.03','.04','.05','.06','.07','.08','.09']));case('TP quartiles',{'lower':(a[1]+a[2])/2,'upper':(a[5]+a[6])/2,'median':(a[3]+a[4])/2,'difference':D(100000000)*((a[3]+a[4])/2-a[0])},{'lower':'.035','upper':'.075','median':'.055','difference':3500000})
case('Additional cap and regime probes',{'pension_cap':D(75_000)*15/10-25000,'annual_pension_cap':D(75_000)*180/10-300000,'statutory_VAT_inclusive':D(120000)*D('.1667'),'trade_tax':max(D(10000000)*D('.1')-D(9000000)*D('.095'),D(10000000)*D('.01')),'production_tax':max(D(5000000)*D('.07')-D(3000000)*D('.05'),D(5000000)*D('.03')),'management_allowed_ordinary':min(D(5000000),D(100000000)*D('.02')),'management_omission_tax_difference':(D(5000000)-D(100000000)*D('.02'))*D('.18')},{'pension_cap':87500,'annual_pension_cap':1050000,'statutory_VAT_inclusive':20004,'trade_tax':145000,'production_tax':200000,'management_allowed_ordinary':2000000,'management_omission_tax_difference':540000})
Path('independent-arithmetic.json').write_text(json.dumps(r,indent=2));print(len(r),'independent cases;',sum(not v['pass'] for v in r),'failures')
