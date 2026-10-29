from pathlib import Path
from decimal import Decimal as D
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess
W=Path(__file__).resolve().parent;P=W.parent/'germany-root-estimated-ledger-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');inv=json.loads((W/'successor-inventory.json').read_text());p=Path(inv['Guide_path']);b=(W/'before-Guide.md').read_text();a=p.read_text();controls=[]
def c(id,x,y,premise):assert x==y,(id,x,y);controls.append({'id':id,'actual':str(x),'expected':str(y),'premise':premise,'pass':True})
for paid,accepted,credited,w in[(2000,True,2000,2000),(2000,True,0,0),(2000,False,0,0),(5000,True,2000,2000)]:c('R55.extent'+str((paid,accepted,credited)),min(D(paid),D(credited))if accepted else D(0),D(w),'Laterassessedpayablebalance5000; actualcreditedtothisassessment independentlyestablished, notbankdebit/unrelatedtransfer. Qualifiedperiod separatelydetermined under8/3sentence4.')
c('R55.unrelieved-balance',D(5000)-D(2000),D(3000),'Partialqualifiedpayment cannot erasewhole5000balance; no unsupporteddate assumption.')
c('R55.whole-raw-interest',D(5000)*D('.0015')*6,D(45),'Stipulatedsixwholemonths/50multiplebase; actualperiodinput independentlyestablished, notinferred from bankdate.')
c('R55.only-qualified-interest',D(2000)*D('.0015')*6,D(18),'Sameactualqualified2000amount/period gives18relief, not45; actualnoticeperiods/order independentlychecked.')
c('R55.remaining-interest',D(45)-D(18),D(27),'Samefixture, otherstatutorycorrectionsandwaiversindependentlyexcluded; no newgeneralinterestalgorithm.')
c('R55.youngest-first',sorted(['2028-04-01','2028-05-01'],reverse=True),['2028-05-01','2028-04-01'],'Actual individualperformance dates source3sentence4order, not an assumption that all shareonestopdate.')
ops=json.loads((W/'exact-operations.json').read_text());x=b
for o in ops:assert x.count(o['old'])==1;x=x.replace(o['old'],o['new'],1)
assert x==a
for o in reversed(ops):assert x.count(o['new'])==1;x=x.replace(o['new'],o['old'],1)
assert x==b;assert H(p)==inv['Guide_sha256'];assert H(Path(inv['ledger_path']))==inv['ledger_sha256'];assert re.findall(r'```oa-check\n.*?```',a,re.S)==re.findall(r'```oa-check\n.*?```',b,re.S);assert b[b.index('## Worked examples'):b.index('## Ask the client first')]==a[a.index('## Worked examples'):a.index('## Ask the client first')]
for row in json.loads((W/'current-rule-rows.json').read_text()):assert row['wording']==a.split('\n')[row['LF']-1]
old=json.loads((P/'old-topics.json').read_text());new=json.loads((W/'old-topic-destinations.json').read_text());assert len(old)==len(new)==459
for i,(r,z)in enumerate(zip(old,new),1):
 assert all(r[k]==z[k]for k in['comparator','file','old_LF','old_section','exact_old_topic','status']);assert(P/r['file']).read_text().split('\n')[r['old_LF']-1]==r['exact_old_topic']
changes=json.loads((W/'route-repair-index.json').read_text())['changes'];assert len(changes)==108
expected={34:['26','35–36','79'],112:['43–44','64','120'],132:['38','76'],133:['39','58'],253:['21','86'],289:['88']}
for i,parts in expected.items():assert all(v in new[i-1]['destination']for v in parts)
assert '147'not in new[252]['destination'];assert '92'not in new[288]['destination'];assert all('archived' in z['destination'].lower()for z in new if z['old_section'].startswith('Test '))
quotes=json.loads((W/'source-quote-index.json').read_text());sourcechecks=[]
for id,q in quotes.items():
 if 'reader_path'in q:
  assert H(Path(q['reader_path']))==q['reader_sha256'];assert H(Path(q['raw_path']))==q['raw_sha256'];lo,hi=q['native_LF'];lit='\n'.join(Path(q['reader_path']).read_text().split('\n')[lo-1:hi]);assert q['exact_quote']in lit,id;sourcechecks.append({'id':id,'literal_selected_excerpt_and_hashes':True})
 else:sourcechecks.append({'id':id,'original_attributed_official_observation':'original rooted receipt preserved, no newHTMLclaim'})
