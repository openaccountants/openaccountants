"""Build the actually read portion of the rental writer ledger, not a final seal."""
from pathlib import Path
from fractions import Fraction as F
from datetime import date
import json, hashlib, re

ROOT = Path('/Users/michaelcutajar/Documents/ChatGPT/OA')
BASE = Path(__file__).parent
GUIDE = ROOT / '.claude/worktrees/europe-germany/skills/international/germany/de-rental-income.md'
CAT = json.loads((BASE / 'cited-source-identities-candidates.json').read_text())['sources']
SOURCES = {v['source_id']: v for v in CAT.values()}
sha = lambda b: hashlib.sha256(b).hexdigest()
write = lambda n, d: (BASE / n).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

# Ranges are selected text actually exposed and read, never inferred from a download.
READ = {'DEB115': [[1,24]], 'DEB032': [[1,89]], 'DEB117': [[1,36]],
        'DEB031': [[1,12],[84,85]], 'DEB118': [[1,14]],
        'DEB180': [[6,18]], 'DEB030': [[6,16],[23,32],[49,49]],
        'DEB040': [[6,12]], 'DEB237': [[6,18]], 'DEB122': [[6,20]],
        'DEB185': [[1074,1079],[2504,2798]],
        'DEB213': [[601,734],[769,787],[811,839]],
        'DEB004': [[6,20]], 'DEB035': [[6,18]], 'DEB038': [[6,20],[35,45]],
        'DEB036': [[6,20]], 'DEB121': [[6,20],[23,30]], 'DEB126': [[6,24]],
        'DEB012': [[7,7],[32,32],[40,40]], 'DEB211': [[611,619],[2048,2053]],
        'DEB212': [[242,283],[521,525],[735,782]],
        'DEB014': [[7,24]],'DEB015':[[9,9]],'DEB016':[[7,27],[42,42]],
        'DEB017':[[7,8]],'DEB018':[[8,8]],'DEB123':[[115,125]],
        'DEB124':[[7,8]],'DEB125':[[9,15]],'DEB044':[[7,8],[44,45]],
        'DEB116':[[70,71]],'DEB127':[[7,7]],'DEB182':[[9,35]],
        'DEB280':[[6,8]],'DEB045':[[6,39]],'DEB042':[[6,19]],
        'DEB029':[[35,37]],'DEB043':[[6,29]],
        'RNT01':[[1,7],[420,445]],'RNT02':[[1,7],[220,249],[266,293],[336,345],[432,440]],
        'RNT03':[[177,186]],'RNT04':[[14,35],[275,310]],'RNT05':[[166,226]],
        'RNT06':[[1,16]],'RNT07':[[1,16]],'RNT08':[[1,18]]}
ANCHORS = []
def q(key, sid, lo, hi, article, note='', start=None, end=None):
    src = SOURCES[sid]
    raw = Path(src['path']).read_bytes()
    reader = Path(src['reader_path']).read_bytes()
    assert sha(raw) == src['sha256'] and sha(reader) == src['reader_sha256']
    assert any(a <= lo <= hi <= b for a,b in READ[sid]), (key, sid, lo, hi)
    original = reader.decode()
    display_lines = original.splitlines(keepends=True)
    offset = sum(len(x) for x in display_lines[:lo-1])
    text = ''.join(display_lines[lo-1:hi]).rstrip('\r\n')
    if start is not None:
        cut = text.index(start)
        offset += cut
        text = text[cut:]
    if end is not None:
        text = text[:text.index(end)+len(end)]
    assert text and original[offset:offset+len(text)] == text
    native_lf = [original[:offset].count('\n')+1,
                 original[:offset+len(text)-1].count('\n')+1]
    row = dict(id=key, source_id=sid, act_article=article, official_url=src['official_url'],
               exact_original_language_quote=text, reader_native_LF=native_lf,
               selected_reader_display_lines=[lo,hi],
               read_on='2026-10-29', source_sha256=src['sha256'],
               reader_sha256=src['reader_sha256'],
               source_kind=src.get('source_kind','retained official raw body and derived reader'), note=note)
    ANCHORS.append(row)

q('R01','DEB115',7,8,'EStG §21(1) no.1')
q('R02','DEB115',10,15,'EStG §21(1) nos.2–4 and §§15a/15b referral')
q('R03','DEB115',17,17,'EStG §21(3)')
q('R04','DEB032',14,20,'EStG §7(4) no.2 and sentence2')
q('R05','DEB032',81,81,'EStG §7(5b)')
q('R06','DEB032',69,79,'EStG §7(5) no.3(c) and sentences2–3',
  'Historic housing branch, not the modern section7(5a) scheme.')
