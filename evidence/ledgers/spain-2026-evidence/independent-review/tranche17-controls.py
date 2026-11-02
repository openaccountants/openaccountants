from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
import json,re
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain');G=(W/'skills/international/spain/es-foral-income-tax.md').read_text().split('\n');C=[]
def ck(n,a,b):
 ok=a==b;C.append({'name':n,'actual':str(a),'expected':str(b),'pass':ok});assert ok,(n,a,b)
def num(x):return D(str(x).replace(',','').replace('%','').strip())
def cents(x):return x.quantize(D('.01'),rounding=ROUND_HALF_UP)
bg=[(0,0,23),(18080,'4158.40',28),(36160,'9220.80',35),(54240,'15548.80',40),(77450,'24832.80',45),(107260,'38247.30',46),(142960,'54669.30',47),(208390,'85421.40',49)]
bs=[(0,0,19),(7500,1425,20),(15000,2925,22),(30000,6225,24),(50000,11025,'25.5'),(90000,21225,26),(120000,29025,'26.5'),(240000,60825,27),(300000,77025,28)]
ng=[(0,0,13),(4458,'579.54',22),(10030,'1805.38',25),(21175,'4591.63',28),(35663,'8648.27','36.5'),(51266,'14343.37','41.5'),(66869,'20818.61',44),(89159,'30626.21',47),(139310,'54197.18',49),(195034,'81501.94','50.5'),(334344,'151853.49',52)]
ns=[(0,0,20),(6000,1200,22),(10000,2080,24),(15000,3280,26),(200000,51380,27),(300000,78380,28)]
for title,start,table in [('Basque-general',222,bg),('Basque-savings',233,bs),('Navarra-general',431,ng),('Navarra-savings',445,ns)]:
 table=[tuple(num(z) for z in r) for r in table]
 for i,r in enumerate(table):
  cells=G[start+i-1].split('|')[1:4];ck(f'{title}-printed-vector-{i}',tuple(num(v) for v in cells),r)
  if i:
   p=table[i-1];diff=abs(p[1]+(r[0]-p[0])*p[2]/100-r[1]);ck(f'{title}-adjacent-cumulative-{i}-within-one-cent',diff<=D('.01'),True)
