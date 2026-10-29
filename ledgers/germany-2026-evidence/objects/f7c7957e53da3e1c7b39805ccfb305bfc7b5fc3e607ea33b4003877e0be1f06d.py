from pathlib import Path
import json,hashlib,re,difflib
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');T=O/'germany-DE-R11-R12-writer-successor-2026-10-29';A=O/'germany-ledger-writer-2026-10-28';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();T.mkdir(exist_ok=True)
for d in ['before','after','support','ledgers']:(T/d).mkdir(exist_ok=True)
p=R/'skills/international/germany/leaving-germany-exit-tax.md';old=p.read_text();(T/'before'/p.name).write_text(old)
q={}
for id,s,lo,hi,art in [('R11.shares','E17',1,1,'EStG § 17(1) sentences 1–4'),('R11.exit-incorporation','A6',1,1,'AStG § 6(1)'),('R11.separate-residence-test','A6',2,2,'AStG § 6(2)')]:
 x=json.loads((A/'sources'/f'{s}.identity.json').read_text());assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256'];q[id]={**x,'id':id,'article':art,'native_LF':[lo,hi],'exact_quote':'\n'.join(Path(x['reader_path']).read_text().split('\n')[lo-1:hi]),'read_on':'2026-10-29','qualification':'Own full selected actual paragraph read. P001/P002 are derivative reader paragraph locators, not enacted words. Exit/predecessor incorporation is expressly a combined-primary-text interpretation; the separate residence aggregation is not a substitute for the share test.'}
