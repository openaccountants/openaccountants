from pathlib import Path
import json,re,hashlib,subprocess
import yaml
K=Path(__file__).resolve().parent;C=K.parents[3];S=C.parent/'work/sources/consumption';G=C/'skills/international/gibraltar/gi-transaction-tax-transition.md'
def norm(t):return re.sub(r'\s+',' ',t).strip()
def sha(b):return hashlib.sha256(b).hexdigest()
def clean(t):
 return '\n'.join(x.strip() for x in t.replace('\f','\n').splitlines() if x.strip() and not re.search(r'© Government of Gibraltar|^\s*Page \d+ of \d+',x))
manifest=json.loads((S/'manifest.json').read_text())+json.loads((S/'targeted-followup-receipts.json').read_text())
spec={x['name']:x['url'] for x in manifest}
spec['eu-deminimis-browser.txt']='https://eur-lex.europa.eu/eli/reg/2023/2831/oj/eng'
spec['council-register-browser.txt']=spec['council-register.html']
proofs={}
def add(id,file,provision,body):
 full=(S/Path(file).with_suffix('.txt')).read_text() if file.endswith('.pdf') else (S/file).read_text()
 assert norm(body) in norm(clean(full)),id
 words=norm(body).split();quotes=[' '.join(words[i:i+45]) for i in range(0,len(words),45)]
 assert quotes and all(q in norm(clean(full)) for q in quotes),id
 raw=S/file
 proofs[id]={'id':id,'source_file':file,'source_sha256':sha(raw.read_bytes()),'url':spec[file],'provision':provision,'read_on':'2026-10-28','evidence_mode':'Exact English source text; whitespace and copyright/page footers normalized; browser-visible text where labelled browser','quotes':quotes}
def pages(id,file,ns,provision):
 text=(S/Path(file).with_suffix('.txt')).read_text().split('\f')
 for n in ns:add(id+'p'+str(n),file,provision+'; physical/printed page '+str(n),clean(text[n-1]))
def span(id,file,provision,start,end,last=False):
 t=clean((S/(Path(file).with_suffix('.txt') if file.endswith('.pdf') else file)).read_text());ms=list(re.finditer(start,t,re.M));assert ms,(id,start);m=ms[-1] if last else ms[0];stop=len(t)
 if end:
  e=re.search(end,t[m.end():],re.M);assert e,(id,end);stop=m.end()+e.start()
 add(id,file,provision,t[m.start():stop])
pages('A','transaction-act.pdf',[1,15,16,53,66,67,68,82,83,84,97,103,104,105,106],'TGEU Act commencement/ss6,10,68,98–102,130–131 and Schedules1–2 as indicated on page')
pages('D','deductions-rules.pdf',[1,2,3,4,5],'Deductions Rules commencement/rules2–6 as indicated on page')
span('T248','treaty-volume1.pdf','Treaty Article248',r'^ARTICLE 248$',r'^ARTICLE 249$')
span('T336','treaty-volume1.pdf','Treaty Article336',r'^ARTICLE 336$',r'^DONE at Brussels')
span('T18','treaty-volume2.pdf','Annex18 opening adaptation and Union acts through deminimis list3.4',r'^ANNEX 18$',r'^4\.\s+Procedural rules')
span('T24','treaty-volume2.pdf','Annex24 II paragraph3 rate sequence and consultations',r'^3\.\s+The rate of the transaction tax',r'^4\.',last=True)
pages('AR','annex19-regulations.pdf',[2,3,4,5],'LN2026/188 regulations3–6 as indicated on page')
pages('UR','union-procedures-regulations.pdf',[2,3,4,5,7,8,9,16,17,18,19,20,21,22,23],'LN2026/211 regulation3–4/Schedules1–2; replacement provisions as indicated on page')
span('IE2A','imports-exports-act.pdf','ImportsExportsAct section2A treaty primacy',r'^2A\.\(1\)',r'^Appointment',last=True)
span('IE17','imports-exports-act.pdf','ImportsExportsAct section17 entry timing',r'^17\. In this section',r'^Inward manifests')
span('IE21','imports-exports-act.pdf','ImportsExportsAct sections21–23 entry/clearance',r'^21\.\(1\)',r'^Passengers’ Baggage')
span('IE109','imports-exports-act.pdf','ImportsExportsAct section109 false documents/statements',r'^109\.\(1\)',r'^Counterfeiting documents')
span('IE117','imports-exports-act.pdf','ImportsExportsAct section117 general penalty',r'^117\.\(1\)',r'^Rewards\.')
span('TR2','transit-guidance.pdf','Transit guidance section2 import home use',r'^2\.\s+Imports for Home Use',r'^3\.\s+Imports')
span('TR4','transit-guidance.pdf','Transit guidance sections4.1–4.2 export processes, including broken crossreference',r'^4\.\s+Exporting Goods',r'^5\.\s+Further Assistance')
span('GNintro','annex19-guidance.pdf','Annex19 guidance introduction and Union-only scope',r'^INTRODUCTION$',r'^1\.\s+IMPORTING')
span('GN1','annex19-guidance.pdf','Annex19 guidance section1 all three entry/discharge processes',r'^1\.\s+IMPORTING',r'^2\.\s+REQUIREMENT')
span('GN25','annex19-guidance.pdf','Annex19 guidance sections2–5 licensing,authorisation,operation,transition',r'^2\.\s+REQUIREMENT',r'^6\.\s+FURTHER')
for n,end in [(1,2),(2,3),(3,4),(5,6),(6,7),(7,8)]:
 span('EU'+str(n),'eu-deminimis-browser.txt','EU2023/2831 Article'+str(n),rf'^Article\s+{n}$',rf'^Article\s+{end}$')
