from pathlib import Path
import json,hashlib,re,difflib,copy
W=Path(__file__).resolve().parent;P=W.parent/'germany-DE-R62-R70-payroll-writer-successor-2026-10-29';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');qs=json.loads((P/'source-quote-index.json').read_text());own=json.loads((W/'own-actual-read-quotes.json').read_text());qs.update(own);proofs=json.loads((W/'preservation-proof.json').read_text());invs=[]
def extra(t):
 ids=[]
 if 'wage tax certificate for 2026' in t.lower()or'Wage tax certificate for 2026'in t:ids+=['R88.certificate','R88.deadline','R88.weekend']
 if "Minijobber's ordinary own pension"in t or'**Minimum pension base' in t:ids+=['R89.minimum','R89.employershare','R89.calculation']
 if ('U1'in t and('tariff'in t or'statutory reimbursement'in t)):ids+=['R90.tariff']
 if '- Several insured jobs together' in t:ids+=['R91.multijob','R91.rounding']
 if '| No 25% (or farm 5%)' in t:ids+=['R92.flat']
 if any(k in t for k in ['**Tax classes**','| II |','| III |','| IV |','Extra child amounts for single parents','**Employees with limited tax liability']):ids+=['R93.classes','R93.missing']
 if '4. **Wage tax data.**'in t:ids+=['R93.missing']
 if '**Sick pay and the maternity top-up' in t or'**Maternity top-up.**'in t:ids+=['R94.maternity']
 if '| Annual wage tax adjustment' in t:ids+=['R95.adjust']
 if '| Employee copy of social-report' in t:ids+=['R96.copy']
 return list(dict.fromkeys(ids))
