from pathlib import Path
import subprocess,re,json,hashlib,shutil,runpy
P=Path(__file__).resolve().parent;R=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());ns=runpy.run_path(str(P/'build-ledger.py'));units=ns['units'];cell=ns['cell']
S=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/faroe-ordinary-completion/independent-review/sources')
for k in ['admin','regulation']:
 for ext in ['html','reader.txt']:shutil.copyfile(S/(k+'.'+ext),P/(k+'.'+ext))
source_lines={k:(P/(k+'.reader.txt')).read_text().splitlines() for k in ['tax','admin','regulation']}
source_urls={'tax':'https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt','admin':'https://logir.fo/Logtingslog/61-fra-02-05-2022-um-fyrisiting-av-skatti-tolli-og-avgjaldi','regulation':'https://logir.fo/Kunngerd/151-fra-19-12-2019-um-land-fyri-land-frabodan'}
read_scopes={}
def q(k,n,needle=None):
 a=source_lines[k];start=next(i for i,x in enumerate(a) if re.match('^§ '+re.escape(n)+r'\.',x));end=next((i for i in range(start+1,len(a)) if a[i].startswith('§ ')),len(a));i=next((i for i in range(start,end) if needle and needle in a[i]),start)
 line=a[i];pos=line.find(needle) if needle else 0;quote=' '.join(line[max(pos,0):].split()[:18]);assert quote in line
 read_scopes.setdefault(k,[]).append([i+1,i+1]);return f'[{k} §{n}]({source_urls[k]}), reader LF{start+1}–{end}; exact anchor LF{i+1}: “{quote}”'