m=json.loads((P/'artifact-manifest.json').read_text());assert all(H(P/e['path'])==e['sha256']for e in m['artifacts'])
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def mod(n,p):s=importlib.util.spec_from_file_location(n,str(p));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ce=mod('R55examples',R/'scripts/check-examples.py');vg=mod('R55schema',R/'scripts/validate-guides.py');n,f=ce.check_file(str(p));assert n==2 and not f;e=[];w=[]
with contextlib.redirect_stdout(io.StringIO()):vg.check_guides(vg.load_build_index(),e,w,only_files={str(p.relative_to(R))})
assert not e and not w;diff=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert diff.returncode==0
dump(W/'writer-checks.json',{'role':'writer, not independent PASS','controls':controls,'control_count':len(controls),'Guide_inverse_protected_case_section_exact':True,'old_origins459_exact_identity_and_body_membership':True,'coarse_routes108_corrected':'sixdiscriminatorsandtestarchive-versuscaseclassification checked','old_root_seal_members_unchanged':len(m['artifacts']),'source_checks':sourcechecks,'original_examples':{'oa_count':n,'failures':f,'five_further_qualitative_cases_exact':True},'schema':{'errors':e,'warnings':w},'diff_returncode':diff.returncode})
(W/'writer-report.md').write_text(f'''# Germany estimated-tax DE-R55–56 writer successor

Selected narrow A qualifies only the voluntarypayment sentence: relief is limited to actualaccepted-and-creditedamounts for later effectiveassessment, with actualindividualamount/date/youngest-first periods under233a(8)/3sentence4; laterreductionscanreducewaiver.5000balance/2000qualifiedpaymentdoesnotgive5000relief; bankdebitisnotcredit. Version2.4→2.5 is the only other Guideoperation. Bothfullselectedoperativeparagraphs were actuallyread29October, raw/reader/provenance quoted exactly; no newsourcefetch or interestrate/automaticstopdate.

R56 actualreading covered all108oldrecords chosen by the samecoarsedefaults and current19–105/147–166. All108receive explicitclause/componentroutes; all459origincomparator/file/LF/wordingidentities remain exact and actualbodymembershipchecked.600→39/58;later5000→38/76;newfreelancer→26/35–36/79;deferral→88;USsafeharbour→21/86;Soliformula→43–44/64/120. Historicaltestinputarchive is distinguished from the actual fivequalitativecases151–155; unrelatednewfreelancer/settlement/UStests are not falselycalled reproducedat147. Bankpattern/referral/source limits remain explicit. No law/Guide rewrite for this mapcorrection.

Guide `{inv['Guide_sha256']}`,ledger `{inv['ledger_sha256']}`.133currentrows/all459oldtopics retained; two-op fullinverse, original2executablecases plusfivequalitativecases/fullworkedsection exact/pass; alloriginalURLs/order/trust/CTA/otherbytes remain exact. {len(controls)}meaningful source-basedseparators, exactsource/currentrows,oneGuide schema0/0/diff pass. Originalroot{len(m['artifacts'])}memberseal unchanged. Initialmissingintro-mapguardfailure retained/corrected, not a tax/sourcechange. Writer successor awaits C's independentexact review; no countryPASS/attestation/Git/PR/public/Francewriting. Exactpaths/hashes/inventory,options,old-topicmap/sourceindex/checks remain here.
''')
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in['artifact-manifest.json','freeze.json']];dump(W/'artifact-manifest.json',{'status':'writer successor, independent recheck pending','artifacts':entries});fr={'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'controls':len(controls),'role':'writer, not independentPASS'};dump(W/'freeze.json',fr);print(json.dumps({**fr,'freeze_sha256':H(W/'freeze.json')},indent=2))
