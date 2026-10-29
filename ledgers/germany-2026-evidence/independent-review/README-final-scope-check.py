from pathlib import Path
import json,hashlib,re,sys
sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
import yaml
R=Path(__file__).parent;D=R.parent/'germany-README-ordinary-coverage-writer-successor-2026-10-29';H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();a=(D/'before/README.md').read_text();b=(D/'after/README.md').read_text();assert H(D/'before/README.md')=='9a5d36d017a780727a82a1235c3f351a4e5a8ca5b2135e4be9cb04a5dc6ebcc4';assert H(D/'after/README.md')=='239811b9f927464f96e8adc06efd9d01c6602bff44bee848d8b13a5b4d4379cb';m=json.loads((D/'artifact-manifest.json').read_text());m=m.get('artifacts',m)if isinstance(m,dict)else m
for z in m:assert H(D/z['path'])==z['sha256']
s=a;ops=json.loads((D/'exact-operations.json').read_text())
for op in ops:assert s.count(op['before'])==1;s=s.replace(op['before'],op['after'],1)
assert s==b
for op in reversed(ops):assert s.count(op['after'])==1;s=s.replace(op['after'],op['before'],1)
assert s==a
ma=yaml.safe_load(a.split('---',2)[1]);mb=yaml.safe_load(b.split('---',2)[1]);assert sorted(mb['partial'])==sorted(['IT-IND','VAT','SC','PR','TP','XB']);assert{k:v for k,v in ma.items()if k!='partial'}=={k:v for k,v in mb.items()if k!='partial'};assert re.findall(r'https?://[^\s)<>|]+',a)==re.findall(r'https?://[^\s)<>|]+',b)
q=json.loads((D/'source-read-scope-bindings.json').read_text());assert H(q['scope_source'])==q['scope_source_sha256'];matrix=json.loads(Path(q['scope_source']).read_text());assert len(q['bindings'])==len(matrix['material_ordinary_boundaries'])==11
for z,original in zip(q['bindings'],matrix['material_ordinary_boundaries']):
 assert z['id']==original['id'];assert z['reviewer_exact_boundary']==original['boundary']
 for g in z['current_Guide_read_scopes']:
  assert H(g['Guide'])==g['Guide_sha256'];ls=Path(g['Guide']).read_text().split('\n');assert[ls[n-1]for n in g['actual_selected_current_Guide_native_LF']]==g['exact_Guide_excerpt']
f=json.loads((R/'country-freeze.json').read_text());companions=[]
for c in f['preserved_companions'][1:]:assert H(c['path'])==c['sha256'];companions.append(c)
current=Path(f['preserved_companions'][0]['path']);assert current.read_text()==b
result={'status':'PASS exact README scope successor for completed independent25-tax/compliance-pair review; country ordinary coverage remains partial in6domains.','README_path':str(current),'README_sha256':H(current),'README_bytes':current.stat().st_size,'manifest_members_rehashed':len(m),'all7operations_actually_read_and_inverted':True,'all6partial_values_and6table_status_cells_actually_read':True,'all11material_boundary_bindings_identity_native_matching':True,'allotherREADMEbytes_routing_URLs_metadata_exact':True,'IT_CORP_ordinary_method_supplied_not_future_form_blocked':True,'four_other_companions_byteexact':companions,'companion_actual_read_scope':'First30LFofeachplusheading/routing diagnostics actually read. No fullbookkeeping/financialstatements/formation/reference law or externalproject attestation claimed. README entire currentbody read.','readiness':'Independent whole25 review complete and all reported repair findings resolved. One honestly scoped source-cited draft country PR is review-ready, subject to root required mechanical checks and any separately verified packaging-only delta. This is not complete ordinary-tax coverage or a credentialed accountant attestation. No Michael research/review requested.'};(R/'README-final-scope-independent-review.json').write_text(json.dumps(result,indent=2)+'\n');print('READMEPASS',len(m),'members/6partials/11bindings/4companions')
