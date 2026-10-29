from pathlib import Path
import json,re,hashlib,subprocess
P=Path(__file__).resolve().parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');S=P/'support/germany-transfer-pricing';REF='62b7639a5a68324a83a96bb0190fff8b7c76f8c5';rel='skills/international/germany/germany-transfer-pricing.md';main_raw=subprocess.check_output(['git','show',REF+':'+rel],cwd=R);raw=(R/rel).read_bytes();text=raw.decode();sha=lambda b:hashlib.sha256(b).hexdigest()
ident={json.loads(f.read_text())['id']:json.loads(f.read_text())for f in (P/'sources').glob('*.identity.json')};A={};src={k:Path(z['reader_path']).read_text().split('\n')for k,z in ident.items()}
roles={'a1':'U2326adf0b537438c','ao90':'Ua6a28ca7a568b265','g1':'Ua93a9e58d3cbbf9f','g2':'U921644cfc5ac7460','g3':'U9fb17aa84a48ba4d','g4':'U8353b35d10b5f3f7','g5':'Uef46f8eacbe29c55','g6':'U9022e5d1ce5ddb70','g7':'Uf6fafa23261f0018','annex':'U5cbe7c20afaf1523','cb':'U0ab387a9c7139dab','ao162':'Uee2258b31aab48c3','apa':'U4912c7b237929b37','eg37':'Ubce83584837ebc71','eg31':'Ua1563fa313d548a8','ao149':'U503bfe74d589da30','matrix':'Ue1b7b85d7f51ac1f','bmf24':'Ua56a40277de56de0','bmf20':'U8ef48f669ff464bb','bmfapa':'U4e7898fbc57f02f9','transmit':'U8b8e2bf28bca907c','faq':'U86fc0388e3db84e2','return':'U89f95c957e4927d3','service':'U03a6dc0ca5c0f130','minimum':'U0085cf8336d322b7','a1a':'U732515333ac6badf','public':'U64cf9e0c4b718812','e4j':'U299b3fbe59cb42d3','e52':'Uc569ed131070949c','fine':'Uec60fb30d6850f63'}
def take(k,role,lo,hi,label):
 so=roles.get(role,role);z=ident[so];q='\n'.join(src[so][lo-1:hi]);assert q
 A[k]=dict(id=k,source=so,article=label,url=z['url'],LF_start=lo,LF_end=hi,exact_quote=q,raw_sha256=z['raw_sha256'],reader_sha256=z['reader_sha256'],read_on='2026-10-28/29; session crossed midnight; not an invented acquisition date',line_convention="literal LF split('\\n')")
def para(k,role,num,label):
 so=roles[role];a=src[so];lo=next(i for i,l in enumerate(a)if l.startswith('('+str(num)+')'));hi=lo+1
 while hi<len(a)and not a[hi].startswith(('(', 'Fußnote','zum Seitenanfang')):hi+=1
 take(k,role,lo+1,hi,label)
for role,nums,law in [('a1',['1','2','3','3a','3b','3c','3d','3e','4','5'],'AStG §1'),('ao90',['1','2','3','4'],'AO §90'),('g1',['1'],'GAufzV §1'),('g2',['1','2','3','4','5','6'],'GAufzV §2'),('g3',['1','2'],'GAufzV §3'),('g4',['1','2','3'],'GAufzV §4'),('g5',['1','2'],'GAufzV §5'),('g6',['1','2','3'],'GAufzV §6'),('cb',['1','2','3','4','5','6','7'],'AO §138a'),('ao162',['3','4','4a'],'AO §162'),('apa',['1','3','4','6','7','8'],'AO §89a'),('eg37',['2','3','5'],'EGAO Art97 §37')]:
 for n in nums:para(role+'-'+n,role,n,law+'('+n+')')
