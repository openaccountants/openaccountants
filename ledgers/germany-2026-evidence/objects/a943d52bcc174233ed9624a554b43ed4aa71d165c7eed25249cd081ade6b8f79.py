from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
from datetime import date,timedelta
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;P=O/'germany-DE-R62-R70-payroll-writer-successor-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');cs=[]
def c(id,a,b,scope):assert a==b,(id,a,b);cs.append({'id':id,'actual':str(a),'expected':str(b),'scope':scope,'pass':True})
from fractions import Fraction as F
c('R88.nominalSunday',date(2027,2,28).weekday(),6,'Statutory41b/93cdeadlineSunday,ordinaryfilingdeadline—notfixedauthorityappointment.')
c('R88.nextworkingday',date(2027,2,28)+timedelta(days=1),date(2027,3,1),'Combinedown108(3)ordinaryMondayadjustment;actualholiday/authorityfactsseparate,nofutureformclaim.')
for pay,total,er,ee in[(100,'32.55','15','17.55'),(175,'32.55','26.25','6.30'),(603,'112.16','90.45','21.71')]:
 base=max(D(pay),D(175));t=(base*D('.186')).quantize(D('.01'),rounding=ROUND_HALF_UP);e=(D(pay)*D('.15')).quantize(D('.01'),rounding=ROUND_HALF_UP)
 c('R89.total'+str(pay),t,D(total),'IsolatedfullmonthinsuredcommercialMini/nootherjob/exemption/partmonthinteraction;actual1638minimum.')
 c('R89.employer'+str(pay),e,D(er),'Employer15%ACTUALpay,not175floor.')
 c('R89.employee'+str(pay),t-e,D(ee),'BVV2minimum-baseemployeeREMAINDER,notuniversal3.6%actualpaybelow175.')
c('R89.scopeguard',False,False,'Anotherinsuredjob/partmonth/exemptioncaseisoutsidethisstatedordinaryminimumworksheet,notautomatic175perjob.')
for tariff,refund in[('.8',800),('.6',600),('.4',400)]:c('R90.tariff'+tariff,D(1000)*D(tariff),D(refund),'Stipulatedactualfundstatute/selectedtariffforeligiblecontinuedwage1000;employercontributionscope separate.')
c('R90.floor',D('.39')>=D('.40'),False,'Fundstatuteauthorityrestricts80%defaultwithratesnotbelow40%;notguessingactualfundtariff.')
a=F(8450)*8450/10450;z=F(8450)*2000/10450
c('R91.precapfirst',min(10000,8450),8450,'Actualordinarypensionjobprecapbeforeproportion,notraw10000.')
c('R91.base1',a,F(1428050,209),'Exactrationalintermediate,notprematurerounding.')
c('R91.base2',z,F(338000,209),'Exactrationalintermediate,notraw2000/12000allocation.')
c('R91.sum',a+z,F(8450),'Commonordinarypensionceilingconserved;minersseparate.')
c('R91.wrongraw1',a!=F(8450)*10000/12000,True,'Separatesactualprecapfromuncapped2jobalgorithm.')
for same,ordinary,w in[(True,True,False),(False,True,True),(True,False,True)]:c('R92.sameemployer'+str((same,ordinary)),not(same and ordinary),w,'Onlyactual40a4no2bar;allother25%/farm5%gatesindependentlymet. Differentemployerdoesnotautomaticallybarunderthisclause.')
for both,notsep,following,w in[(True,True,True,True),(False,True,True,False),(True,False,True,False),(True,True,False,False)]:c('R93.widow'+str((both,notsep,following)),both and notsep and following,w,'BothactualstatutoryunlimitedtaxcategoriesandnotpermanentlyseparatedATDEATH;followingcalendaryear,notresidencealone.')
for months,bothmissing,w in[(3,True,False),(4,True,True),(4,False,False)]:c('R93.retroVI'+str((months,bothmissing)),months>3 and bothmissing,w,'Actualtemporary-data/nofaultbranch;fixturebothID/DOBstillmissing. Do notautomaticallyimposeretroVIonpuretechnicalproblemwithactualdataprovided.')
c('R93.catchupdeduct',D(1200)-D(1000),D(200),'Stipulatedactualpriorrecalculation1200versus1000withheld;differenceinNEXTpayroll,notalwayszeroorreturnonly.')
c('R93.catchuprefund',D(800)-D(1000),D(-200),'Stipulatedcorrectprior800versus1000withheld;negativeadjustmentrefundinNEXTpayroll.')
combined=D(60)+D(40);top=combined-D(13)
c('R94.combined',combined,D(100),'Independentlyestablishednetdailyinputsfromlast3settledcalendarmonths;notinventedgrossnetconversion.')
c('R94.total',top,D(87),'Subtract13onceacrossallrelevantemployers.')
c('R94.AG1',top*D(60)/combined,D('52.20'),'ProportionateactualAG1dailywage.')
c('R94.AG2',top*D(40)/combined,D('34.80'),'ProportionateactualAG2dailywage;notdeduct13again.')
c('R94.sum',top*D(60)/combined+top*D(40)/combined,D(87),'Combinedtopupconserved;special20(3)/(4)selectorsseparate.')
for fullyear,staff,w in[(True,10,True),(False,10,False),(True,9,False)]:c('R95.mandatory'+str((fullyear,staff)),fullyear and staff>=10,w,'Allotheractual42bexclusionsabsent. Nine-staffcasecanbepermitted,justnotcompelledbysize;noobsoleteunlimitedtaxgateinvented.')
c('R96.UVonly',True,True,'Statutorysolelyaccident-datachangeexceptiontonotification,notallreportsexcepted.')
c('R96.terminationclock','immediately after last report','immediately after last report','Actualterminationcopyclock,notpostponedtonextannual30April;nofictionalportal/runtimeclaim.')
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
 assert set(q['immediate_predecessor_id']for q in rows if q['immediate_predecessor_id'])==set(q['id']for q in json.loads((P/'support'/s/'rows.json').read_text()))
 heading='## Worked cases'if s=='germany-payroll'else'## Worked examples'
 def worked(t):a=t.index(heading);b=t.find('\n## ',a+3);return t[a:b]
 assert worked(before)==worked(after);assert re.findall(r'```oa-check.*?```',before,re.S)==re.findall(r'```oa-check.*?```',after,re.S)
 beforefm=before.split('---',2)[1];afterfm=after.split('---',2)[1];assert re.sub(r'version: [^\n]+','version: X',beforefm)==re.sub(r'version: [^\n]+','version: X',afterfm)
 base=P;old=json.loads((W/'support'/s/'old-topic-destinations.json').read_text());prior=json.loads((base/'support'/s/'old-topic-destinations.json').read_text())
 if s=='germany-payroll':
  assert len(old)==len(prior)
  for a,b in zip(old,prior):assert all(a[k]==b[k]for k in ['ref','old_lf','section','wording']);assert a['R88_immediate_predecessor_destination']==b['destination']
 else:
  for key in ['pre_refresh_rows','current_main_rows']:
   assert len(old[key])==len(prior[key])
   for a,b in zip(old[key],prior[key]):assert all(a[k]==b[k]for k in b if k!='current_destination');assert a['R88_immediate_predecessor_destination']==b['current_destination']
 assert H(Path(inv['ledger_path']))==inv['ledger_sha256'];n,fail=ce.check_file(str(p));assert n==proofs[s]['actual_original_oa_blocks']and not fail
 es=[];ws=[]
 with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),es,ws,only_files={str(p.relative_to(R))})
 assert not es and not ws;d=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert d.returncode==0
 pairchecks.append({'slug':s,'ops':len(ops[s]),'all_native_rows_full_inverse_old_identities':True,'original_worked_section_and_oa_exact':True,'oa_blocks':n,'oa_failures':fail,'schema_errors':es,'schema_warnings':ws,'diff_returncode':d.returncode,'schema_stdout':out.getvalue()})
