from pathlib import Path
import re,json,hashlib,html,shutil
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[5];E=R/'evidence/research/gibraltar-2026/completion-2026-10-31';D=E/'evidence-repair-1';D.mkdir(exist_ok=True)
urls=json.loads((E/'source-urls.json').read_text());urls['oecd']='https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/12/tax-challenges-arising-from-digitalisation-of-the-economy-global-anti-base-erosion-model-rules-pillar-two_eed81a23/782bac33-en.pdf';urls['index']='https://www.gibraltarlaws.gov.gi/legislations/global-minimum-tax-act-2024-7478';urls['old404']='https://tax.egov.gi/Downloads/Guidance_Note_Pillar_Two.pdf'
files={'act':'global-minimum-tax-act','allowances':'allowances-rules','ita':'income-tax-act','oecd':'oecd-model-rules','registration':'pillar-two-registration','notification':'pillar-two-notification','gir':'pillar-two-gir','payment':'pillar-two-payment'}
raw={k:(E/'sources'/(n+'.txt')).read_text() for k,n in files.items()}
source_paths={k:E/'sources'/(n+'.txt') for k,n in files.items()}
raw['index']=(D/'sources/gmta-index.html').read_text();source_paths['index']=D/'sources/gmta-index.html'
raw['old404']=(D/'sources/old-registration-404.html').read_text();source_paths['old404']=D/'sources/old-registration-404.html'
# Preserve response status/date, omit the unsolicited anonymous load-balancer cookie from published headers.
for name in ['gmta-index','old-registration-404']:
 p=D/'sources'/(name+'.headers');private=R.parent/(name+'.original-response-headers.txt')
 if p.exists() and not private.exists():shutil.copyfile(p,private)
 if p.exists():p.write_text(''.join(l for l in p.read_text().splitlines(keepends=True) if not l.lower().startswith('set-cookie:')))
norm={};mapping={}
for k,t in raw.items():
 words=list(re.finditer(r'\S+',t)); n=[];m=[]
 for i,w in enumerate(words):
  if i:n.append(' ');m.append(w.start()-1)
  n.append(w.group());m.extend(range(w.start(),w.end()))
 norm[k]=''.join(n);mapping[k]=m
rows=json.loads((E/'ledger.json').read_text()); fixed=[]
def unit(k,start,end,claim,locator,after=None):
 n=norm[k];offset=n.index(after) if after else 0
 try:a=n.index(start,offset);b=n.index(end,a)+len(end)
 except ValueError as x:raise ValueError((k,start,end,after)) from x
 ra=mapping[k][a];rb=mapping[k][b-1]+1;q=raw[k][ra:rb]
 assert q in raw[k]
 return {'subclaim':claim,'act_article_or_document_section':locator,'official_url':urls[k],'read_on':'2026-10-31','original_language':'English','reader_file':str(source_paths[k].relative_to(R)),'reader_sha256':hashlib.sha256(raw[k].encode()).hexdigest(),'reader_lines':[raw[k][:ra].count('\n')+1,raw[k][:rb].count('\n')+1],'physical_pdf_pages':[raw[k][:ra].count('\f')+1,raw[k][:rb].count('\f')+1] if k in files else None,'quote':q,'quote_sha256':hashlib.sha256(q.encode()).hexdigest()}
