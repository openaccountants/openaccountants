from pathlib import Path
import json,re,hashlib,copy,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[2];LEDGER=ROOT/'ledgers/es-foral-income-tax.md'
SPANS={'b26cbbf55000edb7f01a.pdf.reader.txt':(1604,1612),'07a16a8bd5be15b57788.pdf.reader.txt':(1811,1819),'3862507b57a0d844fb13.pdf.reader.txt':(2887,2896)}
def extend(rows):
 changed=[]
 for z in rows:
  if z['guide_LF']==82 and z['quote'].startswith('b)') and '250' in z['quote']:
   lo,hi=SPANS[Path(z['reader']).name];a=Path(z['reader']).read_text().split('\n');q=' '.join(' '.join(a[lo-1:hi]).split());assert '25 por' in q and 'superior al 65 por' in q and not q.endswith('[…]')
   if z['quote']!=q:changed.append((z['id'],z['quote'],q,lo,hi));z['quote']=q
 return changed
if __name__=='__main__':
 h=P/'history-f80fe1e2-before-S-L26';assert not h.exists();h.mkdir()
 for f in ['rows.json','actual-source-read-scopes.json','handover.json','writer-status.md','write-ledger.py']:
  shutil.copyfile(P/f,h/f)
 shutil.copyfile(LEDGER,h/'ledger.md');assert hashlib.sha256(LEDGER.read_bytes()).hexdigest()=='f80fe1e23ff0d241fa7f23fec697200c6791d17237d7bc6d9eaf54304643a23c'
 rows=json.loads((P/'rows.json').read_text());before=copy.deepcopy(rows);(h/'before-six-rows.json').write_text(json.dumps([z for z in rows if 72<=z['id']<=77],ensure_ascii=False,indent=2)+'\n')
 changed=extend(rows);assert [x[0] for x in changed]==[72,74,76]
 text=LEDGER.read_text();ops=[]
 for rid,old,new,lo,hi in changed:
  line=next(l for l in text.split('\n')if l.startswith('| '+str(rid)+' |'));after=line.replace(old,new);assert line!=after and text.count(line)==1;text=text.replace(line,after);ops.append(dict(row=rid,before=line,after=after,reader=rows[rid-1]['reader'],native_LF=[lo,hi]))
 inv=text
 for op in reversed(ops):inv=inv.replace(op['after'],op['before'])
 assert inv==LEDGER.read_text()
 for b,a in zip(before,rows):
  assert (dict(b,quote=a['quote'])==a if b['id'] in [72,74,76] else b==a)
 LEDGER.write_text(text);(P/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 scopes=json.loads((P/'actual-source-read-scopes.json').read_text());olds=copy.deepcopy(scopes)
 for z in scopes['rows']:
  if z['row'] in [72,74,76]:
   lo,hi=SPANS[Path(z['reader']).name];z.update(LF_start=lo,LF_end=hi,scope='S-L26 expanded full own art23(b) sentence actually read2026-10-28, including mobility≥25% and disability≥65% alternatives; no intervening/full-body claim.',read_owner='Group B writer; expanded source quotation actually read for S-L26')
 for b,a in zip(olds['rows'],scopes['rows']):
  if b['row']not in [72,74,76]:assert b==a
 assert scopes['unmatched']==[]
 (P/'actual-source-read-scopes.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
 (P/'S-L26-exact-replacements.json').write_text(json.dumps(dict(finding='S-L26 source-only quotation completion, no Guide error/change',operations=ops,rows_unchanged=2674,floor_rows_73_75_77_unchanged=True,exact_inverse=True),ensure_ascii=False,indent=2)+'\n')
 script=P/'write-ledger.py';s=script.read_text();assert s.count('L.save()')==1;s=s.replace('L.save()',"extend23=runpy.run_path(str(L.p/'S-L26-extend-quotes.py'))['extend']\nextend23(L.rows)\nL.save()");script.write_text(s)
 with (P/'writer-status.md').open('a')as f:f.write('\nS-L26 evidence-only successor: rows72/74/76 now quote full own article23(b), including BLAM≥25% and disability≥65% alternatives. Floor-only rows73/75/77 and all other2674 rows remain exact. Three native selected scopes expanded and actually read; the complete f80fe1e2 predecessor and six-row evidence are preserved. No Guide, rule, amount or oa change.\n')
 checks=[]
 for z in rows:
  if z['id'] in [72,74,76]:
   q=' '.join(Path(z['reader']).read_text().split());assert z['quote'] in q;checks.append(dict(row=z['id'],full_literal_quote_match=True,includes_25pct_mobility=True,includes_65pct_disability=True,reader_sha256=hashlib.sha256(Path(z['reader']).read_bytes()).hexdigest(),raw_sha256=z['raw_sha256']))
 (P/'S-L26-checks.json').write_text(json.dumps(dict(changed_source_rows=3,total_rows=len(rows),unaffected_exact=True,guide_sha256=hashlib.sha256((ROOT/'skills/international/spain/es-foral-income-tax.md').read_bytes()).hexdigest(),checks=checks),ensure_ascii=False,indent=2)+'\n')
 pins=json.loads((h/'handover.json').read_text());paths=[ROOT/z['path'] for z in pins]
 paths += [P/'S-L26-extend-quotes.py',P/'S-L26-exact-replacements.json',P/'S-L26-checks.json',P/'write-ledger.py']
 out=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=len(p.read_bytes()))for p in paths];(P/'handover.json').write_text(json.dumps(out,indent=2)+'\n')
 for p in [LEDGER,P/'rows.json',P/'actual-source-read-scopes.json',P/'handover.json',P/'S-L26-exact-replacements.json']:print(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),len(p.read_bytes()))