take('g7','g7',7,7,'GAufzV §7');take('eg31','eg31',7,7,'EGAO Art97 §31');take('deadline7','ao149',8,8,'AO §149(2)');take('deadlineadvised','ao149',9,24,'AO §149(3)/(4) introductory clause');take('fineintent','fine',24,24,'AO §379(2) opening');take('finebreach','fine',30,31,'AO §379(2) no1c');take('fineamount','fine',48,48,'AO §379(5)');take('transmit','transmit',37,45,'BZSt XML/DIP/upload procedure');take('taxreturn','return',39,46,'BZSt tax return entries / Anlage WA');take('faqnotice','faq',92,93,'BZSt FAQ prior notice');take('faqfine','faq',103,105,'BZSt FAQ fine / competent state authority');take('service','service',35,47,'BZSt APA service eligibility/types');take('minimum','minimum',6,7,'MinStG §101(1)');take('public','public',6,13,'HGB §342b separate duty');take('e4j','e4j',6,6,'EStG §4j repealed');take('e52','e52',22,22,'EStG §52(8c)');take('a1a','a1a',6,12,'AStG §1a actual price-adjustment provision')
# Distinct annex items rather than citing the whole annex for each separate item.
a=src[roles['annex']]
for n in range(1,19):
 if n==1:lo=8
 else:lo=next(i+1 for i,l in enumerate(a)if l==str(n)+'.')
 hi=next((i for i in range(lo,len(a))if re.fullmatch(r'\d+\.',a[i])),len(a)-1)
 if n==18:hi=next(i for i,l in enumerate(a)if l.startswith('Soweit in Satz'))
 take('ann'+str(n),'annex',lo+1,hi,'GAufzV annex item'+str(n))
