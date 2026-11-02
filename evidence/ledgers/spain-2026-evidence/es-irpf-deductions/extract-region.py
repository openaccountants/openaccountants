from pathlib import Path
import json,re,sys
P=Path(__file__).resolve().parent;I={x['key']:x for x in json.loads((P/'source-identities.json').read_text())};name,s,*nums=sys.argv[1:];a=(P/I[s]['reader']).read_text().split('\n');Q={}
for n in nums:
 st=next(i for i,x in enumerate(a) if re.match(r'^Artículo\s+'+re.escape(n)+r'\.',x));en=next((i for i in range(st+1,len(a)) if re.match(r'^(Artículo\s+|Disposición |Se (?:modifica|añade)|Seleccionar redacción:|Texto (?:añadido|original)|CAPÍTULO|TÍTULO)',a[i])),len(a));zs=[]
 for i in range(st+2,en):
  if a[i].strip() and not re.match(r'^\s*(?:\[\[ID:|\[Bloque|Subir|Jurisprudencia|Última actualización|Modificación publicada)',a[i]):zs.append(dict(source=s,article=n,url=I[s]['url'],reader=I[s]['reader'],LF_start=i+1,LF_end=i+1,quote=a[i],read_on='2026-10-28',line_convention='literal LF'))
 Q[name+n]=zs
(P/f'{name}-selected-quotes.pending-read.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
for k,v in Q.items():
 print('\n###',k)
 for z in v:print(z['LF_start'],z['quote'])
