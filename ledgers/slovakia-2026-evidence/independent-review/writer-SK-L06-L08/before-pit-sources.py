from writer import *
# Exact retained scopes read during this writer pass on 28/29 October.
section('ITA2.residence',13,'2',1,72,[(15,32),(32,53),(64,67)])
section('ITA4.PIT',13,'4',1,33,[(4,14),(30,33)])
section('ITA5.pay',13,'5',1,30,[(4,16)])
section('ITA5.contributions',13,'5',245,249,[(245,249)])
for key,lo,hi in [('business',1,37),('no-rental-loss',50,58),('flat',77,107)]:section('ITA6.'+key,13,'6',lo,hi)
section('ITA7.capital',13,'7',1,69,[(4,10),(23,42),(66,69)])
section('ITA8.categories',13,'8',1,60,[(4,22),(54,60)])
for key,lo,hi in [('rental500',36,40),('shared500',48,57),('securities',62,67),('retail-bonds',115,121)]:section('ITA9.'+key,13,'9',lo,hi)
for key,lo,hi in [('base',3,5),('personal',6,17),('spouse',18,46),('spouse-conditions',47,64),('pensioner',65,76),('nonresident',77,81),('DDS-PEPP',82,109),('allocation',110,113)]:section('ITA11.'+key,13,'11',lo,hi)
section('ITA15.PIT',13,'15',1,45,[(6,37),(38,45)])
section('ITA30.loss',13,'30',1,16)
scope('ITA32.filing',13,'sources/13.txt',9760,9788,'§ 32(1)–(2)',[(9763,9769),(9771,9784)])
for key,lo,hi in [('child-age',3,18),('child-months',26,41),('child-cap',42,71),('child-parent',72,99),('child-taper',100,111)]:section('ITA33.'+key,13,'33',lo,hi)
for key,lo,hi in [('eligibility',3,37),('window',38,47),('order-payout',48,64),('death',65,74)]:section('ITA33a.'+key,13,'33a',lo,hi)
section('ITA34.advances',13,'34',1,34,[(4,18),(23,34)])
section('ITA38.settlement',13,'38',1,31,[(4,12),(21,31)],note='SK-L01 correction: annual settlement is unavailable when a §11(11) DDS increase is required; root applied the exact qualification in v1.7. Type A remains the income-only filing route.')
section('TC14.electronic',20,'14')
section('ITA43.PIT',13,'43',1,115,[(4,14),(23,28),(86,88),(100,104)],note='Only the displayed rate, ordinary bank/dividend and government-bond recipient clauses are adopted; no blanket individual bond withholding is inferred.')
section('ITA45.relief',13,'45',1,42,[(4,21),(28,42)])
section('ITA46.payment',13,'46',1,2)
section('ITA46a.minimum',13,'46a')
section('ITA47.rounding',13,'47')
scope('ITA51e.dividends',13,'sources/13.txt',12383,12425,'§ 51e(1)–(4)',[(12388,12396),(12408,12422)])
section('ITA51ea.bonds',13,'51ea')
scope('ITA52zi.dividends2017',13,'sources/13.txt',13645,13669,'§ 52zi(5)',[(13646,13657)])
section('ITA52zzz.transitions',13,'52zzz',1,29,[(6,11),(13,21)])
section('ITA52zzzb.dividends2025',13,'52zzzb',14,31,[(17,26)])
scope('ITA52zzzc.bonds',13,'sources/13.txt',14714,14731,'§ 52zzzc',[(14717,14720),(14726,14731)])
section('ITA52zzzj.2026',13,'52zzzj',1,5)
scope('ITA52zzzm.2027',14,'sources/14.txt',14823,14826,'§ 52zzzm (31 December 2026 version)')
section('ITA52zzy.mortgages',13,'52zzy',1,81,[(4,7),(73,81)],note='Subsections3–13 address the separate 2023 increased-instalment measure and are not adopted as a 2026 ordinary credit.')
scope('ITA33a.historical2023','v00','sources/v00.txt',33401,33580,'Historical § 33a, final2023 body, preserved by current §52zzy',[(33408,33431),(33444,33449),(33455,33496),(33504,33515),(33521,33580)])
scope('Minimum168.2025',2,'sources/02.txt',61,70,'Measure168/2025 and Ministry of Labour amount',[(63,67)])
scope('Wage2024',35,'sources/35.txt',2396,2402,'Official social situation report2024, section2.2.1',[(2396,2399)])
scope('FS.dividend-periods',49,'sources/49.txt',144,170,'Financial Administration official dividend profit-period table',[(158,166)])
# The one missing historical10% clause: actual official web answer. Raw HTML acquisition failed DNS/403,
# so preserve the web extraction and its line numbers without pretending it is an HTML raw body.
w=EVID/'shared/ITA-20240101-web-response.json';v=json.loads(w.read_text());reader=w.with_suffix('.reader.txt')
reader.write_text(v)
receipts['ITA2024web']={'file':str(w),'sha256':sha(w),'url':'https://static.slov-lex.sk/static/SK/ZZ/2003/595/20240101.html'}
# Lossless web response stays untouched. The following reader removes only tool line
# labels and hyperlink wrappers, retaining their original visible text and a coordinate map.
web_lines=[];web_map=[]
for original in v.split('\n'):
    match=re.match(r'^L(\d+): ?(.*)$',original)
    if match:
        visible=re.sub(r'【[^†】]+†(.*?)】',r'\1',match.group(2))
        web_lines.append(visible);web_map.append({'reader_LF':len(web_lines),'web_line':int(match.group(1))})
