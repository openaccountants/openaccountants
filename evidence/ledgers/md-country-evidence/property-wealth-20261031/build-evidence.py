from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib,json,re,shutil,subprocess
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/moldova-pack-2026-10-30');R=W/'repository'
BASE='a691ffba790bfec850c5b18f01d8c4e342c05ae9'
D=R/'evidence/ledgers/md-country-evidence/property-wealth-20261031';D.mkdir(exist_ok=True)
S=D/'sources';S.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
copy_names=['property-wealth-current-code-20261031.json','property-wealth-extra-code-20261031.json','property-law1056-current-20261031.json','property-bij17-current-order-20261031.json','property-bij17-form-20261031.docx','property-bij17-form-20261031.txt','property-bij17-instructions-20261031.docx','property-bij17-instructions-20261031.txt','property-notice-order17-20261031.json','property-notice-repeal2027-header.txt','wealth-notice-order138-20261031.json','wealth-notice-form-20261031.doc','wealth-notice-form-20261031.docx','wealth-notice-form-20261031.txt','property-boscana-rates2026.pdf','property-boscana-rates2026.txt']
for n in [1,2,5,6]:copy_names += [f'property-notice-annex{n}-20261031.{e}' for e in ['doc','docx','txt']]
for name in copy_names:
 shutil.copy2(W/'primary-attachments'/name,S/name)
 if name.endswith('.txt'):
  # Text derivatives only: original DOC/DOCX/PDF and private raw extraction remain exact.
  f=S/name;f.write_text('\n'.join(x.rstrip() for x in f.read_text().splitlines()).rstrip()+'\n')
# Preserve entire website captures privately. Publish only small procedural excerpts,
# distinct from normative law/form sources. No licence conclusion is made here.
proc={
 'wealth-mpay':{'file':'wealth-mpay-20261031.json','quotes':['Impozitul pe avere','IDNP / Cod fiscal','CAUTĂ IDNP / COD FISCAL'],'context':'Public wealth-tax entry: identifier retrieval; no account queried or payment made.'},
 'property-mpay':{'file':'property-mpay-20261031.json','quotes':['Impozitul pe bunuri imobiliare (cu aviz de plata)','Aviz nr.','CAUTĂ AVIZ NR.'],'context':'Public notice-number entry; visible online service link to SFS fisa_imobilului. No account queried or payment made.'},
 'ctif-access':{'file':'property-filing-ctif-access-20261031.json','quotes':['Intrarea în „Cabinetul personal al contribuabilului” este cu statut de persoană fizică, ca cetățean','companiilor și rolurilor necesare'],'context':'Official CTIF FAQ, tax-service question 1: signatory authentication, authorised company/role and initial connection agreement.'}}
for k,v in proc.items():
 j=json.loads((W/'primary-attachments'/v['file']).read_text());text=j['text']
 # Browser visible button labels can be title case in body text; retain actual substring.
 qs=[]
 for q in v['quotes']:
  m=re.search(re.escape(q),text,re.I);assert m,(k,q);qs.append(m.group())
 dump(S/f'{k}-procedural-excerpts.json',{'official_url':j['official_url'],'read_date':j['read_date'],'source_kind':'official website procedural copy, not normative law','exact_excerpts':qs,'read_scope':v['context'],'raw_private_capture':str(W/'primary-attachments'/v['file']),'raw_sha256':sha((W/'primary-attachments'/v['file']).read_bytes()),'publication_review':'Pending parent source-publication assessment; no copyright clearance asserted.'})
