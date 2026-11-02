from pathlib import Path
from html.parser import HTMLParser
import json,hashlib,re
P=Path(__file__).resolve().parent;raw=(P/'sources/N3.body').read_text();i=raw.index('Coeficiente máximo anual');a=raw.rfind('<table>',0,i);b=raw.index('</table>',i)+8;table=raw[a:b];(P/'R26-original-table.html').write_text(table)
class Table(HTMLParser):
 def __init__(self):super().__init__();self.rows=[];self.row=None;self.cell=None
 def handle_starttag(self,t,a):
  if t=='tr':self.row=[]
  if t in ['td','th']:self.cell=''
 def handle_data(self,s):
  if self.cell is not None:self.cell+=s
 def handle_endtag(self,t):
  if t in ['td','th']and self.cell is not None:self.row.append(re.sub(r'\s+',' ',self.cell).strip());self.cell=None
  if t=='tr'and self.row is not None:self.rows.append(self.row);self.row=None
h=Table();h.feed(table);(P/'R26-table-cells.json').write_text(json.dumps(dict(raw_sha256=hashlib.sha256((P/'sources/N3.body').read_bytes()).hexdigest(),current_raw_dated_block=raw[raw.rfind('<div',0,a):a],rows=h.rows),ensure_ascii=False,indent=2)+'\n');(P/'R26-table-reader.txt').write_text('\n'.join('\t'.join(x)for x in h.rows)+'\n');print(*h.rows,sep='\n')
