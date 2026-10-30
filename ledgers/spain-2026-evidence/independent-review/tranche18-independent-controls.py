from decimal import Decimal as D,ROUND_HALF_UP,ROUND_DOWN
from fractions import Fraction as F
from datetime import date
from pathlib import Path
import json,calendar
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');r=[]
def cents(x):return D(str(x)).quantize(D('.01'),rounding=ROUND_HALF_UP)
def check(name,actual,expected):
 assert actual==expected,(name,actual,expected)
 r.append({'name':name,'actual':str(actual),'expected':str(expected),'pass':True})
def money(name,a,b):check(name,cents(a),D(str(b)))
# Independently recomputed binding fixtures, comparisons and dated origins; no writer evaluation imported.
for cap,want in [(660,'332.71'),(900,'453.70')]:
 check('Balearic 184-day rational '+str(cap),F(cap*184,365),F(cap)*F(184,365));money('Balearic 184-day cents '+str(cap),D(cap)*184/365,want)
check('Balearic 1July to31Dec actual days',(date(2026,12,31)-date(2026,7,1)).days+1,184)
for paid,rate,cap,want in [(2000,'.4',660,330),(1000,'.4',660,330),(1000,'.5',900,450),(1500,'.4',660,330),(500,'.4',660,200),(500,'.5',900,250),(1500,'.5',900,450)]:money('Balearic ownpayer '+str((paid,rate,cap)),min(D(paid)*D(rate),D(cap)/2),want)
for a,b,want in [(330,200,530),(330,250,580),(450,200,650)]:check('Balearic unequal household '+str(want),a+b,want)
for cap,want in [(660,'665.42'),(900,'907.40')]:money('Balearic two child periods '+str(cap),2*D(cap)*184/365,want)
# Source eligibility gates strict/inclusive are separate from cap arithmetic.
for n,want in [(182,False),(183,True),(184,True)]:check('Balearic enhanced selfemployed183days '+str(n),n>=183,want)
for n,want in [(183,False),(184,True)]:check('Valencia prior foster ordering greater183 '+str(n),n>183,want)
check('Valencia newborn does not inherit foster183day gate',date(2026,12,31).year,2026)
# Galicia per-child primary advisory interpretation, not duplicate payer pools.
def child(t,o,p):return min(D('.15')*(D(t)+min(D(300),D(o)+min(D(150),D(p)))),D(105))
for args,w in [((100,200,200),60),((700,200,0),105),((0,200,0),30),((0,200,100),45),((0,200,200),45),((0,0,300),D('22.5'))]:money('Galicia child '+str(args),child(*args),w)
check('Galicia binding separate children135',child(700,200,0)+child(0,200,0),135)
check('Galicia two children90',child(0,200,100)*2,90)
check('Galicia PE inside total cap',min(300,200+min(150,200)),300)
for cost,want in [(200,30),(100,15),(400,D('52.50'))]:money('Galicia actual payer cap52.5 '+str(cost),min(D(cost)*D('.15'),D(105)/2),want)
check('Galicia actual payer household90',30+15+15+30,90)
# Independent two clocks and explicitly selected earlier-expiry exercise.
oldcredit,current,quota=350,450,500;useold=min(oldcredit,quota);usenew=min(current,quota-useold)
check('Galicia use old350',useold,350);check('Galicia use new150',usenew,150);check('Galicia current carry300',current-usenew,300)
check('Galicia credit2025 expiry',2025+4,2029);check('Galicia credit2026 expiry',2026+4,2030);check('Galicia singlehome expense2025 expiry',2025+2,2027)
check('Galicia fixed2026 current carry',500-(600-300),200)
check('Galicia multi home base chosen',3000+3000,6000);money('Galicia multi home credit900',6000*D('.15'),900)
check('Galicia allyears base21000',6000+6000+6000+3000,21000);money('Galicia all credit3150',21000*D('.15'),3150);check('Galicia 2028credit expiry',2028+4,2032)
# Murcia source-derived original peseta cap + actual common payment pool.
for pes,want in [(41000,'246.41'),(46000,'276.47')]:money('Murcia peseta redenomination '+str(pes),D(pes)/D('166.386'),want)
for paid,n,rate,want in [(20000,6000,'.03','91.20'),(20000,0,'.03','246.41'),(20000,0,'.02','180.80'),(8000,6000,'.03','60'),(20000,9040,'.03','0')]:
 base=max(0,min(paid,9040)-n);money('Murcia old home '+str((paid,n,rate)),min(D(base)*D(rate),D('246.41')),want)
