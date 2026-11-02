from pathlib import Path
import re,json,hashlib
import yaml
R=Path(__file__).resolve().parents[4];E=R/'evidence/research/gibraltar-2026/legacy-standard-repair-2026-10-31';B=E/'before';B.mkdir(exist_ok=True)
ita='https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf';ubo='https://www.gibraltarlaws.gov.gi/uploads/legislations/proceeds-of-crime/2017s122/2017s122(15-07-26).pdf';companies='https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf';rates='https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf';stamp='https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf';uk='https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force';spain='https://assets.publishing.service.gov.uk/media/6705890ee84ae1fd8592f017/TS_78.2024_UK_Spain_Agreement_Taxation_Financial_Interests_Gibraltar.pdf'
H=['Who this applies to','Rates, bands and thresholds','The base','Deadlines and filing','Penalties and interest','Cross-border points','Two worked examples that recompute','Ask the client first','Sources']
plans={
'gi-company-formation':{
'Who this applies to':['Scope and legal basis'],
'The base':['Subscribers and constitution','Office, director and secretary','Beneficial-ownership reporting after incorporation'],
'Deadlines and filing':['Assemble the application','Compliance declaration and fees','Completion and handover'],
'Penalties and interest':[], 'Cross-border points':[], 'Ask the client first':[], 'Sources':[]},
'gi-income-tax-assessment-appeals':{
'Who this applies to':['Scope and first checks'],
'The base':['Enquiries and assessment limits are different clocks','Information notices: response and appeal','Tax provision during liquidation'],
'Deadlines and filing':['Establish service before calculating the appeal period','Written appeal and grounds','Payment postponement requires a separate application','Tribunal handling and outcome','Supreme Court: case stated on a point of law','Overpayment claims: a separate six-year period'],
'Penalties and interest':[], 'Cross-border points':['Non-residents and statutory representatives','Treaty MAP: a separate submission and collection decision'], 'Ask the client first':[], 'Sources':['Sources']},
'gi-property-stamp-duty':{
'Who this applies to':['Unresolved amendment status'], 'Rates, bands and thresholds':['Statutory calculation'],
'The base':['Qualifying first- and second-time buyers','Specified affordable-housing transactions','Principal mortgage security'],
'Deadlines and filing':['Stamping, responsibility and late instruments','Challenging a stamp-duty assessment'],
'Penalties and interest':[], 'Cross-border points':[], 'Two worked examples that recompute':['Worked boundary checks'], 'Ask the client first':['Working-paper evidence'], 'Sources':['Scope remaining']},
'gi-residential-property-disposals':{
'Who this applies to':['Who this applies to'], 'Rates, bands and thresholds':['Thresholds and scope'], 'The base':['The base and exclusions'],'Deadlines and filing':['Deadlines and filing'],'Penalties and interest':['Penalties and interest'],'Cross-border points':['Cross-border points'],'Two worked examples that recompute':['Two worked examples that recompute'],'Ask the client first':['Ask the client first'],'Sources':['Sources and limits','Disclaimer']},
'gi-spain-tax-residence':{
'Who this applies to':['Agreement, territory and dates'],'The base':['Individuals: domestic residence first','Entities: four independent Spanish-residence triggers'],'Deadlines and filing':[], 'Penalties and interest':[], 'Cross-border points':['Relief, information exchange and disputes'],'Two worked examples that recompute':['Conditional worked checks'],'Ask the client first':['Evidence, open work and output'],'Sources':['Disclaimer']},
'gi-training-planning-and-startup-reliefs':{
'Who this applies to':['Scope'],'The base':['Approved qualifying training',"Architects' fees and planning costs",'Historic start-up credit: entry window closed'],'Deadlines and filing':['Claim preparation and remaining verification'],'Penalties and interest':[],'Cross-border points':[],'Ask the client first':[],'Sources':[]},
'gi-uk-employment-pensions-treaty':{
'Who this applies to':['Establish residence, period and income type'],'The base':['Ordinary employment and all three short-stay conditions','Directors, performers and transport crew','Government service and the Regiment exception','Pensions: source taxation and a conflicting summary','Offshore employment has a separate rule','Student and apprentice maintenance','Double-tax relief: Gibraltar-resident example'],'Deadlines and filing':['Filing workflow and unresolved operations'],'Penalties and interest':[],'Cross-border points':[],'Ask the client first':[],'Sources':['Sources']},
'gi-uk-investment-income-treaty':{
'Who this applies to':['Scope and effective periods','Establish entitlement before using a rate'],'The base':['Dividends: ordinary exemption and property distributions','Interest: recipient or payer qualification is essential','Royalties: a different eligibility list','Source, permanent establishments and related parties','Capital gains: classify the disposed asset before allocating tax'],'Deadlines and filing':['Company UK-interest relief: published application evidence','Relief file and remaining verification'],'Penalties and interest':[],'Cross-border points':['Anti-abuse and dispute procedure'],'Two worked examples that recompute':['Worked examples and boundary checks'],'Ask the client first':[],'Sources':['Sources']}}
rate_rows={
'gi-company-formation': [('Ownership indication','25% plus one share or more than25%; other control/fallback tests remain required',ubo+'#regulation-3'),('Civil penalty ceiling','Up to£10,000 only for the specified failures/persons, safeguards and appeals below',ubo+'#regulation-42')],
'gi-income-tax-assessment-appeals':[('Ordinary assessment appeal','28days from service of the assessment notice; service, written grounds and late-permission conditions below',ita+'#section-35'),('Postponement application','Separate written application within28days of service; eligibility and discretion below',ita+'#section-36'),('Overpayment claim','Sixyears from relevant assessment-year/accounting-period end; proof and finality limits below',ita+'#section-61')],
'gi-spain-tax-residence':[('Dual-resident individual overnight limb','More than183 Spanish nights; defined sporadic absences and alternative family/home/asset tests below',spain),('Entity historical exception','Only specified pre16November2018 entities meeting all cumulative historical conditions below; not a new2026 election',spain)],
'gi-training-planning-and-startup-reliefs':[('Current qualifying training','Additional50% deduction with Commissioner-approved training and ordinary deduction conditions below',ita+'#schedule-3-paragraph-16'),('Historical training enhancement','Additional60% only for periods ending1July2021–30June2023',ita+'#schedule-3-paragraph-16'),('Planning credit','Up to100% eligible fees, total£5,000, own-property application made within24months of trade start and approved under the Town Planning Act, first3years and period-tax cap below',ita+'#schedule-3-paragraph-17'),('Historical startup credit','Only qualifying2016/17entry window below; no fresh2026entry',ita+'#schedule-3-paragraph-17A')],
'gi-uk-employment-pensions-treaty':[('Ordinary employment short stay','At most183days in every relevant12month window AND non-host-resident employer AND cost not borne by hostPE',uk+'#article-14-income-from-employment'),('Gibraltar same-income credit','Lesser of Gibraltar and UK tax on same income, subject toArticle22(3) exclusion',uk+'#article-22-elimination-of-double-taxation'),('Offshore enterprise threshold','30days underArticle21(4) is an enterprisePE test, not employee income-tax exemption',uk+'#article-21-miscellaneous-rules-applicable-to-certain-offshore-activities')],
'gi-uk-investment-income-treaty':[('Ordinary dividend source exemption','Other-territory beneficial-owner residence; property-vehicle andPE exceptions below',uk+'#article-10-dividends'),('Property investment vehicle dividend','15% gross ceiling only underArticle10(2)(b) conditions; qualifying other-territory pension scheme remains exempt',uk+'#article-10-dividends'),('Interest/royalty ownership route, Articles 11(2)–(3) and 12(2)–(3)','Less than25% non-resident shares/other rights; all other residence, beneficial-owner, recipient and anti-abuse conditions below',uk+'#article-11-interest')]}
asks={
'gi-company-formation':['Which private-company form, name and articles are proposed, and which service/filing options are selected?','What shares, rights, authorised/subscribed nominal amounts and paid/unpaid allocations are proposed?','Who are the subscribers, officers, appointors, nominees and ultimate owners/controllers, with what evidence?','What registered office, signature authority, approvals and trigger dates apply?','Which incorporation, officer and Registrar submissions/receipts are already complete?'],
'gi-income-tax-assessment-appeals':['Who is assessed, for which period, and what proves statutory service/notification?','Which profits or gains and amount are disputed, and what supports the written grounds?','What returns, appeal, postponement decisions and actual payments exist, with issue/service dates?','Is the issue a domestic appeal, agency declaration, overpayment claim, point of law or treatyMAP?','Which directions, deadlines, prior decisions and receipt evidence govern this case?'],
'gi-training-planning-and-startup-reliefs':['Which qualifying person and expenditure are involved, and what was already deducted in accounting profit?','What Commissioner training approval or planning approval exists?','Who owns the property, when did trading start and when was the planning application approved?','Which period tax liability and earlier credits constrain the amount usable?','Is this a current claim or a historical window, and what claim/submission evidence exists?'],
'gi-uk-employment-pensions-treaty':['Which domestic/treaty residence and exact assessment periods apply?','What kind of income, source, duty location and relevant12month travel windows are evidenced?','Who employs/pays, where are they resident, and who bears the cost through anyPE?','What pension scheme/source documents and same-income tax liabilities exist?','Which payroll authorisations, claims, payments, appeals and special-status decisions already exist?'],
'gi-uk-investment-income-treaty':['Who is the actual beneficial owner and treaty resident, including any transparent-entity treatment?','Which income/asset category, source, ownership rights andPE connections apply?','What qualifies the recipient/payer, property vehicle, pension scheme or recognised exchange?','What domestic charge, independent-party amount and anti-abuse/remittance facts are evidenced?','Which certified forms, authority determinations, payments, claims and deadlines already exist?']}
boundaries={
'gi-company-formation':'Special-name approvals, alternative entities/sector permissions, historical nominee/appointor cases, section12 cross-reference and live submission/authority receipts remain unresolved. Current source/editorial review of this structural continuation and professional attestation remain separate.',
'gi-income-tax-assessment-appeals':'Current domestic submission channels, disputed service, exact calendar/court procedures, actual directions, refund handling and interest rates, liquidation successor cross-reference and treaty arbitration operation remain unresolved.',
'gi-property-stamp-duty':'BillB05/2025 enactment/commencement; full relief/estate prescriptions, leases/gifts/indirect property/security categories, actual electronic certificate/payment, later interest notices, court procedure and case-specific liabilities remain unresolved.',
'gi-residential-property-disposals':'Acquisition/base/loss/share attribution, historical aggregation/commencement, later exemption orders, exact return fields and treaty/non-resident methods remain incomplete.',
'gi-spain-tax-residence':'FAQ/treaty timing conflict, complete Spanish domestic definitions/valuation/filing and relief, historical entity list, exception eligibility and current referral/claim channels remain unresolved.',
'gi-training-planning-and-startup-reliefs':'Current approval/claim channels, unusual timing/cost allocation and other incentives remain outside the verified method. No historical entry window is reopened.',
'gi-uk-employment-pensions-treaty':'Domestic procedures/authorisations, day counting, employer/recharge and pension-source disputes, special statuses, DT8152 conflict and Gibraltar social-security certificate/benefit coordination remain unresolved.',
'gi-uk-investment-income-treaty':'Other relief/repayment procedures and claim deadlines, disputed entitlement/anti-abuse, treaty capital-gain allocation cases and arbitration operating arrangements remain unresolved.'}
# Meaningful executable controls mirror existing prose scenarios and preserve all stated eligibility limits.
newblocks={
'gi-company-formation':'''### Capital reconciliation control

The authorised/subscribed-capital scenario already stated in the application method has this arithmetic control. It does not prescribe minimum capital or deem unissued shares issued.

```oa-check
name: Gibraltar formation authorised and subscribed capital reconciliation
inputs:
  authorised_shares: 1000
  nominal_per_share: 1
  first_subscriber_shares: 100
  second_subscriber_shares: 100
steps:
  - authorised_nominal: authorised_shares * nominal_per_share
  - subscribed_shares: first_subscriber_shares + second_subscriber_shares
  - subscribed_nominal: subscribed_shares * nominal_per_share
  - authorised_not_subscribed: authorised_shares - subscribed_shares
expected:
  authorised_nominal: 1000
  subscribed_shares: 200
  subscribed_nominal: 200
  authorised_not_subscribed: 800
```

### Ownership-indication boundary control

The25/26-share scenario already stated in the ownership method compares the numerical ownership indication only. Other control facts and the complete investigation remain required in both cases.

```oa-check
name: Gibraltar company ownership indication share boundary
inputs:
  equal_shares: 100
  smaller_holding: 25
  larger_holding: 26
steps:
  - smaller_percent: smaller_holding / equal_shares * 100
  - larger_percent: larger_holding / equal_shares * 100
  - indicative_share_count: equal_shares * 0.25 + 1
expected:
  smaller_percent: 25
  larger_percent: 26
  indicative_share_count: 26
```
''',
'gi-income-tax-assessment-appeals':'''### Postponement scope control

The£20,000 assessment/£12,000 accepted-position example in the postponement method yields the disputed amount below. This is the maximum amount identified for that hypothetical application, not an approval, payment suspension or recalculation of the assessed liability.

```oa-check
name: Gibraltar assessment disputed amount for separate postponement application
inputs:
  assessed_tax: 20000
  accepted_position_tax: 12000
steps:
  - disputed_amount: assessed_tax - accepted_position_tax
  - not_disputed: assessed_tax - disputed_amount
expected:
  disputed_amount: 8000
  not_disputed: 12000
```
''',
'gi-training-planning-and-startup-reliefs':'''### Qualifying training control

This executes the£2,000 current-period training scenario in the method. The approval and ordinary deduction conditions remain necessary; the additional adjustment avoids deducting the accounting expense twice.

```oa-check
name: Gibraltar approved training additional deduction and accounting adjustment
inputs:
  eligible_training_cost: 2000
  additional_deduction_rate: 0.50
steps:
  - ordinary_deduction: eligible_training_cost
  - additional_tax_adjustment: eligible_training_cost * additional_deduction_rate
  - total_deduction: ordinary_deduction + additional_tax_adjustment
expected:
  ordinary_deduction: 2000
  additional_tax_adjustment: 1000
  total_deduction: 3000
```

### Planning-credit limit control

This executes the£6,200 qualifying-cost/£3,000 period-tax scenario in the method, comparing the aggregate cap and the period-tax cap. The resulting unused potential does not establish a refund or carry-forward right.

```oa-check
name: Gibraltar planning credit aggregate and period tax limits
inputs:
  qualifying_cost: 6200
  aggregate_credit_limit: 5000
  tax_for_eligible_period: 3000
steps:
  - potential_credit: min(qualifying_cost, aggregate_credit_limit)
  - usable_this_period: min(potential_credit, tax_for_eligible_period)
  - unused_potential_not_automatic_relief: potential_credit - usable_this_period
expected:
  potential_credit: 5000
  usable_this_period: 3000
  unused_potential_not_automatic_relief: 2000
```
'''}
def readable(t):
 replacements={"more than25%":"more than 25%","Up to£":"Up to £","Up to100%":"Up to 100%","28days":"28 days","within28":"within 28","Sixyears":"Six years","More than183":"More than 183","pre16November2018":"pre-16 November 2018","new2026":"new 2026","Additional50%":"Additional 50%","Additional60%":"Additional 60%","ending1July2021–30June2023":"ending 1 July 2021–30 June 2023","total£":"total £","within24months":"within 24 months","first3years":"first 3 years","qualifying2016/17entry":"qualifying 2016/17 entry","fresh2026entry":"fresh 2026 entry","At most183days":"At most 183 days","relevant12month":"relevant 12-month","hostPE":"host PE","toArticle22(3)":"to Article 22(3)","30days":"30 days","underArticle21(4)":"under Article 21(4)","enterprisePE":"enterprise PE","underArticle10(2)(b)":"under Article 10(2)(b)","Less than25%":"Less than 25%","BillB05/2025":"Bill B05/2025","section12":"section 12","31October":"31 October","The25/26":"The 25/26","The£":"The £","the£":"the £","treatyMAP":"treaty MAP","anyPE":"any PE"}
 for a,b in replacements.items():t=t.replace(a,b)
 return t
