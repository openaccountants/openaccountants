from pathlib import Path
import json,runpy,re
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));R=E['ROOT'];Kit=runpy.run_path(str(P.parent/'es-modelo-111/source-kit.py'))['Kit'];K=Kit(P);q=K.q
for k,id in [('RIRPF','BOE-A-2007-6820'),('LIRPF','BOE-A-2006-20764'),('LGT','BOE-A-2003-23186'),('Order','BOE-A-2025-25272'),('Forms','BOE-A-2007-6032')]:K.cached(k,'https://www.boe.es/buscar/act.php?id='+id)
urls={
'I130':'https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html',
'I131':'https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-131-irpf______sionales-estimacion-objetiva-fraccionado_/instrucciones.html',
'Entry':'https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html',
'Note':'https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html',
'Interest':'https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html',
'Annex':'https://www.boe.es/boe/dias/2015/02/19/pdfs/BOE-A-2015-1656.pdf'}
for k,u in urls.items():K.cached(k,u)
Q={}
missing=[]
def add(k,src,art,*needles):
 Q[k]=[]
 for x in needles:
  try:Q[k].append(q(src,art,x,45))
  except (ValueError,StopIteration):missing.append((k,src,art,x))
add('who','RIRPF','109','obligados a autoliquidar','70 por ciento','inicio de la actividad')
add('partner','RIRPF','112','proporción a su participación')
add('direct','RIRPF','110','20 por ciento del rendimiento neto','trimestres anteriores')
add('objective','RIRPF','110','4 por ciento','3 por ciento','2 por ciento del volumen de ventas')
add('farming','RIRPF','110','forestales o pesqueras','subvenciones de capital y las indemnizaciones')
add('territory','RIRPF','110','reducirán en un 60 por ciento')
add('palma','LIRPF',None,'En los períodos impositivos 2022, 2023, 2024, 2025 y 2026','o en dichos ejercicios, para determinar el tipo del pago fraccionado')
add('5','Order',None,'5 por ciento')
add('home','RIRPF','110','33.007,2 euros','660,14 euros en cada trimestre','0,5 por ciento','importe acumulado en el período impositivo superior a 660,14 euros','construcción o ampliación')
add('higher','RIRPF','110','porcentajes superiores')
add('professional','RIRPF','95','7 por ciento en el período impositivo de inicio','15 por ciento sobre los ingresos íntegros satisfechos','comunicación debidamente firmada')
add('low','RIRPF','110','igual o inferior a 12.000 euros','Igual o inferior a 9.000','Entre 9.000,01 y 10.000','Entre 10.000,01 y 11.000','Entre 11.000,01 y 12.000','diferencia podrá deducirse')
# Full table pairs are separately retained from the actual article, not invented quote numbers.
add('lowinstruction','I130',None,'previos a la aplicación','Casilla 13')
add('dt32','LIRPF',None,'Para los ejercicios 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 y 2024')
add('limits','LIRPF','31','150.000 euros anuales','75.000 euros anuales','250.000 euros anuales','150.000 euros anuales')
add('aggregation','LIRPF','31','cónyuge, descendientes y ascendientes','se elevará al año')
add('ordergate','Order','3','magnitudes excluyentes')
add('entry','Entry',None,'Desde 2016 hasta 2026 inclusive los límites','Desde 2016 hasta 2026 inclusive el volumen de compras')
add('note','Note',None,'ambos no convalidados','Respecto al ejercicio 2026 se mantienen los límites')
add('basis','LIRPF','28','normas del Impuesto sobre Sociedades')
add('box','I130',None,'Casilla 05','Casilla 15','Casilla 16','Casilla 19')
add('negative','I130',None,'A deducir','Negativa')
add('homehistory','LIRPF',None,'Disposición transitoria decimoctava.','Los contribuyentes que hubieran adquirido su vivienda habitual con anterioridad a 1 de enero de 2013')
add('annex','Annex',None,'660,14 euros por trimestre','Total ( 14 – 15 – 16 )','Resultado de la autoliquidación ( 17 – 18 )')
add('modules','I131',None,'dos cifras decimales','25 por 100','Casilla 07','Casilla 15')
add('dates','RIRPF','111','entre el día 1 y el 20','entre el día 1 y el 30','declaración negativa')
add('form','Forms','1','modelo 130')
add('annual','LIRPF','79','Los pagos fraccionados')
add('payment','I130',None,'IBAN','Bizum','2025','SEPA','reconocimiento de deuda')
add('ceuta','LIRPF',None,'Disposición adicional sexagésima cuarta.','se inicie transcurrido un mes','será, durante el período impositivo 2026, del 10 por ciento')
add('late','LGT','27','1 por ciento más otro 1 por ciento','recargo será del 15 por ciento','se reducirá en el 25 por ciento')
add('collection','LGT','28','cinco por ciento','10 por ciento','20 por ciento')
add('191','LGT','191','50 por ciento','50 al 100 por ciento','100 al 150 por ciento')
add('nil','LGT','198','fija de 200 euros','serán la mitad')
add('interest','Interest',None,'4,0625')
add('interestlaw','LGT','26','interés de demora')
def span(key,src,lo,hi):
 z=dict(source=src,article='110.3.c table',url=K.sources[src]['url']+'#a110',quote='\n'.join(K.sources[src]['lines'][lo-1:hi]),reader=str(K.sources[src]['reader'].relative_to(P)),LF_start=lo,LF_end=hi,read_on='2026-10-28');K.quotes.append(z);Q[key].append(z)
