from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
from datetime import date,timedelta
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');cs=[]
def c(id,a,b,scope):assert a==b,(id,a,b);cs.append({'id':id,'actual':str(a),'expected':str(b),'scope':scope,'pass':True})
c('R78.nondeductibletrip',D(50000)*D('.00002')*100,D(100),'Actualnonqualifyingfamilyhome-tripdeductionexceptionnotavailable;listprice/minimumelectricselectors independentlymet.')
c('R78.deductibletrip',D(0),D(0),'Actualspecified9(1)no5s5/6deductionwouldbeavailable;8(2)s5excludesits0.002valuation,notallothercarbenefits.')
c('R79.preallowance',D(2000)*D('.96')-D(500),D(1420),'Actual8(3)qualifyinggoods/servicesnotpredominantlyforstaff/not40;applicablepublicendprice2000/employee500.')
c('R79.taxable',max(0,D(1420)-D(1080)),D(340),'Fullannualallowanceremaining,notduplicatedperitemorwithmonthly50cliff.')
c('R79.exhaustedallowance',max(0,D(1420)-D(0)),D(1420),'Annualallowancealreadyusedelsewhereinsameemployment.')
c('R79.employeehigher',max(0,D(2000)*D('.96')-D(2000)-D(1080)),D(0),'No negativetaxablebenefitfromemployeepayment.')
c('R80.twoadultoccupants',D(285)*(1-D('.4')),D(171),'Otherwiseordinaryadultsharedlodging,notdwelling/household/apprenticespecialcase;beforeemployeepayments.')
for rate,expected in[('.15','242.25'),('.5','142.5'),('.6','114')]:c('R80.selectedreduction'+rate,D(285)*(1-D(rate)),D(expected),'Singleactualstatutoryreductionfixture;noinventeduniversalcombinedfactor.')
c('R80.dailybase',(D(285)/30).quantize(D('.01'),rounding=ROUND_HALF_UP),D('9.50'),'Shortperioddaily1/30statutorycalculation.')
c('R80.twopersondaily',(D('9.5')*D('.6')).quantize(D('.01'),rounding=ROUND_HALF_UP),D('5.70'),'Actual40%reductionapplieddaily,two-decimalrules.')
c('R80.threedays',D('5.70')*3,D('17.10'),'Stipulatedthreelodgingdays,notinvented365fraction.')
c('R81.affiliatedbase',max(D(600),D(960)),D(960),'IndependentlyestablishedcostinclVAT600andactual8(3)s1value960;affiliatedrecipientemployee.')
c('R81.affiliatedtax',D(960)*D('.30'),D(288),'37bselectedeligiblebenefit/capsandothergatesmet;notlowercostbase180.')
for additional,expected in[(True,True),(False,False)]:c('R82.computer'+str(additional),additional,expected,'Otherwiseeligibleoutrightdataprocessingdevicetransfer25%route;salarysacrificefailsadditionality.')
c('R82.publictransportalternative',True,True,'Otherwiseactual3no15benefit/annualuniform25%election,additionalitynotrequired;noautomaticnondeductibleforeignbenefit.')
c('R82.recreationfamilycap',D(156)+D(104)+2*D(52),D(364),'Actualemployee/spouse/twochildrenaggregatecalendarcaps;recreationaluseensuredseparately.')
c('R82.recreationaggregate',D(200)+D(200)<=D(364),False,'Earlier200+current200exceedsstipulatedfamilycap;rateeligibilitynotanassumedexcess-onlyallowance.')
c('R83.2016increment',min(D(700)*D('.3'),D(288),D(700)-D(600)),D(100),'Actualsameemployer2016additional600/current700;all100(3)vehicle/payout/pay-time/distributioncostgatesmet.')
c('R83.no2016',min(D(700)*D('.3'),D(288)),D(210),'No2016additionalcontributioncase;otherevidencegatesindependentlyestablished.')
for amount,expected in[(240,True),(239,False)]:c('R83.minimum'+str(amount),amount>=240,expected,'Actualadditionalannualemployercontributionminimum,notautomaticentitlementfromamountalone.')
c('R83.proportionalrepayment',D(100)*D('.4'),D(40),'Independentlytraced40%ofsubsidisedcontributionreturnedafterfundedentitlementlapse;notuniversalarbitraryrefundallocation.')
c('R84.ordinary8',D(101400)*D('.08'),D(8112),'Qualifyingordinarycurrentyearfirstemployment/payout/electiongates;specialroutesnotstackedbyassumption.')
c('R84.ordinary4',D(101400)*D('.04'),D(4056),'ActualordinarySVthresholdretained;nopositivespecialterminationSVexemptioninvented.')
c('R84.termination2',D(101400)*D('.04')*min(2,10),D(8112),'Actual63sentence3twoqualifyingemploymentcalendaryears;notadditiontootherswithoutinteractionreview.')
c('R84.termination11',D(101400)*D('.04')*min(11,10),D(40560),'Actual63sentence3tenyearcap,nocopyto40bspecialformula.')
c('R84.suspended2',D(101400)*D('.08')*min(2,10),D(16224),'Actualqualifying2suspendedfirstemploymentyears/noGermantaxablepayfromemployer;separatetaxrouteonly.')
c('R84.pooled', (D(1500)+D(1900))/2,D(1700),'Eachactualworker≤2148,pooledaverage≤1752;firstemploymentandother40bgatesstipulated.')
c('R84.poolexclusion',D(2149)>D(2148),True,'Strict>2148workerexcludedfromstatutoryaveraging.')
c('R84.40btermination',D(1752)*3-D(2000),D(3256),'Actual3calendar-yearterminationmultiplierlessindependentlyestablishedcurrent+6prior-yearrelevantflattaxed2000;notinventedtenyearcap.')
c('R85.qualifyingdecline',min(D(8000),D(5000)-D(1000)),D(4000),'Actualbusiness-relateddecline/noexcludedcorporatemeasure;otherevent/eligibilityfactsestablished.')
c('R85.excludeddecline',D(8000),D(8000),'Stipulatednon-business/corporatemeasuredeclinedoesnotuse19a4s4/5lower-valueexception;ordinarydeferredbenefitpremise8000.')
c('R85.gifttrigger',True,True,'Actualwholeorpartialunpaidtransferunder4s1no1isanevent,nosalepriceprerequisite.')
c('R85.consent',False,False,'Noemployeeconsentinpayrollmeansno19a2provisionalnon-taxation;notlaterreturncure.')
c('R85.groupold21',21<=20,False,'Actualgroupcompanyagegate;financial/headcountincorporateddefinitionnotguessedAND/ORvector.')
for law,exempt in[('other-state',True),('German',False)]:c('R86.applicablelaw'+law,law=='other-state',exempt,'ValidbindingA1scopeindependentlyestablished;foreignlawmeansnoadditionalGermanSV,whileGermanoutboundrequiresactualGermanbenefitrulesnotautomaticpositivecharge.')
c('R87.separatestatus',not False,True,'Noemployment-basedcontributiondoesnotimplynoself-employedinsurance;actualseparateSGBVI2/healthselectorsmustbedetermined,notassumedforrealperson.')
qs=json.loads((W/'source-quote-index.json').read_text());qc=[]
for id,q in qs.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256']
 if q.get('native_LF')is None:
  assert id=='R69.SGBX26'and q['exact_quote']in json.loads(Path(q['raw_path']).read_text())['result'];kind='Faithful operative WebL13 in retained official web-tool response JSON, not rawHTML'
 else:
  a,b=q['native_LF'];literal='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert q['exact_quote']in literal,(id,'literal');kind='Exact operative quotation within declared nativeLF range'
 qc.append({'id':id,'identity_and_quote_pass':True,'kind':kind,'own_new_selected':not id.startswith(('A.','B.'))})
