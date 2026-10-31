from pathlib import Path
import json,runpy,re,copy
m=runpy.run_path('ledgers/spain-2026-evidence/group-b-ledger-lib.py');L=m['Ledger']('es-foral-income-tax');I={x['line']:x['text']for x in L.units};E=[]
exec((L.p/'extra-source-catalog.py').read_text())
B=next(x['url']for x in m['CAT']if 'ca_13_2013.pdf/ce52' in x['url']);A='https://web.araba.eus/documents/d/araba/indice_norma-foral_irpf_cas-4-pdf';G=next(x['url']for x in m['CAT']if 'NF%203-2014%20(2026-0)' in x['url']);BR=next(x['url']for x in m['CAT']if 'ca_47_2014.pdf/c17' in x['url']);AR='https://web.araba.eus/documents/d/araba/indice-reglamento_irpf_cas-2-pdf';GR=next(x['url']for x in m['CAT']if 'DF%2033-2014%20(2026-2)' in x['url']);BI='https://www.bizkaia.eus/instrucciones/instruccion_1_2026_75_es.pdf';AI='https://web.araba.eus/documents/1247685/1249666/Instrucci%C3%B3n%2B%2BIRPF%2B2024.pdf/8f47b0d8-fbb0-2644-fbb7-c18fe0e92938?t=1744182672921'
COMPUTED={57,67,69,92,94,134,148,150,159,171,177,191,193,195,197,199,201,213,245,247,296,297,313,327,335,337,339,351,353,369,371,387,391,397,399,401,409,534,637,661,663,665,667,689,721,725,729,766}
def a(lf,u,q,p,kind='',note='',width=550):
 if lf not in I:E.append((lf,'missing guide unit'));return
 variants={'permanecido':['mayor número de días'],'183':['ciento ochenta y tres'],'50 por':['50%'],'opción':['opte','opten','manifieste'],'residencias':['residencial'],'proporción':['proporcional'],'5 por':['5%','cinco por ciento'],'primero':['primer lugar'],'monedas virtuales':['criptoactivos fungibles'],'dos decimales':['tipo medio'],'negativa':['negativos','negativo'],'notarial':['notario'],'seis':['6 años'],'diez':['10 años'],'nueve':['9 meses'],'doce':['12 meses'],'cinco':['5 años','5 períodos','5 periodos'],'15 por':['15%','15 ciento'],'5. b)':['letra b) del apartado 5'],'acumulación':['cuantía máxima'],'por ciento':['por 100'],'certificado':['certificación'],'certificación':['certificaciones'],'primer':['cuantía máxima','periodo impositivo inmediato','período impositivo inmediato'],'prioridad':['las aportaciones realizadas por la propia'],'triple':['tres veces'],'quince años':['15 años'],'60.100':['60.100,00','60.100 euros','60.100,'],'49,00':['en adelante']}
 for needle in [q]+variants.get(q,[]):
  try:
   L.add(I[lf],u,needle,p,kind or ('computed case / labelled own-law derivation'if lf in COMPUTED else 'rule'),note or ('Hypothetical inputs and calculated amounts are computed, not statutory quotations; retain the exact territorial/interpretation boundaries in this Guide unit.'if lf in COMPUTED else''),width);return
  except Exception as e:last=e
 E.append((lf,u,q,str(last)))
def law(lf,u,ar,qs,**kw):
 for q in qs:a(lf,u+('#a'+str(ar)if ar else''),q,('Bizkaia NF13/2013'if u==B else'Álava NF33/2013'if u==A else'Gipuzkoa NF3/2014'if u==G else'B DF47/2014'if u==BR else'A DF40/2014'if u==AR else'G DF33/2014'if u==GR else'A NFGT6/2005'if 'indice-norma-foral-general' in u else'Official act identified by URL')+' article '+str(ar),**kw)
def bag(lf,ar,qs,**kw):
 for u in[B,A,G]:law(lf,u,ar,qs,**kw)
def regs(lf,ars,qs,**kw):
 for u,ar in zip([BR,AR,GR],ars):law(lf,u,ar,qs,**kw)
