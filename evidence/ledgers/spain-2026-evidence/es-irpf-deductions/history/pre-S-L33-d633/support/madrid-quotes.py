from pathlib import Path
import json,re
P=Path(__file__).resolve().parent;A=(P/'sources/S4.reader.txt').read_text().split('\n');I=json.loads((P/'source-identities.json').read_text());U=next(x['url'] for x in I if x['key']=='S4');Q={}
for art in ['4','5','6','7','7 bis','8','8 bis','8 ter','9','10','10 bis','10 ter','11','11 bis','12','12 bis','12 ter','13','13 bis','14','15','16','17','17 bis','18']:
 st=next(i for i,x in enumerate(A) if re.match(r'^\s*Artículo\s+'+re.escape(art)+r'\.',x));en=next((i for i in range(st+1,len(A)) if re.match(r'^\s*(?:Artículo |Se (?:modifica|añade|renumera)|Seleccionar redacción:|Texto añadido|Téngase en cuenta)',A[i])),len(A));arr=[]
 for i in range(st+1,en):
  s=A[i]
  if not s.strip() or s.startswith(('[Bloque','[[ID:')) or s.strip() in ['Subir','Jurisprudencia']:continue
  arr.append(dict(source='S4',article=art,url=U,reader='sources/S4.reader.txt',LF_start=i+1,LF_end=i+1,quote=s,read_on='2026-10-28',line_convention='literal LF'))
 Q['MAD'+art]=arr
(P/'Madrid-selected-quotes.pending-read.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n');print('Madridselectedparagraphs',sum(len(x) for x in Q.values()))
for art in ['4','5','6','7','7 bis','8','8 bis','8 ter','9','10','10 bis','10 ter']:
 print('\n##MAD',art)
 for x in Q['MAD'+art]:print(x['LF_start'],x['quote'])
