"""Build reviewer evidence only. Does not edit Guides, metadata, or author ledgers."""
from pathlib import Path
import re,json,hashlib,subprocess,collections
R=Path(__file__).parent
HEAD='2cec36c47e29f010fe0884693d40018c1313df7e';BASE='46c01152da0fdd1b722f61190c88413d0a195d02';ORIG='e04697d543f9cff8c7a4db148a0f4ec73c65b941'
def git(ref,path):return subprocess.check_output(['git','show',ref+':'+path],text=True)
# Reviewed source groups: full recovered clauses, not the author's short quotation alone.
E={
 'IT2':'primary-web-read-2026-11-01.json income-law table art.2, returned lines130-139; inherited-income-penalties.txt residence/registration fragments',
 'IT3':'inherited-income-selected-clauses.txt art.3, including all art.3(c)(1)-(3) and art.3(d)',
 'IT9':'inherited-income-selected-clauses.txt complete art.9(a)-(e)',
 'IT10':'inherited-income-selected-clauses.txt complete art.10(a)-(b)',
 'IT11':'inherited-income-selected-clauses.txt complete art.11(a)-(j), including cessation art.11(g)',
 'IT12':'inherited-income-selected-clauses.txt art.12(a)-(f); interest exception is truncated, supplemented by independent-additional-primary-followup.json MOIN law p9 lines398-418',
 'IT17':'inherited-income-selected-clauses.txt complete arts.17-19, including filing exemptions and longer advance-payment period under executive instructions',
 'IT22':'inherited-income-penalties.txt art.22 registration fragment',
 'IT27':'inherited-income-penalties.txt art.27 amendment fragment and exclusions',
 'IT36':'inherited-income-penalties.txt art.36(a)-(c) complete neighboring fragments; independent-additional-primary-followup.json MOIN law p17 lines675-683',
 'IT4':'inherited-income-penalties.txt partial art.4; completed failed-check research in independent-additional-primary.json MOIN law p3 lines182-204 (not a 2026-currentness clearance)',
 'FORMS':'agent-a2a55474814cab15f.jsonl.source-extracts.txt lines1508-1545 actual ISTD first-page form names, not form fields',
 'TP':'agent-a2a55474814cab15f.jsonl.source-extracts.txt lines1560-1610 actual ISTD TP file list, not underlying thresholds',
 'GST6':'inherited-gst-selected-clauses.txt damaged art.6 OCR; primary-web-read-2026-11-01.json GST table returned line135 establishes art.6 and16%',
 'GST7':'inherited-gst-selected-clauses.txt zero/exempt/tied supply clauses; original author transcript lines1470-1481 establishes Schedule2; schedule3 supported by actual file-list title, not schedule contents',
 'GSTREG':'inherited-gst-selected-clauses.txt complete registration triggers and voluntary registration; numeric limit remains held',
 'GSTBASE':'inherited-gst-selected-clauses.txt buyer-price clause and tied-supply art.7(c)/(d)',
 'GSTINPUT':'inherited-gst-selected-clauses.txt deductions clause, incomplete purchases/imports and pre-registration subclauses; no complete blocked-input instructions read',
 'GSTSERVICE':'agent-a1aabfd173c8e5b70.jsonl.source-extracts.txt lines1280-1294 complete recovered imported-service payment clause incl partial payment/service and Director-approved deferral',
 'GSTFILE':'inherited-gst-selected-clauses.txt period/payment/invoice clauses and neighbors; directors assigned periods and optional extension',
 'GSTPEN':'agent-a1aabfd173c8e5b70.jsonl.source-extracts.txt lines1268-1276 weekly four-per-thousand charge; inherited-gst-selected-clauses.txt complete minor-contraventions list',
 'GSTREF':'inherited-gst-selected-clauses.txt refund clause, complete nonresident departure subclause50-500; day-limit and article number damaged',
 'RATES':'agent-a2a55474814cab15f.jsonl.source-extracts.txt rates/schedules first-page file-list output; list titles10%,5%,4%,2%, not all product classifications',
 'SSC3':'ssc-law-en.txt arts.3-7,43,49,59; art.4 coverage and exceptions; Arabic rate-source neighboring pages45,49,55',
 'SSC20':'ssc-law-en.txt arts.19-22; original Arabic PDF pages29-31 visually inspected, including protected pre-15Oct2009 wages and inflation catch-up',
 'SSC24':'ssc-law-en.txt art.24 and neighboring arts.25-27; original Arabic PDFp35 visually inspected:2%',
 'SSC42':'ssc-law-en.txt arts.42-47; original Arabic PDFp45 visually inspected:0.75% and government/voluntary exclusions',
 'SSC48':'ssc-law-en.txt arts.48-49; original Arabic PDFp49 visually inspected:0.5%,1% and exclusions',
 'SSC59':'ssc-law-en.txt arts.59-61; original Arabic PDFp55 visually inspected:11%,6.5%,17.5%, reduction and agricultural partial-coverage clauses',
 'SSC64':'ssc-law-en.txt art.64(c)(1)-(4); original Arabic PDFp59 visually inspected:1% hazardous-work employer addition and prescribed-profession condition',
 'CAP':'primary-web-read-2026-11-01.json Arabic Petra returned lines16-21, dated14May2026:3733,3668,623,612,1.77%; inherited English Petra response independently agrees',
 'REDUCTION':'inherited-gst-selected-clauses.txt final Regulation45/2024 OCR excerpt; table incomplete and held; no entitlement cleared',
 'MANIFEST':'source-manifest.json matched all8 non-null cache SHA256 hashes; actual read scope compared with cached returned content; no later-amendment absence inferred',
 'ARITH':'All10 oa-check blocks independently recomputed and check-examples.py --require passed. Inputs remain conditional under named currentness holds.'
}
# Each legal/executable row gets actual independently-read evidence, including rows incorrectly mapped NONE by author.
M={}
def maprows(slug,ids,refs,note=''):
 for n in ids:M[(slug,f'C{n:03}')]=(refs,note)
