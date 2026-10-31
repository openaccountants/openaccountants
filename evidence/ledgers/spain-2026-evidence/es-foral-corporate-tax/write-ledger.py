from pathlib import Path
import runpy,json,copy,re
m=runpy.run_path('ledgers/spain-2026-evidence/group-b-ledger-lib.py');L=m['Ledger']('es-foral-corporate-tax');I={x['line']:x['text']for x in L.units};E=[];BO='https://www.boe.es/buscar/act.php?id=';B='https://www.bizkaia.eus/documents/880307/15187815/ca_11_2013.pdf/5a463c1d-a59b-7e48-6429-80fd22f30bc6?t=1768908575887';A='https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas-3-pdf';AF='https://web.araba.eus/documents/d/araba/norma-foral-del-impuesto-sobre-sociedades_cas';G='https://www.gipuzkoa.eus/documents/2456431/8.0761374E7/NF%202-2014%20%282026%29.pdf/f1231a01-1f83-ee15-e569-7b9b84d44d54';N=BO+'BOE-A-2017-2356';BR='https://www.bizkaia.eus/documents/880307/15187815/ca_203_2013.pdf/5d2f80fc-9d5b-0f71-b578-56da0a5a0c50?t=1679483614806';AR='https://web.araba.eus/documents/d/araba/indice-reglamento-del-impuesto-sobre-sociedades-cas-5-pdf';GR='https://www.gipuzkoa.eus/documents/2456431/8.0761381E7/DF%2017-2015%20%282026%29.pdf/ad233e14-7236-0450-948f-50a669df270f';NR='https://www.navarra.es/documents/48192/6699806/Reglamento%20IS.pdf/ea37edba-eb1b-22d7-a04b-9f9d8fbba4e6'
def a(lf,u,q,p,kind='rule',note='',width=480):
 variants={'3 millones':['tres millones'],'quince':['15 años'],'tres':['3 primeros'],'pagos fraccionados':['pago a cuenta'],'10 empleados':['10 personas empleadas'],'50 empleados':['50 personas empleadas'],'250 empleados':['250 personas empleadas'],'1 millón':['un millón','1.000.000'],'20 millones':['veinte millones'],'90 días':['noventa días'],'cinco años':['5 años','cinco períodos'],'un año':['un año','año anterior'],'ocho años':['8 años','8 ejercicios'],'10 por':['diez por'],'formulación de las cuentas':['formular cuentas anuales'],'recuperación':['reversión'],'Edificios':['Edificios'],'octava':['12,50'],'20 por':['20 puntos','20 por','cinco puntos porcentuales','5 puntos porcentuales'],'100.000':['cien mil','100.000 euros'],'30 años':['treinta','30 períodos'],'5 por':['cinco por'],'cinco':['5 periodos','5 períodos','5 ejercicios'],'no pueda exceder':['no podrá ser inferior','no puede dar lugar'],'tres años':['3 años','tres si'],'5 millones':['cinco millones','5.000.000'],'170 por':['70 por'],'35 por':['35%','35 por'],'valor de mercado':['normal de mercado'],'45 millones':['45.000.000','45 millo-','cuarenta y cinco millones']}
 for needle in [q]+variants.get(q,[]):
  try:L.add(I[lf],u,needle,p,kind,note,width);return
  except Exception as e:last=e
 E.append((lf,u,q,str(last)))
def law(lf,u,ar,qs,kind='rule',note=''):
 for q in qs:a(lf,u+(('#ar-'if u==N else'#a')+str(ar) if ar!='' else ''),q,('Navarra LF26/2016'if u==N else'Own Basque corporate law')+' article '+str(ar),kind,note)
def bag(lf,ar,qs,kind='rule',note=''):
 for u in [B,A,G]:law(lf,u,ar,qs,kind,note)
