from writer import *
PRIOR=json.loads((ARCH/'final-full-pack-review/full-no-loss-unit-ledger.json').read_text())
def units(text):
    # Blank-separated blocks, retaining entire fenced examples and metadata as one unit.
    out=[];buf=[];start=1;fence=False;front=False
    for i,line in enumerate(text.split('\n'),1):
        if i==1 and line=='---':front=True
        elif front and line=='---':front=False
        if line.startswith('```'):fence=not fence
        if not line.strip() and not fence and not front:
            if buf:out.append((start,i-1,'\n'.join(buf)));buf=[]
        else:
            if not buf:start=i
            buf.append(line)
    if buf:out.append((start,i,'\n'.join(buf)))
    return out

def table(slug, overrides=None, earliest=None):
    overrides=overrides or {};path=f'skills/international/slovakia/{slug}.md'
    raw=subprocess.check_output(['git','show','origin/main:'+path],cwd=REPO)
    current=(REPO/path).read_text();gl=current.split('\n')
    prior={r['baseline_text']:r for r in PRIOR if r['file']==slug+'.md'}
    rows=[]
    def locate(text):
        pos=current.find(text)
        if pos<0:return None
        return [current.count('\n',0,pos)+1,current.count('\n',0,pos+len(text))+1]
    for n,(lo,hi,txt) in enumerate(units(raw.decode()),1):
        dest=locate(txt);disposition='Exact retained unit; all embedded topics preserved.'
        if dest is None:
            p=prior.get(txt)
            if n in overrides:dest,disposition=overrides[n]
            elif p and locate(p['closest_final_text']):
                dest=locate(p['closest_final_text']);disposition='Rechecked current destination; prior 423-unit review disposition: '+p['disposition']
            else:
                raise RuntimeError((slug,n,txt[:120]))
        rows.append({'comparator':'origin/main','unit':n,'old_LF_start':lo,'old_LF_end':hi,'old_text':txt,'old_unit_sha256':hashlib.sha256(txt.encode()).hexdigest(),'current_LF':dest,'disposition':disposition})
    # The earliest TP/XB rewrite preimage has no file; other Guides have separately mapped early bodies.
    original={'revision':earliest,'present':False}
    if earliest:
        r=subprocess.run(['git','show',earliest+':'+path],cwd=REPO,capture_output=True)
        original['present']=r.returncode==0
        if r.returncode==0:original.update({'bytes':len(r.stdout),'sha256':hashlib.sha256(r.stdout).hexdigest()})
    d=EVID/slug;d.mkdir(exist_ok=True)
    data={'guide_sha256':sha(REPO/path),'main_revision':subprocess.check_output(['git','rev-parse','origin/main'],cwd=REPO,text=True).strip(),'main_bytes':len(raw),'main_sha256':hashlib.sha256(raw).hexdigest(),'earliest_preimage':original,'prior_423_unit_map_path':str(ARCH/'final-full-pack-review/full-no-loss-unit-ledger.json'),'prior_map_sha256':sha(ARCH/'final-full-pack-review/full-no-loss-unit-ledger.json'),'rows':rows}
    (d/'old-topics.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    out=[f'Main comparator `{data["main_revision"]}`, SHA256 `{data["main_sha256"]}`. Each old block below includes all its table rows, bullets or worked-example fields; full text and unit hashes are in [old-topics.json](slovakia-2026-evidence/'+slug+'/old-topics.json).', '']
    if earliest and not original['present']:out += [f'Earliest rewrite preimage `{earliest}`: this Guide did not exist. There are no earlier topics to route; the failed read-only lookup is recorded as absence, not omitted review.','']
    out += ['| Old unit / native LF | Old topic / exact opening | Current destination | Disposition |','|---|---|---|---|']
    for r in rows:
        preview=ws(r['old_text'])[:210].replace('|','\\|')
        out.append(f'| M{r["unit"]:03d}, LF {r["old_LF_start"]}–{r["old_LF_end"]} | {preview} | Current LF {r["current_LF"][0]}–{r["current_LF"][1]} | {r["disposition"]} |')
    return '\n'.join(out)

def early_table(slug,revision,mapping):
    path=f'skills/international/slovakia/{slug}.md';raw=subprocess.check_output(['git','show',revision+':'+path],cwd=REPO)
    datafile=EVID/slug/'old-topics.json';d=json.loads(datafile.read_text());rows=[]
    blocks=units(raw.decode())
    assert len(mapping)==len(blocks),(slug,len(mapping),len(blocks))
    for n,(lo,hi,txt) in enumerate(blocks,1):
        dest,why=mapping[n]
        rows.append({'comparator':revision,'unit':n,'old_LF_start':lo,'old_LF_end':hi,'old_text':txt,'old_unit_sha256':hashlib.sha256(txt.encode()).hexdigest(),'current_destination':dest,'disposition':why})
    d['earliest_preimage'].update({'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'complete_old_units':len(rows),'rows':rows})
    datafile.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    out=['','### Earliest rewrite preimage destinations','',f'Comparator `{revision}`, SHA256 `{d["earliest_preimage"]["sha256"]}`; {len(rows)} complete old units. Original body remains unchanged in the preserved review archive and is independently identified above. Old rates are historical text, not revived law.','', '| Old unit / native LF | Exact old opening | Current destination | Disposition |','|---|---|---|---|']
    for r in rows:out.append(f'| E{r["unit"]:03d}, LF {r["old_LF_start"]}–{r["old_LF_end"]} | {ws(r["old_text"])[:180].replace("|","\\|")} | {r["current_destination"]} | {r["disposition"]} |')
    return '\n'.join(out)
