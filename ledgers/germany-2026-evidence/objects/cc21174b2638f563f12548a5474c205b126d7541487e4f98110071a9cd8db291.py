from pathlib import Path
import json,re,hashlib,difflib,copy
P=Path(__file__).resolve().parent;O=P.parent;A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();proof=json.loads((P/'preservation-proof.json').read_text());own=json.loads((P/'own-actual-read-quotes.json').read_text());allq=copy.deepcopy(own);summary={}
def dump(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def esc(s):return str(s).replace('|','\\|').replace('\n','<br>')
def anchor(s):return s.lower().replace('.','-').replace('_','-')
def oq(id):return id in own
for slug,pr in proof.items():
 prev=(P/'before'/f'{slug}.md').read_text();cur=(P/'after'/f'{slug}.md').read_text();cl=cur.split('\n');lm=json.loads((P/'support'/f'{slug}.line-map.json').read_text());b=slug in ['de-einkommensteuer-freelancer','de-trade-tax'];base=B if b else A;sup=base/'support'/slug;newrows=[];coverage=set();qq={}
 if b:
  original=json.loads((sup/'rows.json').read_text());glob=json.loads((B/'actual-read-quotes.json').read_text())
  for row in original:
   for id in row['source_quote_ids']:qq['B.'+id]={**glob[id],'id':'B.'+id,'original_quote_id':id,'provenance':'Exact selected quotation reused from sealed original B writer; unchanged legal scope not newly read in this bounded repair.'}
  rr=[{'old_id':row['row'],'lf':row['LF_start'],'end':row['LF_end'],'section':row['section'],'wording':row['wording'],'anchors':['B.'+i for i in row['source_quote_ids']],'kind':row['classification']} for row in original]
 else:
  original=json.loads((sup/'claim-rows.json').read_text());qoriginal=json.loads((sup/'actual-read-quotes.json').read_text());qq={slug+'.'+x['id']:{**x,'id':slug+'.'+x['id'],'original_quote_id':x['id'],'provenance':'Exact selected quotation reused from sealed original A writer; unchanged legal scope not newly read in this bounded repair.'} for x in qoriginal};rr=[{'old_id':i+1,'lf':row['lf'],'end':row['lf'],'section':row['section'],'wording':row['wording'],'anchors':[slug+'.'+x for x in row['anchors']],'kind':row['kind']} for i,row in enumerate(original)]
 def extra(s,lf):
  ids=[]
  if any(x in s for x in ['**Cars.**','**Business-car commuting','**Commuting**','0.0003','first registration','list price, 20','commuting costs of EUR 1,000']):ids+=['R01.business-car','R01.allowance']
  if any(x in s for x in ['Meals on business trips','**Meals**','Meals: arrival']):ids+=['R02.meals','R02.meal-incorporation']
  if slug=='de-employee-income-tax':
   if lf in [86,109,198]:ids+=['R03.soli-children']
   if lf==100:ids+=['R03.employee-expense']
   if lf==50:ids+=['R04.crossborder-mandatory']
  if any(x in s for x in ['**Abfärbung','**Separable own commercial','net receipts','commercial receipts','dual-gate','de minimis','separable commercial activity']):ids+=['R05.statute','R05.BFH-separability','R05.BFH-thresholds','R05.BMF-current','R05.BFH-2022']
  if '**Step 4: losses of limited partners' in s:ids+=['R06.liability']
  if '**Step 5: the retained-profits option' in s:ids+=['R06.retained']
  if s.startswith('| EStG § 4(5) nos. 5'):ids+=['R01.business-car','R02.meal-incorporation']
  if s.startswith('| EStG § 9(1) no. 4'):ids+=['R01.allowance','R02.meals']
  if s.startswith('| BMF EStH'):ids+=['R05.BMF-current']
  if s.startswith('| BFH VIII'):ids+=['R05.BFH-separability','R05.BFH-thresholds']
  if s.startswith('| BFH IV'):ids+=['R05.BFH-2022']
  if slug=='de-corporate-tax':
   if any(x in s for x in ['Interest barrier','Interest expense is deductible','The rule does not apply when net interest','**What are interest expense','| EStG § 4h']):ids+=['R07.interest','R07.corporate-income']
   if 'A commercial partnership pays trade tax' in s:ids+=['R07.commercial']
   if any(x in s for x in ['Foreign corporate recipient within','**For outbound royalties','| EStG §§ 44a']):ids+=['R08.refund-population','R08.foreign-corporation','R08.anti-abuse','R08.procedure','R08.royalty-extent']
   if '**Royalties.**' in s:ids+=['R08.royalty-extent','R08.procedure']
  return ids
 for row in rr:
  start=lm[str(row['lf'])]['start'];end=lm[str(row['end'])]['end'];word='\n'.join(cl[start-1:end]);ids=row['anchors']+extra(word,row['lf']);changed=word!=row['wording']
  if slug=='de-employee-income-tax':
   if any(x.endswith('.HCEILING') for x in ids):ids+=['R03.BMG-health-2026','R03.BMG-care-2026'];changed=True
   if any(x.endswith('.SoliBase') for x in ids):ids+=['R03.soli-children'];changed=True
   if row['lf']==100:ids=[x for x in ids if not x.endswith('.BUSCOST')]
  ids=list(dict.fromkeys(ids));newrows.append({'id':f'{len(newrows)+1:03d}','predecessor_row_id':row['old_id'],'predecessor_native_LF':[row['lf'],row['end']],'native_LF':[start,end],'section':row['section'],'wording':word,'source_quote_ids':ids,'classification':row['kind'],'disposition':'Bounded DE-R01–08 wording/evidence successor' if changed else 'Exact original current unit; only native LF rebound'});coverage.update(range(start,end+1))
 # Add truly new nonempty lines from insertions not already absorbed in changed original units.
 sm=difflib.SequenceMatcher(a=prev.split('\n'),b=cl,autojunk=False)
 for tag,a,z,c,d in sm.get_opcodes():
  if tag not in ['insert','replace']:continue
  for i in range(c,d):
   if i+1 in coverage or not cl[i].strip():continue
   ids=extra(cl[i],i+1)
   if not ids and cl[i].startswith('- Car method'):ids=['R01.business-car','R01.allowance']
   if not ids and cl[i].startswith('version:'):continue
   if not ids and cl[i].startswith('last_updated:'):continue
   assert ids,(slug,i+1,cl[i]);newrows.append({'id':f'{len(newrows)+1:03d}','predecessor_row_id':None,'predecessor_native_LF':None,'native_LF':[i+1,i+1],'section':'DE-R01–08 added ordinary method / intake / selected source','wording':cl[i],'source_quote_ids':ids,'classification':'Computed stipulated example or rule derived from exact stated sources; intake/source rows are not separate statutory amounts.','disposition':'New bounded review-finding correction'});coverage.add(i+1)
 if not b:
  for id,x in qq.items():
   identity=json.loads((A/'sources'/(x['source']+'.identity.json')).read_text())
   assert identity['raw_sha256']==x['raw_sha256'] and identity['reader_sha256']==x['reader_sha256']
   x['raw_path']=identity['raw_path'];x['reader_path']=identity['reader_path']
 allq.update(qq)
 for row in newrows:
  for id in row['source_quote_ids']:assert id in allq,(slug,id)
 # Map original old topics through exact predecessor-current coordinate mapping; retain both strings.
 def maprange(a,z=None):return f"{lm[str(int(a))]['start']}"+(f"–{lm[str(int(z))]['end']}" if z is not None else '')
 def maptext(s):
  return re.sub(r'current\s*LF\s*(\d+)(?:[–−-](\d+))?',lambda m:'current LF'+maprange(m[1],m[2]),s)
 oldpath=sup/('old-topic-destinations.json' if b else 'old-topics.json');old=json.loads(oldpath.read_text());oldnew=copy.deepcopy(old)
 if b:
  oldnew['predecessor_current_Guide_sha256']=oldnew['current_Guide_sha256'];oldnew['current_Guide_sha256']=pr['after_sha256']
  for kind in ['current_main_rows','pre_refresh_rows']:
   for row in oldnew[kind]:
    s=row['current_destination'];row['predecessor_current_destination']=s
    def conv(m):
     lo=int(m[1]);hi=int(m[2]) if m[2] else None
     if str(lo) in lm and (hi is None or str(hi) in lm):return maprange(lo,hi)
     return m[0]
    row['current_destination']=re.sub(r'(?<!\d)(\d+)(?:[–-](\d+))?(?!\d)',conv,s)
    row['predecessor_disposition']=row['disposition']; row['disposition']='Historical topic preserved at the rebound successor destination; the original historical rationale is retained separately. DE-R01–08 corrections govern any affected universal simplification.'; row['successor_disposition']='Destination coordinates rebound mechanically; exact old/new current claims are in canonical rows and operations.'
 else:
  for row in oldnew:row['predecessor_destination']=row['destination'];row['destination']=maptext(row['destination'])
 # Explicit semantic successor distinctions for material historical topics, no revival of incorrect generalizations.
 for row in (oldnew if isinstance(oldnew,list) else oldnew['current_main_rows']+oldnew['pre_refresh_rows']):
  text=str(row.get('wording',row.get('old_exact_opening',''))).lower();notes=[]
  if any(t in text for t in ['commut','fahrten','1%','1 %','car use']):notes.append('DE-R01: business-car commuting positive-difference and actual/logbook method supplied in current Cars/Commuting section; separate private-use method retained.')
  if any(t in text for t in ['meal','verpflegung']):notes.append('DE-R02: arrival/departure requires qualifying overnight; independent non-overnight >8h and 24h branches retained.')
  if any(t in text for t in ['abfärb','abfarb','any commercial','commercial side']):notes.append('DE-R05: universal own-activity contamination corrected to separable dual net-receipt gates; participation limb separate.')
  if 'withdraw' in text or 'retained-profit' in text or '§ 34a' in text:notes.append('DE-R06: statutory tax/Soli withdrawal priority/exclusion and qualifying outside-liability exception preserved in summary; detailed-regime referral retained.')
  if notes:row['bounded_semantic_successor_note']=' '.join(notes)
 d=P/'support'/slug;d.mkdir(exist_ok=True);dump(d/'rows.json',newrows);dump(d/'old-topic-destinations.json',oldnew)
 used=sorted({i for row in newrows for i in row['source_quote_ids']});text=f'# {slug}: successor figure and rule ledger\n\nGuide SHA256 `{pr["after_sha256"]}`; {pr["bytes"]} bytes; actual scoped writer reads 2026-10-29. Predecessor Guide `{pr["before_sha256"]}` and immutable original full ledger at `{base/"ledgers"/(slug+".md")}`. This ledger reuses exact original selected quotations for unchanged claims, with attribution; own selected new reads and administrative/law distinctions are explicit in [source-quotes.md](../source-quotes.md). Writer successor, pending different independent review.\n\nEvery original current unit is retained/rebound below; new ordinary corrections add their own units. Original topic maps remain complete in `../support/{slug}/old-topic-destinations.json`, alongside the exact native line map. No earlier review verdict is inferred to cover changed bytes.\n\n| ID | Section / native LF | Exact current wording | Sources / classification |\n|---|---|---|---|\n'
 for row in newrows:
  ids=', '.join(f'[{id}](../source-quotes.md#{anchor(id)})' for id in row['source_quote_ids']) or 'Routing / presentation / express reservation / protected attribution, no new positive legal rule.'
  text+=f'| {row["id"]} | {esc(row["section"])}; LF{row["native_LF"][0]}–{row["native_LF"][1]} | {esc(row["wording"])} | {ids}. {esc(row["disposition"])} |\n'
 text+='\n## Complete old-topic destinations\n\nThe exact original old-source units, hashes/wording and all predecessor destinations are preserved; successor coordinates are derived mechanically from the pinned native line map. Corrected universal statements are historical claims, not reinstated law.\n\n| Old reference / LF | Exact old topic / opening | Current destination and disposition |\n|---|---|---|\n'
 if isinstance(oldnew,list):
  for row in oldnew:text+=f'| {row["ref"]} LF{row["old_lf"]} | {esc(row["wording"])} | {esc(row["destination"])} {esc(row.get("bounded_semantic_successor_note",""))} |\n'
 else:
  for kind in ['current_main_rows','pre_refresh_rows']:
   for row in oldnew[kind]:text+=f'| {kind} LF{row["old_native_LF"]}; {row["old_unit_sha256"]} | {esc(row.get("old_exact_opening","Exact original current-main unit, retained in original support/preimage"))} | {esc(row["current_destination"])}. {esc(row["disposition"])} {esc(row.get("bounded_semantic_successor_note",""))} |\n'
 (P/'ledgers'/f'{slug}.md').write_text(text)
 summary[slug]={'Guide_sha256':pr['after_sha256'],'ledger_path':str(P/'ledgers'/f'{slug}.md'),'ledger_sha256':H(text.encode()),'current_rows':len(newrows),'original_current_rows':len(original),'old_topics':len(oldnew) if isinstance(oldnew,list) else sum(len(oldnew[k]) for k in ['current_main_rows','pre_refresh_rows']),'used_quote_ids':used,'original_ledger_sha256':H((base/'ledgers'/f'{slug}.md').read_bytes()),'original_support':str(sup)}
# Shared reusable quote index; no duplicated official raw body.
dump(P/'source-quote-index.json',allq);used=sorted({id for x in summary.values() for id in x['used_quote_ids']});txt='# Successor selected source quotations\n\nOwn new/expanded clauses were actually read on 29 October 2026. Other anchors preserve their original writer read date and exact quotation with attribution; reuse is not claimed as a new full-law read. All raw bodies remain at their exact retained paths. Original writer seals are immutable. Native LF means split on LF, not form-feed splitlines.\n'
for id in used:
 q=allq[id];article=q.get('article',q.get('act_article'));u=q.get('url',q.get('official_url'));date=q.get('read_on',q.get('actual_read_date',q.get('read_date','Original recorded writer date; see exact record')));native=q.get('native_LF',[q.get('LF_start'),q.get('LF_end')]);txt+=f'\n<a id="{anchor(id)}"></a>\n## {id}\n\n{article}; {u}; actual read date: {date}. Native/source range: {native}. {q.get("provenance","")} {q.get("qualification","")}\n\n> '+q['exact_quote'].replace('\n','\n> ')+'\n'
 if id in own:txt+='\nRaw/reader identities and paths: `own-actual-read-quotes.json`.\n'
 else:txt+='\nRaw/reader identities and unchanged original provenance: `source-quote-index.json`.\n'
(P/'source-quotes.md').write_text(txt);dump(P/'successor-inventory.json',summary);print(json.dumps({k:{x:y for x,y in v.items() if x not in ['used_quote_ids','original_support']} for k,v in summary.items()},indent=2))
