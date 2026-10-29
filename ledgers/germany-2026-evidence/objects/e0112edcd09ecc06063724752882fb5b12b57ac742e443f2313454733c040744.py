from pathlib import Path
import json,hashlib,re,sys,importlib.util,io,contextlib,subprocess,datetime,copy
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');P=O/'germany-DE-R23-R25-annual-VAT-writer-successor-2026-10-29';W=O/'germany-DE-R24-steuerbar-wording-successor-2026-10-29';W.mkdir(exist_ok=True);R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');s='de-vat-annual-and-special-schemes';p=R/'skills/international/germany'/f'{s}.md';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');b=(W/'before-Guide.md').read_text() if (W/'before-Guide.md').exists() else p.read_text();assert hashlib.sha256(b.encode()).hexdigest()=='6efaea2e7187a02ef34952cf07803f8fb80516c8def1df3fe6b7158c2e7fe196';old='**Small business: what counts.** Total turnover is the sum of taxable supplies counted on receipts,';new='**Small business: what counts.** Total turnover is the sum of supplies within the scope of VAT (steuerbare Umsätze), counted on receipts,';assert b.count(old)==1
(W/'options-and-selection.md').write_text('''# R24 finite terminology precision

Option A, selected: replace only the small-business opening “sum of taxable supplies counted on receipts” with “sum of supplies within the scope of VAT (steuerbare Umsätze), counted on receipts”. This expresses the actual § 19(2) scope and avoids suggesting that exempt main financial/insurance receipts cannot enter the threshold calculation. Keep all category exclusions, controls and eligibility/timing methods unchanged.

Option B: retain the English opening but explicitly state that “taxable” means steuerbar, including exempt supplies unless the stated exclusions apply. A is clearer and shorter.

No new source reading or acquisition is claimed: actual own complete UStG § 19 selected reading on 29 October is sealed in the preceding R23–25 own-actual-read-quotes.json, R23.small-business. Exact quote: “Gesamtumsatz ist die nach vereinnahmten Entgelten berechnete Summe der vom Unternehmer ausgeführten steuerbaren Umsätze im Sinne des § 1 Absatz 1 Nummer 1 abzüglich folgender Umsätze”. Official https://www.gesetze-im-internet.de/ustg_1980/__19.html; native LF8, full category context LF7–18. Sources/raw readers and all quotation text remain byte-exact in that immutable predecessor. Content version advances0.3→0.4; date remains29October.
''')
ops=[{'old':old,'new':new,'native_LF':86},{'old':'version: 0.3','new':'version: 0.4','native_LF':4}];a=b
for x in ops:assert a.count(x['old'])==1;a=a.replace(x['old'],x['new'],1)
z=a
for x in reversed(ops):assert z.count(x['new'])==1;z=z.replace(x['new'],x['old'],1)
assert z==b
assert p.read_text() in [b,a];(W/'before-Guide.md').write_text(b);p.write_text(a);(W/'after-Guide.md').write_bytes(p.read_bytes());dump(W/'exact-operations.json',ops)
# Only one current row wording changes; all source IDs, sections, destinations and quotation references remain exact.
priorrows=P/'support'/s/'rows.json';rows=json.loads(priorrows.read_text());count=0
for row in rows:
 if old in row['wording']:row['wording']=row['wording'].replace(old,new);row['disposition']+='; R24 finite steuerbar terminology precision';count+=1
assert count==1;dump(W/'rows.json',rows)
ledger=(P/'ledgers'/f'{s}.md').read_text();beforeledger=ledger;oldhash=H(W/'before-Guide.md');newhash=H(p);oldbytes=(W/'before-Guide.md').stat().st_size;newbytes=p.stat().st_size;head,tail=ledger.split('## Complete old-topic destinations',1);assert head.count(old)==1;ledger=head.replace(old,new)+'## Complete old-topic destinations'+tail;ledger=ledger.replace('`'+oldhash+'`','`'+newhash+'`',1).replace(f'{oldbytes} bytes',f'{newbytes} bytes',1)
# The row disposition records the narrow successor, without changing quoted primary text or historic old-wording cells.
old_disposition=next(r for r in json.loads(priorrows.read_text())if old in r['wording'])['disposition'];ledger=ledger.replace(new+beforeledger.split(old,1)[1].split('|',1)[0],new+beforeledger.split(old,1)[1].split('|',1)[0],1)
ledger=ledger.replace('# de-vat-annual-and-special-schemes: DE-R23–25 successor figure and rule ledger','# de-vat-annual-and-special-schemes: DE-R23–25 plus R24 terminology successor figure and rule ledger',1)
ledger=ledger.replace('](../source-quotes.md',']('+str(P/'source-quotes.md'))
ledger+='\nR24 terminology successor only: source quotations and complete old-topic table remain exact to the pinned R23–25 predecessor. Prior Guide6efaea2e and ledger785e75da remain historical. Current Guide version0.4. Independent closure pending.\n';(W/f'{s}.md').write_text(ledger)
# Check actual rows, exact unchanged source/body references and original original cases/protections.
for row in rows:
 lo,hi=row['native_LF'];assert row['wording']=='\n'.join(a.split('\n')[lo-1:hi])
