from pathlib import Path
from decimal import Decimal as D
from datetime import datetime,timezone
import json,hashlib,re,sys,importlib.util,contextlib,io,subprocess
W=Path(__file__).resolve().parent;O=W.parent;P=O/'germany-DE-R97-R108-planning-writer-successor-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');cs=[]
def c(id,a,b,scope):assert a==b,(id,a,b);cs.append({'id':id,'actual':str(a),'expected':str(b),'scope':scope,'pass':True})
def minimum(income,allowance):return max(D(60),min(D('.04')*D(income),D(2100))-D(allowance))
def actual_allowance(entitled,payment,required):return D(entitled)*min(D(1),D(payment)/D(required))
c('R114.ordinary_minimum',minimum(20000,175),D(625),'Directly eligible isolated age30 claimant, no indirectly eligible spouse/children, actual prior relevant statutory insured income20k.')
c('R114.half_allowance',actual_allowance(175,D('312.50'),625),D('87.50'),'Actual qualifying own payment, not annual turnover/current income.')
c('R114.high_minimum',minimum(100000,175),D(1925),'Cap4%income at2100 BEFORE subtracting entitled175 allowance.')
c('R114.cap_separator',minimum(100000,175)!=min(D('.04')*100000-175,D(2100)),True,'Reject cap-after-subtraction method.')
c('R114.floor',minimum(0,175),D(60),'Sockel floor even where4%income less allowance is negative.')
c('R114.low_floor',minimum(5000,175),D(60),'Unfloored25 becomes60, no contribution-free full allowance.')
c('R114.floor_half',actual_allowance(175,30,60),D('87.5'),'Actual30 payment over60 statutory minimum, proportional175 allowance.')
c('R114.no_payment',actual_allowance(175,0,625),D(0),'Entitlement before contribution reduction is not automatically credited full175.')
c('R114.overpayment',actual_allowance(175,1000,625),D(175),'Overpayment does not multiply entitlement above full basic allowance.')
c('R114.child_old',minimum(20000,175+185),D(440),'Documented actual pre2008 child entitlement allocated to this directly eligible claimant; not mere childcount.')
c('R114.child_new',minimum(20000,175+300),D(325),'Documented post2007 child entitlement allocated to claimant; otherwise no assumed300.')
c('R114.two_children',minimum(20000,175+185+300),D(140),'Both actual child entitlements independently established; no implied two-claimant duplication.')
c('R114.under25_first',minimum(20000,175+200),D(425),'Directly eligible under25 at year-start, actual first qualifying post2007 requested contribution year. Age30 examples do not include200.')
c('R114.first_year_only',minimum(20000,175),D(625),'Later year does not receive invented repeated200 bonus.')
c('R114.own_plus_allowance_cap',min(D(3000)+175,D(2100)),D(2100),'10a comparison cap for eligible own qualifying payment plus entitled allowance; not sole own-payment cap.')
c('R114.tax_addback',D(9200)+175,D(9375),'Stipulated actual tariff with deduction9200; required entitlement add-back175, not automatic double allowance.')
c('R114.actual_comparison_saving',D(10000)-(D(9200)+175),D(625),'Stipulated actual without-deduction10000; not800+175 saving. No new universal tariff saving.')
c('R114.both_requested_transfer',True,True,'Different-sex married/non-separated qualifying EU/EEA parents: actual joint request needed to transfer mother allocation; no childcount allocation.')
c('R114.total_recovery',False,False,'Child Kindergeld wholly reclaimed for assessment period removes actual child allowance; no positive fixture assumes otherwise.')
inv=json.loads((W/'successor-inventory.json').read_text());p=Path(inv['Guide_path']);assert H(p)==inv['Guide_sha256'];before=(W/'before'/p.name).read_text();after=p.read_text();assert after==(W/'after'/p.name).read_text();ops=json.loads((W/'exact-operations.json').read_text());x=before
for q in ops:assert x.count(q['before'])==1;x=x.replace(q['before'],q['after'],1)
assert x==after
for q in reversed(ops):assert x.count(q['after'])==1;x=x.replace(q['after'],q['before'],1)
assert x==before
para=next(l for l in before.split('\n')if l.startswith('For an ordinary employee with qualifying pension contributions'));assert after.count(para)==1;ls=after.split('\n');n=next(i for i,l in enumerate(ls)if l.startswith('| Later and locked |'));assert all(ls[i].startswith('|')for i in range(n-4,n+1));assert ls[n+1]==''and ls[n+2]==para
c('R113.contiguous_original_table',True,True,'Header/separator/three original data rows contiguous; exact moved employer paragraph after final row, all words/amounts same.')
qs=json.loads((W/'source-quote-index.json').read_text());own=json.loads((W/'own-actual-read-quotes.json').read_text())
for id,q in own.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];assert q['exact_quote']in'\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b])
rows=json.loads((W/'support/rows.json').read_text());priorrows=json.loads((P/'support/germany-tax-optimization/rows.json').read_text());assert [q['id']for q in rows[:len(priorrows)]]==[q['id']for q in priorrows]
for q in rows:
 a,b=q['native_LF'];assert q['wording']=='\n'.join(ls[a-1:b]);assert all(k in qs for k in q['source_quote_ids'])
