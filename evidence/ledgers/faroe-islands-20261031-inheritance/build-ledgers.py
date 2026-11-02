from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent;S=E/'sources'
# Court HTTP captures are preserved verbatim web-tool responses; these reader derivatives
# retain each original publisher line number. They are not labelled raw HTML downloads.
court={}
for f in sorted(S.glob('court-guidance-web-*.txt')):
 for n,t in re.findall(r'^L(\d+): (.*)$',f.read_text(),re.M):court[int(n)]=t
(S/'court.reader.txt').write_text('\n'.join(f'L{n}: {court[n]}' for n in sorted(court) if 382<=n<=611)+'\n')
for name,out in [('opening-d03-web','opening.reader.txt'),('closing-form-web','closing.reader.txt')]:
 (S/out).write_text('\n'.join(f'L{n}: {t}' for n,t in re.findall(r'^L(\d+)(?:@P\d+(?:-\d+)?)?: (.*)$',(S/(name+'.txt')).read_text(),re.M))+'\n')
URL={'duty':'https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa','tax':'https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt','rates':'https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170','capital':'https://logir.fo/Logtingslog/164-fra-21-12-2001-um-skatting-av-kapitalvinningi-sum-seinast-broytt-vid-logtingslog-nr-173','court':'https://domstoldk.euwest01.umbraco.io/fo/faeroeerne/brug-retten/','opening':'https://domstoldk.euwest01.umbraco.io/media/tfjl4r3d/d03-uppger%C3%B0-yvir-ogn-og-skuld-vi%C3%B0-dey%C3%B0a-sambaert-14-%C3%AD-skattal%C3%B3gini-241023.pdf','closing':'https://domstoldk.euwest01.umbraco.io/media/1ndp1gcb/b%C3%BAuppger%C3%B0-14-uppger%C3%B0.pdf','guidance':'https://www.taks.fo/fo/log/vegleidingarskriv-vls-2015/g-deydsbugv','return':'https://www.taks.fo/fo/vinna/sjalvuppgava-2025/sjalvuppgava','calendar':'https://www.taks.fo/fo/taks/taks-kalendarin/freist-at-lata-inn-sjalvuppgavu-2025-hja-feloegum'}
FILE={k:k+'.reader.txt' for k in URL};FILE.update(capital='capital-correct.reader.txt',return_='estate-return.reader.txt',calendar='estate-calendar.reader.txt');FILE['return']='estate-return.reader.txt';FILE['guidance']='estate-guidance.reader.txt'
texts={k:(S/FILE[k]).read_text() for k in URL}
def article(key,num,sub=None):
 t=texts[key];m=re.search(r'^§ '+str(num)+r'\. [^\n]+',t,re.M)
 if not m:raise ValueError((key,num))
 end=re.search(r'^§ \d+(?: [a-z])?\. ',t[m.end():],re.M);q=t[m.start():m.end()+end.start() if end else len(t)].rstrip()
 if sub is not None:
  if sub==1:q=q.split('\nStk. 2.')[0]
  else:
   n=re.search(r'^Stk\. '+str(sub)+r'\. ',q,re.M)
   if not n:raise ValueError((key,num,sub))
   nxt=re.search(r'^Stk\. \d+\. ',q[n.end():],re.M);q=q[n.start():n.end()+nxt.start() if nxt else len(q)]
 return q.strip()
def selectnums(label):
 if '§' not in label:return []
 tail=label[label.index('§'):].lstrip('§ ');result=[];last=None
 for part in re.split(r',\s*',tail):
  part=part.strip()
  ma=re.match(r'(\d+)\((\d+)\)\s*[–-]\s*\((\d+)\)',part)
  if ma:
   last=int(ma[1]);result.extend((last,n) for n in range(int(ma[2]),int(ma[3])+1));continue
  ma=re.match(r'\((\d+)\)',part)
  if ma:
   assert last is not None;result.append((last,int(ma[1])));continue
  ma=re.match(r'(\d+)\s*[–-]\s*(\d+)',part)
  if ma:
   result.extend((n,None) for n in range(int(ma[1]),int(ma[2])+1));last=int(ma[2]);continue
  ma=re.match(r'(\d+)(?:\((\d+)\))?',part)
  if ma:last=int(ma[1]);result.append((last,int(ma[2]) if ma[2] else None))
 return result
