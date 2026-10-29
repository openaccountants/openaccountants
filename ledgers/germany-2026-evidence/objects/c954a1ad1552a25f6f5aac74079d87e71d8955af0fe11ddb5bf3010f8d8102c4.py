from pathlib import Path
import json,hashlib,re,difflib,copy
W=Path(__file__).resolve().parent;O=W.parent;A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');proofs=json.loads((W/'preservation-proof.json').read_text());own=json.loads((W/'own-actual-read-quotes.json').read_text());qs=copy.deepcopy(own);invs=[]
for s,proof in proofs.items():
 base=A if s=='germany-payroll'else B;sup=base/'support'/s;before=(W/'before'/f'{s}.md').read_text();after=(W/'after'/f'{s}.md').read_text();ls=after.split('\n');lm={}
 for tag,a,b,c,d in difflib.SequenceMatcher(a=before.split('\n'),b=ls,autojunk=False).get_opcodes():
  for n in range(a,b):lm[str(n+1)]={'start':c+1 if tag!='equal'else c+n-a+1,'end':d if tag!='equal'else c+n-a+1}
 out=W/'support'/s;out.mkdir(exist_ok=True);dump(out/'line-map.json',lm)
 if s=='germany-payroll':
  originals=json.loads((sup/'claim-rows.json').read_text());originals=[{'id':n,'LF_start':q['lf'],'LF_end':q['lf'],'section':q['section'],'wording':q['wording'],'source_quote_ids':['A.'+v for v in q['anchors']]}for n,q in enumerate(originals,1)]
  for q in json.loads((sup/'actual-read-quotes.json').read_text()):
   id='A.'+q['id'];i=json.loads((A/'sources'/(q['source']+'.identity.json')).read_text());qs[id]={**i,**q,'id':id,'native_LF':[q['LF_start'],q['LF_end']],'provenance':'Exact earlier A writer selected quotation and actual read date reused by attribution; not a new whole-body reading claim.'}
 else:
  originals=json.loads((sup/'rows.json').read_text());originals=[{**q,'id':q['row'],'source_quote_ids':['B.'+v for v in q['source_quote_ids']]}for q in originals]
  bq=json.loads((B/'actual-read-quotes.json').read_text())
  for id in set(k[2:]for q in originals for k in q['source_quote_ids']):
   q=bq[id];qs['B.'+id]={**q,'id':'B.'+id,'url':q['official_url'],'provenance':'Exact earlier B writer selected quotation and actual read date reused by attribution; not a new whole-body reading claim.'}
 def more(t):
  ids=[]
  if '| Company car, home trips' in t:ids+=['R78.car']
  if '| Qualifying staff discount' in t or '**Qualifying staff discounts' in t:ids+=['R79.staffdiscount']
  if '| Lodging, unreduced' in t or '**Meals and lodging' in t:ids+=['R80.lodging']
  if '**§ 37b, 30%' in t:ids+=['R81.37b','R81.admin','R81.third']
  if any(k in t for k in ['| Subject to the precise gates','| Staff event:','- Staff events:','**§ 40(2), 25% and 15%']):ids+=['R82.40','R82.events']
  if '**Low-earner subsidy' in t:ids+=['R83.lowearner']
  if '| bAV: qualifying ordinary annual' in t or '**Tax.** Employer contributions' in t:ids+=['R84.63','R84.56']
  if '**Old contracts.**' in t or '| bAV: ordinary individual' in t:ids+=['R84.40b','R84.56','R84.63']
  if '- Employee shares in the employer' in t:ids+=['R85.shares']
  if '**Social insurance.** An A1' in t:ids+=['R86.A1']
  if '**Effect.** If the decision' in t:ids+=['R87.employment','R87.pension']
  if '**Managing directors.** If a director' in t:ids+=['R87.status','R87.late']
  return list(dict.fromkeys(ids))
 rows=[];covered=set()
 for q in originals:
  a,b=lm[str(q['LF_start'])]['start'],lm[str(q['LF_end'])]['end'];t='\n'.join(ls[a-1:b]);rows.append({'id':f'{len(rows)+1:03d}','prior_row_id':q['id'],'prior_native_LF':[q['LF_start'],q['LF_end']],'native_LF':[a,b],'section':q['section'],'wording':t,'source_quote_ids':list(dict.fromkeys(q['source_quote_ids']+more(t))),'disposition':'Exact original current unit, native coordinates rebound'if t==q['wording']else'Bounded R78–87 own-source condition / metadata successor'});covered.update(range(a,b+1))
 for tag,a,b,c,d in difflib.SequenceMatcher(a=before.split('\n'),b=ls,autojunk=False).get_opcodes():
  if tag not in ['replace','insert']:continue
  for n in range(c,d):
   if n+1 in covered or not ls[n].strip()or ls[n].startswith(('version:','last_updated:')):continue
   ids=more(ls[n]);assert ids,(s,n+1,ls[n]);rows.append({'id':f'{len(rows)+1:03d}','prior_row_id':None,'native_LF':[n+1,n+1],'section':'R78–87 actual ordinary condition / source-read statement','wording':ls[n],'source_quote_ids':ids,'disposition':'New finite source-supported sibling condition, not a new broad payroll audit'})
 oldpath=sup/('old-topics.json'if base==A else'old-topic-destinations.json');old=json.loads(oldpath.read_text())
 def sublf(d,explicit=False):
  def m(x):
   a,b=int(x[1]),int(x[2])if x[2]else None
   if str(a)not in lm or(b and str(b)not in lm):return x[0]
   return ('LF'if explicit else'')+str(lm[str(a)]['start'])+('–'+str(lm[str(b)]['end'])if b else('–'+str(lm[str(a)]['end'])if lm[str(a)]['end']!=lm[str(a)]['start']else''))
  return re.sub(r'LF\s*(\d+)(?:[–-](\d+))?'if explicit else r'(?<!\d)(\d+)(?:[–-](\d+))?(?!\d)',m,d)
 if base==A:
  for q in old:q['prior_sealed_destination']=q['destination'];q['destination']=sublf(q['destination'],True);q['bounded_successor_scope']='R78–87 actual exceptions qualify the retained ordinary rules where applicable; original identities/wording unchanged.'
  count=len(old)
 else:
  old['predecessor_Guide_sha256']=old['Guide_sha256'];old['Guide_sha256']=proof['after_sha256'];count=0
  for key in ['earliest_created_rows','current_main_rows']:
   for q in old[key]:
    count+=1;q['prior_sealed_destination']=q['current_destination'];q['current_destination']=sublf(q['current_destination']);q['bounded_successor_scope']='Same retained old topic; finite source exceptions add gates without removing the topic.'
 dump(out/'rows.json',rows);dump(out/'old-topic-destinations.json',old)
 esc=lambda t:str(t).replace('|','\\|').replace('\n','<br>');anchor=lambda t:t.lower().replace('.','-').replace('_','-')
 text=f'# {s}: DE-R78–87 successor figure/rule ledger\n\nGuide `{proof["after_sha256"]}`, {proof["bytes"]} bytes. Immutable predecessor Guide `{proof["before_sha256"]}` / ledger `{H(base/"ledgers"/(s+".md"))}` at `{base/"ledgers"/(s+".md")}`. Writer work, independent exact review pending. Own selected reads29October2026; earlier anchors retain actual original writer dates/provenance. Exact source quotations/officialURLs/read dates/raw-reader hashes are in [source-quotes.md](../source-quotes.md) and source-quote-index.json. Source bodies are shared by reference, never normalised.\n\n| ID | Section/nativeLF | Exact current wording | Source anchors / disposition |\n|---|---|---|---|\n'
 for q in rows:text+=f'| {q["id"]} | {esc(q["section"])} LF{q["native_LF"]} | {esc(q["wording"])} | '+(', '.join(f'[{k}](../source-quotes.md#{anchor(k)})'for k in q['source_quote_ids'])or'Preserved scope/routing/limitation; no new positive method.')+f'. {q["disposition"]} |\n'
 text+='\n## Complete old-topic destination table\n\nFull exact origin identities and wording are preserved in support/'+s+'/old-topic-destinations.json; prior routes retained separately.\n\n| Prior origin | Exact old topic or faithful retained opening | Current destination / finite scope |\n|---|---|---|\n'
 if base==A:
  for q in old:text+=f'| {q["ref"]} LF{q["old_lf"]} | {esc(q["wording"])} | {esc(q["destination"])} {esc(q["bounded_successor_scope"])} |\n'
 else:
  for key in ['earliest_created_rows','current_main_rows']:
   for q in old[key]:text+=f'| {key} LF{q["old_native_LF"]} / `{q["old_unit_sha256"]}` | {esc(q.get("old_exact_opening","Exact earlier native unit retained by comparator body/hash; no invented opening."))} | {esc(q["current_destination"])} {esc(q["disposition"])} {q["bounded_successor_scope"]} |\n'
 (W/'ledgers'/f'{s}.md').write_text(text);invs.append({'slug':s,'Guide_path':proof['path'],'Guide_sha256':proof['after_sha256'],'bytes':proof['bytes'],'ledger_path':str(W/'ledgers'/f'{s}.md'),'ledger_sha256':H(W/'ledgers'/f'{s}.md'),'rows':len(rows),'prior_rows':len(originals),'old_topics':count,'prior_ledger_path':str(base/'ledgers'/f'{s}.md'),'prior_ledger_sha256':H(base/'ledgers'/f'{s}.md')})
dump(W/'source-quote-index.json',qs);dump(W/'successor-inventory.json',invs);text='# DE-R78–87 actual source quotations\n\nOwn selected reads29October2026; A/B anchors retain exact prior writer read provenance. Read scope is not inferred from acquisition. DVKA is official administrative guidance, not Regulation text; two same-writer exact earlier selected law reads are explicitly bridged.\n'
for id,q in qs.items():text+=f'\n<a id="{anchor(id)}"></a>\n## {id}\n\n{q.get("article",q.get("act_article"))}; {q.get("url",q.get("official_url"))}; actual read {q.get("read_on")}; nativeLF{q.get("native_LF")}. {q.get("actual_read_scope",q.get("provenance",""))}. Exact raw/reader identities: source-quote-index.json.\n\n> '+q['exact_quote'].replace('\n','\n> ')+'\n'
(W/'source-quotes.md').write_text(text);print(json.dumps(invs,indent=2))