# Independent separating computations from the actually read methods; no writer-result import.
ck('B-employee-net',D(40000)-2600,D(37400));ck('B-base',D(37400)-3000,D(34400));q=D('4158.40')+(34400-18080)*D('.28');ck('B-gross',q,D(8728));ck('B-annual-net',q-1615+5000*D('.19'),D(8063));ck('B-payable',q-1615+950-7500,D(563))
nq=cents(D('8648.27')+(37400-35663)*D('.365'));ck('N-general-round-half-up',nq,D('9282.28'));ck('N-work-credit',D(700)-D('.02')*2400,D(652));ck('N-payable',nq+1000-652-1084-8500,D('46.28'))
ck('AG-marginal-allowance-60k',D(35000)*D('.20')+D(25000)*D('.15'),D(10750))
ck('G-charity-BL-not-BI',min(D(20000),D(35000)*D('.30'))*D('.20'),D(2100));ck('wrong-BI-charity-separator',D(40000)*D('.30')*D('.20'),D(2400))
ck('disability-multiplier250-uplift',D(3000)*(1+D('2.5')),D(10500));ck('disability-positive-income-floor',min(D(7500),D(10500)),D(7500));ck('bonus-boundary-left',D(8000)-D('.6098')*D(23000-14800),D('2999.6400'))
ck('FIFO-partial-cost',D(2020)/2,D(1010));ck('FIFO-net-market-value',max(D(1800),D(1750))-18,D(1782));ck('FIFO-gain',D(1782)-1010,D(772));ck('FIFO-gross-tax',D(772)*D('.19'),D('146.68'));ck('wrong-later-lot',D(1782)-D(3030)/2,D(267));ck('updated-older-cost',D(1010)*D('1.020'),D('1030.200'));ck('older-updated-gain',D(1450)-D('14.5')-D('1030.2'),D('405.3'));ck('no-update-separator',D(1450)-D('14.5')-1010,D('425.5'))
for a,b in [(4000,4500),(4500,4000)]:ck(f'swap-symmetry-{a}',max(D(a),D(b))-1000,D(3500))
ck('mixed-main',D(5000)-60-1000,D(3940));ck('incoming-expense',D(5000)+40,D(5040));ck('fee-token-disposal',D(100)-60,D(40));ck('later-sale',D(6000)-5040,D(960));ck('no-double-count-fee',D(3940)+40+960,D(4940));ck('N-established-lot',D(5740)*D('.2'),D(1148));ck('blocked-loss-part-release',D(1000)*D('.4'),D(400));ck('blocked-unreleased',D(1000)-400,D(600))
ck('business-positive-schedule',D('9220.8')+(40000-36160)*D('.35'),D('10564.8'));ck('business-two-decimal-percent',cents(D('10564.8')/40000*100),D('26.41'));ck('business-gain-adjust',D('2.41')/100*10000,D(241));ck('AG-prior-loss-adjust',D('2.41')/100*(10000-6000),D('96.4'));ck('foreign-progressive-tax',D(30000)*D('.2641')-1615,D(6308));ck('business-BI-pool',D(7281)*16000/40000,D('2912.4'));ck('business-cap',D('2912.4')*D('.35'),D('1019.34'));ck('business-carry',D(2000)-D('1019.34'),D('980.66'));ck('wrong-BL-separator',D(7281)*16000/35000!=D('2912.4'),True)
for n,rate,result in [('B-male','.10',1000),('B-female','.15',1500),('AG-male','.15',1500),('AG-female','.20',2000)]:ck('employee-'+n,D(10000)*D(rate),D(result))
ck('new-B-A',min(D(10000)*D('.25'),D(20000)*D('.15')),D(2500));ck('new-G',min(D(10000)*D('.20'),D(20000)*D('.10')),D(2000));ck('ordinary-Basque-businesscap',D(4000)*D('.35'),D(1400));ck('ordinary-N-businesscap',D(4000)*D('.25'),D(1000))
ck('annuity-current-yield',D(30000)*D('.20'),D(6000));ck('AG-exempt-yield',D(10000)*D('.40'),D(4000));ck('annuity-taxable',D(6000)-4000,D(2000));ck('capital30pct',D(80000)*D('.70'),D(56000));ck('old25pct',D(80000)*D('.75'),D(60000))
ck('age65-mid-taper',D(393)-D('.0393')*5000,D('196.5'));ck('age75-mid-taper',D(714)-D('.0714')*5000,D(357));ck('widow-mid-taper',D(200)-D('.02')*5000,D(100));ck('age-credit-exact30k',D(393)-D('.0393')*10000,D(0))
ck('N-pension-income-cap',D(20000)*D('.30'),D(6000));ck('N-pension-spouse-strict8500',D(8500)<D(8500),False);ck('first-modality-net',D(20000)*D('.06')-800,D(400));ck('under100-waiver',D('99.99')<100,True);ck('exact100-not-waived',D(100)<100,False);ck('B-prior-year-instalment',D(20000)*D('.15')-1200,D(1800));ck('B-start-half',D(1800)/2,D(900));ck('B-nonpositive-general',D(80000)*D('.006'),D(480));ck('B-wholesale',D(100000)*D('.0025'),D(250));ck('A-start',D(3000)*D('.05'),D(150));ck('A-agrarian-halfyear',D(100000)*D('.02'),D(2000));ck('N-second-cumulative',D(8000)*D('.20')-400-500,D(700));ck('energy-community-netbase',D(20000)*D('.5')-2000,D(8000));ck('energy-credit',D(8000)*D('.15'),D(1200));ck('care-currentquota',min(D(2000),D(1500)),D(1500));ck('care-unused',D(2000)-1500,D(500));ck('Emanzipa-shared-before-eligibility',min(D(620)*D('.5'),D(280))/2,D(140));ck('IFP-lower-boundary',D(14100)<=14100,True)
(O/'tranche17-own-controls.json').write_text(json.dumps({'method':'Independent Decimal arithmetic and explicit schedule vectors; no writer controls imported. Statutory printed Navarra cumulative quotas retained; adjacent rounding tolerance one cent, not legal universal rounding.','count':len(C),'failures':sum(not z['pass'] for z in C),'controls':C},indent=2)+'\n');print('Own controls',len(C),'all PASS')
