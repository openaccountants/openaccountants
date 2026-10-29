from pathlib import Path
import json,hashlib,re,difflib,copy
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');W=O/'germany-DE-R113-R114-planning-writer-successor-2026-10-29';P=O/'germany-DE-R97-R108-planning-writer-successor-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');p=R/'skills/international/germany/germany-tax-optimization.md';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');W.mkdir(exist_ok=True);(W/'before').mkdir(exist_ok=True);(W/'after').mkdir(exist_ok=True);(W/'ledgers').mkdir(exist_ok=True);(W/'support').mkdir(exist_ok=True)
assert H(p)=='45b98bb40ee1749c47a231894efa9d643177939b66fb9b051b61264c63abcde0';before=p.read_text();(W/'before'/p.name).write_bytes(p.read_bytes());text=before;ops=[]
(W/'options-and-selection.md').write_text('''# DE-R113–114 sourced options before editing

A selected under standing authority. R113: move the exact employee pension paragraph after the original Later-and-locked table row, keeping all legal words/amounts exact and one unpublished version1.3. R114: supply the source-backed directly eligible isolated Riester claimant calculation, documented child entitlement/allocation,2100cap/175basic/185or300child/under25one-off200,4%minimum less entitled allowances with60floor and proportional allowance reduction, plus own10a tax comparison without double counting. Exact five own selected law reads in own-actual-read-quotes.json; no source fetch.

B: repair table with a repeated header; restore statutory numbers but retain minimum-contribution calculation as a named partial. A gives a contiguous table and actual ordinary positive computation already supplied by the retained law. No product ranking, no universal voluntary-self-employed eligibility, no inferred indirect-spouse formula. Preserve original five qualitative cases/0oa/URLs and previous23member seal.
''')
qs=json.loads((P/'source-quote-index.json').read_text());own={}
for id in ['OPT.RIESTER','OPT.RIESTERTEST','OPT.RIESTERBASE','OPT.RIESTERCHILD','OPT.RIESTERMIND']:
 q=copy.deepcopy(qs[id]);assert H(Path(q['raw_path']))==q['raw_sha256'];assert H(Path(q['reader_path']))==q['reader_sha256'];a,b=q['native_LF'];assert q['exact_quote']in'\n'.join(Path(q['reader_path']).read_text().split('\n')[a-1:b]);q['read_on']='2026-10-29';q['provenance']='Own selected entire operative quote/nativeLF actually reread for R114 after C finding; no acquisition or full-body read claim.';own['R114.'+id.removeprefix('OPT.')]=q
qs.update(own);dump(W/'own-actual-read-quotes.json',own)
def op(a,b):
 global text
 assert text.count(a)==1,(a,text.count(a));text=text.replace(a,b,1);ops.append({'before':a,'after':b})
