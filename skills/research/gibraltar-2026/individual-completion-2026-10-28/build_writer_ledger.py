from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as ET
K=Path(__file__).resolve().parent;C=K.parents[3];S=C.parent/'work/sources'
G=C/'skills/international/gibraltar/gi-individual-income-tax.md'
def norm(s):return re.sub(r'\s+',' ',s).strip()
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def clean(s):
 out=[]
 for line in s.replace('\f','\n').splitlines():
  z=line.strip()
  if not z or z.startswith('© Government of Gibraltar') or re.fullmatch(r'Page \d+ of \d+',z):continue
  if re.fullmatch(r'(?:2010-21\s+Income Tax|Income Tax\s+2010-21|1952-11\s+Income Tax|Income Tax\s+1952-11|Income Tax|2010-21|1952-11|Repealed|1992/016|1989/096|1989/099|2004/005)',z):continue
  if z in ['Income Tax (Allowances, Deductions and Exemptions)','Rules, 1992','Rates of Tax Rules, 1989','Home Purchase (Deductions) Rules, 1989','Home Purchase (Special Deduction) Rules 2004']:continue
  if re.fullmatch(r'(?:1992/016\s+Rules, 1992|1989/096\s+Rates of Tax Rules, 1989|1989/099\s+Home Purchase \(Deductions\) Rules, 1989|2004/005\s+Home Purchase \(Special Deduction\) Rules 2004)',z):continue
  if re.fullmatch(r'(?:Rules, 1992\s+1992/016|Rates of Tax Rules, 1989\s+1989/096|Home Purchase \(Deductions\) Rules, 1989\s+1989/099|Home Purchase \(Special Deduction\) Rules 2004\s+2004/005)',z):continue
  out.append(z)
 return '\n'.join(out)
source_specs={
 'A':('allowances-rules-20260323.txt','https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf'),
 'T':('income-tax-act-20260323.txt','https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf'),
 'R':('rates-tax-rules-20240701.txt','https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf'),
 'O':('income-tax-act-1952-repealed.txt','https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1952-11/1952-11o.pdf'),
 'H':('individual/home-purchase-current.txt','https://www.gibraltarlaws.gov.gi/legislations/home-purchase-deductions-rules-1989-398/download'),
 'P':('individual/home-purchase-special-current.txt','https://www.gibraltarlaws.gov.gi/legislations/home-purchase-special-deduction-rules-2004-412/download'),
 'N':('individual/paye-current.txt','https://www.gibraltar.gov.gi/income-tax-office/individuals-and-employees/paye'),
 'E':('individual/tax-services-current.txt','https://portal.egov.gi/services/tax'),
 'SE':('individual/self-employed-current.txt','https://www.gibraltar.gov.gi/income-tax-office/individuals-and-employees/self-employed'),
 'Q':('individual/qnups-revised.txt','https://www.legislation.gov.uk/uksi/2010/51/data.xml'),
 'HM':('individual/hmrc-ihtm17025.txt','https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm17025'),
 'AI':('individual/allowances-index-current.txt','https://www.gibraltarlaws.gov.gi/legislations/income-tax-allowances-deductions-and-exemptions-rules-1992-405')}
source_specs.update({
 'ITO':('final-ordinary/ito-current.txt','https://www.gibraltar.gov.gi/income-tax-office'),
 'IT1':('final-ordinary/individual-return2026.txt','https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Employers/Tax_ReturnForm2026.pdf'),
 'ITG':('final-ordinary/individual-return-guidance2026.txt','https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Tax%20Returns/Tax%20Return%20Guidance%202026_.pdf')})
texts={k:clean((S/p).read_text()) for k,(p,url) in source_specs.items()}
proofs={}
def proof(id,src,provision,start,end=None,last=False):
 t=texts[src];ms=list(re.finditer(start,t,re.M));assert ms,(id,start)
 m=ms[-1] if last else ms[0];stop=len(t)
 if end:
  n=re.search(end,t[m.end():],re.M);assert n,(id,end);stop=m.end()+n.start()
 body=norm(t[m.start():stop]);words=body.split();quotes=[' '.join(words[i:i+45]) for i in range(0,len(words),45)]
 assert all(norm(q) in norm(t) for q in quotes)
 proofs[id]={'id':id,'source':src,'url':source_specs[src][1],'provision':provision,'read_on':'2026-10-28','quotes':quotes}