# Explicit whole nonblank coverage includes appended Riester methods, even where mapped inside one replacement row.
covered={n for q in rows for n in range(q['native_LF'][0],q['native_LF'][1]+1)}
for n,l in enumerate(ls,1):
 if l.startswith(('For an isolated directly eligible claimant','Document allowance entitlement')):assert n in covered
old=json.loads((W/'support/old-topic-destinations.json').read_text());prior=json.loads((P/'support/germany-tax-optimization/old-topic-destinations.json').read_text());assert len(old)==len(prior)==455
for q,b in zip(old,prior):assert all(q[k]==b[k]for k in ['ref','old_lf','section','wording'])
tr=json.loads((W/'pre-refresh-route-index.json').read_text());assert [q['pre_refresh_index']for q in tr]==list(range(1,135))
for q in tr:
 for t in q['components']:
  a,b=t['current_native_LF'];txt='\n'.join(ls[a-1:b]);assert txt==t['current_actual_clause'];assert hashlib.sha256(txt.encode()).hexdigest()==t['current_clause_sha256'];assert all(k in qs for k in t['source_quote_ids'])
for i in [87,88]:
 txt=' '.join(t['current_actual_clause']for t in tr[i-1]['components']);assert all(k in txt for k in ['2,100','625','312.50','87.50','1,925','185','300'])
 c('R114.oldroute'+str(i),True,True,'Prior source-only/historical Riester numeric origin now routes to actual current numeric ordinary method and documented allocation.')
ex=lambda t:re.findall(r'\*\*Example \d\..*?(?=\n\n|\Z)',t,re.S);assert len(ex(before))==5 and ex(before)==ex(after);assert re.findall(r'```oa-check.*?```',before,re.S)==re.findall(r'```oa-check.*?```',after,re.S)==[];assert re.findall(r'https?://[^\s)>]+',before)==re.findall(r'https?://[^\s)>]+',after);assert before.split('---',2)[1]==after.split('---',2)[1];assert H(Path(inv['ledger_path']))==inv['ledger_sha256']
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def mod(n,p):sp=importlib.util.spec_from_file_location(n,str(p));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
ce=mod('r114e',R/'scripts/check-examples.py');vg=mod('r114v',R/'scripts/validate-guides.py');n,fail=ce.check_file(str(p));assert n==0 and not fail;es=[];ws=[]
with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),es,ws,only_files={str(p.relative_to(R))})
assert not es and not ws;d=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert d.returncode==0
m=json.loads((P/'artifact-manifest.json').read_text())['artifacts']
for e in m:assert H(P/e['path'])==e['sha256']
dump(W/'writer-checks.json',{'role':'writer successor, independent review pending','controls':cs,'control_count':len(cs),'own_source_scopes':len(own),'full_inverse_ops':len(ops),'current_rows':len(rows),'all_prior_current_ids':True,'old_origins':len(old),'all134actualcomponents_rebound':True,'original_five_case_paragraphs_exact':True,'original_oa':n,'schema_errors':es,'schema_warnings':ws,'diff_returncode':d.returncode,'prior23members_unchanged':len(m)})
(W/'writer-report.md').write_text('''# Planning DE-R113–114 writer successor

The exact employee pension paragraph now follows the final Basisrente table row; header/separator/three original data rows are contiguous, with every legal word and amount preserved. The existing directly eligible Riester branch now supplies actual2100cap/175basic/185or300child allowance, under25 first-year200 qualification,4%prior relevant income capped before allowance subtraction,60floor and proportional allowance reduction. Child entitlement/Kindergeld recovery/allocation and actual both-parent transfer requests are stated; no universal voluntary-self-employed or indirect-spouse entitlement is inferred. The isolated age30/no-child20k claimant needs625 own payment,312.50 gives87.50 allowance;100k gives1925 minimum. The10a comparison/add-back avoids counting both full deduction saving and allowance. No ranking/product advice or actual client saving is claimed.

Five full own selected operative quotation/native scopes reread29October2026; all raw/reader hashes/officialURLs/original-language quotes retained. No acquisition. Three exact operations invert to45b98bb4, same unpublished1.3 version. All323 current IDs,455 exact old origins and134 component routes retained/rebound;87/88 now point to the numeric method rather than quotations/history alone. All five original qualitative example paragraphs/0oa/URLs/order/CTA/protected metadata exact. writer-checks.json records22meaningful separators, literal native/source/old-route checks, schema0/0/examples/diff. All23predecessor seal members remain unchanged, including its original formatting/numeric-method findings history. Writer only, C’s different exact review pending; no countryPASS/publication/France writing.
''')
entries=[{'path':str(x.relative_to(W)),'sha256':H(x),'bytes':x.stat().st_size}for x in sorted(W.rglob('*'))if x.is_file()and x.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in x.parts];dump(W/'artifact-manifest.json',{'status':'writer successor, independent review pending','artifacts':entries});f={'status':'writer successor, independent review pending','report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(cs)};dump(W/'freeze.json',f);print(json.dumps(f,indent=2))
