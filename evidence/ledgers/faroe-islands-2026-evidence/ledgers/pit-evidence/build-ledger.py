from pathlib import Path
import re,json,hashlib,subprocess,shutil,difflib
P=Path(__file__).resolve().parent;R=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());F=R/'skills/international/faroe-islands/fo-individual-income-tax.md';body=F.read_text();assert hashlib.sha256(F.read_bytes()).hexdigest()=='ebf5863b6f219368291d91aecbe0e260a304900634eaa64451094b44cb7a820c'
(P/'frozen-guide.md').write_bytes(F.read_bytes());S=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/faroe-ordinary-completion/sources');I=S.parent/'independent-review/sources'
ids={'tax':'tax-current','rate':'assessment-current','church':'church-current','support':'support','consumption':'consumption','national':'pit-national','municipal':'pit-municipal','child':'pit-child','rent':'pit-rent','returns':'pit-returns','spouse':'pit-spouse','residence':'vls-c','capital':'capital','pension':'pension','depreciation':'depreciation'}
urls=dict(re.findall(r'^\[([^]]+)\]: (https?://\S+)',body,re.M));lines={};read_anchors={};fallbacks=[]
for k,n in ids.items():
 src=I if k in ['capital','pension','depreciation'] else S
 for ext in ['html','reader.txt']:shutil.copyfile(src/(n+'.'+ext),P/(k+'.'+ext))
 lines[k]=(P/(k+'.reader.txt')).read_text().splitlines()
for n in ['audit-2024.pdf','audit-2024.reader.txt','audit-2024-page-045.png','calculator-180days-150000.ax.txt','calculator-365days-150000.ax.txt','calculator-180days-150000.png','root-web-receipts.json']:shutil.copyfile(S/n,P/n)
shutil.copyfile(S.parent/'root-positive-edit-operations.json',P/'root-positive-edit-operations.json')
def act(k,n,needle=None):
 a=lines[k];start=next(i for i,x in enumerate(a) if re.match('^§ '+re.escape(n)+r'\.',x));end=next((i for i in range(start+1,len(a)) if a[i].startswith('§ ')),len(a));i=next((i for i in range(start,end) if needle and needle in a[i]),start)
 line=a[i];pos=line.find(needle) if needle else 0
 if needle and pos<0:fallbacks.append((k,n,needle))
 quote=' '.join(line[max(pos,0):].split()[:40 if k=='rate' and n=='1' and needle and needle[0].isdigit() else 18]);assert quote in line;read_anchors.setdefault(k,set()).add(i+1)
 return f'[{k} §{n}]({urls[k]}) • {k}.reader.txt LF{start+1}–{end}, quote LF{i+1}: “{quote}”'
def acts(k,*args):return '; '.join(act(k,*x) if isinstance(x,tuple) else act(k,x) for x in args)
def page(k,needle,words=22):
 a=lines[k];i=next(i for i,x in enumerate(a) if needle in x);line=a[i];q=' '.join(line[line.index(needle):].split()[:words]);assert q in line;read_anchors.setdefault(k,set()).add(i+1)
 return f'[{k}]({urls[k]}) • {k}.reader.txt LF{i+1}: “{q}”'
def units(s):
 out=[];section='Metadata'
 for m in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',s):
  u=m.group(0).strip();start=s.count('\n',0,m.start())+1
  if u.startswith('#'):section=u.splitlines()[0]
  if u.startswith('|'):
   for j,t in enumerate(u.splitlines()):out.append((start+j,section,t))
  else:out.append((start,section,u))
 return out
