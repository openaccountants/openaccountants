from pathlib import Path
import json,hashlib,copy,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[2];LEDGER=ROOT/'ledgers/es-foral-income-tax.md'
SPANS={'b26cbbf55000edb7f01a.pdf.reader.txt':(1733,1749),'07a16a8bd5be15b57788.pdf.reader.txt':(1927,1944),'3862507b57a0d844fb13.pdf.reader.txt':(3032,3068)}
def extend(rows):
 changed=[]
 for z in rows:
  if z['guide_LF']==94 and z['quote'].startswith('5.') and Path(z['reader']).name in SPANS:
   lo,hi=SPANS[Path(z['reader']).name];a=Path(z['reader']).read_text().split('\n');q=' '.join(' '.join(a[lo-1:hi]).split());assert all(t in q for t in ['cinco primeros','50 por','directa','indirectamente'])and('mismo grupo'in q)
   if z['quote']!=q:changed.append((z['id'],z['quote'],q,lo,hi));z['quote']=q
 return changed
if __name__=='__main__':
 h=P/'history-7f3efdcc-before-S-L27';assert not h.exists();h.mkdir()
 for f in ['rows.json','actual-source-read-scopes.json','handover.json','writer-status.md','write-ledger.py']:shutil.copyfile(P/f,h/f)
 shutil.copyfile(LEDGER,h/'ledger.md');assert hashlib.sha256(LEDGER.read_bytes()).hexdigest()=='7f3efdcc4ad9cd13615d06643e89e66b18503682a9faef2245628c61e7cc02b3'
 rows=json.loads((P/'rows.json').read_text());before=copy.deepcopy(rows);(h/'before-three-rows.json').write_text(json.dumps([z for z in rows if z['id']in[109,111,113]],ensure_ascii=False,indent=2)+'\n')
 changed=extend(rows);assert [x[0]for x in changed]==[109,111,113]
 text=LEDGER.read_text();ops=[]
 for rid,old,new,lo,hi in changed:
  line=next(l for l in text.split('\n')if l.startswith('| '+str(rid)+' |'));after=line.replace(old,new);assert line!=after and text.count(line)==1;text=text.replace(line,after);ops.append(dict(row=rid,before=line,after=after,reader=rows[rid-1]['reader'],native_LF=[lo,hi],note='G quote retains literal intervening footnotes62/63 and page marker to keep exact native provenance; operative sentence continues at3052.'))
 inv=text
 for op in reversed(ops):inv=inv.replace(op['after'],op['before'])
 assert inv==LEDGER.read_text()
 for b,a in zip(before,rows):assert (dict(b,quote=a['quote'])==a if b['id']in[109,111,113]else b==a)
 LEDGER.write_text(text);(P/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 scopes=json.loads((P/'actual-source-read-scopes.json').read_text());olds=copy.deepcopy(scopes)
 for z in scopes['rows']:
  if z['row']in[109,111,113]:
   lo,hi=SPANS[Path(z['reader']).name];z.update(LF_start=lo,LF_end=hi,scope='S-L27 full own art25.5 selected passage actually read2026-10-28, including timing, prior direct/indirect activity/sameIAE and >50% prior-employer exclusion. G literal footnote/page interruption retained in quotation; operative continuation3052–3068.',read_owner='Group B writer; expanded source quotation actually read for S-L27')
 for b,a in zip(olds['rows'],scopes['rows']):
  if b['row']not in[109,111,113]:assert b==a
 assert scopes['unmatched']==[]
 (P/'actual-source-read-scopes.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
 (P/'S-L27-exact-replacements.json').write_text(json.dumps(dict(finding='S-L27 source-only completion; no Guide error/change',operations=ops,rows_unchanged=2674,exact_inverse=True),ensure_ascii=False,indent=2)+'\n')
 script=P/'write-ledger.py';s=script.read_text();assert s.count('L.save()')==1;s=s.replace('L.save()',"extend25=runpy.run_path(str(L.p/'S-L27-extend-quotes.py'))['extend']\nextend25(L.rows)\nL.save()");script.write_text(s)
 with(P/'writer-status.md').open('a')as f:f.write('\nS-L27 evidence-only successor: own article25.5 rows109/111/113 now include prior direct/indirect activity, sameIAE and >50% prior-employer exclusions, plus complete first-positive/two-period/five-year timing. G literal footnote/page interruption retained so its full native quotation is reproducible. Three selected scopes expanded and actually read. Exact prior7f3efdcc ledger/rows/scopes retained; all other2674rows exact. No Guide/amount/oa change.\n')
 checks=[]
 for z in rows:
  if z['id']in[109,111,113]:
   assert z['quote']in' '.join(Path(z['reader']).read_text().split());checks.append(dict(row=z['id'],full_literal_quote_match=True,includes_activity_exclusions=True,includes_employer_exclusion=True,includes_complete_timing=True,reader_sha256=hashlib.sha256(Path(z['reader']).read_bytes()).hexdigest(),raw_sha256=z['raw_sha256']))
 (P/'S-L27-checks.json').write_text(json.dumps(dict(total_rows=len(rows),changed_rows=3,other_rows_exact=True,guide_sha256=hashlib.sha256((ROOT/'skills/international/spain/es-foral-income-tax.md').read_bytes()).hexdigest(),checks=checks),ensure_ascii=False,indent=2)+'\n')
 paths=[ROOT/z['path']for z in json.loads((h/'handover.json').read_text())];paths += [P/'S-L27-extend-quotes.py',P/'S-L27-exact-replacements.json',P/'S-L27-checks.json'];out=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=len(p.read_bytes()))for p in paths];(P/'handover.json').write_text(json.dumps(out,indent=2)+'\n')
 for p in[LEDGER,P/'rows.json',P/'actual-source-read-scopes.json',P/'handover.json',P/'S-L27-exact-replacements.json']:print(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),len(p.read_bytes()))
