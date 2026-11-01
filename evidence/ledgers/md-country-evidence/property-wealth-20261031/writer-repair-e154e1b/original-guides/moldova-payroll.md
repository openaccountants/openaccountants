---
name: moldova-payroll
description: "Compute Moldova payroll withholding for 2026 using the cumulative income-tax method, documented exemption months and separate social/medical contribution bases. Covers ordinary private and public employers, listed aviation conditions, qualifying agriculture, joiners, leavers, advances, benefits, corrections, IT-park transitions, nonresident source rules and treaty evidence. Use for salary tax, gross to net, CNAS, CNAM, IPC21, IRM19, personal and dependent exemptions, payment timing and payroll reconciliation. This source-cited draft corrects the former employee social deduction and exemption assumptions, and has a bounded source-review record linked under Sources. Its stated implementation gaps keep the domain partial; it does not claim accountant attestation or comprehensive coverage."
version: "0.11"
jurisdiction: MD
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova payroll withholding, 2026 v0.11

## Who this applies to

Compute Moldova's 2026 ordinary employment withholding, employer social contributions and employee medical premiums using the employee's actual status, gross components, accrual period, payment dates and exemption application. This is a source-cited draft. The bounded source-review record is linked under Sources; accountant attestation is not provided. [Fiscal Code arts. 15, 19, 88][code]; [Government Decision 697/2014, 2026 regulation][reg].

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

**Employer-loan benefit, ordinary MDL case.** Current Code art. 19(d) selects the preceding-November BNM weighted rate for **new loans to individuals with a term over five years**. It does not select the employer's own bank cost, the all-bank/all-term total, the individual-entrepreneur series or the 6% monetary-policy base used for late charges. The configured BNM DPMC8 report for **November 2025**, `moneda naţională → persoane fizice: total → peste 5 ani → Rata nominală,%`, shows **8.32%**. The current statutory paragraph does not direct rounding this benchmark up to 9%. Retain the exact report period, currency, borrower group and maturity row, since the report opens at its latest period by default. [Code art. 19(d)][code]; [configured BNM loan report][loanreport].

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

IT-park, day-worker, dual-education, sickness, holiday, agriculture and fixed-founder reporting need the correct nominal categories and periods. Do not use an undated category table or a draft proposal as enacted law. The actual current IPC21 form/annex-3/4 codes and IALS21 form/classifier are now retained and mapped below. Ambiguous exception rules, authenticated technical validation, the missing annual prefix, historical form transitions and the complete liquidation procedure remain explicit gaps. The [social Guide](moldova-social-contributions.md) retains the verified ordinary/liquidation CNAS deadlines and the January–June taxi versus July ordinary transition. A successful filing receipt and treasury allocation are required before treating an obligation as settled.

### Actual IRM19: employment events, insured-risk periods and corrections

Current Order 126 annexes **3,4,4^1,7,8,9** provide IRM19's actual 12-column form, full instructions, technical requirements and three different classifiers. The form prints “IRM2019”; the order/instructions call it IRM19. Order 56, published and effective **30 April 2026**, changes strict risk/date checks; use the amended attachments. Its old IPC18 caption does not make IPC18 a current salary return. All original attachments and their rendered pages were read. [Form][employ3]; [instructions][employ4]; [technical requirements][employ4s1]; [Order 56 points 1,3](https://www.legis.md/cautare/getResults?doc_id=154136&lang=ro).

Report prescribed hiring, employment changes/termination and childcare/paternal orders within **10 working days**, counted from the **day after the date indicated in the order**. When a person is hired and leaves within 10 days of hiring, make **two entries**, preserving both events. The special-pension occupation assignment is also reportable; instruction 3(c) expressly says no employer order is made for that case. Correction under Code 188 records the **original information-system document number** in the correction header, rather than inventing a new linkage or silently overwriting the source event. [Annex 4 general instructions 2–5][employ4].

Use registered employer name/IDNO, SFS office, CNAS code, actual submission date, primary/corrected flag and responsible-person signature. **Telephone and email are mandatory**. The fields are:

