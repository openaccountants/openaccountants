from pathlib import Path
import json, hashlib, re, subprocess, difflib
from decimal import Decimal as D

W = Path(__file__).resolve().parents[2]
O = Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
old = (W/'repository/skills/international/spain/es-foral-non-resident-tax.md').read_bytes()
new = (W/'writer/es-foral-non-resident-tax.a1-gross-candidate.md').read_bytes()
ol = (W/'repository/ledgers/es-foral-non-resident-tax.md').read_bytes()
nl = (W/'writer/es-foral-non-resident-tax.a1-gross-ledger-candidate.md').read_bytes()
ad = (W/'writer/a1-gross-ledger-addition.md').read_bytes()
ids = json.loads((W/'writer/a1-gross-identity.json').read_text())
assert sha(old)==ids['original_guide_sha256'] and sha(new)==ids['candidate_guide_sha256']
assert sha(ol)==ids['original_ledger_sha256'] and sha(nl)==ids['candidate_ledger_sha256']
assert nl.startswith(ol) and nl[len(ol):].strip()==ad.strip()
a,b = old.decode().splitlines(),new.decode().splitlines()
mp = json.loads((W/'writer/a1-gross-old-topic-destinations.json').read_text())
seen,changed=set(),[]
for z in mp:
    i=z['old_line'];seen.add(i);assert z['original']==a[i-1]
    if z['status']=='exact': assert z['destination_lines']==[j+1 for j,s in enumerate(b) if s==a[i-1]]
    else:
        changed.append(i)
        assert all(1<=j<=len(b) for j in z.get('destination_lines',[]))
assert len(mp)==len(seen)==348 and seen=={i+1 for i,s in enumerate(a) if s.strip()}
assert changed==[21,22,97,245,435]
assert old.decode().split('---',2)[1].replace('last_updated: 2026-10-28','last_updated: 2026-10-31').replace('version: 0.3','version: 0.4')==new.decode().split('---',2)[1]
assert b[96].startswith(a[96].split("Gipuzkoa's final")[0])
assert 'This is the statutory method at current rates' not in b[96]
assert 'prospective basis remains the expressly labelled historical-context interpretation above' in b[96]
assert b[244].split('Apply the statutory exemption/documentation')[1]==a[244].split('Apply the statutory exemption/documentation')[1]
assert b[434].split('; a positive PE')[1]==a[434].split('; a positive PE')[1]
def examples(s): return s[s.index('## Two worked examples that recompute'):s.index('## Ask the client first')]
assert examples(old.decode())==examples(new.decode())
assert len(re.findall(r'```oa-check\n.*?```',new.decode(),re.S))==2
test=subprocess.run(['python3',str(W/'repository/scripts/check-examples.py'),str(W/'writer/es-foral-non-resident-tax.a1-gross-candidate.md')],capture_output=True,text=True,check=True)
assert '2 oa-check blocks, 0 failures, 0 missing' in test.stdout
groups=re.findall(r'^\| (A1R-\d+) \|',ad.decode(),re.M)
assert groups==[f'A1R-{i:02d}' for i in range(1,10)]
ctxs=json.loads((W/'writer/a1-gross-source-contexts.json').read_text())
checks=[]
for stem in ['G-IRNR-2026','G-IRNR-regulation-current','G-NF2-2025-original']:
    pdf=W/'sources'/f'{stem}.pdf';txt=W/'sources'/f'{stem}.txt';raw,rd=pdf.read_bytes(),txt.read_bytes()
    assert raw.startswith(b'%PDF-')
    assert subprocess.run(['pdftotext','-layout',str(pdf),'-'],capture_output=True,check=True).stdout==rd
    uses=[z for z in ctxs if z['id'].startswith(stem)];assert uses
    for z in uses:
        assert z['raw_sha256']==sha(raw) and z['reader_sha256']==sha(rd)
        if 'LF_range' in z:
            lo,hi=z['LF_range'];assert '\n'.join(rd.decode().split('\n')[lo-1:hi]).strip()==z['complete_context'].strip()
    checks.append(dict(id=stem,raw_sha256=sha(raw),reader_sha256=sha(rd),raw_reextraction_byte_equal=True,scope='Full current24/25/31 and full regulation17; original2.Six and following IRNR amendment provisions; original pages8–9 visually read. Not entire36page amendment re-audited.'))
