from pathlib import Path
import subprocess,hashlib,json,re,shutil,difflib
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain');O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');P=O/'germany-existing-evidence-reconciliation-2026-10-28';D=Path('/Users/michaelcutajar/Downloads/oa-f1-wt');REF='62b7639a5a68324a83a96bb0190fff8b7c76f8c5';repo=D/'wt-rev-903'
sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args,cwd=R):return subprocess.check_output(['git',*args],cwd=cwd,stderr=subprocess.DEVNULL)
def write(n,z): (P/n).write_text(json.dumps(z,ensure_ascii=False,indent=2)+'\n')
reports=list(sorted((D/'reports').glob('DE*.md')))+[D/'reports'/n for n in ['noloss-A-rev.md','noloss-A.md','restore-rev.md','shrink-audit.md']]
(P/'preserved-review-reports').mkdir(exist_ok=True)
ri=[]
for f in reports:
 b=f.read_bytes();t=P/'preserved-review-reports'/f.name;shutil.copy2(f,t);assert t.read_bytes()==b;ri.append(dict(path=str(f),copy=str(t.relative_to(P)),sha256=sha(b),bytes=len(b),kind='independent review'if '-rev' in f.name or f.name=='restore-rev.md'else 'writer/audit report; not independent legal proof'))
write('preserved-report-identities.json',ri)
external=[]
for f in [O/'claude-status.md',O/'claude-restoration-merged-review-evidence.json',O/'country-register.json',D/'HANDOVER-to-ChatGPT.md',D/'HANDOVER-wave3.md',D/'writer-brief.md',D/'reviewer-brief.md']:
 external.append(dict(path=str(f),sha256=sha(f.read_bytes()),bytes=f.stat().st_size))
write('context-identities.json',external)
sourcefiles=[]
for f in sorted((D/'sources/DE').rglob('*')):
 if f.is_file(): sourcefiles.append(dict(path=str(f),relative=str(f.relative_to(D/'sources/DE')),sha256=sha(f.read_bytes()),bytes=f.stat().st_size,scope='Existing acquired artifact only; no new primary-text reading or claim verification in this inventory'))
write('existing-source-file-identities.json',sourcefiles)
checks={
'de-capital-gains':('2e232d255055a9c5d25176b15126dfff69af4c5c','DE-cg-rev.md',862,['noloss-A-rev.md'],903,'31 earlier figures; later43 across two restored Guides,23 restored items across them'),
'germany-vat-return':('2e232d255055a9c5d25176b15126dfff69af4c5c','DE-vat-rev.md',805,['noloss-A-rev.md'],903,'34 earlier figures; later43 across two restored Guides,23 restored items across them'),
'de-estimated-tax':('427f3162','DE-est-rev.md',873,['restore-rev.md'],883,'36 earlier figures; restoration19 across two Guides,7+1 restored items'),
'de-einkommensteuer-freelancer':('427f3162','DE-free-rev2.md',869,['restore-rev.md'],883,'34 earlier figures; restoration19 across two Guides,7+1 restored items'),
'de-payroll-benefits':('ecc0b877','DE-ben-rev.md',830,[],None,'52 figures'),
'de-payroll':('00c8caae','DE-pr-rev.md',815,[],None,'64 figures and independent PAP script'),
'de-rental-income':('4450784c','DE-rent-rev.md',823,[],None,'38 figures/rules'),
'de-social-contributions':('dbd3e36e','DE-sc-rev.md',853,[],None,'34 figures'),
'de-trade-tax':('05a61fbe','DE-gewst-rev.md',809,[],None,'41 figures')}
exclude={'germany-bookkeeping':'Accounting/bookkeeping; retained as excluded non-tax-computation companion, not silently omitted.','germany-financial-statements':'Financial reporting under HGB; retained as excluded non-tax-computation companion.','germany-formation':'Company incorporation/registration; excluded core tax-computation population; incidental tax passages are not independently cleared.'}
# E-invoice included deliberately as VAT compliance; tax planning included despite not a core domain entry.
refs=[];rows=[];diffdir=P/'review-pin-differences';diffdir.mkdir(exist_ok=True)
paths=git('ls-tree','-r','--name-only',REF,'skills/international/germany').decode().splitlines()
def method_body(b):
 t=b.decode();t=re.sub(r'^---\n.*?\n---\n','',t,count=1,flags=re.S);t=t.split('<!-- openaccountants-cta-block -->')[0];t=re.sub(r'\n> Contributed by [^\n]+\.\s*$','',t);return t.strip()
