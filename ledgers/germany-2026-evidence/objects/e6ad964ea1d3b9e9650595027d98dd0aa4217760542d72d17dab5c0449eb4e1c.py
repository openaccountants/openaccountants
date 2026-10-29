from pathlib import Path
import json,hashlib,re,difflib
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');T=O/'germany-DE-R11-R12-writer-successor-2026-10-29';B=O/'germany-ledger-writer-B-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();q=json.loads((T/'own-actual-read-quotes.json').read_text());x=json.loads((B/'actual-read-quotes.json').read_text())['FR.employee-410-relief'];q['R16.employee-410']={**x,'id':'R16.employee-410','article':'EStG § 46(3)','read_on':'2026-10-29','qualification':'Own full retained native LF41 actually read; deduction eligibility and stated reductions only, no wider hardship/age-relief algorithm invented.'};(T/'own-actual-read-quotes.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
(T/'R16-options-and-selection.md').write_text('''# DE-R16 options before editing, 29 October 2026

**A, selected:** qualify the short employee-side-income deduction by actual46(3): eligible taxable non-wage income excludes32d(6) income; when the eligible total≤€410, reduce its deduction by the statutory excess age-relief component and13(3) amount. Keep the separate410 mandatory-assessment statement and no-wage boundary and all three original cases. Exact own full native41/official URL/hash/read date are retained. **B:** label full subtraction as the no-reduction case and refer affected claimants to the precise conditions. A is the narrow actual-clause correction.

Stipulated otherwise eligible€400, statutory excess-age component€100, no farming amount → deduction€300; no reductions→€400. These controls use independently established statutory reduction inputs, not a new unsupported24a or wider hardship method. No new source acquisition.
''')
slug='de-einkommensteuer-freelancer';p=R/'skills/international/germany'/f'{slug}.md';cur=p.read_text();old='if such income is not more than EUR 410 in total it is taken off again.';new='the separate § 46(3) deduction covers eligible taxable non-wage income not assessed under § 32d(6), where that eligible income totals no more than EUR 410. Reduce the deduction by the part of the age-relief amount exceeding the wage-based component under § 24a sentence 5, using wages excluding § 19(2) pension remuneration, and by the § 13(3) amount (§ 46(3) sentence 2).';assert cur.count(old)==1;cur=cur.replace(old,new,1);p.write_text(cur);(T/'after'/p.name).write_text(cur);ops=json.loads((T/'exact-operations.json').read_text());ops[slug].append({'old':old,'new':new,'reason':'DE-R16 actual eligible-income exclusion and statutory reduction components'});(T/'exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n')
proof=json.loads((T/'preservation-proof.json').read_text());before=(T/'before'/p.name).read_text();f=before
for z in ops[slug]:assert f.count(z['old'])==1;f=f.replace(z['old'],z['new'],1)
assert f==cur;rev=cur
for z in reversed(ops[slug]):assert rev.count(z['new'])==1;rev=rev.replace(z['new'],z['old'],1)
assert rev==before;assert re.findall(r'```oa-(?:check|example)\b.*?```',before,re.S)==re.findall(r'```oa-(?:check|example)\b.*?```',cur,re.S)
st=before.index('## Worked examples') if '## Worked examples' in before else before.index('## Examples');end=before.index('## Ask the client',st);assert before[st:end] in cur
lm={}
for tag,a,b,c,d in difflib.SequenceMatcher(a=before.split('\n'),b=cur.split('\n'),autojunk=False).get_opcodes():
 if tag=='equal':
  for i in range(a,b):lm[str(i+1)]={'start':c+i-a+1,'end':c+i-a+1,'disposition':'Exact predecessor line'}
 elif tag=='replace':
  for i in range(a,b):lm[str(i+1)]={'start':c+1,'end':d,'disposition':'Bounded R14/16 summary correction'}
 elif tag=='delete':raise AssertionError('unexpected deletion')
(T/'support'/f'{slug}.line-map.json').write_text(json.dumps(lm,indent=2)+'\n');(T/'support'/f'{slug}.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),cur.splitlines(True),fromfile='before',tofile='after')));proof[slug]['after_sha256']=H(cur.encode());proof[slug]['bytes']=len(cur.encode());(T/'preservation-proof.json').write_text(json.dumps(proof,indent=2)+'\n');(T/'R16-writer-script.py').write_bytes(Path(__file__).read_bytes());print('freelancer',proof[slug]['after_sha256'])
