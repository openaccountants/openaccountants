from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,ROUND_HALF_UP
from datetime import datetime,timezone
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess
W=Path(__file__).resolve().parent;O=W.parent;P=O/'germany-root-rental-ledger-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');cs=[]
def c(id,a,b,scope):assert a==b,(id,a,b);cs.append({'id':id,'actual':str(a),'expected':str(b),'scope':scope,'pass':True})
def branch(ratio,forecast):return D(1)if ratio>=D('.66')or(ratio>=D('.50')and forecast>=0)else ratio
for ratio,forecast,w in [('.5',0,'1'),('.65',0,'1'),('.65',-1,'.65'),('.49',100,'.49'),('.66',-100,'1')]:c('R109.'+str((ratio,forecast)),branch(D(ratio),forecast),D(w),'Stipulated permanent residential let, full actual other conditions. Published2025 ELSTER no-loss selector on unchanged2026 statutory band; not alleged older BMF express equality wording.')
c('R109.zero_separator',D(10000)*branch(D('.6'),0),D(10000),'Forecast exactlyzero means full expense, not6000 paid-share restriction under this administrative instruction.')
c('R109.loss_separator',D(10000)*branch(D('.6'),-1),D(6000),'Negative forecast retains expense splitting, no automatic all-cost deduction.')
c('R110.four_normal',F(400000)*F(3,100)*4,F(48000),'Four full January years, current own3% branch.')
c('R110.four_special',F(320000)*F(5,100)*4,F(64000),'Eligible320000 capped special base, four independently qualifying years through2029.')
res=F(400000)-48000-64000;life=F(100,3)-4;afa=res/life
c('R110.residual',res,F(288000),'Actual fixture cost less both normal/special deductions.')
c('R110.remaininglife',life,F(88,3),'Mathematical3% life lessfour years, not rounded33years.')
c('R110.exact_afa',afa,F(108000,11),'First following full year2030, exact rational before display.')
c('R110.display',(D(afa.numerator)/D(afa.denominator)).quantize(D('.01'),rounding=ROUND_HALF_UP),D('9818.18'),'Display only; not an assessment-rounding legal claim.')
c('R110.not_originalrate',afa!=F(288000)*F(3,100),True,'Remaining useful-life rate, not unadjusted3% of residual.')
c('R110.5a_alternative',F(288000)*F(5,100),F(14400),'Conditional independent §7(5a) alternative with this separately established residual, not the straight-line example itself.')
c('R110.sunset_wait',2024+4,2028,'Own BMF example:2026 old-window sunset does not cut four-year benefit-period clock; regular2027 unchanged.')
c('R111.direct',D(1000),D(1000),'Identifiable repair wholly rented-room related; private-only expense excluded.')
c('R111.shared',D(10000)*D('.2'),D(2000),'Independently supported20% usable-area allocation for shared roof cost; not a universally prescribed ratio.')
c('R111.total',D(1000)+D(10000)*D('.2'),D(3000),'Before any other actual expense/capitalisation/cheap-let limitation.')
c('R111.private_only',D(700)*0,D(0),'Identifiable private part expense remains excluded; room letting does not convert all household expense.')
inv=json.loads((W/'successor-inventory.json').read_text());p=Path(inv['Guide_path']);assert H(p)==inv['Guide_sha256'];before=(W/'before'/p.name).read_text();after=p.read_text();assert after==(W/'after'/p.name).read_text();ops=json.loads((W/'exact-operations.json').read_text());x=before
for op in ops:assert x.count(op['before'])==1;x=x.replace(op['before'],op['after'],1)
assert x==after
for op in reversed(ops):assert x.count(op['after'])==1;x=x.replace(op['after'],op['before'],1)
assert x==before
qs=json.loads((W/'source-quote-index.json').read_text());own=json.loads((W/'own-actual-read-quotes.json').read_text())
for id,q in own.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];assert q['exact_quote']in'\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b])
rows=json.loads((W/'support/current-rule-rows.json').read_text());ls=after.split('\n')
for q in rows:
 a,b=q['native_LF'];assert q['wording']=='\n'.join(ls[a-1:b]);assert all(k in qs for k in q['source_quote_ids'])