for n,end in [('3A','3AA'),('6','6A'),('6A','6B'),('6B','6C'),('6C','7'),('7','7A'),('7A','8'),('8','9'),('9','10'),('12','13'),('13','14'),('14','14A'),('14A','15'),('15','16'),('16A','16B'),('16B','16C'),('16C','16D'),('16D','16E'),('16E','16F'),('16F','17'),('17','18'),('18','19'),('20','20A'),('20A','20B'),('20B','21'),('21','21A'),('21A','22'),('22','23'),('24','24A'),('24A','25'),('29','30')]:
 start=rf'^{n}\.\s*\(1\)' if n not in ['6A','9','12','13','17','18','20','24A','29'] else rf'^{n}\. '
 proof('A'+n,'A','Allowances Rules '+n,start,rf'^{end}\.',last=n in ['6A','9','12','13','17','18','20','24A','29'])
for n,end in [('2','3'),('3','3A'),('3A','3B'),('3B','3C'),('3C','6')]:
 proof('R'+n,'R','Rates of Tax Rules '+n,rf'^{n}\.\s*\(1\)',rf'^{end}\.\s*\(1\)')
for n,end in [('14A','14B'),('14B','15'),('28','29'),('34','35'),('39','40'),('47','48'),('64','65'),('65','66')]:
 proof('T'+n,'T','Income Tax Act section '+n,rf'^{n}\.\s*\([1l]\)',rf'^{end}\.\s*(?:\([1l]\)|Where)')
proof('A25','A','Allowances Rules 25 revoked',r'^25\. Revoked',r'^26\.',last=True)
proof('Aversions','A','Allowances consolidation amendment table, LN2026/054 commencement',r'^2026/024',r'^ARRANGEMENT OF RULES')
proof('T74R','T','Income Tax Act s74 ordinary-residence definition',r'^“ordinarily resident” when applied to an individual',r'^“pension”')
proof('T74Y','T','Income Tax Act s74 assessment-year definition',r'^“year of assessment” means',r'^Repeals, amendments')
proof('TS1','T','Income Tax Act Schedule 1 Part 1 Tables A/B',r'^“Trade, business, profession or vocation”',r'^Table C',last=True)
proof('TS9','T','Income Tax Act Schedule 9 paragraphs 13–17 and 20',r'^13\. The repeal of provisions',r'^Application paragraphs 17 and 18')
# Include the context-permits proviso as a distinct proof; the source prints it as paragraph 20.
proof('TS920','T','Schedule 9 paragraph 20',r'^20\. Paragraphs 16 and 17 apply',r'^Schedule 10')
proof('O34','O','Repealed Income Tax Act 1952 section 34(3)–(4)',r'^34\.\(1\) and \(2\) Revoked',r'^36\. Repealed')
for n,end in [('2','2A'),('2A','3'),('3','4'),('4','5'),('5','6'),('6','7'),('8',None)]:
 start=rf'^{n}\.\s*\(1\)' if n in ['2','2A','6','8'] else rf'^{n}\. '
 proof('H'+n,'H','Home Purchase Rules '+n,start,rf'^{end}\.' if end else None,last=n in ['3','4','5'])
for n,end in [('2','3'),('3','4'),('4',None)]:
 proof('P'+n,'P','Special Home Purchase Rules '+n,rf'^{n}\.\s*'+('' if n=='2' else r'\(1\)'),rf'^{end}\.' if end else None,last=n=='2')
proof('T19A','T','Income Tax Act Schedule 3 paragraph 19A',r'^19A\.\(1\)',r'^Private Education\.')
proof('T19B','T','Income Tax Act Schedule 3 paragraph 19B',r'^19B\.\(1\)',r'^19C\.\(1\)')
proof('Nhome','N','ITO PAYE property-allowance instructions',r'^In order to claim for the above,',r'^Q\. Do I need')
proof('Nleave','N','ITO PAYE departure FAQ',r'^A\. If you are leaving Gibraltar permanently',r'^Q\. What is a Benefit')
proof('Eroute','E','Tax eServices public service entries and registration notices',r'^Apply for an S1 certificate',r'^Cookie Consent')
proof('SEpay','SE','Self-employed payments on account / balance FAQ',r'^A\. These are advance payments',r'^Q\.\s*What will happen')
proof('SEold','SE','Self-employed allowance-table period label',r'^Amount$',r'^Who is eligible')
proof('HMidentify','HM','HMRC IHTM17025 identifying SI 2010/51',r'^A QNUPS is defined',r'^The regulations specify')
proof('AIcurrent','AI','Official current Allowances Rules version',r'^Last Update: 23 Mar 2026',r'^LEGISLATION MADE UNDER')
qt=texts['Q'].splitlines()
for n,title in [('2','Interpretation'),('3','Scope of these Regulations'),('4','Requirements for qualifying non-UK pension schemes'),('5','Recognition for tax purposes'),('6','Requirements for schemes recognised for tax purposes'),('7','Requirements for schemes established by international organisations'),('Schedule','SCHEDULE')]:
 proof('Q'+n,'Q','SI 2010/51 regulation '+n if n!='Schedule' else 'SI 2010/51 Schedule',r'^'+re.escape(title),r'^'+re.escape({'2':'Scope of these Regulations','3':'Requirements for qualifying non-UK pension schemes','4':'Recognition for tax purposes','5':'Requirements for schemes recognised for tax purposes','6':'Requirements for schemes established by international organisations','7':'SCHEDULE'}.get(n,'THIS NEVER MATCHES')) if n!='Schedule' else None)
