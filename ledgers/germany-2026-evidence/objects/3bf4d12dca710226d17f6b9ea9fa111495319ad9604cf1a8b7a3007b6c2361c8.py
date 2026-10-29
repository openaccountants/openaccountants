from pathlib import Path
from decimal import Decimal as D
import json,hashlib,re,sys,importlib.util,subprocess,contextlib,io
P=Path(__file__).resolve().parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages');H=lambda b:hashlib.sha256(b).hexdigest();controls=[]
def check(id,actual,expected,premise):
 assert actual==expected,(id,actual,expected);controls.append({'id':id,'actual':str(actual),'expected':str(expected),'premise':premise,'pass':True})
def commute(price,km,months,days,actual=None):
 deemed=D(str(price))*D('0.0003')*D(str(km))*D(str(months)) if actual is None else D(str(actual));allowance=D(str(km))*D(str(days))*D('.38');return deemed,allowance,max(D(0),deemed-allowance)
for id,args,out in [('standard',(40000,20,12,200),('2880','1520','1360')),('actual1000',(40000,20,12,200,1000),('1000','1520','0')),('actual2000',(40000,20,12,200,2000),('2000','1520','480')),('six-month-nonpositive',(40000,20,6,200),('1440','1520','0')),('three-month',(40000,20,3,50),('720','380','340'))]:
 for label,x,y in zip(['D','A','extra'],commute(*args),out):check('R01.'+id+'.'+label,x,D(y),'Stipulated ordinary combustion car, no benefits reducing allowance; full one-way km and actual days. Separate private use not included.')
def meal(hours,overnight_branch=False,full=False):return D(28) if full and hours==24 else D(14) if overnight_branch or hours>8 else D(0)
for id,h,o,f,w in [('short-no-overnight',2,False,False,0),('short-departure-overnight',2,True,False,14),('exact8-no-overnight',8,False,False,0),('over8-no-overnight',8.01,False,False,14),('full24',24,False,True,28),('arrival-following-overnight',2,True,False,14)]:check('R02.'+id,meal(h,o,f),D(w),'Qualifying business travel; no supplied meals/reimbursements; within three-month limit. Overnight flag means actual qualifying that/preceding/following-day overnight.')
for total,c,w in [('500000','15000',True),('500000','15000.01',False),('1000000','24500',True),('1000000','24500.01',False)]:
 for result in ['profit','loss']:
  check('R05.net-'+total+'-'+c+'-'+result,D(c)<=D(total)*D('.03') and D(c)<=D(24500),w,'Otherwise qualifying separable own-origin side activity; denominator includes both activities; net receipts, not profit. Branch result does not alter gates.')
for id,withdraw,exclude,result in [('tax-only',20000,20000,105000),('partial',20000,10000,95000),('priority20of25',25000,20000,100000)]:check('R06.retained-'+id,D(100000)-max(D(0),D(withdraw)-D(exclude))+D(5000),D(result),'Stipulated profit100000/trade tax5000/no contributions; exclusion amount independently qualifies as own34a(1)tax+Soli; no full elective-regime computation claimed.')
for liability,w in [(0,8000),(10000,0),(6000,4000)]:check('R06.outside-liability-'+str(liability),min(max(D(0),D(10000)-D(liability)),D(8000)),D(w),'10000 negative-capital increase; 8000 available statutory prior-loss cap; indicated qualifying outside liability exists/arises because of withdrawal and all1(2)/(3)conditions met. No later liability reduction assumed.')
check('R03.health-cap',min(D(72000),D(69750))*D('.0875')*D('.96'),D(5859),'Stipulated fund additional2.9% and sick-pay deduction; explicit current BMG2026 contribution ceiling.')
check('R03.care-cap',min(D(72000),D(69750))*D('.018'),D('1255.50'),'Stipulated parental employee care rate1.8%, outside Saxony; same actual2026 ceiling.')
check('R04.non-table-mandatory-case',not(any([False,False,True])),False,'The listed common cases are false but own46(2)no7 mandatory case is true: voluntary conclusion is false.')
check('R04.no-statutory-mandatory-case',not(any([False,False,False])),True,'No statutory mandatory case applies: application assessment remains available.')
# Corporate single-current-year separators; old/current mixed allocation intentionally not asserted.
for net,escape,ec,ic in [(2000000,True,0,0),(3000000,False,0,0),(4000000,False,0,1000000),(0,False,0,0)]:
 capacity=D(10000000)*D('.30'); generated=D(0) if escape or net<=0 else max(D(0),capacity-D(net)); interest=D(0) if escape else max(D(0),D(net)-capacity)
 check('R07.EBITDA-generation-'+str(net),generated,D(ec),'Tax EBITDA10000000, no prior carries; stated current-year escape facts; generation barred for escape/nonpositive-net years.')
 check('R07.interest-carry-'+str(net),interest,D(ic),'Same fixture; no other escape where indicated; no mixed-carry ordering inference.')
