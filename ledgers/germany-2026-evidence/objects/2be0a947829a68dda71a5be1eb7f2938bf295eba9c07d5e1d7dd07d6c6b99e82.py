from pathlib import Path
import json,hashlib,re,difflib
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');T=O/'germany-DE-R11-R12-writer-successor-2026-10-29';B=O/'germany-ledger-writer-B-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();q=json.loads((T/'own-actual-read-quotes.json').read_text());bq=json.loads((B/'actual-read-quotes.json').read_text())
for id,prior in [('R14.use-or-letting','FR.IAB'),('R15.filing','GT.filing')]:
 x=bq[prior];a,z=x['native_LF'];q[id]={**x,'id':id,'article':x['act_article'],'exact_quote':'\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:z]),'read_on':'2026-10-29','qualification':'Own full selected retained operative clauses actually read; existing main-method branches/conditions are retained; no particular foreign leasing or new exempt-body entitlement inferred.'}
(T/'own-actual-read-quotes.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
(T/'R14-R15-options-and-selection.md').write_text('''# DE-R14–15 options before editing, 29 October 2026

**R14 A, selected:** align only the freelancer cross-border summary with its already-correct main method and own7g(1)/(4)/(6): qualifying own use is in a domestic establishment, while letting is a separate statutory alternative for the required period. Preserve all other profit/asset/timing/use/reporting gates. Do not assert any particular foreign leasing arrangement qualifies. **B:** delete the universal own-use-location sentence and refer directly to the existing qualified two-branch method. Own selected7g paragraphs already retained and actually read; no acquisition or need to restate every other gate.

**R15 A, selected:** add the actual>€5,000 filing branches for the expressly covered other bodies, retaining actual taxable commercial-operation (non-agricultural) and listed partly-exempt/public-law activity conditions. Keep the>€24,500 general branch, all-amount capital-company/cooperative/insurance-association branch, and loss/request overrides. **B:** narrow scope for those bodies and refer the filing method. A is supported by actual own25(1)3–5 and avoids assigning the ordinary sole-trader threshold to these bodies. Exact native7–21 and original-language text/URL/hashes are quoted in own-actual-read-quotes.json.

Separators: qualifying letting is considered under the letting alternative rather than rejected solely for the own-use location condition. An otherwise qualifying private-law body with taxable commercial-operation income€6,000 passes its>€5,000 filing branch despite being below€24,500; exactly€5,000 does not pass that branch, without overriding loss/request facts.
''')
ops=json.loads((T/'exact-operations.json').read_text());proof=json.loads((T/'preservation-proof.json').read_text())
slug='de-einkommensteuer-freelancer';p=R/'skills/international/germany'/f'{slug}.md';old=p.read_text();(T/'before'/p.name).write_text(old);oo=[]
for a,b,why in [('version: 1.5','version: 1.6','Monotonic content version; date already29October'),('- § 7g needs the asset used in a domestic establishment (§ 7g(4)).','- Under § 7g, the own-use alternative requires the qualifying business use in a domestic establishment; letting is a separate statutory alternative for the required period (§ 7g(1), (4), (6)). Apply the main method\'s other asset, profit, timing, use and reporting conditions to the actual arrangement; this does not establish eligibility for a particular foreign leasing arrangement.','DE-R14 align cross-border summary with exact existing main method')]:
 assert old.count(a)==1;oo.append({'old':a,'new':b,'reason':why})
new=old
for x in oo:new=new.replace(x['old'],x['new'],1)
(T/'after'/p.name).write_text(new);p.write_text(new);ops[slug]=oo
slug='de-trade-tax';p=R/'skills/international/germany'/f'{slug}.md';current=p.read_text();oldline=next(l for l in current.split('\n') if l.startswith('**Who must file**'))
old='every non-exempt capital company and cooperative, whatever the amount; a business with a loss carry-forward'
new='every non-exempt capital company, cooperative and insurance mutual association, whatever the amount; other private-law legal persons and associations without legal personality, insofar as they have a commercial operation other than agriculture/forestry whose trade income exceeds EUR 5,000; standing commercial businesses of public-law legal persons whose trade income exceeds EUR 5,000; and the partly exempt businesses listed in § 25(1) no. 5 GewStDV only where they also carry on a taxable activity and taxable trade income exceeds EUR 5,000. The separate overrides remain: a business with a loss carry-forward'
assert current.count(old)==1;ops[slug].append({'old':old,'new':new,'reason':'DE-R15 actual other-body5000 branches, insurance mutual population and preserved overrides'});current=current.replace(old,new,1);(T/'after'/p.name).write_text(current);p.write_text(current)
# Rebuild all exact checks from canonical declared operations/pinned preimages, not from unsealed intermediate hashes.
for slug,oo in ops.items():
 p=R/'skills/international/germany'/f'{slug}.md';old=(T/'before'/p.name).read_text();new=old
 for x in oo:assert new.count(x['old'])==1,(slug,x['reason']);new=new.replace(x['old'],x['new'],1)
 assert new==p.read_text();rev=new
 for x in reversed(oo):assert rev.count(x['new'])==1;rev=rev.replace(x['new'],x['old'],1)
 assert rev==old;blocks=lambda t:re.findall(r'```oa-(?:check|example)\b.*?```',t,re.S);assert blocks(old)==blocks(new)
 if '## Worked framing:' in old:st=old.index('## Worked framing:')
 elif '## Worked examples' in old:st=old.index('## Worked examples')
 else:st=old.index('## Examples')
 end=old.index('## Ask the client',st);assert old[st:end] in new
 fm=lambda s:re.sub(r'(?m)^(version|last_updated):[^\n]*\n','',s.split('---',2)[1]);assert fm(old)==fm(new)
 urls=lambda s:re.findall(r'https?://[^\s<>|)]+',s);it=iter(urls(new));assert all(any(x==y for y in it) for x in urls(old));assert old[old.index('<!-- openaccountants-cta-block -->'):]==new[new.index('<!-- openaccountants-cta-block -->'):]
 (T/'support'/f'{slug}.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before',tofile='after')));lm={}
 for tag,a,b,c,d in difflib.SequenceMatcher(a=old.split('\n'),b=new.split('\n'),autojunk=False).get_opcodes():
  if tag=='equal':
   for i in range(a,b):lm[str(i+1)]={'start':c+i-a+1,'end':c+i-a+1,'disposition':'Exact predecessor line'}
  elif tag=='replace':
   for i in range(a,b):lm[str(i+1)]={'start':c+1,'end':d,'disposition':'Bounded R11–15 correction'}
  elif tag=='delete':raise AssertionError('unexpected deletion')
 (T/'support'/f'{slug}.line-map.json').write_text(json.dumps(lm,indent=2)+'\n');proof[slug]={'path':str(p),'before_sha256':H(old.encode()),'after_sha256':H(new.encode()),'bytes':len(new.encode()),'full_inverse':True,'original_executable_blocks':len(blocks(old)),'original_executable_blocks_exact':True,'original_full_worked_examples_or_framing_exact':True,'original_URL_occurrences_retained_in_order':True,'protected_frontmatter_except_content_version_and_date_exact':True,'CTA_attribution_exact':True}
(T/'exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');(T/'preservation-proof.json').write_text(json.dumps(proof,indent=2)+'\n');(T/'R14-R15-writer-script.py').write_bytes(Path(__file__).read_bytes());print(json.dumps({s:v['after_sha256'] for s,v in proof.items()},indent=2))
