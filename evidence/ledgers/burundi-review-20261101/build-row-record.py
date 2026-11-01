from pathlib import Path
import re
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
notes={
'bi-tax-overview':[
'OBR/ADB allocation checked against July art. 233; INSS role cross-checked against official INSS pages.',
'IR arts. 16–18 and 21: calendar year, eligible entity alternative-year permission and BIF confirmed.',
'Modified-budget final art. 252 independently read in separately captured physical PDF p. 249.',
'July-budget final art. 277 independently read in separately captured physical PDF p. 267.',
'Each substantive route checked against the corresponding actual sibling; no new rate inferred.',
'Current OBR public portal page independently opened: medium/large and small/micro URLs match.',
'Entire published adhesion manual read: NIF/Extranet, administrator authority, uploads and two-email sequence match.',
'Procedure arts. 9, 27 and 32 support next-working-day rule, conditional single 30-day extension and local 10-year records; physical locators need F5 correction.',
'Actual linked Espace Connecte title/content is a bank console manual; correctly excluded as taxpayer submission proof.',
'INSS official declaration page independently confirms quarterly employer and monthly voluntary schedules.',
'Procedure arts. 126, 130, 131 and 142 read with adjacent provisions; fixed class fines, payment fine, withholding fine and interest formula match; no current rate invented.'
],
'bi-income-tax':[
'IR arts. 19–23 confirm separate categories and resident worldwide/nonresident source scope.',
'Annual table and following business paragraphs read; 0/20/30 annual scale, nearest-thousand rounding and business minimum confirmed. Full art. 21 extends onto p. 13.',
'Modified-budget art. 180 and neighboring art. 181 read: equality at 25m, quarterly 1%, over-threshold annual/bookkeeping switch confirmed.',
'July art. 190 retains the same inclusive threshold and annual switch in its second paragraph.',
'IR art. 23 confirms individual 15% second-category rule, including express art. 37(2) reference; physical locator needs F5 correction.',
'IR art. 37 and common base/depreciation/loss provisions read. Imported corporate expense method misses the budget EBMS override: F1.',
'IR arts. 47–48: agriculture/livestock/fish farming exempt, actual fishing gross receipts at most 20m, proof and transformation exclusions confirmed.',
'IR arts. 84 and 87: restricted 4.8m vulnerable-person allowance, 40% ordinary rental deduction, paid loan interest, separate sublet rent-paid deduction confirmed.',
'Modified-budget art. 208: two years from first letting; subletting excluded.',
'July art. 227 carries forward the same new-building condition and sublet exclusion.',
'Modified-budget arts. 80–81: market/land allocation and narrower building-base text read; first-half interaction expressly unresolved.',
'July arts. 79–80: land expressly in rental base; lease-copy and specified A/B traceable payments confirmed.',
'IR arts. 88–93 and 123: individual gain base separated from nonresident gross-price withholding. Detailed valuation and relief remain expressly incomplete.',
'IR arts. 24–26: annual third-month rule, quarterly frequency and source-taxed-only return exemption read; no complete quarterly due-day inferred.',
'Modified-budget rental arts. 79 and 82: following-year March 31 return and September 30 advance of at least quarter prior assessed tax confirmed.',
'July rental arts. 78 and 81 retain same return and minimum advance rules.',
'Actual four-page annual individual form checked: products 1–11, expenses 12–22, bridge 24–27, tax 28/29, credits 32–36 and balance 37 match.',
'Actual two-page quarterly form checked: turnover/rate/tax columns, withheld credits, balance, signature and receipt fields match.'
],
'bi-corporate-income-tax':[
'IR arts. 4 and 94–104 confirm entity residence, resident worldwide/PE scope, and separate rental scale under art. 103.',
'Modified-budget commencement confirmed from actual final art. 252, not inferred from fiscal-year title.',
'July-budget commencement confirmed from actual final art. 277.',
'IR art. 103 p. 34 independently read visually: 30%, nearest thousand, 1% minimum below turnover/30 and first-ten-year free-zone exception confirmed.',
'IR arts. 77–80: five subsequent years, FIFO, at least 25% unlisted capital/vote change, filed-return requirement and foreign-loss restriction confirmed.',
'July art. 218: approved Burundi market listing and public capital percentages for 28/25/20 rates confirmed; no first-half concession inferred.',
'IR arts. 37, 54–55 and 98 support base and corporate gains, but budgets add omitted ordinary EBMS disallowance: F1.',
'IR arts. 59–68: nondepreciable land, straight-line 5/10 rates, computer and other pools 50/25, 500k full deduction and negative-pool recapture confirmed.',
'Modified-budget art. 83 read: minutes absence deemed distribution and two-successive-year carryforward/free-reserve wording confirmed.',
'July arts. 82, 157 and 215 read: broader allocation text, related financing and incentive restrictions correctly routed/limited.',
'IR arts. 16–18 and 104: eligible alternative year, third-month return and medium/large certification confirmed.',
'Procedure arts. 29–30 read: annual schedules support statement, but additional 30-day valued stock-inventory filing omitted: F3.',
'Actual corporate form pages/annexes checked: lines 1–23, annex 1 addbacks, annex 2 losses, evidence credits and acknowledgment/quittance match.',
'IR arts. 130–133: June/Sept/Dec 25% advances, half-year/quarter withholding, fiscal credit and alternative-year/first-partial-year rules confirmed.',
'Published adhesion manual matches NIF/Extranet/authority and activation; actual current URLs checked separately.',
'IR arts. 108–109: separate PE books, independent-enterprise attribution and foreign head-office administration denial confirmed.'
],
'bi-payroll-social':[
'IR employment and employer sections read; actual principal/secondary/casual/termination status controls the rule.',
'Actual three-page April 2026 law read: public-sector/prior pension benefit reform, not replacement ordinary contribution rates.',
'IR arts. 117–119 table p. 39 independently read visually: monthly 0/20/30, secondary 30 and qualifying termination 5/10/15 confirmed.',
'Official INSS current calculation page independently opened; 6% employer/4% employee and 450k pension cap, separate 3%/80k risk branch confirmed.',
'Modified-budget art. 100: employer foreign-labor 4%, annual gross, contract-visa date and March 31 deadline confirmed.',
'July art. 103 retains same annual employer foreign-labor charge and deadline.',
'IR arts. 30–34 read with budget replacement: permitted exclusions, actual employee contributions, 15/60 basic-salary allowances and 20% complementary limit confirmed.',
'Official INSS base/example read: housing/transport etc included, family allowance/reimbursements excluded, applicable minimum-salary floor confirmed.',
'IR arts. 112–116: monthly fifteenth-day return/remittance/payslip and 30-day annual individual recap/regularisation, self-declaring employee condition confirmed.',
'Modified-budget art. 147 replaces employment definition and requires three-month advance cessation/contract notice; no old one-month-after rule carried forward.',
'July art. 155 retains same advance notice wording.',
'Actual monthly form section III read. Principal/casual/secondary/termination blocks match, but 9–11 pension rows incorrectly labeled political/public office: F2.',
'INSS declaration page independently opened: quarterly Modèle VI and first fifteen following-month days; voluntary monthly exception confirmed.',
'Actual attached Q3 2026 notice visually read: employer, affiliation, quarter and attached payment identification confirmed.',
'INSS declaration page independently opened: separate 1.5% declaration and 1.5% payment additions per month/part confirmed.'
],
'bi-vat-gst':[
'VAT arts. 2–10 and 54 support territorial/remote service and recipient duty; claimed exact remote-service phrase is paraphrase: F5.',
'VAT art. 19 entire rate section read: ordinary 18, restricted intermediate 10 and specified zero categories confirmed.',
'Actual 2021 gazette art. 4 read: first-half compulsory strictly greater than 100m, voluntary 5m confirmed.',
'Modified-budget art. 246: separate purchases/imports and stock strictly greater than 100m trigger confirmed.',
'July art. 271 p. 66 independently read visually: inclusive 25m turnover, strict 50m purchase/stock, exclusions, first-next-month invoicing confirmed.',
'VAT arts. 40–42: independent economic activity, threshold, complete books, stable address, prior compliance and acceptance/date conditions confirmed.',
'VAT arts. 10 and 19 read: medical/medicine/education conditional exemptions are distinct from intermediate lists.',
'Actual gazette arts. 9–28 and annexes checked for stated classification/refund claims; 15m ordinary refund minimum and special categories confirmed, subsequent-order limitation retained.',
'July sector arts. 210 and 220–223 read: separately conditioned seeds/electric/hybrid/energy/cooking scope; no blanket operational exemption asserted.',
'VAT arts. 11–18: delivery/service receipt, approved invoice option, related-party exceptions and tax-exclusive/customs/incidental base confirmed.',
'Modified-budget arts. 96–98: State receipt, collected-tax check, cooperation and EBMS condition confirmed.',
'July arts. 98–101: same check/EBMS conditions plus invoice above 500k traceability confirmed.',
'VAT arts. 20–23 support taxable-use recovery and blocked inputs; claimed exact operations adjective differs from actual art. 20: F5.',
'Modified-budget art. 98: three credit periods, next-month request, minimum carry exception, no unrestricted later carry and preserved art. 33 claim right confirmed.',
'July art. 101 retains credit sequence and restrictions; no indefinite carry invented.',
'VAT arts. 37–42 and July art. 271 read: threshold exceptions, application by next-month fifteenth and published invoicing rule; already-over-threshold July transition explicitly unresolved.',
'VAT arts. 25–33, 51–54 read: monthly declaration/payment, request/refund/retention and correction duties. Authenticated completion expressly incomplete.',
'July procedure override art. 259: one pre-audit correction per declaration confirmed.',
'Actual monthly form section I pp. 1–2 checked: output 1–9, inputs 10–16, net/credit 17–18, carry/refund 19–21 and due 22 match.',
'VAT arts. 59–61 visually checked p. 22. Rates mostly match, but post-90-day further-month/part convention unsupported: F4.',
'VAT arts. 45–46 and 54: unrepresented nonresident services, taxable or unregistered recipient, any amount, representative alternative confirmed.'
],
'bi-company-formation':[
'National 2011 company code general/forms provisions read: ordinary SPRL/SU/SA, capacity and legal/natural founders confirmed; OHADA assertion not retained.',
'Company arts. 13–14 confirm branch personality/registration distinction; physical locator p. 3 is wrong: F5.',
'Company arts. 225–229 confirm 2–50, one-year regularisation, freely set capital, full subscription, at least one-third payment and two-year balance.',
'Company arts. 270–273 confirm single natural/legal member, freely set fully paid capital and prohibition on SU creating another SU.',
'Actual fee notice and independently opened current ADB page confirm company 200k, individual 100k, amendment 50k and duplicate 15k.',
'Procedure art. 17 confirms 15 calendar days from activity/creation, subject to budget competence; physical locator p. 6 is wrong: F5.',
'Company general provisions confirm articles/geographic seat/capital/bank/in-kind conditions; exact quote belongs to different SU provision and locator must be aligned: F5.',
'Company art. 236 permits natural/legal SPRL managers, while art. 278 requires natural SU manager. Legal-person SPRL manager needs natural permanent representative under adjacent text.',
'Actual ADB document/account path independently opened; substance matches but quoted foreign-company phrase absent: F5.',
'Modified-budget art. 213 confirms ADB/ANACOOP commercial and OBR exclusive NIF competence plus retained process pending module.',
'July art. 233 confirms same competence and express module transition.',
'Company general accounts and SPRL meeting sections read; Guide routes compliance without inventing a completion promise.'
],
'bi-transfer-pricing':[
'IR art. 57 read fully: foreign dependency/common control, majority/actual decision power and privileged/noncooperative override confirmed.',
'IR art. 2 read: general linked-person 25% direct/indirect participation/votes and family/control relationships confirmed.',
'IR art. 57 imposes keep-available foreign associated transaction pricing documentation without statutory monetary exemption in this article.',
'IR art. 56 read: paid-related-interest 30% pre-interest profit limit, below-twice-adjusted-equity exception confirmed for pre-July wording.',
'July art. 157 read: paid-interest limit, unpaid-interest denial and local-market-average rate condition; old equity exception not repeated and annual cutover remains unresolved.',
'IR arts. 54 and 57 read: genuine deduction and pricing adjustment distinct, transfer mechanisms and written information request confirmed.',
'Actual corporate form line 11 / annex 1 interest and miscellaneous addbacks supports general annual adjustment route, not a separate TP return claim.',
'Procedure art. 32 confirms local 10-year retention; physical p. 11 locator wrong: F5.'
],
'bi-cross-border-tax':[
'IR arts. 3–5 read: permanent residence / more than 183 days in fiscal-ending 12 months and entity incorporation/effective management confirmed. Illegible diplomatic condition expressly not certified.',
'IR arts. 6–7, 20 and 100–102 confirm source rules including electronic/foreign-delivered services and worldwide/source scope.',
'IR art. 8 read: construction/assembly/supervision at least six months versus service/connected-project more than six months in any twelve confirmed.',
'Modified-budget art. 148 full replacement withholding categories and exceptions read; no blanket foreign-payment tax inferred.',
'July art. 156 core 15% categories, PE attribution and bank/State/professional-hire exceptions confirmed.',
'IR art. 123: buyer resident or nonresident, specified acquired assets from nonresident and 5% gross acquisition price confirmed.',
'IR art. 14 confirms foreign tax paid or due and attributable domestic pre-credit ceiling.',
'IR arts. 9–13 read: narrow excluded activities, dependent contracting/stock agents, ordinary independent agents, insurance rule and ownership alone distinction confirmed.',
'IR art. 15 read: assessment/certificate evidence, issuing-authority certification, supported languages/translation, return attachment and six-month fallback confirmed.',
'Actual monthly form section IV pp. 6–7: categories lines 1–6, acquisition line 9, columns 2–5 and total 15 confirmed; obsolete gaming rows excluded.',
'IR arts. 124–129 read: next-month fifteen days, PE payer, ten following fiscal years and agent liability without recovery of own penalties confirmed.',
'Actual two-page domestic Morocco ratification law/instrument read: domestic approval is not evidence of bilateral exchange.',
'Actual treaty art. 30 p. 21 independently read visually with adjacent articles: exchange and following-year withholding/other-tax effect confirmed; no rate applied.'
]}
flags={('bi-corporate-income-tax',7):'F1',('bi-income-tax',6):'F1',('bi-corporate-income-tax',12):'F3',('bi-payroll-social',12):'F2',('bi-vat-gst',20):'F4',('bi-company-formation',2):'F5',('bi-company-formation',6):'F5',('bi-company-formation',7):'F5',('bi-company-formation',9):'F5',('bi-tax-overview',8):'F5',('bi-transfer-pricing',8):'F5',('bi-income-tax',5):'F5',('bi-vat-gst',1):'F5',('bi-vat-gst',13):'F5'}
assert sum(map(len,notes.values()))==114
lines=['# Row-by-row independent source review','','Each ID refers to the physical row of the linked writer ledger, which supplies the exact official URL and article. All rows were read; a “checked” result means the stated scoped claim has primary support subject to the candidly disclosed gaps, not full domain coverage or attestation. Exceptions refer to README.md findings. Source page images were used to settle the particularly error-prone tax tables, VAT sanctions, July threshold, Q3 notice and treaty commencement. No invented claimant facts were treated as statutory figures.','']
for slug,rows in notes.items():
 ledger=ROOT/'evidence/ledgers'/f'{slug}.md'
 actual=[x for x in ledger.read_text().splitlines() if re.match(r'^\| \d+ \|',x)]
 assert len(rows)==len(actual),(slug,len(rows),len(actual))
 lines += [f'## [{slug}](../{slug}.md)','','| Row | Result | Independent check |','|---|---|---|']
 for i,n in enumerate(rows,1): lines.append(f'| {i} | {flags.get((slug,i),"Checked")} | {n} |')
 lines.append('')
lines += ['## Legacy topics and introductions','','All 65 old labeled bullets were independently matched as a multiset to the pinned base, and the actual destination/gap text was read. Groups checked: formation 1–11; corporate 12–22; individual 23–34; payroll 35–46 (including duplicated health headline); overview 47–56 (including duplicated VAT headline); VAT 57–65. All four introductory rows were also compared. The corrected old company form, old USD capital, old fee, corporate gains, blanket nonresident and agriculture rates, aggregate contributions and monthly INSS statements are either corrected with primary sources or expressly unconfirmed. No old-topic loss found. The ordinary business-base and payroll filing-route defects above are newly found defects in destinations, not silent removal of a legacy topic.','','Lost content restored: 0 by this reviewer. No deletion or retirement occurred.']
(OUT/'row-review.md').write_text('\n'.join(lines)+'\n')
print('Recorded',sum(map(len,notes.values())),'physical rows; exceptions',len(flags))