last=next(i+1 for i,l in enumerate(a)if l.startswith('Soweit in Satz'));take('ann-open','annex',last,last,'GAufzV annex final sentence')
for k,lo,hi in [('matrix-def',62,65),('matrix-content',68,90),('matrix-format',91,99),('matrix-before',102,127),('matrix-other',128,133),('matrix-fine',135,137)]:take(k,'matrix',lo,hi,'BMF2Apr2025 '+k)
for n,lo,hi in [('1.1',196,210),('2.2',549,556),('3.9',657,667),('3.10',668,670),('3.12',684,691),('3.13',697,703),('3.30',866,869),('3.63a',1167,1173),('3.74',1241,1246),('3.75',1247,1257),('3.76',1258,1262),('3.77',1263,1269),('3.133',1860,1866),('3.136',1884,1891),('3.152',2170,2177),('4.7',2315,2320),('4.8',2321,2326),('6.2',2343,2349)]:take('b24-'+n,'bmf24',lo,hi,'BMF12Dec2024 Rn'+n)
for n,lo,hi in [('34',368,379),('38',412,415),('39',418,427),('55',636,651),('56',652,656),('88',920,921),('89',923,931)]:take('b20-'+n,'bmf20',lo,hi,'BMF3Dec2020 Rn'+n+' (only as unchanged by later law)')
for n,lo,hi in [('1.1',59,67),('1.3',75,83),('1.5',93,99),('1.8',112,125),('1.18',230,239),('4.2',416,429)]:take('bapa-'+n,'bmfapa',lo,hi,'BMF26Jun2024 Rn'+n)
M={32:['bapa-1.1','cb-6'],33:['a1-1','ao90-3','ao90-4','ao162-3','ao162-4','cb-1','apa-1'],34:['g1-1'],35:['a1-2'],36:['a1-1','a1-4','a1-5'],37:['a1-1','a1-5'],38:['b24-2.2'],39:['g7','eg37-5'],41:['g2-5'],48:['ao90-3','matrix-def'],49:['ao90-3','g6-1'],50:['ao90-3'],51:['ao90-3'],52:['g2-1','g1-1'],53:['g2-2'],54:['g2-3'],55:['g2-4'],56:['g2-5','b20-34'],57:['g4-3'],66:['ao90-3'],72:['ao90-3'],73:['b20-55'],74:['ao90-3'],75:['ao90-3'],76:['g5-1','b20-56'],77:['g5-1','g5-2'],78:['ao90-4'],79:['g2-5','g5-1'],86:['ann3','ann4'],88:['ann1'],109:['ann-open'],117:['g4-1'],118:['ao90-3','g4-1','g6-1'],119:['g4-1'],120:['g4-2'],121:['ao90-4','g2-6'],128:['g6-2'],129:['g6-2'],131:['g6-2'],132:['g6-1','b20-38','ao90-4'],133:['g6-2'],134:['g6-3'],135:['b20-39'],136:['g6-1'],137:['a1-1','b20-88'],138:['g6-1','ao162-4'],142:['eg37-5','ao90-3'],149:['matrix-def'],150:['matrix-content'],151:['matrix-content','g2-3'],152:['ao90-4'],153:['matrix-format'],154:['matrix-before'],155:['matrix-other'],156:['ao162-4'],165:['cb-1'],171:['cb-1'],172:['cb-1'],173:['cb-3'],174:['cb-4'],175:['cb-6'],176:['cb-6','transmit'],177:['cb-5','faqnotice','taxreturn'],178:['cb-2'],179:['eg31'],185:['a1-1'],186:['a1-1'],187:['a1-3'],188:['a1-1','b24-1.1'],189:['a1-3'],190:['a1-4'],204:['a1-3','b24-3.12','b24-3.13'],206:['b24-3.10'],210:['a1-3'],214:['a1-3a'],215:['a1-3a','b24-3.30'],216:['a1-3a'],217:['a1-3a'],218:['ao162-3'],226:['ao90-4'],227:['ao90-4'],228:['ao90-3','ao90-4'],229:['ao90-4'],230:['ao90-3'],231:['cb-6'],232:['cb-5'],233:['taxreturn','ao90-4'],241:['g3-1','ao90-3','ao90-4'],242:['g3-2'],243:['ao90-4','eg37-5'],244:['ao90-4'],245:['ao90-4'],246:['ao90-4'],247:['cb-6'],248:['deadline7','deadlineadvised'],257:['ao162-4'],258:['ao162-4'],259:['ao162-4'],260:['ao162-4'],261:['ao162-4'],263:['ao162-4'],264:['ao162-4'],265:['ao162-4'],266:['ao162-4'],267:['ao162-4'],268:['eg37-5'],269:['b20-89'],273:['ao162-3'],274:['ao162-3'],275:['ao162-3'],276:['eg37-2','eg37-3'],283:['finebreach','fineamount'],285:['fineintent','fineamount'],286:['finebreach','cb-5'],287:['faqfine'],296:['apa-1'],297:['apa-1','bapa-1.5','service'],298:['bapa-1.1'],299:['apa-1','bapa-1.8','service'],300:['apa-1'],301:['apa-1','apa-6'],302:['bapa-1.18'],303:['apa-3'],304:['apa-4'],305:['bapa-4.2'],313:['apa-7'],314:['apa-7'],315:['apa-7'],316:['apa-7','g6-2'],317:['apa-7','g6-2'],319:['apa-7'],320:['apa-1','apa-7'],321:['apa-7'],322:['apa-8'],323:['apa-7','fineamount'],329:['a1-1'],336:['b24-3.74','b24-3.75','b24-3.76','b24-3.77'],337:['a1-3d','b24-3.133','b24-3.136'],338:['a1-3e'],339:['b24-3.152'],340:['b24-3.63a','b24-6.2'],341:['g6-1','g6-2','a1-1'],342:['a1-1'],348:['g6-1','a1-1'],349:['g6-1','g6-2','ao90-4'],350:['ao90-3'],351:['ao90-1','ao90-2'],352:['a1-1'],360:['eg37-5','ao90-3','ao90-4','ao162-4'],361:['matrix-format','matrix-content'],362:['b24-6.2'],363:['b24-3.63a','b24-6.2'],365:['bapa-1.1'],366:['minimum'],367:['a1-3','a1-3a'],376:['a1-1','b20-89'],377:['b24-4.7','b24-4.8'],378:['cb-7','matrix-def'],379:['ann17','cb-1'],383:['a1-1','a1-2','a1-4','a1-5'],384:['a1-3','a1-3a'],385:['g6-2','g6-3'],386:['ao90-3','g4-1','g2-5'],387:['ao90-3','g5-1'],388:['g3-1'],389:['ao90-4'],390:['cb-1','cb-6','taxreturn'],391:['apa-1','apa-3','apa-7'],392:['ao162-3','ao162-4'],406:['a1-3b','a1-3c','a1a'],407:['public'],408:['a1-3d','a1-3e'],409:['a1-5'],412:['ao162-4a'],413:['e4j','e52'],415:['g6-1','ao90-3','ao162-4']}
for n in range(1,19):M[89+n]=['ann'+str(n)]
for lf in range(199,204):M[lf]=['b24-3.9']
# Explicit application bridge uses selected A21 reader paragraphs already actually read in exit stage.
for k,para_no,label in [('a21entry',1,'AStG §21(1)'),('a21finance',2,'AStG §21(1a)')]:
 z=ident['A21'];q=src['A21'][para_no-1];A[k]=dict(id=k,source='A21',article=label,url=z['url'],LF_start=para_no,LF_end=para_no,exact_quote=q,raw_sha256=z['raw_sha256'],reader_sha256=z['reader_sha256'],read_on='2026-10-28',line_convention='derived paragraph reader; literal LF')
