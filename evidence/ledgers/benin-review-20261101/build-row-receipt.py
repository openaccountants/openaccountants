from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
notes={
'bj-company-formation':[
'SARL scope, freely chosen capital and signed 26 March date agree with decree arts. 1, 6, 11; commencement is 5 May 2014.',
'Private instruments are expressly permitted; official APIEx page also offers notarised SARL instruments.',
'Authorised bank/credit/microfinance deposit, company-in-formation account, receipt and statute notation match decree arts. 7–8.',
'AUSCGIE 309 supports one or multiple associates and liability limited to contributions.',
'311-1 requires full subscription, full in-kind payment, half cash at subscription and balance within two years after RCCM.',
'387–389 support 10m fully subscribed capital, one-quarter cash paid and three-year remainder; no public-offering case is computed.',
'376 uses two of three strictly-over thresholds: 125m balance sheet, 250m turnover, 50 permanent staff; judicial one-tenth route confirmed.',
'694 requires one or more statutory auditors for every SA; formation packet does not claim a completed appointment.',
'Fresh APIEx company/prices pages match 22,000/37,000 FCFA, notary exclusion and three working hours after complete submission.',
'Company page expressly lists packet items and mandatory SA/SAS notary; live foreign/in-kind validation stays open.',
'Public process and certificate pages support six stages, RCCM/IFU/CNSS/DGT/legal outputs and DGI-assigned IFU; no live receipt asserted.',
'140 supports annual accounts meeting within six months; RCCM filing procedure is explicitly unresolved.',
'CGI 50(1)(a) requires applicable OHADA annual statements with sector-framework exceptions; guide preserves that limitation.',
'Independent arithmetic: SARL 2m × 1/2 + 22,000 = 1,022,000; SA 10m × 1/4 + 37,000 = 2,537,000. Capital is kept separate from fees.'
],
'bj-corporate-income-tax':[
'CGI 3 form charge confirmed for SA/SAS/SARL; CGI 4 and 145–146 exemptions/incentives screened before ordinary example.',
'CGI 5 includes Benin enterprises and treaty allocations; resident entity and PE limbs plus attribution are not reduced to a universal slogan.',
'46 confirms 30% residual, 25% industrial excluding extractive and listed private schools; mining/petroleum convention cannot undercut ordinary rate.',
'47 confirms 1/3/10% produits encaissables minima, 250,000 floor, vehicle/regulatory and 0.60/litre exception, plus separate 4,000 March levy.',
'43 fifth following exercise confirmed; proof, unused deficit, same enterprise and special restrictions are retained by reference, not a blanket carryforward.',
'20(1)(a)–(g) deduction conditions checked including effective charge, evidence and payment of applicable withholding; net profit is correctly also sourced to 9.',
'36 non-deductibility covers transactions, fines, confiscation, penalties and sanctions within its listed laws/regulations.',
'8 calendar close and school/creation exceptions confirmed; Guide does not compute unresolved first-period election.',
'49 confirms 30 April annual result declaration for preceding exercise, including derogatory regimes.',
'50 full attachment provisions read; Guide describes a preparation list, preserving regulated-sector framework limitation.',
'51 four quarter instalments due 10 March/June/September/December, provisional penultimate-year first instalment, second reconciliation and tax-credit excess confirmed.',
'52 application/authorisation route confirmed; no unilateral instalment reduction is instructed.',
'145–146 art-trading/new-company/incentive rules read and expressly excluded from ordinary examples; no unqualified ordinary-rate claim for them.',
'Independent arithmetic: 10m × 30%=3m beats 1m minimum; 100k ×30%=30k, 20m ×1%=200k, floor 250k wins. Separate totals 3,004,000/254,000.'
],
'bj-cross-border-withholding':[
'141 requires non-residence, no Benin PE and supplied/used-in-Benin service; Guide preserves all three.',
'86 confirms 5% nonresident-associate/qualifying approved-listed dividends, 10% other dividends and 15% residual securities income; bonds excluded from residual opening scope.',
'88 confirms 15% claim/deposit/guarantee interest; 85(1) gross base and 89 treaty condition also read.',
'89 requires lower applicable treaty rate, beneficial ownership and non-exempt income; Guide holds treaty determination pending actual text.',
'142 confirms 20%, accessory costs, treaty residence/beneficial-owner/non-exempt tax evidence, monthly communication and separately invoiced goods exclusion.',
'141 final sentence expressly exempts artistic/cultural services from this retention, not from every tax.',
'REPAIR F2: 85(2) makes interest tax due on payment OR debit/credit accounting entry even unpaid. Guide records dates but never states the second operative trigger.',
'LFR 1 and 3–7 read with signed scans; retained-profit, base, credit, deadline and transitional issues are explicitly held, and 2025 income-period rule is not inferred from signature.',
'LFR 12 adds Benin-enterprise securities gains irrespective of seller/buyer residence, treaty reservation retained; no unsupported gain computation supplied.',
'LFR 13 adds short/long accommodation reservation and rent collection for Benin property, hotel exclusion and platform-owner withholding; no rental base/rate guessed.',
'LFR 6 confirms ordinary next-month/approved-meeting limbs and separate retained-profit date; ordinary-interest accounting trigger needs F2 completion.',
'91(2) supports accompanying monthly gross sums and tax statement; no authenticated field IDs are invented.',
'143 confirms next month after expense recognition, not cash alone, plus debtor/billing-or-collection/provider solidarity.',
'492(3)–(4) confirms underlying remittance plus 100% fine, halved at first failure, extends to 143 persons; general sanctions stay distinct.',
'1 treaty priority is conditional on regularly ratified convention; no complete treaty inventory or named-country entitlement is claimed.',
'Independent arithmetic: 1m ×5%=50k vs10%=100k; services1m ×20%=200k versus unsplit5m ×20%=1m; difference800k. Assumptions exclude unresolved special cases.'
],
'bj-income-tax':[
'119 salary/accessory, end-career and IS-manager charge confirmed; 54 confirms separate business-income chapter.',
'121 connecting factors and permanent-home/vital-interest/183-day fallback verified, including twelve-month continuous or non-continuous presence.',
'125 five monthly bands 0/10/15/19/30% at 60k/150k/250k/500k confirmed in text and rendered pages.',
'125 March1,000/June3,000 levy confirmed; exemption expressly covers 3,000 June levy where income does not exceed first band.',
'122 gross pay including transport and sickness indemnities confirmed; no generic expense deduction inserted.',
'120 statutory dismissal exception and capped private-sector family allowances confirmed; legacy family quotient withheld.',
'123 actual-value default and monthly forfait table independently read/visually checked; Guide explicitly holds live benefit valuation.',
'124 training/collective and individual insurance exclusions read; individual80% condition not replaced by blanket exemption.',
'126 exceptional-pay classes, twelve-month average method and25% special abatement read; Guide routes to separate calculation, not ordinary example.',
'127 payer record and labour-law payslip notation confirmed.',
'128 Benin-established payer deduction, foreign-payer resident spontaneous monthly declaration and finality confirmed.',
'129 monthly remittance by10th of following month confirmed; authenticated form unresolved.',
'472 annual salary statement due30April and foreign/diplomatic payer branches confirmed; not described as universal annual IRPP.',
'Independent arithmetic: 200k gives9k+7.5k=16.5k;600k gives9k+15k+47.5k+30k=101.5k;June3k yields104.5k.'
],
'bj-payroll-social':[
'191 employer/payer charge covers salaries and accessory remuneration; no employee deduction of VPS instructed.',
'192 all seven exemption categories and final nonprofit limitation read; Guide uses supported evidence and does not exempt all nonprofits.',
'192(4) Beninese first-employment two-year condition from hiring plus CNSS declaration confirmed; first-exercise employer exemption is distinct.',
'193 same base as salary ITS confirmed; not unclassified gross payroll.',
'194 ordinary4% and private-teaching2% confirmed.',
'195 same declaration and127–129 payment terms confirmed; no tax deadline is copied into unresolved CNSS.',
'Independent arithmetic:2m ×4%=80k; school(2m−500k)×2%=30k versus40k without supported exemption;10k difference. CNSS not calculated.'
],
'bj-tax-overview':[
'1 law/treaty basis and chapter map verified against CGI headings/charges; no generic annual personal-income computation inferred.',
'5 company territorial/allocation test read; not interchanged with121 salary residence.',
'121 separate salary domicile hierarchy confirmed.',
'8 ordinary calendar close plus school/first-period exceptions confirmed.',
'Signed LFR1 explicitly ties income measures to exercise closed31December2025 unless otherwise specified; June signature not treated as commencement for every measure.',
'485 confirms20%,40% notice/two-month alternatives and integrated interest; Guide stops before case penalty assessment.',
'487 confirms10% unpaid/deferred principal and instalments; no multiplication by months.',
'488 confirms0.25% per month/fraction, following-month start, principal base/cap;485 integration caveat retained.',
'Signed LF3 confirms2026 first spontaneous prior-year declarations, full payment and absence of current control/investigation; not general current-return amnesty.',
'252 excess eligible VAT credit carries forward without time limit; supporting deduction/period conditions remain prerequisite.',
'263(5) withholding belongs in declaration deductions for collection month; valid receipt and period assumed in illustration.',
'Independent arithmetic:1m+180k+16.5k+8k=1,204,500;500k−100k−50k=350k; unsupported150k would create200k comparison and150k understatement.'
],
'bj-transfer-pricing':[
'45 arm’s-length transfer, majority/legal/actual/common control and privileged-regime exception confirmed; no reporting-threshold pricing safe harbour.',
'30 privileged-tax definition is untaxed or more-than-half lower Benin equivalent tax, with real/non-excessive expense proof; Guide references actual test.',
'470 own turnover OR gross assets≥1bn and cross-border control, electronic30April return confirmed.',
'543 own≥1bn OR majority parent/subsidiary threshold tests at close confirmed; group/entity documentation not substitute for primary records.',
'471(1) all three ultimate-parent/consolidation/492bn prior-year conditions confirmed, not every local company.',
'47112-month electronic deadline and paragraphs2–4 secondary/designation/systemic-failure branches read; unverified exchange list explicitly held.',
'542 thirty-day response, reasoned extension≤45total and eight-day insufficient-response notice confirmed.',
'543(4) eight-day formal-notice completion rule confirmed, separate from542 request.',
'496(6) genuinely names TP declaration but references471; Guide withholds exact annual-return fixed fine instead of silently repairing law.',
'REPAIR F3: signed LFR17 supports2/4months and possible4month extension/three-day reasoned notice, but Guide omits statutory any-tax/any-year-under-audit including current-year turnover definition.',
'Independent arithmetic:1,000×12,000=12m versus1,000×10,000=10m;2m candidate addback. Comparable assumed supported, not a legal safe harbour.',
'Independent arithmetic:1bn−900m=100m shortfall,1.2bn−1bn=200m excess; own-assets limb alone meets470, no aggregation.'
],
'bj-vat-gst':[
'223–224 economic independent scope, e-commerce supply and commission charge confirmed; monthlyjob limited to confirmed VAT status.',
'225 option eligibility/express application/effective date/evidence provisions read; unresolved status decisions held.',
'226 continuing obligations for three consecutive exercises after falling below threshold confirmed; no immediate de-registration advice.',
'228 delegates numerical threshold to ministerial order; old50m is expressly unverified, not used to register.',
'229 listed food/origin, books/newspapers advertising exclusion, medical/education, TAFA, agriculture and domestic-gas conditions checked; no blanket sector exemption.',
'230 zero-rate applies export goods and enumerated assimilated cases with243+ input conditions; not every foreign invoice.',
'241 ordinary18% confirmed.',
'237 ordinary consideration and import customs-related base;240 actual documented reductions/exact disbursements read; special margins/public contracts held.',
'233–236 goods/service place, generating event versus collection exigibility, non-import advances and invoice cap checked; paragraph correctly distinguishes them.',
'244 normalised invoice/import-payment/self-supply/withholding documents, necessary recorded business use and liable-supplier condition confirmed.',
'245 deduction timing, omission deadline30April next year and≥100k exVAT cheque/card/bank-transfer requirement confirmed. Law links payment failure to503 sanctions, not automatic loss of deduction.',
'247 and signed LF16 confirm machinery-fuel exclusions and BTP90% invoice VAT limit; passenger/tourism fuel not treated as eligible.',
'248 direct allocation and249 common-input fraction/provisional ratio/upward rounding/30April regularisation confirmed.',
'252 unlimited future-period eligible credit and253 conditional refunds confirmed; no automatic refund assumption.',
'254 normal deadline and signed LF17 exceptional30April next exercise fallback verified; Guide references conditions/time limits and does not certify claim.',
'259 monthly declaration and tax payment by10th following month confirmed.',
'260 invoicing VAT creates liability by fact of invoicing confirmed; wrong invoice not harmless.',
'262 nonresident representative or default recipient/billing/collection VAT+penalty liability confirmed; place test still required.',
'258 platform supply/commission collection/remittance and registration separate from234 place rule confirmed.',
'Signed LFR14 three place limbs confirmed, including any specified Benin participant for commission, beneficiary residence and property location.',
'Signed LF12 permanent-from1January2026 motorcycle/battery/charging scope and delegated goods list read;LF13 separate levies preserved.',
'Signed LF7 limited2026 domestic-gas cylinder/accessory relief read; separate229(17) domestic gas exemption not confused with goods relief.',
'496(2) nil/credit VAT late declaration50k per month/fraction capped500k confirmed.',
'Independent arithmetic:10m×18%=1.8m−720k=1.08m;BTP180k×90%=162k and18k excluded/overstatement. Eligibility assumed evidenced.'
]}
lines=['# Benin independent ledger-row disposition, 1 November 2026','','Every numbered row below was compared with the actual cited official text and its surrounding conditions. Official PDF byte provenance is independently verified in `source-verification-network.json`; fresh native extraction matches in `text-extraction.json`. LFR/LF/decree critical scans were visually read. This is 113 rule/example ledger rows, not 113 distinct numeric rates and not a whole-country certification.','','| Ledger | Row | Result | Independent check | Act / article | Official URL |','|---|---:|---|---|---|---|']
count=0
for slug,ns in notes.items():
 rows=[l for l in (ROOT/'evidence/ledgers'/f'{slug}.md').read_text().splitlines() if re.match(r'^\| \d+ \|',l)]
 assert len(rows)==len(ns),(slug,len(rows),len(ns))
 for row,note in zip(rows,ns):
  cells=[x.strip() for x in row.split('|')];result='Repair F2' if 'REPAIR F2' in note else 'Repair F3' if 'REPAIR F3' in note else 'Checked within scope'
  lines.append(f'| {slug} | {cells[1]} | {result} | {note} | {cells[4]} | {cells[5]} |');count+=1
lines+=['',f'Rows checked: {count}. Two rows require narrow condition/trigger repairs (XB row 7, TP row 10). The ordinary-deadline XB row 11 must be read with the same F2 repair. Remaining numeric/rule content was supported within the stated preparation boundaries; all eight descriptions separately fail required length.']
assert count==113
(HERE/'row-checks.md').write_text('\n'.join(lines)+'\n')
print(f'Wrote {count} independent row dispositions')