reader.write_text('\n'.join(web_lines)+'\n')
(EVID/'shared/ITA-20240101-web-line-map.json').write_text(json.dumps(web_map,indent=2)+'\n')
line=next(x['reader_LF'] for x in web_map if x['web_line']==8089)
scope('ITA15.dividend2024','ITA2024web',reader,line-2,line+4,'Historical §15(a)(5) and(6); official web line8089',[(line,line+4)],'Actual official web response retained; direct HTML HTTPS403 is preserved. Reader removes tool line labels/link wrappers only; web-line map retained. Used only for2024profit-period10% with current transition bridges, not its old business thresholds.')
# Actual Ministry PDF members. The URL identifies the official archive; member names/hashes identify the exact form.
forms=ARCH.parent/'sk-income-forms-completion/independent'
for sid,name,url in [('Aform','forms--DPFOAv25 v1.10_vzor','https://www.mfsr.sk/files/archiv/66/prispevok_16.zip'),('Bform','forms--DPFOBv26 v1.3_vzor','https://www.mfsr.sk/files/archiv/66/prispevok_16.zip'),('Ainstruction','instructions--Poučenie DPFOA_2026','https://www.mfsr.sk/files/archiv/36/prispevok_18.zip'),('Binstruction','instructions--Poučenie DPFOB_2026','https://www.mfsr.sk/files/archiv/36/prispevok_18.zip')]:
 raw=forms/(name+'.pdf');receipts[sid]={'file':str(raw),'sha256':sha(raw),'url':url}
def form(k,sid,name,lo,hi,qs):
    # Complete blank-separated original form blocks prevent a field number or footnote
    # being detached by a guessed display coordinate. These are reference excerpts,
    # not extra Guide rules or claims that unselected pages were read.
    lines=lf(forms/name);blocks=[];start=None
    for n in range(lo,hi+1):
        if lines[n-1].strip():
            if start is None:start=n
        elif start is not None:blocks.append((start,n-1));start=None
    if start is not None:blocks.append((start,hi))
    scope(k,sid,forms/name,lo,hi,'Official Ministry2026 return '+k,blocks,'Archive member and actual PDF/reader hashes retained. Complete original form blocks are reference excerpts; unused labels do not create additional Guide coverage. Field numbers are coordinates, not extra tax relief.')
form('A.details','Aform','forms--DPFOAv25 v1.10_vzor.txt',74,186,[(107,133),(170,185)])
form('A.base','Aform','forms--DPFOAv25 v1.10_vzor.txt',187,242,[(187,233)])
form('A.relief-credit','Aform','forms--DPFOAv25 v1.10_vzor.txt',243,339,[(246,286),(287,325),(326,338)])
form('A.settlement-notes','Aform','forms--DPFOAv25 v1.10_vzor.txt',340,351,[(343,351)])
form('A.payout-attachments','Aform','forms--DPFOAv25 v1.10_vzor.txt',440,512,[(481,496)])
form('B.details','Bform','forms--DPFOBv26 v1.3_vzor.txt',75,162,[(117,145)])
form('B.employment','Bform','forms--DPFOBv26 v1.3_vzor.txt',163,248,[(184,216)])
form('B.flat-expenses','Bform','forms--DPFOBv26 v1.3_vzor.txt',249,321,[(259,268),(283,303)])
form('B.business-loss','Bform','forms--DPFOBv26 v1.3_vzor.txt',322,397,[(325,359),(378,395)])
form('B.rental','Bform','forms--DPFOBv26 v1.3_vzor.txt',398,489,[(401,441),(456,461)])
form('B.capital-other','Bform','forms--DPFOBv26 v1.3_vzor.txt',490,655,[(535,552),(608,655)])
form('B.scales-relief','Bform','forms--DPFOBv26 v1.3_vzor.txt',656,771,[(659,715),(716,768)])
form('B.credits','Bform','forms--DPFOBv26 v1.3_vzor.txt',772,876,[(775,851),(852,874)])
form('B.settlement','Bform','forms--DPFOBv26 v1.3_vzor.txt',877,978,[(880,901),(903,933),(940,947)])
form('B.payout-attachments','Bform','forms--DPFOBv26 v1.3_vzor.txt',1057,1113,[(1083,1100)])
form('B.dividends','Bform','forms--DPFOBv26 v1.3_vzor.txt',1271,1403,[(1274,1282),(1379,1398)])
form('B.bonds','Bform','forms--DPFOBv26 v1.3_vzor.txt',1404,1472,[(1407,1430),(1452,1467)])
form('B.contribution-annex','Bform','forms--DPFOBv26 v1.3_vzor.txt',1473,1551,[(1511,1535)])
form('A.instructions-filing','Ainstruction','instructions--Poučenie DPFOA_2026.txt',7,38,[(10,37)])
form('A.instructions-credits','Ainstruction','instructions--Poučenie DPFOA_2026.txt',650,690,[(660,690)])
form('B.instructions-flat','Binstruction','instructions--Poučenie DPFOB_2026.txt',543,620,[(591,613)])
render_sources()

scopes['ITA43.PIT']['actual_read_ranges']=[[1,45],[81,115]]
scopes['ITA43.PIT']['read_mode']='Two selected retained primary reader ranges actually read; intervening LF46–80 not read for this ledger and not quoted.'
CAT.write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
render_sources()

scope('Act261.PIT',27,'sources/27.txt',942,1014,'Act261/2025 Income Tax Act amendments, points1–6',[(953,961),(963,977),(979,995)])
section('TC154.return-duty',20,'154',1,18,[(4,18)],note='Selected current offence definitions reread; no conclusion about VAT78a(15) special fine/second chance is imported.')
section('TC154.other-duty',20,'154',19,51,[(42,45)])
render_sources()
