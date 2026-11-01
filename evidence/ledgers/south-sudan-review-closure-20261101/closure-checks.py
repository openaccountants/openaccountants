"""Focused independent F1 closure. Writes only this separate closure evidence folder."""
from pathlib import Path
import json, subprocess, re, hashlib, sys
import yaml
ROOT=Path(__file__).resolve().parents[3]; OUT=Path(__file__).resolve().parent
BEFORE='f494e992b8dc888530c2998ac9aba0e6db29aaab'; AFTER='fedb90f1ba8828c7cd8c891180e12d0bab208b72'; BASE='8935b6fc3a7ff0f773334a45a67448f1efe37b19'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def blob(ref,p):return git('show',ref+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def norm(s):return re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).strip().lower()
def rows(b):return [x for x in b.decode().splitlines() if re.match(r'^\| \d+ \|',x)]
original=json.loads(blob(AFTER,'evidence/ledgers/south-sudan-review-20261101/review-checks.json'))
formation='skills/south-sudan/ss-company-formation.md'; ledger='evidence/ledgers/ss-company-formation.md'
paths=list(original['files']); guides=[p for p in paths if p.startswith('skills/south-sudan/ss-')]
assert git('rev-parse','HEAD').decode().strip()==AFTER
hashes={p:sha(blob(AFTER,p)) for p in paths}
unchanged_guides={p:blob(BEFORE,p)==blob(AFTER,p) for p in guides if p!=formation}; assert all(unchanged_guides.values())
ledger_paths=[p for p in paths if re.fullmatch(r'evidence/ledgers/ss-(company-formation|corporate-income-tax|cross-border|income-tax|payroll-social|tax-overview|transfer-pricing|vat-gst)\.md',p)]
changed_rows=[]; unchanged_rows=0
for p in ledger_paths:
 a=rows(blob(BEFORE,p)); b=rows(blob(AFTER,p)); assert len(a)==len(b)
 for old,new in zip(a,b):
  if old==new:unchanged_rows+=1
  else:changed_rows.append({'path':p,'id':int(new.split('|')[1]),'new_row':new})
assert unchanged_rows==97 and len(changed_rows)==1 and changed_rows[0]['path']==ledger and changed_rows[0]['id']==6
source=ROOT.parent/'sources/companies-2012-archived-20260609.pdf'
source_text=subprocess.check_output(['pdftotext','-f','111','-l','115',str(source),'-']).decode()
quotes=re.findall('« (.*?) »',changed_rows[0]['new_row']); quote_matches=[norm(q) in norm(source_text) for q in quotes]; assert len(quotes)==2 and all(quote_matches)
s=blob(AFTER,formation).decode();fm=yaml.safe_load(s.split('---',2)[1]);assert str(fm['version'])=='0.2' and 'working paper v0.2' in s
platform_keys={'review_status','trust_label','verified_by','reviewed_by','reviewed_on','license'}
preserved=[]
for p in guides:
 now=blob(AFTER,p).decode();before=blob(BEFORE,p).decode()
 assert re.findall(r'^```oa-check[^\n]*\n.*?^```',before,re.M|re.S)==re.findall(r'^```oa-check[^\n]*\n.*?^```',now,re.M|re.S)
 try:old=blob(BASE,p).decode()
 except subprocess.CalledProcessError:
  assert not any(line.split(':',1)[0] in platform_keys for line in now.split('---',2)[1].splitlines());continue
 marker='<!-- openaccountants-cta-block -->'
 assert old[old.index(marker):]==now[now.index(marker):]
 keylines=lambda t:[line for line in t.split('---',2)[1].splitlines() if line.split(':',1)[0] in platform_keys]
 assert keylines(old)==keylines(now)
 preserved.append(p)
map_path='evidence/ledgers/ss-old-topic-destinations.md'; assert blob(BEFORE,map_path)==blob(AFTER,map_path)
old_evidence={p:sha((ROOT/p).read_bytes())==h for p,h in json.loads(blob(AFTER,'evidence/ledgers/south-sudan-review-20261101/review-manifest.json'))['files'].items()};assert all(old_evidence.values())
commands=[]
for argv in [
 ['python3','scripts/skill_checks.py',formation],
 ['python3','scripts/check-examples.py',*guides,'--require'],
 ['python3','scripts/check-sync-integrity.py','--base',BASE,'--worktree','--strict-metadata'],
 ['git','diff','--check',BASE,AFTER],
]:
 p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True);commands.append({'argv':argv,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0
r={'date':'2026-11-01','scope':'F1 focused independent closure, with original unchanged review carried forward','initial_freeze':BEFORE,'repaired_freeze':AFTER,'base':BASE,'f1':'closed; corrected annual-return scope agrees with read Companies Act ss.177–181 PDF111–115','source_pdf_sha256':sha(source.read_bytes()),'changed_quote_texts':quotes,'both_exact_quotes_match':all(quote_matches),'guide_sha256':hashes[formation],'ledger_sha256':hashes[ledger],'formation_description_words':len(fm['description'].split()),'formation_version':'0.2','unchanged_other_guides':unchanged_guides,'unchanged_ledger_rows':unchanged_rows,'changed_row_count':len(changed_rows),'all_16_oa_blocks_byte_identical':True,'old_topic_map_byte_identical':True,'old_topic_rows':85,'six_legacy_cta_and_platform_lines_exact':preserved,'both_added_guides_no_platform_keys':True,'initial_review_evidence_hashes_unchanged':old_evidence,'commands':commands,'disposition':'conditional source-baseline acceptance only; no further findings in focused change','holds':['all seven domains partial','post-June2021 annual amendment chain unreconciled','enacted FY2025/26 and FY2026/27 not established','sales-rate and valuation conflicts unresolved','rental-rate and taxpayer-scope conflict unresolved','current social-insurance law and mechanics unresolved','later company-law and live registry procedures unresolved'],'production_cas':'not run; no authentic content_revision','not_claimed':['operative2026 acceptance','accountant attestation','country completion','live filing or payment','production sync/publication permission']}
(OUT/'closure-checks.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'disposition':r['disposition'],'unchanged_ledger_rows':unchanged_rows,'quotes_match':quote_matches,'commands':commands},indent=2))
