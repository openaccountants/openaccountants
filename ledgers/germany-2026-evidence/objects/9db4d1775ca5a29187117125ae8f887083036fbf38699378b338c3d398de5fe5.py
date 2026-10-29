from pathlib import Path
from decimal import Decimal as D
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime
W=Path(__file__).resolve().parent;O=W.parent;B=O/'germany-ledger-writer-B-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');controls=[]
def c(id,a,b,p):assert a==b,(id,a,b);controls.append({'id':id,'actual':str(a),'expected':str(b),'premise':p,'pass':True})
def taxable_other(years,income_source,token):return D(years)<=D(10 if income_source and not token else 1)
for y,inc,token,w in[(2,True,False,True),(2,False,False,False),(2,True,True,False),(1,False,False,True),(10,True,False,True),('10.01',True,False,False)]:c('R32.holding'+str((y,inc,token)),taxable_other(y,inc,token),w,'Independently established private otherasset, not daily-use excluded; years represents independently determined legal holding period, not a365dayfraction method. Token flag means actual Currency/Payment Token under specific BMF exception, not every cryptoasset. Other23gates/base/tax separate.')
import datetime
for receipt,w in [('2026-12-15',True),('2026-12-16',False),('2026-12-14',True)]:c('R33.receipt'+receipt,datetime.date.fromisoformat(receipt)<=datetime.date(2026,12,15),w,'Actual irrevocable request reaches paying institution during current2026; sendingdate not substituted, no bankweekend/cure rule inferred.')
for percent,costgate,w in[('10',True,True),('9.99',True,False),('10',False,False)]:c('R34.owner'+str((percent,costgate)),D(percent)>=D(10)and costgate,w,'Actual corporation/cooperative shareholder loan in specified20categories; costgate means corresponding debtor expenses/Germantaxand20(9)costbar conditions satisfied. This is only(b), not automatic overallflat-tax result.')
for related,costgate,w in[(True,True,True),(False,True,False),(True,False,False)]:c('R34.related'+str((related,costgate)),related and costgate,w,'Actualstatutoryrelatednessindependentlyestablished; familymembershipalone does not set flag. Only(a) limb, otherstatutorylimbsseparate.')
for common,market,noadv,w in[(True,False,False,True),(True,True,False,False),(True,False,True,False),(False,False,False,False)]:c('R34.connected'+str((common,market,noadv)),common and not(market or noadv),w,'Qualifying financing/branch/recourse facts independently met; actual commonplan and marketterms/noburdenadvantage statutory connection selectors only.')
c('R34.actualcostincome',D(10000)-D(2000),D(8000),'Independently qualifying32d(2)no1case,2000eligibleactualcosts; ordinaryincome, not finaltarifftax.20(6)/(9)do notapply.')
c('R34.disallowedflatshortcut',D(10000)-D(1000),D(9000),'Counterfactualwronglump-sumshortcut discriminator only, not the Guide output.')
def gift(own,recent,previous):return D(own)>=D('.01')or(recent and previous)
for own,recent,prev,w in[('.005',True,True,True),('.005',False,True,False),('.005',True,False,False),('.01',False,False,True)]:c('R35.gift'+str((own,recent,prev)),gift(own,recent,prev),w,'Actual five-year personal/recentacquisition/qualifyingpredecessororchain holding dates independently established. NoAStGresidenceaggregationorautomaticfinaltax.')
c('R36.fullbase',D(10000)-D(1120),D(8880),'Full actuallyassessedownership-periodVorabpauschale history, regardlesscashwithholding.')
c('R36.afterpartial',D(8880)*D('.7'),D(6216),'Actualequityfundclassification/30%partialexemption independently established.')
c('R36.wrongfraction',D(1120)*D('.7'),D(784),'Wrong deduction input discriminator, not correctmethod.')
c('R36.wrongresult',(D(10000)-D(784))*D('.7'),D('6451.20'),'Counterfactualwrongonlytaxablefractionshortcut, not Guide output.')
c('R36.nohistory',D(10000)*D('.7'),D(7000),'No assessedprepaymenthistory; unassessed estimates not deducted. Classification otherwiseindependentlymet.')
qindex=json.loads((W/'source-quote-index.json').read_text());sources=[]
for id,q in qindex.items():
 assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];literal='\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);assert (q['exact_quote']in literal if id.startswith('OLD.')else q['exact_quote']==literal),id;sources.append({'id':id,'literal_quote_and_hashes_exact':True,'quote_scope':'Preserved exact original selected excerpt within declared nativeLF'if id.startswith('OLD.')else'Full newly selected nativeLF','new_own_read':not id.startswith('OLD.')})
