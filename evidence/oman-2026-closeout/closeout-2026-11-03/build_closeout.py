"""Deterministic writer evidence generation. Never edits a Guide or frozen evidence."""
from pathlib import Path
import json, re, hashlib, collections, sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
OLD=ROOT/'evidence/oman-2026-closeout'
OUT=Path(__file__).resolve().parent
SOURCES=ROOT.parent/'sources'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
files=['pit-rule-ledger.json','additional-rule-ledger.json','spf-law-ledger.json','vat-law-ledger.json','authority-rule-ledger.json']
rows={r['id']:{**r,'inherited_from':f} for f in files for r in json.loads((OLD/f).read_text())}
guides={p.stem:p for p in (ROOT/'skills/oman').glob('*.md') if p.stem!='README'}
texts={g:p.read_text().splitlines() for g,p in guides.items()}
# Explicit human-selected operative uses. No inherited broad Guide-level placements are used.
M={
'om-company-formation':{
'F-ART4':[20,26,56],'F-ART5':[20,56],'F04':[27],'F01':[28,29,64,66],'F02':[30],'F03':[30],'F05':[31,77,79],
'F-ART219':[37],'F-ART291':[37],'F-ART292':[37],'F-ART293':[37],'F-ART296':[37],'F-ART297':[37],
'C02':[46,47],'A01':[48],'A02':[48,52],'C03':[52],'G09':[52],'SPL58':[52],'C01':[60]},
'om-tax-overview':{
'P01':[26,74,76],'P03':[26,74,76],'P06':[26,74,76],'C10':[27,39,62,64],'C22':[28],'C12':[29],
'C05':[30],'C11':[30],'V036':[31],'V047':[31],'V051':[31],'N01':[32],
'SPL70':[35],'SPL90':[35],'SPL116':[35],'SPL123':[35],'SPL128':[35],
'C01':[39],'SPL1':[39],'A02':[45,46],'C06':[47],'V072':[48],'G09':[48],
'SPL58':[49],'P23':[50],'C19':[54],'V001':[54],'N02':[58]},
'om-income-tax':{
'P01':[20,26,49,66,70,72,84,86,103],'P02':[20],'P03':[28,48,70,72,84,86],
'P04':[66],'P05':[20],'P06':[27,36,70,72,84,86],'P07':[36,84,107],'P08':[29,84,86],
'P09':[42],'P10':[38],'P11':[38],'P12':[38],'P13':[38],'P14':[38],'P15':[31,38],
'P16':[38],'P17':[38],'P18':[38],'P19':[38],'P20':[40],'P21':[84],
'P22':[40],'P23':[48,49,50],'P24':[52],'P25':[53,54],'P26':[62],'P27':[51],
'P28':[30,84],'P29':[32,62],'P30':[62],'P31':[55,56],'P32':[62]},
'om-corporate-income-tax':{
'C01':[20],'C10':[20,26,67,69,82,84],'A01':[20],
'C22':[27,29,82,84],'C12':[30],'C05':[31,63],'C11':[31,63],
'C15':[32],'C19':[33,59,67,69],'C23':[34,59],'C24':[35,59],'C25':[36,59],
'C03':[40],'C-ART159bis-10':[40],'C13':[40],'C14':[40],'C08':[40],'C09':[40],
'C17':[40],'C04':[40],'A03':[40],'C02':[46,47],'A02':[48,49,50],
'C18':[51],'A04':[51,53,55],'C06':[52],'C-ART160':[53],'C-ART160bis':[53],
'C26':[59],'C20':[59],'C-ART40':[63],'A05':[63],'C16':[63]},
'om-payroll-social':{
'P01':[20,38],'SPL68':[20,56],'SPL70':[26,44,60,62,74,76],
'SPL87':[27,56],'SPL90':[27,44,60,62,74,76],
'SPL115':[28,44],'SPL116':[28,44,60,62,74,76],
'SPL121':[29,44,56],'SPL123':[29,44,60,62,74,76],'S02':[29],
'SPL128':[30,44,60,62,74,76],'SPL52':[35,40,44,74,76],'SPL5':[35],
'SPL139':[36],'S03':[36],'SPL155':[37,52],'SPL1':[44,60,62,74,76],
'SPL58':[48],'S01':[56],'SPL136':[56],'SPL138':[56]},
'oman-vat':{
'V055':[20,40],'V057':[20,42],'V060':[20],'V036':[39,64,76,77,116,118,134,136,149,151,169],
'G01':[40,41,134,136],'V061':[41,134,136],'G08':[43,82,84,96,97,110],
'V001':[44,106],'N03':[45,46,47],'V051':[48,89],'V052':[49,95,110,169],'V053':[49],
'V047':[50,90],'G02':[52],'G03':[52],'G04':[52,70],'V037':[52],
'V031':[56,149,151,169],'V032':[56],'V034':[56],'V039':[56,92],'V040':[98,169],
'V041':[58,64,99,116,118,134,136,149,151,169],'V044':[58],
'G05':[31,58,60,116,118,134,136,149,151,169],
'G06':[60,149,151,169],'V043':[60],'V042':[62],'G07':[33,62],
'G09':[82],'V071':[82],'V072':[82,84],'V100':[106],'V101':[106],
'G10':[33,110],'N02':[112]}}
# Printed line references checked against the fixed current Guide hashes below.
# Code block placements include the entire oa-check, not its opening fence only.
def location(g,n):
 ls=texts[g]; end=n
 if ls[n-1].startswith('```'):
  end=next(i+1 for i in range(n,len(ls)) if ls[i].startswith('```'))
 section=''
 for l in ls[:n]:
  if l.startswith('## '):section=l[3:]
 return {'guide':g,'path':str(guides[g].relative_to(ROOT)),'line_start':n,'line_end':end,'section':section,'text':'\n'.join(ls[n-1:end]),'guide_sha256':sha(guides[g])}
for r in rows.values():
 r['historical_placements']=r.pop('placements',[])
 r['placements']=[]
 r['effective_status']='source preparation only; no operative Guide use'
 if r['id'].startswith('S0'):r['source_language']='Arabic original, official gazette, visually read 2026-11-01'
 if r['id'].startswith('V'):r['source_language']='English Tax Authority-hosted translation; Arabic original not transcribed'
 if r.get('complete_checked_clause'):
  r['historical_short_quote']=r['quote']
  # Full already-read clause replaces truncated midword excerpts. Original bytes preserved upstream.
  r['quote']=r['complete_checked_clause']
  r['quote_scope']='Complete previously checked clause in official-hosted English translation, including exceptions; not an Arabic-original claim.'
 else:r['quote_scope']='Inherited exact short excerpt; see quote-coverage-gaps.json for omitted subordinate propositions.'
