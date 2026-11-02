from pathlib import Path
import re,json,subprocess,hashlib
r=Path(__file__).resolve().parents[3];p=Path(__file__).resolve().parent
baseline='a6f0f5b1f50b3edc7f3faef8199852188a60f35c';rows=[]
headings={'## What this file is and scope':'## Who this applies to','## Formation and registration':'### Formation and registration','## Capital, ownership and reporting thresholds':'## Rates, bands and thresholds','## Ownership and recurring management duties':'### Ownership and recurring management duties','## Accounts, audit and separate deadlines':'### Accounts and audit','## Enforcement, retention and output checks':'## Penalties and interest','## Disclaimer':'### General reference notice'}
for f in sorted((r/'skills/faroe-islands').glob('fo-*.md')):
 if f.name=='fo-payroll-levy.md':continue
 oldpath='skills/international/faroe-islands/'+f.name;b=subprocess.check_output(['git','show',baseline+':'+oldpath],cwd=r);old=b.decode();new=f.read_text();newlines=new.splitlines();refs=dict(re.findall(r'^\[([^]]+)\]:\s+(https?://\S+)',old,re.M));used=set();units=[]
 for i,line in enumerate(old.splitlines()):
  if not line.strip():continue
  target=line;reason='exact'
  if line.startswith('|'):
   target=re.sub(r'\[([^]\n]+)\]\[([^]\n]+)\]',lambda m:'['+m.group(1)+']('+refs[m.group(2)]+')' if m.group(2) in refs else m.group(0),line)
   if target!=line:reason='same reference target rendered as inline URL'
  if f.name=='fo-company-registration-reporting.md':
   if line in headings:target=headings[line];reason='canonical heading, body preserved'
   if line=='version: 0.3':target='version: 0.4';reason='new examples/version advance'
   if line=='last_updated: 2026-10-28':target='last_updated: 2026-10-31';reason='new examples/date advance'
   if line.startswith('# Faroe Islands company registration and annual reporting v0.3'):target=line.replace('v0.3','v0.4');reason='heading version advance'
  candidates=[j for j,x in enumerate(newlines) if x==target and j not in used]
  assert candidates,(f.name,i+1,line)
  j=candidates[0];used.add(j);units.append({'old_line':i+1,'old_text':line,'destination':str(f.relative_to(r))+':'+str(j+1),'disposition':reason})
 # CTA must remain byte-exact.
 marker='<!-- openaccountants-cta-block -->';assert (marker in old)==(marker in new),f.name
 if marker in old:assert old.split(marker,1)[1]==new.split(marker,1)[1],f.name
 rows.append({'old_path':oldpath,'new_path':str(f.relative_to(r)),'baseline_sha256':hashlib.sha256(b).hexdigest(),'current_sha256':hashlib.sha256(new.encode()).hexdigest(),'nonblank_units':units,'cta_byte_exact':True,'old_rules_removed':0})
# Historical ledgers/review evidence are relocated byte-exact.
files=subprocess.check_output(['git','ls-tree','-r','--name-only',baseline,'ledgers/'],cwd=r,text=True).splitlines(); evidence=[]
for old in files:
 if not(old.startswith('ledgers/fo-') or old.startswith('ledgers/faroe-islands-') or old=='ledgers/README.md'):continue
 data=subprocess.check_output(['git','show',baseline+':'+old],cwd=r);new=('evidence/ledgers/faroe-islands-2026-evidence/ROOT-LEDGERS-README.md' if old=='ledgers/README.md' else 'evidence/'+old);q=r/new;assert q.read_bytes()==data,old
 evidence.append({'old':old,'new':new,'sha256':hashlib.sha256(data).hexdigest(),'byte_exact':True})
result={'baseline':baseline,'guide_count':len(rows),'nonblank_unit_count':sum(len(x['nonblank_units']) for x in rows),'old_rules_removed':0,'guides':rows,'relocated_evidence_count':len(evidence),'relocated_evidence':evidence}
(p/'preservation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print({k:result[k] for k in ['guide_count','nonblank_unit_count','old_rules_removed','relocated_evidence_count']})