def cell(s):return s.replace('|','\\|').replace('\n','<br>')
calc='[Official2026 calculator]('+urls['calculator']+'), ROOT-observed synthetic public browser output, not replayed by this ledger writer. Preserved AX receipt calculator-180days-150000.ax.txt LF98–183: “Skattskyldugt dagatal”, “180”, “304.100,00”, “85.644,00”, “42.235,40”, “42.235,00”, “4.500,00”; input150.000; “Tal av børnum: 0”; “Úrslitið er bert ein fyribils útrokning.” The separately displayed6.500 child-credit parameter is explicitly EXCLUDED in favour of current law10.700/7.500. Source/fact, not an acquired taxpayer award.'
audit='[Official2024 audit report §4.10 printed44–46]('+urls['church-audit']+'), root selected readerLF2191–2330; printed45 visual retained from root. This writer read2273–2275 and2324–2338 plus surrounding context. Exact original anchors LF2273–2274: “Kirkjuskatturin verður roknaður og kravdur inn umvegis skattaskipanina á sama hátt” / “sum kommuskatturin, t.v.s. at botnfrádrátturin í kommunuskattinum verður drigin frá”. This2024 administrative description is bridged to current Act11–14/Tax46–47; historical rates are not adopted.'
spec=[
('Faroese domestic full',[lambda:acts('tax',('1','180 dagar'),'2','25')]),('Employees, sole traders',[lambda:acts('tax','4','5')]),
('| Below 65,000',[lambda:acts('rate',('1','1) Er inntøkan'))]),('| 65,000 to',[lambda:acts('rate',('1','2) Er inntøkan'))]),('| 180,000 to',[lambda:acts('rate',('1','3) Er inntøkan'))]),('| 330,000 to',[lambda:acts('rate',('1','4) Er inntøkan'))+'; original Act has literal “450.0000”; next band/TAKS current table confirm450,000.']),('| 450,000 to',[lambda:acts('rate',('1','5) Er inntøkan'))]),('| At least 600,000',[lambda:acts('rate',('1','6) Er inntøkan'))]),
("[TAKS's dated2026",[lambda:page('national','Talva yvir landsskatt 2026')]),("[TAKS's dated 2026",[lambda:page('national','Talva yvir landsskatt 2026')]),
('| Municipal exempt',[lambda:acts('tax',('46','0-30.000'))]),('| Municipal rate /',[lambda:page('municipal','Tórshavnar19,00')]),('| Church tax',[lambda:page('municipal','8) Argir')]),('| National child credit',[lambda:acts('rate',('2','10.700'),('2','7.500'))]),('| Specified pensioner',[lambda:acts('rate',('3','10.500'),('3','16.200'),('3','6.000'))]),('| National/municipal/church',[lambda:acts('tax',('54','50%'))]),('| Separate individual',[lambda:acts('capital',('14','35%'))]),('| Eligible housing-interest',[lambda:acts('support',('3','100.000'),('5','35%'))]),('| Qualifying residential',[lambda:acts('rate',('8 a','100.000'),('8 a','25%'),('8 a','trý ár'))]),('| Specified limited-tax',[lambda:acts('rate',('8','42%'),('8','35%'))]),
('Build separate schedules',[lambda:acts('tax','25','28','57','60','61','62')]),('For business profit',[lambda:acts('tax','26','31',('33','rentur'),'32','33 a')]),('Equipment depreciation',[lambda:acts('depreciation','1',('2','30%'),('2','20.000'),'3','4','5','7','8')]),
("Before finalising an individual's",[lambda:acts('tax',('31','Stk. 2.'),('31','Stk. 4.'),('31','Stk. 5.'),('31','Stk. 6.'))]),('Regulation 98/1987',[lambda:acts('consumption','1','2','3')]),('Eligible paid pension',[lambda:acts('pension',('12','40%'),('12','Stk. 3.'),('12','Stk. 4.'))]),
('For a full-year cohabiting',[lambda:acts('tax','4')+'; '+page('spouse','Tjenar annað 20.000')+'; '+page('spouse','Tjenar annað hjúnið einki')]),
('For national child credit',[lambda:acts('rate','2')]),('Determine the tax municipality',[lambda:acts('tax','41','42','43','44','46','47')+'; '+acts('rate','2','3')+'; '+page('child','skulu teir senda TAKS eitt fyribilsskattaskrásetingarskjal.')]),
('For municipal calculation',[lambda:acts('tax',('47','býtast við 100'),('54','50%'),'24')]),('For an ordinary full-year church',[lambda:acts('church','11','12','13','14')+'; '+acts('tax','46','47')+'; '+audit+'; '+page('municipal','8) Argir')]),
('Liability continues while',[lambda:acts('tax','1','6','7','8')+'; '+page('residence','Full skattskylda verður tí ikki stovnað')]),
('For a bounded 2026',[lambda:acts('tax',('24','Stk. 2.'),'46','47')+'; '+calc]),('**Observed control',[lambda:acts('rate','1','2')+'; '+calc]),
('Separate non-business',[lambda:acts('capital','1','3','4',('6','1.000'),'7','8','9','10')]),('Aggregate eligible',[lambda:acts('capital','1','11','12','13',('14','35%'),'15','16','18')]),
('Residential rent',[lambda:acts('rate','8 a')+'; '+page('rent','tríggjar mánaðir')]),('For personal housing',[lambda:acts('support','1','2','2 a',('3','100.000'),'4',('5','35%'),'7','8')]),
('Screen foreign-work',[lambda:acts('tax','25 b',('33','c) 2026'),('33','48.000'),('33','96.000'))+'; '+acts('rate',('1','35%'))]),('The statutory fishing',[lambda:acts('tax',('33','14%'),('33','300.000'),('33','50.000'))]),
('Ordinary individual returns',[lambda:acts('tax',('100','1. mai'),'101','103',('105','15. august'))+'; '+page('returns','1 May')]),('Update preliminary',[lambda:acts('tax','67',('74','1.000'),('74','1. juni'),('76','31. januar'))]),('Reconcile final tax',[lambda:acts('tax','77',('78','4%'),('78','100 kr.'),('78','1.000'),('78','1. mai'),'79','80')]),('Separate capital reporting',[lambda:acts('capital','18')]),
('A missing/late complete',[lambda:acts('tax','104',('135','0,7%'))+'; '+acts('capital','18')]),('False/misleading information',[lambda:acts('tax','78','139','139 a','139 b','140','141')]),
('Classify domestic versus',[lambda:acts('tax','1','2')+'; '+acts('rate','1','8')]),('Capital Income Act §19 permits',[lambda:acts('capital','19','2 a','2 b','2 c','2 d','2 e','2 f')+'; '+acts('tax','154')]),
]
rows=[]
for lf,sec,u in units(body):
 if u.startswith(('---','#','<!--','> Contributed')) or re.match(r'^\[[^]]+\]:',u) or sec=='## Sources' or sec=='## Talk to an accountant' or u.startswith(('|---','| Income interval','| Other item')):continue
 source=[]
 for needle,fns in spec:
  if needle in u:source.extend(fn() for fn in fns)
 kind='express current rule / bounded working-paper application'
 if sec.startswith(('### 1.','### 2.')) or u.startswith('```oa-check'):
  source=[acts('rate','1','2')+'; '+acts('tax','31','46','47')+'; '+acts('depreciation',('2','30%'))+'; '+acts('pension','12')+'; '+acts('capital',('14','35%'))+'; '+page('municipal','Tórshavnar19,00')];kind='hypothetical independently eligible inputs plus derived arithmetic; not quotations of fixed statutory allowances'
 if not source:source=['Scope/operational/intake instruction or inherited trust/period framing; no separate positive entitlement. Legal/computational rows are supplied separately.'];kind='operational / precise limitation / metadata statement'
 rows.append(dict(id=f'PIT-{len(rows)+1:03}',lf=lf,section=sec,wording=u,source='; '.join(source),read_on='2026-10-28 selected original quote anchors; prior full source checks retain original Guide dates',status=kind))