remaining=D(500);use={};vintages={2020:D(100),2021:D(200),2022:D(400)}
for year,amount in sorted(vintages.items()):
 if 2026-5<=year<2026:
  use[year]=min(remaining,amount);remaining-=use[year]
check('R07.oldest-eligible-vintage',use,{2021:D(200),2022:D(300)},'500 demand after current capacity in financial year2026;2020 expired,2021 then2022 capacity; no interest-carry allocation assumed.')
for paid,current,w in [('9000','1000',True),('9000','1000.01',False),('10000','0.01',False)]:check('R08.same-payer-cap-'+paid+'-'+current,D(paid)+D(current)<=D(10000),w,'Same actual payer and recipient/calendar year; actual treaty eligibility/extent established separately, not presumed from a treaty existing.')
check('R08.partial-treaty-residual',D(1000)*D('.10'),D(100),'Pure stipulated counterexample: actual applicable treaty leaves10% German tax; qualifying annual cap, no exemption certificate needed for this50c2no2 scope.10% is a hypothetical input, not a treaty rate supplied by the Guide; zero is incorrect.')
check('R08.two-fifths-refund',D(1000)*D('.25')*D(2)/D(5),D(100),'Qualifying KStG2no1 corporate recipient;250 withholding paid; actual50d3 and50c3/5 claim/proof/procedure conditions independently satisfied. No automatic refund for every foreign entity.')
proof=json.loads((P/'preservation-proof.json').read_text());inv=json.loads((P/'successor-inventory.json').read_text());q=json.loads((P/'own-actual-read-quotes.json').read_text());sourcechecks=[]
for id,x in q.items():
 if 'raw_path' in x:assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256']
 if 'reader_path' in x:
  p=Path(x['reader_path']);assert H(p.read_bytes())==x['reader_sha256'];lo,hi=x['native_LF'];assert '\n'.join(p.read_text().split('\n')[lo-1:hi])==x['exact_quote']
 if 'web_tool_response_path' in x:assert H(Path(x['web_tool_response_path']).read_bytes())==x['web_tool_response_sha256']
 sourcechecks.append({'id':id,'exact_retained_identity_and_quote':True})
# Check own actual sibling-routing observations, distinct from whole-sibling legal review.
obs=[]
for slug,lo,hi in [('de-partners-and-part-year',89,120),('germany-to-switzerland-cross-border-tax',82,99),('germany-to-switzerland-cross-border-tax',242,242)]:
 p=R/'skills/international/germany'/f'{slug}.md';# partners has current additions: observed frozen original at89–120 is preserved in before
 if slug=='de-partners-and-part-year':p=P/'before'/p.name
 obs.append({'path':str(p),'sha256':H(p.read_bytes()),'native_LF':[lo,hi],'actual_quote':'\n'.join(p.read_text().split('\n')[lo-1:hi]),'read_date':'2026-10-29','scope':'Own actual availability/precise-limit observation only; no independent whole sibling legal verdict.'})
(P/'sibling-routing-observations.json').write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n')
# Scoped executable original cases and schema, no index generation / full-repo tests.
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,str(path));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
ce=module('repair_examples',R/'scripts/check-examples.py');vg=module('repair_validator',R/'scripts/validate-guides.py');errors=[];warnings=[];ex={};files=set()
for slug,p in proof.items():
 path=Path(p['path']);assert H(path.read_bytes())==p['after_sha256'];assert H((P/'ledgers'/f'{slug}.md').read_bytes())==inv[slug]['ledger_sha256'];n,f=ce.check_file(str(path));assert not f,(slug,f);ex[slug]={'original_blocks':n,'failures':f};files.add(str(path.relative_to(R)))
 rows=json.loads((P/'support'/slug/'rows.json').read_text());lines=path.read_text().split('\n')
 for row in rows:
  lo,hi=row['native_LF'];assert row['wording']=='\n'.join(lines[lo-1:hi])
 assert len({r['predecessor_row_id'] for r in rows if r['predecessor_row_id'] is not None})==inv[slug]['original_current_rows']
with contextlib.redirect_stdout(io.StringIO()) as log:vg.check_guides(vg.load_build_index(),errors,warnings,only_files=files)
assert not errors and not warnings,(errors,warnings)
diff=subprocess.run(['git','diff','--check','--',*sorted(files)],cwd=R,capture_output=True,text=True);assert diff.returncode==0,diff.stdout+diff.stderr
result={'writer_only':True,'no_independent_PASS':True,'controls':controls,'control_count':len(controls),'own_source_checks':sourcechecks,'own_selected_source_anchor_count':len(q),'examples':ex,'original_block_count':sum(x['original_blocks'] for x in ex.values()),'canonical_scoped_schema':{'files':len(files),'errors':errors,'warnings':warnings,'stdout':log.getvalue()},'scoped_diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr},'all_original_current_rows_rebound':True,'all_current_row_wording_native_exact':True,'all_successor_current_Guide_ledger_hashes_match':True}
(P/'writer-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['controls','own_source_checks']},indent=2))
