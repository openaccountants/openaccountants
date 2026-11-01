#!/usr/bin/env python3
"""Fail closed on the narrow figure move, prior evidence preservation and current source identities."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
E=Path(__file__).resolve().parent;R=E.parents[2]
sys.path.insert(0,str(R/'scripts'))
import skill_checks

def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
def read(path):return (R/path).read_bytes() if (R/path).exists() else git('show','HEAD:'+path)
baseline=json.loads((E/'preservation-baseline.json').read_text());base=baseline['base_commit']
transform=json.loads((E/'permitted-old-guide-transform.json').read_text());oldpath=transform['path']
original=git('show',base+':'+oldpath)
assert (E/'predecessor-bi-income-tax.md.txt').read_bytes()==original
expected=original.decode()
for row in transform['exact_replacements']:
 assert expected.count(row['before'])==1,row
 expected=expected.replace(row['before'],row['after'])
assert read(oldpath)==expected.encode()
assert sha(read(oldpath))==transform['result_sha256']
kept=[]
for row in baseline['files']:
 path=row['path'];b=git('show',base+':'+path)
 assert sha(b)==row['sha256']
 assert git('rev-parse',base+':'+path).decode().strip()==row['blob']
 if row['treatment']=='byte-identical':
  assert read(path)==b,path
  kept.append(path)
newpath='skills/burundi/bi-capital-income-tax.md';text=read(newpath).decode();fm=skill_checks.read_frontmatter(text)
assert 80<=len(fm['description'].split())<=150
assert fm['tier']=='2' or fm['tier']==2
assert not any(x in fm for x in ['review_status','trust_label','license','reviewed_by','reviewed_on','authored_by'])
assert 'openaccountants-cta-block' not in text
checks={}
for path in [newpath,oldpath]:
 checks[path]=skill_checks.run_all(path)
 assert len(checks[path])==15
 assert not any(checks[path].values()),checks[path]
ledger=json.loads((E/'bi-capital-income-tax.json').read_text())
assert len(ledger)==47
for row in ledger:
 for key in ['section','claim','act','article','pdf_locator','official_url','exact_quote','read_date','source_sha256','source_read_scope']:
  assert row.get(key),f'{row["id"]} missing {key}'
 assert row['read_date']=='2026-11-01'
source_count=0
for row in json.loads((E/'source-artifacts.json').read_text()):
 path=R.parent/'sources'/row['path'];assert path.exists(),str(path)
 assert sha(path.read_bytes())==row['sha256'],row['path']
 source_count+=1
oldmap=json.loads((E/'old-topic-destinations.json').read_text())['all_current_old_guide_body_units']
assert len(oldmap)==294
for row in oldmap:
 assert sha(row['old_text'].encode())==row['sha256']
 assert row['old_text'] in git('show',base+':'+row['path']).decode()
md=read('skills/burundi/README.md').decode();oldmd=git('show',base+':skills/burundi/README.md').decode()
oldpartial=oldmd.split('partial:\n',1)[1].split('\n---',1)[0]
assert md.split('partial:\n',1)[1].split('\n---',1)[0]==oldpartial
# Country map edits are the exact two approved routing replacements and one appended scope block.
expected_md=oldmd.replace('  IT-IND: bi-income-tax\n','  IT-IND: [bi-income-tax, bi-capital-income-tax]\n').replace('| IT-IND | bi-income-tax | sourced from the law; partial |','| IT-IND | bi-income-tax; bi-capital-income-tax | original business/rental scope accepted; new capital scope independent review pending; partial |')
assert md.startswith(expected_md+'\n## Individual capital computation addition\n')
assert len(re.findall(r'^## ',md[len(expected_md):],re.M))==1
print(json.dumps({'result':'pass','predecessor':base,'old_files_preserved':len(kept),'old_guide_bodies_byte_identical':sum(p.startswith('skills/burundi/') for p in kept),'prior_evidence_byte_identical':sum(p.startswith('evidence/') for p in kept),'old_guide_exact_replacements':len(transform['exact_replacements']),'old_substantive_body_rows_replaced':1,'all_old_body_units_mapped':len(oldmap),'seven_partial_domains_preserved':True,'source_artifacts_hashed':source_count,'ledger_rows':len(ledger),'shape_checks':checks,'new_guide_sha256':sha(text.encode()),'new_description_words':len(fm['description'].split())},ensure_ascii=False,indent=2))
