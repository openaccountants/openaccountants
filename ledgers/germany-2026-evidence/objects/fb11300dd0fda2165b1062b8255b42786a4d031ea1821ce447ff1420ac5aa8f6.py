from pathlib import Path
import json,hashlib,re,difflib
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');T=O/'germany-DE-R11-R12-writer-successor-2026-10-29';A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();quotes=json.loads((T/'own-actual-read-quotes.json').read_text())
x=json.loads((B/'actual-read-quotes.json').read_text())['GT.ownerwages'];quotes['R12.qualifying-wages']={**x,'id':'R12.qualifying-wages','article':'GewStG § 31(1)–(5)','native_LF':[7,11],'exact_quote':'\n'.join(Path(x['reader_path']).read_text().split('\n')[6:11]),'read_on':'2026-10-29','qualification':'Own full retained five operative paragraphs actually read in this repair phase, not inferred from prior writer/reviewer verdict.'}
for id,s,lo,hi,article in [('R13.grace','Uee7f672101b3d3dd',7,9,'AO § 240(1)–(3)'),('R13.method','Ud818a09838515be4',7,13,'AO § 224(1)–(2)')]:
 x=json.loads((A/'sources'/f'{s}.identity.json').read_text());quotes[id]={**x,'id':id,'article':article,'native_LF':[lo,hi],'exact_quote':'\n'.join(Path(x['reader_path']).read_text().split('\n')[lo-1:hi]),'read_on':'2026-10-29','qualification':'Own full selected retained statutory text read. Three-day noncollection grace is separate from effective payment/deemed cheque timing; only the actual224(2)no1 category is excluded, not all payments involving cash through bank accounts.'}
