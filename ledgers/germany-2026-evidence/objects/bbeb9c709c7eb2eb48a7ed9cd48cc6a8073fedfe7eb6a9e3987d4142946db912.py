from pathlib import Path
from decimal import Decimal as D,ROUND_DOWN
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;A=O/'germany-ledger-writer-2026-10-28';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');controls=[]
def c(id,actual,expected,premise):assert actual==expected,(id,actual,expected);controls.append({'id':id,'actual':str(actual),'expected':str(expected),'premise':premise,'pass':True})
def soli(base):return max(D(0),min(D(base)*D('.055'),(D(base)-D(20350))*D('.119'))).quantize(D('.01'),rounding=ROUND_DOWN)
for b,w in [('20350','0'),('20400','5.95'),('20350.05','0'),('20400.05','5.95'),('40000','2200')]:c('R18.base'+b,soli(b),D(w),'Independently established ordinary single assessment base; no32d(3)/(4)component. Fractions of a cent dropped. Mixed/special withholding branches not run through this function.')
c('R18.separate32d',D(750)*D('.055'),D('41.25'),'Preserved original32d(3)fixture, separate surcharge without ordinary threshold/cap.')
c('R19.refund-arithmetic',D(2500)*D(2)/D(5),D(1000),'Actual capital tax withheld/remitted2500; amount only conditional on all independently established population/procedure/anti-abuse gates. No automatic entitlement or surcharge refund inferred.')
def denial(owners_lack,source_lacks,rebuttal,listed):return owners_lack and source_lacks and not(rebuttal or listed)
for vals,w in [((True,True,False,False),True),((False,True,False,False),False),((True,False,False,False),False),((True,True,True,False),False),((True,True,False,True),False)]:c('R19.denial'+str(vals),denial(*vals),w,'Actual50d3conditional statutory denial only; independent42AO and other relief gates remain. Rebuttal/listing flags mean exact statutory proof/listedclassfacts, not assumed substance.')
def application(branch,substantive,nationality):return substantive and (nationality if branch in ['4b','5']else True)
for br,sub,nat,w in [('4b',True,False,False),('4d',True,False,True),('4e',True,False,True),('6',True,False,True),('5',True,False,False),('4d',False,True,False),('4b',True,True,True)]:c('R20.branch'+str((br,sub,nat)),application(br,sub,nat),w,'Branch-specific classification only. Substantive statutory application/income requirements independently established; nationality flag includes actual relevant permitted residence route. No special tariff/insurance/credit computation inferred.')
def excluded(only_registry,related,treaty_opposes):return only_registry and(not related or treaty_opposes)
for sole,related,treaty,w in [(True,False,False,True),(True,True,False,False),(True,True,True,True),(False,False,False,False)]:c('R21.registry'+str((sole,related,treaty)),excluded(sole,related,treaty),w,'Other-right category established. If not sole registry, this exception does not settle another domestic source link; treaty flag incorporates actual applicable treaty-application rules.')
def asset(german,other,attribution,within):return D(german)/(D(german)+D(other))>D('.5') and attribution and within
for g,o,att,within,w in [(40,60,True,True,False),(60,40,True,True,True),(50,50,True,True,False),(60,40,False,True,False),(60,40,True,False,False)]:c('R22.asset'+str((g,o,att,within)),asset(g,o,att,within),w,'Active business book values at an actual relevant test time; marketvalues irrelevant to this domestic percentage; within means actual365daywindow. Overall17/treaty/taxgates separate.')
# Exact source/reader bytes and each own selected quotation, plus original A index reused by attribution.
quotes=json.loads((W/'source-quote-index.json').read_text());source=[]
for id,q in quotes.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];literal='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert literal==q['exact_quote'],id;source.append({'id':id,'hashes_and_literal_quote':True,'own_new_selected_read':not id.startswith('NR.')})
proof=json.loads((W/'preservation-proof.json').read_text());inv=json.loads((W/'successor-inventory.json').read_text());p=Path(proof['path']);old=(W/'before'/p.name).read_text();new=p.read_text();assert H(p)==proof['after_sha256'];ops=json.loads((W/'exact-operations.json').read_text());x=old
for op in ops:assert x.count(op['before'])==1;x=x.replace(op['before'],op['after'],1)
assert x==new
for op in reversed(ops):assert x.count(op['after'])==1;x=x.replace(op['after'],op['before'],1)
assert x==old
rr=json.loads((W/'support/de-non-resident-tax/rows.json').read_text());oldrr=json.loads((A/'support/de-non-resident-tax/claim-rows.json').read_text());lines=new.split('\n')
for r in rr:
 a,b=r['native_LF'];assert r['wording']=='\n'.join(lines[a-1:b]);assert all(k in quotes for k in r['source_quote_ids'])
