from pathlib import Path
import json,hashlib,re
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');P=O/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29';Q=O/'germany-DE-R09-corporate-rounding-writer-successor-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');p=R/'skills/international/germany/de-trade-tax.md';old=p.read_text();H=lambda b:hashlib.sha256(b).hexdigest();assert H(p.read_bytes())=='d8ca2561b7b20f54a376ef3469679521ecbe0623944c34e1ef57e27709ea74d4'
clause='; any de minimis limit for Abfärbung under § 15(3) no. 1 EStG (case law, not in the statute)';assert old.count(clause)==1
(Q/'R10-options-and-selection.md').write_text('''# DE-R10: scope-status consistency options before editing

**A, selected under standing writer authority:** remove only the obsolete semicolon-delimited reservation that says any Abfärbung de minimis limit is unconfirmed. The sealed R05 positive method already supplies own statutory/BFH/BMF gates, read in full selected scopes; no new tax figure or method is added. Preserve the remaining ELSTER2026 form and Munich2026 decision reservations byte-exact.

**B:** narrow the reservation to an actually unsupplied distinct intersection, with evidence naming that intersection. There is no reason to invent a new hypothetical gap merely to replace this obsolete sentence. A is selected.

Source/read basis stays exactly in the immutable R01–08 own-actual-read-quotes.json R05.BMF-current/BFH-separability/BFH-thresholds/BFH-2022. The earlier stale Sources reservation remains preserved as historical preimage, not silently erased from the earlier sealed review target.
''')
ops=[{'old':'version: 1.2','new':'version: 1.3','reason':'Monotonic content version; actual read date already29October'},{'old':clause,'new':'','reason':'DE-R10 remove only obsolete supplied-method reservation'}];new=old
for x in ops:new=new.replace(x['old'],x['new'],1)
reverse=new
for x in reversed(ops):
 if x['new']=='':
  # Exact inverse uses pinned original complete paragraph rather than an ambiguous empty replacement.
  oldline=next(l for l in old.split('\n') if clause in l);newline=oldline.replace(clause,'');assert reverse.count(newline)==1;reverse=reverse.replace(newline,oldline,1)
 else:reverse=reverse.replace(x['new'],x['old'],1)
assert reverse==old
assert len(new.split('\n'))==len(old.split('\n'));n=next(i for i,l in enumerate(old.split('\n'),1) if clause in l)
(Q/'before'/p.name).write_text(old);(Q/'after'/p.name).write_text(new);(Q/'R10-exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');p.write_text(new)
rows=json.loads((P/'support/de-trade-tax/rows.json').read_text());lines=new.split('\n')
for row in rows:
 lo,hi=row['native_LF'];row['prior_sealed_native_LF']=[lo,hi];row['wording']='\n'.join(lines[lo-1:hi])
 if lo<=n<=hi:row['R10_disposition']='Only obsolete de minimis reservation removed; retained form/Munich reservations exact.'
(Q/'support/trade-rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');topics=json.loads((P/'support/de-trade-tax/old-topic-destinations.json').read_text());topics['predecessor_sealed_current_Guide_sha256']=topics['current_Guide_sha256'];topics['current_Guide_sha256']=H(new.encode());(Q/'support/trade-old-topic-destinations.json').write_text(json.dumps(topics,ensure_ascii=False,indent=2)+'\n')
def e(s):return str(s).replace('|','\\|').replace('\n','<br>')
def anchor(s):return s.lower().replace('.','-').replace('_','-')
t=f'# de-trade-tax: DE-R10 successor figure and rule ledger\n\nCurrent Guide SHA256 `{H(new.encode())}`, {len(new.encode())} bytes; predecessor sealed R01–08 Guide `{H(old.encode())}` / ledger `{H((P/"ledgers/de-trade-tax.md").read_bytes())}`. Same positive tax methods, exact source quotations and old-topic destinations; only the stale supplied-method reservation is removed. All unchanged selected quotations/read provenance remain in [{P}/source-quotes.md]({P}/source-quotes.md). Writer successor, different review pending.\n\n| ID | Section / native LF | Exact current wording | Sources |\n|---|---|---|---|\n'
for row in rows:
 refs=', '.join(f'[{id}]({P}/source-quotes.md#{anchor(id)})' for id in row['source_quote_ids']) or 'Preserved routing/presentation/express remaining reservation/attribution; no new legal figure.'
 t+=f'| {row["id"]} | {e(row["section"])} LF{row["native_LF"]} | {e(row["wording"])} | {refs} |\n'
t+='\n## Complete old-topic destinations\n\nAll prior exact historical units, hashes and dispositions remain in support/trade-old-topic-destinations.json. Native coordinates are unchanged.\n\n| Old reference / LF | Old topic opening | Current destination / disposition |\n|---|---|---|\n'
for k in ['current_main_rows','pre_refresh_rows']:
 for row in topics[k]:t+=f'| {k} LF{row["old_native_LF"]}; {row["old_unit_sha256"]} | {e(row.get("old_exact_opening","Exact original current-main block retained in the original sealed support"))} | {e(row["current_destination"])}; {e(row["disposition"])} |\n'
(Q/'ledgers/de-trade-tax.md').write_text(t)
import difflib
(Q/'support/trade.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before',tofile='after')))
blocks=lambda x:re.findall(r'```oa-(?:check|example)\b.*?```',x,re.S);assert blocks(old)==blocks(new)
start=old.index('## Worked examples') if '## Worked examples' in old else old.index('## Examples');end=old.index('## Ask the client',start);assert old[start:end] in new
urls=lambda x:re.findall(r'https?://[^\s<>|)]+',x);assert urls(old)==urls(new)
assert old[old.index('<!-- openaccountants-cta-block -->'):]==new[new.index('<!-- openaccountants-cta-block -->'):]
assert old.split('---',2)[1].replace('version: 1.2','version: X')==new.split('---',2)[1].replace('version: 1.3','version: X')
pr={'Guide_path':str(p),'before_Guide_sha256':H(old.encode()),'after_Guide_sha256':H(new.encode()),'bytes':len(new.encode()),'ledger_sha256':H(t.encode()),'current_rows':len(rows),'full_inverse':True,'only_obsolete_clause_and_version_changed':True,'both_original_oa_and_full_example_prose_exact':True,'all_original_URL_occurrences_exact':True,'protected_metadata_except_version_exact':True,'CTA_attribution_exact':True,'remaining_form_and_Munich_reservations_exact':True,'native_LF_unchanged':True}
(Q/'R10-proof-and-inventory.json').write_text(json.dumps(pr,indent=2)+'\n');(Q/'R10-writer-script.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(pr,indent=2))