M[39]+=['a21entry','a21finance'];M[344]=['a21finance'];M[364]=['a21finance'];M[367]+=['a21entry']
if __name__=='__main__':
 (S/'TP-anchor-bank.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n');(S/'TP-current-bindings.json').write_text(json.dumps(M,indent=2)+'\n');print(len(A),'source anchors',len(M),'explicit current units bound')
# Supplementary exact date/effect anchors; no assumption that acquisition proves these clauses were read.
take('date24','bmf24',8,8,'BMF12Dec2024 actual date');take('date20','bmf20',9,9,'BMF3Dec2020 actual date');take('datematrix','matrix',8,8,'BMF2Apr2025 actual date');take('dateapa','bmfapa',8,8,'BMF26Jun2024 actual date');take('aparepeal','bmfapa',594,605,'BMF26Jun2024 sectionII; old pending applications retained');take('b24-doc','bmf24',1019,1021,'BMF12Dec2024 Rn3.46 reference to2020 documentation principles')
M[19]=['date24','date20','datematrix','dateapa','eg37-5','b24-doc'];M[365]=['dateapa','aparepeal'];M[414]=['a1-1','b24-1.1'];M[420]=['a1-3b','a1-3c','a1a']

base_rows=json.loads((P/'history/TP-before-root-DE-L03/support/claim-rows.json').read_text());new_rows=json.loads((S/'pending-claim-inventory.json').read_text());MM={}
for z in base_rows:
 hits=[x for x in new_rows if x['wording']==z['wording']]
 if hits and z['lf']in M:MM[hits[0]['lf']]=M[z['lf']]
M=MM
for z in new_rows:
 if z['wording'].startswith('Version '):pass
 elif z['wording'].startswith('- Worked-example source contexts'):M[z['lf']]=['a1-1','a1-2','a1-3','b24-3.9','b24-3.74','b24-3.75','b24-3.76','b24-3.77']
 elif z['section'].startswith('Example 1:'):M[z['lf']]=['a1-1','b24-3.74','b24-3.75','b24-3.76','b24-3.77']
 elif z['section'].startswith('Example 2:'):M[z['lf']]=['a1-1','a1-2','a1-3','b24-3.9']

