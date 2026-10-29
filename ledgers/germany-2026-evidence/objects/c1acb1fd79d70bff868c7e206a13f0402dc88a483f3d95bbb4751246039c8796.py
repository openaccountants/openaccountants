from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
from datetime import date,timedelta
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');cs=[]
def c(id,a,b,scope):assert a==b,(id,a,b);cs.append({'id':id,'actual':str(a),'expected':str(b),'scope':scope,'pass':True})
for same,within,cover,w in [(True,True,True,True),(False,True,True,False),(True,False,True,False),(True,True,False,False)]:c('R72.group'+str((same,within,cover)),same and within and cover,w,'ActualDRV4bself-employmentopinion and lateremploymentfinding independentlystipulated; sameincludesactualworkcircumstances/uniformcontract;withinmeanscontractconcluded≤2yearsfromreceipt. Individualone-month/consentnotimported;otherstatutorydategates separate.')
for credible,nofault,w in [(True,True,True),(True,False,False),(False,True,False)]:c('R72.latecharge'+str((credible,nofault)),credible and nofault,w,'Actualretrospectivecontributionnotice;24(2)excludeschargeonlytotheshownextent,notuniversalzeroarrears.')
for deductible,w in [(5000,True),(6000,False),(4999,True)]:c('R73.productcap'+str(deductible),deductible<=5000,w,'Specifiedordinarypersonwithin193(3),authorisedinsurer/outpatient/inpatientothergates separatelymet;5000aggregateannualdeductibleonly,notallpolicyentitlement.')
c('R74.partialyear',D(12000)/6*D('.049'),D(98),'Stipulated2025dutyJuly–December,sixbegundutymonths;2026rate4.9;priorDecembertransitionalamountseparate.')
c('R74.fullprior',D(12000)/12*D('.049'),D(49),'Fullprior-year dutycontrast;notuniversal12denominator.')
c('R74.midJuly',12-7+1,6,'BegunJulymonthcountsdespiteactualmidmonthstart;otherdutyfactsstipulated.')
for amount,w in [(40,False),(D('40.01'),True),(98,True)]:c('R74.threshold'+str(amount),D(amount)>40,w,'Actualcalculatedmonthlyprepaymentmuststrictlyexceed40;othernotice/periodgatesseparate.')
for compulsory,free,minor,w in [(False,False,False,True),(True,False,False,False),(False,True,False,False),(False,True,True,True)]:c('R75.entry'+str((compulsory,free,minor)),not compulsory and(not free or minor),w,'Independentlyqualifying15hours/priorhistory;compulsory25/26,free27/28;minorflagmeans27(2)onlynotanyarbitraryfreecategory.')
c('R75.suspensionminor',False,False,'Actual27(2)minorjobdoesnotsuspendparagraph4insurance;notimporting28intothatclause.')
c('R76.nominalSunday',date(2026,5,31).weekday(),6,'Nominal3monthwindowfor1Marchstartends31May2026Sunday,not3×30days.')
c('R76.adjusted',date(2026,5,31)+timedelta(days=1),date(2026,6,1),'OrdinarySGBX26(3)deadline;noactualholiday/expressauthoritynotice/appointmentexceptionstipulated.')
for reminderwarning,remaining,after2weeks,decision,w in [(True,110,True,True,True),(False,110,True,True,False),(True,100,True,True,False),(True,110,False,True,False),(True,110,True,False,False)]:c('R77.decisiongates'+str((reminderwarning,remaining,after2weeks,decision)),reminderwarning and remaining>100 and after2weeks and decision,w,'Stipulatedmonthshare100/twomontharrearsatreminder;eligibledeterminationnotinstantstart. Receiptandthree-daystartclockseparate.')
c('R77.afterreceipt',date(2026,6,1)+timedelta(days=3),date(2026,6,4),'Stipulatedactualsuspensiondecisionreceived1June;3daysafterreceipt,notreminder/twoweeksalone;actualproceduredateexceptionsseparate.')
qs=json.loads((W/'source-quote-index.json').read_text());qc=[]
for id,q in qs.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256']
 if q.get('native_LF')is None:
  assert id=='R76.SGBX26'and q['exact_quote']in json.loads(Path(q['raw_path']).read_text())['result'];kind='Faithful operative WebL13 in retained official web-tool response JSON, not rawHTML'
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
 calendar_op=next(o for o in ops[s]if o['finding']=='R76');assert worked(after).replace(calendar_op['after'],calendar_op['before'],1)==worked(before);assert re.findall(r'```oa-check.*?```',before,re.S)==re.findall(r'```oa-check.*?```',after,re.S)
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
 pairchecks.append({'slug':s,'ops':len(ops[s]),'all_native_rows_full_inverse_old_identities':True,'original_oa_and_case_amounts_exact_yoga_calendar_sentence_corrected':True,'oa_blocks':n,'oa_failures':fail,'schema_errors':es,'schema_warnings':ws,'diff_returncode':d.returncode,'schema_stdout':out.getvalue()})
priorchecks=[]
for base,filename in [(B,'artifact-manifest.json')]:
 m=json.loads((base/filename).read_text())
 for e in m:assert H(base/e['path'])==e['sha256']
 priorchecks.append({'manifest':str(base/filename),'sha256':H(base/filename),'members':len(m),'mismatches':0})
checks={'role':'writer only, different independent review pending','controls':cs,'control_count':len(cs),'own_selected_quote_records':9,'source_checks':qc,'pairs':pairchecks,'original_writer_manifests':priorchecks};dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f"""# Germany social DE-R72–77 writer successor

Selected narrow A adds the actual group-opinion protection/comparablecover/two-year contract gates, retrospective no-fault late-charge qualification, complete193(3)private minimum product/population cap, partial-year levy denominator/commencement, unemployment concurrent-status/delayedclock/suspension gates, yoga ordinary Sunday deadline adjustment and KSK warning/decision/three-day commencement. Eight own selected complete operative scopes read29October2026; exact earlier own SGBX26official-observation reading is reused by explicit bridge, not called originalHTML/acquisition. Source quotes/officialURLs/hashes/actualscopes are in own-actual-read-quotes.json and source-quote-index.json.

Guide/ledger pins in successor-inventory.json. Twelve canonical operations including2.2→2.3 invert to exact preimage.187priorcurrentunits/203oldtopics retain everyidentity;two precise new operative rows produce189current. Original2oa/allnumericcaseinputs/algebra/URLs/order/CTA/trust/bylines/protectedmetadata pass. Only yoga's erroneous calendar prose changes within the worked section; no whole-case-prose-byteexact claim. {len(cs)} own controls, exactsource/nativechecks and scoped schema0/0/examples/diff pass; all515originalBmembers unchanged. No lower-proven-income startup pension/spouse-income/owneraccident computation claimed resolved; genuine reservations remain precise. This is writer work pending C's exact independent review, not a countryPASS or publication.

Separators: actual4cgroup route can apply without individualone-monthapplication only with its own gates;5000annualdeductiblepassesitscap/6000fails;12000/sixbegunmonths×4.9%=98 ratherthan49;concurrentcompulsorystatusbarsentry/minor27(2)doesnot;31May2026Sunday→ordinary1June;twoweeks/remainderalonecannotstartKSKsuspensionwithoutwarning/decision/receiptandthree-dayclock. Payment/instalmentroute and precise genuine limits retained.
""")
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'writer successor, independent review pending','artifacts':entries});f={'status':'writer successor, independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pairs':invs,'controls':len(cs)};dump(W/'freeze.json',f);print(json.dumps({**f,'freeze_sha256':H(W/'freeze.json')},indent=2))
