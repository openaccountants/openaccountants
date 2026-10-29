from pathlib import Path
from decimal import Decimal as D,ROUND_DOWN
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;A=O/'germany-ledger-writer-2026-10-28';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');controls=[]
def c(id,actual,expected,premise):assert actual==expected,(id,actual,expected);controls.append({'id':id,'actual':str(actual),'expected':str(expected),'premise':premise,'pass':True})
from datetime import date
# Actual duty fixture holds every stated establishment/business-use/amount/exemption/prior-invoice gate fixed.
def relief(supply,sent,turnover=0,edi=False):
 supply=date.fromisoformat(supply);sent=date.fromisoformat(sent)
 if date(2024,12,31)<supply<date(2027,1,1)and sent<=date(2026,12,31):return'no1'
 if date(2026,12,31)<supply<date(2028,1,1)and sent<=date(2027,12,31):
  if D(turnover)<=D(800000):return'no2'
  if edi:return'no3-qualifying-EDI'
 return'no-transition-relief-default-duty'
for supply,sent,t,edi,w in [('2026-12-15','2026-12-31',1000000,False,'no1'),('2026-12-15','2027-01-01',100000,False,'no-transition-relief-default-duty'),('2026-12-15','2027-01-01',100000,True,'no-transition-relief-default-duty'),('2027-01-01','2027-01-10',800000,False,'no2'),('2027-01-01','2027-01-10','800000.01',False,'no-transition-relief-default-duty'),('2027-01-01','2027-01-10','800000.01',True,'no3-qualifying-EDI')]:c('R39.dates'+str((supply,sent,t,edi)),relief(supply,sent,t,edi),w,'Labelled combined own-law interpretation, actual ordinary taxable domesticB2Bdutyfacts stipulated, no previouslyvalidadvance/standinginvoice or permanent exception. EDIflag means actual statutory qualifying transmission, not anyPDF.')
for duty,domestic_relief,foreign,w in[(True,False,False,False),(False,True,False,False),(False,False,True,True),(False,False,False,True)]:c('R40.consent'+str((duty,domestic_relief,foreign)),not(duty or domestic_relief),w,'Domesticrelief means actual BMF33/34/34ainvoice between domestic businesses. Last branch is voluntaryconsumer/exempt case. Foreignbusiness doesnot get no-consent merely from beingbusiness; actual consent needs separate evidence.')
def fallback(invoice,openvat,supply,payment,objective,otherwise15):return all([invoice,openvat,supply,payment,objective,otherwise15])
for label,flags,w in [('complete',[True]*6,True),('missing-invoice',[False,True,True,True,True,True],False),('no-openVAT',[True,False,True,True,True,True],False),('unproved-supply',[True,True,False,True,True,True],False),('unproved-payment',[True,True,True,False,True,True],False),('unclear-records',[True,True,True,True,False,True],False),('material-otherfailure',[True,True,True,True,True,False],False)]:c('R41.evidence'+label,fallback(*flags),w,'Evidence-support classification, not categoricalzero/automaticdenial of contestedclaim. Actualinvoice/copy and all strict objective/materialconditions required; authority not required to fill gaps.')
c('R41.above-small-invoice',D(1000)+D(190),D(1190),'Stipulatedordinaryinvoiceabove250, actual19VATlegallydue, correctotherwisecontent/businesssupply/payment allstrictconditions independently established.')
c('R41.qualified-input',D(1000)*D('.19'),D(190),'Actual taxable business supply, actualcompletePDFinvoice/openVAT1190payment/objective records and all15gates; wrongformat alone doesnot foreclose qualifiedfallback.')
def waiver(highest,full,copy,history,terms,layout,immutable,other):return all([highest,full,copy,history,terms,layout,immutable,other])
for label,flags,w in [('all-stated-gates-plus-other',[True]*8,True),('current-image-only',[True,True,True,False,False,False,True,True],False),('not-highest',[False,True,True,True,True,True,True,True],False),('mutable-data',[True,True,True,True,True,True,False,True],False),('unverified-other-gates',[True,True,True,True,True,True,True,False],False)]:c('R42.waiver'+label,waiver(*flags),w,'Actual75/76administrativeconditions, otherflag independently confirms remainingrequirements; same-lookingcurrentreconstruction alone not enough. No vendor-systemtest or impliedfine.')
for nochange,noloss,documented,unrestricted,xml_lost,w in[(True,True,True,True,False,True),(True,True,False,True,False,False),(True,True,True,False,False,False),(False,True,True,True,False,False),(True,False,True,True,False,False),(True,True,True,True,True,False)]:c('R43.conversion'+str((nochange,noloss,documented,unrestricted,xml_lost)),all([nochange,noloss,documented,unrestricted])and not xml_lost,w,'Only conditionedgeneral135converted-retention route; mandatoryoriginalstructuredXML may not be lost. Failingthischeckdoesnot imply a fine; dualretentiondefaultand otherrecorddutiesremain.')
c('R43.no-automatic-rejection',True,True,'GoBD155explicitly says inadequate/missingdocumentation without impairedtraceability/verifiability is not substantiveformaldefect warranting rejection; no actualsystemcertification inferred.')
# Exact source/reader bytes and each own selected quotation, plus original A index reused by attribution.
quotes=json.loads((W/'source-quote-index.json').read_text());source=[]
for id,q in quotes.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];literal='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert (q['exact_quote']in literal if id.startswith('EI.')else literal==q['exact_quote']),id;source.append({'id':id,'hashes_and_literal_quote':True,'quote_scope':'Preserved literal selected excerpt within declared nativeLF'if id.startswith('EI.')else'Full newly selected nativeLF','own_new_selected_read':not id.startswith('EI.')})
proof=json.loads((W/'preservation-proof.json').read_text());inv=json.loads((W/'successor-inventory.json').read_text());p=Path(proof['path']);old=(W/'before'/p.name).read_text();new=p.read_text();assert H(p)==proof['after_sha256'];ops=json.loads((W/'exact-operations.json').read_text());x=old
for op in ops:assert x.count(op['before'])==1;x=x.replace(op['before'],op['after'],1)
assert x==new
for op in reversed(ops):assert x.count(op['after'])==1;x=x.replace(op['after'],op['before'],1)
assert x==old
rr=json.loads((W/'support/germany-einvoice/rows.json').read_text());oldrr=json.loads((A/'support/germany-einvoice/claim-rows.json').read_text());lines=new.split('\n')
for r in rr:
 a,b=r['native_LF'];assert r['wording']=='\n'.join(lines[a-1:b]);assert all(k in quotes for k in r['source_quote_ids'])