# A1 current definitions do not create an exclusive German worldwide comparison.
rows=json.loads((S/'pending-claim-inventory.json').read_text())
for z in rows:
 lf=z['lf'];w=z['wording'];z['anchors']=M.get(lf,[])
 if z['section'].startswith('Example '):z['kind']='fictional example gates/inputs/computation; quoted own method, not official numerical input'
 elif z['anchors']:z['kind']='legal rule / source chain'
 elif z['section']=='Ask the client first':z['kind']='intake question; not a positive legal assertion'
 elif z['section']in ['Sources','Disclaimer']or lf in [44,325]:z['kind']='source routing, attribution or disclaimer'
 elif lf in [23,31,40,42] or w.startswith('Version '):z['kind']='version/country/currency context; not a tax figure'
 elif w.startswith('**')and w.endswith('**'):z['kind']='presentation subheading'
 elif w in ['| Field | Value |','| What | Value | Note |','| Item | Detail |','| Method | Accepted |','| Obligation | Detail | Law and link |','| Item | Deadline | Law and link |','| Area | Detail |','| Date | Development | Link |','| Related Guide | Interaction |']or w.startswith('| Source'):z['kind']='presentation/source-table routing'
 elif lf in [306,405,410,411]:z['kind']='explicit operational limit/referral; no quantitative entitlement asserted'
 elif lf==375:z['kind']='working-paper coordination advice, not a separately asserted disclosure statute'
 else:z['kind']=next((x['kind']for x in base_rows if x['wording']==w),'UNCLASSIFIED')
 if w.startswith('- A relocation of functions'):z['finding']='DE-L01 resolved by root Guide successor: own1(3b) transfer package /1(3c) intangible remuneration /1a price-adjustment split; old wording retained in history'
 if lf in [138,415]:z['limit']='Actual smaller-company transaction-matrix boundary remains explicit; no invented exemption'
# Complete old-topic extraction and exact semantic mapping against real pre-September refresh plus currentmain.
def units(t):
 s='';meta=True
 for i,l in enumerate(t.split('\n'),1):
  if i==1:continue
  if meta:
   if l=='---':meta=False
   continue
  if '<!-- openaccountants-cta-block -->'in l:break
  if l.startswith('#'):s=l.lstrip('# ');continue
  if l.strip()and not re.fullmatch(r'\|[-:| ]+\|',l):yield i,s,l
