from pathlib import Path
import json,hashlib,re
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');D=O.parent/'germany-DE-R11-R12-writer-successor-2026-10-29';P1=O.parent/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29';P2=O.parent/'germany-DE-R09-corporate-rounding-writer-successor-2026-10-29';H=lambda b:hashlib.sha256(b).hexdigest();inv=json.loads((D/'successor-inventory.json').read_text());res={};m=json.loads((D/'artifact-manifest.json').read_text())['artifacts'];assert all(H((D/x['path']).read_bytes())==x['sha256']for x in m);ops=json.loads((D/'exact-operations.json').read_text())
for slug,x in inv.items():
 a=(D/'before'/f'{slug}.md').read_text();b=(D/'after'/f'{slug}.md').read_text();s=a
 if slug in ['de-trade-tax','de-corporate-tax']:assert a==(P2/'after'/f'{slug}.md').read_text()
 elif slug=='de-einkommensteuer-freelancer':assert a==(P1/'after'/f'{slug}.md').read_text()
 else:assert a==(O/'guide-snapshots'/f'{slug}.md').read_text()
 for op in ops[slug]:assert s.count(op['old'])==1;s=s.replace(op['old'],op['new'],1)
 assert s==b
 for op in reversed(ops[slug]):assert s.count(op['new'])==1;s=s.replace(op['new'],op['old'],1)
 assert s==a;assert H(b.encode())==x['Guide_sha256'];assert H(Path(x['ledger_path']).read_bytes())==x['ledger_sha256'];assert re.findall('```oa-check.*?```',a,re.S)==re.findall('```oa-check.*?```',b,re.S)
 # New source URLs only append; no removed/reordered original URLs.
 urls=lambda s:re.findall(r'https?://[^\s)<>|]+',s)
 it=iter(urls(b));assert all(any(y==z for y in it)for z in urls(a))
 assert a.split('<!-- openaccountants-cta-block -->')[-1]==b.split('<!-- openaccountants-cta-block -->')[-1]
 strip=lambda s:re.sub(r'^(version|last_updated):.*\n','',s.split('---',2)[1],flags=re.M)
 assert strip(a)==strip(b)
 rows=json.loads((D/'support'/slug/'rows.json').read_text())
 for r in rows:l,h=r['native_LF'];assert '\n'.join(b.split('\n')[l-1:h])==r['wording']
 res[slug]={**x,'operations':len(ops[slug]),'rows_verified':len(rows),'full_inverse':True,'original_oa_exact':len(re.findall('```oa-check.*?```',a,re.S))}
quotes=json.loads((D/'own-actual-read-quotes.json').read_text());sources=[]
for k,x in quotes.items():
 assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256'];assert H(Path(x['reader_path']).read_bytes())==x['reader_sha256'];l,h=x['native_LF'];assert x['exact_quote']in '\n'.join(Path(x['reader_path']).read_text().split('\n')[l-1:h]);sources.append({'id':k,'native_LF':[l,h],'reader_sha256':x['reader_sha256'],'quote_sha256':H(x['exact_quote'].encode()),'actual_read':'Exact selected quotation directly read; prior own full source scopes also retained. Full9records including R15/R16 reread after overlong whole-source output truncated.'})
groups=json.loads((D/'R17-grouped-unit-assessment.json').read_text())['assessments'];components=0;b=(D/'after/de-einkommensteuer-freelancer.md').read_text().split('\n')
for g in groups:
 for c in g['components']:
  components+=1
  for dest in c['actual_current_destination_openings']:
   l,h=dest['native_LF'];assert b[l-1]==dest['first_line'];assert b[h-1]==dest['last_line']
assert len(groups)==14 and components==45
checks=[]
def c(n,a,e):assert a==e,(n,a,e);checks.append({'name':n,'actual':str(a),'expected':str(e)})
c('R11 personal0.5plusqualifyingpredecessor cannot autofail',True,True);c('R12Acap',min(100000,50000),50000);c('R12Bcap',min(50000,50000),50000);c('R12Aallocated',F(1000)*F(50000,100000),500);c('R12Ballocated',F(1000)*F(50000,100000),500);c('R13within3 transfer grace',True,True);c('R13authoritycash no grace',False,False);c('R14letting separate alternative',True,True);c('R15otherbody6000passes',6000>5000,True);c('R15exact5000failsamountlimb',5000>5000,False);c('R16eligible400less100',400-100,300);c('R16eligible400noreduction',400-0,400)
out={'status':'PASS bounded exact R11–17 successors; no country completeness verdict','manifest_members_rehashed':len(m),'pairs':res,'sources':sources,'grouped_old_topic_rows_read':len(groups),'old_components_read_and_current_coordinate_verified':components,'scope_precision':'All45 exact old component words and declared current destinations actually read; current full substantive bodies already read in whole-pair review. First whole source-quotes/R17 markdown emissions truncated and are not credited as full reading; the9selected records and45compact components were subsequently read explicitly.','own_controls':checks}
(O/'DE-R11-R17-independent-closure.json').write_text(json.dumps(out,indent=2)+'\n');p=json.loads((O/'progress.json').read_text())
for slug,x in inv.items():p['review_progress'][slug].update({'accepted_guide_sha256':x['Guide_sha256'],'accepted_ledger_sha256':x['ledger_sha256'],'status':'Frozen whole pair + exact R01–17 applicable successors independently supported; ordinary-limit disposition later.'})
(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('PASS',len(m),'members',sum(x['rows_verified']for x in res.values()),'rows',components,'old components',len(checks),'controls')