md='# Faroe personal income tax: whole-Guide figure/rule ledger\n\nFrozen Guide v0.5 SHA256 ebf5863b6f219368291d91aecbe0e260a304900634eaa64451094b44cb7a820c. Ledger writer did not edit the Guide. Every substantive paragraph/rate row appears verbatim below, including derived example inputs and explicit boundaries. Exact source anchors are selected snippets, not a claim to have reread every acquired law in full. Short original-language quotes and full article locators allow bounded independent review. Root observed the synthetic calculator; this writer read/recomputed the retained output and does not claim an independent UI replay. Calculator child-credit display6,500 is excluded, not source authority over current law10,700/7,500.\n\n## Whole-Guide rows\n\n| ID / Guide LF / section | Exact Guide wording and figures | Official source / article / exact original-language quote / reader scope | Read date / status |\n|---|---|---|---|\n'
for z in rows:md+='| '+cell(f'{z["id"]}, LF{z["lf"]}, {z["section"]}')+' | '+cell(z['wording'])+' | '+cell(z['source'])+' | '+cell(z['read_on']+'; '+z['status'])+' |\n'
oldmaps=[];ops=json.loads((P/'root-positive-edit-operations.json').read_text());ops=[x for x in ops if x['file']==F.name]
md+='\n## Complete old-topic destination table\n\nActual Git objects are compared. Each blank-delimited original topic, each table row, both entire oa blocks, metadata, source definitions, byline and CTA is mapped. Exact matches are distinguished from root-authored reconciliations; original text is never silently omitted from this ledger.\n\n| Baseline | Every original unit / LF / section | Frozen v0.5 destination or explicit reconciliation |\n|---|---|---|\n'
for ref in ['origin/main','20572441dcdae9ebd4c282597940338832ade34e']:
 run=subprocess.run(['git','show',ref+':'+str(F.relative_to(R))],capture_output=True,text=True)
 if run.returncode:md+='| '+ref+' | File absent at this path | Published20572441 body mapped separately; no main file to lose |\n';continue
 old=run.stdout;(P/(ref.replace('/','-')+'-baseline.md')).write_text(old)
 current_units=units(body)
 for lf,sec,u in units(old):
  if u in body:dest=f'LF{body[:body.index(u)].count(chr(10))+1}, exact'
  else:
   match=[x for x in ops if x['old'] in u or u in x['old']]
   cand=[x for x in current_units if x[1]==sec]
   nearest=max(cand,key=lambda x:difflib.SequenceMatcher(None,u,x[2]).ratio()) if cand else (1,'Metadata',body.split('\n\n',1)[0])
   dest=f'Reconciled current LF{nearest[0]} in {sec}; original unit retained here and in saved Git baseline. '
   if match:dest+='Root operation(s) '+','.join(str(ops.index(x)+1) for x in match)+'.'
   else:dest+='Metadata/date/version or church-method/scope reconciliation preceding root-positive-edit ledger; compare exact full original/frozen bodies, not a claimed byte-exact unit.'
  oldmaps.append(dict(ref=ref,old_lf=lf,section=sec,old=u,destination=dest));md+='| '+ref+' | '+cell(f'LF{lf}, {sec}: '+u)+' | '+cell(dest)+' |\n'
