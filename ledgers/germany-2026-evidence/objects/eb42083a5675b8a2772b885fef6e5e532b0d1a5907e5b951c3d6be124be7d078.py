from pathlib import Path
import json,hashlib,re,copy,difflib
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-DE-R47-R54-Swiss-writer-successor-2026-10-29');A=W.parent/'germany-ledger-writer-2026-10-28';s='germany-to-switzerland-cross-border-tax';sup=A/'support'/s;H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');proof=json.loads((W/'preservation-proof.json').read_text());before=(W/'before'/f'{s}.md').read_text();after=(W/'after'/f'{s}.md').read_text();lines=after.split('\n');lm=json.loads((W/'support/line-map.json').read_text());own=json.loads((W/'own-actual-read-quotes.json').read_text());qs=copy.deepcopy(own)
for q in json.loads((sup/'actual-read-quotes.json').read_text()):
 id='CH.'+q['id'];identity=json.loads((A/'sources'/(q['source']+'.identity.json')).read_text());qs[id]={**identity,**q,'id':id,'native_LF':[q['LF_start'],q['LF_end']],'read_on':q.get('read_on',q.get('actual_read_on')),'provenance':'Exact original A writer quotation and actual prior read date reused by reference. This successor does not claim a new full-source read.'}
def more(t):
 ids=[]
 if '- The 2026 tariff applies'in t:ids+=['R47-53.SoliRate','R47-53.SOLILIMIT']
 if any(x in t for x in ['**2. Weekly stayer','- After testing art. 15(2)','| Weekly stayer |','**Lost commuter status found late.**']):ids+=['R47-53.SUBJECTTAX','R47-53.SALARY']
 if '**4. Germans who move'in t:ids+=['R47-53.RES']
 if '**Treaty tail, art. 4(4)'in t:ids+=['R47-53.TAIL']
 if t.startswith('Protocol no. 9 covers'):ids+=['R47-53.PUBPENSION','R47-53.PENSCREDIT','R47-53.PENS1','R47-53.PENS2']
 if '**Late filing surcharge'in t:ids+=['R54.extensions']
 if '**Swiss withholding for German residents, dividends, interest.**'in t:ids+=['R47-53.CHDIV']
 if 'Selected operative clauses actually read on 29 October' in t or'7. For the relevant exception:'in t:ids+=list(json.loads((W/'own-actual-read-quotes.json').read_text()))
 return ids
rows=[];covered=set();original=json.loads((sup/'claim-rows.json').read_text())
for i,r in enumerate(original,1):
 a,b=lm[str(r['lf'])]['start'],lm[str(r['lf'])]['end'];t='\n'.join(lines[a-1:b]);ids=list(dict.fromkeys(['CH.'+x for x in r['anchors']]+more(t)));rows.append({'id':f'{i:03d}','prior_row_id':i,'prior_native_LF':[r['lf'],r['lf']],'native_LF':[a,b],'section':r['section'],'wording':t,'source_quote_ids':ids,'disposition':'Exact prior current unit with rebound native coordinates' if r['wording']==t else 'R47–54 bounded source-backed condition successor'});covered.update(range(a,b+1))
for tag,a,b,c,d in difflib.SequenceMatcher(a=before.split('\n'),b=lines,autojunk=False).get_opcodes():
 if tag not in ['replace','insert']:continue
 for i in range(c,d):
  if i+1 in covered or not lines[i].strip() or lines[i].startswith(('version:','last_updated:')):continue
  ids=more(lines[i]);assert ids,(i+1,lines[i]);rows.append({'id':f'{len(rows)+1:03d}','prior_row_id':None,'native_LF':[i+1,i+1],'section':'R47–54 new bounded operative condition / labelled computed separator / actual read source','wording':lines[i],'source_quote_ids':ids,'disposition':'New sourced correction; fixture amounts stipulated and computed'});covered.add(i+1)
old=json.loads((sup/'old-topics.json').read_text())
def mapping(m):
 a,b=int(m[1]),int(m[2])if m[2]else None
 return 'LF'+str(lm[str(a)]['start'])+('–'+str(lm[str(b)]['end'])if b else ('–'+str(lm[str(a)]['end'])if lm[str(a)]['end']!=lm[str(a)]['start']else''))