ops=json.loads((W/'exact-operations.json').read_text());proofs=json.loads((W/'preservation-proof.json').read_text());invs=json.loads((W/'successor-inventory.json').read_text());pairchecks=[]
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def mod(n,p):s=importlib.util.spec_from_file_location(n,str(p));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ce=mod('R62_examples',R/'scripts/check-examples.py');vg=mod('R62_schema',R/'scripts/validate-guides.py')
for inv in invs:
 s=inv['slug'];p=Path(inv['Guide_path']);before=(W/'before'/p.name).read_text();after=p.read_text();assert H(p)==inv['Guide_sha256'];x=before
 for op in ops[s]:assert x.count(op['before'])==1;x=x.replace(op['before'],op['after'],1)
 assert x==after
 for op in reversed(ops[s]):assert x.count(op['after'])==1;x=x.replace(op['after'],op['before'],1)
 assert x==before
 rows=json.loads((W/'support'/s/'rows.json').read_text());lines=after.split('\n')
 for q in rows:
  a,b=q['native_LF'];assert q['wording']=='\n'.join(lines[a-1:b]);assert all(k in qs for k in q['source_quote_ids'])
 assert len(set(q['prior_row_id']for q in rows if q['prior_row_id']))==inv['prior_rows']
 heading='## Worked cases'if s=='germany-payroll'else'## Worked examples'
 def worked(t):a=t.index(heading);b=t.find('\n## ',a+3);return t[a:b]
 assert worked(before)==worked(after);assert re.findall(r'```oa-check.*?```',before,re.S)==re.findall(r'```oa-check.*?```',after,re.S)
 beforefm=before.split('---',2)[1];afterfm=after.split('---',2)[1];assert re.sub(r'version: [^\n]+','version: X',beforefm)==re.sub(r'version: [^\n]+','version: X',afterfm)
 base=A if s=='germany-payroll'else B;old=json.loads((W/'support'/s/'old-topic-destinations.json').read_text());prior=json.loads((base/'support'/s/('old-topics.json'if base==A else'old-topic-destinations.json')).read_text())
 if base==A:
  assert len(old)==len(prior)
  for a,b in zip(old,prior):assert all(a[k]==b[k]for k in ['ref','old_lf','section','wording']);assert a['prior_sealed_destination']==b['destination']
 else:
  for key in ['earliest_created_rows','current_main_rows']:
   assert len(old[key])==len(prior[key])
   for a,b in zip(old[key],prior[key]):assert all(a[k]==b[k]for k in b if k!='current_destination');assert a['prior_sealed_destination']==b['current_destination']
 assert H(Path(inv['ledger_path']))==inv['ledger_sha256'];n,fail=ce.check_file(str(p));assert n==proofs[s]['actual_original_oa_blocks']and not fail
 es=[];ws=[]
 with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),es,ws,only_files={str(p.relative_to(R))})
 assert not es and not ws;d=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert d.returncode==0
 pairchecks.append({'slug':s,'ops':len(ops[s]),'all_native_rows_full_inverse_old_identities':True,'original_worked_section_and_oa_exact':True,'oa_blocks':n,'oa_failures':fail,'schema_errors':es,'schema_warnings':ws,'diff_returncode':d.returncode,'schema_stdout':out.getvalue()})
