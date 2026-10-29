from pathlib import Path
from decimal import Decimal as D,ROUND_DOWN
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;A=O/'germany-ledger-writer-2026-10-28';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');controls=[]
def c(id,actual,expected,premise):assert actual==expected,(id,actual,expected);controls.append({'id':id,'actual':str(actual),'expected':str(expected),'premise':premise,'pass':True})
from datetime import date
for income,age,farm,w in[(400,0,0,400),(400,100,0,300),(400,100,50,250)]:c('R44.deduction'+str((income,age,farm)),D(income)-D(age)-D(farm),D(w),'Actualeligible46(3)income≤410; age means independently determined statutoryexcess24areduction and farmactual13(3)amount. No broadernegative/hardship algorithm inferred.')
c('R44.exclude32d6',D(400),D(400),'Eligibleordinarynon-withheldincome400; additional100optional32d6tariffincome is excluded from46(3)eligibleamount, not combined500. Other filinggates separate.')
for amount,limit,w in[(900,1000,True),(1800,1000,False),(200,256,True),(400,256,False)]:c('R45.per-person'+str((amount,limit)),D(amount)<D(limit),w,'Actualperson-specificpositive totals after statutorywithin-boxnetting; twoowners900each/200each tested separately, not one pooled2000/512limit. No actualownershipsplit inferred.')
c('R45.no-pooling-sales',all(D(x)<1000 for x in[900,900]),True,'Twoactualspouseswithseparate900gains; not a single1800ownerusing2000fictitiouslimit.')
c('R45.no-pooling-services',all(D(x)<256 for x in[200,200]),True,'Twoactualspouseswithseparate200serviceincome; not a single400ownerusing512fictitiouslimit.')
c('R45.predecessor-clock',date(2026,9,1)>date(2025,1,1),True,'SimpleinheritedpurchasedCurrencyToken, predecessoracquired1Jan2024; disposal1Sep2026 afterone-yearanniversary1Jan2025. Death1Mar2026doesnot restartclock; no365dayfractionalgorithm.')
c('R45.predecessor-cost',D(12000)-D(10000),D(2000),'Simpleactualpredecessoracquisitioncost10000, sale12000, nocosts; deathFMV11000doesnot createassumedstepup. Holding/thresholds decide taxableoutcome separately.')
c('R45.wrong-death-stepup',D(12000)-D(11000),D(1000),'Counterfactualwrongdeathmarketvaluebasis discriminator, not Guide method.')
for amount,limit,w in[('255.99',256,True),(256,256,False),('999.99',1000,True),(1000,1000,False)]:c('R46.2025nonentry'+str((amount,limit)),D(amount)<D(limit),w,'Actual2025ELSTERAnlageSOpositiveincome/gaininstruction only. Exactthreshold fallsoutside statement; not evidenceof2026formlayout/overallno-returnduty.')
c('R46.lossentry','declare-within-scope-loss','declare-within-scope-loss','Actual2025instruction separatelyrequests within-scope losses; negativeamount not silentlyassigned nonentrybecause no positivetax. Overallfiling/correctionduties remain separate.')
# Exact source/reader bytes and each own selected quotation, plus original A index reused by attribution.
quotes=json.loads((W/'source-quote-index.json').read_text());source=[]
for id,q in quotes.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];literal='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert (q['exact_quote']in literal if id.startswith('CR.')else literal==q['exact_quote']),id;source.append({'id':id,'hashes_and_literal_quote':True,'quote_scope':'Preserved literal selected excerpt within declared nativeLF'if id.startswith('CR.')else'Full newly selected nativeLF','own_new_selected_read':not id.startswith('CR.')})
proof=json.loads((W/'preservation-proof.json').read_text());inv=json.loads((W/'successor-inventory.json').read_text());p=Path(proof['path']);old=(W/'before'/p.name).read_text();new=p.read_text();assert H(p)==proof['after_sha256'];ops=json.loads((W/'exact-operations.json').read_text());x=old
for op in ops:assert x.count(op['before'])==1;x=x.replace(op['before'],op['after'],1)
assert x==new
for op in reversed(ops):assert x.count(op['after'])==1;x=x.replace(op['after'],op['before'],1)
assert x==old
rr=json.loads((W/'support/de-crypto-tax/rows.json').read_text());oldrr=json.loads((A/'support/de-crypto-tax/claim-rows.json').read_text());lines=new.split('\n')
for r in rr:
 a,b=r['native_LF'];assert r['wording']=='\n'.join(lines[a-1:b]);assert all(k in quotes for k in r['source_quote_ids'])
