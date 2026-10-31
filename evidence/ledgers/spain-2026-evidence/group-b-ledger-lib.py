from pathlib import Path
from urllib.parse import urldefrag
import json,re,hashlib,gzip,html.parser,subprocess,difflib
ROOT=Path.cwd();E=ROOT/'ledgers/spain-2026-evidence';CAT=json.loads((E/'group-b-source-catalog.json').read_text())
class H(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
  if self.skip:return
  d=dict(a)
  if d.get('id'):self.out.append('\n[[ID:'+d['id']+']]\n')
  if t in ('p','tr','li','h1','h2','h3','h4','br','div'):self.out.append('\n')
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip=max(0,self.skip-1)
  if t in ('p','tr','li','h1','h2','h3','h4','div'):self.out.append('\n')
 def handle_data(self,x):
  if not self.skip:self.out.append(x)
from functools import lru_cache
@lru_cache(maxsize=256)
def source(url):
 u,anchor=urldefrag(url);xs=[x for x in CAT if x['url']==u]
 if not xs:raise ValueError('not catalogued '+u)
 xs.sort(key=lambda x:(not x.get('selected_answer',False),not bool(x['readers']),'spain-fresh-whole-pack-review-0f104150'not in x['raw']))
 x=xs[0].copy();p=Path(x['raw']);b=p.read_bytes();x['actual_raw_sha256']=hashlib.sha256(b).hexdigest();x['actual_raw_bytes']=len(b)
 if x['readers']:
  rp=Path(x['readers'][0]);t=rp.read_text();x['reader']=str(rp);x['reader_sha256']=hashlib.sha256(rp.read_bytes()).hexdigest()
 else:
  if b[:2]==b'\x1f\x8b':b=gzip.decompress(b)
  if b.startswith(b'%PDF'):raise ValueError('PDF reader missing '+str(p))
  try:z=b.decode('utf-8')
  except UnicodeDecodeError:z=b.decode('cp1252')
  h=H();h.feed(z);t=''.join(h.out);rp=E/('group-b-derived-'+hashlib.sha256(b).hexdigest()[:16]+'.txt');rp.write_text(t);x['reader']=str(rp);x['reader_sha256']=hashlib.sha256(rp.read_bytes()).hexdigest()
 if anchor:
  m=re.search(r'\[\[ID:'+re.escape(anchor)+r'\]\]',t)
  if m:
   end=re.search(r'\[\[ID:(?:a\d|ar-|da|dt|df|bloque)',t[m.end():]);t=t[m.start():m.end()+end.start() if end else len(t)]
  elif re.fullmatch(r'a[0-9]+',anchor) and b.startswith(b'%PDF'):
   number=anchor[1:];chunks=[]
   pat=r'(?m)^\s*(?:Artículo|Art\.)\s*'+number+r'\.(?![0-9A-Za-z])'
   for z in re.finditer(pat,t):
    end=re.search(r'(?m)^\s*(?:Artículo|Art\.)\s*[0-9]+',t[z.end():]);part=t[z.start():z.end()+end.start() if end else len(t)]
    if len(part)>200:chunks.append(part)
   if chunks:t='\n\n'.join(chunks)
  elif re.fullmatch(r'a[0-9]+(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies)',anchor) and b.startswith(b'%PDF'):
   number,suffix=re.fullmatch(r'a([0-9]+)([a-z]+)',anchor).groups();chunks=[]
   pat=r'(?m)^\s*(?:Artículo|Art\.)\s*'+number+r'[.\s]*'+suffix+r'\b'
   for z in re.finditer(pat,t):
    end=re.search(r'(?m)^\s*(?:Artículo|Art\.)\s*[0-9]+',t[z.end():]);part=t[z.start():z.end()+end.start() if end else len(t)]
    if len(part)>200:chunks.append(part)
   if chunks:t='\n\n'.join(chunks)
  elif re.fullmatch(r'anexo[0-9]+',anchor) and b.startswith(b'%PDF'):
   number=anchor[5:];chunks=[]
   for z in re.finditer(r'(?m)^\s*ANEXO\s*'+number+r'\b',t):
    end=re.search(r'(?m)^\s*ANEXO\s*[0-9]+\b',t[z.end():]);part=t[z.start():z.end()+end.start() if end else len(t)]
    if len(part)>200:chunks.append(part)
   if chunks:t=chunks[-1]
  elif re.fullmatch(r'a[0-9]+',anchor) and not b.startswith(b'%PDF'):
   number=anchor[1:];m=re.search(r'Artículo\s+'+number+r'\.',t)
   if m:
    end=re.search(r'Artículo\s+[0-9]+\.',t[m.end():]);t=t[m.start():m.end()+end.start()if end else len(t)]
 x['selected_url']=url;x['text']=t;return x
def norm(t):return re.sub(r'\s+',' ',t).strip()
def snippet(url,needle,width=420):
 x=source(url);t=x['text'];paras=[norm(z)for z in re.split(r'\n\s*\n',t)if z.strip()];matches=[z for z in paras if needle.lower()in z.lower()]
 if not matches:raise ValueError('missing quote needle '+needle+' '+url)
 t=matches[0];i=t.lower().find(needle.lower());start=0 if i<width-80 else max(0,i-160)
 if start:start=t.rfind(' ',0,start)+1
 end=min(len(t),max(start+width,i+len(needle)))
 if end<len(t):end=t.rfind(' ',start,end)
 return ('[…] 'if start else'')+t[start:end]+(' […]'if end<len(t)else'')

def units(text):
 ls=text.splitlines();sec='';sub='';fence=False;out=[];refs={k:v for k,v in re.findall(r'^\[([^]]+)\]:\s*(\S+)',text,re.M)}
 for i,l in enumerate(ls,1):
  if l.startswith('## '):sec=l[3:];sub='';continue
  if l.startswith('### '):sub=l[4:];continue
  if l.startswith('```'):fence=not fence;continue
  if fence or not sec or sec in ['Sources','Talk to a verified accountant']or not l.strip()or (l.startswith(('|---','<!--','---')) or re.match(r'^\[[^]]+\]:',l)):continue
  if l.startswith('|')and all(v.strip().lower()in ['', 'item','amount or test','tax year','official source','obligation','deadline and required action','event','statutory consequence before applicable reductions','competent law','ordinary aggregation test','primary provisions'] for v in l.split('|')):continue
  out.append({'line':i,'section':sec+(' / '+sub if sub else''),'text':l,'references':refs})
 return out
class Ledger:
 def __init__(self,slug):self.slug=slug;self.p=E/slug;self.guide=(self.p/'frozen-guide.txt').read_text();self.units=units(self.guide);self.rows=[];self.sources={}
 def add(self,guide_needle,url,quote_needle,provision,kind='rule',note='',width=420):
  matches=[u for u in self.units if guide_needle in u['text']]
  if len(matches)!=1:raise ValueError((guide_needle,len(matches)))
  u=matches[0];x=source(url);q=snippet(url,quote_needle,width);self.sources[url]=x;self.rows.append(dict(id=len(self.rows)+1,section=u['section'],guide_LF=u['line'],guide_wording=u['text'],provision=provision,url=url,quote=q,read_on='2026-10-28',kind=kind,note=note,raw_sha256=x['actual_raw_sha256'],reader=x['reader']))
 def save(self):
  def c(s):return str(s).replace('|','\\|').replace('\n',' ')
  ident=json.loads((self.p/'identity.json').read_text());o=[f'# {self.slug}: figure and rule ledger',f'Frozen Guide SHA256 `{ident["sha256"]}`; HEAD0b5e62451de50220ac6d80c7813d547d08108641. Writer evidence, not independent review or accountant attestation. Source quotations retain original language with whitespace joined; case figures are computed, not quoted statutory amounts. All source bodies are reused by exact identity, not silently replaced.','| # | Guide section and native LF | Figure / rule as written | Source act/article | Official URL | Exact short source quote | Actual read date | Type / scope |','|---|---|---|---|---|---|---|---|']
  for z in self.rows:o.append('| '+' | '.join(c(v)for v in [z['id'],z['section']+'; LF'+str(z['guide_LF']),z['guide_wording'],z['provision'],z['url'],z['quote'],z['read_on'],z['kind']+(': '+z['note'] if z['note']else'')])+' |')
  covered={z['guide_LF']for z in self.rows};missing=[u for u in self.units if u['line']not in covered];o+=['','## Evidence gaps / non-rule working instructions','Every substantive Guide unit is retained in the inventory. This table is not a claim that its rule is false. A quotation gap is explicitly distinguished from a computed illustration, client question or reserved method.','| Native LF | Section | Exact Guide wording | Disposition |','|---|---|---|---|']
  for u in missing:
   t=u['text'];typ='Client fact gathering'if u['section'].startswith('Ask')else ('Table column heading or workflow introduction; no independent tax amount'if (t.startswith('|')and 'Official source'in t)or t.endswith(':')else 'Exact quotation still to match to retained primary; do not treat as ledger-verified')
   o.append('| '+' | '.join(c(v)for v in [u['line'],u['section'],t,typ])+' |')
  o+=['','## Old topics carried','| Prior body native LF | Exact old substantive topic | Current destination / disposition |','|---|---|---|']
  old=self.p/'prior-main-guide.txt'
  if old.exists():
   oldtext=old.read_text();oldunits=units(oldtext);(self.p/'prior-main-identity.txt').write_text('Actual local origin/main62b7639a5a68324a83a96bb0190fff8b7c76f8c5\n')
  else:
   path='skills/international/spain/'+self.slug+'.md';z=subprocess.run(['git','log','--diff-filter=A','--format=%H','--',path],capture_output=True,text=True);sha=z.stdout.splitlines()[-1]if z.stdout.strip()else'';q=subprocess.run(['git','show',sha+':'+path],capture_output=True);oldtext=q.stdout.decode()if q.returncode==0 else'';oldunits=units(oldtext);(self.p/'earliest-branch-guide.txt').write_text(oldtext);o.append('| n/a | No prior published-main body exists for this Guide | Earliest retained branch body '+sha+' used below as an additional preservation comparator, not represented as prior public main. |')
  overrides=json.loads((self.p/'old-topic-overrides.json').read_text())if(self.p/'old-topic-overrides.json').exists()else{}
  for u in oldunits:
   exact=[v for v in self.units if v['text']==u['text']]
   if str(u['line'])in overrides:dest=overrides[str(u['line'])]
   elif exact:dest=exact[0]['section']+'; current LF'+str(exact[0]['line'])+'; exact retained'
   else:
    best=max(self.units,key=lambda v:difflib.SequenceMatcher(None,re.sub(r'https?://\S+','',u['text']),re.sub(r'https?://\S+','',v['text'])).ratio());dest='Changed topic: candidate destination '+best['section']+' current LF'+str(best['line'])+'; matching is a locator aid, not proof of substantive preservation'
   dest=overrides.get(str(u['line']),dest)
   o.append('| '+' | '.join(c(v)for v in [u['line'],u['text'],dest])+' |')
  reservations=[l for l in self.guide.splitlines()if l.startswith('**Not yet confirmed')or l.startswith('**Remaining')or l.startswith('**Scope limitation')]
  if reservations:o+=['','## Frozen reservations retained verbatim',*reservations]
  (ROOT/'ledgers'/f'{self.slug}.md').write_text('\n'.join(o)+'\n');(self.p/'rows.json').write_text(json.dumps(self.rows,indent=2,ensure_ascii=False)+'\n');(self.p/'all-guide-units.json').write_text(json.dumps(self.units,indent=2,ensure_ascii=False)+'\n');(self.p/'source-read-receipts.json').write_text(json.dumps([{k:v for k,v in x.items()if k!='text'}for x in self.sources.values()],indent=2,ensure_ascii=False)+'\n');print(self.slug,'rows',len(self.rows),'remaining units',len(missing))
