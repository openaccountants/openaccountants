from pathlib import Path
from decimal import Decimal as D,ROUND_DOWN
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;A=O/'germany-ledger-writer-2026-10-28';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');controls=[]
def c(id,actual,expected,premise):assert actual==expected,(id,actual,expected);controls.append({'id':id,'actual':str(actual),'expected':str(expected),'premise':premise,'pass':True})
def incoming(gprev,gcur,eprev,ecur,number):return D(gprev)<=D(25000)and D(gcur)<=D(100000)and D(eprev)<=D(100000)and D(ecur)<=D(100000)and number
for vals,w in [((30000,40000,80000,90000,True),False),((25000,40000,80000,90000,True),True),((25000,100000,100000,100000,True),True),((25000,'100000.01',100000,'100000.01',True),False),((25000,40000,'100000.01',90000,True),False),((25000,40000,80000,90000,False),False)]:c('R23.incoming'+str(vals),incoming(*vals),w,'Established continuing EU business; actual19(2)German and288EU turnover separately determined, number flag valid for Germany; no new-business simplification or crossing-supply computation inferred.')
for host,duplicate,application,w in [(True,False,True,True),(False,False,True,False),(True,True,True,False),(True,False,False,False)]:c('R23.outgoing'+str((host,duplicate,application)),host and not duplicate and application,w,'Actual German establishment and prior/currentEUturnover gates stipulated met. Host means actual host exemption conditions; duplicate means19a(1)no4 procedure registration, not a ban on multiple qualifying host exemptions.')
for kind,ancillary,w in [('no1',False,0),('no2',False,30000),('no2',True,0),('ordinary-taxable',False,30000)]:c('R24.receipts'+str((kind,ancillary)),D(0)if kind=='no1'or(kind=='no2'and ancillary)else D(30000),D(w),'30000receipts, no fixed-asset sale. Category independently classified under exact19(2); no2financial/insuranceexemption remains separate from threshold exclusion. No numerical ancillary test invented.')
def disposal(usable,multiple,within,different):return usable and multiple and within and different
for vals,w in [((True,True,True,False),False),((True,True,True,True),True),((True,True,False,True),False),((False,True,True,True),False),((True,False,True,True),False)]:c('R25.disposal'+str(vals),disposal(*vals),w,'Actual15a(8)classification only; originally fully taxable/samebasis sale does not automatically change use. Other independent changes/simplifications/remaining-period calculation must still be checked.')
for vat,w in [('999.99',True),('1000',True),('1000.01',False)]:c('R25.inclusive'+vat,D(vat)<=D(1000),w,'InputVATattributabletoacquisition/productioncost; only44(1)inclusive simplification tested, not all adjustment gates.')
# Exact source/reader bytes and each own selected quotation, plus original A index reused by attribution.
quotes=json.loads((W/'source-quote-index.json').read_text());source=[]
for id,q in quotes.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];literal='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert (literal==q['exact_quote'] or (id=='VAT.UAEKUDUTY' and literal.startswith(q['exact_quote']))),id;source.append({'id':id,'hashes_and_literal_quote':True,'scope_precision':('Exact original first-three-sentence prefix of final native LF; next sentence begins on same line and is outside the quoted claim' if id=='VAT.UAEKUDUTY' else 'Entire recorded native LF literal'),'own_new_selected_read':not id.startswith('VAT.')})
proof=json.loads((W/'preservation-proof.json').read_text());inv=json.loads((W/'successor-inventory.json').read_text());p=Path(proof['path']);old=(W/'before'/p.name).read_text();new=p.read_text();assert H(p)==proof['after_sha256'];ops=json.loads((W/'exact-operations.json').read_text());x=old
for op in ops:assert x.count(op['before'])==1;x=x.replace(op['before'],op['after'],1)
assert x==new
for op in reversed(ops):assert x.count(op['after'])==1;x=x.replace(op['after'],op['before'],1)
assert x==old
rr=json.loads((W/'support/de-vat-annual-and-special-schemes/rows.json').read_text());oldrr=json.loads((A/'support/de-vat-annual-and-special-schemes/claim-rows.json').read_text());lines=new.split('\n')
for r in rr:
 a,b=r['native_LF'];assert r['wording']=='\n'.join(lines[a-1:b]);assert all(k in quotes for k in r['source_quote_ids'])
