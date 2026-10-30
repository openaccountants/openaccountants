from pathlib import Path
import runpy,json,re,shutil,hashlib
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P/'ledger-engine.py'));R=E['ROOT'];f=R/'skills/international/spain/es-beckham.md';b=f.read_text()
base=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-fresh-whole-pack-review-0f104150');receipts=json.loads((base/'source-receipts.json').read_text())
keys={'LIRPF':'BOE-A-2006-20764','RIRPF':'BOE-A-2007-6820','IRNR':'BOE-A-2004-4527','LGT':'BOE-A-2003-23186','Order149151':'BOE-A-2023-25416'};src={};ident=[]
for k,id in keys.items():
 rec=next(x for x in receipts if x['url'].endswith('id='+id));raw=base/rec['path'];reader=raw.with_suffix('.reader.txt');a=P/'sources'/f'{k}.body';d=P/'sources'/f'{k}.reader.txt';shutil.copyfile(raw,a);shutil.copyfile(reader,d);src[k]=dict(url=rec['url'],lines=d.read_text().splitlines(),reader=d);ident.append(dict(id=k,url=rec['url'],raw_file=str(a.relative_to(P)),raw_sha256=E['sha'](a),reader_file=str(d.relative_to(P)),reader_sha256=E['sha'](d),acquired_utc=rec['downloaded_utc'],scope='Selected exact quote intervals only; not whole acquired body reading.'))
fold=base.parent/'spain-fresh-review-repairs/F25-Beckham-withholding-gate'
for ext in ['html','reader.txt']:shutil.copyfile(fold/('AEAT-general-incoming-worker.'+ext),P/'sources'/('AEAT147.'+ext))
src['AEAT147']=dict(url='https://sede.agenciatributaria.gob.es/Sede/irpf/tengo-que-presentar-declaracion/regimen-fiscal-aplicable-trabajadores-desplazados.html',lines=(P/'sources/AEAT147.reader.txt').read_text().splitlines(),reader=P/'sources/AEAT147.reader.txt')
ident.append(dict(id='AEAT147',url=src['AEAT147']['url'],raw_file='sources/AEAT147.html',raw_sha256=E['sha'](P/'sources/AEAT147.html'),reader_file='sources/AEAT147.reader.txt',reader_sha256=E['sha'](P/'sources/AEAT147.reader.txt'),scope='Actual LF14–21 incoming-worker procedure plusModelo147; no whole page read claim.'))
quotes=[]
def q(k,article,needle,words=30):
 a=src[k]['lines'];start=0;end=len(a)
 if article:
  start=next(i for i,x in enumerate(a) if re.match(r'^Artículo\s+'+re.escape(article)+r'\.',x));end=next((i for i in range(start+1,len(a)) if re.match(r'^Artículo\s+\d',a[i])),len(a))
 hits=[i for i in range(start,end) if needle in a[i]]
 if not hits:raise ValueError(k,article,needle)
 i=hits[0];line=a[i];j=line.index(needle);m=list(re.finditer(r'\S+',line[j:]));quote=line[j:j+m[min(words,len(m))-1].end()];assert quote in line
 z=dict(source=k,article=article,url=src[k]['url']+('#a'+article.replace(' ','') if article else ''),quote=quote,reader=str(src[k]['reader'].relative_to(P)),LF_start=i+1,LF_end=i+1,read_on='2026-10-28');quotes.append(z);return z

def span(k,needle,n=5):
 a=src[k]['lines'];start=next(i for i,x in enumerate(a) if x.startswith('Artículo 93.'));end=next(i for i in range(start+1,len(a)) if a[i].startswith('Artículo 94.'));i=next(i for i in range(start,end) if needle in a[i]);t='\n'.join(a[i:i+n]);z=dict(source=k,article='93.2.e scale',url=src[k]['url']+'#a93',quote=t,reader=str(src[k]['reader'].relative_to(P)),LF_start=i+1,LF_end=i+n,read_on='2026-10-28');quotes.append(z);return z
