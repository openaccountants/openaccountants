from decimal import Decimal as D, ROUND_HALF_UP
from fractions import Fraction as F
from math import ceil
from datetime import date
from pathlib import Path
import json
out=Path(__file__).parent;checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def pension(x):
 # Independently accumulate annual marginal bands by their widths.
 r=F(0);remain=F(x)
 for width,rate in [(12000,F(8,100)),(6700,F(30,100)),(10**12,F(40,100))]:
  unit=min(max(remain,0),width);r+=unit*rate;remain-=unit
 return r
for x,y in [(12000,960),(18700,2970),(20000,3490)]:c('IRNR pension '+str(x),pension(x),F(y))
c('IRNR general vs investment rate separate',D('10000')*D('.24')-D('10000')*D('.19'),D('500'))
c('IRNR EU verified rent cost base',D('12000')-D('3500'),D('8500'))
c('IRNR EU rent tax',D('8500')*D('.19'),D('1615'))
c('IRNR2026 year365days',(date(2027,1,1)-date(2026,1,1)).days,365)
b=D('100000')*D('.011')*D(185)/365
c('IRNR ownuse partyear roundedtax',(b*D('.19')).quantize(D('.01'),rounding=ROUND_HALF_UP),D('105.93'))
c('IRNR distinct rent plus ownuse total',D('1615')+(b*D('.19')).quantize(D('.01'),rounding=ROUND_HALF_UP),D('1720.93'))
c('IRNR halfowner ownuse halfbase',D('100000')*D('.011')*D('.5'),D('550'))
c('IRNR unnotified cadastral50percent greater-value',max(180000,200000)*F(1,2)*F(11,1000),1100)
c('IRNR timeshare exactly2weeks excluded',14<=14,True)
c('IRNR timeshare15days notexcluded',15<=14,False)
c('IRNR3percent retention on consideration',D('250000')*D('.03'),D('7500'))
c('IRNR3percent notgain',D('250000')*D('.03')!=D('50000')*D('.03'),True)
c('IRNR ordinary withholding gross can exceed netfinal',D('12000')*D('.19')-D('8500')*D('.19'),D('665'))
c('IRNR exit exact4million fails aggregate',4000000>4000000,False)
c('IRNR exit alternative exact25percent fails',F(25,100)>F(1,4),False)
c('IRNR exit alternative exact1million fails',1000000>1000000,False)
c('IRNR exit positivegain notmarketvalue',5000000-3000000,2000000)
c('IRNR exit savings incremental',71880+(2000000-300000)*F(30,100),581880)
c('IRNR unlisted capitalisation20percent',F(60000,1)/F(20,100),300000)
c('IRNR PE19percent remittance conditional branch',D('100000')*D('.19'),D('19000'))
# IGIC source year/rate boundaries and independent recovery ledgers.
c('IGIC ordinary30000threshold equality',30000<=30000,True)
c('IGIC ordinary30000.01 fails2026ordinary',D('30000.01')<=30000,False)
c('IGIC exceptional50000 equality eligibilitylimb',50000<=50000,True)
c('IGIC firsthalf50000 notautomatic ordinarythreshold',50000<=30000,False)
c('IGIC halfyear annualise',D('20000')*2,D('40000'))
c('IGIC electronics exactly10000 noamounttrigger',10000>10000,False)
c('IGIC electronics10000.01 amounttrigger',D('10000.01')>10000,True)
c('IGIC baddebt nonbusiness exactly50 fails',50>50,False)
c('IGIC baddebt50.01 succeeds amountlimb',D('50.01')>50,True)
c('IGIC specialprorrata exact110percent triggers',F(110)>=F(11,10)*100,True)
c('IGIC general roundedup ratio',ceil(F(60001,100000)*100),61)
c('IGIC annual investment10point exactly nogate',abs(80-70)>10,False)
c('IGIC annual investment11point gate',abs(80-69)>10,True)
c('IGIC ordinaryexample output',20000*F(7,100)+2000*F(7,100),1540)
c('IGIC retailer implicitburden',1000*F(7,10)*F(7,100),49)
c('IGIC vehicle supported50percent input',70*F(1,2),35)
c('IGIC ordinaryexample input',350+280+140+35+49,854)
c('IGIC ordinaryexample net',1540-854-200,486)
G=F(1000+6000+3000)*F(60,100);S=1000+3000*F(60,100)
c('IGIC generalrecovery',G,6000);c('IGIC specialrecovery',S,2800)
c('IGIC compulsoryspecial',G>=F(11,10)*S and G>0,True)
c('IGIC annual provisional correction',S-3500,-700)
c('IGIC investment cashrepayment',F(7000)*(F(80,100)-F(60,100))/5,280)
c('IGIC combined annual entitlement',S-280,2520)
c('IGIC combined correction',S-280-3500,-980)
c('IGIC sectors exclusive plus shared',1000+1000*F(60,100),1600)
c('IGIC sale remaining2026through2028',2028-2026+1,3)
c('IGIC taxable-sale uncappedextra',(14000-7000)*F(3,5),4200)
c('IGIC taxable-sale actualoutputcap',min(4200,5000*F(7,100)),350)
c('IGIC exempt nonentitling sale cashrepayment',7000*F(3,5),4200)
c('IGIC startup global300k500k',F(300000,500000),F(3,5))
c('IGIC startup adjustment cashrepayment',10000*(F(80,100)-F(3,5)),2000)
def startup_years(start):
 first=start.year+(start>=date(start.year,7,1))
 return list(range(first,first+4))
c('IGIC1July2026 counts next4years',startup_years(date(2026,7,1)),[2027,2028,2029,2030])
c('IGIC30June2026 counts current4years',startup_years(date(2026,6,30)),[2026,2027,2028,2029])
(out/'tranche2-controls.json').write_text(json.dumps({'count':len(checks),'scope':'Own arithmetic/threshold separators; actual claimant/classification/election conditions remain required. Last two calendar lists reflect sourcebefore1July criterion, not runtime controls.','checks':checks},indent=2)+'\n')
print(len(checks),'PASS')
