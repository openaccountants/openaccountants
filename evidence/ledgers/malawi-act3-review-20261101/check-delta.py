from pathlib import Path
import hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
BASE='db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6';PRIOR='ee69982119be3271ba7c8ccad2932b96c3cefcb3';FREEZE='6e37fc6093718c07bb554a44194aeb10727cae21';INITIAL='9dcab78579d5e78dbdf7fa615186a8fdab96dcee'
sys.path.insert(0,str(ROOT/'scripts'))
from frontmatter_yaml import load_frontmatter
sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.run(['git',*a],cwd=ROOT,capture_output=True,check=True).stdout
def front(t):return load_frontmatter(t.split('---',2)[1])
paths=sorted((ROOT/'skills/malawi').glob('mw-*.md'));r={'freeze':FREEZE,'actual_head':git('rev-parse','HEAD').decode().strip(),'prior':PRIOR,'pinned_base':BASE,'guides':{}}
blocks=lambda s:re.findall(r'```oa-check\n.*?\n```',s,re.S)
for p in paths:
 rel=str(p.relative_to(ROOT));s=p.read_text();old=git('show',f'{PRIOR}:{rel}').decode();orig=git('show',f'{INITIAL}:{rel}').decode();a,b=front(old),front(s);keys={k for k in a.keys()|b.keys() if a.get(k)!=b.get(k)};marker='<!-- openaccountants-cta-block -->';cta=lambda t:t.split(marker,1)[1] if marker in t else None
 r['guides'][p.name]={'sha256':sha(p.read_bytes()),'description_words':len(b['description'].split()),'description_exact_to_prior':b['description']==a['description'],'changed_frontmatter_keys':sorted(keys),'only_tax_notes_and_version_changed':keys=={'tax_year_notes','version'},'all_other_metadata_equal':all(a.get(k)==b.get(k) for k in a.keys()|b.keys() if k not in keys),'version':str(b['version']),'heading_version_1_3':re.search(r'^# .+$',s,re.M).group().endswith(' v1.3'),'examples_equal_prior':blocks(s)==blocks(old),'examples_equal_initial':blocks(s)==blocks(orig),'example_count':len(blocks(s)),'cta_equal_prior':cta(s)==cta(old),'cta_equal_initial':cta(s)==cta(orig),'hold_present':all(x in s for x in ['**Current-year source hold.**','Do not use this draft','Appointed commencement notices','remain unread','period allocation and the complete operative chain are not approved'])}
r['prior_evidence']={}
for folder in ['malawi-review-20261101','malawi-review-closure-20261101','malawi-repair-1']:
 r['prior_evidence'][folder]={}
 for p in (ROOT/'evidence/ledgers'/folder).iterdir():
  if p.is_file():r['prior_evidence'][folder][p.name]={'sha256':sha(p.read_bytes()),'identical_to_prior':p.read_bytes()==git('show',f'{PRIOR}:{p.relative_to(ROOT)}')}
# Map and prior closure findings carried without rewrite.
p=ROOT/'evidence/ledgers/mw-old-topic-destinations.md';r['topic_map_unchanged']=p.read_bytes()==git('show',f'{PRIOR}:{p.relative_to(ROOT)}')
rd=(ROOT/'skills/malawi/README.md').read_text();r['readme_all_seven_partial']=set(front(rd)['partial'])=={'IT-IND','IT-CORP','VAT','SC','PR','TP','XB'};r['readme_F4_open']='F4 remains OPEN' in rd
r['ledger_counts']={};r['ledger_added_rows']=[];r['ledger_changed_rows']=[]
rows=lambda t:{l.split('|')[1].strip():l for l in t.splitlines() if re.match(r'^\| (?:\d+|Detail-\d+) \|',l)}
for p in sorted((ROOT/'evidence/ledgers').glob('mw-*.md')):
 if 'old-topic' in p.name:continue
 new=rows(p.read_text());old=rows(git('show',f'{PRIOR}:{p.relative_to(ROOT)}').decode());r['ledger_counts'][p.name]={'before':len(old),'after':len(new)}
 for k,v in new.items():
  if k not in old:r['ledger_added_rows'].append({'file':p.name,'row':k,'text':v})
  elif old[k]!=v:r['ledger_changed_rows'].append({'file':p.name,'row':k,'text':v})
 assert set(old)<=set(new)
r['physical_ledger_count']=sum(v['after'] for v in r['ledger_counts'].values());r['prior_physical_ledger_count']=sum(v['before'] for v in r['ledger_counts'].values())
# Match the supporting prior PDFs to the original independently downloaded bytes.
prior_sources=json.loads((ROOT/'evidence/ledgers/malawi-review-20261101/source-downloads.json').read_text())['files']
local_by_url={'73f74c7c-868f-4521-9046-17cc5c13ced2':'tax2024.pdf','f9c5b41b-5dce-4764-b7c2-923c808bda48':'tax-dec2025.pdf','06b35bf5-faa2-4fa1-81f7-af650cce4dff':'tax-principal.pdf','e43a8644-e1e1-46d8-82d7-7e80afd5fd50':'misc2021.pdf'}
r['supporting_pdf_integrity']={}
for key,file in local_by_url.items():
 source=next(x for x in prior_sources if key in x['url']);h=sha((ROOT.parent/'sources'/file).read_bytes());r['supporting_pdf_integrity'][file]={'sha256':h,'matches_original_independent_download':h==source['sha256'],'url':source['url']}
r['commands']=[]
commands=[['python3','scripts/skill_checks.py',*[str(p.relative_to(ROOT)) for p in paths]],['python3','scripts/check-examples.py','--require',*[str(p.relative_to(ROOT)) for p in paths]],['python3','evidence/ledgers/malawi-act3-repair-20261101/pinned-validation.py'],['git','diff','--check',BASE],['git','diff','--check','--cached']]
for cmd in commands:
 c=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);r['commands'].append({'argv':cmd,'exit_code':c.returncode,'stdout':c.stdout,'stderr':c.stderr})
r['mechanical_pass']=r['actual_head']==FREEZE and all(v['description_exact_to_prior'] and 80<=v['description_words']<=150 and v['only_tax_notes_and_version_changed'] and v['all_other_metadata_equal'] and v['version']=='1.3' and v['heading_version_1_3'] and v['examples_equal_prior'] and v['examples_equal_initial'] and v['cta_equal_prior'] and v['cta_equal_initial'] and v['hold_present'] for v in r['guides'].values()) and all(v['identical_to_prior'] for folder in r['prior_evidence'].values() for v in folder.values()) and r['topic_map_unchanged'] and r['readme_all_seven_partial'] and r['readme_F4_open'] and r['physical_ledger_count']==89 and len(r['ledger_added_rows'])==3 and {(v['file'],v['row']) for v in r['ledger_changed_rows']}=={('mw-corporate-income-tax.md','2'),('mw-corporate-income-tax.md','3')} and all(v['matches_original_independent_download'] for v in r['supporting_pdf_integrity'].values()) and all(v['exit_code']==0 for v in r['commands'])
(HERE/'delta-checks.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'mechanical_pass':r['mechanical_pass'],'ledger_before':r['prior_physical_ledger_count'],'ledger_after':r['physical_ledger_count'],'added_rows':[(v['file'],v['row']) for v in r['ledger_added_rows']],'changed_rows':[(v['file'],v['row']) for v in r['ledger_changed_rows']],'examples':sum(v['example_count'] for v in r['guides'].values()),'commands':[(v['argv'][:2],v['exit_code']) for v in r['commands']]},indent=2))
