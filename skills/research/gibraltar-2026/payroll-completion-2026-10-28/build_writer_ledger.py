from pathlib import Path
import json,re,hashlib,subprocess
K=Path(__file__).resolve().parent;C=K.parents[3];S=C.parent/'work/sources';G=C/'skills/international/gibraltar/gi-payroll-social-insurance.md'
def norm(s):return re.sub(r'\s+',' ',s).strip()
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def clean(s):
 lines=[]
 for line in s.replace('\f','\n').splitlines():
  t=line.strip()
  if not t or t.startswith('© Government of Gibraltar') or re.fullmatch(r'(?:Page \d+(?: of \d+)?|\d+\s*\|\s*Page)',t):continue
  if re.fullmatch(r'(?:2010-21|1955-14|1952-10|1989/114|1955.08.04-5|2001/032|2024/086|1992/016)',t):continue
  if re.fullmatch(r'(?:Income Tax|Social Security \(Insurance\)|Social Security \(Employment Injuries|Insurance\)|Social Insurance \(Contributions\) Regulations|Employment Injuries \(Contributions\) Regulations 2001|Income Tax \(Pay As You Earn\) Regulations, 1989|Income Tax \(Allowances, Deductions and Exemptions\)|Rules, 1992)',t):continue
  if re.match(r'^(?:2010-21|1955-14|1952-10|1989/114|1955.08.04-5|2001/032|1992/016)\s{2,}',t):continue
  if re.search(r'\s{2,}(?:2010-21|1955-14|1952-10|1989/114|1955.08.04-5|2001/032|1992/016)$',t):continue
  lines.append(t)
 return '\n'.join(lines)
manifest=json.loads((S/'payroll/manifest.json').read_text());byname={r['name']:r for r in manifest}
keys={'PR':'paye-regulations.pdf','SI':'si-regulations.pdf','SA':'si-act.pdf','EI':'injuries-regulations.pdf','EN':'employer-notes.pdf','EMP':'employers-current.html','P8':'p8-guide.pdf','SE1':'se1.pdf','SCS':'se-schedule202627.pdf','SG':'se-guide.pdf','CA22':'ca3822-current.html','CA37':'ca3837-current.html','IN':'uk-inbound-current.html','DET':'detached-workers-current.html','SOC':'social-insurance-current.html','UK':'uk-order.pdf'}
specs={k:{'path':'payroll/'+Path(f).with_suffix('.txt').name,'raw':'payroll/'+f,'url':byname[f]['url']} for k,f in keys.items()}
specs.update({
 'B':{'path':'income-tax-act-20260323.txt','raw':'income-tax-act-20260323.pdf','url':'https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf'},
 'AL':{'path':'allowances-rules-20260323.txt','raw':'allowances-rules-20260323.pdf','url':'https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf'},
 'I':{'path':'individual/paye-current.txt','raw':'individual/paye-current.html','url':'https://www.gibraltar.gov.gi/income-tax-office/individuals-and-employees/paye'},
 'CONTACT':{'path':'corporate/ito-contacts-current.txt','raw':'corporate/ito-contacts-current.html','url':'https://www.gibraltar.gov.gi/contacts/income-tax-office-76'},
 'FORM':{'path':'payroll/second-employment-exemption.txt','raw':'payroll/second-employment-exemption.pdf','url':'https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/docs/contributions/4%29%20SOCIAL%20INSURANCE%20EXEMPTION.pdf'},
 'TREATY':{'path':'uk-gibraltar-treaty-official.txt','raw':'uk-gibraltar-treaty-official.html','url':'https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force'}})
texts={k:clean((S/v['path']).read_text()) for k,v in specs.items()};full_b=texts['B'];i=full_b.rfind('SCHEDULE 7');j=full_b.find('SCHEDULE 8',i);assert i>0 and j>i;texts['B']=full_b[i:j]
proofs={}
def addproof(id,src,provision,body):
 words=norm(body).split();quotes=[' '.join(words[i:i+45]) for i in range(0,len(words),45)];assert quotes and all(q in norm(texts[src]) for q in quotes)
 proofs[id]={'id':id,'source':src,'url':specs[src]['url'],'provision':provision,'read_on':'2026-10-28','evidence_mode':'Exact original-language source text, whitespace/layout headers normalized','quotes':quotes}