para=next(l for l in text.split('\n')if l.startswith('For an ordinary employee with qualifying pension contributions'));last=next(l for l in text.split('\n')if l.startswith('| Later and locked |'));op('\n\n'+para+'\n'+last,'\n'+last+'\n\n'+para)
old=next(l for l in text.split('\n')if l.startswith('| Deduction, allowances |'))
new='| Deduction, allowances | For an eligible claimant, own qualifying contributions plus the entitled allowance are capped at EUR 2,100 yearly for the § 10a special-expense comparison. The tax office tests whether that deduction is better than the allowance entitlement; if so, it adds that entitlement back to the tax calculated with the deduction, preventing a double benefit (§ 10a(2)). Basic allowance EUR 175; child allowance EUR 185, or EUR 300 for a child born after 2007, only with the actual § 85 entitlement and allocation below. Allowances are proportionately reduced below the § 86 minimum own contribution. https://www.gesetze-im-internet.de/estg/__10a.html |'
op(old,new)
addition='''

For an isolated directly eligible claimant, with no indirectly eligible spouse, compute the yearly minimum own payment as `max(EUR 60, min(4% × prior-year relevant statutory insured income, EUR 2,100) − entitled basic and child allowances)` (§ 86). Use the actual relevant income category, not turnover or current-year profit. If the actual qualifying own contribution is below that minimum, multiply the entitled allowance by the contribution/minimum ratio; payment at or above the minimum gives the full entitlement. A directly eligible age-30 claimant with no children and prior relevant insured income EUR 20,000 needs EUR 625: min(EUR 800, EUR 2,100) − EUR 175. Paying EUR 312.50 gives EUR 87.50 allowance. With relevant income EUR 100,000, the same claimant needs EUR 1,925. A lower result cannot remove the EUR 60 floor. These are contribution/allowance computations, not a promised tax saving; the actual § 10a tax comparison remains separate.

Document allowance entitlement rather than using child count alone. Under § 85, Kindergeld must be assessed to the entitled person; a full-year total recovery removes that child allowance. If several eligible persons receive Kindergeld for the same child, the first entitlement period in the year determines allocation. For qualifying married, non-separated EU/EEA-resident different-sex parents, allocation is to the mother unless both request the father; for the corresponding same-sex married or civil-partner parents, allocation is to the Kindergeld-assessed parent unless both request the other. That request cannot be withdrawn for an elapsed contribution year. Section 84 adds a one-off EUR 200 to the basic allowance for a directly eligible person under 25 at the start of the contribution year, for the first eligible post-2007 contribution year for which an allowance is requested. The age-30 examples do not include it. Product qualification and indirect-spouse or other eligibility populations require their own actual statutory conditions; voluntary pension contributions alone do not establish the compulsory-insurance branch above.'''
op(new,new+addition)
p.write_text(text);(W/'after'/p.name).write_text(text);dump(W/'exact-operations.json',ops)
bl=before.split('\n');ls=text.split('\n');lm={}
for tag,a,b,c,d in difflib.SequenceMatcher(a=bl,b=ls,autojunk=False).get_opcodes():
 for n in range(a,b):lm[str(n+1)]=[c+1 if tag!='equal'else c+n-a+1,d if tag!='equal'else c+n-a+1]
# Exact moved paragraph and original table row: keep identity rather than map a deletion to an empty range.
for line in [para,last]:
 n=bl.index(line)+1;m=ls.index(line)+1;lm[str(n)]=[m,m]
dump(W/'support/line-map.json',lm);rows=[];covered=set();priorrows=json.loads((P/'support/germany-tax-optimization/rows.json').read_text())
for q in priorrows:
 q=copy.deepcopy(q);a,b=q['native_LF'];x,y=lm[str(a)][0],lm[str(b)][1];assert x<=y;t='\n'.join(ls[x-1:y]);q['R113_R114_prior_native_LF']=[a,b];q['native_LF']=[x,y];q['wording']=t
 if '| Deduction, allowances |'in t:q['source_quote_ids']=list(dict.fromkeys(q['source_quote_ids']+list(own)))
 rows.append(q);covered.update(range(x,y+1))
for n,l in enumerate(ls,1):
 if n in covered or not l.strip():continue
 if l.startswith(('For an isolated directly eligible claimant','Document allowance entitlement')):rows.append({'id':str(len(rows)+1),'prior_row_id':None,'native_LF':[n,n],'section':'R114 directly eligible Riester calculation/entitlement','wording':l,'source_quote_ids':list(own),'disposition':'Positive source-backed narrow ordinary contribution/allowance method; figures computed, claimant facts stipulated'})