oldref='7dc926e3c7c7befd1f5c7cb533f1669b861a344b';older=subprocess.check_output(['git','show',oldref+':'+rel],cwd=R).decode();old=[]
fieldmap={
('Section 1','Tax authority'):(32,'Reconciledassessment/audit/BZStroles'),('Section 1','Key TP legislation'):(33,'Expandedoperativechain'),('Section 1','Documentation regulation'):(34,'Retainedregulation'),('Section 1','Effective date (current regime)'):(39,'Reconciledcommencement'),('Section 1','Documentation language'):(41,'CORRECTED: Englishrequiresapplication/permission, notautomatic practice'),('Section 1','Skill version'):(42,'Presentationversion'),
('2.1','Required?'):(66,'CORRECTED: Germanbusinessownturnover, notgroupconsolidatedrevenue'),('2.1','Format'):(76,'CORRECTED: ownGAufzVannex18items'),('2.1','Filing'):(78,'Retained30daydeadline'),('2.1','Language'):(79,'CORRECTED: priorEnglishautomaticpracticebecomespermissiongate'),
('2.2','Required?'):(118,'CORRECTED: dutyexistsbelowthreshold;reliefnotexemption'),('2.2','Thresholds'):(128,'Retainedboththresholds; current128–137completeconditions'),('2.2','Format'):(119,'Expandedownfourblocks'),('2.2','Filing'):(121,'CORRECTED: anytime request; notonlyduringaudit'),
('2.3','Content'):(150,'Retainedexpandedcontents'),('2.3','Submission'):(152,'Retainedwithoutseparaterequest'),('2.3','Format'):(153,'Retainedofficiallayoutpluspermitteddeparture'),
('2.4','Threshold'):(165,'Retained750millionpriorconsolidatedrevenue'),('2.4','Filing deadline'):(175,'Retainedoneyear'),('2.4','Filing method'):(176,'RetainedXMLpluscurrentDIP'),('2.4','Notification'):(177,'CORRECTED: taxreturnstatement, noseparateannualBZStnotice'),('2.4','Effective'):(179,'Retained2015/2016distinction'),
('Section 4','Transaction matrix'):(226,'Retained'),('Section 4','Master File'):(227,'Retained'),('Section 4','Local File'):(229,'Retained30days,requestanytime'),('Section 4','Extraordinary transactions'):(228,'Retained'),('Section 4','CbCR'):(231,'Retained'),('Section 4','CbCR notification'):(232,'CORRECTED: taxreturnstatement,noseparateannualBZStnotice'),('Section 4','Corporate tax return'):(233,'Qualified: noTPfileswithreturn; CbCRAnlageWAstatementretained'),
('Section 5','Documentation preparation'):(241,'CORRECTED: extraordinarysixmonthrule,otherrecordsreadyforrequest'),('Section 5','Transaction matrix + Master File submission'):(243,'Retained'),('Section 5','Local File submission'):(245,'Retained'),('Section 5','Extraordinary transactions'):(244,'Retained'),('Section 5','CbCR filing'):(247,'Retained'),('Section 5','Corporate tax return'):(248,'Expandedsevenmonths/advisedlastFeb/earlierorder'),
('Section 6','Non-submission or unusable documentation'):(257,'Retainedfixedfloorand5–10percentcurrent257–267'),('Section 6','Late submission of documentation'):(260,'Retainedlateusablecase;100full-dayfloorLF261'),('Section 6','Non-submission of transaction matrix'):(257,'Retainedfixed5000'),('Section 6','Late/missing CbCR'):(283,'Retainedintent/recklessnessandconditions'),('Section 6','Late/missing CbCR notification'):(286,'CORRECTED: taxreturnstatementnotnamedin379fine; ownfallbackconsequence'),('Section 6','Adverse estimation'):(273,'Retainedrebuttablepresumption'),('Section 6','Burden of proof'):(274,'CORRECTED: ownstatutorypresumption/range,notgeneralburdenshift'),
('Section 7','Availability'):(296,'Retainedtreaty/risk/prospectgates'),('Section 7','Types'):(297,'CORRECTED: interstatebi/multi;notgenericunilateralAPA'),('Section 7','Governing authority'):(298,'RetainedownBZSt/Landauthorityroles'),('Section 7','Application fee'):(313,'CORRECTED:30000standard/10000smaller, not20000'),('Section 7','Typical duration'):(301,'CORRECTED: normallymax5years,notstatutory3yearfloor'),('Section 7','Processing time'):(306,'Not yet confirmed: historical12–36monthsnotprintedinthecitedpages; explicitcurrentlimit'),('Section 7','Binding effect'):(304,'Retainedconditionalbindingeffect'),('Section 7','Annual reporting'):(305,'Retainednormallycontractualcompliancereport'),
('Section 8','Low-value intra-group services'):(336,'Retained5percentwithowneligibility/uniformapplication'),('Section 8','Interest rates'):(337,'ReplacedgenericBundesbankbenchmarkwithownAStGgroup-ratingandnamedanalysisconditions'),('Section 8','Documentation thresholds'):(341,'CORRECTED: bothnotexceeded; lightercompliancenotdutyexemption'),('Section 8','Small transactions'):(342,'Retained'),
('Section 9','January 2025'):(360,'RetainedcurrentBEGIV'),('Section 9','April 2025'):(361,'Retained'),('Section 9','2024'):(366,'CORRECTED: ownMinStGafter30Dec2023,notfrom31Decunqualified'),('Section 9','2022'):(367,'Retainedexpandedownlaw'),
('Section 10','germany-bookkeeping'):(375,'Retainedworking-papercoordination'),('Section 10','germany-corporate-tax'):(376,'Movedtosamecurrentcorporateparagraph/siblingde-corporate-tax'),('Section 10','germany-vat'):(377,'Retainedcustoms/importVATmethodandcurrentgermany-vat-returnroute'),('Section 10','CbCR'):(378,'Qualified: owntransmission/usepowers,notunprovedblanketcase-selectionclaim'),('Section 10','Financial statements'):(379,'Retainedcoordinationadviceandconsolidated-revenuebasis')}
# Human-readable destination labels; no guessed numeric similarity is used.
for key,(target,note) in list(fieldmap.items()):
 if note.startswith('CORRECTED:'): note='Corrected historical formulation; the exact current rule is quoted at the linked destination'
 elif note.startswith('Not yet confirmed:'): note='Not yet confirmed: historical 12–36 month processing time is not printed by the acquired authority pages'
 else: note='Same substantive topic retained or expanded at the exact current rule'
 fieldmap[key]=(target,note)