for slug,rows in rate_rows.items():
 rate_rows[slug]=[(readable(a),readable(b),u.split('#')[0] if '.pdf#' in u else u) for a,b,u in rows]
for slug,ls in asks.items():asks[slug]=[readable(x) for x in ls]
for slug,t in boundaries.items():boundaries[slug]=readable(t)
for slug,t in newblocks.items():newblocks[slug]=readable(t)
rate_rows['gi-company-formation'][0]=('Ownership indication, UBO regulation 3(2)',)+rate_rows['gi-company-formation'][0][1:]
rate_rows['gi-company-formation'][1]=('Civil penalty ceiling, UBO regulation 42',)+rate_rows['gi-company-formation'][1][1:]
for i,loc in enumerate(['ITA section 35','ITA section 36','ITA section 61']):
 a,b,u=rate_rows['gi-income-tax-assessment-appeals'][i];rate_rows['gi-income-tax-assessment-appeals'][i]=(a+', '+loc,b,u)
for i,loc in enumerate(['Schedule 3 paragraph 16','Schedule 3 paragraph 16(2A)','Schedule 3 paragraph 17','Schedule 3 paragraph 17A']):
 a,b,u=rate_rows['gi-training-planning-and-startup-reliefs'][i];rate_rows['gi-training-planning-and-startup-reliefs'][i]=(a+', '+loc,b,u)