add('EU41','eu-deminimis-browser.txt','EU2023/2831 Article4(1), transparent aid',clean((S/'eu-deminimis-browser.txt').read_text()).split('Calculation of gross grant equivalent',1)[1].split('2.',1)[0].strip())
add('COUNCIL','council-register-browser.txt','Council treaty register observations','Provisional application as of 15/07/2026 - See Art. 336(2)')
from html.parser import HTMLParser
class Text(HTMLParser):
 def __init__(self):super().__init__();self.t=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ['script','style']:self.skip+=1
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip:self.t.append(s)
h=Text();h.feed((S/'deductions-announcement.html').read_text());txt=norm(' '.join(h.t));(S/'deductions-announcement-browserless.txt').write_text(txt)
spec['deductions-announcement-browserless.txt']=spec['deductions-announcement.html']
for q in ['15 July','12 October']:
 i=txt.index(q);a=max(0,txt.rfind('.',0,i)+1);b=txt.find('.',i)+1;add('ANN'+q.split()[0],'deductions-announcement-browserless.txt','Official announcement initial90day period',txt[a:b])
old=json.loads((K/'original-paragraphs.json').read_text());current=G.read_text();before=(K/'gi-transaction-tax-transition.before.txt').read_text();archive=(K/'preserved-consumption-controls.md').read_text();reconciled=json.loads((K/'reconciled-original-paragraphs.json').read_text())
def paras(t):
 body=t.split('---',2)[2].split('<!-- openaccountants-cta-block -->')[0];head='Title';out=[]
 for p in re.split(r'\n\s*\n',body.strip()):
  if p.startswith('#'):
   if p.startswith('## '):head=p[3:]
   elif p.startswith('### '):head=head.split(' > ')[0]+' > '+p[4:]
   continue
  out.append((head,p))
 return out
cur=paras(current);maps=[]
for x in old:
 hits=[(h,p) for h,p in cur if p==x['text']]
 if hits:dest='Guide: '+hits[0][0];target=x['text'];why='Full original paragraph unchanged'
 elif x['text'] in archive:dest='preserved-consumption-controls.md';target=x['text'];why='Full original production/cost/rate illustration and original block unchanged in supplement'
 else:
  assert x['id'] in reconciled,x['id'];target=reconciled[x['id']];hits=[(h,p) for h,p in cur if p==target];assert len(hits)==1,x['id'];dest='Guide: '+hits[0][0];why='Explicit source-date/provenance/aid-method/remaining-gap reconciliation; original snapshot retained'
 maps.append({k:v for k,v in x.items() if k!='text'}|{'destination':dest,'current_sha256':sha(target.encode()),'paragraph_exact':target==x['text'],'actual_old_anchor':norm(x['text'])[:180],'disposition':why})
