from ledger_common import *
from fractions import Fraction as F
import math
slug='de-partners-and-part-year';rel='skills/international/germany/'+slug+'.md';raw=(R/rel).read_bytes();rows=list(units(raw.decode()));A={x['id']:x for x in json.loads((P/'support/de-income-tax/actual-read-quotes.json').read_text())};ep={x['id']:x for x in json.loads((P/'support/de-employee-income-tax/actual-read-quotes.json').read_text())}
for k in ['EMPLOYEE1230','COUPLE','ANNUAL','UNION','AO169']:A[k]=ep[k]
for k,so,lo,hi,art in [('PARTNER','Udd3313a3d03caa2a',9,10,'EStG §15(1) no2'),('PROFPART','U2230842af39717f7',17,17,'EStG §18(4)'),('MIXED','Udd3313a3d03caa2a',16,17,'EStG §15(3) no1'),('FORM','Udd3313a3d03caa2a',18,19,'EStG §15(3) no2'),('OPTION','Ue475dd2d8340b460',7,7,'KStG §1a(1) opening'),('INCOMEPERIOD','U14def75b3e601808',7,21,'EStG §2(1)'),('DETERMINATION','Ue887b51b668b3da1',7,8,'AO §179(1)/(2)'),('SUBJECT','U238ed59613d7e177',7,11,'AO §180(1) no2(a)'),('ONEPARTNER','U238ed59613d7e177',31,35,'AO §180(3)'),('FOREIGNDET','U238ed59613d7e177',37,40,'AO §180(5)'),('BIND','Uf61e6e820db3ffc3',7,7,'AO §182(1)'),('CHALLENGE','Ub73921a271e57902',8,8,'AO §351(2)'),('WHOF','U3315c1c42705c606',7,20,'AO §181(1)/(2)/(2a)'),('PARTCREDIT','Uc8f6bc69fc989c90',19,21,'EStG §35(2)–(4)'),('LIMITEDLOSS','Uaa4bd03133099579',7,11,'EStG §15a(1)–(4)'),('LIMITEDSAME','Uaa4bd03133099579',12,15,'EStG §15a(5) nos1/2'),('RETAIN','U04496684f283eed9',7,16,'EStG §34a(1)/(2), actual ordinary tax-payment withdrawal exclusion retained in quote'),('RECAPTURE','U04496684f283eed9',17,18,'EStG §34a(3)/(4)'),('PAYTRADE','Ubcfbb75636b0e7ab',7,7,'GewStG §5(1)'),('TRADEBASE','Uf36ac91d2b49b128',7,7,'GewStG §7 opening'),('TRADEDIV','Uccaace8ab6d45098',25,26,'GewStG §9 no2, full exceptions retained'),('CHANGE','U3c63ebfe1ecaac17',7,7,'GewStG §35b(1)'),('PARTLATE','Ua52afa3591a7820d',23,29,'AO §152(4)–(7)'),('MOVEINCOME','Ud922e63d4ac780f0',30,31,'EStG §32b(1) no2'),('PRORATE','Ud922e63d4ac780f0',56,64,'EStG §32b(2)'),('INSFOREIGN','U9f1b9a0058651caf',56,62,'EStG §10(2) no1 and own EU/EEA/Swiss exception'),('MANRATE','Ue2aedfd86ca19038',1141,1161,'EStH2025 H32b general exact example; not2026 statutory rounding'),('MANMOVE','Ue2aedfd86ca19038',1209,1211,'EStH2025 H32b temporary full liability'),('MANLOSS','Ue2aedfd86ca19038',1189,1194,'EStH2025 H32b foreign losses and exceptions'),('MANAHV','Ue2aedfd86ca19038',1188,1188,'EStH2025 H32b SwissAHV'),('MANKEY','U225307f99621c6a2',1222,1227,'BMF3November2016 as amended, Rn22/24'),('MANINS','Udc5977ffc0a66264',1908,1911,'BMF insurance letter Rn199, limited to cited exempt-pay context'),('MANFORM','Uaa16a18ba6ac4c8e',306,313,'ELSTER2025 ESt1B/FB/FE-G/FE-S names, not2026 form proof')]:take(A,k,so,lo,hi,art)
M={17:['ANNUAL','MOVEINCOME','PARTNER','DETERMINATION'],32:['RES','PARTNER'],33:['PROF','PROFPART','MIXED','FORM'],34:['MIXED'],35:['FORM'],36:['OPTION'],40:['RES','ANNUAL'],41:['ANNUAL'],48:['TARIFF','SPLIT'],49:['ANNUAL','TARIFF'],50:['PRORATE','MANRATE'],51:['MANRATE'],52:['EMPLOYEE1230','PRORATE'],53:['CREDIT','PARTCREDIT'],54:['PARTCREDIT'],55:['G11'],56:['RETAIN'],57:['RECAPTURE'],58:['RETAIN'],59:['SOLILIMIT','SoliRate'],60:['PARTLATE','AO152-10'],66:['DETERMINATION','SUBJECT','BIND'],68:['CASH','NOTRADEEXP'],69:['PARTNER'],70:['BUSCOST','PARTNER','SUBJECT'],71:['PARTNER','MANKEY'],72:['FOREIGNDET','PARTCREDIT'],74:['BIND','CHALLENGE','BASE'],76:['PAYTRADE','TRADEBASE','TRADEDIV','PARTCREDIT','MANKEY','CREDIT'],78:['LIMITEDLOSS','LIMITEDSAME'],80:['RETAIN','RECAPTURE','SoliRate'],84:['RES','ANNUAL'],86:['ANNUAL'],88:['INCOMEPERIOD'],89:['ANNUAL','NRTRADE'],90:['ANNUAL','EMPLOYEE1230','TARIFF'],92:['PROGRESSION','MOVEINCOME'],94:['MOVEINCOME','MANMOVE'],95:['PROGRESSION'],97:['PROGEXCEPTIONS','MOVEINCOME','MANLOSS'],99:['PRORATE','MANLOSS','MANAHV','EMPLOYEE1230'],101:['PRORATE','MANRATE','TARIFF'],103:['COUPLE'],109:['WHOF','MANFORM'],110:['WHOF','AO149-2','AO108'],111:['AO149-3','AO149-4'],112:['AO149-3'],113:['AO149-2','AO149-3','AO108'],114:['BIND','CHANGE'],115:['ANNUAL','AO149-2','AO149-3'],119:['PARTLATE','AO152-1','AO152-2','AO152-3','AO152-10'],120:['AO233a-2','AO238-1a','AO240-1'],121:['AO233a-1','DETERMINATION'],122:['CRIME','RECKLESS'],126:['NRTRADE','ONEPARTNER'],127:['FOREIGNDET','PROGRESSION','PROGEXCEPTIONS'],128:['PARTNER'],129:['MOVEINCOME','FOREIGNCREDIT'],130:['INSFOREIGN','MANINS','MANAHV']}
M[18]=M.pop(17)
case=['PARTNER','MANKEY','PARTCREDIT','CREDIT','G11','TARIFF','LUMPSUM','SOLILIMIT','SoliRate','ANNUAL','MOVEINCOME','PRORATE','MANRATE','EMPLOYEE1230']
for z in rows:
 z['anchors']=M.get(z['lf'],[])
 if z['section'].startswith('Example'):z.update(anchors=case,kind='computed fictional input / arithmetic / output')
 elif z['anchors']:z['kind']='positive own statutory/admin rule'
 elif z['section']=='Sources':z['kind']='historical source route / precise stated boundary / attribution'
 elif z['section']=='Ask the client first':z['kind']='intake question; positive parameters sourced in current substantive rows'
 elif z['wording'].startswith('|'):z['kind']='presentation table label'
 elif z['lf']in [20,21,22,23,24,25,26,30,38,42]:z['kind']='scope / sibling routing / section introduction'
 else:z['kind']='UNCLASSIFIED'
 if z['lf']==80:z['evidence_note']='Current text expressly a summary/referral, not complete34a calculation. Exact quote includes tax/surcharge-payment withdrawal exclusion and annual recapture balance; no simple unconditional withdrawal formula is certified.'
 if z['lf']==128:z['evidence_note']='The substantial-interest25percent limb is ownAStG2(3), checked in named exit-tax ledger; this is an expressly referred business-exit population, not automatic6AStG application to every partnership share.'
