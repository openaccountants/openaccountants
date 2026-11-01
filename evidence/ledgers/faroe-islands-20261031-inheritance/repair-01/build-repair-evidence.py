from pathlib import Path
import re,json,hashlib,subprocess,tarfile,io,ast
P=Path(__file__).resolve().parent;E=P.parent;R=E.parents[2]
anchor='aa3de1064ae435d69e650d19733c315d6146f35d';review_commit='805268ba7'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
URL=next(ast.literal_eval(n.value) for n in ast.parse((E/'build-ledgers.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='URL' for t in n.targets))
# Append a distinct row. The64 independently checked original rows and source
# bytes remain immutable; do not rerun the historical initial-ledger builder.
slug='fo-estate-income-tax';guide=R/'skills/faroe-islands'/f'{slug}.md';body=guide.read_text();a=body.index('If an estate omits');b=body.index('\n\n',a);claim=' '.join(body[a:b].split())
src=(E/'sources/tax.reader.txt').read_text();a=src.index('§ 103.');b=src.index('\n§ 103 a.',a);sec=src[a:b];p1=sec.split('\nStk. 2.')[0];p3=sec[sec.index('Stk. 3.'):];quote=p1+'\n\n'+p3
row=dict(id='ET-029',section='Penalties and interest',claim=claim,sources=[dict(act_article='Tax Act §103(1), (3)',url=URL['tax'],read_date='2026-10-31',source_file='sources/tax.reader.txt',original_language_quote=quote,kind='statute')],finding='FO-EST-002',note='Required accounts omitted makes the return invalid; the authority can set a deadline and impose100DKK/day from expiry until receipt. Not automatic on every late return and distinct from§14(7)/§104.')
(P/'estate-accounts-sanction.rows.json').write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
(P/'estate-accounts-sanction.md').write_text('# ET-029: neighbouring accounts-sanction rule\n\n'+claim+'\n\nTax Act§103(1),(3), read31October2026. [Official source]('+URL['tax']+'). Existing source reader retained byte-exact; fresh official read in tax-103-fresh-web.txt.\n\n'+ '\n'.join('> '+q for q in quote.splitlines())+'\n')
# Verify every old ledger row is byte-exact and its complete rule remains in
# the same current Guide. New source paragraph is separate, not a renumbering.
claimmap=[]
for oldslug in ['fo-inheritance-duty','fo-estate-income-tax']:
 p=E/f'{oldslug}.rows.json';old=subprocess.check_output(['git','show',f'{anchor}:{p.relative_to(R)}']);assert old==p.read_bytes()
 raw=(R/'skills/faroe-islands'/f'{oldslug}.md').read_text();words=list(re.finditer(r'\S+',raw));normal=' '.join(m.group() for m in words)
 for rec in json.loads(old):
  assert rec['claim'] in normal,rec['id']
  first=rec['claim'].split()[0:5];prefix=' '.join(first);index=normal.index(prefix);char=0;line=1
  for m in words:
   if char>=index:line=raw[:m.start()].count('\n')+1;break
   char+=len(m.group())+1
  claimmap.append(dict(id=rec['id'],destination=f'skills/faroe-islands/{oldslug}.md:{line}',disposition='Complete original rule retained verbatim after whitespace normalization; original row/source bytes unchanged.'))
claimmap.append(dict(id='ET-029',destination=f'skills/faroe-islands/{slug}.md:'+str(body[:body.index('If an estate omits')].count('\n')+1),disposition='Added neighbouring statutory sanction.'))
(P/'current-row-destinations.json').write_text(json.dumps(claimmap,ensure_ascii=False,indent=2)+'\n')
# Verify every original captured source, initial ledger and independent-review file.
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',review_commit,str((E/'sources').relative_to(R)),str((E/'independent-review').relative_to(R))],text=True).splitlines()
blob=subprocess.check_output(['git','archive','--format=tar',review_commit,'--',*paths]);retained=[]
with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
 for m in tar:
  if not m.isfile():continue
  p=R/m.name;assert tar.extractfile(m).read()==p.read_bytes(),m.name;retained.append(dict(path=m.name,sha256=sha(p)))
# All nine earlier Guides remain exact against their established preservation anchor.
for rec in json.loads((E/'preservation.json').read_text())['old_topics_destinations']:
 assert sha(R/rec['path'])==rec['sha256']
(P/'preservation.json').write_text(json.dumps(dict(anchor=anchor,initial_review_commit=review_commit,old_rows_retained=64,new_rows=1,nine_predecessor_guides_unchanged=True,retained_source_and_review_files=retained,initial_snapshot_files=[dict(path=str(p.relative_to(R)),sha256=sha(p)) for p in sorted((P/'initial-snapshot').glob('*'))]),ensure_ascii=False,indent=2)+'\n')
# Mechanical link resolution checks apply to actual Markdown definitions/cells.
linkchecks=[]
for oldslug in ['fo-inheritance-duty','fo-estate-income-tax']:
 raw=(R/'skills/faroe-islands'/f'{oldslug}.md').read_text();defs=dict(re.findall(r'^\[([^\]]+)\]: (\S+)\s*$',raw,re.M))
 for key in ['court','opening','closing']:
  if f'[{key}]:' not in raw:continue
  assert defs[key]==URL[key]
  assert raw.count(URL[key])==2,(oldslug,key,raw.count(URL[key]))
  linkchecks.append(dict(guide=oldslug,key=key,url=URL[key],reference_definition_exact=True,sources_cell_exact=True,spaces_or_concatenation=False,live_read='Official publisher web retrieval31October2026; court readable and linked D03sixpages/closingfourpages reopened.',direct_raw_access='Direct HTTP route remains403 in prior source-access note; no bypass or CAPTCHA.'))
 for line in raw.splitlines():
  if line.startswith('|') and 'https://' in line:
   for cell in line.split('|'):
    if cell.strip().startswith('https://'):assert not re.search(r'\s',cell.strip()),(oldslug,line[:80])
 assert 'trust_label:' not in raw and 'category: international\n' in raw
(P/'link-resolution.json').write_text(json.dumps(linkchecks,ensure_ascii=False,indent=2)+'\n')
assert all(' '.join(q.split()) in ' '.join(src.split()) for q in quote.split('\n\n'))
# Keep historical81quote checks; append exactly one new quote group.
old=json.loads((P/'initial-snapshot/quote-integrity.json').read_text());assert len(old)==81
(E/'quote-integrity.json').write_text(json.dumps(old+[dict(row='ET-029',article='Tax Act§103(1),(3)',all_quote_parts_exact=True)],ensure_ascii=False,indent=2)+'\n')
# Current manifest supersedes the initial one, which remains an exact snapshot.
initial=json.loads((P/'initial-snapshot/writer-manifest.json').read_text());inputs=[R/x['path'] for x in initial['inputs']]
inputs.extend(p for p in P.rglob('*') if p.is_file() and p.name not in ['validation.json','closure-request.md'])
inputs.extend(p for p in (E/'independent-review').glob('*') if p.is_file())
inputs=sorted(set(inputs));manifest=dict(date='2026-10-31',initial_candidate=anchor,initial_manifest_sha256=sha(P/'initial-snapshot/writer-manifest.json'),initial_review_commit=review_commit,original_ledger_rows=64,additional_ledger_rows=1,exact_quote_groups=82,ledger_paths=['fo-inheritance-duty.rows.json','fo-estate-income-tax.rows.json','repair-01/estate-accounts-sanction.rows.json'],inputs=[dict(path=str(p.relative_to(R)),sha256=sha(p)) for p in inputs],independent_review='Initial64rules checked; bounded repair closure pending',publication_rights='Not assessed by this tax-source repair. No statement that all official pages are free to republish.',scope='No country-gap clearance, professional attestation, push, authority contact, filing or payment.')
(E/'writer-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('64original rows retained;1appended row;82quote groups;',len(inputs),'current manifest inputs; manifestSHA256',sha(E/'writer-manifest.json'))
