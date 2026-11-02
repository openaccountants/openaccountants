"""Read-only candidate binding/preservation check; full captures stay outside Git."""
from pathlib import Path
import hashlib, json, re
import yaml
R=Path(__file__).resolve().parents[4]
E=Path(__file__).resolve().parent
D=R.parent/'category-2-private-sources-2026-10-31'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def fm(t): return yaml.safe_load(t.split('---',2)[1])
before=json.loads((E/'before.json').read_text())
for p,h in before['files'].items():
    if p.endswith('/README.md'): continue
    assert sha(R/p)==h,p
old=fm((E/'README.before.md').read_text()); current=fm((R/'skills/gibraltar/README.md').read_text())
assert old['partial']==current['partial'] and len(current['partial'])==7
G=R/'skills/gibraltar/gi-category-2-income-tax.md';text=G.read_text();lines=text.splitlines();meta=fm(text)
assert meta['name']=='gi-category-2-income-tax' and meta['job']=='category-2-individual'
assert 80<=len(meta['description'].split())<=150
assert meta['version']=='0.1' and '# Gibraltar Category 2 certificate, income tax and IT1C v0.1' in text
assert text.count('```oa-check')==4
ledger=json.loads((E/'ledger.json').read_text());receipts=json.loads((E/'source-receipts.json').read_text())['sources'];sources={x['id']:x for x in receipts}
for row in ledger['rows']:
    assert lines[row['guide_line']-1]==row['claim'],row['id']
    assert all(x in ledger['operative_excerpts'] for x in row['excerpts']),row['id']
for k,q in ledger['operative_excerpts'].items():
    s=sources[q['source']];base=D if s['retention']=='private outside Git' else R;p=base/s['text_file'];raw=base/s['raw_file']
    assert sha(p)==q['text_sha256']==s['text_sha256'],k
    assert sha(raw)==s['raw_sha256'],k
    t=p.read_text();a=t.find(q['quote']);assert a>=0,k
    assert hashlib.sha256(q['quote'].encode()).hexdigest()==q['quote_sha256'],k
    assert [t[:a].count('\n')+1,t[:a+len(q['quote'])].count('\n')+1]==q['native_lines'],k
for p in E.rglob('*'):
    assert p.suffix.lower() not in {'.pdf','.html','.png','.jpg'},p
manifest=E/'candidate-manifest.json'
if manifest.exists():
    for p,h in json.loads(manifest.read_text())['files'].items(): assert sha(R/p)==h,p
print(f"PASS: 18 inherited Guides unchanged; seven partial values unchanged; {len(ledger['rows'])} row bindings; {len(ledger['operative_excerpts'])} exact excerpt/source bindings; four controls; {len(meta['description'].split())}-word description; no new full captures in evidence")