q('R07','DEB032',80,80,'EStG §7(5a)',
  start='1Bei Gebäuden',end='freiwillig angezeigt hat.')
q('R08','DEB032',80,80,'EStG §7(5a) sentences4–8',
  start='4Die Absetzung',end='maßgebenden Prozentsatz.')
q('R09','DEB032',7,7,'EStG §7(1) sentence4',start='4Im Jahr',end='vorangeht.')
q('R10','DEB032',7,7,'EStG §7(1) sentences1–2',start='1Bei Wirtschaftsgütern',end='Wirtschaftsguts.')
q('R11','DEB117',7,7,'EStG §7b(1)')
q('R12','DEB117',9,11,'EStG §7b(2) sentence1 nos.1–2')
q('R13','DEB117',13,13,'EStG §7b(2) sentence1 no.3')
q('R14','DEB117',14,21,'EStG §7b(2) sentence2 and (3)')
q('R15','DEB117',22,28,'EStG §7b(4)')
q('R16','DEB117',29,29,'EStG §7b(5)')
q('R17','DEB122',15,15,'EStG §7a(9)')
q('R18','DEB031',10,10,'EStG §6(1) no.1a')
q('R19','DEB030',49,49,'EStG §9(5)')
q('R20','DEB118',7,7,'EStDV §82b(1)')
q('R21','DEB118',8,9,'EStDV §82b(2)–(3)')
q('R22','DEB031',84,84,'EStG §6(2) sentence1',start='1Die Anschaffungs-',end='nicht übersteigen.')
q('R23','DEB030',26,26,'EStG §9(1) sentence3 no.7')
q('R24','DEB115',16,16,'EStG §21(2)')
q('R25','DEB040',7,7,'EStG §11(1) sentences1–3',start='1Einnahmen',end='geleistet wird.')
q('R26','DEB040',8,8,'EStG §11(2) sentences1–4',start='1Ausgaben',end='marktüblich ist.')
q('R27','DEB030',7,10,'EStG §9(1) sentences1–3 nos.1–2')
q('R28','DEB030',14,14,'EStG §9(1) sentence3 no.4 sentence2',start='2Zur Abgeltung',end='benutzt.')
q('R29','DEB030',16,16,'EStG §9(1) sentence3 no.4a sentence2',start='2Anstelle',end='festgesetzt sind.')
q('R30','DEB030',32,32,'EStG §9(3)')
q('R31','DEB180',8,8,'BRKG §5(2)',
  'Read with EStG9(1)no4a/9(3): that tax rule imports the highest vehicle rate; does not impose an employer approval condition on a private landlord.')
q('R32','DEB237',7,7,'HGB §255(1)')
q('R33','DEB237',8,8,'HGB §255(2) sentence1',end='entstehen.')
q('R34','DEB185',2580,2587,'ELSTER 2025 AnlageV instructions: Werbungskosten',
  'Dated 2025 form and practice instructions; no assertion of published2026 line numbers.')
q('R35','DEB185',2591,2593,'ELSTER 2025 AnlageV: building/land and acquired reserve')
q('R36','DEB185',2601,2601,'ELSTER 2025 AnlageV: former own-use building')
q('R37','DEB185',2610,2610,'ELSTER 2025 AnlageV: shorter useful life proof')
q('R38','DEB185',2644,2644,'ELSTER 2025 AnlageV: free acquisition predecessor rate')
q('R39','DEB185',2697,2699,'ELSTER 2025 AnlageV lines42–45: furniture and800VAT-exclusive gate')
q('R40','DEB185',2700,2702,'ELSTER 2025 AnlageV lines46–51: interest/financing')
q('R41','DEB185',2709,2714,'ELSTER 2025 AnlageV lines55–72: improvement/acquisition/reserve')
q('R42','DEB185',2737,2744,'ELSTER 2025 AnlageV lines87–88: cheap-let ratio/forecast/cut')
q('R43','DEB185',2745,2749,'ELSTER 2025 AnlageV: alternative equal-ranking market rent proofs')
q('R44','DEB185',2751,2754,'ELSTER 2025 official cheap-let example inputs/income')
q('R45','DEB185',2758,2762,'ELSTER 2025 official cheap-let example costs/pre-cut result')
q('R46','DEB185',2775,2777,'ELSTER 2025 official cheap-let example40percent/cost cut/result')
q('R47','DEB185',2780,2785,'ELSTER 2025 AnlageV-FeWo scope and four objects per form')
q('R48','DEB185',2793,2797,'ELSTER 2025 AnlageV-FeWo own-use/day allocation/local letting days')
q('R49','DEB185',2547,2558,'ELSTER 2025 AnlageV lines13–24 income and Umlagen')
q('R50','DEB185',2563,2572,'ELSTER 2025 AnlageV lines25–31/89 deposits/sites/grants')
q('R51','DEB185',2717,2728,'ELSTER 2025 AnlageV lines73–82 passed/unpassed/other costs')
q('R52','DEB185',2731,2735,'ELSTER 2025 AnlageV example line83/85/86 and account fees',
  'Guide bank keywords are editorial interpretations, not quoted official form labels.')
