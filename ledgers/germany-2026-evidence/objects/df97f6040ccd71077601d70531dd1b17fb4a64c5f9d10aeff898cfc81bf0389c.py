from pathlib import Path
import json,re,hashlib,difflib,copy
T=Path(__file__).resolve().parent;O=T.parent;P=O/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29';Q=O/'germany-DE-R09-corporate-rounding-writer-successor-2026-10-29';A=O/'germany-ledger-writer-2026-10-28';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();proof=json.loads((T/'preservation-proof.json').read_text());own=json.loads((T/'own-actual-read-quotes.json').read_text());allq=copy.deepcopy(own);inventory={}
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def e(x):return str(x).replace('|','\\|').replace('\n','<br>')
def anchor(x):return x.lower().replace('.','-').replace('_','-')
def source_link(id):
 if id in allq:return '../source-quotes.md#'+anchor(id)
 return str((Q if id.startswith('R09.') else P)/'source-quotes.md')+'#'+anchor(id)
def more(text):
 ids=[]
 if any(x in text for x in ['Test the shares.','**Which shares.**','**Recent free acquisition','Ordinary personal minimum','highest direct or indirect','Selected § 6(1)']):ids+=['R11.shares','R11.exit-incorporation','R11.separate-residence-test']
 if any(x in text for x in ['**6. Apportion','**Qualifying apportionment','For a stipulated ordinary corporation','For apportionment, obtain pay','| GewStG § 31(1)']):ids+=['R12.qualifying-wages']
 if any(x in text for x in ['Late payment surcharge','| AO § 240(3)']):ids+=['R13.grace','R13.method']
 if '- Under § 7g, the own-use alternative' in text:ids+=['R14.use-or-letting']
 if '**Who must file**' in text:ids+=['R15.filing']
 if '**Side income next to a job**' in text:ids+=['R16.employee-410']
 return ids
