from pathlib import Path
import hashlib,json,re,difflib
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');P=O/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29';Q=O/'germany-DE-R09-corporate-rounding-writer-successor-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');A=O/'germany-ledger-writer-2026-10-28';Q.mkdir(exist_ok=True);(Q/'ledgers').mkdir(exist_ok=True);H=lambda b:hashlib.sha256(b).hexdigest()
for d in ['before','after','support']:(Q/d).mkdir(exist_ok=True)
p=R/'skills/international/germany/de-corporate-tax.md';old=p.read_text();assert H(p.read_bytes())=='87aaeab2154e651a0dc94832e825030a1a7e2d164881181245393e3d8b5ded1f';(Q/'before'/p.name).write_bytes(p.read_bytes())
x=json.loads((A/'sources/U816365676f95809c.identity.json').read_text());assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256'];q={**x,'id':'R09.assessment-rounding','article':'KStG § 31(1) sentence 2, selected whole paragraph for context','native_LF':[7,7],'exact_quote':Path(x['reader_path']).read_text().split('\n')[6],'read_on':'2026-10-29','qualification':'Own full selected statutory paragraph actually read. Whole-euro assessed corporate-tax rounding in taxpayer favour; no general base/surcharge/refund rounding method inferred.'};(Q/'own-actual-read-quotes.json').write_text(json.dumps({q['id']:q},ensure_ascii=False,indent=2)+'\n')
(Q/'options-and-selection.md').write_text('''# DE-R09: options before editing, 29 October 2026

**A, selected under root's standing authority:** add the actual assessment step after taxable-base work: each individual assessed KSt amount is rounded in the taxpayer's favour to whole euros, KStG31(1)sentence2. Supply the ordinary positive10001×15%=1500.15→1500 separator outside the two protected original examples. Preserve distinct base/surcharge rules and all prior R07/08 qualifications. Exact original-language source/URL/hash/actual read date are in own-actual-read-quotes.json.

**B:** label multiplication as an intermediate amount and refer the final assessment rounding directly to31(1)sentence2. This is less immediately computable than A and is not selected.

This is a minimal successor to the sealed R01–08 seven-Guide writer bundle. That bundle, its source quotations and all historical finding/preimage artifacts remain immutable. Only the corporate Guide/ledger is superseded; the other six pairs remain exact.
''')
newrule='9. **Corporate-tax assessment rounding.** Round each individual assessed corporate-tax amount in the taxpayer\'s favour to whole euros ([§ 31(1) sentence 2 KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html)). For an ordinary positive amount this means rounding down: stipulated taxable income of EUR 10,001 at 15% gives EUR 1,500.15 before rounding and assessed KSt of EUR 1,500. This is the assessed KSt step; underlying bases and surcharges retain their own rules.'
ops=[{'old':'version: 0.3','new':'version: 0.4','reason':'Monotonic content version, date already29October'},{'old':'\n## Deadlines and filing\n','new':'\n'+newrule+'\n\n## Deadlines and filing\n','reason':'DE-R09 exact assessment rule/positive separator outside original examples'}]
for z in ops:assert old.count(z['old'])==1
new=old
for z in ops:new=new.replace(z['old'],z['new'],1)
rev=new
for z in reversed(ops):rev=rev.replace(z['new'],z['old'],1)
assert rev==old
blocks=lambda t:re.findall(r'```oa-(?:check|example)\b.*?```',t,re.S);assert blocks(new)==blocks(old)
start=old.index('## Worked examples') if '## Worked examples' in old else old.index('## Examples');end=old.index('## Ask the client',start);assert old[start:end] in new
urls=lambda t:re.findall(r'https?://[^\s<>|)]+',t);it=iter(urls(new));assert all(any(x==y for y in it) for x in urls(old))
assert old[old.index('<!-- openaccountants-cta-block -->'):]==new[new.index('<!-- openaccountants-cta-block -->'):]
assert re.sub('(?m)^version: .+$','version: X',old.split('---',2)[1])==re.sub('(?m)^version: .+$','version: X',new.split('---',2)[1])
(Q/'exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');(Q/'after'/p.name).write_text(new);p.write_text(new);(Q/'support/Guide.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before',tofile='after')))
sm=difflib.SequenceMatcher(a=old.split('\n'),b=new.split('\n'),autojunk=False);lm={}
for tag,a,b,c,d in sm.get_opcodes():
 if tag=='equal':
  for i in range(a,b):lm[str(i+1)]={'start':c+i-a+1,'end':c+i-a+1}
 elif tag=='replace':
  for i in range(a,b):lm[str(i+1)]={'start':c+1,'end':d}
 elif tag=='delete':raise AssertionError('unexpected deletion')
