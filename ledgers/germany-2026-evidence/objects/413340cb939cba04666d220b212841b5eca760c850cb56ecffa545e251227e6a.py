from pathlib import Path
import json,hashlib,copy,difflib,re
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-DE-R26-R31-advance-VAT-writer-successor-2026-10-29');B=W.parent/'germany-ledger-writer-B-2026-10-29';s='germany-vat-return';sup=B/'support'/s;H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');proof=json.loads((W/'preservation-proof.json').read_text());before=(W/'before'/f'{s}.md').read_text();after=(W/'after'/f'{s}.md').read_text();lines=after.split('\n');lm=json.loads((W/'support/line-map.json').read_text());qs=json.loads((W/'own-actual-read-quotes.json').read_text());original=json.loads((sup/'rows.json').read_text());oldq=json.loads((B/'actual-read-quotes.json').read_text());used=set(k for r in original for k in r['source_quote_ids'])
for id in used:qs['OLD.'+id]={**oldq[id],'url':oldq[id]['official_url'],'provenance':'Exact prior B-writer quotation/actual read date reused, not a new whole-source reading claim. R31 supplies the extended operative anchor for the prior partial PR.latefilingformula.'}
def more(t):
 ids=[]
 if '**Place of supply first' in t or'7. Actual service type'in t or'| UStG § 3a(2)'in t:ids+=['R26.place']
 if '| Qualifying solar'in t or'**Solar at 0%'in t or'7. Actual service type'in t or'| UStG § 3a(2)'in t:ids+=['R27.solar']
 if '**What the 7%'in t or'7. Actual service type'in t or'| UStG § 3a(2)'in t:ids+=['R27.water']
 if '| Bank fees'in t or'7. Actual service type'in t or'| UStG § 3a(2)'in t:ids+=['R28.finance']
 if '- **Goods.**'in t or'7. Actual service type'in t or'| UStG § 3a(2)'in t:ids+=['R29.exemption-ZM','R29.ICS','R29.presumption']
 if '- foreign VAT wrongly'in t or'7. Actual service type'in t or'| AO § 152(8)'in t:ids+=['R30.foreign-input']
 if 'special prepayment' in t.lower() and('formula'in t.lower()or'late'in t.lower())or'| AO § 152(8)'in t:ids+=['R31.late-filing-exclusion']
 return ids
rows=[];covered=set()
for i,r in enumerate(original,1):
 a,b=lm[str(r['LF_start'])]['start'],lm[str(r['LF_end'])]['end'];t='\n'.join(lines[a-1:b]);ids=list(dict.fromkeys(['OLD.'+x for x in r['source_quote_ids']]+more(t)));rows.append({'id':f'{i:03d}','prior_row_id':r['row'],'prior_native_LF':[r['LF_start'],r['LF_end']],'native_LF':[a,b],'section':r['section'],'wording':t,'source_quote_ids':ids,'disposition':'Exact prior current wording with native coordinates rebound'if t==r['wording']else'R26–31 bounded operative condition successor'});covered.update(range(a,b+1))
# The correctly stated formula exclusion must explicitly route to the newly complete operative anchor.
assert 'R31.late-filing-exclusion'in next(x for x in rows if x['prior_row_id']==101)['source_quote_ids']
for tag,a,b,c,d in difflib.SequenceMatcher(a=before.split('\n'),b=lines,autojunk=False).get_opcodes():
 if tag not in['replace','insert']:continue
 for i in range(c,d):
  if i+1 in covered or not lines[i].strip()or lines[i].startswith(('version:','last_updated:')):continue
  ids=more(lines[i]);assert ids,(i+1,lines[i]);rows.append({'id':f'{len(rows)+1:03d}','prior_row_id':None,'native_LF':[i+1,i+1],'section':'R26–31 sourced condition/intake/actual selected read','wording':lines[i],'source_quote_ids':ids,'disposition':'New bounded source-backed correction; any fixture values explicitly stipulated/computed'});covered.add(i+1)
ot=copy.deepcopy(json.loads((sup/'old-topic-destinations.json').read_text()));ot['prior_Guide_sha256']=ot['Guide_sha256'];ot['Guide_sha256']=proof['after_sha256']
def mapmatch(m):
 a=int(m[1]);b=int(m[2])if m[2]else None
 if str(a)not in lm or(b and str(b)not in lm):raise Exception(m.group())
 return str(lm[str(a)]['start'])+('–'+str(lm[str(b)]['end'])if b else('–'+str(lm[str(a)]['end'])if lm[str(a)]['start']!=lm[str(a)]['end']else''))