assert set(r['prior_row_id']for r in rr if r['prior_row_id'])==set(range(1,len(oldrr)+1))
ot=json.loads((W/'support/de-non-resident-tax/old-topic-destinations.json').read_text());prior=json.loads((A/'support/de-non-resident-tax/old-topics.json').read_text());assert len(ot)==len(prior)
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
checks={'role':'writer, not independent review','controls':controls,'control_count':len(controls),'own_selected_native_ranges':8,'exact_source_checks':source,'prior_A_manifest':{'sha256':H(A/'writer-A-handover-manifest.json'),'members_rehashed':len(priorhash),'mismatches':0},'full_inverse_and_all_native_rows':True,'all_prior203_current_units_and404_old_topics_retained':True,'original_examples':{'blocks':n,'failures':failures,'whole_original_worked_section_exact':True},'schema':{'errors':errors,'warnings':warnings,'stdout':out.getvalue()},'diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr}}
dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f'''# Germany non-resident DE-R18–22 writer successor

The five findings are corrected with selected narrow Option A from the actual retained own-law clauses. This is a writer proposal pending C's exact independent recheck, not a country PASS or accountant attestation.

R18 adds the assessment-base/11.9% sliding-cap and cent-truncation step; ordinary single base20,400 gives5.95, while the original32d example remains41.25. R19 replaces automatic entity refund/denial with the actual44a(9)population, incorporated procedure, conjunctive50d(3)test and statutory rebuttal/listed-class exceptions. R20 gives the omitted statutory assessment gates and their actual branch-specific nationality/residence restriction without inventing the referred tariff, insurance or credit calculations. R21 supplies the exact other-rights registry-only exceptions while keeping domestic location/exploitation separate. R22 uses active-asset book values, seller attribution and the365daywindow, preserving17/treaty conditions. The actual intake and selected-read source entries are rebound. Existing genuine reservations stay exact.

Guide `{proof['after_sha256']}` ({proof['bytes']}bytes), version0.3, 29October2026; ledger `{inv['ledger_sha256']}`. The complete successor ledger has{inv['current_rows']}current units, retains all203prior identities, and maps all404exact old-topic identities to current destinations with preserved predecessor routes and correction notes. Source-quote-index.json retains every original A anchor with attributed actual prior reading; eight new selected native ranges were actually read29October, exact original-language text/official URLs/raw-reader hashes in own-actual-read-quotes.json. Cached acquisition is not promoted to reading; no fresh source fetch was needed.

All{len(priorhash)}original A manifest members rehash unchanged. Thirteen exact operations/full inverse, all original URLs in order, attribution/CTA/trust/protected fields and whole original worked section are preserved. Both original executable examples pass;{len(controls)}new separating numerical/classification controls, current native rows, source literals and scoped one-Guide schema0/0/diff pass. No Git, PR, public platform or France changes. Exact inventory, read scopes, options, operations, checks and original preimage remain alongside this report. Original country freeze and earlier independent findings remain unchanged; country review continues separately.
''')
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file() and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'Writer successor, independent review pending','artifacts':entries});freeze={'status':'writer successor, different independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(controls)};dump(W/'freeze.json',freeze);print(json.dumps({**freeze,'freeze_sha256':H(W/'freeze.json')},indent=2))