for field,target in [('Comparable Uncontrolled Price (CUP)',199),('Resale Price Method (RPM)',200),('Cost Plus Method (CPM)',201),('Transactional Net Margin Method (TNMM)',202),('Profit Split Method (PSM)',203),("Hypothetical arm's length test",204)]:
 fieldmap[('3.2',field)]=(target,'Accepted method retained; historical unique-to-Germany label is not established by the German primary text' if target==204 else 'Accepted method retained')
for ref,body in [(oldref,older),(REF,main_raw.decode())]:
 for lf,sec,w in units(body):
  matches=[z for z in rows if z['wording']==w];dest=None
  if matches:dest='Exact wording retained: '+matches[0]['section']+', currentLF'+str(matches[0]['lf'])
  elif w.startswith('**')and w.endswith('**')or re.match(r'^\| (Field|What|Item|Method|Obligation|Area|Date|Related skill|Offence) \|',w):dest='Presentation heading/table labels; current matching substantive section retained'
  elif lf==406 and ref==REF:dest='Source-corrected referral at currentLF444: §1(3b) transfer package; §1(3c) intangible remuneration; §1a price adjustment. Original intangible topic retained; original single §1a-only locator corrected by root.'
  elif w.startswith('Version '):dest='Presentation version updated to1.2; currentLF23, no substantive rule dropped'
  elif sec=='Disclaimer':dest='Disclaimer/presentation; current Disclaimer and originalCTA untouched'
  elif w.startswith('|'):
   field=w.split('|')[1].strip();sk=next((key for key in ['2.1','2.2','2.3','2.4','3.2','Section 10','Section 1','Section 4','Section 5','Section 6','Section 7','Section 8','Section 9']if sec.startswith(key)),sec)
   mm=fieldmap.get((sk,field))
   if mm:dest=mm[1]+'; currentLF'+str(mm[0])+', '+next(z['section']for z in rows if z['lf']==mm[0])
   elif field in ['OECD member?','BEPS signatory?']:dest='Not yet confirmed: historical membership/signatory statement is not quoted from the acquired primary pages; no current replacement is asserted'
   elif field=='Ongoing':dest='Not yet confirmed: historical audit intensity/digital tools assertion is not established. Amount B monitoring is superseded by the actual limited method at current LF340/363'
  elif sec.startswith('3.1'):dest='Expanded own arm\'s length and hypothetical method, current LF185–190'
  elif sec.startswith('3.3'):dest='Corrected: no automatic CUP priority; best-fitting method at current LF210'
  elif sec.startswith('3.4'):dest='Corrected: statutory median unless another in-range value is credibly more appropriate, current LF214–218'
  elif sec.startswith('3.2'):dest='Own BMF accepted methods at current LF199–204. Historical exclusive-to-Germany label is not confirmed and is not retained'
  elif sec.startswith('2.3'):dest='Current transaction matrix commencement at LF142 and full catalogue LF149–156'
  elif 'Germany does not have broad statutory' in w:dest='Qualified, source-bounded absence of a general safe harbour, current LF329/348'
  elif sec.startswith('8.1'):
   if 'EUR 100m group' in w:dest='Corrected: own German business prior turnover, current LF350'
   elif 'EUR 6m' in w:dest='Corrected: both inclusive thresholds and lighter record duties, current LF349'
   elif '§90 AO' in w:dest='Retained general cooperation duty, current LF351'
   else:dest='Retained pricing challenge rule and operational explanation, current LF348/352'
  if dest is None:dest='PENDING SEMANTIC DESTINATION';print('OLDUNMAPPED',ref[:8],lf,sec,w[:160])
  old.append(dict(ref=ref,old_lf=lf,section=sec,wording=w,destination=dest))
