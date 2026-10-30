---
name: moldova-payroll
description: "Compute Moldova payroll withholding for 2026 using the cumulative income-tax method, documented exemption months and separate social/medical contribution bases. Covers ordinary private and public employers, listed aviation conditions, qualifying agriculture, joiners, leavers, advances, benefits, corrections, IT-park transitions, nonresident source rules and treaty evidence. Use for salary tax, gross to net, CNAS, CNAM, IPC21, IRM19, personal and dependent exemptions, payment timing and payroll reconciliation. This source-cited writer draft corrects the former employee social deduction and exemption assumptions, preserves predecessor topics through explicit destinations, and requires whole-country independent review. Its stated implementation gaps keep the domain partial; it does not claim accountant attestation or comprehensive coverage."
version: 0.5
jurisdiction: MD
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova payroll withholding, 2026 v0.5

## Who this applies to

Compute Moldova's 2026 ordinary employment withholding, employer social contributions and employee medical premiums using the employee's actual status, gross components, accrual period, payment dates and exemption application. This local source-cited writer draft replaces the old 2025 method. It has not completed independent whole-country review or accountant attestation. Do not treat its former “Tier 1 rules” heading as a professional sign-off. [Fiscal Code arts. 15, 19, 88][code]; [Government Decision 697/2014, 2026 regulation][reg].

Article 88 also treats covered work/service payments to individuals not carrying on business, board/audit-commission remuneration and administrator mandates through its employment-income rules. The regulation covers day workers, student trainees and dual-education learners as specified. Day workers cannot claim the chapter-4 exemptions. Registered independent service entrepreneurs have a separate single tax, but art. 88(8) treats their relations with counterparties outside art. 24(11^1)'s conditions as employment for tax purposes. Registration or an invoice alone does not settle that test. [Arts. 15(a^1), 24(11^1), 88(5)–(8)][code]; [regulation points 1–6, 9^2][reg].

Choose the employer social category independently: ordinary private/commercial and specified higher-education/medical employers; budgetary/public institutions; listed special-condition aviation; qualifying agriculture; or the actual special regime. A general hazardous-work description does not prove a 32% rate. Ordinary payroll has no additional 6% employee social withholding under the listed employer tariffs. The old Guide's employee 6% deduction and 27%-of-gross “combined employee rate” are corrected here. [CNAS instructions points 9–13][cnas]; [Law 489 art. 17][social].

IT-park salary, the historical/sector software-worker rules referenced by the regulation, and fixed/self-payer contributions need their actual regime and dates. IT-park status does not exempt every civil-service contract, and the accrued-versus-paid transition rules matter when entering/leaving the park regime. See [social/medical contributions](moldova-social-contributions.md) for the full category map and its remaining gaps, and [individual income tax](moldova-income-tax.md) for annual liability and final withholding. This Guide is not a labour-law calculation of contractual wage, paid leave, sickness entitlement or severance. Establish those amounts from the applicable documents/law before taxing them. [Law 489 art. 19(7)][social]; [regulation points 5, 36^1, 39][reg].

## Rates, bands and thresholds

Amounts are MDL. The statutory rate does not establish the tax base or entitlement.

| Item | 2026 rule | Primary source |
|---|---|---|
| Ordinary personal employment tax | 12% of the taxable base, withheld using the cumulative method | [Code art. 15(a), 88][code]; [regulation points 36–44][reg] |
| Day-worker income tax | 12%, without chapter-4 exemptions | [Art. 15(a^1)][code]; [regulation point 9^2][reg] |
| Ordinary private/commercial employer social contribution | 24% of the applicable contribution base | [CNAS point 9.2][cnas]; [IPC21 table 2, row 1.1(b)][ipc] |
| Specified budgetary/public employer social contribution | 29%, with the stated higher-education/medical exceptions | [CNAS point 9.1][cnas]; [IPC21 row 1.1(a)][ipc] |
| Listed aviation special conditions | Specified public category 39%; specified private category 32%; check the exact annex-2 occupation | [CNAS points 10–10.2][cnas]; [Law 489 annex 2][social] |
| Qualifying agriculture | Employer 18% plus State 6%, total 24%; qualifying CAEM 01.1–01.6 income at least 70% of operating income | [Law 489 art. 17(3^1)–(3^2)][social]; [CNAS points 13–13.4][cnas] |
| Ordinary employee social deduction | No additional employee 6% under these employer-category tariffs | [CNAS points 9–10][cnas] |
| Ordinary employee medical premium | 9% of covered gross remuneration, withheld by the payer; do not split into an assumed 4.5%/4.5% | [Medical budget art. 4(1)][medicalbudget]; [Law 1593 arts. 4, 6, 12, 20][health] |
| National minimum monthly salary input | 6,300 from 1 January; apply actual worked time and the separate social floor | [CNAS point 19.1][cnas]; [Law 489 art. 22][social] |
| Part-time/reduced-work social floor | Contribution at least 25% of the contribution on the full national minimum, alongside the time-proportionate minimum base | [Law 489 art. 22(1)][social] |
| Forecast monthly average salary | 17,400; reference input, not an automatic contractual wage or ceiling | [CNAS point 12.1 citing Government Decision 773/2025][cnas] |
| Standard personal exemption | 29,700 annually; monthly twelfth 2,475 for an eligible month. Resident's annual taxable-income test is strictly below 360,000, excluding art. 90^1 income and including the specified retail/plant-purchasing income | [Code art. 33(1)–(1^1), January comparison][jan]; [current art. 33][code]; [regulation points 10–10^1, 18][reg] |
| Increased personal exemption | 34,620 annually; monthly twelfth 2,885, only for the statutory categories and documented entitlement | [Art. 33(2)][code]; [regulation points 30–32][reg] |
| Qualifying spouse exemption | 21,780 annually; monthly twelfth 1,815. Spouse must be in art. 33(2)'s category and not use the personal exemption; not a universal spouse allowance | [Art. 34][code]; [regulation points 11–13, 33][reg] |
| Ordinary qualifying dependent | 9,900 annually; monthly twelfth 825 | [Art. 35(1)][code]; [regulation points 14–15, 34–35][reg] |
| Specified disabled dependent | 21,780 annually; monthly twelfth 1,815; apply the actual statutory disability/relationship conditions | [Art. 35][code] |
| Dependent's income condition | Income not above 12,400 annually, with the specified disability-State-allowance exclusion | [Art. 35(2)(b)][code] |
| Employer-owned property for personal use | Statutory benefit uses 0.0373% per day of the prescribed tax-undepreciated value fixed from the start month | [Art. 19(e)][code]; [regulation point 8(5)][reg] |

