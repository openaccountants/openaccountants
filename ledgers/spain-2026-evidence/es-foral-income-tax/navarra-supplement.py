# Own finite Navarra business-credit / instalment chain; root retains separate housing/advance selection.
NP='https://www.boe.es/buscar/act.php?id=BON-n-2008-90013&p=20260420&tn=1';NC='https://www.boe.es/buscar/act.php?id=BOE-A-2017-2356';NR='https://www.navarra.es/es/web/normativa-hacienda/-/reglamento-del-impuesto-sobre-la-renta-de-las-personas-f%C3%ADsicas-df-174/1999-de-24-de-mayo-?print=true'
rootnav=Path('ledgers/spain-2026-evidence/root-navarra-pit');nrp=(rootnav/'N3-current-selected.txt').resolve();nrraw=next(z for z in json.loads((rootnav/'source-identities.json').read_text())if z['key']=='N3');nt=nrp.read_text()
def regpart(lf,ar):
 st=nt.index('Artículo '+str(ar)+'.');en=nt.find('Artículo ',st+len('Artículo '+str(ar)+'.'));text=nt[st:en if en>=0 else len(nt)]
 if ar==78:
  i=text.index('4. Cuando los rendimientos');text=text[i:]
 # Each actual paragraph retained separately, with complete exact current date-selected provenance.
 for q in[m['norm'](v)for v in text.split('\n')if v.strip()and not v.startswith('Artículo')]:
  L.rows.append(dict(id=len(L.rows)+1,section=next(v['section']for v in L.units if v['line']==lf),guide_LF=lf,guide_wording=I[lf],provision='Navarra DF174/1999 current article'+str(ar),url=NR,quote=q,read_on='2026-10-28',kind='own current primary rule / computed illustration where stated',note='Exact current R dated-div selection: fdesde<=20261028<fhasta, excluding historical annotation notes; original HTML and dated-block provenance retained in root-navarra-pit. Selected provisions actually read by this writer; no claim of whole-source read.',raw_sha256=nrraw['raw_sha256'],reader=str(nrp)))
 L.sources[NR]=dict(url=NR,actual_raw_sha256=nrraw['raw_sha256'],raw=str(rootnav/nrraw['raw']),reader=str(nrp),reader_sha256=__import__('hashlib').sha256(nrp.read_bytes()).hexdigest(),date_filter_provenance=str(rootnav/'N3-dated-current-blocks.json'))
regpart(697,56)
for lf,ars in[(733,[91,78]),(735,[92]),(737,[92]),(739,[92,93,94])]:
 for ar in ars:regpart(lf,ar)
for lf,u,ar,qs in[(405,NP,62,['incentivos y estímulos']),(405,NP,64,['62.3']),(409,NP,64,['62.3']),(405,NC,67,['25 por','quince','siguiente orden']),(409,NC,67,['25 por','hasta el inicio'])]:
 for q in qs:a(lf,u+'#a'+str(ar),q,'Navarra DFL4/2008 '+str(ar)+' /LF26/2016 '+str(ar)+' own corporate-credit incorporation/use order',width=1000)
# No first-modality filing6500/amended100strict threshold chain.
for u,q in[('https://www.lexnavarra.navarra.es/detalle.asp?r=29810','inferior a 100 euros'),('https://bon.navarra.es/es/anuncio/-/texto/2011/75/3','6.500 euros')]:a(735,u,q,'Navarra OF40/2009 article2 as amended by actual OF48/2011 article1.2; no4500currentthreshold',width=1100)
for q in['formato electrónico','vía electrónica','domiciliación','carta de pago']:a(739,'https://bon.navarra.es/es/anuncio/-/texto/2026/63/0',q,'Navarra OF23/2026 article1 modifyingOF40/2009 modelo130 actual electronic/payment procedure',width=1100)
for q in['propuesta','pago']:a(739,NP+'#a80',q,'Navarra DFL4/2008 article80.6 paid authority proposal effect',width=900)
for anchor,q in[('da-63','1 por 100'),('da-45','normativa foral del Impuesto sobre Sociedades')]:a(733,NP+'#'+anchor,q,'Navarra DFL4/2008 DA62 freight/removal /DA44 entrepreneur own incorporation',width=1200)
# Own current entrepreneurship3.1–3/6–8, not IAE inscription alone.
t=m['norm'](m['source'](NC+'#da-3')['text'])
for num,end in[(1,'2. No se considerarán'),(2,'3. Beneficios fiscales'),(3,'4. Beneficios fiscales'),(6,'7. No podrán'),(7,'8. Incumplimientos'),(8,'Se modifica')]:
 start={1:'1. Se considerarán',2:'2. No se considerarán',3:'3. Beneficios fiscales',6:'6. Registro de personas',7:'7. No podrán',8:'8. Incumplimientos'}[num];i=t.index(start);j=t.find(end,i+len(start));qt=t[i:j if j>=0 else len(t)]
 if num==3:qt=qt[:qt.index('b)')].strip()
 push(733,NC+'#da-3',qt[:2600].rsplit(' ',1)[0]+(' […]'if len(qt)>2600 else''),'Navarra LF26/2016 DA3.'+str(num)+' own entrepreneur statutory population /registry /conditions /breach')