def proof(id,src,provision,start,end=None,last=False):
 t=texts[src];ms=list(re.finditer(start,t,re.M));assert ms,(id,start);m=ms[-1] if last else ms[0];stop=len(t)
 if end:
  n=re.search(end,t[m.end():],re.M);assert n,(id,end);stop=m.end()+n.start()
 addproof(id,src,provision,t[m.start():stop])
for n,end in [('2','3'),('3','4'),('4','5'),('5','6'),('6','7'),('8','9'),('11','12'),('13','13A'),('13A','14'),('16','17'),('17','18')]:
 plain={'2':r'^2\. In these','3':r'^3\. Where any payment','6':r'^6\. The Commissioner','13':r'^13\. Within one month','16':r'^16\. The Commissioner'}
 proof('PR'+n,'PR','PAYE Regulations '+n,plain.get(n,rf'^{n}\.\([1l]\)'),rf'^{end}\.\s*')
for n,end in [('4','4A'),('4A','4B'),('4B','4C'),('4C','5'),('5','6'),('6','7'),('7','8'),('17A','18')]:
 proof('SI'+n,'SI','Social Insurance Contributions Regulations '+n,rf'^{n}\.\s*'+(r'\(1\)' if n!='6' else r'Where contributions'),rf'^{end}\.\s*')
for n,end in [('5','6'),('7','8')]:proof('SA'+n,'SA','Social Security Insurance Act section '+n,rf'^{n}\.\([1l]\)',rf'^{end}\.\s*')
for n,end in [('2','3'),('3','4'),('4','5'),('5','6'),('7','8'),('8','9'),('9','10'),('10','11'),('12','13')]:
 plain={'2':r'^2\. In these','7':r'^7\. No person','9':r'^9\. Subject','12':r'^12\.'}
 proof('EI'+n,'EI','Employment Injuries Contributions Regulations '+n,plain.get(n,rf'^{n}\.\([1l]\)'),rf'^{end}\.\s*',last=n=='12')
for n,end in [('1','2'),('6','7'),('7','8'),('8','9'),('9','10'),('10','11'),('11','12'),('12','20'),('20','29'),('29','37'),('37','48'),('48','49'),('70','79'),('73','74'),('74','75')]:
 plain={'70':r'^70\. This Chapter','73':r'^73\.\(1\)'}
 proof('B'+n,'B','Income Tax Act Schedule7 paragraph '+n+('–'+str(int(end)-1) if end.isdigit() and int(end)>int(n)+1 else ''),plain.get(n,rf'^{n}\.\([1l]\)'),rf'^{end}\.\s*')
