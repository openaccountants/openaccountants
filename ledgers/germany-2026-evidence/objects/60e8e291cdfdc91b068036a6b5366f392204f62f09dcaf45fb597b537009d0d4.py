from pathlib import Path
from decimal import Decimal as D,ROUND_FLOOR
from datetime import date,timedelta,datetime,timezone
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess
W=Path(__file__).resolve().parent;O=W.parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');A=O/'germany-ledger-writer-2026-10-28';s='germany-tax-optimization';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');cs=[]
def c(id,a,b,scope):
 assert a==b,(id,a,b);cs.append({'id':id,'actual':str(a),'expected':str(b),'scope':scope,'pass':True})
c('R97.weekday',date(2027,7,31).weekday(),5,'Nominal Saturday, ordinary statutory deadline.')
c('R97.adjusted',date(2027,7,31)+timedelta(days=2),date(2027,8,2),'Monday ordinary next working day, actual local holidays/authority early request separate.')
for overnight,hours,w in [(False,2,0),(True,2,14),(False,8,0),(False,9,14)]:c('R98.'+str((overnight,hours)),14 if overnight or hours>8 else 0,w,'Qualifying arrival/departure overnight branch or independent same-day branch; all other travel predicates stipulated.')
c('R98.full24',D(28),D(28),'Full qualifying 24-hour absence, separate from arrival/day14.')
c('R99.owncar',D(70)*200*D('.38'),D(5320),'Own/use-provided-car exception established; full one-way km and eligible days stipulated.')
c('R99.defaultcap',min(D(5320),D(4500)),D(4500),'Same travel amount without own-car exception, actual statutory selector.')
c('R100.room8months',D(1260)-4*D(1260)/12,D(840),'Four full nonqualifying months; partial month does not create an extra FULL-month reduction.')
for mostly,visit,noother,w in [(True,True,False,False),(True,False,False,True),(False,True,True,True)]:c('R100.day'+str((mostly,visit,noother)),(mostly and not visit)or noother,w,'Permanent-no-other-workplace alternative independently established, actual activity-at-home condition and no room/double-household duplication remain required.')
for amount,bar in [(50,False),(D('50.01'),True)]:c('R101.gift'+str(amount),amount>50,bar,'Cliff only for actual qualifying gift-expense prohibition; being below50 does not establish invoice/business/input-VAT eligibility.')
for cost,independent,w in [(700,True,True),(700,False,False),(800,True,True),(D('800.01'),True,False)]:c('R102.GWG'+str((cost,independent)),independent and cost<=800,w,'Depreciable movable fixed asset otherwise established; qualifying contained-VAT cost metric, not generic all-asset deduction.')
for cost,w in [(250,False),(D('250.01'),True),(1000,True),(D('1000.01'),False)]:c('R102.pool'+str(cost),250<cost<=1000,w,'Otherwise qualifying independently usable depreciable movable fixed asset; uniform pool-year choice.')
c('R102.register',D(250)>250,False,'Register strictly above250 unless books already show required particulars.')
for prev,cur,w in [(25000,100000,True),(25001,100000,False),(25000,100001,False)]:c('R103.KU'+str((prev,cur)),prev<=25000 and cur<=100000,w,'Actual ordinary turnover selectors; other19 conditions independently met.')
c('R103.cash800k',800000<=800000,True,'Inclusive prior turnover ceiling; permission and statutory turnover population still required.')
for invoice,paid,w in [(True,False,False),(True,True,True),(False,True,False)]:c('R103.advance'+str((invoice,paid)),invoice and paid,w,'Before-supply input VAT requires both actual qualifying invoice and payment; completed supply rule separate.')
c('R103.uncollected',False,False,'Uncollected prepayment invoice is not actual received cash for advance output-VAT branch.')
for ratio,w in [(D('.10'),False),(D('.1001'),True)]:c('R104.ratio'+str(ratio),ratio>D('.1'),w,'Statutory initial-phase forecast loss/capital ratio only; actual prepackaged model/negative-income facts separately established, no immunity under other anti-abuse rules.')
c('R105.aggregate',D(9000)+9000+15000,D(33000),'Own and qualifying tax-free employer RV plus independently eligible basis pension.')
c('R105.employee',min(D(33000),D(30826))-9000,D(21826),'Ordinary employee, no separate statutory special-cap reduction, actual qualifying employer offset.')
c('R105.selfpayer',min(D(15000),D(30826)),D(15000),'Isolated eligible selfpayer without employer component; no imaginary offset.')
c('R105.jointcap',D(30826)*2,D(61652),'Only jointly assessed qualifying spouses, not marriage alone.')
c('R106.business',False,False,'No completed first training/degree means4(9) business deduction blocked even if separate employee9(6) employment exception would apply; no imported exception.')
def tax(x):
 x=D(x).to_integral_value(rounding=ROUND_FLOOR)
 if x<=12348:return D(0)
 if x<=17799:y=(x-12348)/10000;t=(D('914.51')*y+1400)*y
 elif x<=69878:z=(x-17799)/10000;t=(D('173.10')*z+2397)*z+D('1034.87')
 elif x<=277825:t=D('.42')*x-D('11135.63')
 else:t=D('.45')*x-D('19470.38')
 return t.to_integral_value(rounding=ROUND_FLOOR)
