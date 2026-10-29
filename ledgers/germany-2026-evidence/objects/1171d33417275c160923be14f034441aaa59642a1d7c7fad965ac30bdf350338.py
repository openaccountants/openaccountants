from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;O=P.parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');C=O/'germany-ledger-independent-review-2026-10-29/new-primary-checks';B=O/'germany-ledger-writer-B-2026-10-29';h=lambda b:hashlib.sha256(b).hexdigest()
q=json.loads((P/'own-actual-read-quotes.json').read_text());c=json.loads((B/'source-candidate-catalog.json').read_text());x=c['https://www.gesetze-im-internet.de/estg/__15.html']
q['R05.statute']={**x,'id':'R05.statute','article':'EStG § 15(2)–(3)','native_LF':[15,19],'exact_quote':'\n'.join(Path(x['reader_path']).read_text().split('\n')[14:19]),'read_on':'2026-10-29','qualification':'Own current statute read, interpreted with actual BMF/BFH threshold authorities, not as a rule excluding judicial interpretation.'}
for id,raw,reader,lo,hi,article,url in [
 ('R05.BFH-separability','BFH-VIIIR6-12.pdf','BFH-VIIIR6-12.reader.txt',282,314,'BFH VIII R 6/12, paras 45–50','https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/pdf/STRE201510044?type=1646225765'),
 ('R05.BFH-thresholds','BFH-VIIIR6-12.pdf','BFH-VIIIR6-12.reader.txt',315,378,'BFH VIII R 6/12, paras 51–59','https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/pdf/STRE201510044?type=1646225765'),
 ('R05.BMF-current','EStH15-8.html','EStH15-8.reader.txt',2178,2190,'BMF EStH 2025 H 15.8(5), Bagatellgrenze/separate participation limb','https://grsth.bundesfinanzministerium.de/esth/2025/A-Einkommensteuergesetz/II-Einkommen-2-24b/8-Die-einzelnen-Einkunftsarten-13-24b/b-Gewerbebetrieb-15-17/Paragraf-15/paragraf-15.html')]:
  p=C/reader;q[id]={'id':id,'raw_path':str(C/raw),'raw_sha256':h((C/raw).read_bytes()),'reader_path':str(p),'reader_sha256':h(p.read_bytes()),'native_LF':[lo,hi],'exact_quote':'\n'.join(p.read_text().split('\n')[lo-1:hi]),'article':article,'url':url,'read_on':'2026-10-29','qualification':'Own actual selected reading of exact retained official body, first acquired by independent reviewer; its verdict is not adopted as writer proof.'}
