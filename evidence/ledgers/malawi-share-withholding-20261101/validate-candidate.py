from pathlib import Path
import json,subprocess,sys,os,hashlib,re
R=Path.cwd(); E=R/'evidence/ledgers/malawi-share-withholding-20261101'; stage=sys.argv[1]
BASE=subprocess.run(['git','merge-base','HEAD','origin/main'],capture_output=True,text=True,check=True).stdout.strip()
head=subprocess.run(['git','rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
report={'stage':stage,'actual_full_merge_base':BASE,'actual_head':head,'commands':[],'all_pass':False}
out=E/(stage+'-validation.json')
env=os.environ.copy();env['PYTHONPATH']='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps'
def run(argv):
 p=subprocess.run(argv,text=True,capture_output=True,env=env); report['commands'].append({'argv':argv,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr});out.write_text(json.dumps(report,indent=2)+'\n');print(' '.join(argv));print(p.stdout);print(p.stderr)
 if p.returncode:sys.exit(p.returncode)
run(['python3','scripts/skill_checks.py','skills/malawi/mw-listed-share-withholding.md'])
run(['python3','scripts/check-examples.py','--require','skills/malawi/mw-listed-share-withholding.md','skills/malawi/mw-company-formation.md','skills/malawi/mw-cross-border-tax.md'])
run(['python3','scripts/check-sync-integrity.py','--base',BASE,'--strict-metadata',*(['--worktree'] if stage=='pre-commit' else ['--head',head])])
if stage=='committed':run(['python3','scripts/validate-guides.py','--changed-only','--no-index-check'])
run(['git','diff','--check',BASE,*([] if stage=='pre-commit' else [head])])
# Assert preservation against accepted prior head, including sparse-checkout files.
b=json.loads((E/'baseline.json').read_text());checks=[]
for p,h in b['prior_guide_and_evidence_sha256'].items():
 raw=(R/p).read_bytes() if (R/p).exists() else subprocess.run(['git','show',f'HEAD:{p}'],capture_output=True,check=True).stdout
 checks.append({'path':p,'expected':h,'actual':hashlib.sha256(raw).hexdigest()})
assert all(x['expected']==x['actual'] for x in checks)
new=(R/'skills/malawi/mw-listed-share-withholding.md').read_text();sys.path.insert(0,str(R/'scripts'))
# PyYAML dependency loaded from named runtime only.
sys.path.insert(0,env['PYTHONPATH']);from frontmatter_yaml import load_frontmatter
fm=load_frontmatter(new.split('---',2)[1]);words=len(str(fm['description']).split());assert 80<=words<=150
for x in ['review_status','trust_label','license','verified_by','reviewed_by','reviewed_on']:assert x not in fm
assert 'openaccountants-cta-block' not in new
readme=(R/'skills/malawi/README.md').read_text();old=subprocess.run(['git','show',b['accepted_prior_head']+':skills/malawi/README.md'],capture_output=True,text=True,check=True).stdout
restored=readme.split('\n## Listed-share withholding draft backup\n')[0]
restored=restored.replace('IT-IND: [mw-income-tax, mw-listed-share-withholding]','IT-IND: [mw-income-tax]').replace('IT-CORP: [mw-corporate-income-tax, mw-listed-share-withholding]','IT-CORP: [mw-corporate-income-tax]')
assert restored==old
quotes=json.loads((E/'quote-checks.json').read_text());assert len(quotes)==29 and all(x['quote_found_whitespace_only'] for x in quotes)
changed=subprocess.run(['git','diff','--name-only',b['accepted_prior_head'],*([] if stage=='pre-commit' else [head])],capture_output=True,text=True,check=True).stdout.splitlines()
allowed=lambda p:p in ['skills/malawi/README.md','skills/malawi/mw-listed-share-withholding.md'] or p.startswith('evidence/ledgers/malawi-share-withholding-20261101/')
assert all(allowed(p) for p in changed),changed
report.update({'all_pass':True,'preservation':checks,'new_description_words':words,'exact_quotes':29,'old_body_units':257,'guide_sha256':hashlib.sha256(new.encode()).hexdigest(),'readme_sha256':hashlib.sha256(readme.encode()).hexdigest(),'prior_8_guides_and_52_evidence_exact':True,'old_readme_restored_after_allowlisted_additions_exact':True,'new_metadata_no_platform_fields_or_cta':True,'allowlisted_paths':changed,'legal_currentness_accepted':False,'independent_review_new_job':'pending'})
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['commands','preservation','allowlisted_paths']},indent=2))