proof('ALtermination','AL','Allowances Rules3(7)–(10)',r'^\(7\) any sum paid as compensation',r'^\(11\)')
proof('AL317','AL','Allowances Rules3(17), printed investment-income wording',r'^\(17\) the investment income',r'^\(18\)')
proof('ALhealth','AL','Allowances Rules20A–20B',r'^20A\.\(1\)',r'^21\.\(1\)')
proof('EMPregister','EMP','Current employer FAQ registration/leaver/annual obligations',r'^Q\. How do I register as an employer\?$',r'^Q\. How can I apply for exemptions on Redundancy',last=True)
proof('EMPtermination','EMP','Current employer FAQ redundancy/gratuity application documents and payment hold',r'^Q\. How can I apply for exemptions on Redundancy',r'^For\s+any enquiries',last=True)
proof('EMPperiod','EMP','Current employer page2026/27 table links and2025/26 form dates',r'^P8, P10, P12 Guidelines',r'^Tax Table 2025/2026')
proof('EMPnotes','EMP','Current employer page notes explicitly grouped under2025/26',r'^Tax Table 2025/2026',r'^Tax Table 2024/2025')
proof('Iregister','I','Current employee FAQ first/returning starter registration',r'^Q\. I.m commencing employment in Gibraltar, what documents',r'^Q\. Of the')
proof('Ileave','I','Current employee FAQ permanent/indefinite departure',r'^A\. If you are leaving Gibraltar permanently',r'^Q\. What is a Benefit')
proof('Ibenefit','I','Current employee FAQ benefit threshold, election and pension contributions',r'^Q\. What is a Benefit-in-Kind',r'^Individuals and Employees',last=True)
proof('CONTACTsi','CONTACT','Current ITO Social Insurance Contributions Section general contact',r'^Social Insurance Contributions Section',r'^Students Exemptions')
proof('FORM','FORM','Official second-employment exemption application, entire one-page form',r'^SOCIAL INSURANCE EXEMPTION')
proof('ENfreq','EN','Employer notes2025/26 sections3–5 and payment frequency',r'^3\. CODES',r'^6\. LUMP SUM',last=True)
proof('ENlump','EN','Employer notes2025/26 section6 cessation lump sums',r'^6\. LUMP SUM',r'^7\. STUDENTS')
proof('ENpart','EN','Employer notes2025/26 section8 and part-time classification',r'^8\. PART-TIME',r'^PART 1')
proof('ENtables','EN','Employer notes2025/26 sections9–10 including disputed historical cells',r'^9\. HOW TO READ',r'^PART 3')
proof('ENshared','EN','Employer notes2025/26 section11.1 shared final week',r'^11\.1 HOW TO CALCULATE',r'^11\.2 HOW TO CALCULATE')
proof('ENpartial','EN','Employer notes2025/26 section11.2 partial-month weeks/limits',r'^11\.2 HOW TO CALCULATE',r'^2\.',last=True)
proof('ENjobs','EN','Employer notes2025/26 multiple-employer certificate instruction',r'^An employee who works for more than one employer',r'^SOCIAL INSURANCE CONTRIBUTIONS CALENDAR')
proof('UKorder','UK','UK social-security Order2024 paragraphs2–4',r'^2\. This Order comes',r'^Variation of Social Security')
proof('SE1','SE1','Official SE1 form sections3–9, status/document/licence and separate-PAYE fields',r'^Section 3 - Employment Details')
proof('SCS','SCS','Official 2026/27 self-employed annual schedule, one page',r'^26/27')
proof('SGerrors','SG','July2025 self-employed guide shared-week/partial-month printed intermediate products',r'^With effect from 1st July 2025',r'^When contributions need not be paid')
proof('SGadmin','SG','July2025 self-employed guide physical page8: monthly payment, written-rate authority and annual assessment',r'^Monthly remittances',r'^For further information',last=True)
proof('CA22','CA22','HMRC CA3822: Gibraltar,12month lead time, eligibility, agent, evidence, extension and online route',r'^You can use this form',r'^Check when you can expect a reply')
proof('CA22postal','CA22','HMRC CA3822 official change log: print/post removed',r'^Print and post option',r'^22 June 2023')
proof('CA37','CA37','HMRC CA3837: Gibraltar,12month lead time, evidence, agent, extension and online route',r'^You can use this form',r'^Check when you can expect a reply')
proof('CA37postal','CA37','HMRC CA3837 official change log: postal form removed',r'^The postal form \(CA3837\)',r'^5 June 2023')
proof('IN','IN','HMRC inbound Gibraltar coverage/PDA1 and work-permit distinction',r'^Coming to work in the UK —\s+from Gibraltar',r'^If you live in the UK',last=True)
proof('DET','DET','Current Gibraltar detached-worker contact',r'^For information on detached workers,',r'^Employers and Trusts')
proof('TREATY14','TREATY','UK–Gibraltar income-tax agreement Article14, distinct183day employment rule',r'^ARTICLE 14: Income from employment',r'^ARTICLE 15:',last=True)
# P8 evidence is scoped to the relevant actual pages; no invented field from a screenshot.
p8pages=(S/'payroll/p8-guide.txt').read_text().split('\f')
for n in [7,8,9,10,11,13,14,16,17]:addproof('P8p'+str(n),'P8','P8 submission guidance2025/26, physical/printed page'+str(n),clean(p8pages[n-1]))
visual=json.loads((K/'visual-source-proofs.json').read_text())
for p in visual:
 assert hashlib.sha256((S/'payroll'/p['source_file']).read_bytes()).hexdigest()==p['source_pdf_sha256'];assert p['id'] not in proofs;proofs[p['id']]=p