assert re.findall(r'```oa-check\n.*?```',a,re.S)==re.findall(r'```oa-check\n.*?```',b,re.S)
assert a.split('## Worked examples')[1].split('## Ask the client first')[0]==b.split('## Worked examples')[1].split('## Ask the client first')[0]
m=json.loads((P/'artifact-manifest.json').read_text());assert all(H(P/x['path'])==x['sha256']for x in m['artifacts'])
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def module(n,path):spec=importlib.util.spec_from_file_location(n,str(path));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
ce=module('R24ex',R/'scripts/check-examples.py');vg=module('R24schema',R/'scripts/validate-guides.py');n,f=ce.check_file(str(p));assert n==2 and not f;e=[];w=[]
with contextlib.redirect_stdout(io.StringIO()):vg.check_guides(vg.load_build_index(),e,w,only_files={str(p.relative_to(R))})
assert not e and not w;dc=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert dc.returncode==0
inv={'Guide_path':str(p),'Guide_sha256':H(p),'Guide_bytes':p.stat().st_size,'ledger_path':str(W/f'{s}.md'),'ledger_sha256':H(W/f'{s}.md'),'rows_path':str(W/'rows.json'),'rows_sha256':H(W/'rows.json'),'old_topics_path':str(P/'support'/s/'old-topic-destinations.json'),'old_topics_sha256':H(P/'support'/s/'old-topic-destinations.json'),'source_index_path':str(P/'source-quote-index.json'),'source_index_sha256':H(P/'source-quote-index.json'),'prior_manifest_sha256':H(P/'artifact-manifest.json')};dump(W/'successor-inventory.json',inv)
checks={'one_changed_current_row':count,'current_rows':len(rows),'same_native_coordinates':True,'full_inverse_exact':True,'prior_manifest_members_unchanged':len(m['artifacts']),'original_oa_blocks_exact_and_pass':n,'whole_worked_section_exact':True,'source_index_and_all_quote_bodies_unchanged':True,'schema_errors':e,'schema_warnings':w,'diff_returncode':dc.returncode};dump(W/'writer-checks.json',checks)
(W/'writer-report.md').write_text(f'''# R24 terminology successor

The selected narrow A replaces only the ambiguous English opening at native LF86 with “supplies within the scope of VAT (steuerbare Umsätze), counted on receipts”. Version0.3→0.4 is the only other Guide operation. Actual eligibility, exclusions, figures, calculations, examples, URLs and protected fields remain exact. No fresh source acquisition or expanded reading claim; the already-read own19(2) supports the precise term.

Guide `{inv['Guide_sha256']}`; ledger `{inv['ledger_sha256']}`. One current row's wording changes; all177native row bindings, all347old-topic identities and exact source quotation bodies remain bound to the immutable preceding seal. The source links are made absolute to that same unmodified quotation file for portability from this successor folder. Both original examples/full worked section pass/exact; full inverse and scoped schema0/0/diff pass. All20prior seal artifacts rehash unchanged. This is a bounded writer successor awaiting C's independent closure, not a country PASS. Exact paths/hashes are in successor-inventory.json.
''')
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in['artifact-manifest.json','freeze.json']];dump(W/'artifact-manifest.json',{'status':'writer terminology successor; independent closure pending','artifacts':entries});dump(W/'freeze.json',{'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'status':'writer, not independent PASS'});print(json.dumps({'report':H(W/'writer-report.md'),'manifest':H(W/'artifact-manifest.json'),'freeze':H(W/'freeze.json'),'pair':inv},indent=2))
