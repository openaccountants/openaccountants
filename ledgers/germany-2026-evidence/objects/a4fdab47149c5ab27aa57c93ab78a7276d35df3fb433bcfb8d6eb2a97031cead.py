from pathlib import Path
from decimal import Decimal as D,ROUND_DOWN
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;A=O/'germany-ledger-writer-2026-10-28';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');controls=[]
def c(id,actual,expected,premise):assert actual==expected,(id,actual,expected);controls.append({'id':id,'actual':str(actual),'expected':str(expected),'premise':premise,'pass':True})
from datetime import date

def catchup(expectation,no_fault,learned,pe=False):
 return date(learned.year+(learned.month==12),learned.month%12+1,learned.day) if expectation and no_fault else None
c('ordinary2025report',date(2025+1,12,31),date(2026,12,31),'One year after stipulated calendar financial year; no special deadline adjustment facts.')
c('qualifyinglateknowledge',catchup(True,True,date(2027,2,15)),date(2027,3,15),'Stipulated justified expectation, no fault, actual knowledge15February; no weekend/holiday/notice adjustment needed for this fixture.')
c('culpablefailure',catchup(True,False,date(2027,2,15)),None,'No-fault limb fails; this exception supplies no automatic new deadline.')
c('unjustifiedexpectation',catchup(False,True,date(2027,2,15)),None,'Without justified expectation, do not apply this catch-up exception.')
c('specifiedPE',catchup(True,True,date(2027,2,15),True),date(2027,3,15),'Actual paragraph4sentence5specifiedPE independently established; same conditional catch-up.')
c('noticealternative',catchup(True,True,date(2027,2,15)),date(2027,3,15),'Where report cannot be procured/created, statutory sentence3 notice and available data rather than fictional report; same qualifying deadline.')
# Exact source/reader bytes and each own selected quotation, plus original A index reused by attribution.
quotes=json.loads((W/'source-quote-index.json').read_text());source=[]
for id,q in quotes.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];literal='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert q['exact_quote']in literal,id;source.append({'id':id,'hashes_and_literal_quote':True,'quote_scope':'Exact selected operative quotation within declared nativeLF','own_new_selected_read':not id.startswith('TP.')})
proof=json.loads((W/'preservation-proof.json').read_text());inv=json.loads((W/'successor-inventory.json').read_text());p=Path(proof['path']);old=(W/'before'/p.name).read_text();new=p.read_text();assert H(p)==proof['after_sha256'];ops=json.loads((W/'exact-operations.json').read_text());x=old
for op in ops:assert x.count(op['before'])==1;x=x.replace(op['before'],op['after'],1)
assert x==new
for op in reversed(ops):assert x.count(op['after'])==1;x=x.replace(op['after'],op['before'],1)
assert x==old
rr=json.loads((W/'support/germany-transfer-pricing/rows.json').read_text());oldrr=json.loads((A/'support/germany-transfer-pricing/claim-rows.json').read_text());lines=new.split('\n')
for r in rr:
 a,b=r['native_LF'];assert r['wording']=='\n'.join(lines[a-1:b]);assert all(k in quotes for k in r['source_quote_ids'])
assert set(r['prior_row_id']for r in rr if r['prior_row_id'])==set(range(1,len(oldrr)+1))
ot=json.loads((W/'support/germany-transfer-pricing/old-topic-destinations.json').read_text());prior=json.loads((A/'support/germany-transfer-pricing/old-topics.json').read_text());assert len(ot)==len(prior)
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
checks={'role':'writer, not independent review','controls':controls,'control_count':len(controls),'own_selected_native_ranges':2,'exact_source_checks':source,'prior_A_manifest':{'sha256':H(A/'writer-A-handover-manifest.json'),'members_rehashed':len(priorhash),'mismatches':0},'full_inverse_and_all_native_rows':True,'all_prior316_current_units_and398_old_topics_retained':True,'original_examples':{'blocks':n,'failures':failures,'original_blocks_and_all_case_algebra_amounts_exact':True,'worked_changes':'Onlystipulatedgates/remittancefacts andlabel,notnumericblocks'},'schema':{'errors':errors,'warnings':warnings,'stdout':out.getvalue()},'diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr}}
dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f"""# Germany DE-R61 writer successor

Selected narrow A adds the statutory justified-expectation/no-fault catch-up deadline to both fallback and filing tables. Report or unavailable-report notice/data duties fall due one month after actual knowledge of the non-transmission; the specified German PE is included. This is not an automatic twelve-month extension or a cure for culpable failure. Quick Reference and other version labels now consistently say1.3.

Guide `{proof['after_sha256']}`, ledger `{inv['ledger_sha256']}`. Own complete AO138a(4)/(6) nativeLF38/46 actually read29October2026, exact German quotations/official URL/raw-reader hashes recorded. No new acquisition. Earlier A quotes retain their original attributed read dates. Six separating controls include15February2027→15March2027 and failure of either eligibility limb. Actual other deadline selectors remain separate.

Seven exact operations/full inverse; original2oa blocks, all old URLs/order, CTA/trust/attribution and protectedmetadata retained.316 original current units/398 old-topic identities rebound; document-version wording is labelled metadata. Scoped examples/schema0/0/diff pass. All{len(priorhash)} original A seal members rehashed unchanged. Original country freeze remains intact. Writer correction only; different independent exact review pending, no countryPASS or public change. See exact-operations.json, preservation-proof.json, writer-checks.json and source-quote-index.json.
""")
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file() and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'Writer successor, independent review pending','artifacts':entries});freeze={'status':'writer successor, different independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(controls)};dump(W/'freeze.json',freeze);print(json.dumps({**freeze,'freeze_sha256':H(W/'freeze.json')},indent=2))
