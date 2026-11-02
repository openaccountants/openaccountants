from pathlib import Path
import runpy,json,re
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));R=E['ROOT'];Kit=runpy.run_path(str(P/'source-kit.py'))['Kit'];K=Kit(P);q=K.q
base=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');fresh=base/'spain-fresh-whole-pack-review-0f104150';g110=base/'spain-G110-January-extension-independent-review/sources'
for k,id in [('RIRPF','BOE-A-2007-6820'),('LIRPF','BOE-A-2006-20764'),('LGT','BOE-A-2003-23186'),('LIS','BOE-A-2014-12328'),('LIVA','BOE-A-1992-28740'),('RIVA','BOE-A-1992-28925'),('Order111','BOE-A-2011-4948'),('Order190','BOE-A-2009-18567'),('Electronic','BOE-A-2013-12385')]:K.cached(k,'https://www.boe.es/buscar/act.php?id='+id)
K.cached('Instructions','https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/pagos-cuenta/modelo-111-reten_____moniales-imputaciones-renta-autoliquidacion_/instrucciones.html')
for k,n,u in [('Calendar','AEAT-debit2026','https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html'),('August','AEAT-August2026','https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/agosto/hasta-20-agosto.html'),('RD960','State-RD960-2013-original','https://www.boe.es/buscar/doc.php?id=BOE-A-2013-12771')]:K.local(k,u,g110/(n+'.html'),g110/(n+'.reader.txt'))
Q={
'payer':[q('RIRPF','76','Las personas jurídicas'),q('RIRPF','76','cuando satisfagan rentas en el ejercicio de sus actividades'),q('RIRPF','76','sin mediación de establecimiento permanente')],
'scope':[q('Order111','2','rendimientos del trabajo'),q('Order111','2','explotación del derecho de imagen')],
'corporate':[q('LIRPF','8','Las personas físicas'),q('LIS','7','Las personas jurídicas'),q('LIRPF','27','rendimientos íntegros de actividades económicas')],
'15':[q('RIRPF','95','15 por ciento sobre los ingresos íntegros satisfechos')],
'start':[q('RIRPF','95','7 por ciento en el período impositivo de inicio',55),q('RIRPF','95','comunicación debidamente firmada')],
'artist':[q('RIRPF','95','inferior a 15.000 euros y represente más del 75',42)],
'agri':[q('RIRPF','95','engorde de porcino y avicultura: 1 por ciento'),q('RIRPF','95','Restantes casos: 2 por ciento'),q('RIRPF','95','con excepción de las subvenciones')],
'forest':[q('RIRPF','95','actividad forestal'),q('RIRPF','95','2 por ciento sobre los ingresos íntegros')],
'modules':[q('RIRPF','95','1 por ciento sobre los ingresos íntegros'),q('RIRPF','95','método de estimación directa')],
'employment':[q('RIRPF','80','Con carácter general, el tipo de retención que resulte según el artículo 86')],
'director':[q('RIRPF','80','35 por ciento'),q('RIRPF','80','19 por ciento'),q('RIRPF','80','100.000 euros')],
'course':[q('RIRPF','80','15 por ciento para los rendimientos derivados de impartir cursos')],
'rights':[q('RIRPF','101','24 por ciento'),q('RIRPF','101','19 por ciento'),q('RIRPF','101','15 por ciento'),q('RIRPF','101','7 por ciento')],
'image':[q('RIRPF','107','19 por ciento')],
'relief':[q('RIRPF','95','reducirán en un 60 por ciento'),q('LIRPF',None,'En los períodos impositivos 2022, 2023, 2024, 2025 y 2026',55),q('LIRPF',None,'en 2026, a partir de la entrada en vigor del Real Decreto-ley 23/2026',55)],
'paid':[q('RIRPF','78','momento en que se satisfagan o abonen')],
'base':[q('RIRPF','95','ingresos íntegros satisfechos'),q('LIRPF','28','normas del Impuesto sobre Sociedades')],
'inkind':[q('RIRPF','102','aplicando a su valor'),q('RIRPF','104','valor de mercado'),q('LIRPF','43','se adicionará el ingreso a cuenta')],
'counts':[q('Instructions',None,'Número total de personas físicas'),q('Instructions',None,'casilla 01'),q('Instructions',None,'casilla 07')],
'box01':[q('Instructions',None,'Casillas 01 y 07'),q('Instructions',None,'Casillas 02 y 08'),q('Instructions',None,'Casillas 03 y 09')],
'box04':[q('Instructions',None,'Casillas 04 y 10'),q('Instructions',None,'Casillas 05 y 11'),q('Instructions',None,'Casillas 06 y 12')],
'box13':[q('Instructions',None,'En las casillas 13, 14 y 15')],
'box19':[q('Instructions',None,'En las casillas 19, 20 y 21')],
'box25':[q('Instructions',None,'Casilla 25'),q('Instructions',None,'Casilla 26'),q('Instructions',None,'Casilla 27')],
'boxsum':[q('Instructions',None,'Casilla 28'),q('Instructions',None,'Exclusivamente en el supuesto de autoliquidación complementaria'),q('Instructions',None,'resultado habrá de ser siempre una cantidad positiva'),q('Order111','9','autoliquidación complementaria')],
'nil':[q('RIRPF','108','presentará declaración negativa'),q('RIRPF','108','No procederá presentación de declaración negativa')],
'annual':[q('RIRPF','108','relación nominativa de los perceptores'),q('RIRPF','108','las rentas exentas'),q('Order190','2','obligados')],
'credit':[q('LIRPF','99','causa imputable exclusivamente al retenedor')],
'70':[q('RIRPF','109','70 por ciento'),q('RIRPF','109','inicio de la actividad')],
'quarter':[q('RIRPF','108','primeros veinte días naturales de los meses de abril')],
'month':[q('RIRPF','108','veinte primeros días naturales de cada mes')],
'frequency':[q('RIVA','71','6.010.121,04 euros'),q('RIRPF','108','6 millones de euros')],
'working':[q('Order111','3','primer día hábil inmediato siguiente')],
'debit':[q('Calendar',None,'Con carácter general: domiciliación del 1 al 15 de enero'),q('Calendar',None,'7M 26: 1 al 17 de agosto')],
'190date':[q('Order190','5','31 de enero')],
'certificate':[q('RIRPF','108','con anterioridad a la apertura del plazo de declaración')],
'july':[q('RD960',None,'con efectos desde 1 de enero de 2014'),q('RD960',None,'en relación con las cantidades retenidas y los ingresos a cuenta que correspondan por el mes inmediato anterior, cuando se trate de retenedores',55),q('August',None,'Hasta el 20 de agosto'),q('August',None,'Julio 2026. Grandes empresas: 111'),q('Calendar',None,'7M 26: 1 al 17 de agosto')],
'electronic':[q('Electronic','3','sociedad anónima'),q('LGT','65','obligaciones tributarias que deban cumplir el retenedor')],
'late':[q('LGT','27','1 por ciento más otro 1 por ciento'),q('LGT','27','12 meses desde el término',50)],
'191':[q('LGT','191','Constituye infracción tributaria dejar de ingresar')],
'nilpenalty':[q('LGT','198','fija de 200 euros'),q('LGT','198','serán la mitad')],
'infopenalty':[q('LGT','198','20 euros por cada dato',50),q('LGT','198','serán la mitad')],
'collection':[q('LGT','26','interés de demora es una prestación accesoria'),q('LGT','28','recargos del período ejecutivo')],
'VAT21':[q('LIVA','90','21 por ciento')],
}
spec=[('makes legal','payer'),('[Orden EHA/586/2011 art. 2]','scope'),('An ordinary service','corporate'),('| Ordinary professional','15'),('| Starting professional','start'),('| Specified artistic','artist'),('| Agriculture/livestock','agri'),('| Forestry','forest'),('| Listed business','modules'),('| Ordinary employment','employment'),('| Director/board','director'),('| Courses/conferences','course'),('| Other listed rights','rights'),('| Special image-right','image'),('The start concession','start'),('The start concession','relief'),('[RIRPF art. 78]','paid'),('For an ordinary professional invoice','base'),('For a cash fee','base'),('For in-kind','inkind'),('Use the statutory form','counts'),('| Employment, cash','box01'),('| Employment, in kind','box04'),('| Economic activities, cash','box01'),('| Economic activities, in kind','box04'),('| Subject prizes','box13'),('| Public-forest','box19'),('| Same gains','box19'),('| Special art.','box25'),('`box28','boxsum'),('If subject income','nil'),("Reconcile the year's",'annual'),("The payer's 111",'credit'),("The payer's 111",'70'),('| Quarterly','quarter'),('| Monthly','month'),('| Ordinary turnover','frequency'),('| Non-working','working'),('| Direct debit','debit'),('| Electronic Modelo190','190date'),('| Electronic Modelo 190','190date'),('| Recipient certificate','certificate'),('The current [2026 calendar]','july'),('**Legislative bridge','july'),('Select electronic filing','electronic'),('| Unprompted late','late'),('| More than twelve','late'),('| Under-remitted','191'),('| Required nil','nilpenalty'),('| Annual information','infopenalty'),('Collection surcharges','collection'),('Classify the recipient','scope'),('Ceuta/Melilla and the dated La Palma','relief')]
b=(R/'skills/international/spain/es-modelo-111.md').read_text();rows=[]
for lf,sec,u in E['units'](b):
 if u.startswith(('---','#','<!--')) or 'Talk to a verified accountant' in sec or u.startswith(('|---','| Income/classification','| Category','| Obligation','| Situation')):continue
 used=[]
 for needle,k in spec:
  if needle in u and k not in used:used.append(k)
 status='Express rule / sourced administrative form coordinate / working-paper application'
 if 'worked examples' in sec.lower():used=['paid','15','start','box01','boxsum','VAT21'];status='Hypothetical case inputs and arithmetic derived from quoted legal rates and form coordinates; payroll410.50 is a stipulated sibling-example input'
 if sec.startswith('## Ask') or u.startswith('Compute the payer'):status='Operational intake/status, no new entitlement'
 if sec.startswith('## Sources'):used=[];status='Source bibliography or expressly retained source/factual boundary'
 selected=[z for k in used for z in Q[k]]
 for clause in E['clauses'](u):rows.append(dict(lf=lf,section=sec,wording=clause,authority='; '.join(dict.fromkeys(z['source']+' art.'+str(z['article']) for z in selected)) or status,url='; '.join(dict.fromkeys(z['url'] for z in selected)) or 'Current cited Sources; no separate legal amount',quote='; '.join(z['reader']+f' LF{z["LF_start"]}–{z["LF_end"]}: “'+z['quote']+'”' for z in selected) or 'Operational/bibliographic/precisely reserved wording. No fabricated statutory quote.',status=status))
result=E['render']('es-modelo-111',rows,[('February','Current Deadlines and filing / recipient certificate: certificate before recipient IRPF window; no universal1February requirement.'),('September','Current legislative bridge identifies RD960 replacement/current108/2026calendar; original form-order July exception retained historically, not controlling the current monthly route.'),('150%','Current Penalties: conduct-based LGT191 classification; no automatic universal150%.'),('037','Current Map and total the return: historical037 reference explicitly not treated as available2026form.')]);K.save();(P/'ledger-summary.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
