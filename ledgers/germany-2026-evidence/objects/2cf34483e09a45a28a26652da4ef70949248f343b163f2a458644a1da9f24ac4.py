from pathlib import Path
import json,re,hashlib,subprocess
P=Path(__file__).resolve().parent
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany')
REF='62b7639a5a68324a83a96bb0190fff8b7c76f8c5'
sha=lambda b:hashlib.sha256(b).hexdigest()
def units(body):
 sec='';meta=True
 for i,l in enumerate(body.split('\n'),1):
  if i==1:continue
  if meta:
   if l=='---':meta=False
   continue
  if '<!-- openaccountants-cta-block -->'in l:break
  if l.startswith('#'):sec=l.lstrip('# ');continue
  if l.strip()and l!='---'and not re.fullmatch(r'\|[-:| ]+\|',l):yield dict(lf=i,section=sec,wording=l)
def bank():return {json.loads(f.read_text())['id']:json.loads(f.read_text())for f in(P/'sources').glob('*.identity.json')}
def take(A,k,so,lo,hi,art,quote=None):
 I=bank();z=I[so];ls=Path(z['reader_path']).read_text().split('\n');q=quote or'\n'.join(ls[lo-1:hi]);assert q and q in'\n'.join(ls[lo-1:hi]),(k,lo,hi)
 A[k]=dict(id=k,source=so,article=art,url=z['url'],LF_start=lo,LF_end=hi,exact_quote=q,raw_sha256=z['raw_sha256'],reader_sha256=z['reader_sha256'],read_on='2026-10-29',line_convention="literal LF split('\\n')")
def write(slug,raw,rows,A,old,C,notes):
 S=P/'support'/slug;S.mkdir(parents=True,exist_ok=True)
 for n,v in [('claim-rows.json',rows),('actual-read-quotes.json',list(A.values())),('old-topics.json',old),('supplementary-controls.json',C)]: (S/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
 def esc(v):return str(v).replace('|','\\|').replace('\n','<br>')
 out=['# Figure/rule ledger: '+slug,'',f'Guide SHA256 `{sha(raw)}`; actual public-main comparator `{REF}`. Private writer evidence, not independent review. Current nonblank units and their exact wording are retained. Dates below are actual selected-clause reads, not acquisition dates or inherited Guide source dates.','','| Guide LF | Section | Exact current wording | Official act/article and URL | Exact original-language quote / computed classification | Read date |','|---|---|---|---|---|---|']
 for z in rows:
  a=[A[k]for k in z['anchors']];cite='<br>'.join(x['article']+' '+x['url']for x in a)or'—';q='<br>'.join(x['exact_quote']for x in a)or z['kind']
  if z['kind'].startswith('computed'):q='Declared fictional input or computed arithmetic, not an official numerical quotation. Source parameters: '+', '.join(x['article']for x in a)
  if z.get('evidence_note'):q+='<br>Exact evidence limit: '+z['evidence_note']
  out.append('| '+' | '.join(esc(v)for v in [z['lf'],z['section'],z['wording'],cite,q,'2026-10-29'if a else'—'])+' |')
 out+=['','## Complete old-topic destinations','','Every actual old nonblank unit is retained below. Exact wording is distinguished from corrected law, historical examples and specific unverified assertions; no separately verified platform body is invented.','','| Actual comparator / LF | Exact old unit | Verified destination or precise historical limit |','|---|---|---|']
 for z in old:out.append('| '+' | '.join(esc(v)for v in [z['ref'][:12]+':'+str(z['old_lf']),z['wording'],z['destination']])+' |')
 out+=['','## Writer checks and limits','',notes,'']
 f=P/'ledgers'/(slug+'.md');f.write_text('\n'.join(out))
 I=bank();integrity=[]
 for so in sorted(set(x['source']for x in A.values())):
  z=I[so];a=sha(Path(z['raw_path']).read_bytes());b=sha(Path(z['reader_path']).read_bytes());assert(a,b)==(z['raw_sha256'],z['reader_sha256']);integrity.append(dict(source=so,raw_sha256=a,reader_sha256=b))
 (S/'source-integrity.json').write_text(json.dumps(integrity,indent=2)+'\n')
 checks=dict(guide_sha256=sha(raw),ledger_sha256=sha(f.read_bytes()),current_units=len(rows),source_anchors=len(A),old_units=len(old),controls=len(C),unclassified=[z['lf']for z in rows if z['kind']=='UNCLASSIFIED'],pending_old=[(z['ref'],z['old_lf'])for z in old if z['destination'].startswith('PENDING')],all_quotes_native_exact=all(x['exact_quote']in'\n'.join(Path(I[x['source']]['reader_path']).read_text().split('\n')[x['LF_start']-1:x['LF_end']])for x in A.values()),guide_unchanged=(R/('skills/international/germany/'+slug+'.md')).read_bytes()==raw)
 (S/'writer-checks.json').write_text(json.dumps(checks,indent=2)+'\n');print(checks)
