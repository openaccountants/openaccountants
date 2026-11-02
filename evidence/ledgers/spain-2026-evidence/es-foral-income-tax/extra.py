# Additional selected source anchors; snippets are literal source spans, not English backtranslations.
def push(lf,u,quote,provision,kind='rule',note=''):
 x=m['source'](u);L.sources[u]=x;L.rows.append(dict(id=len(L.rows)+1,section=next(v['section']for v in L.units if v['line']==lf),guide_LF=lf,guide_wording=I[lf],provision=provision,url=u,quote=quote,read_on='2026-10-28',kind=kind,note=note,raw_sha256=x['actual_raw_sha256'],reader=x['reader']))
def part(lf,u,start,end,needle,width=650,provision='Selected operative primary passage'):
 full=m['norm'](m['source'](u)['text']);hits=list(re.finditer(re.escape(start),full,re.I));candidates=[]
 for h in hits:
  after=h.start()+len(start);endhits=list(re.finditer(re.escape(end),full[after:],re.I))if end else [];j=after+endhits[0].start()if endhits else len(full);txt=full[h.start():j]
  if needle.lower()in txt.lower():candidates.append(txt)
 if not candidates:E.append((lf,u,'bounded section',start,needle));return
 t=min(candidates,key=len);k=t.lower().find(needle.lower());k=max(0,k-90);k=t.rfind(' ',0,k)+1 if k else 0;e=min(len(t),k+width);e=t.rfind(' ',k,e)if e<len(t)else e;push(lf,u,t[k:e]+(' […]'if e<len(t)else''),provision,'own primary / labelled derivation as stated','Only this selected source passage is claimed read; case amounts remain computed.')
for lf in[52,61]:
 for q in ['llegada y salida','días no laborales','particular']:part(lf,BI,'2.2.10.','2.2.11.',q,750,'B Instruction1/2026 2.2.10')
for lf in[65,67]:part(lf,BI,'15.13.1.','15.13.2.','la totalidad',900,'B Instruction1/2026 15.13.1 full foreign-tax limb')
part(69,BI,'15.13.2.','15.14.','50%',900,'B Instruction1/2026 15.13.2')
part(67,AI,'14.9.1.','14.9.2.','60.100',900,'A2024 Instruction14.9.1 proportional foreign-tax limb')
for lf in[387,389,391,393]:part(lf,BI,'15.9.1.','15.9.2.','Base Imponible',650,'B2026 Instruction15.9.1 own business-BI quota allocation')
for lf in[351,353]:part(lf,BI,'15.10.1.','15.10.2.','1.200',750,'B2026 Instruction15.10.1 precise annual/joint rule')
part(351,BI,'15.10.1.','15.10.2.','gran empresa',1000,'B2026 Instruction15.10.1.2 SME-entry exception')
for lf in[175,177]:
 for u,start,end in[(B,'Disposición Adicional Vigesimocuarta.','Disposición Adicional Vigesimoquinta.'),(A,'Vigésima.','Vigesimoprimera.'),(G,'Disposición adicional vigésima.','Disposición adicional vigésima primera.')]:
  for q in ['10.000','3 por']:part(lf,u,start,end,q,700,'Own listed-disposal special3% alternative DA')
# Current local crypto/new-law enactments, with their own2025 operation.
for lf in[186,201,203]:
 for u,ar in[('https://www.bizkaia.eus/lehendakaritza/Bao_bob/2025/12/15/I-1369_cas.pdf?hash=876ba5bcda895797e9501b0edde9292d',''),('https://www.araba.eus/botha/Boletines/2025/147/2025_147_03861_C.pdf',''),('https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2025/11/28/c2508038.pdf','')]:a(lf,u,'criptoactivos fungibles','Own2025 crypto amendment; same-type loss/FIFO',width=900)
# Exact selected own annual cost-update factors; full table remains in companion.
for lf in[189,191]:
 for place in['bizkaia','araba','gipuzkoa']:
  for year in[2025,2026]:reuse(lf,'PIT_coef_'+place+'_2026_'+str(year))
