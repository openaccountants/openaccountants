#!/usr/bin/env python3
"""Frozen Benin property review: independent extraction, identity and preservation.

This is additive evidence. It does not modify a Guide, original ledger or source.
Legal verdict notes are the independent reader's findings, not automated validation.
"""
from pathlib import Path
from decimal import Decimal as D
import hashlib
import json
import re
import subprocess
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
WRITER = ROOT / 'evidence/ledgers/benin-property-20261101'
SOURCES = ROOT.parent / 'sources'
BASE = '59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
FROZEN = '29102d1f721ee3bd8feaffa01d520e7fe92f6344'
sys.path.insert(0, str(ROOT / 'scripts'))
import skill_checks

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', s).strip()

def save(name, obj):
    path = OUT / name
    assert not path.exists(), 'Review records are immutable: ' + name
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

# Notes follow a fresh reading of full clauses and their neighbours, not snippets.
TFU = [
    'Art151 charges the annual Benin-situs property contribution; art104(3) merely puts distinct IRF/ORTB on the same title. Separate jobs are correct.',
    'Art152 distinguishes permanently fixed structures, commercial/industrial uncultivated land, and light structures. Its income-producing/commercial override is retained.',
    'Art156(1)-(2) supports whole-year owner at 1 January and the usufruct, emphyteutic and building-lease exceptions, including completion-year split and notice names.',
    'Art156(3)-(4) and original LF15 support payment on behalf of an inaccessible owner and cadastral-only assessment when all listed persons are unknown. No title adjudication inferred.',
    'Art159(1) non-built range is 3-7%; the actual local annual decision is required.',
    'Art159(1) built range is 4-8%; the actual local annual decision is required.',
    'Art159(2) ties 5%/6% fallback to no rate adopted at Code commencement. The Guide correctly refuses to call them universal 2026 rates.',
    'Art157 prescribes rental value and a ministerial method. Purchase price, actual rent and LFR20 public-domain tariffs are not certified substitutes.',
    'Art158 prescribes administrative value at 1 January, market-value determinations, five-year revision and notification, with ministerial bases only under its no-adopted-value condition.',
    'Art159(2) retains prior-year rates after non-notification. Art158(3) actually says taux du quinquennat precedent, so preserving that wording without inventing a new valuation rule is sound.',
    'Art153(1)-(6) exemption screen is accurate as a screen. Exact ownership, recognized sports status and agricultural-use conditions must still be evidenced. No blanket exemption is granted.',
    'Art155 requires non-subdivided land sown/planted/replanted in woods of any species. The Guide does not exempt an ordinary vacant plot.',
    'Art154(1),(3) gives the fourth-following-year entry, principal residence, one grant per person, exclusive family use and changed-use termination from the conversion year.',
    'Art154(2) requires the letter, permit copy, title and timely completion/first-use-year declaration, plus current pre-existing-building TFU. Late discovery rule is preserved.',
    'Arts157-159 support category base times supported local rate; art104(3) supports keeping IRF and ORTB distinct.',
    'Art161(1)-(2) supports simple letter within 30 days of acquisition/completion and the separate address-sign/inscription duty. No authenticated filing claimed.',
    'Art161(3) runs across PDF77-78: au is on the preceding page. The complete French quote and 10 December deadline are correct across that page boundary.',
    'Art162 specifies prior-year total, 50% by 10 February and remaining 50% by 30 April. No unverified first-year proxy or new balance deadline is invented.',
    'Art163 requires tenant/farm-lessee payment on the owner behalf and receipt offset against rent. Separating this from IRF withholding prevents duplicate offsets.',
    'Arts164-165 support mutation responsibility, continued old-owner collection pending mutation, recourse and certified TFU-current mention. Statutory presumptions are not treated as title resolution.',
    'Original LF2 scan PDF2 supports calendar-2026 listed late-charge relief only with full TFU rights payment and landowner IFU. No IRF relief or principal cancellation inferred.',
    'Original LF15/47/48 scans PDF4/14 confirm the cadastral addition and express 1 January 2026 commencement. June fiscal arts1-19/finals read do not replace CGI151-165 or original LF2. Later unidentified instruments remain held.',
]
IRF = [
    'Art101(1) names natural and assimilated persons; the listed State/commune/public-establishment/association/NGO assimilation is limited to exclusively property income.',
    'Art101(2) is a turnover test above 50% and applies to partners of non-IS property-predominant companies. The neighbouring TPVI asset test in art109 is not substituted.',
    'Art102(1) includes furnished, built/non-built, building-lease and accessory rights income, subject to its prior business-profit exclusion. No universal landlord IRF treatment is asserted.',
    'Art104(1) sets 12% for the article103 IRF base.',
    'Art104(2)-(3) adds FCFA4,000 ORTB and requires distinct amounts on the TFU title. This is not a TFU percentage uplift.',
    'Art106(1) withholds 12% of gross rent and reduces that withholding to 10% for IBA/IS landlords. It does not replace the 12% individual IRF charging rule.',
    'Art106(2) exemption concerns natural-person tenants, with an intermediary profits-tax entity exception. It is not an individual-landlord exemption.',
    'Art103(1) adds owner costs contractually shifted to the tenant and subtracts tenant costs paid by the owner. No general expense allowance is supplied by this chapter.',
    'Arts102(2),103(2),157 distinguish reserved owner enjoyment from free third-party use without legal obligation, with art157 valuation for the latter.',
    'Art106(5) requires withholding both performed and remitted for deduction; art106(8) offsets it against instalments. Separate evidence columns are appropriate.',
    'Art106(3) literally says liberatoire while (5)/(8) provide deductions/instalment offsets. The Guide quotes both and does not certify a refund or final IBA/IS liability. Its example is a provisional arithmetic reconciliation, not a payment instruction.',
    'Art105 requires prior-year tenant/rent/withholding statement by 10 February and tax on unwithheld income with it; direct administrative base determination and dispute reference are retained.',
    'Art106(4) ties ordinary remittance to the next-month 10th and expressly ties an advance to the month of actual payment, not subsequent letting months.',
    'Art106(6)-(7) supports Treasury precompte and named monthly statement for State leases, and owner joint responsibility for remittance.',
    'Art106(8) links IRF quarterly instalments to IBA; art66 links IBA payment to IS; art51 supplies quarters, dates and first-acompte penultimate-year regularisation.',
    'Art107(1)-(2) says before 31 January, specifies receipts/withholding/partners/parts, moves the office-abroad filing to property situs and requires company payment for partners on unwithheld income.',
    'Art107(3)-(5) keeps partners annual declaration but prevents re-taxing the share to the extent already paid by the company, and allocates company information/late-remittance sanctions.',
    'June LFR13 signed scan PDF4 adds CGI106(9), Benin-property short/long bookings and rent collection, Beninese/foreign matching operators, hotel-beneficiary exception and platform-owner obligation. Individual guests are not substituted.',
    'Original LF48 has an express 1 January 2026 date. June LFR1 says prior-year income absent contrary specification; LFR13 has no payment cutover, and LFR48-49 repeal/execute without a calendar date. First operational payment/catch-up remains held, not annulled.',
    'Art66 on PDF37 and art51 on PDF32 support the cross-reference timetable. The rental annual statement remains art105 10 February, not the generic IS annual deadline.',
]
assert len(TFU) == 22 and len(IRF) == 20