(T/'own-actual-read-quotes.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
(T/'R11-options-and-selection.md').write_text('''# DE-R11 options before editing, 29 October 2026

**A, selected under standing authority:** qualify the personal1% share test by the exact recent free-transfer/predecessor rule of EStG17(1)sentence4. The present holder must have acquired the relevant share free of charge within the five years before the deemed disposal; the holder did not meet the personal1% test, but a predecessor, including an earlier predecessor in successive free transfers, met the1% test within the relevant five-year period under sentence1. Label this as reading AStG6(1)'s17(1)sentence1 reference together with17(1)sentence4's express application of sentence1. This is not an assertion that AStG itself prints all the gift-share conditions. Retain AStG6(2)'s distinct seven/twelve-year residence aggregation and all existing valuation/tax-chain/treaty limitations. Ask for both share and transfer histories.

**B:** withdraw the universal personal holding test and reserve the recent-free-transfer branch pending an interpretation. A is supported as a bounded combined-own-primary reading: AStG deems a disposal of17(1)sentence1 shares, and17(1)sentence4 expressly applies sentence1 to the stated free-acquisition/predecessor facts. No explicit agency ruling or universal tax result is fabricated.

Own full E17 P001 and A6 P001/P002 were actually read; exact quotes, retained hashes/paths and read date are in own-actual-read-quotes.json. A donor's holding is not borrowed without the acquisition/timing conditions, and donor residence history alone never proves the shareholding limb. No new source acquisition.
''')
ops=[]
def add(a,b,why):assert old.count(a)==1,(why,old.count(a));ops.append({'old':a,'new':b,'reason':why})
add('name: leaving-germany-exit-tax','name: leaving-germany-exit-tax\nversion: 0.1','First explicit content-version field; name/slug unchanged')
add('last_updated: 2026-10-15','last_updated: 2026-10-29','Actual source reading/correction date')
oldstep=next(l for l in old.split('\n') if l.startswith('1. Test the shares.'))
newstep='1. Test the shares. § 6 AStG refers to shares within § 17(1) sentence 1 EStG. Test the holder\'s own direct or indirect minimum participation within the last five years, and the recent free-acquisition/predecessor exception below. This uses the combined-source reading of § 6(1) AStG with § 17(1) sentence 4 EStG described under "Which shares". The test concerns the company\'s capital, so shares in a German GmbH and in a foreign company both count. See [§ 17 EStG](https://www.gesetze-im-internet.de/estg/__17.html).'
add(oldstep,newstep,'DE-R11 personal holding is not the only statutory share route')
oldpara=next(l for l in old.split('\n') if l.startswith('**Which shares.**'))
extra='''**Recent free acquisition: combined-source interpretation.** Read § 6(1) AStG's reference to § 17(1) sentence 1 EStG together with § 17(1) sentence 4, which expressly applies sentence 1 to the following predecessor case. If the relevant share was acquired free of charge within the five years before the deemed disposal, a holder who did not personally meet the 1% test must still be tested where the predecessor, or an earlier predecessor in a chain of free transfers, met that participation test within the relevant five-year period under sentence 1. Record the acquisition and each relevant transfer date, direct/indirect holdings and the predecessor's qualifying holding dates. A recent gift or inheritance of a 0.5% share therefore does not fail solely because the current holder never reached 1%, if the qualifying predecessor test is met. This is a separate shareholding rule from the residence-period aggregation in § 6(2) AStG; all other person, trigger and tax-chain conditions still apply.'''
add(oldpara,oldpara+'\n\n'+extra,'DE-R11 exact transfer/share gates and explicit interpretation label')
add('| Minimum shareholding, directly or indirectly, at any time within the last five years | 1% |','| Ordinary personal minimum shareholding, directly or indirectly, at any time within the last five years; recent free acquisitions also use the predecessor rule above | 1% |','DE-R11 table qualifies personal-only statement')
oldask=next(l for l in old.split('\n') if l.startswith('- Which company shares'))
add(oldask,oldask+' What were the highest direct or indirect holdings in the last five years? For a recent gift or inheritance, obtain exact acquisition/transfer dates and the relevant predecessor holdings and dates, including any chain of free transfers.','DE-R11 actual decision-changing evidence')
marker='\n<!-- openaccountants-cta-block -->';add(marker,'\nSelected § 6(1)–(2) AStG and § 17(1) EStG clauses re-read on 29 October 2026 for the predecessor share test and its distinct residence-period conditions; the combined-source interpretation is labelled above.\n'+marker,'DE-R11 scoped actual read date; existing source URL order retained')
new=old
for x in ops:new=new.replace(x['old'],x['new'],1)
rev=new
for x in reversed(ops):assert rev.count(x['new'])==1;rev=rev.replace(x['new'],x['old'],1)
assert rev==old
case=old[old.index('## Worked framing:'):old.index('## Ask the client first')];assert case in new
assert re.findall(r'```oa-(?:check|example)\b.*?```',old,re.S)==re.findall(r'```oa-(?:check|example)\b.*?```',new,re.S)
urls=lambda s:re.findall(r'https?://[^\s<>|)]+',s);assert urls(old)==urls(new)
fm=lambda s:re.sub(r'(?m)^(version|last_updated):[^\n]*\n','',s.split('---',2)[1]);assert fm(old)==fm(new)
assert old[old.index('<!-- openaccountants-cta-block -->'):]==new[new.index('<!-- openaccountants-cta-block -->'):]
(T/'exact-operations.json').write_text(json.dumps({'leaving-germany-exit-tax':ops},ensure_ascii=False,indent=2)+'\n');(T/'after'/p.name).write_text(new);p.write_text(new);(T/'support/exit.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before',tofile='after')))
lm={}
for tag,a,b,c,d in difflib.SequenceMatcher(a=old.split('\n'),b=new.split('\n'),autojunk=False).get_opcodes():
 if tag=='equal':
  for i in range(a,b):lm[str(i+1)]={'start':c+i-a+1,'end':c+i-a+1,'disposition':'Exact original line'}
 elif tag=='replace':
  for i in range(a,b):lm[str(i+1)]={'start':c+1,'end':d,'disposition':'Bounded R11 correction'}
 elif tag=='delete':raise AssertionError('unexpected deletion')
(T/'support/leaving-germany-exit-tax.line-map.json').write_text(json.dumps(lm,indent=2)+'\n')
proof={'leaving-germany-exit-tax':{'path':str(p),'before_sha256':H(old.encode()),'after_sha256':H(new.encode()),'bytes':len(new.encode()),'full_inverse':True,'original_executable_blocks':0,'original_executable_blocks_exact':True,'original_full_worked_framing_exact':True,'original_URL_occurrences_exact':True,'protected_frontmatter_except_content_version_and_date_exact':True,'CTA_attribution_exact':True}}
(T/'preservation-proof.json').write_text(json.dumps(proof,indent=2)+'\n');(T/'R11-writer-script.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(proof,indent=2))
