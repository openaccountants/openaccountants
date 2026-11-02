from fractions import Fraction as F
from decimal import Decimal,ROUND_HALF_UP
from pathlib import Path
import json,re
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain');E=W/'ledgers/spain-2026-evidence/es-income-tax';O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def money(v):return (Decimal(v.numerator)/Decimal(v.denominator)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
g=(W/'skills/international/spain/es-income-tax.md').read_text().split('\n');anchors=json.loads((E/'regional-scale-native-anchors.json').read_text())
def esnum(t):
 t=t.strip().strip('» %').replace(' ','').replace('\u00a0','').replace('\u202f','')
 if t in ['–','—','-']:return F(0)
 if 'adelante' in t.lower():return None
 return F(t.replace('.','').replace(',','.'))
for k,x in enumerate(anchors,1):
 vals=[s.strip() for s in x['quote'].split('\n') if s.strip()];assert len(vals)==4,(k,vals)
 src=[esnum(v) for v in vals];v=[t.strip() for t in g[x['guide_lf']-1].split('|')[1:5]];current=[None if 'No upper' in z else F(z.strip('%')) for z in v]
 for j,(a,b) in enumerate(zip(src,current),1):c(f'regionrow{k}cell{j}',a,b)
# Scales independent of the writer implementation.
state=[(0,0,F('.095')),(12450,F('1182.75'),F('.12')),(20200,F('2112.75'),F('.15')),(35200,F('4362.75'),F('.185')),(60000,F('8950.75'),F('.225')),(300000,F('62950.75'),F('.245'))]
madrid=[(0,0,F('.085')),(F('13362.22'),F('1135.79'),F('.107')),(F('19004.63'),F('1739.53'),F('.128')),(F('35425.68'),F('3841.42'),F('.174')),(F('57320.40'),F('7651.10'),F('.205'))]
def scale(v,table):
 row=next(z for z in reversed(table) if v>=z[0]);return row[1]+(v-row[0])*row[2]
for b,q,r in state[1:]:c('stateCumulative'+str(b),scale(b,state),q)
c('over300kExtraState',scale(400000,state),F('87450.75'));c('MadridAge65',F('5956.65')+F('1234.26'),F('7190.91'));c('MadridAge75',F('7190.91')+F('1502.58'),F('8693.49'));c('BalearicAge65',6700*F('1.1'),7370);c('BalearicAge75',8100*F('1.1'),8910);c('CanaryAge75',5606+1162+1414,8182);c('GaliciaAge75',5789+1199+1460,8448)
R=18000-1150;c('employmentReference',R,16850);red=7302-F('1.75')*(R-14852);c('employmentReduction',red,F('3805.5'));B=R-2000-red;c('employmentBase',B,F('11044.5'));st=money(scale(B,state)-scale(5550,state));mt=money(scale(B,madrid)-scale(F('5956.65'),madrid));c('employeeStateCents',st,Decimal('521.98'));c('employeeMadridCents',mt,Decimal('432.47'));credit=F('590.89')-F('.2')*(18000-17094);c('employeeCredit',credit,F('409.69'));total=F(st)+F(mt)-credit;c('employeeFinal',total,F('544.76'));c('employeeRefund',600-total,F('55.24'))
c('simplifiedCombinedCap',min(2000,40000*F('.05')),2000);c('Ceuta10cap',min(2000,40000*F('.1')),2000);c('CeutaLowerProfit',min(2000,10000*F('.1')),1000);c('ordinaryLowerProfit',min(2000,10000*F('.05')),500)
st=money(scale(38000,state)-scale(5550,state));mt=money(scale(38000,madrid)-scale(F('5956.65'),madrid));c('professionalState',st,Decimal('4353.50'));c('professionalMadrid',mt,Decimal('3783.04'));offset=min(4000,10000*F('.25'));c('basketOffset',offset,2500);c('lossCarry',4000-offset,1500);bs=10000-offset;sav=6000*F('.19')+(bs-6000)*F('.21');c('savingsTax',sav,1455);c('professionalTotal',F(st)+F(mt)+sav,F('9591.54'));c('professionalPayable',F(st)+F(mt)+sav-9000,F('591.54'))
c('7pFullYear',2000+36500*F(45,365),6500);c('7pFullTaxable',38500-6500,32000);c('7pShort',3000+18400*F(46,184),7600);c('7pShortTaxable',21400-7600,13800);c('wrong365',money(3000+18400*F(46,365)),Decimal('5318.90'));c('7pTwoPayers',27300*F(39,273)+18400*F(36,92),11100);c('7pSharedCap',min(60100,40000+30000),60100);c('residualCredit',min(1990,4975),1990)
c('suppliesHome',1000*F('.3')*F(20,100),60);c('pensionE500',500*F('2.5'),1250);c('pensionE1500',1250+F('.25')*(1500-500),1500);c('pensionOver1500',1501,1501);c('pensionSalary60kStrict',60000>60000,False);c('spouse8kFails',8000<8000,False);c('pensionCombinedIncrement',min(8500,8500+4250),8500);c('pensionIncome30',10000*F('.3'),3000)
C=1800;T=26000;M=5550+1980;qa=scale(C,state)+scale(T-C,state)-scale(M,state);c('annuityProgAugQuota',qa,F('2168.4'));rate=100*qa/T;c('annuityProgRate',rate,F('8.34'));c('annuityProgHalf',qa*F(23000,T),F('1918.2'));c('annuityProgCombined',2*qa*F(23000,T),F('3836.4'));c('annuityEqualFails',23000<23000,False)
c('AEATRegionalAverageCorrectRound',money(2475*F(100,26800)),Decimal('9.24'));c('AEATCitySubtract',F(5778)-F('2035.01'),F('3742.99'));c('CeutaGeneralRounded',money(F('.6')*(2*F('3685.5'))*F(31000,34200)),Decimal('4008.79'));c('CeutaSavingsRounded',money(F('.6')*(2*F('2092.5'))*F(500,20500)),Decimal('61.24'));c('CeutaPublishedAddends',F('4008.78')+F('61.24'),F('4070.02'));c('CeutaSingleEndRoundDifferent',money(F('.6')*((2*F('3685.5'))*F(31000,34200)+(2*F('2092.5'))*F(500,20500))),Decimal('4070.03'))
c('residence183NotDayLimb',183>183,False);c('day184Yes',184>183,True);c('descendant8000Equality',8000<=8000,True);c('dependent1800Strict',1800>1800,False);c('50pctCreditSplit',100*F('.5'),50)
(O/'tranche16-controls.json').write_text(json.dumps({'count':len(checks),'checks':checks,'scope':'420 source table cell comparisons plus independent selected computations. Published cumulative cents used as enacted; no universal rounding convention or unresolved spillover/cross-basket rule invented.'},indent=2)+'\n');print(len(checks),'PASS')