for s,proof in proofs.items():
 original=(W/'before'/f'{s}.md').read_text();after=(W/'after'/f'{s}.md').read_text();ls=after.split('\n');lm={}
 for tag,a,b,c,d in difflib.SequenceMatcher(a=original.split('\n'),b=ls,autojunk=False).get_opcodes():
  for n in range(a,b):lm[str(n+1)]={'start':c+1 if tag!='equal'else c+n-a+1,'end':d if tag!='equal'else c+n-a+1}
 sup=W/'support'/s;sup.mkdir(exist_ok=True);dump(sup/'line-map.json',lm);prior=json.loads((P/'support'/s/'rows.json').read_text());rows=[];covered=set()
 for q in prior:
  a,b=lm[str(q['native_LF'][0])]['start'],lm[str(q['native_LF'][1])]['end'];t='\n'.join(ls[a-1:b]);r=copy.deepcopy(q);r.update({'immediate_predecessor_id':q['id'],'immediate_predecessor_native_LF':q['native_LF'],'immediate_predecessor_wording':q['wording'],'native_LF':[a,b],'wording':t,'source_quote_ids':list(dict.fromkeys(q['source_quote_ids']+extra(t)))})
  if t!=q['wording']:r['disposition']='R88–96 bounded own-source selector/computation/operational successor; R62–70 gates retained'
  rows.append(r);covered.update(range(a,b+1))
 for tag,a,b,c,d in difflib.SequenceMatcher(a=original.split('\n'),b=ls,autojunk=False).get_opcodes():
  if tag not in ['replace','insert']:continue
  for n in range(c,d):
   if n+1 in covered or not ls[n].strip()or ls[n].startswith(('version:','last_updated:')):continue
   ids=extra(ls[n]);assert ids,(s,n+1,ls[n]);rows.append({'id':f'{len(rows)+1:03d}','prior_row_id':None,'immediate_predecessor_id':None,'native_LF':[n+1,n+1],'section':'R88–96 exact ordinary selector / labelled computation / duty','wording':ls[n],'source_quote_ids':ids,'disposition':'New finite own-source condition, not a new general payroll audit'})
 old=json.loads((P/'support'/s/'old-topic-destinations.json').read_text())
 def route(d,explicit):
  def m(x):
   a,b=int(x[1]),int(x[2])if x[2]else None
   if str(a)not in lm or(b and str(b)not in lm):return x[0]
   return('LF'if explicit else'')+str(lm[str(a)]['start'])+('–'+str(lm[str(b)]['end'])if b else('–'+str(lm[str(a)]['end'])if lm[str(a)]['end']!=lm[str(a)]['start']else''))
  return re.sub(r'LF\s*(\d+)(?:[–-](\d+))?'if explicit else r'(?<!\d)(\d+)(?:[–-](\d+))?(?!\d)',m,d)
 if isinstance(old,list):
  for q in old:q['R88_immediate_predecessor_destination']=q['destination'];q['destination']=route(q['destination'],True);q['R88_scope']='Actual R88–96 gates/one-source-derived calendar date qualify this same retained topic where relevant; R62–70 scope retained.'
  count=len(old)
 else:
  old['R88_immediate_predecessor_Guide_sha256']=old['Guide_sha256'];old['Guide_sha256']=proof['after_sha256'];count=0
  for key in ['pre_refresh_rows','current_main_rows']:
   for q in old[key]:count+=1;q['R88_immediate_predecessor_destination']=q['current_destination'];q['current_destination']=route(q['current_destination'],False);q['R88_scope']='Actual R88–96 same-method qualifications; earlier R62–70 conditions retained.'
 dump(sup/'rows.json',rows);dump(sup/'old-topic-destinations.json',old);esc=lambda t:str(t).replace('|','\\|').replace('\n','<br>');anchor=lambda k:k.lower().replace('.','-').replace('_','-')
 ledger=f'# {s}: R88–96 current successor ledger\n\nGuide `{proof["after_sha256"]}`, {proof["bytes"]}bytes. Immediate predecessor `{proof["before_sha256"]}`; exact prior ledger `{H(P/"ledgers"/(s+".md"))}` at `{P/"ledgers"/(s+".md")}`. All prior evidence/seals immutable. Writer correction, independent review pending. New own selected reads29October2026; earlier source quotations retain their original attributed writer/read dates. Exact clauses/officialURLs/hashes/native scopes in [source-quotes.md](../source-quotes.md) and source-quote-index.json.\n\n| ID | Section/nativeLF | Exact current wording | Source IDs/disposition |\n|---|---|---|---|\n'
 for q in rows:ledger+=f'| {q["id"]} | {esc(q["section"])} LF{q["native_LF"]} | {esc(q["wording"])} | '+(', '.join(f'[{k}](../source-quotes.md#{anchor(k)})'for k in q['source_quote_ids'])or'Preserved scope/routing/precise limitation; no new positive method.')+f'. {q["disposition"]} |\n'
 ledger+='\n## Complete old-topic destination table\n\nOriginal origins/wording are immutable; each immediate route retained separately.\n\n| Historical origin | Exact old wording or retained faithful opening | Current destination / finite qualification |\n|---|---|---|\n'
 if isinstance(old,list):
  for q in old:ledger+=f'| {q["ref"]} LF{q["old_lf"]} | {esc(q["wording"])} | {esc(q["destination"])} {q["R88_scope"]} |\n'
 else:
  for key in ['pre_refresh_rows','current_main_rows']:
   for q in old[key]:ledger+=f'| {key} LF{q["old_native_LF"]} / `{q["old_unit_sha256"]}` | {esc(q.get("old_exact_opening","Exact original native unit retained by comparator body/hash; no invented text."))} | {esc(q["current_destination"])} {esc(q["disposition"])} {q["R88_scope"]} |\n'
 (W/'ledgers'/f'{s}.md').write_text(ledger);invs.append({'slug':s,'Guide_path':proof['path'],'Guide_sha256':proof['after_sha256'],'bytes':proof['bytes'],'ledger_path':str(W/'ledgers'/f'{s}.md'),'ledger_sha256':H(W/'ledgers'/f'{s}.md'),'rows':len(rows),'immediate_prior_rows':len(prior),'old_topics':count,'prior_ledger_path':str(P/'ledgers'/f'{s}.md'),'prior_ledger_sha256':H(P/'ledgers'/f'{s}.md')})
needed=set(k for inv in invs for q in json.loads((W/'support'/inv['slug']/'rows.json').read_text())for k in q['source_quote_ids']);qs={k:q for k,q in qs.items()if k in needed};dump(W/'source-quote-index.json',qs);dump(W/'successor-inventory.json',invs);t='# R88–96 exact source quotations\n\nFifteen own selected operative scopes read29October2026. Earlier anchors retain prior writer actual read dates/provenance, explicitly reused. Source bodies stay exact/shared by reference. One earlier SGBX26source remains a web-tool observation JSON, not rawHTML.\n'
for id,q in qs.items():t+=f'\n<a id="{anchor(id)}"></a>\n## {id}\n\n{q.get("article",q.get("act_article"))}; {q.get("url",q.get("official_url"))}; read{q.get("read_on")}; nativeLF{q.get("native_LF")}. {q.get("actual_read_scope",q.get("provenance",""))}. Exactraw/readeridentities: source-quote-index.json.\n\n> '+q['exact_quote'].replace('\n','\n> ')+'\n'
(W/'source-quotes.md').write_text(t);print(json.dumps(invs,indent=2))