for lf,ar,qs in [(28,15,['12 millones','dos decimales']),(30,14,['75 por ciento']),(34,16,['15 por 100']),(36,17,['pago fraccionado']),(45,15,['12 millones'])]:law(lf,BO+'BOE-A-2002-9969',ar,qs)
for lf,anchor,qs in [(28,'a1-22',['doce millones']),(32,'a1-21',['75 por ciento']),(34,'a2-14',['15 por ciento']),(36,'a2-17',['pago a cuenta'])]:
 for q in qs:a(lf,BO+'BOE-A-1990-31117#'+anchor,q,'Navarra Economic Agreement own allocation')
bag(30,2,['domicilio fiscal']);bag(42,56,['20 por']);bag(43,56,['24 por']);law(44,N,51,['28 por','25 por','23 por','19 por'])
for lf,qs in [(54,['2 millones','10 empleados']),(55,['10 millones','50 empleados']),(56,['43 millones','250 empleados']),(57,['25 por','letras b) y c)']),(58,['período impositivo anterior','grupo de sociedades']),(60,['85 por']),(62,['letras b) y c)']),(64,['85 por'])]:bag(lf,13,qs)
for lf,qs in [(54,['1 millón']),(55,['20 millones']),(57,['25 por']),(58,['grupo de sociedades'])]:law(lf,N,12,qs)
law(60,N,51,['50 por']);bag(66,14,['90 días','75 por']);law(66,N,8,['patrimonial'])
law(64,B,13,['tres']);law(64,A,13,['cinco']);law(64,G,13,['arrendamiento'])
bag(72,15,['resultado contable']);law(72,N,42,['artículo 43']);bag(76,31,['multas','Impuesto sobre Sociedades']);law(76,N,23,['multas']);bag(77,31,['50 por','5 por','300 euros']);law(77,N,23,['50 por','1 por','300 euros'])
bag(78,31,['vehículos']);bag(79,'25bis',['30 por','3 millones','cinco años']);law(79,N,24,['30 por','1 millón','quince']);bag(80,33,['5 por','3 por','un año']);law(80,N,35,['5 por','gestión'])
bag(82,'25bis',['70 por','ocho años']);law(82,N,24,['70 por','ocho años'])
bag(86,33,['50 por','mutuas']);bag(88,33,['10 por','patrimoniales']);law(88,B,33,['tres años']);law(88,A,33,['tres años']);bag(90,33,['50 por'],'computed illustration','10000×50%=5000base,24%=1200; counterfactual full2400 or exempt0, conditional on actual domestic payer/no33.3 exclusion.')
bag(94,22,['insolvencias']);law(98,B,22,['formulación de las cuentas','seis meses']);law(99,A,22,['formulación de las cuentas','seis meses']);law(100,G,22,['devengo','seis meses']);law(101,N,20,['devengo','seis meses']);bag(103,22,['garantizados','vinculadas']);law(103,N,20,['liquidación','garantizados']);bag(105,22,['1 por','saldo']);law(105,N,20,['globales']);bag(107,22,['seis meses'],'computed dates','Due31August2026→4monthsat31December vs6monthsby31March2027 formulation date; no court event assumed.');bag(109,22,['1 por'],'computed allowance','(500000−100000−50000)×1%=3500closing ceiling;old2000allows1500addition, subject booked expense.');bag(109,54,['recuperación'])
for lf in [113,115,116,117,118,120,122]:bag(lf,40,['valor contable'if lf==117 else 'depreciación monetaria'],'computed interpretation'if lf==120 else'rule','Case100000×1.071−3000×1.040−3000×1.020−94000=6920;56000−6920=49080;positive5000caps deduction5000;loss0.'if lf==120 else'')
for u in [B,A]:law(127,u,31,['3.000','30.000','3.600','7.200','40.000','intereses'])
law(129,G,31,['3.000','30.000','3.600','7.200','40.000']);law(131,N,23,['25.000','4.000','7.000'])
for lf,q in [(137,'Edificios'),(138,'uso industrial'),(139,'Instalaciones'),(140,'Maquinaria'),(141,'Maquinaria'),(142,'Mobiliario'),(143,'informáticos'),(144,'Autobuses'),(145,'Moldes'),(146,'Otros')]:
 bag(lf,17,[q]);law(lf,NR,3,[{137:'Edificaciones',138:'uso industrial',140:'Maquinaria',143:'Equipos para',144:'Elementos de transporte (autobuses',146:'Otro inmovilizado'}.get(lf,q)])
