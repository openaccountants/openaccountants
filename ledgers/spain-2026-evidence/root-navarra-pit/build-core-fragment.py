from pathlib import Path
import json,re,hashlib
P=Path(__file__).resolve().parent;repo=P.parents[2];Q=json.loads((P/'quotes-draft.json').read_text());g=repo/'skills/international/spain/es-foral-income-tax.md';lines=g.read_text().split('\n')
M={37:['P59'],38:['P60'],415:['P55repeal','PDA58repeal','P62_9'],417:['P17','P18','R9','P62_6'],419:['P34','P35','P36','PDT33'],421:['P36'],423:['P53','P54','P56','P57'],425:['P55limits','P55comp','P57'],452:['P59'],454:['P58','P61','P66','P67foreign'],456:['P73','P75'],462:['P62_5'],463:['P62_10','P62_5'],464:['P62_9','P64'],465:['P62_9'],466:['P62_9'],467:['P62_9'],468:['P62_9','P64'],469:['P62_9'],470:['P62_9'],471:['P62_2','P75'],472:['P62_6'],473:['P62_8'],474:['P62_11'],475:['P62_12'],476:['P62_13'],477:['P62_14'],479:['P64'],481:['P62_1','P62_4'],483:['PDA65','P64'],487:['P68quater','P64'],489:['P68']}
for lf in range(431,442):M[lf]=['P59']
for lf in range(445,451):M[lf]=['P60']
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
   rows.append(dict(guide_LF=lf,guide_wording=lines[lf-1],act_article=('Navarra DF174/1999'if z['source']=='R'else'Navarra DFL4/2008')+' art/section '+z['article'],official_URL=z['url'],source_quote=z['quote'],source_reader=str(P/z['reader']),source_reader_SHA256=z['reader_sha256'],source_raw_SHA256=z['raw_sha256'],source_read_date='2026-10-28',source_native_LF=[z['LF_start'],z['LF_end']],quote_key=z['key'],classification='Own current primary provision / fictional arithmetic where expressly labelled',note='Only selected exact original-language paragraphs read; no whole-source-read claim. Table first-row zero lower-bound/quota is implicit in the source table and calculation; printed rest-of-band amount is not mislabelled as lower bound. LF471advanceincompatibility andLF481preservation gateways are additionally bound by the later Navarra housing fragment; no completeclaim from this fragment alone.'))
for z in rows:
 ls=Path(z['source_reader']).read_text().split('\n');a,b=z['source_native_LF'];assert re.sub(r'\s+',' ','\n'.join(ls[a-1:b])).strip()==z['source_quote'],z['quote_key']
f=P/'core-fragment.json';f.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(P/'core-fragment-controls.json').write_text(json.dumps(dict(guide_sha256=hashlib.sha256(g.read_bytes()).hexdigest(),fragment_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),current_units=len(M),rows=len(rows),selected_article_subsection_scopes=len(readkeys),actual_original_language_native_checks='all output rows pass literal LF comparison',status='Writer fragment only, no independent PASS; remaining housing/advance/pension/payment/source-specific scopes pending'),indent=2)+'\n');print(len(rows),'rows',len(M),'units',len(readkeys),'scopes',hashlib.sha256(f.read_bytes()).hexdigest())
