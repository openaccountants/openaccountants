from pathlib import Path
from fractions import Fraction as F
import json,re,hashlib
w=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-faroe');r=w/'skills/research/faroe-islands-2026/ordinary-completion-2026-10-28';s=r/'payroll-formation-sources';o=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/faroe-ordinary-completion/ledger-review');h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();normal=lambda t:' '.join(t.split())
rows=[];issues=[]
for slug in ['fo-payroll-contributions','fo-company-registration-reporting']:
 t=(r/'ledgers'/(slug+'.md')).read_text();claims=[line.split('|') for line in t.split('## Old topics carried')[0].splitlines() if re.match(r'^\| \d+ \|',line)]
 for c in claims:
  n=int(c[1]);loc=c[4].strip();m=re.match(r'([\w-]+):.*native LF\s*(\d+)–(\d+)',loc);assert m,(slug,n,loc);src,a,b=m.group(1),int(m.group(2)),int(m.group(3));q=c[6].strip();q=re.sub(r'(?:Exact commencement LF\d+: |; exact publication LF\d+: )',' […] ',q);q=q.replace('kunngjørd.;','kunngjørd.');ls=(s/(src+'.reader.txt')).read_text().splitlines();body=normal(' '.join(ls[a-1:b]));pos=0
  for fragment in q.split(' […]'):
   fragment=normal(fragment).strip();fragment=re.sub(r'^Exact (?:exception anchor|owner-wage sentence) at LF\d+: ', '', fragment)
   if not fragment:continue
   at=body.find(fragment,pos)
   if at<0:issues.append({'slug':slug,'row':n,'source':src,'range':[a,b],'missing_fragment':fragment})
   else:pos=at+len(fragment)
  rows.append({'slug':slug,'row':n,'claim':c[3].strip(),'source':src,'range':[a,b],'verdict':'Independently assessed within stated conditions; operational/research limits preserved'})
ident=[]
for x in json.loads((r/'payroll-formation-source-read-ledger.json').read_text()):
 for field in ['raw','reader']:
  p=Path(x[field]);assert h(p)==x[field+'_sha256'],p;ident.append({'path':str(p),'sha256':h(p)})
checks=[]
def ck(n,a,e):assert a==e,(n,a,e);checks.append({'id':n,'actual':str(a),'expected':str(e),'pass':True})
ck('health30k',175+30000*F(7,1000),385);ck('worker30k',385+900+258+180,1723);ck('employer30k',30000*(F(3,100)+F(86,10000)+F(6,1000)+F(5,10000)+F(2,1000)),1413)
ck('pension-preliminary',3600*F(2,5),1440);ck('pension-account',3600*F(3,5),2160);ck('monthly-supplement',30000*F(15,1000),450);ck('labour-selected',30000+3600+1413+450,35463)
ck('ALSworkerannual',min(700000,650000)*F(6,1000),3900);ck('ALSployerannual',700000*F(6,1000),4200);ck('pensioncap',min(1500000*F(12,100),150000),150000);ck('pensionoutside-min',180000-150000,30000);ck('pensioncap-tax',150000*F(2,5),60000);ck('pensioncap-account',150000*F(3,5),90000)
ck('low-A',249*F(3,25),F(747,25));ck('boundary-A',250*F(3,25),30);ck('low-exclusion',249*F(3,25)<30,True);ck('boundary-not-excluded',250*F(3,25)<30,False)
ck('partyear-B',100000*F(3,25)*F(292,365),9600);ck('no-duty-B-reduction',12000*F(73,365),2400)
ck('provedpayment',max(56800-5000,0),51800);ck('provedpayment-floor',max(56800-60000,0),0);ck('mileage',56800*F(4000,10000),22720);ck('calendar-separator',56800*F(1,2)-22720,5680)
ck('foreign-funding-target',30000*F(3,25),3600);ck('foreign-topup',3600-2700,900);ck('finaltax235k',12000*F(3,10),3600);ck('pensionrefund',12000*F(1,10),1200)
for cap,prem,pct,total in [(200000,100000,F(1,4),75000),(50000,20000,F(1),70000),(100000,60000,F(1,2),80000)]:ck('SpF'+str(cap),cap*pct+prem*pct,total)
ck('SpF-counterreading',50000+100000,150000);ck('PF',500000*F(1,4)+100000,225000);ck('noncash',200000+100000,300000)
ck('late-third-cap',min(3000,3000),3000);ck('late-total-not-sum',500+2000+3000==3000,False)
# Exact original forward/reverse repairs; this is stronger than matching a reported hash alone.
ops=json.loads((r/'payroll-formation-exact-replacements.json').read_text());proof=[]
for slug in ['fo-payroll-contributions','fo-company-registration-reporting']:
 p=w/'skills/international/faroe-islands'/(slug+'.md');new=p.read_text();old=new
 for x in reversed(ops[slug]):assert old.count(x['new'])==1,(slug,x['new'][:70]);old=old.replace(x['new'],x['old'],1)
 import subprocess
 published=subprocess.check_output(['git','show','20572441dcdae9ebd4c282597940338832ade34e:skills/international/faroe-islands/'+slug+'.md'],cwd=w,text=True);assert old==published
 rebuilt=old
 for x in ops[slug]:assert rebuilt.count(x['old'])==1;rebuilt=rebuilt.replace(x['old'],x['new'],1)
 assert rebuilt==new
 oa=lambda z:re.findall(r'```oa-check\n.*?```',z,re.S);assert oa(old)==oa(new)
 urls=lambda z:re.findall(r'https?://[^\s<>\])]+',z);oldurls=urls(old);it=iter(urls(new));assert all(any(y==x for y in it) for x in oldurls)
 import yaml
 fm=lambda z:yaml.safe_load(z.split('---',2)[1]);a,b=fm(old),fm(new)
 for k in set(a)|set(b):
  if k not in ['version','last_updated','description']:assert a.get(k)==b.get(k),k
 assert re.findall(r'^## .*',old,re.M)==re.findall(r'^## .*',new,re.M)
 assert old[old.index('> Contributed by '):]==new[new.index('> Contributed by '):]
 proof.append({'slug':slug,'sha256':h(p),'ledger_sha256':h(r/'ledgers'/(slug+'.md')),'rows':sum(x['slug']==slug for x in rows),'main_oa_exact':len(oa(old)),'whole_inverse':True,'forward_rebuild':True,'old_URL_occurrence_order':True,'protected_metadata':True,'old_H2_order':True,'byline_CTA_suffix':True})
(o/'tranche4-row-checks.json').write_text(json.dumps({'rows':rows,'quote_issues':issues,'source_identity_checks':ident,'protection':proof},ensure_ascii=False,indent=2)+'\n');(o/'tranche4-controls.json').write_text(json.dumps(checks,indent=2)+'\n');print('rows',len(rows),'quote issues',issues,'sourcepairs',len(ident)//2,'controls',len(checks),'proof',proof)
