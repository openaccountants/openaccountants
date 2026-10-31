from pathlib import Path
import json,re,shutil,hashlib
B=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-fresh-whole-pack-review-0f104150')
class Kit:
 def __init__(self,p):self.p=Path(p);self.sources={};self.identities=[];self.quotes=[];self.receipts=json.loads((B/'source-receipts.json').read_text())+json.loads((B/'source-receipts-additional.json').read_text())
 def cached(self,key,url,shared=None):
  rec=next(x for x in self.receipts if x.get('url')==url);raw=B/rec['path'];reader=raw.with_suffix('.reader.txt')
  if not reader.exists():reader=raw.with_suffix('.pdf.reader.txt')
  return self.local(key,url,raw,reader,rec.get('downloaded_utc'),shared)
 def local(self,key,url,raw,reader,date='2026-10-28',shared=None):
  raw=Path(raw);reader=Path(reader)
  if shared:
   dstraw=Path(shared)/raw.name;dstreader=Path(shared)/reader.name
  else:dstraw=self.p/'sources'/f'{key}.body';dstreader=self.p/'sources'/f'{key}.reader.txt'
  dstraw.parent.mkdir(parents=True,exist_ok=True)
  if not dstraw.exists():shutil.copyfile(raw,dstraw)
  if not dstreader.exists():shutil.copyfile(reader,dstreader)
  assert hashlib.sha256(raw.read_bytes()).digest()==hashlib.sha256(dstraw.read_bytes()).digest()
  assert hashlib.sha256(reader.read_bytes()).digest()==hashlib.sha256(dstreader.read_bytes()).digest()
  self.sources[key]=dict(url=url,lines=dstreader.read_text().splitlines(),reader=dstreader)
  self.identities.append(dict(key=key,url=url,raw=str(dstraw.relative_to(self.p)),raw_sha256=hashlib.sha256(dstraw.read_bytes()).hexdigest(),reader=str(dstreader.relative_to(self.p)),reader_sha256=hashlib.sha256(dstreader.read_bytes()).hexdigest(),acquired=date,read_scope='Selected exact quote intervals recorded separately; acquisition is not whole-source reading.'))
 def q(self,k,article,needle,words=32,scope=None):
  a=self.sources[k]['lines'];start=0;end=len(a)
  if scope:start,end=scope[0]-1,scope[1]
  if article:
   start=next(i for i,x in enumerate(a) if re.match(r'^Artículo\s+'+re.escape(article)+r'\.',x));end=next((i for i in range(start+1,len(a)) if re.match(r'^Artículo\s+\d',a[i])),len(a))
  pattern=re.compile(re.escape(needle).replace(r'\ ',r'\s+'),re.IGNORECASE)
  hits=[i for i in range(start,end) if pattern.search(a[i])]
  if not hits:raise ValueError(k,article,needle)
  i=hits[0];line=a[i];j=pattern.search(line).start();m=list(re.finditer(r'\S+',line[j:]));quote=line[j:j+m[min(words,len(m))-1].end()]
  z=dict(source=k,article=article,url=self.sources[k]['url']+('#a'+article.replace(' ','') if article else ''),quote=quote,reader=str(self.sources[k]['reader'].relative_to(self.p)),LF_start=i+1,LF_end=i+1,read_on='2026-10-28');self.quotes.append(z);return z
 def save(self):
  (self.p/'source-identities.json').write_text(json.dumps(self.identities,ensure_ascii=False,indent=2)+'\n');(self.p/'actual-read-quotes.json').write_text(json.dumps(self.quotes,ensure_ascii=False,indent=2)+'\n')
