---
name: uk-freelance-intake
description: "UK freelancer tax intake: read uploaded records, confirm missing facts and route sole-trader Self Assessment, VAT, bookkeeping, National Insurance and other income to the relevant Guides. Record company, partnership, residence and employment-status questions without deciding them from labels or arithmetic."
version: "1.0"
type: router
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# UK freelancer tax intake (2026/27)

## Scope

Collect and confirm the facts before preparing a sole trader's return. Company, partnership, umbrella and agency arrangements can be recorded here, but their classification and company-level filings need specialist review. This intake does not establish residence, employment status, a trade or relief eligibility. Obtain professional review before filing; do not file for the user.

The primary year is 2026/27, 6 April 2026 to 5 April 2027. Historical cases keep their own years: 2025/26 is 6 April 2025 to 5 April 2026. The tax year runs 6 April to 5 April ([HMRC](https://www.gov.uk/self-employed-records)). Do not apply current-year rates retrospectively.

## Ask the client first

Read all uploaded records first, then batch only missing questions. Keep the source document and tax year beside each figure. Missing means `null`, not zero; a bank description, invoice or address alone does not establish tax status. Confirm the extracted summary once and retain corrections.

- Identity, birth date, UTR, NI/VAT numbers, marital status, residence history, UK arrivals/departures, Scottish status and foreign income/gains.
- Each activity's start date, structure, partners, client/sector, contract and actual working practices, substitutes, supervision, payment terms, SDS and client-size confirmation. Record disputed status and trade-or-hobby indicators both ways.
- All business/personal bank statements, invoices/receipts, capital purchases and prior capital-allowance schedules; reconcile deposits to invoices, excluding identified transfers rather than calling all deposits turnover. Record CIS statements and deductions for review.
- Gross income by trade and property source; monthly VAT taxable turnover and future contracts; VAT registration date/scheme/periods, goods costs and first registration date for FRS; earlier returns and MTD letters/status.
- Expenses, private-use shares, vehicle type/business and total mileage, prior vehicle method, home-working hours/costs, separate/living-at-business premises, accounting method and method changes.
- P60/payslips, employment income, PAYE/Class 1 NI and loan deductions, loan plan/balance, pensions and relief method, Marriage Allowance elections, Child Benefit, savings/dividends, rent and asset/crypto disposals.
- Prior SA302/returns, HMRC statements/notices, assessed tax, tax collected at source and each payment's allocation/year; outstanding VAT periods, staff/payroll and unreported earlier years.

Keep deductions and VAT recoverability as proposed classifications until checked. Do not infer VAT registration from charged VAT or HMRC payments alone. With incomplete records, identify the specific missing evidence and continue only separable work.

## The method, step by step

1. **Classify before calculating.** Employment and self-employment can coexist ([HMRC employment status](https://www.gov.uk/employment-status/selfemployed-contractor)). Invoice wording, one client or a company registration alone settles nothing. For residence/split year, non-residence, Scottish taxpayer status, trade/hobby badges, CIS classification or disputed employment status: Check this point with one of our partner accountants. Route residence to **uk-statutory-residence-test**, foreign income/FIG/remittance history to **uk-non-dom**, and personal tax to **uk-income-tax-sa100**.

2. **Return and registration.** HMRC's sole-trader trigger is gross trading income **more than £1,000**, before relief/expenses. Partners, CGT payable, HICBC not paid through PAYE, off-payroll workers repaying loans, and an HMRC request can also require a return ([who must send one](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return)). Exactly £1,000 does not meet that sole-trader trigger; it does not establish that no return is required. Do not ignore a notice to file; ask HMRC to withdraw it if appropriate. Untaxed property, interest, dividends or foreign income needs its own filing check.

For 2025/26, tell HMRC by **5 October 2026** if a return is needed and this is the first return, or the person registered before but needed none for 2024/25 ([deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)). For later years' notification duties, late notification and penalties: Check this point with one of our partner accountants.

3. **Trading allowance.** The annual £1,000 allowance is shared across relevant trades/miscellaneous income, not reset for each business. Full relief at or below £1,000 requires relevant income, no election out and no exclusion. Above £1,000, partial relief needs an election and replaces expenses/other allowances; it cannot create a loss ([HMRC allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income); [full relief](https://www.legislation.gov.uk/ukpga/2005/5/section/783AE); [partial relief](https://www.legislation.gov.uk/ukpga/2005/5/section/783AH)).

It does not apply to partnership trading income or a rent-a-room trade. The tax-year exclusions include trade/property income from a company the person or a connected person owns/controls, a partnership where either is a partner, or their employer or their spouse/civil partner's employer ([HMRC](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income); [relevant trade](https://www.legislation.gov.uk/ukpga/2005/5/section/783AA)). Keep income records even when using the allowance. Record actual expenses as well; route to **uk-self-employment-sa103** and **uk-bookkeeping**. Property has a separate £1,000 allowance, but its eligibility, expenses/finance-cost restrictions and elections require **uk-rental-sa105**: Check this point with one of our partner accountants.

4. **VAT.** These ordinary registration tests are for a UK-established business. Taxable turnover includes zero-rated supplies; exempt/outside-scope supplies are excluded. Check the actual VAT classification, not bank receipts or customer country alone ([HMRC registration](https://www.gov.uk/register-for-vat)).

- At each month end, taxable supplies in the preceding year **over £90,000** trigger registration; exactly £90,000 does not exceed that test. Notify within 30 days after that month ends; ordinary effective date is the first day of the second month after exceeding it.
- At any time, reasonable grounds that taxable supplies in the **next 30 days alone** will exceed £90,000 trigger registration. Notify by the end of that period; effective date is when the expectation arose ([statutory tests](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1); [notification/effective dates](https://www.gov.uk/register-for-vat)).
- Route immediately to **uk-vat-return**. Non-established businesses, temporary excess/zero-rating exceptions, overseas supplies/reverse charge, voluntary registration, cancellation and late-registration consequences: Check this point with one of our partner accountants.
- Record the current scheme. FRS joining/leaving turnover bases, anniversary/forward tests, limited-cost relevant goods and period apportionment, sector rate and first-registration discount: Check this point with one of our partner accountants. Do not admit/retain a business from a threshold alone.

5. **MTD for Income Tax.** Ordinary new-entry thresholds are strictly **over £50,000 in 2024/25 → 6 April 2026; over £30,000 in 2025/26 → 6 April 2027; over £20,000 in 2026/27 → 6 April 2028** ([HMRC start dates](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax)). Exactly £50,000 does not exceed the first threshold. These tests do not alone settle exemption or an existing continuing obligation.

Generally combine relevant self-employment and property income before expenses. Employment, individual partnership profit shares, dividends, State/private pensions do not count. HMRC's original illustration is £25,000 rent + £27,000 self-employment = £52,000 ([qualifying income](https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax)). Net-only reporting, part-year annualisation (including the original 6-month illustration), amended/ceased income, exemptions, continuing duty/exit, no HMRC letter, partnerships, signup/history requirements, software/digital records, quarterly and annual submissions: Check this point with one of our partner accountants. Route to **uk-bookkeeping** before deciding a start date.

6. **National Insurance.** Record age, residence, liable profits, other employment and weeks of self-employment. Accounting profit is not automatically Class 4 liable profit. For ordinary eligible Class 2 weeks, profits at/above **£7,105 in 2026/27** are treated as paid; below it voluntary Class 2 is **£3.65 a week**. For **2025/26** the corresponding figures are **£6,845 and £3.50** ([rates](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions); [Class 2 law](https://www.legislation.gov.uk/ukpga/1992/4/section/11)). No full-year pension-credit promise follows from a profit figure.

Ordinary Class 4 in both years is 6% on liable profits above £12,570 up to £50,270, plus 2% above £50,270; none at exactly £12,570 ([Class 4 law](https://www.legislation.gov.uk/ukpga/1992/4/section/15); [rates](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions)). Pension-age/non-residence exemptions, dual-status maximum/deferment, losses/basis adjustments, voluntary payment/credits and special occupations (including examiners, landlords, ministers and investors): Check this point with one of our partner accountants. Route to **uk-national-insurance**.

7. **Payments on account.** Reconcile the relevant Income Tax/Class 4 amount after creditable tax collected at source. Exclude CGT, Class 2, SA student/postgraduate loan repayments and coded underpayments as appropriate; the total SA cash bill is not the base ([HMRC SAM1100](https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1100)). No instalments if that relevant unpaid amount is **less than £1,000**, OR **more than 80%** of the relevant assessed tax was collected outside SA. Exactly 80% fails only the percentage exemption; the £1,000 exemption must still be tested. Exactly £1,000 fails only the amount exemption ([HMRC](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).

Otherwise each advance is half the preceding year's relevant amount, due 31 January within the tax year and the following 31 July ([TMA s59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A)). A first filer may owe the balance plus the next year's first advance on the same January date. Route to **uk-payments-on-account**; reductions, unusual assessments/allocations and payment plans: Check this point with one of our partner accountants.

8. **Records and handoff.** Keep sole-trader records at least five years after the relevant 31 January submission deadline, longer where the enquiry window/enquiry requires it ([HMRC](https://www.gov.uk/self-employed-records/how-long-to-keep-your-records); [TMA s12B](https://www.legislation.gov.uk/ukpga/1970/9/section/12B)). Replace lost records if possible; otherwise use best figures, disclose estimates/provisional figures and supply actual figures when available. Late-return retention extensions or record penalties: Check this point with one of our partner accountants.

Hand the confirmed package to **uk-return-assembly**: taxpayer/classification evidence, dated income by source, proposed expense/capital/private-use treatment, VAT/FRS/MTD status, loan/pension/Marriage Allowance fields, prior-year calculations and allocated payments, documents and unresolved flags. Keep every unknown as `null`; name the Guide/accountant needed to close each flag. **uk-self-employment-sa103** handles trade pages; **uk-income-tax-sa100** personal tax, savings/dividends/Child Benefit and filing; **uk-rental-sa105** rent; **uk-capital-gains-sa108** and **uk-crypto-tax** disposals; **uk-payroll** staff/company payroll; **uk-student-loan-repayment** loans. Do not promise an automatic calculation or filing before those checks.

## Boundary and exception table

| Situation | Intake action |
| --- | --- |
| Allowance threshold met but employer/connected income or notice present | Resolve exclusions/notice; no automatic full-relief or no-return conclusion |
| VAT threshold or MTD threshold met | Check exact period, establishment/qualifying income and exceptions before a legal conclusion |
| £2,400 assessed tax and £1,920 PAYE | 80% exactly, but £480 left is below £1,000: see Case 4 |
| Company, umbrella, agency or partnership | Record evidence; do not relabel income as a sole trade |

### IR35 and off-payroll working

The rules concern services through an intermediary where direct engagement would have been employment. They are considered engagement by engagement. Umbrella employees are unlikely to fall under these rules; a direct sole trader's employment-status question is separate ([HMRC IR35](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35)).

For an ordinary UK public-sector or medium/large private-sector client, the client decides status; for a small private-sector client the worker's intermediary does. A five-person workforce alone does not establish size ([HMRC clients](https://www.gov.uk/guidance/off-payroll-working-for-clients); [small-client guidance](https://www.gov.uk/guidance/off-payroll-working-for-intermediaries-and-contractors-providing-services-to-small-clients-in-the-private-sector)). Client-size statutory thresholds, relevant financial years, transition/group/simplified tests and overseas clients: Check this point with one of our partner accountants. Obtain dated evidence rather than choosing between Companies Act and HMRC headline figures.

Retain the SDS/reasons, contracts, actual practices and any change. If the rules apply under the client-determination regime, the deemed employer deducts Income Tax/employee NI and pays employer NI; loan repayments are not deducted from those fees and the off-payroll borrower must register/file Self Assessment ([HMRC IR35](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35)). For missing SDS, size requests, CEST accuracy/contract conditions, disagreements/deadlines, fee-chain liability, deemed employment payment and paying already-taxed fees as salary/dividends: Check this point with one of our partner accountants.

## Worked cases

These are conditional illustrations. A numerical result never proves status, relief eligibility or registration.

**Case 1. Side sales, 2025/26.** Employee; £800 handmade-goods gross takings; no other untaxed income. £800 < £1,000 does not meet the sole-trader trigger. Only assuming relevant income, eligible full relief, no election out/exclusion, no notice or other filing reason may no return be needed. Keep records. Missing conditions: Check this point with one of our partner accountants. Sources: step 2 and [allowance rules](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income).

**Case 2. New web designer, June 2025 start.** Never filed; 2025/26 takings £34,000, stated profit £30,000. Assuming a genuine sole trade, the gross trigger requires a return and first-return notification by 5 October 2026; ordinary online return/balance date 31 January 2027. Assuming ordinary eligible NI status/weeks and £30,000 is liable profit, Class 2 is treated paid for eligible weeks using the historical £6,845 threshold; Class 4 = (£30,000 − £12,570) × 6% = £17,430 × 6% = **£1,045.80**. Sources: steps 2 and 6.

First-year payments on account for 2026/27 on 31 January/31 July 2027 depend on BOTH exemptions and the correct base, not profit alone. £34,000 − £30,000 = £4,000 above the 2025/26 MTD threshold before annualisation; a start on 6 April 2027 requires qualifying-income and exemption checks and does not rule out an earlier obligation from other sources. Check this point with one of our partner accountants. Routes: **uk-income-tax-sa100**, **uk-national-insurance**, **uk-bookkeeping**.

```oa-check
name: New sole trader, Class 4 on GBP 30,000 profit and the MTD test on GBP 34,000 takings (2025/26)
inputs:
  takings: 34000
  profit: 30000
  lower_profits_limit: 12570
  upper_profits_limit: 50270
  class4_main: 0.06
  class2_line: 6845
  mtd_threshold_2025: 30000
steps:
  - class4: (min(profit, upper_profits_limit) - lower_profits_limit) * class4_main
  - profit_over_class2_line: profit - class2_line
  - takings_over_mtd_threshold: takings - mtd_threshold_2025
expected:
  class4: 1045.80
  profit_over_class2_line: 23155.00
  takings_over_mtd_threshold: 4000.00
```

**Case 3. Consultant.** 2024/25 gross takings £55,000; unregistered for VAT; first rolling-year taxable turnover excess over £90,000 at August 2026 month end. Assuming £55,000 is qualifying income and no exemption, MTD starts 6 April 2026. Assuming ordinary UK-established VAT liability, no applicable exception and no earlier forward-test trigger, notify by **30 September 2026**, effective **1 October 2026**. MTD absence/registration remedy or exception facts missing: Check this point with one of our partner accountants. Routes: **uk-bookkeeping**, **uk-vat-return**. Sources: steps 4–5.

**Case 4. Employee's sideline.** Stipulate relevant assessed Income Tax/Class 4 £2,400, creditable PAYE £2,100 and no other adjustments: £2,100 / £2,400 = **87.5%**; £300 remains. Both the over-80% and under-£1,000 exemptions apply. With PAYE instead **£1,920**, the share is exactly **80%** and £480 remains: the percentage exemption fails, but **the under-£1,000 exemption still means no payments on account**. The original claim that instalments become due at £1,920 was wrong ([HMRC tests](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).

```oa-check
name: Payments on account, 80% test, GBP 2,100 of GBP 2,400 paid through PAYE
inputs:
  total_tax: 2400
  paid_at_source: 2100
  test_share: 0.80
steps:
  - share_paid: paid_at_source / total_tax
  - margin_over_test: share_paid - test_share
  - paye_at_exactly_80: total_tax * test_share
  - balance_at_exactly_80: total_tax - paye_at_exactly_80
  - self_assessment_part: total_tax - paid_at_source
expected:
  share_paid: 0.875
  margin_over_test: 0.075
  paye_at_exactly_80: 1920.00
  balance_at_exactly_80: 480.00
  self_assessment_part: 300.00
```

**Case 5. Own company, large bank.** IT contractor; bank SDS says inside; student loan being repaid. Assuming the ordinary client-determination regime applies, the client decides and deemed employer accounts for Income Tax/employee/employer NI. Loan repayments need Self Assessment. Company accounts/payroll, disputes and extraction of already-taxed fees: Check this point with one of our partner accountants. Routes: **uk-income-tax-sa100**, **uk-payroll**; source: [HMRC IR35](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35).

**Case 6. Same contractor, five-person design studio.** Five people do not establish small-client status. Obtain the legal entity, financial-year, turnover/assets, group and UK-connection evidence. Only if a small private-sector client is established does the intermediary decide under that regime. Determination/deemed payment: Check this point with one of our partner accountants. Source: [HMRC small-client guidance](https://www.gov.uk/guidance/off-payroll-working-for-intermediaries-and-contractors-providing-services-to-small-clients-in-the-private-sector).

**Case 7. October 2025 arrival, overseas clients.** Preserve 2025/26; do not infer split-year or FIG eligibility, or VAT place of supply, from arrival/client country. Check this point with one of our partner accountants. Route first to **uk-statutory-residence-test** and **uk-non-dom**; hold the dependent computation.

**Historical intake illustration, 2025/26 (restored).** These are the original unverified illustrative document entries, not figures to copy into a user's return. Jane Smith, single, Manchester, software developer, stated full-year resident/sole trader, stated standard VAT number GB 123 4567 89. Confirm all status/identity entries from evidence.

- Client amounts £42,000 + £20,000 + £10,000 = £72,000; original VAT illustration £72,000 × 20% = £14,400. The separate £5,000 non-UK-client entry has no established inclusion or place-of-supply classification. Reconcile it; do not assume outside scope. The 20% arithmetic assumes every £72,000 supply is standard-rated; it does not establish VAT due.
- Software £2,400; insurance £600; accountancy £900; telephone/broadband £840; vehicle fuel £2,800 and maintenance £500; MacBook Pro £1,800 in March 2026; claimed input VAT about £1,500. These listed costs total £8,040 before the laptop, £9,840 including it; private use, deductibility, cash basis/capital allowances/AIA and VAT recovery remain unresolved. Check this point with one of our partner accountants.
- Employment £15,000, PAYE £1,200, Class 1 NI £720; Plan 2 and £400 PAYE loan repayments. The original £27,295 loan threshold is an unverified historical label, not a usable 2025/26 threshold; no extra repayment is computed. Check this point with one of our partner accountants.
- Original payments £3,000 on 31 January 2026 and £3,000 on 31 July 2025 total £6,000, but span different ordinary advance-tax years. Do not treat them as two advances for one year. Original 2024/25 SA liability £8,500 and profit £48,000 do not prove a POA base; only if £8,500 is the relevant base and neither exemption applies is each 2025/26 advance £4,250, totalling £8,500. Check allocations and actual payments with **uk-payments-on-account**; unresolved facts: Check this point with one of our partner accountants.
- Original Q1–Q3 2025/26 filed/Q4 January–March 2026 outstanding labels require actual VAT periods; the illustrative £58,000 pre-capital-allowance profit is unsupported. £72,000 − £8,040 = £63,960 before resolving the laptop and other items, not £58,000; £72,000 − £58,000 implies £14,000 costs, £5,960 more than those listed before the laptop. Do not use either arithmetic subtotal as taxable profit. Check this point with one of our partner accountants.

## When to refuse or refer

Stop the affected calculation and say: **Check this point with one of our partner accountants.** Record why, the evidence needed and the receiving Guide. Apply this to the holds above and to unreported years, enquiries/avoidance schemes, company CT600/accounts, partnership/LLP SA800, Scottish rates, foreign income/gains/FIG/remittance history, construction/CIS, and inadequate records. Payroll goes to **uk-payroll** at any staff count; the old 1–5/over-5 employee gate is not a tax rule.

Historical expense-method topics remain with **uk-bookkeeping**/**uk-self-employment-sa103**: cash-basis eligibility/exclusions (underwriting, herd basis, averaging, renovation allowance, mineral extraction, R&D), method changes, depreciation versus tax deductions, vehicle method continuity/prior capital claims, home/premises/private-use treatment, pensions and Marriage Allowance. Check this point with one of our partner accountants. Do not revive the old £150,000 cash-basis cap, treat 45p mileage as a 2026/27 rate, or infer a £1,260 Marriage Allowance transfer from marital status. The historical home illustration's £10/£18/£26 monthly amounts and 25–50/51–100/101+ hours, and mileage's first 10,000/excess 25p/motorcycle 24p, require the correct year and eligibility before use; no claim is calculated here.

## Filing and payment

For ordinary 2025/26 returns: paper **31 October 2026**, online **31 January 2027**. The usual balance is due **31 January 2027**; eligible 2026/27 advances are **31 January/31 July 2027**. For ordinary 2026/27 returns: paper **31 October 2027**, online/balance **31 January 2028**, with eligible 2027/28 advances **31 January/31 July 2028** ([deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines); [TMA s8](https://www.legislation.gov.uk/ukpga/1970/9/section/8); [s59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A); [s59B](https://www.legislation.gov.uk/ukpga/1970/9/section/59B)).

A late s8 notice after 31 July but by 31 October gives three months for paper and the ordinary January online deadline; after 31 October it gives three months for either. The balance moves to three months after the notice only where the statutory conditions apply, including notification under s7 within six months after year end and HMRC's s8/8A notice after 31 October. Registration after 5 October alone does not establish either extension ([s8](https://www.legislation.gov.uk/ukpga/1970/9/section/8); [s59B](https://www.legislation.gov.uk/ukpga/1970/9/section/59B)). Other notice/payment exceptions: Check this point with one of our partner accountants.

The ordinary online cutoff to request tax-code collection for 2025/26 is **30 December 2026** (for 2026/27, **30 December 2027**); meeting that date alone is not entitlement. Coding-out amount/capacity/eligibility, notification failures, penalties, interest and the applicable MTD regime: Check this point with one of our partner accountants. Route to **uk-income-tax-sa100**.

## Completion checklist

- [ ] Year/source beside every input; documents parsed before gap questions; summary confirmed.
- [ ] No status, registration, relief, exemption or private-use percentage inferred without evidence.
- [ ] Every income, expense, capital, VAT, payroll, loan and prior-payment topic routed; all dependent computations held where facts are missing.
- [ ] Confirmed package and unresolved flags delivered to **uk-return-assembly** with working-paper/reviewer-brief/calendar needs, without promising an automatic filing.

## Sources

Official sources, checked for the passages retained above on 26 November 2026:

- [HMRC filing triggers](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return), [allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income), [deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines). Read on: 2026-11-26.
- [VAT registration](https://www.gov.uk/register-for-vat), [MTD start dates](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax), [qualifying income](https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax). Read on: 2026-11-26.
- [NI rates by year](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions), [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account), [record retention](https://www.gov.uk/self-employed-records/how-long-to-keep-your-records). Read on: 2026-11-26.
- [Employment status](https://www.gov.uk/employment-status/selfemployed-contractor), [IR35](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35), [client responsibilities](https://www.gov.uk/guidance/off-payroll-working-for-clients). Statutes are linked in the relevant steps. Read on: 2026-11-26.

Not yet confirmed: the expressly referred classification, eligibility and exceptional-case points above. Their dependent conclusions remain on hold; they are not usable filing instructions.
