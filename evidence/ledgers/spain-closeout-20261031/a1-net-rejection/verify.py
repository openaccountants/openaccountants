from pathlib import Path
import json, hashlib, re, subprocess, difflib
from decimal import Decimal as D

W = Path(__file__).resolve().parents[2]
O = Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
old = (W/'repository/skills/international/spain/es-foral-non-resident-tax.md').read_bytes()
new = (W/'writer/es-foral-non-resident-tax.a1-candidate.md').read_bytes()
ol = (W/'repository/ledgers/es-foral-non-resident-tax.md').read_bytes()
nl = (W/'writer/es-foral-non-resident-tax.a1-ledger-candidate.md').read_bytes()
ad = (W/'writer/a1-ledger-addition.md').read_bytes()
ids = json.loads((W/'writer/a1-identity.json').read_text())
assert sha(old)==ids['original_guide_sha256'] and sha(new)==ids['candidate_guide_sha256']
assert sha(ol)==ids['original_ledger_sha256'] and sha(nl)==ids['candidate_ledger_sha256']
assert nl.startswith(ol) and nl[len(ol):].strip()==ad.strip()
a,b = old.decode().splitlines(),new.decode().splitlines()
mp = json.loads((W/'writer/a1-old-topic-destinations.json').read_text())
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
assert b[244].split('Apply the statutory exemption/documentation')[1]==a[244].split('Apply the statutory exemption/documentation')[1]
assert b[434].split('; a positive PE')[1]==a[434].split('; a positive PE')[1]
def examples(s): return s[s.index('## Two worked examples that recompute'):s.index('## Ask the client first')]
assert examples(old.decode())==examples(new.decode())
assert len(re.findall(r'```oa-check\n.*?```',new.decode(),re.S))==2
test=subprocess.run(['python3',str(W/'repository/scripts/check-examples.py'),str(W/'writer/es-foral-non-resident-tax.a1-candidate.md')],capture_output=True,text=True,check=True)
assert '2 oa-check blocks, 0 failures, 0 missing' in test.stdout
groups=re.findall(r'^\| (A1-\d+) \|',ad.decode(),re.M)
assert groups==[f'A1-{i:02d}' for i in range(1,8)]
ctxs=json.loads((W/'writer/a1-source-contexts.json').read_text())
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
result=dict(verdict='REJECT_CURRENT_NET_METHOD_FOR_ORDINARY_COMPLETION',A1_closed=False,publication_approved=False,open_findings=['F-A1-01'],does_not_hold_net_legally_impossible=True,does_not_approve_gross_as_settled=True,binding_ruling_not_only_admissible_route=True,groups_checked=groups,conditional_arithmetic_pass=True,guide_sha256=sha(new),ledger_sha256=sha(nl),baseline_guide_sha256=sha(old),baseline_ledger_sha256=sha(ol),ledger_exact_original_prefix=True,all348_predecessor_destinations_checked=True,exact_predecessor_lines=343,changed_lines=changed,original_examples_section_unchanged=True,original_examples_sha256=sha(examples(old.decode()).encode()),actual_examples_test=test.stdout.strip(),frontmatter_only_date_version_changes=True,source_facts_and_provenance_pass=True,accountant_attestation=False,country_complete=False,harness_erratum='An initial transient assertion selected a procedural-law contents heading instead of the operative article11. Corrected selector excludes the contents heading; the actual complete article was read and checked. No source or candidate change made.')
(O/'independent-checks.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,indent=2,ensure_ascii=False))
