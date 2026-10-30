from pathlib import Path
import json,re
P=Path(__file__).resolve().parent
ID={z['key']:z for z in json.loads((P/'source-identities.json').read_text())}
ALIAS={'B':'bizkaia_irnr_pdf','A':'araba_irnr_current_pdf','G':'gipuzkoa_irnr_0_pdf','BP':'02_pdf','AP':'03_pdf','GP':'04_pdf','BR':'10_pdf','AR':'11_pdf','GR':'12_pdf','BC':'bizkaia_cit_current','AC':'alava_cit_current','GC':'gipuzkoa_cit_current','NC':'navarra_cit_current','CE':'basque_agreement_html','CN':'navarra_agreement_html','State':'state_irnr_current_html','N':'navarra_state_irnr_html','BT':'interest_bizkaia_nfgt','AT':'interest_araba_nfgt','GT':'interest_gipuzkoa_nfgt','NT':'interest_navarra_general'}
Q={};missing=[]
def norm(s):return re.sub(r'\s+',' ',s).strip()
def text(src):return (P/ID[ALIAS.get(src,src)]['reader']).read_text()
def article_scope(t,article):
 if article is None:return 0,len(t)
 pat=r'(?m)^\s*Artículo\s+'+re.escape(str(article))+r'\.(?!\d)'
 for match in re.finditer(pat,t):
  end=re.search(r'(?m)^\s*Artículo\s+\d+(?:\s+bis)?\.(?!\d)',t[match.end():]);last=match.end()+end.start() if end else len(t)
  # Dotted TOC entries and one-line heading listings are not operative source scopes.
  heading=t[match.start():match.start()+200]
  if last-match.start()>200 and not re.search(r'\.{5,}',heading):return match.start(),last
 raise ValueError('operative article scope absent '+str(article))