| IRM19 columns | Meaning and current constraints |
|---|---|
| 1; 2 | Entry number; identity-document name in uppercase Latin letters with applicable diacritics/hyphen. |
| 3; 4 | IDNP:13 digits and population-register match; CPAS:11 digits and insured-register match. Technical requirements expressly permit **0 as an exception** for either field. Match both to the same person; where one is 0, match the other to the name. Do not manufacture an identifier or treat every missing-IDNP case as a hiring prohibition. |
| 5; 6; 7 | Insured-risk category and its start/end dates, completed **together**; no ordinary hiring/termination values in these fields. Dates use **dd.mm.yyyy**, with start **earlier than** end; permitted childcare/adoption/guardianship/paternal periods can cross the reporting year. The form duplicates a start-date caption, but the instructions identify 6 as start and 7 as end. |
| 8; 9; 10 | Employment-relation code; termination-reason code **only when 8 is 02 or 08**, otherwise 9 is blank; date that relation code applies, required with 8 and not before **1 April 2019**. |
| 11; 12 | CNAS special-pension occupation code and its assignment date, for the specified assignments/transfers. This is a separate occupation classifier, not the ordinary payroll insured-category or contribution tariff. Its full current occupation list remains to be verified. |

Sources: [actual form][employ3]; [annex 4 completion rules and note][employ4]; [technical requirements 1–11][employ4s1]. Without IDNP, the instruction additionally requires the IRM19 information **on paper to territorial CNAM agencies/representatives**. Preserve that separate delivery evidence; zero in the electronic field does not discharge this paper route. [Annex 4 final note][employ4].

