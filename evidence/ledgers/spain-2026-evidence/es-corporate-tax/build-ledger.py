from pathlib import Path
import runpy,json,re
P=Path(__file__).resolve().parent
E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));R=E['ROOT']
Q=json.loads((P/'quotes.json').read_text())
baseline=(P/'baseline-current.md').read_text()
current=(R/'skills/international/spain/es-corporate-tax.md').read_text()
M={
21:[],25:[],29:['who','worldwide','residence'],31:['period','periodAccounting','periodclose','transition'],33:['patrimonial','patrimonialRest','new15','erd101','annualExempt'],37:['transition'],
41:['ordinary25'],42:['microRates','erd101'],43:['microRates'],44:['microRates'],45:['microRates','erd101'],46:['new15'],47:['banks30'],48:['charity10','fund1','pension0'],49:['cooperative'],50:['cooperative'],51:['loss70'],52:['lossDAs'],53:['loss70','lossShort'],54:['netFinance','netFinanceCarry'],55:['cap20'],56:['level10'],57:['minimum'],58:['minimum'],59:['minimum','transition'],60:['withholding'],62:['erd101','new15','microRates'],64:['transition','microNew'],
70:['accounting','accrual','booking'],72:['nondeduct','impairment15k','related','donation40'],74:['debt6','collective1'],76:['netFinance','netFinanceCarry','financeExceptions'],80:['depMethods','depAlternatives'],84:['works2','build2'],85:['industrial3'],86:['install10','furniture10','other10'],87:['machinery12'],88:['transport16'],89:['lorry20'],90:['hardware25'],91:['software33'],93:['intangibles','free300','ERDaccelerated','freeEmployment','freeEmployment24'],
97:['participation5','participation10tax','participationDisposal','participationPayer'],99:['participation95','participationSmall'],101:['foreignPE','foreignPEcessation','foreignCredit','foreignDividendCredit','lossDAs'],105:['cap20','loss70','level10','taxNet','202levels'],107:['cap20','capOwnFunds','capFundsExclusions','capTable'],109:['capCap20','capCaps','capCarry','capHeadcountHold','cap20','capBreach'],111:['loss70','lossShort','lossNew','lossDAs','lossTrafficking','lossHistory'],113:['level10','level5breach','levelNoDouble','202levels'],117:['taxNet','minimumOrdering'],121:['RDI25','RDI17','RDI8'],122:['innovation12'],123:['disabledCredit'],124:['filmCredit','film20'],125:['creditCap'],126:['donation40','donationCap'],128:['RDIcost','innovationGrant','creditCarry','creditDiscount','donationCap'],130:['minimum','minimumOrdering'],132:['prepayments'],136:['ceuta60','ceutaEntry','ceutaDF','ceutaOld'],138:['ceutaNew120','ceutaOldCap','ceutaEntry'],140:['ZECinvestmentClock','ZECwho','ZECjobs','ZEC4','ZECcoefficient','ZECminimum','ZECcap','ZEC30'],
146:['annual'],147:['annual'],148:['periodPay','202instructions'],149:['withholdingDuties'],150:['TP232','TP232date'],152:['annual','annualExempt'],154:['202base','20218'],156:['20218','202fiveSevenths','202compulsory','202nineteenTwentieths','202trigger','202election','202instructions'],158:['202trigger','202minimum','202Ceuta','ceutaEntry'],160:['202nil','202electronic','periodPay'],
166:['late'],167:['late'],168:['late25'],169:['enforcement'],170:['penalty191','penalty191grave','penalty191very'],171:['penalty198'],172:['interest','interest26'],174:['penalty191','penalty191grave','penalty191very','reductions188','capBreach','level5breach','nondeduct'],178:['worldwide','related','withholding','withholdingExempt'],180:['exit','exitOneYear','residence'],182:[],188:['microRates','erd101','minimum','prepayments'],190:['microRates','prepayments'],207:['microRates'],209:['microRates']}
old_by_wording={u:(lf,sec) for lf,sec,u in E['units'](baseline)}
rows=[];used=set()
for lf,sec,u in E['units'](current):
 oldlf=old_by_wording.get(u,(None,None))[0]
 if u.startswith('Add back own-funds remuneration'):oldlf=72
 if oldlf in M:
  keys=M[oldlf];kind='Positive rule checked against the quoted own law/administrative chain; combined calculations and administrative interpretations are identified in the Guide.'
 elif u.startswith(('---','#','>','<!--')) or sec.startswith(('## Ask the client','## Talk to a verified','## Sources')) or (u.startswith('|') and (re.match(r'^\|[\s|:-]+$',u) or any(s in u for s in ['| Item |','| Selected linear','| Credit |','| Obligation |','| Event |']))):
  keys=[];kind='Presentation, protected attribution/CTA, factual intake, bibliography or express unresolved scope boundary; no positive statutory figure asserted.'
 elif lf==1:
  keys=[];kind='Metadata/summary. Operative rules are traced in the substantive rows, with no professional attestation claimed.'
 else:raise RuntimeError(('Unclassified current unit',lf,sec,u[:100]))
 if oldlf in (21,25,182):kind='Precise scope/intake/review instruction; no new statutory figure, treaty result or specialist-regime determination asserted.'
 if oldlf in (188,190,207,209):kind='HYPOTHETICAL client inputs and DERIVED arithmetic. Legal constants quoted separately; no claim that official law prints these example outputs.'
 if oldlf==72:kind+=' Bounded old-main art15.k participation-impairment topic restored in v1.3; other categories are not declared deductible by omission.'
 if oldlf==99:kind+=' 95% is explicitly derived from the statutory 5% reduction, subject to the own exception conditions.'
 if oldlf==107:kind+=' Literal statutory overlap at exactly5% and AEAT administrative table are both retained; not a purported legislative correction.'
 if oldlf in (59,130):kind+=' Reduced-rate minimum rounding precision is expressly reserved pending applicable return instructions; no unsupported rounded amount inserted.'
 if oldlf in (136,138,158):kind+=' Annual non-ended-period test and instalment-window test are distinct; prior art33 reader applies only to its historical period.'
 if oldlf==160:kind+=' Future annual2026 form/schema/calendar not relabelled from2025-return forms.'
 quotes=[]
 for k in keys:
  z=Q[k];used.add(k)
  quotes.append(k+'; '+z['source']+((' art.'+z['article']) if z['article'] else '')+'; '+z['reader']+' LF'+str(z['LF_start'])+'–'+str(z['LF_end'])+': «'+z['quote']+'»')
 for wording in E['clauses'](u) if keys and not u.startswith('```') else [u]:
  rows.append(dict(lf=lf,section=sec,wording=wording,authority='; '.join(dict.fromkeys(Q[k]['source']+(' art.'+Q[k]['article'] if Q[k]['article'] else '') for k in keys)) if keys else 'Not a positive legal figure/rule',url='; '.join(dict.fromkeys(Q[k]['url'] for k in keys)),quote='\n\n'.join(quotes) if keys else 'No statutory quote claimed for presentation, protected wording, factual intake, bibliography or an express scope limitation.',read_on='2026-10-28',status=kind))

