# Evidence-only branch precision; no Guide changes.
# Remove generic 60% irregular-income and 15-year life-insurance anchors that do not prove these pension clauses.
L.rows=[z for z in L.rows if not(z['guide_LF']==657 and '#a19' in z['url'])and not(z['guide_LF']in[659,661]and '#a9'in z['url']and z['provision'].endswith('article 9'))and not(z['guide_LF']in[758,760]and '#a75'in z['url'])]
# Heading matches are routing labels, replaced with actual operative paragraphs from the same own article.
for z in L.rows:
 if len(z['quote'])<140 and re.match(r'Artículo ',z['quote']):
  x=m['source'](z['url']);pars=[m['norm'](p)for p in re.split(r'\n\s*\n',x['text'])if p.strip()];choices=[p for p in pars if len(p)>145 and not p.startswith(('Artículo','CAPÍTULO','TÍTULO','Texto vigente'))]
  if choices:z['quote']=choices[0][:1200].rsplit(' ',1)[0]+(' […]'if len(choices[0])>1200 else'')
# Own foreign route / treaty hierarchy, no accidental scale substitution.
bag(758,9,['efectivamente realizados en el extranjero']);bag(760,5,['sin perjuicio'])
# Correct issuer clause, not the article title / social-security subsection.
for z in L.rows:
 if z['guide_LF']==373 and z['url']==GR+'#a89' and len(z['quote'])<140:
  text=m['norm'](m['source'](z['url'])['text']);st=text.index('6. Las entidades');en=text.index('7. Las Administraciones',st);z['quote']=text[st:en].strip()
# Replace truncated transition and fallback selectors with whole bounded operative passages.
L.rows=[z for z in L.rows if z['provision']not in['Own preserved pre2026 capital-benefit transition','Own provider-information yield fallback DA42/A40/G42','B2026 Instruction17.4 preserved first-capital benefit treatment']]
for u,start,end in[(B,'Disposición Transitoria Trigésima Séptima.','DISPOSICIONES DEROGATORIAS'),(A,'Trigésimo primera. (35) Régimen transitorio','Trigésimo segunda.'),(G,'Disposición transitoria trigésima sexta. Régimen transitorio','Disposición transitoria trigésima séptima.')]:
 t=m['norm'](m['source'](u)['text']);st=t.lower().rfind(start.lower());en=t.lower().find(end.lower(),st+len(start));assert st>=0 and en>st
 for lf in[657,667]:push(lf,u,t[st:en].strip(),'Own DT37 / DT31 / DT36 preserved art19.2(b) at31December2025')
for u in[B,A,G]:
 t=m['norm'](m['source'](u)['text']);marker='Sin perjuicio de las obligaciones de información vigentes, en los supuestos'if u==B else'la primera aportación al sistema de previsión';st=t.lower().find(marker.lower());en=t.find('Reglamentariamente',st);assert st>=0 and en>st
 if u!=B:st=t.rfind('Siempre que',0,st)
 push(665,u,t[st:en].strip(),'Own DA42/A40/G42 full provider-information conditions and fallback')
# Current administrative explanation expressly attributes 60% to the preserved historic19.2(b).
part(657,BI,'17.4.','18. OBLIGACION','60',650,'B2026 Instruction17.4 preserved first-capital benefit treatment')
part(667,BI,'17.4.','18. OBLIGACION','60',650,'B2026 Instruction17.4 preserved first-capital benefit treatment')
# Actual 2025 own agency explanations of the historic60% rule, not current19.2(a).
AM='https://web.araba.eus/documents/d/araba/manual_renta_renta2025_es-pdf';GM='https://www.gipuzkoa.eus/documents/2456431/87520117/Renta2025.pdf/4410d04e-34dc-da8b-d54a-a4ad03208482?t=1774256248621'
for u in[AM,GM]:
 t=m['source'](u)['text'];paras=[m['norm'](p)for p in re.split(r'\n\s*\n',t)if p.strip()];valid=[p for p in paras if re.search(r'60\s*(?:por\s*(?:100|ciento)|%)',p,re.I)and('capital'in p.lower())and any(q in p.lower()for q in['primera','contingencia'])]
 if valid:
  for lf in[657,667]:push(lf,u,valid[0][:1800].rsplit(' ',1)[0]+(' […]'if len(valid[0])>1800 else''),'Own 2025 agency manual historic first-capital integration; incorporated solely via current transition')
 else:E.append((657,u,'historic60% exact paragraph missing'))
