from fractions import Fraction as F
from pathlib import Path
import json
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
# Independent arithmetic on the explicit ordinary fact patterns, not tests of writer code.
c('microEligibleAssetsEquality',2_000_000<=2_000_000,True);c('microStaffTenNotBelow',10<10,False);c('BcorporateShare25Disqualifier',F(25,100)>=F(1,4),True);c('NcorporateShare25NotOver',F(1,4)>F(1,4),False);c('NturnoverHalfEquality',50_000>=100_000*F(1,2),True)
c('domesticDividendIntegrated',10_000*F(1,2),5000);c('domesticDividendQuota',5000*F('.24'),1200);c('dividendWrongFullQuota',10_000*F('.24'),2400)
c('globalImpairmentCeiling',(500_000-100_000-50_000)*F('.01'),3500);c('globalImpairmentIncrement',3500-2000,1500)
c('indexedCost',100_000*F('1.071'),107100);c('indexedDepreciation',3000*F('1.040')+3000*F('1.020'),6180);c('indexedNet',107100-6180,100920);c('carrying',100000-6000,94000);c('monetaryDeduction',100920-94000,6920);c('positiveDisposal',150000-94000-6920,49080);c('monetaryCapPositive',min(6920,5000),5000);c('lossNoCorrection',max(0,min(6920,-5000)),0)
c('carOrdinaryCap',min(10000*F('.5'),3000,F('.5')*F('.2')*30000),3000);c('carLowerExpense',min(2000*F('.5'),3000,3000),1000);c('electricDepRateCap',min(10000*F('.5'),4000,F('.5')*F('.2')*40000),4000);c('BfinancingProportion',2000*F('.5')*min(1,F(30000,40000)),750);c('NotherWithFinanceCap',min(12000*F('.5'),4000),4000)
c('microOptionBase',100000*(1-F('.15')),85000);c('microGrossQuota',85000*F('.2'),17000);c('microBucket',17000*F('.35'),5950);c('microFloor',85000*F('.15'),12750);c('microUsed',min(6000,5950,17000-12750),4250);c('microCarry',6000-4250,1750);c('microPayable',12750-10000,2750)
c('Nquota',100000*F('.19'),19000);c('NcreditBucket',19000*F('.25'),4750);c('Nclaim',min(8000,4750,19000-13000),4750);c('Ncarry',8000-4750,3250);c('Npayable',19000-4750-10000,4250);c('Ninstalment',(20000-2000)*F('.3'),5400)
c('AlavaAmountNoCredit',5000>100000*F('.1') or 5000>5_000_000,False);c('AlavaInterpretedFloor',100000*F('.17'),17000);c('AlavaDefaultFloor',100000*F('.19'),19000);c('AlavaSeparate6kClaim',min(6000,8400,24000-17000),6000);c('AlavaSeparate8kClaim',min(8000,8400,24000-17000),7000);c('NoCreditNoRateCut',24000-min(0,8400,7000),24000)
def nfloor(z,foreign,filmrd,p=F('.18'),h=F('.13')):return max(0,p*z-foreign) if filmrd==0 else max(0,h*z,p*z-foreign-filmrd)
c('NforeignOnlyMinimum',nfloor(100000,10000,0),8000);c('NfilmMinimum',nfloor(100000,6000,5000),13000);c('NfilmQuota',28000-6000-5000,17000);c('NforeignBelowFloorNoFilm',nfloor(100000,16000,0),2000);c('NfilmClaimImpossiblePositive',12000-1<nfloor(100000,16000,1),True)
c('SequentialOrdinary',100000*F('.35'),35000);c('SequentialRD',(100000-35000)*F('.7'),45500);c('SequentialEnv',(100000-35000-45500)*F('.5'),9750)
c('BenvGrant',20000*(1-F('.24')),15200);c('BenvBase',100000-15200,84800);c('BenvGenerated',84800*F('.35'),29680);c('AGenvGenerated',(100000-20000)*F('.35'),28000);c('TerritorialDifference',29680-28000,1680)
c('AGhire2026',7000*F('1.1'),7700);c('AGspecialHire',7700*2,15400);c('WomenYoungOverlay',F('.35')+F('.1'),F('.45'))
c('PensionRatio',F(1000,100000),F('.01'));c('PreferredBelow15',1000*F('.1'),100);c('OtherBelow15',1000*F('.05'),50);c('PreferredAt15',1500*F('.15'),225);c('OtherAt15',1500*F('.1'),150)
c('BGmeasure',190000+60000,250000);c('BGpriorMean',(100000+100000+100000)/3,100000)
slices=[15000,25000,25000,50000];parts=[F('.01'),F('.02'),F('.03'),F('.04')];s=sum(F('.24')*x*a for x,a in zip(slices,parts));c('BGsurcharge',s,816);c('BGincreasedQuota',190000*F('.24')+s,46416);c('BGnet',190000-46416,143584);c('WrongAverageAllocation',s*F(190000,250000),F('620.16'));c('WrongDirectProfitCharge',sum(x*a for x,a in zip(slices,parts)),3400)
t=F('.24');m=76000;E=190000;E0=F('1.35')*m/(1-t);c('AtriggerPreTax',E0,135000);left=E-E0;S=F(0);used=[]
for w,a in [(F('.15')*m,F('.01')),(F('.25')*m,F('.02')),(F('.25')*m,F('.03')),(None,F('.04'))]:
 I=left if w is None else min(left,w/(1-t-a*t));left-=I;S+=t*a*I;used.append(I)
c('AtaxableExcess',sum(used),55000);c('AexactSurcharge',S,F(29432841,111746));c('AwholeReconciliation',(E-(t*E+S))+(t*E+S),E);c('AthirdBand',F('1.75')*m < E-(t*E+S) <= 2*m,True);c('ADisplayCents',round(float(45600+S),2),45863.39)
c('232EqualNoTrigger',36000>36000,False);c('232CentTrigger',F('36000.01')>36000,True);c('BaggregateTwoTypes',20000+20000>36000,True);c('AGseparateTypes',any(v>36000 for v in [20000,20000]),False)
(O/'tranche14-controls.json').write_text(json.dumps({'count':len(checks),'checks':checks,'scope':'Independent selected ordinary fact patterns; conditional interpretations retained, no universal accounting allocation or return rounding proved.'},indent=2)+'\n');print(len(checks),'PASS')