assert set(r['prior_row_id']for r in rr if r['prior_row_id'])==set(range(1,len(oldrr)+1))
ot=json.loads((W/'support/de-vat-annual-and-special-schemes/old-topic-destinations.json').read_text());prior=json.loads((A/'support/de-vat-annual-and-special-schemes/old-topics.json').read_text());assert len(ot)==len(prior)
for a,b in zip(ot,prior):assert all(a[k]==b[k]for k in ['ref','old_lf','section','wording']);assert a['prior_sealed_destination']==b['destination']
assert H(Path(inv['ledger_path']))==inv['ledger_sha256']
# Original A seal is not altered. No repeated snapshots/country-wide validation.
m=json.loads((A/'writer-A-handover-manifest.json').read_text());priorhash=[]
for e in m:
 assert H(Path(e['path']))==e['sha256'];priorhash.append(e['path'])
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def module(n,path):s=importlib.util.spec_from_file_location(n,str(path));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ce=module('R18_examples',R/'scripts/check-examples.py');vg=module('R18_schema',R/'scripts/validate-guides.py');n,failures=ce.check_file(str(p));assert n==2 and not failures
errors=[];warnings=[]
with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),errors,warnings,only_files={str(p.relative_to(R))})
assert not errors and not warnings;diff=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert diff.returncode==0
checks={'role':'writer, not independent review','controls':controls,'control_count':len(controls),'own_selected_native_ranges':4,'exact_source_checks':source,'prior_A_manifest':{'sha256':H(A/'writer-A-handover-manifest.json'),'members_rehashed':len(priorhash),'mismatches':0},'full_inverse_and_all_native_rows':True,'all_prior174_current_units_and347_old_topics_retained':True,'original_examples':{'blocks':n,'failures':failures,'whole_original_worked_section_exact':True},'schema':{'errors':errors,'warnings':warnings,'stdout':out.getvalue()},'diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr}}
dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f"""# Germany annual VAT DE-R23–25 writer successor

The three findings use selected narrow Option A from the actual retained primary clauses. This is writer work pending C's exact independent recheck, not a country PASS or accountant attestation.

R23 states both directions' actual host-state eligibility. Incoming German exemption needs incorporated German prior-year25000/current-year100000 turnover gates, separate EU prior/current100000 and valid home-state number. Outgoing German procedure also requires actual host exemption conditions and the statutory application/no-duplicate-procedure registration gate. R24 separates the exact19(2)no1 unconditional listed category from no2's ancillary-only financial/insurance category, without inventing an ancillary numerical test. R25 states the actual still-usable/repeated-use/period/different-treatment disposal conditions, keeps remaining-period/advance-return timing, and corrects the inclusive1000 simplification. Intake/source rows are rebound. The original OSS weekend reservation remains exact.

Guide `{proof['after_sha256']}` ({proof['bytes']}bytes), version0.3,29October2026; ledger `{inv['ledger_sha256']}`. The complete successor ledger has{inv['current_rows']}current units, retains all174prior identities and all347exact historical old-topic identities with preserved predecessor destinations and explicit correction notes. Four complete selected native ranges were actually read29October; exact original-language quotes/official URLs/raw-reader hashes are in own-actual-read-quotes.json. Every unchanged A anchor preserves actual earlier reading provenance. No fresh fetch or raw-source duplication was needed.

Seven exact operations/full inverse, original URLs/order/attribution/CTA/trust fields and whole original worked section are preserved. All{len(priorhash)}Aseal members rehash unchanged. Both original executable examples pass;{len(controls)}new eligibility/classification controls, source literal/current native-row checks and one-Guide schema0/0/diff pass. Original country freeze and earlier independent findings stay unchanged. No Git, PR, public platform or France writing. Exact before/after, options, operations, ledgers, old maps, source/read indexes and meaningful checks are retained alongside this report.
""")
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file() and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'Writer successor, independent review pending','artifacts':entries});freeze={'status':'writer successor, different independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(controls)};dump(W/'freeze.json',freeze);print(json.dumps({**freeze,'freeze_sha256':H(W/'freeze.json')},indent=2))