assert sorted(q['prior_row_id']for q in rows if q['prior_row_id'])==list(range(1,290))
old=json.loads((W/'support/old-topics.json').read_text());prior=json.loads((P/'old-topics.json').read_text())
for key in ['pre_refresh_rows','main_baseline_rows']:
 assert len(old[key])==len(prior[key])
 for q,b in zip(old[key],prior[key]):
  assert all(q[k]==b[k]for k in b if k not in['destination_current_native_LF','destination_wording']);assert q['prior_sealed_destination_current_native_LF']==b['destination_current_native_LF'];assert q['destination_wording']==[ls[n-1]for n in q['destination_current_native_LF']]
def worked(t):a=t.index('## Worked examples');b=t.find('\n## ',a+3);return t[a:b]
assert worked(before)==worked(after);assert re.findall(r'```oa-check.*?```',before,re.S)==re.findall(r'```oa-check.*?```',after,re.S)
assert re.findall(r'https?://[^\s)>]+',before)==re.findall(r'https?://[^\s)>]+',after)
assert re.sub(r'version: [^\n]+','version: X',before.split('---',2)[1])==re.sub(r'version: [^\n]+','version: X',after.split('---',2)[1]);assert H(Path(inv['ledger_path']))==inv['ledger_sha256']
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def mod(n,p):sp=importlib.util.spec_from_file_location(n,str(p));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
ce=mod('examples109',R/'scripts/check-examples.py');vg=mod('schema109',R/'scripts/validate-guides.py');n,fail=ce.check_file(str(p));assert n==2 and not fail
es=[];ws=[]
with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),es,ws,only_files={str(p.relative_to(R))})
assert not es and not ws;d=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert d.returncode==0
m=json.loads((P/'artifact-manifest.json').read_text())['artifacts']
for e in m:assert H(P/e['path'])==e['sha256']
dump(W/'writer-checks.json',{'role':'writer successor, independent review pending','controls':cs,'control_count':len(cs),'own_source_pairs_and_exact_native_quotes_checked':len(own),'original135_quotes_reused_by_attribution':True,'rows':len(rows),'old_origins':550,'full_inverse_ops':len(ops),'original_two_oa_and_full_worked_section_exact':True,'oa_blocks':n,'oa_failures':fail,'schema_errors':es,'schema_warnings':ws,'diff_returncode':d.returncode,'original_root_manifest_members_unchanged':len(m)})
(W/'writer-report.md').write_text('''# Germany rental DE-R109–111 writer successor

Narrow A supplies the dated published ELSTER no-forecast-loss branch, including zero, on the unchanged2026 cheap-let band. The older BMF positive-surplus wording remains identified; this is an administrative method, not a claimed new equality statute or2026 form layout. Own7a(9)/BMF66 supplies the positive post-four-year residual-value/remaining-life formula; the full January400000 example gives288000 residual and88/3 years, hence108000/11 annual AfA from2030, displayed9818.18 only. The old-window sunset does not shorten its four-year clock. Mixed owner/rental-room costs now follow actual direct attribution and documented shared allocation;1000 direct plus10000×20%=3000 before other applicable limits. Twentypercent is a stipulated supported allocation fact, not a universal area mandate.

Six retained own operative native scopes read in full29October2026, with exact raw/reader hashes, original-language quotations and officialURLs. No source acquisition; original135root quotes retain attributed read dates and RNT08 remains a web observation. Eight exact operations invert to original7723c03d. All289 prior units retained among290 current units;550 actual old identities/wording preserved and destinations rebound. Original two executable cases, entire worked section, URLs/order, protected metadata, CTA and bylines exact. writer-checks.json records20 meaningful separators, literal quote/row checks, scoped schema0/0/examples/diff. All163original root-seal members unchanged. Writer successor only, C’s different exact independent review pending; no country PASS/publication or France writing.
''')
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'writer successor, independent review pending','artifacts':entries});f={'status':'writer successor, independent review pending','created_UTC':datetime.now(timezone.utc).isoformat(),'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(cs)};dump(W/'freeze.json',f);print(json.dumps({**f,'freeze_sha256':H(W/'freeze.json')},indent=2))
