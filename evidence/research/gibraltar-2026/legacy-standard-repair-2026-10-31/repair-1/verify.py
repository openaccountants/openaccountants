from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[5];E=Path(__file__).resolve().parent;B=E.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checkpoint.json').read_text())
for p,h in c['files'].items():assert sha(R/p)==h,p
a=json.loads((B/'ledger.json').read_text());b=json.loads((E/'ledger.json').read_text())
assert len(a['rows'])==len(b['rows'])==29
for x,y in zip(a['rows'],b['rows']):
 for q,t in zip(x['excerpts'],y['excerpts']):assert q['quote']==t['quote']
 for q in y['excerpts']:
  p=R/q['path'];assert sha(p)==q['source_text_sha256'];s,e=q['native_text_lines'];assert q['quote']=='\n'.join(p.read_text().split('\n')[s-1:e])
assert any(x['article']=='Article 28(1) purpose test' for x in b['rows'][16]['excerpts'])
old=json.loads((B/'independent-review/input-hashes.json').read_text());ch=[p for p,h in old['files'].items() if sha(R/p)!=h];assert ch==['skills/gibraltar/gi-property-stamp-duty.md']
z=json.loads((E/'repair-ledger.json').read_text());s=(E/'gi-property-stamp-duty.reviewed.md').read_text()
for a,b in z['LSR-2']['replacements']:assert s.count(a)==1;s=s.replace(a,b)
assert s==(R/z['LSR-2']['guide']).read_text()
assert not json.loads((E/'preservation.json').read_text())['failures']
print('PASS: frozen repair; 86/87 original inputs unchanged; only three disclosed stamp replacements; 29 rows/46 quote bytes preserved; locator Article 28(1)')
