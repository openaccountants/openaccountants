from pathlib import Path
import json,hashlib,re,subprocess
R=Path.cwd();D=R/'evidence/ledgers/md-country-evidence/property-wealth-20261031/writer-repair-e154e1b';O=D/'independent-closure'
sha=lambda x:hashlib.sha256(x).hexdigest()
checks=[]
def ck(n,v):
 checks.append({'check':n,'pass':bool(v)})
 if not v:raise AssertionError(n)
def old(p):return subprocess.check_output(['git','show','3ad7f3e98:'+p])
m=D/'repair-input-manifest.json';ck('repair manifest pinned',sha(m.read_bytes())=='f2e1d43902992ac39a25bdab361636642fadec77cfcda8f7509db2b7941680ac')
inputs=json.loads(m.read_text())['inputs']
for x in inputs:ck('manifest '+x['path'],sha((R/x['path']).read_bytes())==x['sha256'] and len((R/x['path']).read_bytes())==x['bytes'])
changes=json.loads((D/'changes.json').read_text())['changes'];snap=json.loads((D/'original-guide-manifest.json').read_text())['Guides'];expanded=0;examples=0
for s in snap:
 rel=s['path'];a=(R/s['original_snapshot']).read_text();b=(R/rel).read_text();ck('snapshot '+rel,a.encode()==old(rel));v=a
 defs=dict(re.findall(r'^\[([^\]]+)\]:\s*(\S+)\s*$',a,re.M))
 for c in changes:
  if c['file']!=rel:continue
  if 'rows' in c:
   for row in c['rows']:
    expected=row['before']
    for exp in row['expansions']:
     ck('inline target '+rel+'/'+exp['reference'],defs[exp['reference']]==exp['url'])
     ref='['+exp['label']+']['+exp['reference']+']';replacement='['+exp['label']+']('+exp['url']+')';ck('original reference '+rel,ref in expected);expected=expected.replace(ref,replacement)
    ck('citation-only row '+rel,expected==row['after']);ck('unique row '+rel,v.count(row['before'])==1);v=v.replace(row['before'],row['after']);expanded+=1
  elif 'before' in c:
   ck('unique legal repair '+c['before'],v.count(c['before'])==1);v=v.replace(c['before'],c['after'])
  else:
   v=v.replace('version: "'+c['old_version']+'"','version: "'+c['new_version']+'"',1).replace(c['old_H1'],c['new_H1'],1)
 ck('all bytes explained '+rel,v==b)
 ck('metadata except version exact '+rel,re.sub(r'^version:.*$','',a.split('---',2)[1],flags=re.M)==re.sub(r'^version:.*$','',b.split('---',2)[1],flags=re.M))
 ck('Sources dates CTA preserved '+rel,a.split('## Sources',1)[1]==b.split('## Sources',1)[1])
 blocks=lambda t:re.findall(r'^```oa-check[^\n]*\n.*?^```[ \t]*$',t,re.M|re.S)
 ck('examples exact '+rel,blocks(a)==blocks(b));examples+=len(blocks(a))
 if any('old_version' in c and c['file']==rel for c in changes):
  version=re.search(r'^version: "(.*?)"$',b,re.M).group(1);ck('changed H1 version '+rel,re.search(r'^# .*v'+re.escape(version)+r'$',b,re.M) is not None)
# All original source/ledger/review evidence, not just sources selected by the repair manifest.
original_evidence=subprocess.check_output(['git','ls-tree','-r','--name-only','3ad7f3e98','--','evidence/ledgers'],text=True).splitlines()
changed=set(subprocess.check_output(['git','diff','--name-only','3ad7f3e98','--','evidence/ledgers'],text=True).splitlines())
for p in original_evidence:ck('original evidence '+p,p not in changed)
unitmap=json.loads((D/'current-old-topic-destinations.json').read_text())
for u in unitmap['original_candidate_units']:
 a=(R/u['original_snapshot']).read_text().splitlines();rel,line=u['current_destination'].rsplit(':',1);line=int(line);units=list(re.finditer(r'\S[^\n]*(?:\n(?![ \t]*\n)[^\n]*)*',(R/u['original_snapshot']).read_text()));text=units[u['source_unit']-1].group().rstrip('\n');ck('original unit '+u['current_destination'],sha(text.encode())==u['original_sha256']);current='\n'.join((R/rel).read_text().splitlines()[line-1:line-1+len(text.splitlines())]);ck('current unit '+u['current_destination'],sha(current.encode())==u['current_sha256'])
pre=json.loads((D.parent/'old-topic-destinations.json').read_text())['rows']
for a,b in zip(pre,unitmap['predecessor_units']):
 ck('predecessor locator '+a['destination'],a['source_file']==b['source_file'] and a['old_sha256']==b['original_sha256']);rel,line=b['current_destination'].rsplit(':',1);t='\n'.join((R/rel).read_text().splitlines()[int(line)-1:int(line)-1+len(a['old_text'].splitlines())]);t+='\n' if a['old_text'].endswith('\n') else '';ck('predecessor current hash '+a['destination'],sha(t.encode())==b['current_sha256'])
count=0
for g in json.loads((D/'current-ledger-destinations.json').read_text())['Guides']:
 ck('current ledger Guide hash '+g['Guide'],sha((R/g['Guide']).read_bytes())==g['current_Guide_sha256']);l=json.loads((R/g['historical_ledger']).read_text());ck('historical ledger hash '+g['historical_ledger'],sha((R/g['historical_ledger']).read_bytes())==g['historical_ledger_sha256']);ck('row count '+g['Guide'],len(l['rows'])==len(g['current_destinations'])==g['source_rows']);count+=len(l['rows'])
 for row,dest in zip(l['rows'],g['current_destinations']):
  ck('row hash '+row['id'],sha(json.dumps(row,ensure_ascii=False,sort_keys=True).encode())==dest['row_sha256'] and row['id']==dest['row_id'])
  for dst in dest['current_H2_destinations']:
   rel,line=dst.rsplit(':',1);ck('current H2 '+row['id'],(R/rel).read_text().splitlines()[int(line)-1].startswith('## '))
ck('104 expansions',expanded==104);ck('26 example blocks',examples==26);ck('1072 predecessors',len(pre)==len(unitmap['predecessor_units'])==1072);ck('4692 rows',count==4692)
result={'candidate':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'manifest_sha256':sha(m.read_bytes()),'inputs':len(inputs),'checks':len(checks),'failures':0,'citation_rows':expanded,'original_candidate_units':len(unitmap['original_candidate_units']),'predecessor_units':len(pre),'source_bindings':count,'example_blocks_preserved':examples,'original_evidence_files':len(original_evidence),'details':checks}
(O/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='details'}))
