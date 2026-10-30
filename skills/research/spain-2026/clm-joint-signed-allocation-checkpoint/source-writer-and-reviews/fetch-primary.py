from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
from hashlib import sha256
from html.parser import HTMLParser
import json,gzip
P=Path(__file__).parent
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0;self.links=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
  if t in ['p','div','li','br','tr','h1','h2','h3']:self.parts.append('\n')
  if t=='a':self.links += [v for k,v in a if k=='href']
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip:self.parts.append(d)
jobs=[('fresh-lirpf-current','https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764'),('fresh-clm-current','https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368'),('fresh-clm-law2-2021','https://www.boe.es/buscar/doc.php?id=BOE-A-2021-11513'),('fresh-clm-law1-2026','https://docm.jccm.es/portaldocm/verArchivoHtml.do?ruta=2026%2F03%2F30%2Fhtml%2F2026_2465.html&tipo=rutaDocm'),('fresh-aeat-clm-2025','https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/10-cumplimentacion-irpf-deducciones-autonomicas/10_7-castilla-mancha/10_7_16-traslado-vivienda-habitual.html')]
def run(job):
 name,url=job
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0','X-Requested-With':'XMLHttpRequest'}),timeout=35) as r:
   b=r.read();rec={'name':name,'url':url,'final_url':r.url,'status':r.status,'bytes':len(b),'sha256':sha256(b).hexdigest(),'read_utc':datetime.now(timezone.utc).isoformat(),'file':'sources/'+name+'.html'}
  (P/rec['file']).write_bytes(b);t=Text();t.feed((gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b).decode('utf-8'));(P/'sources'/(name+'.txt')).write_text(''.join(t.parts));(P/'sources'/(name+'-links.json')).write_text(json.dumps(t.links,indent=2)+'\n');return rec
 except Exception as e:return {'name':name,'url':url,'error':str(e),'read_utc':datetime.now(timezone.utc).isoformat()}
r=list(ThreadPoolExecutor(max_workers=4).map(run,jobs));(P/'fresh-primary-receipts.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps([{k:v for k,v in x.items() if k in ['name','status','bytes','error']} for x in r],indent=2))