def U(k,start,end,claim,loc,after=None):return unit(k,start,end,claim,loc,after)
P={}
P['commence']=U('act','2.(1) This Act','31 December 2024.','General fiscal-year application and separately dated IIR commencement, inclusive on/after','GMTA s2(1)–(3)')
P['threshold']=U('oecd','The GloBE Rules apply to Constituent Entities','Entities that are Excluded Entities are not subject to the GloBE Rules.','750million, two/four years, special Article6.1 and proportionate non12month threshold; excluded entities','Model Rules art1.1.1–1.1.3')
P['domestic']=U('act','“Wholly Domestic Group” means','immediately preceding the tested Fiscal Year.','All entities/UPE located Gibraltar and750million in two/four preceding years','GMTA s3(1), Wholly Domestic Group definition')
P['location']=U('act','(4) For the purposes of this Act, the location','Article 10.3.','Entity location follows Model Rules10.3','GMTA s3(4)')
P['part4']=U('act','15. A Wholly Domestic Group is treated as an MNE Group for the purposes of Part 4.','15. A Wholly Domestic Group is treated as an MNE Group for the purposes of Part 4.','Domestic group MNE treatment is for Part4','GMTA s15')
P['iir']=U('act','12. An Ultimate Parent Entity','the MNE Group that includes the Ultimate Parent Entity, Intermediate Parent Entity or Partially Owned Parent Entity.','Listed parents charged under IIR and Model Rules','GMTA s12')
P['utpr']=U('act','13. The following provisions','international activity).','UTPR charging Articles2.4–2.6 and9.3 disapplied from Part3','GMTA s13')
P['investment']=U('act','14. This Part does not apply','Insurance Investment Entities.','Investment/Insurance Investment exclusion for Part4','GMTA s14')
P['joint']=U('act','16. Each Domestic Constituent Entity','determined under this Part.','Domestic constituent joint liability and fiscal-year scope','GMTA s16',after='14. This Part does not apply')
P['jv']=U('act','17. Each Domestic Joint Venture','determined under this Part.','Separate domesticJV/subsidiary joint liability','GMTA s17')
P['aa1']=U('allowances','3AA.(1) An election','Global Minimum Tax Act 2024.','Parent must be in scope of both Acts','Allowances r3AA(1)')
P['aa2']=U('allowances','(2) Where there is an Approved Election','Constituent Entities of that Group.','Only specified charge-levying provisions disapplied for rule9 periods, parent and constituents','Allowances r3AA(2)',after='3AA.(1)')
P['aa3']=U('allowances','(3) For the purposes of this rule','(b) is an Ultimate Parent Entity.','Parent is constituent ordinarily resident/registered/established Gibraltar and UPE','Allowances r3AA(3)',after='3AA.(1)')
P['aa4']=U('allowances','(4) An Approved Election is one made','approved in writing by the Commissioner.','Written request and written approval','Allowances r3AA(4)',after='3AA.(1)')
P['aa56']=U('allowances','(5) An Approved Election is valid','requirements of this rule are met.','Effective approval date and mandatory approval when requirements met','Allowances r3AA(5)–(6)',after='3AA.(1)')
P['aa78']=U('allowances','(7) If the Commissioner rejects','(c) state the grounds of appeal.','Rejection appeal to both recipients,30day notification trigger and grounds','Allowances r3AA(7)–(8)',after='3AA.(1)')
P['aa9']=U('allowances','(9) An Approved Election is effective','Income Tax Act 2010 is not yet due.','Basis periods starting after election; older periods only when return not yet due on election date','Allowances r3AA(9)',after='3AA.(1)')
P['aa10']=U('allowances','(10) The election shall cease','the election not remaining valid.','Cessation through parent notification or unmet conditions with Commissioner reasons','Allowances r3AA(10)',after='3AA.(1)')
P['aa1114']=U('allowances','(11) An election made','provided that the conditions of this rule are met.','Conditional18months, first-awareness notification/reasonable steps, Commissioner validity determination, possible reelection','Allowances r3AA(11)–(14)',after='3AA.(1)')
P['aa15']=U('allowances','(15) The Commissioner may rely','rule after 1 March 2025 is an Approved Election.','PartVI/Schedule4 antiavoidance for elections after1March2025','Allowances r3AA(15)',after='3AA.(1)')
P['aa16']=U('allowances','(16) The terms','Model Rules (as appropriate).','Defined constituent/group/UPE import','Allowances r3AA(16)',after='3AA.(1)')
P['a55']=U('allowances','(55) Income that would otherwise be assessable to tax under the Income Tax Act 2010 where','an election under Rule 3AA.','Separate ordinary income exemption within approved-election context','Allowances r3(55)')
P['ita40']=U('ita','(6) (a) The Commissioner may counteract','provisions.','Election counteraction trigger and all three contextual considerations','ITA s40(6)(a)–(b)')
P['rate']=U('act','11. The Minimum Rate','shall be fifteen percent.','Statutory minimum15percent','GMTA s11')
P['modified']=U('act','18. The Top-up Tax','Chapters 2 through 4 of this Part.','Domestic calculation uses Model Rules subject to specified domestic modifications','GMTA s18')
P['interpret']=U('act','4.(1) The Model Rules','OECD Commentary including the Safe Harbours.','Model Rules have effect; interpretation refers to Commentary/safeharbours','GMTA s4')
P['timing']=U('act','6.(1) Amendments made','a legal notice published in the Gazette.','Commentary timing based on fiscal-year start after approval or other ministerial notice, including inapplicability notices','GMTA s6')
P['elections']=U('act','7. Elections made','same effect for the purposes of this Act.','GIR elections have same computation effect','GMTA s7')
P['fx']=U('act','8. If the Top-up Tax','Year to which the Top-up Tax relates.','Sterling conversion at fiscal-year average, no numeric FX rate prescribed','GMTA s8')
P['disapply']=U('act','19. The following provisions','international activity).','All listed domestic disapplications including Article5.2.3 formula and allocations','GMTA s19')
P['safe']=U('act','20. The QDMTT Safe Harbour','purposes of this Part.','Only Part4 QDMTT safeharbour exclusion established by this provision','GMTA s20')
P['foreign']=U('act','21. Notwithstanding Article 4.3.2','and member of a Domestic JV Group.','Foreign owner/mainentity taxes excluded from Gibraltar adjustedcoveredtaxes','GMTA s21')
P['outgoing']=U('act','22. The Adjusted Covered Taxes','after taking into account Article 4.3.3).','Domestic owner/mainentity taxes allocated to foreign entities excluded','GMTA s22')
P['pools23']=U('act','23. The Top-up Tax','Domestic Joint Ventures or Domestic JV Subsidiaries.','Separate constituent totals excludeJV totals','GMTA s23')
P['pools24']=U('act','24. The Top-up Tax','calculated for that Domestic JV Group.','JV total uses separateJV computation','GMTA s24')
P['formula']=U('act','25. There shall be separate','(Top-up Tax Percentage x Excess Profits) + Additional Current Top-up Tax','Minorityowned,JV and other pools; domestic formula including additional tax','GMTA s25')
P['26']=U('act','26.(1) For the purposes of Part 3','form made available by the Commissioner.','15/18months both conditions, UPE/DFE group filer and prescribed supporting information','GMTA s26(1)–(3)')
P['27']=U('act','27.(1) Except as otherwise provided','form made available by the Commissioner.','Part4 statutory15/18month conditions, appointed DLE for all local entities/JVs and information','GMTA s27(1)–(3)')
P['28']=U('act','28.(1) For the purposes of Part 3','form made available by the Commissioner.','Actual overseas GIR/effective reportingyearQCAA, specified Part3/4 notifiers,3month deadline and attachments','GMTA s28(1)–(4)')
P['29']=U('act','29.(1) The Top-up Tax','Domestic Joint Ventures, and Domestic JV Subsidiaries.','GIR deadline payment; Part3 parents/joint liability, Part4DLE payer','GMTA s29(1)–(3)')
P['30']=U('act','30.(1) A person required','notification, as the case may be.','GIR and notification record duty and10year period from FYend','GMTA s30')
P['3335']=U('act','33. Subject to the provisions','under this Act.','Assessment/amendment10years and ITA35 imported appeals','GMTA ss33–35')
P['36']=U('act','36. Subject to section 34','amount of Top-up Tax assessed.','Finality subject to valid appeal ands34','GMTA s36')
P['52']=U('act','52.(1) If it be proved','repayment to be made accordingly.','Overpayment entitlement, tenyear endpoint and Commissioner certification/payment','GMTA s52(1)–(3)')
P['ita61']=U('ita','61.(1) If it be proved','repayment to be made accordingly.','Separate ordinary income-tax claim period sixyears from relevant year/accountingperiodend','ITA s61(1)–(3)')
P['44']=U('act','44.(1) If the Top-up Tax','due and payable.','2percent dayafterdue; later30day trigger5percent of remaining tax and firstsurcharge','GMTA s44(1)(a)–(b)')
P['43']=U('act','43. An Ultimate Parent Entity','as required in accordance with this Act.','1000failurefile/notify, statutory shallmay wording retained','GMTA s43')
P['45']=U('act','45.(1) A person who fails','confirm or set aside the penalty.','5000recordfailure and Magistratesappeal','GMTA s45')
P['47']=U('act','47.(1) This section applies','sections 38 or 39.','Noticefailure500, further1000afterone-month trigger, meaning of submissiondate and appeals','GMTA s47')
P['48']=U('act','48. Notwithstanding any other provision','carrying out his duties under this Act.','Conditional discretionary penalty relief; no automatic waiver','GMTA s48')
P['49']=U('act','49.(1) A penalty under this Part','recoverable as a civil debt.','Penalty payment30day trigger and enforcement','GMTA s49')
# Original group IDs stay fixed; attach responsive subclaim evidence rather than replace with another generic fragment.
keys={1:['commence'],2:['threshold'],3:['domestic','location','part4'],4:['iir','utpr','investment','joint','jv'],5:['aa1','aa3','aa16'],6:['a55','aa2','aa4','aa56'],7:['aa9','aa56'],8:['aa78'],9:['aa10','aa1114'],10:['aa15'],11:['ita40'],12:[],13:['rate','modified'],14:['interpret','timing','disapply','safe','foreign','outgoing','pools23','pools24','formula','fx'],15:['elections'],16:['26','27'],17:['28'],18:['29'],19:['26','27','28','29'],20:[],21:[],22:[],23:[],24:[],25:[],26:['30','3335','36'],27:['52','ita61'],28:['44'],29:['43','45','47','48','49'],30:['commence','location','foreign','outgoing','28'],31:['fx','formula'],32:['44'],33:[],34:[],35:[]}
for i,r in enumerate(rows,1):
 r=dict(r);r.pop('quote');r['evidence']=[P[k] for k in keys[i]];r['classification']='tax rules and stated conditions';r['status']='writer evidence repaired; bounded independent closure pending';r['supersedes_fragment_only']=True
 fixed.append(r)