q('R53','DEB213',618,621,'BMF08Oct2004 para1 and notes2 in official EStH2024 Anhang30II',
  'Selected retained official text plus notes. This is not proof that no later2025/2026 amendment exists.')
q('R54','DEB213',636,642,'BMF08Oct2004 paras5–7: temporary intention/evidence')
q('R55','DEB213',646,650,'BMF08Oct2004 paras7notes/8/9: term/factual rebuttal')
q('R56','DEB213',652,652,'BMF08Oct2004 para10: later evidence/AO173')
q('R57','DEB213',665,669,'BMF08Oct2004 para13 WITH operative2021 note',
  'Never quote the old56/75percent amounts without the attached note replacing them by50/66percent from2021.')
q('R58','DEB213',677,677,'BMF08Oct2004 para15: relatives and unrelated tenants')
q('R59','DEB213',682,684,'BMF08Oct2004 para16 WITH25percent shortfall note')
q('R60','DEB213',686,690,'BMF08Oct2004 para17: no-own-use evidence')
q('R61','DEB213',694,696,'BMF08Oct2004 paras18–19: proof/marketing/work visits')
q('R62','DEB213',701,707,'BMF08Oct2004 paras21–23: own-use forecast and vacancy allocation')
q('R63','DEB213',713,723,'BMF08Oct2004 paras25–26 WITH vacancy notes')
q('R64','DEB213',729,729,'BMF08Oct2004 para27: taxpayer evidence burden')
q('R65','DEB213',733,733,'BMF08Oct2004 para27 example: cheap-let contract30year start')
q('R66','DEB213',771,776,'BMF08Oct2004 paras33–34: forecast scope/30years/sale gains/per-object')
q('R67','DEB213',783,784,'BMF08Oct2004 para34 example2 and straight-line forecast rule',
  'Modern7(5a) is not named by the2004 letter; Guide exclusion follows the stated7(4) forecast rule and general exclusion of actual special/degressive deductions.')
q('R68','DEB213',785,787,'BMF08Oct2004 para34: fiveyear estimate/objective changes/10percent margins')
q('R69','DEB213',832,834,'BMF08Oct2004 paras39–40: eligible holiday periods/mixed costs')
q('R70','DEB004',8,8,'EStG §23(1) sentence1 no.1: tenyears and own-use exception')
q('R71','DEB004',13,13,'EStG §23(1) sentence3: single free successor',
  start='3Bei unentgeltlichem Erwerb',end='zuzurechnen.')
q('R72','DEB004',18,18,'EStG §23(3) sentences1/4–8',
  'Full paragraph retained to cover tax base, AfA reduction,1000cliff and private-sale loss ring-fence.')
q('R73','DEB035',7,7,'EStG §10d(1): two-year ordered carryback/1m2m/full waiver')
q('R74','DEB035',8,8,'EStG §10d(2): carryforward thresholds/70percent')
q('R75','DEB035',10,10,'EStG §10d(4) sentence1: separate determination',
  start='1Der am Schluss',end='festzustellen.')
q('R76','DEB038',8,9,'EStG §46(2) no.1: employee410 filing trigger')
q('R77','DEB038',41,43,'EStG §46(3)/(5):410 deduction/phaseout regulation')
q('R78','DEB036',7,7,'EStG §37(1): quarterly payment dates')
q('R79','DEB036',9,9,'EStG §37(3) sentences8–10: newbuilding loss/7b exception',
  start='8Negative Einkünfte',end='Anspruch genommen werden.')
q('R80','DEB036',11,11,'EStG §37(5) sentence1:400 annual/100 per date',
  start='1Vorauszahlungen',end='betragen.')
q('R81','DEB126',19,23,'EStG §39a(1) no.5: allowance imports37(3) timing')
q('R82','DEB121',24,25,'EStG §35c(2)/(3): exclusive own-use/no expense duplication')
q('R83','DEB012',7,7,'EStG §52(1):2026 application',
  start='1Diese Fassung',end='anzuwenden.')