s='jo-income-tax'
maprows(s,[2],['IT2','IT3','IT9','IT11']);maprows(s,range(5,12),['IT11']);maprows(s,range(12,16),['IT9']);maprows(s,[16,17],['IT10']);maprows(s,[18,19],['IT12']);maprows(s,[20],['IT11']);maprows(s,[21],['IT2','IT3','IT4']);maprows(s,[22],['IT9']);maprows(s,[24],['IT22']);maprows(s,[25,26,27,28,31],['IT17']);maprows(s,[29],['IT27']);maprows(s,[30,45],['FORMS']);maprows(s,[32],['IT36']);maprows(s,[33],['IT3','IT12']);maprows(s,range(34,38),['IT9','IT11','ARITH']);maprows(s,[44,46],['MANIFEST'])
s='jo-corporate-income-tax'
maprows(s,[2],['IT3']);maprows(s,range(4,13),['IT11']);maprows(s,[13],['IT3']);maprows(s,[14],['IT11']);maprows(s,[15,16,17],['IT12']);maprows(s,[18,19],['IT17']);maprows(s,[20],['IT3','IT4']);maprows(s,[22,23,24],['IT17']);maprows(s,[25],['IT12']);maprows(s,[26,41],['FORMS']);maprows(s,[28],['IT36','IT12']);maprows(s,[29],['IT3','TP']);maprows(s,[30,31],['IT11','ARITH']);maprows(s,[32,33],['IT9','IT11','IT4','ARITH']);maprows(s,[40,43],['MANIFEST']);maprows(s,[42],['TP'])
s='jo-payroll-social'
maprows(s,[2],['SSC3','IT12']);maprows(s,[4,5,14],['SSC59']);maprows(s,[6],['SSC24']);maprows(s,[7],['SSC42']);maprows(s,[8,9],['SSC48']);maprows(s,[10,11,12],['SSC59','SSC24','SSC42','SSC48','ARITH']);maprows(s,[13],['SSC64']);maprows(s,[15,17,38],['CAP']);maprows(s,[16,19,22],['SSC20']);maprows(s,[20,39],['REDUCTION']);maprows(s,[23],['IT12']);maprows(s,[25],['SSC20']);maprows(s,range(27,31),['SSC59','SSC24','SSC42','SSC48','SSC20','CAP','ARITH']);maprows(s,[37,40,41],['MANIFEST'])
s='jo-tax-overview'
maprows(s,[2],['IT2','IT3']);maprows(s,[4,5,6],['IT11']);maprows(s,[7],['GST6']);maprows(s,[8],['SSC3','SSC59','SSC24','SSC42','SSC48','ARITH']);maprows(s,[9,11],['IT17']);maprows(s,[12],['IT36','GSTPEN','SSC20']);maprows(s,[13],['IT12']);maprows(s,[14,15],['IT11','ARITH']);maprows(s,[16,17],['SSC3','SSC20','SSC59','SSC24','SSC42','SSC48','CAP','ARITH']);maprows(s,[24,25,26,27],['MANIFEST'])
s='jordan-gst'
maprows(s,[2],['GSTREG']);maprows(s,[4],['FORMS','GST6']);maprows(s,[6],['GST6']);maprows(s,[7,8,35],['GST7']);maprows(s,[9,49,50],['RATES']);maprows(s,[10,11],['GSTREG']);maprows(s,[12],['GSTREF']);maprows(s,[13],['GSTBASE']);maprows(s,[14],['GSTINPUT']);maprows(s,[15],['GST6','GSTINPUT','GSTSERVICE']);maprows(s,range(26,32),['GSTFILE']);maprows(s,[33],['GSTPEN']);maprows(s,[34],['GSTREF']);maprows(s,[36,37],['GST6','ARITH']);maprows(s,[38,39],['GSTPEN','ARITH']);maprows(s,[48,52],['MANIFEST']);maprows(s,[51],['FORMS'])
F=[
 {'id':'JR01','priority':'P1','rows':['jo-income-tax:C032','jo-corporate-income-tax:C028','jo-tax-overview:C012'],'problem':'Article36(b) requires both timely filing and payment of the tax declared. The personal Guide states only timely filing. The other two penalty summaries omit this scoped exception.','fix':'Say: If the return and the declared tax were both filed/paid on time and the later difference is no more than JOD5,000, the late charge on the difference runs from notification of the audit decision; above that, art.36(a) applies. Keep the currentness hold. Make the other summaries carry or explicitly cross-reference these conditions.','evidence':['IT36']},
 {'id':'JR02','priority':'P1','rows':['jordan-gst:C015'],'problem':'Imported-service timing loses both partial-payment/service triggers and their proportional limits.','fix':'State one month from paying the service fee or any part, to the extent relating to that part; customs release of the item carrying the service; or six months from receiving the service or any part, to the extent relating to that part, whichever applies first. Preserve Director-approved deferral and currentness hold.','evidence':['GSTSERVICE']},
 {'id':'JR03','priority':'P1','rows':['jo-tax-overview:C002','jo-tax-overview:C008','jo-tax-overview:C012'],'problem':'Overview says foreign income is taxed only when funded from Jordan, omitting art.3(c)(2) foreign-branch income. Its social-security headline omits ordinary full-coverage scope, and1% monthly interest omits the art.19(a)(2)60-day-from-employment condition.','fix':'Include the foreign-branch route with audited final statements, or expressly limit the sentence to resident individuals. Put ordinary full-coverage employment beside14.25%/7.5%. Add the60-day source condition and distinguish source-baseline interest from a current assessment.','evidence':['IT3','SSC3','SSC20']},
 {'id':'JR04','priority':'P1','rows':['jo-income-tax:C019','jo-corporate-income-tax:C016'],'problem':'Interest/deposit withholding rows omit the taxable-income qualification and domestic bank/financial-company payer condition; corporate row also omits interbank and designated-recipient exceptions. These are explicit neighbors in art.12(a)(2).','fix':'Restrict the rows to taxable interest/commissions/qualifying deposit profits paid by banks and financial companies in Jordan; carry the interbank and executive-instruction exclusions beside the corporate figure or state that entitlement remains held until the full exclusion check is made. Preserve finality distinctions.','evidence':['IT12']},
 {'id':'JR05','priority':'P1','rows':['jordan-gst:C004','jordan-gst:C008','jordan-gst:C012','jordan-gst:C014','jordan-gst:C015'],'problem':'Some GST positive legal extracts exceed the actually readable evidence: special tax computed first has no supporting clause here; no input in the exempt row is not proved by a schedule-list title; purchases/imports and pre-registration deduction clauses are truncated. The Guide asserts deduction art.19 and refund art.20(d) although the author ledger explicitly says these article numbers were not established.','fix':'Read and quote complete official clauses and establish the article numbers, or move the unsupported portion/number to an explicit hold. Retain the readable sales-return and bad-debt material, and the50-500 nonresident departure refund amounts as conditional clause extracts with an article-number hold. Do not clear positive input entitlement using damaged OCR.','evidence':['GSTINPUT','GSTREF','GST7','GST6']},
 {'id':'JR06','priority':'P2','rows':['jo-corporate-income-tax:C008','jo-corporate-income-tax:C009','jo-corporate-income-tax:C010','jo-corporate-income-tax:C011','jo-corporate-income-tax:C024','jo-tax-overview:C006'],'problem':'National-contribution cessation in art.11(g) applies to all art.11(f), but only the other-companies row states it. The half-year advance due-date row omits the express executive-instruction longer-period exception.','fix':'Use a common note beside all national-contribution rows/headline stating art.11(g) applies to every rate and its actual trigger is not cleared. Add unless executive instructions allow a longer period to the advance deadline.','evidence':['IT11','IT17']},
 {'id':'JR07','priority':'P2','rows':[], 'problem':'The author ledger is not yet a complete figure ledger: several legal rows use NONE; some multi-rule rows cite only an unrelated clause, and payroll Regulation45 source rowC039 cites IncomeTax art.3. Arithmetic/source-read rows are mixed with legal holdings.','fix':'Replace heuristic mappings with all the actual relevant source/quote IDs for each legal proposition, including operative source-baseline conditions. At minimum repair incomeC021/C026/C030/C031/C033; corporateC020/C023/C026/C029/C032; payrollC002/C010-C012/C023/C025/C029/C039; overviewC002/C005-C008/C012/C016; GSTC002/C004/C008/C009/C012-C015/C033. A source table/header/investigation prompt may remain NONE; an assertion of legal entitlement/rate cannot. Add source records for forms, TP, Regulation45 and the fresh MOIN failed-check research.','evidence':['MANIFEST']}
]
ledger_repairs={'jo-income-tax':[21,26,30,31,33],'jo-corporate-income-tax':[20,23,26,29,32],'jo-payroll-social':[2,10,11,12,23,25,29,39],'jo-tax-overview':[2,5,6,7,8,12,16],'jordan-gst':[2,4,8,9,12,13,14,15,33]}
F[-1]['rows']=[s+':C'+str(n).zfill(3) for s,ns in ledger_repairs.items() for n in ns]
Fmap=collections.defaultdict(list)
for f in F:
 for r in f['rows']:Fmap[r].append(f['id'])