# Explicit process/inference/assumption classification, not a legal absence claim.
for i in [12,33,34]:fixed[i-1]['classification']='writer process/research boundary; not a statutory obligation or legally proved absence'
fixed[11]['process_note']='Retained election-channel research boundary. Rule3AA supports the written election/approval duties in GMT05–10; the Guide does not claim that no channel exists. No unrelated statutory quotation is used to prove a negative.'
fixed[32]['process_note']='Writer/client evidence checklist. No claim that every checklist item is a separately prescribed statutory filing requirement. Legal tests are evidenced in GMT01–29.'
fixed[33]['process_note']='Writer self-check controls crossreferencing GMT01–29. No additional statutory duty, rate or deadline.'
for i in [3,7,19,27,28,31,32]:fixed[i-1]['illustrations']='All scenario principal amounts, FX input, dates selected as assumptions and numerical outputs are writer examples, not official amounts. Recomputed independently in the unchanged initial review. No scenario establishes legal eligibility.'
fixed[14]['scope_note']='The final sentence excluding full safeharbour/deferredtax/IIR derivation is a writer scope declaration, not an exemption from those rules.'
# Extra registration evidence, granular for every numbered workflow limb.
def add(i,k,start,end,claim,loc,after=None):fixed[i-1]['evidence'].append(U(k,start,end,claim,loc,after))
add(20,'registration','The following MNE Groups','Form GMTAREG1 - Constituent Entity Template).','Registration scope,750million two/four years, onlyone group filer and local entity list','Registration guidance §3')
add(20,'registration','Each MNE Group should only register once in relation to Pillar Two.','required by 31 March 2026.','Initial cohort31Dec2024–31Aug2025,28Feb2026deadline; later6months with authority example','Registration guidance §4')
add(20,'registration','The following information is required for registration:','responsible person for GIR compliance.','All legalentity/DLE/Gibraltarentity, fiscalyear, responsible-person/contact/photoID/director-authorisation fields','Registration guidance §5')
add(20,'registration','As noted in question 5 above, the individual completing the registration process','notification (as applicable).','Authorised agent with identification/letter becomes authorisedGIR/notification filer','Registration guidance §6')
add(20,'registration','The Income Tax Office will review the registration form submitted','additional information and / or clarifications are required.','ITO reviews and contactsDLE; request is not final legal approval','Registration guidance §7')
add(20,'registration','In most cases, changes following registration','identify any changes in a given Fiscal Year.','Annualnotification/localGIR captures entitychanges when no annualnotification','Registration guidance §8',after='The Income Tax Office will review the registration form submitted')
add(20,'registration','9. What happens if an MNE Group','Pillar Two Rules.','Outofscope written reasons/email and6months FYend','Registration guidance §9',after='The Income Tax Office will review')
add(20,'registration','10. What happens if there is a change','notifications going forward.','DLE change annualnotification or writtenemail ASAP/12months, newenrolment','Registration guidance §10',after='The Income Tax Office will review')
add(20,'registration','1. Proceed to the HM Government','2. Select “GIR” and click on “enrolment”.','Portal URL andGIRenrolment','Registration Appendix1 steps1–2',after='Appendix 1:')
add(20,'registration','“Reporting Entity Name”','confirmations for your records if required.' if False else 'submission confirmation for your records if required.','All newenrolment fieldnames,Multinational/GIR/newcombined restriction,GMTAREG1includingfiler,roles,UPE,TIN,dd/mm,primaryuserIDauthority andpreserve screenshots','Registration Appendix1 formnotes',after='Appendix 1:')
add(20,'registration','1. Proceed to the HM Government','Please save a screenshot of the submission confirmation for your records if required.','ExistingCbC login,Filings/Create,GIRenrolment,fiscalperiod,form,validate-submit,confirmation; not duplicatecombinednewregistration','Registration Appendix2 steps1–10',after='Appendix 2: Pillar 2 Registration Process')
# Notification common-understanding limitation; obligation source separately included GMT17.
add(21,'notification','For the purposes of Part 3 and Part 4','will continue to increase in the coming weeks and months.','QCAA required, defaultlocalGIR, activatedOECDrelationship isproof not intention','Notification guidance §4',after='4. Jurisdictions which have')
add(21,'notification','Gibraltar is adopting the common understanding','local GIR filing obligations in Gibraltar.','Only2024reportingyear commonunderstanding circumstances andsection48penaltydiscretion','Notification guidance §4',after='4. Jurisdictions which have')
# A–G and every submit/correct control, split around concrete steps.
add(22,'notification','1. Proceed to the HM Government','used in registration will be displayed as follows:','GIRPortal registereduserlogin,verifyTINviaEntityManagement','Notification Appendix1 steps1–4',after='Appendix 1 – How to file')
add(22,'notification','5. Start a new','6. Complete the form.','Reports,Unscheduled,GIRDelegationArticle8.1.3,AddNewReport','Notification Appendix1 step5',after='Appendix 1 – How to file')
add(22,'notification','Complete sections A-G','see point 3 above).','AllA–Gfields,DLEbox,agenttitle/company,UPEalways,DFEonlywhenexchangethere,period,registeredTIN','Notification Appendix1 step6',after='Appendix 1 – How to file')
add(22,'notification','7. Download the draft form','JSON file format if required.','DraftJSON backup and optionalJSON upload','Notification Appendix1 step7',after='Appendix 1 – How to file')
add(22,'notification','8. Submit the notification.','Once accepted the submission status will change to valid as follows:','Previewvalidatesmissingfields,Reportsubmits,acceptedValidstatus','Notification Appendix1 step8',after='Appendix 1 – How to file')
add(22,'notification','9. Invalid submission','Revoke: Allows the user to revoke a notification previously made.','Invalidstatus/results,correct-resubmit,all5Actionsincludingedit/download/revoke','Notification Appendix1 steps9–10',after='Appendix 1 – How to file')
add(22,'notification','6. What happens after the Article','available to view on the online portal (see Appendix 1).','InitialvalidationversusITOreview; onlycontactifquestions','Notification guidance §6',after='5. How to submit a notification')
# GIR controls: exact statuteconditions are already above.
add(23,'gir','The same standardised GIR template','filed centrally in another jurisdiction.','Local/central schema anddissemination limited towhatGibraltarwouldreceive','GIR guidance §4')
add(23,'gir','A GIR filed in Gibraltar should','and local filing of a GIR in Gibraltar.','XMLformat forbothlocal/central','GIR guidance §5')
add(23,'gir','Please note that there is currently no testing environment.','forbidden character sequences (’—’, ’/*’, ’&#’).','Finalonlynotestportal; complete4localvalidationrules andcodes','GIR Appendix1 step1',after='Appendix 1 – How to file')
add(23,'gir','Please note that in relation to validation rule “40004”','where local filing applies.','TINmatchesregistration,DocRefIDuniquecomponent,correctlocalfilingrole/jurisdiction','GIR Appendix1 step1',after='Appendix 1 – How to file')
add(23,'gir','2. Proceed to the HM Government','GMTAnotifications@gibraltar.gov.gi','GIRPortalregisteredlogin,ReportsScheduledGIR,period andmissingperiodcontact','GIR Appendix1 steps2–5',after='Appendix 1 – How to file')
add(23,'gir','Click on the relevant reporting date','submitted GIR has passed the various validation checks.','UploadReport/Selectfile/Submit,ExportPDFreceiptthenconfirmSubmittedValid','GIR Appendix1 steps5–7',after='Appendix 1 – How to file')
add(23,'gir','Further details in relation to the submission','uploaded following the above steps.','Actionvalidationresults,rejectedXMLspecificmessages andcorrectedupload','GIR Appendix1 steps7–8',after='Appendix 1 – How to file')
add(23,'gir','9. Amending a GIR previously submitted','GMTAnotifications@gibraltar.gov.gi','AcceptedGIRamendment instructionsnotyetpublished;authoritycontactroute','GIR Appendix1 step9',after='Appendix 1 – How to file')
add(24,'payment','Gibraltar Top-up Tax Return','Date:','GMTA1allfields1–6,authoriseddeclaration/contact/capacity/signature/date','GMTA1 pp1–2')
add(24,'payment','Who is required to complete Form GMTA1?','GMTAreturns@gibraltar.gov.gi','Liabilitytrigger,separateGMTA1plusGIR/notification/CT1,duedateandemail','GMTA1 p3 notes')
fixed[23]['evidence']+=[P['26'],P['27']]
fixed[23]['comparison_note']='The form note abbreviates the18month condition. GMT16 statutory26/27 evidence governs both required tests; separate CT1 obligation is conditional, not a claim overriding approved rule3AA relief.'
add(25,'payment','Payment should be made by bank transfer only.','PROVIDED TO THE DESIGNATED LOCAL ENTITY.','Banktransferonly anduniqueassignedtopuptaxpaymentreference','GMTA1 p3 payment details')
add(25,'payment','Please contact the Income Tax Office','tax.accountsenquiries@gibraltar.gov.gi','Ifcannotpaybytransfer,ITOassistancephoneoption2andemail','GMTA1 p3 assistance')
fixed[24]['process_note']='Reconciliation and no-live-action statements are writer process declarations. A sentform/receiptisnotproof ofbankexecution or allocation; no statutory source is claimed for the writer having taken no action.'
fixed[29]['classification']='writer crossreference control with own-law tests identified; no additional statutory duty'
fixed[29]['process_note']='Separates previously evidenced legal tests; no general treaty claim is inferred from the GIRQCAA rule.'
# Specific current metadata/operational-gap evidence for GMT19 and35.
add(35,'gir','9. Amending a GIR previously submitted','GMTAnotifications@gibraltar.gov.gi','CurrentJune11accepted-amendmentinstructionisforthcoming/contactoffice','GIR Appendix1 step9',after='Appendix 1 – How to file')
add(35,'index','Global Minimum Tax Act 2024 <span>Current Version</span>','Global Minimum Tax Act 2024 <span>Current Version</span>','Official index displaysCurrentVersion label','Act index, current heading')
add(35,'index','<h5 class="text-center">This version is out of date </h5>','<h5 class="text-center">This version is out of date </h5>','Sameindexalso displaysoutofdateversionlabel','Act index, historical version heading')
for attr,after in [('src="https://www.gibraltarlaws.gov.gi/assets/vendor/viewerjs/?zoom=page-width#../../../uploads/legislations/minimum-tax/2024-20/2024-20o.pdf"','Global Minimum Tax Act 2024 <span>Current Version</span>'),('data-pdf="https://www.gibraltarlaws.gov.gi/assets/vendor/viewerjs/?zoom=page-width#../../../uploads/legislations/minimum-tax/2024-20/2024-20o.pdf"','This version is out of date')]:
 add(35,'index',attr,attr,'Bothdisplayedentrieslinkthesame2024-20oPDF','Act index, embeddedPDFtarget',after)