Q={
'elig':[q('LIRPF','93','durante los cinco períodos impositivos siguientes'),q('LIRPF','93','cinco períodos impositivos anteriores'),q('LIRPF','93','deportistas profesionales')],
'employment':[q('LIRPF','93','la actividad laboral se preste a distancia'),q('LIRPF','93','exista una carta de desplazamiento')],
'activity':[q('LIRPF','93','más del 40'),q('LIRPF','93','entidad patrimonial'),q('LIRPF','93','Que no obtenga rentas'),q('RIRPF','113','informe favorable emitido por la Empresa Nacional de Innovación')],
'bar':[q('RIRPF','116','No podrán ejercitar esta opción'),q('AEAT147',None,'mediante la presentación del modelo 147')],
'family':[q('LIRPF','93','menores de veinticinco años'),q('LIRPF','93','sea inferior a la base liquidable'),q('RIRPF','113','no adquieran la residencia fiscal en España antes')],
'duration':[q('RIRPF','115','durante los cinco períodos impositivos siguientes')],
'24':[span('LIRPF','      Hasta 600.000 euros.',2)],'47':[span('LIRPF','      Desde 600.000,01 euros en adelante.',2)],
'19':[span('LIRPF','      0',4)],'21':[span('LIRPF','      6.000,00',4)],'23':[span('LIRPF','      50.000,00',4)],'27':[span('LIRPF','      200.000,00',4)],'30':[span('LIRPF','      300.000,00',4),q('LIRPF','93','con efectos desde el 1 de enero de 2025')],
'withhold':[q('LIRPF','93','porcentaje de retención o ingreso a cuenta sobre rendimientos del trabajo será el 24',50)],
'source':[q('LIRPF','93','se entenderán obtenidos en territorio español'),q('RIRPF','114','con anterioridad a la fecha de desplazamiento'),q('IRNR','13','Los dividendos'),q('IRNR','13','Los rendimientos derivados, directa o indirectamente, de bienes inmuebles')],
'base':[q('IRNR','24','estará constituida por su importe íntegro'),q('LIRPF','93','No resultará de aplicación lo dispuesto'),q('LIRPF','93','sin que sea posible compensación alguna')],
'credit':[q('LIRPF','80','se deducirá la menor'),q('LIRPF','80','tipo de gravamen se expresará con dos decimales'),q('RIRPF','114','con el límite del 30 por ciento',60)],
'deduct':[q('IRNR','26','Las cantidades correspondientes a las deducciones por donativos'),q('IRNR','26','Las retenciones e ingresos a cuenta'),q('RIRPF','114','cuotas satisfechas a cuenta')],
'professional':[q('RIRPF','114','solamente estarán sujetos a retención'),q('RIRPF','114','deberá consignarse el tipo de retención'),q('RIRPF','114','modelos de declaración previstos para el Impuesto')],
'property':[q('RIRPF','114','A las transmisiones de bienes inmuebles')],
'wealth':[q('LIRPF','93','sujeto por obligación real'),q('RIRPF','120','a condición de reciprocidad')],
'election':[q('RIRPF','116','plazo máximo de seis meses',60)],
'associated':[q('RIRPF','116','desde la fecha de su entrada en territorio español',50)],
'evidence':[q('RIRPF','119','documentación justificativa del alta'),q('RIRPF','119','ante las personas o entidades obligadas a practicar retención')],
'return':[q('Order149151','3','será el mismo que se apruebe cada ejercicio'),q('Order149151','4','cinco días antes'),q('Order149151','4','presentación electrónica por Internet')],
'renounce':[q('RIRPF','117','meses de noviembre y diciembre'),q('RIRPF','117','no podrán volver a optar')],
'exclusion':[q('RIRPF','118','período impositivo en que se produzca el incumplimiento'),q('RIRPF','118','plazo de un mes'),q('RIRPF','118','no podrán volver a optar')],
'endposting':[q('RIRPF','119','plazo de un mes desde que hubiera finalizado')],
'familyloss':[q('RIRPF','118','quedarán conjuntamente excluidos'),q('RIRPF','118','quedará individualmente excluido'),q('RIRPF','118','divorcio o nulidad del matrimonio')],
'late':[q('LGT','27','1 por ciento más otro 1 por ciento'),q('LGT','27','12 meses desde el término',60)],
'penalty':[q('LGT','191','Constituye infracción tributaria'),q('LGT','198','Constituye infracción tributaria'),q('LGT','199','Constituye infracción tributaria'),q('LGT','26','interés de demora es una prestación accesoria'),q('LGT','28','recargos del período ejecutivo')],
'exit':[q('LIRPF','95 bis','hubieran optado por el régimen fiscal especial')],
}
# Associate exact paragraph/list/table context with the actual primary quote sets above.
spec=[('lets qualifying','elig'),('Qualifying employment','employment'),('An administrator','activity'),('Before electing','bar'),('For example, an employee','bar'),('Qualifying spouse','family'),('| Regime duration','duration'),('| Pre-move','elig'),('| Ordinary special','24'),('| Same base above','47'),('| Spanish-source savings-category','19'),('| >6,000','21'),('| >50,000','23'),('| >200,000','27'),('| >300,000','30'),('| Employment withholding','withhold'),('| Foreign-work','credit'),('Under [LIRPF','source'),('For other income','source'),('Apply the IRNR base','base'),('1. Build a source','base'),('2. Compute','24'),('2. Compute','47'),('3. Compute','30'),('4. Determine','deduct'),('5. For foreign','credit'),('6. Subtract','deduct'),('6. Subtract','withhold'),('For professional economic','professional'),('For professional economic','property'),('The election sets wealth','wealth'),('| Principal election','election'),('| Prior incoming','bar'),('| Associated person','associated'),('| Evidence and accreditation','evidence'),('| Annual return','return'),('| Voluntary renunciation','renounce'),('| Exclusion','exclusion'),('| Posting ends','endposting'),('An NIE alone','election'),('An NIE alone','return'),('For associated people','familyloss'),('An unprompted late','late'),('An unprompted late','penalty'),('The central cross-border','source'),('The central cross-border','credit'),('A tax visa','wealth'),('A tax visa','exit')]
rows=[]
for lf,sec,u in E['units'](b):
 if u.startswith(('---','#','<!--')) or 'Talk to a verified accountant' in sec or u.startswith('|---') or u.startswith('| Item') or u.startswith('| Action'):continue
 keys_used=[]
 for needle,k in spec:
  if needle in u and k not in keys_used:keys_used.append(k)
 kind='Express primary rule / scope application'
 if 'worked examples' in sec.lower():keys_used=['24','47','19','30','source','credit','withhold'];kind='Hypothetical independently established inputs and computed outputs, not statutory fixed amounts'
 if sec.startswith('## Ask the client') or u.startswith('Calculate the 2026'):kind='Operational intake / status statement, not a tax entitlement'
 if sec.startswith('## Sources') and not u.startswith('**Not yet confirmed'):
  kind='Source bibliography / read-date routing record';keys_used=[]
 if u.startswith('**Not yet confirmed'):kind='Precisely retained ordinary/specialist boundary; no positive method invented';keys_used=[]
 selected=[x for k in keys_used for x in Q[k]]
 for clause in E['clauses'](u):
  quote='; '.join(x['reader']+f' LF{x["LF_start"]}–{x["LF_end"]}: “'+x['quote']+'”' for x in selected) if selected else 'No independent numerical entitlement: operational/bibliographic/precisely reserved wording. Legal methods have separate quoted rows.'
  if '77,307.69' in clause:quote+=' PRECISION: this is the raw unrounded fraction. LIRPF80.2 requires effective rate expressed to2decimals (25.77%→77,310); additional50,250 cap still binds, so final tax/refund unchanged. Frozen Guide unchanged; distinct reviewer disposition required.'
  rows.append(dict(lf=lf,section=sec,wording=clause,authority='; '.join(dict.fromkeys(x['source']+' art.'+str(x['article']) for x in selected)) or kind,url='; '.join(dict.fromkeys(x['url'] for x in selected)) or 'See current cited Sources / factual intake',quote=quote,read_on='2026-10-28 selected actual primary quote reading; inherited bibliography dates as written',status=kind))
