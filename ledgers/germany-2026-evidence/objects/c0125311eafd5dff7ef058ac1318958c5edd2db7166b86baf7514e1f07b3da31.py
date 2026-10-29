from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
from datetime import date,timedelta
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');cs=[]
def c(id,a,b,scope):assert a==b,(id,a,b);cs.append({'id':id,'actual':str(a),'expected':str(b),'scope':scope,'pass':True})
for n,nofault,employee_breach,alone,kind,w in [(3,False,False,False,False,True),(4,False,False,False,False,False),(4,True,False,False,False,True),(4,False,True,False,False,True),(4,False,False,True,False,True),(4,False,False,False,True,True)]:c('R62.'+str((n,nofault,employee_breach,alone,kind)),n<=3 or nofault or employee_breach or alone or kind,w,'Tests whether actual28gordinarydeduction timingbar/exception applies, not an invented universal recovery procedure. Employee_breach means actual intentional/gross-negligent28o1breach.')
c('R63.U1bonus',D(5000)+D(1000)-D(1000),D(5000),'Stipulated regular pay and23aone-timebonus, ordinaryU1base excludesbonus. NoautomaticU2/insolvency deduction.')
for weeks,noright,w in [(4,True,True),(4,False,False),(5,True,False)]:c('R63.shortjob'+str((weeks,noright)),weeks<=4 and noright,w,'U1shortjob exclusion needs BOTH actual≤4weeks and noEntgFG3(3)entitlement due to nature; durationalone notenough.')
c('R63.shorttimeactualbase',min(D(1500),D(8450)),D(1500),'Stipulated actual earned1500 duringshorttimeallowance, not hypothetical2500; actualAAGlevybase.')
for hourly,premium,free,excess in [(30,'7.50','6.25','1.25'),(25,'6.25','6.25','0'),(20,'5','5','0')]:
 c('R64.taxpremium'+str(hourly),D(hourly)*D('.25'),D(premium),'Actual additional25%nightworkpremise, hourlybasicpay≤50taxceiling.')
 c('R64.SVfree'+str(hourly),min(D(hourly),D(25))*D('.25'),D(free),'PartialSvEVexemption; actualrate/work/additionalpaygates independently met.')
 c('R64.SVexcess'+str(hourly),max(0,D(hourly)-D(25))*D('.25'),D(excess),'Onlyexcesscomponent contributory, not entirepremiumbecausehourlypay>25.')
for start_before,hour,w in [(True,3,True),(False,3,False),(True,5,False)]:c('R64.followingday'+str((start_before,hour)),start_before and 0<=hour<4,w,'PreviousdayactuallySunday/holiday;actualEStG3b3no2continued00–04work, notuniversalstacking.')
for months,previous,w in [(2,False,True),(2,True,False),(4,False,False)]:c('R65.accompanying'+str((months,previous)),months<=3 and not previous,w,'Training/studyaccompanyinginternship branch, actualsame-trainerpriorinternship selector; notcompulsory/orientationbranch.')
c('R66.agriculturaltime',14<=15,True,'Stipulated14weekagriculturaljob, actual90workingdaylimit/occupationalfacts independentlyfit; notnonagricultural3monthworksheet.')
c('R66.nonagriculturaltime',80<=70,False,'Stipulated nonagricultural80workingdays; no15/90transplant.')
for gross,w in [(False,date(2026,8,3)),(True,None)]:c('R66.aggregationdecision'+str(gross),None if gross else date(2026,8,3),w,'Actualcompetentaggregationdecisionnotified3August;grossflagincludesintentional/grossnegligentinvestigationfailure. Ifexceptionfailsnoalternateuniversalretrodateinferred.')
c('R67.totalrate',sum(map(D,['18.6','3.6','2.6','14.6','2.9'])),D('42.3'),'ActualBMGpublished2026average2.9, independentfixedbranchrates; notfundspecificordinaryemployeeKVZ.')
c('R67.F',(D(28)/D('42.3')).quantize(D('.0001'),rounding=ROUND_HALF_UP),D('.6619'),'ActualstatutoryfourdecimalFrounding;42.3denominator notunroundedrateestimate.')
c('R67.monthlyceiling',D(69750)/12,D('5812.50'),'ExplicitBMG2026administrativeceiling/PAPvalues, no2027statuteadaptation.')
c('R68.closureouterlimit',date(2026,6,30)+timedelta(weeks=6),date(2026,8,11),'Stipulatedclosuretrigger30June;actualnextpayrollmayearlier; notwaitingFebruary2027.')
c('R68.nextpayroll',min(date(2026,7,31),date(2026,8,11)),date(2026,7,31),'Stipulatedactualnextpayroll31July, beforeouter6weeks;actualtrigger/procedurefacts separate.')
c('R69.nominalweekday',date(2026,2,15).weekday(),6,'PythonMonday0Sunday6;nominalDEUV15February2026Sunday.')
c('R69.ordinaryadjustment',date(2026,2,15)+timedelta(days=1),date(2026,2,16),'OrdinarySGBX26(3)deadline,Mondaynotlocalholiday/noexpressauthoritynotice;notAO108orofficialappointment.')
c('R70.contingentexpense',D(2000)+D(100)-D(100),D(2000),'Stipulatedregularpay2000plus100expensecontingentonactualcostnotincurredduringillness;expenseexcluded.')
c('R70.performancepay',D(80)*D(20),D(1600),'Stipulatedachievableaverage20perregularhour/80regularhours;notzeroactualoutputduringincapacity orautomaticovertimecontinuation.')
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
  for key in ['pre_refresh_rows','current_main_rows']:
   assert len(old[key])==len(prior[key])
   for a,b in zip(old[key],prior[key]):assert all(a[k]==b[k]for k in b if k!='current_destination');assert a['prior_sealed_destination']==b['current_destination']
 assert H(Path(inv['ledger_path']))==inv['ledger_sha256'];n,fail=ce.check_file(str(p));assert n==proofs[s]['actual_original_oa_blocks']and not fail
 es=[];ws=[]
 with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),es,ws,only_files={str(p.relative_to(R))})
 assert not es and not ws;d=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert d.returncode==0
 pairchecks.append({'slug':s,'ops':len(ops[s]),'all_native_rows_full_inverse_old_identities':True,'original_worked_section_and_oa_exact':True,'oa_blocks':n,'oa_failures':fail,'schema_errors':es,'schema_warnings':ws,'diff_returncode':d.returncode,'schema_stdout':out.getvalue()})