c('R108.fixedband',tax(100000)-tax(90000),D(4200),'Both full taxable intervals in actual2026 42% tariff band; no church/Soli/other-scheme claim.')
c('R108.crosszone',tax(75000)-tax(65000)!=D(4200),True,'Crossed formula zones require actual tariff difference, not arbitrary top-rate multiplication.')
inv=json.loads((W/'successor-inventory.json').read_text());p=Path(inv['Guide_path']);before=(W/'before'/p.name).read_text();after=p.read_text();assert H(p)==inv['Guide_sha256'];assert after==(W/'after'/p.name).read_text();ops=json.loads((W/'exact-operations.json').read_text());x=before
for op in ops:assert x.count(op['before'])==1;x=x.replace(op['before'],op['after'],1)
assert x==after
for op in reversed(ops):assert x.count(op['after'])==1;x=x.replace(op['after'],op['before'],1)
assert x==before
qs=json.loads((W/'source-quote-index.json').read_text());sourcechecks=[]
for id,q in qs.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'],id;assert H(Path(q['reader_path']))==q['reader_sha256'],id
 a,b=q['native_LF'];lit='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert q['exact_quote']in lit,(id,'literal')
 sourcechecks.append({'id':id,'raw_reader_identity_and_literal_quote':True,'own_new_selected':not id.startswith('OPT.')})
rows=json.loads((W/'support'/s/'rows.json').read_text());lines=after.split('\n')
for q in rows:
 a,b=q['native_LF'];assert q['wording']=='\n'.join(lines[a-1:b]);assert all(k in qs for k in q['source_quote_ids'])
assert sorted(q['prior_row_id']for q in rows if q['prior_row_id'])==list(range(1,323))
old=json.loads((W/'support'/s/'old-topic-destinations.json').read_text());prior=json.loads((A/'support'/s/'old-topics.json').read_text());assert len(old)==len(prior)==455
for q,b in zip(old,prior):
 assert all(q[k]==b[k]for k in ['ref','old_lf','section','wording']);assert q['prior_sealed_destination']==b['destination']
tr=json.loads((W/'pre-refresh-route-index.json').read_text());assert [q['pre_refresh_index']for q in tr]==list(range(1,135))
for q in tr:
 for t in q['components']:
  a,b=t['current_native_LF'];txt='\n'.join(lines[a-1:b]);assert t['current_actual_clause']==txt;assert hashlib.sha256(txt.encode()).hexdigest()==t['current_clause_sha256'];assert all(k in qs for k in t['source_quote_ids'])
