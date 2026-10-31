from pathlib import Path
import json
P=Path(__file__).resolve().parent;Q=json.load(open(P/'quotes.json'));I={z['key']:z for z in json.load(open(P/'source-identities.json'))}
def setspan(k,src,art,rr):
 a=(P/'sources'/(src+'.reader.txt')).read_text().splitlines();Q[k]=[]
 for lo,hi in rr:Q[k].append(dict(source=src,article=art,url=I[src]['url'],quote='\n'.join(a[lo-1:hi]),reader='sources/'+src+'.reader.txt',LF_start=lo,LF_end=hi,read_on='2026-10-28'))
a=(P/'sources/S0.reader.txt').read_text().splitlines()
for j,needle in enumerate(['1.ª Contribuyente soltero','2.ª Contribuyente cuyo cónyuge','3.ª Otras situaciones']):
 lo=next(i+1 for i in range(4631,4690) if a[i].strip().startswith(needle));setspan('threshold'+str(j),'S0','81.1',[(lo,lo+3),(4676+2*j,4676+2*j)])
setspan('_undeclared','S0','81.1 third category',[(4680,4686)]);Q['threshold2']+=Q.pop('_undeclared')
lo=next(i+1 for i in range(4880,4940) if a[i].strip()=='0,00')
for j in range(6):setspan('scale'+str(j),'S0','85.1',[(lo+5*j,lo+5*j+3)])
setspan('FOGASA','S6','33.1/2',[(2218,2224)])
setspan('FOGASAmoney','S10','official2026FAQ',[(47,55)])
setspan('_date','S14','AEAT2026 dated versions',[(94,98)]);Q['algoDate']+=Q.pop('_date')
setspan('thresholdTable','S0','81.1–3',[(4632,4690)])
setspan('scaleTable','S0','85.1–3',[(4880,4954)])
setspan('regularise','S0','87.2',[(5118,5140)])
setspan('regulariseMortgage','S0','87.3.b',[(5148,5148)])
setspan('regulariseIRNR','S0','87.3.b',[(5150,5150)])
setspan('regulariseDate','S0','87.4',[(5162,5164)])
for k,rows in Q.items():Q[k]=list({(z['source'],z['LF_start'],z['LF_end'],z['quote']):z for z in rows}.values())
(P/'quotes.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
f=P/'build-ledger.py';s=f.read_text().replace("39<=lf<=41:ks=['thresholdTable']","39<=lf<=41:ks=['threshold'+str(lf-39)]").replace("63<=lf<=68:ks=['scaleTable']","63<=lf<=68:ks=['scale'+str(lf-63)]")
s=s.replace("if lf in [27]:", "if 63<=lf<=68:status='Statutory lower boundary, opening quota, width and rate quoted; displayed upper endpoint computed as opening base plus width.'\n if lf in [27]:")
f.write_text(s)
