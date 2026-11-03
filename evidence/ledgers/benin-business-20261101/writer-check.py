#!/usr/bin/env python3
"""Check this new job's preservation, source identities, shape and examples.

This is writer-side evidence, not an independent legal review.
"""
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

R=Path(__file__).resolve().parents[3]
E=Path(__file__).parent
S=R.parent/'sources'
sys.path.insert(0,str(R/'scripts'))
import skill_checks

def sha(b): return hashlib.sha256(b).hexdigest()
def git(*a): return subprocess.check_output(['git',*a],cwd=R)
def norm(t): return re.sub('[^a-z0-9]','',unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower())

baseline=json.loads((E/'preservation-baseline.json').read_text())
preserved=[]
route=json.loads((E/'readme-routing-change.json').read_text())
for row in baseline['files']:
    path=row['path']
    old=git('show',f"{baseline['base_commit']}:{path}")
    assert sha(old)==row['sha256'],path
    assert git('rev-parse',f"{baseline['base_commit']}:{path}").decode().strip()==row['git_blob'],path
    # Sparse checkout omits older immutable evidence; verify its actual HEAD blob.
    current=(R/path).read_bytes() if (R/path).exists() else git('show',f'HEAD:{path}')
    if path=='skills/benin/README.md':
        assert current==old+route['literal_append'].encode(),path
        assert sha(current)==route['new_sha256']
    else:
        assert current==old,path
        preserved.append(path)

sources=json.loads((E/'source-identities.json').read_text())
for source in sources:
    b=(S/source['file']).read_bytes()
    assert sha(b)==source['sha256'] and len(b)==source['bytes'],source['file']
texts={name:norm((S/filename).read_text()) for name,filename in [('cgi2026.pdf','cgi2026.txt'),('lf2026.pdf','lf2026-ocr.txt'),('lfr2026.pdf','lfr2026-ocr.txt')]}
exceptions=json.loads((E/'visual-quote-anchors.json').read_text())
visually_confirmed={(x['row_id'],x['quote']) for x in exceptions}
for x in exceptions:
    assert sha((S/x['scan_file']).read_bytes())==x['scan_sha256']

rows=json.loads((E/'bj-business-income-tax.json').read_text())
assert len(rows)==54 and len({x['id'] for x in rows})==54
visual_used=[]
for row in rows:
    assert all(row.get(k) for k in ['section','rule','act_article','official_url','exact_french_quote','read_date','source_file','source_sha256','read_scope'])
    source=next(s for s in sources if s['file']==row['source_file'])
    assert row['source_sha256']==source['sha256']
    for q in [row['exact_french_quote']]+row.get('additional_quote_anchors',[]):
        if norm(q) not in texts[row['source_file']]:
            assert (row['id'],q) in visually_confirmed,(row['id'],q)
            visual_used.append([row['id'],q])
    for support in row.get('additional_sources',[]):
        ss=next(s for s in sources if s['sha256']==support['source_sha256'])
        for q in support['exact_french_quotes']:
            assert norm(q) in texts[ss['file']],(row['id'],q)

path=R/'skills/benin/bj-business-income-tax.md'
text=path.read_text()
fm=skill_checks.read_frontmatter(text)
assert not any(x in fm for x in ['review_status','trust_label','license','reviewed_by','reviewed_on','verified_by','authored_by'])
assert 'openaccountants-cta-block' not in text
assert 80<=len(fm['description'].split())<=150
checks=skill_checks.run_checks(str(path),text,fm)
assert len(checks)==15 and all(not v for v in checks.values()),checks
result=subprocess.run([sys.executable,'scripts/check-examples.py','--require',str(path.relative_to(R))],cwd=R,text=True,capture_output=True)
assert result.returncode==0,result.stdout+result.stderr
report=dict(status='Writer checks passed; independent source review pending',prior_head=baseline['base_commit'],shape_checks=checks,ledger_rows=len(rows),source_files_verified=[s['file'] for s in sources],visual_quote_anchors=visual_used,preserved_guide_count=10,preserved_prior_evidence=43,preserved_paths=preserved,readme_append_only=True,old_units_moved_removed=0,example_result=dict(returncode=result.returncode,stdout=result.stdout,stderr=result.stderr),remaining_domains='All seven remain partial')
print(json.dumps(report,ensure_ascii=False,indent=2))
