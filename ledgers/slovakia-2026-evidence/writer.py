from pathlib import Path
import json,hashlib,re,subprocess
REPO=Path(__file__).resolve().parents[2]
EVID=Path(__file__).resolve().parent
ARCH=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/sk-whole-pack-review')
DATE='2026-10-29'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def lf(p):return Path(p).read_text().split('\n')
def ws(s):return ' '.join(s.split())
receipts=json.loads((ARCH/'consolidated-source-manifest.json').read_text())
receipts={str(x['id']):x for x in receipts if x.get('file')}
CAT=EVID/'source-scopes.json'
scopes=json.loads(CAT.read_text()) if CAT.exists() else {}
def scope(key,sid,reader,start,end,article,quote_ranges=None,note=''):
    reader=Path(reader)
    if not reader.is_absolute():reader=ARCH/reader
    lines=lf(reader)
    assert 1<=start<=end<=len(lines),(key,start,end,len(lines))
    receipt=receipts[str(sid)]
    raw=Path(receipt['file']);assert sha(raw)==receipt['sha256']
    quotes=[]
    for lo,hi in quote_ranges or [(start,end)]:
        assert start<=lo<=hi<=end
        quote=ws('\n'.join(lines[lo-1:hi]));assert quote
        quotes.append({'LF_start':lo,'LF_end':hi,'quote':quote})
    scopes[key]={'source_id':str(sid),'article':article,'official_url':receipt['url'],'raw_path':str(raw),'raw_sha256':sha(raw),'reader_path':str(reader),'reader_sha256':sha(reader),'actual_read_LF_start':start,'actual_read_LF_end':end,'quotations':quotes,'read_date':scopes.get(key,{}).get('read_date',DATE),'read_mode':'Selected retained primary reader actually read by this writer; full body not asserted read. Whitespace joined only in quotations.','note':note}
    CAT.write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
    return key

def section(key,sid,article,start=1,end=None,quotes=None,note=''):
    p=ARCH/f'final-full-pack-review/sections/{sid}-{article}.txt'
    return scope(key,sid,p,start,end or len(lf(p))-1,f'§ {article}',quotes,note)

def render(slug,entries,oldmap):
    guide=REPO/f'skills/international/slovakia/{slug}.md'; gl=lf(guide)
    out=[f'# {slug}: figure and rule ledger', '', f'Writer evidence, read {DATE}. Guide SHA256 `{sha(guide)}` ({guide.stat().st_size} bytes). No Guide edits or independent-review verdict. References below identify actual selected reads, not merely downloaded bodies. Derived case inputs are stipulated and outputs are computed, not statutory figures. Native LF means splitting the identified reader on `\\n`; quote whitespace is joined only.', '', '## Figure and rule rows', '', '| ID | Guide section and native LF | Exact Guide wording | Basis / qualification |', '|---|---|---|---|']
    used=set(); covered=set(); sectionname='Metadata'; manifest=[]
    for n,(lo,hi,refs,kind) in enumerate(entries,1):
        assert lo<=hi
        text='\n'.join(gl[lo-1:hi]); assert text.strip(),(slug,lo,hi)
        for r in refs:assert r in scopes,r
        used.update(refs); covered.update(range(lo,hi+1))
        sname=' / '.join(x.lstrip('# ') for x in gl[:lo] if x.startswith('## '))
        sname=sname.split(' / ')[-1] if sname else 'Scope / metadata'
        wording=text.replace('|','\\|').replace('\n','<br>')
        basis=', '.join(f'[{r}](slovakia-2026-evidence/source-quotes.md#{r.lower().replace(".","-")})' for r in refs)
        out.append(f'| {n:03d} | {sname}, LF {lo}'+(f'–{hi}' if hi!=lo else '')+f' | {wording} | {basis}. {kind} |')
        manifest.append({'row':n,'LF_start':lo,'LF_end':hi,'guide_wording':text,'source_scopes':refs,'classification':kind})
    out+=['','## Source identities and actual reads','','Sources are shared to avoid duplicating official bodies across seven ledgers. Each source ID below resolves to the act/article, official URL, short exact original-language excerpts, native reader lines, raw and reader hashes, and actual read date in [the quotation catalog](slovakia-2026-evidence/source-quotes.md). The machine-readable [source-scope ledger](slovakia-2026-evidence/source-scopes.json) retains the exact local originals.','',', '.join(f'`{x}`' for x in sorted(used)), '', '## Complete old-topic destinations','','The comparator map distinguishes unchanged content, supported corrections, historical-only material and new topics. It does not revive unsupported old figures. See the retained 423-unit prior review only as attributed evidence; this writer’s current destination coordinates and comparator hashes are separately recorded below.','',oldmap]
    (REPO/f'ledgers/{slug}.md').write_text('\n'.join(out)+'\n')
    d=EVID/slug;d.mkdir(exist_ok=True)
    (d/'rows.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    (d/'coverage.json').write_text(json.dumps({'guide_sha256':sha(guide),'covered_native_LF':sorted(covered),'entries':len(entries),'source_scopes':sorted(used)},indent=2)+'\n')

def render_sources():
    out=['# Slovakia retained primary quotations','',f'Actual selected-read dates appear per entry; this catalog rendered {DATE}. No whole-body read is implied. Original-language text is verbatim except joined whitespace; multiple quotations are explicitly separated. Raw bodies remain in the preserved archive, identified by absolute paths and hashes in source-scopes.json. This catalog is writer evidence, not an independent verdict.','']
    for k,s in sorted(scopes.items()):
        out += [f'<a id="{k.lower().replace(chr(46),chr(45))}"></a>', '', f'## {k}', '', f'{s["article"]}. [Official source]({s["official_url"]}). Read {s["read_date"]}; reader actual native LF ranges {s.get("actual_read_ranges", [[s["actual_read_LF_start"], s["actual_read_LF_end"]]])}. Raw SHA256 `{s["raw_sha256"]}`; reader SHA256 `{s["reader_sha256"]}`.', '']
        for q in s['quotations']:out += [f'LF {q["LF_start"]}–{q["LF_end"]}:', '> '+q['quote'], '']
        if s['note']:out += [s['note'],'']
    (EVID/'source-quotes.md').write_text('\n'.join(out)+'\n')
