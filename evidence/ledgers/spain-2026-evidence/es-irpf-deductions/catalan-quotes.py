from pathlib import Path
import json,re
P=Path(__file__).resolve().parent;I={x['key']:x for x in json.loads((P/'source-identities.json').read_text())};A={s:(P/x['reader']).read_text().split('\n') for s,x in I.items()};Q={}
def span(k,s,art,lo,hi):
 Q[k]=[dict(source=s,article=art,url=I[s]['url'],reader=I[s]['reader'],LF_start=i+1,LF_end=i+1,quote=A[s][i],read_on='2026-10-28',line_convention='literal LF') for i in range(lo-1,hi) if A[s][i].strip() and not re.match(r'^\s*(?:\[\[ID:|\[Bloque|Subir|Se (?:modifica|añade)|Seleccionar redacción:|Texto (?:añadido|original)|Última actualización|Modificación publicada)',A[s][i])]
def art(k,s,n):
 a=A[s];st=next(i for i,x in enumerate(a) if x.startswith('Artículo '+n+'.'));en=next((i for i in range(st+1,len(a)) if re.match(r'^(Artículo |Disposición |Se (?:modifica|añade)|Seleccionar redacción:)',a[i])),len(a));span(k,s,n,st+2,en)
for n in ['611-1','612-1','612-2','612-3','612-4','612-5','612-6','612-7','612-8','612-9','612-10','612-11','612-12','613-1']:art('CAT'+n,'S5',n)
for n in ['57','58','59','60','61']:art('Rural'+n,'S15',n)
span('RuralDA1','S15','DA1/DA2',2047,2065);span('RuralDT1','S15','DT1',2137,2147);span('RuralDF10','S15','DF10',2365,2369)
span('July37','S6','37.1–3 new612-13/14/15',3203,3269);span('July126','S6','126 amends ruralDA1.2',9612,9635);span('JulyDF8','S6','DF8',11304,11318)
(P/'Catalan-selected-quotes.pending-read.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
for k in Q:
 if k.startswith('CAT'):print('\n###',k);[print(z['LF_start'],z['quote']) for z in Q[k]]