for g,m in M.items():
 for rid,ns in m.items():
  for n in ns:rows[rid]['placements'].append(location(g,n))
  rows[rid]['effective_status']='operative reference or conditional illustration; apply per-use scope below'
# Source record supplement helpers. Cache reads only, never a network request.
def clause(path,article):
 txt=(SOURCES/path).read_text()
 pat=r'(?m)^\s*Article\s*\(?'+re.escape(article)+r'\)?\s*\n'
 hits=list(re.finditer(pat,txt))
 if not hits:raise ValueError((path,article))
 hit=hits[-1]; after=txt[hit.end():]
 nxt=re.search(r'(?m)^\s*Article\s*\(?[IVX\d]',after)
 return after[:nxt.start() if nxt else len(after)].strip(),txt[:hit.start()].count('\f')+1
supp=[]
def add(rid,title,parent,article,path,uses,conditions):
 base=rows[parent]
 q,page=clause(path,article)
 raw=SOURCES/path.replace('.txt','.pdf')
 r={k:base[k] for k in ['act','official_url','source_language','raw_path','raw_sha256']}
 r.update(id=rid,rule=title,article=article,pdf_page=page,quote=q,conditions=conditions,
 read_on='2026-11-03',read_scope='Cached complete clause re-read to close a specific omitted-condition ledger gap. Earlier full-law acceptance preserved.',
 inherited_from='supplement to '+parent,status='writer documentation supplement; fresh independent review pending',effective_status='operative reference or conditional illustration',placements=[])
 if raw.exists():r.update(raw_path=str(raw.relative_to(ROOT.parent)) if False else '../sources/'+str(raw.relative_to(SOURCES)),raw_sha256=sha(raw))
 for g,ns in uses.items():r['placements'] += [location(g,n) for n in ns]
 rows[rid]=r;supp.append(rid)
add('SPL127','Maternity covered categories and exclusions','SPL128','127','spf-law-retry.txt',{'om-payroll-social':[30,44,60,62,74,76]},'All Omanis working in Oman, all contract types including temporary/training/retired; exclude self-employed, part-time, GCC-working and overseas Omanis; non-Omani categories require Board decision. No universal employer charge follows from this law clause alone.')
add('SPL-DVI','Original decree timing and issue date','SPL128','VI','spf-law-retry.txt',{'om-payroll-social':[20,26,27,28,29,30,36]},'General start 1 January 2024; maternity one year after 19 July 2023. Original VI(2),(3),(5) expressly superseded by RD60/2025, never applied as current text. FAQ historical maternity/sick dates remain unreconciled.')
for art,title,use in [('159bis 4','SME standard-regime following-year start',[82]),('159bis 5','SME permitted excess and additional-activity continuation',[82]),('159bis 6','Chairman modification power subject to Cabinet approval',[82]),('159bis 9','Small-enterprise supporting books and records',[40]),('159bis 18','Small-enterprise return three months and exemption evidence',[49]),('72','No loss carryforward from exempt activity',[40]),('126','Related-party non-arm-length arrangement adjustment',[40]),('132','Related parties and control power',[40]),('133','Corporate and relative control definitions',[40])]:
 add('ITL-'+art.replace(' ','-'),title,'C17',art,'prior-writer/itlaw.txt',{'om-corporate-income-tax':use},'Read the full quoted clause together with the parent source row; eligibility/excess decision remains held and the arithmetic comparison is not a claim of automatic regime switching.')
for art,title,ns in [('20','Recipient reverse-charge scope',[64,77,116,118,149,151]),('23','General services place of supply',[64,77,116,118,149,151]),('24','Special services place-of-supply exceptions',[49,64,77,116,118,149,151])]:
 add('VAT-'+art,title,'V041',art,'prior-writer/vat.txt',{'oman-vat':ns},'Oman taxable recipient and Oman place of supply required. Art24 overrides general rule: transport starts; immovable property location; non-taxable transport rental disposal; telecom/e-services actual use/benefit; listed restaurant/hotel/cultural/etc services actual performance. Bank supplier pattern is triage only, not proof.')
# Complete authority quote scopes from already-cached sections. These do not establish live portal access.
def segment(path,lo,hi):
 txt=(SOURCES/path).read_text(); ls=txt.splitlines()
 return '\n'.join(ls[lo-1:hi]).strip(),txt[:sum(len(x)+1 for x in ls[:lo-1])].count('\f')+1
QUOTE_RANGES={
'A01':('prior-writer/faq.txt',[(2272,2272)],'Income Tax FAQs, question 1'),
'A02':('prior-writer/faq.txt',[(2295,2296)],'Income Tax FAQs, question 2'),
'A03':('prior-writer/faq.txt',[(2371,2372)],'Income Tax FAQs, question 5'),
'A04':('prior-writer/faq.txt',[(2295,2296),(2394,2394),(2417,2417),(2439,2439),(2460,2460)],'Income Tax FAQs, questions 2, 6, 7, 8, 9'),
'A05':('prior-writer/faq.txt',[(2605,2617)],'Income Tax FAQs, question 15'),
'G01':('ed454949c42c.txt',[(1,1000)],'Threshold decision, articles One and Two'),
'G02':('d093475a3da6.txt',[(439,469)],'Real Estate guide, sections 5.2 and 5.3'),
'G03':('6d32d9466d04.txt',[(284,333)],'Health Care guide, section 3.1'),
'G04':('00e2a9830c8f.txt',[(450,500),(1251,1270)],'Financial Services guide, sections 4.1, 4.2 and life-insurance passage'),
'G05':('dc6c07a154ab.txt',[(582,853)],'Input Tax guide, sections 2.7 to 2.11'),
'G06':('dc6c07a154ab.txt',[(983,1061)],'Input Tax guide, section 2.13'),
'G07':('dc6c07a154ab.txt',[(854,894),(1062,1155)],'Input Tax guide, sections 2.12 and 2.14 through annual-adjustment requirement'),
'G08':('debd4cf3d454.txt',[(491,529)],'Return Filing guide, sections 3.3 and 3.4'),
'G09':('debd4cf3d454.txt',[(530,584)],'Return Filing guide, sections 3.5 and 4'),
'G10':('4d7308dc95f1.txt',[(1,1000)],'VAT for Free Zones, complete two-page note')}
for rid,(path,ranges,loc) in QUOTE_RANGES.items():
 r=rows[rid];r['historical_short_quote']=r['quote'];r['quote_fragments']=[]
 for lo,hi in ranges:
  q,page=segment(path,lo,hi)
  r['quote_fragments'].append({'quote':q,'text_cache':'../sources/'+path,'text_lines':[lo,min(hi,len((SOURCES/path).read_text().splitlines()))],'pdf_page':page if path.endswith('.txt') and not 'faq' in path else None})
 r['quote']='\n\n'.join(x['quote'] for x in r['quote_fragments'])
 r['act']='Tax Authority official English guidance; not itself a statutory instrument' if rid!='G01' else 'Tax Authority registration-threshold decision'
 r['article']=loc;r['excerpt_checked_on']='2026-11-03';r['quote_scope']='Complete relevant cached answer/section excerpts listed with extraction-line locators. No whole-guide/current-amendment assertion.'