for i,loc in enumerate(['Article 2(1)(b)','Article 2(2)(b)']):
 a,b,u=rate_rows['gi-spain-tax-residence'][i];rate_rows['gi-spain-tax-residence'][i]=(a+', '+loc,b,u)

description_additions={
'gi-company-formation':'Use for 2026 private-company incorporation preparation, capital allocation and beneficial-owner evidence gathering.',
'gi-property-stamp-duty':'Use for 2026 transaction classification and conditional calculations; do not certify liability until the stated amendment-status and filing gaps are resolved.',
'gi-residential-property-disposals':'Use for 2026 disposal screening and taxpayer evidence collection before a separate computation, return or payment decision.',
'gi-training-planning-and-startup-reliefs':'Use for 2026 employer and self-employed working papers.'}
notice="> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction."
# Save before snapshots once, so repeated local repair never uses a partially transformed file.
for slug in plans:
 p=R/'skills/gibraltar'/(slug+'.md');q=B/(slug+'.md')
 if not q.exists():q.write_bytes(p.read_bytes())
(E/'draft-options.md').write_text('''# Legacy-standard repair options\n\nA. Selected: reorganise all existing substantive sections into the canonical reference shape, add a source/date index from the existing provenance, attach the already-cited URL to rate rows, and make the existing formation/appeal/training examples executable. Preserve every topic, condition, qualification, control, attribution and CTA.\n\nB. Full substantive rewrite: unnecessary for these 11 validation defects and risks losing accepted research. New tax jobs and unresolved core computations stay in their own subsequent country continuation. Neither option clears country partials.\n''')
for slug,plan in plans.items():
 old=(B/(slug+'.md')).read_text();fmtext,body=old.split('---',2)[1:];fm=yaml.safe_load(fmtext)
 suffix=''
 if '<!-- openaccountants-cta-block -->' in body:
  body,suffix=body.split('<!-- openaccountants-cta-block -->',1);suffix='<!-- openaccountants-cta-block -->'+suffix
  # The attribution remains verbatim immediately before the preserved platform CTA.
  attr=re.search(r'\n> Contributed by[^\n]+\n\s*$',body)
  if attr:suffix=body[attr.start():]+suffix;body=body[:attr.start()]
 sp=re.split(r'^## (.+)\n',body,flags=re.M);intro=sp[0];sections=dict(zip(sp[1::2],sp[2::2]))
 allocated=[x for v in plan.values() for x in v];assert set(allocated)==set(sections),(slug,set(sections)-set(allocated))
 buckets={h:[] for h in H}
 for h,parts in plan.items():
  for orig in parts:
   t=sections[orig]
   # Preserve existing examples verbatim but route their prose and executable block to the examples section.
   if h!='Two worked examples that recompute':
    ex=[]
    pat=re.compile(r'([^\n]+(?:\n(?!\n)[^\n]+)*)\n\n(```oa-check\n.*?\n```)',re.S)
    def move(m):ex.append(m.group(0));return ''
    t=pat.sub(move,t)
    for x in ex:buckets['Two worked examples that recompute'].append(x)
   # Demote old thematic headings; canonical new headings are the only writer H2 set.
   t=re.sub(r'^(#{3,}) ',r'#\1 ',t,flags=re.M)
   if h=='Sources' and orig=='Sources':buckets[h].append(t)
   elif orig==h:buckets[h].append(t)
   else:buckets[h].append('### '+orig+'\n\n'+t)
 if slug in newblocks:buckets['Two worked examples that recompute'].append(newblocks[slug])
 if slug in rate_rows:
  table='| Rule | Figure and conditions | Official source |\n|---|---|---|\n'
  for a,b,u in rate_rows[slug]:table+=f'| {a} | {b} | {u} |\n'
  buckets['Rates, bands and thresholds'].insert(0,table)
 # Source every existing rates row using its already-cited immediate source, without altering the old cells.
 if slug in ['gi-property-stamp-duty','gi-residential-property-disposals']:
  content='\n'.join(buckets['Rates, bands and thresholds']);lines=[];intable=False;row=0;u=stamp if slug=='gi-property-stamp-duty' else ita
  for line in content.splitlines():
   if line.startswith('|'):
    if not intable:row=0;intable=True
    row+=1
    line+=(' Official source |' if row==1 else '---|' if row==2 else f' {u} |')
   else:intable=False
   lines.append(line)
  buckets['Rates, bands and thresholds']=['\n'.join(lines)+'\n']
 # Move existing responsive surcharge/interest discussion into its canonical section.
 if slug=='gi-income-tax-assessment-appeals':
  needle='Postponement of collection **does not change the original due date**'
  for i,t in enumerate(buckets['Deadlines and filing']):
   ps=t.split('\n\n')
   move=[p for p in ps if p.startswith(needle)]
   if move:
    buckets['Penalties and interest'].extend(move);buckets['Deadlines and filing'][i]='\n\n'.join(p for p in ps if p not in move)
 # Move an already-written penalty block to the canonical penalty section.
 if slug=='gi-company-formation':
  base='\n'.join(buckets['The base']);a=base.index('#### Discrepancy reports and enforcement');b=base.index('#### Register access and non-disclosure applications',a)
  buckets['The base']=[base[:a]+base[b:]];buckets['Penalties and interest']=[base[a:b]]
 if not buckets['Penalties and interest']:buckets['Penalties and interest']=['This Guide does not compute a separate penalty or interest amount for the stated job. Keep the domestic return/payment and dispute requirements in the linked taxpayer Guides separate from the allocation, formation or relief test. The unresolved procedural limits remain listed in Sources. This is a scope boundary, not a finding that no penalty applies.\n']
 if not buckets['Cross-border points']:buckets['Cross-border points']=['This job does not by itself determine foreign-country liability or replace a separate residence, treaty, payroll or foreign-tax-relief analysis. Preserve those conclusions separately using the linked country Guides and the facts identified below. No additional foreign exemption or claim method is established here.\n']
 if not buckets['Deadlines and filing']:buckets['Deadlines and filing']=['Keep the actual domestic filing, claim, payment and appeal dates separate from the treaty tests and authority-cooperation dates below. Current case-specific submission channels and implementation remain unconfirmed. Do not treat this Guide or a completed working paper as a submitted return, accepted claim or deadline extension.\n']
 if slug in asks:buckets['Ask the client first'].insert(0,'\n'.join(f'{i}. {x}' for i,x in enumerate(asks[slug],1))+'\n')
 # Keep old Sources text verbatim; add the dates from existing source provenance, not a fictional fresh whole-pack read.
 src='\n'.join(buckets['Sources']);meta={x['url']:str(x['as_of']) for x in fm.get('sources',[])}
 def date_list(m):
  u=m.group(2);d=meta.get(u,meta.get(u.split('#')[0]));assert d,(slug,u);return m.group(0)+'; read on '+d+'.'
 src=re.sub(r'^(- \[[^\n]+\]\((https?://[^\n]+)\))$',date_list,src,flags=re.M)
 src+='\n### Preserved source-read provenance\n\nThe dates below preserve the source reads recorded in the existing Guide. This structural repair does not claim a fresh verification of every old rule. New executable controls repeat the existing scenario assumptions; their exact responsive source excerpts and 31 October read scopes are recorded in the country repair ledger.\n\n| Source | Official URL | Recorded read date |\n|---|---|---|\n'
 for x in fm.get('sources',[]):src+=f"| {x['title']} | {x['url']} | {x['as_of']} |\n"
 src+='\nNot yet confirmed: '+boundaries[slug]+' The country remains partial; this continuation does not grant professional attestation.\n'
 buckets['Sources']=[src]
 oldv=str(fm['version']);bits=oldv.split('.');bits[-1]=str(int(bits[-1])+1);newv='.'.join(bits)
 fmtext=re.sub(r'^version:.*$',f'version: "{newv}"',fmtext,flags=re.M);fmtext=re.sub(r'^last_updated:.*$','last_updated: 2026-10-31',fmtext,flags=re.M);intro=intro.replace('v'+oldv+'\n','v'+newv+'\n')
 if slug in description_additions:
  old_description=fm['description'].rstrip();description=old_description+' '+description_additions[slug]
  fmtext=re.sub(r'(?ms)^description: >\n.*?(?=^[a-z_]+:)', 'description: >\n  '+description+'\n',fmtext)
 intro=intro.rstrip()+'\n\n'+notice+'\n\n'
 new='---'+fmtext+'---'+intro
 for h in H:
  assert buckets[h],(slug,h)
  new+='## '+h+'\n\n'+'\n'.join(buckets[h]).rstrip()+'\n\n'
 new+=suffix
 if not suffix:new=new.rstrip()+'\n'
 (R/'skills/gibraltar'/(slug+'.md')).write_text(new)
print('restructured',len(plans),'Guides; original snapshots retained')
