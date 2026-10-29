from pathlib import Path
import json,hashlib,re,difflib,copy
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');W=O/'germany-DE-R109-R111-rental-writer-successor-2026-10-29';P=O/'germany-root-rental-ledger-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');p=R/'skills/international/germany/de-rental-income.md';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');W.mkdir(exist_ok=True);(W/'before').mkdir(exist_ok=True);(W/'after').mkdir(exist_ok=True);(W/'ledgers').mkdir(exist_ok=True);(W/'support').mkdir(exist_ok=True)
before=(W/'before'/p.name).read_text();text=(W/'after'/p.name).read_text();assert p.read_text()==text;own=json.loads((W/'own-actual-read-quotes.json').read_text());ops=json.loads((W/'exact-operations.json').read_text())
# Rebind every original unit and all550 actual old origins; add only newly inserted operative paragraphs.
bl=before.split('\n');ls=text.split('\n');lm={}
for tag,a,b,c,d in difflib.SequenceMatcher(a=bl,b=ls,autojunk=False).get_opcodes():
 for n in range(a,b):lm[str(n+1)]=[c+1 if tag!='equal'else c+n-a+1,d if tag!='equal'else c+n-a+1]
dump(W/'support/line-map.json',lm);priorrows=json.loads((P/'current-rule-rows.json').read_text());rows=[];covered=set()
def extra(t):
 z=[]
 if 'no loss'in t or'no-loss'in t or'zero or positive forecast'in t:z+=['R109-111.R42']
 if 'four-year benefit period'in t or'Continuing that fully qualifying January'in t:z+=['R109-111.R17','R109-111.R89','R109-111.R92']
 if any(k in t for k in ['Costs attributable to the owner','For mixed private and rental use','costs attributable to own-use']):z+=['R109-111.R34','R109-111.R120']
 return z
for n,q in enumerate(priorrows,1):
 a,b=lm[str(q['native_LF'])];t='\n'.join(ls[a-1:b]);rows.append({'id':f'{n:03d}','prior_row_id':n,'native_LF':[a,b],'section':q['section'],'wording':t,'source_quote_ids':list(dict.fromkeys(q['anchors']+extra(t))),'classification':q['classification'],'prior_native_LF':q['native_LF'],'disposition':'Exact original unit or bounded R109–111 qualification; historical wording retained in preimage'});covered.update(range(a,b+1))
for n,l in enumerate(ls,1):
 if n in covered or not l.strip():continue
 ex=extra(l)
 if ex:rows.append({'id':str(len(rows)+1),'prior_row_id':None,'native_LF':[n,n],'section':'Finite ordinary rental calculation','wording':l,'source_quote_ids':ex,'classification':'new_sourced_computation','disposition':'Computed fixture, actual independent allocation/historical qualification facts required'})
old=json.loads((P/'old-topics.json').read_text());old['current_guide_sha256']=H(p)
for key in ['pre_refresh_rows','main_baseline_rows']:
 for q in old[key]:
  q['prior_sealed_destination_current_native_LF']=q['destination_current_native_LF'];q['prior_sealed_destination_wording']=q.get('destination_wording',[bl[a-1]for a in q['destination_current_native_LF']]);new=sorted(set(n for a in q['destination_current_native_LF']for n in range(lm[str(a)][0],lm[str(a)][1]+1)));q['destination_current_native_LF']=new;q['destination_wording']=[ls[n-1]for n in new];q['successor_scope']='R109–111 actual administrative no-loss/remaining-life/attribution corrections qualify matching earlier claims; full old wording/identity retained.'
dump(W/'support/current-rule-rows.json',rows);dump(W/'support/old-topics.json',old)
qs={q['id']:{**q,'provenance':'Original root selected quotation/actual read date reused by attribution; not new own whole-source reading.'}for q in json.loads((P/'source-quotes.json').read_text())};qs.update(own);dump(W/'source-quote-index.json',qs);dump(W/'source-index-reference.json',{'original_source_identities_path':str(P/'source-identities.json'),'sha256':H(P/'source-identities.json'),'original_source_quotes_sha256':H(P/'source-quotes.json'),'scope':'Exact original135 quotes retained; six own selected re-reads supplement. RNT08 remains web observation, not raw HTML.'})
esc=lambda t:str(t).replace('|','\\|').replace('\n','<br>');t=f'# de-rental-income R109–111 successor ledger\n\nGuide `{H(p)}`, {p.stat().st_size} bytes. Original Guide7723c03d / ledger800b72f5 and163-member root seal unchanged. Writer correction, independent review pending. Source IDs bind exact original-language quotations/officialURLs/nativeLF/read dates in source-quote-index.json and source-quotes.md; original root source-identities.json remains referenced without duplicate bodies.\n\n| ID/native LF | Section | Exact wording | Source IDs/classification |\n|---|---|---|---|\n'
for q in rows:t+=f'| {q["id"]} / {q["native_LF"]} | {esc(q["section"])} | {esc(q["wording"])} | {esc(q["source_quote_ids"])} / {q["classification"]} |\n'
t+='\n## Complete old-topic destinations\n\nAll550 actual old origins and exact original wording retained with original destination and successor clauses.\n\n| Origin/nativeLF | Exact old wording | Actual current nativeLF / wording |\n|---|---|---|\n'
for key in ['pre_refresh_rows','main_baseline_rows']:
 for q in old[key]:t+=f'| {q["origin"]} / {q["old_native_LF"]} | {esc(q["old_wording"])} | {q["destination_current_native_LF"]} / {esc(q["destination_wording"])} |\n'
(W/'ledgers'/p.name).write_text(t);t='# Rental source quotations\n\nOriginal135 exact quotations retained with attributed original read dates. Six own operative native scopes read29October2026. See source-index-reference.json for exact original identity table. No source acquisition.\n'
for id,q in qs.items():t+=f'\n## {id}\n\n{q["act_article"]}; {q["official_url"]}; read {q["read_on"]}; nativeLF {q["reader_native_LF"]}. {q.get("note","")}\n\n> '+q['exact_original_language_quote'].replace('\n','\n> ')+'\n'
(W/'source-quotes.md').write_text(t);dump(W/'successor-inventory.json',{'slug':p.stem,'Guide_path':str(p),'Guide_sha256':H(p),'Guide_bytes':p.stat().st_size,'ledger_path':str(W/'ledgers'/p.name),'ledger_sha256':H(W/'ledgers'/p.name),'rows':len(rows),'prior_rows':len(priorrows),'old_origins':sum(len(old[k])for k in ['pre_refresh_rows','main_baseline_rows']),'own_selected_quotes':len(own),'ops':len(ops)})
print((W/'successor-inventory.json').read_text())
