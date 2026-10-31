from pathlib import Path
import json,hashlib,copy,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[2];LEDGER=ROOT/'ledgers/es-foral-income-tax.md'
def extend(rows):
 changed=[]
 for z in rows:
  if z['guide_LF']==142 and Path(z['reader']).name=='cace46b9e8c983a501af.pdf.reader.txt':
   a=Path(z['reader']).read_text().split('\n');q=' '.join(' '.join(a[3821:3832]).split());assert q.startswith('6.')and q.endswith('produzca dicho incumplimiento.')
   if z['quote']!=q or z['provision']!='G DF33/2014 article 45.6 (current operative text)':
    changed.append(copy.deepcopy(z));z.update(quote=q,provision='G DF33/2014 article 45.6 (current operative text)')
 return changed
if __name__=='__main__':
 h=P/'history-8d7e9452-before-S-L28';assert not h.exists();h.mkdir()
 for f in ['rows.json','actual-source-read-scopes.json','handover.json','writer-status.md','write-ledger.py']:shutil.copyfile(P/f,h/f)
 shutil.copyfile(LEDGER,h/'ledger.md');assert hashlib.sha256(LEDGER.read_bytes()).hexdigest()=='8d7e9452beb304e35de92515ace56c640c401f21ff4bffb1d5cace75a48ec406'
 rows=json.loads((P/'rows.json').read_text());before=copy.deepcopy(rows);old=extend(rows);assert len(old)==1 and old[0]['id']==225;new=rows[224]
 (h/'before-row225.json').write_text(json.dumps(old[0],ensure_ascii=False,indent=2)+'\n')
 text=LEDGER.read_text();line=next(l for l in text.split('\n')if l.startswith('| 225 |'));after=line.replace(old[0]['quote'],new['quote']).replace(' | '+old[0]['provision']+' | ',' | '+new['provision']+' | ');assert text.count(line)==1 and after!=line;out=text.replace(line,after);assert out.replace(after,line)==text
 LEDGER.write_text(out);(P/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');assert all(b==a for b,a in zip(before,rows)if b['id']!=225)
 scopes=json.loads((P/'actual-source-read-scopes.json').read_text());olds=copy.deepcopy(scopes)
 for z in scopes['rows']:
  if z['row']==225:z.update(provision=new['provision'],LF_start=3822,LF_end=3832,scope='S-L28 own current rule45.6 actually read2026-10-28; version footnote3614–3635 also actually read identifies former45 as vigente31December2025 and new acquisition gate. Historical5 at3717–3722 retained only in predecessor evidence, never relabelled6.',read_owner='Group B writer; current operative clause and version context actually read for S-L28')
 assert all(b==a for b,a in zip(olds['rows'],scopes['rows'])if b['row']!=225);assert scopes['unmatched']==[]
 (P/'actual-source-read-scopes.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
 (P/'S-L28-exact-replacements.json').write_text(json.dumps(dict(finding='S-L28 source coordinate/version only; Guide correct',row=225,before=line,after=after,exact_inverse=True,other_rows_exact=2676,historical_clause={'LF':[3717,3722],'status':'historical45.5 only, preserved in predecessor'},current_clause={'LF':[3822,3832],'status':'current45.6'},version_context_actually_read=[3614,3635]),ensure_ascii=False,indent=2)+'\n')
 script=P/'write-ledger.py';s=script.read_text();assert s.count('L.save()')==1;s=s.replace('L.save()',"current45=runpy.run_path(str(L.p/'S-L28-current-rule.py'))['extend']\ncurrent45(L.rows)\nL.save()");script.write_text(s)
 with(P/'writer-status.md').open('a')as f:f.write('\nS-L28 evidence-only successor: row225 now cites full current G45.6 native3822–3832. Version footnote3614–3635 was actually read and identifies former45 as vigente31December2025; predecessor row’s historical45.5 is preserved as historical only. No renumbering of historical text. Exact one-line/row delta and all other2676rows unchanged, with only affected read scope updated. No Guide/figure/oa change.\n')
 assert new['quote']in' '.join(Path(new['reader']).read_text().split())
 (P/'S-L28-checks.json').write_text(json.dumps(dict(row=225,literal_current_quote_match=True,first_clause_number='6',full_end_present=True,other_rows_exact=2676,guide_sha256=hashlib.sha256((ROOT/'skills/international/spain/es-foral-income-tax.md').read_bytes()).hexdigest(),raw_sha256=new['raw_sha256'],reader_sha256=hashlib.sha256(Path(new['reader']).read_bytes()).hexdigest()),indent=2)+'\n')
 paths=[ROOT/z['path']for z in json.loads((h/'handover.json').read_text())]+[P/'S-L28-current-rule.py',P/'S-L28-exact-replacements.json',P/'S-L28-checks.json'];pins=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=len(p.read_bytes()))for p in paths];(P/'handover.json').write_text(json.dumps(pins,indent=2)+'\n')
 for p in[LEDGER,P/'rows.json',P/'actual-source-read-scopes.json',P/'handover.json',P/'S-L28-exact-replacements.json']:print(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),len(p.read_bytes()))