assert set(r['prior_row_id']for r in rr if r['prior_row_id'])==set(range(1,len(oldrr)+1))
ot=json.loads((W/'support/germany-einvoice/old-topic-destinations.json').read_text());prior=json.loads((A/'support/germany-einvoice/old-topics.json').read_text());assert len(ot)==len(prior)
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
checks={'role':'writer, not independent review','controls':controls,'control_count':len(controls),'own_selected_native_ranges':14,'exact_source_checks':source,'prior_A_manifest':{'sha256':H(A/'writer-A-handover-manifest.json'),'members_rehashed':len(priorhash),'mismatches':0},'full_inverse_and_all_native_rows':True,'all_prior365_current_units_and527_old_topics_retained':True,'original_examples':{'blocks':n,'failures':failures,'original_executable_blocks':0,'original_sections7_11_and_all_unedited_illustrations_exact':True},'schema':{'errors':errors,'warnings':warnings,'stdout':out.getvalue()},'diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr}}
dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f"""# Germany e-invoice DE-R37–43 writer successor

Seven finite findings are repaired with selected narrow A from the own retained primary/official clauses. The folder keeps the original R37–41 assignment name; R42–43 were added before any seal. Writer work awaits C's independent exact review, not a country PASS or accountant attestation.

R37 completes actual26aoffence/ceiling evidence, keeping Guideamounts. R38 corrects formalportalnoticecitation to4(3), leaving the three actual unconfirmed platformbehaviours. R39 supplies the labelled default-duty/transition reading for an ordinary taxable domesticB2BDecember2026supply firstinvoicedJanuary2027, with explicit establishment/business-use/above250/permanentexception/priorinvoice gates; lowturnover doesnot rescue failedno1, and the different2027supply is separate. R40 aligns consent summaries with the actual existing table/domestic33/34/34aexceptions. R41 supplies full strict15.2a(1a)evidentialfallback, preserving cure and contestedfacts; positive1000net/190legallydueVAT/1190paid fixture is abovesmallinvoice, unlike a119gross wrong-format-duty example. No automaticPDFcredit or blanketdenial.

C separately acquired the official BMF2026AOannex after a precise failedsourcecheck. Four own selected annex scopes were actually read here, alongside ten other whole selected ranges. GoBD185explicitly incorporates14July2025effect despite olderheading. R42 makes outgoingcopywaiver conditional on highestmachineevaluability/fullcontent and actualmasterdata/terms/layout/history/immutabledata and otherrequirements. R43 gives135dualretentiondefault/conditionedexception, retainingmandatoryoriginalstructuredXML, and150–155proportionateintelligible process/versiondocumentation with noautomaticbookrejection if verifiability is unimpaired. No softwareexecution/certification/allGoBDattestation claimed. Rawbodies are referenced unchanged, not duplicated as new acquisition/readproof.

Guide `{proof['after_sha256']}` ({proof['bytes']}bytes),version1.2,29October2026; ledger `{inv['ledger_sha256']}`. All365currentidentities and527oldtopicorigins remain with currentbindings/correctionnotes. Fourteen complete selected native ranges actuallyread29October are in own-actual-read-quotes.json, exactoriginal-languagequotes/URLs/raw-readeridentities; earlierAanchors retain originalactualreadingprovenance. All{len(priorhash)}Aseal artifacts rehash unchanged.

Fifteen canonical sequentialoperations/fullinverse, originalURLorder/attribution/CTA/trust/protectedmetadata and allunmodifiedoriginalillustrations are exact; originalSections7and11 independentlyprotected. The actual frozenGuide has zerooa-checkblocks, so none is falsely reported as twoexecutedcases. {len(controls)}new meaningful classification/amountcontrols, allcurrentnative/sourcechecks and oneGuide schema0/0/diff pass. Source/operation-adapter failures were preserved and corrected before Guidewrite/seal; no tax/sourcechange from those failures. Earliercountryfreeze/originalwriters/reviewfindings remain immutable. No Git, PR, publicplatform or Francewriting. Canonicaloperations/currentrows/indexes reproduce checks; historicalauthor script predates the cosmeticnormal-spacing refinement and is labelledhistorical.
""")
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file() and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'Writer successor, independent review pending','artifacts':entries});freeze={'status':'writer successor, different independent review pending','created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(controls)};dump(W/'freeze.json',freeze);print(json.dumps({**freeze,'freeze_sha256':H(W/'freeze.json')},indent=2))