(P.parent/'fo-individual-income-tax.md').write_text(md);(P/'claim-rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(P/'old-topic-map.json').write_text(json.dumps(oldmaps,ensure_ascii=False,indent=2)+'\n')
identity=[]
for k in lines:
 identity.append(dict(id=k,url=urls[k],raw_file=k+'.html',raw_sha256=hashlib.sha256((P/(k+'.html')).read_bytes()).hexdigest(),reader_file=k+'.reader.txt',reader_sha256=hashlib.sha256((P/(k+'.reader.txt')).read_bytes()).hexdigest(),actual_exact_quote_anchor_LF=sorted(read_anchors.get(k,set())),reading_note='Selected quote anchors checked for ledger; full article ranges in ledger are context locators, not an assertion of full acquired-law read. Root full method reads remain attributed to root.'))
for n in ['audit-2024.pdf','audit-2024.reader.txt','audit-2024-page-045.png','calculator-180days-150000.ax.txt','calculator-365days-150000.ax.txt','calculator-180days-150000.png','root-web-receipts.json']:identity.append(dict(file=n,sha256=hashlib.sha256((P/n).read_bytes()).hexdigest(),reading_note='Audit selected2191–2330, church printed45; calculator retained AX fields read, no own UI replay. Whole artifact acquisition is not full reading.'))
(P/'source-identities-and-read-scopes.json').write_text(json.dumps(identity,ensure_ascii=False,indent=2)+'\n');print(len(rows),'claim rows;',len(oldmaps),'complete old unit maps; Guide remains frozen',hashlib.sha256(F.read_bytes()).hexdigest())

print('Quote-anchor fallbacks:', sorted(set(fallbacks)))