assert set(r['prior_row_id']for r in rr if r['prior_row_id'])==set(range(1,len(oldrr)+1))
ot=json.loads((W/'support/de-crypto-tax/old-topic-destinations.json').read_text());prior=json.loads((A/'support/de-crypto-tax/old-topics.json').read_text());assert len(ot)==len(prior)
for a,b in zip(ot,prior):assert all(a[k]==b[k]for k in ['ref','old_lf','section','wording']);assert a['prior_sealed_destination']==b['destination']
assert H(Path(inv['ledger_path']))==inv['ledger_sha256']
# Original A seal is not altered. No repeated snapshots/country-wide validation.
m=json.loads((A/'writer-A-handover-manifest.json').read_text());priorhash=[]
for e in m:
 assert H(Path(e['path']))==e['sha256'];priorhash.append(e['path'])
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def module(n,path):s=importlib.util.spec_from_file_location(n,str(path));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ce=module('R18_examples',R/'scripts/check-examples.py');vg=module('R18_schema',R/'scripts/validate-guides.py');n,failures=ce.check_file(str(p));assert n==0 and not failures
errors=[];warnings=[]
with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),errors,warnings,only_files={str(p.relative_to(R))})
assert not errors and not warnings;diff=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert diff.returncode==0
checks={'role':'writer, not independent review','controls':controls,'control_count':len(controls),'own_selected_native_ranges':7,'exact_source_checks':source,'prior_A_manifest':{'sha256':H(A/'writer-A-handover-manifest.json'),'members_rehashed':len(priorhash),'mismatches':0},'full_inverse_and_all_native_rows':True,'all_prior156_current_units_and346_old_topics_retained':True,'original_examples':{'blocks':n,'failures':failures,'original_executable_blocks':0,'original_sections7_11_and_all_unedited_illustrations_exact':True},'schema':{'errors':errors,'warnings':warnings,'stdout':out.getvalue()},'diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr}}
dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f"""# Germany crypto DE-R44–46 writer successor

Three finite own-source findings use selected narrow A. This is writer work pending C's exact independent review, not a country PASS or accountant attestation.

R44 qualifies the46(3)employee deduction by actual eligibleincome,32d6exclusion and excessage/13(3)reductions, with400−100=300separator and separate above410hardshipreferral. R45 replaces false sourceabsence with the actual2025ELSTERsimpleinheritance/per-personthresholdroute. The2026ordinaryroute is expressly labelled unchanged-statute/admin-method continuation, not a2026formread. Predecessor dates/costs/ownership are required; no deathclockreset, assumedmarketstepup, pooledspousalallowance or contestedestateallocation is invented. R46 gives actual2025below256/1000nonentry andwithin-scopelossentry instructions; actual2026formlayout, otherincome/overallfiling and153duties remain separate.

Guide `{proof['after_sha256']}` ({proof['bytes']}bytes),version1.2,29October2026; ledger `{inv['ledger_sha256']}`. Seven full own selected ranges actuallyread29October, with exactoriginal-languagequotes/officialURLs/raw-readeridentities and dated2025formscope in own-actual-read-quotes.json. EarlierAanchors retain their actualoriginalreading/excerptprovenance. No fresh acquisition or rawchange. All{len(priorhash)}Aseal members rehash unchanged. The fullledger retains156prior currentIDs, has158currentunits and preserves346oldtopicidentities/destinationhistory with correctionnotes.

Eight exactoperations/fullinverse, alloriginalURLorder/attribution/CTA/trust/protectedfields and everyuneditedoriginalillustration are exact. ActualoriginalGuide has0oa-checkblocks, faithfully reported. {len(controls)}meaningful new controls, allnative/sourcechecks and scoped oneGuide schema0/0/diff pass. Original protocol/NFT/loan/classificationlimits remain unchanged. Original countryfreeze/priorwriters/reviews are immutable. No Git, PR, publicplatform or Francewriting. Exact options/preimages/operations/current-oldmaps/sourceindexes/checks remain alongside this report.
""")
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file() and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'Writer successor, independent review pending','artifacts':entries});freeze={'status':'writer successor, different independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(controls)};dump(W/'freeze.json',freeze);print(json.dumps({**freeze,'freeze_sha256':H(W/'freeze.json')},indent=2))