# New authority rows absent from original canonical inventory.
def guidance(rid,title,path,url,article,quotes,uses,conditions,act='Tax Authority official English guidance'):
 raw=SOURCES/path
 r={'id':rid,'rule':title,'act':act,'article':article,'official_url':url,'source_language':'English official-hosted guidance, quoted as published; not an Arabic-original transcription','raw_path':'../sources/'+path,'raw_sha256':sha(raw),'read_on':'2026-11-03','read_scope':'Specific omitted operative-use quote read from existing cache only; earlier source acceptance preserved.','quote':quotes,'conditions':conditions,'placements':[],'status':'writer checked, independent review pending','inherited_from':'new documentation supplement','effective_status':'operative published-source statement; conditional on stated scope'}
 for g,ns in uses.items():r['placements'] += [location(g,n) for n in ns]
 rows[rid]=r;supp.append(rid)
faq='https://tms.taxoman.gov.om/portal/web/taxportal/personal-income-tax-faqs'
pfaq=(SOURCES/'b381bc93de5b-clean.txt').read_text()
def faqquote(text,num):
 m=re.search(r'(?m)^'+str(num)+r'\. ',text); after=text[m.start():]
 return after.split('Is this information helpful?')[0].strip()
for num,ns in [(2,[42]),(3,[42]),(7,[40]),(17,[42]),(18,[42]),(19,[42]),(20,[66])]:
 guidance('PFAQ-'+str(num),'PIT FAQ '+str(num),'b381bc93de5b.html',faq,'Question '+str(num),faqquote(pfaq,num),{'om-income-tax':ns},'Future PIT regime only, from 2028. FAQ20 does not repeal legacy withholding in 2026.')
form=rows['G08'];q,page=segment('debd4cf3d454.txt',316,490)
guidance('G11','VAT filing screens and published return boxes','debd4cf3d454.pdf',form['official_url'],'Return Filing guide section 3.2, physical PDF pp8 to13',q,{'oman-vat':[64,84,*range(88,101),102,110,169]},'June2021 published form only; not authenticated live portal. GCC boxes expressly not activated, current GCC treatment held. Refund checklist contents not recovered. Box mappings attach to every current printed table row.')
q=(SOURCES/'c76a33b92c4f-clean.txt').read_text();q=q[q.index('The conference witnessed'):q.index('The conference highlighted')].strip()
guidance('NEWS-RAFID','Announced Rafid launch and first electronic tax invoice','c76a33b92c4f.html','https://tms.taxoman.gov.om/portal/web/taxportal/-/tax-conference-2026-highlights-the-latest-developments-and-changes-in-the-tax-system','Tax Conference announcement, 21 September2026',q,{'oman-vat':[112],'om-tax-overview':[58]},'Announcement fact only. No operative phase dates from this news.')
# Keep N02 wholly on e-invoicing guidance; it is not the source for the separate Rafid announcement.
r=rows['N02'];txt=(SOURCES/'d5c8786e2026-clean.txt').read_text()
r['quote']=txt[txt.index('Implementation Phases & Timeline'):txt.index('How the System Works')].strip()+'\n\n'+txt[txt.index('Obligations'):txt.index('Back to Homepage')].strip()
r.update(act='Tax Authority e-invoicing guidance',article='Implementation Phases & Timeline; Obligations',quote_scope='Exact complete relevant sections',excerpt_checked_on='2026-11-03')
# The FAQ has independent commencement dates: cite its actual cached answer without adopting those dates as law.
from html.parser import HTMLParser
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,d):self.parts.append(d)
x=Text();x.feed((SOURCES/'spf-faq.html').read_text());st=' '.join(' '.join(x.parts).split())
start=st.find('What are the contribution rates')
# Preserve a short source excerpt located by the actual rate answer, not navigation.
ratepos=st.find('11%',start)
if ratepos<0:ratepos=st.find('11 %',start)
if ratepos<0:raise ValueError('SPF FAQ rate answer not located')
guidance('SPF-FAQ','Fund published rates and unresolved historical dates','spf-faq.html','https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/','Contribution-rate answer in Fund FAQ HTML',st[max(start,ratepos-700):ratepos+1700],{'om-payroll-social':[26,27,28,29,30,31],'om-tax-overview':[35]},'Published FAQ only. RD60/2025 statutory sick commencement and original decree maternity anniversary conflict with FAQ historical dates; neither implementation date is newly treated as settled.')
# Visual quote completion is separate from inherited source-read dates.
from arabic_quote_supplements import QUOTES
for rid,quotes in QUOTES.items():
 r=rows[rid];r['historical_short_quote']=r['quote'];r['quote_fragments']=quotes;r['quote']='\n\n'.join(quotes)
 r['excerpt_checked_on']='2026-11-03';r['quote_scope']='Exact selected Arabic original clauses transcribed visually from cached source-page renders; no invented English-to-Arabic translation. Full law was previously visually read; independent every-row verification pending.'
 if rid.startswith('P'):
  pages=[int(x) for x in re.findall(r'\d+',str(r['gazette_page']))]
  r['visual_locator']='Gazette1602 printed page(s) '+str(r['gazette_page'])+'; cached rendered/pit-NN.png has NN=printed page minus6'
 else:r['visual_locator']='Gazette1604 printed p9; rendered/spf-2025-amendment.png'
