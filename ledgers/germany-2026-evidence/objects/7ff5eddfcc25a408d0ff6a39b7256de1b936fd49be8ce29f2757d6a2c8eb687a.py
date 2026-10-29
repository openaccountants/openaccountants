from pathlib import Path
import json,hashlib,re,copy,sys,importlib.util,io,contextlib,subprocess,datetime
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');P=O/'germany-DE-R57-R60-treaty-writer-successor-2026-10-29';W=O/'germany-DE-R58-R59-treaty-gate-precision-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');s='de-treaty-withholding-rates';p=next((R/'skills').rglob(s+'.md'));H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');W.mkdir();[(W/x).mkdir()for x in ['before','after','ledgers','support']];original=p.read_text();assert H(p)=='e0af931443833336734547a462ee47978d568c247571d2691fad966c5b0e5ecf';(W/'before'/p.name).write_text(original);b=original;ops=[]
def op(old,new):
 global b
 assert b.count(old)==1;ops.append({'before':old,'after':new});b=b.replace(old,new,1)
(W/'options-and-selection.md').write_text('''# R58/R59 exact review refinements: two options

A selected: append all actual Anlage2 company gates to the operative43bdividend row, rather than relying on the fictional50groyalty example: specified companyform, EUtaxresidence/noDTAthird-countryresidence, listed/replacementtax withoutoption and notexempt. Replace only "limited-liability foreign capital company" with "foreign capital company with limited German tax liability" in50j. These are actual law conditions; no new research or legal-form requirement is invented.

B: add a general operative paragraph explicitly incorporating the complete Anlage2 definition and cross-reference it in43b, while using the same exact50jterm. A keeps the gates visible at the actual decision row.

Own actual selected reread29October2026: prior R58.company-forms native7–10 andR58.residence-tax67–71, plus50jfulloperative7–20 at R57-60.PORTFOLIO; exact German clauses/URLs/hashes retained in prior source index and own-read-receipt.json. The initial R58quickrowoperation was a no-op and did not implement the intended general gate; its frozen report remains historical, needs-fix for this precise point. Initial50jEnglishterm was imprecise. No original numeric case or algebra changes.
''')
op('version: 0.3','version: 0.4');op('EU parent company (form in Anlage 2 EStG) holding at least 10% directly; 12 months without break','EU parent company in a form listed in Anlage 2 EStG, treated as resident in an EU member state for tax purposes and not as resident outside the EU under a treaty with a third state, subject without an option to a listed tax or its replacement and not exempt from it; holding at least 10% directly for 12 months without break');op('limited-liability foreign capital company','foreign capital company with limited German tax liability');p.write_text(b);(W/'after'/p.name).write_text(b);dump(W/'exact-operations.json',ops)
qs=json.loads((P/'source-quote-index.json').read_text());reads={}
for k in ['R58.company-forms','R58.residence-tax','R57-60.PORTFOLIO']:
 q=qs[k];assert H(Path(q['raw_path']))==q['raw_sha256']and H(Path(q['reader_path']))==q['reader_sha256'];a,z=q['native_LF'];assert q['exact_quote']in'\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:z]);reads[k]={**q,'actual_reread':'2026-10-29, complete selected operative quote; no whole-body claim'}
dump(W/'own-read-receipt.json',reads);dump(W/'source-index-reference.json',{'path':str(P/'source-quote-index.json'),'sha256':H(P/'source-quote-index.json'),'all_body_and_quote_bytes_unchanged':True})
rows=json.loads((P/'support'/s/'rows.json').read_text());ls=b.split('\n');changed=[]
for q in rows:
 a,z=q['native_LF'];t='\n'.join(ls[a-1:z]);q['immediate_predecessor_wording']=q['wording'];q['immediate_predecessor_row_id']=q['id']
 if t!=q['wording']:changed.append(q['id']);q['disposition']='R58/R59 exact independent review qualification successor; original numeric case unchanged'
 q['wording']=t
 if '| § 43b EU Parent'in t:q['source_quote_ids']=list(dict.fromkeys(q['source_quote_ids']+['R57-60.PARENT','R58.company-forms','R58.residence-tax']))
(W/'support'/s).mkdir();dump(W/'support'/s/'rows.json',rows);old=json.loads((P/'support'/s/'old-topic-destinations.json').read_text())
for q in old:
 q['immediate_predecessor_destination']=q['destination']
 if '43b'in q['wording'].lower():q['bounded_successor_scope']+=' R58 final: the general operative dividend row now expressly supplies all Anlage2 residence/tax gates.'
 if '50j'in q['wording'].lower():q['bounded_successor_scope']+=' R59 final: limited German tax liability is the actual population, not limited-liability legal form.'