# Retained exact own-source quote anchors selected by the root's nonresident ledger writer.
Q=json.loads(Path('ledgers/spain-2026-evidence/es-foral-non-resident-tax/quotes.json').read_text())
def reuse(lf,key):
 z=Q[key];u=z['url'];x=m['source'](u);L.sources[u]=x
 L.rows.append(dict(id=len(L.rows)+1,section=next(v['section']for v in L.units if v['line']==lf),guide_LF=lf,guide_wording=I[lf],provision='Own source '+z['article']+'; '+key,url=u,quote=z['quote'],read_on='2026-10-28',kind='rule / computed illustration where expressly labelled',note='Exact retained primary quotation; selected native source scope is preserved in source-read-scopes. Hypothetical inputs/output amounts are computed.',raw_sha256=x['actual_raw_sha256'],reader=x['reader']))
CE='https://www.boe.es/buscar/act.php?id=BOE-A-2002-9969'
for lf,ar,qs in [(25,43,['permanecido','principal centro','última residencia','183']),(25,6,['mayor base']),(27,7,['teletrabajo','centro de trabajo','buques','pensiones']),(27,10,['domicilio fiscal'])]:
 for q in qs:a(lf,CE+'#a'+str(ar),q,'Basque Economic Agreement article '+str(ar))
for lf,ar,qs in [(35,75,['18.080','49,00']),(36,76,['7.500','28,00']),(39,77,['1.615']),(48,9,['efectivamente realizados en el extranjero']),(52,9,['60.100']),(53,9,['prestación de servicios transnacional']),(54,9,['fronterizos'])]:bag(lf,ar,qs)if lf in[35,36,39,48]else law(lf,{52:B,53:A,54:G}[lf],ar,qs)
law(39,A,77,['200','500'])
regs(57,[11,11,11],['días del año','retribuciones específicas'])
regs(63,[11,11,11],['excesos']);law(63,B,9,['opción']);law(63,A,105,['requerimiento']);law(63,G,104,['requerimiento'])
for lf,ar,qs in [(65,92,['menor']),(69,92,['183','50 por','plazo voluntario'])]:law(lf,B,ar,qs)
law(67,A,92,['menor']);law(67,G,91,['menor'])
bag(73,22,['Seguridad Social','políticos']);bag(73,21,['íntegros'])
for lf,q in [(77,'14.800'),(78,'0,6098'),(79,'3.000'),(80,'7.500'),(82,'100 por')]:bag(lf,23,[q])
bag(82,23,['250 por','negativo']);bag(84,25,['600.000','año']);law(84,BR,29,['deberá determinarse']);law(84,AR,29,['opción']);law(84,GR,28,['opción']);bag(84,27,['Impuesto sobre Sociedades']);bag(84,28,['amortizaciones'])
for lf,u in[(88,B),(89,A),(90,G),(92,B),(92,A),(92,G)]:law(lf,u,28,['35.000','85.000','10 por'])
law(89,A,28,['45 por']);bag(94,25,['10 por','15 por','cinco','50 por'])
for ar,qs in[(63,['viviendas','ganancias']),(65,['25 por','treinta']),(66,['cuatro'])]:bag({63:98,65:100,66:100}[ar],ar,qs)
bag(102,67,['orden','ahorro']);bag(102,73,['4.896'])
for lf,ar,qs in [(106,71,['5.000']),(107,71,['8.000']),(108,71,['4.000']),(109,71,['10.000','preferencia']),(110,70,['2.400','8.000']),(111,71,['cinco']),(113,70,['jubilación','capital'])]:bag(lf,ar,qs)
for key in ['BP','AP','GP']:
 for suffix in ['gaincost','gaindep','gainsale','gainyears','marketfloor']:reuse(117,key+'_'+suffix)
