from pathlib import Path
import json,hashlib,copy,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[2];LEDGER=ROOT/'ledgers/es-foral-income-tax.md'
SPANS={'a7c99b3a159d15f09b51.pdf.reader.txt':(787,923,'Bizkaia NF11/2013 article13.1–7 (operative size/activity/group conditions); BC_size'),'c510a8b86fa0754d0c64.pdf.reader.txt':(799,1171,'Álava NF37/2013 articles13.1–7,14.1(a)/14.2 (operative size and adjusted-asset conditions); AC_size'),'ebe984cc20350ca756ca.pdf.reader.txt':(1368,1777,'Gipuzkoa NF2/2014 articles13.1–7,14.1(a)/14.2 (operative size and adjusted-asset conditions); GC_size')}
def extend(rows):
 changed=[]
 for z in rows:
  if z['guide_LF']==351 and any(x in z['provision']for x in ['BC_size','AC_size','GC_size']):
   lo,hi,provision=SPANS[Path(z['reader']).name];a=Path(z['reader']).read_text().split('\n');q=' '.join(' '.join(a[lo-1:hi]).split());assert '85 por'in q and '250 personas'in q and 'cuantitativo'in q and 'grupo'in q
   if z['quote']!=q or z['provision']!=provision:changed.append(copy.deepcopy(z));z.update(quote=q,provision=provision)
 return changed
if __name__=='__main__':
 h=P/'history-3b32d1e7-before-S-L29';assert not h.exists();h.mkdir()
 for f in ['rows.json','actual-source-read-scopes.json','handover.json','writer-status.md','write-ledger.py']:shutil.copyfile(P/f,h/f)
 shutil.copyfile(LEDGER,h/'ledger.md');assert hashlib.sha256(LEDGER.read_bytes()).hexdigest()=='3b32d1e7e4165647dc623c28029e831a7903ab3bdc9e85d30df8a53912713447'
 rows=json.loads((P/'rows.json').read_text());before=copy.deepcopy(rows);old=extend(rows);assert [z['id']for z in old]==[918,919,920];(h/'before-three-rows.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
 text=LEDGER.read_text();ops=[]
 for b in old:
  a=rows[b['id']-1];line=next(l for l in text.split('\n')if l.startswith('| '+str(b['id'])+' |'));after=line.replace(b['quote'],a['quote']).replace(' | '+b['provision']+' | ',' | '+a['provision']+' | ');assert line!=after and text.count(line)==1;text=text.replace(line,after);ops.append(dict(row=b['id'],before=line,after=after,reader=a['reader'],native_LF=list(SPANS[Path(a['reader']).name][:2])))
 inv=text
 for op in reversed(ops):inv=inv.replace(op['after'],op['before'])
 assert inv==LEDGER.read_text();assert all(b==a for b,a in zip(before,rows)if b['id']not in[918,919,920])
 LEDGER.write_text(text);(P/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 scopes=json.loads((P/'actual-source-read-scopes.json').read_text());olds=copy.deepcopy(scopes)
 for z in scopes['rows']:
  if z['row']in[918,919,920]:
   lo,hi,pr=SPANS[Path(z['reader']).name];z.update(provision=pr,LF_start=lo,LF_end=hi,scope='S-L29 operative own current13 size/activity/85%/staff/shareholder/reference/group text actually read2026-10-28; A/G additionally14.1(a)90day>half test and full14.2 adjustments. Original retained literal reader page markers/footnotes remain in exact quote. No preamble/index treated as authority.',read_owner='Group B writer; retained own corporate primary operative scopes actually read for S-L29')
 assert all(b==a for b,a in zip(olds['rows'],scopes['rows'])if b['row']not in[918,919,920]);assert scopes['unmatched']==[];(P/'actual-source-read-scopes.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
 (P/'S-L29-exact-replacements.json').write_text(json.dumps(dict(finding='S-L29 source-only: fallback preamble/index replaced with operative current own conditions; no Guide error/change',operations=ops,exact_inverse=True,other_rows_exact=2674),ensure_ascii=False,indent=2)+'\n')
 script=P/'write-ledger.py';s=script.read_text();assert s.count('L.save()')==1;s=s.replace('L.save()',"operativeSize=runpy.run_path(str(L.p/'S-L29-operative-size.py'))['extend']\noperativeSize(L.rows)\nL.save()");script.write_text(s)
 with(P/'writer-status.md').open('a')as f:f.write('\nS-L29 evidence-only successor: rows918/919/920 now quote own operative B13, A13+14.1(a)/14.2 and G13+14.1(a)/14.2. Full85% economic operation, size/staff/shareholder, quantitative shareholder limitation, period/annualisation and group conditions are present; A/G asset test and adjustments are explicit. Native reader page/footnote markers retained for exact provenance. Prior preamble/index fallbacks retained as failed evidence history, not authority. Exactly3rows changed; all other2674rows exact. No Guide/figure/oa change.\n')
 checks=[]
 for z in rows:
  if z['id']in[918,919,920]:
   q=z['quote'];assert q in' '.join(Path(z['reader']).read_text().split());assert q.startswith('Artículo 13.')
   if z['id']in[919,920]:assert 'noventa días'in q and 'más de la mitad'in q and '2.'in q and 'contabilidad'in q
   checks.append(dict(row=z['id'],literal_operative_quote_match=True,includes_economic_size_staff_shareholder_group_conditions=True,includes_A_G_adjusted_assets=z['id']in[919,920],raw_sha256=z['raw_sha256'],reader_sha256=hashlib.sha256(Path(z['reader']).read_bytes()).hexdigest()))
 (P/'S-L29-checks.json').write_text(json.dumps(dict(total_rows=len(rows),changed_rows=3,other_rows_exact=2674,guide_sha256=hashlib.sha256((ROOT/'skills/international/spain/es-foral-income-tax.md').read_bytes()).hexdigest(),checks=checks),ensure_ascii=False,indent=2)+'\n')
 paths=[ROOT/z['path']for z in json.loads((h/'handover.json').read_text())]+[P/'S-L29-operative-size.py',P/'S-L29-exact-replacements.json',P/'S-L29-checks.json'];pins=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=len(p.read_bytes()))for p in paths];(P/'handover.json').write_text(json.dumps(pins,indent=2)+'\n')
 for p in[LEDGER,P/'rows.json',P/'actual-source-read-scopes.json',P/'handover.json',P/'S-L29-exact-replacements.json']:print(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),len(p.read_bytes()))
