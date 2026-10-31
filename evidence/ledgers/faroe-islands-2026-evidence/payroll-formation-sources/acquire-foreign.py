from pathlib import Path
import json,urllib.request,hashlib,concurrent.futures,shutil
from html.parser import HTMLParser
p=Path(__file__).parent; old=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/faroe-ordinary-completion/independent-review/sources')
class Reader(HTMLParser):
 def __init__(self):super().__init__();self.bits=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
  if t in ('p','br','div','tr','li','h1','h2','h3'):self.bits.append('\n')
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip=max(0,self.skip-1)
  if t in ('p','div','tr','li'):self.bits.append('\n')
 def handle_data(self,d):
  if not self.skip:self.bits.append(d)
def get(k,u):
 r={'id':k,'url':u,'read_on':'2026-10-28'}
 try:
  if (old/f'{k}.html').exists(): b=(old/f'{k}.html').read_bytes();r['reused_from']=str(old/f'{k}.html')
  else:
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as x:b=x.read();r['final_url']=x.url
  (p/f'{k}.html').write_bytes(b); h=Reader();h.feed(b.decode('utf-8','replace'));text='\n'.join(x.strip() for x in ''.join(h.bits).splitlines() if x.strip())+'\n';(p/f'{k}.reader.txt').write_text(text)
  r.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),reader_sha256=hashlib.sha256(text.encode()).hexdigest(),acquired=True,actual_read=False)
 except Exception as e:r.update(acquired=False,error=str(e))
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(lambda kv:get(*kv),json.loads((p/'foreign-exact-urls.json').read_text()).items()))
(p/'foreign-exact-acquisition.json').write_text(json.dumps(r,indent=2)); print(json.dumps([{k:x[k] for k in ('id','acquired','error') if k in x} for x in r],indent=2))