part(189,AI,'8.25.','8.26.','45',750,'A2024 Instruction8.25 acquisition-update/received basis')
part(193,AI,'8.25.','8.26.','permuta',900,'A2024 Instruction8.25 own received-asset basis')
part(201,BI,'8.10.','8.11.','criptoactivos',900,'B2026 Instruction8.10 matching-unit loss release')
# Actual acquisition-gate enactments: implementation retains their precise date population.
for lf in[138,321]:
 for u in['https://www.bizkaia.eus/lehendakaritza/Bao_bob/2025/04/22/I-441_cas.pdf','https://www.araba.eus/BOTHA/Boletines/2025/044/2025_044_01182_C.pdf']:
  for q in['contratos de arrendamiento','adquisiciones de vivienda']:a(lf,u,q,'Own2025enactment final effective-date clause for2026contracts/acquisitions',width=1100)
law(138,G,49,['2026']);a(321,G,'contratos se suscriban o se prorroguen','Own G86 effective note219',width=850);law(321,G,87,['2026'])
for q in['30 por','5 por','20 por','50 por','dos periodos','tres ejercicios']:law(140,GR,45,[q])
# Issuer reports and literal current certificate renumbering.
for u,ar,q in[(BR,117,'enero'),(AR,123,'enero'),(GR,89,'información')]:law(373,u,ar,[q,'adquisición'])
# Own-source pension clauses isolated by their actual numbered exemption within article9.
def clause(lf,u,ar,sub,needle,width=650):
 x=m['source'](u+'#a'+str(ar));t=x['text'];ma=list(re.finditer(r'(?m)^\s*'+str(sub)+r'\.(?:[0-9]+)?\s+',t))
 if not ma:E.append((lf,u,'clause',sub));return
 z=ma[-1];end=re.search(r'(?m)^\s*'+str(sub+1)+r'\.(?:[0-9]+)?\s+',t[z.end():]);text=m['norm'](t[z.start():z.end()+end.start()if end else len(t)]);k=text.lower().find(needle.lower())
 if k<0:E.append((lf,u,sub,needle));return
 a0=max(0,k-130);a0=text.rfind(' ',0,a0)+1 if a0 else 0;en=min(len(text),a0+width);en=text.rfind(' ',a0,en)if en<len(text)else en;push(lf,u+'#a'+str(ar),text[a0:en]+(' […]'if en<len(text)else''),'Own article '+str(ar)+'.'+str(sub),'rule / computed case where expressly labelled')
for lf in[659,661]:
 for u,sub in[(B,38),(A,44),(G,39)]:
  for q in['15','constante']:clause(lf,u,9,sub,q,850)
 for u,sub in[(A,44),(G,39)]:clause(lf,u,9,sub,'40',800)
for lf in[655,667]:bag(lf,37,['derechos económicos','aportaciones'])
for lf in[657,667]:
 for u,start,end in[(B,'Disposición Transitoria Trigésima Séptima.','Disposición Transitoria Trigésima Octava.'),(A,'Trigésimo primera.','Trigésima segunda.'),(G,'Disposición transitoria trigésima sexta.','Disposición transitoria trigésima séptima.')]:part(lf,u,start,end,'2026',900,'Own preserved pre2026 capital-benefit transition')
for lf in[663]:
 for u in[B,A,G]:a(lf,u,'el plazo de duración de la renta se computará','Own original-annuity-date additional provision',width=1100)
for lf in[665]:
 for u in[B,A,G]:
  part(lf,u,'la primera aportación al sistema de previsión','Reglamentariamente','1 por',1500,'Own provider-information yield fallback DA42/A40/G42')
# No-exemption small-route and active annual settlement are sourced elsewhere, not new methods.
for lf in[31,758,760]:bag(lf,75,['escala'])
# Foreign crypto custody: own2026 substantive gate is distinct from existing model-window orders.
BCUST='https://www.bizkaia.eus/documents/880307/15187815/ca_205_2008.pdf';ACUST='https://www.araba.eus/botha/Boletines/2026/122/2026_122_02967_C.pdf';GCUST='https://www.gipuzkoa.eus/documents/2456431/null/DF%2047-2013%20%282024-1%29.pdf/550c41c4-559d-808c-e123-b14fed696801'
BORD='https://www.bizkaia.eus/lehendakaritza/Bao_bob/2023/11/17/I-1346_cas.pdf?hash=7950f6b5cc88ab8b92ad8c236d3a13e6';AORD='https://www.araba.eus/botha/Boletines/2024/016/2024_016_00332_C.pdf';GORD='https://www.gipuzkoa.eus/documents/2456431/62711141/OF%20571-2023.pdf/1139fb71-fe01-3a52-6169-e4fa8568fd67?t=1703674947346'
for u,ar,lf in[(BCUST,'53quater',705),(ACUST,'23bis',706),(GCUST,'54bis',707)]:
 for l in[lf,701,710,712]:
  law(l,u,ar,['autorizad','notificación','registro','custodia','50.000','20.000','titulares','contabilidad'])
 law(lf,u,ar,['enero','marzo'if u==BCUST else'junio'])