bag(124,42,['400.000','65','dependencia']);regs(128,[67,61,64],['tres años','doce meses','dos años']);law(128,BR,67,['residencias']);law(128,GR,64,['residencias']);bag(130,42,['dación']);law(130,A,42,['separación']);law(130,G,42,['separación'])
bag(134,49,['reinversión']);regs(134,[49,46,45],['principal','proporción']);regs(136,[49,46,45],['dos años','plazos','rehabilitación']);regs(142,[49,46,45],['incumplimiento','intereses'])
regs(146,['49bis','46bis','45bis'],['seis meses','año','5 por']);bag(148,42,['240.000']);regs(150,['49bis','46bis','45bis'],['retención','siguiente','incumplimiento'])
for lf in[155,157,159]:
 for prefix in['BP','AP','GP']:reuse(lf,prefix+'_div1500')
bag(157,39,['íntegros','asistencia técnica']);law(157,B,99,['individual']);law(157,A,99,['individual']);law(157,G,98,['individual'])
for lf,qs in[(167,['cotización']),(169,['capitalizar','20 por','balance']),(171,['capitalizar']),(173,['primero','liberadas','suscripción'])]:bag(lf,47,qs)
bag(173,43,['dos meses','año'])
for lf in[181,185,186,187,191,193,195,197,199]:
 bag(lf,45,['adquisición','enajenación'])
for u,q in[(B,'monedas virtuales'),(A,'monedas virtuales'),(G,'monedas virtuales')]:
 for lf in[181,185,186,191]:law(lf,u,47,[q])
for lf in[187,193,195,199]:bag(lf,47,['permuta'])
for lf in[201,203]:bag(lf,43,['monedas virtuales'])
bag(213,66,['cuatro']);bag(213,63,['ganancias'])
# Full current scales: one actual own statutory table row per Guide row/province.
from decimal import Decimal as D
def nums(s):
 return [D(x.replace('.','').replace(',','.'))for x in re.findall(r'(?<![A-Za-z0-9])\d+(?:\.\d{3})*(?:,\d+)?(?![A-Za-z0-9])',s)]
def scale(lf,u,ar):
 vals=[D(c.strip().replace(',','').replace('%',''))for c in I[lf].split('|')[1:4]];x=m['source'](u+'#a'+str(ar));cand=[]
 for ln in x['text'].splitlines():
  ns=nums(ln)
  if len(ns)>=3 and ns[0]==vals[0]and ns[-1]==vals[2]and(vals[1]in ns[1:-1]or vals[0]==0 and vals[1]==0):cand.append(m['norm'](ln))
 if len(cand)!=1:E.append((lf,u,'scale exact row',cand));return
 L.sources[x['selected_url']]=x;L.rows.append(dict(id=len(L.rows)+1,section=next(v['section']for v in L.units if v['line']==lf),guide_LF=lf,guide_wording=I[lf],provision=('B NF13/2013'if u==B else'A NF33/2013'if u==A else'G NF3/2014')+' article '+str(ar)+' own2026table',url=x['selected_url'],quote=cand[0],read_on='2026-10-28',kind='statutory table row',note='Exact own row; source may omit printed zero quota in first B general row. Numeric vector independently matched.',raw_sha256=x['actual_raw_sha256'],reader=x['reader']))
for u in[B,A,G]:
 for lf in range(222,230):scale(lf,u,75)
 for lf in range(233,242):scale(lf,u,76)
bag(218,75,['escala']);bag(245,75,['dos decimales','Sociedades']);bag(247,75,['pérdidas']);law(247,A,75,['años anteriores']);law(247,G,75,['años anteriores']);bag(249,77,['1.615']);bag(249,78,['negativa']);law(249,B,95,['retenciones']);law(249,A,95,['retenciones']);law(249,G,94,['retenciones']);law(249,A,77,['200'])
for u,ar in[(B,92),(A,92),(G,91)]:law(251,u,ar,['menor','dos decimales'])
for u,qs in[(B,['682','844','1.421','1.680','2.195']),(A,['734,80','909,70','1.532,30','1.811,70','2.366,10']),(G,['682','844','1.421','1.680','2.195'])]:law(257,u,79,qs)
for u,q in[(B,'394'),(A,'424,60'),(G,'394')]:law(258,u,79,[q])
law(259,A,79,['68,20','incompatible'])
for lf,ar,q in[(260,81,'328'),(261,82,'906'),(262,82,'1.294'),(263,82,'1.552'),(264,82,'1.935')]:
 for u in[B,G]:law(lf,u,ar,['2.040'if lf==264 and u==G else q])