court_ranges={'opening/private-administration sections':[(383,398),(449,475)],'insurance section':[(562,602)],'inventories':[(477,499)],'approval/invoice':[(493,499)]}
def source(key,label):
 if key in ['duty','tax','rates','capital']:
  nums=selectnums(label)
  if not nums:raise ValueError(('NO ARTICLE',key,label))
  q='\n\n'.join(article(key,n,sub) for n,sub in nums)
 elif key=='court':
  ranges=next((v for k,v in court_ranges.items() if k in label),[(382,611)])
  q='\n\n'.join('\n'.join(t for n,t in sorted(court.items()) if a<=n<=b) for a,b in ranges)
 elif key=='guidance':
  t=texts[key];m=t.index('Nettoinntøkan skal roknast');q=t[m:t.index('G.2.2.',m)]
 elif key in ['opening','closing']:q=texts[key]
 elif key=='calendar':
  t=texts[key];a=t.index('01. juli 2026');q=t[a:t.index('Samband',a)]
 elif key=='return':
  t=texts[key];a=t.index('Sjálvuppgáva hjá feløgum');q=t[a:t.index('Samband',a)]
 else:raise ValueError(key)
 assert q.strip()
 return dict(act_article=label,url=URL[key],read_date='2026-10-31',source_file='sources/'+FILE[key],original_language_quote=q,kind='statute' if key in ['duty','tax','rates','capital'] else 'official-authority')
records={}
for slug,prefix in [('fo-inheritance-duty','IH'),('fo-estate-income-tax','ET')]:
 s=(R/'skills/faroe-islands'/f'{slug}.md').read_text().split('---',2)[2];s=re.sub(r'```oa-check\n.*?\n```','',s,flags=re.S)
 section=None;blocks=[]
 for p in s.split('\n\n'):
  p=p.strip()
  if p.startswith('## '):section=p[3:];continue
  if not p or p.startswith(('#','>','[','Not yet confirmed:','OpenAccountants')) or section in ['Ask the client first','Sources'] or section is None:continue
  if p.startswith('|'):
   chunks=[x for x in p.splitlines()[2:] if x.startswith('|')]
  else:chunks=re.split(r'\n(?=\d\. )',p)
  for chunk in chunks:
   refs=re.findall(r'\[([^\[\]\n]+)\]\[([a-z]+)\]',chunk)
   # Inline rates rows carry the official URL rather than reference links.
   if not refs:
    refs=[(lab,next(k for k,v in URL.items() if v==url)) for lab,url in re.findall(r'\[([^\[\]\n]+)\]\((https?://[^)]+)\)',chunk) if url in URL.values()]
   if not refs:raise ValueError(('UNSOURCED BLOCK',slug,chunk[:120]))
   row=dict(id=f'{prefix}-{len(blocks)+1:03}',section=section,claim=' '.join(chunk.split()),sources=[source(k,lab) for lab,k in refs if k in URL])
   if section=='Two worked examples that recompute':row['kind']='computed-fictional-case';row['note']='Scenario figures are fictional/precomputed inputs, not statutory thresholds. Recompute with check-examples.py; source quotes establish classification and settlement law.'
   blocks.append(row)
 records[slug]=blocks
 (E/f'{slug}.rows.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2)+'\n')
 out=[f'# {slug}: figure and rule ledger','',f'Read date: 2026-10-31. Rows: {len(blocks)}. Source-cited draft; independent review pending.','', 'Each row reproduces the exact current Guide rule or rate row, with responsive original-language clauses for every cited source. Full clauses are retained where the rule has multiple conditions. Original web-tool source responses and raw HTML receipts are separate; reader derivatives never claim to be raw publisher bytes.','']
 for row in blocks:
  out.extend([f"## {row['id']} — {row['section']}",'',row['claim'],''])
  if row.get('note'):out.extend([row['note'],''])
  for src in row['sources']:
   out.extend([f"**{src['act_article']}** · [official source]({src['url']}) · read {src['read_date']} · `{src['source_file']}`",'', 'Exact original-language quote:','', *['> '+line for line in src['original_language_quote'].splitlines()], ''])
 (E/f'{slug}.md').write_text('\n'.join(out)+'\n')
print({k:len(v) for k,v in records.items()})