priorchecks=[]
for base,filename in [(B,'artifact-manifest.json')]:
 m=json.loads((base/filename).read_text())
 for e in m:assert H(base/e['path'])==e['sha256']
 priorchecks.append({'manifest':str(base/filename),'sha256':H(base/filename),'members':len(m),'mismatches':0})
checks={'role':'writer only, different independent review pending','controls':cs,'control_count':len(cs),'own_selected_quote_records':18,'source_checks':qc,'pairs':pairchecks,'original_writer_manifests':priorchecks};dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f"""# Germany benefits DE-R78–87 writer successor

Selected narrow A qualifies existing ordinary benefit methods: deductible family-home-trip exception, exact staffdiscount/payment/annualallowance formula, lodging reductions/dailyrounding/dwelling distinction, affiliated37bminimumvalue/noaffiliatedthirdpartySVexemption, precise40flat-taxgates,100firstemployment/2016increment/repayment conditions, ordinaryversusspecialpensionroutes,19apaid/unpaidtransfer/group/declinevalueconditions, A1direction and employment-statusversusseparateinsurance duties. No SMEfinancial Boolean is guessed; no specialtaxfreepensionpayment is assigned an inventedSVexemption. German-lawoutboundA1continuesapplicableGermanrules, not automaticbenefitcontributionexemption.

Sixteenown selected operative quotations read29October2026;twoexactown7a/24readings reused by explicit R72bridge. All original-languageclauses/officialURLs/read dates/raw-readerhashes in own-actual-read-quotes.json; DVKA administrativeguidance is notmislabelledRegulationtext. No new acquisition or wholebodyreadingclaim.

Guide/ledger exactpins: successor-inventory.json. Twenty-one canonicalops including0.2→0.3 inverttoexactpreimage. All90priorcurrentunits/73earliest-created+currentmainoldorigins preserved;oneprecisenewstaffdiscountrowgives91current. No nonexistentpre-additionGuideis invented. Original2oa/fullworkedsection/amounts/algebra/URLs/order/CTA/trust/bylines/protectedmetadata pass. {len(cs)}own separatingcontrols,allsource/nativechecks/scoped schema0/0/examples/diff pass;all515originalBmembersunchanged. Genuine original source-specificreservations preserved. Writercorrectionpending C'sdifferentexactreview,notcountryPASS/publication. NoFrancewriting.

Separators include staffprice2000/payment500→1420beforeallowance/340taxable;twoadultlodgingoccupants285×60%=171each;affiliated37bcost600/value960→288tax;2016additional600/current700caps100subsidyat100;twostatutoryterminationyears4%ceiling→8112taxroutewithoutassumedSVrelief;qualifyingdeferred8000/fair5000/payment1000→4000;gifttransfertriggers19a;GermanA1isnotzeroSV. Existing real-person/application-specificfactsremaininputs.
""")
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'writer successor, independent review pending','artifacts':entries});f={'status':'writer successor, independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pairs':invs,'controls':len(cs)};dump(W/'freeze.json',f);print(json.dumps({**f,'freeze_sha256':H(W/'freeze.json')},indent=2))