for path in paths:
 b=git('show',REF+':'+path);slug=Path(path).stem;urls=list(dict.fromkeys(re.findall(r'https?://[^\s<>|)\]"\x27]+',b.decode())))
 row=dict(slug=slug,path=path,reference=REF,git_blob=git('rev-parse',REF+':'+path).decode().strip(),sha256=sha(b),bytes=len(b),literal_LF_lines=len(b.decode().split('\n')),worktree_identical=(R/path).read_bytes()==b,cited_URLs=urls,ledger='No pre-existing Guide figure ledger located in requested main tree or Downloads ledgers directory. A new review still requires the ledger; prior completed review remains preserved.')
 if slug in ['README','references']:
  row.update(population='routing/source-index companion',review_chain='Not itself a tax-computation Guide');refs.append(row);continue
 if slug in exclude:
  row.update(population='excluded non-tax-computation companion',exclusion_reason=exclude[slug],review_chain='No independent whole-body review located; excluded for explicit scope reason, not passed')
 else:
  row['population']='tax/compliance Guide'
  if slug in checks:
   pin,report,pr,rest,restpr,scope=checks[slug];full=git('rev-parse',pin+'^{commit}',cwd=repo).decode().strip();old=git('show',full+':'+path,cwd=repo)
   diff=''.join(difflib.unified_diff(old.decode().splitlines(True),b.decode().splitlines(True),fromfile=full+'/'+path,tofile=REF+'/'+path))
   df=diffdir/(slug+'.diff');df.write_text(diff)
   row.update(review_chain='Existing independent finite Guide review plus restoration where listed; not whole-country review',independent_report=report,original_PR=pr,restoration_reports=rest,restoration_PR=restpr,review_scope_as_reported=scope,comparison_pin=full,review_pin_sha256=sha(old),full_file_exact=(b==old),method_body_exact_ignoring_frontmatter_and_attribution_CTA_tail=(method_body(b)==method_body(old)),comparison_diff=str(df.relative_to(P)),comparison_limit='Full metadata/tail differences remain recorded; method-body equality is a mechanical identity result, not new legal clearance.')
   assert row['method_body_exact_ignoring_frontmatter_and_attribution_CTA_tail']
  else:row.update(review_chain='MISSING: no independently pinned full/selected Guide review located in searched preserved evidence; current citations or sibling reports are not proof',independent_report=None)
 rows.append(row)
write('guide-evidence-map.json',rows);write('routing-and-exclusion-map.json',refs+[x for x in rows if x['population'].startswith('excluded')])
e=json.loads((O/'claude-restoration-merged-review-evidence.json').read_text());de=next(x for x in e['pull_requests'] if x['number']==903);write('preserved-PR903-evidence-extract.json',de)
reg=json.loads((O/'country-register.json').read_text());write('preserved-country-register-DE-extract.json',next(x for x in reg if x.get('code')=='DE'))
# Preserve original independent payroll computation artifact separately, no execution/new review.
f=D/'tmp-DE-pr-rev/pap.py';shutil.copy2(f,P/'preserved-review-reports/DE-pr-independent-pap.py')
write('inventory-summary.json',dict(reference=REF,worktree_all30_exact=all(x['worktree_identical'] for x in rows+refs),all_country_files=len(paths),tax_compliance_guides=sum(x['population']=='tax/compliance Guide'for x in rows),excluded_non_tax_companions=len(exclude),routing_source_companions=len(refs),tax_guides_with_located_independent_report=len(checks),tax_guides_without_located_independent_report=sum(x['population']=='tax/compliance Guide'and not x.get('independent_report')for x in rows),full_file_review_pin_matches=sum(x.get('full_file_exact',False)for x in rows),nine_method_bodies_match=True,cached_source_artifacts=len(sourcefiles),source_read_ledger='No per-claim/per-source normalized actual-reading ledger found for Germany. Reports describe selected primary sources and stated limitations; acquisition inventory is not actual reading.',whole_pack_review='NOT LOCATED; coverage-complete labels and scoped restoration do not establish it',new_legal_research=False,new_country_review=False,Guide_or_Git_mutations=False))
lines=['# Germany existing-evidence reconciliation','',f'Inventory only, 28 October 2026. Requested public-main snapshot `{REF}`. All 30 Germany files in the Spain checkout match that snapshot byte-for-byte. No tax content, Git state or existing evidence was changed.','',f'The population is **25 tax/compliance Guides**, three explicit non-tax-computation companions and two routing/reference files. Nine tax Guides have located independent finite review reports; **16 have no located independent pinned Guide review chain**. No whole-country independent review or existing figure-ledger set was located. This inventory is not a new legal review or country-completion verdict.','','## Existing independent chains','','| Guide | Preserved independent review | Exact identity at requested main | Scope boundary |','|---|---|---|---|']
for x in rows:
 if x.get('independent_report'):
  reports=[x['independent_report']]+x['restoration_reports'];ident='Full file exact'if x['full_file_exact']else'Method body exact; metadata/tail changes in saved diff'
  lines.append(f"| {x['slug']} | "+', '.join(f'[{n}](preserved-review-reports/{n})'for n in reports)+f" | {ident}; pin `{x['comparison_pin'][:12]}` | {x['review_scope_as_reported']} |")