assert git('rev-parse', 'HEAD').decode().strip() == FROZEN
changed = git('diff', '--name-only', BASE, FROZEN).decode().splitlines()
frozen_files = []
for name in changed:
    data = git('show', FROZEN + ':' + name)
    assert (ROOT/name).read_bytes() == data
    frozen_files.append({'path': name, 'git_blob': git('rev-parse', FROZEN+':'+name).decode().strip(), 'sha256': sha(data)})

baseline = json.loads((WRITER/'preservation-baseline.json').read_text())
assert baseline['base_commit'] == BASE
preserved = []
for item in baseline['files']:
    name = item['path']
    original = git('show', BASE+':'+name)
    assert sha(original) == item['sha256']
    assert git('rev-parse', BASE+':'+name).decode().strip() == item['git_blob']
    if name == 'skills/benin/README.md':
        continue
    assert git('show', FROZEN+':'+name) == original
    if (ROOT/name).exists():
        assert (ROOT/name).read_bytes() == original
    preserved.append({'path': name, 'sha256': sha(original), 'exact': True})
assert sum(x['path'].startswith('skills/') for x in preserved) == 8
assert sum(x['path'].startswith('evidence/') for x in preserved) == 28
original_guides = git('ls-tree','-r','--name-only',BASE,'skills/benin').decode().splitlines()
assert set(original_guides) == {x['path'] for x in preserved if x['path'].startswith('skills/')} | {'skills/benin/README.md'}
assert not [p for p in changed if p.startswith('skills/benin/') and p not in ['skills/benin/README.md','skills/benin/bj-property-tfu.md','skills/benin/bj-rental-income-tax.md']]
rd = json.loads((WRITER/'readme-routing-change.json').read_text())
old_readme = git('show',BASE+':skills/benin/README.md').decode()
expected_readme = old_readme
for replacement in rd['changes']:
    assert expected_readme.count(replacement['before']) == 1
    expected_readme = expected_readme.replace(replacement['before'],replacement['after'])
