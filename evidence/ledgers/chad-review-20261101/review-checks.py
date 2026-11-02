#!/usr/bin/env python3
"""Reproduce the mechanical and preservation portion of the independent review."""
from pathlib import Path
import datetime, hashlib, json, os, re, subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
FROZEN = '0a85c3bd65f4dc30edf9319cf52d04c395a1d305'
ENV = dict(os.environ, PYTHONPATH='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps')
def sha(b): return hashlib.sha256(b).hexdigest()
def git(*args): return subprocess.check_output(['git', *args], cwd=ROOT)
def run(argv):
    p = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, text=True)
    return dict(argv=argv, returncode=p.returncode, stdout=p.stdout, stderr=p.stderr)
assert git('rev-parse', 'HEAD').decode().strip() == FROZEN
manifest=json.loads((ROOT/'evidence/ledgers/chad-draft-20261101/candidate-manifest.json').read_text())
files = list(manifest) + ['evidence/ledgers/chad-draft-20261101/candidate-manifest.json', 'evidence/ledgers/chad-draft-20261101/source-record.json']
candidate={}
for name in files:
    b=(ROOT/name).read_bytes()
    committed=git('show', f'{FROZEN}:{name}')
    candidate[name]={'sha256':sha(b), 'matches_frozen_commit':b==committed, 'matches_draft_manifest':sha(b)==manifest[name] if name in manifest else None}
    assert b==committed
    if name in manifest: assert sha(b)==manifest[name]
legacy_expected=json.loads((ROOT/'../sources/legacy-sha256.json').read_text())
maptext=(ROOT/'evidence/ledgers/chad-old-topics.md').read_text()
maptopics={line.split('|')[1].strip() for line in maptext.splitlines() if line.startswith('| td-')}
legacy={}
for name, expected in legacy_expected.items():
    rel=f'skills/chad/{name}'
    b=(ROOT/rel).read_bytes()
    body=b.decode().split('<!-- openaccountants-cta-block -->')[0].split('---',2)[-1]
    topics=[line.strip() for line in body.splitlines() if re.match(r'^#{1,6}\s|^\s*-\s+\*\*|^\s*\|',line) and not re.match(r'^\s*\|\s*[-:]+',line)]
    missing=[topic for topic in topics if f'{name}: {topic}' not in maptopics]
    legacy[name]={'sha256':sha(b), 'matches_capture':sha(b)==expected, 'matches_frozen_parent':b==git('show',f'{FROZEN}^:{rel}'), 'matches_fetched_origin_main':b==git('show',f'origin/main:{rel}'), 'topics':len(topics), 'missing_topics':missing}
    assert sha(b)==expected and b==git('show',f'{FROZEN}^:{rel}') and not missing
source=ROOT/'../sources/arrete-135-review-20261101.pdf'
commands=[
    ['git','status','-sb'],
    ['git','diff','--name-status','origin/main...HEAD'],
    ['pdfinfo',str(source)],
    ['python3','scripts/skill_checks.py','skills/chad/td-import-exemption-eligibility.md'],
    ['python3','scripts/check-examples.py','--require','skills/chad/td-import-exemption-eligibility.md'],
    ['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],
]
results=[run(command) for command in commands]
assert all(result['returncode']==0 for result in results)
result={'candidate_commit':FROZEN,'reviewed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'origin_main_at_review':git('rev-parse','origin/main').decode().strip(), 'candidate_files':candidate,'legacy_files':legacy,'topic_total':sum(row['topics'] for row in legacy.values()),'source':{'url':'https://ecofinances.gouv.td/wp-content/uploads/2026/09/Arrete-N135-Exoneration-des-droits-et-taxes-sur-les-produits09092026164852.pdf','private_path':str(source.resolve()),'bytes':source.stat().st_size,'sha256':sha(source.read_bytes()),'matches_writer_capture':source.read_bytes()==(ROOT/'../sources/arrete-135-2026.pdf').read_bytes()},'commands':results}
finance=ROOT/'../sources/finance-law-review-20261101.pdf'
result['additional_sources']=[{'url':'https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf','private_path':str(finance.resolve()),'bytes':finance.stat().st_size,'sha256':sha(finance.read_bytes()),'matches_writer_capture':finance.read_bytes()==(ROOT/'../sources/finance-law-2026.pdf').read_bytes(),'read_scope':'PDF page78 visually, arts64-66 and art65 table. No whole-law review claimed.'}]
(OUT/'check-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate_files':len(candidate),'legacy_files':len(legacy),'legacy_topics':result['topic_total'],'commands_passed':len(results),'source_matches':result['source']['matches_writer_capture']}))
