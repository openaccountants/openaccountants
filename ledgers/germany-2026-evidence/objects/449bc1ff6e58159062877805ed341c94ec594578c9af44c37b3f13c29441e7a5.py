from pathlib import Path
import json,hashlib,re,difflib,copy,runpy
W=Path(__file__).resolve().parent;O=W.parent;A=O/'germany-ledger-writer-2026-10-28';C=O/'germany-ledger-independent-review-2026-10-29';s='germany-tax-optimization';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');sup=A/'support'/s;before=(W/'before'/f'{s}.md').read_text();after=(W/'after'/f'{s}.md').read_text();ls=after.split('\n');bl=before.split('\n');lm={}
for tag,a,b,c,d in difflib.SequenceMatcher(a=bl,b=ls,autojunk=False).get_opcodes():
 for n in range(a,b):lm[str(n+1)]={'start':c+1 if tag!='equal'else c+n-a+1,'end':d if tag!='equal'else c+n-a+1}
(W/'support'/s).mkdir(exist_ok=True);dump(W/'support/line-map.json',lm);own=json.loads((W/'own-actual-read-quotes.json').read_text());qs=copy.deepcopy(own)
for q in json.loads((sup/'actual-read-quotes.json').read_text()):
 id='OPT.'+q['id'];i=json.loads((A/'sources'/(q['source']+'.identity.json')).read_text());qs[id]={**i,**q,'id':id,'native_LF':[q['LF_start'],q['LF_end']],'provenance':'Exact original A writer selected quotation and actual read date reused by explicit attribution; not a new own whole-source read.'}
def more(t):
 ids=[]
 if '| Filing deadline' in t:ids+=['R97-108.AO149-2','R97-108.AO108']
 if '| Meals: arrival/departure' in t:ids+=['R97-108.MEALS']
 if '| Commuting allowance' in t or'| Yearly cap where the own-car' in t:ids+=['R97-108.COMMUTE','R97-108.COMMUTEBRIDGE']
 if '| Home working day rate |'in t:ids+=['R97-108.DAY']
 if '| Yearly flat amount for a home office room' in t:ids+=['R97-108.ROOM']
 if '| Professional development |' in t:ids+=['R106.business-training']
 if any(k in t for k in ['| Immediate write-off,','| Pool,','| Immediate write-off:','| Pool: cost','The alternative is the logbook method.']):ids+=['R97-108.E6-2','R97-108.POOL','OPT.VATCOST']
 if '| Defer invoicing' in t:ids+=['R97-108.VATSUPPLY','R97-108.VATCASH']
 if '| Kleinunternehmerregelung' in t:ids+=['OPT.KU']
 if '| Ist-Versteuerung' in t:ids+=['R97-108.VATCASH']
 if '| Input VAT timing' in t:ids+=['R97-108.INPUTRULE','R97-108.INPUTVAT','R97-108.GIFTS']
 if '| Reverse charge for EU services' in t:ids+=['R26.planning-bridge','OPT.RCDEBTOR','OPT.VATRECIPIENT']
 if '| Intra-year offset' in t or'| Deferral models' in t:ids+=['R97-108.MODELLOSS']
 if '| Cap 2026, jointly assessed spouses' in t or t.startswith('For an ordinary employee with qualifying pension contributions'):ids+=['R97-108.PENSIONELIG','R97-108.PENSIONCAP']
 if t.startswith('This Guide presents planning mechanisms'):ids+=['R97-108.TARIFF','R97-108.PENSIONELIG','R97-108.PENSIONCAP','R97-108.E6-2','R97-108.POOL']
 return list(dict.fromkeys(ids))