for i,z in enumerate(L.rows,1):z['id']=i

# Right-column derivative avoids interleaving adjacent historical manual columns; raw unchanged.
x=m['source'](GM);rp=L.p/'G2025manual-p52-right.reader.txt';ct=m['norm'](rp.read_text());st=ct.index('Se integrará el 60% de las siguientes prestaciones',ct.index('e)'));en=ct.index('– SOLO',st);quote=ct[st:en].strip()
for z in L.rows:
 if z['url']==GM and 'Own 2025 agency manual' in z['provision']:
  z['quote']=quote;z['reader']=str(rp.resolve());z['note']='Actual original PDF p52 right column; pdftotext -f52 -l52 -x290 -y0 -W305 -H842 -layout; literal extraction, no textual correction. Historical2025 rule incorporated only through current DT36.'
L.sources[GM]=dict(x,reader=str(rp.resolve()),reader_sha256=__import__('hashlib').sha256(rp.read_bytes()).hexdigest())
# B own final commencement text, not explanatory preamble.
for z in L.rows:
 if z['guide_LF']in[138,321]and'Own2025enactment final' in z['provision']and'Bizkaia'in z['url'].title():
  t=m['norm'](m['source'](z['url'])['text']);st=t.rfind('No obstante lo previsto en el párrafo anterior:');en=t.find('Lo dispuesto en los apartados Uno, Dos, Tres',st);assert st>=0 and en>st;z['quote']=t[st:en].strip();z['provision']='Bizkaia NF2/2025 DF3 own operative commencement;86.8 rental and87.10 acquisition2026 dates'
# Do not mistake an article-title match, page footnote or broad option keyword for its operative rule.
for z in L.rows:
 if z['quote'].startswith('Artículo '):
  pars=[m['norm'](p)for p in re.split(r'\n\s*\n',m['source'](z['url'])['text'])if p.strip()];choices=[p for p in pars if len(p)>145 and not p.startswith(('Artículo','CAPÍTULO','TÍTULO','Texto vigente'))]
  if choices:
   q=choices[0];z['quote']=q if len(q)<=1200 else q[:1200].rsplit(' ',1)[0]+' […]'
 if z['guide_LF']==63 and z['url']==B+'#a9':
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('contribuyente podrá optar');en=t.find('.',i);z['quote']=t[i:en+1]
 if z['guide_LF']==100 and z['url']==G+'#a66':
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('Si el resultado de la integración');en=t.index('cuatro años siguientes',i)+len('cuatro años siguientes');z['quote']=t[i:en]
for u in[B,A,G]:
 x=m['source'](u+'#a9');t=x['text'];start=list(re.finditer(r'(?m)^\s*17\.(?:[0-9]+)?\s+',t))[-1];end=re.search(r'(?m)^\s*18\.(?:[0-9]+)?\s+',t[start.end():]);block=m['norm'](t[start.start():start.end()+end.start()if end else len(t)])
 for q in['no residente','impuesto de naturaleza','convenio']:
  i=block.lower().find(q);assert i>=0;(push(48,u+'#a9',block[max(0,i-130):min(len(block),i+700)].rsplit(' ',1)[0]+' […]','Own article9.17 foreign beneficiary/comparable-tax/treaty actual condition'))
# Full operative numerator/value limbs and FIFO, not an adjacent explanatory footnote.
for z in L.rows:
 if z['guide_LF']==173 and z['url']==G+'#a47'and'primero del artículo' in z['quote']:
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('cuando existan valores homogéneos');a0=t.rfind('2.',0,i);en=t.find('.',i);z['quote']=t[a0:en+1]
for lf in[181,185,186,191,193,195,197,199]:
 for pref in['BP','AP','GP']:
  for su in['gaincost','gainsale','marketfloor']:reuse(lf,pref+'_'+su)
