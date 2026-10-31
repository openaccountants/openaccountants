from pathlib import Path
import json,re,hashlib
P=Path(__file__).resolve().parent;repo=P.parents[2];Q=json.loads((P/'quotes-draft.json').read_text());g=repo/'skills/international/spain/es-foral-income-tax.md';lines=g.read_text().split('\n')
M={498:['D15','D16','D17','P64'],499:['D30','D48','P64'],500:['D43','D30','D48','P64'],502:['D48','D50','D18','D32','D45'],508:['P24','P25'],536:['P25','R12'],538:['R13','R26table'],540:['P25'],544:['P25'],545:['P25'],546:['P25'],547:['P25'],549:['P25','R14','P53','P54'],551:['P25']}
readkeys=set(k for v in M.values()for k in v);split={}
# Quote complete contiguous paragraphs; no mid-sentence clipping, interpolated numbers or ellipses.
for key in readkeys:
 z=Q[key];reader=(P/z['reader']).read_text();ls=reader.split('\n');raw='\n'.join(ls[z['LF_start']-1:z['LF_end']]);offset=sum(len(v)+1 for v in ls[:z['LF_start']-1]);pars=list(re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',raw));groups=[];group=[];count=0
 for par in pars:
  if group and count+len(par.group())>1500:groups.append(group);group=[];count=0
  group.append(par);count+=len(par.group())
 if group:groups.append(group)
 split[key]=[]
 for n,group in enumerate(groups,1):
  a=offset+group[0].start();b=offset+group[-1].end()
  while b>a and reader[b-1].isspace():b-=1
  q=dict(z,key=key+'_'+str(n),quote=re.sub(r'\s+',' ',reader[a:b]).strip(),LF_start=reader.count('\n',0,a)+1,LF_end=reader.count('\n',0,b-1)+1);split[key].append(q)
rows=[]
for lf,keys in sorted(M.items()):
 for key in keys:
  for z in split[key]:
   rows.append(dict(guide_LF=lf,guide_wording=lines[lf-1],act_article=({'R':'Navarra DF174/1999','D':'Navarra DFL2/2023'}.get(z['source'],'Navarra DFL4/2008'))+' art/section '+z['article'],official_URL=z['url'],source_quote=z['quote'],source_reader=str(P/z['reader']),source_reader_SHA256=z['reader_sha256'],source_raw_SHA256=z['raw_sha256'],source_read_date='2026-10-28',source_native_LF=[z['LF_start'],z['LF_end']],quote_key=z['key'],classification='Own current primary provision / fictional arithmetic where expressly labelled',note='Only selected exact original-language paragraphs read; no whole-source-read claim. R26table uses exact Spanish current HTMLcells with tab-delimited boundaries, rawtable/dateattrs retained; no1510 merged-cell interpretation. Oldest-carried-expense sequencing in LF536 is the stated worksheet convention within the statutory current-expense priority/four-year expiry, not an express quoted statutory ordering of old origins.'))
for z in rows:
 ls=Path(z['source_reader']).read_text().split('\n');a,b=z['source_native_LF'];assert re.sub(r'\s+',' ','\n'.join(ls[a-1:b])).strip()==z['source_quote'],z['quote_key']
f=P/'giving-landlord-fragment.json';f.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(P/'giving-landlord-fragment-controls.json').write_text(json.dumps(dict(guide_sha256=hashlib.sha256(g.read_bytes()).hexdigest(),fragment_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),current_units=len(M),rows=len(rows),selected_article_subsection_scopes=len(readkeys),actual_original_language_native_checks='all output rows pass literal LF comparison',status='Writer fragment only, no independent PASS; remaining housing/advance/pension/payment/source-specific scopes pending'),indent=2)+'\n');print(len(rows),'rows',len(M),'units',len(readkeys),'scopes',hashlib.sha256(f.read_bytes()).hexdigest())