Both the January and current Code retain the cited personal/spouse/dependent amounts and the strict personal-exemption gate. At exactly 360,000, do not apply a rule written as “less than”. Do not substitute annualised contractual gross alone for the statutory annual-income test. Dependent/spouse relief has its own conditions; loss of the standard personal exemption does not automatically erase every other documented exemption. The employer is not obliged to track loss of the personal-exemption right; the employee's annual liability and application duties remain separate. [Arts. 33–35, 88(1)][code]; [regulation points 10^1, 16][reg].

## The base

### Build separate payroll, contribution and payment records

Record the employer's registration/activity/category, worker identity, contractual and actual status, actual hours and dates, accrual month, each taxable payment, gross cash, benefits, excluded amounts and supporting law. Maintain separate bases for PIT, social insurance and medical insurance. Do not treat every meal ticket or reimbursement as taxable under every system. The amounts “calculated”, “directed to payment”, “paid”, “insured income” and “net bank transfer” serve different purposes. [Code arts. 18–20, 88][code]; [Law 489 arts. 20, 22–23][social]; [Law 1593 arts. 3–6, 20][health]; [IPC21 tables 1–2][ipc].

PIT includes covered salary, bonus, commission, fees, taxable material assistance and non-cash benefits, less only the deductions/exemptions actually available. Exclusions require the precise art. 20 category and relevant art. 24/Government limits. A vendor name or an accounting description is not an exemption. Keep business travel, transport/food/training, gifts, medical benefits, childcare, vouchers and other reimbursements separately identified. The [corporate Guide](md-corporate-income-tax.md) records the underlying employee-benefit caps and its Government-procedure gaps; do not silently treat an unresolved cap as unlimited. [Code arts. 18(c), 19–20, 24][code]; [regulation points 3, 6–8][reg].

For benefits, establish the actual valuation rule. Taxable benefits include personal-expense reimbursements and payments to third parties, the excess nominal meal-ticket value, specified trainee transport/food over the allowed amount, forgiven employee debt, covered housing top-ups, concessional loans and employer property used personally. For an employer-owned asset, art. 19(e) uses the statutory daily percentage and starting tax-undepreciated value rather than a guessed rental price; non-owned assets use the employer's actual daily right-of-use cost. A below-cost employee charge leaves the difference as a benefit under regulation point 8(5). For concessional loans, compare the actual employee rate with the preceding-November BNM weighted new individual-loan rate for terms above five years; the banking/non-bank-lender ordinary-customer exception has its own facts. The ordinary MDL benchmark and observed loan/day formula are supplied below; the stated foreign-currency and implementation limits remain. [Art. 19][code]; [regulation points 7–8][reg].

**Employer-loan benefit, ordinary MDL case.** Current Code art. 19(d) selects the preceding-November BNM weighted rate for **new loans to individuals with a term over five years**. It does not select the employer's own bank cost, the all-bank/all-term total, the individual-entrepreneur series or the 6% monetary-policy base used for late charges. The configured BNM DPMC8 report for **November 2025**, `moneda naţională → persoane fizice: total → peste 5 ani → Rata nominală,%`, shows **8.32%**. Use that fetched input for this ordinary MDL calculation in 2026; do not import the different old rounding-up/own-loan-maturity wording from archived summaries. The current statutory paragraph does not direct rounding this benchmark up to 9%. Retain the exact report period, currency, borrower group and maturity row, since the report opens at its latest period by default. [Code art. 19(d)][code]; [configured BNM loan report][loanreport].

The formula image embedded in current regulation point 8(4) was visually read: `F = S × (Nzl / 365) × ((Rd − Rdc) / 100)`. `F` is the benefit, `S` the loan balance, `Nzl` the days of use in the month, `Rd` the BNM benchmark and `Rdc` the employee loan rate, with rates expressed as percentages. Apply the Code's **positive-difference** rule: a benchmark-minus-contract-rate result at or below zero produces no positive interest benefit. For the ordinary MDL case, calculate each established balance segment as `balance × use_days / 365 × max(0, 8.32 − actual_employee_rate_percent) / 100`, then total the month's segments. Do not divide an annual benefit by twelve irrespective of days, use the full original principal after repayment, or create a negative taxable benefit. [Code art. 19(d)][code]; [regulation point 8(4), monthly determination and repayments][reg]; [official formula image][loanformula].