ng=W/'repository/ledgers/spain-2026-evidence/es-foral-non-resident-tax/sources/Gipuzkoa_NF2_2005_arts26_28_195.reader.txt'
ns=ng.read_text();match=re.search(r'^Artículo 11\. Interpretación de las normas tributarias\.\s*\n',ns,re.M);assert match
h=match.start();end=ns.index('Artículo 12.',h);nctx=ns[h:end]
assert 'apartado 1 del artículo 3 del Código Civil' in nctx
checks.append(dict(id='G-NFGT11',reader_sha256=sha(ng.read_bytes()),raw_sha256=sha(ng.with_name('Gipuzkoa_NF2_2005_arts26_28_195.body').read_bytes()),context_sha256=sha(nctx.encode()),scope='Complete operative article11 in retained official text; no new whole-law reading claimed.'))
hist=W/'sources/G-IRNR-historical2020.txt';histpdf=hist.with_suffix('.pdf')
assert subprocess.run(['pdftotext','-layout',str(histpdf),'-'],capture_output=True,check=True).stdout==hist.read_bytes()
hs=hist.read_text();assert re.search(r'6\..{0,50}Cuando se trate',hs,re.S)
checks.append(dict(id='G-IRNR-historical2020',raw_sha256=sha(histpdf.read_bytes()),reader_sha256=sha(hist.read_bytes()),scope='Own historical24.6 expense text and31.2 same retained exclusion; used as historical context, never current rate/base law.'))
(O/'source-read-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
gross,expense,rate=D(20000),D(1200),D('.19');final=(gross-expense)*rate;net=final;grosswh=gross*rate
assert final==D(3572) and grosswh==D(3800) and grosswh-final==D(228) and net-final==0
controls=dict(literal_conditional=dict(gross=str(gross),expense=str(expense),base=str(gross-expense),rate=str(rate),withholding=str(net),final_tax=str(final),refund=str(net-final),arithmetic_pass=True,legal_selection_approved=False),historical_concordance_conditional=dict(base=str(gross),withholding=str(grosswh),final_tax=str(final),refund=str(grosswh-final),arithmetic_pass=True,legal_selection_approved=False),difference=str(grosswh-net),not_an_election=True)
(O/'independent-controls.json').write_text(json.dumps(controls,indent=2)+'\n')
result=dict(verdict='PASS_BOUNDED_OWN_HISTORICAL_CONTEXT_GROSS_METHOD',A1_method_gap_closed_if_applied=True,publication_approved=True,open_findings=[],does_not_hold_net_legally_impossible=True,does_not_approve_gross_as_binding=True,binding_ruling_not_only_admissible_route=True,groups_checked=groups,conditional_arithmetic_pass=True,guide_sha256=sha(new),ledger_sha256=sha(nl),baseline_guide_sha256=sha(old),baseline_ledger_sha256=sha(ol),ledger_exact_original_prefix=True,all348_predecessor_destinations_checked=True,exact_predecessor_lines=343,changed_lines=changed,original_examples_section_unchanged=True,original_examples_sha256=sha(examples(old.decode()).encode()),actual_examples_test=test.stdout.strip(),frontmatter_only_date_version_changes=True,source_facts_and_provenance_pass=True,accountant_attestation=False,country_complete=False,prior_net_rejection_preserved=True,prior_net_rejection_does_not_become_retroactive_PASS=True)

# Independently bind every newly added context to actual native-LF source bytes.
for z in ctxs:
    if z['id'].startswith('G-2020-'):
        raw=(W/'sources/G-IRNR-historical2020.pdf').read_bytes(); rd=(W/'sources/G-IRNR-historical2020.txt').read_bytes()
    elif z['id']=='G-NFGT11':
        raw=ng.with_name('Gipuzkoa_NF2_2005_arts26_28_195.body').read_bytes();rd=ng.read_bytes()
    else: continue
    assert sha(raw)==z['raw_sha256'] and sha(rd)==z['reader_sha256']
    lo,hi=z['LF_range'];assert '\n'.join(rd.decode().split('\n')[lo-1:hi]).strip()==z['complete_context'].strip()
# Current and historical31.2 first paragraph must match in full, not merely its digits.
def exclusion(s):
    x=s.index('2. Los sujetos obligados a retener deberán retener');y=s.index('Sin perjuicio de lo anterior',x)
    return re.sub(r'\s+',' ',s[x:y]).strip()
current=(W/'sources/G-IRNR-2026.txt').read_text(); historic=(W/'sources/G-IRNR-historical2020.txt').read_text()
assert exclusion(current)==exclusion(historic)
result['current_historical31_2_complete_first_paragraph_equal']=True
# Bind materialized source/destination/control targets to reviewed writer files.
base=W/'repository/ledgers/spain-closeout-20261031';support={}
for name,writer in [('a1-source-contexts.json','a1-gross-source-contexts.json'),('a1-old-topic-destinations.json','a1-gross-old-topic-destinations.json'),('a1-writer-controls.json','a1-gross-controls.json')]:
    p=base/name;q=W/'writer'/writer;assert p.read_bytes()==q.read_bytes();support[name]=sha(p.read_bytes())
# Earlier rejected input and complete rejection evidence remain exact.
assert sha((base/'a1-net-rejection/writer-inputs/es-foral-non-resident-tax.a1-candidate.md').read_bytes())=='3727c1fcc8a67afb0c88a1d1842397f7d2d0b4234a812eaa888fa0735d72b3a2'
archive_hashes={}
for q in (W/'review/a1').iterdir():
    if q.is_file():
        p=base/'a1-net-rejection'/q.name
        assert p.read_bytes()==q.read_bytes()
        archive_hashes[q.name]=sha(p.read_bytes())
result['original_net_review_archive_hashes']=archive_hashes
result['harness_erratum']='First archive check used writer/ instead of the actual writer-inputs/ archive directory and stopped. Corrected to the observed directory, then verified all original rejection review artifacts byte for byte; no writer/source change.'
result['support_target_hashes']=support
result['selected_method']='own historical-context gross; rate/expense authority current'
result['residual_interpretation_limit']='No express own concordance ruling, controlling court result or actual assessment is claimed; contrary current-numbering interpretation remains recorded.'
result['resolved_findings']=['F-A1-01 through a newly supported contextual bridge, with original net proposal still rejected','F-A1R-01: ambiguous statutory-method phrase narrowed','F-A1R-02: evidence targets materialized and byte-checked']
controls['literal_conditional']['selected_method']=False
controls['historical_concordance_conditional']['selected_method']=True
controls['historical_concordance_conditional']['legal_selection_approved']='bounded source-derived interpretation only'
(O/'independent-controls.json').write_text(json.dumps(controls,indent=2)+'\n')
(O/'independent-checks.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('Final exact gross candidate and supporting package checks PASS')
