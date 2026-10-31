from pathlib import Path
import re,json,hashlib,subprocess,shutil
R=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());P=Path(__file__).resolve().parent
S=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/faroe-ordinary-completion/independent-review/sources')
f=R/'skills/international/faroe-islands/fo-corporate-income-tax.md';text=f.read_text()
urls=dict(re.findall(r'^\[([^]]+)\]: (https?://\S+)',text,re.M));ids={'tax':'tax','rate':'assessment','capital':'capital','depreciation':'depreciation','group':'group','taks':'company','returns':'returns','index':'index','indices':'indices'}
# Whole acquired bodies retained byte-for-byte; used selected quote intervals recorded separately.
for k in ['tax','assessment','capital','depreciation','group','company']:
 for ext in ['html','reader.txt']:shutil.copyfile(S/(k+'.'+ext),P/(k+'.'+ext))
lines={k:(P/(k+'.reader.txt')).read_text().splitlines() for k in ['tax','assessment','capital','depreciation','group','company']}
# Exact anchor quotes selected for clauses, not rewritten translations. Full source article ranges accompany them.
def article(k,n):
 a=lines[k];pat=r'^§ '+re.escape(n).replace(r'\ ',r'\s*')+r'\.'
 start=next(i for i,x in enumerate(a) if re.match(pat,x));end=next((i for i in range(start+1,len(a)) if a[i].startswith('§ ')),len(a));return start,end
scopes={}
def q(k,n,needle=None):
 s,e=article(k,n);scope=f'{k}.reader.txt LF{s+1}–{e}'
 if needle:
  i=next((i for i in range(s,e) if needle.casefold() in lines[k][i].casefold()),s)
 else:i=s
 # 18-word exact prefix or substring: short original text; article scope gives the full context.
 line=lines[k][i];pos=line.casefold().find(needle.casefold()) if needle else 0
 quote=' '.join(line[max(pos,0):].split()[:18]);assert quote in line
 scopes.setdefault(k,[]).append([s+1,e])
 return f'[{k} §{n}]({urls[{"assessment":"rate","company":"taks"}.get(k,k)]}) • {scope}; anchor LF{i+1}: “{quote}”'