# Keep proofs confined to the operative portions actually used, without unrelated company/notice penalties.
def requote(id,body,provision=None):
 words=norm(body).split();proofs[id]['quotes']=[' '.join(words[i:i+45]) for i in range(0,len(words),45)]
 if provision:proofs[id]['provision']=provision
 assert all(norm(q) in norm(texts[proofs[id]['source']]) for q in proofs[id]['quotes'])
for id in ['R3B','R3C']:
 body=' '.join(proofs[id]['quotes']);requote(id,body[:body.index('modifications.')+len('modifications.')])
b=' '.join(proofs['T28']['quotes']);requote('T28',b[:b.index('(3) In the case of a trust')],'Income Tax Act section 28(1)–(2)')
b=' '.join(proofs['T34']['quotes']);requote('T34',b[:b.index('(4) Notwithstanding')],'Income Tax Act section 34(1)–(3)')
b=' '.join(proofs['T39']['quotes']);first=b[:b.index('(4) (a) A company')];later=b[b.index('(5) Where the Taxpayer'):b.index('(8) The Minister')]
# Separate the non-contiguous portions; do not present their junction as an exact quote.
requote('T39',first,'Income Tax Act section 39(1)–(3)')
proofs['T39reduce']={**proofs['T39'],'id':'T39reduce'};requote('T39reduce',later,'Income Tax Act section 39(5)–(7)')
b=' '.join(proofs['T65']['quotes']);first=b[:b.index('(3) In the event')];later=b[b.index('(4) The Commissioner may'):b.index('Penalties for failure to comply with requirements on certain notices.')]
requote('T65',first,'Income Tax Act section 65(1)–(2)')
proofs['T65relief']={**proofs['T65'],'id':'T65relief'};requote('T65relief',later,'Income Tax Act section 65(4)–(5)')
assert hashlib.sha256((S/'individual/qnups-revised.xml').read_bytes()).hexdigest()=='bd6472b4eb7741dc1b5a83bdf82229084f4236bdb7ba3ce0895d8ec1e1da90f3'
xml=(S/'individual/qnups-revised.xml').read_text();assert 'RestrictStartDate="2020-12-31"' in xml
proofs['Qxml']={'id':'Qxml','source':'QXML','url':source_specs['Q'][1],'provision':'Official revised SI 2010/51 XML root version metadata','read_on':'2026-10-28','quotes':['RestrictStartDate="2020-12-31"']}
old=json.loads((K/'original-paragraphs.json').read_text());old_by={x['id']:x for x in old}
rows=[]
def add(id,rule,section,refs,oldids='',new=''):
 ids=[f'IND-P{int(x):03}' for x in oldids.split()] if oldids else []
 rows.append({'id':id,'rule':rule,'guide_section':section,'proof_ids':refs.split(),'original_paragraph_ids':ids,'new_anchor':new,'read_on':'2026-10-28'})