for lf in[187,193,195,199]:
 for u in[B,A,G]:
  t=m['norm'](m['source'](u+'#a47')['text']);i=t.index('De la permuta de bienes o derechos');en=t.find('k)',i)if u==G else t.find('j)',i);push(lf,u+'#a47',t[i:en].strip(),'Own47(i)B/A /47(j)G complete max-market-value permutation rule')
for u in[B,A,G]:
 law(173,u,43,['no admitidos'])
 # Complete preserved retirement prohibition: general system membership paragraph is not its substitute.
 t=m['norm'](m['source'](u+'#a70')['text']);matches=list(re.finditer('jubilación',t,re.I))
 for z in matches:
  piece=t[max(0,z.start()-180):z.start()+350]
  if any(q in piece.lower()for q in['reducir','reducción']):push(113,u+'#a70',piece,'Own70 retirement-year reduction restriction; read with exact71 carry conditions');break
# Exact four residual page-footnote keyword matches replaced by the operative own passage.
for z in L.rows:
 if z['url'].startswith(G)and re.match(r'\d+ (?:Est[ae]|El apartado|La letra)',z['quote']):
  t=m['norm'](m['source'](z['url'])['text']);q='Si el resultado de la integración'if z['guide_LF']==213 else'4.'if z['guide_LF']==285 else'Las cantidades no deducidas'if z['guide_LF']==349 else'permanecer en su patrimonio';i=t.find(q);assert i>=0;z['quote']=t[max(0,i-70):i+650].rsplit(' ',1)[0]+' […]'
# Own charitable-giving rate/ceiling/carry, scoped to governing provision rather than whole-document first number.
AU='https://web.araba.eus/documents/1247685/1248445/%C3%8DNDICES_NF%2BMECENAZGO-CAS.pdf/b51493c8-e36d-2090-bec3-908084e051c2?t=1673261049711';GU='https://www.gipuzkoa.eus/documents/2456431/2461522/NF%2B3-2004%2B%282020-1%29.pdf/a421e3bf-fdd3-35c8-25b2-3c756fc0be0c'
L.rows=[z for z in L.rows if not(z['guide_LF']==496 and z['url']==AU)and not(z['guide_LF']==497 and z['url']==GU)]
for q in['30 por','35 por','cinco','generales','general y del ahorro']: 
 if q in['generales']:continue
 a(496,AU+'#a22',q,'Álava NF35/2021 article22 ordinary gift30%/combined35%BI/five-year carry')
a(496,AU+'#a31','45 por','Álava NF35/2021 article31 designated priority45% route',width=800)
a(497,GU+'#a21','20 por','Gipuzkoa NF3/2004 article21 ordinary gift rate')
a(497,GU+'#a21','30 por','Gipuzkoa NF3/2004 article21.2 30% base LIQUIDABLE; frozen wording finding',note='Current Guide says taxable base; primary says base liquidable. Difference reported to parent; no Guide mutation by this writer.')
for q in['30 por','certificado','modelo informativo']:law(497,G,90,[q])
for i,z in enumerate(L.rows,1):z['id']=i
for z in L.rows:
 if z['provision']=='Own listed-disposal special3% alternative DA'and z['url']==A:
  t=m['norm'](m['source'](A)['text']);i=t.index('especial del tres por ciento');st=t.rfind('1.',0,i);st=st if i-st<700 else max(0,i-150);en=t.index('Cuando',i)if'Cuando'in t[i:]else i+1000;z['quote']=t[st:min(en,i+1100)].strip();z['provision']='Álava NF33/2013 DA20 exact ordinary listed-disposal3% alternative'
# Remove misleading matching of unrelated employer-private service language; the correct particular-day exclusion is quoted alongside non-working days.
L.rows=[z for z in L.rows if not(z['provision']=='B Instruction1/2026 2.2.10'and'deba ser, objeto de facturación'in z['quote'])]
for i,z in enumerate(L.rows,1):z['id']=i
# Published reports and qualification clauses have several same-keyword populations: isolate actual numbered limbs.
for u,num in[(BR,8),(AR,13)]:
 txt=m['source'](u+'#a'+('117'if u==BR else'123'))['text'];ss=list(re.finditer(r'(?m)^\s*'+str(num)+r'\.(?:\s*\([0-9]+\))?\s+',txt));assert ss;st=ss[-1];en=re.search(r'(?m)^\s*'+str(num+1)+r'\.',txt[st.end():]);qt=m['norm'](txt[st.start():st.end()+en.start()if en else len(txt)]);assert'certific'in qt.lower()
 L.rows=[z for z in L.rows if not(z['guide_LF']==373 and z['url'].startswith(u))];push(373,u+'#a'+('117'if u==BR else'123'),qt,'B DF47/2014 117.8 /A DF40/2014 123.13 own issuer annual report, January window')
