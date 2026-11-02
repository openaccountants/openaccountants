from pathlib import Path
import json,re,hashlib
P=Path(__file__).resolve().parent;repo=P.parents[2];Q=json.loads((P/'quotes-draft.json').read_text());g=repo/'skills/international/spain/es-foral-income-tax.md';lines=g.read_text().split('\n')
M={553:['Mdependent','Mdependent2','IPREM2026table','LPGE90','P62_9'],557:['LT15','LT17','LT24','PDT17discrepancy','P62_1'],561:['LT15','H12home'],562:['LT17','H15home','H17home','H17joint'],563:['LT24','H17home','H17joint'],565:['LT15','H12jointcap'],567:['H12home','H15home','H17home','H17joint','Mhomefamily','Mhomecarry'],569:['LT17','H17home','H17joint'],573:['H17home','H17joint','Mhomeincome'],574:['H17home','H17joint','Mhomeincome'],575:['H17home','H17joint','Mhomeincome'],577:['H17home','H17joint'],579:['R2017_51','R2017_52','H12home','H15home','H17home'],581:['R2017_52','P65netassets','R55recapture','P83recapture'],583:['PDA28','LT15'],585:['PDA33','PDA35'],587:['LDT8','Mhomecarry'],589:['LT15','LT17','H17home','H17joint','P61'],643:['PDA13'],645:['PDA13','IPREM2026table','LPGE90','MdisabilityAnnuity','MdisabilityIPREM','MdisabilityIPREMvalue'],647:['PDA13'],673:['P17','P14pensions'],675:['PDT25','H17pension'],677:['PDT25','H17pension'],679:['PDT25','H17pension']}
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
   rows.append(dict(guide_LF=lf,guide_wording=lines[lf-1],act_article=({'R':'Navarra DF174/1999 current','R2017':'Navarra DF174/1999 preserved2017version','L':'Navarra ownconsolidatedDFL4/2008','M':'Navarra official2025income manual updated2026','H12':'Navarra DFL4/2008 preserved2012version','H15':'Navarra DFL4/2008 preserved2015version','H17':'Navarra DFL4/2008 preserved2017version','IPREM2026':'CastillaLaMancha official2026IPREMtable','LPGE':'State LPGE31/2022 DA90 original2023amounts with current2026continuationtable'}.get(z['source'],'Navarra DFL4/2008 current2026edition'))+' art/section '+z['article'],official_URL=z['url'],source_quote=z['quote'],source_reader=str(P/z['reader']),source_reader_SHA256=z['reader_sha256'],source_raw_SHA256=z['raw_sha256'],source_read_date='2026-10-28',source_native_LF=[z['LF_start'],z['LF_end']],quote_key=z['key'],classification='Own current primary provision / fictional arithmetic where expressly labelled',note='Only selected exact original-language paragraphs read; no whole-source-read claim. Historical H12/H15/H17/R2017 rules apply only through own current LT15/17/24 preservation gateway. Old9015/21035annualcaps are overridden by LT15; old2015incomeceilings are replaced through LT17 by2017ones. H17joint historical other-family amounts are not adopted as current2026credits. Current2026IPREMcontinuation is separately sourced; no2026income manual claimed. Hypothetical controls are derived, not enactment quotations.'))
for z in rows:
 ls=Path(z['source_reader']).read_text().split('\n');a,b=z['source_native_LF'];assert re.sub(r'\s+',' ','\n'.join(ls[a-1:b])).strip()==z['source_quote'],z['quote_key']
f=P/'home-pension-fragment.json';f.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(P/'home-pension-fragment-controls.json').write_text(json.dumps(dict(guide_sha256=hashlib.sha256(g.read_bytes()).hexdigest(),fragment_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),current_units=len(M),rows=len(rows),selected_article_subsection_scopes=len(readkeys),actual_original_language_native_checks='all output rows pass literal LF comparison',status='Writer fragment only, no independent PASS; remaining advance/source-specific scopes pending; payments/business/returnthreshold delegated to writerB'),indent=2)+'\n');print(len(rows),'rows',len(M),'units',len(readkeys),'scopes',hashlib.sha256(f.read_bytes()).hexdigest())