groups=[('A1p1',[])]
refs={4:['Ap1','Ap66'],5:['Ap67'],6:['Ap103'],7:['Ap103','Ap104'],8:['Ap103','Ap104'],9:['Ap104'],10:['Ap104'],11:['Ap15','Ap16','T248','T336','T24','COUNCIL'],12:['Ap104','Ap105','T24','COUNCIL'],13:['Ap104','Ap105','T24','COUNCIL'],14:['Ap66','Ap67','T24','T336'],15:['Ap103','Ap104','Ap105','T24','COUNCIL'],16:['Ap105'],17:['Ap105','Ap106'],19:['Ap103','Ap104','Ap105'],22:['Ap104','Ap105','Ap106'],23:['Ap67','Ap68'],24:['Ap68'],26:['TR2','TR4'],27:['TR2','TR4'],28:['TR4','Ap68'],29:['Ap15','COUNCIL'],30:['Ap82','Ap83'],31:['Ap83'],32:['Ap83'],33:['Ap83','Ap84'],34:['Ap82','Ap83'],36:['Dp1','Dp2'],37:['Dp2','Dp5','ANN15','ANN12'],38:['Dp2','Dp3','Dp4'],39:['Dp2','Dp3'],40:['Dp2','Dp3','Dp4'],42:['Dp2','Dp3'],43:['Dp3','Dp4'],44:['Dp4'],45:['Dp5','Ap53','T18','EU2','EU3']}
newrefs={'N01':['URp2','URp3','URp4','URp5','GNintro'],'N02':['GN25'],'N03':['ARp3','GN1'],'N04':['ARp3','ARp4','GN1'],'N05':['ARp3','ARp4','GN25'],'N06':['IE2A','IE17','IE21','Ap97','TR2'],'N07':['URp16','URp17','URp18','URp19'],'N08':['URp2','URp19','URp20','URp21','URp22','URp23'],'N09':['URp8','URp9','URp19'],'N10':['IE2A','IE21','IE109','IE117'],'N11':['TR4','Ap68'],'N12':['Ap53','T18','EU3'],'N13':['T18','EU1','EU2','EU3','EU5'],'N14':['EU41','EU6','EU7','Dp5']}
rows=[];dest={m['id']:m['destination'] for m in maps}
for n,ps in refs.items():
 x=old[n-1];rows.append({'id':x['id'],'rule':reconciled.get(x['id'],x['text']),'original_assertion':x['text'],'guide_section':dest[x['id']],'proof_ids':ps,'read_on':'2026-10-28','derivation_note':'Synthetic examples establish arithmetic only; sourced provisions establish formulas/conditions. Earlier reviews preserved, not extended to new material.'})
for id,assertion in json.loads((K/'new-methods.json').read_text()).items():
 hits=[(h,p) for h,p in cur if p==assertion];assert len(hits)==1,id;rows.append({'id':'CON-'+id,'rule':assertion,'guide_section':'Guide: '+hits[0][0],'proof_ids':newrefs[id],'read_on':'2026-10-28'})