# Current scope source notes on the admin example and old cases remain explicit.
used={k for z in rows for k in z['anchors']};A={k:v for k,v in A.items()if k in used}
old=[]
for ref in ['b0e37140e1383d6e8628f6d4d8e8b63831b8703a',REF]:
 body=subprocess.check_output(['git','show',ref+':'+rel],cwd=R).decode()
 for z in units(body):
  same=next((x for x in rows if x['wording']==z['wording']),None)
  if same:d='Exact wording retained at current LF'+str(same['lf'])+', '+same['section']
  elif 'still on'in z['wording']:d='Historical sibling-year warning replaced by current source-specific2026 handoff at LF21.'
  else:d='PENDING semantic destination'
  old.append(dict(ref=ref,old_lf=z['lf'],section=z['section'],wording=z['wording'],destination=d))
C=[]
def ck(n,a,b):assert a==b,(n,a,b);C.append(dict(label=n,actual=str(a),expected=str(b)))
def tariff(v):
 x=math.floor(v)
 if x<=12348:t=F(0)
 elif x<=17799:y=F(x-12348,10000);t=(F('914.51')*y+1400)*y
 elif x<=69878:z=F(x-17799,10000);t=(F('173.10')*z+2397)*z+F('1034.87')
 elif x<=277825:t=F(42,100)*x-F('11135.63')
 else:t=F(45,100)*x-F('19470.38')
 return math.floor(t)