add('IND-01','Assessment year 1 July 2026–30 June 2027 is derived from the statutory twelve-month cycle following January–June 2011.','Who this applies to','T74Y','2')
add('IND-02','183-day / three consecutive years exceeding 300 days residence tests; part of day counts. Treaty residence is separate.','Who this applies to','T74R','4')
add('IND-03','Ordinary ABS and both GIBS marginal tables, £25,000 table switch, election and exact Commissioner disregard conditions; overrides only 2022/23 and 2023/24. Synthetic pre-credit examples £7,990 and £4,160 use different bases.','Rates, bands and thresholds','R2 R3A R3B R3C','6 7 8 25 26 65')
add('IND-04','Partial-year one-twelfth language retained. Repealed s34(3) was non-resident relief; current s34(3) is assessments. Schedule 9 continuity is conditional; current rewritten eligibility not established. Rule 24 concerns non-resident pensioners, not every frontier worker.','Rates, bands and thresholds','R2 R3A O34 T34 TS9 TS920 A24','9')
add('IND-05','ABS balance after eligible deductions; £3,455 personal allowance, complete-month residence reduction and GIBS exclusion.','The base','A6','10 11')
add('IND-06','GIBS and spouse/civil-partner restrictions, grandfathered claims and separate self-only exceptions; no double spouse claims.','The base','A6A A6B','12 16',new='Apply the system and spouse restrictions')
add('IND-07','Minimum-deductions top-up is difference to £4,343, not another full allowance. Revoked-rule-25 reference and monthly reduction retained. Example £4,343 less £3,455 is £888; £5,000 already above floor.','The base','A16C A6A A6B A25','11 13 67')
add('IND-08','Low-income allowance amounts, four income ranges, form and PAYE provisional-code reconciliation, complete non-resident months.','The base','A16B','11')
add('IND-09','ABS tax-credit ceiling greater of £300 or 2%; PAYE-table implementation and complete-month reduction; no claimed automatic refund entitlement.','The base','A6C','11')
add('IND-10','GIBS approved-pension deduction from earned income is paid contributions capped at £1,500.','The base','A24A','11')
add('IND-11','Approved ABS/GIBS health premiums and covered persons; £5,395/£3,000 caps, deduction not tax credit, reduction of otherwise eligible deduction by non-resident months. Examples £6,000 to £5,395, £3,000 to £2,250 and £2,400 to £1,800.','The base','A20A A20B A6A A6B A29','14 15 17')
add('IND-12','Gross assessable income at most £11,450 exempt; four specific taper ranges, exact L/T0 amounts and 0.2 formula, no gap extrapolation. £17,601 gives £44.40; £17,822 gives £0.20. Fractional-pound treatment unresolved.','The base','A16E','19 20 21 22')
add('IND-13','High-income taper over £99,999 to £103,333; £1,000 minus 0.3 times excess over £100,000; £101,000 gives £700; implementation tables distinct.','The base','A16F','24')
add('IND-14','Section 28 return due 30 November following year end, subject to exceptions; foreign-income nil-tax omission requires discretionary Commissioner confirmation. Example 30 November 2027 derived, not universal.','Deadlines and filing','T28 T74Y','27')
add('IND-15','Individual payments on account: each 50% of previous relevant liability, property/trade heads and PAYE-first ordering. Instalments 31 January and 30 June, return set-off; example 2027 dates derived.','Deadlines and filing','T39 TS1 T74Y','28 29')
add('IND-16','General November payment rule and self-employed published balance-with-return explanation. £6,000 prior relevant tax gives two £3,000 payments; £7,500 final gives £1,500 balance or £5,000 final gives £1,000 excess. No other credits/offsets assumed.','Deadlines and filing','T39 SEpay','29 31')
add('IND-17','Claimed reduction needs Commissioner decision; shortfall retains original due date for surcharge.','Deadlines and filing','T39reduce','30')
add('IND-18','Old self-employed allowance table expressly 2021/2022 and 2022/23; current public service listing does not prove future 2026/27 authenticated fields. Delivery, payment and employer remittance distinct.','Deadlines and filing','SEold Eroute','33')
add('IND-19','Approved/statutory pension specified ages/categories; 0% only for qualifying pension, other chargeable income assessed separately after applicable apportioned allowances.','The base','A3A','34 35')
add('IND-20','Imported pension source, approval, taxable component at 2.5%; section-specific EU definition means UK. Irrevocable 30% commutation (Commissioner variation), age-55, ill-health and onward-transfer conditions. Synthetic £20,000 component gives £500 versus different qualifying 0% pension gives zero.','The base','T14A A3A','36 37 45')
add('IND-21','Separate s14B 2.5% approved/conforming fund route and statutory-instrument definition under UK IHTA s271A; not actual fund approval or inheritance-tax conclusion.','The base','T14B HMidentify Q4','38')
add('IND-22','Official revised SI 2010/51 XML dated 2020-12-31 in root RestrictStartDate and same SHA as earlier research. HMRC identifies instrument; as-made PDF not treated as current.','The base','HMidentify Q3 Qxml','39')
add('IND-23','QNUPS ordinary route requires both tax recognition and regulation 6; international-organisation route has statutory organisation/service and regulation 7 tests.','The base','Q4','40')
add('IND-24','Both primary conditions plus A or B, pension-tax-relief alternatives, approval/recognition/registration, no-system residence/70% lifetime-income/benefit-timing requirements.','The base','Q5','42')
add('IND-25','Occupational/non-occupational regulatory routes; no-body exception only where absence is sole reason, specified geography or 70% and benefit timing; not failure to obtain existing registration.','The base','Q6','42 43')
add('IND-26','Schedule specifies Australian complying superannuation plan; international-organisation route has its own 70% and pension-rule-1 timing tests. Relevant scheme funds and pension rule 1 are defined, not all portfolio assets or Gibraltar age 55.','The base','QSchedule Q7 Q2 Q5 Q6','43 44')
add('IND-27','Executor succeeds pre-death income rights/duties/liabilities, estate debt; provision does not classify post-death estate income.','The base','T47','48')
add('IND-28','Pre-death-income assessment limit is end of third assessment year following death-year. Death 15 October 2026 gives 30 June 2030, not an anniversary or universal return extension.','The base','T47 T74Y','49 50')
add('IND-29','Death reduction limited to rules 6–19, complete calendar months before assessment-year end. Assumed £6,000 and eight months gives £4,000 reduction/£2,000 left; June has zero complete months.','The base','T47','51 52')
add('IND-30','Section 28 late-return penalties £50 then £300 at three months and £500 at six months: cumulative £850; reasonable excuse throughout default permits discretionary relief.','Penalties and interest','T65 T65relief','55')
add('IND-31','Unpaid-tax surcharge 10% next day, further 20% of unpaid tax and first surcharge at statutory 90-day point. £1,000 wholly unpaid gives £100 plus £220, total £1,320.','Penalties and interest','T64','56')
add('IND-32','Non-resident 17% first £16,000 / 39% remainder, GIBS and express exclusions; pension rule 24 is not general frontier-worker relief.','Cross-border points','R3 A24','58')
add('IND-33','Non-resident Gibraltar pensioner relief rules 6–21 as resident, limited by hypothetical worldwide tax times chargeable/worldwide income with foreign credits ignored; no new charge on exempt foreign income. Assumed 50,000/20,000/10,000 gives floor 4,000 and restriction 1,000 from 3,000; 5,000 unaffected.','Cross-border points','A24','60 61 62')
add('IND-34','Prescribed claim form/manner and particulars/proof; case evidence and separate foreign-credit analysis required, no actual claim inferred.','Cross-border points','A29','64')
add('IND-35','Two main examples retain explicit full-year/election/eligibility and different-base assumptions; original marginal arithmetic and £888 top-up recompute.','Two worked examples that recompute','R2 R3A A6 A16C A6A A6B','65 67')
add('IND-36','Spouse/partner £3,455; actual qualifying maintenance, court/agreement cap, complete-month wording and separate-claim restrictions.','The base','A7 A20 A6A A6B',new='| Spouse/civil partner, rule 7 |')
add('IND-37','Disabled individual £10,000 each, unmarried/co-resident parent, Director confirmation notwithstanding five-year residency; no 8/9 double claim, Commissioner allocation and preserved 1999 provision.','The base','A7A A6A A6B',new='| Disabled individual, rule 7A |')
add('IND-38','First-child £1,190, age/education/articles alternatives, birth/step/adoption month reduction, qualifying maintenance cap. Rule 14 own-income exceptions, no 8/9 duplication, nonresident-child restriction, allocation and medical/education consultation.','The base','A8 A14 A20 A6A A6B',new='| Child, rule 8 |')
add('IND-39','Child abroad £1,375 each, age 16 at start, qualifying foreign education/training, ordinarily resident claimant, no similar foreign relief; child rule 14 restrictions.','The base','A9 A14 A6A A6B',new='| Child educated abroad, rule 9 |')
add('IND-40','£5,800 custody/maintenance deduction and joint-custody half, legal separation and father rule7(b)/(c) exclusions, death reduction transferred to survivor, monthly residence qualification. Synthetic half £2,900.','The base','A12 A13 A20 A6A A6B',new='| Parent with custody and maintenance, rule 12 |')
add('IND-41','Qualified independent nursery actual fees capped at £5,480 per child; residence, registration, access, comparability and market-value conditions. £6,000 assumed eligible fees gives £5,480.','The base','A14A A6A A6B',new='| Nursery, rule 14A |')
add('IND-42','Apprentice £380 with complete-month residence reduction, specified approved written contract and reciprocal training.','The base','A15 A6A A6B',new='| Apprentice, rule 15 |')
add('IND-43','Blind claimant or spouse/partner £5,475, medical certificate and rule20 residence reductions.','The base','A17 A20 A6A A6B',new='| Blind person, rule 17 |')
add('IND-44','Dependent-relative incapacity/widowed-mother tests, total income at most £3,455, £250 or resident £400 reduced by excess over £3,090, two-person cap/joint contribution allocation/months. Printed negative-result anomaly unresolved. £3,200 gives £110 reduction and £140/£290 before other reductions.','The base','A18 A20 A6A A6B',new='Rule 18 concerns a relative')
add('IND-45','Senior male65/female60 conditions, printed £12,645 less both named £3,455 amounts, complete nonresident months; revoked rule25 and unmarried/mixed-system treatment not silently repaired.','The base','A16A A6A A6B A25',new='Rule 16A specifies a senior-citizen')
add('IND-46','Earned-income age60 credit up to £4,000/tax liability; all £6,000 pension/annuity and 25%-capital Commissioner-opinion exclusions; no GIBS, monthly age/residence and prescribed claim.','The base','A16D A25',new='Rule 16D is a separate tax credit')
add('IND-47','Rule21 own/spouse life, specified approved fund contributions and preserved former Fund entitlement; exclusions, no duplication, 1/6 total/1/7 component/7% death-capital ceilings, months and spouse restrictions.','The base','A21 A6A A6B',new='For ABS, rule 21 covers')
add('IND-48','Approved personal pension/annuity actual contributions capped at lesser 20% earned income or £35,000; employment providing pension excluded, prescribed claim; not GIBS. Assumed 50,000/12,000 gives 10,000; GIBS24A remains1,500.','The base','A21A A6A A24A',new='Rule 21A separately allows')
add('IND-49','Mortgage actual qualifying interest/use/cost/licensed lender, £350,000 aggregate principal not interest, pre2008 transition, own/spouse/50:50 and £1,500 GIBS ceiling.','The base','A22 A6B',new='Rule 22 permits qualifying interest')
add('IND-50','Mortgage disposal/use/child/parking conditions; 12month first-claim/occupation and replacement use, 30day recapture date, 3year garage disposal, 12month use, no motorcycle; old s74 not converted to current clock.','The base','A22',new='Keep the disposal and use conditions')
add('IND-51','PostJuly2019 ordinary £13,000 aggregate home/child entitlement with acquisition/payment/cost/Crown exclusions, special certificate, prior2001 adjustment, ownership and election, policy-proceeds exclusion, carryover and discretionary provisional refund.','The base','H2 H2A H3 H4 H5',new='The Home Purchase (Deductions) Rules give')
add('IND-52','GIBS £7,500 postJuly2019 limit with conditions, spouse grandfathering/half relief, 12month legal-estate disposal/occupation forfeiture and death exceptions; old s74 no invented clock.','The base','H8 H6',new='For a current eligible GIBS claimant')
add('IND-53','Special £4,000 total/£1,000 annual, ordinary rule2 entitlement, payment/repeat/ownership/partner limits; printed historic10,000/11,500 tests do not establish current13,000 eligibility; GIBS exclusion/spouse exceptions.','The base','P2 P3 P4',new='The separate Home Purchase (Special Deduction) Rules specify')
add('IND-54','Published mortgage/home application documents and yearly lender interest letter; plain-language page not substituted for statutory conditions.','The base','Nhome',new='For administration, the current Income Tax Office')
add('IND-55','Gym/PT credit lesser10% eligible Gibraltar cost or own liability; PT registered/compliant, full evidence, no transfer/carryforward. Assumed900/50 gives50.','The base','T19A',new='Schedule 3 paragraph 19A permits')
add('IND-56','Private Gibraltar primary/secondary tuition credit lesser10% or liability; defined child, no nursery, full evidence, no transfer/carryforward. Separate assumed8,000/900 gives800; credit stacking not inferred.','The base','T19B',new='Paragraph 19B applies the same')
add('IND-57','Published separate return/payment/representation services, account/identity/tax registration and taxpayer-reference link. Public entry not authenticated future-year release or successful submission/payment.','Deadlines and filing','Eroute',new='The current government Tax eServices page lists')
add('IND-58','Permanent/indefinite departure FAQ: final-assessment form plus last-employer P7A Part1 to paye.leavinggib@gibraltar.gov.gi; not tax clearance, exemption or new deadline.','Deadlines and filing','Nleave',new='For an employee leaving Gibraltar permanently')
add('IND-59','Current allowance index names 23March2026; amendment table in same PDF includes LN2026/054 commencement23March2026. Publication26March not a missing consolidation inferred.','Sources','AIcurrent Aversions',new='Earlier reads and completed review scopes remain recorded')
proof('ITOinterim','ITO','Current ITO maintenance and interim editable-PDF notice',r'^IMPORTANT NOTICE:',r'^PDF Tax Return')
proof('IT1p1','IT1','Current IT1 first page: taxpayer types, period labels, email routing and ID/authority',r'^Form IT1',r'^INCOME & OUTGOINGS')
proof('ITGnotice','ITG','Current return guidance opening maintenance/interim notice',r'^Dear Taxpayer,',r'^Key areas')
proof('ITGyear','ITG','Current return guidance income year and elections',r'^What is my tax return',r'^How do I submit my tax return',last=True)
proof('ITGemail','ITG','Return guidance page10 email, photo-ID and attachment instructions',r'^How do I submit my tax return by email\?',r'^How do I submit a previous year',last=True)
proof('ITGagent','ITG','Return guidance email authority and representative name/capacity',r'^If you are submitting a tax return by email on behalf',r'^Return to list',last=True)
add('IND-60','Current maintenance notice overrides inference from public portal listing; 2026 IT1 actual income/election years and receipt deadline; category email, ID, authority and attachment requirements. No future-year form or actual receipt inferred.','Deadlines and filing','ITOinterim IT1p1 ITGnotice ITGyear ITGemail ITGagent',new='As read on 28 October 2026, the ITO main page')
# Exact original paragraph evidence is held once and mapped to actual destinations.
current=G.read_text();archive=(K/'preserved-individual-controls.md').read_text()
def paras(t):
 body=t.split('---',2)[2].split('<!-- openaccountants-cta-block -->')[0];head='Title';out=[]
 for p in re.split(r'\n\s*\n',body.strip()):
  if p.startswith('#'):head=p.lstrip('#').strip();continue
  out.append((head,p))
 return out
