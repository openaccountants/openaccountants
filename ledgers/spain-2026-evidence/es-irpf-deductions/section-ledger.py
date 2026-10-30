from pathlib import Path
import json,re,hashlib,runpy
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));G=E['ROOT']/'skills/international/spain/es-irpf-deductions.md'
def build(name,Q,M,ranges,notes=''):
 b=G.read_text();rows=[];used=set()
 for lf,sec,u in E['units'](b):
  if not any(lo<=lf<=hi for lo,hi in ranges) or u.startswith('#') or re.match(r'^\|[\s|:-]+$',u):continue
  if u.startswith('|') and re.match(r'^\|[\s|:-]+$',b.split('\n')[lf]):continue
  if lf not in M:raise AssertionError((lf,u[:100]))
  keys=M[lf];zs=[x for k in keys for x in Q[k]];used.update(keys)
  for c in E['clauses'](u):rows.append(dict(lf=lf,section=sec,wording=c,keys=keys,authority='; '.join(dict.fromkeys(x['source']+' '+x['article'] for x in zs)),url='; '.join(dict.fromkeys(x['url'] for x in zs)),quote='; '.join(x['reader']+f' LF{x["LF_start"]}–{x["LF_end"]}: “'+x['quote']+'”' for x in zs),read_on='2026-10-28',status='Exact current wording. Express sourced rule; stated numerical cases are computed from sourced inputs and all applicable gates; disclosed interpretations/reservations remain as worded.'))
 esc=lambda s:str(s).replace('|','\\|').replace('\n','<br>')
 md=f'# es-irpf-deductions: {name} section ledger\n\nGuide SHA256 `{hashlib.sha256(G.read_bytes()).hexdigest()}`. Current scopes {ranges} read in full. Selected exact source paragraphs actually read 2026-10-28; full acquisition does not claim full-body reading. {notes} No Guide edit or independent PASS.\n\n| Current LF | Section | Exact current figure/rule | Act/article | Official URL | Exact original-language quote / scope | Read date/status |\n|---|---|---|---|---|---|---|\n'
 for x in rows:md+='| '+' | '.join(esc(x[k]) for k in ['lf','section','wording','authority','url','quote'])+' |2026-10-28; '+x['status']+' |\n'
 checks=[]
 for k in used:
  for x in Q[k]:
   assert x['quote'] in '\n'.join((P/x['reader']).read_text().split('\n')[x['LF_start']-1:x['LF_end']]),(k,x['LF_start']);checks.append(k+':'+str(x['LF_start']))
 assert all(x['wording'] in b for x in rows)
 (P/f'sections/{name}.md').write_text(md);(P/f'sections/{name}-claim-rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(P/f'sections/{name}-actual-read-quotes.json').write_text(json.dumps([dict(key=k,**x) for k in sorted(used) for x in Q[k]],ensure_ascii=False,indent=2)+'\n');(P/f'{name}-selected-quotes.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n');(P/f'sections/{name}-writer-checks.json').write_text(json.dumps(dict(guide_sha256=hashlib.sha256(G.read_bytes()).hexdigest(),rows=len(rows),exact_native_quoted_paragraphs=len(checks),all_wordings_current=True,source_keys=sorted(used)),indent=2)+'\n');print(name,len(rows),len(checks),hashlib.sha256(md.encode()).hexdigest())
