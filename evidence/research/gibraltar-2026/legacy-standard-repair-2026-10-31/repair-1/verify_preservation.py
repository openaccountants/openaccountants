from pathlib import Path
import re,json,hashlib,collections,yaml
R=Path(__file__).resolve().parents[5]; BASE=R/'evidence/research/gibraltar-2026/legacy-standard-repair-2026-10-31'; E=BASE/'repair-1'
report=[];fails=[]
for b in sorted((BASE/'before').glob('*.md')):
 old=b.read_text();p=R/'skills/gibraltar'/b.name;new=p.read_text(); of=yaml.safe_load(old.split('---',2)[1]);nf=yaml.safe_load(new.split('---',2)[1]);of.pop('version');of.pop('last_updated');nf.pop('version');nf.pop('last_updated');od=of.pop('description');nd=nf.pop('description');assert nd.startswith(od.rstrip()),b.name;assert 80<=len(nd.split())<=150,b.name;assert of==nf,b.name
 ob=old.split('---',2)[2];nb=new.split('---',2)[2];topic='Introduction';dests=[];records=[]
 nl=nb.splitlines();used=set();context=[];h2='Introduction';h3='';contexts=[]
 for x in nl:
  if x.startswith('## '):h2=x[3:];h3=''
  elif x.startswith('### '):h3=x[4:]
  contexts.append((h2,h3))
 for lineno,x in enumerate(ob.splitlines(),1):
  if x.startswith('## '):topic=x[3:];continue
  if x.startswith('#') or not x.strip():continue
  # Metadata has been parsed separately. Body version tagline is the only changed plain-text token.
  if re.fullmatch(r'.*v\d+\.\d+(?:\.\d+)?',x):
   pattern=re.sub(r'v\d+\.\d+(?:\.\d+)?','vVERSION',x)
   found=[i for i,z in enumerate(nl) if i not in used and re.sub(r'v\d+\.\d+(?:\.\d+)?','vVERSION',z)==pattern]
  else:
   found=[i for i,z in enumerate(nl) if i not in used and (z==x or (x.startswith(('|','- [')) and z.startswith(x)))]
  if not found:fails.append((b.name,lineno,x));continue
  i=found[0];used.add(i);records.append({'old_body_line':lineno,'old_topic':topic,'sha256':hashlib.sha256(x.encode()).hexdigest(),'new_body_line':i+1,'destination':list(contexts[i]),'reliable_topic_anchor':sum(1 for z in nl if z==x or (x.startswith(('|','- [')) and z.startswith(x)))==1})
 oldchecks=re.findall(r'```oa-check\n.*?\n```',ob,re.S);newchecks=re.findall(r'```oa-check\n.*?\n```',nb,re.S)
 assert all(x in newchecks for x in oldchecks),b.name
 marker='<!-- openaccountants-cta-block -->'
 assert (marker in old)==(marker in new),b.name
 if marker in old:assert old.split(marker,1)[1]==new.split(marker,1)[1],b.name
 topics={x['old_topic']:sorted(set(tuple(z['destination']) for z in records if z['old_topic']==x['old_topic'] and z['reliable_topic_anchor'])) for x in records}
 report.append({'slug':b.stem,'before_sha256':hashlib.sha256(b.read_bytes()).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'frontmatter_preserved_except_version_last_updated_and_documented_description_append':True,'CTA_suffix_identical':True,'original_checks':len(oldchecks),'current_checks':len(newchecks),'original_nonblank_nonheading_lines':len(records),'topic_destinations':topics,'line_bindings':records})
(E/'preservation.json').write_text(json.dumps({'guides':report,'failures':fails},indent=2)+'\n')
print('guides',len(report),'preserved lines',sum(x['original_nonblank_nonheading_lines'] for x in report),'failures',len(fails));print(json.dumps(fails[:25],indent=2))
assert not fails
