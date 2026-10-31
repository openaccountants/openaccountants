from pathlib import Path
import runpy,json,re
m=runpy.run_path('ledgers/spain-2026-evidence/group-b-ledger-lib.py');L=m['Ledger']('es-foral-payroll');I={x['line']:x['text']for x in L.units};E=[];BO='https://www.boe.es/buscar/act.php?id=';B='https://www.bizkaia.eus/documents/880307/15187815/ca_47_2014.pdf';A='https://web.araba.eus/documents/d/araba/indice-reglamento_irpf_cas-2-pdf';G='https://www.gipuzkoa.eus/documents/2456431/8.0755457E7/DF%2033-2014%20(2026-2).pdf/7e4c25eb-a139-fa5f-d310-deaa4c4bcffd';N='https://www.navarra.es/es/web/normativa-hacienda/-/reglamento-del-impuesto-sobre-la-renta-de-las-personas-f%C3%ADsicas-df-174/1999-de-24-de-mayo-?print=true'
def a(lf,u,q,p,kind='rule',note='',width=500):
 try:L.add(I[lf],u,q,p,kind,note,width)
 except Exception as e:E.append((lf,u,q,str(e)))
def table(lf,u,article,needle,occ=0):
 x=m['source'](u+'#a'+str(article));ls=[m['norm'](l)for l in x['text'].splitlines()if m['norm'](l).startswith(needle+' ')];
 if not ls:E.append((lf,u,needle,'table row missing'));return
 a(lf,u+'#a'+str(article),needle,'Own regulation article '+str(article)+' actual table row','statutory table','Whole row is quoted from actual current operative table, not from Guide transcription.');L.rows[-1]['quote']=ls[occ]
for lf,art,url,q in [(26,7,BO+'BOE-A-2002-9969#a7','centro de trabajo'),(28,10,BO+'BOE-A-1990-31117#a1-13','centro de trabajo')]:a(lf,url,q,'Economic Agreement article '+str(art))
for lf in range(46,81):
 if lf not in I or not I[lf].startswith('|'):continue
 needle=I[lf].split('|')[1].strip()
 for url,art in [(B,88),(A,84),(G,100)]:table(lf,url,art,needle)
for lf in range(98,106):
 needle=I[lf].split('|')[1].strip()
 for url,art in [(B,88),(A,84),(G,100)]:table(lf,url,art,needle,-1)
for lf in range(117,142):
 needle='Más de '+I[lf].split('|')[1].strip();table(lf,N,71,needle)
for lf,needle in [(155,'17.000,01 23.250'),(156,'23.250,01 41.250'),(157,'41.250,01 94.750'),(158,'94.750,01 En adelante')]:table(lf,N,71,needle)
for url,art in [(B,88),(A,84),(G,100)]:
 for lf,q,p in [(34,'Tabla general','summary35table'),(42,'20.000,01','flatnotmarginal'),(84,'percepción íntegra','annualgross'),(84,'variables previsibles','variablepay'),(85,'primero del año natural','familydate'),(85,'más de 30 años','age'),(86,'totalidad de las','wholepayment'),(87,'exclusivamente','prospectivechange'),(87,'anteriormente satisfechas','reengagement'),(88,'no podrá ser inferior al','contractfloors'),(94,'25 por','mobility'),(94,'65 por','disability'),(109,'elevación al año','pensionannualisation'),(109,'multiplicar por 100','dailyforecast'),(109,'duración indefinida','spousepension'),(200,'29.790,01','computedexample')]:a(lf,url+'#a'+str(art),q,'Own regulation '+str(art)+' '+p,'rule / computed application'if lf in[42,200]else'rule','Case325/150 uses30000forecast→13% less7points, then2500cash; computed, not statutory amount.'if lf==200 else'')
for lf,q,p in [(35,'Tabla de porcentajes','table25summary'),(113,'20.01.26','corrected2026commencement'),(145,'percepción íntegra','forecast'),(145,'ingreso a cuenta','inkindforecast'),(149,'primero de cada año','familydate'),(151,'inferiores a cero','disabilityfloor'),(160,'jornada incompleta','parttimefloor'),(160,'35 por 100','directors'),(162,'exclusivamente','prospectivechange'),(164,'con un hijo','pensioncolumn'),(164,'multiplicar por 100','dailyforecast'),(164,'pensión compensatoria','spousepension'),(219,'Más de 27.500','computedexample')]:a(lf,N+'#a'+('70'if p=='directors'else'71'),q,'DF174/1999 article '+('70'if p=='directors'else'71')+' '+p,'computed application'if lf==219 else'rule','30000→12.6%,2500×12.6%=315; 30250equality remains earlierrow; parttime1000×2%=20.'if lf==219 else'')
for lf,url,article,q,p in [(172,B,106,'veinticinco','filing25'),(173,A,104,'septiembre','July10September'),(173,A,104,'negativa','negative'),(174,G,120,'trimestralmente','frequency'),(175,N,90,'enero','generalclock'),(179,B,106,'negativa','negative'),(179,G,120,'negativa','negative'),(179,N,90,'negativa','negative')]:a(lf,url+'#a'+str(article),q,'Own regulation article '+str(article)+' '+p)
for lf,url,q,p in [(172,'https://www.bizkaia.eus/lehendakaritza/Bao_bob/2022/12/23/I-1160_cas.pdf?hash=7616a7ccaecc78b9aafa548934f8043a','enero','DF153/2022 DF1 Januaryextension'),(174,'https://www.gipuzkoa.eus/es/web/ogasuna/impuestos/modelo/110','25','G110currentclock'),(174,'https://www.gipuzkoa.eus/es/web/ogasuna/impuestos/modelo/111','septiembre','G111currentclock'),(174,'https://www.gipuzkoa.eus/es/web/ogasuna/impuestos/modelo/190','31 de enero','G190currentclock'),(175,'https://www.lexnavarra.navarra.es/detalle.asp?r=12301','agosto','OF25/2011quarter'),(175,'https://www.lexnavarra.navarra.es/detalle.asp?r=12301','septiembre','OF25/2011month'),(175,'https://www.lexnavarra.navarra.es/detalle.asp?r=37052','febrero','OF4/2016annual'),(177,'https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2022/12/23/c2208406.pdf','último día','OF575/2022January'),(177,'https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2022/12/23/c2208406.pdf','110','OF575/2022modeltable')]:a(lf,url,q,p)
for lf,url,arts in [(187,'https://www.bizkaia.eus/documents/880307/15187815/ca_2_2005.pdf?idioma=ca',[(26,'seis meses'),(27,'0,5'),(28,'20 por'),(196,'250'),(203,'400')]),(188,'https://web.araba.eus/documents/d/araba/indice-norma-foral-general-tributaria-cas-8-pdf',[(27,'seis meses'),(27,'doce meses'),(28,'10 por'),(195,'150'),(195,'30 por')]),(189,'https://www.gipuzkoa.eus/documents/2456431/8.6741042E7/NF%202-2005%20%282026%29.pdf/b8f36f3d-32d7-f2bf-c007-b7e250cb49e2',[(27,'tres meses'),(27,'intereses'),(28,'5 por'),(195,'150')]),(190,BO+'BOE-A-2001-3494',[(52,'1 por'),(52,'15 por'),(76,'180'),(77,'200'),(76,'55 por')])]:
 for ar,q in arts:a(lf,url+'#a'+str(ar),q,'Own procedure law article '+str(ar))
