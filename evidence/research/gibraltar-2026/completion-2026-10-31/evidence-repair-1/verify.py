#!/usr/bin/env python3
"""Reproduce frozen statement/quote/preservation bindings, not legal acceptance."""
from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent;R=D.parents[4];E=D.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((D/'checkpoint.json').read_text())
for label in ['guide_bytes_unchanged','initial_review_files_unchanged','repair_files']:
 for f,h in c[label].items():assert sha(R/f)==h,(label,f)
old=json.loads((E/'checkpoint.json').read_text())
assert sha(E/'checkpoint.json')==c['original_writer_checkpoint_sha256']
for label in ['guide_files','evidence_files']:
 for f,h in old[label].items():assert sha(R/f)==h,(label,f)
rows=json.loads((D/'ledger.json').read_text());initial={r['id']:r for r in json.loads((E/'ledger.json').read_text())}
assert len(rows)==35
body=(R/'skills/gibraltar/gi-global-minimum-tax.md').read_text();count=0
for r in rows:
 assert r['statement']==initial[r['id']]['statement']
 assert r['statement_sha256']==hashlib.sha256(r['statement'].encode()).hexdigest()
 assert r['statement'] in body
 for e in r['evidence']:
  reader=R/e['reader_file'];text=reader.read_text();quote=e['quote']
  assert sha(reader)==e['reader_sha256']
  assert quote in text
  assert hashlib.sha256(quote.encode()).hexdigest()==e['quote_sha256']
  # Ensure the selected range covers the actual operative quote, not an earlier contents entry.
  lines=text.split("\n");a,b=e['reader_lines'];linequote='\n'.join(lines[a-1:b])
  assert ''.join(quote.split()) in ''.join(linequote.split()),(r['id'],e['act_article_or_document_section'])
  assert len(quote)<3500,(r['id'],'unexpected broad extraction')
  count+=1
for n in [12,33,34]:
 r=rows[n-1];assert r['evidence']==[] and 'not a statutory obligation' in r['classification']
assert count==104
print('PASS: 35 exact statement bindings, 104 native-source excerpts, all Guide and original writer/reviewer hashes preserved. Bounded legal closure is separate.')
