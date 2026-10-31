from pathlib import Path
import runpy,json,re,hashlib,subprocess,os
P=Path(__file__).resolve().parent;R=P.parents[2]
E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'))
guide=R/'skills/international/spain/es-corporate-tax.md'
before=(P/'baseline-current.md').read_text();after=guide.read_text()
checks=[]
def check(name,ok):
 checks.append(dict(name=name,pass_=bool(ok)))
 if not ok:raise AssertionError(name)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
insert=' Add back equity-interest impairment within the categories in art. 15.k, testing its incorporated art. 21 holding/foreign-tax conditions.'
inverse=after.replace(insert,'',1).replace('version: 1.3','version: 1.2',1).replace('# Corporate income tax in Spain v1.3','# Corporate income tax in Spain v1.2',1).replace('last_updated: 2026-10-28','last_updated: 2026-10-25',1)
# Baseline metadata date is read from its actual field, never presumed.
inverse=re.sub(r'(?m)^last_updated: .*$',re.search(r'(?m)^last_updated: .*$',before).group(0),inverse,count=1)
check('Full inverse: only restored sentence plus version/date metadata and H1',inverse==before)
check('Original two executable cases byte-exact',re.findall(r'```oa-check[\s\S]*?```',before)==re.findall(r'```oa-check[\s\S]*?```',after) and len(re.findall(r'```oa-check',after))==2)
check('Protected CTA byte-exact',before.split('<!-- openaccountants-cta-block -->',1)[1]==after.split('<!-- openaccountants-cta-block -->',1)[1])
check('Protected byline byte-exact',next(x for x in before.splitlines() if 'Based on work' in x)==next(x for x in after.splitlines() if 'Based on work' in x))
check('All frozen-PR URL spellings and sequence retained',re.findall(r'https?://[^\s)<>]+',before)==re.findall(r'https?://[^\s)<>]+',after))
rows=json.loads((P/'claim-rows.json').read_text())
for z in rows:check(z['id']+' exact current wording',z['wording'] in after)
for z in json.loads((P/'actual-read-quotes.json').read_text()):
 native=(P/z['reader']).read_text().splitlines()
 check(z['key']+' exact native quoted LF interval',z['quote']=='\n'.join(native[z['LF_start']-1:z['LF_end']]))
for z in json.loads((P/'source-identities.json').read_text()):
 check(z['key']+' raw identity',sha(P/z['raw'])==z['raw_sha256'])
 check(z['key']+' reader identity',sha(P/z['reader'])==z['reader_sha256'])
maps=json.loads((P/'old-topics.json').read_text())
check('No guessed or unmapped old-topic destination',not any(z['destination'].startswith('EXPLICIT TOPIC-MAPPING GAP') for z in maps))
for ref in ['62b7639a5a68324a83a96bb0190fff8b7c76f8c5','0b5e62451de50220ac6d80c7813d547d08108641']:
 old=subprocess.check_output(['git','show',ref+':skills/international/spain/es-corporate-tax.md'],cwd=R,text=True)
 mapped=[z for z in maps if z['ref']==ref]
 check(ref+' every original unit/order retained',[(z['old_lf'],z['section'],z['wording']) for z in mapped]==E['units'](old))
env=dict(os.environ,PYTHONPATH='/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
run=subprocess.run(['python3','scripts/check-examples.py',str(guide)],cwd=R,env=env,text=True,capture_output=True)
(P/'oa-check-result.txt').write_text(run.stdout+run.stderr)
check('Two executable example computations',run.returncode==0)
report=dict(scope='Writer integrity/quote/location/arithmetic controls, not independent legal review or country completion',controls=len(checks),checks=checks,guide_sha256=sha(guide),ledger_sha256=sha(R/'ledgers/es-corporate-tax.md'),oa_output=run.stdout)
(P/'writer-check-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