priorchecks=[]
for base,filename in [(A,'writer-A-handover-manifest.json'),(B,'artifact-manifest.json')]:
 m=json.loads((base/filename).read_text())
 for e in m:assert H(base/e['path'])==e['sha256']
 priorchecks.append({'manifest':str(base/filename),'sha256':H(base/filename),'members':len(m),'mismatches':0})
checks={'role':'writer only, different independent review pending','controls':cs,'control_count':len(cs),'own_selected_quote_records':16,'source_checks':qc,'pairs':pairchecks,'original_writer_manifests':priorchecks};dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f'''# Germany payroll DE-R62–70 writer successor

Selected narrow A supplies the actual recovery exceptions, U1 exclusions, partial premium contribution exemption/overnight continuation, same-trainer internship gate, agricultural/aggregation distinction, explicit BMG2026 administrative rate/ceiling, accelerated accident-insurance report, ordinary2025 Sunday deadline adjustment and sickness-pay qualifiers. Sixteen own selected records were actually read29October2026. Source-quote-index.json distinguishes operative law, BMG administrative publication and the retained SGBX26 web-tool JSON observation; it does not claim Gazette acquisition, portal execution or whole-source reading.

The report's native coordinates identify A's germany-payroll. Its unchanged ordinary conditions are also mirrored in B's de-payroll only where the same already concrete omission exists. B's correct agricultural15/90, published F and2027-only statutory boundary are retained. Its missing accident-insurance annual-report sibling route is added with actual trigger/population gates. The two exact deltas remain separate in exact-operations.json. This is bounded writer work awaiting different exact review, not a countryPASS.

Guide/ledger pairs and sizes: successor-inventory.json. All{sum(p['ops']for p in pairchecks)}canonical operations invert to exact saved preimages; all original URLs/order/CTA/trust/bylines/protectedmetadata and complete original worked sections preserved. Actual original counts are germany-payroll0oa/de-payroll2oa, not invented blocks.346+136 original current units retain every ID; new precise rows and complete512+175 old-topic identities are explicitly rebound. {len(cs)} separating controls, all native/source identity/quote checks, scoped schema0/0/examples/diff pass. Original A610 and B515 members rehashed unchanged; original countryfreeze/reviews untouched. No Git/PR/public/France writer changes.

Useful separators:5000regular+1000bonus gives U1base5000;30hourly×25% gives7.50taxfree/6.25SVfree/1.25contributory; repeat same-trainer two-month internship fails that exclusion; aggregate-status no-fault notified-date is separate from gross-negligent failure;28/42.3 rounds0.6619; closure30June/nextpay31July cannot waitFebruary2027; nominal15February2026Sunday moves ordinary report to16February;100unincurred contingentexpense is excluded. Options, exact sources, preimages/operations/inverses and genuine retained limitations are saved here.
''')
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'writer successor, independent review pending','artifacts':entries});f={'status':'writer successor, independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pairs':invs,'controls':len(cs)};dump(W/'freeze.json',f);print(json.dumps({**f,'freeze_sha256':H(W/'freeze.json')},indent=2))