# Section routes identify the actual substantive current destinations, never fuzzy text matches.
routes=[
('### 4.1','Current The base /4 LF107–109: own-funds definition/exclusions,20/23/26.5/30%,headcount bands,20/25%base cap,3year holds,2yearcarry and breach. Literal5%overlap retained beside actual AEAT administrative table; old ask-accountant fallback superseded.'),
('### 4.2','Current The base /4 LF111:70/50/25%reference caps,minimum1m/shortperiod,exceptions,anti-trafficking,10yearchecking and later substantiation. International-credit50%grosscap is LF101, not the loss-cap paragraph.'),
('### 4.3','Current Rates LF56 and The base /4 LF113:10%/1m/shortperiod,5yearaddback,profit reserve,no-double-funding,instalments and5%breach. Quoted current AEAT2025-and-following form eligibility chain replaces the old blanket referral.'),
('### 4.4','Current The base /5 LF121–128: individual R&D25/42+17+8,innovation12,disability9k/12k,film30/25+20m/10mepisode,25/50/10credit caps,20%optionaldiscount,15/18yearcarry,donations40/50/15+10yearcarry. Each row destination refined by its tax topic.'),
('### 4.5','Current The base /6 LF136–138:60%annual bonification with explicit2026non-ended3Sepgate,employee60k/1.2m and firsttwo120k/2.4m,earlier50%/50k/400k;commercialcycle conditions. Prior undated assertion is qualified,not backdated.'),
('### 4.6','Current Rates LF57–59 and The base /5 LF130:trigger20m/group,15/10/18/60%,reducedrate15/25roundup,exceptions,Canary/ZECbase and permissible-credit ordering. Actual roundingprecision remains explicit Sources LF253 boundary.'),
('### 4.7','Current The base /2 LF80–93:methods and exactselectedassetrows,300/25kfreeassets,intangible1/20,ERDacceleration,120k and24+24months employmentfreewriteoff. Separate collectivebaddebt1% moved toLF74.'),
('### 4.8','Current The base /3 LF97–99:5%holding/year/foreign10%,disposalconditionatdate,5%managementreductionandderived95%,qualified40m/2021/3year exception. Dividend subsequent-year completion is not generalized todisposals.'),
('### Two Modalities','Current Deadlines LF154–156:40.2last-periodgross-taxnetofspecifiedcredits18%,shortpriorperiodaggregation;40.3current3/9/11months,floor5/7orceil19/20,exact>6mmandatory/>=10mlargescale and census election. Derived percentages permitted when labelled.'),
('### Calendar','Current Deadlines LF148 first20Apr/Oct/Dec. Historical foralState-form periodkeys are separately flagged as notrestated,not presumed retained in a sibling.'),
('### Pago Fraccionado','Current Deadlines LF156–158:DA14>=10m,23/25%minimum,actualstatutoryadjustments/exclusions,and distinct CeutaDA20paymentwindow60%. Historical court-effect story retained inoldbody,not asserted as an unresolved2026operatingfloor.'),
('### Retenciones','Current Rates LF60,Deadlines LF149,Tax balanceLF132 and Cross-borderLF178:19/24/20,residentpayerduties,certificate,qualifiedexemptionsandCeutaurbanrenthalf19%. Nonresident recipient/treaty routing distinguished.'),
('### Exempt','Current Deadlines LF152:fullyexemptart9.1,allthree75k/2k/withheldpartialexemption gates,other9.2–9.4income declarations. Dormancy/loss/nil tax notautomaticexemption.'),
('## Section 1:','Current Who LF29–33,accounting LF70,RatesLF41–64,annual/instalmentDeadlinesLF146–160. Currency andtaxname retained in metadata/amountwording;historical25Julycalendar shortcut qualified by actualperiod and filingcalendar.'),
('### Common Territory','Current Who LF33,RatesLF41–48,62–64:2026DT44rates,ownstart-year,shortbanddays/365,groupannualised1m/10mtests,newactivity/patrimonialexclusions.'),
('### ERD Transitional','Current Rates LF64 explicit2025–2028ERD24/23/22/21then20andmicro21/22,19/21then17/20,plusLF43–45own2026rows.'),
('### Foral','Current Who LF31routes fourterritories to es-foral-corporate-tax.md ordinarymethod;precise sibling Sources limits retained. No generic no-official-source barrier reinstated.'),
('### Special Regimes','Current Rates LF48–50 protected/creditcooperatives,funds/pension;The base/6LF136–140Ceuta/ZEC. Canaryart27investmentreserve remains explicit specialistboundary LF140.'),
('## Section 2:','Current Who LF29residenceandworldwide,LF33patrimonial;RatesLF41–64specificcommonstaging/specialrates,foralsiblingrouteLF31.'),
('## Section 3:','Current The base orderedLF70–140 plus balanceLF132. Accounting→adjustments→capreserve→loss→level→rate→bonifications/doubletaxcredits→othercredits withart30bisordering→prepayments. Old credits-before-bonifications/generalmaxfloor simplification corrected.'),
('## Section 6:','Current The base /1 LF72–76:art15addbacks/1%entertainment/15kimpairment restored andart16netfinance30%/1m/shortperiod/unlimitedcostcarry/fiveyearcapacity. Unnamed subcategories are distinguished below rather than falsely claimed verbatimprose.'),
('## Section 7:','Current The base /6 LF140:4%eligiblepart,investmenttwo-years100k/50k,jobs5/3within6months,coefficientversus1.8m+500k50jobs,30%taxreductioncapandnoncooperativeexclusion. Fullspecialistclaim remains fact-specific.'),
('## Section 8:','Current orderedThe baseLF70–132and twohypotheticalcomputedcasesLF188–225. Old orderonlycase retained historically; derivedexampleamounts nowexpresslypermittedandlabelled,not represented as enactedsums.'),
('## Section 9:','Current Deadlines LF146–160 annual200,instalments202,withholdingand232sibling route. Modelo220specialistboundary LF152;232thresholds/method separately supplied in spain-transfer-pricing.md RatesLF39–45/DeadlinesLF67–70.'),
('## Section 10:','SOURCE CORRECTION: current introLF25/WhoLF29–33 and sixintakequestionsLF230–235 establish actualterritory/period/entity/turnover/eligibility;unknownfacts are notdefaulted tocommonterritory/SL/2026/accounting=tax/higherassumedrate.'),
('## The method','Current The base LF70–140andDeadlinesLF146–160provide substantiveorderedcalculation and filing/election;rate selectionLF41–64,foralrouteLF31,232methodinverifiedTPsibling. Historicalordering/blanketderivedfigureprohibition corrected.'),
('## Ask','Current six consequential questions LF230–235 retainperiod,territory,turnover/group,patrimonial/newstatus,lossyear/checks,funds/headcount,territorialsubstanceandinstalmentelection.'),
('## When','Current Cross-border LF178–182/SourcesLF253 giveprecise specialist boundaries;fourforalordinarymethodsprovidedinsiblingLF31andTPpricing/disclosuremethodinsiblingLF150. No blanket unsupported refusalreinstated.'),
('## PROHIBITIONS','Current factualeligibilityandlimits throughout Rates/The base/Deadlines/Cross-border. Overbroadbanonlossesbeyondpercentage correctedbyown1mminimum/exceptions;creditcapqualifiedbyownexceptionsandminimumordering.'),
('## Sources','Current Sources LF239–253 and immutableprior-mainbaseline retain sourcehistory. HistoricalsourceURLspellingsthatdiffer are retained inledger;not falselyclaimedidenticalcurrentURLs. Currentyear sourcedfrom actualdatedlaw.'),
('## Disclaimer','Current protectedgeneralreference/CTA and currentqualifiedreviewinstructions;originalexpandeddisclaimerretained inprior-mainbaseline.'),
('## Talk','Current protectedCTA LF261–273,unchanged fromfrozenPRbody.'),
('Metadata','Current protectedmetadata/H1,attributionLF23;historicalversion/summarypresentationretainedinbaseline.')]

