from pathlib import Path
import re,json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2];IDS={x['key']:x for x in json.loads((P/'source-identities.json').read_text())};AL={'P':'N1','R':'N3','R2017':'N3','M':'N4','L':'N27','H17':'N28','H12':'N29','H15':'N30','D':'N51','CN':'N0'};Q={};errors=[]
def norm(x):return re.sub(r'\s+',' ',x).strip()
def src(k):return IDS[AL.get(k,k)]
def text(k):return (P/('N3-current-selected.txt'if k=='R'else'N3-20171231-selected.txt'if k=='R2017'else src(k)['reader'])).read_text()
def scope(k,art,sub=None):
 t=text(k);hits=list(re.finditer(r'(?m)^\s*Artículo\s+'+re.escape(str(art))+r'\.(?!\d)',t))
 for m in hits:
  h=re.search(r'(?m)^\s*Artículo\s+\d+(?:\.|\s)',t[m.end():]);e=m.end()+h.start()if h else len(t)
  z=t[m.start():e]
  if len(z)>150 and not re.search(r'\.{5,}',z[:180]):
   # BOE operative body ends before its amendment/version notes.
   if k not in ['R','R2017']:z=re.split(r'(?m)^(?:Se modifica|Se añade|Se deroga|Subir|\s*Seleccionar redacción)',z)[0]
   a=m.start();b=a+len(z)
   if sub is not None:
    v=re.search(r'(?m)^'+re.escape(str(sub))+r'\.\s',z)
    if not v:raise ValueError('subsection missing '+str((k,art,sub)))
    w=re.search(r'(?m)^\d+\.\s',z[v.end():]);b=a+(v.end()+w.start()if w else len(z));a+=v.start()
   return t,a,b
 raise ValueError('article missing '+str((k,art)))
def quote(key,k,art,needle=None,following=0,sub=None):
 try:
  t,a,b=scope(k,art,sub);z=t[a:b]
  if needle:
   pars=list(re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',z))if k not in ['R','R2017']else list(re.finditer(r'[^\n]+',z))
   hit=next(i for i,p in enumerate(pars)if needle.casefold() in norm(p.group()).casefold());p=pars[hit];b=a+pars[min(hit+following,len(pars)-1)].end();a+=p.start()
  while b>a and t[b-1].isspace():b-=1
  sid=src(k);reader='N3-current-selected.txt'if k=='R'else'N3-20171231-selected.txt'if k=='R2017'else sid['reader']
  Q[key]=dict(key=key,source=k,article=str(art)+('.'+str(sub)if sub is not None else''),url=sid['url'],quote=norm(t[a:b]),reader=reader,LF_start=t.count('\n',0,a)+1,LF_end=t.count('\n',0,b-1)+1,raw_sha256=sid['raw_sha256'],reader_sha256=hashlib.sha256((P/reader).read_bytes()).hexdigest(),read_on='2026-10-28',scope_note='Current raw dated-block selector fdesde<=20261028<fhasta; datedblocks/raw original preserved'if k=='R'else'Only selected actual source scope; historical P edition used only as expressly preserved')
 except Exception as e:errors.append([key,k,art,sub,needle,str(e)])
def native(key,k,lo,hi,article):
 sid=src(k);t=(P/sid['reader']).read_text();Q[key]=dict(key=key,source=k,article=article,url=sid['url'],quote=norm('\n'.join(t.split('\n')[lo-1:hi])),reader=sid['reader'],LF_start=lo,LF_end=hi,raw_sha256=sid['raw_sha256'],reader_sha256=sid['reader_sha256'],read_on='2026-10-28')
for art in [7,17,18,24,25,28,32,34,35,36,39,40,41,43,45,53,54,55,56,57,58,59,60,61,64,66,67,68,70,71,73,75,80,83]:quote('P'+str(art),'P',art)
for sub in [1,2,3,4,5,6,8,9,10,11,12,13,14]:quote('P62_'+str(sub),'P',62,sub=sub)
for art in [5,8,9,12,13,14,26,40,56,78,91,92,93,94]:quote('R'+str(art),'R',art)
for art in [8,9,10,11,12,13,14,15,16]:quote('CN'+str(art),'CN',art)
for art in [15,16,17,18,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,48,49,50]:quote('D'+str(art),'D',art)
for key,k,a,n,f,s in [
 ('P7n','P',7,'n) Los rendimientos',6,None),('P39small','P',39,'d) Con ocasión de transmisiones',2,5),
 ('P39home','P',39,'b)',1,5),('P39loss','P',39,'e)',2,6),('P43swap','P',43,'h) De la permuta',2,1),('P43FIFO','P',43,'valores homogéneos',1,2),
 ('P43unlisted','P',43,'b) De valores no admitidos',5,1),('P43listed','P',43,'a) De valores representativos',0,1),
 ('R5day','R',5,'Para el cálculo del importe',0,None),('R5specific','R',5,'A efectos de la exención',0,None),
 ('R40scope','R',40,'1. Podrán',4,None),('R40timing','R',40,'4. La reinversión',5,None),('R40condition','R',40,'6. a)',4,None),('R40construct','R',40,'7.a)',8,None),
 ('P62creditwork','P',62,None,0,5),('P62family','P',62,None,0,9),('P62businesscredit','P',62,None,0,3),('P64businesscredit','P',64,None,0,2),
 ('P67foreign','P',67,None,0,None),('P45annuity','P',45,None,0,3),('P83recapture','P',83,None,0,4)
]:quote(key,k,a,n,f,s)
quote('P28div','P',28,'a) Los dividendos',0)
quote('P32custody','P',32,'a) Los gastos de administración',2)
quote('P39definition','P',39,None,0,1)
quote('P39lossrelease','P',39,'En los casos previstos',0,6)
quote('P43rights','P',43,'k) De la transmisión',0,1)
native('Mforeign','M',1160,1203,'2025manual foreign-work physical25–26; own payer-duration worksheet')
quote('P45home','P',45,None,0,1)
quote('R40rehab','R',40,'8. Se entenderá',0)
quote('P68quater','P','68 quater')
native('P55repeal','P',4299,4301,'55 repeal note2016 familybase reductions')
native('PDA58repeal','P',8622,8626,'DA58 currentrepeal')
native('PDT33','P',9847,9853,'DT33 2026specialelection')
native('PDA65','P',8797,8845,'DA65 current2026 energyefficiency')
quote('P55limits','P',55,'7.º a)',40,1)
quote('P55comp','P',55,None,0,2)
quote('H17home','H17',62,None,0,1)
quote('H17joint','H17',75)
quote('H15home','H15',62,None,0,1)
quote('H12home','H12',62,None,0,1)
quote('P65netassets','P',65)
quote('R55recapture','R',55)
quote('P68quinquies','P','68 quinquies')
quote('CIT67','CIT',67)
native('LT15','L',4932,4948,'DT15 preservedpre2013homecredit')
native('LT17','L',4954,4969,'DT17 preserved2013–2015homecredit')
native('LT24','L',5011,5015,'DT24 preserved2016–2017homecredit')
native('Mdependent','M',12615,12618,'2025manual actualannualIPREMbasisprinted227')
native('Mdependent2','M',12747,12752,'2025manual disabilityrelative annualIPREM/familybasisprinted230')
def disp(key,k,heading):
 t=text(k);hits=list(re.finditer(r'(?mi)^'+re.escape(heading)+r'\.',t));m=hits[-1] if hits else (_ for _ in ()).throw(ValueError((key,heading,'missing')));n=re.search(r'(?mi)^Disposición (?:adicional|transitoria|final) ',t[m.end():]);end=m.end()+n.start()if n else len(t);cut=re.search(r'(?mi)^\s*Seleccionar redacción:',t[m.start():end]);end=m.start()+cut.start()if cut else end;lo=t.count('\n',0,m.start())+1;hi=t.count('\n',0,end-1)+1
 native(key,k,lo,hi,heading+'; operativebody and explicit amendment/commencement context')
for key,k,heading in [('LDT8','L','Disposición Transitoria Octava'),('PDA28','P','Disposición adicional vigesimoctava'),('PDA33','P','Disposición adicional trigésima tercera'),('PDA35','P','Disposición adicional trigésimo quinta'),('PDT25','P','Disposición transitoria vigesimoquinta')]:disp(key,k,heading)
for art in [51,52]:quote('R2017_'+str(art),'R2017',art)
# Keep the dated current original table's cell boundaries, rather than concatenating15and10.
if (P/'R26-table-reader.txt').exists():
 z=dict(Q['R26']);f=P/'R26-table-reader.txt';t=f.read_text();z.update(key='R26table',reader='R26-table-reader.txt',reader_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),quote=norm(t),LF_start=1,LF_end=len(t.split('\n'))-1,scope_note='Exact current original-language HTML table cells with tab-delimited cell boundaries; raw table and datedblock provenance retained.');Q['R26table']=z