for kind in['pre_refresh_rows','current_main_rows']:
 for r in ot[kind]:
  d=r['current_destination'];r['prior_sealed_current_destination']=d;parts=d.split(';');parts=[p if p.strip().startswith('companion')else re.sub(r'(\d+)(?:[–-](\d+))?',mapmatch,p)for p in parts];r['current_destination']=';'.join(parts);t=r['old_exact_opening'].lower();notes=[]
  if 'place of supply' in t or'§ 3a' in t:notes+=['R26: general business service route now subject to actual receiving-establishment/ordinary exception selectors.']
  if 'solar'in t or'water'in t:notes+=['R27: solar operator population and exact Annex2water exclusions supplied.']
  if 'bank fees'in t:notes+=['R28: actual bank transaction/invoice classification replaces identity-based exemption; custody/debtcollection exceptions explicit.']
  if 'foreign vat'in t:notes+=['R30: no automatic foreign refund/cost treatment; legality/recoverability established separately.']
  if 'intra-eu supplies'in t or'arrival'in t:notes+=['R29: actual6a/4gates and17a document-class pairs, with fallback/statutory proof boundaries retained.']
  r['bounded_successor_scope']=' '.join(notes)
(W/'support'/s).mkdir(exist_ok=True);dump(W/'support'/s/'rows.json',rows);dump(W/'support'/s/'old-topic-destinations.json',ot)
def e(t):return str(t).replace('|','\\|').replace('\n','<br>')
def anc(id):return id.lower().replace('.','-').replace('_','-')
t=f'# {s}: DE-R26–31 successor figure/rule ledger\n\nGuide `{proof["after_sha256"]}`, {proof["bytes"]} bytes. Immutable original B Guide `{proof["before_sha256"]}`, ledger `{B/"ledgers"/(s+".md")}` / `{H(B/"ledgers"/(s+".md"))}`. Writer corrections, different independent recheck pending. Nine selected operative ranges actually read29October2026; original-language quotes/official URLs/read dates and raw-reader identities: [source-quotes.md](../source-quotes.md). OLD anchors preserve exact earlier writer read provenance by reference, not an inference from cached acquisition. R31 complete no5/closing-factor quotation supplements the preserved historical partial prefix.\n\n| ID | Section / native LF | Exact current wording | Source anchors / disposition |\n|---|---|---|---|\n'
for r in rows:t+=f'| {r["id"]} | {e(r["section"])} LF{r["native_LF"]} | {e(r["wording"])} | '+(', '.join(f'[{id}](../source-quotes.md#{anc(id)})'for id in r['source_quote_ids'])or'Preserved scope/routing/presentation/express limitation; no new positive tax rule.')+f'. {e(r["disposition"])} |\n'
t+='\n## Complete old-topic destinations\n\nEvery exact old-unit origin/hash/opening and predecessor route remains in support/germany-vat-return/old-topic-destinations.json, with current native coordinates and bounded correction notes. References explicitly marked companion retain their own coordinates.\n\n| Origin / native LF / hash | Exact old opening | Current destination / disposition |\n|---|---|---|\n'
for kind in['pre_refresh_rows','current_main_rows']:
 for r in ot[kind]:t+=f'| {kind} LF{r["old_native_LF"]} / {r["old_unit_sha256"]} | {e(r["old_exact_opening"])} | {e(r["current_destination"])}. {e(r["disposition"])} {e(r["bounded_successor_scope"])} |\n'
(W/'ledgers'/f'{s}.md').write_text(t);t='# R26–31 selected source quotations\n\nNine own selected native ranges actually read29October2026. OLD-prefixed anchors preserve earlier actual B writer reading and exact quotation with explicit attribution. Raw bodies remain unchanged, readers are identified derivatives.\n'
for id,q in qs.items():t+=f'\n<a id="{anc(id)}"></a>\n## {id}\n\n{q["act_article"]}; {q["url"]}; actual read: {q["read_on"]}; native LF{q["native_LF"]}. {q.get("provenance",q.get("actual_read_scope",""))} Exact identities: source-quote-index.json.\n\n> '+q['exact_quote'].replace('\n','\n> ')+'\n'
(W/'source-quotes.md').write_text(t);dump(W/'source-quote-index.json',qs);inv={'slug':s,'Guide_path':proof['path'],'Guide_sha256':proof['after_sha256'],'bytes':proof['bytes'],'ledger_path':str(W/'ledgers'/f'{s}.md'),'ledger_sha256':H(W/'ledgers'/f'{s}.md'),'current_rows':len(rows),'prior_current_rows':len(original),'old_topics':len(ot['pre_refresh_rows'])+len(ot['current_main_rows']),'prior_ledger':str(B/'ledgers'/f'{s}.md'),'prior_ledger_sha256':H(B/'ledgers'/f'{s}.md')};dump(W/'successor-inventory.json',inv);print(json.dumps(inv,indent=2))