(T/'own-actual-read-quotes.json').write_text(json.dumps(quotes,ensure_ascii=False,indent=2)+'\n')
(T/'R12-R13-options-and-selection.md').write_text('''# DE-R12–13 options before editing, 29 October 2026

**R12 A, selected:** use actual GewStG31 qualifying wages before the existing29 full€1,000 rounding/key. Ordinary input gates:19(1)no1 employment pay, other-law exempt amounts excluded except overtime/Sunday/holiday/night supplements included regardless of income-tax treatment; trainee remuneration and profit-based one-off remuneration excluded; remaining remuneration capped at€50,000 for each employee. Preserve own31(3) partly-exempt-business condition, separate total€25,000 working-owner amount and special-industry scope. Add actual employee-level intake and the corporation/two-establishment100,000/50,000→50,000/50,000→500/500 of1000 separator outside original cases. **B:** refer unsupplied31 wage-base classification rather than retain unqualified all-pay computation. A is fully supported by the already retained own statutory paragraphs, actually read7–11; no acquisition.

**R13 A, selected:** qualify trade/corporate three-day grace by exact AO240(3)→224(2)no1 exception, naming payment instruments handed/sent to the authority, including cash/cheques. Account transfers/deposits remain their distinct no2 method; no indiscriminate exclusion of all cash-related transactions. Preserve1%,€50 rounding, due-date/payment timing rules and original cases. **B:** remove unqualified short grace conclusions and refer directly to the actual statutory condition. A supplies the finite ordinary operational gate. Both own clauses are quoted/read, no new source hunt.
''')
ops=json.loads((T/'exact-operations.json').read_text());proof=json.loads((T/'preservation-proof.json').read_text())
for slug,version in [('de-trade-tax','1.4'),('de-corporate-tax','0.5')]:
 p=R/'skills/international/germany'/f'{slug}.md';old=p.read_text();(T/'before'/p.name).write_text(old);oo=[]
 def add(a,b,why):assert old.count(a)==1,(slug,why,old.count(a));oo.append({'old':a,'new':b,'reason':why})
 ver=re.search(r'^version: (.+)$',old,re.M).group(1);add('version: '+ver,'version: '+version,'Monotonic content version; actual date already29October')
 if slug=='de-trade-tax':
  a='The key is wages paid at each establishment, rounded down to full EUR 1,000';b='The key uses the qualifying statutory wages of each establishment under § 31, then rounds them down to full EUR 1,000';add(a,b,'DE-R12 statutory wage base before preserved29 key')
  line=next(l for l in old.split('\n') if l.startswith('**6. Apportion between municipalities'))
  # Separate insertion after the full original paragraph preserves its source URL occurrence order.
  insert='''**Qualifying apportionment wages (§ 31(1)–(4) GewStG).** Start with employment remuneration under § 19(1) no. 1 EStG, excluding amounts exempt from income tax under other legislation. Include overtime and Sunday, public-holiday and night-work supplements regardless of their income-tax treatment. Exclude remuneration paid to people employed for vocational training and one-off remuneration calculated by profit. For each individual employee, exclude the remaining remuneration above EUR 50,000. Where the business is partly trade-tax exempt, exclude pay of employees who do not work exclusively or predominantly in the taxable business or part. Apply these employee rules before aggregating the establishment's qualifying wages and applying the § 29 rounding and apportionment key. The separate total EUR 25,000 working-owner amount under § 31(5) remains as stated above.

For a stipulated ordinary corporation with two establishments, one employee at A paid EUR 100,000 and one at B paid EUR 50,000, with no trainee pay, profit-based bonus or other adjustment, qualifying wages are EUR 50,000 at each establishment. A EUR 1,000 base amount therefore splits EUR 500 to each, before each municipality applies its own multiplier. The uncapped 2:1 salary ratio is not the statutory key.'''
  # Operation applies to paragraph after the first sentence replacement has already occurred.
  adjusted=line.replace(a,b);oo.append({'old':adjusted,'new':adjusted+'\n\n'+insert,'reason':'DE-R12 complete common31 input gates and separating worksheet'})
  add('none for a delay of up to three days','none for a delay of up to three days except payments within § 224(2) no. 1 AO, including cash or cheques handed or sent to the tax authority','DE-R13 exact payment-method exception')
  ask=next(l for l in old.split('\n') if l.startswith('- In which municipalities did it have premises'))
  add(ask,ask+' For apportionment, obtain pay by employee and establishment, trainee status, profit-based one-off bonuses, tax-exempt items and overtime/Sunday/holiday/night supplements, so the per-employee EUR 50,000 limit and § 31 exclusions can be applied.','DE-R12 actual wage-base facts')
 else:
  add('except for cheque payment','except payments within § 224(2) no. 1 AO, including cash or cheques handed or sent to the tax authority','DE-R13 full statutory payment-method category')
 marker='| Source | URL | Read on |';pos=old.index(marker);end=old.index('\n\n',pos);extra='\n| AO § 240(3) and § 224(2) no. 1 (three-day grace payment-method exception), selected operative clauses re-read | https://www.gesetze-im-internet.de/ao_1977/__224.html | 2026-10-29 |'
 if slug=='de-trade-tax':extra+='\n| GewStG § 31(1)–(5), qualifying apportionment wages, exclusions and employee ceiling, selected full clauses re-read | https://www.gesetze-im-internet.de/gewstg/__31.html | 2026-10-29 |'
 add(old[pos:end],old[pos:end]+extra,'DE-R12/13 actual selected read-date/source binding')
 new=old
 for x in oo:assert new.count(x['old'])==1,(slug,x['reason']);new=new.replace(x['old'],x['new'],1)
 rev=new
 for x in reversed(oo):assert rev.count(x['new'])==1;rev=rev.replace(x['new'],x['old'],1)
 assert rev==old
 blocks=lambda s:re.findall(r'```oa-(?:check|example)\b.*?```',s,re.S);assert blocks(old)==blocks(new)
 h=old.index('## Worked examples') if '## Worked examples' in old else old.index('## Examples');e=old.index('## Ask the client',h);assert old[h:e] in new
 urls=lambda s:re.findall(r'https?://[^\s<>|)]+',s);it=iter(urls(new));assert all(any(x==y for y in it) for x in urls(old))
 assert old[old.index('<!-- openaccountants-cta-block -->'):]==new[new.index('<!-- openaccountants-cta-block -->'):]
 assert re.sub(r'(?m)^version: .+$','version: X',old.split('---',2)[1])==re.sub(r'(?m)^version: .+$','version: X',new.split('---',2)[1])
 (T/'after'/p.name).write_text(new);p.write_text(new);(T/'support'/f'{slug}.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before',tofile='after')));lm={}
 for tag,a,b,c,d in difflib.SequenceMatcher(a=old.split('\n'),b=new.split('\n'),autojunk=False).get_opcodes():
  if tag=='equal':
   for i in range(a,b):lm[str(i+1)]={'start':c+i-a+1,'end':c+i-a+1,'disposition':'Exact predecessor line'}
  elif tag=='replace':
   for i in range(a,b):lm[str(i+1)]={'start':c+1,'end':d,'disposition':'Bounded R12/13 correction'}
  elif tag=='delete':raise AssertionError('unexpected deletion')
 (T/'support'/f'{slug}.line-map.json').write_text(json.dumps(lm,indent=2)+'\n');proof[slug]={'path':str(p),'before_sha256':H(old.encode()),'after_sha256':H(new.encode()),'bytes':len(new.encode()),'full_inverse':True,'original_executable_blocks':len(blocks(old)),'original_executable_blocks_exact':True,'original_full_worked_examples_exact':True,'original_URL_occurrences_retained_in_order':True,'protected_frontmatter_except_content_version_and_date_exact':True,'CTA_attribution_exact':True};ops[slug]=oo
(T/'exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');(T/'preservation-proof.json').write_text(json.dumps(proof,indent=2)+'\n');(T/'R12-R13-writer-script.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(proof,indent=2))
