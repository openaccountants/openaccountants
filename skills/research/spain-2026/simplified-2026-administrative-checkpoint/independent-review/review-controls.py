from pathlib import Path
from decimal import Decimal as D
from collections import Counter
import json,re,hashlib,datetime,importlib.util,sys,subprocess,shutil,difflib
p=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-evidence/spain/review/simplified-2026-administrative-bridge');q=p/'independent-review';q.mkdir(exist_ok=True)
controls=[]
def ck(n,a,e=True,source='LIRPF31/LIVA122; AEAT current2026eligibility'):
 controls.append({'id':n,'actual':str(a),'expected':str(e),'pass':a==e,'source':source});assert a==e,(n,a,e)
def numerical(r,b,p):return D(r)<=D(250000) and D(b)<=D(125000) and D(p)<=D(250000)
for n,args,want in [('distinguishing-middle',('200000','100000','220000'),True),('all-equality',('250000','125000','250000'),True),('all-zero',('0','0','0'),True)]:ck(n,numerical(*args),want)
base=[D(250000),D(125000),D(250000)]
for i in range(3):
 for eps in ['-.01','0','.01']:
  x=base[:];x[i]+=D(eps);ck('threshold-limb%s-delta%s'%(i,eps),numerical(*x),D(eps)<=0)
old=lambda r,b,p:D(r)<=150000 and D(b)<=75000 and D(p)<=150000
ck('middle-fails-ordinary-baseline',old('200000','100000','220000'),False)
for a,expected in [('100000','200000'),('50000','100000'),('110000','220000')]:ck('six-month-annualisation-'+a,D(a)*12/6,D(expected))
ck('annualisation-crosses-total',D('130000')*2>D(250000));ck('annualisation-equality',D('125000')*2,D(250000))
ck('qualifying-family-total',D('200000')+60000,D(260000));ck('aggregated-fails-total',numerical('260000','100000','220000'),False)
# Aggregation requires relationship/specified entity + sameIAE + common direction + either kind of shared means.
for related,similar,directed,personnel,material,expect in [(1,1,1,1,0,True),(1,1,1,0,1,True),(1,1,1,0,0,False),(1,1,0,1,1,False),(1,0,1,1,1,False),(0,1,1,1,1,False)]:ck('family-gates-%s%s%s%s%s'%(related,similar,directed,personnel,material),bool(related and similar and directed and (personnel or material)),expect,'LIRPF31/order3: both main conditions; shared personnel OR material')
ck('subcontracting-in-purchases',D('240000')+D('10000'),D(250000));ck('extra-subcontract-excludes',numerical('200000','100000',D('240000')+D('10000.01')),False)
ck('capital-asset-excluded-from-purchase-limb',D('700000')-D('500000'),D('200000'))
ck('farm-receipts-equality',D('250000')<=250000);ck('farm-receipts-excess',D('250000.01')<=250000,False)
# These date controls test the named limb only, not validity under every possible procedure.
from datetime import date
start,end=date(2026,2,5),date(2026,2,16)
for d,expect in [(date(2026,2,4),False),(start,True),(date(2026,2,15),True),(end,True),(date(2026,2,17),False)]:ck('exceptional-window-'+str(d),start<=d<=end,expect,'RDL2/2026art11(1),4February publication')
ck('jan30-not-preserved-by-jan-vigencia-limb',date(2026,1,30)<date(2026,1,28),False,'RDL2art11(2); RDL16repeal published28January; another route not decided')
for quarter,timely,expect in [(1,True,True),(2,True,False),(1,False,False)]:ck('established-implicit-q%s-timely%s'%(quarter,timely),quarter==1 and timely,expect,'RIRPF33(1)(b)/RIVA33(2), timely first calendar quarter')
ck('zero-first-quarter-declaration-still-filing-act',True,True,'RIRPF33: timely presentation, no positive-cash condition')
for first_required,timely,expect in [(True,True,True),(False,True,False),(True,False,False)]:ck('new-activity-first-required%s-timely%s'%(first_required,timely),first_required and timely,expect,'RIVA33(2),actual startup; IRPFfirst activity-quarter separately')
ck('same-year-new-activity-does-not-automatically-recast-old',True,True,'RIVA33(2)/RIRPF35; separate coordination effects remain')
(q/'controls.json').write_text(json.dumps(controls,indent=2))
# Every old unit is classified. Long unchanged units are represented by hash and actual first line;
# changed units retain complete old text, plus rationale; table rows are separate units.
def units(s):
 out=[];lines=s.splitlines();i=0
 while i<len(lines):
  if not lines[i].strip():i+=1;continue
  start=i
  if lines[i].startswith('```'):
   i+=1
   while i<len(lines) and not lines[i].startswith('```'):i+=1
   i+=1
  elif lines[i].startswith('|') or lines[i].startswith('#') or i==0 or (s.startswith('---') and i<lines[1:].index('---')+1):i+=1
  else:
   i+=1
   while i<len(lines) and lines[i].strip() and not lines[i].startswith(('|','#','```')):i+=1
  out.append((start+1,'\n'.join(lines[start:i])))
 return out
