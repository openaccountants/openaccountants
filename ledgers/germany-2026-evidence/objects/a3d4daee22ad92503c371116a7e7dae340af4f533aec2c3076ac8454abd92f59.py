from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;A=P.parent/'germany-ledger-writer-2026-10-28';q=json.loads((P/'own-actual-read-quotes.json').read_text());h=lambda b:hashlib.sha256(b).hexdigest()
for id,s,lo,hi,article in [('R06.retained','U04496684f283eed9',7,16,'EStG § 34a(1)–(2)'),('R06.liability','Uaa4bd03133099579',7,11,'EStG § 15a(1)–(4)')]:
 x=json.loads((A/'sources'/f'{s}.identity.json').read_text());assert h(Path(x['raw_path']).read_bytes())==x['raw_sha256'];q[id]={**x,'id':id,'article':article,'native_LF':[lo,hi],'exact_quote':'\n'.join(Path(x['reader_path']).read_text().split('\n')[lo-1:hi]),'read_on':'2026-10-29','qualification':'Own full selected retained operative paragraphs read; existing detailed regime referral remains.'}
(P/'own-actual-read-quotes.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
(P/'R06-options-and-selection.md').write_text('''# DE-R06 options before editing, 29 October 2026

Root selected **Option A**: add own §34a(2) sentences2–3 tax/Soli withdrawal exclusion and statutory priority to the existing retained-profit summary; add own §15a(3) sentence1 qualifying outside-liability exception to the withdrawal add-back summary, with its actual §15a(1) conditions retained. Exact actual own paragraphs and source identities are in own-actual-read-quotes.json. Preserve the detailed scheme referral and both original examples.

**Option B**: remove the incomplete arithmetic definitions and use qualified summaries with actual statutory references, without suggesting a complete method. A is the narrower useful correction of the already supplied formula.

Separators: a stipulated €20,000 withdrawal fully within the tax/Soli exclusion does not mechanically reduce retained profit by €20,000. For a €10,000 negative-capital increase and €8,000 available prior-loss cap, no qualifying outside liability gives €8,000 add-back; €10,000 qualifying coverage gives zero; €6,000 qualifying coverage leaves €4,000, subject to the actual liability conditions and other statutory facts. These are conditional arithmetic controls, not a full elective-regime implementation.
''')
ops=json.loads((P/'exact-operations.json').read_text());slug='de-partners-and-part-year';t=(P/'before'/f'{slug}.md').read_text()
for old,new,reason in [
 ('Withdrawals that create or increase a negative capital account are added as profit, up to the losses that were deductible in that year and the ten years before (§ 15a(3)).','Withdrawals that create or increase a negative capital account are added as profit only to the extent they are not covered by qualifying outside liability that exists or arises because of those withdrawals under § 15a(1) sentence 2, subject to its register, proof and genuine-exposure conditions. The add-back is capped at the losses deductible in that year and the ten years before (§ 15a(3)).','DE-R06 qualifying outside-liability exception and retained cap'),
 ('Profit left in = profit less the positive balance of withdrawals over contributions, plus trade tax (§ 34a(2)).','Profit left in = profit less the positive balance of withdrawals over contributions, plus trade tax (§ 34a(2)). Exclude withdrawals for the income tax under § 34a(1) sentence 1 and its related solidarity surcharge; withdrawals are deemed used first for these taxes up to their amount (§ 34a(2) sentences 2–3).','DE-R06 actual tax/Soli withdrawal exclusion and statutory priority')]:
 assert t.count(old)==1;ops[slug].append({'old':old,'new':new,'reason':reason})
(P/'exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');print('R06 exact own clauses/options/operations prepared before editing.')