for lf,ar,q in[(260,81,'423,72'),(261,82,'1.025,64'),(262,82,'1.464,54'),(263,82,'1.756,75'),(264,82,'2.191,03')]:law(lf,A,ar,[q])
bag(265,83,['393','714','20.000']);law(266,B,'83quinquies',['200','30.000','incompatible']);law(266,A,'82bis',['200','30.000','incompatible']);law(266,G,'82bis',['200','30.000','incompatible'])
bag(268,79,['treinta','salario mínimo','partes iguales','judicial','tutela']);bag(270,81,['conviva','salario mínimo','partes iguales']);law(270,A,81,['red foral']);law(270,A,79,['15 por','4.000']);law(270,A,81,['15 por','4.000']);bag(272,82,['doble','cuarto grado','totalidad']);bag(274,83,['0,0393','0,0714','negativa']);bag(274,84,['devengo']);bag(276,80,['15 por','30 por']);law(276,G,80,['notarial'])
for u in[B,A,G]:law(282,u,86,['20 por','1.600','35 por','2.800','68.000'])
for u in[B,G]:law(283,u,87,['18 por','1.530','23 por','1.955','36.000','68.000'])
law(284,A,87,['18 por','1.530','20 por','1.836','25 por','2.346','36.000','68.000'])
bag(285,87,['seis','diez']);bag(286,'87bis',['18 por','3.000']);bag(287,85,['30 por','3.000']);law(287,A,85,['cada']);law(287,G,85,['cada'])
for lf,ars,qs in[(288,['83bis','81ter','83bis'],['250','183']),(290,['83ter','83ter','83quater'],['1.500','nueve','doce','67 por','85 por','cinco']),(291,['83quater','83bis','83ter'],['200','50 por','67 por','nueve']),(292,['91bis','93bis','90bis'],['15 por','20 por','25 por','cinco']),(293,['91ter','93ter','90ter'],['10 por','15 por','cinco']),(294,[93,93,92],['20 por']),(295,['91quater','87ter','90quater'],['15 por','20.000','30 por','dos años']),(296,['91quinquies','87quater','90quinquies'],['5 por','10 por','10.000','40.000','subvenciones']),(297,['91sexies','87quinquies','90sexies'],['15 por','5.000','subvenciones'])]:
 for u,ar in zip([B,A,G],ars):law(lf,u,ar,qs)
law(288,B,'83bis',['500','iguales']);law(288,G,'83bis',['500','iguales']);law(288,A,'81ter',['incompatible']);law(289,A,'81bis',['500','718,08','1.436,16'])
for lf in[325,327,329]:law(lf,A,87,['4 ter','2.346','5. b)'])
for lf,qs in[(333,['certificados']),(335,['expida','dos años']),(337,['coeficiente','subvenciones']),(339,['cinco','acumulación'])]:
 for u,ar in[(B,'91quater'),(A,'87ter'),(G,'90quater')]:law(lf,u,ar,[q for q in qs if not(lf==339 and u==B and q=='acumulación')])
# Complete direct ordinary share-credit provisions, with each own rate/limit/history.
for lf,u,ar,qs in[(343,B,89,['acciones']),(343,A,89,['opciones']),(343,G,89,['opciones']),(347,B,89,['10 por','15 por','1.200','1.800','5 por','cinco','cuarto','igualdad']),(348,A,89,['15 por','20 por','1.500','2.000','6.000','8.000','cuatro','40 por','dos','cinco']),(349,G,89,['15 por','20 por','1.500','2.000','6.000','8.000','cuatro','40 por','despido'])]:law(lf,u,ar,qs)
for lf in[353,355]:
 for u in[B,A,G]:law(lf,u,89,['intereses'if lf==355 else'por ciento'])