ledger=[];checks=[]
manifest=json.loads((p/'candidate-manifest.json').read_text())
for n,m in manifest.items():
 a=(p/'before'/n).read_text();b=(p/'candidates'/n).read_text();bb=b.encode();ckey={'file':n,'sha256':hashlib.sha256(bb).hexdigest(),'bytes':len(bb)};assert ckey['sha256']==m['candidate_sha256'];assert len(bb)==m['candidate_bytes'];assert hashlib.sha256(a.encode()).hexdigest()==m['before_sha256']
 ca=Counter(t for _,t in units(b));changed=[];ls=[]
 for num,(line,t) in enumerate(units(a),1):
  h=hashlib.sha256(t.encode()).hexdigest();r={'unit':num,'before_line':line,'sha256':h,'first_line':t.splitlines()[0][:160]}
  if ca[t]:ca[t]-=1;r['disposition']='BYTE EXACT'
  else:
   r.update(disposition='SOURCE-JUSTIFIED SURGICAL REPLACEMENT',before_text=t)
   if t.startswith('version:'):why='Monotonic substantive version advance'
   elif t.startswith('description:'):why='Estimated-tax description now distinguishes statutory baseline from published AEATroute'
   elif 'Out of scope:' in t:why='README status now reflects published route and precise remaining boundary; all domain partial mappings unchanged'
   elif t.startswith('|'):why='Entry-limit table retains ordinary values and source URLs; adds distinct administrative column'
   elif t.startswith('### Objective-method'):why='Updated heading accurately identifies ordinary text and current published route'
   elif n=='es-income-tax.md' and t.startswith('Confirm normal,'):why='Old method paragraph retained as prefix; adds linked updated entry/election route'
   elif 'simplified-regime' in t or 'AEAT entry page' in t or 'Not yet confirmed' in t or 'Not yet confirmed' in t or n in ['spain-vat-return.md','es-income-tax.md']:why='Old conflict/reservation replaced by actual later-read post-repeal explanation; all unrelated rules/reservations retained'
   else:raise AssertionError(('Unclassified old unit',n,line,t[:250]))
   r['reason']=why;changed.append(r)
  ls.append(r)
 # URL order/multiplicity, exact oa, all old source rows, metadata, H2, attribution/CTA.
 urls=lambda z:re.findall(r'https?://[^\s)<>\]]+',z)
 old,new=urls(a),urls(b);it=iter(new);url_order=all(any(v==x for v in it) for x in old);assert url_order
 oa=lambda z:re.findall(r'^```oa-check\n.*?^```',z,re.M|re.S)
 assert oa(a)==oa(b);assert len(oa(a))==(0 if n=='README.md' else 2)
 assert re.findall(r'^## .*',a,re.M)==re.findall(r'^## .*',b,re.M)
 if n!='README.md':
  assert a[a.index('<!-- openaccountants-cta-block -->'):]==b[b.index('<!-- openaccountants-cta-block -->'):]
  af,bf=a.split('---',2)[1],b.split('---',2)[1]
  remove=lambda z:'\n'.join(x for x in z.splitlines() if not x.startswith('version:') and not(n=='es-estimated-tax.md' and x.startswith('description:')))
  assert remove(af)==remove(bf)
  oldrows=[x for x in a[a.index('## Sources'):].splitlines() if x.startswith('|')];assert all(x in b for x in oldrows)
 else:assert a.split('---',2)[1]==b.split('---',2)[1]
 checks.append(dict(ckey,old_url_occurrences=len(old),old_url_order_preserved=True,oa_exact=True,protected_meta_exact=True,source_rows_exact=True,units=len(ls),changed_units=len(changed)))
 ledger.append({'file':n,'units':ls})
(q/'unit-preservation-ledger.json').write_text(json.dumps(ledger,indent=2));(q/'preservation-controls.json').write_text(json.dumps(checks,indent=2))
(q/'reviewed-candidates').mkdir(exist_ok=True)
for n in manifest:shutil.copyfile(p/'candidates'/n,q/'reviewed-candidates'/n)
# Use actual repository's arithmetic runner, limited to the four candidates.
cmd=[sys.executable,str(Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain/scripts/check-examples.py'))]+[str(q/'reviewed-candidates'/n) for n in manifest if n!='README.md']
r=subprocess.run(cmd,capture_output=True,text=True);(q/'oa-run.log').write_text(r.stdout+r.stderr);assert r.returncode==0
print(json.dumps({'arithmetic_gate_controls':len(controls),'original_oa_runner':r.stdout.strip(),'files':checks},indent=2))