dump(S/'age-efiling-procedural-excerpt.json',{'official_url':'https://www.egov.md/ro/content/serviciul-declaratia-electronica','read_date':'2026-10-31','source_kind':'official website procedural copy, not normative law','exact_excerpts':['Serviciul Declaraţie electronică reprezintă o metodă de perfectare şi prezentare a documentelor fiscale online.'],'read_scope':'Official AGE public page, electronic declaration service, actually opened through web tool. No authenticated return tested.','publication_review':'Pending parent source-publication assessment; no copyright clearance asserted.'})
# Future repeal entry was visibly read in the law register; keep temporal status explicit.
dump(S/'wealth-notice-future-repeal-entry.json',{'official_url':'https://www.legis.md/cautare/getResults?doc_id=155986&lang=ro','read_date':'2026-10-31','source_kind':'normative register repeal header, future commencement','text':'Abrogat prin OMF123 din 18.08.26, MO386-389/21.08.26 art.683b; în vigoare 01.01.27','read_scope':'Header visibly read in normal browser; operative 2016 version and original form separately retained. Not an operative 2026 repeal.'})
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def docx_units(name):
 with ZipFile(S/name) as z:root=etree.fromstring(z.read('word/document.xml'))
 paras=[''.join(p.xpath('.//w:t/text()',namespaces=ns)) for p in root.findall('.//w:p',ns)]
 tables=[]
 for ti,t in enumerate(root.findall('.//w:tbl',ns),1):
  for ri,tr in enumerate(t.findall('./w:tr',ns),1):
   cells=['\n'.join(''.join(p.xpath('.//w:t/text()',namespaces=ns)) for p in tc.findall('.//w:p',ns)) for tc in tr.findall('./w:tc',ns)]
   tables.append({'table':ti,'row':ri,'cells':cells})
 j={'original_file':name,'original_sha256':sha((S/name).read_bytes()),'paragraphs':paras,'table_rows':tables,'derivative':'Exact Word paragraph/cell text; no translation or OCR. DOC conversions are derived; original DOC retained.'}
 dump(S/(name.replace('.docx','-units.json')),j);return j
units={n:docx_units(n) for n in copy_names if n.endswith('.docx')}
code=json.loads((S/'property-wealth-current-code-20261031.json').read_text());extra=json.loads((S/'property-wealth-extra-code-20261031.json').read_text())
articles={a['article']:a['text'] for a in code['articles']+extra['articles']}
CODE=code['official_url'];rows={'property':[],'wealth':[]}
def add(job,section,act,url,quote,source,context=None,date='2026-10-31',kind='normative act or approved form',rule=None):
 if not quote.strip():return
 prefix='MD-PROP' if job=='property' else 'MD-WEALTH';rs=rows[job]
 rs.append({'id':f'{prefix}-{len(rs)+1:03d}','rule_or_figure':rule or act,'Guide_section':section,'act_article_or_official_section':act,'official_url':url,'exact_original_language_quote':quote,'read_date':date,'source_observation':str(source.relative_to(R)),'source_context':quote,'source_text_sha256':sha(quote.encode()),'surrounding_context_sha256':sha((context or quote).encode()),'surrounding_context_locator':act+' in source_observation; complete surrounding text is retained there without repeated copies in each ledger row','source_kind':kind,'independent_review':'PENDING NEW METHOD REVIEW'})
def paragraphs(t):return [x.strip() for x in re.split(r'\n\s*\n',t) if x.strip()]
sections={'276':'Who this applies to','277':'Who this applies to','278':'Who this applies to','279':'The base','280':'Rates, bands and thresholds','2801':'Deadlines and filing','281':'The base','2811':'Deadlines and filing','282':'Deadlines and filing','2821':'The base','283':'The base','284':'The base','285':'The base','286':'Deadlines and filing','287':'The base'}
for job,nums in [('property',list(sections)),('wealth',['2871','2872','2873','2874','2875','2876','2877'])]:
 for n in nums:
  for i,p in enumerate(paragraphs(articles[n]),1):
   # Retain every normative paragraph including first short operative clauses;
   # skip only article heading/formatting fragments, never a repeal or threshold.
   if p.startswith('Articolul ') or (len(p)<20 and not any(c.isdigit() for c in p)):continue
   sec=sections[n] if job=='property' else ('Rates, bands and thresholds' if n in ['2873','2874'] else 'Deadlines and filing' if n in ['2875','2876','2877'] else 'Who this applies to')
   add(job,sec,f'Fiscal Code article {n}, retained paragraph {i}',CODE,p,S/'property-wealth-current-code-20261031.json',context=articles[n])
