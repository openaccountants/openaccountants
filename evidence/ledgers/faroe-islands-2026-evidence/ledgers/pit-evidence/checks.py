from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal,ROUND_HALF_UP
import json,re,hashlib,subprocess
P=Path(__file__).resolve().parent;R=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());f=R/'skills/international/faroe-islands/fo-individual-income-tax.md';b=f.read_text();out=[]
def check(n,a,e):
 assert a==e,(n,a,e);out.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def nat(i):
 if i<65000:return 0
 if i<180000:return Q(13,100)*(i-65000)
 if i<330000:return 14950+Q(15,100)*(i-180000)
 if i<450000:return 37450+Q(20,100)*(i-330000)
 if i<600000:return 61450+Q(25,100)*(i-450000)
 return 98950+Q(30,100)*(i-600000)
for i,e in [(64999,0),(65000,0),(180000,14950),(330000,37450),(450000,61450),(600000,98950)]:check(f'national boundary{i}',nat(i),e)
for i,lo,up in [(180000,lambda x:Q(13,100)*(x-65000),lambda x:14950+Q(15,100)*(x-180000)),(330000,lambda x:14950+Q(15,100)*(x-180000),lambda x:37450+Q(20,100)*(x-330000)),(450000,lambda x:37450+Q(20,100)*(x-330000),lambda x:61450+Q(25,100)*(x-450000)),(600000,lambda x:61450+Q(25,100)*(x-450000),lambda x:98950+Q(30,100)*(x-600000))]:check('adjacent formula continuity'+str(i),lo(i),up(i))
check('original full-year national',nat(300000),32950);check('original municipal',Q(19,100)*(300000-30000),51300)
check('original combined84250',nat(300000)+Q(19,100)*(300000-30000),84250)
check('hypothetical church Torshavn',Q(85,10000)*(300000-30000),2295);check('hypothetical church Argir',Q(9,1000)*(300000-30000),2430)
check('20k/300k transfer amount',30000-20000,10000);check('adjusted higher290k',300000-(30000-20000),290000);check('zero/300k adjusted higher',300000-(30000-0),270000)
annual=Q(150000*365,180);rounded=(annual//100)*100
check('180day unrounded annual equivalent',annual,Q(912500,3));check('observed annual rounded304100',rounded,304100)
check('observed annual national',nat(rounded),33565);check('observed annual municipal',Q(19,100)*(rounded-30000),52079)
gross=nat(rounded)+Q(19,100)*(rounded-30000);check('observed gross85644',gross,85644)
reduced=gross*Q(180,365);dp=(Decimal(reduced.numerator)/Decimal(reduced.denominator)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
check('observed reduced two-decimal42235.40',str(dp),'42235.40');check('observed final whole-kr display (fixture only)',int(reduced),42235)
check('365day150k no-credit national+municipal',nat(150000)+Q(19,100)*(150000-30000),33850)
check('observed separate AM3percent input',Q(3,100)*150000,4500)
base=600000-260000-60000-40000;check('original trader base',base,240000);check('consumption floor original',min(max(200000-base,0),60000),0)
check('consumption floor capped hypothetical increase',min(max(400000-base,0),60000),60000)
check('original child-credit national',nat(base)-10700,13250);check('original child-credit municipal',Q(19,100)*(base-30000)-9000,30900)
check('original capitalnet',40000-5000+5000,40000);check('original capitaltax',40000*Q(35,100),14000);check('original trader income tax58150',13250+30900+14000,58150)
check('Guide SHA untouched',hashlib.sha256(f.read_bytes()).hexdigest(),'ebf5863b6f219368291d91aecbe0e260a304900634eaa64451094b44cb7a820c')
old=subprocess.check_output(['git','show','20572441dcdae9ebd4c282597940338832ade34e:'+str(f.relative_to(R))],text=True)
blocks=lambda s:re.findall(r'```oa-check\n.*?\n```',s,re.S)
check('exactly two main examples',len(blocks(b)),2);check('published original blocks exact',blocks(b),blocks(old))
rows=json.loads((P/'claim-rows.json').read_text());check('every generated claim wording still in Guide',all(z['wording'] in b for z in rows),True)
for z in json.loads((P/'source-identities-and-read-scopes.json').read_text()):
 if 'raw_file' in z:
  check('raw identity '+z['id'],hashlib.sha256((P/z['raw_file']).read_bytes()).hexdigest(),z['raw_sha256']);check('reader identity '+z['id'],hashlib.sha256((P/z['reader_file']).read_bytes()).hexdigest(),z['reader_sha256'])
(P/'check-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(len(out),'ledger writer assertions passed; no independent-review or own UI-replay claim')
