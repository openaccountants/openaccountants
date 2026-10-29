from pathlib import Path
import json,hashlib,datetime
P=Path(__file__).resolve().parent;O=P.parent;H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();conf=json.loads((O/'germany-publication-preparation-2026-10-29/authorised-inputs.portability-v2.json').read_text());refs=[]
for x in [conf['freeze'],*conf['manifests']]:
 p=Path(x['path']);assert H(p)==x['sha256'];refs.append({**x,'status':'Exact original freeze/manifest unchanged by this writer repair'})
C=O/'germany-ledger-independent-review-2026-10-29'
for name in ['findings-first-PIT.md','findings-employee-PIT.md','finding-DE-R05-abfaerbung.md','finding-DE-R06-partner-summary-qualifications.md','finding-DE-R07-corporate-carry-conditions.md','finding-DE-R08-corporate-withholding-gates.md']:
 p=C/name;refs.append({'path':str(p),'sha256':H(p),'status':'Independent finding actually read; repair is writer work, not self-independent closure'})
(P/'preserved-original-seals-and-finding-references.json').write_text(json.dumps(refs,indent=2)+'\n')
inv=json.loads((P/'successor-inventory.json').read_text());checks=json.loads((P/'writer-checks.json').read_text());rows=sum(x['current_rows'] for x in inv.values());topics=sum(x['old_topics'] for x in inv.values());nq=checks['own_selected_source_anchor_count'];nc=checks['control_count'];cases=checks['original_block_count']
t='''# Germany DE-R01–08 writer successor, 29 October 2026

The eight selected findings are repaired in seven authorised Guides. This is a writer handover for the different country reviewer, not an independent PASS, country-completion claim or accountant attestation. The folder name preserves the original R01–04 assignment; later R05–08 additions are explicitly recorded.

- R01 supplies the ordinary combustion business-car commuting positive-difference computation, actual/logbook alternative, required facts and €1,360 / zero / €480 separators in all three business-income routes. Private-use add-back remains separate; EV/hybrid and family-home-trip rules are not inferred.
- R02 adds the actual qualifying overnight gate, preserves independent non-overnight >8h and full24h branches, and aligns the fuller freelancer prose with its existing overnight table.
- R03 binds the employee child/Soli and employment-cost claims to the full own statutory clauses. The unchanged2026 health/care ceiling is expressly supported by actual current BMG administrative application, independently of the bare special-JAEG amount. Actual BGBl2026/228 replaces223 through Article1no61 under general commencement; its new paragraph4 expressly sets2027. Neither a fictional deferred commencement nor a verbatim current2026 incorporation is claimed.
- R04 qualifies voluntary filing against the complete statutory mandatory test and routes to the actual part-year/Swiss-commuter methods with their named source limits.
- R05 supplies the inclusive separable own-activity net-receipt gates≤3% AND≤€24,500, including gain/loss parity and four boundary computations. The commercial branch retains its own classification; inseparable overall activity and participation-income treatment are distinct. Partners/trade and the freelancer scope are consistent.
- R06 adds the exact34a tax/Soli withdrawal exclusion/priority and15a qualifying outside-liability exception to existing summaries. Detailed elective/exit methods remain referred.
- R07 qualifies EBITDA carry generation, chronological five-year use and old-interest escape restriction, and narrows the partnership trade-tax sentence to commercial partnerships. The precise absence of a full mixed-old/current-interest administrative allocation worksheet remains explicit.
- R08 conditions royalty relief on actual treaty extent and inclusive same-payer/recipient annual remuneration, retaining the return duty. The two-fifths refund retains its actual limited-corporate population, anti-abuse and incorporated refund procedure; no treaty rate is invented.

'''
t+=f'''`successor-inventory.json` binds all seven exact current Guide/ledger hashes. The ledgers contain {rows} current rows and {topics} complete old-topic dispositions, preserving every original current unit and all original historical-topic entries with predecessor and successor coordinates. `own-actual-read-quotes.json` records {nq} own selected source anchors. Unchanged original A/B quotations are reused with attribution in `source-quote-index.json`; acquisition is not counted as reading. No raw source body is duplicated per row.

All {cases} original executable cases and full original worked-example sections remain byte-exact and pass. {nc} new separating writer controls, seven-Guide canonical schema0errors/0warnings, scoped diff check and exact row/native/hash checks pass in `writer-checks.json`. Every Guide has a full inverse, preserved original URL occurrence order, attribution, CTA and protected metadata, with only declared content version/date changes (`preservation-proof.json`, `exact-operations.json`). First-four intermediate pins remain as history. The original country freeze and all four original writer manifests rehash unchanged; no original ledger, Git state, country index, PR, public app or France Guide was changed.

Different reviewer C must close the exact successors. No old whole-country or writer result is silently treated as covering these changed bytes. The private portability build still targets the original authorised country freeze and remains review-pending; it must be rebuilt from a later authorised successor freeze before publication.
'''
(P/'writer-report.md').write_text(t)
# Freeze members exclude the two self-referential seal files. A later correction must use a new successor folder.
entries=[]
for p in sorted(P.rglob('*')):
 if p.is_file() and p.name not in ['artifact-manifest.json','freeze.json'] and '__pycache__' not in p.parts:entries.append({'path':str(p.relative_to(P)),'sha256':H(p),'bytes':p.stat().st_size})
manifest={'status':'Immutable writer successor, different independent review pending','artifacts':entries};mp=P/'artifact-manifest.json';mp.write_text(json.dumps(manifest,indent=2)+'\n')
freeze={'created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'role':'writer, no independent PASS','report':{'path':str(P/'writer-report.md'),'sha256':H(P/'writer-report.md')},'manifest':{'path':str(mp),'sha256':H(mp),'members':len(entries)},'seven_pairs':inv,'original_cases':cases,'writer_controls':nc,'own_selected_source_anchors':nq,'schema_errors':0,'schema_warnings':0,'original_country_freeze_unchanged':True};fp=P/'freeze.json';fp.write_text(json.dumps(freeze,indent=2)+'\n')
for x in entries:assert H(P/x['path'])==x['sha256']
print(json.dumps({'report':freeze['report'],'manifest':freeze['manifest'],'freeze_sha256':H(fp),'cases':cases,'controls':nc,'rows':rows,'old_topics':topics,'pairs':{k:{'Guide':v['Guide_sha256'],'ledger':v['ledger_sha256']} for k,v in inv.items()}},indent=2))