expected_readme += rd['append_only_addition']
assert expected_readme == (ROOT/'skills/benin/README.md').read_text()
partial = expected_readme.split('partial:\n',1)[1].split('---',1)[0]
assert set(re.findall(r'^  ([A-Z-]+):',partial,re.M)) == {'IT-IND','IT-CORP','VAT','SC','PR','TP','XB'}
assert len(json.loads((WRITER/'old-topic-destinations.json').read_text())['existing_guides']) == 8

source_records = json.loads((WRITER/'source-identities.json').read_text())
for item in source_records:
    data = (SOURCES/item['file']).read_bytes()
    assert sha(data) == item['sha256'] and len(data) == item['bytes']
source_lookup = {item['file']:item for item in source_records}
cgi = subprocess.check_output(['pdftotext','-layout',str(SOURCES/'cgi2026.pdf'),'-']).decode()
cgi_pages = cgi.split('\f')
rows = []
for slug,notes in [('bj-property-tfu',TFU),('bj-rental-income-tax',IRF)]:
    ledger = json.loads((WRITER/(slug+'.json')).read_text())
    human = (WRITER/(slug+'.md')).read_text()
    guide = (ROOT/'skills/benin'/(slug+'.md')).read_text()
    assert len(ledger) == len(notes)
    fm = skill_checks.read_frontmatter(guide)
    checks = skill_checks.run_checks(str(ROOT/'skills/benin'/(slug+'.md')),guide,fm)
    assert len(checks) == 15 and not any(checks.values())
    forbidden = ['review_status','license','authored_by','trust_label','drafted_by','approved_by','validation_status','validated','verified_by','reviewed_by','reviewed_on']
    assert not [key for key in forbidden if key in fm]
    assert 'openaccountants-cta-block' not in guide
    for row,note in zip(ledger,notes):
        assert row['id'] in human and row['rule'] in human
        assert row['exact_french_quote'] in human and row['official_url'] in human
        assert row['act_article'] in human and row['source_sha256'] in human
        assert row['section'] in guide
        assert row['source_sha256'] == source_lookup[row['source_file']]['sha256']
        locator = int(re.search(r'page=(\d+)',row['official_url']).group(1))
        if row['source_file'] == 'cgi2026.pdf':
            quote = norm(row['exact_french_quote'])
            matches = [i+1 for i,p in enumerate(cgi_pages) if quote in norm(p)]
            if row['id'] == 'bj-property-tfu:17':
                # The source sentence crosses a page footer. Remove only standalone
                # page-number lines before testing this continuous sentence.
                across = re.sub(r'(?m)^\s*\d+\s*$', '', cgi_pages[76]+cgi_pages[77])
                assert quote in norm(across)
                matches = [77,78]
            assert locator in matches, (row['id'],locator,matches)
            quote_check = 'Exact wording after whitespace/apostrophe normalization in freshly extracted cached PDF bytes'
        else:
            matches = [locator]
            quote_check = 'Exact wording visually confirmed in the hash-bound signed scan; OCR is a reading aid only'
        rows.append({**row,'verdict':'accepted within stated working-paper scope','review_date':'2026-11-01','reviewed_source_pdf_pages':matches,'quote_check':quote_check,'independent_reason':note})