bag(148,17,['15 años','50 años','25 años']);law(148,N,16,['funcionamiento'])
bag(150,21,['1.500','1,5','25 por']);law(150,B,21,['20.000','40.000']);law(150,A,21,['20.000','40.000']);law(150,N,18,['1.800']);law(150,N,16,['1,5']);bag(152,20,['décima']);bag(152,25,['octava']);law(152,N,17,['décima'])
for u in ['https://www.bizkaia.eus/lehendakaritza/Bao_bob/2026/04/20/I-441_cas.pdf','https://www.araba.eus/botha/Boletines/2026/045/2026_045_01089_C.pdf','https://www.gipuzkoa.eus/documents/2456431/8.813641E7/DF-Norma%202-2026%20medidas%20para%20mitigar%20Crisis%20Oriente%20Medio.pdf/925d814a-7f73-6e58-f249-a1437b1d76bf']:
 a(156,u,'1,5','Own2026 emergency art4 accelerated depreciation');a(158,u,'primer trimestre','Own2026 emergency art3 PITonlyinstalment');a(250,u,'2026','Own2026 hiring overlay');a(262,u,'45 por' if 'bizkaia' in u else '10 puntos','Own2026 women/young hiring overlay')
bag(162,32,['15 por'],'computed microbase','100000×85%=85000 before losses;no quota discount.');bag(164,51,['15 por','20 por','cinco años']);bag(166,52,['10 por','15 por','25 por','diez años','5 por']);law(166,B,52,['20 por']);law(166,A,52,['30 por']);law(166,G,52,['30 por']);law(168,B,53,['65 por','45 por','50 por']);law(168,A,53,['65 por','45 por','50 por']);law(168,G,53,['60 por','45 por','50 por']);law(168,B,53,['100.000']);law(168,A,53,['100.000']);bag(168,53,['15 por']);law(170,N,44,['45 por','60 por','40 por']);law(170,N,45,['50.000']);law(170,N,45,['dos años']);a(170,'https://www.boe.es/buscar/doc.php?id=BOE-A-2026-10888','31 de diciembre de 2027','Navarra DLF1/2026 materialisationextension')
bag(174,55,['30 años','50 por','microempresas']);bag(176,55,['cinco','15 por']);law(178,N,43,['quince','70 por','1 millón','tres'])
for lf,qs in [(186,['20 por']),(187,['24 por']),(188,['28 por']),(194,['24 por'])]:bag(lf,56,qs)
law(186,N,51,['19 por','23 por']);law(187,N,51,['28 por','25 por']);law(190,N,51,['igualdad','tres'])
bag(195,60,['30 años','no tendrá la consideración de gasto']);bag(196,67,['35 por','70 por','50 por']);bag(197,59,['no pueda exceder']);bag(198,68,['retenciones']);
for lf,q in [(202,'70 por'),(203,'50 por'),(204,'35 por'),(205,'62'),(207,'30 años')]:bag(lf,67 if lf!=205 else 59,[q])
for lf,q in [(211,'19 por'),(212,'17 por'),(213,'15 por'),(214,'15 por'),(215,'13 por'),(217,'cinco')]:
 for u in [B,G]:law(lf,u,59,[('Estas entidades aplicarán' if lf==213 else ('Del 13 por' if u==B else 'serán del 11') if lf==215 else q)])
