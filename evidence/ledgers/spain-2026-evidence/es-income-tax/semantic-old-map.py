from pathlib import Path
import json
P=Path(__file__).resolve().parent;a=json.loads((P/'old-topics.json').read_text());N={}
def put(lfs,txt):
 for x in a:
  if x['ref'].startswith('62') and x.get('old_lf') in lfs:N[x['wording']]=txt
put([20,22],'Current LF20/26/30 ordinary2026 common-territory resident scope; exact old2025 comparison/campaign assertions remain historical and are not relabelled2026.')
put([26,27,50],'Current LF26–30 residence9/worldwide/category and separateforal/IRNR/Beckham routing; no assumed ordinary split-year return.')
put([28],'Current LF28 actual community72 days→definedmaininterest→lastdeclaredresidence with antiavoidance; no choice of lowest-rate region.')
put([29],'Current LF477/482 RETA-registration annual mandatory return with art96 conditions separate from ordinary salary thresholds.')
put([30,336,337],'Current LF30/502–506 routes actualforal/IRNR/Beckham/treaty/exit facts to separate own methods, not a blanket refusal of supplied ordinary resident computation.')
put([31],'Current LF286/322/484 links category/rental/capital/crypto, socialcontributions and estimated-tax companion methods; oldslug spellings retained here as history.')
put([33,333,334],'Current LF36–267 supplies state half and all15 actual2026regional scales; LF359–373 regional minima; LF407 creditcompanion. No universal combinedSpanishrate or regionalhalf refusal.')
put([51,52,53,365],'Current LF276/322 directassessment600000 combinedprior-turnover,annualisation,conditions,renunciation/exclusion; normal/simplified are actual established methods, not defaults.')
put([54,174,178,179,180,181,183,184,185,186,187,286,335],'Current LF322 routes objective-assessment2026 entry/election/peractivity methods to es-estimated-tax, preserving enactedlowerbaseline versus publishedAEATnonconvalidationroute. Old figures/cases remain here; no claim currentincomeGuide independently reproduces all131boxes or verifies2025limits from a2026note.')
put([55,56,57,59,134,157,290,366,367],'Current LF286/324 reconciles actual gross receipts/expenses, owneligiblecontributions, irrecoverableversusrecoverableVAT and prepayments/loanprincipal/drawings. CORRECTION: VATregistration alone does not exclude allVATexpense, and mixedasset deductibility follows actualRIRPF22 rather than anychosenpercentage.')
put([58,191,195,196,197,198,199,200,201,202,203,204,206,370],'Current LF335 complete10groups rates/maximumyears includingsoftwareingroup5; RIRPF30.1/officialtable versus normalcorporate-tax depreciation distinguished.')
put([60,163,164,165,167,168,371],'Current LF276/337 simplified5%/combined2000cap,600000eligibility and2026Ceuta10% separate. Historical2023/2025comparisons are preserved here, not quoted as a new2026enactment.')
put([61,372],'Current LF286/288 classifies allincome and separatelynets general/savings baskets,25%crossbasket/fouryear limits; no salary offset of a shareloss.')
put([62,63,64,65,373],'Current LF398–405 applies stateandactualregional scales separately with separate minimum allocation; minimumtax subtraction rather than marginal-rate income deduction.')
put([66],'Current LF407/409 creditpositions and es-irpf-deductions complete national/15regioncatalogues; precise remainingordinary interactions remain inSources/README.')
put([67,220,374],'Current LF407/484 prepayment reconciliation and LF516/551 two actualworkedannualbalances; withholding/instalments are not expense, eligibleexcess canrefund.')
put([68,348,349,375],'Current LF478/640 2026-income return filed2027 underactualfuturepublishedwindow/form/paymentrules; oldphone/inperson/60:40option assertions are not separately verifiedfor2027.')
put(list(range(74,90)),'Current LF36–47 State63only sixbands/openingquotas and LF59–267 all15own2026scales. Old2025comparison/manualURLis historical; currentstatehalf is never asserted as fullIRPF or annualwithholdingscale.')
put(list(range(93,102)),'Current LF49–57 both66/76half scales and explicitlyderivedcombined19/21/23/27/30rates; actualper-half minima remain separate. Old2025dates retained historically.')
put(list(range(105,128))+[280],'Current LF347–373 state57–61minimumcomponents/relative8000/ownreturn1800/share/taxaccrual/cohabitation and separate actualregional profiles. Current359/373 personalagetotals are computed, not all additiveincrements.')
put([128],'Current LF345 joint82–84 actualfamilyelection3400/2150,cohabitingother-parent exclusion and sharedbase/minimum limits; noautomatic adultminimum multiplication.')
put([130],'Current LF308–318 employment20fullthreebands/netRexcludes19.2.fallowance; distinctgrosslowpayDA61credit. Oldapproximateautónomoeligibilityclaimnot a substitute for actual6500gate.')
put([136,137,138,139,140,277,368],'Current LF328/333 main-home30%×businessareafractionorprovedalternative; separatepremises follow actualbusinessuse/generalcostrules. CurrentIRPFpartialasset/indivisibility rule prevents chosenunsupportedprivate/businesspercentages.')
put([142,143,144,148,149,151,278,279,369],'Current LF329–330 ownworkingmealsbusinesspurpose+restaurant/hospitality+electronicpayment andactualdaily26.67/53.34Spain,48.08/91.35foreigncaps; entertainingclients remains different and is not newly quantifiedhere.')
put([153],'Current LF331 healthinsurance500percoveredtaxpayer/spouse/cohabitingchildunder25 or1500disabledperson; actualcoveredfactsrequired.')
put([155,288],'CORRECTED DEFAULT: current LF322/333/592–599 requires actualmethod/assetuseevidence; no default simplifiedassessment or unsupportedIRPFvehicleproration. Currentfamilyminima require evidence, not an inventedzeroentitlement where factsunknown.')
put([169,338],'Current LF339 supplies ordinary32.2allgates/2000additionalbands/disability/alternativeincome1620taper/newactivity20% and simplified-itemincompatibility; no longer a blanket referral.')
put([170,214,285,339],'Current LF337/466/508 Ceutaqualifying10%/2000cap andexactannualversusinstalmenteffectivewindow; LF454–464 actual68.4territorialsource/creditconditions. Withholding60%reduction separately ines-estimated-tax/111, not the annual60%credit itself.')
put([212,213,217,218,281,321],'Current LF279/484 professionalgrossfees15%,eligible7%start+next2years/nopriorprofessionalactivity/signednotice andactualobligedpayer. Old2000invoice140numericfixture retained onlyhistory, not claimedidenticalcurrentexample.')
put([215,219,221],'Current LF286/407/484 actualincomeclassification/obligedwithholdergateway and Modelo111/estimated/rental/crypto companionroutes; oldspecial1%/artist15000+75%/rent19%details are not independently restated inthisincomeGuide, and remainexacthistoryratherthanfalselymapped15%professionalrule.')
put([225,226,227,282,350],'Current LF278/280/479/484 plus es-estimated-tax ordinary130year-to-date20%,actualpreviousyear/startperiod70% professionalexemption,1–20Apr/Jul/Oct,1–30Jan/nonworkingday adjustment; noautomaticexceptionforalltraders.')
put([228],'Current LF484 detailedestimated-taxcompanion preservesnegative-quarterrouteversusannualrefund; an instalment isnot a standaloneannualrefund.')
put([229],'SOURCE CORRECTION: current LF484 expressly distinguishes VATcalendar/fourthquarterdate from130calendar; old"samequarterlycalendar"blanketassertion isnotretained.')
put([233],'Current LF30/506 routes ordinarynonresidents to IRNRcompanion afterresidence; old24/19rates are historicalrouting figures, not an ordinaryresidentIRPFrate or a newcompleteIRNRmethod.')
put(list(range(237,269))+[283,284,326,342],'Current LF490–498 conditionalLGT27late/198no-loss/191classifiedoffence/28collection andactual2026interest. Old3k/concealment/book/withholdingand18830/40reductiondetail remains historical here: current generic"statutoryreductions"doesnotpretend torepeat eacholdpercent/condition; actualproceedingmustbeclassified.')
put([294,296],'Current LF549–588 actual2026 professionalexample tests simplifiedcap/annualhalves/baskets/prepaymentreconciliation; old55000consultantfictionalvalues remain history, not identicalcurrentcase.')
put([304],'Current LF328 mainhome30%×evidencedareafraction rule suppliesold80/12/4.5%/135examplemethod; exactoldfictionalnumbers remainhistory, not an extra mainoa block.')
put([311],'Current LF329–330 supplies olddeclared32/18/100mealinputs through actual26.67/53.34 caps/electronicgate; oldfixturehistory retained, not fictionalstatutoryamounts.')
put([316],'Current LF407/516/551 creditactualprepayments/refundmethod; old10500/8250/4000/1750refundfixture remains exacthistory, not identicalcurrentexample.')
put([340],'Current LF286 capitalgains/rental/cryptocompanions provideowncategory computations; no blanketordinaryshare-disposalrefusal or importedcorporateparticipationexemption.')
put([341],'Current LF26/30individualscope andcorporatecompanion; thisincomeGuide doesnot compute acompanytaxpayer.')
put([354,355,356,357,358,359],'HISTORICAL YEAR / CORRECTION: old2025campaign8Apr–30Jun2026/debit25Jun/60:40closedreturn details stay exacthere; current LF478/640 doesnot assert those as2027dates/options. Current LF480 uses approved67bisrectificativa/exceptions, correcting theoldblanketcomplementaria/refundrequestsplit. Current2026scales/lowpaycredit are not assumedidenticalto2025.')
# Every substantive main unit has a specific semantic destination; headings/table separators remain presentation.
for x in a:
 if x['ref'].startswith('62') and 'exact original unit' not in x['destination'] and x['wording'] not in N:
  if x['wording'].startswith(('#','**')) and ('table' in x['wording'].lower() or x['wording'].startswith('#')):continue
  if x.get('old_lf',0)>=361 and x['section'].startswith('## Completion'):N[x['wording']]='Current LF592–599 intake and corresponding actualbase/rate/source methods; output is source-cited draft, not professional attestation. Exactoldchecklistwords remainhistorical.'