# Independent arithmetic and decisions, separately from the repository oa-check engine.
examples = [
    {'id':'TFU-1','calculation':'1,200,000 x 6% = 72,000; 8,000,000 x 5% = 400,000; total 472,000','values':[str(D(1200000)*D('.06')),str(D(8000000)*D('.05')),str(D(1200000)*D('.06')+D(8000000)*D('.05'))],'decision':'Different statutory categories require different supported bases. 6%/5% are assumed actual local facts within the ranges, not national rates.'},
    {'id':'TFU-2','calculation':'2023 + 4 = 2027; 900,000 x 6% = 54,000','values':[2023+4,str(D(900000)*D('.06'))],'decision':'Valid exclusive principal-residence use would still be exempt in 2026; full commercial conversion in 2026 ends the remaining exemption from that year. No proration invented.'},
    {'id':'IRF-1','calculation':'2,400,000 + 120,000 - 60,000 = 2,460,000; x12% = 295,200; +4,000 -288,000 = 11,200','values':[str(D(2400000)+D(120000)-D(60000)),str((D(2400000)+D(120000)-D(60000))*D('.12')),str((D(2400000)+D(120000)-D(60000))*D('.12')+D(4000)-D(288000))],'decision':'Receipt-backed withholding is kept separate from adjusted base and ORTB. 11,200 is labelled an arithmetic reconciliation before instalments, not an authenticated payable balance or a resolution of final-withholding/ORTB settlement.'},
    {'id':'IRF-2','calculation':'150,000 x 6 = 900,000; x12% =108,000; exempt direct individual tenant withholding 0; business-landlord x10%=90,000','values':[str(D(150000)*D(6)),str(D(900000)*D('.12')),0,str(D(900000)*D('.10'))],'decision':'5 May advance remits by 10 June, not each future letting month. Direct natural-person tenant is exempt under art106(2), but landlord IRF is not extinguished. IBA/IS branch computes withholding only. No platform is assumed.'},
]
assert examples[0]['values'] == ['72000.00','400000.00','472000.00']
assert examples[1]['values'] == [2027,'54000.00']
assert examples[2]['values'] == ['2460000','295200.00','11200.00']
assert examples[3]['values'] == ['900000','108000.00',0,'90000.00']

commands = [
    ['python3','scripts/skill_checks.py','skills/benin/bj-property-tfu.md','skills/benin/bj-rental-income-tax.md'],
    ['python3','scripts/check-examples.py','--require','skills/benin/bj-property-tfu.md','skills/benin/bj-rental-income-tax.md'],
    ['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],
    ['python3','scripts/check-sync-integrity.py','--base',BASE,'--mode','audit','--strict-metadata'],
    ['git','diff','--check',BASE,FROZEN],
]
results = []
for cmd in commands:
    result = subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
    results.append({'command':cmd,'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    assert result.returncode == 0, results[-1]
save('row-verdicts.json',rows)
save('mechanical-preservation.json',{
    'frozen_commit':FROZEN,'base_commit':BASE,'frozen_files':frozen_files,
    'preserved_files':preserved,'preserved_guide_count':8,'preserved_prior_evidence_count':28,
    'rewritten_old_body_units':0,'lost_content_restored':0,
    'readme_exactly_matches_two_partial_explanation_replacements_and_appendix':True,
    'all_seven_domains_partial':True,'no_new_platform_fields_or_cta':True,
    'ledger_human_json_agreement':True,'ledger_rows':42,'source_identities':source_records,
    'independent_examples':examples,'checks':results,
    'warnings':['TFU slug has no standard seven-domain token; README names the separate ownership-tax job.','Rental IRF and salary ITS share IT-IND but are distinct jobs; prior salary Guide unchanged.'],
    'network_note':'Reviewer git fetch origin failed DNS resolution. Review is bound to the local frozen full commit. Parent reported a successful origin fetch immediately before branching from the stated base; parent owns remote/publication reconciliation.',
    'source_acquisition':'No new source acquisition. Existing official source captures were sufficient for every cited check; full source files stay outside Git.',
})
md = ['# Benin property and rental: independent row verdicts','',f'Frozen commit: `{FROZEN}`. Read/review date: 2026-11-01. All 42 rows accepted within the stated partial preparation scope. No accountant attestation or complete-country certification.','',
      '| Ledger row | Act / locator | Verdict and independent reason |','|---|---|---|']
for row in rows:
    md.append('| '+row['id']+' | '+row['act_article']+'; PDF '+','.join(map(str,row['reviewed_source_pdf_pages']))+' | Accepted. '+row['independent_reason'].replace('|','/')+' |')
(OUT/'row-verdicts.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'frozen_commit':FROZEN,'rows_accepted':len(rows),'guide_shapes_passed':30,'examples_passed':4,'preserved_guides':8,'preserved_prior_evidence':28,'rewritten_old_body_units':0},indent=2))
