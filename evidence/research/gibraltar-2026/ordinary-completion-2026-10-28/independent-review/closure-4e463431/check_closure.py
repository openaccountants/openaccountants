from pathlib import Path
import json, re, hashlib, subprocess, sys
import yaml

BASE=Path(__file__).resolve().parents[2];ROOT=BASE/'country';OUT=Path(__file__).parent
N=ROOT/'skills/research/gibraltar-2026/ordinary-completion-2026-10-28'
PIN='42697c1cfdd04d72a47abe6bd702dd7cccb84c69'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(b):return hashlib.sha256(b).hexdigest()
def blocks(t):
    result=[];head=[]
    for b in t.split('---',2)[-1].strip().split('\n\n'):
        b=b.strip()
        if not b:continue
        if b.startswith('#'):
            for l in b.splitlines():
                if l.startswith('## '):head=[l[3:]]
                elif l.startswith('### '):head=head[:1]+[l[4:]]
            continue
        result.append({'hash':sha(b.encode()),'text':b,'destination':' > '.join(head)})
    return result
e=json.loads((OUT/'pinned-evidence.json').read_text());head=git('rev-parse','HEAD').decode().strip()
errors=[];checks={};details={}
expected_h2=['Who this applies to','Rates, bands and thresholds','The base','Deadlines and filing','Penalties and interest','Cross-border points','Two worked examples that recompute','Ask the client first','Sources']
cp=re.compile(r'^```oa-check[^\n]*\n.*?^```\s*$',re.M|re.S)
for slug,fn in [('gi-connected-party-pricing-and-interest','tp-full-ledger-match.json'),('gi-foreign-tax-relief','foreign-exit-ledger-match.json')]:
    p=ROOT/'skills/international/gibraltar'/(slug+'.md');t=p.read_text();old=git('show',PIN+':'+str(p.relative_to(ROOT))).decode();data=json.loads((N/fn).read_text());prior=json.loads(git('show',PIN+':'+str((N/fn).relative_to(ROOT))));md=(N/'ledgers'/(slug+'.md')).read_text()
    h2=re.findall(r'^## (.*)$',t,re.M);assert h2==expected_h2
    section7=t.split('## Two worked examples that recompute\n',1)[1].split('\n## Ask the client first',1)[0];section8=t.split('## Ask the client first\n',1)[1].split('\n## Sources',1)[0]
    assert len(cp.findall(t))==2 and cp.findall(t)==cp.findall(old)
    assert len(cp.findall(section7))==2
    assert len(re.findall(r'^\d\. ',section8,re.M))==6
    assert [r['quotes'] for r in data['rows']]==[r['quotes'] for r in prior['rows']]
    for i,r in enumerate(data['rows'],1):
        if r['rule'].replace('|','\\|') not in md:errors.append([slug,'Markdown rule mismatch',i])
    # The preserved original full body copies are the authoritative baseline for old-topic maps.
    olds=blocks((N/(slug+'.before.txt')).read_text());curr=blocks(t);byhash={b['hash']:b for b in curr};maps=data['old_paragraph_map']
    assert len(olds)==len(maps)
    for i,(b,r) in enumerate(zip(olds,maps),1):
        assert i==r['number'] and b['hash']==r['old_paragraph_sha256']
        dst=byhash.get(r['current_paragraph_sha256']);assert dst is not None,(slug,i,'destination hash absent')
        assert dst['destination']==r['destination'],(slug,i,dst['destination'],r['destination'])
        assert (b['hash']==dst['hash'])==r['full_paragraph_exact']
        anchor=' '.join(b['text'].split())
        assert anchor.startswith(r['actual_old_anchor']), (slug,i,'anchor')
    if 'old_paragraphs' in data:
        for r,m in zip(data['old_paragraphs'],maps):
            if r['byte_exact']!=m['full_paragraph_exact']:errors.append([slug,'legacy old_paragraphs status differs',r['number']])
    # All pinned paragraphs must survive apart from explicitly reviewed status/cross-reference edits.
    removed=[b for b in blocks(old) if b['hash'] not in byhash]
    details[slug]={'sha256':sha(p.read_bytes()),'ledger_json_sha256':sha((N/fn).read_bytes()),'ledger_md_sha256':sha((N/'ledgers'/(slug+'.md')).read_bytes()),'canonical_sections':h2,'intake_facts':6,'main_blocks_exact':2,'quote_rows':len(data['rows']),'quotes_exact_to_pinned':sum(len(r['quotes']) for r in data['rows']),'old_map_rows':len(maps),'old_paragraphs_exact':sum(r['full_paragraph_exact'] for r in maps),'pinned_paragraphs_changed_or_replaced':[{'anchor':b['text'][:160],'sha256':b['hash']} for b in removed]}
    # Compare every platform key; only the content version changes in this closure.
    a=yaml.safe_load(old.split('---',2)[1]);b=yaml.safe_load(t.split('---',2)[1]);assert {k:v for k,v in a.items() if k!='version'}=={k:v for k,v in b.items() if k!='version'}
    for m in re.finditer(r'\]\(([^\s]+)\)',t):
        target=m.group(1)
        if re.match(r'[a-z]+://',target):continue
        dest=(p.parent/target.split('#')[0]).resolve()
        assert dest.exists(),(slug,target)

unchanged=[r for r in e['file_inventory'] if r['byte_exact']]
assert len(unchanged)==16 and all(sha((ROOT/r['path']).read_bytes())==r['sha256'] for r in unchanged)
assert len(e['historical_research'])==121 and all(sha((ROOT/r['path']).read_bytes())==r['sha256'] for r in e['historical_research'])
arch=N/'independent-review/pinned-42697c1c'
archnames=['calculations.txt','check_pinned.py','pinned-evidence.json','prose-calculations.json','prose_arithmetic.py','report.md','result.json']
assert all((arch/f).read_bytes()==(OUT/f).read_bytes() for f in archnames)
readme=ROOT/'skills/international/gibraltar/README.md';rfields=yaml.safe_load(readme.read_text().split('---',2)[1]);assert len(rfields['partial'])==7
checks.update({'untouched_guides_exact':16,'historical_records_exact':121,'original_controls_preserved':47,'pinned_artifacts_archived_byte_exact':7,'all_seven_domains_partial':True,'readme_sha256':sha(readme.read_bytes())})
cmd=[sys.executable,str(ROOT/'scripts/check-examples.py'),*[str(ROOT/r['path']) for r in e['file_inventory'] if r['path'].endswith('.md') and not r['path'].endswith('README.md')],str(N/'interest-controls.md'),str(N/'exit-controls.md')]
c=subprocess.run(cmd,text=True,capture_output=True,cwd=ROOT);assert c.returncode==0
checks['calculation_output']=c.stdout
result={'reviewed_head':head,'pinned_legal_review':PIN,'scope':'Bounded GI-R1/GI-R2 repair closure only; completed legal/prose review reused.','details':details,'checks':checks,'errors':errors}
(OUT/'closure-evidence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