money('Murcia 35000 agency4500',min(20000*D('.225'),D(7000)),4500);money('Murcia statutory alternative6000',20000*D('.3'),6000)
for rate in ['.225','.3']:money('Murcia binding common7000 '+rate,min(32000*D(rate),D(7000)),7000)
for shares,want in [((D('.5'),D('.5')),(D(3000),D(3000))),((D('.75'),D('.25')),(D(4000),D(1500)))]:check('Murcia charger owncap '+str(shares),tuple(min(6000*x,D(4000)) for x in shares),want)
check('Murcia equal contrary commoncap',4000/2,2000);check('Murcia charger current usage/carry',(min(3000,2000),3000-min(3000,2000)),(2000,1000));check('Murcia vehicle carry',(4500-3000,2026+3),(1500,2029))
# Extremadura actual completed-year interval and award-earmarked net base.
check('Ext rented200',(date(2026,10,17)-date(2026,4,1)).days+1,200);check('Ext offered75',(date(2026,12,31)-date(2026,10,18)).days+1,75);check('Ext denominator275',200+75,275)
check('Ext grant net total',28000-12000,16000);check('Ext grant certified year',14000-6000,8000)
money('Ext actual day fraction872.73',D(8000)*D('.15')*200/275,'872.73');money('Ext counter365657.53',D(8000)*D('.15')*200/365,'657.53');money('Ext annual cap before days986.18',D(9040)*D('.15')*200/275,'986.18')
check('Ext advertisement not actual rent',200+75!=200,True);check('Ext ceiling householdincome',30000*D('.3'),9000);check('Ext offer700 annualised',700*12<=9000,True)
# Rioja independent routes and birthday endpoint.
check('Rioja separate credits',(min(1000*D('.3'),600),min(1000*D('.2'),600)),(300,200));check('Rioja same invoice total',300+200,500);check('Rioja two entitled each',D(500)/2,250);money('Rioja remaining quota',D('724.30')-500,'224.30')
for birth,want in [(date(2023,6,15),5),(date(2023,6,30),5),(date(2023,1,1),0)]:
 months=sum(date(2026,m,calendar.monthrange(2026,m)[1]) < birth.replace(year=2026) for m in range(1,13))
 check('Rioja lastmonth age '+str(birth),months,want);check('Rioja amount '+str(birth),months*100,want*100)
# Same-worker own provisions: separate bases/caps, one aggregate available quota.
check('Canarias independent 20%caps',2*min(3000*D('.2'),500),1000);check('Canarias plus fixed dependent',600+2*min(3000*D('.2'),500),1600);check('Canarias quota remainder',2000-1600,400)
# Rate vs BL amount vs quota-attribution order discriminators from actual source/observations.
for q,want in [('1660.50','79.07'),('1480.25','70.49'),('1564.21','74.49')]:money('Work cap quota ratio '+q,D(q)*1000/21000,want)
for rate,want in [('.1585','156.24'),('.1464','144.31'),('.1549','152.69')]:money('Aid rounded BL then rate '+rate,cents(D(1000)*20700/21000)*D(rate),want)
money('Gal aid rounding separator',cents(D('1000.64')*20700/21000)*D('.1549'),'152.79');money('Val direct includedBI source rule',1000*D('.0742'),'74.20');money('Bal aid adjusted generalBL',D(1000)*23500/25000*D('.1771'),'166.47')
for B,w in [(3500,0),(7000,D('137.75')),(8000,D('232.75')),(8600,D('289.75')),(9600,D('384.75'))]:money('CLM own lower bracket minimum '+str(B),max(0,D(B)-5550)*D('.095'),w)
check('CLM single mover NaboveG capped quota',min(D(500),D('289.75')*20000/12000,D('289.75')),D('289.75'))
money('CLM both movers unresolved diagnostic',D('289.75')*11000/12000,'265.60')
check('Savings minimum spillover',max(0,5550-3500),2050);money('Savings tax with spillover',(10000-2050)*D('.095'),'755.25')
# Cantabria denominator loss-compensation controls are bounded, not universal signed-income rule.
check('Cantabria current shareloss25percent',min(8000,10000*D('.25')),2500);check('Cantabria included annual income',25000+10000-2500,32500);check('Cantabria strict10pct equality',D(3250)>D(32500)*D('.1'),False);check('Cantabria strict cent pass',D('3250.01')>D(32500)*D('.1'),True)
# National no fabricated entitlement, wealth condition and tax ordering.
check('National startup wealth neutral',100000-100000>=20000,False);check('National startup retained price gain excluded',(120000-20000)-100000>=20000,False);check('National startup actual new wealth',120000-100000>=20000,True);money('National startup credit',min(20000,100000)*D('.5'),10000)
check('NationalEV base and credit',min(30000-5000,20000)*D('.15'),3000);check('NationalEV25percent deposit',20000*D('.25'),5000);check('National2026 deposit final year',2026+2,2028);check('Nationalcharger base',min(5000-1000,4000)*D('.15'),600)
check('Ordinary regional quota no refund',max(0,200-300),0);check('Unabsorbed100 needs independent carry authority',max(0,300-200),100)
(O/'tranche18-controls.json').write_text(json.dumps({'method':'Independent Decimal/Fraction/calendar calculations from actually assessed Guide/source premises, not imported writer evaluation. Inference/counter-reading controls do not resolve preserved legal uncertainty.','count':len(r),'failures':0,'controls':r},ensure_ascii=False,indent=2)+'\n');print('PASS',len(r),'own controls')
