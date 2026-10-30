from pathlib import Path
import json,runpy,re
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));R=E['ROOT'];Kit=runpy.run_path(str(P.parent/'es-modelo-111/source-kit.py'))['Kit'];K=Kit(P);q=K.q;b=(R/'skills/international/spain/es-capital-gains.md').read_text();B=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');F=B/'spain-fresh-whole-pack-review-0f104150'
for k,id in [('L','BOE-A-2006-20764'),('R','BOE-A-2007-6820'),('N','BOE-A-2004-4527'),('NR','BOE-A-2004-14532'),('O210','BOE-A-2010-19707'),('LGT','BOE-A-2003-23186')]:K.cached(k,'https://www.boe.es/buscar/act.php?id='+id)
u='https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/determinacion-bi-irnr-sin-establecimiento-permanente/ganancias-patrimon-proced-bienes-adquiridos-1994.html';K.cached('Nold',u)
u='https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/que-ocurre-cuando-vendo-inmueble/transmision-vivienda-habitual-mayores-65-anos.html';s=B/'spain-ownership-SC-scope-independent-review/sources';K.local('Ownership',u,s/'AEATownership.body',s/'AEATownership.reader.txt')
for k,id,raw in [('D29','2026-20823','25560a7b8c1e1329f3c2'),('D26','2026-20266','0b52c942f87fea673eb5'),('Repeal','2026-20526','f39e1b97fbfaa403f985')]:K.local(k,'https://www.boe.es/buscar/doc.php?id=BOE-A-'+id,F/'sources'/(raw+'.body'),B/'spain-fresh-review-repairs/root-remaining-primary-reads-20261028'/(raw+'.reader.txt'))
K.local('RDL18','https://www.boe.es/buscar/act.php?id=BOE-A-2012-6280',P/'sources/RDL18.body',P/'sources/RDL18.reader.txt')
Q={};missing=[]
def add(k,src,art,*needles):
 Q[k]=[]
 for n in needles:
  try:Q[k].append(q(src,art,n,55,scope=(11533,11605) if k=='old' else (10070,10090) if k=='2012' else (12137,12145) if k=='rights' else None))
  except (ValueError,StopIteration):missing.append((k,src,art,n))
def span(k,src,art,lo,hi):
 z=dict(source=src,article=art,url=K.sources[src]['url']+('#a'+art if art.isdigit() else ''),quote='\n'.join(K.sources[src]['lines'][lo-1:hi]),reader=str(K.sources[src]['reader'].relative_to(P)),LF_start=lo,LF_end=hi,read_on='2026-10-28');K.quotes.append(z);Q.setdefault(k,[]).append(z)
for art in ['66','76']:
 a=K.sources['L']['lines'];st=next(i for i,x in enumerate(a) if x.startswith('Artículo '+art+'.'));st=next(i for i in range(st,len(a)) if a[i].strip()=='0')
 for j in range(5):span('scale'+str(j),'L',art,st+1+j*5,st+4+j*5)