dump(W/'support'/s/'old-topic-destinations.json',old)
def esc(t):return str(t).replace('|','\\|').replace('\n','<br>')
t=f'# {s}: R58/R59 precise successor ledger\n\nGuide `{H(p)}`, {p.stat().st_size} bytes; predecessor Guide `{H(W/"before"/p.name)}` / ledger `{H(P/"ledgers"/(s+".md"))}`. Original seal unchanged. Source quotes and all actual original read dates remain byte-exact at [{P/"source-quotes.md"}]({P/"source-quotes.md"}); hash-bound source-index-reference.json. Own actual three selected rereads29October2026 in own-read-receipt.json. Writer correction, exact independent review pending.\n\n| ID | Section/nativeLF | Exact current wording | Source IDs/disposition |\n|---|---|---|---|\n'
for q in rows:t+=f'| {q["id"]} | {esc(q["section"])} LF{q["native_LF"]} | {esc(q["wording"])} | {esc(q["source_quote_ids"])}. {q["disposition"]} |\n'
t+='\n## Complete old-topic destination table\n\n| Historical reference | Exact old wording | Current destination/qualification |\n|---|---|---|\n'
for q in old:t+=f'| {q["ref"]} LF{q["old_lf"]} | {esc(q["wording"])} | {esc(q["destination"])} {esc(q["bounded_successor_scope"])} |\n'
(W/'ledgers'/p.name).write_text(t)
x=original
for q in ops:assert x.count(q['before'])==1;x=x.replace(q['before'],q['after'],1)
assert x==b
for q in reversed(ops):assert x.count(q['after'])==1;x=x.replace(q['after'],q['before'],1)
assert x==original
blocks=lambda t:re.findall(r'```oa-check.*?```',t,re.S);assert blocks(original)==blocks(b)and len(blocks(b))==2
assert re.findall(r'https?://[^\s<>|)]+',original)==re.findall(r'https?://[^\s<>|)]+',b)
sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
def mod(n,p):sp=importlib.util.spec_from_file_location(n,str(p));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
ce=mod('R58_examples',R/'scripts/check-examples.py');vg=mod('R58_schema',R/'scripts/validate-guides.py');n,f=ce.check_file(str(p));assert n==2 and not f;es=[];ws=[]
with contextlib.redirect_stdout(io.StringIO())as out:vg.check_guides(vg.load_build_index(),es,ws,only_files={str(p.relative_to(R))})
assert not es and not ws;d=subprocess.run(['git','diff','--check','--',str(p.relative_to(R))],cwd=R,capture_output=True,text=True);assert d.returncode==0
# Preserve entire first treaty seal. Source quotes are not silently edited.
m=json.loads((P/'artifact-manifest.json').read_text())['artifacts']
for e in m:assert H(P/e['path'])==e['sha256']
inv={'slug':s,'Guide_path':str(p),'Guide_sha256':H(p),'bytes':p.stat().st_size,'ledger_path':str(W/'ledgers'/p.name),'ledger_sha256':H(W/'ledgers'/p.name),'rows':len(rows),'old_topics':len(old),'prior_manifest':str(P/'artifact-manifest.json'),'prior_manifest_sha256':H(P/'artifact-manifest.json')};dump(W/'successor-inventory.json',inv)
checks={'three_exact_ops_inverse':True,'changed_rows':changed,'own_selected_read_records':3,'prior21_members_unchanged':True,'original2oa_exact_and_pass':True,'all_old_URLs_exact':True,'no_other_tax_rule_amount_case_change':True,'all166_current_and329_old_identities_preserved':True,'schema_errors':es,'schema_warnings':ws,'diff_returncode':d.returncode,'controls':[{'EU_resident':True,'third_country_treaty_resident':False,'no_option_taxed':True,'not_exempt':True,'all_additional_definition_gates':True},{'EU_resident':True,'third_country_treaty_resident':True,'no_option_taxed':True,'not_exempt':True,'all_additional_definition_gates':False},{'EU_resident':True,'third_country_treaty_resident':False,'no_option_taxed':False,'not_exempt':True,'all_additional_definition_gates':False},{'EU_resident':True,'third_country_treaty_resident':False,'no_option_taxed':True,'not_exempt':False,'all_additional_definition_gates':False}]}
for q in checks['controls']:assert(q['EU_resident']and not q['third_country_treaty_resident']and q['no_option_taxed']and q['not_exempt'])==q['all_additional_definition_gates']
dump(W/'writer-checks.json',checks);(W/'writer-report.md').write_text(f'''# Treaty R58/R59 precise writer successor

The initial treaty seal's general43brow lacked the actual Anlage2tax-residence/tax-status gates despite the intended source interpretation. This successor expressly supplies them there. It also translates beschränkt steuerpflichtige Kapitalgesellschaft accurately as foreign capital company with limited German tax liability; it does not impose an invented limited-liability legal-form test. Earlier incorrect implementation/wording is preserved in the immutable first seal.

Three canonical operations includingversion0.3→0.4; every other byte is recovered by exact inverse. Three actual selected own rereads29October2026, original source bodies/quotes unchanged.166current/329oldidentities retained; full current ledger rebound. Four statutory-gate separators,2originaloa exact/pass, URLorder/protections and scoped schema0/0/diff pass. All21priorseal members rehashed unchanged. Guide `{inv['Guide_sha256']}`, ledger `{inv['ledger_sha256']}`. This is a bounded writer correction pending C's exact recheck, not a countryPASS.
''')
# Own reproducible operations/check helper saved after authoring, original entry invocation retained outside seal.
(W/'historical-apply-and-check.py').write_text(Path('/tmp/treaty-refine.py').read_text())
entries=[{'path':str(p.relative_to(W)),'sha256':H(p),'bytes':p.stat().st_size}for p in sorted(W.rglob('*'))if p.is_file()and p.name not in ['artifact-manifest.json','freeze.json']];dump(W/'artifact-manifest.json',{'artifacts':entries});f={'report_sha256':H(W/'writer-report.md'),'manifest_sha256':H(W/'artifact-manifest.json'),'members':len(entries),'pair':inv,'independent_review':'pending'};dump(W/'freeze.json',f);print(json.dumps(f,indent=2))
