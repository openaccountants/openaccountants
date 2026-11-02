from pathlib import Path
import json,re,hashlib
P=Path(__file__).resolve().parent;repo=P.parents[2];Q=json.loads((P/'quotes-draft.json').read_text());g=repo/'skills/international/spain/es-foral-income-tax.md';lines=g.read_text().split('\n')
M={25: ['CN8', 'CN9'], 27: ['CN10', 'CN11', 'CN12', 'CN13', 'CN14', 'CN15', 'CN16', 'P66'], 471: ['P68quinquies'], 481: ['LT15', 'LT17', 'LT24', 'PDA33', 'PDA35', 'LDT8'], 593: ['P68quinquies', 'HR8', 'HCformula', 'S26value'], 595: ['P68quinquies', 'Eminimum'], 597: ['HRannexII', 'HL18', 'HLDA19'], 599: ['HR7', 'HRannexII'], 603: ['HRannexII'], 604: ['HRannexII'], 605: ['HRannexII'], 606: ['HRannexII'], 607: ['HRannexII'], 609: ['HRannexII', 'HLweighting', 'HCformula'], 611: ['P68quinquies', 'HL18', 'HL21', 'Eminimum'], 615: ['P68quinquies'], 616: ['P68quinquies'], 617: ['P68quinquies'], 618: ['P68quinquies'], 620: ['P68quinquies', 'HRannexII', 'HCformula', 'S26value'], 622: ['P68quinquies', 'HR68', 'HR72', 'HLDA19', 'DSVAIS'], 624: ['P68quinquies', 'DSconditions'], 626: ['P68quinquies', 'DSconditions']}
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
   rows.append(dict(guide_LF=lf,guide_wording=lines[lf-1],act_article=({'CN':'Navarra current State-Navarra economic agreement','HR':'Navarra DF61/2013 housing regulation','HL':'Navarra LF10/2010 housing law','HC':'Navarra official weighted-family-income calculator','S26':'Navarra Resolution357/2026 annual SARA','E':'Navarra OF187E/2026 Emanzipa minimum amendment','DS':'Navarra official DAVID service','R':'Navarra DF174/1999 current','R2017':'Navarra DF174/1999 preserved2017version','L':'Navarra ownconsolidatedDFL4/2008','M':'Navarra official2025income manual updated2026','H12':'Navarra DFL4/2008 preserved2012version','H15':'Navarra DFL4/2008 preserved2015version','H17':'Navarra DFL4/2008 preserved2017version','IPREM2026':'CastillaLaMancha official2026IPREMtable','LPGE':'State LPGE31/2022 DA90 original2023amounts with current2026continuationtable'}.get(z['source'],'Navarra DFL4/2008 current2026edition'))+' art/section '+z['article'],official_URL=z['url'],source_quote=z['quote'],source_reader=str(P/z['reader']),source_reader_SHA256=z['reader_sha256'],source_raw_SHA256=z['raw_sha256'],source_read_date='2026-10-28',source_native_LF=[z['LF_start'],z['LF_end']],quote_key=z['key'],classification='Own current primary provision / fictional arithmetic where expressly labelled',note='Only selected exact original-language paragraphs read; no whole-source-read claim. Current Eminimum raises the old P68quinquies3000 Emanzipa minimum to5000 from18September2026; old award/renewal periods are preserved. HLDA19 replaces old housing-regulation IPREM references with SARA from1January2019. The calculator summary does not override statutory inclusive disability/age boundaries or one-or-more category weighting. SARA follows the same income year, rather than newest publication. Preserved home branches require own current LT15/17/24 gates. Hypothetical controls are derived, not enactment quotations.'))
for z in rows:
 ls=Path(z['source_reader']).read_text().split('\n');a,b=z['source_native_LF'];assert re.sub(r'\s+',' ','\n'.join(ls[a-1:b])).strip()==z['source_quote'],z['quote_key']
f=P/'advance-residence-fragment.json';f.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(P/'advance-residence-fragment-controls.json').write_text(json.dumps(dict(guide_sha256=hashlib.sha256(g.read_bytes()).hexdigest(),fragment_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),current_units=len(M),rows=len(rows),selected_article_subsection_scopes=len(readkeys),actual_original_language_native_checks='all output rows pass literal LF comparison',status='Writer fragment only, no independent PASS; root Navarra finite fragment complete; payments/business/returnthreshold independently owned by writerB; full Guide ledger owned by writerB'),indent=2)+'\n');print(len(rows),'rows',len(M),'units',len(readkeys),'scopes',hashlib.sha256(f.read_bytes()).hexdigest())