fixed[34]['classification']='mixed: metadata observation and explicit writer research limits, not legal exemptions'
fixed[34]['process_note']='FullGloBE/safeharbour/election/cessation/liveacknowledgement exclusions are scope declarations. Displayedindexlabels andidenticaltargets do not prove no laterGazettenotice exists. No fresh scopeacceptance inferred from2021ModelRules.'
fixed[18]['source_observations']={'exact_old_url':urls['old404'],'initial_dated_writer_record':'docs/research/2026-10-22-gibraltar-minimum-tax-sources.json','original_record_sha256':hashlib.sha256((R/'docs/research/2026-10-22-gibraltar-minimum-tax-sources.json').read_bytes()).hexdigest(),'initial_independent_review_limit':'docs/research/2026-10-22-gibraltar-minimum-tax-full-review.md explicitly didnot independentlyreproduce original404','31Oct_refetch_headers':'sources/old-registration-404.headers','31Oct_response_body':'sources/old-registration-404.html','classification':'HTTPsourceavailabilityobservation, not a tax-law proposition'}
fixed[18]['evidence'].append(U('old404','HTTP Error 404.0 - Not Found','HTTP Error 404.0 - Not Found','ExactoldURLcurrentlyreturns404;responseheaderrecordsHTTP404','Current31OctpublicHTTPresponse'))
fixed[18]['derivation']={'fiscal_year_end_assumption':'2024-12-31','ordinary_due':'2026-03-31','conditional_first_year_due':'2026-06-30','notification_due':'three months before the legally applicable GIRdeadline','conditions':'BothGMTA26/27firstsubjectyearandnopriorforeignGIRrequiredtests,notmerelyfirstGibraltarfiling','status':'arithmetic plus observed availability; not extension'}
# Preserve independent review report and all its inputs verbatim. Revised ledger is separate.
assert len(fixed)==35
for r in fixed:
 assert r['statement_sha256']==hashlib.sha256(r['statement'].encode()).hexdigest(),r['id']
 assert r['statement'] in (R/'skills/gibraltar/gi-global-minimum-tax.md').read_text(),r['id']
 for q in r['evidence']:assert q['quote'] in (R/q['reader_file']).read_text(),(r['id'],q['subclaim'])