notes=[('Foreign employment income','Current Who this applies to / Identify Spanish-source income correctly: corrected historical exemption to LIRPF93.2.b worldwide regime-period work deeming; old contrary claim retained here, not silently lost.'),('Foreign investment income','Current Identify Spanish-source income correctly: foreign passive income uses own IRNR13 source test; historical blanket inclusion corrected, source and service period separated.'),('Foreign dividends','Current Identify Spanish-source income correctly: own IRNR13 source test; historical blanket taxable foreign-passive claim corrected.'),('Foreign rental income','Current Identify Spanish-source income correctly: genuine foreign-source passive rent not automatically subject; Spanish property source separately included.'),('28%','Current Rates table:2026 top savings30%, opening quota71,880; 2025 effective amendment retained. Historical28% replaced by current law.'),('20% of total income','Current Who this applies to: visa/immigration facts do not dispense with tax-route gates. Historical blanket20%client-income tax qualification is not asserted; employment versus ordinary freelance distinction and actual93routes supplied.'),('Individuals managing qualified investment','Current Who this applies to: qualified actual employment/administrator/entrepreneur/highly-qualified routes replace unsupported automatic investment-manager eligibility.'),('30 June','Current Deadlines and filing: annual approved campaign window and actual direct-debit cut-off replace unchanging30June date.'),('Missing the 6-month','Current Deadlines and filing: substantive six-month clock retained; actual filed evidence/procedure reviewed before declaring an automatic cure or irretrievability.'),('cannot be corrected retroactively','Current Deadlines and filing: substantive election clock retained with precise procedural boundary, no assumed automatic correction or irretrievability.'),('Register with Spanish Social Security or obtain NIE','Current Deadlines and filing: actual qualifying activity/SS/origin documentation controls; NIE alone expressly insufficient.')]
result=E['render']('es-beckham',rows,notes);(P/'source-identities.json').write_text(json.dumps(ident,ensure_ascii=False,indent=2)+'\n');(P/'actual-read-quotes.json').write_text(json.dumps(quotes,ensure_ascii=False,indent=2)+'\n');(P/'ledger-summary.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
