import json,re,hashlib
from fractions import Fraction as F
from pathlib import Path
out=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');p=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain/ledgers/spain-2026-evidence/spain-crypto-tax');checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def savings(b):
 b=F(b);return sum(max(0,min(b,hi)-lo)*F(rate,100) for lo,hi,rate in [(0,6000,19),(6000,50000,21),(50000,200000,23),(200000,300000,27),(300000,max(b,300000),30)])
for b,t in [(0,0),(6000,1140),(50000,10380),(200000,44880),(300000,71880),(400000,101880),(29650,F(12213,2)),(7500,1455),(26000,5340)]:c('savingstax'+str(b),savings(b),t)
for b,r in [(6000,21),(50000,23),(200000,27),(300000,30)]:c('marginalcent'+str(b),savings(F(b)+F(1,100))-savings(b),F(r,10000))
c('buyplusfee',25000+150,25150);c('netfiat',55000-200,54800);c('fiatgain',54800-25150,29650)
c('globalFIFO2secondunits',12-10,2);c('FIFOcost',12000+2*F(10000,5),16000);c('FIFOremaining',10000-2*F(10000,5),6000);c('wrongexchangeFIFOseparator',16000!=10000+7*1200,True)
c('swapmax',max(45600,44000),45600);c('swapgain',45600-16000,29600);c('swapinbasis',max(45600,44000),45600);c('swapoppositemax',max(44000,45600),45600)
c('disposalbasket',29600-33000,-3400);c('cross25',min(3400,10000*F(25,100)),2500);c('savingsbase',10000-2500,7500);c('carriedloss',3400-2500,900)
c('smallnegativefullyused',min(1000,10000*F(25,100)),1000);c('positivegainsnegativeincome',min(3000,8000*F(25,100)),2000);c('remainingincomeloss',3000-2000,1000);c('bothnegativecrossnone',max(0,-1000)*F(25,100),0)
c('mixedweightedout',100*F(60,100),60);c('mixedweightedin',100-60,40);c('outgain',5000-60-1000,3940);c('incomingbasis',5000+40,5040);c('feetokengain',100-60,40);c('latersale',6000-5040,960);c('feereconciliation',3940+40+960,4940);c('economicnet',6000-1000-60,4940)
c('badsubtractoutfrombasis',6000-(5000-60+40),1020);c('badbasisoverstatesgain',1020-960,60);c('badomitfeegain',3940+960,4900);c('badusehistoricalfee',5000-36-1000+(100-60)+6000-(5000+24),4980)
c('oldidentityloss',6000-10000,-4000);c('newpurchasegain',7000-6500,500);c('releasedoldnet',500-4000,-3500);c('blockednotbasisuplift',6500,6500)
c('721exact50k',50000>50000,False);c('72150001',50001>50000,True);c('721selfcustodyexcluded',50001,150001-100000);c('721reportwhole',50001,50001);c('721notexcess',50001!=1,True)
c('721sameincreaseexact20k',70000-50000>20000,False);c('721increase20001',70001-50000>20000,True);c('721latestnotinitial',120000-100000>20000,False)
c('generalcreditlosslimited',min(10000,20000*F(25,100)),5000);c('creditlossremainder',10000-5000,5000)
c('late0months',10000*F(1,100),100);c('late11months',10000*F(12,100),1200);c('lateafter12',10000*F(15,100),1500);c('late25reduction',1500*F(75,100),1125)
for n,e in [(1,300),(15,300),(16,320),(1001,20000)]:c('infofloorcap'+str(n),min(max(20*n,300),20000),e)
c('infohalfminimum',F(300,2),150);c('infohalfmaximum',F(20000,2),10000)
g=(p.parents[2]/'skills/international/spain/spain-crypto-tax.md').read_bytes();c('fullfrozenGuideexact',g==(p/'frozen-guide.md').read_bytes(),True);c('publishedGuideexact',g==(p/'published-guide.md').read_bytes(),True)
(out/'tranche11-controls.json').write_text(json.dumps({'count':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'PASS')