def q(key,src,article,needle,following=0):
 try:
  t=text(src);lo,hi=article_scope(t,article);scope=t[lo:hi]
  paras=list(re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',scope))
  matchpat=(r'(?<!\w)'if needle[:1].isalnum()else'')+re.escape(norm(needle))+(r'(?!\w)'if needle[-1:].isalnum()else'')
  matches=[i for i,z in enumerate(paras)if re.search(matchpat,norm(z.group()),re.I)]
  if not matches:raise ValueError('complete source paragraph missing needle '+needle)
  z=paras[matches[0]];end=paras[min(matches[0]+following,len(paras)-1)].end();start=lo+z.start();end=lo+end
  while end>start and t[end-1].isspace():end-=1
  srcid=ID[ALIAS.get(src,src)]
  Q[key]=dict(source=src,article=str(article)if article is not None else'',url=srcid['url'],quote=norm(t[start:end]),reader=srcid['reader'],LF_start=t.count('\n',0,start)+1,LF_end=t.count('\n',0,end-1)+1,read_on='2026-10-28',normalisation='Original-language complete paragraph(s), whitespace joined only; native reader line numbers count literal LF, not PDF form-feed characters.')
 except Exception as exc:missing.append([key,src,article,needle,str(exc)])

for s in ['B','A','G']:
 for tag,article,needle,n in [
  ('ownlaw',3,'interpretará en concordancia',0),('taxpayer',5,'personas físicas y entidades',0),('PE',13,'seis meses',0),('source',13,'Rentas',0),('divexempt',14,'9',0),('interestexempt',14,'intereses',2),('separate',15,'separada',1),('PEincome',16,'actividad',1),
  ('PEbase',18,'disposiciones del régimen general',0),('PEcharges',18,'casa central',7),('PEcapital',18,'capitales propios',0),('PEexcluded',18,'38',0),('PEsize',18,'microempresas',2),('PErate',19,'56',0),('remittance',19,'20',1),('remitexempt',19,'La imposición complementaria no será aplicable',2),('PEcredits',19,'En la cuota íntegra',3),('PEreturn',21,'veinticinco',1),
  ('gross',24,'importe íntegro',0),('activitycost',24,'personal',0),('gain',24,'ganancias patrimoniales',2),('EUcost',24,'residentes en otro Estado miembro',4),('EEA',24,'Espacio Económico Europeo',0),('rate',25,'24',0),('capitalrate',25,'f)',3),('pension',25,'pensiones',1),('diplomatic',25,'misiones',0),('seasonal',25,'temporada',0),('buyer',25,'3 por',1),('credit',26,'sólo se deducirán',2),('accrual',27,'Tratándose de rendimientos',2),('withhold',31,'equivalente',1),('withholdExclude',31,'24',0),('nofile',28,'No se exigirá',0)]:q(s+'_'+tag,s,article,needle,n)
for s in ['BP','AP','GP']:
 for tag,art,needle,n in [('div1500',9,'1.500',2),('wagecost',22,'Seguridad Social',1),('rent',32,'30 por',1),('rent70',32,'70 por',2),('rent20',32,'20 por',1),('insurance',32,'300',1),('rentnonnegative',32,'negativo',0),('gaincost',45,'gastos',2),('gaindep',45,'amortizaciones',1),('gainsale',45,'valor de transmisión',0)]:q(s+'_'+tag,s,art,needle,n)
 q(s+'_gainyears',s,45,'Los coeficientes se aplicarán',2)
 q(s+'_marketfloor',s,45,'normal de mercado',0)
 q(s+'_reference70',s,32,'índices de referencia',2)
 q(s+'_rentfinance',s,32,'a)',1)
for s in ['BP','GP']:q(s+'_rent',s,32,'30 por',4)
q('AP_rural','AP',32,'35 por',1)
for s,art in [('BR',37),('AR',36),('GR',35)]:
 q(s+'_costs',s,art,'necesarios',100)
 q(s+'_dep',s,art+1,'3 por',3)
 q(s+'_movables',s,art+1,'mobiliaria',1)
 q(s+'_usufruct',s,art+1,'duración determinado',2)
for s in ['BC','AC','GC']:
 q(s+'_residence',s,11,'residencia',1)
 q(s+'_size',s,13,'microempresa',5)
 q(s+'_rate',s,56,'24',2)
 q(s+'_index',s,40,'depreciación monetaria',3)
q('BC_surcharge','BC','57 bis','Los contribuyentes',2)
q('AC_surcharge','AC',56,'resultado contable positivo',2)
q('GC_surcharge','GC',56,'resultado',2)
q('NC_PE','NC',135,'no residentes',2)
q('NC_rate','NC',51,'28',4)
q('NC_small23','NC',51,'23 por',1)
q('NC_micro19','NC',51,'19 por',1)
q('Navarra_continuation','N',None,'no ha sido aprobado',0)
for src,arts in [('CE',[14,15,16,17,18,21,22,23]),('CN',[18,19,20,21,22,23,28,29,30])]:
 for art in arts:
  for tag,needle,n in [('scope','',0)]:
   # Full article extracts are retained for actual source reading; claim rows use selected paragraphs below.
   try:
    t=text(src);lo,hi=article_scope(t,art);(P/f'{src}-art{art}.selected.txt').write_text(t[lo:hi])
   except Exception as exc:missing.append([src,art,str(exc)])
for src,art,tag,needle,n in [('CE',21,'CElaw','normativa autónoma',1),('CE',21,'CEPE','seis meses',0),('CE',22,'CEconnections','inmuebles',2),('CE',22,'CEshared','proporción',3),('CE',23,'CEwithhold','proporción',1),('CE',15,'CEthreshold','12 millones',2),('CE',15,'CEround','dos decimales',1),('CN',28,'CNlaw','normativa foral navarra',2),('CN',29,'CNconnections','inmuebles',2),('CN',29,'CNshared','proporción',3),('CN',30,'CNwithhold','proporción',1),('CN',19,'CNthreshold','doce millones',2),('CN',19,'CNround','dos decimales',1)]:q(tag,src,art,needle,n)
for src,art,tag,needle,n in [('State',19,'StateRemit','19 por',1),('State',24,'StateImpute','inmuebles',1),('State',25,'StateRates','24 por',1)]:q(tag,src,art,needle,n)
q('StateImpute','State',24,'renta imputada',0)
q('CElaw','CE',21,'normativa autónoma',4)
q('CE75','CE',14,'75',2)
q('CEannualise','CE',14,'inferior a un año',0)
q('CEstartup','CE',14,'inicio de la actividad',1)
q('CN75','CN',18,'75',2)
q('CNannualise','CN',19,'inferior al año',0)
q('CNPElaw','CN',28,'1. Cuando se graven',1)
q('CEdate','CE',21,'01/05/2025',0)
q('CNdate','CN',28,'26/07/2025',0)
q('ATlate','AT',27,'seis meses',4)
q('BTcollection','BT',28,'5 por',3)
q('BT400norequest','BT',203,'sin requerimiento previo',2)
q('StateOwnuse','LIRPF2026',85,'1,1',1)
q('StateOwnuseGeneral','LIRPF2026',85,'2 por ciento',0)

q('StatePEoverrides','State',18,'casa central',5)
q('N211','navarra_210_order_current_html',5,'un mes',0)
q('Gcorrection','coef_gipuzkoa_correction',None,'transitoria',1)
for s in ['B','A','G']:q(s+'_PEaccounts',s,22,'separada',1)
for src,art,tag,needle,n in [
 ('CE',22,'CEproperty','inmuebles',0),('CE',22,'CEwork','trabajo',1),('CE',22,'CEpension','pensiones',0),('CE',22,'CEservices','servicios',1),('CE',22,'CEpublic','entidades públicas',0),('CE',22,'CErepresent','representación',2),
 ('CN',29,'CNproperty','inmuebles',0),('CN',29,'CNwork','trabajo',1),('CN',29,'CNpension','pensiones',0),('CN',29,'CNservices','servicios',1),('CN',29,'CNpublic','entidades públicas',0),('CN',29,'CNrepresent','representación',2),
 ('BT',26,'BTlateinterest','seis meses',0),('BT',27,'BTdecl5','5 por',1),('BT',27,'BTdeclhalf','0,5',1),('BT',28,'BTcollection','1. Los recargos',5),('BT',196,'BTpenalty','250',0),('BT',203,'BT400','400',2),
 ('AT',27,'ATlate','seis meses',4),('AT',28,'ATcollection','5 por',3),('AT',195,'ATpenalty','150',3),('AT',195,'ATwithheld','125 por',1),('AT',195,'ATlater','30 por',0),
 ('GT',27,'GTlate','tres meses',3),('GT',28,'GTcollection','5 por',3),('GT',195,'GTpenalty','150',3),('GT',195,'GTwithheld','105 por',1),
 ('NT',52,'NTlate','1 por',4),('NT',76,'NTpenalty','180',2),('NT',77,'NTwithheld','200',1),('NT',76,'NTlater','55 por',0),('NT',71,'NTreduction','conformidad',2),
 ('AT',26,'ATinterest','25 por',1),('GT',26,'GTinterest','25 por',1),('NT',50,'NTinterest','25 por',1),
 ('budget_bizkaia_2026',None,'Bbudget','4,0625',1),('budget_gipuzkoa_2026',None,'Gbudget','4,0625',1),('interest_bizkaia_2026',None,'legal2026','2026',2),('interest_navarra_2026',None,'Ninterest2026','4,0625',1),
 ('bizkaia_no_imputation_html',None,'Bnoimpute','2026',1),('bizkaia_rent2026_html',None,'BrentExample','70',1),('bizkaia_sale2026_html',None,'BsaleExample','1,249',1),
 ('bizkaia_deadlines_html',None,'B210windows','tres meses',2),('bizkaia_deadlines_html',None,'B210quarter','veinticinco',2),('bizkaia_deadlines_html',None,'B210refund','febrero',1),
 ('gipuzkoa_210_html',None,'G210windows','tres meses',0),('gipuzkoa_210_html',None,'G210quarter','25',2),('gipuzkoa_210_html',None,'G210refund','febrero',1),
 ('navarra_210_order_current_html',4,'N210windows','tres meses',2),('navarra_210_order_current_html',4,'N210quarter','agosto',1),('navarra_210_order_current_html',4,'N210refund','febrero',1),
 ('gipuzkoa_216_html',None,'G216','25',2),('gipuzkoa_296_html',None,'G296','enero',0),('navarra_216_order_html',5,'N216','agosto',1),('navarra_296_current_html',5,'N296','febrero',1),
 ('Bizkaia_DF153_2022_DF1',None,'BJanuary','enero',1),('bizkaia_296_pdf',None,'B296','enero',1),
 ('araba_calendar2026_pdf',None,'Acalendar','210',2),('araba_irnr_reg_pdf',18,'A211','fecha de la transmisión',0),('bizkaia_irnr_reg_pdf',18,'B211','fecha de la transmisión',0),('gipuzkoa_irnr_1_pdf',18,'G211','fecha de la transmisión',0)
]:q(tag,src,art,needle,n)
for s in ['B','A','G']:
 q(s+'_PEworldwide',s,13,'totalidad',0)
 q(s+'_imputationDeleted',s,13,'j)',0)
 q(s+'_PEloss',s,18,'compensar sus bases',0)
 q(s+'_provinceShare',s,13,'4.',2)
q('B_edition','B',None,'01/01/2026',0)
for tag,needle in [('BcalFebruary','Otsailaren 2'),('BcalApril','Apirilaren 27'),('BcalJuly','Uztailaren 27'),('BcalOctober','Urriaren 26')]:q(tag,'bizkaia_216_calendar2026_html',None,needle,0)
q('G_diplomatic','G',25,'misiones diplomáticas',0)
q('G_divexempt','G',14,'a)6',5)
def native_interval(key,src,article,lo,hi,note=''):
 sid=ID[ALIAS.get(src,src)];native=text(src).split('\n')
 Q[key]=dict(source=src,article=str(article),url=sid['url'],quote=norm('\n'.join(native[lo-1:hi])),reader=sid['reader'],LF_start=lo,LF_end=hi,read_on='2026-10-28',normalisation='Exact complete selected native LF interval, whitespace joined; '+note)
native_interval('A_pension','A',25,1570,1587,'Intro plus all three operative pension rows.')
native_interval('G_pension','G',25,2079,2094,'Intro plus all three operative pension rows.')
native_interval('BJanuary','Bizkaia_DF153_2022_DF1','DF1',1164,1174)
native_interval('BJanuaryEffect','Bizkaia_DF153_2022_DF1','DF3',1192,1197)
q('N210zero','navarra_210_order_current_html',4,'cuota cero',0)
native_interval('StateOwnuseDA55','LIRPF','DA55 actual2026 overlay',10810,10814)
native_interval('A210calendar','araba_calendar2026_pdf','2026 official210calendar',436,464)
native_interval('A211216calendar','araba_calendar2026_pdf','2026 official211/216calendar',466,489)
native_interval('A296calendar','araba_calendar2026_pdf','2026 official296calendar',501,524)
native_interval('B_PITcontext','coef_bizkaia_2026',1,48,62)
native_interval('A_PITcontext','coef_araba_2026',1,65,70)
native_interval('G_PITcontext','coef_gipuzkoa_2026','DA1',1720,1730)
native_interval('B_CITcontext','coef_bizkaia_2026',2,114,118)
native_interval('A_CITcontext','coef_araba_2026',2,124,126)
native_interval('G_CITcontext','coef_gipuzkoa_2026','DA2',1780,1788)
native_interval('B_PITexception','coef_bizkaia_2026',1,106,108)
native_interval('A_PITexception','coef_araba_2026',1,108,109)
native_interval('G_PITexception','coef_gipuzkoa_2026','DA1',1777,1779)
native_interval('G_CITtiming','coef_gipuzkoa_2026','DA2',1848,1854)
native_interval('AT2027boundary','AT','NF21/2025 art7 future-effect footnote47.1',12371,12374,'Dated future boundary only, no2026concession claimed.')
sid=ID['bizkaia_original216_order2015_pdf'];native=text('bizkaia_original216_order2015_pdf').split('\n')
Q['B216']=dict(source='bizkaia_original216_order2015_pdf',article='OF1564/2015 art3, actual216order at Gazette p17979ff',url=sid['url'],quote=norm('\n'.join(native[2363:2384])),reader=sid['reader'],LF_start=2364,LF_end=2384,read_on='2026-10-28',normalisation='Exact own bilingual Gazette interval, whitespace joined. Its January25text is overridden by later DF153/2022DF1, not treated as currentJanuaryendpoint.')

# Each native table row is independently selected from each own decree, never copied from the Guide.
guide=(P/'frozen-guide.txt').read_text()
for table,(start,end)in {'PIT':(132,166),'CIT':(196,239)}.items():
 for line in guide.splitlines()[start-1:end]:
  z=re.match(r'^\|\s*((?:19|20)\d{2})(?: and earlier)?\s*\|\s*([\d.]+)',line)
  if not z:continue
  year,value=z.groups()
  for src in ['coef_bizkaia_2026','coef_araba_2026','coef_gipuzkoa_2026']:
   t=text(src);ls=t.split('\n');hits=[]
   for i,x in enumerate(ls):
    if re.search(r'\b'+year+r'\b',x)and re.search(r'\b'+re.escape(value.replace('.',','))+r'\b',x):hits.append((i,x))
   # Some values coincide between PIT and CIT; table context selects the correct occurrence.
   marker='1983'
   citstart=next(i for i,x in enumerate(ls)if marker in x and '3,137'in x)
   hits=[(i,x)for i,x in hits if(i<citstart if table=='PIT'else i>=citstart)]
   if len(hits)!=1:missing.append([table,year,src,'expected one own native row',hits]);continue
   i,x=hits[0];sid=ID[src];Q[f'{table}_{src}_{year}']=dict(source=src,article=('DA1'if table=='PIT'else'DA2')if src=='coef_gipuzkoa_2026'else('1'if table=='PIT'else'2'),url=sid['url'],quote=norm(x),reader=sid['reader'],LF_start=i+1,LF_end=i+1,read_on='2026-10-28',normalisation='Whole native table row, whitespace joined; bilingual Gipuzkoa row retains both columns. Own table context recorded separately.')
(P/'quotes.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
(P/'quote-preparation-errors.json').write_text(json.dumps(missing,ensure_ascii=False,indent=2)+'\n')
print('prepared',len(Q),'errors',len(missing));print(json.dumps(missing,ensure_ascii=False))
