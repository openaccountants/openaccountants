import json,math
from fractions import Fraction as F
from decimal import Decimal,ROUND_HALF_UP
from pathlib import Path
out=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def money(x):
 x=F(x);return (Decimal(x.numerator)/Decimal(x.denominator)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
def t(b):
 b=F(b);return sum(max(0,min(b,hi)-lo)*F(rate,100) for lo,hi,rate in [(0,12450,19),(12450,20200,24),(20200,35200,30),(35200,60000,37),(60000,300000,45),(300000,max(b,300000),47)])
def truncpct(q,g):return F(math.floor(F(q)/g*10000),100)
def red(r):
 r=F(r)
 if r<=14852:return min(r,7302)
 if r<=F('17673.52'):return F(7302)-F('1.75')*(r-14852)
 if r<F('19747.5'):return F('2364.34')-F('1.14')*(r-F('17673.52'))
 return 0
for b,e in [(0,0),(12450,F('2365.5')),(20200,F('4225.5')),(35200,F('8725.5')),(60000,F('17901.5')),(300000,F('125901.5')),(400000,F('172901.5'))]:c('scale'+str(b),t(b),e)
c('ordinarySSsum',F('.047')+F('.0155')+F('.001')+F('.0015'),F('.065'));c('annualSS',30000*F('.065'),1950);c('ordinaryR',30000-1950,28050);c('ordinaryRED',red(28050),0);c('ordinaryB',30000-1950-2000,26050);c('T26050',t(26050),F('5980.5'));c('min5550',t(5550),F('1054.5'));c('Q4926',t(26050)-t(5550),4926);c('43capnotbinding',(30000-15876)*F('.43')>4926,True);c('ordinaryrate',truncpct(4926,30000),F('16.42'));c('monthlytax',2500*F('.1642'),F('410.5'));c('monthlySS',2500*F('.065'),F('162.5'));c('netcash',2500-F('410.5')-F('162.5'),1927);c('employerSS',2500*(F('.236')+F('.055')+F('.002')+F('.006')+F('.0075')+F('.015')),F('803.75'));c('employercost',2500+F('803.75'),F('3303.75'))
c('revisedSS',36000*F('.065'),2340);c('revisedB',36000-2340-2000,31660);c('revisedquota',t(31660)-t(5550),6609);c('remainingquota',6609-2463,4146);c('remainingpay',36000-15000,21000);c('regtruncated',truncpct(4146,21000),F('19.74'));c('regmonthlytax',3500*F('.1974'),F('690.9'));c('regmonthlySS',3500*F('.065'),F('227.5'));c('regmonthlynet',3500-F('690.9')-F('227.5'),F('2581.6'));c('regannual',2463+6*F('690.9'),F('6608.4'));c('regdifference',6609-F('6608.4'),F('.6'))
r=F('21008.84')-F('2194.78');c('separatorR',r,F('18814.06'));raw=red(r);c('separatorrawRED',raw,F('1064.1244'));rd=F(money(raw));c('separatorroundedRED',rd,F('1064.12'));b=r-2000-rd;c('separatorB',b,F('15749.94'));q=t(b)-t(5550);c('separatorQ',q,F('2102.9856'));c('separator43cap',(F('21008.84')-15876)*F('.43'),F('2207.1212'));c('separatorcorrectrate',truncpct(q,F('21008.84')),F('10.01'));c('separatorwrongunrounded',truncpct(t(r-2000-raw)-t(5550),F('21008.84')),10)
c('REDat14852',red(14852),7302);c('REDat1767352',red(F('17673.52')),F('2364.34'));c('REDat197475',red(F('19747.5')),0);c('REDonecentbelowend',money(red(F('19747.49'))),Decimal('.01'));c('REDcappedatR',red(4000),4000)
c('halfcentup',money(F('1.005')),Decimal('1.01'));c('subtotalafterloop',money(2*F(1150,3)),Decimal('766.67'));c('wrongperrelative',2*money(F(1150,3)),Decimal('766.66'));c('pcttruncnotround',truncpct(F('17.85964523'),100),F('17.85'))
c('shortcontractminimum',max(0,2),2);c('Ceutafloor',2*F('.4'),F('.8'));c('Ceutaspecialfloor',15*F('.4'),6);c('mortgage2points',F('16.42')-2,F('14.42'));c('mortgagecutoffstrict',F('33007.20')<F('33007.2'),False);c('quota35200inclusive',35200<=35200,True);c('spouse1500inclusive',1500<=1500,True)
c('kindaccount',1000*F('.1642'),F('164.2'));c('kindcertificateborne',1000+F('164.2'),F('1164.2'));c('kindcertificatecharged',1000,1000)
c('SMIyear',1221*14,17094);c('SMI12instalments',F(17094,12),F('1424.5'));c('FOGASAreconstruction',money(2*(F('40.70')+F(2*1221,365))),Decimal('94.78'));c('FOGASAwages',F('94.78')*120,F('11373.6'));c('FOGASAindemnity',F('94.78')*365,F('34594.7'))
c('ordinaryITday4to20',17*100*F('.6'),1020);c('ordinaryITday21plus10days',10*100*F('.75'),750);c('oldmenstruationday1to20',20*100*F('.6'),1200);c('newcertainprocessday2to20',19*100*F('.6'),1140);c('donation100',100*F(1),100);c('BRpreviousmonth',F(3000,30),100);c('newcertainBRpriorprevious',F(2700,30),90)
c('nursing8hourHalfHourExample',100*F(1,16),F('6.25'));c('birthparttime365',F(12000,365),F(2400,73));c('birthshortactual',F(6000,180),F(100,3));c('objective5years',5*20*100,10000);c('unfair5years',5*33*100,16500);c('fixedtermhalfyear',F(12,2)*100,600);c('wageinterest10',1000*F('.1'),100)
c('hospital7noextension', 7>7,False);c('hospital8extension',min(8,13*7),8);c('hospital100capped',min(100,13*7),91);c('motherMandatory6weeks',6*7,42)
(out/'tranche13-controls.json').write_text(json.dumps({'count':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'PASS')
