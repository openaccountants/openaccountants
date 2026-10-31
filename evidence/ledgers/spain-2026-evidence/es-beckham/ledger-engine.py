from pathlib import Path
import re,json,hashlib,subprocess,difflib
ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
FROZEN='0b5e62451de50220ac6d80c7813d547d08108641'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def units(s):
 out=[];section='Metadata';sub=''
 for m in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',s):
  u=m.group(0).strip();lf=s.count('\n',0,m.start())+1
  if u.startswith('## '):section=u.splitlines()[0];sub=''
  elif u.startswith('### '):sub=u.splitlines()[0]
  sec=section+(' / '+sub if sub else '')
  if u.startswith('|') or (not u.startswith('```') and re.match(r'^(?:\d+\.|[-*]) ',u)):
   for j,line in enumerate(u.splitlines()):
    if line.strip():out.append((lf+j,sec,line))
  else:out.append((lf,sec,u))
 return out

def clauses(u):
 if u.startswith(('|','```')):return [u]
 # One sentence or semicolon clause per rule, preserving exact original substring.
 return [x for x in re.split(r'(?<=[.!?])\s+(?=[A-Z][a-z]|No\b|Do\b|For\b|The\b|A\s)|;\s+(?=[A-Z]|[a-z])',u) if x]

def render(slug,rows,notes=None,section_routes=None):
 p=ROOT/'ledgers/spain-2026-evidence'/slug;p.mkdir(parents=True,exist_ok=True);f=ROOT/'skills/international/spain'/f'{slug}.md';b=f.read_text();p.joinpath('frozen-guide.md').write_bytes(f.read_bytes())
 assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==FROZEN
 oldmaps=[]
 for ref,title in [('62b7639a5a68324a83a96bb0190fff8b7c76f8c5','actual published main comparator (origin/main at start)'),(FROZEN,'frozen GitHub-public PR branch body')]:
  run=subprocess.run(['git','show',ref+':'+str(f.relative_to(ROOT))],cwd=ROOT,capture_output=True,text=True)
  if run.returncode:oldmaps.append(dict(ref=ref,title=title,wording='Guide absent at this path',destination='No prior file; frozen PR-branch lineage separately mapped.'));continue
  p.joinpath(('prior-main' if ref!=FROZEN else 'published')+'-guide.md').write_text(run.stdout)
  current=units(b);current_terms=[set(re.findall(r'\w+',x[2].lower())) for x in current]
  for lf,sec,u in units(run.stdout):
   if u in b:dest=f'Current LF{b[:b.index(u)].count(chr(10))+1}, exact original unit'
   else:
    dest='EXPLICIT TOPIC-MAPPING GAP: original unit retained here and in baseline; no guessed line pointer is asserted.'
    if section_routes:
     for key,value in section_routes:
      if key in sec:dest=value;break
    if notes:
     for needle,note in notes:
      if needle in u:dest=note;break
    if u.startswith('#') or re.match(r'^\|(?:[ -]*\|)+$',u):dest='Presentation heading/table separator, not a separate substantive tax rule. '+dest
   oldmaps.append(dict(ref=ref,title=title,old_lf=lf,section=sec,wording=u,destination=dest))
 def c(x):return str(x).replace('|','\\|').replace('\n','<br>')
 md=f'# {slug}: whole-Guide figure and rule ledger\n\nFrozen HEAD `{FROZEN}`; Guide SHA256 `{sha(f)}`. Writer record, 28 October 2026. The ledger writer has not edited the Guide. The Git HEAD identifies the supplied branch base; the Guide SHA identifies the current root-supplied body. This ledger is neither an independent PASS nor country completion or professional attestation. Every substantive rule/figure unit is retained verbatim below; derived fictional-case amounts are labelled separately from statutory numbers. Acquisition does not mean reading. Actual quoted Spanish source scopes, reader/raw hashes and source-chain qualifications are in the accompanying evidence.\n\n| # / current Guide LF | Guide section | Figure / rule exactly as written | Official act/article or page | Official URL | Short exact original-language quote / selected read scope | Actual read date / status |\n|---|---|---|---|---|---|---|\n'
 for i,z in enumerate(rows,1):
  z['id']=f'{slug}-{i:04}';md+='| '+c(z['id']+' / LF'+str(z['lf']))+' | '+c(z['section'])+' | '+c(z['wording'])+' | '+c(z['authority'])+' | '+c(z['url'])+' | '+c(z['quote'])+' | '+c(z.get('read_on','2026-10-28')+'; '+z['status'])+' |\n'
 md+='\n## Old topics carried\n\nEvery old blank-delimited topic, list item, table row, source block, example, byline and CTA is mapped against actual published-main and frozen GitHub-public PR-branch Git objects. Corrections of historical unsupported statements are explicit; old wording remains retained in this table and the byte-identical baseline copies. Current precise Sources limitations remain in the claim ledger.\n\n| Baseline / original LF | Every old topic as written | Current destination / correction / precise boundary |\n|---|---|---|\n'
 for z in oldmaps:md+='| '+c(z['title']+' '+z['ref']+' LF'+str(z.get('old_lf','—')))+' | '+c(z['wording'])+' | '+c(z['destination'])+' |\n'
 (ROOT/'ledgers'/f'{slug}.md').write_text(md);p.joinpath('claim-rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');p.joinpath('old-topics.json').write_text(json.dumps(oldmaps,ensure_ascii=False,indent=2)+'\n')
 return dict(slug=slug,guide_sha256=sha(f),ledger_sha256=sha(ROOT/'ledgers'/f'{slug}.md'),rows=len(rows),old_units=len(oldmaps))