q('R84','DEB012',32,32,'EStG §52(15a):old7b2026 sunset/modern branch')
q('R85','DEB012',40,40,'EStG §52(18b):70percent starts2024')
q('R86','DEB211',611,619,'BGBl2024I108 Article6:60percent from2028')
q('R87','DEB211',2051,2051,'BGBl2024I108 Article35(9):Article6 effective1Jan2028')
q('R88','DEB212',247,254,'BMF21May2025 para16:old7b2026 sunset')
q('R89','DEB212',273,282,'BMF21May2025 para16 example1:2024 buyer last2026 claim/fourth lost')
q('R90','DEB212',521,523,'BMF21May2025 para43:land and associated side costs excluded')
q('R91','DEB212',735,742,'BMF21May2025 para65:normalAfA uncapped actualcost')
q('R92','DEB212',746,751,'BMF21May2025 para66:restvalue after fouryear benefit period')
q('R93','DEB212',770,770,'BMF21May2025 example7:straightline firstyear month-cut')
q('R94','DEB185',2653,2668,'ELSTER2025 AnlageV:old/new7b aid and checklist distinctions')
q('R95','DEB014',8,10,'AO §149(2)/(3):ordinary sevenmonths/advised eligibility')
q('R96','DEB014',23,24,'AO §149(3)/(4):advised February deadline/earlier call')
q('R97','DEB015',9,9,'AO §108(3):weekend/publicholiday rollover')
q('R98','DEB016',7,22,'AO §152(1)–(3):discretion/14months/19months/earlier call/exceptions')
q('R99','DEB016',27,27,'AO §152(5):calendar-year surcharge computation')
q('R100','DEB016',42,42,'AO §152(10):whole euro floor and25000cap')
q('R101','DEB017',7,8,'AO §233a(1)/(2):assessment interest/ordinary15months')
q('R102','DEB018',8,8,'AO §238(1a):0.15percent monthly/1.8annual')
q('R103','DEB123',115,122,'UStG §4no12:property exemption/exceptions')
q('R104','DEB124',7,8,'UStG §9(1)/(2):business recipient/eligible use/proof')
q('R105','DEB125',9,15,'UStG §27(2):historic option exemption',
  'Both completion and construction-start conditions are in the source. The Guide says SOME buildings, not that start alone suffices.')
q('R106','DEB044',7,8,'UStG §12(1)/(2):19percent/7percent')
q('R107','DEB044',44,45,'UStG §12(2)no11:guest room7percent/no unrelated extras')
q('R108','DEB116',70,71,'EStG §49(1)no6:domestic rental source')
q('R109','DEB127',7,7,'EStG §50(1)sentences1–2:domestic costs/basicallowance addback',
  start='1Beschränkt Steuerpflichtige',end='Grundfreibetrags.')
q('R110','DEB182',9,19,'EGAO Art97§36(3)no1(e):2020–24 scope/advised2024date30April2026')
q('R111','DEB280',7,7,'EStG §1(1) sentence1:resident unlimited liability',
  start='1Natürliche Personen',end='einkommensteuerpflichtig.')
q('R112','DEB045',17,25,'EStG §2(1)no6/(2)no2:rent category/receipt less expense measure')
q('R113','DEB045',27,29,'EStG §2(3)–(5):aggregate income to taxable base')
q('R114','DEB045',33,33,'EStG §2(7):calendar year and part-year resident assessment')
q('R115','DEB042',7,14,'EStG §12:private expenses/personal income taxes/criminal penalties',
  'Church tax is not a rental Werbungskosten deduction; this quote preserves the express special-expense exceptions instead of denying all possible deductibility.')
q('R116','DEB029',36,37,'EStG §4(5)no8:fines with statutory economic-benefit exception',
  'Read with EStG9(5); generic Guide exclusion does not decide an exceptional disgorgement payment.')
q('R117','DEB043',7,8,'UStG §15(1)no1:input-tax business/invoice gate')
q('R118','DEB043',15,24,'UStG §15(1) finalsentence/(1a)/(1b)/(2):use and exclusion gates')
q('R119','DEB185',1074,1079,'ELSTER2025 AnlageN:dated commuting rate30cfirst20km/38c thereafter',
  'Only the dated2025rate is applied here; rental-property first-place classification remains unconfirmed.')