def refs(k,*articles):return '; '.join(q(k,*a) if isinstance(a,tuple) else q(k,a) for a in articles)
TP=[
('Under Tax Act',lambda:refs('tax','37 a','118 a')),
('General capital/vote',lambda:refs('tax',('37 a','meira enn 50%'))),
('Documentation-exemption balance',lambda:refs('tax',('118 a','36 mió.'))),('Documentation-exemption net',lambda:refs('tax',('118 a','72 mió.'))),('Documentation-exemption average',lambda:refs('tax',('118 a','50 fulltíðar'))),
('Thin-capitalisation debt',lambda:refs('tax',('37 b','4:1'))),('Related-party contributed',lambda:refs('tax',('37 b','2 ár'))),
('For the §118a(6)',lambda:refs('tax',('118 a','tveimum fylgjandi'),('118 a','Tó kann TAKS'))+'; Act191/2018 §1(11), actual webLF405–412, “í tveimum fylgjandi roknskaparárum”; §2LF488–489, “kemur í gildi 1. januar 2019”. '+ 'https://logir.fo/Logtingslog/191-fra-21-12-2018-um-broyting-i-logtingslog-um-landsskatt-og-kommunuskatt-Skattalogin'),
('Use independent-party',lambda:refs('tax','37 a')),
('TAKS\'s older guidance',lambda:'[TAKS2017 original English guidance](https://taks-2.cdn.fo/savn/2009/171027-transfer-pricing-guidelines.pdf?s=8fH4hUHIJNGzb9vHkqvE-ZUgNzk), actual webLF326–376, PDFpp12–13; exact quotes “transactions exceeding 500,000” / “not to say that individuals and enterprises should not keep documentation”; methodsLF365–370 “CUP method”, “Resale method”, “Cost plus method”, “Transactional net margin method”, “Profit split method”. Current duties cross-checkedTax118a.'),
('Practical workpaper',lambda:refs('tax',('118 a','Stk. 4.'))),('Tax Act §37b applies',lambda:refs('tax',('37 b','4:1'),('37 b','Lán frá triðjamanni'),('37 b','Frádráttaravmarkingin'))),
('Use year-end',lambda:refs('tax',('37 b','kursvirðið'),('37 b','2 ár'),('37 b','Kurstap'))),('Apply §37b(4)',lambda:refs('tax',('37 b','Stk. 4.'),('37 b','Stk. 5.'),('37 b','Stk. 6.'))),
('Disclose transaction',lambda:refs('tax',('118 a','slag og vav'),('118 a','60 dagar'))),('TAKS\'s company-return',lambda:refs('tax',('100','1. juli'),('103','rakstrarroknskap'),('105','15. august'))+'; online channel is earlier25October operational guidance, not a tested submission.'),
('Do not substitute',lambda:refs('tax','118 a')),
('Missing required',lambda:refs('tax',('118 a','Stk. 5.'),('141','3)'),('141','2 ár'),'139','140')),
('Ordinary company late',lambda:refs('tax',('81','0,7%'),('146','12%'))),
('Tax Act §37a(4)',lambda:refs('tax',('37 a','Stk. 4.'))+'; '+refs('admin',('8','5 ár'),'9')),
]
CB=[
('Tax Act §§118b',lambda:refs('tax','118 b')),
('Faroese ultimate-parent threshold',lambda:refs('tax',('118 c','5,6 mia.'))),('Report deadline',lambda:refs('tax',('118 c','12 mánaðir'))),('Notification |',lambda:refs('tax','118 f')+'; '+refs('regulation','2')),
('[Tax Act][law];',lambda:refs('tax','118 c')+'; TAKS actual webLF14–16; original quote “Markið á 5,6 milliardir krónur skal tulkast sambært vegleiðing hjá OECD um gjaldoyrasveiggj.” https://www.taks.fo/fo/vinna/skattur/land-fyri-land-fragreiding'),
('1. Establish the group',lambda:refs('tax','118 b','118 c','118 d','118 e','118 f')),
('**Local-filing threshold',lambda:refs('tax','118 c','118 d')+'; TAKS webLF14, “minst 5,6 milliardir krónur”; difference not silently resolved.'),
('Regulation §4 and',lambda:refs('regulation',('4','talvu 1-3'),('4','Umsetningurin fevnir ikki'),('4','Goldin skattur fevnir'),('4','ikki um útsettan'))),
('Use consistent employee',lambda:refs('regulation',('4','fulltíðarstørv'),('4','tøkan pening'),('4','Góðtikið fæ'),('4','Samanspardur vinningur'))),
('For a calendar',lambda:refs('tax',('118 c','12 mánaðir'),'118 f')),
('Notification identifies',lambda:refs('regulation','1','2','3')),
('TAKS publishes',lambda:'[TAKS CbCR guidance](https://www.taks.fo/fo/vinna/skattur/land-fyri-land-fragreiding), actual webLF19,43,48–50,72–74; exact quotes “TAKS skal hava avrit av fulltrú, um triðipersónur letur inn vegna samtaksfelagið.” and “Send um álítandi postskipan”. No transmission tested.'),
('If a parent refuses',lambda:refs('regulation',('4','Stk. 5.'))),
('Section 139c',lambda:refs('tax',('139 c','Við bót'),('139 c','1)'),('139 c','2)'))),
('Retain evidence for',lambda:refs('tax','118 e')+'; TAKS actual webLF22–25/64–67 refers to exchange agreements; exact anchor “Virkjaðar avtalur um útveksling”; no bilateral route inferred.'),
]
allcounts={};allproof={}
for slug,spec in [('fo-transfer-pricing',TP),('fo-country-by-country-reporting',CB)]:
 f=R/'skills/international/faroe-islands'/f'{slug}.md';body=f.read_text();(P/(slug+'-baseline.md')).write_text(body);rows=[]
 for lf,section,u in units(body):
  if u.startswith(('---','#')) or re.match(r'^\[[^]]+\]:',u) or section=='## Sources' or u.startswith(('|---','| Test')):continue
  sources=[]
  for needle,fn in spec:
   if needle in u:sources.append(fn())
  kind='express rule / record instruction'
  if section.startswith(('### 1.','### 2.')) or u.startswith('```oa-check'):
   if slug=='fo-transfer-pricing':sources=[refs('tax','37 a') if section.startswith('### 1.') else refs('tax',('118 a','36 mió.'),('118 a','72 mió.'),('118 a','50 fulltíðar'))]
   else:sources=[refs('tax',('118 c','5,6 mia.')) if section.startswith('### 1.') else refs('regulation',('4','Goldin skattur fevnir'),('4','ikki um útsettan'))]
   kind='hypothetical inputs / derived arithmetic; not quoted statutory amounts'
  if not sources:sources=['Operational workpaper, intake, caveat or expressly reserved scope; no separate tax entitlement asserted. See substantive rows and whole-unit mapping.'];kind='operational / explicit boundary'
  rows.append(dict(id=f'{slug}-{len(rows)+1:03}',lf=lf,section=section,wording=u,sources='; '.join(sources),read_on='2026-10-28 selected quoted primary scopes; old operational claims retain original read dates',status=kind))
 md=f'# {slug}: whole-Guide figure/rule ledger\n\nWriter record,28October2026; Guide body unchanged. Exact paragraph/rate wording below covers every substantive unit, including derived example inputs; source quotes are short original-language anchors with full article locators. Whole acquired sources are not claimed wholly read. Current Tax118a contains no explicit first-year/new-company substitute for the two-year test; startup application remains an ordinary legal-method boundary, not a Danish relief imported by analogy. No country-completion or independent-review claim.\n\n| ID / Guide LF / section | Exact Guide wording | Official source / act/article / short exact original quote | Read date / status |\n|---|---|---|---|\n'
 for z in rows:md+='| '+cell(f'{z["id"]} / LF{z["lf"]} / {z["section"]}')+' | '+cell(z['wording'])+' | '+cell(z['sources'])+' | '+cell(z['read_on']+'; '+z['status'])+' |\n'
 md+='\n## Complete old-topic destination table\n\n| Baseline | Every old topic/unit | Current exact destination |\n|---|---|---|\n';count=0
 for ref in ['origin/main','20572441dcdae9ebd4c282597940338832ade34e']:
  run=subprocess.run(['git','show',ref+':'+str(f.relative_to(R))],capture_output=True,text=True)
  if run.returncode:md+='| '+ref+' | Guide absent at this path | Published20572441 baseline mapped separately; no main content lost |\n';continue
  for lf,sec,u in units(run.stdout):
   assert u in body,(slug,lf,u[:50]);dest=body[:body.index(u)].count('\n')+1;md+='| '+ref+' | '+cell(f'LF{lf}, {sec}: {u}')+' | '+f'LF{dest}, exact'+' |\n';count+=1
 (P.parent/(slug+'.md')).write_text(md);(P/(slug+'-claim-rows.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');allcounts[slug]=dict(claim_rows=len(rows),old_units=count);allproof[slug]=dict(current_sha256=hashlib.sha256(body.encode()).hexdigest(),unchanged_vs_published=body==subprocess.check_output(['git','show','20572441dcdae9ebd4c282597940338832ade34e:'+str(f.relative_to(R))],text=True),original_oa_blocks=len(re.findall(r'```oa-check\n.*?\n```',body,re.S)))
ident=[]
for k,a in source_lines.items():ident.append(dict(id=k,url=source_urls[k],raw_sha256=hashlib.sha256((P/(k+'.html')).read_bytes()).hexdigest(),reader_sha256=hashlib.sha256((P/(k+'.reader.txt')).read_bytes()).hexdigest(),selected_exact_quote_anchor_LF=sorted(set(tuple(v) for v in read_scopes.get(k,[]))),actual_full_operative_read_scopes=({'tax':[[593,624],[870,923],[1072,1076]],'regulation':[[299,327]],'admin':[[327,338]]}[k]),note='Other source parts acquired, not fully read. Web originals/excerpts and PDF page labels separately preserved in tp-cb-web-source-response.json.'))
(P/'tp-cb-source-read-identities.json').write_text(json.dumps(ident,ensure_ascii=False,indent=2)+'\n');(P/'tp-cb-preservation-proof.json').write_text(json.dumps(allproof,indent=2)+'\n');print(json.dumps(allcounts));print(json.dumps(allproof))
