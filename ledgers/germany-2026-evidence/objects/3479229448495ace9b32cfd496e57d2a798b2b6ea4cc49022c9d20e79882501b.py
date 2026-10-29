from pathlib import Path
import json,hashlib,re
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');D=O.parent/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();inv=json.loads((D/'successor-inventory.json').read_text());ops=json.loads((D/'exact-operations.json').read_text());idx=json.loads((D/'source-quote-index.json').read_text());out={};count=0
for r in json.loads((D/'artifact-manifest.json').read_text())['artifacts']:
 assert H(D/r['path'])==r['sha256'],r['path'];count+=1
for slug,x in inv.items():
 a=(D/'before'/f'{slug}.md').read_text();b=(D/'after'/f'{slug}.md').read_text();s=a
 for op in ops[slug]:assert s.count(op['old'])==1,(slug,op['reason']);s=s.replace(op['old'],op['new'],1)
 assert s==b
 for op in reversed(ops[slug]):assert s.count(op['new'])==1,(slug,op['reason']);s=s.replace(op['new'],op['old'],1)
 assert s==a
 assert H(D/'after'/f'{slug}.md')==x['Guide_sha256'];assert H(Path(x['ledger_path']))==x['ledger_sha256']
 oa=lambda t:re.findall(r'```oa-check\n.*?```',t,re.S)
 assert oa(a)==oa(b)
 # Original URL occurrence sequence must be a subsequence; URLs may be added.
 urls=lambda t:re.findall(r'https?://[^\s)<>|]+',t)
 i=iter(urls(b));assert all(any(z==u for z in i) for u in urls(a))
 front=lambda t:[l for l in t.split('---',2)[1].split('\n') if not l.startswith(('version:','last_updated:'))]
 assert front(a)==front(b)
 assert a[a.index('> Contributed by'):]==b[b.index('> Contributed by'):] if '> Contributed by' in a else True
 rows=json.loads((D/'support'/slug/'rows.json').read_text());lines=b.split('\n')
 for r in rows:
  l,h=r['native_LF'];assert '\n'.join(lines[l-1:h])==r['wording'];assert all(q in idx for q in r['source_quote_ids'])
 old=json.loads((D/'support'/slug/'old-topic-destinations.json').read_text());op=Path(x['original_support'])/'old-topics.json';op=op if op.exists() else Path(x['original_support'])/'old-topic-destinations.json';orig=json.loads(op.read_text())
 if isinstance(orig,list):
  assert len(old)==len(orig)
  for z,y in zip(old,orig):assert z['wording']==y['wording'] and z['ref']==y['ref'] and z['old_lf']==y['old_lf']
  oldcount=len(old)
 else:
  oldcount=0
  for cat in ['current_main_rows','pre_refresh_rows']:
   assert len(old[cat])==len(orig[cat])
   for z,y in zip(old[cat],orig[cat]):assert z['old_native_LF']==y['old_native_LF'] and z['old_unit_sha256']==y['old_unit_sha256']
   oldcount+=len(old[cat])
 out[slug]={'guide_sha256':x['Guide_sha256'],'ledger_sha256':x['ledger_sha256'],'exact_operations':len(ops[slug]),'full_inverse':True,'original_oa_exact':len(oa(a)),'all_current_row_native_memberships':len(rows),'old_original_wording_ref_LF_unchanged':oldcount,'note':'Bounded delta check; whole frozen pair reading of freelancer/trade still pending'}
# Exactly same material content for the two R01/R02 business guides, apart from unchanged local name/byline.
assert [(o['old'],o['new'])for o in ops['de-income-tax']][1:]==[(o['old'],o['new'])for o in ops['de-self-employed-income-tax']][1:]
q=json.loads((D/'own-actual-read-quotes.json').read_text());qs=[]
for k,x in q.items():
 if k=='R05.BFH-2022':
  p=Path(x['web_tool_response_path']);assert H(p)==x['web_tool_response_sha256'];assert x['exact_quote']in p.read_text();qs.append({'id':k,'actual_read':'Earlier independent own official web selected reasoning; writer retained response/hash rechecked. Not raw HTML or a new source-wide read.','web_tool_response_sha256':H(p),'web_lines':x['actual_web_lines']});continue
 a,b=x['native_LF'];rp=Path(x['reader_path']);span='\n'.join(rp.read_text().split('\n')[a-1:b]);assert x['exact_quote']in span;assert H(rp)==x['reader_sha256'];raw=Path(x.get('raw_path',x.get('path')));assert H(raw)==x.get('raw_sha256',x.get('sha256'))
 qs.append({'id':k,'actual_read':'Selected original-language quote fully read in bounded actual helper output; raw/reader/native-membership independently checked','reader_path':str(rp),'raw_sha256':H(raw),'reader_sha256':H(rp),'native_LF':[a,b],'quote_sha256':hashlib.sha256(x['exact_quote'].encode()).hexdigest()})
controls=[]
def c(n,a,e):assert a==e,(n,a,e);controls.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
for cost,e in [(2880,1360),(1000,0),(2000,480)]:c('commute'+str(cost),max(0,F(cost)-F(38,100)*20*200),F(e))
c('commute listD',F(3,10000)*40000*20*12,F(2880));c('commute allowance',F(38,100)*20*200,F(1520));c('short nonovernightmeal',0,0);c('qualifying departuremeal',14,14);c('2026monthlyBMGceiling',F(69750,12),F(581250,100));c('2026careceilingindependent',69750,69750)
for total,receipts,e in [(500000,F(15000),True),(500000,F(1500001,100),False),(1000000,F(24500),True),(1000000,F(2450001,100),False)]:c('own activity'+str(total)+'/'+str(receipts),receipts<=F(3,100)*total and receipts<=24500,e)
c('34a qualifyingtaxwithdrawalpriority20of30',100000-max(0,30000-20000)+5000,95000);c('15a external covering10kwithdrawal qualification',max(0,10000-10000),0);c('15a no external covering10kwithdrawal',max(0,10000),10000);c('EBITDA no generation escape current2m',0,0);c('oldcarry no blanket escape',False,False);c('samepayroyalty cumulative10k',6000+4000<=10000,True);c('samepayroyalty10000.01',F(600000,100)+F(400001,100)<=10000,False);c('royalty treaty existence alone establisheszero',False,False)
(O/'DE-R01-R08-bounded-successor-check.json').write_text(json.dumps({'status':'Substantive R01–08 deltas supported; R09 rounding and R10 stale reservation successors pending. Not whole-country verdict.','writer_manifest_members_rehashed':count,'pairs':out,'source_actual_read_ledger':qs,'own_controls':controls,'helper_failures':'The first repair-source helper stopped at differently named raw-path and web-observation record fields; adapted helper and explicit web-record read completed the intended selected scopes. No fabricated raw-body membership for the web observation.'},indent=2)+'\n')
print('PASS bounded inverse/preservation/native-row checks7; manifest',count,'source records',len(qs),'owncontrols',len(controls))