q('R120','DEB185',2504,2520,'ELSTER2025 AnlageV/V-FeWo/V-Sonstige/AnlageAUS scope')
q('R121','RNT01',428,443,'BFH14July2016 IVR34/13 para37:hotel-like demarcation',
  'Demarcation paragraph in the shopping-centre judgment. Does not make every extra service a trade; only scoped referral in this Guide.')
q('R122','RNT02',223,247,'BFH21July2020 IXR26/19 paras23–25:contractual price split/verification')
q('R123','RNT02',277,284,'BFH21July2020 IXR26/19 para30:market-value ratio',
  'The ratio principle is used; no2026application of old ImmoWertV procedural wording is asserted.')
q('R124','RNT02',336,341,'BFH21July2020 IXR26/19 para37:separate valuation/no residual method',
  'Historic work-aid criticism is not asserted against the revised2026tool. Only the stated ratio/no residual method principle is bound.')
q('R125','RNT02',433,440,'BFH21July2020 IXR26/19 para45:independent valuation')
q('R126','RNT03',178,186,'FGMünster10Dec2019 2K2497/17E paras21–25:deposit economic receipt',
  'Corroborating reasoning only: judgment was reversed by BFHIXR11/20 on attribution/repair compensation; exact appeal tenor R127 retained. Current administrative ELSTER treatment R50 and statutory trust attribution R131 provide separate support. Not represented as an unreversed binding judgment.')
q('R127','RNT04',25,32,'BFH9July2021 IXR11/20 appeal disposition',
  'Appeal history forR126. The retained BFH body does not address the deposit wording; no BFHdeposit holding is invented.')
q('R128','RNT04',288,296,'BFH9July2021 IXR11/20 paras31–32:repair maintenance and payment year',
  'Case-specific repair examples inform the Guide examples; actual standard improvement/15percent cost gates still govern.')
q('R129','RNT05',199,226,'BFH6February2018 IXR14/17 paras18–20:furnished market comparison',
  'Only the market-measurement rule is adopted; historical56/75percent thresholds in earlier paragraphs are not used for2026.')
q('R130','RNT06',7,14,'AO §370(1):false/incomplete facts and tax-shortfall offence',
  'No sentence/penalty amount is added to the Guide. Criminal case is an explicit referral.')
q('R131','RNT07',7,10,'AO §39(1)/(2)no1:ownership/trust attribution')
q('R132','DEB032',11,20,'EStG §7(4):building AfA until fully depreciated')
q('R133','DEB185',2521,2544,'ELSTER2025 AnlageV lines6–12:property dates/use/floor area')
q('R134','DEB185',2669,2671,'ELSTER2025 AnlageV lines39–41:7h/7i headings')
q('R135','RNT08',8,10,'BMF2026 purchase-price work-aid official web observation',
  'Official indexed announcement observation only; rawHTML/open routes returned503. No tool execution/XLSXinspection or direct-body reading is claimed.')

# Complete the finite source pass without pretending individual examples are
# verbatim statute. Applications and editorial limits remain identified below.
OVERRIDES={
25:(['R03','R121'],'Bound category rule and source-backed hotel-style referral; not a categorical trade determination.'),
67:(['R49','R50','R01','R02','R25','R126','R127','R131'],'Bound actual receipts/deposit treatment; furniture consideration is an application of paid rental-use income, not an imputed charge.'),
75:(['R27','R23','R34','R40','R41','R51','R52'],'Bound income-related cost categories. Incidental management/legal/advertising/account fees are writer applications of9(1), not assertions of automatic deductibility without the income connection.'),
77:(['R27','R32','R34','R41','R115','R116','R19'],'Bound applications of interest-versus-acquisition/private-cost rules. Principal is distinguished from interest; exceptional economic-benefit disgorgement is not decided by the generic fine exclusion. Church-tax special-expense treatment is outside this rental-cost list.'),
88:(['R123','R124','R122','R125','R135'],'Bound market-value/contract/expert principles plus explicitly identified official work-aid web observation; no2026work-aid execution.'),
91:(['R132','R27','R131'],'Bound ordinary cessation inference from own depreciable asset/rental use; exact month-of-sale AfA expressly remains unconfirmed.'),
112:(['R128','R33','R18','R19','R26','R20'],'Bound maintenance principle and stated examples; fact-sensitive production/acquisition/15percent gates are retained in adjacent paragraphs.'),
121:(['R01','R02','R10','R22','R23','R39','R129'],'Bound actual rental consideration/furniture depreciation/800gate and newly sourced market-comparison method.'),
158:(['R121','R103','R106','R107','R13'],'Bound demarcation/referral, accommodationVAT and7bexclusion; no general VAT filing computation claimed.'),
192:(['R95','R96','R97','R110','R84','R119','R28'],'Bound filing dates,2024transition and dated2025/2026commuting figures; property-specific first-place classification remains unconfirmed.'),
234:(['R04','R27','R29','R30','R31','R41','R32'],'Invented fixture inputs and bound legal parameters; all original executable expected outputs preserved and recomputed.'),
268:(['R24','R42','R44','R45','R46','R57','R65','R66','R67','R68'],'Bound actual official2025example reused against unchanged2026cheap-let test; forecast method and arithmetic separately verified.'),
}