(D/'ledger.json').write_text(json.dumps(fixed,indent=2,ensure_ascii=False)+'\n')
md=['# Gibraltar minimum-tax evidence repair1','', 'This revision supersedes only the generic fragments in the initial35row writer ledger. Initial writer files, initial independent report and allGuidebytes remain unchanged. Each operative excerpt below responds to the named subclaim; writer process/research boundaries and illustrative assumptions are separately labelled. Bounded independent closure is pending.','']
for r in fixed:
 md+=['## '+r['id']+' — '+r['act_article_or_document_section'],'','Classification: '+r['classification'], '', 'ExactGuideunitSHA256: `'+r['statement_sha256']+'`','']
 for name in ['process_note','scope_note','comparison_note','illustrations','derivation','source_observations']:
  if name in r:md+=[name+': '+(r[name] if isinstance(r[name],str) else json.dumps(r[name],ensure_ascii=False)),'']
 for j,q in enumerate(r['evidence'],1):
  md+=['### Evidence '+str(j)+': '+q['subclaim'],'',q['act_article_or_document_section']+'; '+q['official_url']+'; read '+q['read_on']+'; readerlines '+str(q['reader_lines'])+'; physicalpages '+str(q['physical_pdf_pages']), '', '```text',q['quote'],'```','']