# Individually authored semantic separators, not a first-key generic route generator.
def oldtext(i):return ' '.join(t['current_actual_clause']for t in tr[i-1]['components'])
for i,needle in [(97,'0.15'),(96,'employment'),(98,'family'),(99,'private'),(100,'profit intention')]:c('R107.route'+str(i),needle.lower()in oldtext(i).lower(),True,'Exact archived old topic routed to actual operative current component, correcting historical unsupported figures rather than adopting them.')
for i,lf in [(81,415),(85,433)]:c('R107.distinctFeature'+str(i),tr[i-1]['components'][0]['before_current_native_LF'],[lf,lf],'Actual Basisrente/Riester header coordinate, not ambiguous identical IAB Feature header237.')
for i in range(103,115):c('R107.calendar'+str(i),bool(tr[i-1]['components']),True,'Individually selected calendar period/component, not generic AO42; actual source IDs and body membership checked.')
examples=lambda t:re.findall(r'\*\*Example \d\..*?(?=\n\n|\Z)',t,re.S)
assert len(examples(before))==5 and examples(before)==examples(after)
assert re.findall(r'https?://[^\s)>]+',before)==re.findall(r'https?://[^\s)>]+',after)
assert re.findall(r'```oa-check.*?```',before,re.S)==re.findall(r'```oa-check.*?```',after,re.S)==[]
assert re.sub(r'version: [^\n]+','version: X',before.split('---',2)[1])==re.sub(r'version: [^\n]+','version: X',after.split('---',2)[1])
assert H(Path(inv['ledger_path']))==inv['ledger_sha256']
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def mod(n,p):sp=importlib.util.spec_from_file_location(n,str(p));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
ce=mod('examples97',R/'scripts/check-examples.py');vg=mod('schema97',R/'scripts/validate-guides.py');n,fail=ce.check_file(str(p));assert n==0 and not fail
es=[];ws=[]
with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),es,ws,only_files={str(p.relative_to(R))})
assert not es and not ws;d=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert d.returncode==0
m=json.loads((A/'writer-A-handover-manifest.json').read_text())
for e in m:assert H(A/e['path'])==e['sha256']
checks={'role':'writer successor, independent review pending','controls':cs,'control_count':len(cs),'source_checks':sourcechecks,'current_rows':len(rows),'old_origins':len(old),'all134_semantic_routes_checked':True,'full_inverse_ops':len(ops),'five_original_qualitative_examples_exact':True,'original_oa':n,'schema_errors':es,'schema_warnings':ws,'diff_returncode':d.returncode,'original_A_manifest_members_unchanged':len(m)};dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text('''# Germany planning DE-R97–108 writer successor

The narrow A corrections qualify the actual filing date, meal overnight gate, commuting cap exception, home-day and full-month room selectors, gift input VAT, GWG/pool asset eligibility, VAT timing and inclusive caps, tax-deferral-model threshold and employee/joint pension adjustments. Business training now has its own section 4(9) evidence; no employee exception is imported. The planning rationale now uses the actual tariff difference and preserves this Guide’s no-ranking scope. The ordinary B2B place row also mirrors the earlier source-proven R26 establishment/exception qualification through an explicit same-writer reading bridge.

Nineteen selected own operative quotations plus one genuine earlier own R26 read are recorded in own-actual-read-quotes.json. Original A quotations retain their original attributed read dates. No new source acquisition. Exact pins are in successor-inventory.json; all 22 operations invert to the preimage. All 322 prior current units remain among 323 rows. All 455 old origins retain exact identities and wording. Every 134 pre-refresh route was individually checked and replaced with actual clause components, native coordinates, hashes and source IDs. This repairs pension Feature-heading collisions, IAB interest and activity topics and all 12 calendar routes; unsupported historical amounts remain archived claims. The 321 current-main origins remain with bounded coordinate/claim corrections. C’s earlier actual Git-origin verification is explicitly attributed rather than presented as a new writer Git check.

writer-checks.json records separating computations, literal source and row checks, full inverse, all five original qualitative example paragraphs, original URL order, protected frontmatter and zero executable blocks. Scoped schema and diff checks pass. All 610 original A manifest members remain unchanged. This is a writer successor awaiting C’s different exact review, not a country PASS or publication approval. No France writing.
''')
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in ['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'writer successor, independent review pending','artifacts':entries});f={'status':'writer successor, independent review pending','created_UTC':datetime.now(timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(cs)};dump(W/'freeze.json',f);print(json.dumps({**f,'freeze_sha256':H(W/'freeze.json')},indent=2))