native('Mhomefamily','M',13350,13365,'2025manualprinted240 preserved15/18/30andLF5/2019family')
native('Mhomecarry','M',13372,13396,'2025manualprinted240 preservedannual/lifetimecapandnocarry')
native('Mhomeincome','M',13109,13133,'2025manualprinted236 preserved2017incomeceilings')
native('PDT17discrepancy','P',9505,9509,'BOE20260420DT17duplicates2022businessrenunciation; preserveactualLhomeDT17')
quote('H12jointcap','H12',75,'21.035',0)
native('IPREM2026table','IPREM2026',133,148,'Official2026annual12/14paymentIPREMtable')
disp('LPGE90','LPGE','Disposición adicional nonagésima')
disp('PDA13','P','Disposición adicional decimotercera')
quote('P14pensions','P',14,None,0,2)
quote('H17pension','H17',17,None,0,2)
native('MdisabilityAnnuity','M',3886,3902,'2025manual actualdisabilityannuity/relevantcombinedIPREMcategory')
native('MdisabilityIPREM','M',3138,3146,'2025manual combinedannuities/protectedworkincome3IPREMcontext')
native('MdisabilityIPREMvalue','M',3165,3173,'2025manual combinedcategory numeric3times8400=25200')
for k,arts in [('HR',[7,8,68,72]),('HL',[18,21,'25.bis'])]:
 for art in arts:quote(k+str(art),k,art)
native('HRannexII','HR',1253,1280,'AnnexIIcurrentfamilyweighting with P68quinquiesSARA statutoryoverride of olderIPREMreference')
native('HCformula','HC',487,540,'Officialsame-income-yearSARAformula/table')
native('Eminimum','E',49,79,'OF187E/2026publication17Sept/5000newminimum/renewal/effectdate')
native('HLweighting','HL',692,692,'HL25bis3 actualgender-violenceweighting')
native('HLDA19','HL',1658,1659,'DA19generalhousingIPREM-to-SARAsubstitutionfrom2019')
native('S26value','S26',292,330,'Resolution357/2026 actualincome-year2026SARA11201.44 plus prior202510919.71')
native('DSconditions','DS',500,552,'ActualDAVIDserviceconditions/amounts/incompatibility')
native('DSVAIS','DS',550,568,'ActualVAISpriorprogramme/60percent360/twoyearservicewording;statutorymaximumcontrols')
(P/'quotes-draft.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n');(P/'preparation-errors.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2)+'\n');print('draft quotes',len(Q),'errors',errors)
