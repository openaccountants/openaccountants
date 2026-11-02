from pathlib import Path
import json,re,hashlib,subprocess,yaml
w=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-faroe');base=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/faroe-ordinary-completion');o=base/'ledger-review-final';o.mkdir(exist_ok=True);e=w/'ledgers/faroe-islands-2026-evidence';mp=json.loads((e/'PACKAGING-PATH-MAP.json').read_text());h=lambda b:hashlib.sha256(b).hexdigest();checks={};ident={}
assert mp==json.loads((base/'packaging-proof.json').read_text())
for rel,sha in mp['original_files'].items():
 p=e/rel;assert p.is_file() and h(p.read_bytes())==sha,rel
checks['all_original_evidence_files_byte_exact']=len(mp['original_files']);assert not (w/mp['old_prefix']).exists()
expected={}
for n in [1,2,3,4]:
 if n==1:
  rs=json.loads((base/'ledger-review/tranche1-preservation-coverage.json').read_text())
  for x in rs:expected[x['slug']+'.md']=x['sha256']
 elif n==2:
  rs=json.loads((base/'ledger-review/tranche2-preservation.json').read_text())
  for x in rs:expected[x['slug']+'.md']=x['sha256']
 elif n==3:expected['fo-individual-income-tax.md']=json.loads((base/'ledger-review/tranche3-checks.json').read_text())['pin']
 else:
  for x in json.loads((base/'ledger-review/tranche4-row-checks.json').read_text())['protection']:expected[x['slug']+'.md']=x['sha256']
for f,sha in mp['canonical_ledger_copies'].items():
 a=(w/'ledgers'/f).read_bytes();b=(e/'ledgers'/f).read_bytes();assert a==b and h(a)==sha
# Bind canonical ledger bytes to our independently checked row/protection receipts, not just writer map.
reviewed_ledger={}
for x in json.loads((base/'ledger-review/tranche1-row-verdicts.json').read_text()):
 if isinstance(x,dict):pass
x=json.loads((base/'ledger-review/tranche1-row-verdicts.json').read_text());print('tr1 ledger container',type(x).__name__)
# Every exact canonical copy also matches the preserved independently reviewed source ledger path hash in reports/results.
for n in [2,4]:
 z=json.loads((base/f'ledger-review/tranche{n}-'+('preservation.json' if n==2 else 'row-checks.json')).read_text()) if False else None
for x in json.loads((base/'ledger-review/tranche2-preservation.json').read_text()):reviewed_ledger[x['slug']+'.md']=x['ledger_sha256']
reviewed_ledger['fo-individual-income-tax.md']=json.loads((base/'ledger-review/tranche3-checks.json').read_text())['ledger_sha256']
for x in json.loads((base/'ledger-review/tranche4-row-checks.json').read_text())['protection']:reviewed_ledger[x['slug']+'.md']=x['ledger_sha256']
reviewed_ledger.update({'fo-corporate-income-tax.md':'dfb164a2eab618f49fbebbf30b0271a944ff47ca61d0e2d59bb47c3724b9146f','fo-transfer-pricing.md':'7133136945ccc3439b43d86682a74067a7fdd1e6a414289a17408a33147822d8','fo-country-by-country-reporting.md':'45e6998c3404de6e51f6ec0ec9a961e9fc851513780d871e834c5f2a82465c21'})
assert reviewed_ledger==mp['canonical_ledger_copies'];checks['canonical_reviewed_ledger_copies_exact']=len(reviewed_ledger)
pathops={Path(x['path']).name:x for x in mp['guide_path_only_operations']};totaloa=0;protected=[]
for f,sha in expected.items():
 p=w/'skills/international/faroe-islands'/f;b=p.read_text();reviewed=b
 if f in pathops:
  x=pathops[f];assert h(p.read_bytes())==x['after_sha256'];assert b.count(x['new_prefix'])==x['count'];reviewed=b.replace(x['new_prefix'],x['old_prefix']);assert h(reviewed.encode())==sha==x['before_sha256']
 else:assert h(p.read_bytes())==sha
 old=subprocess.check_output(['git','show','20572441dcdae9ebd4c282597940338832ade34e:skills/international/faroe-islands/'+f],cwd=w,text=True)
 oa=lambda t:re.findall(r'```oa-check\n.*?```',t,re.S);assert oa(old)==oa(b);totaloa+=len(oa(b))
 fm=lambda t:yaml.safe_load(t.split('---',2)[1]);a,c=fm(old),fm(b)
 for key in set(a)|set(c):
  if key not in ['version','last_updated','description']:assert a.get(key)==c.get(key),(f,key)
 if '> Contributed by ' in old:assert old[old.index('> Contributed by '):]==b[b.index('> Contributed by '):]
 else:assert '> Contributed by ' not in b
 urls=lambda t:re.findall(r'https?://[^\s<>\])]+',t);it=iter(urls(b));assert all(any(y==x for y in it) for x in urls(old)),f
 assert re.findall(r'^## .*',old,re.M)==re.findall(r'^## .*',b,re.M)
 for dest in re.findall(r'\]\(([^)]+)\)',b):
  if dest.startswith('../../../ledgers/'):assert (p.parent/dest.split('#')[0]).resolve().exists(),(f,dest)
 ident[f]={'sha256':h(p.read_bytes()),'bytes':p.stat().st_size};protected.append(f)