assert len({x['id'] for x in ANCHORS})==len(ANCHORS)
write('actual-source-quotes-core.json', ANCHORS)
write('actual-read-scopes.json', {'date':'2026-10-29','official_reader_display_lines':READ,
      'coordinate_note':'Read exposures used Python splitlines display coordinates, including PDF formfeeds. Exact quote reader_native_LF values are separately computed from preserved substring offsets; no raw-reader normalization.',
      'current_guide_read_native_LF':[[1,len(GUIDE.read_text().split('\n'))]],
      'old_pre_refresh_read_native_LF':[[1,len((BASE/'pre-refresh-original.md').read_text().split('\n'))]],
      'scope':'Selected actually read excerpts; no full-source or independent review claim.'})

# Core bindings are explicit. A multi-clause rule remains partial until every clause is bound.
MAPPING = [
 (24,['R01','R02'],'bound'),(25,['R03'],'partial: hotel-like/business boundary needs source'),
 (27,['R108'],'bound'),
 (26,['R111','R112'],'bound residence/scope; foreign-treaty computation is explicit referral'),
 (28,['R83','R114'],'bound'),(29,['R112','R113','R25','R26'],'bound measure; full tariff belongs to sibling'),
 (39,['R04'],'bound'),(40,['R04'],'bound'),(41,['R04'],'bound'),(42,['R07','R08'],'bound'),
 (43,['R11'],'bound'),(44,['R12','R14'],'bound'),
 (45,['R12','R14','R84'],'bound'),
 (46,['R18','R19'],'bound'),(47,['R20'],'bound'),(48,['R22','R23','R39'],'bound'),
 (49,['R24'],'bound'),(50,['R24'],'bound'),(51,['R29','R30','R31'],'bound'),(52,['R28','R30'],'bound'),
 (53,['R70'],'bound'),(54,['R72'],'bound'),(55,['R73'],'bound'),
 (56,['R74','R85','R86','R87'],'bound'),(57,['R76'],'bound'),(58,['R80'],'bound'),
 (59,['R103','R104','R106','R107'],'bound'),(60,['R98','R99','R100'],'bound'),
 (61,['R101','R102'],'bound'),
 (67,['R49','R50'],'partial: furniture/refundable-deposit exclusion require exact anchors'),
 (68,['R49','R51'],'bound'),(69,['R25','R26'],'bound'),(73,['R27','R34'],'bound'),
 (75,['R27','R23','R40','R41','R51','R52'],'partial: broad enumerated incidental fees need individual source coverage'),
 (76,['R28','R29','R30','R31'],'bound for numeric rule; actual first-place determination explicitly unconfirmed'),
 (77,['R32','R34','R41'],'partial: personal tax/fine/principal exclusions need exact source clauses'),
 (78,['R82'],'bound'),
 (82,['R04','R05'],'bound'),(83,['R04','R37'],'bound'),(84,['R06'],'bound afterDE-L22 restoration'),
 (85,['R38'],'bound'),(86,['R07','R08'],'bound'),
 (87,['R32','R35','R36','R50'],'bound'),
 (88,['R35'],'partial: actual March2026 BMF search observation and market-value clause need explicit binding'),
 (89,['R09','R08','R06','R93'],'bound'),
 (90,['R04','R07','R08','R09'],'arithmetic controls; selected clauses bound'),
 (91,['R04'],'partial: sale-year cessation not sourced here'),
 (95,['R11'],'bound'),(97,['R12'],'bound'),
 (98,['R14','R91'],'bound'),
 (99,['R11'],'bound'),(100,['R13'],'bound'),(101,['R12'],'bound'),
 (102,['R84','R88','R89'],'bound'),(103,['R15'],'bound'),(104,['R17','R92'],'bound'),
 (105,['R16','R84','R94'],'bound'),
 (106,['R04','R11','R12','R13','R14','R90','R91'],'bound plus arithmetic controls'),
 (112,['R26','R20'],'partial: maintenance examples not stated by generic clauses'),
 (113,['R33','R41'],'bound'),(114,['R32','R41'],'bound'),(115,['R18','R19'],'bound'),
 (116,['R18','R19','R04'],'arithmetic checked; assessment correction is explicit referral'),
 (117,['R20','R21'],'bound; special scheme computation is referral'),
 (121,['R10','R22','R23','R39'],'partial: furniture-surcharge income source pending'),
 (125,['R24'],'bound for statutory home scope; frequency observation is editorial'),
 (129,['R24','R42'],'bound'),(130,['R42'],'bound'),(131,['R24','R42'],'bound'),
 (133,['R42'],'bound'),(134,['R34','R42'],'bound'),
 (135,['R57'],'bound with explicit2021 note'),(136,['R65','R66','R67'],'bound'),
 (137,['R67'],'bound; modern5a exclusion is the disclosed application of the7(4) forecast method'),
 (138,['R68'],'bound'),(139,['R68'],'bound'),(140,['R66'],'bound'),(141,['R57'],'bound'),
 (142,['R43'],'bound'),(143,['R24'],'bound statutory home scope; commercial case referred'),
 (149,['R53'],'bound to retained official handbook'),(150,['R54','R55'],'bound'),
 (151,['R63','R64'],'bound'),
 (152,['R47'],'bound'),(153,['R48'],'bound'),
 (154,['R59'],'bound with qualification'),(155,['R60','R61'],'bound'),
 (156,['R62','R66','R67','R68','R69'],'bound'),(157,['R56','R53'],'bound'),
 (158,['R103','R106','R107','R13'],'partial: hotel-like trade boundary source pending; VAT filing handed to sibling'),
 (162,['R103','R104','R105','R106','R49','R51','R117','R118'],'bound as basic option/input method subject to actual15 invoice/use/exclusion gates; full VAT computation is sibling scope'),
 (166,['R112','R113'],'bound aggregate rental loss offset'),
 (167,['R73'],'bound'),(168,['R74','R75','R85','R86','R87'],'bound'),(169,['R02'],'bound'),
 (173,['R70'],'bound'),(174,['R70'],'bound'),(175,['R72'],'bound'),(176,['R72'],'bound'),
 (177,['R71'],'bound; heirs-community computation is explicit referral'),
 (178,['R21','R15'],'bound'),(179,['R70','R72','R04'],'arithmetic checked; sale-year AfA expressly stipulated/unconfirmed'),
 (190,['R76','R77'],'bound'),(193,['R78','R79','R80','R81'],'bound'),
 (191,['R95','R96','R97'],'bound plus calendar computation'),
 (192,['R95','R96','R97','R110','R84'],'partial: historical2025 commuting rate source remains explicit check'),
 (216,['R95','R96','R98','R99','R100'],'bound plus calendar computation'),
 (217,['R101','R102'],'bound plus calendar computation'),(218,['R15'],'bound'),
 (223,['R108','R109'],'bound; options and assessment procedure are explicit sibling handoff'),
 (225,['R07','R11'],'bound only with stated territorial/help gates; foreign-property taxability referred'),
 (234,['R04','R27','R29','R30','R31','R41'],'fixture inputs plus partially bound exclusions'),
 (236,['R49','R51','R52'],'arithmetic checked; tariff sibling remains handoff'),
 (266,['R44','R45'],'bound official illustrative2025 inputs reused for2026 statutory test'),
 (268,['R24','R42','R44','R45','R46'],'bound and arithmetic checked; forecast method separate pending source'),
]
lines=GUIDE.read_text().splitlines()
MAPPING=[(n,*OVERRIDES[n]) if n in OVERRIDES else (n,a,s) for n,a,s in MAPPING]
assert len({n for n,a,s in MAPPING})==len(MAPPING)
write('current-core-bindings.json', [dict(native_LF=n,wording=lines[n-1],anchors=a,status=s,
     guide_sha256=sha(GUIDE.read_bytes())) for n,a,s in MAPPING])

