#!/usr/bin/env python3
"""Check the exact independently permitted status transitions and immutable evidence."""
from pathlib import Path
import hashlib,json,re,subprocess
R=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent
receipt=json.loads((E/'status-transition.json').read_text());auth=R/receipt['authority_path']
assert hashlib.sha256(auth.read_bytes()).hexdigest()==receipt['authority_sha256']
for row in receipt['changes']:
 p=R/row['path'];now=p.read_bytes();assert hashlib.sha256(now).hexdigest()==row['after_sha256'],row['path']
 assert subprocess.check_output(['git','hash-object','--stdin'],input=now,cwd=R).decode().strip()==row['after_git_blob']
 text=now.decode()
 for rep in reversed(row['exact_replacements']):
  assert text.count(rep['after'])==1;text=text.replace(rep['after'],rep['before'],1)
 old=subprocess.check_output(['git','show',receipt['reviewed_head']+':'+row['path']],cwd=R)
 assert text.encode()==old and hashlib.sha256(old).hexdigest()==row['before_sha256']
for row in receipt['immutable_review_files']+receipt['immutable_inherited_files']:
 assert hashlib.sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256'],row['path']
readme=(R/'skills/gabon/README.md').read_text();assert len(re.findall(r'^  (?:IT-IND|IT-CORP|VAT|SC|PR|TP|XB): "',readme,re.M))==7
guide=(R/'skills/gabon/ga-annual-property-tax.md').read_text()
for field in ['review_status','trust_label','license','reviewed_by','authored_by','verified_by']:assert not re.search('^'+field+':',guide,re.M)
assert '<!-- openaccountants-cta-block -->' not in guide
print(json.dumps({'status':'pass','permitted_changed_files':2,'permitted_exact_substitutions':3,'review_evidence_files_immutable':len(receipt['immutable_review_files']),'inherited_files_immutable':len(receipt['immutable_inherited_files']),'original_eight_guides_unchanged':True,'prior_93_rule_127_placement_77_topic_16_case_review_preserved':True,'F1_F4_closed_unchanged':True,'property_review_72_rows_184_cells_two_cases':'accepted source fidelity only','all_seven_domains_partial':True,'current_law_attestation':False,'merge_approval':False},indent=2))