(P/'semantic-map-overrides.json').write_text(json.dumps(list(N.items()),ensure_ascii=False,indent=2)+'\n')
s=(P/'build-ledger.py').read_text().replace('notes=[]',"notes=json.loads((P/'semantic-map-overrides.json').read_text())")
s=s.replace("('## Rates',", "('## Scope','Current LF26–30 ordinaryscope,residence/community andseparateforal/IRNR/Beckhamroutes.'),('## The method','Current LF284–468 orderedcategory/base/expense/minimum/quota/prepaymentmethod.'),('## Figures','Current actual2026state/regional/savings/minimum/expense/paymenttables; oldyearcomparison remains historical.'),('## Boundaries','Current actualexpense/asset/family/withholding/loss/filinggates withspecificcorrections inthismap; no unsupporteddefault.'),('## Worked cases','Current two actualoa annualcases and historicalfictionalfixturesmappedtomethods, not identicalnumbers.'),('## When to refuse','Current Sources/companionroutes supplyordinary methods and precisely retained gaps; no blanketrefusal.'),('## Filing','Current478–484/640 filingyear/form/rectificativa andactualpaymentdates;2025closedcampaignnotrelabeled2027.'),('## Completion','Current consequentialintake/orderedbase/scales/credit/prepaymentreconciliation.'),('## Disclaimer','CurrentprotectedCTA/disclaimer.'),('## Rates',")
(P/'build-ledger.py').write_text(s)