L.rows=[z for z in L.rows if not(z['guide_LF']==373 and z['url']==GR+'#a89'and'Los órganos o entidades'in z['quote'])]
# Actual A2026 foreign-custody amended paragraph, not the DAC8 explanatory preamble.
t=m['norm'](m['source'](ACUST)['text']);i=t.rfind('Los criptoactivos se entenderán situados en el extranjero');assert i>=0;en=t.find('2.',i);qt=t[i:en].strip()if en>i and en-i<2500 else t[i:i+1500].rsplit(' ',1)[0]+' […]'
for z in L.rows:
 if z['url'].startswith(ACUST)and any(q in z['quote']for q in['A este respecto, se destaca','Por otro lado, la Directiva','incorporando en su ámbito','las modificaciones nece','casos para discernir','a la que se permita prestar']):z['quote']=qt;z['provision']='Álava DF35/2026 own replacement23bis foreign-custodian actual definition'
for u,lf in[(BORD,705)]:
 t=m['norm'](m['source'](u)['text']);i=t.index('La presentación del modelo 721, «Declaración informativa sobre monedas virtuales situadas en el extranjero», se realizará');assert i>=0;en=t.find('Artículo 5',i);qt=t[i:en].strip();
 for z in L.rows:
  if z['guide_LF']==lf and z['url']==u:z['quote']=qt
# Care exceptional 300-hour training: different from the SMI percentage table.
u='https://egoitza.gipuzkoa.eus/ogasuna/normativa/docs/0001288c.pdf';t=m['norm'](m['source'](u)['text']);i=t.find('300 horas');assert i>=0
for z in L.rows:
 if z['guide_LF']==301 and z['url']==u and('De 300,01%'in z['quote']):z['quote']=t[max(0,i-430):i+450].rsplit(' ',1)[0]+' […]';z['provision']='G DF6/2023 DT1 exceptional/provisional qualification exact300-hour branch'
# Citation finding repaired by parent; preserve old wording in predecessor support and bind current wording only.
for z in L.rows:
 if z['guide_LF']==497:z['guide_wording']=I[497];z['note']=z['note'].replace('Current Guide says taxable base; primary says base liquidable. Difference reported to parent; no Guide mutation by this writer.','Parent corrected prior taxable-base wording to liquidable base; predecessor retained. Exact own90.2/21.2 chain, no Guide mutation by this writer.')
for i,z in enumerate(L.rows,1):z['id']=i
# Final exact native clause selectors for paragraph-number / page-footnote ambiguity.
for z in L.rows:
 if z['url']==G+'#a5':
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('Lo previsto en esta Norma Foral');z['quote']=t[i:t.index('.',i)+1]
 if z['url']==G+'#a75'and z['guide_LF']in[31,218]:
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('La base liquidable general será gravada');z['quote']=t[i:t.index('2.',i)].strip()
 if z['url']==G+'#a87'and z['guide_LF']==285:
  t=m['source'](z['url'])['text'];ss=list(re.finditer(r'(?m)^\s*4\.(?:[0-9]+)?\s+',t));assert ss;st=ss[-1];en=re.search(r'(?m)^\s*5\.',t[st.end():]);z['quote']=m['norm'](t[st.start():st.end()+en.start()if en else len(t)])[:1700].rsplit(' ',1)[0]+' […]'
 if z['url']==GR+'#a45bis'and z['guide_LF']==146 and'publicación'in z['quote']:
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('A efectos de lo previsto');z['quote']=t[i:t.index('2.',i)].strip()
 if z['guide_LF']in[325,327,329]and z['url']==A+'#a87'and len(z['quote'])<70:
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('4 ter.');en=t.index('5.',i);z['quote']=t[i:en].strip()
 if z['provision']=='Álava NF33/2013 DA20 exact ordinary listed-disposal3% alternative'and z['quote'].startswith('odrán'):z['quote']='[…] '+z['quote'][z['quote'].index('optar'):]