rows=[];oldrows=[];coverage=[]
for p in sorted((R/'ledgers').glob('*.md')):
 slug=p.stem;txt=p.read_text();guide='skills/jordan/'+slug+'.md';old=git(BASE,guide);oldlines=old.splitlines();seen=[]
 for l in txt.splitlines():
  if l.startswith('| C'):
   cells=l.split(' | ');cid=cells[0][2:];claim=cells[1].replace('\\|','|').replace('<br>','\n');refs,note=M.get((slug,cid),([],''));key=slug+':'+cid;all_issues=Fmap.get(key,[]);issues=[v for v in all_issues if v!='JR07']
   if slug=='jo-company-formation':verdict='inherited_2025_hold_not_verified';note='Byte-identical to base and original PR head; no company-law primary reading claimed. README expressly holds whole Guide.'
   elif issues:verdict='correction_required';note='; '.join(issues)
   elif refs:verdict='supported_conditional_baseline';note=note or 'Checked against complete available clause and neighbors. Not a2026-currentness or filing clearance.'
   else:verdict='safeguard_structure_or_explicit_hold';note='Read as navigation, table structure, evidence-gathering prompt, non-legal working-paper instruction, or expressly unresolved matter. No legal verification asserted.'
   if '```oa-check' in claim and not issues:verdict='arithmetic_pass_conditional_inputs'
   rows.append({'guide':slug,'row':cid,'claim_sha256':hashlib.sha256(claim.encode()).hexdigest(),'claim':claim,'verdict':verdict,'evidence_refs':refs,'finding_ids':issues,'note':note,'author_evidence':cells[2]})
  elif re.match(r'^\| \d+ \|',l):
   cells=l.split(' | ');n=int(cells[0][2:]);seen.append(n);raw=oldlines[n-1];h=re.search(r'`([a-f0-9]{64})`',cells[-2]).group(1);shown=cells[1].replace('\\|','|').replace('<br>','\n')
   oldrows.append({'guide':slug,'base_line':n,'line_sha256':h,'identity_pass':hashlib.sha256(raw.encode()).hexdigest()==h and raw==shown,'verdict':'historical_identity_pass_destination_spotchecked_separately','destination':cells[-1].rstrip(' |')})
 body_start=next(i for i,l in enumerate(oldlines,1) if i>1 and l=='---')
 body_end=next(i for i,l in enumerate(oldlines,1) if '<!-- openaccountants-cta-block -->' in l)
 expected=[i for i in range(body_start+1,body_end) if oldlines[i-1].strip()]
 coverage.append({'guide':slug,'all_nonblank_base_body_lines_enumerated':expected==seen,'current_rows':sum(v['guide']==slug for v in rows),'old_rows':len(seen)})