for r in rows:assert all(k in proofs for k in r['proof_ids']),(r['id'],r['proof_ids'])
nonrule=[1,2,3,18,20,25,35,46,47,48,49];controls=[21,41]
assert set(refs)|set(nonrule)|set(controls)==set(range(1,50))
marker='<!-- openaccountants-cta-block -->';assert current.count(marker)==1 and current[current.index(marker):]==before[before.index(marker):]
assert before==subprocess.check_output(['git','show','b98e7f01:skills/international/gibraltar/gi-transaction-tax-transition.md'],cwd=C).decode()
H=['Who this applies to','Rates, bands and thresholds','The base','Deadlines and filing','Penalties and interest','Cross-border points','Two worked examples that recompute','Ask the client first','Sources'];assert re.findall(r'^## (.+)$',current.split(marker)[0],re.M)==H
pat=re.compile(r'```oa-check\n.*?```',re.S);assert len(pat.findall(current))==2 and len(pat.findall(archive))==1 and all(b in current+archive for b in pat.findall(before))
a=yaml.safe_load(before.split('---',2)[1]);b=yaml.safe_load(current.split('---',2)[1]);mutable={'description','last_updated','version','sources'};assert {k:v for k,v in a.items() if k not in mutable}=={k:v for k,v in b.items() if k not in mutable}
result={'status':'Writer candidate only; independent country review pending','guide_version':'0.9','guide_sha256':sha(current.encode()),'rows':rows,'source_proofs':list(proofs.values()),'old_paragraph_map':maps,'nonrule_original_ids':[f'CON-P{i:03}' for i in nonrule],'original_control_ids':[f'CON-P{i:03}' for i in controls],'country_complete':False,'independent_acceptance':False,'published':False}
(K/'ledger.json').write_text(json.dumps(result,indent=2)+'\n')
esc=lambda s:s.replace('|','\\|').replace('\n',' ')
md=['# Gibraltar goods transaction tax: full figure/rule ledger\n','Writer v0.9, read 28 October 2026. Every original paragraph has a destination. All original arithmetic survives; the main Guide contains two original controls. Primary sources are English; exact quotations use at most45 words per snippet and preserve their own URLs/provisions. New material remains unreviewed and unpublished. Earlier review evidence is unchanged and does not accept this continuation.\n','## Rules and figures\n','| ID | Guide section and complete assertion | Exact original-language proof and official source | Read date |','|---|---|---|---|']
for r in rows:
 evidence=[]
 for id in r['proof_ids']:
  p=proofs[id];evidence.append(f'[{id}](#proof-{id.lower()}): {p["provision"]}; [official source]({p["url"]}); “{p["quotes"][0]}”')
 md.append('| '+' | '.join(esc(s) for s in [r['id'],r['guide_section']+': '+r['rule'],'; '.join(evidence),r['read_on']])+' |')
md+=['\n## Exact source proofs\n','Context is preserved across consecutive snippets; do not read a headline without its conditions. PDF hashes identify the cached official versions; browser text captures identify pages blocked by script fetches. Warehousing endpoint wording was also checked visually against complete physical page3 of both regulation and guidance.\n']
for p in proofs.values():
 md.append(f'### Proof {p["id"]}\n\n{p["provision"]}. [Official source]({p["url"]}). Read {p["read_on"]}. Source SHA256 `{p["source_sha256"]}`.\n')
 md.extend('> '+q+'\n' for q in p['quotes'])
md+=['## Complete old-topic destination table\n','All49 original full paragraphs/hashes are in [original-paragraphs.json](../original-paragraphs.json). The dated source statement, table provenance, aid evidence-limit and overall limit are explicitly reconciled. Original wording remains in the baseline snapshot. The full production/cost/rate illustrations remain in the supplement.\n','| Original ID | Original section | Original anchor | Current destination / preservation |','|---|---|---|---|']
for m in maps:md.append('| '+' | '.join(esc(s) for s in [m['id'],m['heading'],m['actual_old_anchor'],m['destination']+'; '+m['disposition']])+' |')
md+=['\n## Nonrule/control accounting\n',', '.join(result['nonrule_original_ids'])+' are scope, provenance, workflow or evidence-limit records. '+', '.join(result['original_control_ids'])+' are the two main executable controls; CON-P022 includes the original third control and conditional rate illustration, which remain in the supplement and also receive a source-backed derived-rule row. No original topic is silently removed.\n','No new professional attestation, live filing or country-complete finding. The Guide Sources line names all remaining uncertainties.\n']
(K/'ledgers/gi-transaction-tax-transition.md').write_text('\n'.join(md)+'\n')
audit={'rule_rows':len(rows),'inherited_rule_paragraphs':len(refs),'new_method_rows':len(newrefs),'proofs':len(proofs),'exact_quote_snippets':sum(len(p['quotes']) for p in proofs.values()),'old_paragraph_destinations':len(maps),'original_paragraphs_exact_across_guide_supplement':sum(m['paragraph_exact'] for m in maps),'explicit_reconciliations':len(reconciled),'original_controls_preserved':3,'main_controls':2,'canonical_sections':9,'CTA_exact':True,'protected_metadata_exact':True,'independent_acceptance':False,'published':False,'country_complete':False}
(K/'writer-complete-audit.json').write_text(json.dumps(audit,indent=2)+'\n');print(json.dumps(audit))