for i,z in enumerate(L.rows,1):z['id']=i
for z in L.rows:
 if 'Álava DF35/2026'in z['provision']:z['provision']=z['provision'].replace('DF35/2026','DF36/2026 DA2 modifying DF111/2008')
 if z['provision'].startswith('Own source '):
  for pref,label in[('BP_','Bizkaia NF13/2013'),('AP_','Álava NF33/2013'),('GP_','Gipuzkoa NF3/2014'),('BR_','Bizkaia DF47/2014'),('AR_','Álava DF40/2014'),('GR_','Gipuzkoa DF33/2014'),('BC_','Bizkaia NF11/2013'),('AC_','Álava NF37/2013'),('GC_','Gipuzkoa NF2/2014')]:
   if pref in z['provision']:z['provision']=z['provision'].replace('Own source ',label+' ');break
 if z['guide_LF']==496 and z['url']==AU+'#a31':
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('b) Los contribuyentes del Impuesto sobre la Renta de las Personas Físicas');en=t.index('c)',i);z['quote']=t[i:en].strip()
for u in[B,A,G]:
 t=m['source'](u+'#a70')['text']
 for num in[5,6]:
  ss=list(re.finditer(r'(?m)^\s*'+str(num)+r'\.(?:[0-9]+)?\s*(?:\([0-9]+\)\s*)*',t));assert ss;st=ss[-1];en=re.search(r'(?m)^\s*'+str(num+1)+r'\.',t[st.end():]);qt=m['norm'](t[st.start():st.end()+en.start()if en else len(t)]);push(113,u+'#a70',(qt[:1700].rsplit(' ',1)[0]+' […]'if len(qt)>1700 else qt),'Own NF13/2013 /33/2013 /3/2014 article70.'+str(num)+' retirement/coincident-capital rule and named exceptions')
for i,z in enumerate(L.rows,1):z['id']=i
for u in[B,A,G]:
 for q in['proporción','aportaciones y contribuciones']:
  law(655,u,37,[q],width=1000)
# Own Gipuzkoa progression statutory worksheet, not a treaty-category entitlement.
part(685,G,'Disposición adicional trigésimo octava.','Disposición adicional trigésima novena.','Las rentas exentas con progresividad se añadirán',1200,'Gipuzkoa NF3/2014 DA38 actual exempt-progression mechanism')
# Preserved valuation/certificate sources behind all-territory donor evidence paragraph.
for lf in[504]:
 law(lf,B,91,['mecenazgo']);law(lf,A,91,['mecenazgo']);law(lf,G,90,['certificado'])
for i,z in enumerate(L.rows,1):z['id']=i
# Gross-general-quota definition underlying the business attribution worksheet.
for u in[B,A,G]:
 for q in['artículo 77','negativ']:law(389,u,74,[q],width=900)
# Hypothetical examples are not statutory figures even when their rules share a source row.
for z in L.rows:
 if re.search(r'\b(example|control|hypothetical|Assume)\b',z['guide_wording'],re.I)and'computed'not in z['kind']:z['kind']='computed illustration, sourced underlying rule';z['note']+=' The case inputs/results are derived, not a quotation of statutory amounts.'
for i,z in enumerate(L.rows,1):z['id']=i
# Remaining express conditions in compound pension/order/share units.
for u in[B,A,G]:
 for lf,ar,qs in[(631,72,['beneficiari']),(633,72,['Sucesiones','financiera']),(111,71,['financiera']),(633,70,['intereses de demora']),(173,47,['totalmente liberadas'])]:
  for q in qs:law(lf,u,ar,[q],width=1000)
 t=m['source'](u+'#a67')['text'];paras=[m['norm'](v)for v in re.split(r'\n\s*\n',t)if v.strip()]
 for q in paras:
  if any(k in q.lower()for k in['primero:','segundo:','tercero:','no podrá dar lugar','remanente']):push(102,u+'#a67',q,'Own NF13/2013 /33/2013 /3/2014 article67 ordered general/savings reductions')
for i,z in enumerate(L.rows,1):z['id']=i
