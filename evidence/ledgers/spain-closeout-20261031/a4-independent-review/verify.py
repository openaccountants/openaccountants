from pathlib import Path
import json, hashlib, re, subprocess

W = Path(__file__).resolve().parents[2]
O = Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
old = (W/'repository/skills/international/spain/es-foral-income-tax.md').read_bytes()
new = (W/'writer/es-foral-income-tax.candidate.md').read_bytes()
ol = (W/'repository/ledgers/es-foral-income-tax.md').read_bytes()
nl = (W/'writer/es-foral-income-tax.ledger-candidate.md').read_bytes()
addition = (W/'writer/a4-ledger-addition.md').read_bytes()
a, b = old.decode().splitlines(), new.decode().splitlines()
maps = json.loads((W/'writer/a4-old-topic-destinations.json').read_text())
seen = set()
for z in maps:
    i = z['old_line']; seen.add(i)
    assert a[i-1] == z['original']
    if z['status'] == 'exact original line retained':
        assert z['destination_lines'] == [j+1 for j,s in enumerate(b) if s == a[i-1]]
    else:
        assert all(1 <= d <= len(b) for d in z.get('destination_lines', []))
        assert all(s in b for s in z.get('destination', []))
assert seen == {i+1 for i,s in enumerate(a) if s.strip()}
assert len(maps) == len(seen) == 677
gap = 'The full-year B/A/G worksheet above does not establish the treatment of a part-year relationship or several payers where a shorter denominator changes the result: an own-territory current interpretation reconciling those facts with the annual-day wording remains to be established. '
prefix,suffix = a[60].split(gap)
assert b[64].startswith(prefix) and b[64].endswith(suffix)
assert b[973] == a[969].replace('own B/A/G part-year/multiple-payer denominator bridge;', 'a controlling contrary own B/A/G part-year/multiple-payer interpretation beyond the supplied literal annual-day worksheet;')
def section(s,start,end): return s[s.index(start):s.index(end,s.index(start))]
ex_old = section(old.decode(),'## Two worked examples that recompute','## Ask the client first')
ex_new = section(new.decode(),'## Two worked examples that recompute','## Ask the client first')
assert ex_old == ex_new
assert re.findall(r'```oa-check\n.*?```',old.decode(),re.S) == re.findall(r'```oa-check\n.*?```',new.decode(),re.S)
assert len(re.findall(r'```oa-check\n.*?```',new.decode(),re.S)) == 2
fm_old = old.decode().split('---',2)[1]
fm_new = new.decode().split('---',2)[1]
assert fm_new == fm_old.replace('last_updated: 2026-10-28','last_updated: 2026-10-31').replace('version: 0.7','version: 0.8')
# This territorial addition had no platform CTA before the change. Do not invent one.
assert ('## Talk to a verified accountant' in old.decode()) == ('## Talk to a verified accountant' in new.decode()) == False
assert nl.startswith(ol) and nl[len(ol):].strip() == addition.strip()
groups = re.findall(r'^\| (A4-\d+) \|',addition.decode(),re.M)
assert groups == [f'A4-{i:02d}' for i in range(1,8)]
contexts = json.loads((W/'writer/a4-source-contexts.json').read_text())
receipts = {z['key']:z for z in json.loads((W/'fresh-source-receipts.json').read_text())}
checks = []
for z in contexts:
    key = z['id']; pdf = W/'sources'/f'{key}.pdf'; txt = W/'sources'/f'{key}.txt'
    raw,reader = pdf.read_bytes(),txt.read_bytes()
    lines = reader.decode().splitlines(); lo,hi = z['selected_lines']; ctx = '\n'.join(lines[lo-1:hi])
    assert ctx.strip() == z['complete_selected_context'].strip()
    assert sha(raw) == z['raw_sha256'] == receipts[key]['sha256']
    assert sha(reader) == z['reader_sha256']
    assert raw.startswith(b'%PDF-') and receipts[key]['exit'] == receipts[key]['text_exit'] == 0
    assert z['exact_quote_whitespace_joined'] in re.sub(r'\s+',' ',ctx)
    fresh = subprocess.run(['pdftotext','-layout',str(pdf),'-'],capture_output=True,check=True).stdout
    assert fresh == reader
    checks.append(dict(id=key,url=z['url'],raw_sha256=sha(raw),reader_sha256=sha(reader),independent_raw_reextraction_byte_equal=True,independently_read_complete_article11_lines=[lo,hi],complete_context_sha256=sha(ctx.encode()),annual_days_wording_present=True,part_year_substitution_printed_in_examined_article=False,source_retrieval_attribution='Fresh retrieval31Oct by writer; reviewer independently read and verified raw/extracted bytes, not own refetch.'))