p=P/'sources/BFH-IVR42-19.web-response.json';q['R05.BFH-2022']={'id':'R05.BFH-2022','article':'BFH IV R 42/19, B.III.3, paras 27–33','url':'https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202210200/','web_tool_response_path':str(p),'web_tool_response_sha256':h(p.read_bytes()),'actual_web_lines':[161,178],'exact_quote':'Dies bedeutet zugleich, dass die bisherige Geringfügigkeitsgrenze mit ihrer absoluten und relativen Umsatzgrenze sowohl bei Gewinnen als auch bei Verlusten zu beachten ist. Wird diese Bagatellgrenze überschritten, färben gewerbliche Gewinne und gewerbliche Verluste gleichermaßen ab.','read_on':'2026-10-29','qualification':'Own actual official web reading, retained web-tool response JSON, not original HTML. The full B.III.3 reasoning was read.'}
(P/'own-actual-read-quotes.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
(P/'R05-options-and-selection.md').write_text('''# DE-R05 options before editing, 29 October 2026

Root selected **A**: qualify separable own-origin commercial activity by the inclusive annual net-receipt gates, commercial receipts ≤3% of total net receipts AND ≤€24,500, whether branch profit or loss. Preserve its own commercial classification, the separability premise, and the distinct participation-income limb. Add four boundary controls and actual intake facts to partners/trade. Narrow the already-owned freelancer's universal scope parenthesis to the actual supplied classification route. Actual own EStG15(2)–(3), BFH VIII R6/12 paras45–60, BMF2025 H15.8(5), and own official BFHIVR42/19 BIII3 are pinned in own-actual-read-quotes.json. The BMF source expressly denies the own-activity de minimis test to commercial participation income; trade-tax participation treatment stays on its existing separate decree route.

**B**: remove the universal own-side-activity statement and refer classification to the actual BMF/BFH two-gate method in a named completed sibling. This would supply less immediate method than A and is not selected.

The figures measure annual NET RECEIPTS, not profit, and the denominator includes both separable activities. There is no universal safe harbour for inseparably commercial activity and no transplantation to participation receipts. No original example is modified.
''')
ops=json.loads((P/'exact-operations.json').read_text());oldproof=P/'preservation-proof.json';(P/'first-four-preservation-proof.json').write_bytes(oldproof.read_bytes())
for slug in ['de-partners-and-part-year','de-trade-tax']:
 p=R/'skills/international/germany'/f'{slug}.md';(P/'before'/p.name).write_bytes(p.read_bytes());t=p.read_text();oo=[]
 def add(old,new,reason):assert t.count(old)==1;(oo.append({'old':old,'new':new,'reason':reason}))
 import re
 v=re.search(r'^version: (.+)$',t,re.M).group(1);parts=v.split('.');parts[-1]=str(int(parts[-1])+1);add('version: '+v,'version: '+'.'.join(parts),'Content version')
 if 'last_updated: 2026-10-29' not in t:add(re.search(r'^last_updated: .+$',t,re.M).group(),'last_updated: 2026-10-29','Actual read/correction date')
 method='''**Separable own commercial side activity: annual net-receipt test.** Under the BFH interpretation adopted in BMF EStH 2025 H 15.8(5), an otherwise noncommercial partnership's separable own commercial activity does not reclassify the rest if BOTH `commercial net receipts ≤ 0.03 × total partnership net receipts` AND `commercial net receipts ≤ EUR 24,500` for the assessment period. Total receipts include the commercial and noncommercial activities, excluding VAT. Apply the same test whether the commercial branch makes a profit or a loss. The branch remains commercial in its own right; an inseparably commercial overall activity does not become a free profession under this exception. This own-activity test does not apply to commercial income received through a participation in another partnership; keep that income-tax limb and its separate trade-tax treatment distinct.

For an otherwise qualifying separable professional partnership, total net receipts of EUR 500,000 and commercial net receipts of EUR 15,000 pass both gates exactly; EUR 15,000.01 fails the 3% gate. At total net receipts of EUR 1,000,000, commercial receipts of EUR 24,500 pass both; EUR 24,500.01 fails the absolute gate although below 3%. These are receipts tests, not a profit allowance. The outcome under these two gates is unchanged if the commercial branch has a loss.'''
 if slug=='de-partners-and-part-year':
  old=next(l for l in t.split('\n') if l.startswith('  - **Abfärbung'))
  new='  - **Abfärbung (§ 15(3) no. 1 EStG).** A separable own commercial activity can make the whole activity commercial, subject to the two-gate de minimis exception below, whether that branch makes a profit or a loss. Commercial participation income is a separate limb without that de minimis exception. Its trade-tax treatment follows the separate route in `de-trade-tax`.'
  add(old,new,'DE-R05 qualify universal contamination and distinguish participation')
  old=next(l for l in t.split('\n') if l.startswith('- **Out of scope.** Partnerships'))
  add(old,old+'\n\n'+method,'DE-R05 positive dual-gate classification and four boundary controls')
  old=next(l for l in t.split('\n') if l.startswith('2. **Partners:**'))
  new='2. **Partners:** what the partnership does, who manages it, whether own commercial and professional activities are separable, annual net receipts of each and total net receipts, and whether any commercial income instead comes from a participation. These decide the two-gate exception and separate participation rule. For commercial imprinting, identify every personally liable partner and everyone authorised to manage.'
  add(old,new,'DE-R05 intake replaces inaccurate automatic conclusion')
 else:
  old=next(l for l in t.split('\n') if l.startswith('| A partnership that also carries'))
  new=old.replace('also carries on any commercial activity of its own','also carries on a separable commercial activity of its own').replace('Yes: the whole activity counts as commercial (Abfärbung). The statute prints no minimum amount','The whole activity counts as commercial unless the BFH/BMF two-gate de minimis exception below applies; the commercial branch keeps its own classification')
  add(old,new,'DE-R05 judicial interpretation, not statute-only universal')
  old=next(l for l in t.split('\n') if l.startswith('- **Abfärbung is a partnership rule.**'))
  add(old,old+'\n\n'+method,'DE-R05 positive calculation distinct from participation decree')
  old=next(l for l in t.split('\n') if l.startswith('- What exactly does the business do'))
  add(old,old+' For a partnership, can its own commercial and noncommercial activities be separated, what are each activity\'s and total annual net receipts, and is any commercial income instead from another partnership?','DE-R05 intake facts')
 marker='| Source | URL | Read on |';pos=t.index(marker);end=t.index('\n\n',pos)
 addition='\n| BMF EStH 2025 H 15.8(5), judicial two-gate de minimis interpretation, losses and separate participation-income limb | https://grsth.bundesfinanzministerium.de/esth/2025/A-Einkommensteuergesetz/II-Einkommen-2-24b/8-Die-einzelnen-Einkunftsarten-13-24b/b-Gewerbebetrieb-15-17/Paragraf-15/paragraf-15.html | 2026-10-29 |\n| BFH VIII R 6/12, separability and inclusive net-receipt gates | https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/pdf/STRE201510044?type=1646225765 | 2026-10-29 |\n| BFH IV R 42/19, B.III.3, threshold retained for both gains and losses | https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202210200/ | 2026-10-29 |'
 add(t[pos:end],t[pos:end]+addition,'DE-R05 selected primary judicial/administrative sources')
 ops[slug]=oo
slug='de-einkommensteuer-freelancer';t=(P/'before'/f'{slug}.md').read_text();old='a partnership that also trades is a trade as a whole, § 15(3) no. 1 EStG';assert old in t;ops[slug].append({'old':old,'new':'for partnership commercial classification and the separable own-activity de minimis exception under § 15(3) no. 1 EStG, use `de-partners-and-part-year` and `de-trade-tax`','reason':'DE-R05 align already-owned sibling scope with actual supplied classification method'})
(P/'exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n')
print('R05 sources/options/operations prepared; no Guide edited by this preparation.')
