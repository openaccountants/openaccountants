from pathlib import Path
import json,hashlib,re,subprocess
O=Path(__file__).resolve().parent
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany')
H=Path('/Users/michaelcutajar/Downloads/oa-f1-wt/wt-rev-903')
DATE='2026-10-29'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def lf(p):return Path(p).read_text().split('\n')
def ws(x):return ' '.join(x.split())
C=json.loads((O/'source-candidate-catalog.json').read_text())
BYID={v['source_id']:v for v in C.values()}
QP=O/'actual-read-quotes.json';Q=json.loads(QP.read_text()) if QP.exists() else {}
def quote(key,sid,lo,hi=None,article='',fragment=None,read_ranges=None,note=''):
 s=BYID[f'DEB{sid:03d}' if isinstance(sid,int) else sid];lines=lf(s['reader_path']);hi=hi or lo;context='\n'.join(lines[lo-1:hi]);assert context.strip();q=fragment or context
 assert q in context,(key,q[:70])
 Q[key]={'source_id':s['source_id'],'act_article':article,'official_url':s['official_url'],'raw_path':s['path'],'raw_sha256':s['sha256'],'reader_path':s['reader_path'],'reader_sha256':s['reader_sha256'],'native_LF':[lo,hi],'exact_quote':q,'read_on':DATE,'actual_read_scope':read_ranges or [[lo,hi]],'read_mode':'Selected operative text actually read by this writer; no whole-body acquisition/read inference. Literal extracted text; HTML block whitespace normalization identified in candidate catalog.','note':note}
 assert sha(s['path'])==s['sha256'];assert sha(s['reader_path'])==s['reader_sha256']
 QP.write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
def line(sid,n):return lf(BYID[f'DEB{sid:03d}']['reader_path'])[n-1]
def first(sid,n,count=1):
 s=line(sid,n);pieces=re.split(r'(?<=\.) (?=\d?[A-ZÄÖÜ])',s);return ' '.join(pieces[:count])
def render_quotes():
 out=['# Germany B: actual selected official quotations','',f'Writer readings {DATE}. Shared retained raw bodies are linked by exact hash and absolute paths in actual-read-quotes.json; acquisition candidates alone are not actual reads. This is not an independent review.','']
 for k,q in Q.items():
  out += [f'<a id="{k.lower().replace(".","-")}"></a>','',f'## {k}','',f'{q["act_article"]}; [official source]({q["official_url"]}); read {q["read_on"]}; reader native LF{q["native_LF"]}. Raw SHA256 `{q["raw_sha256"]}`, reader SHA256 `{q["reader_sha256"]}`.','', '> '+q['exact_quote'].replace('\n','\n> '),'',q['note'],'']
 (O/'source-quotes.md').write_text('\n'.join(out)+'\n')
def render(slug,rows,oldtext='Old-topic table in preparation; not review-ready.'):
 p=R/f'skills/international/germany/{slug}.md';ls=lf(p);out=[f'# {slug}: figure and rule ledger','',f'Writer evidence; Guide SHA256 `{sha(p)}`. Guide unchanged by this writer. Original-language quotations and actual reads resolve in [source-quotes.md](../source-quotes.md), with raw/reader hashes in actual-read-quotes.json. Stipulated inputs and computed outputs are distinguished from law.','', '| ID | Guide section / native LF | Exact wording | Source / qualification |','|---|---|---|---|'];mr=[]
 for i,(lo,hi,refs,kind) in enumerate(rows,1):
  text='\n'.join(ls[lo-1:hi]);sect=[x[3:] for x in ls[:lo] if x.startswith('## ')];section=sect[-1] if sect else 'Scope/metadata';assert text.strip()
  for ref in refs:assert ref in Q,ref
  wording=text.replace('|','\\|').replace('\n','<br>');sources=', '.join(f'[{q}](../source-quotes.md#{q.lower().replace(".","-")})' for q in refs)
  out.append(f'| {i:03d} | {section}, LF{lo}'+(f'–{hi}' if hi!=lo else '')+f' | {wording} | {sources}. {kind} |');mr.append({'row':i,'LF_start':lo,'LF_end':hi,'section':section,'wording':text,'source_quote_ids':refs,'classification':kind})
 out+=['','## Old topics carried','',oldtext,''];d=O/'ledgers';d.mkdir(exist_ok=True);(d/(slug+'.md')).write_text('\n'.join(out));d=O/'support'/slug;d.mkdir(parents=True,exist_ok=True);(d/'rows.json').write_text(json.dumps(mr,ensure_ascii=False,indent=2)+'\n');render_quotes()