The regulation requires monthly determination and recalculation for principal repayments; it also applies the stated method to loans granted and still unpaid in periods through 2019. Obtain the actual agreement, disbursement/balance and rate histories, repayment allocation and days of use. The bank/non-bank-lender exception requires the same financial product on general conditions accepted for **at least one third-party individual**; employment by a lender alone is insufficient. Keep loan principal, actual interest and the deemed benefit separate. Feed the benefit into the applicable cumulative PIT calculation; this value-only method does not establish every contribution-base exclusion, actual cash withholding or a no-cash-wages remittance route. Foreign-currency/FX-linked benchmark selection, no-observation rows, conversion and precise transaction-day/final monetary-rounding conventions remain explicit gaps. A published foreign-currency row showing zero rate **and zero volume** is not treated as proof of a universal zero employee-loan benchmark. [Code arts. 19(d), 88][code]; [regulation points 8(4), 38–44][reg]; [BNM report currency/borrower/term data and notes][loanreport].


Social contributions use the covered accrued salary/remuneration base and the employer's statutory category. Compare the actual base with the national minimum proportionate to time worked and, for part-time/reduced work, the separate minimum contribution of one quarter of the full-minimum contribution. Do not deduct the employer's contribution from the employee's cash. Agriculture's State 6% is not an employer outlay or employee withholding. Special aviation and public rates are not general substitutes for 24%. [Law 489 arts. 17, 20, 22–23][social]; [CNAS points 9–13][cnas].

Medical premiums ordinarily apply to covered gross before PIT or other deductions, and follow the actual remuneration payment timing. Excluded remuneration and IT-park salary require their own statutory tests. Do not import the social minimum floor into the employee's medical base. A payment in 2026 for remuneration through 31 December 2020 has IPC21 instruction point 9's specific historical health-premium rule; the ordinary current-payroll percentage summary is not a historical-period calculation. [Law 1593 arts. 3–6, 12, 20][health]; [medical budget art. 4][medicalbudget]; [IPC21 instruction point 9][ipc].

### Establish exemptions from applications and evidence

Obtain the signed application and current supporting evidence, including residence, disability/qualifying category, marriage and spouse non-use, dependent relationship/identity/income and guardian status where relevant. Use regulation points 30–35 and its tables for the document requirements and exemption codes P, M, Sm, Nx and Hx. The old blanket refusal “missing IDNP means never file” is replaced by the actual IPC21 identity rule in the filing section. A taxpayer identification record, an exemption application and a social-insurance record are different evidence. [Code art. 88(2)–(4)][code]; [regulation points 17, 30–35][reg].

A resident can use exemptions at the main employment, secondary employment, service payer or dual-education location as permitted, but cannot duplicate the personal exemption for the same period at another place. Day workers receive no chapter-4 exemptions. The increased personal category requires the exact art. 33(2) grounds, including the listed Chernobyl, qualifying war/disability and rehabilitated-repression categories. A general family or disability label is not enough. Qualifying spouse relief is whole rather than divided between spouses; divorce requires the stated annual recalculation. Dependents must meet art. 35's cumulative relationship and income conditions, with the specified guardian/curator route and disability allowances excluded from the income test. [Code arts. 33–35][code]; [regulation points 9–16][reg].

Grant or cancel exemptions from the month after the application is submitted/withdrawn. Each eligible month uses its annual twelfth; do not automatically grant twelve months to a mid-year hire or use a daily fraction. An employee whose employment continues need not submit a new application every year solely because the year changes, but changed circumstances require a new signed application within 10 days and expiring evidence still needs renewal. If the application or supporting documents are missing, incomplete or withdrawn, withhold **without exemptions** under point 21; do not default to the standard personal amount. Residence acquired mid-year has the separate application/annual-return route, not an automatic employer recalculation from January. Special-regime months, mixed standard/special months, death and spouse/dependent changes have their own provisions. [Code art. 88(2)–(3)][code]; [regulation points 16^1–26, 38][reg].

### Compute PIT cumulatively and reconcile the current payment

1. Establish the start of the current-year employment/covered relationship and the applicable payment-year rules. For December salary paid in January, regulation point 29 uses the rate/exemptions at payment. This does not change the separate social accrual and insured-period record.
2. For each payment, keep cumulative taxable gross and taxable benefits, deductible medical premiums and other verified payroll deductions, and the cumulative exemptions for eligible months. Determine taxable cumulative income after these deductions/exemptions, without inventing an employee 6% social deduction. Article 35^2 permits actual mandatory personal contributions under its own conditions; the employer's contribution is not that personal payment. Other annual personal deductions require their actual legal/reporting route rather than an assumed monthly allowance.
3. Calculate cumulative ordinary PIT at 12% and compare with PIT already withheld this year from the same relationship. Current withholding is the difference required by the cumulative record. Separate payments and advances within the same month do not each receive another month's exemption. A negative adjustment/refund has the regulation's correction method; do not blindly floor the withholding difference to zero and lose a genuine overpayment.
4. Reconcile the amount of PIT/medical withheld, other lawful deductions and actual net cash. Employer cost is gross plus employer social and any actual additional employer cost, not an automatic employee tax gross-up. Keep non-cash benefits and prior advances separately so they are not paid in cash twice.
5. Reconcile nominal insured periods/contributions, the payment-period PIT/medical report, employee personal record and treasury payments. Keep proof of filing acceptance and allocation, not merely a screenshot of a submitted draft.

[Code arts. 15, 35^2, 88, 92][code]; [regulation points 29, 36–44, 48^2–49][reg]; [IPC21 instructions][ipc].

Regulation point 42 specifies whole-value personal-record entries with the final entry in decimals, while automated accounting systems can calculate the stated indicators with decimals. The worked examples use the permitted automated decimal method. Preserve the system's statutory rounding treatment through the cumulative record; do not round every intermediate monthly rate into a different annual liability. [Regulation points 41–43][reg].

### Joiners, leavers, leave, special regimes and corrections

