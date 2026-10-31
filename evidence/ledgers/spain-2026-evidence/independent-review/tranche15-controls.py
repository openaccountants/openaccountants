from fractions import Fraction as F
from pathlib import Path
import json,re,datetime,hashlib
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain');P=W/'ledgers/spain-2026-evidence/es-foral-non-resident-tax';O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');Q=json.loads((P/'selected-quotes-for-writer-read.json').read_text());R=json.loads((P/'claim-rows.json').read_text());checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
# Every own-source table cell compared against the actual current table, not writer vectors.
g=(W/'skills/international/spain/es-foral-non-resident-tax.md').read_text();pit=g.split('### Complete2026 non-PE property-gain coefficients')[1].split('### PEs:')[0];cit=g.split('### Separate2026 PE/CIT monetary-correction coefficients')[1].split('## Deadlines')[0]
for x in Q:
 m=re.match(r'(CIT|PIT)_coef_(araba|bizkaia|gipuzkoa)_2026_(\d+)$',x['key'])
 if not m:continue
 kind,province,year=m.groups();rows=re.findall(r'^\|\s*'+year+r'(?: and earlier)?\s*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|',pit if kind=='PIT' else cit,re.M);assert len(rows)==1
 sourcecells=re.findall(r'\b\d+,\d{3}\b',x['quote']);assert sourcecells and all(v==sourcecells[0] for v in sourcecells)
 idx={'bizkaia':0,'araba':1,'gipuzkoa':2}[province];c(x['key'],F(rows[0][idx]),F(sourcecells[0].replace(',','.')))
# Selected independent ordinary computations and strict boundaries.
c('residential30',12000*(1-F('.3'))*F('.19'),1596);c('rural35',12000*(1-F('.35'))*F('.19'),1482);c('restricted70',12000*(1-F('.7'))*F('.19'),684);c('otherDwelling20',12000*(1-F('.2'))*F('.19'),1824);c('residentialFloor',max(0,12000*(1-F('.7'))-5000),0);c('insuranceCap',min(450,300),300)
c('nonresidentialDep',100000*F('.03'),3000);c('nonresidentialBase',12000-2000-3000,7000);c('nonresidentialTax',7000*F('.19'),1330);c('noExpenseThirdCountry',12000*F('.24'),2880)
c('wageFinal', (20000-1200)*F('.19'),3572);c('BAgrossWithholding',20000*F('.19'),3800);c('BArefund',3800-3572,228)
c('individualDividend', (6000-1500)*F('.19'),855);c('individualCapGlobal',min(1000,1500)+min(1000,max(0,1500-1000)),1500);c('corporateNoIndividualExemption',6000*F('.19'),1140);c('sharedWithholding60',1140*F('.6'),684);c('sharedWithholding40',1140*F('.4'),456)
def pension(p):return min(p,12000)*F('.08')+min(max(p-12000,0),6700)*F('.3')+max(p-18700,0)*F('.4')
c('pension12000',pension(12000),960);c('pension18700',pension(18700),2970);c('pension20000',pension(20000),3490);c('pensionAveragePayment',pension(20000)*F(2000,20000),349)
c('indexedBasis',203000*F('1.249'),253547);c('netSale',400000-1500,398500);c('gain',398500-253547,144953);c('gainTax',144953*F('.19'),F('27541.07'));c('buyer3Gross',400000*F('.03'),12000);c('sellerBalance',F('27541.07')-12000,F('15541.07'));c('buyerWrong3Gain',144953*F('.03')!=12000,True)
c('NavarraImputation',100000*F('.011')*F('.19'),209);c('partYearImputation',100000*F('.011')*F(100,365)*F('.19'),F(4180,73));c('PIT1994BeforeException',100000*F('2.030'),203000);c('PIT1994Dec31Exception',100000*F('2.156'),215600);c('exceptionDifference',215600-203000,12600)
c('PEquota',104000*F('.24'),24960);c('PEbalance',24960-5000,19960);c('PEshare60',19960*F('.6'),11976);c('PEshare40',19960*F('.4'),7984);c('PEordinaryOwn19Interpretation',190000*F('.24'),45600);c('ResidentComparatorNotPEEnactment',45600+816,46416)
c('BasqueRemittance',10000*F('.2'),2000);c('StateNavarraRemittance',10000*F('.19'),1900);c('remittanceDifference',2000-1900,100)
c('interestDerived',F('3.25')*F('1.25'),F('4.0625'));c('interestYear',10000*F('.040625'),F('406.25'));c('interest73days',10000*F('.040625')*F(73,365),F('81.25'));c('thresholdInclusive',12000000<=12000000,True);c('thresholdNextCent',F('12000000.01')>12000000,True);c('annualiseHalf',6000001*2,12000002)
for n,d in [('Feb2',datetime.date(2026,2,2)),('Apr27',datetime.date(2026,4,27)),('Jul27',datetime.date(2026,7,27)),('Oct26',datetime.date(2026,10,26))]:c('calendarMonday'+n,d.weekday(),0)
(O/'tranche15-controls.json').write_text(json.dumps({'count':len(checks),'checks':checks,'scope':'231 actual own coefficient cells plus selected independent computations. B/A gross withholding valid; G cross-reference discrepancy is not silently resolved by arithmetic.'},indent=2)+'\n');print(len(checks),'PASS')
