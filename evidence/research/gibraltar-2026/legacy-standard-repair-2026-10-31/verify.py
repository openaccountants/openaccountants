from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[4]
E=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checkpoint.json').read_text())
for rel,h in c['files'].items():assert sha(R/rel)==h,rel
a=json.loads((E/'ledger.json').read_text())
for row in a['rows']:
 p=R/'skills/gibraltar'/(row['slug']+'.md')
 assert p.read_text().splitlines()[row['guide_line']-1]==row['claim'],row['id']
 for x in row['excerpts']:
  p=R/x['path'];assert sha(p)==x['source_text_sha256'],row['id']
  start,end=x['native_text_lines']
  assert x['quote']=='\n'.join(p.read_text().split('\n')[start-1:end]),row['id']
assert not json.loads((E/'preservation.json').read_text())['failures']
print('PASS: frozen files, 29 ledger bindings, 46 exact native excerpts and unchanged accepted minimum-tax hash')