For a mid-year joiner, accumulate income from employment and exemptions from their actual permitted start. Point 40 counts the employment month and termination month for its employment-month purpose; that is not permission to override point 18's exemption-application timing. A second employer does not import the first employer's payroll record without a lawful basis, and the same-period personal exemption cannot be duplicated. [Regulation points 9–10, 18, 38–40][reg].

For payments after termination in the same tax year, use the cumulative income and the exemption months available up to termination. For arrears paid in a later year, start the prescribed new personal record and calculate at payment under point 46. For unlawful dismissal/reinstatement payments, use point 47, including the special reporting treatment when a bailiff takes the salary amount without withholding; corrections to annual beneficiary information require the stated notice. These are tax rules, not authority to choose a severance or back-pay amount. [Regulation points 45–47][reg]; [Code art. 92(4^1)][code].

For the last taxable payment before maternity leave, point 48 has a special exemption calculation: the full-year employee route and the mid-year employment/application route differ. If the worker returns that year, preserve the exemptions already granted; withdrawing the application before year-end requires the specified recalculation to actual entitlement. Employer-funded and public-budget sickness periods also have distinct nominal social-reporting categories. Do not tax an exempt benefit simply because a salary bank account receives it. [Regulation point 48][reg]; [Code art. 20][code]; [CNAS points 8.1–8.3][cnas].

For IT-park salary, withholding is included in the resident's single tax under the actual regime. Salary accrued under the ordinary regime but paid during the special regime retains ordinary treatment; salary accrued under the special regime but paid after returning to ordinary treatment is not taxed again at payment. The regulation's separate software-occupation method is not identical to IT-park status. Exact park eligibility, single-tax minimum/headcount and every historical sector transition remain a specialist gap; do not assume that an ordinary civil-contract payment is included merely because the payer is a park resident. [Regulation points 5, 36^1, 39, 41–41^1][reg]; [IPC21 instruction point 4][ipc].

If a payment was made net/without withholding, regulation point 48^1 has the prescribed cumulative gross-up formula, including medical premiums, execution-order deductions, exemptions and prior income/tax. Do not divide every net payment by 0.88 or combine tax rates by addition. Error correction before the last day of the fiscal period is required by point 48^2. For repayment of wrongly paid salary/overstated benefits, record the negative adjustment and calculate what the employee returns after excess tax is reconciled; the employee does not automatically repay the full gross. [Regulation points 48^1–49][reg].

### Bank/payslip reading and the working paper

Use “SALARIU”, “SALARIU NET”, “SALARIZARE”, “AVANS”, “PREMIU”, “BONUS”, “CONCEDIU”, “INDEMNIZATIE” and similar Romanian/English descriptions as search cues. “CNAS”, “BASS” and social references identify possible social movements; “CNAM”, “FAOAM” and medical references identify possible health movements; “SFS”, “IPC21” and “IMPOZIT PE VENIT” identify possible reporting/treasury movements. These names are not evidence of the gross, a legal exemption or the tax period. Received salary, an employer's outgoing net payment, statutory remittances, refunds, pensions and private transfers must not be double counted or automatically classified for VAT.

Reconcile payslip gross and benefits, medical withholding, PIT, other lawful deductions, advances and net cash. On the employer side, reconcile gross accrual, employer social, State agricultural compensation where applicable and the actual cash settlements. Maib/MICB/OTP/Victoriabank are possible statement labels, not legal classifications. A combined payment cannot prove every liability is discharged. A bank-only file supports a transaction reconciliation; obtain contracts, payroll, the exemption application and declarations before finalising the legal calculation.

The working paper keeps identity and valid IDNP/CPAS; tax year; employer category; contractual status/hours; gross accrual and payment date; taxable/non-taxable benefit basis; separate PIT/social/medical bases; application/evidence and exemption codes/start months; annual personal-income gate evidence; cumulative income, medical, exemptions and prior tax; current withholding; other deductions/net cash; employer cost; source/article/read dates; IPC21 tables and nominal periods; annual beneficiary information; treasury allocation; and unresolved questions. Do not replace the statutory annual-income test with “monthly gross × 12”, copy an old 2025 minimum, or assume missing documents prove a deduction.

## Deadlines and filing

| Obligation | Rule | Primary source |
|---|---|---|
| Withhold PIT | At the statutory salary/remuneration payment stage using the cumulative record | [Code art. 88][code]; [regulation points 36, 38, 43–44][reg] |
| PIT remittance and monthly withholding report | By the 25th after the month the payments were made | [Code art. 92(1)–(2)][code] |
| Percentage medical payment | By the 25th after the month covered remuneration was paid | [Law 1593 arts. 12, 20][health] |
| Ordinary social payment/reporting | Generally the 25th after the reporting month for the category, preserving accrual and insured-period distinctions | [CNAS points 23–28, 40–41][cnas] |
| Annual payer information | Code art. 92(3)'s annual information by 25 January following the year; keep this separate from monthly IPC21 and special categories | [Art. 92(3)][code] |
| Employee/recipient income-tax information | By 1 March following the year, subject to the statute's exceptions; corrections engage the 15-working-day notification rule | [Art. 92(4)–(4^1)][code] |
| Employment start/change/end information | IRM19 within 10 working days for the prescribed events | [CNAS point 32][cnas] |
| Changed exemption circumstances | Employee submits the new signed application within 10 days; relief timing follows the regulation | [Code art. 88(3)][code]; [regulation points 18, 22][reg] |
| Individual annual return where required | Normally 30 April following the tax year for the ordinary individual category; separate entity/professional and departure rules apply | [Code art. 83][code]; [CET18 instructions point 7][cet] |