original=json.loads((sup/'claim-rows.json').read_text());rows=[];covered=set()
for n,q in enumerate(original,1):
 a,b=lm[str(q['lf'])]['start'],lm[str(q['lf'])]['end'];t='\n'.join(ls[a-1:b]);ids=list(dict.fromkeys(['OPT.'+k for k in q['anchors']]+more(t)));r={'id':f'{n:03d}','prior_row_id':n,'prior_native_LF':[q['lf'],q['lf']],'native_LF':[a,b],'section':q['section'],'wording':t,'source_quote_ids':ids,'disposition':'Exact original current unit; native coordinates rebound'if t==q['wording']else'R97–108 bounded same-method source qualification/correction; old claim retained as history'}
 if '| Professional development |'in t:r['source_anchor_qualification']={'OPT.TRAINING':'Definition/employee-companion reference only. Do not import its employment exception into business4(9). Actual business eligibility anchor R106.business-training governs.'}
 rows.append(r);covered.update(range(a,b+1))
for tag,a,b,c,d in difflib.SequenceMatcher(a=bl,b=ls,autojunk=False).get_opcodes():
 if tag not in ['replace','insert']:continue
 for n in range(c,d):
  if n+1 in covered or not ls[n].strip()or ls[n].startswith(('version:','last_updated:')):continue
  ids=more(ls[n]);assert ids,(n+1,ls[n]);rows.append({'id':f'{len(rows)+1:03d}','prior_row_id':None,'native_LF':[n+1,n+1],'section':'R105 actual employee pension contribution/cap adjustment','wording':ls[n],'source_quote_ids':ids,'disposition':'New finite sourced ordinary adjustment / labelled separating computation'})
M=runpy.run_path(str(W/'pre-refresh-routes.py'))['MAP'];old=json.loads((sup/'old-topics.json').read_text());pre=[q for q in old if q['ref'].startswith('2884')];assert len(pre)==134;pi=0;trace=[]
def mapped(a,b):return lm[str(a)]['start'],lm[str(b)]['end']
def refs(a,b):return list(dict.fromkeys(k for q in rows if not(q['native_LF'][1]<a or q['native_LF'][0]>b)for k in q['source_quote_ids']))
for q in old:
 q['prior_sealed_destination']=q['destination']
 if q['ref'].startswith('2884'):
  pi+=1;m=M[pi];components=[]
  for a,b in m['before_current_LFs']:
   assert 1<=a<=b<=len(bl);x,y=mapped(a,b);t='\n'.join(ls[x-1:y]);components.append({'before_current_native_LF':[a,b],'before_actual_clause':'\n'.join(bl[a-1:b]),'current_native_LF':[x,y],'current_actual_clause':t,'current_clause_sha256':hashlib.sha256(t.encode()).hexdigest(),'source_quote_ids':refs(x,y)})
  q['destination']='; '.join('LF'+str(c['current_native_LF'][0])+('–'+str(c['current_native_LF'][1])if c['current_native_LF'][1]!=c['current_native_LF'][0]else'')for c in components)+'. '+m['semantic_disposition'];q['semantic_disposition']=m['semantic_disposition'];q['component_destinations']=components;q['pre_refresh_index']=pi;trace.append({'pre_refresh_index':pi,'old_native_LF':q['old_lf'],'old_wording_sha256':hashlib.sha256(q['wording'].encode()).hexdigest(),'components':components,'disposition':m['semantic_disposition']})
 else:
  # Keep321 main origins, rebind each correct immediate predecessor destination; changed claims explicitly qualified.
  def m(x):
   a,b=int(x[1]),int(x[2])if x[2]else None
   if str(a)not in lm or(b and str(b)not in lm):return x[0]
   x,y=mapped(a,b or a);return'LF'+str(x)+('–'+str(y)if y!=x else'')
  q['destination']=re.sub(r'LF\s*(\d+)(?:[–-](\d+))?',m,q['destination']);q['bounded_successor_scope']='Same current-main origin retained; R97–108 conditions/source-derived date/actual tax scope qualify matching claims. Historical wording remains exact, not automatic law.'
  # Explicitly stop asserting word-for-word retention when an old claim changed.
  if q['wording']not in after:q['destination']=q['destination'].replace('Exactwordingretained','Historical wording preserved in exact comparator; current same-topic correction at')