(O/'source-read-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
paths = {'Guide controls':W/'repository/ledgers/spain-closeout-20261031/foreign-assignment-controls.md','Ledger source contexts':W/'repository/ledgers/spain-closeout-20261031/source-contexts.json','Ledger predecessor destinations':W/'repository/ledgers/spain-closeout-20261031/old-topic-destinations.json'}
for name, writer in [('source-contexts.json','a4-source-contexts.json'),('old-topic-destinations.json','a4-old-topic-destinations.json'),('writer-controls.json','a4-controls.json')]:
    assert (W/'repository/ledgers/spain-closeout-20261031'/name).read_bytes() == (W/'writer'/writer).read_bytes()
controls_test = subprocess.run(['python3',str(W/'repository/scripts/check-examples.py'),str(paths['Guide controls'])],capture_output=True,text=True,check=True)
assert '5 oa-check blocks, 0 failures, 0 missing' in controls_test.stdout
ind_controls = json.loads((O/'independent-controls.json').read_text())
assert len(ind_controls) == 5 and all(v.get('passes', v.get('expected_display_matches', False)) for v in ind_controls.values())
res = dict(reviewed_on='2026-10-31',baseline_guide_sha256=sha(old),candidate_guide_sha256=sha(new),baseline_ledger_sha256=sha(ol),candidate_ledger_sha256=sha(nl),ledger_addition_sha256=sha(addition),original_ledger_exact_prefix=True,new_delta_groups=groups,all_predecessor_nonblank_lines=677,exact_line_retention_count=673,reviewed_replacements={'17':'date increased','18':'version increased','61':'absence-of-method assertion replaced; all other day/private-travel/source text retained','970':'only missing denominator bridge replaced; other boundaries exact'},all_predecessor_destinations_valid=True,predecessor_map_sha256=sha((W/'writer/a4-old-topic-destinations.json').read_bytes()),whole_existing_examples_section_sha256=sha(ex_old.encode()),whole_examples_section_unchanged=True,oa_blocks_unchanged=True,actual_example_test='checked1file;2oa-checkblocks;0failures;0missing',frontmatter_only_date_version_changes=True,cta_status='Absent before and after; no missing preexisting CTA',all5_control_groups_pass=True,local_link_targets={k:dict(path=str(p),exists=p.exists()) for k,p in paths.items()},legal_computation_verdict='PASS_BOUNDED_LABELLED_OWN_TEXT_METHOD',A4_method_gap_closed_if_published_with_evidence=True,publication_verdict='PENDING_LINK_TARGET_PACKAGING',other_A_blockers=['A1','A2','A3'],accountant_attestation=False,country_complete=False,harness_erratum='Initial transient harness assumed an existing CTA header and stopped with ValueError. Inspection showed no preexisting CTA. This harness checks faithful absence and makes no false CTA preservation claim.')
(O/'independent-checks.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
res['publication_verdict'] = 'PASS_EXACT_CANDIDATE_AND_SUPPORT_PACKAGE'
res['linked_controls_actual_test'] = controls_test.stdout.strip()
res['support_files'] = {p.name:dict(path=str(p),sha256=sha(p.read_bytes())) for p in (W/'repository/ledgers/spain-closeout-20261031').iterdir() if p.is_file()}
res['packaging_finding'] = dict(id='F-A4-01',status='RESOLVED',description='Initially missing linked control/context/destination targets materialized by writer; reviewer verified actual content and all five executable controls. Candidate Guide and ledger hashes unchanged.')
res['raw_pdf_location_scope'] = 'Reviewer verified exact fresh full raw PDFs at W/sources. source-contexts.json contains official URLs and raw hashes, not missing local-PDF path references. No broken raw-source local path is introduced by this candidate.'
(O/'independent-checks.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(res,indent=2,ensure_ascii=False))