CONTROL=[]
def check(name,actual,expected,kind='arithmetic'):
    assert actual==expected,(name,actual,expected)
    CONTROL.append(dict(name=name,actual=str(actual),expected=str(expected),kind=kind,result='PASS'))
check('oldcase1 income',9*(1200+250),13050)
check('oldcase1 declining firstyear',F(300000)*F(5,100)*F(9,12),11250)
check('oldcase1 othercosts',9000+2250+600,11850)
check('oldcase1 loss',13050-11850-11250,-10050)
check('oldcase1 straightline',F(300000)*F(3,100)*F(9,12),6750)
check('oldcase1 straightline loss',13050-11850-6750,-5550)
check('oldcase1 nextyear restvalue',F(300000-11250)*F(5,100),F(28875,2))
check('oldcase2 cost threshold',F(200000)*F(15,100),30000)
check('oldcase2 overcliff',12000+19000>30000,True)
check('oldcase2 equal threshold notover',12000+18000>30000,False)
check('oldcase2 yearly cost depreciation',31000*F(2,100),620)
check('oldcase3 paid ratio',F(270+150,60*15+150),F(2,5))
check('oldcase3 income',(270+150)*12,5040)
check('oldcase3 allowedcost',4920*F(2,5),1968)
check('oldcase3 surplus',5040-1968,3072)
check('oldcase3 spouse',F(3072,2),1536)
check('oldcase3 fullpaid variant above66',F(700,1050)>=F(66,100),True)
check('oldcase3 forecast variant',F(1,2)<=F(600,1050)<F(66,100),True)
check('oldcase4 costperm2',F(400000,80),5000)
check('oldcase4 costeligibility',F(400000,80)<=5200,True)
check('oldcase4 cap',80*4000,320000)
check('oldcase4 specialannual',320000*F(5,100),16000)
check('oldcase4 normalannual',400000*F(3,100),12000)
check('oldcase4 totalfirstyear',16000+12000,28000)
check('oldcase4 ineligiblevariant',F(420000,80)>5200,True)
check('oldcase5 stipulatedAfA',4000+6*4800+800,33600)
check('oldcase5 reducedcost',300000-33600,266400)
check('oldcase5 gain',340000-266400-10000,63600)
check('oldcase6 carried rental loss',13050-11850-11250,-10050,
      'arithmetic only: legal prepayment year gate still pending source binding')
