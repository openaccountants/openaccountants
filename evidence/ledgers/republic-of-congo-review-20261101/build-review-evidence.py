from pathlib import Path
import json,re,hashlib,subprocess
D=Path('evidence/ledgers/republic-of-congo-draft-20261101');O=Path('evidence/ledgers/republic-of-congo-review-20261101')
# These notes record manual reading of the complete relevant source pages and their neighbouring provisions.
notes='''C01|LF46-47|28 ordinary;25 microfinance/private school;28 mining/quarry/property;33 foreign legal persons;hydrocarbon contract floor;profit floor1000
C02|LF30-31|SA/SAS/SARL single member included;lucrative public/activity scope;partnership option/exemptions not erased
C03|LF33-34|net receipts less deductible costs;OHADA/sector accounting;preceding year;31December except cessation
C04|LF35-36|all nine deduction limbs;NIU and SFEC;cash greater-than-or-equal200000;business year/evidence/net-assets/exempt/abnormal exclusions
C05|LF38-39|IS excluded;taxes borne and assessed in year;refund enters notified-year receipts;fines/confiscations/penalties excluded
C06|LF39-40|market terms;paid-up capital;BEAC+3points;20percent nonexempt EBE;5year interest carry;financial/insurance operating-interest exception
C07|LF41,43|ordinary losses through fifth following year;exempt-year losses barred;Article53 unlimited deferred depreciation conflicts with Article75 ordinary-loss treatment: F02
C08|LF47|1percent all operating/financial/nonordinary products;exclude final-withheld products;minimum versus ordinary
C09|LF47-48|provisional15March declaration;prior/lastclosed base;four15March/June/September/December instalments;same-year credit;retained if liability lower/nil
C10|LF47-48;CAL1,4|86F four months;86G balance on return;15May calendar conflict explicitly held;firstperiod86 exception not operative instruction
C11|LF47,66-67|128 fifteen-day existence;130 electronic real regime and expert certification absent auditor;131 three sets/electronic and DSF schedules;portal version held;Article86E three-month constitution limit omitted: F04
C12|LF47|86C8 nonpayment50percent specific minimum only
C13|LF66|130 noncompliance electronic obligation10percent amount to declare
C14|LF71-72|374ter before administration claim/information request;0.5percent per delayday;20percent cap;no penalty only particular case
C15|CAL1,4-5;LF47-48|calendar DSF15May after close;IS/IBA15May;statutory conflict and no extension certified
I01|LF30,55-66|enacted chapter replacement IS/IBA/IRCM/IRF/ITS;not former global bands
I02|LF57|IBA30percent;floor1000;minimum1.5percent all operating/financial/nonordinary products;IS minimum framework
I03|LF56-57|straight-line only;doubtful debts excluded;third following loss year;3A credit excluded;own drawings/costs/capital interest/rent;split mixed;50percent representation
I04|LF57-58|not exceeding VAT boundary;all six exclusions;VAT option immediate;2 successive below years;ceases year after excess;rates/threshold held
I05|LF56|owned/usufruct/rented home latter>=1continuous year;principal stay;posting/retained interests;absence>24months;Congo-source nonresidents;foreign branch directors presumed;no universal183days
I06|LF59-61|IRCM15percent;hidden35percent;distributed/interest/security/PE categories separate;no general resident-interest-zero
I07|LF60-61|payer operated Congo OR resident beneficiary;decision event;dividend payment exigibility no later3months;gross base
I08|LF61-63|outside IS property;gross rents9percent;gains10percent;Congo property regardless residence or resident foreign property;documented acquisition/improvement costs
I09|LF62|free direct-line ancestor/descendant occupation;principal-home disposal>=5years;State/local authority income
I10|LF62-63|IS/IBA/public tenants;15March or3months new lease;other tenant individual15May;balance15May20Aug15Nov;property-tax advances;gain3months;registry/land-conservation split
I11|LF63|tenant default joint tax liability plus principal-equivalent fine;gain default cross-reference;not general penalty
I12|LF63-64|salary/directors not assigned IRCM;pensions/annuities scope;retirement exemption and specified benefit conditions;no invented blanket exemption
I13|LF64|available permanent home then vital interests;State abroad;resident foreign work/employer;nonresident Congo-work employer establishment wording;treaties separate
I14|LF64-65|actual benefits or housing20social-capped;staff7 utilities5 phone2 car3 food20gross;reference deducts stated mandatory amounts;allstaff mutual exclusion;retirement then20deduction
I15|LF64-65|round1000 then quotient thenmultiply;1/2/2.5 and0.5 increment max6.5;separate spouses;childless widow2years;116C referral;missing116B widow nonmarital child exception: F01
I16|LF65-66|no separate income;under21/infirm;student25 evidence;foster/protected latter<=2;mother court order;1January versus31December/death increased-dependants/marriage
I17|LF65-66|fixed1200 first0-615000;10percent615001-1500000;15percent1500001-3500000;20percent3500001-5000000;30thereafter;belowSMIG annual minimum1200;SMIG amount not invented
I18|LF65-67|monthly withholding;single-source final;multiple-source annual;foreign selfdeclare/pay;2026under114-116H;DAS3 paragraph explicitly2025;unresolved calendar kept
I19|LF57-59|minimalcash accounts;two chronological registers;monthlydecl;withholding/annualstatements;quarterlyendorsement;form294;firstyear estimate;15day formalities;supplierlist15followingquarter
I20|LF58-59|98.5 defaults assessmentexofficio+100000;99 supplierlist failure500000;triggers separate
T01|LF43-44|dependent/control/commoncontrol foreign;privilegedterritory no dependency needed;indirect prices/other shifts;availableinfo/comparables/FAR;threshold not substantive exemption
T02|LF44-45|legalpersons Congo;turnover OR gross assets>=500000000;foreign related transactions any nature;equality passes
T03|LF44-45|all five group content limbs;changes,structure/counterparties,FAR,intangibles,policy
T04|LF44-45|localactivity/flows/royalties;costsharing;APAs/rulings;FAR/method reason;comparables asappropriate;aggregatebynature>50000000 separate from entity threshold
T05|LF45|does not replace transaction proof;available audit commencement
T06|LF45|81I entities;spontaneous annual prescribed declaration within6months after resultdeadline;light/full accompanying CbC;no750m stated;calendar held
T07|LF45|all listed CbC aggregates byjurisdiction;retained earnings years;cash excluded from tangibles;entities with local controlled flow/residence/activities
T08|LF45-46|5000000 after8day unanswered demand;25000000 missingfull docs at audit;5000000 lateCbC/accompanyingdecl;overlap not mechanically stacked
T09|LF45|CbC nonproduction after8days questions controlled prices;foreign nonarm'slength/policy charges reintegrated
T10|LF45-46|audit request on precise listed matters;initial>=1month;reasoned extension total<=3months;insufficient response completion30days;specified missingitems/sanctions
T11|LF46|five methods including profit split;justified consistent FAR andarm'slength;no hierarchy/median invented;visual fifth method read
T12|LF46|bilateral treatycompetent/unilateral;unilateral limited scope;<=3years renewableconditions;conclusion10000000 not mere application approval
T13|LF45-46|foreignrequest within originalperiod;until endyear afterresponse;outer sixth followingtaxyear;not universal six-yearperiod
X01|LF31-34|registered OR effectivemanagement;nonresidentPE;attribution PE/same-similargoods/same-similaractivities
X02|LF31-33|fixedplaces list;construction/assembly/install/supervision>3months;services same/connected>183 inany12months;otherPElimbs independently apply
X03|LF32-33|listed preparatory/auxiliary exceptions;fragmentation alternatives existingPE,combined nonauxiliary,complementarycoherentfunctions
X04|LF32-33|habitual contract/principalrole orstockdelivery;nonreinsurance insurance rule;ordinaryindependentagent;near-exclusive related exception;controlalone insufficient;>50/control facts
X05|LF47|treatyreservation;residentpayer/fornonresidentPE;services/royalties20percent;equipment/knowhow/software included
X06|LF33-34|foreignPE ofCEMACcompany;foreignlistedreceipts;actualtax deduction OR cappedcredit;PElosses5years onlylaterPEprofits
X07|LF51-54|intermittent/precarious qualifyingforeignentities;22percenttaxexclusivereceipts margin;86Aforeign33 via92C;derived7.26percentnotallin;exclusionconditions held
X08|LF51-54|existence/ATE/modifications;15secondfollowingmonthdecl/pay;cessation beforedeparture;92D named supplierfields;withholding92Bclock not certified
X09|LF53-54,71|100000 missing/incompleteinvoiceelement;8daydemand100percent;pre-demand1percentworkingdaymax50;inmonth500000withoutinterest;374ter coordination held
X10|LF60-62|nonresident direct/indirect securitygains;alone/linked>=10percentpreceding365days;otherpropertyrich rules not erased
V01|CGI299,309;LF106|historical18percent and5percentofVAT;centimesnondeductible;0.9percentbase derived;LF18/5 stateinvoice corroboration;currentnessheld;row needs CGI link F03
V02|CAL2;LF77-78|calendar18/5/0;newAnnex3exempt and5reduced;product+tariff before relief;forestry/SEZ/export held;row needs LF link F03
V03|CGI290-292,298-299|independent remuneratedeconomicsupplies;imports/selfsupplies;consideration;nearest1000;customsvalue+duty/excise;historical scope explicit
V04|CGI296-297|gooddelivery/servicesperformanceevent;goods deliveryexigibility;services/works receiptsincludingadvance;authoriseddebits;customsconsumptiondeclaration;historical
V05|LF77|cash expense EXCEEDING200000;exact200000 not thisexclusion;IS>= boundary different;otherconditions stillrequired
V06|LF77-78|Octoberstructuralcredits;annualphysicalstock/fixedasset inventory administrationpresent;present>=20days beforework;noncompliancecancels31Decembercredit
V07|CGI304-305|15daystart existence/registration;prescribed localsupplier/input/invoice/importdetails;failureexofficioreintegration;NIF/NIU andcurrentprocedureheld
V08|CGI306-307;CAL2|historical15dayfollowingmonth spontaneousdecl/pay;nilreturn required;CALmonthly15 evidence;currentform/operativecalendarheld
V09|CGI304-306|originalinvoices/imports;partyidentification,serial/date,description,base,rate/tax,total;10years extendedoutstandingcredits;SFECheld
P01|LF65-66,79|ITS versus employercharges;TUS fundallocation/CNSSassignedcollection;not oldheadlinecategories rates
P02|LF5-6|individual/informallabouremployer affiliation;2026first25000declarants allIRPP/halfemployerSS+health;inclusion/administrationheld
P03|CAL1-2;LF25p2-3|CALCNSScombined24.28;CAMUemployee2.27/employer4.55;monthly15entries;LF25CNSS4.55/20.28 conflict held not operative
P04|LF5-6|2026rates remaintextsinforce;not itself split/cap solution
P05|LF25p2-3;CAL2;LF5|CNSSemployer20.28/employee4.55;combined24.28 conflict;2026continuity;governingsplit/capsheld
F01|CO25-26,68-69,89,200-201|SARLoneormorememberslimitedliability;SAsingleholder;SASoneormorearticlesgovernance;branchnoseparatepersonality
F02|SARL2;CO69-70|nationalcapitalfreelyfixed;equalsharesnominal>=5000;OHADA1000000defaultsubjectnationalrule;scanvisualread
F03|CO69-70;SARL2-3|allsubscribed;inkindfullypaid;cash>=half;remainder2yearsfromRCCM;immediatedepositapprovedinstitutionreceipt;founder/notaryprescribeddeclarations
F04|CO89,187,200-201|SA10000000;cashquarter/remainder3years;listed/publicoffer100000000;SASarticlescapital/nopublicoffer
F05|SARL1-3|privateornotarialarticles;private-notarialminutesnotcompulsory;mandatoryparticulars;not exemptionfrom validarticles/evidence
F06|CO6-7;ACPCE|preciseaddressnotPOalone;ownership/lease/water/electric/internet/otherproof;not mandatoryseparatecommerciallease
F07|ACPCEidentity|director/members/SAauditoridentityvalid;legalpersonRCCM;foreignerresidentorlongvisa+passport/criminalorhonour;directorNIU/photo/marriagewhereapplicable
F08|ACPCEconstitutional|SARLprivate/notarial+regularity;othernotarial+subscription;SAconstitutiveminutes;capitalproof;PDFencouraged;regulatedadditionaldocs
F09|PORT|publicaccount/login;uniqueform/upload;onlinepayment;electronicemaildocuments;noauthenticatedissuancesequenceclaim
F10|PORT|displaySARL/SARLU300000;SA/SAS/SASU500000;fee notcapital/professionalquote;exemptions/ancillaryheld
F11|CO25-26|branchRCCM;foreignownercontributetoOHADAStatecompanywithin2years;ministerdispensation2nonrenewable subjectspecialregime;not onlyCongosubsidiary
F12|CO25-26|courtdecisionthenRCCMremoval/legalpublication;not automatictimer
F13|CO86-88|>=1auditorif2of3strictly>125000000balance,>250000000turnover,>50staff;2preexpiryyearslosscriteria;minority>=onetenthcourt
F14|CO153;LF66-67|SAoneormoreauditors;taxDSFseparate;fullrecurringfilingsheld
O01|LF30,55-66|2026transpositionincome-taxarchitecture;routebyreceipt
O02|LF33,46-47|31Decemberordinary;startfinal6monthsoptionfirstperiodthroughnextyear;notifybefore31Decemberstartyear
O03|LF114|61 prior-executionrulesonlynotcontrary;62publication/executionStateLaw;latercurrentnessheld'''
parsed={}
for line in notes.splitlines():
 id,pages,note=line.split('|',2);parsed[id]={'source_pages':pages,'manual_limb_checks':note}
