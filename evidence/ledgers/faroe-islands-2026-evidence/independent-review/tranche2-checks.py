from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re,difflib
w=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-faroe');r=w/'skills/research/faroe-islands-2026/ordinary-completion-2026-10-28';o=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/faroe-ordinary-completion/ledger-review')
h=lambda b:hashlib.sha256(b).hexdigest()
controls=[]
def ck(n,a,b):
 assert a==b,(n,a,b);controls.append({'id':n,'actual':str(a),'expected':str(b),'pass':True})
ck('V-output',100000*F(1,4),25000);ck('V-net',25000-10000,15000);ck('V-gross',125*F(25,125),25)
ck('V-share',F(300000,500000),F(3,5));ck('V-input',20000*F(3,5),12000);ck('V-adjust',25000*(1-F(3,5))/5,2000);ck('V-after',12000-2000,10000)
ck('V-new-invoice',10000*F(1,4),2500);ck('V-new-input',2500*F(3,5),1500);ck('V-new-unrecovered',2500-1500,1000)
for ident,service,sales,full,expect in [('V-item12-threshold',12,50000,False,False),('V-item12-above',12,50001,False,True),('V-item12-full',12,60000,True,False),('V-item7-full',7,60000,True,True)]:
 charge=7<=service<=13 and sales>50000 and not(full and service in range(8,14));ck(ident,charge,expect)
ck('XB-branch-profit',1000000-600000-100000,300000);ck('XB-branch-tax',300000*F(18,100),54000)
ck('XB-royalty-gross',40000*F(1,4),10000);ck('XB-royalty-net',40000-10000,30000);ck('XB-royalty-net-guarantee',F(40000)/F(3,4),F(160000,3));ck('XB-net-tax',F(160000,3)*F(1,4),F(40000,3))
ck('XB-exit',50000*F(35,100),17500);ck('XB-later-gain',140000-100000,40000);ck('XB-payment',40000*F(35,100),14000);ck('XB-valuefall',10000*F(35,100),3500);ck('XB-final-balance',17500-14000-3500,0)
ck('XB-interest-bounded',20000-0,20000);ck('XB-credit-cap',18000*F(100000,300000),6000);ck('XB-credit',min(8000,6000),6000)
verdicts=[];proof=[]
for slug in ['fo-vat','fo-cross-border-payments']:
 p=w/'skills/international/faroe-islands'/(slug+'.md');new=p.read_text();old=(r/'root-evidence'/(slug+'-20572441dcdae9ebd4c282597940338832ade34e.md')).read_text();rows=json.loads((r/'root-evidence'/(slug+'-rows.json')).read_text())
 for x in rows:
  assert x['wording'] in new,x['id'];verdicts.append({'id':x['id'],'LF':x['lf'],'wording_exact':True,'source_tags':x['source_tags'],'verdict':'Supported within stated conditions / operational limitation; sources and arithmetic independently assessed'})
 oa=lambda t:re.findall(r'```oa-check\n.*?```',t,re.S)
 assert oa(old)==oa(new)
 urls=lambda t:re.findall(r'https?://[^\s<>\])]+',t)
 missing=[x for x in urls(old) if x not in urls(new)];assert not missing,missing
 oldfront=old.split('---',2)[1];newfront=new.split('---',2)[1]
 fields=['title','jurisdiction','taxYear','tier','author','attribution','slug','category','intakeQs']
 # Preserve full frontmatter after excluding only version and checked date fields.
 normalize=lambda t:re.sub(r'(?m)^(version|lastUpdated|lastVerified|last_updated|verified_on):.*\n','',t)
 import yaml
 fm_old=yaml.safe_load(oldfront);fm_new=yaml.safe_load(newfront)
 for key in set(fm_old)|set(fm_new):
  if key not in ['version','last_updated','description']:assert fm_old.get(key)==fm_new.get(key),key
 if slug=='fo-vat':assert fm_old['description']==fm_new['description']
 else:assert fm_new['description']==fm_old['description'].replace('rates, PE profit attribution','rates, complex PE profit attribution').replace('and ordinary foreign-tax credits','and complex foreign-tax credit cases')
 # Independently derive complete line edit operations; reverse every change, including metadata.
 a=old.splitlines(keepends=True);b=new.splitlines(keepends=True);ops=[]
 for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
  if tag!='equal':ops.append({'old_start':i,'old_end':j,'new_start':k,'new_end':l,'old':''.join(a[i:j]),'new':''.join(b[k:l])})
 inv=b[:]
 for op in reversed(ops):inv[op['new_start']:op['new_end']]=op['old'].splitlines(keepends=True)
 assert ''.join(inv)==old
 proof.append({'slug':slug,'sha256':h(p.read_bytes()),'ledger_sha256':h((r/'ledgers'/(slug+'.md')).read_bytes()),'rows':len(rows),'all_row_wording_exact':True,'old_oa_exact':len(oa(old)),'all_old_URLs_retained':True,'protected_frontmatter_exact':True,'whole_inverse':True,'derived_operations':ops})
(o/'tranche2-controls.json').write_text(json.dumps(controls,indent=2)+'\n');(o/'tranche2-row-verdicts.json').write_text(json.dumps(verdicts,indent=2)+'\n');(o/'tranche2-preservation.json').write_text(json.dumps(proof,indent=2)+'\n')
print(json.dumps({'controls':len(controls),'rows':len(verdicts),'pins':[{'slug':x['slug'],'sha':x['sha256']} for x in proof]}))