for r in old:
 d=r['destination'];r['prior_sealed_destination']=d;r['destination']=re.sub(r'LF\s*(\d+)(?:[–-](\d+))?',mapping,d);word=r['wording'].lower();notes=[]
 if 'solidarity'in word or'20,350'in word:notes+=['R47: actual assessedbase/individual-jointthreshold/11.9%phasein, separate settlementcredit.']
 if 'swiss tax paid'in word or'proof of swiss tax'in word or'refused until'in word:notes+=['R48: actualwaiver ORassessedtaxpaid proof; subsequentassessmentamendmentconditions retained.']
 if 'treaty tail'in word:notes+=['R49: actualadditionalGermantaxcap beyond6–22, no trade tax; not commutercredit.']
 if 'weekly stayer'in word or'work days in switzerland'in word:notes+=['R50: actual15(2)calendarpresence/employer/PE exception before ordinaryworkdayallocation.']
 if 'moving ends'in word:notes+=['R51: domesticliability actuallyending is conditional on residence/home/habitualabode, separate treatyresidence.']
 if 'public service'in word and'pension'in word:notes+=['R52: current/lastrelevantinsuranceemployment, exactperiodic/capitalprocedure/taxable-share/no-double-refund gates.']
 if 'dividend'in word:notes+=['R53: residual15%vsactualspecialpopulations; beneficialresidentnonpartnership/direct10%/paymentinclusive365zero gates.']
 if 'compulsory'in word and'29 february'in word:notes+=['R54: actual109extension/zero-negative/no-nettax exclusions qualifycompulsion; discretionseparate.']
 r['bounded_successor_scope']=' '.join(notes)
(W/'support'/s).mkdir(exist_ok=True);dump(W/'support'/s/'rows.json',rows);dump(W/'support'/s/'old-topic-destinations.json',old)
def esc(t):return str(t).replace('|','\\|').replace('\n','<br>')
def anchor(id):return id.lower().replace('.','-').replace('_','-')
t=f'# {s}: DE-R47–54 successor figure and rule ledger\n\nGuide `{proof["after_sha256"]}`, {proof["bytes"]} bytes. Immutable predecessor Guide `{proof["before_sha256"]}`; predecessor ledger `{A/"ledgers"/(s+".md")}` / `{H(A/"ledgers"/(s+".md"))}`. Every current substantive unit and every prior old-topic identity is retained below, with exact changed scope and native coordinates. Writer corrections, different independent review pending. New own selected operative reads: 29 October 2026. Earlier anchors retain actual original A-writer reading provenance, not a claim that acquisition proves reading. Exact original-language quotes, official URLs/read dates/raw-reader identities: [source-quotes.md](../source-quotes.md).\n\n| ID | Section / native LF | Exact current wording | Source anchors / disposition |\n|---|---|---|---|\n'
for r in rows:t+=f'| {r["id"]} | {esc(r["section"])} LF{r["native_LF"]} | {esc(r["wording"])} | '+(', '.join(f'[{id}](../source-quotes.md#{anchor(id)})'for id in r['source_quote_ids'])or'Preserved scope/routing/express limitation/attribution; no new positive rule.')+f'. {r["disposition"]} |\n'
t+='\n## Complete old-topic destinations\n\nExact old origins and full wording remain in support/germany-to-switzerland-cross-border-tax/old-topic-destinations.json. Prior coordinates are preserved as history and current coordinates are mechanically rebound; correction notes identify substantive qualifications.\n\n| Historical reference / native LF | Exact old topic | Current destination / correction |\n|---|---|---|\n'
for r in old:t+=f'| {r["ref"]} LF{r["old_lf"]} | {esc(r["wording"])} | {esc(r["destination"])} {esc(r["bounded_successor_scope"])} |\n'
(W/'ledgers'/f'{s}.md').write_text(t)
t='# DE-R47–54 exact source quotations\n\nTwelve own selected native ranges were actually read on 29 October 2026. CH-prefixed anchors retain original A writer read dates and exact quotes; their reuse is explicitly attributed. Readers are derivatives; raw bytes stay unchanged.\n'
for id,q in qs.items():t+=f'\n<a id="{anchor(id)}"></a>\n## {id}\n\n{q.get("act_article",q.get("article"))}; {q["url"]}; actual read: {q["read_on"]}; native LF{q["native_LF"]}. {q.get("actual_read_scope",q.get("provenance",""))} Full raw/reader paths and SHA-256 hashes: source-quote-index.json.\n\n> '+q['exact_quote'].replace('\n','\n> ')+'\n'
(W/'source-quotes.md').write_text(t);dump(W/'source-quote-index.json',qs)
inv={'slug':s,'Guide_path':proof['path'],'Guide_sha256':proof['after_sha256'],'bytes':proof['bytes'],'ledger_path':str(W/'ledgers'/f'{s}.md'),'ledger_sha256':H(W/'ledgers'/f'{s}.md'),'current_rows':len(rows),'prior_current_rows':len(original),'old_topics':len(old),'prior_ledger':str(A/'ledgers'/f'{s}.md'),'prior_ledger_sha256':H(A/'ledgers'/f'{s}.md')};dump(W/'successor-inventory.json',inv);print(json.dumps(inv,indent=2))