priorchecks=[]
m=json.loads((P/'artifact-manifest.json').read_text())['artifacts']
for e in m:assert H(P/e['path'])==e['sha256']
priorchecks.append({'manifest':str(P/'artifact-manifest.json'),'sha256':H(P/'artifact-manifest.json'),'members':len(m),'mismatches':0})
checks={'role':'writer only, different independent review pending','controls':cs,'control_count':len(cs),'own_selected_quote_records':15,'source_checks':qc,'pairs':pairchecks,'original_writer_manifests':priorchecks};dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f"""# Germany payroll DE-R88–96 writer successor

Selected narrow A supplies the combined-law1March2027certificate deadline, qualified175Minijobminimum/employee remainder, actualU1fundtariff restriction of statutory80%(40%floor), each-jobprecapbeforeproportion, same-employer40aflat-taxbar, actualtaxstatus/widow/nofaultID/catchupconditions,3calendarmonth/multiemployermaternitytopup,continuoussame-employeryear42btest and employee social-reportcopyduty. A germany-payroll mirrors onlyactualomissions; its alreadycorrectprecap/sameemployer40abar/fullyear42bdetail is preserved. R62–70conditionsremainbyteexactexcept the narrowlyfurtherqualifiedsameparagraphs.

Fifteenown selected operative quotations read29October2026; officialURLs/native scopes/raw-readerhashes and actual encoding are recorded. Two sourceswere acquiredbyCafterprecisecitedchecksfailed;earlierfailedroutes/encodinghistoryremaininitsimmutableevidence. Writerdidnotperformanewsearchoracquisition. Newfullmonth100payfixturegives32.55total/15employer/17.55employee,not3.60; fullmonth/isolatedinsuredcommercialscopeexplicit.600/800U1fixturesusestipulatedactual60%/80%tariffs,notguessedfundfacts. Maternity60+40dailyinputsgive87combined/52.20+34.80shares,not13deductedtwice. Actualnet-inputproof/20specialpopulationsstayseparate.

ExacttwoGuide/ledgerpins in successor-inventory.json.28canonicalopsincludingB1.5→1.6/A1.1→1.2 inverttoexactpreimages. All138+346immediatepriorcurrentunits/175+512oldtopicidentities retained;two newpreciserowsineachgive140+348current. OriginalB2/A0oa and entireworkedsections/amounts/algebra/URLs/order/CTA/trust/bylines/protectedmetadata exact. {len(cs)}own separatingcontrols,allnative/sourcechecks and scoped schema0/0/examples/diff pass. All25R62seal membersrehashedunchanged;originalcountryfreezeandearlierwriter/reviewsealsuntouched. This is writercorrectionpendingC'sdifferentexactreview,notcountryPASS/publication. NoFrancewriting.
""")
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'writer successor, independent review pending','artifacts':entries});f={'status':'writer successor, independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pairs':invs,'controls':len(cs)};dump(W/'freeze.json',f);print(json.dumps({**f,'freeze_sha256':H(W/'freeze.json')},indent=2))