for lf,q in [(211,'19 por'),(212,'17 por'),(213,'15 por'),(214,'15 por'),(215,'15 por')]:law(lf,A,59,['Estas entidades aplicarán' if lf==213 else q])
for u in [BR,GR]:law(219,u,'33bis',['inversiones'])
for lf in [223,225]:law(lf,A,59,['inversiones'],'labelled own-law amount-only interpretation','Source-derived potential-investment reading, not enacted Álava33bis;5000machine no art61 credit;separate6000claimleaves18000;8000claimlimited7000/carry1000.');law(lf,A,61,['10 por']);law(lf,A,67,['35 por'])
a(227,'https://www.araba.eus/botha/Boletines/2025/147/2025_147_03861_C.pdf','2035','NF21/2025 art3Quinto temporary19default');a(227,'https://www.araba.eus/botha/Boletines/2025/044/2025_044_01182_C.pdf','2026','NF3/2025 article12/DF1 effectchain')
law(231,N,53,['18 por','16 por','13 por','11 por','10 por']);law(233,N,53,['apartado'],'labelled conditionalminimum calculation','Foreignonly10000/Z100000→8000;foreign6000+film5000→minimum13000/effective17000;foreign16000→QL12000 retainforeign/no incompatiblepositivefilmclaim.');law(235,N,67,['25 por','quince'])
bag(243,67,['subvenciones','tres años','cinco años']);law(243,N,67,['subvenciones']);bag(247,61,['10 por','líquida del 5','5 millones']);law(247,N,58,['10 por']);law(247,N,59,['6.000','300.000']);bag(248,62,['30 por','50 por','20 por','10 por']);law(248,N,61,['40 por','10 por']);bag(249,63,['15 por','20 por','1 millón']);law(249,N,61,['15 por']);bag(252,66,['170 por','tres']);bag(254,62,['25 por']);law(254,N,61,['informe']);law(256,N,66,['10 por','27.000']);law(258,N,63,['30.000','Exceso hasta 60.000','40 por']);law(258,N,64,['15 por','30 por','35.000','150.000','200.000','30.000','1.500.000'])
for lf,ars,qs in [(262,['66decies','66octies','66octies'],['35 por','10 por','70 por']),(264,['66sexies','66quinquies','66quater'],['5 por','15 por','2.500','7.500']),(266,['66septies','66sexies','66quinquies'],['15 por','20 por','25 por','1,5']),(266,['66octies','66septies','66sexies'],['10 por','1,5']),(272,['66nonies','61bis','66septies'],['10 por','3.000','500','15.000','20.000'])]:
 for u,ar in zip([B,A,G],ars):law(lf,u,ar,qs)
for lf in [268,270]:
 for u in[B,A,G]:a(lf,u,'las contribuciones realizadas a sistemas de previsión social de empleo','Own corporate transitional employer-pension DAs','combined law / computed case','Beginning2025–29 below1.5%:preferred10%/other5%;1%of100000=1000→100/50;at1500 permanent225/150;no same-expense duplicated credit.')
law(272,A,'61ter',['15 por','5.000','25.000','10.000']);bag(274,65,['35 por','15 por']);law(276,B,67,['subvenciones'],'computed environmental base','20000×.76=15200;100000−15200=84800×.35=29680.');
for u in[A,G]:law(276,u,65,['subvenciones'],'computed environmental base','100000−20000=80000×.35=28000;territorialdifference1680.')
for u in[B,A]:law(278,u,'66bis',['25 por','35 por','cinco años'])
law(280,B,'66ter',['10 por','15 por']);law(282,N,62,['1,20','contrato']);law(284,N,56,['diez años']);law(284,N,57,['diez años'])
# Existing selected provincial information-return and procedural quotations, actually read in this ledger phase.
pr=json.loads(Path('ledgers/spain-2026-evidence/es-foral-payroll/rows.json').read_text())
for lf,oldlf in [(355,183),(359,187),(360,188),(361,189),(362,190),(364,192)]:
 for z in pr:
  if z['guide_LF']==oldlf:
   z=copy.deepcopy(z);z.update(id=len(L.rows)+1,guide_LF=lf,guide_wording=I[lf],section=next(x['section']for x in L.units if x['line']==lf));L.rows.append(z);L.sources[z['url']]=m['source'](z['url'])