add('class','L','33','variaciones en el valor del patrimonio','alteración en la composición')
add('savings','L','46','transmisiones de elementos patrimoniales')
add('business','L','28','no se incluirán las ganancias o pérdidas patrimoniales')
add('deathgift','L','33','transmisiones lucrativas por causa de muerte','división de la cosa común','transmisiones lucrativas por actos ínter vivos')
add('minimum','L','56','base liquidable general','base liquidable del ahorro')
add('minscale','L','66','se minorará en el importe derivado de aplicar')
add('loss','L','49','25 por ciento','cuatro años siguientes','cuantía máxima que permita')
add('repurchase','L','33','dos meses anteriores o posteriores','año anterior o posterior','año siguiente','se integrarán a medida que se transmitan')
add('otherloss','L','33','consumo','no justificadas','juego')
add('sale','L','35','importe real por el que dicha adquisición','inversiones y mejoras','excluidos los intereses','normal de mercado','gastos y tributos a que se refiere la letra b)')
add('depreciation','R','40','amortización mínima','independencia de la efectiva consideración')
add('giftbasis','L','36','normas del Impuesto sobre Sucesiones y Donaciones','pactos sucesorios','posición del donante')
add('listed','L','37','cotización en dichos mercados en la fecha','precio pactado')
add('unlisted','L','37','El valor de transmisión así calculado se tendrá en cuenta para determinar el valor de adquisición de los valores o participaciones que corresponda al adquirente','El valor del patrimonio neto que corresponda a los valores transmitidos resultante del balance correspondiente al último ejercicio cerrado','devengo del Impuesto','capitalizar al tipo del 20 por ciento','tres ejercicios sociales','dividendos distribuidos','condiciones normales de mercado','valor de adquisición')
add('bonus','L','37','parcialmente liberadas','totalmente liberadas','derechos de suscripción')
add('fifo','L','37','se considerará que los transmitidos por el contribuyente')
add('rights','L',None,'se deducirá el importe obtenido por las transmisiones de derechos de suscripción realizadas con anterioridad a 1 de enero de 2017','con excepción del importe de tales derechos','se entenderá que los transmitidos correspondieron a los valores adquiridos en primer lugar')
add('home','R','41','principal del préstamo','período no superior a dos años','plazo de los dos años anteriores','parte proporcional de la ganancia','intención de reinvertir','25 por ciento')
add('over65','L','33','mayores de 65 años','dependencia severa o de gran dependencia')
add('ownership','Ownership',None,'nuda propiedad','usufructuario','pleno dominio')
add('homegates','R','41 bis','tres años','doce meses','dos años anteriores')
add('annuity','R','42','mayores de 65 años','El contrato de renta vitalicia deberá suscribirse entre el contribuyente','El incumplimiento de cualquiera de las condiciones establecidas en este artículo, o la anticipación','seis meses','se destine íntegramente','finalización del ejercicio siguiente','periodicidad inferior o igual al año','plazo de un año','cinco por ciento','comunicar a la entidad aseguradora','240.000 euros','parte proporcional de la ganancia','reinversiones anteriores','intención de reinvertir','autoliquidación complementaria')
add('annuitydeath','R',None,'únicamente podrá existir un potencial beneficiario','no podrán exceder de 10 años','no resultará de aplicación a los contratos de seguros de vida')
span('annuitytable','R','DA9',7102,next(i+1 for i,x in enumerate(K.sources['R']['lines']) if i>7102 and x.strip()=='50 por 100'))
add('relocation','R','41 bis','por razón de su edad o situación de dependencia','trasladó su residencia a un centro especializado o al domicilio de un familiar','o en el supuesto de transmisión por personas mayores de 65 años','tercer grado','separación, divorcio o nulidad','cuando tal situación concurra en el cónyuge que permaneció en la misma')
add('currentdate','D29',None,'Disposición final tercera.','Disposición final decimoprimera.','entrará en vigor el día siguiente al de su publicación','08/10/2026')
add('priordate','D26',None,'Disposición final tercera.','Disposición final undécima.','entrará en vigor el día siguiente al de su publicación','01/10/2026')
add('repeal','Repeal',None,'derogar el Real Decreto-ley','02/10/2026')
add('old','L',None,'adquiridos con anterioridad a 31 de diciembre de 1994','fecha de adquisición y el 19 de enero de 2006, ambos inclusive','redondeado por exceso','un 11,11 por ciento','un 25 por ciento','un 14,28 por ciento','superior a diez, cinco y ocho años','desde 1 de enero de 2015 hasta la fecha','Cuando sea inferior a 400.000 euros','Cuando sea superior a 400.000 euros','a efectos del Impuesto sobre el Patrimonio del año 2005','con más de tres años de antelación','Si se hubiesen efectuado mejoras en los elementos patrimoniales transmitidos')
add('generalpool','L','48','ganancias y pérdidas patrimoniales')
add('territory','L','68','60 por ciento','ganancias patrimoniales')
add('2012','L',None,'50 por ciento las ganancias patrimoniales','a partir de la entrada en vigor del Real Decreto-Ley 18/2012','segundo grado','una vez aplicada la exención prevista en esta disposición adicional')
add('N2012','N',None,'50 por ciento las ganancias patrimoniales','a partir de la entrada en vigor del Real Decreto-Ley 18/2012','Disposición transitoria primera.')
add('Nold','Nold',None,'400.000','11,11','25%','14,28','2005')
add('timing','L','14','alteración patrimonial')
add('return','L','96','obligados a presentar y suscribir declaración')
add('recapture','R','41','autoliquidación complementaria','intereses de demora')
add('Nsale','NR','14','3 por ciento','un mes','tres meses')
add('Ndate','O210','5','tres meses','un mes')
add('late','LGT','27','1 por ciento más otro 1 por ciento','recargo será del 15 por ciento')
add('penalty','LGT','191','Constituye infracción tributaria dejar de ingresar')
add('interest','LGT','26','interés de demora')
add('collection','LGT','28','recargos del período ejecutivo')
add('Nrate','N','25','f) El 19 por ciento','Ganancias patrimoniales que se pongan de manifiesto')
add('Nbasis','N','24','ganancias patrimoniales se determinará aplicando')
add('worldwide','L','2','con independencia del lugar donde se hubiesen producido')
add('2012date','RDL18',None,'12/05/2012','entrará en vigor el mismo día de su publicación')
# S-L07: append full native enactment and alternative valuation clauses.
span('currentdate','D29','DF3.1',2240,2246)
span('priordate','D26','DF3.1',2220,2226)
span('old','L','DT9.1.2',11565,11571)
if missing:raise ValueError(missing)
spec=[('defines a gain/loss','class'),('defines a gain/loss','savings'),("An individual business's",'business'),("An individual business's",'deathgift'),('The state/autonomous','minimum'),('The state/autonomous','minscale'),('| Cross-offset','loss'),('| Unused admitted','loss'),('| Listed homogeneous','repurchase'),('| Unlisted homogeneous','repurchase'),('| Other sold','repurchase'),('| Main-home reinvestment','home'),('| Over-65 insured','annuity'),('| Pre-1994','old'),('For an ordinary sale','sale'),('`acquisition_value','sale'),('`transfer_value','sale'),('`gain_or_loss','sale'),('Exclude acquisition interest','depreciation'),('Exclude acquisition interest','sale'),('Exclude acquisition interest','giftbasis'),('For listed shares','listed'),('For listed shares','fifo'),('Under article37.1(a)','listed'),('Under article37.1(a)','fifo'),('For ordinary unlisted','unlisted'),('Example with otherwise ordinary','unlisted'),('For partially paid','bonus'),('For a2026 disposal','rights'),('Funds, tax-neutral','repurchase'),('1. **Main-home','home'),('2. **Main-home','over65'),('2. **Main-home','ownership'),('2. **Main-home','homegates'),('3. **Over-65','annuity'),('The insured contract','annuity'),('The insured contract','annuitydeath'),('The insured contract','annuitytable'),('Breach of an article 42','annuity'),('For the article41bis.3','relocation'),('If marital separation','relocation'),('For example, assume a73','relocation'),('For example, assume a73','over65'),('Use the dated legislative','currentdate'),('Use the dated legislative','priordate'),('Use the dated legislative','repeal'),('A property that is neither','home'),('- Only qualifying','old'),('- Calculate the ordinary','old'),('- **Listed securities','old'),('- Count pre-31','old'),('- Check cumulative','old'),('Under [art. 49]','loss'),('Under [art. 49]','generalpool'),('Before pooling','repurchase'),('Before pooling','otherloss'),('Integrate with all other','minimum'),('Integrate with all other','minscale'),('Integrate with all other','scale0'),('Integrate with all other','scale1'),('Integrate with all other','scale2'),('Integrate with all other','scale3'),('Integrate with all other','scale4'),('Integrate with all other','territory'),('For an individual resident','2012'),('For an individual resident','2012date'),('A non-resident **without','N2012'),('A non-resident **without','2012date'),('A non-resident **without','Nold'),('Residents include','timing'),('Residents include','return'),('If reinvestment conditions fail','recapture'),('If reinvestment conditions fail','annuity'),("For a non-resident's Spanish-property sale",'Nsale'),("For a non-resident's Spanish-property sale",'Ndate'),('Distinguish an unprompted','late'),('Distinguish an unprompted','penalty'),('Distinguish an unprompted','interest'),('Distinguish an unprompted','collection'),('Ordinary non-resident transfer','Nrate'),('Ordinary non-resident transfer','Nbasis'),('The IRNR transitional','worldwide')]
rows=[]
for lf,sec,u in E['units'](b):
 if u.startswith(('---','#','<!--')) or 'Talk to a verified accountant' in sec or u.startswith(('|---','| 2026 resident','| Relief/loss item','| Official source')):continue
 ks=[]
 for n,k in spec:
  if n in u and k not in ks:ks.append(k)
 status='Express operative rule or stated bounded interpretation; actual precise source limits remain'
 if u.startswith('|') and ('resident savings' in sec or any(x in u for x in ['| 0–6,000','| >6,000','| >50,000','| >200,000','| >300,000'])):
  ix=0 if '| 0–6,000' in u else 1 if '| >6,000' in u else 2 if '| >50,000' in u else 3 if '| >200,000' in u else 4;ks=['scale'+str(ix)];status='Combined rate and opening quota computed by adding the quoted state and autonomous halves; statutory band widths/half rates quoted'
 if 'worked examples' in sec.lower():ks=['sale','loss','repurchase','scale0','scale1'];status='Hypothetical stated inputs and computed case values from sourced rates/eligibility, not fixed statutory case amounts'
 elif any(x in u for x in ['Example with otherwise','For a2026 disposal','3. **Over-65','For example, assume a73']):status='Express legal method plus labelled hypothetical separator/input and computed outputs, not invented legal figures'
 if sec.startswith('## Ask') or sec.startswith('## Sources') or sec=='Metadata':ks=[];status='Operational intake, bibliography, attribution or precisely retained source boundary'
 z=[a for k in ks for a in Q[k]]
 for clause in E['clauses'](u):rows.append(dict(lf=lf,section=sec,wording=clause,authority='; '.join(dict.fromkeys(x['source']+' art.'+str(x['article']) for x in z)) or status,url='; '.join(dict.fromkeys(x['url'] for x in z)) or 'Frozen companion routing/status: no separate positive entitlement asserted',quote='; '.join(x['reader']+f' LF{x["LF_start"]}–{x["LF_end"]}: “'+x['quote']+'”' for x in z) or 'No fabricated quote: actual scope routing/intake/bibliography/precise reservation only.',status=status))
