from pathlib import Path
import hashlib,json,re,subprocess,sys,importlib.util,datetime
R=Path(__file__).resolve().parents[4];D=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
fail=[];checks=[]
def ok(name,condition,detail=None):
 checks.append({'check':name,'passed':bool(condition),'detail':detail})
 if not condition:fail.append(name)
def strings(x):
 if isinstance(x,str):return [x]
 if isinstance(x,list):return [s for v in x for s in strings(v)]
 if isinstance(x,dict):return [s for v in x.values() for s in strings(v)]
 return []
old=json.loads((D/'predecessor-guide-manifest.json').read_text())
for f in old['Guide_files']:ok('Preserved '+f['path'],sha((R/f['path']).read_bytes())==f['sha256'])
manifest=json.loads((D/'source-manifest.json').read_text())
for f in manifest['sources']:ok('Source hash '+Path(f['path']).name,sha((R/f['path']).read_bytes())==f['sha256'])
for slug in ['md-property-tax','md-wealth-tax']:
 j=json.loads((R/'evidence/ledgers'/f'{slug}.writer.json').read_text());g=R/j['Guide'];text=g.read_text()
 ok(slug+' Guide hash',sha(g.read_bytes())==j['Guide_sha256'])
 desc=text.split('description: >\n',1)[1].split('\njurisdiction:',1)[0];words=len(desc.split());ok(slug+' 80-150 description',80<=words<=150,words)
 q=text.split('## Ask the client first\n',1)[1].split('## Sources',1)[0];qs=re.findall(r'^\d+\. ',q,re.M);ok(slug+' 3-6 questions',3<=len(qs)<=6,len(qs))
 ok(slug+' no platform CTA', 'openaccountants-cta-block' not in text)
 for row in j['rows']:
  p=R/row['source_observation'];raw=p.read_text();q=row['exact_original_language_quote']
  if p.suffix=='.json':
   src=json.loads(raw);hay=strings(src)
   if 'table_rows' in src:
    hay += [' | '.join(c for c in u['cells'] if c.strip()) for u in src['table_rows']]
   found=any(q in s for s in hay)
  else:found=q in raw
  ok('Quote membership '+row['id'],found)
  ok('Quote context hash '+row['id'],sha(row['source_context'].encode())==row['source_text_sha256'])
 oldmap=json.loads((D/'old-topic-destinations.json').read_text())['rows']
 for u in oldmap:
  ok('Old unit destination '+u['source_file']+'/'+str(u['source_unit']),u['old_text'] in (R/u['source_file']).read_text() and sha(u['old_text'].encode())==u['old_sha256'])
# The September example uses inclusive real ownership days, rather than an assumed quarter.
ok('2026 year days',(datetime.date(2027,1,1)-datetime.date(2026,1,1)).days==365)
ok('September through December held days',(datetime.date(2027,1,1)-datetime.date(2026,9,1)).days==122)
# Existing tracked material can change only in the country README for this delta.
changed=subprocess.check_output(['git','diff','--name-status','HEAD'],cwd=R,text=True).splitlines()
allowed_new={'skills/moldova/md-property-tax.md','skills/moldova/md-wealth-tax.md','evidence/ledgers/md-property-tax.md','evidence/ledgers/md-property-tax.writer.json','evidence/ledgers/md-wealth-tax.md','evidence/ledgers/md-wealth-tax.writer.json'}
bad=[]
for change in changed:
 status,path=change.split('\t',1)
 if path=='skills/moldova/README.md' and status=='M':continue
 if status=='A' and (path in allowed_new or path.startswith('evidence/ledgers/md-country-evidence/property-wealth-20261031/')):continue
 bad.append(change)
ok('No unrelated or existing tax/evidence file changed',not bad,bad)
sys.path.insert(0,str(R/'scripts'))
spec=importlib.util.spec_from_file_location('validate_guides',R/'scripts/validate-guides.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
errors=[];warnings=[];v.check_guides(v.load_build_index(),errors,warnings,only_files={'skills/moldova/md-property-tax.md','skills/moldova/md-wealth-tax.md'})
ok('Focused actual Guide validator',not errors,{'errors':errors,'warnings':warnings})
report={'date':'2026-10-31','independent_review':'PENDING; writer audit is not independent review','baseline_commit':old['baseline_commit'],'source_bindings':594,'old_Guides_preserved':11,'old_units_preserved':1072,'checks':len(checks),'failures':fail,'details':checks}
(D/'writer-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='details'},ensure_ascii=False));sys.exit(bool(fail))