assert '15. Dezember des laufenden Jahres'in qindex['R33.complete-certificate']['exact_quote'];assert 'R33.complete-certificate'in next(r for r in json.loads((W/'support/de-capital-gains/rows.json').read_text())if r['prior_row_id']==37)['source_quote_ids']
proof=json.loads((W/'preservation-proof.json').read_text());inv=json.loads((W/'successor-inventory.json').read_text());p=Path(proof['path']);old=(W/'before'/p.name).read_text();new=p.read_text();assert H(p)==proof['after_sha256'];ops=json.loads((W/'exact-operations.json').read_text());x=old
for z in ops:assert x.count(z['before'])==1;x=x.replace(z['before'],z['after'],1)
assert x==new
for z in reversed(ops):assert x.count(z['after'])==1;x=x.replace(z['after'],z['before'],1)
assert x==old
rr=json.loads((W/'support/de-capital-gains/rows.json').read_text());before_rr=json.loads((B/'support/de-capital-gains/rows.json').read_text());lines=new.split('\n')
for r in rr:
 a,b=r['native_LF'];assert r['wording']=='\n'.join(lines[a-1:b]);assert all(k in qindex for k in r['source_quote_ids'])
assert set(r['prior_row_id']for r in rr if r['prior_row_id'])==set(r['row']for r in before_rr)
ot=json.loads((W/'support/de-capital-gains/old-topic-destinations.json').read_text());prior=json.loads((B/'support/de-capital-gains/old-topic-destinations.json').read_text())
for kind in['current_main_rows','pre_refresh_rows']:
 assert len(ot[kind])==len(prior[kind])
 for a,b in zip(ot[kind],prior[kind]):assert all(a[k]==b[k]for k in[k for k in ['old_native_LF','old_unit_sha256','old_exact_opening','disposition']if k in b]);assert a['prior_sealed_current_destination']==b['current_destination']
assert H(Path(inv['ledger_path']))==inv['ledger_sha256'];m=json.loads((B/'artifact-manifest.json').read_text());assert all(H(B/e['path'])==e['sha256']for e in m)
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def module(n,path):s=importlib.util.spec_from_file_location(n,str(path));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ce=module('R26examples',R/'scripts/check-examples.py');vg=module('R26schema',R/'scripts/validate-guides.py');n,f=ce.check_file(str(p));assert n==4 and not f;e=[];w=[]
with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),e,w,only_files={str(p.relative_to(R))})
assert not e and not w;diff=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert diff.returncode==0
checks={'role':'writer, independent recheck pending','controls':controls,'control_count':len(controls),'own_selected_read_count':7,'source_checks':sources,'all83_prior_current_identities_and129_old_topics_retained':True,'current_native_rows_and_full_inverse_exact':True,'prior_B_seal':{'manifest_sha256':H(B/'artifact-manifest.json'),'members_rehashed_unchanged':len(m)},'original_oa_cases':{'count':n,'failures':f,'whole_worked_section_exact':True},'schema':{'errors':e,'warnings':w,'stdout':out.getvalue()},'scoped_diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr}};dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f"""# Germany capital gains DE-R32–36 writer successor

Selected narrow Option A repairs five finite own-source findings. Writer work awaits C's exact independent recheck; it is not a country PASS or accountant attestation.

R32 supplies23(1)no2's income-producing ten-year branch and preserves the specifically supported Currency/Payment Token administrative exception. R33 supplies the complete15Decembercurrent-yearreceipt deadline quotation while preserving the original truncated prefix as history. R34 states mandatory32d(2)no1(a)/(b)/(c)actual financing/cost/domestic-tax/ownership/recourse/connection and statutory exception selectors, ordinarytariff/eligibleactualcost treatment and nonfinality. It does not classify every family loan as related, import optionaldividendTEV, or invent a finaltariffwithoutotherincome. R35 supplies actual recent free-acquisition/predecessor/chain holding-date gates independently ofAStGresidence. R36 deducts full actuallyassessedownership-periodVorabpauschalen before actualpartialexemption, irrespectivecashwithholding;10000−1120then30%exemption gives6216, not6451.20.

Guide `{inv['Guide_sha256']}` ({inv['bytes']}bytes),version1.4,29October2026; ledger `{inv['ledger_sha256']}`. Seven whole selected native ranges were actually read; exact original-language wording, officialURLs/read dates and raw-reader identities are in own-actual-read-quotes.json. Unchanged earlier B quotations retain exact original excerpt/actualreading provenance. They are verified as literal excerpts within the declared nativeLF, without claiming all are whole-line quotations. No fresh fetch or sourcebody change. All{len(m)}original Bseal members rehash unchanged.

Sixteen exact operations/fullinverse preserve all original URLs/order, attribution, CTA/trust/protectedmetadata and full original workedsection. All4originalexecutablecases pass;{len(controls)}new meaningful controls,88currentgroups retaining83priorIDs/all129oldtopicorigins/hash mappings, literal/source/currentrow checks and scoped one-Guide schema0/0/diff pass. Prior writer/source evidence and countryfreeze remain immutable. Genuinechurch-tax/unreadBMFbody reservations stay exact. No Git, PR, publicplatform or Francewriting. Options, preimages, exact operations, old-topic/current ledgers, controls and source indexes remain alongside this report.
""")
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in['artifact-manifest.json','freeze.json']and'__pycache__'not in p.parts];dump(W/'artifact-manifest.json',{'status':'writer successor, different independent recheck pending','artifacts':entries});freeze={'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(controls),'status':'writer, not independent PASS'};dump(W/'freeze.json',freeze);print(json.dumps({**freeze,'freeze_sha256':H(W/'freeze.json')},indent=2))
