from pathlib import Path
import hashlib,json,subprocess,re,tarfile
from decimal import Decimal
R=Path.cwd();D=R/'evidence/ledgers/svalbard-beneficial-owners-20261031';O=D/'independent-review';P=R.parent/'independent-beneficial-owners-private';W=R.parent/'reuse-check';S=R.parent/'sources'
sha=lambda b:hashlib.sha256(b).hexdigest()
checks=[]
def ck(n,v):
 checks.append({'check':n,'pass':bool(v)})
 if not v:raise AssertionError(n)
manifest=D/'writer-manifest.json';ck('manifest pinned',sha(manifest.read_bytes())=='1a5b235a0e17185e7fad57afc65cecc261a877c6fce9ce544a372d8a698b8cdc');inputs=json.loads(manifest.read_text())['inputs']
for x in inputs:ck('input '+x['path'],sha((R/x['path']).read_bytes())==x['sha256'])
rowsdoc=json.loads((D/'rows.json').read_text());rows=rowsdoc['rows'];g=R/rowsdoc['guide'];gt=g.read_text();ck('41 rows',len(rows)==41);ck('Guide hash',sha(g.read_bytes())==rowsdoc['guide_sha256'])
for row in rows:
 source=R/row['source_path'] if 'source_path'in row else S/row['private_capture_name'];reader=source.with_suffix('.txt');ck('raw source '+row['id'],sha(source.read_bytes())==row['raw_sha256']);ck('reader '+row['id'],sha(reader.read_bytes())==row['reader_sha256']);quote='\n'.join(reader.read_text().splitlines()[row['reader_start_line']-1:row['reader_end_line']]);ck('complete reader quote '+row['id'],quote==row['exact_original_language_quote'])
# Check raw XML membership in the retained official API packages, without extracting whole packages.
archive_receipts=json.loads((D/'api-dataset-receipts.json').read_text());members={}
for item in archive_receipts:
 archive=W/item['filename'];ck('archive hash '+item['filename'],sha(archive.read_bytes())==item['sha256']);needed={r['api_member']:r['source_path'] for r in rows if r.get('api_archive')==item['filename']}
 with tarfile.open(archive,'r:bz2') as tar:
  for member,path in needed.items():
   raw=tar.extractfile(member).read();ck('exact API member '+member,raw==(R/path).read_bytes());members[member]=sha(raw)
 listed={x['filename']:x for x in json.loads((P/'api-list.raw').read_text())};ck('fresh dataset metadata '+item['filename'],listed[item['filename']]==item['listed_metadata'])
for item in json.loads((D/'procedure-source-receipts.json').read_text()):
 ck('private procedure raw '+item['name'],sha((S/(item['name']+'.html')).read_bytes())==item['raw_sha256']);ck('private procedure reader '+item['name'],sha((S/(item['name']+'.txt')).read_bytes())==item['reader_sha256'])
fresh=json.loads((P/'fresh-quote-comparison.json').read_text());ck('38 direct fresh quote matches',sum(bool(x.get('fresh_quote_matches_whitespace_and_presentation_normalized')) for x in fresh)==38)
# Altinn has a direct HTTP403 receipt; web.open succeeded and its full public procedure was read separately.
api=json.loads((P/'api-spec.raw').read_text());ck('public API NLOD declaration',api['tags'][0]['name']=='Public data' and 'NLOD 2.0' in api['tags'][0]['description']);ck('public download no auth',api['paths']['/v1/publicData/get/{filename}']['get']['description'].endswith('No authentication required.'))
preserve=json.loads((D/'preservation.json').read_text());base=preserve['baseline'];ck('nine predecessors',len(preserve['old_guides'])==9)
for x in preserve['old_guides']:
 old=subprocess.check_output(['git','show',base+':'+x['path']]);ck('predecessor exact '+x['path'],old==(R/x['path']).read_bytes() and sha(old)==x['sha256'])
readme=(R/'skills/svalbard/README.md').read_text();oldreadme=subprocess.check_output(['git','show',base+':skills/svalbard/README.md'],text=True);ck('README baseline snapshot',oldreadme==(D/'predecessor-README.md').read_text())
for x in preserve['old_readme_units']:
 ck('README original unit '+str(x['old_line']),oldreadme.splitlines()[x['old_line']-1]==x['text'])
 if x['status']=='exact retained':ck('README destination '+str(x['old_line']),x['text'] in readme)
 else:
  expected=x['text'].replace('The nine Guides','The ten Guides').replace('The three explicit domain gaps above','The ordinary-company beneficial-owner Guide has a figure ledger and awaits independent review. The three explicit domain gaps above');ck('README enumerated count/status update',expected in readme)
# Immutable existing Svalbard sources, ledgers, initial reviews and research.
tracked=subprocess.check_output(['git','ls-tree','-r','--name-only',base,'--','evidence','docs/research'],text=True).splitlines();prior=[p for p in tracked if 'svalbard' in p.lower()];changed=set(subprocess.check_output(['git','diff','--name-only',base,'--','evidence','docs/research'],text=True).splitlines())
for p in prior:ck('prior evidence unchanged '+p,p not in changed)
linemap=json.loads((D/'line-map.json').read_text());ck('line-map Guide hash',linemap['guide_sha256']==sha(g.read_bytes()))
for x in linemap['lines']:ck('Guide line '+str(x['line']),sha(gt.splitlines()[x['line']-1].encode())==x['sha256'])
fm=gt.split('---',2)[1];desc=re.search(r'description: >\n(.*?)\njurisdiction:',fm,re.S).group(1);words=len(desc.split());ck('description 80-150 words',80<=words<=150);ck('H1/frontmatter version parity','version: 0.1' in fm and re.search(r'^# .* v0.1$',gt,re.M));ck('no new platform-owned keys',not re.search(r'^(trust_label|authored_by|review_status|license|reviewed_by|reviewed_on|verified_by|drafted_by|approved_by|validation_status|validated):',fm,re.M));ck('full notice','This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person\'s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.' in gt);ck('five intake questions',len(re.findall(r'^- ',gt.split('## Ask the client first')[1].split('## Sources')[0],re.M))==5)
calc={'direct_boundary_percent':2500/10000*100,'direct_qualifying_percent':2600/10000*100,'shares_exceeding_threshold':2600-10000*.25,'indirect_downstream_excess':30-25,'indirect_upstream_excess':50-50,'economic_product_percent':30*50/100,'first_daily_NOK':str(Decimal('1345')*Decimal('.5')),'second_daily_NOK':'1345','third_daily_NOK':str(Decimal('1345')*Decimal('1.5')),'first_56_days_NOK':str(56*Decimal('672.5')),'next_70_days_NOK':str(70*Decimal('1345')),'18_week_cumulative_NOK':str(56*Decimal('672.5')+70*Decimal('1345'))}
result={'candidate':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'manifest_sha256':sha(manifest.read_bytes()),'input_count':len(inputs),'rows':41,'unique_quote_groups':31,'checks':len(checks),'failures':0,'predecessor_Guides_exact':9,'prior_Svalbard_evidence_files_unchanged':len(prior),'description_words':words,'API_members':members,'arithmetic':calc,'details':checks}
(O/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='details'},ensure_ascii=False))
