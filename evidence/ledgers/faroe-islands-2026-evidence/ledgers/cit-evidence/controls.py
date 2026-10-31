from pathlib import Path
from fractions import Fraction as F
import json,re,hashlib,sys,subprocess
import yaml
P=Path(__file__).resolve().parent;R=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());f=R/'skills/international/faroe-islands/fo-corporate-income-tax.md'
b=f.read_text();old=(P/'baseline-cit.md').read_text();out=[]
def check(label,actual,expected):
 assert actual==expected,(label,actual,expected);out.append(dict(name=label,actual=str(actual),expected=str(expected),result='pass'))
rate=F(18,100)
check('goodwill yearly 100000/10',F(100000,10),10000)
check('fixed five-year right annual',F(100000,5),20000)
check('ten-year total acquisition deduction',10000*10,100000)
check('purchase year plus next nine last year',2026+9,2035)
check('five-year final year',2026+4,2030)
check('sale unrelieved basis after four deductions',100000-4*10000,60000)
check('hypothetical sale proceeds80000 less unrelieved60000',80000-(100000-4*10000),20000)
A=200000-40000-30000;C=70000;Bcap=25000-5000;Bremaining=100000-Bcap;pool=A+C
check('A pre-group+own group loss before shared loss',A,130000)
check('B own capital net after prior capital loss',Bcap,20000)
check('B current loss after capital offset',Bremaining,80000)
a=F(Bremaining*A,pool);c=F(Bremaining*C,pool)
check('A proportional loss',a,52000);check('C proportional loss',c,28000)
check('loss allocated once',a+c,Bremaining);check('A final ordinary base',A-a,78000);check('C final ordinary base',C-c,42000)
check('combined ordinary base',A+C-a-c,120000);check('combined tax',(A+C-a-c)*rate,21600)
check('B loss compensation',(a+c)*rate,14400);check('A to parent loss compensation',a*rate,9360);check('A to parent tax',(A-a)*rate,14040)
check('C own saving',c*rate,5040);check('C own final tax',(C-c)*rate,7560)
check('C parent net cash',21600+14400-9360-14040,C*rate)
check('loss capped at aggregate surplus',min(300000,200000),200000)
check('loss cap preserves unused balance',300000-min(300000,200000),100000)
def recapture(p,book,prior,index):return min(prior,max(p-book,0)),max(p-index,0)
check('indexed-loss separating case',recapture(900000,700000,300000,1100000),(200000,0))
check('proceeds equal unindexed book value',recapture(700000,700000,300000,1100000),(0,0))
check('full depreciation cap plus indexed gain',recapture(1200000,700000,300000,1100000),(300000,100000))
check('disposal loss not negative taxable gain',recapture(600000,700000,300000,1100000),(0,0))
blocks=lambda s:re.findall(r'```oa-check\n.*?\n```',s,re.S)
check('exactly2 main blocks',len(blocks(b)),2);check('two old blocks byte-exact',blocks(b),blocks(old))
meta=lambda s:yaml.safe_load(s.split('---',2)[1]);m1=meta(old);m2=meta(b)
check('protected metadata', {k:v for k,v in m2.items() if k not in ['version','last_updated']},{k:v for k,v in m1.items() if k not in ['version','last_updated']})
check('version06',m2['version'],0.6);check('aligned H1',bool(re.search(r'^# Faroe Islands corporate income tax v0.6$',b,re.M)),True)
check('original H2 order',re.findall(r'^## .*$',b,re.M),re.findall(r'^## .*$',old,re.M))
check('questions preserved',old.split('## Ask the client first')[1].split('## Sources')[0],b.split('## Ask the client first')[1].split('## Sources')[0])
oldurls=re.findall(r'^\[[^]]+\]: (https?://\S+)',old,re.M);newurls=re.findall(r'^\[[^]]+\]: (https?://\S+)',b,re.M)
check('old URL definitions and order',newurls[:len(oldurls)],oldurls)
z=b.removesuffix('\n[vls-n]: https://www.taks.fo/fo/log/vegleidingarskriv-vls-2015/n-skattligar-avskrivingar\n')
for op in reversed(json.loads((P/'exact-operations.json').read_text())):assert z.count(op['new'])==1;z=z.replace(op['new'],op['old'],1)
check('full exact reverse reconstruction',hashlib.sha256(z.encode()).hexdigest(),hashlib.sha256(old.encode()).hexdigest())
# Check source table column counts, accounting for Markdown links and rows only.
source=b.split('## Sources\n',1)[1].split('Not yet confirmed:',1)[0]
check('source rows have3columns',all(len(x.split('|'))==5 for x in source.splitlines() if x.startswith('|')),True)
(P/'control-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(out),'writer assertions passed; no independent review claimed')
print('CIT SHA256',hashlib.sha256(b.encode()).hexdigest(),len(b.encode()))