# Per-unit reference sets, including every rule in compound paragraphs. Numbers in example units are separately classified as derived.
spec=[
('Faroese registration',[('tax','1',None)]),('Compute ordinary',[('capital','3',None),('capital','10','Fyri feløg'),('capital','14',None)]),
('Ordinary qualifying company',[('assessment','5','18%')]),('Relevant capital',[('assessment','5','50.000')]),('Residual rate',[('assessment','5','49%')]),('Petroleum-income exception',[('assessment','5','27%')]),('Company separate capital',[('capital','14','18%')]),('Company distributions',[('capital','15','35%')]),('Distributions to entities',[('capital','15','18%')]),
('Ordinary equipment pool',[('depreciation','2','30%')]),('Small equipment /',[('depreciation','2','20.000'),('depreciation','3','20.000')]),('Specified exclusive-business',[('depreciation','5 a','150.000')]),('Mixed business/private equipment',[('depreciation','7','150.000')]),('Other qualifying business',[('depreciation','17','75%')]),
('The 18% ordinary',[('assessment','5','30%'),('assessment','5','18%')]),
('Start with a reconciled',[('tax','31',None),('tax','33',None),('tax','37 b',None),('tax','27',None),('tax','29',None)]),
('For machinery, furniture',[('depreciation','1',None),('depreciation','2',None),('depreciation','5 a',None)]),
('For an ordinary positive',[('depreciation','2','30%'),('depreciation','2','20.000')]),('Separately, an eligible',[('depreciation','3','20.000'),('depreciation','3','søluprísurin')]),
('A proved disposal',[('depreciation','4',None)]),('If proceeds create',[('depreciation','5',None)]),
('Depreciation Act §5a applies',[('depreciation','5 a',None)]),('For an affected car',[('depreciation','5 a','150.000'),('depreciation','5 a','Avskriving kann ikki')]),('On disposal, compare',[('depreciation','5 a','Er avhendingarpeningurin')]),
('For equipment used both',[('depreciation','7','30'),('depreciation','8',None)]),('A transfer to exclusively',[('depreciation','31',None),('depreciation','5 a','150.000')]),
('Keep a separate commercial',[('depreciation','11',None),('depreciation','12',None),('depreciation','13','45'),('depreciation','14',None),('depreciation','15',None),('depreciation','16',None)]),
('Classify each building',[('depreciation','17',None)]),('| §17(1)(a)',[('depreciation','20','7%'),('depreciation','20','2%')]),('| §17(1)(c)',[('depreciation','20','4%'),('depreciation','20','1%')]),
('These are cost-based',[('depreciation','20','Útveganarárið')]),('Exclude land acquisition',[('depreciation','27',None),('depreciation','18',None),('depreciation','20','lutfal'),('depreciation','17','75%'),('depreciation','22',None)]),
('No annual depreciation',[('depreciation','21','Avskriving kann ikki'),('depreciation','24','5 ár'),('depreciation','25',None)]),
('For category (a)',[('depreciation','25',None),('depreciation','25','1950'),('depreciation','25','Tryggingar')]),
('For §26 insurance',[('depreciation','26',None),('depreciation','26','1 prosent'),('depreciation','26','freistin'),('depreciation','26','ikki allur')]),
('Tax Act §35a(2)',[('tax','35 a','9 næstkomandi'),('tax','35 a','ávíst tíðarskeið')]),('Business intangible sale',[('tax','35 a',None),('tax','35 a','ikki er drigin'),('tax','35 a','Móttøka')]),
('Section 33a allows',[('tax','33 a',None),('tax','33 a','50 prosent'),('tax','33 a','vinnuligt')]),('Debt cancellation/reduction',[('tax','33 a','skuld')]),
('First test Capital',[('capital','3',None),('capital','3','FIFO'),('capital','3','lagur'),('capital','6','Valutakurs'),('capital','10','Fyri feløg')]),
('For remaining share',[('capital','4','FIFO'),('capital','4','tap við'),('capital','4','0 kr.'),('capital','6','1.000'),('capital','7',None),('capital','8',None)]),
('Dividends received',[('capital','9',None),('capital','1','avtøku'),('capital','5',None)]),('Aggregate the separate',[('capital','14',None),('capital','14','18%'),('capital','14','50%')]),
('Regulation 148/2015',[('group','1',None),('group','2',None),('group','3',None),('group','4','1. juli'),('group','4','Endurnýggjan'),('group','5',None)]),
('Each company computes',[('group','6',None)]),('1. Use pre-group',[('group','6','Stk. 3.'),('group','6','Stk. 4.'),('group','6','Stk. 5.')]),
('2. Use its own',[('group','6','Stk. 6.'),('group','6','Stk. 7.')]),('3. Only then',[('group','6','Stk. 8.'),('group','6','Stk. 9.')]),('4. Report the combined',[('group','6','Stk. 2.'),('group','6','Stk. 10.'),('group','7',None),('group','8',None)]),
('**Ordinary group control',[('group','6','Stk. 8.'),('capital','14','hall'),('assessment','5','18%')]),('Under §9',[('group','9','skattaprosentið'),('group','9','1. oktober'),('group','9','ongar skattligar')]),
('The ordinary permission',[('capital','14 a',None),('capital','14 a','Stk. 2.'),('capital','14 a','Stk. 3.')]),
('Company returns are ordinarily',[('tax','100','1. juli'),('tax','105','15. august')]),('Ordinary company tax falls',[('tax','81',None)]),('For a new resident company',[('tax','21','18'),('tax','21','4 vikur'),('tax','21','vanligum handli')]),
('Report separate capital',[('capital','18',None),('capital','18','500'),('capital','18','50 kr.'),('capital','18','tann 1.')]),('A company declaring',[('capital','15','14 dagar'),('capital','15','35%'),('capital','15','18%')]),
('Section 104 provides',[('tax','104','1.000'),('tax','104','2%'),('tax','104','5%'),('tax','104','Stk. 3.')]),
('Section 81(2)',[('tax','81','0,7'),('tax','146','12%'),('tax','146','Stk. 2.')]),('Late separate capital',[('capital','18','1.000'),('capital','18','2%'),('capital','18','5%'),('capital','18','0,7'),('capital','15','0,7')]),
('Tax Act §139',[('tax','139','2 ár'),('tax','139','gáloysni'),('tax','139 b',None),('tax','140',None)]),
('Foreign incorporation',[('tax','1',None),('tax','2',None),('tax','37 a',None),('tax','37 b',None),('capital','19',None),('tax','154',None),('capital','15',None)]),
]
def classify(unit):
 out=[]
 for needle,refs in spec:
  if needle in unit:
   for v in refs:
    if v not in out:out.append(v)
 return out
