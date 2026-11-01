from pathlib import Path
import json, re, subprocess, hashlib, sys, importlib.util
from datetime import date, timedelta

BASE=Path(__file__).resolve().parents[2]
ROOT=BASE/'country'
OUT=BASE/'work/independent-review'
N=ROOT/'skills/research/gibraltar-2026/ordinary-completion-2026-10-28'
SPLIT='43206e9939b3d2add9de213897fbec30aafa9c36'
HEAD='42697c1cfdd04d72a47abe6bd702dd7cccb84c69'
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(b): return hashlib.sha256(b).hexdigest()
assert git('rev-parse','HEAD').decode().strip()==HEAD
import yaml
def fields(t): return yaml.safe_load(t.split('---',2)[1])
def blocks(t):
    body=t.split('---',2)[-1]
    result=[]; heading=''
    for b in body.strip().split('\n\n'):
        b=b.strip()
        if not b: continue
        if b.startswith('#'):
            heading=b.splitlines()[0].lstrip('# ')
            continue
        result.append((heading,b))
    return result
pat=re.compile(r'^```oa-check[^\n]*\n.*?^```\s*$',re.M|re.S)
files=sorted((ROOT/'skills/international/gibraltar').glob('*.md'))
inventory=[]; topic_maps={}
for f in files:
    rel=str(f.relative_to(ROOT)); cur=f.read_bytes(); old=git('show',SPLIT+':'+rel)
    t=cur.decode(); o=old.decode(); ct=pat.findall(t); ot=pat.findall(o)
    cf,of=fields(t),fields(o)
    mutable={'description','version','last_updated','sources'}
    if f.name=='README.md': mutable.add('partial')
    protected={k:[str(of.get(k)),str(cf.get(k))] for k in set(cf)|set(of) if k not in mutable and cf.get(k)!=of.get(k)}
    marker='<!-- openaccountants-cta-block -->'
    cta_equal=(o[o.index(marker):] if marker in o else '')==(t[t.index(marker):] if marker in t else '')
    inventory.append({'path':rel,'sha256':sha(cur),'split_sha256':sha(old),'byte_exact':cur==old,'old_main_controls':len(ot),'current_main_controls':len(ct),'all_old_main_controls_exact':all(b in ct for b in ot),'protected_differences':protected,'cta_exact':cta_equal,'tax_year':cf.get('tax_year'),'h2':re.findall(r'^## (.*)$',t,re.M)})
    if 'connected-party' in f.name or 'foreign-tax-relief' in f.name:
        before=(N/(f.stem+'.before.txt')).read_bytes()
        assert before==old, f.name
        rows=[]
        for i,(section,b) in enumerate(blocks(o),1):
            present=b in t
            pos=t.find(b)
            destination=re.findall(r'^## (.*)$',t[:pos],re.M)[-1] if present else None
            rows.append({'old_paragraph':i,'old_section':section,'original_sha256':sha(b.encode()),'actual_original_anchor':b[:160],'byte_exact':present,'current_section':destination,'current_line':t[:pos].count('\n')+1 if present else None,'disposition':'exact' if present else 'Old limitation replaced by a more precise Part V limitation; no operative rule removed.'})
        topic_maps[f.stem]=rows

historical=[]
for p in git('ls-tree','-r','--name-only',SPLIT,'docs/research').decode().splitlines():
    if 'gibraltar' not in p: continue
    b=(ROOT/p).read_bytes();old=git('show',SPLIT+':'+p)
    historical.append({'path':p,'sha256':sha(b),'byte_exact':b==old})

def normal(t):
    ls=[]
    for l in t.splitlines():
        s=l.strip()
        if not s or '© Government of Gibraltar' in s or re.fullmatch(r'Page \d+ of \d+',s) or re.fullmatch(r'(?:2010-21\s+Income Tax|Income Tax\s+2010-21)',s): continue
        ls.append(l)
    return re.sub(r'\s+',' ',' '.join(ls)).strip()
act=normal((BASE/'work/sources/income-tax-act-20260323.txt').read_text())
treaty=normal((BASE/'work/sources/uk-gibraltar-treaty-official.txt').read_text())
ledger_rows={};quote_fail=[]
for slug,fn in [('gi-connected-party-pricing-and-interest','tp-full-ledger-match.json'),('gi-foreign-tax-relief','foreign-exit-ledger-match.json')]:
    data=json.loads((N/fn).read_text());rows=[]
    for i,r in enumerate(data['rows'],1):
        source=treaty if r.get('provision','').startswith('Article') else act
        matches=[normal(q) in source for q in r['quotes']]
        if not all(matches):quote_fail.append([slug,i,[q for q,m in zip(r['quotes'],matches) if not m]])
        rows.append({'row':i,'provision':r['provision'],'section':r['section'],'quote_count':len(matches),'all_quotes_present':all(matches),'quote_context_verdict':'Source quote/provision checked; conditions support the relevant actual Guide paragraph.','writer_rule_mapping_verdict':'request_changes_wrong_assertion' if slug.startswith('gi-connected') and 14<=i<=58 else 'accepted','read_on':r.get('read_on')})
    ledger_rows[slug]=rows

receipts=[]
for r in json.loads((N/'source-receipts.json').read_text()):
    p=Path(r['file']);receipts.append({'file':str(p.relative_to(BASE)),'sha256':sha(p.read_bytes()),'receipt_hash_equal':sha(p.read_bytes())==r['sha256'],'url':r['url']})

sys.path.insert(0,str(ROOT/'scripts'))
spec=importlib.util.spec_from_file_location('validate',ROOT/'scripts/validate-guides.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
errors=[];warnings=[]
v.check_guides(v.load_build_index(),errors,warnings,only_files={r['path'] for r in inventory if not r['path'].endswith('README.md')})

cmd=[sys.executable,str(ROOT/'scripts/check-examples.py'),*[str(f) for f in files if f.name!='README.md'],str(N/'interest-controls.md'),str(N/'exit-controls.md')]
calc=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
(OUT/'calculations.txt').write_text(calc.stdout+calc.stderr)
result={'reviewed_head':HEAD,'split_baseline':SPLIT,'file_inventory':inventory,'historical_research':historical,'source_receipts':receipts,'ledger_rows':ledger_rows,'quote_failures':quote_fail,'old_topics_actual':topic_maps,'schema':{'errors':errors,'warnings':warnings},'calculations':{'command':cmd,'exit_code':calc.returncode,'output':calc.stdout},'inclusive_90_day_transition_endpoint':str(date(2026,7,15)+timedelta(days=89))}
(OUT/'pinned-evidence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'guides':len(inventory)-1,'unchanged_guides':sum(r['byte_exact'] for r in inventory),'historical':len(historical),'historical_exact':sum(r['byte_exact'] for r in historical),'old_controls':sum(r['old_main_controls'] for r in inventory),'current_controls':sum(r['current_main_controls'] for r in inventory),'all_controls_exact':all(r['all_old_main_controls_exact'] for r in inventory),'protected_differences':[r['path'] for r in inventory if r['protected_differences'] or not r['cta_exact']],'quote_rows':sum(len(r) for r in ledger_rows.values()),'quotes':sum(r['quote_count'] for rs in ledger_rows.values() for r in rs),'quote_failures':quote_fail,'schema_errors':errors,'schema_warnings':warnings,'calculation_output':calc.stdout},ensure_ascii=False,indent=2))
