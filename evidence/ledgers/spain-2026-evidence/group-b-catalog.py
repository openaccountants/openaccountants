from pathlib import Path
from urllib.parse import urldefrag
import json,hashlib
OA=Path('/Users/michaelcutajar/Documents/ChatGPT/OA');WT=Path.cwd();out=WT/'ledgers/spain-2026-evidence';roots=[OA/'output/europe-closeout-2026-10-27', WT/'skills/research/spain-2026'];records=[];seen=set()
def resolve(v,parent):
 if not isinstance(v,str)or len(v)>1200:return None
 p=Path(v)
 for c in [p,parent/p,WT/p,OA/p,parent/'sources'/p.name]:
  try:
   if c.is_file()and c.suffix.lower()not in ['.json','.md','.py','.png']:return c.resolve()
  except OSError:pass
 return None
def visit(x,parent,receipt):
 if isinstance(x,list):
  for y in x:visit(y,parent,receipt)
 elif isinstance(x,dict):
  u=x.get('url',x.get('URL',x.get('source_url')))
  if isinstance(u,str)and u.startswith('http'):
   candidates=[]
   for k in ['raw_path','raw','path','local_path','body_path','file','pdf','raw_file','stored_path','source_path']:
    p=resolve(x.get(k),parent)
    if p and ('reader'not in p.name and p.suffix not in ['.txt']):candidates.append(p)
   for p in candidates:
    key=(urldefrag(u)[0],str(p))
    if key in seen:continue
    seen.add(key);readers=[]
    for k in ['reader','reader_path','text_path','text','text_file']:
     q=resolve(x.get(k),parent)
     if q:readers.append(str(q))
    for q in [p.with_suffix('.reader.txt'),p.with_suffix('.pdf.reader.txt'),p.with_suffix('.txt'),p.with_name(p.stem+'.reader.txt')]:
     if q.exists():readers.append(str(q))
    records.append(dict(url=urldefrag(u)[0],raw=str(p),readers=list(dict.fromkeys(readers)),receipt=str(receipt),claimed_sha256=x.get('sha256',x.get('raw_sha256'))))
  for y in x.values():
   if isinstance(y,(dict,list)):visit(y,parent,receipt)
for root in roots:
 for p in root.rglob('*.json'):
  if root.name=='europe-closeout-2026-10-27'and not p.relative_to(root).parts[0].startswith('spain-'):continue
  if not any(w in p.name.lower() for w in ['source','receipt','identity','artifact','manifest','acquisit']):continue
  try:visit(json.loads(p.read_text()),p.parent,p)
  except (ValueError,UnicodeError):pass
(out/'group-b-source-catalog.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n');print('records',len(records),'uniqueurls',len(set(x['url']for x in records)))
