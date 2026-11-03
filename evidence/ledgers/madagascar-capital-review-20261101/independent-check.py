#!/usr/bin/env python3
"""Read-only check of the frozen capital candidate; writes reviewer evidence only."""
from pathlib import Path
import hashlib, json, os, re, subprocess, sys
from decimal import Decimal, ROUND_FLOOR

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
HEAD = 'b60a51a4adb08da4ea3eb4a8a5e1962b1a2b8a78'
CONTENT = '918a4af3712e455678bf6084874a2f01313bdb12'
PRIOR = 'abe41a37adcb9d3f58a377b8b7219a73674cb234'
BASE = '59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
WRITER = ROOT/'evidence/ledgers/madagascar-capital-20261101'
sha = lambda x: hashlib.sha256(x).hexdigest()
norm = lambda x: re.sub(r'\s+', ' ', x).strip()
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)
def dump(name, value):
    (OUT/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')

assert git('rev-parse', 'HEAD').decode().strip() == HEAD
assert git('merge-base', HEAD, 'origin/main').decode().strip() == BASE
assert git('rev-parse', 'origin/main').decode().strip() == BASE
assert git('diff', '--name-only', CONTENT, HEAD).decode().splitlines() == [
    'evidence/ledgers/madagascar-capital-20261101/committed-validation.json']
target_paths = [f'skills/madagascar/{x}' for x in ['mg-capital-income.md', 'README.md']]
target_paths += [str(p.relative_to(ROOT)) for p in sorted(WRITER.iterdir()) if p.is_file()]
dump('initial-input-hashes.json', {'head': HEAD, 'content_head': CONTENT,
     'prior_head': PRIOR, 'actual_local_merge_base': BASE,
     'files': [{'path': p, 'git_blob': git('rev-parse', f'{HEAD}:{p}').decode().strip(),
                'sha256': sha(git('show', f'{HEAD}:{p}')),
                'working_copy_equal': (ROOT/p).read_bytes() == git('show', f'{HEAD}:{p}')}
               for p in target_paths]})

rows = json.loads((WRITER/'mg-capital-income.json').read_text())
assert [x['id'] for x in rows] == [f'C{i:02}' for i in range(1, 47)]
page_map = {
 'cdi': {'13':[14], '43':[44], '44':[45], '45':[46], '172–174':[173,174,175], '209':[210]},
 'cpf': {'16':[17], '17':[18]},
 'lfi': {'42':[44], '129':[131]},
 'lfr': {'20':[24], '22':[26], '48':[52]}}
quote_results=[]
for row in rows:
    pdf = ROOT/row['cached_pdf']
    key = pdf.name.split('-')[0]
    pages = page_map[key][row['printed_page']]
    text = '\n'.join(subprocess.check_output(
        ['pdftotext', '-layout', '-f', str(p), '-l', str(p), str(pdf), '-'], text=True) for p in pages)
    assert sha(pdf.read_bytes()) == row['pdf_sha256']
    checks = [{'quote': q, 'exact_after_whitespace_only': norm(q) in norm(text)}
              for q in row['exact_french_quotes']]
    assert all(x['exact_after_whitespace_only'] for x in checks), row['id']
    quote_results.append({'id': row['id'], 'article': row['article'],
        'printed_pages': row['printed_page'], 'physical_pages': pages,
        'pdf_sha256': sha(pdf.read_bytes()), 'fresh_page_extraction_sha256': sha(text.encode()),
        'checks': checks})
dump('independent-page-quote-check.json', {'method':
    'Fresh pdftotext -layout extraction of the specific cached PDF pages, not writer cached text; exact matching changes whitespace only. Semantic/neighbour review is separate.',
    'rows':quote_results, 'passed_rows':len(quote_results)})

baseline = json.loads((WRITER/'preservation-baseline.json').read_text())
assert baseline['immutable_prior_head'] == PRIOR
all_old = git('ls-tree','-r','--name-only',PRIOR,'--','skills/madagascar','evidence/ledgers').decode().splitlines()
old_guides = [p for p in all_old if p.startswith('skills/madagascar/') and p.endswith('.md') and not p.endswith('/README.md')]
old_evidence = [p for p in all_old if p.startswith('evidence/ledgers/madagascar-') or p.startswith('evidence/ledgers/mg-')]
assert len(old_guides) == 9 and len(old_evidence) == 48
assert set(x['path'] for x in baseline['files']) == set(old_guides + old_evidence)
pres=[]
topics=[]
for path in sorted(old_guides + old_evidence):
    old = git('show', f'{PRIOR}:{path}'); new = git('show', f'{HEAD}:{path}')
    assert old == new
    bound = next(x for x in baseline['files'] if x['path'] == path)
    assert sha(old) == bound['sha256']
    assert git('rev-parse',f'{HEAD}:{path}').decode().strip() == bound['git_blob']
    pres.append({'path':path, 'prior_and_target_blob':bound['git_blob'],
        'sha256':sha(old), 'identical':True, 'working_copy_present':(ROOT/path).exists()})
    if path in old_guides:
        lines=old.decode().splitlines()
        starts=[0]+[i for i,l in enumerate(lines) if l.startswith('## ')]
        for i,s in enumerate(starts):
            end=starts[i+1] if i+1<len(starts) else len(lines)
            topics.append({'old_file':path,'old_lines':[s+1,end],
                'section':'Frontmatter/title/preamble' if s==0 else lines[s],
                'destination':path, 'destination_lines':[s+1,end],
                'decision':'Complete unchanged bytes at the identical blob, including all intervening bullets/tables and suffix.'})
dump('preservation-review.json', {'prior_head':PRIOR,'target':HEAD,
 'guide_count':len(old_guides),'evidence_count':len(old_evidence),
 'sparse_evidence_compared_from_git':sum(not (ROOT/p).exists() for p in old_evidence),
 'removed_topics':0,'lost_content_restored':0,'files':pres})
dump('complete-old-topic-map.json', {'basis':'Every line of all nine old Guides maps to identical old file and line range. No rewrite or retirement.', 'sections':topics})

def down(x):return (x/Decimal(1000)).to_integral_value(rounding=ROUND_FLOOR)*1000
d=Decimal(10005999); a=d*Decimal('.5'); b=down(a); tax=b*Decimal('.2')
interest=Decimal(1234567); ib=down(interest); coop=ib*Decimal('.1'); normal=ib*Decimal('.2')
dump('independent-cases.json', {'method':'Decimal recomputation independent of oa-check engine',
 'case1':{k:str(v) for k,v in {'gross':d,'after_allowance':a,'rounded_base':b,'ircm':tax,'net':d-tax}.items()},
 'case2':{k:str(v) for k,v in {'income':interest,'rounded_base':ib,'cooperative_ircm':coop,'ordinary_ircm':normal,'difference':normal-coop}.items()},
 'classification':'Case 2 is a documented fact/category decision, not an election; ordinary nonexempt receipts only; no historical II-B result or disposal formula.'})

sys.path.insert(0,str(ROOT/'scripts'))
from frontmatter_yaml import load_frontmatter
import skill_checks
path=ROOT/'skills/madagascar/mg-capital-income.md'; text=path.read_text()
fm=load_frontmatter(text.split('---',2)[1])
shape=skill_checks.run_checks(str(path),text,fm)
assert len(shape)==15 and not any(shape.values())
dump('shape-checks.json', {'count':len(shape),'results':shape,
 'description_words':len(fm['description'].split()),'accountant_review_keys':{
 k:fm.get(k) for k in ['tier','reviewed_by','reviewed_on']}})
commands=[
 ['python3','scripts/check-examples.py','--require','skills/madagascar/mg-capital-income.md'],
 ['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],
 ['python3','scripts/check-sync-integrity.py','--base',BASE,'--mode','audit','--strict-metadata'],
 ['git','diff','--check',BASE,HEAD],
 ['git','diff','--check']]
results=[]
for cmd in commands:
    r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    results.append({'command':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
dump('machine-checks.json', {'target':HEAD,'actual_local_merge_base':BASE,
    'environment':{'PYTHONPATH':os.environ.get('PYTHONPATH')},'checks':results})
assert all(x['exit_code']==0 for x in results)
print(json.dumps({'rows':len(rows),'quote_checks':'pass','preserved_guides':len(old_guides),
 'preserved_evidence':len(old_evidence),'old_sections_mapped':len(topics),
 'shape_checks':len(shape),'machine_commands':len(results),'all_machine_checks_pass':True},indent=2))