for v in rows:
 v['current_text_identity_pass']=v['claim'].split(': ',1)[1] in git(HEAD,'skills/jordan/'+v['guide']+'.md')
 v['ledger_evidence_correction_requested']=v['guide']+':'+v['row'] in F[-1]['rows']
 if v['ledger_evidence_correction_requested']:v['finding_ids'].append('JR07')
out={'reviewer':'Fresh independent Codex reviewer; did not author the Guides','read_date':'2026-11-01','inspected_head':HEAD,'merge_base':BASE,'original_pr_head':ORIG,'verdict':'changes_requested','scope':'Conditional source-baseline partial pack; no2026 operative-law clearance','evidence_groups':E,'findings':F,'counts':{'current_rows':len(rows),'old_rows':len(oldrows),'current_verdicts':dict(collections.Counter(v['verdict'] for v in rows)),'old_identity_failures':sum(not v['identity_pass'] for v in oldrows),'current_text_identity_failures':sum(not v['current_text_identity_pass'] for v in rows),'ledger_evidence_correction_rows':len(F[-1]['rows'])},'coverage':coverage,'current_row_verdicts':rows,'old_row_verdicts':oldrows}
(R/'independent-row-verdicts.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(R/'independent-correction-requests.json').write_text(json.dumps({'head':HEAD,'findings':F},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out['counts'],indent=2));print(json.dumps(coverage,indent=2))
