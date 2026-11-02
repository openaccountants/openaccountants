from pathlib import Path
import json,hashlib,copy,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[2];LEDGER=ROOT/'ledgers/es-foral-income-tax.md';PARTS=[(843,878),(1942,1978)]
def extend(rows):
 changed=[]
 for z in rows:
  if z['guide_LF']==301 and Path(z['reader']).name=='G6-2023-current.txt' and (z['quote'].startswith('Decreto Foral 6/2023') or z['provision'].startswith('G DF6/2023 article11.3(f) and DT1.1–3')):
   a=Path(z['reader']).read_text().split('\n');parts=[dict(LF_start=lo,LF_end=hi,quote=' '.join(' '.join(a[lo-1:hi]).split()))for lo,hi in PARTS];q=' […] '.join(x['quote']for x in parts);pr='G DF6/2023 article11.3(f) and DT1.1–3: two separately quoted operative scopes'
   assert 'diciembre de 2023.'in q and 'Cuidados Auxiliares'in q and 'mismos efectos'in q
   if z['quote']!=q or z['provision']!=pr:changed.append(copy.deepcopy(z));z.update(quote=q,provision=pr,quote_segments=parts)
 return changed
if __name__=='__main__':
 h=P/'history-05f230a5-before-S-L31';h.mkdir(exist_ok=True)
 for f in ['rows.json','actual-source-read-scopes.json','handover.json','writer-status.md','write-ledger.py','check-scopes.py']:
  if (h/f).exists():assert (h/f).read_bytes()==(P/f).read_bytes()
  else:shutil.copyfile(P/f,h/f)
 
 if (h/'ledger.md').exists():assert (h/'ledger.md').read_bytes()==LEDGER.read_bytes()
 else:shutil.copyfile(LEDGER,h/'ledger.md')
 assert hashlib.sha256(LEDGER.read_bytes()).hexdigest()=='05f230a5b10d846c043ffd8b7e7fe8b6f0c823dcad33a6ca0b9e5708e3bb52dc'
 rows=json.loads((P/'rows.json').read_text());before=copy.deepcopy(rows);old=extend(rows);assert len(old)==1 and old[0]['id']==1315;new=rows[1314];(h/'before-row1315.json').write_text(json.dumps(old[0],ensure_ascii=False,indent=2)+'\n')
 text=LEDGER.read_text();line=next(l for l in text.split('\n')if l.startswith('| 1315 |'));after=line.replace(old[0]['quote'],new['quote']).replace(' | '+old[0]['provision']+' | ',' | '+new['provision']+' | ');assert text.count(line)==1 and after!=line;out=text.replace(line,after);assert out.replace(after,line)==text;assert all(b==a for b,a in zip(before,rows)if b['id']!=1315)
 LEDGER.write_text(out);(P/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 scopes=json.loads((P/'actual-source-read-scopes.json').read_text());olds=copy.deepcopy(scopes)
 for z in scopes['rows']:
  if z['row']==1315:
   z.pop('LF_start');z.pop('LF_end');z.update(provision=new['provision'],native_quote_parts=[dict(LF_start=lo,LF_end=hi)for lo,hi in PARTS],scope='S-L31 two separate operative scopes actually read2026-10-28:843–878 credential list and1942–1978 DT1.1–3 including provisional expiry31December2023. Internal […] explicitly omits intervening text; no continuous843–1978 reading claimed. Literal reader page markers retained within each part.',read_owner='Group B writer; both operative selected scopes actually read for S-L31')
 assert all(b==a for b,a in zip(olds['rows'],scopes['rows'])if b['row']!=1315);assert scopes['unmatched']==[];(P/'actual-source-read-scopes.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
 (P/'S-L31-exact-replacements.json').write_text(json.dumps(dict(finding='S-L31 source-only fallback replacement; Guide correct',row=1315,before=line,after=after,exact_inverse=True,other_rows_exact=2676,native_quote_parts=PARTS),ensure_ascii=False,indent=2)+'\n')
 script=P/'write-ledger.py';s=script.read_text();assert s.count('L.save()')==1;s=s.replace('L.save()',"careQualifications=runpy.run_path(str(L.p/'S-L31-care-qualification.py'))['extend']\ncareQualifications(L.rows)\nL.save()");script.write_text(s)
 # Narrow regeneration support: explicit noncontiguous quotations are validated part by part.
 cp=P/'check-scopes.py';s=cp.read_text();needle=" t,n,coords=cache[str(rp)];q=re.sub(r'^\\[…\\] | \\[…\\]$','',z['quote']);i=n.find(q)";assert needle in s
 replacement=""" t,n,coords=cache[str(rp)]
 if z.get('quote_segments'):
  parts=z['quote_segments'];valid=all(part['quote'] in ' '.join(' '.join(t.split('\\n')[part['LF_start']-1:part['LF_end']]).split()) for part in parts)
  if not valid:bad.append(z['id']);continue
  scopes.append(dict(row=z['id'],url=z['url'],provision=z['provision'],raw_sha256=z['raw_sha256'],reader=str(rp),reader_sha256=hashlib.sha256(rp.read_bytes()).hexdigest(),native_quote_parts=[dict(LF_start=q['LF_start'],LF_end=q['LF_end'])for q in parts],read_on='2026-10-28',scope='Explicit noncontiguous selected quotations actually read; internal ellipsis omits intervening text, with each native part validated separately.'))
  continue
 q=re.sub(r'^\\[…\\] | \\[…\\]$','',z['quote']);i=n.find(q)"""
 cp.write_text(s.replace(needle,replacement))
 with(P/'writer-status.md').open('a')as f:f.write('\nS-L31 evidence-only successor: row1315 now has two explicit operative quote parts: G6/2023 native843–878 credential list and1942–1978 DT1.1–3, including provisional expiry31December2023. Internal ellipsis explicitly skips intervening text; native_quote_parts records separate ranges. Prior disclaimer fallback preserved in history. Exactlyone row/line changed; other2676rows exact. Narrow scope-check regeneration support validates each explicit part separately. No Guide/amount/oa change.\n')
 checks=[]
 for part in new['quote_segments']:
  a=Path(new['reader']).read_text().split('\n');assert part['quote']==' '.join(' '.join(a[part['LF_start']-1:part['LF_end']]).split());checks.append(dict(LF_start=part['LF_start'],LF_end=part['LF_end'],literal_match=True))
 (P/'S-L31-checks.json').write_text(json.dumps(dict(row=1315,two_actual_selected_reads=True,noncontinuous_scope_explicit=True,other_rows_exact=2676,guide_sha256=hashlib.sha256((ROOT/'skills/international/spain/es-foral-income-tax.md').read_bytes()).hexdigest(),raw_sha256=new['raw_sha256'],reader_sha256=hashlib.sha256(Path(new['reader']).read_bytes()).hexdigest(),parts=checks),indent=2)+'\n')
 paths=[ROOT/z['path']for z in json.loads((h/'handover.json').read_text())]+[P/'S-L31-care-qualification.py',P/'S-L31-exact-replacements.json',P/'S-L31-checks.json',P/'check-scopes.py'];pins=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=len(p.read_bytes()))for p in paths];(P/'handover.json').write_text(json.dumps(pins,indent=2)+'\n')
 for p in[LEDGER,P/'rows.json',P/'actual-source-read-scopes.json',P/'handover.json',P/'S-L31-exact-replacements.json']:print(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),len(p.read_bytes()))