cur=paras(current);maps=[]
for x in old:
 matches=[(h,p) for h,p in cur if p==x['text']]
 if matches:dest='Guide: '+matches[0][0];target=x['text'];disposition='Full original paragraph byte-exact'
 elif x['text'] in archive:dest='preserved-individual-controls.md';target=x['text'];disposition='Full original executable block byte-exact in supplement'
 else:
  changed={9:'**Partial-year limitation:**',10:'First establish assessable income under the charging provisions.',33:'The authenticated 2026/27 return fields/release'}
  i=int(x['id'][-3:]);assert i in changed,(x['id'],x['text'][:100]);matches=[(h,p) for h,p in cur if p.startswith(changed[i])];assert len(matches)==1
  dest='Guide: '+matches[0][0];target=matches[0][1];disposition={9:'All operative limitations preserved; old-reference subject and conditional continuity evidence added.',10:'Core method retained; old incomplete-schedule caveat narrowed to named outstanding instruments/drafting questions.',33:'Untested future-year form and special cases retained; public routes verified separately, old allowance-table caution retained.'}[i]
 maps.append({**{k:v for k,v in x.items() if k!='text'},'destination':dest,'current_sha256':sha(target),'disposition':disposition,'paragraph_exact':x['text']==target,'actual_old_anchor':norm(x['text'])[:180]})
