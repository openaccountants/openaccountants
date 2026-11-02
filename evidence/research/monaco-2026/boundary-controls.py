#!/usr/bin/env python3
"""Additional Monaco controls; independent fixtures, not part of the 14 Guide examples.
Sources/method limits: completion-research.md and the cited Guide provisions.
Run with Python 3; uses Decimal and explicit expected values.
"""
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_CEILING
import json
from pathlib import Path
results=[]
def check(name,actual,expected):
    assert actual==expected,(name,str(actual),str(expected))
    results.append({'name':name,'actual':str(actual),'expected':str(expected),'pass':True})
def cents(x):return x.quantize(D('.01'),rounding=ROUND_HALF_UP)
def executive(turnover,band):
    # Sum the individual increments, independently of the Guide's compact formula.
    remaining=max(D(turnover)-D(band),D(0));amount=D(67680);number=0
    while remaining>0:
        number+=1;amount+=D(67680)*(D('.75') if number<=7 else D('.8'));remaining-=D(band)
    return amount
for t,expected in [('0','67680'),('125000','67680'),('125000.01','118440'),('1000000','423000'),('1000000.01','477144'),('3500000','1505880')]:
    check('service executive turnover '+t,executive(t,125000),D(expected))
check('other business scale top',executive(7000000,250000),D(1505880))
for marginal,ceiling in [('2.40','6.40'),('2.65','6.65'),('2.90','6.90')]:
    check('derived shareholder ceiling from marginal '+marginal,D(marginal)+D(2)+D(2),D(ceiling))
for profit,loss,expected in [('999999','2000000','999999'),('1000000','2000000','1000000'),('1000001','2000000','1000000.5'),('2000000','2000000','1500000')]:
    check('ordinary loss cap profit '+profit,min(D(loss),D(profit),D(1000000)+max(D(profit)-D(1000000),D(0))/2),D(expected))
for holding,quota in [('20','.2'),('34.999','.2'),('35','.1'),('49.999','.1'),('50','.05')]:
    h=D(holding);check('participation quota at '+holding,D('.2') if h<35 else D('.1') if h<50 else D('.05'),D(quota))
check('participation quota actual expense cap',min(D(10000)*D('.2'),D(600)),D(600))
# Full-month cash salary; ordinary coverage; no minima/in-kind/insurance assumptions imported.
for period,pay,cap,car,rate,a,top,expected_er,expected_ee in [
 ('March','12000','9800','6112','.0833','3971','31768','3716.11','1645.93'),
 ('October','3000','10000','6276','.0839','4067','32536','955.56','397.74')]:
    p=D(pay);cmrc=min(p,D(a))*D('.1002')+max(D(0),min(p,D(top))-D(a))*D('.2429')
    er=cents(min(p,D(cap))*D('.1345'))+cents(min(p,D(car))*D(rate))+cents(min(p,D(16020))*D('.04'))+cents(cmrc*D('.6'))
    ee=cents(min(p,D(car))*D('.0685'))+cents(min(p,D(16020))*D('.024'))+cents(cmrc*D('.4'))
    check(period+' total employer',er,D(expected_er));check(period+' total employee',ee,D(expected_ee))
check('CMRC October half-time A cap',D(4067)*D('75.5')/D(151),D('2033.5'))
check('CARTI early class four',D('550.08')*4,D('2200.32'))
check('CARTI late class four',D('564.84')*4,D('2259.36'))
check('January 169 hours minimum',D('12.02')*169,D('2031.38'))
check('June 169 hours minimum',D('12.31')*169,D('2080.39'))
check('June minimum including 5 percent allowance',cents(D('2080.39')*D('1.05')),D('2184.41'))
check('domestic 254 hours eligible under native law',D(254)<=D(254),True)
check('domestic 254.01 hours excluded under ordinary hours limb',D('254.01')<=D(254),False)
check('VAT quarterly equality 4000 excluded',D(4000)<D(4000),False)
check('EU introduction declaration equality 460000',D(460000)>=D(460000),True)
check('additional statistical equality 460000 not exceedance',D(460000)>D(460000),False)
check('CbCR 750 million not excluded',D(750000000)<D(750000000),False)
check('active NFE ordinary test equality 50 percent fails',D('.5')<D('.5') and D('.2')<D('.5'),False)
check('VAT coefficient upward rounding',D('.501').quantize(D('.01'),rounding=ROUND_CEILING),D('.51'))
check('ordinary excluded-car diesel admission',D(100)*D('.8'),D(80))
check('ordinary excluded-car LPG admission',D(100)*D('.5'),D(50))
check('small acquisition exact 10000 remains within threshold',D(10000)<=D(10000),True)
check('small acquisition 10000.01 loses threshold',D('10000.01')<=D(10000),False)
check('2026 acquisition election expiry year',2026+2,2028)
check('new company corporate holding exact50 not above limit',D(50)>D(50),False)
check('new company deemed family participation exact25 included',D(25)>=D(25),True)
if __name__=='__main__':
    target=Path(__file__).with_name('boundary-controls-results.json')
    target.write_text(json.dumps({'controls':results,'passed':len(results),'failed':0},indent=2)+'\n')
    print(f'{len(results)} additional boundary controls passed')