# Same worked annual return facts; underlying current N income/scales/credit rows are separately quoted in parent core fragment.
for z in list(L.rows):
 if 'parent writer'in z['note']and z['guide_LF']in[462,464]:
  zz=copy.deepcopy(z);zz.update(id=len(L.rows)+1,guide_LF=801,guide_wording=I[801],section=next(v['section']for v in L.units if v['line']==801));zz['kind']='computed annual control; own current N source rule';L.rows.append(zz)
for i,z in enumerate(L.rows,1):z['id']=i

# Complete statutory credit-order paragraphs, not just the ordering heading.
t=m['source'](NC+'#a67')['text'];i=t.index('4. Las deducciones');en=t.index('6. Una misma',i);block=t[i:en]
for lf in[405,409]:
 for q in[m['norm'](v)for v in re.split(r'\n\s*\n',block)if v.strip()]:push(lf,NC+'#a67',q,'Navarra LF26/2016 article67.4–5 full limited-credit ceiling/carry/order')
# Replace broad first-keyword matches by the actual enacted paragraphs just read.
for z in L.rows:
 if z['provision'].startswith('Navarra DFL4/2008 ')and'/LF26/2016'in z['provision']:z['provision']=('Navarra DFL4/2008'if z['url'].startswith(NP)else'Navarra LF26/2016')+' article'+z['url'].split('#a')[-1]+' own business-credit incorporation/use'
 if z['guide_LF']==735 and z['url']=='https://www.lexnavarra.navarra.es/detalle.asp?r=29810':
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('b) Aquéllos cuyo pago fraccionado trimestral');en=t.index('Artículo 3.',i);z['quote']=t[i:en].strip()
 if z['guide_LF']==735 and z['url']=='https://bon.navarra.es/es/anuncio/-/texto/2011/75/3':
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('Dos.-Artículo 2.º, segundo párrafo, letra a).');en=t.index('Tres.-Artículo',i);z['quote']=t[i:en].strip()
L.rows=[z for z in L.rows if not(z['guide_LF']==739 and('OF23/2026'in z['provision']or'80.6 paid'in z['provision']))]
u='https://bon.navarra.es/es/anuncio/-/texto/2026/63/0';text=m['source'](u)['text'];st=text.index('Uno.–Artículo 1.1.');en=text.index('Tres.–Se suprime el anexo',st)
for q in[m['norm'](v)for v in text[st:en].split('\n')if v.strip()]:push(739,u,q,'Navarra OF23/2026 article1.1–2 actual130 electronic form/window/payment')
t=m['source'](NP+'#a80')['text'];st=t.index('6. Los sujetos pasivos');en=t.index('7. Las retenciones',st)
for q in[m['norm'](v)for v in re.split(r'\n\s*\n',t[st:en])if v.strip()]:push(739,NP+'#a80',q,'Navarra DFL4/2008 article80.6 authority proposal paid/confirmed/unconfirmed obligation')
a(733,NP+'#da-63','no estarán obligados','Navarra DFL4/2008 DA62.2 actual qualifying freight/removal instalment exemption',width=650)
for i,z in enumerate(L.rows,1):z['id']=i
# Additional Basque form/FAQ anchors: paragraph721 includes these actual administration branches.
u='https://www.bizkaia.eus/fitxategiak/05/ogasuna/ereduak/Argitaratu/130CasInst.pdf'
for q in['70%','negativo','25 por ciento','Casillas 07','0,25 por','20%']:a(721,u,q,'Bizkaia published Modelo130 instructions; own receipt/form branch, not common130',width=850)
u='https://www.bizkaia.eus/ogasuna/ereduak/descargar_documento.asp?Idioma=CA&val1=8AA405AF81D76CC992B77CD9B7C7112FCA1B1651B529D2961D5EFE269326793A';t=m['norm'](m['source'](u)['text']);st=t.index('Actividades agrícolas,');en=t.index('Fecha y firma declarante',st);push(721,u,t[st:en].strip(),'Bizkaia actual retained Modelo130 PDFp1 boxes05–20; printed2018 version, actual saved image visually read',note='Saved p1 screenshot actually viewed. General fallback15–18 includes17 withholding; wholesalers19–20 has no additional withholding box. Source version and present read date are distinct.')
for u,q in[('https://www.bizkaia.eus/ogasuna/faq/faq_detalle.asp?idregistro=900001002&IdEtiquetaBuscar=190&Idioma=CA&Tem_Codigo=7884&pant=listado','0,5'),('https://www.bizkaia.eus/ogasuna/faq/faq_detalle.asp?idregistro=900001003&IdEtiquetaBuscar=190&Idioma=CA&Tem_Codigo=7884&pant=listado','retenciones')]:a(721,u,q,'Bizkaia actual specific130 FAQ branch',width=1000)
for i,z in enumerate(L.rows,1):z['id']=i
# Final source-cell precision, retaining literal originals and exact scopes.
for z in L.rows:
 if 'specific130 FAQ' in z['provision']:
  t=m['norm'](m['source'](z['url'])['text']);q='Como regla general el importe a ingresar'if'900001002'in z['url']else'En particular, cuando se trate de actividades';i=t.index(q);en=t.index('Enlaces',i);z['quote']=t[i:en].strip();z['note']='Published actual administrative explanation expressly nonbinding; operative DF47/2014 art110 and actual form/instructions are separately quoted.'
 if z['provision']=='B2026 Instruction15.10.1.2 SME-entry exception'and'15.11.'in z['quote']:z['quote']=z['quote'].split('15.11.')[0].strip()
 if z['provision']=='B DF84/2026 operative replacement/effect; not full DAC8 review':
  t=m['norm'](m['source'](z['url'])['text']);i=t.index('El presente Decreto Foral entrará en vigor');en=t.index('En Bilbao,',i);z['quote']=t[i:en].strip();z['provision']='Bizkaia DF84/2026 DF6 own operative commencement2026 /limited2027exception'