for n,v in [('claim-rows.json',rows),('actual-read-quotes.json',list(A.values())),('old-topics.json',old)]: (S/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
missing=[z['lf']for z in rows if z['kind']=='UNCLASSIFIED'];print('CURRENT UNCLASSIFIED',missing)
# Shared source bank holds complete exact selected clauses once. Each row quotes its own anchor text.
def esc(s):return str(s).replace('|','\\|').replace('\n','<br>').replace('\r','')
out=['# Figure/rule ledger: germany-transfer-pricing','',f'Current local root-corrected Guide `{sha(raw)}`, derived from public main `{REF}`. Private writer ledger, not independent review. No Guide edit. Actual selected readings occurred across 28/29 October 2026; the source log preserves the session date boundary instead of inventing per-clause timestamps. Original raw sources are shared, never copied per row or normalized.','','Rows preserve every current substantive/operational unit; presentation/source routing is explicitly classified. Every positive source-bound legal row carries the quoted own provision. DE-L01 at currentLF406 has been source-corrected by root: the former §1a-only referral is recorded in the old-topic history, while the current row distinguishes transfer packages, intangible remuneration and price adjustment. Existing precise transaction-matrix/small-company and other Sources boundaries remain unaltered.','','| LF | Section | Exact current figure/rule | Own act/article / officialURL | Short original-language clause (complete selected operative context) / classification | Read on |','|---|---|---|---|---|---|']
for z in rows:
 aa=[A[k]for k in z['anchors']];cite='<br>'.join(a['article']+' '+a['url']for a in aa)or'—';q='<br>'.join(a['exact_quote']for a in aa)or z['kind'];
 if z['section'].startswith('Example ') and not z['wording'].startswith('These are fictional'):q='Fictional input or arithmetic derived from this example’s declared facts; not an official-source numerical quotation. Source gates are quoted in the example narrative row and actual-read-quotes.json.'
 out.append('| '+' | '.join(esc(x)for x in [z['lf'],z['section'],z['wording'],cite,q,'2026-10-28/29'if aa else'—'])+' |')
out+=['','## Old topics carried','',f'Actual pre-September20 source-refresh comparator `{oldref}` plus current public-main `{REF}`. No separate platform predecessor is claimed. Semantic corrections are explicit, not false retention of older wrong rules.','','| Comparator/LF | Exact old topic | Verified current destination / correction / boundary |','|---|---|---|']
for z in old:out.append('| '+' | '.join(esc(x)for x in [z['ref'][:12]+':'+str(z['old_lf']),z['wording'],z['destination']])+' |')
out+=['','## Writer checks and limits','','The 124 original prepared anchors plus narrow date/effect additions are exact substrings of pinned readers. No claim that5434lines of2024BMFannexes or1003lines of2020principles were wholly read. Selected named paragraphs only; actual-scope log and bank quote coordinates use literalLF, including PDF formfeeds as ordinary characters. Older2020paragraphs are used only with the unchanged own current statute/regulation and the2024BMFreference, never as invented2026quotations.','','No actual-case pricing study or administrative software was run. Original main and v1.1 had zero executable worked examples; root added two explicitly fictional sourced examples in v1.2. The saved DE-L03 options predate that root edit. Both algorithms use declared hypothetical eligibility/comparability inputs, not invented statutory prices; no automatic CUP priority or median is implied. Derived internal controls separately test threshold inclusivity/lag, fixed-vs-proportional surcharge andAPAfees from the quoted own clauses, not as official worked-example quotations.','']
f=P/'ledgers/germany-transfer-pricing.md';f.write_text('\n'.join(out))
checks=dict(guide_sha256=sha(raw),ledger_sha256=sha(f.read_bytes()),current_units=len(rows),quoted_anchors=len(A),old_units=len(old),unclassified_current=missing,pending_old=[z['old_lf']for z in old if z['destination']=='PENDING SEMANTIC DESTINATION'],literal_quote_substrings=all(a['exact_quote']in'\n'.join(src[a['source']])for a in A.values()),Guide_unchanged=(R/rel).read_bytes()==raw,known_finding='DE-L01 source-corrected by root; writer did not edit Guide',new_independent_review=False);(S/'writer-checks.json').write_text(json.dumps(checks,indent=2)+'\n');print(checks)