for lf,u,ar,qs in[(359,B,90,['25 por']),(359,A,90,['25 por']),(359,G,'89bis',['20 por']),(363,B,90,['25 por','30 por','20 por','25 por','cinco','certificado']),(364,A,90,['25 por','30 por','20 por','25 por','cinco','certificado']),(365,G,'89bis',['20 por','25 por','50.000','10 por','400.000','40 por','tres','doce','certificado'])]:law(lf,u,ar,qs)
for lf in[367,369,371,375]:
 for u,ar in[(B,90),(A,90),(G,'89bis')]:law(lf,u,ar,['intereses'if lf==375 else'cinco'if lf==371 else'25 por'if u!=G else'20 por'])
for lf in[379,381,383,387,389,391,393,397,399,401,403,409]:bag(lf,88,['actividades económicas','treinta'])
for lf in[391,401]:bag(lf,75,['18.080']);bag(lf,77,['1.615'])
# Qualification and deemed-return chains; only actual selected provisions are used.
law(299,BR,'66bis',['546/1995','1593/2011','1074/2012','superior','1379/2008','331/1997','certificación'])
law(301,GR,'63bis',['6/2023']);law(301,A,'81ter',['250'])
for lf,ar,q in[(303,'66ter','acuerdo'),(305,'66ter','rechace')]:law(lf,BR,ar,[q,'intereses'if lf==305 else'certificado'])
for lf,ar,q in[(303,'63ter','acuerdo'),(305,'63ter','rechace')]:law(lf,GR,ar,[q,'intereses'if lf==305 else'certificado'])
for lf in[307,309,313]:law(lf,A,'83ter',['demandante','nueve','doce','1.500','cinco'])
law(307,A,94,['documental']);law(311,A,94,['documental']);a(311,'https://web.araba.eus/es/-/hacienda/renta/deducciones-familias','IDC','Álava published actual certificate/IDC evidence');a(311,'https://www.lanbide.euskadi.eus/informacion/mi-lanbidenet/weblan00-content/es/?r01-Domain-Origin=net','mejora','Lanbide certificate scope')
AT='https://web.araba.eus/documents/d/araba/indice-norma-foral-general-tributaria-cas-8-pdf'
for ar,qs in[(117,['incumplimiento','complementarias']),(116,['rectificación']),(26,['intereses'])]:law(315,AT,ar,qs)
law(315,A,102,['beneficio'])
for u,ar in[(B,'93bis'),(A,'94bis'),(G,'92bis')]:law(317,u,ar,['cinco','primer'])
for lf in[325,327,329]:law(lf,A,87,['dependencia','menores de 36'])
# Incorporations and exact prior-source quotes, not cross-territory analogies.
for lf in[351]:
 for key in ['BC_size','AC_size','GC_size']:reuse(lf,key)
for lf in[495,496,497]:
 u={495:'https://www.bizkaia.eus/ogasuna/guregida/noticia.asp?IdRegistro=900010980&idioma=ca',496:'https://web.araba.eus/documents/1247685/1248445/%C3%8DNDICES_NF%2BMECENAZGO-CAS.pdf/b51493c8-e36d-2090-bec3-908084e051c2?t=1673261049711',497:'https://www.gipuzkoa.eus/documents/2456431/2461522/NF%2B3-2004%2B%282020-1%29.pdf/a421e3bf-fdd3-35c8-25b2-3c756fc0be0c'}[lf]
 for q in(['30 por','35 por','cinco']if lf!=497 else ['20 por','30 por']):a(lf,u,q,'Own charitable-giving NF4/2019 art22 / A NF35/2021 arts19–22 / G NF3/2004 arts18–21')
for lf,suffixes in[(508,['rent']),(510,['rent','rentfinance','rentnonnegative']),(514,['rent','insurance']),(515,['rent70']),(516,['reference70','insurance']),(517,['reference70']),(518,['rent20']),(534,['rent','rent70','rent20','insurance'])]:
 for pref in['BP','AP','GP']:
  for suf in suffixes:reuse(lf,pref+'_'+suf)