Use IPC21's approved version for the reporting period. The currently read Order 94 consolidation reflects Order 56 operative 30 April 2026; verify the earlier period's applicable form when correcting it. Table 1 code 11 columns 4–6 records paid salary/covered remuneration before medical deduction, withheld PIT and withheld medical premiums. Table 2 records the nominal insured person, work/insured periods, category, contribution tariff, occupation code, social base and calculated contribution; it is not a duplicate cash-wage table. One employee can require multiple rows for different categories/periods. Preserve the SFS/CNAS transmission and accepted receipt. [Order 94, annex 2, reporting preamble and tables 1–2][ipc].

For table 2, a missing IDNP is entered as zero if the valid CPAS is available; a missing CPAS is entered as zero if the valid IDNP is available. **Both cannot be zero.** Do not invent either identifier or reject a lawfully identifiable worker solely because one is absent. The occupation code is mandatory under the current instruction. Full 2027 proposed CPAS changes are not current 2026 filing instructions. [IPC21 table 2, columns 3–4, 8][ipc].

A corrected IPC21 is the complete prescribed replacement/version, not an ad hoc delta. Identity/category/occupation/period corrections, fiscal-control social recalculations and corrections to previously controlled periods have different checkboxes and scope; do not select mutually incompatible declaration types. The fiscal-control nominal recalculation route has the stated 30-calendar-day submission rule. The no-return exception requires no payments to individuals, no calculated social contributions **and no employees**, not merely zero bank salary. Pre-2021 corrections use the historic forms/administration rather than forcing IPC21. [IPC21 instruction points 2–7 and preamble][ipc].

IT-park, day-worker, dual-education, sickness, holiday, agriculture and fixed-founder reporting need the correct nominal categories and periods. Do not use an undated category table or a draft proposal as enacted law. Current IPC21 annex-3/4 machine-code detail, actual attached annual forms/classifiers and their technical validations, all historical form transitions and the complete liquidation procedure remain explicit gaps. The [social Guide](moldova-social-contributions.md) retains the verified ordinary/liquidation CNAS deadlines and the January–June taxi versus July ordinary transition. A successful filing receipt and treasury allocation are required before treating an obligation as settled.

### Annual salary and resident-payment information: IALS21

Use **IALS21**, approved by MF Order 95/2020 from reporting year 2021, for its covered salary and resident non-salary payments. Keep the monthly IPC21, annual information report, employee information and any personal CET18 return separate. The ordinary annual deadline is Code art. 92(3)'s **25 January following the calendar year**; the same paragraph has the **15-day** liquidation/division rule measured from approval of the liquidation/distribution balance sheet. Article 92(8) instead gives the specified non-VAT individual entrepreneur/peasant farm with annual average employees not exceeding five the unified-report route and **25 March** deadline. Do not apply the ordinary annual form/deadline to that exception without classifying the payer. [Code art. 92(2)–(5), (8)][code]; [Order 95 approval and annex 2][ials].

Start with the payer's fiscal code, registered name, administering SFS office, head-office four-character CUATM, four-digit main activity code, reporting year and actual submission date. The rendered annex gives period format `P/AAAA`, but omits the values after its introductory sentence for `P`; the actual attachment/portal prefix remains unverified and is not invented here. Reconcile the annual recipient/source totals to the payment record and monthly declarations, including prior-period salary paid in the reporting year. [Order 95 annex 2, preamble and column 6][ials].

| IALS21 column | Current instruction and preparation step | Primary source |
|---|---|---|
| 1–3 | Consecutive entry number across all pages; employee/recipient fiscal code; name and surname | [Order 95 annex 2, columns 1–3][ials] |
| 4 | Spouse fiscal code only where spouse relief is used; it does not create eligibility | [Order 95 annex 2, column 4][ials]; [Code art. 34][code] |
| 5 | Income-source code from the monthly declaration. **Do not fill `SAL a)` from reporting year 2024.** Preserve separate recipient/source records rather than merging different income classifications | [Order 95 annex 2, column 5][ials] |
| 6 | Total income directed for payment in the fiscal period, **including prior-period salary paid in the current year**; use the income amount rather than net bank cash | [Order 95 annex 2, column 6][ials] |
| 7 | Citizenship-country code from annex 3, not months worked or a guessed residence-country code. Leave it blank for a Moldovan citizen; for multiple citizenships use the citizenship with which the person acted in the employment/civil relationship. The actual classifier attachment remains unretained | [Order 95 annex 2, column 7][ials] |
| 8–12 | Actual relief amounts: `P` standard personal, `M` increased personal, `Sm` qualifying spouse, `N` ordinary dependent, `H` specified disabled dependent. Apply the legal eligibility and application-month rules above; do not shift columns using the original 2020 layout | [Order 95 annex 2, columns 8–12][ials]; [Code arts. 33–35][code] |
| 13 | Total exemptions actually granted for the fiscal period; reconcile to the applicable relief columns and payroll records | [Order 95 annex 2, column 13][ials] |
| 14 | Withheld compulsory medical premiums permitted as a deduction under Code art. 35^2(1) | [Order 95 annex 2, column 14][ials] |
| 15 | The instruction expressly refers to withheld individual social contributions deductible under art. 36(7) **as worded before 1 January 2021**. The existence of this field does not authorise a new employee 6% deduction for 2026 or reporting the employer's social charge as an employee deduction | [Order 95 annex 2, column 15][ials]; [Code art. 35^2][code]; [Law 489 arts. 17, 20, 22][social] |
| 16 | Income tax actually withheld at source; reconcile to the cumulative payroll tax record and monthly returns | [Order 95 annex 2, column 16][ials] |