# English translation provenance must be labelled honestly.
for rid,r in rows.items():
 if rid.startswith('F'):
  r['source_language']='English FSA-hosted unofficial translation; PDF expressly states Arabic prevails'
 r.setdefault('source_language','English authority-hosted translation; no Arabic-original transcription asserted')
 r.setdefault('act','Tax Authority official publication, source URL below')
 r.setdefault('article',r.get('conditions','Source passage identified in read scope'))

# Close omitted contextual/authority references without broad inherited placements.
ft=(SOURCES/'prior-writer/faq.txt').read_text().splitlines()
for prefix in ['Dues can be paid','The principal officer can add']:
 line=next(l.strip() for l in ft if l.strip().startswith(prefix))
 rows['A04']['quote']+='\n\n'+line
rows['A04']['quote_fragments']=[x for x in rows['A04']['quote_fragments'] if x['quote'].strip()]
rows['ITL-159bis-18']['rule']='Small-enterprise three-month return deadline'
rows['ITL-159bis-18']['conditions']='Electronic return under159bis17; within three months after year end; signed under134(4). Exempt-filing proof comes separately from FAQ2.'
# Actual law supplies/imports scope is used in overview, not all VAT-law rows by inheritance.
add('VAT-12','VAT taxable supplies and imports scope','V041','12','prior-writer/vat.txt',{'oman-vat':[20],'om-tax-overview':[39]},'Taxable supply by taxable person in Oman, deemed supplies and imports; exemptions/zero rates/place-of-supply rules apply.')
add('ITL-120','Tax treaty double-tax relief framework','C16','120','prior-writer/itlaw.txt',{'om-corporate-income-tax':[63]},'Treaty relief depends on actual agreement and its operative status; news signature is not entry into force.')
# Paragraph-specific source quotes for the signed-treaty announcements.
q='\n\n'.join(segment('10fb767c66ff.txt',a,b)[0] for a,b in [(2346,2353),(2489,2496)])
guidance('NEWS-DTA','Austria and Angola signature announcements','10fb767c66ff.html','https://tms.taxoman.gov.om/portal/news','News list entries29January2026 and21September2026',q,{'om-tax-overview':[58]},'Signature announcement only; no treaty benefits or entry into force inferred. Actual treaties not checked.')
rows['N01']['quote']=(SOURCES/'54a254c0906e-clean.txt').read_text().split('Excise Tax:')[-1].split('Back to Homepage')[0].strip()
rows['N01'].update(act='Tax Authority tax-rate webpage',article='Excise Tax table, last updated29October2025',effective_status='nonoperative currentness hold; historical source statement only')
rows['N03']['quote']=(SOURCES/'6b45665e2c87-clean.txt').read_text().split('The Tax Authority, has issued')[1].split('These decisions align')[0]
rows['N03']['quote']='The Tax Authority, has issued'+rows['N03']['quote']
rows['N03'].update(act='Tax Authority announcement28September2026',article='Three new administrative decisions announcement; annexes not recovered',effective_status='nonoperative annex/currentness hold; announcement only')
# The short record must never misrepresent the category-coverage-only passages as a universal live charge.
for rid,r in rows.items():
 for p in r['placements']:
  g=p['guide']; n=p['line_start'];sec=p['section']
  scope='Known core rule within the source/read scope; apply all quoted conditions.'
  if rid.startswith('P') and not rid.startswith('SPF'):
   scope='2028 statutory regime only; for2026 only the commencement distinction applies. No implementation/form availability conclusion.'
  if rid in ['C22','ITL-159bis-4','ITL-159bis-5','ITL-159bis-6']:
   scope='Conditional SME rule; eligibility thresholds and permitted-excess implementing decision held. No automatic current qualification.'
  if g=='om-payroll-social' and n in [60,62]:scope='Conditional statutory arithmetic illustration: ordinary covered Omani worker, all five branches assumed applicable; not a universal2026 payroll rate.'
  if g=='om-payroll-social' and n in [74,76]:scope='NONOPERATIVE live2026 above-ceiling computation; preserved assumed3000 statutory illustration only. Current ceiling/implementation must be closed.'
  if g=='om-tax-overview' and n==35:scope='Conditional five-branch totals only; sibling payroll commencement/current-ceiling holds apply.'
  if rid in ['S01','S02','S03','SPL-DVI']:scope='Statutory timing/source history only. Original VI(2),(3),(5) superseded; current category/start decisions and conflicting FAQ history remain held as specified.'
  if rid in ['N01','N03']:scope=r['effective_status']
  if rid in ['N02','NEWS-RAFID','NEWS-DTA']:scope='Published authority guidance/announcement fact only; no phase commencement or treaty-in-force instruction.'
  if rid=='SPF-FAQ':scope='Published rates table; conflicting historical dates not adopted as settled law.'
  if rid=='G11':scope='Published June2021 form illustration only, not authenticated current portal; GCC boxes not activated in that source.'
  if rid in ['G08','G09'] and g=='om-company-formation':scope='Sibling-Guide annual-checklist referral only; no formation-specific VAT rule or procedure inferred.'
  if sec=='Two worked examples that recompute' and scope.startswith('Known'):
   scope='Illustrative inputs, not statutory thresholds. Operative rate/base/evidence conditions apply; arithmetic retained from accepted13oa-check blocks.'
  p.setdefault('use_scope',scope)

# Source-preparation rows that are present solely in held/source sections get explicit exact held destinations.
for rid,g,needle in [('C21','om-corporate-income-tax','Not yet confirmed:'),('C-ART48','om-tax-overview','Not yet confirmed:'),('C-ART49','om-tax-overview','Not yet confirmed:'),('C-ART51','om-tax-overview','Not yet confirmed:')]:
 n=next(i+1 for i,l in enumerate(texts[g]) if l.startswith(needle))
 rows[rid]['placements'].append({**location(g,n),'use_scope':'held historical/source explanation only; not a live filing instruction'})
 rows[rid]['effective_status']='nonoperative held topic only'