a(147,BO+'BOE-A-2022-22128#da-90','8.400','LPGE31/2022 DA90 annualIPREM14payments','combinedsource annualbasis','8400 and double16800 follow selected ownNavarraannualdependentbasis; not monthly7200test.')
for url,ar in [(B,87),(A,83),(G,99)]:
 a(86,url+'#a'+str(ar),'retribuciones dinerarias y en especie','Own regulation article '+str(ar)+' combinedinkind')
 a(84,url+'#a'+str(ar),'contribuciones','Own regulation article '+str(ar)+' excludedpensioncontributions')
a(147,'https://www.navarra.es/documents/48192/35409067/Manual%2Bte%C3%B3rico%2Bde%2Bla%2Bcampa%C3%B1a%2Bde%2B2025.pdf/c9e11ce5-ae6f-eb9a-040b-265f1f040525?download=true&t=1775726152475','8.400','Navarra2025manualannualdependentbasis','datedadministrativebasis','Actual2025manualpublishedin2026; current2026continuationis labelled inference with unchanged own law and indicator, not2026manual claim.')
for url,art in [(B,88),(A,84),(G,100)]:
 a(88,url+'#a'+str(art),'15 por','Own regulation '+str(art)+'15floor')
for lf,url,q,pr in [(168,G+'#a120','mensualmente','monthly category'),(183,B.replace('47_2014','2_2005')+'?idioma=ca#a26','Los intereses de demora se devengarán','administration procedure interest'),(192,A.replace('indice-reglamento_irpf_cas-2-pdf','indice-norma-foral-general-tributaria-cas-8-pdf')+'#a27','aplazamiento','unpaid filing and executive period'),(196,BO+'BOE-A-2002-9969#a7','centro de trabajo','work allocation')]:a(lf,url,q,pr)
for ar,qs in [(27,['5 por','0,5']),(28,['0,5','5 por'])]:
 for q in qs:a(187,'https://www.bizkaia.eus/documents/880307/15187815/ca_2_2005.pdf?idioma=ca#a'+str(ar),q,'Bizkaia NFGT '+str(ar))
for lf,url,ar,qs in [(188,'https://web.araba.eus/documents/d/araba/indice-norma-foral-general-tributaria-cas-8-pdf',195,['75 por','125 por','diez por']), (189,'https://www.gipuzkoa.eus/documents/2456431/8.6741042E7/NF%202-2005%20%282026%29.pdf/b8f36f3d-32d7-f2bf-c007-b7e250cb49e2',195,['80 por','75 por','105 por','10 por']), (190,BO+'BOE-A-2001-3494',52,['5 por','10 por'])]:
 for q in qs:a(lf,url+'#a'+str(ar),q,'Own procedure law article '+str(ar)+' supplementary rate')
for row in L.rows:
 if row['guide_LF']==200:
  x=m['source'](row['url']);row['quote']=next(m['norm'](z)for z in x['text'].splitlines()if '29.790,01'in z)
for u in ['https://www.bizkaia.eus/documents/880307/15187815/ca_13_2013.pdf/ce52e403-4fca-9ef7-bf85-2505ba29f921?t=1784098584068','https://web.araba.eus/documents/d/araba/indice_norma-foral_irpf_cas-4-pdf','https://www.gipuzkoa.eus/documents/2456431/8.0759126E7/NF%203-2014%20(2026-0).pdf/8ab5c95c-3f89-8fdf-5cb8-01950e3983cc']:
 a(85,u+'#a79','salario mínimo interprofesional','Own PIT79 descendant income gate')
a(147,'https://vivienda.castillalamancha.es/iprem','8.400','Official2026 indicator continuation')
if E:print('ERRORS',*E,sep='\n');(L.p/'draft-errors.json').write_text(json.dumps(E,indent=2))
else:L.save()