check('newcase1 income',(950+180)*12,13560)
check('newcase1 AfA',180000*F(2,100),3600)
check('newcase1 travel',300*F(30,100),90)
check('newcase1 costs',3600+4200+2160+540+1500+90+60,12150)
check('newcase1 surplus',13560-12150,1410)
check('newcase2 allcosts',3000+1800+120,4920)
check('newcase2 precutresult',5040-4920,120)
check('newcase2 percentagecut',(1-F(2,5))*100,60)
check('newcase2 disallowedcost',4920*F(3,5),2952)
check('cheaplet50boundary',F(525,1050)<F(1,2),False,'threshold separator')
check('cheaplet66boundary',F(693,1050)>=F(66,100),True,'threshold separator')
check('new7bcliffinclusive',80*5200,416000,'threshold separator')
check('new7bfirstcentover',F(41600001,100)/80>5200,True,'threshold separator')
check('2026 unadvised nominal31July2027 Saturday',date(2027,7,31).weekday(),5,'calendar')
check('2026 unadvised moved2August2027 Monday',date(2027,8,2).weekday(),0,'calendar')
check('2026 advised29February2028 Tuesday',date(2028,2,29).weekday(),1,'calendar')
check('2025 unadvised31July2026 Friday',date(2026,7,31).weekday(),4,'calendar')
check('2025 advised nominal28February2027 Sunday',date(2027,2,28).weekday(),6,'calendar')
check('2025 advised moved1March2027 Monday',date(2027,3,1).weekday(),0,'calendar')
check('2024 advised30April2026 Thursday',date(2026,4,30).weekday(),3,'calendar')
write('writer-arithmetic-core.json',CONTROL)

progress=json.loads((BASE/'reading-progress.json').read_text())
progress.update(old_pre_refresh_actual_read_native_LF=[[1,len((BASE/'pre-refresh-original.md').read_text().split('\n'))]],
    old_unread_native_LF=[],actual_legal_quote_binding=f'{len(ANCHORS)} core actual quote anchors; partial bindings remain explicit',
    no_Guide_edits=False,Guide_edit='DE-L22/DE-L24 selected OptionA old-topic/case restorations; writer scope only',
    current_guide_sha256=sha(GUIDE.read_bytes()),writer_controls=len(CONTROL),
    status='IN PROGRESS: not final ledger, no independent verdict; forecasts/filing/losses/source completeness still pending')
write('reading-progress.json',progress)
print(json.dumps({'actual_anchors':len(ANCHORS),'core_units':len(MAPPING),'writer_controls':len(CONTROL),
                  'Guide_sha256':sha(GUIDE.read_bytes()),'status':'partial writer evidence; no country review'},indent=2))