old=json.loads((K/'original-paragraphs.json').read_text());byid={int(x['id'][-3:]):x for x in old}
groups=[
 ('CLyear','2'),('EMPregister PR13 PR13A PR11','4 5'),('EMPperiod P8p8 P8p11','6'),('P8p7 P8p9 P8p10 P8p17','7'),('P8p13 P8p14','8 101'),('P8p16 P8p8 P8p11','9'),
 ('PR2 PR3','10'),('PR6 PR8','11'),('PR4 PR5','12'),('PR13 PR13A','13'),('EMPperiod EMPnotes ENfreq','14'),('ENfreq ENtables','15'),('ENfreq','16'),('ENlump ENpart','17'),
 ('ENfreq ENtables D35 M35 MSIe MSIr','19 20'),('Dgrey','21'),('D35 ENfreq','22'),('M35 MSIe MSIr CLerem CLerer','24'),('PR11','27 28 103'),('PR16 PR17','29 30 31'),
 ('CLyear CLerem CLerer CLse','33 34 35'),('CLerem CLerer CLmwem CLmwer CLpn CLpner CLt2 CLt2er CLxx','37 38 39 95'),('CLerwem CLerwer CLeraem CLeraer CLerem','40'),
 ('SA7','41 43'),('SA5','42 44'),('ENpartial ENshared CLerwem CLerwer','45 46 47 97 99'),('SI17A','48 49 50'),('SI4A SI4B EI2','51 52'),('SI4','53'),('SE1','54'),
 ('SCS','55'),('SCS SI4A SI4B','56'),('SGadmin','57 59'),('SGerrors','58'),('SI4C','60'),('SI4','61'),('EI5 SI4','62'),('EI4 EI8 SI4','63'),('EI7 EI4 SI4','64'),
 ('SI5 EI9 EI10 EI12','65 66 67 68 69'),('UKorder UK2 TREATY14','70'),('UK9 UK9ordinary','71'),('UK10 UK13','72 73 74'),('UK11','75 76 77'),('UK14 SA7','78'),
 ('UK9special UK9sea UK9air UK11 UK12 UK12overlap','79'),('IN DET','80'),('CA22 CA22postal','82 83'),('CA37 CA37postal','84 85'),('EI3 SI4 ENjobs','87'),('SA7 SI4 EI3 EI4 EI5 EI7 EI8','88'),
 ('CLerem CLerer PR8','89 90 92'),]
refs={}
for names,ids in groups:
 for s in ids.split():
  n=int(s);assert n not in refs,n;refs[n]=names.split()
nonrule=[1,3,18,26,32,36,81,86,91,94,105,106,107,108,109,110,111]
code=[23,25,93,96,98,100,102,104]
expected=set(range(1,112))-set(nonrule+code);assert set(refs)==expected,(sorted(expected-set(refs)),sorted(set(refs)-expected))
current=G.read_text();archive=(K/'preserved-payroll-controls.md').read_text()
def paras(t):
 body=t.split('---',2)[2].split('<!-- openaccountants-cta-block -->')[0];root='Title';head=root;out=[]
 for p in re.split(r'\n\s*\n',body.strip()):
  if p.startswith('#'):
   if p.startswith('## '):root=p[3:].strip();head=root
   elif p.startswith('### '):head=root+' > '+p[4:].strip()
   continue
  out.append((head,p))
 return out