for i,z in enumerate(L.rows,1):z['id']=i
# Exact duplicate anchors for the same Guide unit add no evidence; keep aliases for reproducibility.
seen={};kept=[];aliases=[]
for z in L.rows:
 k=(z['guide_LF'],z['url'],z['quote'],z['raw_sha256'],z['reader'])
 if k in seen:aliases.append(dict(original_row=z['id'],kept_pre_numbering=seen[k],guide_LF=z['guide_LF'],provision=z['provision'],note=z['note']));continue
 seen[k]=z['id'];kept.append(z)
L.rows=kept
(L.p/'exact-duplicate-anchor-aliases.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')
for i,z in enumerate(L.rows,1):z['id']=i
# Last two Navarra units: existing current721 and same own NFGT source anchors already read for payroll.
NU='https://www.lexnavarra.navarra.es/detalle.asp?r=56169';t=m['source'](NU)['text'];st=t.rfind('Artículo 1.');en=t.index('Disposición Final Única.',st);block=t[st:en]
for q in[m['norm'](v)for v in block.split('\n')if len(v.strip())>55]:push(708,NU,q,'Navarra OF29/2023 current articles1–7, amended19/2024 procedure; own foreign-custody/competence/window',note='Full actual operative1–7 text read from retained official consolidation2026-10-28, not its scripts/navigation. No B/A/G foreign-custody test imported; governing current1.2 points to own DFL4/2008 DA4.8.')
for z in json.loads(Path('ledgers/spain-2026-evidence/es-foral-payroll/rows.json').read_text()):
 if z['guide_LF']==190:
  zz=copy.deepcopy(z);zz.update(id=len(L.rows)+1,guide_LF=752,guide_wording=I[752],section=next(v['section']for v in L.units if v['line']==752));zz['note']+=' Reused exact own NFGT operative scope already actually read for the ready payroll ledger; source claim rechecked against identical current late-correction/penalty branch.';L.rows.append(zz);L.sources[zz['url']]=m['source'](zz['url'])
for i,z in enumerate(L.rows,1):z['id']=i