notes=[
('Add back own-funds remuneration','Current LF72 preserves the entire frozen-PR accounts-to-tax paragraph verbatim and inserts the bounded art15.k participation-impairment sentence. No original clause removed; current quote chain includes nondeductible categories, related-party treatment and donation-credit distinction.'),
('No official page resolves the overlap','SOURCE CORRECTION: current LF107 retains literalart25overlap and supplies actualAEATtable>=5%26.5%.3yearholds/basecaps/exclusionscarriedLF107–109;oldtake-lower/askaccountantfallbacksuperseded.'),
('no page says in terms whether','SOURCE CORRECTION: current LF113quotesart105andcurrent2025-and-followingAEAT202instructions,positiveeligibility/10%/1m/5yearmechanics;oldblanketreferralreplacedbyqualifiedmethod.'),
('This Guide does not state a net exempt percentage','SOURCE CORRECTION: current LF97–99 distinguishesdividend/disposalyearconditionsand explicitlyderived95%from5%,with40m/2021/3year exception;notanunsourcedstatutory95%quote.'),
('A company taxed under Navarra\'s rules marks 2P','NOT RESTATED / NOT YET CONFIRMED: historicalStateModelo202foralperiodkeys2P/0Aretainedinbaseline;currentLF148givescommonwindowsandLF31routesforalordinarymethods,butno current sibling is claimed tocontain these exactState-formkeys.'),
('| Modelo 220 |','SPECIALIST BOUNDARY: currentLF152explicitlypreserves consolidation/groupreturn requirement butdoesnotassembleModelo220;historicalparent-windowassertionretainedhere,notindependentlyrevalidatedasfull2026formmethod.'),
('decree that first introduced this floor','CORRECTION/BOUNDARY: currentLF156–158usesactualcurrentDA14and2025-and-followingAEATinstructionsfor23/25%minimum,adjustmentsandexceptions. Old2020court-effects narrative remains historicalinbaseline,not asserted as reason toleavecurrentoperatingfloorundecided.'),
('Expenses of acts contrary','CurrentLF72incorporatesotherart15disallowances;exactold15.fillegal-acts wording retainedhereandcurrentownlawquoteinledger. No falseclaimofexplicitnamedcurrentprose;category remains sourced art15.f,notdeclared deductible.'),
('Service charges from, or paid through','CurrentLF72incorporatesotherart15disallowances;exactold15.glisted-jurisdiction service-charge/proofexception retainedhereandquotedcurrentownart15.g. CurrentGuide doesnotnameeveryitemseparately;notdeclared deductible.'),
('Impairment of holdings','RESTORED: currentThe base/1LF72explicitlyrestoresoldart15.kparticipation-impairmentaddback,testingart21holding/foreigntaxconditions. v1.3boundedone-sentencechange;source/before-afterrecordpreserved.'),
('Bad debt provision a small company','CurrentThe base/1LF74collective1%debtorallowancewithownart104exclusions/rollforward,notdepreciationLF93.'),
('Cap on the credits for international','CurrentThe base/3LF101DA15international-credit50%grosscap;notloss-capLF111.'),
('| Research and development','CurrentThe base/5LF12125/42qualifyingR&Dplus17researchstaff/8investment.'),
('| Extra deduction for qualified researchers','CurrentLF12117%qualifiedexclusiveR&Dstaffadditionalcredit.'),
('| Investment in assets used only for research','CurrentLF1218%qualifiedR&Dassetinvestment.'),
('| Technological innovation','CurrentLF12212%qualifyinginnovation;grant/projectgateLF128.'),
('| Increase in the average headcount of workers with a disability','CurrentLF1239k/12kperperson-year33/65%tests.'),
('| Spanish film','CurrentLF12430%first1m/25%excess;specialistqualification,20mtotal/10mepisode.'),
('| Joint cap','CurrentLF12525%capafterbonifications/internationalcredits.'),
('| Raised cap','CurrentLF12550%raisedcapwhereperiodart35/36credits>10%adjustedgrosstax.'),
('| Share of the gross tax','CurrentLF125>10%triggerforthe50%cap.'),
('| Discount where','CurrentLF128optional20%discountsubjecttoownart39.2conditions;notautomaticcashrefund.'),
('The film deduction is capped','CurrentLF12420m/10mepisodeandLF12815/18yearcarry.'),
('| Deduction on the base of the donation','CurrentLF12640%donationcredit.'),
('| Deduction to the same body','CurrentLF12650%qualifiedrepetition;ownfullquotedart20historygatesinledger.'),
('| Cap on the base of the deduction','CurrentLF12615%donationbasecap;LF12810yearcarry.'),
('Amounts above the cap carry forward ten years','CurrentLF128donationcredit10yearcarry,separatefrom15/18yearChapterIVcarry.'),
('No official page says how far that rounding','CurrentRatesLF59minimum15/25roundupandSourcesLF253actualroundingprecisionboundary;LF130properbonification/creditordering. No unsupportednumericalfloorinserted.'),
('This Guide does not print the resulting percentage','CurrentDeadlinesLF154–156own18%last-taxand40.3floor5/7/ceil19/20rates,current3/9/11monthbase,>6mmandatory,>=10mlargescale,election. Derivedoutput permitted,labelled rather than prohibited.'),
('| All transactions with the same related party','SIBLING:spain-transfer-pricing.mdRatesLF39own232>250kperpartytest.'),
('| Specific transactions, each type','SIBLING:spain-transfer-pricing.mdRatesLF40own232>100kspecifictypegate.'),
('| Transactions of the same type valued','SIBLING:spain-transfer-pricing.mdRatesLF41own232>50%turnovertest.'),
('| Modelo 232 |','SIBLING:spain-transfer-pricing.mdRatesLF39–45andDeadlinesLF67–70full232thresholds/specialcases/monthfollowing10months;currentcorporateLF150explicitroute.'),
('The worked example that stood here','CurrentThe baseLF70–132retainscompleteorderedmethodandtwohypotheticalcomputedcasesLF188–225;oldclaiminventedinputsforbiddenreplacedbylabelledfictionalinputs/derivedoutputs.'),
('Do not state an effective rate','CORRECTION:currentexamplesLF188–225explicitlyallowderivedarithmetic;neitheranoutputnoreffectiverateis falselypresented as astatutorynumber.'),
('NEVER compensate losses beyond','CORRECTION:currentLF111ownpercentagecap+minimum1m/exceptions;formerabsolutepercentage-onlybanincomplete.'),
('NEVER exceed the joint cap','CORRECTION:currentLF125/128/130ordinarycap,ownoptional20%route,Canary/minimumexceptions;notablanketbanignoringstatutoryexceptions.')]
res=E['render']('es-corporate-tax',rows,notes,routes)
f=R/'ledgers/es-corporate-tax.md'
f.write_text(f.read_text().replace('The ledger writer has not edited the Guide.','The root writer restored a bounded prior-topic sentence in v1.3; before/after/source proof is retained. Independent review remains required.'))
res['ledger_sha256']=E['sha'](f)
(P/'ledger-summary.json').write_text(json.dumps(res,indent=2)+'\n')
(P/'actual-read-quotes.json').write_text(json.dumps([dict(key=k,**Q[k]) for k in sorted(used)],ensure_ascii=False,indent=2)+'\n')
print(json.dumps(res));print('usedquoteanchors',len(used),'explicitmapgaps',sum(x['destination'].startswith('EXPLICIT TOPIC-MAPPING GAP') for x in json.loads((P/'old-topics.json').read_text())))