In the dependent-information annex, columns 1–4 identify the sequence, employee fiscal code, ordinary dependent fiscal code and specified disabled dependent fiscal code respectively. Keep the two dependent categories distinct. A corrected IALS21 follows Code art. 188; the separate recipient-notification duty is **15 working days** under art. 92(4^1), and the ordinary **1 March** recipient information has the exceptions in art. 92(4). The annual report itself does not prove the tax remittance. [Order 95 annex 2, dependent annex and corrections][ials]; [Code arts. 188, 92(4)–(4^1)][code].

**2026 version and special entries.** The preceding 19 September 2024 consolidation and current text agree on the ordinary column mapping above. Amending Order 59/2026 became effective on **8 May 2026**. Its added note limits the specified taxi `TAXI`/`SAL` split around **10,000 MDL per employee per month**, and the associated columns-8–12 restriction, to **1 January–30 June 2026 inclusive**. Do not carry that special annual-report rule into July–December. It also deletes the older day-worker personal-exemption sentence; current annex 2 lists only columns **1, 2, 3, 5, 6, 7 and 16** for covered day-worker remuneration. The prior sentence does not establish a current entitlement contrary to the Code and payroll regulation. Actual attached forms, country-code lists, missing period-prefix values and portal acceptance checks still need separate verification; the directly read column instructions do not certify those files. [Pre-amendment annex 2][ialspre]; [current annex 2][ials]; [Order 59/2026 points 1, 3][ialsamend]; [Code art. 33(1^1)][code]; [regulation point 9][reg].

## Penalties and interest

**Calendar-2026 ordinary tax late charge.** Code art. 228(3) and the BNM decision of 6 November 2025, point 1, supply the calculation: the retained **6.00%** short-term policy rate, rounded up to a whole percent, plus **5 percentage points**, divided by **365 days**, gives **0.0301% per delayed day** after rounding the daily percentage to four decimal places. The decimal multiplier is **0.000301**. Apply it to the established outstanding principal for each chargeable day; split changes in principal and calendar year. This calculation concerns debts governed by art. 228 and does not replace a separate statutory regime's rate or establish case-specific relief. [Code art. 228(2)–(3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); [BNM decision, point 1](https://bnm.md/en/node/69226).

**Medical and social rates remain separate.** Medical Law 1593 art. 30(1)–(1^1) applies the Code method from **1 January 2026**, as recorded in the January text and Law 146/2025 commencement annotations, so the above 2026 medical daily rate is **0.0301%**. Preserve art. 30(2)'s documented inter-account-transfer examination exception. Social-contribution late charges retain the separate **0.1%** annual-budget rate; do not use it for ordinary tax or medical premiums. [Current Law 1593 art. 30](https://www.legis.md/cautare/getResults?doc_id=152955&lang=ro); [January art. 30 and commencement](https://www.legis.md/cautare/getResults?doc_id=149273&lang=ro); [Law 320/2025 art. 4](https://www.legis.md/cautare/getResults?doc_id=156540&lang=ro).

PIT and medical late charges use the applicable Fiscal Code art. 228/Law 1593 art. 30 mechanism, rather than the social-insurance daily rate. Article 228 ordinarily runs from the day after the due date through payment inclusive and sets its annual BNM-derived formula; apply the actual debt movements and documented statutory non-accrual periods. Social contribution arrears use the 2026 social-budget 0.1% per delayed day of outstanding principal through actual payment, with Law 489's transfer/set-off exceptions and special qualifying-agriculture timing. Do not compound every liability or multiply the bank balance by a guessed historical rate. [Code art. 228][code]; [Law 1593 art. 30][health]; [Law 489 art. 28][social]; [social budget art. 4][socialbudget].

Filing fines depend on the liable category under art. 232: for the corporate category, art. 260(1) provides 500–1,000 per return with a 10,000 total cap; the individual category has different amounts. Article 261(4) provides the separate 20%–30% understatement sanction, with its qualifying self-correction exception; evasion has the separate 80%–100% rule. Retain the actual notice, offence, correction date and debt movements. A payroll calculation alone cannot establish every administrative/criminal sanction or eliminate a lawful late charge. [Code arts. 232, 260–261][code]; [regulation points 26, 48^2–49][reg].

## Cross-border points

Determine tax residence and actual income source before choosing relief. Nonresident remuneration and employer benefits can fall within art. 71(n)–(o), including the stated administrator/management payments irrespective of where the administrative duties are performed. Article 88 is not replaced by a generic “all foreign workers are exempt” rule. A nonresident's ordinary personal exemptions are not automatically those of a resident; where art. 74 applies its self-assessment route excludes deductions/exemptions and has the specific three-day cessation filing/payment rule. [Code arts. 5, 13–14, 71(n)–(o), 74, 88][code].

Apply the actual treaty's employment/management provisions and residence facts. Under art. 79^3 the individual residence certificate is provided by payment in original paper and/or electronic form; translate unless in English/Russian. The certificate's stated year(s), changed residence conditions and first-60-days extension rule matter. If it is absent, apply domestic law; a later certificate can use the statute's recalculation/refund procedure, not an unsupported lower percentage. Preserve corrected reporting and the actual operative treaty/protocol. No country-specific rate or day-count exemption is certified here. [Art. 79^3][code].

Social-security treaty coverage, posting certificates and medical coverage are separate from an income-tax residence certificate. Obtain work locations/dates, employer/PE cost bearer, treaty and competent-authority coverage records. Refer annual foreign-income/credit questions to the individual Guide and business affiliated transactions to the TP Guide, respecting their remaining gaps.

## Two worked examples that recompute

### 1. Continuing ordinary employee, January 2026