(D/'ledger.md').write_text('\n'.join(md))
reviewfiles={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (E/'independent-review').rglob('*') if p.is_file()}
guides={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'skills/gibraltar').glob('*.md')}
assert guides['skills/gibraltar/gi-global-minimum-tax.md']=='c990bb86a134fbc3a20efb13f05f04cf7b3c8623f7e882c28dc835e990f39b26'
checkpoint=json.loads((E/'checkpoint.json').read_text())
for f,h in checkpoint['guide_files'].items():assert guides[f]==h,f
for f,h in checkpoint['evidence_files'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h,f
newfiles={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file() and p.name!='checkpoint.json'}
(D/'checkpoint.json').write_text(json.dumps({'reviewed_writer_commit':'393be24383a0fee17a7fcc3ea6a6bd2d87d4076a','all35_rows_repaired':True,'evidence_units':sum(len(r['evidence']) for r in fixed),'guide_bytes_unchanged':guides,'initial_review_files_unchanged':reviewfiles,'original_writer_checkpoint_sha256':hashlib.sha256((E/'checkpoint.json').read_bytes()).hexdigest(),'repair_files':newfiles,'closure':'pending','country_complete':False,'push':False},indent=2)+'\n')
print('repaired',len(fixed),'rows;',sum(len(r['evidence']) for r in fixed),'responsive evidenceunits; allGuideandinitialwritercheckpointbytes unchanged')
