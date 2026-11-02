from pathlib import Path
import hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent;INITIAL='a61fda399fa613455862d3cc72d5c403cd330ccc';HEAD='3a14e7b7bbb9ac80425e046325b0b946e66fb927';BASE='a7888d0d6c1f7cb0fed13d8d3f6b7e05f1d12297'
sys.path.insert(0,str(ROOT/'scripts'))
from frontmatter_yaml import load_frontmatter
sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.run(['git',*args],cwd=ROOT,capture_output=True,check=True).stdout
def fm(t):return load_frontmatter(t.split('---',2)[1])
paths=sorted((ROOT/'skills/benin').glob('bj-*.md'));r={'initial_candidate':INITIAL,'repaired_head':HEAD,'actual_head':git('rev-parse','HEAD').decode().strip(),'pinned_base':BASE,'guides':{}}
for p in paths:
 rel=str(p.relative_to(ROOT));b=p.read_bytes();text=b.decode();old=git('show',f'{INITIAL}:{rel}').decode();a,z=fm(old),fm(text);changes={k:[str(a.get(k)),str(z.get(k))] for k in a.keys()|z.keys() if a.get(k)!=z.get(k)}
 blocks=lambda t:re.findall(r'```oa-check\n.*?\n```',t,re.S)
 marker='<!-- openaccountants-cta-block -->';cta=lambda t:t.split(marker,1)[1] if marker in t else None
 heading=re.search(r'^# .+$',text,re.M).group()
 r['guides'][p.name]={'sha256':sha(b),'description_words':len(z['description'].split()),'description_pass':80<=len(z['description'].split())<=150,'version':'0.2' if str(z['version'])=='0.2' else str(z['version']),'heading':heading,'title_version_pass':heading.endswith(' v0.2'),'changed_frontmatter_keys':sorted(changes),'only_description_version_metadata_changed':set(changes)=={'description','version'},'all_other_frontmatter_preserved':{k:a.get(k)==z.get(k) for k in a.keys()|z.keys() if k not in {'description','version'}},'examples_byte_identical':blocks(old)==blocks(text),'example_count':len(blocks(text)),'cta_tail_exact':cta(old)==cta(text)}
# Original writer evidence must be identical to the initial frozen commit.
r['initial_writer_evidence']={p.name:{'sha256':sha(p.read_bytes()),'identical_to_initial':p.read_bytes()==git('show',f'{INITIAL}:{p.relative_to(ROOT)}')} for p in (ROOT/'evidence/ledgers/benin-draft-20261101').iterdir() if p.is_file()}
# The initial reviewer records stay in place; their committed byte hashes are frozen here.
r['initial_review_evidence']={p.name:{'sha256':sha(p.read_bytes()),'identical_to_committed_record':p.read_bytes()==git('show',f'{HEAD}:{p.relative_to(ROOT)}')} for p in (ROOT/'evidence/ledgers/benin-review-20261101').iterdir() if p.is_file()}
r['repair_receipt_hashes']={p.name:sha(p.read_bytes()) for p in (ROOT/'evidence/ledgers/benin-repair-1').iterdir() if p.is_file()}
# Reconcile all ledger rows: exactly the two reported legal rows may differ.
r['changed_ledger_rows']=[];r['ledger_count']=0
for p in sorted((ROOT/'evidence/ledgers').glob('bj-*.md')):
 old=git('show',f'{INITIAL}:{p.relative_to(ROOT)}').decode();oldrows=[x for x in old.splitlines() if re.match(r'^\| \d+ \|',x)];newrows=[x for x in p.read_text().splitlines() if re.match(r'^\| \d+ \|',x)];assert len(oldrows)==len(newrows);r['ledger_count']+=len(newrows)
 for a,z in zip(oldrows,newrows):
  if a!=z:r['changed_ledger_rows'].append({'file':p.name,'row':int(z.split('|')[1]),'old':a,'new':z})