assert pi==134;dump(W/'support'/s/'rows.json',rows);dump(W/'support'/s/'old-topic-destinations.json',old);dump(W/'pre-refresh-route-index.json',trace)
# Exact attribution of the prior independently verified455Gitold-origin identities, not a new writerGitquery.
p=C/'germany-tax-optimization-old-origin-check.json';(W/'attributed-prior-old-origin-check.json').write_bytes(p.read_bytes());dump(W/'old-origin-review-reference.json',{'source':str(p),'sha256':H(p),'copy_sha256':H(W/'attributed-prior-old-origin-check.json'),'provenance':'C independent reviewer actual realGitold-origin verification reused by attribution; writer read every134pre-refresh wording/destination and selected actual current target clauses. Not a new writerGitobjectquery.'})
esc=lambda t:str(t).replace('|','\\|').replace('\n','<br>');anchor=lambda k:k.lower().replace('.','-').replace('_','-');proof=json.loads((W/'preservation-proof.json').read_text());t=f'# {s}: R97–108 successor ledger\n\nGuide `{proof["after_sha256"]}`, {proof["bytes"]}bytes; predecessor Guide `{proof["before_sha256"]}` / ledger `{H(A/"ledgers"/(s+".md"))}` at `{A/"ledgers"/(s+".md")}`. Writer correction, different independent review pending. Exact original-language clauses/officialURLs/read dates/raw-reader hashes in [source-quotes.md](../source-quotes.md) and source-quote-index.json. Nineteen own selected operative quotations read29October2026 plus exact earlier own R26reading bridge; original A quotations retain attributed actual prior read dates. No acquisition-as-reading claim.\n\n| ID | Section/nativeLF | Exact current wording | Source IDs/disposition |\n|---|---|---|---|\n'
for q in rows:t+=f'| {q["id"]} | {esc(q["section"])} LF{q["native_LF"]} | {esc(q["wording"])} | '+(', '.join(f'[{k}](../source-quotes.md#{anchor(k)})'for k in q['source_quote_ids'])or'Preserved scope/routing/precise limitation; no new positive rule.')+f'. {esc(q["disposition"])} {esc(q.get("source_anchor_qualification",""))} |\n'
t+='\n## Complete old-topic destinations\n\nAll455origins/fullhistoricalwording retained. Every134pre-refresh route is individually authored against actual clause components and source anchors, with exact earlierroute retained separately. The321currentmainorigins retain correct source-topic routes with coordinates rebound; literal changes are explicit corrections. Exact component text/native/hash/sourceIDs: pre-refresh-route-index.json. Unsupported historical claims remain labelled archives, not promoted as law.\n\n| Exact old origin | Exact historical wording | Current component destination / correction |\n|---|---|---|\n'
for q in old:t+=f'| {q["ref"]} LF{q["old_lf"]} | {esc(q["wording"])} | {esc(q["destination"])} {esc(q.get("bounded_successor_scope",""))} |\n'
(W/'ledgers'/f'{s}.md').write_text(t);dump(W/'source-quote-index.json',qs);text='# R97–108 source quotations\n\nNineteen own selected operative scopes read29October2026 and one genuine same-writer earlier R26bridge. Original A quotes/actual dates reused by explicit attribution. Full identities/raw-reader paths/hashes: source-quote-index.json. R106 actual business4(9) governs; prior employee9(6)source is definition/companionreference only.\n'
for id,q in qs.items():text+=f'\n<a id="{anchor(id)}"></a>\n## {id}\n\n{q.get("article",q.get("act_article"))}; {q.get("url",q.get("official_url"))}; read{q.get("read_on")}; nativeLF{q.get("native_LF")}. {q.get("actual_read_scope",q.get("provenance",""))}\n\n> '+q['exact_quote'].replace('\n','\n> ')+'\n'
(W/'source-quotes.md').write_text(text);inv={'slug':s,'Guide_path':proof['path'],'Guide_sha256':proof['after_sha256'],'bytes':proof['bytes'],'ledger_path':str(W/'ledgers'/f'{s}.md'),'ledger_sha256':H(W/'ledgers'/f'{s}.md'),'rows':len(rows),'prior_rows':len(original),'old_topics':len(old),'pre_refresh_semantic_routes':len(trace),'current_main_origins':len(old)-len(trace)};dump(W/'successor-inventory.json',inv);print(json.dumps(inv,indent=2))