old=json.loads((P/'support/germany-tax-optimization/old-topic-destinations.json').read_text());tr=[];newnumeric=[n for n,l in enumerate(ls,1)if l.startswith('| Deduction, allowances |')or l.startswith('For an isolated directly eligible claimant')or l.startswith('Document allowance entitlement')]
for q in old:
 q['R113_R114_prior_destination']=q['destination']
 if 'component_destinations'in q:
  for t in q['component_destinations']:
   a,b=t['current_native_LF'];x,y=lm[str(a)][0],lm[str(b)][1];t['R113_R114_prior_native_LF']=[a,b];t['current_native_LF']=[x,y];t['current_actual_clause']='\n'.join(ls[x-1:y]);t['current_clause_sha256']=hashlib.sha256(t['current_actual_clause'].encode()).hexdigest()
  if q['pre_refresh_index']in[87,88]:
   q['component_destinations']=[{'current_native_LF':[n,n],'current_actual_clause':ls[n-1],'current_clause_sha256':hashlib.sha256(ls[n-1].encode()).hexdigest(),'source_quote_ids':list(own)}for n in newnumeric];q['semantic_disposition']='R114 actual positive directly eligible isolated claimant method restores statutory2100/175/185or300/minimum4%-cap-less-allowance60floor/ratio, subject to documented entitlement. Old universal voluntary-self-employed eligibility is not adopted.'
  q['destination']='; '.join('LF'+str(t['current_native_LF'][0])+('–'+str(t['current_native_LF'][1])if t['current_native_LF'][0]!=t['current_native_LF'][1]else'')for t in q['component_destinations'])+'. '+q['semantic_disposition'];tr.append({'pre_refresh_index':q['pre_refresh_index'],'old_native_LF':q['old_lf'],'components':q['component_destinations'],'disposition':q['semantic_disposition']})
 else:
  def m(t):
   a,b=int(t[1]),int(t[2])if t[2]else int(t[1]);x,y=lm[str(a)][0],lm[str(b)][1];return'LF'+str(x)+('–'+str(y)if x!=y else'')
  q['destination']=re.sub(r'LF\s*(\d+)(?:[–-](\d+))?',m,q['destination'])
dump(W/'support/rows.json',rows);dump(W/'support/old-topic-destinations.json',old);dump(W/'pre-refresh-route-index.json',tr);dump(W/'source-quote-index.json',qs)
esc=lambda t:str(t).replace('|','\\|').replace('\n','<br>');t=f'# Germany planning R113–114 exact successor ledger\n\nGuide `{H(p)}`, {p.stat().st_size} bytes, unpublished version1.3. Previous Guide45b98bb4/ledger7c49b980/23member seal unchanged. Five own selected law scopes actually reread29October2026; full quotes/officialURLs/nativeLF/raw-reader hashes in source-quote-index.json/source-quotes.md, original137 quoted records retain prior attributed readings. Writer successor, different independent review pending.\n\n| ID/nativeLF | Section | Exact current wording | Source IDs |\n|---|---|---|---|\n'
for q in rows:t+=f'| {q["id"]}/{q["native_LF"]} | {esc(q["section"])} | {esc(q["wording"])} | {esc(q["source_quote_ids"])} {esc(q.get("source_anchor_qualification",""))} |\n'
t+='\n## Complete old-topic destinations\n\nAll455old identities/wording retained. All134 actual component routes rebound;87/88 now point to the positive numeric Riester method, not source-only history.\n\n| Origin/LF | Exact old wording | Actual current clause destinations |\n|---|---|---|\n'
for q in old:t+=f'| {q["ref"]}/{q["old_lf"]} | {esc(q["wording"])} | {esc(q["destination"])} |\n'
(W/'ledgers'/p.name).write_text(t);t='# Planning R113–114 source quotations\n\nFive own operative rereads29October2026. All exact prior quotation/source-body bytes retained with attributed read dates. No new acquisition.\n'
for id,q in qs.items():t+=f'\n## {id}\n\n{q.get("article",q.get("act_article"))}; {q.get("url",q.get("official_url"))}; read {q.get("read_on")}; nativeLF {q["native_LF"]}. {q.get("provenance",q.get("actual_read_scope",""))}\n\n> '+q['exact_quote'].replace('\n','\n> ')+'\n'
(W/'source-quotes.md').write_text(t);dump(W/'successor-inventory.json',{'slug':p.stem,'Guide_path':str(p),'Guide_sha256':H(p),'Guide_bytes':p.stat().st_size,'ledger_path':str(W/'ledgers'/p.name),'ledger_sha256':H(W/'ledgers'/p.name),'rows':len(rows),'prior_rows':len(priorrows),'old_origins':len(old),'own_selected_quotes':len(own),'ops':len(ops)})
print((W/'successor-inventory.json').read_text())