Assume an ordinary private employer, a full month, covered gross accrued and paid 17,400, no taxable non-cash benefit/other deduction, and an employee continuing from the prior year with a valid prior application giving the January standard personal exemption. The statutory annual-income test is satisfied and no exemption is duplicated. Medical is 1,566; the month's exemption is 2,475; ordinary PIT base is 13,359 and PIT 1,603.08. Net cash is 14,230.92. Employer social is 4,176 and gross-plus-social cost 21,576. The contribution bases exceed the ordinary minimum. Automated decimal records are assumed. [Code arts. 15, 33, 35^2, 88][code]; [regulation points 18, 20, 36–44][reg]; [CNAS point 9.2][cnas]; [medical budget art. 4(1)][medicalbudget].

```oa-check
name: Moldova 2026 continuing employee January cumulative payroll
inputs:
  gross: 17400
  medical_rate: 0.09
  annual_personal_exemption: 29700
  eligible_months: 1
  pit_rate: 0.12
  employer_social_rate: 0.24
  prior_pit: 0
steps:
  medical: gross * medical_rate
  cumulative_exemption: annual_personal_exemption / 12 * eligible_months
  cumulative_taxable: max(0, gross - medical - cumulative_exemption)
  cumulative_pit: cumulative_taxable * pit_rate
  current_pit: cumulative_pit - prior_pit
  net_cash: gross - medical - current_pit
  employer_social: gross * employer_social_rate
  employer_cost: gross + employer_social
expected:
  medical: 1566
  cumulative_exemption: 2475
  cumulative_taxable: 13359
  current_pit: 1603.08
  net_cash: 14230.92
  employer_social: 4176
  employer_cost: 21576
```

### 2. February joiner, two March payments and one month's exemption

Assume an ordinary private employee starts in February and submits the application in February, so the first eligible exemption month is March. February paid gross was 10,000, medical 900 and PIT 1,092 without exemptions. In March the employee receives 4,000 then 6,000, both covered ordinary remuneration. Keep one March exemption of 2,475, not one per payment. At the first payment, cumulative gross 14,000 minus medical 1,260 and exemption 2,475 gives taxable 10,265 and cumulative PIT 1,231.80; withhold 139.80 after February's 1,092. At the second payment, cumulative taxable income is 15,725 and PIT 1,887; withhold a further 655.20. March total PIT is 795, medical 900 and net 8,305. No other deductions/benefits or special regimes; the annual-income condition is satisfied. [Regulation points 18, 21, 38, 40, 42–44][reg]; [Code arts. 15, 33, 35^2, 88][code].

```oa-check
name: Moldova 2026 February joiner and two March payment reconciliation
inputs:
  february_gross: 10000
  february_medical: 900
  february_pit: 1092
  march_first_gross: 4000
  march_second_gross: 6000
  medical_rate: 0.09
  march_eligible_exemption: 2475
  pit_rate: 0.12
steps:
  first_cumulative_gross: february_gross + march_first_gross
  first_cumulative_medical: february_medical + march_first_gross * medical_rate
  first_cumulative_taxable: max(0, first_cumulative_gross - first_cumulative_medical - march_eligible_exemption)
  first_cumulative_pit: first_cumulative_taxable * pit_rate
  first_current_pit: first_cumulative_pit - february_pit
  second_cumulative_gross: first_cumulative_gross + march_second_gross
  second_cumulative_medical: first_cumulative_medical + march_second_gross * medical_rate
  second_cumulative_taxable: max(0, second_cumulative_gross - second_cumulative_medical - march_eligible_exemption)
  second_cumulative_pit: second_cumulative_taxable * pit_rate
  second_current_pit: second_cumulative_pit - first_cumulative_pit
  march_total_pit: first_current_pit + second_current_pit
  march_medical: (march_first_gross + march_second_gross) * medical_rate
  march_net: march_first_gross + march_second_gross - march_medical - march_total_pit
expected:
  first_cumulative_taxable: 10265
  first_current_pit: 139.80
  second_cumulative_taxable: 15725
  second_current_pit: 655.20
  march_total_pit: 795
  march_medical: 900
  march_net: 8305
```

The old six narrative examples and twelve test items remain archived with exact original facts. Their erroneous employee social deductions, combined-rate addition, guessed exemption timing and 2025 minimum/reference labels are not recertified. For an otherwise eligible ordinary full-month case, removing the unsupported employee 6% increases the old 16,100 input's net to 13,189.88; 20,000 with two ordinary dependent monthly exemptions gives 16,511; 18,000 with the ordinary personal monthly exemption gives 14,711.40; 10,000 gives 8,305. A 35,000 input with no personal exemption gives 28,028. These are assumed comparison fixtures, not an exemption decision or proof of an employer's aviation/agricultural status. At the 2026 full minimum 6,300, the equivalent eligible-month net is 5,342.04. The ledger maps each old example/test separately; only the two blocks above are the Guide's current executable examples.

## Ask the client first

- Supply employer registration/activity/category and the worker's actual contract, residence, identity/IDNP/CPAS, start/end dates, hours and any special-regime or cross-border facts.
- Supply accrued and paid gross by component/date, benefits/reimbursements, leave/sickness periods, prior advances, other deductions and the underlying entitlement calculations.
- Supply the signed exemption application, residence/qualifying-category documents, spouse non-use, dependents' relationship/income evidence and the dates rights/applications changed. Was the same-period personal exemption used elsewhere?
- Supply cumulative payroll/personal records, actual medical premiums and prior PIT, including joiners, leavers, later-year arrears, special-regime periods and corrections.
- Supply IPC21/IRM19 and annual information filings with accepted receipts, nominal categories/periods and treasury-account statements, payments, refunds and notices.
- For treaty/social coverage, supply exact work locations/dates, payer/PE cost allocation, operative treaty, residence certificate and competent-authority coverage evidence.

## Sources

