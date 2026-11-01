from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,ROUND_HALF_UP
import re,json,hashlib,difflib
w=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-faroe');r=w/'skills/research/faroe-islands-2026/ordinary-completion-2026-10-28/ledgers/pit-evidence';o=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/faroe-ordinary-completion/ledger-review');p=w/'skills/international/faroe-islands/fo-individual-income-tax.md';h=lambda b:hashlib.sha256(b).hexdigest();s=p.read_text();rows=json.loads((r/'claim-rows.json').read_text());quotes=[]
for x in rows:
 assert x['wording'] in s,x['id']
 for fn,n,q in re.findall(r'([\w-]+\.reader\.txt).*?quote LF(\d+): “([^”]+)”',x['source']):
  line=(r/fn).read_text().splitlines()[int(n)-1];assert q in line,(x['id'],fn,n,q);quotes.append({'id':x['id'],'file':fn,'LF':int(n),'exact':True})
# Every writer identity is checked, including raw bodies; no assertion of reading every acquired line.
ident=[]
for x in json.loads((r/'source-identities-and-read-scopes.json').read_text()):
 for key,hashkey in [('raw_file','raw_sha256'),('reader_file','reader_sha256'),('file','sha256')]:
  if key in x:
   f=r/x[key];assert h(f.read_bytes())==x[hashkey];ident.append({'file':x[key],'sha256':x[hashkey]})
checks=[]
def ck(n,a,e):assert a==e,(n,a,e);checks.append({'id':n,'actual':str(a),'expected':str(e),'pass':True})
def national(x):
 limits=[(65000,180000,F(13,100)),(180000,330000,F(15,100)),(330000,450000,F(1,5)),(450000,600000,F(1,4)),(600000,10**12,F(3,10))]
 return sum(max(0,min(x,b)-a)*rate for a,b,rate in limits)
for x,e in [(65000,0),(180000,14950),(330000,37450),(450000,61450),(600000,98950),(300000,32950),(240000,23950),(304100,33565),(150000,11050)]:ck('national'+str(x),national(x),e)
ck('ordinary municipal',F(19,100)*270000,51300);ck('ordinary combined',national(300000)+51300,84250)
ck('trader base',600000-260000-60000-40000,240000);ck('trader national',national(240000)-10700,13250);ck('trader municipal',210000*F(19,100)-9000,30900);ck('capital net',40000-5000+5000,40000);ck('capital tax',40000*F(35,100),14000);ck('trader total',13250+30900+14000,58150)
for i,cons,dep,e in [(240000,200000,60000,0),(240000,260000,60000,20000),(240000,400000,60000,60000)]:ck('consumption'+str(cons),min(max(cons-i,0),dep),e)
for low,high,expect in [(20000,300000,(30000,290000)),(0,300000,(30000,270000))]:
 transfer=30000-low;ck('spouse'+str(low),(low+transfer,high-transfer),expect);ck('spouse conserve'+str(low),sum(expect),low+high)
for x,rate,e in [(300000,F(85,10000),2295),(300000,F(9,1000),2430),(300099,F(85,10000),2295),(29999,F(85,10000),0)]:ck('church'+str(x)+str(rate),max((x//100)*100-30000,0)*rate,e)
annual=F(150000*365,180);base=(annual//100)*100;ck('annual raw',annual,F(912500,3));ck('annual rounded',base,304100);ck('annual muni',(base-30000)*F(19,100),52079);ck('annual total',national(base)+52079,85644);q=F(85644*180,365);v=(Decimal(q.numerator)/Decimal(q.denominator)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP);ck('observed reduced2dp',str(v),'42235.40');ck('observed whole',int(q),42235);ck('actual AM',150000*F(3,100),4500);ck('365day check',national(150000)+120000*F(19,100),33850)
old=(r/'20572441dcdae9ebd4c282597940338832ade34e-baseline.md').read_text();oa=lambda x:re.findall(r'```oa-check\n.*?```',x,re.S);assert oa(old)==oa(s);urls=lambda x:re.findall(r'https?://[^\s<>\])]+',x);assert all(x in urls(s) for x in urls(old))
a=old.splitlines(True);b=s.splitlines(True);ops=[]
for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
 if tag!='equal':ops.append({'old_start':i,'old_end':j,'new_start':k,'new_end':l,'old':''.join(a[i:j]),'new':''.join(b[k:l])})
inv=b[:]
for x in reversed(ops):inv[x['new_start']:x['new_end']]=x['old'].splitlines(True)
assert ''.join(inv)==old
import yaml
fm=lambda t:yaml.safe_load(t.split('---',2)[1]);fo,fn=fm(old),fm(s)
for key in set(fo)|set(fn):
 if key not in ['version','last_updated','description']:assert fo.get(key)==fn.get(key),key
assert fn['description']==fo['description'].replace('part-year annualisation','part-year credits')
result={'pin':h(p.read_bytes()),'rows':len(rows),'ledger_sha256':h((r.parent/'fo-individual-income-tax.md').read_bytes()),'quote_checks':quotes,'source_identity_checks':ident,'old_oa_exact':len(oa(old)),'oldtopic_units':131,'whole_inverse':True,'all_old_URLs':True,'protected_frontmatter':True,'operations':ops}
(o/'tranche3-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');(o/'tranche3-controls.json').write_text(json.dumps(checks,indent=2)+'\n');print('rows',len(rows),'quotes',len(quotes),'controls',len(checks),'Guide',result['pin'])