# Semantic destinations, never guessed nearest-text line numbers.
routes=[('## Quick reference','Current Who and Rates: gains classification and actual2026combinedsavingsscale; losses/relief limits and common-versusIRNR scope. Historical table is preserved verbatim here.'),('The scale is really two halves','Current Rates: state/autonomous66/76half-rates separately quoted and combined; minimum uses tax-on-minimum mechanism, not universalbase deduction.'),('## Savings income','Current Rates: current19/21/23/27/30 and openingquotas computed from66+76halves; annualaggregation/minimum allocation supplied.'),('## Main residence','Current The base / Main-home and annuity relief plus dated status extensions: actualpositivegain/qualifyingproceeds/loan-net ratio, before/after2years, over65ownership and recapture conditions. Unrelated240000annuityceiling notimposedonhome.'),('## Assets bought','Current Pre-1994 abatement: completeDT9 days/special2005values/roundedholdingyears/classpercentages/cumulative400000transfer-cap; equality boundary explicit.'),('the repurchase rules','Current Loss pools / repurchase restrictions: listed2months/unlistedyear/otherfollowingyear and deferredrelease separate from admitted4yearcarry.'),('## Capital losses','Current Loss pools: twoannualsavingsbaskets,25%cross-offset,4yearmaximum-use carry and repurchase-deferred/signed losses; generalnon-transfer48separate.'),('## Non-residents','Current Urban property acquired2012 and nonresidentoldassets plus Deadlines/Cross-border: ownIRNR19%,3%buyerpayment, basis/211/210gateway, incorporatedoldassets/half-gainconditions.'),('## Ceuta and Melilla','Current Loss pools/finaltax: conditional68.4 attributabletaxcredit, not a separatecapital-gainmarginaltable; specifiednonresidentmovablegain exclusions.'),('## The method','Current orderedordinarybasis/lot method, separateactualreliefs, loss pools and annualcombinedtax/prepayments, with twooaexamples.'),('## When','Current Sources preciselyreserves decisiveDT9equality, specialisedrestructuring/succession/treatyfacts; ordinarycomputedroutes supplied.'),('Metadata','Current supplied metadata/H1v1.4 and common-territory scope; old versions remain as history.'),('## Rates','Current Rates table, full state+autonomous halves and minimum allocation; relief/loss timing table.'),('## The base','Current ordinary basis/lot identification, listed/unlisted floor/FIFO/rights history, home/annuity, dated extensions, DT9 and loss pools; precise statutory boundaries remain.'),('## Deadlines','Current Deadlines: accrual-year resident return, recapture supplements and nonresident property-sale211/210 windows.'),('## Penalties','Current Penalties and interest: statutory voluntary/assessed/recapture/collection distinctions, no universal150%.'),('## Cross-border','Current Cross-border and2012/old-assets subsection: ownIRNR19%/3%/half-gain/old-asset source methods; worldwide resident gain remains residentIRPF.'),('## Two worked','Current twooa cases preserve ordinary basis/savings bands and separate deferred/admitted-loss ledgers; original exampleinputs retained exactly as history.'),('## Ask','Current six consequential intake questions.'),('## Sources','Current operative/source-chain bibliography and precise limits; old absent URL spellings retained here rather than represented as unchanged currentURLs.'),('## Talk','Current protected CTA/disclaimer unchanged.')]
res=E['render']('es-capital-gains',rows,[],routes);K.save();(P/'ledger-summary.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