(Q/'support/native-line-map.json').write_text(json.dumps(lm,indent=2)+'\n')
rows=json.loads((P/'support/de-corporate-tax/rows.json').read_text());oldrows=json.loads(json.dumps(rows));lines=new.split('\n')
for row in rows:
 a,b=row['native_LF'];row['prior_sealed_native_LF']=[a,b];row['native_LF']=[lm[str(a)]['start'],lm[str(b)]['end']];row['wording']='\n'.join(lines[row['native_LF'][0]-1:row['native_LF'][1]])
n=lines.index(newrule)+1;rows.append({'id':f'{len(rows)+1:03d}','predecessor_row_id':None,'native_LF':[n,n],'section':'The taxable base / final assessed KSt','wording':newrule,'source_quote_ids':['R09.assessment-rounding','de-corporate-tax.KStG23'],'classification':'Statutory assessment rule and explicitly stipulated/computed positive example','disposition':'DE-R09 narrow ordinary output-rule correction'})
(Q/'support/rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');topics=json.loads((P/'support/de-corporate-tax/old-topic-destinations.json').read_text())
for row in topics:
 row['prior_sealed_destination']=row['destination'];row['destination']=re.sub(r'current\s*LF\s*(\d+)(?:[–-](\d+))?',lambda m:'current LF'+str(lm[m[1]]['start'])+('–'+str(lm[m[2]]['end']) if m[2] else ''),row['destination'])
 if '15%' in row['wording'] or '15 %' in row['wording']:row['R09_scope_note']='Existing15% rate remains; final ordinary positive assessment rounds down under actual31(1)sentence2, supplied at current LF'+str(n)+'.'
(Q/'support/old-topic-destinations.json').write_text(json.dumps(topics,ensure_ascii=False,indent=2)+'\n')
def e(s):return str(s).replace('|','\\|').replace('\n','<br>')
def anchor(s):return s.lower().replace('.','-').replace('_','-')
t=f'# de-corporate-tax: DE-R09 successor figure and rule ledger\n\nCurrent Guide SHA256 `{H(new.encode())}`, {len(new.encode())} bytes. Predecessor R01–08 Guide `{H(old.encode())}` and ledger `{H((P/"ledgers/de-corporate-tax.md").read_bytes())}` remain sealed at `{P}`. All unchanged quotations retain exact original writer/read provenance in [{P}/source-quotes.md]({P}/source-quotes.md); the sole own expanded source is below. Writer successor, different review pending.\n\n| ID | Section / native LF | Exact current wording | Sources |\n|---|---|---|---|\n'
for row in rows:
 refs=[]
 for id in row['source_quote_ids']:
  target=('../source-quotes.md' if id.startswith('R09.') else str(P/'source-quotes.md'))+'#'+anchor(id);refs.append(f'[{id}]({target})')
 t+=f'| {row["id"]} | {e(row["section"])} LF{row["native_LF"]} | {e(row["wording"])} | '+(', '.join(refs) or 'Preserved routing/presentation/express limitation/attribution; no new positive rule.')+' |\n'
t+='\n## Complete old-topic destinations\n\nAll historical units and predecessor dispositions remain recorded in support/old-topic-destinations.json; only current coordinates and the explicit assessment qualification are rebound.\n\n| Old ref / LF | Exact old topic | Current destination |\n|---|---|---|\n'
for row in topics:t+=f'| {row["ref"]} LF{row["old_lf"]} | {e(row["wording"])} | {e(row["destination"])} {e(row.get("R09_scope_note",""))} |\n'
(Q/'ledgers/de-corporate-tax.md').write_text(t)
(Q/'source-quotes.md').write_text('# DE-R09 own selected source\n\n<a id="r09-assessment-rounding"></a>\n## R09.assessment-rounding\n\nKStG §31(1)sentence2; https://www.gesetze-im-internet.de/kstg_1977/__31.html; actually read2026-10-29, full native LF7. Raw/reader paths/hashes are in own-actual-read-quotes.json.\n\n> '+q['exact_quote']+'\n\nAll earlier exact source anchors and read provenance are preserved by reference to the sealed R01–08 source-quote index, not falsely recorded as new reading.\n')
proof={'prior_seven_writer_manifest':{'path':str(P/'artifact-manifest.json'),'sha256':H((P/'artifact-manifest.json').read_bytes())},'before_Guide_sha256':H(old.encode()),'after_Guide_sha256':H(new.encode()),'Guide_path':str(p),'bytes':len(new.encode()),'ledger_sha256':H(t.encode()),'full_inverse':True,'original_two_oa_exact':True,'original_complete_worked_examples_exact':True,'old_URL_occurrences_retained_in_order':True,'protected_metadata_except_version_exact':True,'CTA_attribution_exact':True,'current_rows':len(rows),'prior_current_rows':len(oldrows),'complete_old_topic_rows':len(topics),'other_six_pairs_unchanged':True}
(Q/'proof-and-inventory.json').write_text(json.dumps(proof,indent=2)+'\n');(Q/'writer-script.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(proof,indent=2))