for lf,u,q in[(705,BORD,'marzo'),(706,AORD,'marzo'),(707,GORD,'abril')]:a(lf,u,q,'Own existing721model order filing window; future2027 procedure remains bounded',width=700)
a(707,'https://www.gipuzkoa.eus/es/web/ogasuna/impuestos/modelo/721','50.000','G actual public721 page; inconsistency is expressly retained',width=700)
a(705,'https://www.bizkaia.eus/lehendakaritza/Bao_bob/2026/10/09/I-1138_cas.pdf','2026','B DF84/2026 operative replacement/effect; not full DAC8 review',width=700)
for lf in[719]:regs(lf,[109,105,121],['actividades económicas'])

for lf in[387,389,391,393]:part(lf,AI,'14.7.1.','14.7.2.','Base imponible',650,'A2024 Instruction14.7.1 explicit business-BI pool')
for lf in[397,399,401,403]:part(lf,'https://www.gipuzkoa.eus/documents/2456431/13761128/1-FAQ-TEXTO%2BUNIFICADO%2B19-05-2021.pdf/029ebb00-0fb1-aefe-cfde-2bae0eef4dd6','15.22 ','15.23 ','base imponible',1250,'G own TicketBAI FAQ15.22; only attribution formula incorporated as labelled ordinary88 inference')
for lf in[657,667]:part(lf,BI,'17.4.','17.5.','60',1000,'B2026 Instruction17.4 preserved first-capital benefit treatment')
# Actual care qualification / agreement / refusal chain, not analogical additions to Álava.
for q in['2.000','300','2023','agosto de 2022']:a(301,'https://egoitza.gipuzkoa.eus/ogasuna/normativa/docs/0001288c.pdf',q,'G DF6/2023 article11.3(f)/DT1 actual current qualification',width=850)
a(303,'https://www.boe.es/buscar/act.php?id=BOE-A-2023-5365#a3','Acuerdo de actividad','Ley3/2023 article3(f) documented activity agreement',width=650)
for ar in[45,46,47]:a(303,'https://www.boe.es/buscar/act.php?id=BOE-A-2024-8710#a'+str(ar),'acuerdo','RD438/2024 article'+str(ar)+' actual activity-agreement framework',width=650)
a(303,'https://www.boe.es/boe/dias/2024/12/16/pdfs/BOE-A-2024-26189.pdf','Fecha y firma','Resolution5December2024 actual agreement model',width=650)
for q in['25 %','20 %','45.3']:a(305,'https://www.boe.es/buscar/act.php?id=BOE-A-2023-1405#a48',q,'Basque Ley14/2022 article48.2 offer-refusal exceptions',width=750)
for q in['Vida laboral o certificado','IDC']:a(307,'https://web.araba.eus/es/-/hacienda/renta/deducciones-familias',q,'A actual family evidence instructions, certificate/IDC method',width=650)
# Statutory incorporation source for the ordinary35%business pool.
corp=json.loads(Path('ledgers/spain-2026-evidence/es-foral-corporate-tax/rows.json').read_text())
for z in corp:
 if z['guide_LF']in[196,202,203,204,207]:
  for lf in[381,391,401,403,409]:
   zz=copy.deepcopy(z);zz.update(id=len(L.rows)+1,guide_LF=lf,guide_wording=I[lf],section=next(x['section']for x in L.units if x['line']==lf));zz['note']='Own corporate credit-use groups incorporated through own PIT88. All example inputs/results are computed; special financing/block populations remain distinct.';L.rows.append(zz);L.sources[zz['url']]=m['source'](zz['url'])