cur=paras(current);maps=[]
for x in old:
 matches=[(h,p) for h,p in cur if p==x['text']]
 if matches:target=x['text'];dest='Guide: '+matches[0][0];disposition='Full original paragraph byte-exact'
 elif x['text'] in archive:target=x['text'];dest='preserved-payroll-controls.md';disposition='Full original executable block byte-exact in supplement'
 else:
  assert x['id']=='PAY-P106',(x['id'],x['text'][:100]);matches=[(h,p) for h,p in cur if p.startswith('The annual P8 controls above do not resolve')];assert len(matches)==1
  dest='Guide: '+matches[0][0];target=matches[0][1];disposition='Old minimum-wage/leave/redundancy/pension and employer-cost limits retained; blanket missing-benefit sentence narrowed to new sourced ordinary methods and explicit unresolved/specialist limits.'
 maps.append({k:v for k,v in x.items() if k!='text'}|{'destination':dest,'current_sha256':sha(target),'paragraph_exact':target==x['text'],'actual_old_anchor':norm(x['text'])[:180],'disposition':disposition})
dest={m['id']:m['destination'] for m in maps};rows=[]
for n in sorted(refs):
 x=byid[n];rows.append({'id':x['id'],'rule':x['text'],'guide_section':dest[x['id']],'proof_ids':refs[n],'read_on':'2026-10-28','original_paragraph_ids':[x['id']],'derivation_note':'Prose/example inputs are synthetic where stated; quotations establish the legal formula/table/condition, not those inputs. Unresolved source and operational limits remain explicit.'})
newrows=[
 ('N01','Starter employer/employee contact routes, returning P7A and actual code/certificate duties','Keep separate employer registration','EMPregister Iregister PR4 PR5 PR8 PR13A'),
 ('N02','Old/new employer P7A duties distinct from employee final-assessment claim and its published address','On leaving an employment,','EMPregister Ileave PR13A'),
 ('N03','Commissioner PAYE coding/direction recovery is not employer-made code or SI arrears permission','For PAYE previously not deducted/paid,','PR4 PR8 PR11'),
 ('N04','Redundancy/gratuity submission documents, published enquiry route and hold/directive before payment','For a proposed redundancy exemption,','EMPtermination ENlump'),
 ('N05','Different unfair-dismissal/redundancy/terminal/retiring injury death exemption categories; Commissioner and tribunal conditions retained','The exemption depends on the type of payment,','ALtermination'),
 ('N06','Choose special benefit Chapter first, money/moneysworth, employment/family link, exclusions and distinct SI/wage base','Schedule 7 paragraph 1 includes','B1 B37'),
 ('N07','Expenses exceed qualifying paid-away amount; cash/noncash vouchers/cards, exclusions/timing/value and no double counting','**Expenses, vouchers and cards:**','B6 B7 B8 B9 B10 B11'),
 ('N08','Accommodation rental/actual-higher rent/employee payment/nil, shared allocation, specific skills four-year exception and declaration','**Living accommodation:**','B12'),
 ('N09','Car/van definitions,3500kg, private use,25% first4years/0%, provision-market comparator, all pool conditions and shared-use rule; paragraph28 fuel90%/madegood, covered provision routes and printed paragraph23 reference','**Cars and vans:**','B20 B37'),
 ('N10','Loan scope/comparable unconnected interest less paid, relief exception,£1000 expense-advance/sixmonth/records, allocation/writeoff/death','**Employment-related loans:**','B29'),
 ('N11','Residual provision cost, madegood,20% nonland asset comparator, actual hire/additional expense and market transfer; no car double-rule','**Residual benefits and assets:**','B37 ALhealth'),
 ('N12','Nonapproved pension charge, no double charge and broken rule3(17) definition distinguished from administrative FAQ','**Pension caution:**','B48 AL317 Ibenefit'),
 ('N13','Separate explicit synthetic valuations500/500/8000, fuel1500, loan1500,18000/2700; no combined tax or SI result','**Independent valuation illustrations:**','B6 B8 B12 B20 B29 B37'),
 ('N14','Primary below£250 aggregate wording differs from first£250 FAQ; no automatic subtraction or exactly250 conclusion','Paragraph 73 states that no return/tax','B73 Ibenefit P8p14'),
 ('N15','Employer election20%/29% on relevant established whole benefit value and no extra employee tax on employer-paid tax; separate1000/20000 examples200/5800','Under paragraph 74 the employer can elect','B74 EMPregister'),
 ('N16','Dispensation statement/notice/scope, expense restriction, revocation and30day affected-return duty; no self approval','For a dispensation, paragraphs','B70'),
 ('N17','Published maximum-in-primary second-job form,three payslips/ID/two jobs/contact, changed circumstances and approval/certificate','ITO publishes a Social Insurance Exemption form','FORM CONTACTsi'),
 ('N18','Published max-case application not universal below-max allocation or retrospective refund','This supplies a published route for the maximum','FORM EI3 SI4 ENjobs'),
 ('N19','Court-recovery employer sums satisfy contributions and cannot be recovered from insured person; ordinary missed-wage question distinct','Social Insurance regulation 7 concerns','SI7 SA7')]