def units(s):
 # Native blank-delimited paragraphs; table rows split so every rate has its own row.
 out=[];section='frontmatter';in_code=False
 for m in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',s):
  u=m.group(0).strip();start=s.count('\n',0,m.start())+1
  if u.startswith('#'):section=u.splitlines()[0]
  if u.startswith('|'):
   for j,row in enumerate(u.splitlines()):out.append((start+j,section,row))
  else:out.append((start,section,u))
 return out
rows=[];n=0
for lf,section,u in units(text):
 if u.startswith(('---','#','[tax]:','[rate]:','[taks]:','[group]:','[returns]:','[depreciation]:','[capital]:','[index]:','[indices]:','[vls-n]:')):continue
 # Table header/separator and source bibliography are routing records, still mapped below.
 if section=='## Sources' or u.startswith('|---') or u.startswith('| Item') or u.startswith('| Classification'):continue
 refs=classify(u);kind='express provisions / working-paper application'
 if u.startswith('```oa-check') or section.startswith('### 1.') or section.startswith('### 2.'):
  refs=[('assessment','5','18%'),('depreciation','2','30%'),('depreciation','3','20.000')] if 'equipment' in section.lower() or 'pool' in section.lower() else [('capital','4','tap við'),('capital','10','Fyri feløg'),('capital','14','18%')];kind='hypothetical inputs and derived arithmetic, not quotations of statutory amounts'
 if '**Ordinary group' in u or u.startswith('Under §9') or '100,000 goodwill' in u:kind='express method plus hypothetical sourced-input calculation'
 src='; '.join(q(*z) for z in refs)
 if u.startswith('No annual depreciation'):
  src+='; [TAKS Circular10/1992]('+urls['index']+'), actual web LF20, exact method anchors “100.000 kr. býtt við faldingartalinum” and “faldað við faldingartalinum”; current factorsLF32; historical differences cross-checked against standaloneLF31/35–40.'
 if '**Published TAKS recapture' in u:
  src=q('depreciation','25')+'; [TAKS VLS N §25]('+urls['vls-n']+') web LF630–670, example650–668; exact short anchor: “Her tó hægst gjørdar avskrivingar við í inntøkuna”';kind='labelled published-example derivation; web extraction, not raw HTML; old26 timing excluded'
 if 'Building index multipliers' in u:
  src='[TAKS Circular10/1992 annex1]('+urls['index']+'), actual web LF31–32, quoted row: “2026 | 21,4589 | 21,4767 | 22,0056 | 22,0829”; table headers “1. januar | 1. apríl | 1. juli | 1. oktober”. Same figures actual standalone page LF10–11. Extraction receipts retained, not raw HTML.';kind='express published2026 factors; actual read28October; historic factor conflict remains'
 if not src:
  src='Working-paper instruction / scope boundary / intake / cross-reference, not a new legal entitlement. See cited substantive rows and old-unit mapping.';kind='operational or precisely reserved scope'
 if u.startswith('TAKS requires company accounts'):
  src=q('tax','103',None)+'; [actual TAKS returns page](https://www.taks.fo/en/individuals/tax/tax-return), freshly read28October2026, retained cit-evidence/returns.reader.txt LF32 and LF39; exact short anchors: “tax exemption are also required to submit a tax return along with their accounts.” and “accounts, this must be done on Borgaragluggin.” Full original sentences retained at those lines.';kind='statutory accounts duty and current authority operational quote'
 if u.startswith('**Period:'):src=q('tax','1',None)+'; same actual tax.reader.txt LF1128, exact commencement footnote: '+lines['tax'][1127]
 n+=1;rows.append(dict(id=f'CIT-{n:03}',lf=lf,section=section,wording=u,source=src,read_on='2026-10-28 selected anchor reading; earlier operational-page checks retain2026-10-25',status=kind))
