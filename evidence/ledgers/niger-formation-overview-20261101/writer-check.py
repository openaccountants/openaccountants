from pathlib import Path
import sys,json,hashlib,subprocess,re,os
R=Path(__file__).resolve().parents[3];E=R/'evidence/ledgers/niger-formation-overview-20261101';B='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8';sys.path.insert(0,str(R/'scripts'));import skill_checks
sluglist=['ne-company-formation','ne-tax-overview'];checks={};preservation=[]
for slug in sluglist:
 p=R/'skills/niger'/f'{slug}.md';new=p.read_text();orig=subprocess.check_output(['git','show',B+':skills/niger/'+p.name],cwd=R).decode();fm=skill_checks.read_frontmatter(new);oldfm=skill_checks.read_frontmatter(orig);c=skill_checks.run_checks(str(p),new,fm);assert all(not v for v in c.values()),c
 n=len(str(fm['description']).split());assert 80<=n<=150,n;assert new[new.index('<!-- openaccountants-cta-block -->'):]==orig[orig.index('<!-- openaccountants-cta-block -->'):]
 for key in ['review_status','trust_label','license','authored_by','drafted_by','approved_by','validation_status','validated']:
  assert fm.get(key)==oldfm.get(key),(slug,key)
 checks[slug]={'all_15_checks':c,'description_words':n,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'platform_keys_and_full_cta_exact':True}
base=json.loads((E/'preservation-baseline.json').read_text())
for x in base['preserved']:
 p=R/x['path'];raw=p.read_bytes() if p.exists() else subprocess.check_output(['git','show','HEAD:'+x['path']],cwd=R);assert hashlib.sha256(raw).hexdigest()==x['sha256'],x['path'];preservation.append({'path':x['path'],'sha256':x['sha256'],'unchanged':True})
# Compare actual pre-CTA baseline units and immutable map one-to-one.
m=json.loads((E/'old-topic-destinations.json').read_text());counts={}
for slug in sluglist:
 orig=subprocess.check_output(['git','show',B+':skills/niger/'+slug+'.md'],cwd=R).decode();body=orig.split('---',2)[2].split('<!-- openaccountants-cta-block -->')[0];u=[]
 for x in [x.strip() for x in re.split(r'\n\s*\n',body) if x.strip()]:u.extend(x.splitlines() if x.startswith('- ') else [x])
 mapped=[x['old_text'] for x in m if x['guide']==slug];assert u==mapped;counts[slug]=len(u)
changed=subprocess.check_output(['git','diff','--name-only',B],cwd=R).decode().splitlines();assert all(p in {'skills/niger/ne-company-formation.md','skills/niger/ne-tax-overview.md','skills/niger/README.md'} or p.startswith('evidence/ledgers/niger-formation-overview-20261101/') for p in changed),changed
out={'pinned_base':B,'guide_checks':checks,'preserved_files':preservation,'old_topics':counts,'source_ledger_records':{slug:len(json.loads((E/(slug+'.json')).read_text())) for slug in sluglist},'independent_review':'Pending; writer checks do not establish source acceptance.','no_accountant_attestation':True}
(E/'writer-checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'guide_hashes':{k:v['sha256'] for k,v in checks.items()},'checks_per_guide':15,'preserved':len(preservation),'old_topics':counts,'rows':out['source_ledger_records']},indent=2))