for id,rule,anchor,names in newrows:
 matches=[(h,p) for h,p in cur if p.startswith(anchor)];assert len(matches)==1,(id,anchor,len(matches))
 rows.append({'id':'PAY-'+id,'rule':rule,'assertion':matches[0][1],'guide_section':'Guide: '+matches[0][0],'new_anchor':anchor,'proof_ids':names.split(),'read_on':'2026-10-28','original_paragraph_ids':[],'derivation_note':'New writer method; no independent acceptance or publication.'})
for r in rows:assert all(k in proofs for k in r['proof_ids']),(r['id'],[k for k in r['proof_ids'] if k not in proofs])
assert len(maps)==111 and sum(m['paragraph_exact'] for m in maps)==110
marker='<!-- openaccountants-cta-block -->';before=(K/'gi-payroll-social-insurance.before.txt').read_text();assert current.count(marker)==1 and current[current.index(marker):]==before[before.index(marker):]
assert before==subprocess.check_output(['git','show','b98e7f01:skills/international/gibraltar/gi-payroll-social-insurance.md'],cwd=C).decode()
H=['Who this applies to','Rates, bands and thresholds','The base','Deadlines and filing','Penalties and interest','Cross-border points','Two worked examples that recompute','Ask the client first','Sources'];assert re.findall(r'^## (.+)$',current.split(marker)[0],re.M)==H
pat=re.compile(r'```oa-check\n.*?```',re.S);assert len(pat.findall(before))==8 and len(pat.findall(current))==2 and len(pat.findall(archive))==6 and all(b in current+archive for b in pat.findall(before))
result={'status':'Full payroll writer ledger; independent country new-material review pending','guide_version':'0.15','read_on':'2026-10-28','guide_sha256':sha(current),'rows':rows,'source_proofs':list(proofs.values()),'old_paragraph_map':maps,'nonrule_original_ids':[f'PAY-P{i:03}' for i in nonrule],'original_control_ids':[f'PAY-P{i:03}' for i in code],'inherited_legal_derived_paragraphs':len(expected),'new_rule_rows':len(newrows),'country_complete':False,'independent_acceptance':False,'published':False}
(K/'ledger.json').write_text(json.dumps(result,indent=2)+'\n')
esc=lambda s:s.replace('|','\\|').replace('\n',' ')
md=['# Gibraltar payroll and social insurance: full figure/rule ledger\n','Writer source checks on 28 October 2026. Guide v0.15 is new, unreviewed country material. The earlier whole/delta reviews keep their exact scopes. No accountant attestation, completed country or live payroll/filing is claimed. English is the sources’ original language. Text quotes are own-source matched after whitespace/layout-header normalization, at most 45 words each. Scanned agreement and table cells have separately labelled visual transcriptions tied to source PDF hashes and exact page/row/column locators; OCR is not quotation authority.\n','## Rule and figure inventory\n','All 86 original legal/derived paragraphs are recorded in full, with current destinations and exact source-quote proofs. Original synthetic examples stay explicitly conditional; source quotations establish the formula, table or rule rather than inventing their inputs. New method rows also preserve the actual current assertion text in ledger.json.\n','| ID | Current section; rule or figure and conditions | Exact original-language quotation/provision evidence | Read date |','|---|---|---|---|']
for r in rows:
 parts=[]
 for k in r['proof_ids']:
  p=proofs[k];parts.append(f'[{k}](#proof-{k.lower()}): {p["provision"]}; [official source]({p["url"]}); “{p["quotes"][0]}”')
 md.append('| '+' | '.join(esc(v) for v in [r['id'],r['guide_section']+': '+r['rule'],'; '.join(parts),r['read_on']])+' |')
