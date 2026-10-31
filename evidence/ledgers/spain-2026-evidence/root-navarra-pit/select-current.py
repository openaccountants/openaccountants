from pathlib import Path
from html.parser import HTMLParser
import json,re,sys
DATE=sys.argv[1] if len(sys.argv)>1 else "20261028"
P=Path(__file__).resolve().parent
class Dated(HTMLParser):
 def __init__(self):super().__init__();self.stack=[];self.items=[];self.active=None
 def handle_starttag(self,t,a):
  d=dict(a);self.stack.append(t) if t not in ['br','hr','img','input','meta','link'] else None
  if t=='div'and 'fdesde'in d:
   if self.active:raise RuntimeError('nested dated block')
   self.active=dict(attrs=d,depth=len(self.stack),text='')
 def handle_data(self,s):
  if self.active:self.active['text']+=s
 def handle_endtag(self,t):
  if self.active and len(self.stack)==self.active['depth']and t=='div':
   x=self.active;self.active=None;d=x['attrs'];dt=DATE
   if d['fdesde']<=dt<d['fhasta'] and not re.search(r'\bn\b',d.get('class','')):
    x['text']=re.sub(r'\s+',' ',x['text']).strip();self.items.append(x)
  if t in self.stack:
   while self.stack:
    z=self.stack.pop()
    if z==t:break
for key in ['N3','N27']:
 h=Dated();raw=(P/'sources'/(key+'.body')).read_bytes()
 try: text=raw.decode('utf-8')
 except UnicodeDecodeError: text=raw.decode('cp1252')
 h.feed(text);(P/(key+('-dated-current-blocks.json'if DATE=='20261028'else'-dated-'+DATE+'-blocks.json'))).write_text(json.dumps(h.items,ensure_ascii=False,indent=2)+'\n');(P/(key+('-current-selected.txt'if DATE=='20261028'else'-'+DATE+'-selected.txt'))).write_text('\n'.join(x['text']for x in h.items)+'\n');print(key,len(h.items))