checks['old_main_examples_exact']=totaloa;assert totaloa==14;checks['all8_protected_metadata_byline_CTA_H2_oldURLorder']=protected
# README exact declared forward/inverse.
old=(base/'README.before-ledger-checkpoint.md').read_text();actual=(w/'skills/international/faroe-islands/README.md').read_text();ops=json.loads((base/'README-ledger-update-operations.json').read_text());new=old
for a,b in ops['replacements'].items():assert new.count(a)==1;new=new.replace(a,b,1)
assert new.count(ops['insert_after'])==1;new=new.replace(ops['insert_after'],ops['insert_after']+ops['insertion'],1);assert new==actual==(base/'README.exact-after-ledger-checkpoint.md').read_text()
inv=actual.replace(ops['insert_after']+ops['insertion'],ops['insert_after'],1)
for a,b in reversed(list(ops['replacements'].items())):assert inv.count(b)==1;inv=inv.replace(b,a,1)
assert inv==old
frozen=json.loads((base/'freeze.json').read_text());assert h(old.encode())==frozen['files']['README.md']['sha256'];checks['README_complete_declared_forward_inverse']=True
for dest in re.findall(r'\]\(([^)]+)\)',actual):
 if dest.startswith('../../../ledgers/'):assert (w/'skills/international/faroe-islands'/dest).resolve().exists(),dest
ident['README.md']={'sha256':h(actual.encode()),'bytes':len(actual.encode())}
# Inspect ingestion code separately: skills and packages/us-federal only. No new FO snapshot can be ingested.
front=[]
for p in (w/'skills').rglob('*.md'):
 if p.name.lower().startswith('readme'):continue
 text=p.read_text(errors='replace')
 if text.startswith('---') and re.search(r'(?m)^jurisdiction:\s*["\x27]?FO(?:["\x27]?\s*)$',text.split('---',2)[1]):front.append(str(p.relative_to(w)))
assert sorted(front)==sorted('skills/international/faroe-islands/'+f for f in expected),front
checks['only8_FO_frontmatter_Guides_in_ingestion_tree']=front
archive=[]
for n in [1,2,3,4]:
 p=base/f'ledger-review/tranche{n}-report.md';q=e/f'independent-review/tranche{n}-report.md';assert q.read_bytes()==p.read_bytes();archive.append({'tranche':n,'sha256':h(p.read_bytes())})
checks['independent_tranche_reports_archive_exact']=archive
(o/'checks.json').write_text(json.dumps({'checks':checks,'final9identities':ident,'scope':'Pure packaging/README/protection check. No new legal research or full-body restart. Original261source/evidence bytes verified by hashes; acquired is not read.'},indent=2)+'\n');print(json.dumps({'checks':{k:v for k,v in checks.items() if not isinstance(v,list)},'final':ident},indent=2))
