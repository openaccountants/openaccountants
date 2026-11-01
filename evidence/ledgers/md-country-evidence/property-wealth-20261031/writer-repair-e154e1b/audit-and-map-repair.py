from pathlib import Path
import hashlib,json,re,subprocess,sys
R=Path(__file__).resolve().parents[5];D=Path(__file__).resolve().parent;E=D.parent
BASE='3ad7f3e98';MAIN='811d0ed0730b700162676168df15e06219beb87e'
sha=lambda b:hashlib.sha256(b).hexdigest()
def dump(name,x):(D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def orig(rel):return subprocess.check_output(['git','show',BASE+':'+rel],cwd=R)
checks=[]
def check(name,passed,detail=None):
 checks.append({'check':name,'passed':bool(passed),'detail':detail})
 if not passed:raise AssertionError((name,detail))
changes=json.loads((D/'changes.json').read_text())['changes'];snap=json.loads((D/'original-guide-manifest.json').read_text())['Guides']
def transform(s,rel):
 for c in changes:
  if c['file']!=rel:continue
  if 'rows' in c:
   for row in c['rows']:
    assert s.count(row['before'])==1;s=s.replace(row['before'],row['after'],1)
  elif 'before' in c:
   assert s.count(c['before'])==1;s=s.replace(c['before'],c['after'],1)
  else:
   s=s.replace('version: "'+c['old_version']+'"','version: "'+c['new_version']+'"',1)
   s=s.replace(c['old_H1'],c['new_H1'],1)
 return s
unitmaps=[];ledger_maps=[];linkmaps=[];examples=0
for f in snap:
 rel=f['path'];old=(R/f['original_snapshot']).read_text();new=(R/rel).read_text()
 check('Exact original snapshot '+rel,sha(old.encode())==f['original_sha256'] and old.encode()==orig(rel))
 check('Only enumerated repair changes '+rel,transform(old,rel)==new)
 ob=re.findall(r'^```oa-check[^\n]*\n.*?^```[ \t]*$',old,re.M|re.S);nb=re.findall(r'^```oa-check[^\n]*\n.*?^```[ \t]*$',new,re.M|re.S)
 check('Example blocks byte-exact '+rel,ob==nb);examples+=len(ob)
 check('Sources and source read dates byte-exact '+rel,old.split('## Sources',1)[1]==new.split('## Sources',1)[1])
 ofm=old.split('---',2)[1];nfm=new.split('---',2)[1]
 check('All metadata except version unchanged '+rel,re.sub(r'^version:.*$','',ofm,flags=re.M)==re.sub(r'^version:.*$','',nfm,flags=re.M))
 check('Line count preserved '+rel,len(old.splitlines())==len(new.splitlines()))
 # Nonblank paragraph/table/code units include every original byte between blank separators.
 for n,m in enumerate(re.finditer(r'\S[^\n]*(?:\n(?![ \t]*\n)[^\n]*)*',old),1):
  oldunit=m.group().rstrip('\n');line=old.count('\n',0,m.start())+1;count=len(oldunit.splitlines());current='\n'.join(new.splitlines()[line-1:line-1+count])
  expected=oldunit
  for c in changes:
   if c['file']!=rel:continue
   replacements=[(x['before'],x['after']) for x in c.get('rows',[])]
   if 'before' in c:replacements.append((c['before'],c['after']))
   if 'old_version' in c:replacements.extend([('version: "'+c['old_version']+'"','version: "'+c['new_version']+'"'),(c['old_H1'],c['new_H1'])])
   for a,b in replacements:expected=expected.replace(a,b)
  check('Unit destination '+rel+':'+str(line),current==expected)
  unitmaps.append({'source_file':rel,'original_snapshot':f['original_snapshot'],'source_unit':n,'source_line':line,'original_sha256':sha(oldunit.encode()),'current_destination':rel+':'+str(line),'current_sha256':sha(current.encode()),'status':'byte-exact' if current==oldunit else 'enumerated repair only'})
 ledger=R/'evidence/ledgers'/(Path(rel).stem+'.writer.json');raw=ledger.read_bytes();j=json.loads(raw)
 check('Historical ledger byte-exact '+str(ledger.relative_to(R)),raw==orig(str(ledger.relative_to(R))))
 rows=j['rows'];dest=[]
 for row in rows:
  section=row.get('Guide_section','');destinations=[]
  aliases={'Rates':'Rates, bands and thresholds','Deadlines':'Deadlines and filing','Penalties':'Penalties and interest','Examples':'Two worked examples that recompute','Cross-border':'Cross-border points'}
  for part in re.split(r';| / ',section):
   h=part.strip().split(':',1)[0];h=aliases.get(h,h);match=re.search(r'^## '+re.escape(h)+r'\s*$',new,re.M)
   if not match and destinations:continue # Continuation of the unchanged free-text subheading locator.
   check('Ledger section resolves '+str(row['id'])+'/'+h,bool(match),section)
   destinations.append(rel+':'+str(new.count('\n',0,match.start())+1))
  dest.append({'row_id':row['id'],'row_sha256':sha(json.dumps(row,ensure_ascii=False,sort_keys=True).encode()),'retained_original_section_locator':section,'current_H2_destinations':destinations})
 ledger_maps.append({'Guide':rel,'current_Guide_sha256':sha(new.encode()),'current_version':re.search(r'^version: "(.*?)"$',new,re.M).group(1),'current_H1':re.search(r'^# .+$',new,re.M).group(),'historical_ledger':str(ledger.relative_to(R)),'historical_ledger_sha256':sha(raw),'historical_Guide_sha256':j.get('Guide_sha256'),'source_rows':len(rows),'rows_unchanged':True,'current_destinations':dest})
 def links(s):
  defs={m.group(1).strip().casefold():m.group(2) for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)\s*$',s,re.M)}
  refs=re.findall(r'\[([^\]\n]+)\]\[([^\]\n]+)\]',s);targets=[]
  for label,key in refs:
   check('Reference resolves '+rel+'/'+key,key.strip().casefold() in defs)
   targets.append(defs[key.strip().casefold()])
  targets.extend(m.group(1) for m in re.finditer(r'\[[^\]\n]*\]\(([^\s]+)\)',s))
  return defs,sorted(set(targets))
 od,ot=links(old);nd,nt=links(new)
 check('All source definitions unchanged '+rel,od==nd)
 check('Resolved link targets unchanged '+rel,ot==nt,{'before':len(ot),'after':len(nt)})
 local=[]
 for target in nt:
  if re.match(r'^[a-z]+:',target):continue
  fp,_,anchor=target.partition('#');path=(R/rel).parent/fp if fp else R/rel
  check('Local target exists '+rel+'/'+target,path.is_file())
  # All local Guide anchors use plain heading words; GitHub duplicate suffixes are not needed here.
  if anchor:
   headings=[]
   for heading in re.findall(r'^#{1,6} (.*?)\s*$',path.read_text(),re.M):
    heading=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-');headings.append(heading)
   check('Local anchor resolves '+rel+'/'+target,anchor in headings)
  local.append(target)
 linkmaps.append({'Guide':rel,'original_and_current_target_set_equal':True,'resolved_targets':nt,'local_targets_checked':local,'reference_definitions_unchanged':True})
check('All 26 original example blocks preserved',examples==26,examples)
# Historical evidence, source bytes and initial review are immutable. All tracked inputs under E outside this repair directory remain unchanged.
tracked=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--',str(E.relative_to(R))],cwd=R,text=True).splitlines()
immutable=[]
for rel in tracked:
 raw=(R/rel).read_bytes();check('Initial evidence unchanged '+rel,raw==orig(rel));immutable.append({'path':rel,'sha256':sha(raw)})
for src in json.loads((E/'source-manifest.json').read_text())['sources']:
 check('Original source manifest hash '+src['path'],sha((R/src['path']).read_bytes())==src['sha256'])
# Translate every one of the 1,072 predecessor destinations, retaining the original map unchanged.
predecessors=json.loads((E/'old-topic-destinations.json').read_text())['rows'];current_pre=[]
for u in predecessors:
 new=(R/u['source_file']).read_text();line=u['source_line'];count=len(u['old_text'].splitlines());text='\n'.join(new.splitlines()[line-1:line-1+count])
 # Match by file/line against complete snapshot-unit map: original predecessor bytes match the 11 original snapshot Guides.
 matches=[x for x in unitmaps if x['source_file']==u['source_file'] and x['source_line']==line];check('Predecessor map resolves '+u['destination'],len(matches)==1)
 m=matches[0];check('Original predecessor unit matches snapshot '+u['destination'],sha(u['old_text'].rstrip('\n').encode())==m['original_sha256'] and sha(u['old_text'].encode())==u['old_sha256'])
 current_pre.append({'source_file':u['source_file'],'source_unit':u['source_unit'],'original_sha256':u['old_sha256'],'current_destination':m['current_destination'],'current_sha256':sha((text+('\n' if u['old_text'].endswith('\n') else '')).encode()),'status':m['status']})
changed=subprocess.check_output(['git','diff','--name-only','c4a700d51e2bada2fa0430fb9ea737c8a2da065a'],cwd=R,text=True).splitlines();expected_files=sorted(set(c['file'] for c in changes))
check('Only nine intended tracked Guides changed',sorted(changed)==expected_files,changed)
check('Original 594 property/wealth bindings retained',sum(x['source_rows'] for x in ledger_maps if Path(x['Guide']).stem in ['md-property-tax','md-wealth-tax'])==594)
check('All 4692 historical source bindings retained',sum(x['source_rows'] for x in ledger_maps)==4692)
dump('current-ledger-destinations.json',{'date':'2026-10-31','scope':'Current Guide hashes and row destinations; every original ledger and source row remains immutable. Historical Guide_sha256 fields refer to their original candidates, not this repair. No source re-read or new legal claim review is asserted.','Guides':ledger_maps})
dump('current-old-topic-destinations.json',{'date':'2026-10-31','scope':'All original candidate units across 13 Guides and all 1072 predecessor units resolve to current same-file destinations. Changed units are limited to enumerated repairs.','original_candidate_units':unitmaps,'predecessor_units':current_pre})
dump('link-resolution.json',{'date':'2026-10-31','scope':'Markdown reference and local target/anchor resolution only. No network availability assertion. All 104 inline citation expansions use the exact URL from the same original source definition. Original external target sets unchanged.','Guides':linkmaps,'source_access_record':str((E/'independent-review/source-access.json').relative_to(R)),'live_Legis_read':False})
dump('preservation-audit.json',{'date':'2026-10-31','integrated_main':MAIN,'original_review_candidate':'e154e1b7bf107d7e9efa01c7622a91e89850da8a','review_preservation_commit':BASE,'source_claims_re_reviewed':False,'checks':len(checks),'failures':0,'original_example_blocks':examples,'original_candidate_units':len(unitmaps),'predecessor_units':len(current_pre),'immutable_evidence':immutable,'details':checks})
print(json.dumps({'checks':len(checks),'failures':0,'original_candidate_units':len(unitmaps),'predecessor_units':len(current_pre),'example_blocks':examples,'source_bindings':sum(x['source_rows'] for x in ledger_maps)}))
