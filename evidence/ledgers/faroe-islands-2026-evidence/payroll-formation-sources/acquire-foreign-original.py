from pathlib import Path
import urllib.request,json,hashlib
from html.parser import HTMLParser
p=Path(__file__).parent
urls={'foreign2023-original':'https://logir.fo/GetFile/getpdf.aspx?objType=File&objId=38060'}
r=[]
for k,u in urls.items():
 try:
  with urllib.request.urlopen(u,timeout=40) as x:b=x.read()
  f=p/(k+('.pdf' if b.startswith(b'%PDF')else'.html'));f.write_bytes(b);r.append(dict(id=k,url=u,path=str(f),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b)))
 except Exception as e:r.append(dict(id=k,url=u,error=str(e)))
(p/'foreign-original-acquisition.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
class H(HTMLParser):
 def handle_starttag(self,t,a):
  if t=='a':
   u=dict(a).get('href','')
   if '52-fra-19' in u:print('FOREIGN52',u)
if(p/'foreign-index.html').exists():H().feed((p/'foreign-index.html').read_text())