Read 30 October 2026. [The payroll ledger](../../../ledgers/moldova-payroll.md) contains source bindings, original-topic destinations and assumed-example evidence. This is a local writer draft with ordinary implementation and specialist gaps, not accountant attestation or completed pack review. The original frontmatter attribution and stamped CTA remain unchanged.

| Official source | Scope actually read | Read on |
|---|---|---|
| [BNM monetary-policy decision, 6 November 2025, point 1](https://bnm.md/en/node/69226) | Fetched 6.00% short-term base input; calendar-2026 daily percentage derived with Code 228(3), rather than copied from an old rate. | 2026-10-30 |
| [Current Fiscal Code][code] | Selected employment, benefit, exemption, deduction, filing, nonresident/treaty and enforcement provisions cited above | 2026-10-30 |
| [January Code][jan] | Personal/spouse/dependent and individual-deduction provisions compared to current selected text | 2026-10-30 |
| [BNM DPMC8 loan report, configured November 2025][loanreport] | Domestic-currency new individual-total loans over five years: 8.32%; query settings and returned report text retained, not the default latest report | 2026-10-30 |
| [Official regulation loan-formula image][loanformula] | Formula visually read in browser; raw binary retrieval returned 403, so no retained PNG file is claimed | 2026-10-30 |
| [Government Decision 697, 1 January 2026 regulation][reg] | Scope, benefits, exemption/documents and full rendered computation/correction text; attached annex forms remain unretained; embedded loan formula visually read separately | 2026-10-30 |
| [MF Order 95/2020 current annex 2][ials], [preceding consolidation][ialspre] and [actual Order 59/2026][ialsamend] | Directly read annual IALS21 columns, dependent/correction method and May amendment with January–June taxi limit; actual form/classifier attachments and omitted period-prefix values remain unverified | 2026-10-30 |
| [Order 94/2020, 30 April 2026 consolidation][ipc] | Reporting/correction rules, preamble, ordinary table-1 fields and selected nominal table-2 instructions; full annex-3/4 code set not yet certified | 2026-10-30 |
| [Order 150/2018, 3 April 2026 CET18 instructions][cet] | Individual categories/departure timing and ordinary field mappings; not a replacement for entity/professional returns | 2026-10-30 |
| [CNAS 2026 instructions][cnas] | Complete retained authority instruction, especially points 8–13, 23–33, 40–41 | 2026-10-30 |
| [Law 489/1999][social] | Selected charging/minimum/arrears and exclusion provisions; direct tariff-annex retention remains open in social Guide | 2026-10-30 |
| [Law 1593/2002][health] | Medical categories, base, timing, reporting and penalty provisions | 2026-10-30 |
| [Medical budget, Law 321/2025 art. 4][medicalbudget] | Current percentage premium and fixed-category amounts | 2026-10-30 |
| [Social budget, Law 320/2025 arts. 3–4][socialbudget] | Original 2026 fixed amounts/daily social charge; later charging-version comparison remains open | 2026-10-30 |

Not yet confirmed: full 2026 commencement/form-version comparison beyond the selected January/current and IALS21 May-amendment checks; operative attached IPC21 annex-3/4 code sets, actual IALS21 form/country-classifier attachments and omitted period-prefix values, portal technical validations, all liquidation/historical correction routes and remaining nominal special categories; remaining Government benefit/travel/food/training implementation, meal-ticket nominal amount and non-cash exceptions; foreign-currency/FX-linked loan benchmark choice, missing-observation handling, exact transaction-day/conversion/final-rounding and no-cash-wages remittance; statutory entitlement computation for contractual wage/leave/sickness/severance and execution deductions; taxpayer-specific pre-2026 medical-penalty transition and arrears-account allocation; complete IT-park/software-occupation eligibility and historical entry/exit treatment; treaty-by-treaty employment/social coverage. The old 2025 figures 5,500 minimum and 16,100 forecast, employee 6%/27% net-pay model, universal 32% hazardous-work default, blanket missing-IDNP refusal, automatic personal exemption without application, non-cumulative monthly formula and assumed 2026 continuity are corrected or retained as historical subjects, not certified current rules. The old dividend/farming/winnings summary belongs to the individual/corporate income classifications; a statutory peasant-farm 7% income-tax rate is not a general payroll or farming-distribution withholding rate. All old examples/tests remain in the archive with their legal-assumption corrections. The payroll domain stays partial until ordinary gaps and whole-country independent review are closed.

[code]: https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro
[jan]: https://www.legis.md/cautare/getResults?doc_id=149766&lang=ro
[reg]: https://www.legis.md/cautare/getResults?doc_id=152473&lang=ro
[ipc]: https://www.legis.md/cautare/getResults?doc_id=154168&lang=ro
[cet]: https://www.legis.md/cautare/getResults?doc_id=153807&lang=ro
[cnas]: https://cnas.gov.md/sites/default/files/2026-10/Particularitati2026.pdf
[social]: https://www.legis.md/cautare/getResults?doc_id=156677&lang=ro
[health]: https://www.legis.md/cautare/getResults?doc_id=152955&lang=ro
[medicalbudget]: https://www.legis.md/cautare/getResults?doc_id=156542&lang=ro
[socialbudget]: https://www.legis.md/cautare/getResults?doc_id=152321&lang=ro


[loanreport]: https://bnm.md/bdi/pages/reports/dpmc/DPMC8.xhtml?id=0&lang=ro
[loanformula]: https://www.legis.md/UserFiles/images/RO/2020/mo165-176md/formula_543.png

[ials]: https://www.legis.md/cautare/getResults?doc_id=154297&lang=ro
[ialspre]: https://www.legis.md/cautare/getResults?doc_id=145086&lang=ro
[ialsamend]: https://www.legis.md/cautare/getResults?doc_id=154274&lang=ro

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