# Add only the administrative rules actually used, preserving surrounding articles in source.
for job in rows:
 for n in ['129','187','188','228','232','260','261','267','2671','2672','2673']:
  if job=='wealth' and n in ['187','188','232','261']:continue
  for i,p in enumerate(paragraphs(articles[n]),1):
   select=False
   if n=='129':select=p.startswith('(8)')
   elif n=='187':select=p.startswith(('(3)','j)','k)','(4)','(5)','(6)'))
   elif n=='188':select=p.startswith(('(1)','(2)','(3)','(4)','b)','c)','d)'))
   elif n=='228':select=p.startswith(('(1)','(2)','(21)','(3)','(5)','a)','a1)','a2)','b)','(6)','(7)'))
   elif n=='232':select=p.startswith(('a)','b)','c)'))
   elif n=='260':select=p.startswith('(1)')
   elif n=='261':select=p.startswith(('(4)','(41)','(5)'))
   else:select=not p.startswith('Articolul ') and len(p)>45
   if select:add(job,'Deadlines and filing' if n in ['129','187','188'] else 'Penalties and interest',f'Fiscal Code article {n}, retained paragraph {i}',CODE,p,S/('property-wealth-extra-code-20261031.json' if n in ['129','187','188','232'] else 'property-wealth-current-code-20261031.json'),context=articles[n])
trans=json.loads((S/'property-law1056-current-20261031.json').read_text())
start=trans['text'].index('Articolul 4.')
for i,p in enumerate(paragraphs(trans['text'][start:]),1):
 if p.startswith(('PREŞEDINTELE','Nr. 1056')) or p.startswith('Articolul 4.'):continue
 if len(p)<20:continue
 add('property','Deadlines and filing' if p.startswith(('(7)','(9)','a) persoanele','b) pentru persoanele','c) persoanele','d) prevederile','c) prevederile')) else 'The base',f'Law 1056/2000 article 4/annexes, retained paragraph {i}',trans['official_url'],p,S/'property-law1056-current-20261031.json')
# Approval orders and complete operative instructions.
for job,name in [('property','property-bij17-current-order-20261031.json'),('property','property-notice-order17-20261031.json'),('wealth','wealth-notice-order138-20261031.json')]:
 j=json.loads((S/name).read_text());t=j.get('text') or j.get('body') or j.get('content')
 assert t,(name,j.keys())
 for i,p in enumerate(paragraphs(t),1):
  if any(x in p for x in ['Se aprobă','Se abrogă','intră în vigoare','se aplică','MODIFICAT','OMF130','OSFS533']):add(job,'Deadlines and filing',f'{name} operative approval paragraph {i}',j['official_url'],p,S/name)
inst=units['property-bij17-instructions-20261031.docx']
for i,p in enumerate(inst['paragraphs'],1):
 if len(p.strip())>30:add('property','Deadlines and filing' if not p.startswith(('6.','7.','8.','9.','10.')) else 'The base',f'BIJ17 approved instructions, original Word paragraph {i}','https://www.legis.md/UserFiles/Image/RO/2024/mo459-461ro/anexa2_73.docx',p,S/'property-bij17-instructions-20261031-units.json')
# Actual form fields: one binding per meaningful nonempty Word table row, no blank grids.
form_urls={'property-bij17-form-20261031.docx':'https://www.legis.md/UserFiles/Image/RO/2021/mo%2057-65%20md/anexa1_73.docx','wealth-notice-form-20261031.docx':'https://www.legis.md/UserFiles/Image/anexa_138.doc'}
order=json.loads((S/'property-notice-order17-20261031.json').read_text())
for n in [1,2,5,6]:form_urls[f'property-notice-annex{n}-20261031.docx']=next(x['url'] for x in order['links'] if x['text'].strip()==f'anexa nr.{n}')
for name,url in form_urls.items():
 job='wealth' if name.startswith('wealth') else 'property';seen=set()
 for u in units[name]['table_rows']:
  q=' | '.join(c for c in u['cells'] if c.strip())
  if not any(re.search(r'[A-Za-zăâîșţț]',c) for c in u['cells']) or q in seen:continue
  seen.add(q)
  add(job,'Deadlines and filing',f'{name}, table {u["table"]} row {u["row"]} exact cell sequence',url,q,S/name.replace('.docx','-units.json'),context=q,rule='Approved form fields/category or relief-code row; read with the entire row and governing law')
