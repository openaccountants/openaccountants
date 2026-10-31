from pathlib import Path
from fractions import Fraction as F
import json,re,hashlib,subprocess
P=Path(__file__).resolve().parent;R=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());g=R/'skills/international/spain/es-beckham.md';body=g.read_text();out=[]
def c(name,a,e):
 assert a==e,(name,a,e);out.append(dict(name=name,actual=str(a),expected=str(e),pass_check=True))
c('Guide frozen SHA',hashlib.sha256(g.read_bytes()).hexdigest(),'edbac3851deb99dc27ba7115600060bfc2554578c88c03238ff4c8d44d722b02')
for z in json.loads((P/'actual-read-quotes.json').read_text()):
 a=(P/z['reader']).read_text().splitlines();c(z['source']+' exact quote LF'+str(z['LF_start']),z['quote'] in '\n'.join(a[z['LF_start']-1:z['LF_end']]),True)
for z in json.loads((P/'source-identities.json').read_text()):
 c(z['id']+' raw unchanged',hashlib.sha256((P/z['raw_file']).read_bytes()).hexdigest(),z['raw_sha256']);c(z['id']+' reader unchanged',hashlib.sha256((P/z['reader_file']).read_bytes()).hexdigest(),z['reader_sha256'])
rows=json.loads((P/'claim-rows.json').read_text());c('every exact current rule wording in Guide',all(z['wording'] in body for z in rows),True)
c('main oa count',len(re.findall('```oa-check',body)),2)
c('example1 salary tax',110000*F(24,100),26400);c('example1 Spanish dividend tax',4000*F(19,100),760);c('example1 combined',26400+760,27160)
o=600000*F(24,100)+50000*F(47,100);s=71880+10000*F(30,100);c('example2 ordinary',o,167500);c('example2 savings',s,74880)
raw=300000*o/650000;c('historical raw fraction retained as correction history',raw,F(1005000,13));c('current effective percentage',round(100*float(o)/650000,2),25.77);c('current rounded-rate foreign limit',F(2577,10000)*300000,77310)
cap=o*F(30,100);c('example2 binding credit',min(80000,raw,cap),50250);c('example2 after credit',o+s-cap,192130);c('example2 salary withheld',650000*F(24,100),156000);c('example2 dividend withheld',310000*F(19,100),58900);c('example2 return',o+s-cap-156000-58900,-22770)
(P/'ledger-check-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(len(out),'writer-ledger checks passed; S-L01 rounded percentage and current limit checked; old fraction retained only as correction history')