nonrule=[1,3,5,41,47,54,57,59,69,70,71,72,73]
executable=[18,23,32,46,53,63,66,68]
covered={i for r in rows for i in r['original_paragraph_ids']}
expected={x['id'] for x in old}-{f'IND-P{i:03}' for i in nonrule+executable}
assert covered==expected,(sorted(expected-covered),sorted(covered-expected))
for r in rows:
 assert all(p in proofs for p in r['proof_ids'])
 if r['new_anchor']:assert r['new_anchor'] in current,r['id']
 assert r['guide_section'] in current
result={'read_on':'2026-10-28','guide_version':'0.10','status':'Full individual writer ledger; independent country review pending','rows':rows,'source_proofs':list(proofs.values()),'old_paragraph_map':maps,'original_nonrule_paragraph_ids':[f'IND-P{i:03}' for i in nonrule],'original_executable_paragraph_ids':[f'IND-P{i:03}' for i in executable],'guide_sha256':sha(current),'before_sha256':sha((K/'gi-individual-income-tax.before.txt').read_text()),'original_qnups_xml_sha256':'bd6472b4eb7741dc1b5a83bdf82229084f4236bdb7ba3ce0895d8ec1e1da90f3','new_independent_acceptance':False,'published':False,'country_complete':False}
(K/'ledger.json').write_text(json.dumps(result,indent=2)+'\n')
esc=lambda t:t.replace('|','\\|').replace('\n',' ')
md=['# Gibraltar individual income tax: full figure/rule ledger\n','Writer source checks on 28 October 2026. Guide v0.10 is **unreviewed new country material**. Prior reviews remain preserved at their exact scope; no accountant attestation or country completion is claimed. English is the original language of these sources. Quotes below are exact after whitespace/layout-header normalization, each at most 45 words, and matched only against its own named source. Derived examples use explicit synthetic inputs; the law supplies the formula, not those inputs.\n','## Rule inventory\n','Each row links the full exact source-quote proof and names the current section and old paragraph IDs. Every proof includes the act/article, official URL and actual read date. Multiple citations preserve interacting restrictions rather than using a single keyword to stand for an entire rule.\n','| ID | Current section; rule/figure and qualifications | Exact original-language quote and complete provision evidence | Original paragraphs / new anchor | Read date |','|---|---|---|---|---|']
for r in rows:
 refs=[]
 for k in r['proof_ids']:
  p=proofs[k];refs.append(f'[{k}](#proof-{k.lower()}): {p["provision"]}; [official source]({p["url"]}); “{p["quotes"][0]}”')
 md.append('| '+' | '.join(map(esc,[r['id'],r['guide_section']+': '+r['rule'],'; '.join(refs),' '.join(r['original_paragraph_ids'])+(' / '+r['new_anchor'] if r['new_anchor'] else ''),r['read_on']]))+' |')