oldmap=git('show',f'{INITIAL}:evidence/ledgers/benin-old-topics.md').decode();newmap=(ROOT/'evidence/ledgers/benin-old-topics.md').read_text();mrows=lambda t:[x.split('|') for x in t.splitlines() if x.startswith('| bj-')];ar,zr=mrows(oldmap),mrows(newmap);assert len(ar)==len(zr)==81
r['topic_map']={'rows':81,'original_topic_cells_unchanged':all(a[1]==z[1] for a,z in zip(ar,zr)),'reason_cells_unchanged':all(a[3]==z[3] for a,z in zip(ar,zr)),'changes':[]}
for a,z in zip(ar,zr):
 if a[2]!=z[2]:
  target=z[2].strip();fn,anchor=target.split('#');s=(ROOT/'skills/benin'/fn).read_text();anchors={re.sub(r'[^a-z0-9 -]','',x.lower()).replace(' ','-') for x in re.findall(r'^## (.*)$',s,re.M)}
  r['topic_map']['changes'].append({'topic':z[1].strip(),'new_target':target,'target_exists':anchor in anchors})
# Same-day source freshness was independently established in the initial review.
# Re-hash actual PDFs instead of repeating all ten unchanged network requests.
prior=json.loads((ROOT/'evidence/ledgers/benin-review-20261101/source-verification-network.json').read_text());r['official_pdf_integrity']=[]
for source in prior['sources']:
 if source['file'] in {'cgi2026.pdf','lfr2026.pdf'}:
  b=(ROOT.parent/'sources'/source['file']).read_bytes();r['official_pdf_integrity'].append({'file':source['file'],'url':source['url'],'sha256':sha(b),'matches_independent_same_day_official_fetch':sha(b)==source['fresh_sha256'],'original_fetch_utc':prior['utc']})
r['readme_byte_identical_to_initial']=(ROOT/'skills/benin/README.md').read_bytes()==git('show',f'{INITIAL}:skills/benin/README.md')
r['commands']=[]
commands=[['python3','scripts/skill_checks.py',*[str(p.relative_to(ROOT)) for p in paths]],['python3','scripts/check-examples.py','--require',*[str(p.relative_to(ROOT)) for p in paths]],['python3','evidence/ledgers/benin-draft-20261101/pinned-validation.py'],['git','diff','--check',BASE],['git','diff','--check','--cached']]
for cmd in commands:
 c=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);r['commands'].append({'argv':cmd,'exit_code':c.returncode,'stdout':c.stdout,'stderr':c.stderr})
r['passed']=r['actual_head']==HEAD and all(x['description_pass'] and x['title_version_pass'] and x['only_description_version_metadata_changed'] and x['examples_byte_identical'] and x['cta_tail_exact'] for x in r['guides'].values()) and all(x['identical_to_initial'] for x in r['initial_writer_evidence'].values()) and all(x['identical_to_committed_record'] for x in r['initial_review_evidence'].values()) and {(x['file'],x['row']) for x in r['changed_ledger_rows']}=={('bj-cross-border-withholding.md',7),('bj-transfer-pricing.md',10)} and len(r['topic_map']['changes'])==6 and r['topic_map']['original_topic_cells_unchanged'] and r['topic_map']['reason_cells_unchanged'] and all(x['target_exists'] for x in r['topic_map']['changes']) and all(x['matches_independent_same_day_official_fetch'] for x in r['official_pdf_integrity']) and r['readme_byte_identical_to_initial'] and all(x['exit_code']==0 for x in r['commands'])
(HERE/'closure-receipt.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':r['passed'],'descriptions':{k:v['description_words'] for k,v in r['guides'].items()},'examples_unchanged':sum(v['example_count'] for v in r['guides'].values()),'changed_ledger_rows':[(x['file'],x['row']) for x in r['changed_ledger_rows']],'map_fixes':len(r['topic_map']['changes']),'commands':[(x['argv'][:2],x['exit_code']) for x in r['commands']]},indent=2))