# Reuse the already reviewed enacted wage; do not redo its independent review.
wage=R/'evidence/ledgers/md-country-evidence/sources/fiscal-code-article-PLANNING-HG773-WAGE2026.json';j=json.loads(wage.read_text());p=next(x for x in paragraphs(j['text']) if x.startswith('Se aprobă'))
add('wealth','Rates, bands and thresholds','HG773/2025 operative 2026 wage paragraph',j['official_url'],p,wage,date='2026-10-30',rule='Enacted forecast salary; derived gate 200 × 17,400 = 3,480,000')
for job,key in [('wealth','wealth-mpay'),('property','property-mpay'),('property','ctif-access'),('property','age-efiling')]:
 fn=S/(key+'-procedural-excerpts.json' if key!='age-efiling' else 'age-efiling-procedural-excerpt.json');j=json.loads(fn.read_text())
 for i,q in enumerate(j['exact_excerpts'],1):add(job,'Deadlines and filing',f'{key} public procedural field/excerpt {i}',j['official_url'],q,fn,kind=j['source_kind'],rule=j['read_scope'])
future=S/'wealth-notice-future-repeal-entry.json';j=json.loads(future.read_text());add('wealth','Deadlines and filing','MF Order138 register: future 1 January 2027 repeal',j['official_url'],j['text'],future)
# Local example is explicitly locality-specific; preserve exact PDF reading order/layout.
boscana=(S/'property-boscana-rates2026.txt').read_text();i=boscana.index('6.');e=boscana.index('7.',i);q=boscana[i:e].strip()
add('property','Two worked examples that recompute','Boscana decision 6/3 of 10 December 2025, annex 1 II.6','https://boscana.sat.md/wp-content/uploads/sites/14/2026/02/Cotele-impozitului-funciar-si-pe-bunurile-imobiliare-2026.pdf',q,S/'property-boscana-rates2026.txt',rule='Actual Boscana ordinary agricultural 2 and pasture 0.75 per degree-hectare; no universal municipal rate')
# Complete old topic destinations: every predecessor unit remains byte-exact at the same path.
old=[];baseline=[]
for file in sorted((R/'skills/moldova').glob('*.md')):
 if file.name in ['md-property-tax.md','md-wealth-tax.md']:continue
 rel=str(file.relative_to(R));b=subprocess.check_output(['git','show',BASE+':'+rel],cwd=R)
 if file.name=='README.md':
  (D/'README-before-property-wealth.md').write_bytes(b);continue
 assert file.read_bytes()==b,rel
 baseline.append({'path':rel,'sha256':sha(b)})
 text=b.decode();off=0
 for n,m in enumerate(re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',text),1):
  body=m.group();line=text.count('\n',0,m.start())+1
  old.append({'source_file':rel,'source_unit':n,'source_line':line,'old_text':body,'old_sha256':sha(body.encode()),'destination':rel+':'+str(line),'status':'Retained byte-exact in existing Guide; the two new methods are additions, not rewrites.'})
dump(D/'predecessor-guide-manifest.json',{'baseline_commit':BASE,'Guide_files':baseline,'new_jobs_have_no_predecessor':True,'lost_content':0})
dump(D/'old-topic-destinations.json',{'scope':'All 11 predecessor Guides; every nonblank paragraph/table/code unit kept at its original destination. Original earlier 3,913-row and 185-row reviews not reopened.','rows':old})
md=['# Complete Moldova predecessor destinations','',f'{len(old)} predecessor units across {len(baseline)} existing Guides, all retained byte-exact. No old Guide is rewritten by this delta. Full original unit text and hashes are in `old-topic-destinations.json`.','', '| Source / unit | Old topic excerpt | Destination |','|---|---|---|']
for u in old:md.append('| '+u['source_file']+' / '+str(u['source_unit'])+' | '+re.sub(r'\s+',' ',u['old_text'])[:100].replace('|','\\|')+' | '+u['destination']+' |')
(D/'OLD-TOPIC-DESTINATIONS.md').write_text('\n'.join(md)+'\n')
for job,rs in rows.items():
 slug='md-property-tax' if job=='property' else 'md-wealth-tax';guide=R/'skills/moldova'/f'{slug}.md'
 obj={'Guide':str(guide.relative_to(R)),'new_job':job+'-tax','read_date':'2026-10-31','status':'New operative method candidate; independent review pending; country remains partial.','Guide_sha256':sha(guide.read_bytes()),'rows':rs,'old_topic_destinations':'evidence/ledgers/md-country-evidence/property-wealth-20261031/old-topic-destinations.json','predecessor_preservation_manifest':'evidence/ledgers/md-country-evidence/property-wealth-20261031/predecessor-guide-manifest.json','calculation_examples':'Both Guide oa-check blocks are hypothetical facts; cited law/local decision controls the parameters.','source_publication_review':'Normative source/form material separated from minimal official website procedural excerpts; raw website captures retained privately. No blanket copyright clearance.'}
 dump(R/'evidence/ledgers'/f'{slug}.writer.json',obj)
 out=[f'# {slug} figure and rule ledger','',f'{len(rs)} source bindings. Quote membership and source hashes are mechanically checked; independent legal review is pending. Complete surrounding provisions remain in the source artifact. Form-table rows use a vertical bar between exact original cells; the row locator identifies those cells. The complete old-topic destination table is linked below.','', '| ID | Guide section | Act/article/form field | Official URL | Exact original-language quote | Read date |','|---|---|---|---|---|---|']
 for r in rs:out.append('| '+' | '.join(str(r[k]).replace('|','\\|').replace('\n','<br>') for k in ['id','Guide_section','act_article_or_official_section','official_url','exact_original_language_quote','read_date'])+' |')
 out+=['','## Complete old-topic destinations','','These are new jobs. All 11 predecessor Guides and their topics are retained byte-exact. See the [complete per-unit destination table](md-country-evidence/property-wealth-20261031/OLD-TOPIC-DESTINATIONS.md), [full original units/hashes](md-country-evidence/property-wealth-20261031/old-topic-destinations.json) and [file manifest](md-country-evidence/property-wealth-20261031/predecessor-guide-manifest.json). No original tax topic, CTA or platform attribution was removed.','', '## Review boundaries','','The new method needs fresh independent review. Prior 3,913-row review and accepted 185-row VAT refund review remain separate; these source bindings do not establish country completion.']
 (R/'evidence/ledgers'/f'{slug}.md').write_text('\n'.join(out)+'\n')
# Readiness is not completeness. Preserve the full remaining country scope unchanged.
shutil.copy2(R/'evidence/ledgers/md-country-evidence/vat-refund-20261031/completion-scope-and-next-jobs.json',D/'completion-scope-before-property-wealth.json')
dump(D/'WRITER-CHOICES.json',{'date':'2026-10-31','options':[{'label':'A. Separate property and wealth methods','selected':True,'why':'Different taxpayer populations, bases, assessing bodies, returns/notices, deadlines and payment keys.'},{'label':'B. Combined property and wealth reference','selected':False,'why':'Would conflate separate jobs and weaken routing; retain cross-links instead.'}],'unresolved_operative_questions':['Article283(6) first-year decision/accepted relief code','Law1056 unevaluated farm-land SCITL/unified-return interaction','Authenticated BIJ17/UNIF25 technical acceptance/final rounding','Taxpayer-specific local decisions, valuations and municipal appeal route'],'not_excluded':'All ordinary branches remain in the method and completion scope. These questions are not counted as comprehensive closure.','no_authority_contact':True,'no_push':True})
# Source-kind manifest pins originals and text derivatives. Never call website wrappers statutes.
manifest=[]
for f in sorted(S.iterdir()):
 kind='normative act/form or derivative'
 if 'procedural-excerpt' in f.name:kind='official website procedural excerpt; separate publication review pending'
 manifest.append({'path':str(f.relative_to(R)),'sha256':sha(f.read_bytes()),'bytes':f.stat().st_size,'kind':kind})
dump(D/'source-manifest.json',{'date':'2026-10-31','sources':manifest,'raw_originals_preserved':True,'text_derivatives':'Trailing line whitespace/blank EOF normalised in public .txt derivatives only; private raw extraction and original DOC/DOCX/PDF bytes retained unchanged.','private_raw_website_capture_directory':str(W/'primary-attachments'),'rendering_read_record':'BIJ17 form 5 pages/instructions 3 pages; wealth notice 1 page; property notices annexes 1/2/5/6 one page each; Boscana all 4 pages were visually inspected. Original DOC conversions retained alongside original binaries.','blocked_sources':['SFS public wealth FAQ and workflow pages: direct 403/normal-browser automatic security verification; no CAPTCHA solved.','SFS 2025 electronic filing guide/Monitorul copy: 403; not used to assert unobserved portal button sequence.'],'copyright_status':'No blanket clearance claimed. Normative content and website procedural text are distinguished for parent publication review.'})
print(json.dumps({'property_rows':len(rows['property']),'wealth_rows':len(rows['wealth']),'predecessor_Guides':len(baseline),'old_units':len(old),'source_files':len(manifest)}))