md+=['\n## Exact source proofs\n','Every proof keeps its own official URL and actual date. Read full linked context and conditions, not just a headline number. Visual proofs must be checked against the saved original PDF/rendered page, not against OCR or this transcription alone.\n']
for p in proofs.values():
 md.append(f'### Proof {p["id"]}\n\n{p["provision"]}. [Official source]({p["url"]}). Read {p["read_on"]}. {p["evidence_mode"]}.\n')
 for q in p['quotes']:md.append('> '+q+'\n')
md+=['## Complete old-topic destination table\n','Original full paragraphs and hashes are in [original-paragraphs.json](../original-paragraphs.json). All 111 entries are mapped from actual current paragraph matches. 110 stay byte-exact across Guide/supplement; one evidence-limit paragraph is explicitly narrowed for the new sourced benefit methods. All 8 original checks remain byte-exact.\n','| Original ID | Original section | Actual original anchor | Current destination / preservation |','|---|---|---|---|']
for m in maps:md.append('| '+' | '.join(esc(v) for v in [m['id'],m['heading'],m['actual_old_anchor'],m['destination']+'; '+m['disposition']])+' |')
md+=['\n## Nonrule/control accounting and remaining limits\n','Nonrule/intake/source-status/record/exclusion records: '+', '.join(result['nonrule_original_ids'])+'. They are preserved, with the one mapped limitation reconciliation, without pretending they are new legal authority.\n','Original executable records: '+', '.join(result['original_control_ids'])+'. Two stay in the main Guide, six are in [preserved-payroll-controls.md](../preserved-payroll-controls.md). Three separate new benefit scenarios are in [benefit-controls.md](../benefit-controls.md).\n','Unresolved points remain explicit: dated PAYE notes versus current-linked tables; grey-cell treatment; ordinary missed employee-SI wage recovery; first-employer/general concurrent allocation; annual-form/quarterly-duty interaction; threshold wording/boundary; the pension definition cross-reference; procedural/year and specialist limits. The published maximum-in-main-job form supplies a bounded application route, not general exemption approval. No email, claim, live payroll or payment was sent.\n']
(K/'ledgers/gi-payroll-social-insurance.md').write_text('\n'.join(md)+'\n')
summary={'rows':len(rows),'inherited_rule_paragraphs':len(expected),'new_rule_rows':len(newrows),'proofs':len(proofs),'text_quotes':sum(len(p['quotes']) for p in proofs.values() if p not in visual),'visual_quotes':sum(len(p['quotes']) for p in visual),'old_paragraph_destinations':111,'old_paragraphs_exact':110,'original_controls_preserved':8,'main_controls':2,'new_benefit_blocks':3,'canonical_sections':9,'CTA_exact':True,'independent_acceptance':False,'published':False,'country_complete':False}
(K/'writer-complete-audit.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