for slug,pr in proof.items():
 isexit=slug=='leaving-germany-exit-tax';iscorp=slug=='de-corporate-tax';isfree=slug=='de-einkommensteuer-freelancer';sup=(A/'support'/slug if isexit else P/'support'/slug if isfree else Q/'support');rowfile=sup/('claim-rows.json' if isexit else 'rows.json' if iscorp or isfree else 'trade-rows.json');oldfile=sup/('old-topics.json' if isexit else 'old-topic-destinations.json' if iscorp or isfree else 'trade-old-topic-destinations.json');rr=json.loads(rowfile.read_text());oldtopics=json.loads(oldfile.read_text());before=(T/'before'/f'{slug}.md').read_text();after=(T/'after'/f'{slug}.md').read_text();lines=after.split('\n');lm=json.loads((T/'support'/f'{slug}.line-map.json').read_text());rows=[];covered=set()
 if isexit:
  for x in json.loads((sup/'actual-read-quotes.json').read_text()):
   identity=json.loads((A/'sources'/(x['source']+'.identity.json')).read_text());id='EXIT.'+x['id'];allq[id]={**identity,**x,'id':id,'native_LF':[x['paragraph'],x['paragraph']],'read_on':x['actual_read_on'],'provenance':'Exact quotation/read date reused from sealed original A writer; not asserted as a new reading in this bounded phase. Reader Pxxx prefix is a locator.'}
 for i,row in enumerate(rr):
  oldlf=[row['lf'],row['lf']] if isexit else row['native_LF'];a,b=[lm[str(oldlf[0])]['start'],lm[str(oldlf[1])]['end']];text='\n'.join(lines[a-1:b]);ids=['EXIT.'+x for x in row['anchors']] if isexit else row['source_quote_ids'];ids=list(dict.fromkeys(ids+more(text)));rows.append({'id':f'{len(rows)+1:03d}','prior_row_id':row.get('id',i+1),'prior_native_LF':oldlf,'native_LF':[a,b],'section':row['section'],'wording':text,'source_quote_ids':ids,'disposition':'Bounded source/condition successor' if text!=row['wording'] else 'Exact predecessor current unit, native coordinates rebound'});covered.update(range(a,b+1))
 for tag,a,b,c,d in difflib.SequenceMatcher(a=before.split('\n'),b=lines,autojunk=False).get_opcodes():
  if tag not in ['insert','replace']:continue
  for i in range(c,d):
   if i+1 in covered or not lines[i].strip() or lines[i].startswith(('version:','last_updated:')):continue
   ids=more(lines[i]);assert ids,(slug,i+1,lines[i]);rows.append({'id':f'{len(rows)+1:03d}','prior_row_id':None,'prior_native_LF':None,'native_LF':[i+1,i+1],'section':'R11–17 new ordinary condition / computed separator / actual source read','wording':lines[i],'source_quote_ids':ids,'disposition':'New bounded ordinary correction; any fixture amounts explicitly stipulated/computed'});covered.add(i+1)
 def mapped(a,b=None):return str(lm[str(int(a))]['start'])+('–'+str(lm[str(int(b))]['end']) if b else '')
 def labelmap(text):return re.sub(r'\bLF\s*(\d+)(?:[–-](\d+))?',lambda m:'LF'+mapped(m[1],m[2]),text)
 topics=copy.deepcopy(oldtopics)
 if isinstance(topics,list):
  for row in topics:row['prior_sealed_destination']=row['destination'];row['destination']=labelmap(row['destination'])
 else:
  topics['prior_sealed_current_Guide_sha256']=topics['current_Guide_sha256'];topics['current_Guide_sha256']=pr['after_sha256']
  for kind in ['current_main_rows','pre_refresh_rows']:
   for row in topics[kind]:
    s=row['current_destination'];row['prior_sealed_current_destination']=s
    # Own-file bare ranges precede semicolon-qualified sibling locators. Never apply this file's shift to another Guide's LF.
    parts=s.split(';',1);parts[0]=re.sub(r'(\d+)(?:[–-](\d+))?',lambda m:mapped(m[1],m[2]),parts[0]);row['current_destination']=';'.join(parts)
    if not isfree and 'de-self-employed-income-tax' in s and 'de-corporate-tax' in s:
     # Directly checked actual current adviser-deadline rows; previous generic same-file shift was not a valid sibling coordinate rule.
     row['current_destination']=re.sub(r'de-self-employed-income-tax\d+','de-self-employed-income-tax LF121',row['current_destination']);row['current_destination']=re.sub(r'de-corporate-tax\d+','de-corporate-tax LF93',row['current_destination']);row['sibling_coordinate_precision']='Actual current self LF121/corporate LF93 were read; preserve prior sealed mechanical coordinates as history, not semantic evidence.'
 if isfree:
  import runpy
  topics=runpy.run_path(str(T/'R17-components.py'))['enrich'](topics)
 # Explicit semantic qualification for the corrected gift share and wage/filing topics.
 for row in (topics if isinstance(topics,list) else topics['current_main_rows']+topics['pre_refresh_rows']):
  oldtext=str(row.get('wording',row.get('old_exact_opening',''))).lower();notes=[]
  if isexit and ('1%' in oldtext or '1 %' in oldtext or 'test the shares' in oldtext):notes.append('R11: personal share threshold now has the labelled recent-free-acquisition/predecessor exception; residence aggregation remains separate.')
  if not isexit and 'wage' in oldtext:notes.append('R12: apportionment uses statutory31 qualifying wages before29 rounding/key, not uncapped all-pay.')
  if not isexit and ('grace' in oldtext or 'three day' in oldtext):notes.append('R13: grace excludes actual224(2)no1 payment methods; independent effective payment rules retained.')
  if notes:row['bounded_successor_scope']=' '.join(notes)
 d=T/'support'/slug;d.mkdir(exist_ok=True);dump(d/'rows.json',rows);dump(d/'old-topic-destinations.json',topics)
 oldledger=(A if isexit else P if isfree else Q)/'ledgers'/f'{slug}.md';text=f'# {slug}: R11–17 successor figure and rule ledger\n\nGuide `{pr["after_sha256"]}`, {pr["bytes"]} bytes. Predecessor Guide `{pr["before_sha256"]}`; immutable predecessor ledger `{oldledger}` / `{H(oldledger.read_bytes())}`. Own selected clauses were read on 29 October 2026; exact original-language source quotations/official URLs/read dates are in [source-quotes.md](../source-quotes.md). Other current source anchors retain their actual earlier writer provenance by reference to the immutable prior indexes. Writer successor, different independent review pending.\n\n| ID | Section / native LF | Exact current wording | Source anchors / disposition |\n|---|---|---|---|\n'
 for row in rows:
  refs=', '.join(f'[{x}]({source_link(x)})' for x in row['source_quote_ids']) or 'Preserved routing/presentation/express limitation/attribution; no new positive rule.';text+=f'| {row["id"]} | {e(row["section"])} LF{row["native_LF"]} | {e(row["wording"])} | {refs}. {e(row["disposition"])} |\n'
 text+='\n## Complete old-topic destinations\n\nEvery predecessor historical unit remains in support/'+slug+'/old-topic-destinations.json, including all earlier wording/hashes and destination history.\n\n| Historical reference / LF | Exact topic / opening | Current destination and bounded correction |\n|---|---|---|\n'
 if isinstance(topics,list):
  for row in topics:text+=f'| {row["ref"]} LF{row["old_lf"]} | {e(row["wording"])} | {e(row["destination"])} {e(row.get("bounded_successor_scope",""))} {e(row.get("R17_disposition",""))} |\n'
 else:
  for kind in ['current_main_rows','pre_refresh_rows']:
   for row in topics[kind]:text+=f'| {kind} LF{row["old_native_LF"]} / {row["old_unit_sha256"]} | {e(row.get("old_exact_opening","Exact original current-main body retained in its original writer preimage"))} | {e(row["current_destination"])}. {e(row["disposition"])} {e(row.get("bounded_successor_scope",""))} {e(row.get("R17_disposition",""))} |\n'
 (T/'ledgers'/f'{slug}.md').write_text(text);inventory[slug]={'Guide_path':pr['path'],'Guide_sha256':pr['after_sha256'],'bytes':pr['bytes'],'ledger_path':str(T/'ledgers'/f'{slug}.md'),'ledger_sha256':H(text.encode()),'current_rows':len(rows),'prior_current_rows':len(rr),'old_topics':len(topics) if isinstance(topics,list) else len(topics['current_main_rows'])+len(topics['pre_refresh_rows']),'prior_ledger':str(oldledger),'prior_ledger_sha256':H(oldledger.read_bytes())}
text='# R11–17 selected source quotations\n\nOwn new selected text was actually read on 29 October 2026. EXIT anchors are exact original A writer quotations with their original read date, reused with explicit attribution. Other unchanged P/Q anchors link to their immutable source indexes. No acquired source is claimed read merely because it is cached.\n'
for id,x in allq.items():
 u=x.get('url',x.get('official_url'));art=x.get('article',x.get('act_article'));date=x.get('read_on',x.get('actual_read_on'));text+=f'\n<a id="{anchor(id)}"></a>\n## {id}\n\n{art}; {u}; actual read: {date}; native LF {x.get("native_LF")}. {x.get("provenance","")} {x.get("qualification","")} Raw/reader paths and hashes: source-quote-index.json.\n\n> '+x['exact_quote'].replace('\n','\n> ')+'\n'
(T/'source-quotes.md').write_text(text);dump(T/'source-quote-index.json',allq);dump(T/'successor-inventory.json',inventory);print(json.dumps(inventory,indent=2))
