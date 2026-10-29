# Initial generic adapter met explicitly null nativeLF on own official web JSON observation. Correctly treats it as decoded web observation, no rawHTML/native-reader span invented.
from pathlib import Path
import json,hashlib,re,sys
R=Path(__file__).parent;O=R.parent;H=lambda b:hashlib.sha256(b).hexdigest();norm=lambda s:' '.join(s.split());bank=[]
def walk(v,origin):
 if isinstance(v,dict):
  q=v.get('exact_quote',v.get('exact_original_language_quote'));raw=v.get('raw_sha256',v.get('source_sha256'))
  if q and raw:bank.append((raw,norm(q),origin))
  for z in v.values():walk(z,origin)
 elif isinstance(v,list):
  for z in v:walk(z,origin)
for p in R.glob('*.json'):
 if any(k in p.name for k in ['quote-reuse-plan','selected-source','source-read-ledger']):
  try:walk(json.loads(p.read_text()),p.name)
  except json.JSONDecodeError:pass
# Earliest full PIT actual scopes already completed before quote-plan convention.
for slug in ['de-income-tax','de-self-employed-income-tax','de-employee-income-tax','de-partners-and-part-year','de-corporate-tax','leaving-germany-exit-tax']:
 p=O/'germany-ledger-writer-2026-10-28/support'/slug/'actual-read-quotes.json'
 if p.exists():walk(json.loads(p.read_text()),slug+' completed first-PIT source reading')
allresults=[]
for name in sys.argv[1:]:
 D=O/name;x=json.loads((D/'successor-inventory.json').read_text());pairs=x if isinstance(x,list)else[x];m=json.loads((D/'artifact-manifest.json').read_text());m=m.get('artifacts',m)if isinstance(m,dict)else m
 for v in m:assert H((D/v['path']).read_bytes())==v['sha256'],v
 ops=json.loads((D/'exact-operations.json').read_text());out=[]
 for pair in pairs:
  slug=pair['slug'];a=(D/'before'/f'{slug}.md').read_text();b=(D/'after'/f'{slug}.md').read_text();local=ops[slug]if isinstance(ops,dict)else ops;s=a
  for op in local:
   lo=op.get('before',op.get('old'));hi=op.get('after',op.get('new'));assert s.count(lo)==1,(slug,op);s=s.replace(lo,hi,1)
  assert s==b
  for op in reversed(local):
   lo=op.get('before',op.get('old'));hi=op.get('after',op.get('new'));assert s.count(hi)==1,(slug,op);s=s.replace(hi,lo,1)
  assert s==a;assert H(b.encode())==pair['Guide_sha256'];assert H(Path(pair['ledger_path']).read_bytes())==pair['ledger_sha256'];assert len(b.encode())==pair.get('bytes',pair.get('Guide_bytes'));assert re.findall(r'```oa-check.*?```',a,re.S)==re.findall(r'```oa-check.*?```',b,re.S)
  strip=lambda z:re.sub(r'^(version|last_updated):.*\n','',z.split('---',2)[1],flags=re.M)
  assert strip(a)==strip(b)
  url=lambda z:re.findall(r'https?://[^\s)<>|]+',z)
  oldurls=url(a);newurls=url(b);pos=0
  for u in oldurls:
   try:pos=newurls.index(u,pos)+1
   except ValueError:raise AssertionError(('oldURLorder',slug,u))
  marker='<!-- openaccountants-cta-block -->';assert(marker in a)==(marker in b)
  if marker in a:assert a[a.index(marker):]==b[b.index(marker):]
  rp=D/'support'/slug/'rows.json';rp=next(v for v in [rp,D/'support/current-rule-rows.json',D/'support/rows.json']if v.exists());rows=json.loads(rp.read_text());ls=b.split('\n')
  for q in rows:
   span=q.get('native_LF',q.get('LF'));l,h=span if isinstance(span,list)else(span,span);assert '\n'.join(ls[l-1:h])==q['wording'],(slug,q['id'])
  out.append({'pair':pair,'before_sha256':H(a.encode()),'operations':len(local),'full_inverse':True,'all_native_current_rows':len(rows),'original_oa_byteexact':len(re.findall(r'```oa-check',a)),'protected_metadata_CTA_oldURLorder':True})
 sourcefile=next((D/f for f in ['own-actual-read-quotes.json','own-read-receipt.json']if(D/f).exists()),None);sources=[]
 if sourcefile:
  qs=json.loads(sourcefile.read_text());qs=list(qs.values())if isinstance(qs,dict)else qs
  for q in qs:
   raw=q.get('raw_path',q.get('path'));sha=q.get('raw_sha256',q.get('sha256'));reader=q['reader_path'];assert H(Path(raw).read_bytes())==sha;assert H(Path(reader).read_bytes())==q['reader_sha256'];span=q['native_LF'];words=q.get('exact_quote',q.get('exact_original_language_quote'));l,h=span if span else (None,None);assert (words in '\n'.join(Path(reader).read_text().split('\n')[l-1:h])) if span else words in json.dumps(json.loads(Path(reader).read_text()),ensure_ascii=False);matches=[origin for sh,old,origin in bank if sh==sha and norm(words)in old];rec={'id':q['id'],'reader_path':reader,'raw_sha256':sha,'reader_sha256':q['reader_sha256'],'native_LF':[l,h],'quote_sha256':H(words.encode()),'exact_prior_read_bridge':matches[:1]}
   if not matches:print('UNBRIDGED',name,q['id'],l,h)
   sources.append(rec)
 result={'successor_folder':name,'manifest_members_rehashed':len(m),'pairs':out,'sources':sources,'status':'Mechanical exact checks only; final independent legal/read/control verdict supplied separately.'};allresults.append(result);print('CHECKED',name,len(m),'members',[(z['pair']['slug'],z['all_native_current_rows'])for z in out])
(R/'pending-successor-mechanical-results.json').write_text(json.dumps(allresults,indent=2)+'\n')