# Surcharge and accounting interpretations are source-derived, not quotations of an official algebra.
for lf in [292,296,298,301,303,307,308,309,310,311,313,315]:
 for u,ar in [(B,'57bis'),(A,56),(G,56)]:law(lf,u,ar,['cuota íntegra' if u==B else 'resultado contable positivo'],'labelled source-derived method / computed illustration','Own gross-quota attribution;115000fullytaxableexcess→36+120+180+480=816;notuniversalBI/Rallocation. Allcase amountscomputed;35/50/75/100bands fromownprovision.')
for u,da in [(BR,'décima'),(GR,'novena')]:
 for lf in [294,298,303]:a(lf,u,'deterioro','Own regulation surcharge measure DA '+da)
for lf in [319,321,323,325,327,329,333,334,335,336,337,339,341]:
 law(lf,AF,56,['incremento de la base imponible'],'labelled Álava correspondence interpretation / computed case','Literal BI-threshold alternative remains explicit;netPGCcurrenttax-only worksheet,notbindingruling/universalR. ExactS29432841/111746;display263.39;Q45863.39;derivedfeedbackinputsnotprintedlawamounts.')
law(319,'https://web.araba.eus/documents/d/araba/indice-norma-foral-general-tributaria-cas-8-pdf',11,['sentido jurídico']);law(319,BO+'BOE-A-1885-6627',35,['resultado']);a(323,BO+'BOE-A-2007-19884','impuesto corriente y diferido','PGCNRV13.4 taxexpense');law(323,AF,31,['Impuesto sobre Sociedades']);a(341,'https://web.araba.eus/documents/d/araba/norma-foral-del-imic','59','NF17/2025 DF1/DA31 surcharge exception');a(341,'https://www.araba.eus/botha/Boletines/2025/147/2025_147_03861_C.pdf','2030','NF21/2025 article3Cuarto 2026–30')
bag(345,'130bis',['5 por','octubre']);law(347,N,68,['30 por','20 por','nueve']);a(349,'https://www.bizkaia.eus/lehendakaritza/Bao_bob/2026/06/15/I-678_cas.pdf','2025','OF298/2026 periodscope');bag(351,126,['seis meses','25 días']);law(351,N,75,['quinto','séptimo'])
bag(368,42,['25 por','valor de mercado']);law(368,N,28,['25 por']);bag(372,43,['250.000','400.000','20 por','15 por']);bag(373,43,['500.000']);law(373,N,30,['250.000']);law(374,NR,31,['45 millones']);bag(377,43,['36.000','60.000','dos puntos']);law(379,'https://www.lexnavarra.navarra.es/detalle.asp?r=50181','',['250.000','100.000','50 por']);bag(383,43,['750 millones'])
for lf,u in [(391,'https://www.bizkaia.eus/lehendakaritza/Bao_bob/2018/06/20/I-614_cas.pdf?hash=2b88ef4ffa0b9176fffed62d97b059cb'),(392,'https://www.araba.eus/botha/Boletines/2018/076/2018_076_02511_C.pdf'),(393,'https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2018/09/20/c1806246.pdf')]:
 a(lf,u,'36.000','Own model232 orderarticle2');a(399,u,'diez meses','Own model232 orderfiling');a(395,u,'consolidación','Own model232 orderexceptions');a(397,u,'devengo','Own model232 ordertiming');a(401,u,'36.000','Own model232 orderboundary','computed strictthreshold','36000equalnotcross;36000.01cross;20000services+20000differenttype→B40000aggregate, A/Gseparategroups20000 each.')
for lf in[407,441]:
 law(lf,N if lf==441 else B,67,['25 por'if lf==441 else'35 por'],'computed main example','Allcasefactsandderivedamountscomputed;2existingoa retained byteexact;microbase/size/minimum independentlyclassified.')