md+=['\n## Exact quotation proofs\n','Quoted provisions include their operative conditions and exceptions. An old statutory reference is evidence of what is printed, not proof of an inferred modern renumbering. Statutory drafting questions remain partial in the Guide.\n']
for p in proofs.values():
 md.append(f'### Proof {p["id"]}\n\n{p["provision"]}. [Official source]({p["url"]}). Read {p["read_on"]}.\n')
 for q in p['quotes']:md.append('> '+q+'\n')
md+=['## Complete old-topic destination table\n','The original 73 paragraph records, full text and SHA-256 values are in [original-paragraphs.json](../original-paragraphs.json); this map is computed from actual current paragraph matches. Full legal/prose content is retained, with three explicitly reconciled paragraphs. All eight original executable controls remain byte-exact across the Guide and supplement.\n','| Original ID | Original section | Actual content anchor | Current destination and preservation |','|---|---|---|---|']
for m in maps:md.append('| '+' | '.join(esc(x) for x in [m['id'],m['heading'],m['actual_old_anchor'],m['destination']+'; '+m['disposition']])+' |')
md+=['\n## Nonrule and executable accounting\n','Nonrule records (intake, retained exclusions, source/read-scope notes, records recommendations, review status, disclaimer and byline): '+', '.join(result['original_nonrule_paragraph_ids'])+'. These are preserved rather than recharacterised as legal authority.\n','Original executable records: '+', '.join(result['original_executable_paragraph_ids'])+'. The six supplementary blocks moved exactly to [preserved-individual-controls.md](../preserved-individual-controls.md); the two main blocks stay in the Guide. Four new separate calculation scenarios are in [ordinary-deduction-controls.md](../ordinary-deduction-controls.md).\n','## Source-version and procedure limits\n','The revised UK XML is byte-exact to the earlier 22 October source receipt, SHA-256 `bd6472b4eb7741dc1b5a83bdf82229084f4236bdb7ba3ce0895d8ec1e1da90f3`, and its root has `RestrictStartDate="2020-12-31"`. No fresh UK age, transfer or inheritance-tax conclusion is inferred. The current allowance index and consolidation include LN2026/054; the printed commencement date is 23 March, notwithstanding 26 March publication. Only specified provisions were read, not the entire 297-page Act. The source receipt lists actual read scopes and file hashes.\n','The public portal verifies that services are published; the current ITO maintenance/interim PDF notice controls the supported ordinary 2026 filing route. Neither source proves authenticated 2026/27 form release, operational receipt, payment acceptance or a case-specific approval. No form, payment or email was submitted. Current Guide limits include part-year cross-reference eligibility, the printed senior/dependant/old-assessment references, the special-home historical tests, separate property/energy instruments, social-insurance deduction authority and credit interactions.\n']
(K/'ledgers/gi-individual-income-tax.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'rows':len(rows),'proofs':len(proofs),'short_quotes':sum(len(p['quotes']) for p in proofs.values()),'old_paragraphs':len(maps),'unchanged_old_paragraphs':sum(m['paragraph_exact'] for m in maps),'inherited_rule_paragraphs':len(expected)}))