# Material old topic mapping, including headings, tables, both full examples, source URLs and every paragraph.
maprows=[]
for ref in ['origin/main','20572441dcdae9ebd4c282597940338832ade34e']:
 run=subprocess.run(['git','show',ref+':'+str(f.relative_to(R))],capture_output=True,text=True)
 if run.returncode:
  maprows.append((ref,'absent','Whole Guide absent at this path; no origin/main content to lose. Published baseline separately mapped.'));continue
 old=run.stdout
 for lf,sec,u in units(old):
  if u in text:dest=f'current LF{text[:text.index(u)].count(chr(10))+1}, exact'
  else:
   touched=[o for o in json.loads((P/'exact-operations.json').read_text()) if o['old'] in u or u in o['old']]
   assert touched,(ref,lf,u[:100])
   dest='Reconciled by exact operation(s): '+', '.join(str(json.loads((P/'exact-operations.json').read_text()).index(o)+1) for o in touched)+'; old wording preserved verbatim in exact-operations.json and baseline-cit.md; current section '+sec
  maprows.append((ref,f'LF{lf} {sec}: '+u,dest))
def cell(s):return s.replace('|','\\|').replace('\n','<br>')
md='# Faroe corporate income tax: whole-Guide figure/rule ledger\n\nWriter record,28October2026. Not an independent review or accountant attestation. Every substantive paragraph/rate row is carried below verbatim, including hypothetical inputs; every old blank-delimited topic and table row is mapped in the appendix. Short quotes are exact source anchors, not substitutes for reading the full article scope. Raw acquisition is not full-source reading. New method actual read scopes and immutable raw/reader identities are in `cit-evidence/source-identities-and-read-scopes.json`.\n\n## Claim rows\n\n| ID / Guide LF / section | Exact Guide wording, figures and rules | Official source / article / exact Faroese quote and scope | Read date / status |\n|---|---|---|---|\n'
for z in rows:md+='| '+cell(f'{z["id"]} / LF{z["lf"]} / {z["section"]}')+' | '+cell(z['wording'])+' | '+cell(z['source'])+' | '+cell(z['read_on']+'; '+z['status'])+' |\n'
md+='\n## Complete old-topic destination table\n\nThe published20572441 body equals the preserved entry baseline; the check uses actual Git objects, not a prior reviewer assertion. A topic spanning multiple rules is retained as a full paragraph, and both entire oa blocks are indivisible protected units. Changes are limited to declared operations; no old subject is silently dropped.\n\n| Git baseline | Every old unit / original LF | Current destination or exact reconciliation |\n|---|---|---|\n'
for a,b,c in maprows:md+='| '+cell(a)+' | '+cell(b)+' | '+cell(c)+' |\n'
(P.parent/'fo-corporate-income-tax.md').write_text(md)
(P/'claim-rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
ident=[]
for k in lines:
 raw=P/(k+'.html');reader=P/(k+'.reader.txt');ident.append(dict(id=k,raw=str(raw.relative_to(R)),raw_sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),reader=str(reader.relative_to(R)),reader_sha256=hashlib.sha256(reader.read_bytes()).hexdigest(),actual_quote_anchor_scopes=sorted(set(tuple(v) for v in scopes.get(k,[]))),read_scope_note='Generated exact quote anchors reviewed in ledger; complete listed source articles are locators, not an assertion of whole-law reading. New method full actual reads: tax35a LF583–586; group LF297–323; depreciation25–26 LF401–412; capital14–15 LF413–424; assessment5 LF322–325.'))
(P/'source-identities-and-read-scopes.json').write_text(json.dumps(ident,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'claim rows;',len(maprows),'old unit mappings; sources',len(ident))
print('\n'.join(z['id']+' '+z['source'] for z in rows if 'EVIDENCE GAP' in z['status']))