# Exact own form distinction; 2025 annex is corroboration, not a 2026 surcharge form.
a(323,'https://www.araba.eus/botha/Boletines/2026/073/2026_073_01914_C.pdf','1000','OF380/2026 annex 2025 return field1000','administrative corroboration',width=260)
a(323,'https://www.araba.eus/botha/Boletines/2026/073/2026_073_01914_C.pdf','1005','OF380/2026 annex 2025 return field1005','administrative corroboration',width=300)
law(375,NR,30,['estructura','intangibles','financiación']);law(375,NR,31,['comparabilidad','Conciliación'])
for q in ['Modelo 232','Modelo 231']:a(381,'https://web.araba.eus/documents/d/araba/b_plazos-de-presentacion_2026_es-pdf',q,'Álava actual2026calendar page15',width=700)
for u in ['https://www.bizkaia.eus/lehendakaritza/Bao_bob/2018/06/20/I-614_cas.pdf?hash=2b88ef4ffa0b9176fffed62d97b059cb','https://www.araba.eus/botha/Boletines/2018/076/2018_076_02511_C.pdf','https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2018/09/20/c1806246.pdf']:
 a(387,u,'Estarán obligados a presentar','Ownmodel232order art2 localpopulation',width=900)


# Selected coefficient rows from exact own provincial CIT tables, not the PIT table.
cr=json.loads(Path('ledgers/spain-2026-evidence/es-foral-non-resident-tax/quotes.json').read_text())
for place in ['bizkaia','araba','gipuzkoa']:
 for year in [2023,2024,2025]:
  z=cr['CIT_coef_'+place+'_2026_'+str(year)];u=z['url'];x=m['source'](u)
  L.sources[u]=x;L.rows.append(dict(id=len(L.rows)+1,section=next(v['section'] for v in L.units if v['line']==120),guide_LF=120,guide_wording=I[120],provision=z['article'],url=u,quote=z['quote'],read_on='2026-10-28',kind='statutory coefficient / computed illustration',note='Own CIT coefficient row; native LF '+str(z.get('LF_start'))+'–'+str(z.get('LF_end'))+'; hypothetical cost/depreciation amounts and arithmetic computed.',raw_sha256=x['actual_raw_sha256'],reader=x['reader']))


for u,ar in [(B,'57bis'),(A,56),(G,56)]:
 for k in [1,2,3,4]:law(296,u,ar,['tipo adicional del '+str(k)],'labelled own-law correspondence / statutory band','Actual gross-quota band wording; no universal allocation or official algebra asserted.')
for u in[B,A,G]:
 for lf in[268,270]:a(lf,u,'las contribuciones realizadas a Planes de Previsión Social Preferentes' if u!=G else 'contribuciones realizadas a planes de previsión social preferentes','Own transitional preferred pension DA','transitional rule / computed case',width=1000)


law(258,N,64,['sin que en ningún caso supere','no genera emisiones','capacidad mayor de 2kWh','dos fuentes de energía','autoconsumo compartido','sistema hidráulico','hasta un máximo de 15','bombas de calor','tengan carácter obligatorio','informe acreditativo','30 por 100 si son vehículos eléctricos','L1e y L2e:','L3e, L4e y L5e:','L6e y L7e:','acceso público','inferior 22 kW','superior a 22 kW','potencia normal:','hasta 50 kW:','el exceso podrá acogerse','fecha de la Resolución','importe percibido','contabilización dentro','opción de compra'])
law(258,N,63,['patrocinadas informen','juego'])


for u in [BR,GR]:
 for q in ['resultados contables negativos o cero','durante los cuatro primeros','periodo de un año consecutivo','cuentas contables consolidadas','Tampoco resultará de aplicación']:
  a(294,u,q,'Own regulatory surcharge DA10/DA9 scope',width=650)

if E:print('ERRORS',*E,sep='\n');(L.p/'draft-errors.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
else:
 exec((L.p/'precision.py').read_text())
 L.save()
 __import__('runpy').run_path(str(L.p/'S-L21-preserve-ledger.py'))