ti=300000+120000-4000;m=(ti-24500)*F('.035');g=m*F('3.8');inc=300000*F('.6')+120000-4000;tx=inc-15000-36;t=tariff(tx);credit=min(4*m*F('.6'),t,g*F('.6'));it=t-credit;sol=math.floor(min(it*F('.055'),(it-20350)*F('.119'))*100)/100
for n,a,b in [('KG trade base',ti,416000),('KG Messbetrag',m,F('13702.50')),('KG trade tax',g,F('52069.50')),('Anna income',inc,296000),('Anna Messbetrag',m*F('.6'),F('8221.50')),('Anna trade payable',g*F('.6'),F('31241.70')),('Anna taxable',tx,280964),('Anna tariff',t,106963),('Anna credit',credit,F('31241.70')),('Anna income tax',it,F('75721.30')),('Anna solidarity',str(sol),'4164.67'),('credit amount unused',4*m*F('.6')-credit,F('1644.30'))]:ck(n,a,b)
tx=36000-1230-5500-36;rb=tx+30000;rt=tariff(rb);rate=F(math.floor(F(rt,rb)*1000000),1000000)
for n,a,b in [('arrival taxable',tx,29234),('arrival rate base',rb,59234),('arrival base tax',rt,13938),('arrival rate',rate,F('.235304')),('arrival tax',math.floor(tx*rate),6878),('arrival plain tax',tariff(tx),4002),('official2025 rounding example',F(math.floor(F(2540,37000)*1000000),1000000),F('.068648')),('limited loss positive capital10k/loss30k blocked',max(30000-10000,0),20000),('partnership positive100k one month surcharge',100000*F('.000625'),F('62.50'))]:ck(n,a,b)
write(slug,raw,rows,A,old,C,'The full current Guide and actual first-introduction/main bodies were read. Same-writer common tariff/deadline sources are reused; partnership and selected original own official2025 handbook/ELSTER clauses were actually read29October2026. The four-decimal percentage truncation is expressly the published2025 example inference, not a quoted statutory rounding clause or2026 software observation. All example inputs are fictional; exactFraction controls recompute both current oa cases, including after-credit Soli and the general profit-key allocation. The detailed34a election/recapture method, exact2026 determination forms and part-year foreign-period social-insurance deduction remain precisely stated referrals/evidence limits. No complete foreign treaty selection or limited-partner capital/debt ledger is invented. No independent or country PASS.')
