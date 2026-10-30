from fractions import Fraction as F
from decimal import Decimal as D
from pathlib import Path
import json
out=Path(__file__).parent;checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
c('Ceuta computer output CN8471',30000*F(35,1000),1050)
c('Ceuta importbase without doubled incidental',10000+600,10600)
c('Ceuta componentimport CN8473',10600*F(35,1000),371)
c('Ceuta directproducer interior',1050-371,679)
c('Ceuta import plus interior own remittances',371+679,1050)
c('Ceuta invalid service and electricity credit separator',679!=(1050-371-40-1),True)
c('Melilla officecomputer import',10600*F(10,100),1060)
c('Melilla general consultancy',20000*F(4,100),800)
c('Melilla advertising',10000*F(5,1000),50)
c('Melilla service return noinputrecovery',800+50,850)
c('Melilla own import plus service remittances',1060+850,1910)
c('Melilla computers cannot use Ceuta3.5percent',10600*F(10,100)!=10600*F(35,1000),True)
c('Ceuta included4percent price base',F(10400)/F(104,100),10000)
c('Ceuta included4percent tax',10400-F(10400)/F(104,100),400)
c('Ceuta electronic service versus telecommunication rate',10000*F(5,1000)!=10000*F(10,100),True)
c('Melilla electronic service versus telecommunications',10000*F(5,1000)!=10000*F(8,100),True)
c('Melilla protectedhousing max2garage equality',2<=2,True)
c('Melilla mainlyresidential50percent equality qualifies',F(50,100)>=F(1,2),True)
c('Melilla49.99percent fails residentialarea limb',F(4999,10000)>=F(1,2),False)
c('Melilla exactly6m notmonthlytrigger',6000000>6000000,False)
c('Melilla6m.01 monthlytrigger',D('6000000.01')>6000000,True)
c('Melilla objective prior450k equality passes amountgate',450000<=450000,True)
c('Melilla objective construction priorpublic40k equality',40000>40000,False)
c('Ceuta objective service100k equality passes amountgate',100000<=100000,True)
# Eligibility/module yield stipulated: computation is base*coefficient, not a universal turnover tax.
quarterbase=F(6000)*2/4
c('Melilla modules generalservice quarterlybase',quarterbase,3000)
c('Melilla modules generalservice quarterlytax',quarterbase*F(4,100),120)
c('Melilla modules actualannualyield Q4balance',8000*2*F(4,100)-3*120,280)
c('Melilla modules hospitality1.5 coefficient',6000*F(3,2)/4*F(1,100),F(45,2))
# Every monthly class checked on original paid tax1000, eligible used asset,11months.
rates=[('machinery','1.00','890'),('medical','1.25','862.50'),('ships_aircraft','0.85','906.50'),('internal_transport','0.85','906.50'),('external_transport','1.35','851.50'),('trucks','1.65','818.50'),('furniture','0.85','906.50'),('tools','2.00','780'),('IT','2.00','780'),('electronic','1.65','818.50'),('other','1.25','862.50')]
for n,r,expected in rates:c('Melilla export monthly '+n,D('1000')*(1-D(r)/100*11),D(expected))
c('Melilla export fractional11 versus exact10months',1000*(1-F(2,100)*10)-1000*(1-F(2,100)*11),20)
c('Melilla reduction linear not compounded',F(1000)*(1-F(2,100)*11)!=F(1000)*(1-F(2,100))**11,True)
c('Melilla fee separate from depreciation',F(780)-30,750)
(out/'tranche3-controls.json').write_text(json.dumps({'scope':'Own separating calculations. Actual city/CN/IAE/status/election/evidence/elapsed calendar inputs remain claimant gates; no statutory safe margin or generic bankdeadline invented.','count':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'PASS')