Technical requirement 12 generally separates risk fields 5–7 from relation/date fields 8–10 and special-occupation fields 11–12. Preserve its **specific category 158 exception**: selecting 158 automatically sets relation 8 to **03** and date 10 to date 6. Do not generalise this automatic combination to the other risk categories. For paternal leave, the current technical requirement permits a declared period of **5–45 days**. That is a form-validation bound, not proof that every person is entitled to 45 paid days or benefits. The attachment does not settle the inclusive/exclusive day-count boundary algorithm; no authenticated portal result is claimed. [Requirements 5–6,12 and note][employ4s1]; [Order 56 point 1](https://www.legis.md/cautare/getResults?doc_id=154136&lang=ro).

Keep the three code sets distinct:

| Classifier | Actual current codes and scope |
|---|---|
| Employment relations, annex 7 | **01** indefinite hire; **05** fixed-term hire; **02** termination; **03** suspension; **04** cancellation of suspension. **06/07/08/09/10** are the respective military indefinite/fixed-term/termination/suspension/cancellation codes for the specified military/special-service population only. |
| Termination reasons, annex 8 | **111** unit liquidation; **112** individual-employer cessation; **113** staff/headcount reduction; **114** resignation; **115** Labour Code 82 termination except (b); **116** other Labour Code dismissal; **211** individual-employer death/declaration of death/missing. Public-service **311/312/313/314** distinguish liquidation/reduction/resignation/other; special public-service **411/412/413** distinguish entity liquidation or post reduction/resignation/other specified grounds. |
| Insured risks, annex 9 | **157** childcare to 3; **158** additional unpaid childcare 3–4; **165** paternal; **175** partially paid pre-adoption entrustment; **176** paid adoption or guardianship-placement leave; **177** partially paid care for adopted/placed child to 3; **178** corresponding care for an adopted/placed child over 3. |

Sources: [annex 7 complete bilingual table/footnotes][employ7]; [annex 8 complete bilingual table][employ8]; [annex 9 IRM table][employ9]. Annex 7's 03 footnote excludes the stated circumstances outside the parties' will, employee-initiated medically certified care for an ill family member up to 2 years, and partially paid childcare to 3. Apply the actual event/medical-status rules; a reporting code does not itself prove a lawful dismissal, leave entitlement or benefit award. Blank 2019 amendment captions in annexes 7/8, annex 9's Russian 2019 caption and tariff-year 2021 heading are retained as source defects, not treated as current effective dates or rates.

Do not duplicate the **risk-category information already reported through IRM19 column 5** in IPC21 table 2. This limited instruction does not cancel required salary/contribution records for that person. Pre-1 April 2019 IPC18/DSA19 directions are historical. CAS18-AN's annual fixed-founder/month/person/correction method and its different missing-IDNP rule are in the [social Guide](moldova-social-contributions.md); it is not an employment-event replacement. [Annex 4 general instructions 6–7][employ4]; [CAS instructions][employ6].

### Complete the actual IPC21 attachments

The current Order 94 annex 1 form, annex 3 insured-person catalogue and annex 4 completion requirements have now been read in full. Use the legal employer/category/base rules in the [social Guide](moldova-social-contributions.md) before choosing a code or tariff. A code's presence in the catalogue does not establish a person's entitlement or make a State-paid benefit an employer payment. [Actual form](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an1_94md.docx); [category catalogue](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an3_94ro.docx); [completion requirements](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an_4_94md.docx), read 31 October 2026.

Keep the registered payer name, fiscal/CNAS identifiers, SFS office, four-digit activity, four-character head-office CUATM, contact details, actual submission date and reporting period. The current annex-2 instruction supplies monthly format `P/NN/AAAA`, with `P = L`, months 1–12 and the reporting year. Keep the IT-park marker separate from declaration type. Primary, ordinary correction, fiscal-control social recalculation and insured-person-data correction are distinct modes; the instruction forbids selecting incompatible modes together. [Current Order 94 annex 2 preamble][ipc]; [actual form header](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an1_94md.docx).

| Actual form area | Preparation and reconciliation |
|---|---|
| Table 1 | Columns 1–3 distinguish the numerical row, legal income category and income-source code. Columns 4, 5 and 6 separately report covered income, withheld PIT and applicable medical premiums. An `X` marks a field not to complete. Salary row 11 has source code `SAL`; the full income-code catalogue is retained. |
| Table 1 control sum | Start with total row 61 column 5, then subtract column-5 amounts for rows 41–49 and 49^1. This printed control is not simply total tax, total wages or the medical-premium total. |
| Salary subdivision annex | List subdivision locality codes and their salary PIT. Its column-3 total equals Table 1 `SAL` column 5. Reconcile allocation without reporting the same tax twice. |
| Table 1.1 | A separate corporate dividend-deferral schedule for profit years 2023–2026, not an employee withholding computation. The actual columns are profit year, pre-tax accounting profit, dividends paid, ratio column 4/3, relevant VEN12 row-170 tax and column 7 = ratio × column 6. Establish the corporate eligibility, profit origin and tax-period rules separately; a blank form does not create a deferral entitlement. |
| Table 2 nominal rows | Columns 1–4: sequence, insured person's name, IDNP, CPAS. Columns 5–6: actual work/employer-funded sickness dates. Column 7: category; **7^1: tariff**, distinct from occupation column 8; columns 9–11: social base, temporary-incapacity benefit and calculated contribution. Number continuously across pages and repeat the same person's sequence where that person needs multiple entries. |
| Table 2 summary | Reconcile category/rate branches 1.1–1.7 to eligible nominal rows and column-11 total, observing the separate IT-park and fiscal-control/correction rules. Keep percentage branches distinct from fixed-contribution rows 1.5/1.6; a shaded `X` is not a zero social base. |

Table source: [complete current annex 1](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an1_94md.docx). The current statutory company rules remain in the [corporate Guide](md-corporate-income-tax.md); this payroll method does not resolve its remaining deferral-election or rounding questions.

The actual insured-person catalogue provides these reporting classifications. Select the precise factual branch; a tariff printed beside a category must still match the legal employer/rate/base conditions, rather than being chosen by preference.

| Category code | Actual catalogue population |
|---|---|
| 101; 105; 116; 123; 137 | Employment contract; civil contract; post-termination payments; concurrent employment; specified one-off payment to a person not employed by the entity. |
| 124; 140–144 | Elected/appointed executive, legislative or judicial role; State notary; State lawyer; court worker; specified one-off payment during sickness/maternity/child-care leave; prosecution worker, respectively. Code 143 concerns that one-off payment, not the ordinary sickness benefit. |
| 127; 174; 172 | Individual-enterprise founder; independent justice professional; independent medical practitioner. The catalogue prints annual fixed amounts **MDL 22,878** for 127 and **MDL 30,966** for 174; apply the actual charging periods/exclusions in the social Guide. Category 172 is the separate percentage route. |
| 147; 161; 148 | Specified agriculture population meeting the catalogue's 70% activity condition; the other/sub-70% agriculture population; legally specified special working conditions. Do not infer the reduced/agriculture or special-condition route from an occupation title alone. |
| 14912 | Covered day worker. The catalogue's 6% social route is not an ordinary employee social withholding rate. |
| 15311; 15312; 15321; 15322; 15332; 15342 | Respectively ordinary sickness/non-work accident funded by employer or BASS; work accident/occupational illness funded by employer or BASS; sick-child care from BASS; specified incapacity paid from BASS from its first day. Preserve funding source and reporting responsibility. |
| 155; 15511; 156; 159 | Extended annual leave; extended paternal leave; specified part-time return before child-care leave ends; unpaid leave. |
| 160; 16011; 16012; 16013 | Ordinary paid leave; study leave; additional paid leave; specified unpaid care leave of up to five working days under the cited Labour Code provisions. These catalogue names do not themselves calculate leave entitlement/pay. |
| 162; 16211 | IT-park employee; specified IT-park employee returning part-time before child-care leave ends. Keep the actual IT marker, insured-income rules and single-tax reporting distinct from ordinary payroll contribution totals. |
| 163; 168; 170; 171 | Board/audit/internal-control member; court-ordered reinstatement; externally funded project/programme worker; rest/holiday days. |
| 179; 180; 182; 903 | Specified employer-funded technical-unemployment allowance; Chernobyl-related additional leave; dual-education pupil; specified unused-leave compensation for military personnel. |

Source: [complete actual 2026 category catalogue](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an3_94ro.docx), including all printed alternative tariffs. A printed zero in a catalogue is not a universal PIT exemption or permission to fill every monetary field with zero.

Apply annex 4's actual validation conditions to the working paper: uppercase Latin-script names with the permitted diacritics/hyphen; registered 13-digit IDNP or the stated zero exception; registered 11-digit CPAS or its zero exception; never both zero and, when both exist, the same person. Dates use `dd.mm.yyyy`. Ordinary category 101 uses the reported month's date range. Preserve the actual category/occupation/tariff and each field's applicability. For employer-funded ordinary sickness category 15311, the requirements leave columns 9 and 11 empty and use the benefit field; do not add the benefit to the ordinary contribution base merely because it is paid with wages. [Annex 4 part I, points 1–14](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an_4_94md.docx).

For ordinary consistent branches, reconcile nominal contributions by the applicable 29%/24% or 39%/32% branch; independent doctor 172, fixed founder 127, fixed justice 174 and day-worker 14912 have their separate summary routes. The agriculture summary distinguishes total 24% from the employer-funded 18% component and requires its actual activity/category conditions. Annex 4 excludes IT-park categories 162/16211 from the ordinary nominal total; do not turn that reporting exclusion into exemption from the single tax. The sum of **absolute** manual-versus-calculated contribution differences in summary rows 1.1–1.4 must not exceed **MDL 50** under the printed validation rule. This is a validation tolerance, not a reduction in the legal contribution. [Annex 4 part II, points 1–27](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an_4_94md.docx).

The attached requirements retain overlapping start-date rules in part-I points 7/8, different-length field-mask lists in 12/13 and inconsistent exclusion prose/error text in part-II point 22. Keep those exact texts; do not invent one universal exception algorithm from them. For an affected special category or changed portal validation, confirm the applicable instruction and accepted filing outcome. The full evidence is retained; no live portal acceptance is claimed.

For assumed ordinary category-101 employees already established to use the 24% branch, social bases MDL 40,000 and MDL 60,000 give contributions MDL 9,600 and MDL 14,400. A separate already-classified 15311 benefit of MDL 1,500 goes in the benefit field: the nominal social-base total remains MDL 100,000, benefit total MDL 1,500 and contribution total MDL 24,000. This checks the reporting bridge, not actual eligibility or the payroll PIT/medical calculation.

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

**2026 version and special entries.** The preceding 19 September 2024 consolidation and current text agree on the ordinary column mapping above. Amending Order 59/2026 became effective on **8 May 2026**. Its added note limits the specified taxi `TAXI`/`SAL` split around **10,000 MDL per employee per month**, and the associated columns-8–12 restriction, to **1 January–30 June 2026 inclusive**. Do not carry that special annual-report rule into July–December. It also deletes the older day-worker personal-exemption sentence; current annex 2 lists only columns **1, 2, 3, 5, 6, 7 and 16** for covered day-worker remuneration. The prior sentence does not establish a current entitlement contrary to the Code and payroll regulation. The actual current form and complete country list have now been read separately below; missing annual-prefix values and authenticated portal acceptance remain unresolved. [Pre-amendment annex 2][ialspre]; [current annex 2][ials]; [Order 59/2026 points 1, 3][ialsamend]; [Code art. 33(1^1)][code]; [regulation point 9][reg].

### Reconcile the actual IALS21 form and country list

The current Order 95 link supplies the original IALS21 `.doc`, now retained unchanged. Both pages were read after local conversion for rendering; the actual sixteen-column main form and four-column dependent annex agree with the field method above. The printed column-13 total is **columns 8+9+10+11+12**. Only actual legally allowed reliefs belong in those fields: P/M remain alternatives, and the spouse field requires the current specific entitlement. The form's control sum is **total column 16**, not gross income column 6 or medical premiums column 14. Record the entry count and authorised director/chief-accountant signatures. The legacy social column 15 does not establish a current ordinary employee 6% deduction. [Actual IALS21 form, both pages](https://www.legis.md/UserFiles/Image/RO/2021/mo239-248md/95_an_1.doc), read 31 October 2026; [current completion instructions][ials].

The actual Order 95 annex-3 classifier uses three-letter entries, including `DEU` Germany, `MLT` Malta, `MDA` Moldova, `ROU` Romania, `GBR` United Kingdom and `USA` United States. Apply the current instruction's rule to **leave column 7 blank for a Moldovan citizen** and, for multiple citizenships, use the citizenship presented in the employment/civil relationship. The list's MDA entry does not override that blank-field rule. Preserve the annex's legacy labels and `Liberland/LBL` observation without asserting current ISO status or live portal acceptance. The annual-prefix omission in the current instructions remains unresolved by these attachments. [Actual country list](https://www.legis.md/UserFiles/Image/RO/2021/mo239-248md/anexa%20nr_3_95.docx); [Order 95 annex 2, preamble and column 7][ials].

### Annual IT-park salary information: actual ISAPTI17 and employee statement

Use the current Order 135 annexes **3–4** for the annual **ISAPTI17** information to SFS and **5–6** for the separate information delivered to each employee. Allfour original DOCX attachments and all four rendered pages were read. These are salary-payment information outputs under Code 374, separate from ordinary IALS21, IPC21 nominal insured-income reporting and the employer's monthly IU17 tax computation. The annual SFS deadline is **25 January** following the payment year; the employee-information deadline is **1 March**. [Current Order 135][parkorder]; [actual ISAPTI17][isaptiactual]/[instructions][isaptiinstructions]; [employee information][parkemployee]/[instructions][parkemployeeinstructions]; [Code 374](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

ISAPTI17's header requires registered taxpayer name/fiscal code, **four-digit CAEM-2**, actual park registration code, **four-character head-office CUATM**, SFS office, calendar year, actual submission date and number of entries. Number records consecutively over the whole statement, across pages. In the actual table, **column 2** is the employee fiscal identifier, **3** the name, **4** total covered labour-law salary payments to or for that employee, and **5** the months active in the park. The printed **control sum is total column 4**, with the month-total cell marked unused. Keep the head-only or authorised two-signature method from instruction 13; a printed accountant-signature line does not override that instruction. [Annex 3 fields/footer][isaptiactual]; [annex 4 instructions 1–13][isaptiinstructions].

The employee statement identifies the resident employer and employee by names/fiscal codes and the year. Its two columns are the covered salary-payment amount and the employee's park-active months. Keep the form's own **number/date** and **proof that it was sent or handed to that employee**. This form is not an instruction to send a draft without the firm's normal approval. Reconcile its amount/month fields to the corresponding annual SFS record, rather than copying the forecast insured-income base or the employer's 7% turnover tax. [Annex 5 fields and delivery-evidence note][parkemployee]; [annex 6 instructions 1–3][parkemployeeinstructions]; [Code 374(1)(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

For an assumed matched payment-year ledger, employee A has covered salary payments **30,000** and **two** active months; employee B has **20,000** and **one**. The annual monetary control sum is **50,000**, and each employee statement carries that employee's own amount and months. Do not replace 50,000 with the IPC21 fixed insured-income reference or sum active months into an asserted current-month headcount. The source calls the field “months active”, while Code 374 describes months whose paid salary was covered by the single tax: where accrual/payment cross a regime/year boundary, apply Code 375 and retain that reconciliation; these forms alone do not verify every cross-year month-count/portal rule. [Actual forms 3/5][isaptiactual]; [annex 4 points 11–12][isaptiinstructions]; [annex 6 points 2–3][parkemployeeinstructions]; [Code 374–375](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

### Eligible small-business annual reporting through UNIF25

Current Code 92(8) replaces the ordinary annual information-return route for the specified non-VAT individual entrepreneur/farm with annual average staffing not above five; the unified report is due 25 March. It is an exception to annual 92(3), **not a repeal of monthly payment/reporting under 92(1)–(2)** or the separate recipient-information duty. Use the actual whole-year category and change dates in the [individual-income Guide](moldova-income-tax.md). [Code 92(1)–(4),(8)][code]; [SFS Order 300/2025 and actual UNIF25 form][unif25order].

Actual table 3 has 16 columns: sequence 1; recipient fiscal identifier 2 and name 3; qualifying spouse identifier 4; income-source code 5 from the monthly report; actual annual payments 6, including prior-period salary paid this year; citizenship-country code 7; reliefP/M/Sm/N/H in 8–12; total relief 13; medical premiums withheld 14; printed individual-social field 15; PIT withheld 16. For a Moldovan citizen, 7 is blank; with multiple citizenships, the instructions use the citizenship presented in the employment/civil relationship. Use the referenced approved classifier rather than a guessed residence-country code. The dependent annex records the employee identifier and separate N/H dependent identifiers. [Actual form table 3 and dependent annex][unif25form]; [instructions 119–120][unif25instructions].

Current entitlement controls the relief fields: P and M are alternatives; Sm requires the specific current spouse conditions. The printed social field 15 does not create an ordinary employee 6% social deduction, and instruction 119 supplies no completion paragraph for that field. Preserve the current category-based [social method](moldova-social-contributions.md). For covered day workers, the instructions list fields 1,2,3,5,6,7,16; their older following sentence allows personal relief, but **current Code 15(a¹) expressly excludes chapter 4 exemptions**. Do not apply that stale sentence. MF Order 59/2026 removes the parallel old text from IALS21; it does not establish an amendment to UNIF25. [Current Code 15(a¹),33–35][code]; [UNIF25 instructions 119–120][unif25instructions]; [MF Order 59/2026 point 1(d)][ialsamend].

Reconcile table 3 payment and withholding totals to the actual monthly records and recipient evidence. UNIF25's supplied annex has tables 1,3,4,6,7; there are no separate tables 2/5 in that approved binary. Neither those numbering gaps nor the legacy individual-social header prove that monthly CNAS/CNAM declarations have been completed. Actual classifier values, field 15/portal validation and inconsistent-source handling beyond these stated current-law rules remain open. [Actual full form][unif25form]; [Code 92(2),(8)][code].


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


## Ask the client first

- Supply employer registration/activity/category and the worker's actual contract, residence, identity/IDNP/CPAS, start/end dates, hours and any special-regime or cross-border facts.
- Supply accrued and paid gross by component/date, benefits/reimbursements, leave/sickness periods, prior advances, other deductions and the underlying entitlement calculations.
- Supply the signed exemption application, residence/qualifying-category documents, spouse non-use, dependents' relationship/income evidence and the dates rights/applications changed. Was the same-period personal exemption used elsewhere?
- Supply cumulative payroll/personal records, actual medical premiums and prior PIT, including joiners, leavers, later-year arrears, special-regime periods and corrections.
- Supply IPC21/IRM19 and annual information filings with accepted receipts, nominal categories/periods and treasury-account statements, payments, refunds and notices.
- For treaty/social coverage, supply exact work locations/dates, payer/PE cost allocation, operative treaty, residence certificate and competent-authority coverage evidence.

## Sources

**Bounded source review, 31 October 2026.** The [independent review record](../../evidence/ledgers/md-country-evidence/independent-review/FINAL-REVIEW.md) covers the stated source/claim scope. Ordinary gaps below remain unresolved. This Guide remains a source-cited draft, without accountant attestation or comprehensive coverage.

Primary-source reads on 30–31 October 2026, with individual dates below.

| Official source | Scope actually read | Read on |
|---|---|---|
| [UNIF25 actual full form](https://www.legis.md/UserFiles/Image/RO/2025/mo309-312ro/an1_300ro.docx), [complete instructions](https://www.legis.md/UserFiles/Image/RO/2025/mo309-312ro/an2_300ro.docx) and [current Code interfaces](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro) | Remaining form pages 3–4/instructions 36–136 read and visually checked; selected supporting/payment/property methods applied, with source inconsistencies and implementation limits explicit. Earlier core observation preserved | 2026-10-31 |
| [BNM monetary-policy decision, 6 November 2025, point 1](https://bnm.md/en/node/69226) | Fetched 6.00% short-term base input; calendar-2026 daily percentage derived with Code 228(3), rather than copied from an old rate. | 2026-10-30 |
| [Current Fiscal Code][code] | Selected employment, benefit, exemption, deduction, filing, nonresident/treaty and enforcement provisions cited above | 2026-10-30 |
| [January Code][jan] | Personal/spouse/dependent and individual-deduction provisions compared to current selected text | 2026-10-30 |
| [BNM DPMC8 loan report, configured November 2025][loanreport] | Domestic-currency new individual-total loans over five years: 8.32%; query settings and returned report text retained, not the default latest report | 2026-10-30 |
| [Official regulation loan-formula image][loanformula] | Formula visually read in browser; raw binary retrieval returned 403, so no retained PNG file is claimed | 2026-10-30 |
| [Government Decision 697, 1 January 2026 regulation][reg] | Scope, benefits, exemption/documents and full rendered computation/correction text; attached annex forms remain unretained; embedded loan formula visually read separately | 2026-10-30 |
| [MF Order 95/2020 current annex 2][ials], [preceding consolidation][ialspre] and [actual Order 59/2026][ialsamend] | Directly read annual IALS21 columns, dependent/correction method and May amendment with January–June taxi limit; current form/classifier attachments separately retained/read below; omitted annual-prefix values remain unverified | 2026-10-30 |
| [Order 94/2020, 30 April 2026 consolidation][ipc] | Reporting/correction rules, preamble, ordinary table-1 fields and selected nominal table-2 instructions; full annex-3/4 code set not yet certified | 2026-10-30 |
| [Order 150/2018, 3 April 2026 CET18 instructions][cet] | Individual categories/departure timing and ordinary field mappings; not a replacement for entity/professional returns | 2026-10-30 |
| [CNAS 2026 instructions][cnas] | Complete retained authority instruction, especially points 8–13, 23–33, 40–41 | 2026-10-30 |
| [Law 489/1999][social] | Selected charging/minimum/arrears and exclusion provisions; direct tariff-annex retention remains open in social Guide | 2026-10-30 |
| [Law 1593/2002][health] | Medical categories, base, timing, reporting and penalty provisions | 2026-10-30 |
| [Medical budget, Law 321/2025 art. 4][medicalbudget] | Current percentage premium and fixed-category amounts | 2026-10-30 |
| [Social budget, Law 320/2025 arts. 3–4][socialbudget] | Original 2026 fixed amounts/daily social charge; later charging-version comparison remains open | 2026-10-30 |
| [Current IALS21 form](https://www.legis.md/UserFiles/Image/RO/2021/mo239-248md/95_an_1.doc) and [country classifier](https://www.legis.md/UserFiles/Image/RO/2021/mo239-248md/anexa%20nr_3_95.docx) | Original DOC retained unchanged; local conversion/read of both form pages and all eight classifier pages. Actual totals, signatures, sixteen columns/dependent annex and own three-letter codes; annual-prefix/portal and atypical-code limits retained. | 2026-10-31 |
| [Current IPC21 form](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an1_94md.docx), [categories](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an3_94ro.docx) and [requirements](https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an_4_94md.docx) | All three/four/five pages read and visually inspected; actual source/insured codes, table controls, nominal field masks and exception conflicts retained. Official validation rules read; live portal not tested. | 2026-10-31 |

| [Current ISAPTI17 form][isaptiactual]/[instructions][isaptiinstructions] and [employee statement][parkemployee]/[instructions][parkemployeeinstructions] | Allfour original DOCX/allfourrendered pages read. Header/record/paid-salary/month fields, monetarycontrolsum, signatures and separateemployee-delivery evidence mapped; cross-regime month counts and authenticated implementation remain explicit | 2026-10-31 |

| [Order 126 IRM19 form][employ3], [instructions][employ4], [technical requirements][employ4s1] and [relations][employ7]/[termination][employ8]/[risk][employ9] classifiers | Original files/full 11 rendered pages read; event/deadline/identity/field/code/correction methods and 30 April 2026 changes applied. Specific 158 exception, additional CNAM paper route and source/portal limits explicit; shared annex 9 also supports CAS | 2026-10-31 |

Not yet confirmed: full 2026 commencement/form-version comparison beyond the selected January/current, IALS21 May and actual IRM19/CAS18-AN April-amendment checks; full current CNAS special-pension occupation list, paternal technical boundary-day counting and authenticated IRM19 correction/automatic 158-field behaviour;  IALS21 omitted annual-prefix values and atypical country entries, IPC21 duplicated date/field-mask and part-II exclusion conflicts, authenticated portal validation, all liquidation/historical correction routes and case-specific nominal special-category implementation; remaining Government benefit/travel/food/training implementation, meal-ticket nominal amount and non-cash exceptions; foreign-currency/FX-linked loan benchmark choice, missing-observation handling, exact transaction-day/conversion/final-rounding and no-cash-wages remittance; statutory entitlement computation for contractual wage/leave/sickness/severance and execution deductions; taxpayer-specific pre-2026 medical-penalty transition and arrears-account allocation; complete IT-park/software-occupation eligibility and historical entry/exit treatment; treaty-by-treaty employment/social coverage. The old 2025 figures 5,500 minimum and 16,100 forecast, employee 6%/27% net-pay model, universal 32% hazardous-work default, blanket missing-IDNP refusal, automatic personal exemption without application, non-cumulative monthly formula and assumed 2026 continuity are corrected or retained as historical subjects, not certified current rules. The old dividend/farming/winnings summary belongs to the individual/corporate income classifications; a statutory peasant-farm 7% income-tax rate is not a general payroll or farming-distribution withholding rate. The payroll domain stays partial until ordinary gaps are closed.

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

[unif25order]: https://www.legis.md/cautare/getResults?doc_id=148910&lang=ro
[unif25form]: https://www.legis.md/UserFiles/Image/RO/2025/mo309-312ro/an1_300ro.docx
[unif25instructions]: https://www.legis.md/UserFiles/Image/RO/2025/mo309-312ro/an2_300ro.docx

[parkorder]: https://www.legis.md/cautare/getResults?doc_id=154298&lang=ro
[isaptiactual]: https://www.legis.md/UserFiles/Image/RO/2025/mo544-546ro/an_3_135md.docx
[isaptiinstructions]: https://www.legis.md/UserFiles/Image/RO/2025/mo544-546ro/an_4_135md.docx
[parkemployee]: https://www.legis.md/UserFiles/Image/RO/2022/mo129-133md/an_5_135md.docx
[parkemployeeinstructions]: https://www.legis.md/UserFiles/Image/RO/2022/mo129-133md/an_6_135md.docx

[employ3]: https://www.legis.md/UserFiles/Image/RO/2024/mo%20282-285ro/a_3_126md.docx

[employ4]: https://www.legis.md/UserFiles/Image/RO/2025/mo297-300ro/an_4_126md.docx

[employ4s1]: https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an_4-1_126md.docx

[employ6]: https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an_6_126md.docx

[employ7]: https://www.legis.md/UserFiles/Image/RO/2019/mo59-65md/anexa%20nr_7_126.doc

[employ8]: https://www.legis.md/UserFiles/Image/RU/2022/mo%20267-273%20ru/an_8_126.doc

[employ9]: https://www.legis.md/UserFiles/Image/RO/2026/mo186-189ro/an_9_126md.docx

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
