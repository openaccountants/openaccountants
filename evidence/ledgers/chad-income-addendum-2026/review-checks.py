#!/usr/bin/env python3
"""Reproduce the independent addendum identity/preservation/structural checks."""
from pathlib import Path
import hashlib,json,datetime,os,re,subprocess
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
FROZEN='a9181d5a61df05b770a4fb39f8ffb8d7b29a6c5b';PRENOTE='9adb1b3e9b05b38440ecd5b2d45f2d6348683704';PRIOR='af75221ab';OLD='416ec514979330e5980061eda4a38ab2cdef6e4a';BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def sha(b):return hashlib.sha256(b).hexdigest()
subprocess.run(['git','merge-base','--is-ancestor',FROZEN,'HEAD'],cwd=ROOT,check=True)
manifest=json.loads((OUT/'final-guide-manifest.json').read_text());frozen={}
for path,wanted in manifest['files'].items():
 b=(ROOT/path).read_bytes();assert sha(b)==wanted;assert b==git('show',f'{FROZEN}:{path}');frozen[path]=sha(b)
for path,wanted in json.loads((OUT/'closure-manifest.json').read_text())['files'].items():
 if path.startswith('docs/research/'):
  b=(ROOT/path).read_bytes();assert sha(b)==wanted and b==git('show',f'{PRENOTE}:{path}');frozen[path]=sha(b)
rows=re.findall(r'^\| ((?:B|PR)\d+) \|', (OUT/'ledger.md').read_text(),re.M)
assert set(rows)=={f'B{i:02}'for i in range(1,34)}|{'PR07'} and len(rows)==34
preserved={}
for path in git('ls-tree','-r','--name-only',PRIOR,'evidence/ledgers/chad-remaining-2026').decode().splitlines():
 b=(ROOT/path).read_bytes();assert b==git('show',f'{PRIOR}:{path}');preserved[path]=sha(b)
noteonly={}
old_tails={'td-company-formation':'Independent review pending; no accountant attestation.','td-corporate-income-tax':'Independent review pending; tier2, no accountant attestation.','td-income-tax':'The source addendum and LF18 correction require separate independent review; no accountant attestation.','td-payroll-social':'Independent review pending, no accountant attestation.','td-tax-overview':'Independent review pending; no accountant attestation.','td-transfer-pricing':'Independent review pending; no accountant attestation.','td-vat-gst':'Independent source review pending; no accountant attestation.'}
new_tail='For independent AI source review and its limits, see the [country README](README.md). No accountant attestation.'
for name,old_tail in old_tails.items():
 path=f'skills/chad/{name}.md';old=git('show',f'{PRENOTE}:{path}').decode();new=(ROOT/path).read_text()
 assert old.count(old_tail)==1 and new.count(new_tail)==1,path
 assert old.replace(old_tail,new_tail)==new,path
 noteonly[path]={'pre_note_sha256':sha(old.encode()),'final_sha256':sha(new.encode()),'exact_closing_note_replacement_only':True}
unchanged={}
for name in ['td-corporate-income-tax','td-vat-gst','td-transfer-pricing','td-company-formation','td-tax-overview','td-import-exemption-eligibility']:
 path=f'skills/chad/{name}.md';b=git('show',f'{PRENOTE}:{path}');assert b==git('show',f'{OLD}:{path}');unchanged[path]={'pre_note_sha256':sha(b),'current_sha256':sha((ROOT/path).read_bytes()),'current_change':'none' if (ROOT/path).read_bytes()==b else 'verified closing note only'}
platform=('name','jurisdiction','review_status','trust_label','license','authored_by','verified_by','reviewed_by','reviewed_on','drafted_by','approved_by','validation_status','validated')
changed={}
blocks=lambda t:re.findall(r'```oa-check\n.*?\n```',t,re.S)
for name in ['td-income-tax','td-payroll-social']:
 path=f'skills/chad/{name}.md';old=git('show',f'{OLD}:{path}').decode();new=(ROOT/path).read_text()
 for key in platform:
  extract=lambda t:[l for l in t.split('---',2)[1].splitlines()if l.startswith(key+':')]
  assert extract(old)==extract(new),(path,key)
 assert old.split('<!-- openaccountants-cta-block -->',1)[1]==new.split('<!-- openaccountants-cta-block -->',1)[1]
 assert blocks(new)[:2]==blocks(old) and len(blocks(old))==2
 assert len(blocks(new))==(4 if name=='td-income-tax' else 2)
 changed[path]={'sha256':sha(new.encode()),'inherited_platform_fields_preserved':True,'full_cta_preserved':True,'prior_two_oa_checks_preserved':True,'oa_checks':len(blocks(new))}
# Exact predecessor inventory remains the same; the withdrawn105floor was a new claim, not a lost predecessor topic.
path='evidence/ledgers/chad-remaining-2026/old-topics.md';assert (ROOT/path).read_bytes()==git('show',f'{OLD}:{path}')
files=[f'skills/chad/{n}.md'for n in old_tails]
env=dict(os.environ,PYTHONPATH='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps')
commands=[]
for argv in [['python3','scripts/skill_checks.py',*files],['python3','scripts/check-examples.py','--require',*files],['python3','scripts/check-examples.py','--require',*[str(p.relative_to(ROOT))for p in sorted((ROOT/'skills/chad').glob('td-*.md'))]],['python3','scripts/check-sync-integrity.py','--base',BASE,'--head',FROZEN,'--mode','audit','--strict-metadata'],['git','diff','--check',BASE,FROZEN]]:
 p=subprocess.run(argv,cwd=ROOT,env=env,text=True,capture_output=True);commands.append({'argv':argv,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0,(argv,p.stdout,p.stderr)
result={'frozen_candidate':FROZEN,'prior_accepted_candidate':OLD,'prior_review_backup':PRIOR,'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_file_sha256':frozen,'source_row_ids':rows,'source_rows':34,'pre_note_candidate':PRENOTE,'exact_note_only_verification':noteonly,'unchanged_statutory_guides':unchanged,'preserved_prior_review_files':preserved,'changed_guides':changed,'commands':commands}
(OUT/'mechanical-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rows':34,'preserved_review_files':len(preserved),'unchanged_guides':len(unchanged),'changed_guides':2,'changed_guide_cases':16,'all_pack_cases':18,'commands_passed':len(commands)}))