# Every effective source hash is verified against actual cached bytes without changing acquisition provenance.
checks=[]
for r in rows.values():
 p=ROOT/r['raw_path']; ok=p.exists() and sha(p)==r['raw_sha256']
 r['cache_hash_verified_on']='2026-11-03';r['cache_hash_matches']=ok
 if not ok:checks.append(r['id'])
 r['acquisition_provenance']='Existing normal-TLS cache/manifest; no new fetch. Prior-writer originals lack independently attested original fetch timestamp. Read date is not a fetch date.'
assert not checks,checks
save('effective-source-ledger.json',list(rows.values()))
save('guide-manifest.json',[{'guide':g,'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size,'head_at_start':'79e6ff19b14fd2a62c1c402879103291ad7883d0'} for g,p in guides.items()])
save('supplement-ids.json',supp)
# No source pages or full raw blobs are copied into this folder.
print('Built',len(rows),'source records;',sum(len(r['placements']) for r in rows.values()),'exact source-use placements;',len(supp),'supplements')
# Exact predecessor-block destinations. Each initial-PR block has its own current span.
# Tables are mapped to their actual current table, never merely a section heading.
INITIAL={
'om-company-formation':[(20,20),(26,33),(39,39),(45,50),(52,52),(56,56),(60,60),(64,64),(66,75),(77,77),(79,88),(92,96),('sources','table'),('holds','holds')],
'om-corporate-income-tax':[(20,20),(26,36),(40,40),(46,53),(55,55),(59,59),(63,63),(67,67),(69,80),(82,82),(84,96),(100,105),('sources','table'),('holds','holds')],
'om-income-tax':[(20,20),(26,32),(36,36),(38,38),(40,40),(42,42),(48,56),(58,58),(62,62),(66,66),(70,70),(72,82),(84,84),(86,99),(103,108),('sources','table'),('holds','holds')],
'om-payroll-social':[(20,20),(26,31),(35,38),(40,40),(44,44),(48,48),(52,52),(56,56),(60,60),(62,72),(74,74),(76,88),(92,96),('sources','table'),('holds','holds')],
'om-tax-overview':[(20,20),(26,35),(39,39),(45,50),(54,54),(58,58),(62,62),(64,72),(74,74),(76,86),(90,94),('sources','table'),('holds','holds')],
'oman-vat':[(20,20),(22,22),(24,29),(33,33),(39,50),(52,52),(56,56),(58,58),(60,60),(62,62),(64,64),(66,66),(70,78),(82,82),(84,84),(88,100),(102,102),(106,106),(110,110),(112,112),(116,116),(118,132),(134,134),(136,147),(169,169),(173,178),('sources','table'),('holds','holds')]}
# Base VAT block IDs are immutable. This precise map distinguishes repaired, held and consolidated topics.
VAT_BASE={
1:[39],2:[39,40,41,42,48,49,50,52,82],3:[22],4:[24,26,27,28,29],5:[31],6:[31,58],7:[31,169],8:[33],
9:[66,70],10:[70],11:[66,72,73,74,75],12:[72,73,74,75],13:[66,76],14:[76],15:[66,77],16:[77],17:[66,78],18:[78],
19:[149,151],20:[64,149,151],21:[149,151],22:[149,151],23:[149,151],24:[60,149,151],
25:[39],26:[48,49,50,52],27:[50,52],28:['holds',110],29:[88,89,90,91,92,93,94,95,96,97,98],30:[88,89,90,91,92,93,94,95,96,97,98],
31:[99],32:[99],33:[100,169],34:[100,169],35:[64,94],36:[56,110],37:[56,64,110],38:[60,'holds'],39:[62],
40:[82],41:[82],42:[106],43:[106,'holds'],44:[64,149,151],45:[49,169],46:[60,149,151],47:['holds',110],48:[52],49:[52],50:[33,110],51:[169],
52:[169],53:[169],54:[116,118],55:[169],56:[169],57:[33],58:['holds'],59:[169,'holds'],60:['cta'],61:['cta']}
BASE_BULLETS={
'om-company-formation': [[27,37],[26,37,60],[32,33,39,60],['holds'],['holds'],[27,37],[45,'holds'],['holds'],['holds'],[52],[31,37]],
'om-corporate-income-tax':[[20,26,27,30],[26],[27,28,29,'holds'],[30],[40,'holds'],[31,63],[31,63],[31,63],[31,63],[52],[48,49,51],['holds']],
'om-income-tax':[[20,26,103],[28],[27,28,38],[20,28],[20],[38],[38],['holds'],['holds'],['holds']],
'om-payroll-social':[[20,38],[20],[26],[26],[27,56],[28],[28],[31,60,62,'holds'],[56,'holds'],[35,40,44],[48]],
'om-tax-overview':[['holds'],[20],[20],[26],[26],[27],[31,'holds'],[39,'holds'],[45,46],[48],[33,34,'holds']]}
def symline(g,tag):
 ls=texts[g]
 if tag=='holds':return next(i+1 for i,l in enumerate(ls) if l.startswith('Not yet confirmed:'))
 if tag=='cta':return next(i+1 for i,l in enumerate(ls) if l=='<!-- openaccountants-cta-block -->')
 raise ValueError(tag)
def span(g,a,b):
 if a=='sources':
  start=next(i+1 for i,l in enumerate(texts[g]) if l.startswith('| Source |'))
  end=start
  while end<len(texts[g]) and texts[g][end].startswith('|'):end+=1
  a,b=start,end
 elif a=='holds':a=b=symline(g,a)
 elif a=='cta':
  a=symline(g,'cta');b=len(texts[g])
 out=location(g,a);out['line_end']=b;out['text']='\n'.join(texts[g][a-1:b]);return out
def destinations(g,ns):
 return [span(g,n,n) if isinstance(n,int) else span(g,n,n) for n in ns]
topics=[]
for original in json.loads((OLD/'topic-destinations.json').read_text()):
 r={**original};g=r['guide'];seq=int(r['id'].rsplit(':',1)[1]);r['historical_destination']=r.pop('destination');r['historical_writer_semantic_review']=r.pop('writer_semantic_review')
 if r['predecessor']=='initial-pr':
  a,b=INITIAL[g][seq-1];r['effective_destinations']=[span(g,a,b)]
  r['semantic_change']='Retained at the exact current block below; source host/read scope updated where appropriate. Compare the preserved original and current text, including all stated conditions.'
 elif g=='oman-vat':
  ns=VAT_BASE[seq];r['effective_destinations']=destinations(g,ns)
  r['semantic_change']='Consolidated into the exact listed current paragraph/table/example. Corrected legal classifications and holds are stated explicitly below; original input is preserved in the immutable snapshot.'
 elif (g=='om-company-formation' and seq==1) or (g=='om-income-tax' and seq==1):
  ns=[20,27,32,33,39] if g=='om-company-formation' else [20,26,27,28,103]
  r['effective_destinations']=destinations(g,ns)
  r['semantic_change']='Old broad introductory assertion narrowed to current-year scope; foreign ownership held, and personal-tax nil is not a claim of no legacy business/nonresident-service income tax.'
 else:
  bullets=[l for l in r['original_body_unit'].splitlines() if l.startswith('- **')]
  assert len(bullets)==len(BASE_BULLETS[g]),(g,len(bullets))
  r['atomic_destinations']=[{'original_topic':l,'destinations':destinations(g,ns)} for l,ns in zip(bullets,BASE_BULLETS[g])]
  unique=[]
  for ns in BASE_BULLETS[g]:
   for n in ns:
    if n not in unique:unique.append(n)
  r['effective_destinations']=destinations(g,unique)
  r['semantic_change']='Each original bullet has its own exact destination. Repeated withholding bullets consolidate at the same rule; no repeated source row is counted as new country coverage.'
 r['review_state']='Writer reconciliation for fresh independent semantic review; not independent acceptance'
 topics.append(r)
# Specific corrections, loss/hold dispositions and preserved example assumptions, keyed by immutable topic.
NOTES={
'oman-vat:actual-base:002':'Quick table split into rates and deadlines. Healthcare/education repaired from zero to exempt; first residential supply repaired to5%; nonresident threshold removed; refund and portal controls conditional.',
'oman-vat:actual-base:005':'Bank-only minimum retained for triage; bank statement alone cannot establish VAT class/input entitlement.',
'oman-vat:actual-base:006':'OMR20 evidence cutoff explicitly NONOPERATIVE at current31. Valid evidence required at58.',
'oman-vat:actual-base:010':'All bank aliases preserved at70; fees no longer blanket exempt. Margin/fee distinction at52 and70.',
'oman-vat:actual-base:012':'Every government pattern preserved at72–75, including customs import check and old PASI alias.',
'oman-vat:actual-base:016':'All named SaaS suppliers preserved at77; foreign services receive RC only after recipient/place-of-supply/invoice checks. Supplier name alone proves nothing.',
'oman-vat:actual-base:019':'USD14.99/OMR5.77 retained at149. Date03.01.2026 and literal bank-row punctuation remain in immutable snapshot rather than current prose; not a tax eligibility condition.',
'oman-vat:actual-base:021':'OMR2000 net sale retained. Original10.01.2026/Invoice001 bank tokens preserved in snapshot; current149 explicitly assumes net taxable sale rather than inferring it from receipt.',
'oman-vat:actual-base:023':'OMR8000 sedan and private-use assumption retained at149. Original20.01.2026/TOYOTA bank tokens preserved in snapshot. Old<9-seat rule corrected to not-more-than10 including driver at60.',
'oman-vat:actual-base:024':'Private sedan input still blocked; passenger test corrected to <=10 including driver; mixed private/business only private portion blocked.',
'oman-vat:actual-base:026':'Exports/transport retained with statutory regulatory conditions; healthcare/education corrected to exempt; first residential supply corrected to5%, resale exempt. No original incorrect zero instruction survives as operative.',
'oman-vat:actual-base:028':'Qatar/Kuwait non-implementing-state conclusion held explicitly; GCC boxes retain published not-activated condition. No inference from Bahrain.',
'oman-vat:actual-base:030':'Old1–9 output-box numbering replaced by published1a–5b. Each old function maps to current supplies/RC/import/export/adjustment rows; current layout is explicitly dated2021.',
'oman-vat:actual-base:032':'Old10–15 input-box numbering replaced by published6a–6d; imports and fixed assets remain. Published form conditional on live-form check.',
'oman-vat:actual-base:034':'Old16–18 net numbering replaced by7a–7c; credit-brought-forward reconciliation expressly retained at31 and169.',
'oman-vat:actual-base:038':'Passenger threshold and exception scope corrected from law guide; clubs unresolved and expressly held. Personal portion/entertainment/catering and resale conditions retained at60.',
'oman-vat:actual-base:039':'Turnover method retained only for residual input after direct attribution and excluded supplies; annual adjustment added. Old universal approval assertion replaced by published standard method.',
'oman-vat:actual-base:041':'Last-day-of-next-month shortcut repaired to30days after period end; quarter and first-part-period conditions at82.',
'oman-vat:actual-base:043':'Old25/day(max2500) and5000 registration fine held, not substituted as law. Law100/101 intentional offence ranges operative and quoted.',
'oman-vat:actual-base:047':'Old Qatar zero-rating instruction held. No country-specific export conclusion is operative.',
'oman-vat:actual-base:048':'Licensed healthcare corrected from0% to exemption at52; licence condition retained.',
'oman-vat:actual-base:049':'First residential sale corrected to5%; old3-year zero window withdrawn as unsupported. Resale exemption retained with related-input block.',
'oman-vat:actual-base:050':'Authorisation and VAT registration required; four named zones remain. R-OM-2 referral persists rather than automatic zero rating.',
'oman-vat:actual-base:051':'Credit-note adjustment preserved conditionally under art40; no unconditional rule inferred from bank record.',
'oman-vat:actual-base:057':'Escalation policy remains at33. Literal legacy REVIEWER FLAG / ESCALATION REQUIRED template is preserved in snapshot only; not an operative legal rule.',
'oman-vat:actual-base:058':'Direct taxes/contributions explicitly out of scope and linked to overview. PASI11.5/7 replaced by current conditional8/14.5, not carried forward as fact. Alcohol/pork excise held.',
'oman-vat:actual-base:059':'5/0/exempt and blocked-input/credit controls retained at169. Qatar/Kuwait assumption held rather than silently retained.',
'om-corporate-income-tax:initial-pr:003':'Cash-basis citation repaired to159bis10, books159bis9; all original loss/depreciation/exemption/accounting-period subjects retained at40.',
'om-corporate-income-tax:initial-pr:007':'No-PE withholding scope expanded to include payments not attributable to existing PE (art40); exclusions, credit deadline and dividend/interest hold preserved.',
'om-corporate-income-tax:initial-pr:010':'OMR40000 comparison and4800 difference retained; automatic every-threshold-switch claim corrected for following-year/continuation provisions159bis4/5.',
'om-income-tax:initial-pr:004':'Main-home two-year period runs from notification; resident ownership/location and once-in-life second-home choice added. New-resident18-month period starts day after nonresident status ends; family/regulatory relief conditions retained.',
'om-income-tax:initial-pr:013':'80000/20000/1300/900 amounts preserved. Annual threshold then costs distinguished from gross-basis advance withholding; eligibility and3-year election stated.',
'om-income-tax:initial-pr:015':'Nil-before2028 answer narrowed to new PIT; registered-business and legacy nonresident-service withholding separately tested.',
'om-payroll-social:initial-pr:002':'Rates retained; sick statutory timing and maternity anniversary versus FAQ dates explicitly held.8/14.5 totals conditional on all five branches.',
'om-payroll-social:initial-pr:003':'Starting3000 ceiling no longer asserted as live2026 without annual decision;9% savings commencement requires Board decision within amended4years.',
'om-payroll-social:initial-pr:008':'Non-Omani injury date corrected to19July2028 under RD60 amendment; categories/start decisions remain required.',
'om-payroll-social:initial-pr:009':'1000/145/80 arithmetic preserved as ordinary covered Omani employee, all five branches applying.',
'om-payroll-social:initial-pr:011':'4000/3000/460/245 example preserved as statutory illustration explicitly NONOPERATIVE for live2026 until ceiling/commencement closed.',
'oman-vat:initial-pr:001':'First-supply automatic nonresident registration replaced by art57 date liable to VAT; all-zero exemption by application retained.',
'oman-vat:initial-pr:009':'Blocked categories retained with employee500 evidence/business-use limit, catering exceptions, rental/emergency and private-use portion conditions.',
'oman-vat:initial-pr:010':'Residual-only attribution, exclusions,3-decimal rounding and annual true-up added; not a blanket turnover deduction.',
}
for r in topics:
 if r['id'] in NOTES:r['semantic_change']=NOTES[r['id']]
save('effective-topic-destinations.json',topics)
# Every inherited topic and source row is preserved and has a traceable current disposition.
assert len(topics)==169
assert len(set(r['id'] for r in topics))==169
assert len(set(rows))==len(rows)
# Writer classifications are explicit. These are not independently accepted coverage counts.
used=[r for r in rows.values() if r['placements']]
prep=[r for r in rows.values() if not r['placements']]
save('source-preparation-only.json',[{'id':r['id'],'rule':r['rule'],'reason':'No present operative use located; preserve completed source work without inflating the current Guide ledger.'} for r in prep])
# Validate exact ranges and attached bytes, which also catches accidental line drift.
errors=[]
for r in used:
 for p in r['placements']:
  ls=texts[p['guide']]
  if p['text']!='\n'.join(ls[p['line_start']-1:p['line_end']]):errors.append(r['id']+':placement-byte-drift')
  if not p['text'].strip():errors.append(r['id']+':blank-placement')
  if p['text'].startswith(('  ','inputs:','steps:','expected:')):errors.append(r['id']+':formatting-not-claim')
for r in topics:
 snapshot=ROOT/r['snapshot']
 if sha(snapshot)!=r['snapshot_sha256']:errors.append(r['id']+':snapshot-hash')
 if r['original_body_unit'] not in snapshot.read_text():errors.append(r['id']+':missing-original')
 for p in r['effective_destinations']:
  if not p['text'].strip():errors.append(r['id']+':blank-destination')
# Exact current held topics, with source that is actually missing rather than available unread law.
HOLDS={
'om-company-formation':[
('Foreign investment and restrictions',[32,33,39,45,60],'Official complete FCIL and current ministerial restriction instruments not recovered; private-source predecessor summary remains nonoperative.'),
('Incorporation portal, fees, timing, annualCR renewal',[52,'holds'],'Authenticated current register/procedure instrument unavailable; old steps/timeline and150000capital practice explicitly held.'),
('One-person procedures and specific auditor application',['holds'],'Core291–297/278 law is available and operative above. Missing procedural Regulations and case-specific application alone remain held.')],
'om-tax-overview':[
('Current excise instruments',[32,'holds'],'2025authority rate-page headline is historical, not2026instrument closure.'),
('Top-up amended current application',[33,34,'holds'],'RD101/2026 full amendment unavailable in original cache; decree-only private translation does not close operative law. Do not compute15%/750m/2of4 as current instructions.'),
('Treaties/e-invoicing implementation',[58,'holds'],'Signed-news entries are not in-force treaty instruments; future phase commencement dates not established.'),
('Held predecessor/history topics',['holds'],'VAT16April2021decisive commencement not recovered; worldwide corporate basis not closed. AvailableITL1(20)/48–51period facts remain in inherited held paragraph and their known source rows are preserved, not claimed newly completed.')],
'om-income-tax':[
('PIT implementation and legacy separate questions',[58,'holds'],'Executive Regulations/current return forms, employer remittance dates and detailed controls not recovered. Does not hold availablecorePIT law;2028statutory rules are ledgered above.'),
('Pre2028 investment gains/nonresident legacy pay',['holds'],'Separate decisive pre2028instruments not checked; newPITcommencement does not determine every legacy liability.')],
'om-corporate-income-tax':[
('SME qualification and permitted excess',[28,82,'holds'],'FAQhigherthresholds versus originalstatutorythresholds; implementingexcess/modificationdecision not recovered. Known159bis4–6clauses quoted; availableclauses not treated as missing.'),
('Dividend/interest withholding',[31,63,'holds'],'Suspension instruments/currentness unclosed;10%covered-service core does not settle these categories.'),
('Later amendments, worldwide basis/provisional return',['holds'],'PostRD118/2020closure and precise preexisting worldwide/provisional rules not established; originalSMEregistrationassertion also unsupported and held.'),
('Four-month statutory locator/audit',['holds'],'EnglishPDFphysicalgap around134remains; fourmonths backed by FAQ2. Tax-audit statutoryscope separate from auditedaccountsFAQguidance.')],
'om-payroll-social':[
('Current contribution ceiling',[35,74,76,'holds'],'AnnualBoardceilingdecision unavailable;3000is statutorystartingamount.4000example is nonoperativeforlive2026.'),
('Sick/maternity historical implementation dates',[29,30,'holds'],'FAQ1July2025sick/1July2024maternity conflict with statutory3year/1yearanniversaryafter19July2023. Rates do not settleimplementation. Preserveconflict withoutchoosingone.'),
('Non-Omani categories/savingsstart',[36,56,'holds'],'Boardcategory/startdecisions not recovered;9%basicrate and4yearouterlimit do not prove currentstart. Injuryamended5yearterm known.'),
('Fund screens/GCCnationalrates',[48,'holds'],'Portalrejectedconnections; noauthenticatedstepsorcountry-specificGCCrates.')],
'oman-vat':[
('September annexes',[45,46,47,'holds'],'News28Septnotoperativeannexes; no productclassificationfromannouncement.'),
('GCC transition/current form',[91,93,102,110,'holds'],'June2021publishedformnotactivatedboxes; Qatar/Kuwait/nonimplementingstatusandliveportalnotclosed.'),
('Regulations-specific gaps',['holds'],'Old25/daymax2500and5000fines, clubmembership, monthlyperiods and relevantamendedregulationarticlesnotclosed; do not inferfromcorelaw.'),
('Other implementation/outofscope',['holds'],'E-invoicephasecommencementandTaxpayerChecklistlayoutunrecovered; alcohol/porkexciseoutofscopeandheld.')]
}
holdrecords=[]
for g,items in HOLDS.items():
 for title,ns,why in items:holdrecords.append({'guide':g,'topic':title,'locations':destinations(g,ns),'reason':why,'status':'genuine nonoperative/currentness hold; no assertion of country completion'})
save('genuine-holds.json',holdrecords)
# Markdown tables are the per-Guide effective ledgers, with every source excerpt in a source appendix.
def esc(s):return str(s).replace('|','\\|').replace('\n','<br>')
counts=[]
for g in guides:
 rr=[r for r in rows.values() if any(p['guide']==g for p in r['placements'])]
 placements=[(r,p) for r in rr for p in r['placements'] if p['guide']==g]
 tt=[r for r in topics if r['guide']==g]
 body=[f'# {g}: effective writer ledger, 3 November 2026','',
 'Writer documentation for fresh independent every-row and semantic review. This does not replace the earlier independent MERGE review or assert a new independent PASS. Frozen INCOMPLETE receipts and original ledgers remain unchanged.',
 '',f'Guide SHA256: `{sha(guides[g])}`. {len(rr)} source records; {len(placements)} exact source-use placements; {len(tt)} immutable predecessor blocks. Counts are evidence inventories, not completeness scores.','',
 'All positions below refer to the unchanged current Guide. Full quotes, language, act/locator, official URL, cache SHA256 and actual read dates appear in the source appendix. Cached prior-writer acquisitions have no independently timestamp-attested original fetch; the read date is not a fetch date. No new network acquisition or raw source blob is included.','',
 '| Source ID | Rule | Exact current uses | Conditions and status |','|---|---|---|---|']
 for r in rr:
  pp=[p for p in r['placements'] if p['guide']==g]
  locs=', '.join(f"{p['line_start']}–{p['line_end']} ({p['section']})" for p in pp)
  body.append('| '+ ' | '.join(map(esc,[r['id'],r['rule'],locs,r['conditions']]))+' |')
 body+=['','## Exact use inventory','', '| Guide lines | Source IDs | Text / per-use scope |','|---|---|---|']
 byloc=collections.defaultdict(list)
 for r,p in placements:byloc[(p['line_start'],p['line_end'])].append((r,p))
 for (a,b),rp in sorted(byloc.items()):
  p=rp[0][1];scopes=list(dict.fromkeys(q['use_scope'] for _,q in rp))
  body.append('| '+ ' | '.join(map(esc,[f'{a}–{b}',', '.join(r['id'] for r,_ in rp),p['text']+'\nSCOPE: '+'; '.join(scopes)]))+' |')
 body+=['','## Source quotations and provenance','']
 for r in rr:
  body += [f"### {r['id']}: {r['rule']}",'',f"{r['act']}; {r['article']}; printed/PDF locator: {r.get('gazette_page',r.get('pdf_page',r.get('visual_locator','see section/text locator')))}.",f"Official source: {r['official_url']}",f"Language: {r['source_language']}. Source read: {r['read_on']}; excerpt check: {r.get('excerpt_checked_on',r.get('read_on'))}.",f"Cache: `{r['raw_path']}` SHA256 `{r['raw_sha256']}` (bytes rechecked 2026-11-03).",f"Read scope: {r['read_scope']}",'',*['> '+l if l else '>' for l in r['quote'].splitlines()],'',f"Conditions: {r['conditions']}",'']
 body+=['## Predecessor destinations','', '| Immutable predecessor block | Exact current lines | Disposition |','|---|---|---|']
 for t in tt:
  body.append('| '+' | '.join(map(esc,[t['id'],', '.join(str(p['line_start'])+'–'+str(p['line_end']) for p in t['effective_destinations']),t['semantic_change']]))+' |')
 body+=['','The JSON topic map preserves each original block verbatim, snapshot hash, current block bytes and per-bullet destinations for grouped base summaries. Literal historical bank tokens and escalation formatting that remain snapshot-only are disclosed there; this is not a certification that every old sentence was republished.','', '## Genuine holds','']
 for h in holdrecords:
  if h['guide']==g:body+=['- '+h['topic']+': '+h['reason']]
 (OUT/'ledgers'/f'{g}.md').write_text('\n'.join(l.rstrip() for l in body).rstrip()+'\n')
 counts.append({'guide':g,'source_records':len(rr),'source_use_placements':len(placements),'predecessor_blocks':len(tt),'guide_sha256':sha(guides[g]),'ledger':f'ledgers/{g}.md'})
save('per-guide-counts.json',counts)
save('mechanical-checks.json',{'errors':errors,'all_169_predecessor_blocks_preserved':len(topics)==169,'all_source_cache_hashes_match':all(r['cache_hash_matches'] for r in rows.values()),'source_records':len(rows),'inherited_source_records':142,'supplement_source_records':len(supp),'source_use_placements':sum(len(r['placements']) for r in rows.values()),'source_preparation_only_records':len(prep),'checks_are':'Writer mechanical integrity only. No independent legal/semantic PASS.'})
assert not errors,errors
print('Rendered six effective ledgers;169precise topic destinations;',len(prep),'source-preparation-only records. Mechanical errors:',len(errors))