for lf in[514,520,534]:reuse(lf,'AP_rural')
for lf in[520]:bag(lf,63,['viviendas'])
for lf,suf in[(522,'costs'),(526,'dep'),(527,'dep'),(528,'movables'),(529,'usufruct'),(530,'usufruct'),(532,'dep')]:
 for pref in['BR','AR','GR']:reuse(lf,pref+'_'+suf)
for lf,ar,qs in[(631,72,['65 por','33 por','24.250','8.000','cuarto']),(633,72,['24.250','prioridad','proporcional','cinco']),(635,9,['triple']),(637,72,['24.250','proporcional'])]:bag(lf,ar,qs)
bag(653,18,['pensiones']);bag(655,37,['diferencia positiva']);bag(655,19,['70 por','300.000']);bag(655,63,['37'])
for u in[B,A,G]:
 law(657,u,19,['60 por'])
 law(659,u,9,['quince años'])
 law(661,u,9,['quince años'])
 law(667,u,19,['70 por'])
 law(667,u,37,['diferencia positiva'])
# Own treaty progression, not assumed treaty-category eligibility.
law(685,G,75,['dos decimales']);law(685,G,76,['dos decimales']);law(689,G,75,['dos decimales']);law(689,G,77,['1.615']);bag(683,5,['tratados']);bag(687,5,['tratados']);a(687,'https://www.boe.es/buscar/act.php?id=BOE-A-2012-10212','tomar en consideración','Spain–Germany treaty22(1)(b), conditional progression not income-category entitlement')
for lf,u,ar in[(695,B,102),(695,A,102),(695,G,101)]:law(lf,u,ar,['20.000','1.600'])
# Personal business payment chapters are distinct, and their source paragraphs are preserved.
for lf,u,ar,qs in[(721,BR,109,['70 por']),(721,BR,110,['5 por','0,5 por','0,25 por','20 por','2 por']),(723,BR,111,['25','negativa']),(723,BR,110,['revisión']),(725,AR,106,['5 por','6 por','oficio']),(727,AR,107,['día uno']),(727,AR,106,['revisión']),(729,GR,121,['50 por','70 por']),(729,GR,122,['5 por','pérdidas']),(729,GR,123,['1 por']),(731,GR,124,['día 1']),(731,GR,124,['no resultasen'])]:law(lf,u,ar,qs)
# Existing own NFGT procedural quotations were actually selected/read for the ready payroll ledger.
pr=json.loads(Path('ledgers/spain-2026-evidence/es-foral-payroll/rows.json').read_text())
for lf,oldlf in[(745,183),(749,187),(750,188),(751,189),(754,192)]:
 for z in pr:
  if z['guide_LF']==oldlf:
   z=copy.deepcopy(z);z.update(id=len(L.rows)+1,guide_LF=lf,guide_wording=I[lf],section=next(x['section']for x in L.units if x['line']==lf));L.rows.append(z);L.sources[z['url']]=m['source'](z['url'])
# Mirror own Q1 relief from already-read corporate emergency instruments.
cr=json.loads(Path('ledgers/spain-2026-evidence/es-foral-corporate-tax/rows.json').read_text())
for z in cr:
 if z['guide_LF']==158:
  z=copy.deepcopy(z);z.update(id=len(L.rows)+1,guide_LF=741,guide_wording=I[741],section=next(x['section']for x in L.units if x['line']==741));L.rows.append(z);L.sources[z['url']]=m['source'](z['url'])
# Main oa control facts are hypothetical, rules remain the ordinary current22/23/75/76/77/95 chain.
for ar,qs in[(22,['Seguridad Social']),(23,['3.000']),(75,['18.080']),(76,['19,00']),(77,['1.615'])]:bag(766,ar,qs)
exec((L.p/'extra.py').read_text())
exec((L.p/'precision.py').read_text())
exec((L.p/'integrate-navarra.py').read_text())
exec((L.p/'navarra-supplement.py').read_text())
(L.p/'builder-errors.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
L.save()
runpy.run_path(str(L.p/'finalize-dispositions.py'))
print('ERRORCOUNT',len(E));print(*E,sep='\n')
