from pathlib import Path
import json,hashlib,copy,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[2];LEDGER=ROOT/'ledgers/es-foral-income-tax.md'
def extend(rows):
 changed=[]
 for z in rows:
  if z['guide_LF']==707 and Path(z['reader']).name=='G47-2013-information-reg.txt' and (z['quote'].startswith('modifican determinados reglamentos')or z['quote'].startswith('118 Este artículo')):
   a=Path(z['reader']).read_text().split('\n');q=' '.join(' '.join(a[4764:4773]).split());pr='G DF47/2013 article54bis amendment note118: DF26/2025 DF1.8, effects1January2026';assert '26/2025'in q and q.endswith('2026.')
   if z['quote']!=q or z['provision']!=pr:changed.append(copy.deepcopy(z));z.update(quote=q,provision=pr)
 return changed
if __name__=='__main__':
 h=P/'history-965a7e29-before-S-L30';assert not h.exists();h.mkdir()
 for f in ['rows.json','actual-source-read-scopes.json','handover.json','writer-status.md','write-ledger.py']:shutil.copyfile(P/f,h/f)
 shutil.copyfile(LEDGER,h/'ledger.md');assert hashlib.sha256(LEDGER.read_bytes()).hexdigest()=='965a7e29d62dd472cde4072c75dc67ad67ecc5fcc81ce6c45a93cf7039ac2cbb'
 rows=json.loads((P/'rows.json').read_text());before=copy.deepcopy(rows);old=extend(rows);assert len(old)==1 and old[0]['id']==1295;new=rows[1294];(h/'before-row1295.json').write_text(json.dumps(old[0],ensure_ascii=False,indent=2)+'\n')
 text=LEDGER.read_text();line=next(l for l in text.split('\n')if l.startswith('| 1295 |'));after=line.replace(old[0]['quote'],new['quote']).replace(' | '+old[0]['provision']+' | ',' | '+new['provision']+' | ');assert text.count(line)==1 and after!=line;out=text.replace(line,after);assert out.replace(after,line)==text;assert all(b==a for b,a in zip(before,rows)if b['id']!=1295)
 LEDGER.write_text(out);(P/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 scopes=json.loads((P/'actual-source-read-scopes.json').read_text());olds=copy.deepcopy(scopes)
 for z in scopes['rows']:
  if z['row']==1295:z.update(provision=new['provision'],LF_start=4765,LF_end=4773,scope='S-L30 actual note118 read2026-10-28: DF26/2025 DF1.8, BOG30December2025 and application1January2026. Surrounding4741–4778 also actually read; note115/2022 retained only as historical evidence, not current amendment authority.',read_owner='Group B writer; correct2026 amendment note actually read for S-L30')
 assert all(b==a for b,a in zip(olds['rows'],scopes['rows'])if b['row']!=1295);assert scopes['unmatched']==[];(P/'actual-source-read-scopes.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
 (P/'S-L30-exact-replacements.json').write_text(json.dumps(dict(finding='S-L30 source coordinate/version only; Guide correct',row=1295,before=line,after=after,exact_inverse=True,other_rows_exact=2676,historical_note115=[4750,4752],current_note118=[4765,4773]),ensure_ascii=False,indent=2)+'\n')
 script=P/'write-ledger.py';s=script.read_text();assert s.count('L.save()')==1;s=s.replace('L.save()',"current54bis=runpy.run_path(str(L.p/'S-L30-current-amendment.py'))['extend']\ncurrent54bis(L.rows)\nL.save()");script.write_text(s)
 with(P/'writer-status.md').open('a')as f:f.write('\nS-L30 evidence-only successor: row1295 quotes actualG54bis amendment note118 at4765–4773: DF26/2025 DF1.8, BOG30December2025, application1January2026. Historicalnote115/DF12/2021 effects2022 remains only in predecessor evidence. Exactlyone row/line and its native scope changed; all other2676rows exact. No Guide/amount/oa change.\n')
 assert new['quote']in' '.join(Path(new['reader']).read_text().split());(P/'S-L30-checks.json').write_text(json.dumps(dict(row=1295,literal_note118_match=True,correct_enactment_and_effect=True,other_rows_exact=2676,guide_sha256=hashlib.sha256((ROOT/'skills/international/spain/es-foral-income-tax.md').read_bytes()).hexdigest(),raw_sha256=new['raw_sha256'],reader_sha256=hashlib.sha256(Path(new['reader']).read_bytes()).hexdigest()),indent=2)+'\n')
 paths=[ROOT/z['path']for z in json.loads((h/'handover.json').read_text())]+[P/'S-L30-current-amendment.py',P/'S-L30-exact-replacements.json',P/'S-L30-checks.json'];pins=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=len(p.read_bytes()))for p in paths];(P/'handover.json').write_text(json.dumps(pins,indent=2)+'\n')
 for p in[LEDGER,P/'rows.json',P/'actual-source-read-scopes.json',P/'handover.json',P/'S-L30-exact-replacements.json']:print(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),len(p.read_bytes()))