lines+=['','PR903 is a two-Guide restoration: `germany-vat-return` and `de-capital-gains`. Preserved GitHub evidence records final head `2e232d255055a9c5d25176b15126dfff69af4c5c`, merge `08ed44c5ae12909de8ddea8bcdd6207b699b3032`, and [independent comment](https://github.com/openaccountants/openaccountants/pull/903#issuecomment-6447804028). It reports 43 figures and 23 restored items across those two files, with two VAT assertions left unconfirmed. These are not 43 figures for every Guide. PR883 covers only estimated tax and freelancer restoration; its independent report expressly says it read the diffs only.','', 'The initial review reports are preserved rather than replaced. Examples of their still-recorded limits include state church-tax rules, selected future-year/form details, U1/U2/accident rates, some pensions/benefit routes and specific rental administrative updates. The full original reports contain the precise lists. No current closure is inferred from their historical ready-to-merge wording.','','## Missing independent Guide chains','','| Actual tax/compliance Guide | Existing evidence that can be reused | Missing chain |','|---|---|---|']
for x in rows:
 if x['population']=='tax/compliance Guide'and not x.get('independent_report'):lines.append(f"| {x['slug']} | {len(x['cited_URLs'])} cited URL strings in frozen body; source-family cache may overlap | No pinned independent full/selected Guide review located; sibling checks and coverage labels are insufficient |")
lines+=['','`germany-einvoice` is included because it states VAT invoicing compliance; `germany-tax-optimization` is included because it states tax calculations/planning rules. Overlapping `germany-payroll` is retained as its own Guide; the independent `de-payroll` review explicitly identifies the overlap but does not clear the entire older sibling.','','## Explicit exclusions and routing','','| File | Inventory treatment |','|---|---|']
for slug,reason in exclude.items():lines.append(f'| {slug} | {reason} |')
lines+=['| README | Seven-domain routing and coverage metadata; not a legal review |','| references | Source/project index; not a tax-computation Guide |','','## Source and preservation evidence','','- `existing-source-file-identities.json` hashes all 277 existing files in `~/Downloads/oa-f1-wt/sources/DE`. These include original official HTML/PDF bodies and some extracted text. Hashing is acquisition/preservation inventory only; neither valid response status nor actual selected reading is invented.','- Review reports identify statutes, articles, BMF letters, official PAP/test tables and selected actual checks. No Germany per-claim actual-read ledger or raw-to-quote scope manifest was located. File names and body citations alone cannot supply that missing link.','- `guide-evidence-map.json` pins every actual Guide blob/SHA256, cited URLs, exact review commit where recoverable and source/review limits. Full differences against the nine recovered review pins are saved under `review-pin-differences/`; none changes the compared tax-method body once frontmatter and contributor/CTA tails are separately excluded. Seven full-file differences are disclosed, not called protected-byte PASS.','- `preserved-review-reports/` contains byte-exact copies of 23 historical reports/audits plus the independent payroll PAP script. Existing original paths/hashes are retained in `preserved-report-identities.json`; no prior review was discarded.','- `claude-status.md` expressly distinguishes coverage-map completeness, whole-pack review and no-loss closure; it records unfinished duplicate handling and limits of earlier no-loss sweeps. The saved country register already classifies DE as restoration merged / pack evidence reconciliation, not final country PASS.','','Search was bounded to the requested Git snapshot/current Germany tree, existing closeout output/status/register/comment evidence, repository research/doc names, the historical `oa-f1-wt` reports/source/ledger folders and named DE review worktree objects. No new source fetch, primary-law research, test run, professional attestation or ledger bypass occurred. The missing-chain labels mean not located in those preserved locations, not proof that no historical review ever existed.','']
(P/'report.md').write_text('\n'.join(lines))
manifest=[]
for f in sorted(P.rglob('*')):
 if f.is_file() and f.name!='artifact-manifest.json':manifest.append(dict(path=str(f.relative_to(P)),sha256=sha(f.read_bytes()),bytes=f.stat().st_size))
write('artifact-manifest.json',manifest)
print(json.dumps(json.loads((P/'inventory-summary.json').read_text()),indent=2));print('report',sha((P/'report.md').read_bytes()));print('manifest',sha((P/'artifact-manifest.json').read_bytes()))