regs=json.loads((D/'rule-register.json').read_text());assert set(parsed)=={r['id'] for r in regs},(set(parsed)^{r['id'] for r in regs})
coverage=[]
for r in regs:
 item={'id':r['id'],'act_article':r['act_article'],**parsed[r['id']],'status':'changes_required' if r['id'] in {'I15','C07','C11'} else 'supported_with_stated_partial_scope','reviewed_guide_placements':[],'ledger_row_present':False}
 for slug in r['guide_placements']:
  f=Path('skills/republic-of-congo')/(slug+'.md'); t=f.read_text(); lines=[i for i,l in enumerate(t.splitlines(),1) if re.search(r'\bledger '+r['id']+r'\b',l)]
  assert lines,(r['id'],slug)
  item['reviewed_guide_placements'].append({'file':str(f),'lines':lines,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
  ledger=(D/(slug+'.md')).read_text(); assert '| '+r['id']+' |' in ledger
  item['ledger_row_present']=True
 coverage.append(item)
(O/'rule-coverage.json').write_text(json.dumps({'reviewed_head':'5ca4e55e6d601b99dad0d1b73e3f5d2688e4717a','base':'59c23acba2ad66dd2bb29ffc81ffbb9289769ef8','grouped_records':len(coverage),'meaning':'Grouped records are not represented as a count of individual figures. Every stated numeric and conditional limb was read, with source pages and caveats below; all indexed Guide rows and ledger counterparts were checked. Example and prose placements were separately read and are recorded in cases.json and review.md.','rows':coverage},indent=2)+'\n')
print('Recorded',len(coverage),'rule rows and',sum(len(x['reviewed_guide_placements']) for x in coverage),'indexed Guide placements')