span('low','RIRPF',6296,6310)
if missing:raise ValueError(missing)
spec=[('Ordinary common-territory','who'),('Test the withholding','who'),('For an income-attribution','partner'),('| Direct assessment','direct'),('| Objective assessment','objective'),('| Agriculture/','farming'),('| Qualifying Ceuta','territory'),('| Qualifying La Palma','palma'),('| Eligible activity','who'),('| General reduction','5'),('| Legacy','home'),('The taxpayer can elect','higher'),('The taxpayer can elect','professional'),('The prior-year low','low'),('| At most 9','low'),('| 9,000.','low'),('| 10,000.','low'),('| 11,000.','low'),('| Above 12','low'),('Use prior-year activity','lowinstruction'),('Ordinary statutory baseline','limits'),('| Non-agricultural activity receipts','limits'),('| Subset requiring','limits'),('| Agricultural/livestock/forestry receipts','limits'),('| Purchases/services','limits'),('Apply related-family','aggregation'),('Apply related-family','ordergate'),('The earlier25October','dt32'),('The earlier25October','note'),('The earlier25October','entry'),('For a full preceding year','entry'),('Use the underlying','basis'),('| 01–03','basis'),('| 04','direct'),('| 05','annex'),('| 06–07','direct'),('| 08–11','farming'),('| 12','annex'),('| 13–14','low'),('| 15','box'),('| 16','home'),('| 17–19','annex'),('Eligible year-to-date withholding','direct'),('A positive result','negative'),('First verify entitlement','homehistory'),('First verify entitlement','home'),('The current AEAT Modelo 130','annex'),('The current AEAT Modelo 130','home'),('Obtain an activity-specific','modules'),('Box 01 aggregates','modules'),('| Q1 / Q2','dates'),('| Q4','dates'),('| No amount payable','dates'),('| Forms and prescribed','form'),('Use the period','annual'),('For a payable Modelo130','payment'),('The instructions also','payment'),('**Ceuta 2026','ceuta'),('| Voluntary late','late'),('| Such return','late'),('| Conditions for surcharge','late'),('| Executive collection','collection'),('| Underpayment offence','191'),('| Ordinary late','nil'),('| Default interest','interest'),('Do not assign every','191'),('Ceuta/Melilla','palma')]
b=(R/'skills/international/spain/es-estimated-tax.md').read_text();rows=[]
for lf,sec,u in E['units'](b):
 if u.startswith(('---','#','<!--')) or 'Talk to a verified accountant' in sec or u.startswith(('|---','| Item |','| Prior-year net','| Preceding-year measure','| Box |','| Obligation |','| Event |')):continue
 ks=[]
 for n,k in spec:
  if n in u and k not in ks:ks.append(k)
 status='Express law / published administrative method; stated conflicts and precise limits retained'
 if 'worked examples' in sec.lower():ks=['direct','low','negative'];status='Computed hypothetical case amounts from the stated inputs and cited rules, not statutory amounts'
 if sec.startswith('## Ask') or sec.startswith('## Sources') or sec=='Metadata':ks=[];status='Operational intake, bibliography, attribution or precise evidence reservation'
 z=[a for k in ks for a in Q[k]]
 for clause in E['clauses'](u):rows.append(dict(lf=lf,section=sec,wording=clause,authority='; '.join(dict.fromkeys(x['source']+' art.'+str(x['article']) for x in z)) or status,url='; '.join(dict.fromkeys(x['url'] for x in z)) or 'See current Sources; no independent new entitlement',quote='; '.join(x['reader']+f' LF{x["LF_start"]}: “'+x['quote']+'”' for x in z) or 'No invented quote; operational text or expressly retained boundary.',status=status))
res=E['render']('es-estimated-tax',rows,[('250,000','Current objective entry table distinguishes statutory baseline and preserved published2026AEAT route; actual note after nonconvalidation supplied, neither repealed decree treated as live.'),('660.14','Current Legacy home adjustment explicitly corrects web annual-cap/reversed-subtraction errors against regulation and gazetted form.'),('bank','Current payment route restores the full bank/SEPA/NRC/card/Bizum/debt/transfer/current-account terms and retains2025paper vintage.')]);K.save();(P/'ledger-summary.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
