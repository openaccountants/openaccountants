---
name: sl-income-tax
description: "Sierra Leone personal income and PAYE workpaper for the 2026 research year. Use for resident employee withholding, a taxable benefit, documented expense reimbursement, redundancy payment, an allowance or a non-resident employment question. It traces the annual band table to the signed Finance Act copy, records the official currency conversion and distinguishes a steady monthly allocation from a complete live payroll method. The workpaper reconciles employment receipts, statutory exclusions and eligible pension deductions before applying a rate. It routes residence and foreign-income questions to the country cross-border Guide. All predecessor topics are mapped to a correction, source rule or explicit hold. Two cases recompute ordinary withholding and the treatment of a qualifying termination payment. Current forms and the complete amendment chain remain unfinished."
jurisdiction: SL
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 1.0
tax_year_notes: "2026 intake; read historical statutory baseline and specific enacted amendments, with current NRA corroboration; full law/forms not closed"
---

# Sierra Leone Personal Income Tax and PAYE v1.0

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Resident and temporarily resident employees whose withholding follows First Schedule PartI, and non-resident employees whose withholding follows Second Schedule PartII. Establish status using [residence and foreign income](sl-cross-border.md); nationality alone does not select the tax schedule. The employer's withholding duty survives other deductions and laws restricting attachment of pay. [Income Tax Act s.116, NRA2017 consolidation](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).

Personal assessable income is broader than salary: the opened ss.22-25 distinguish employment, business, property and other income or gains, excluding exempt amounts. This is primarily an employment/PAYE workpaper. Sole-trader regimes, capital gains, rental and specialist-business calculations require their own full reconciliation; do not tax every gross receipt through a monthly salary table. The NRA consolidation is expressly unofficial and ends in2017; identified later Acts and current authority guidance do not prove the complete operative2026 chain. [Income Tax Act ss.22-25](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf). Independent review of this rewrite is pending.

## Rates, bands and thresholds

The signed NRA-hosted Finance Act2020 s.21(a) replaces First Schedule PartI with **annual** old-Leone amounts. The Bank's notice gives newLe1 = oldLe1,000. The table below converts those endpoints; its monthly column is one-twelfth for a steady twelve-month workpaper, not an authenticated cumulative/partial-period employer instruction. The NRA's February2026 guidance separately confirms the monthly tax-free amount. [Finance Act2020 s.21(a)](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2020_d8deee2366.pdf); [Bank notice, denomination table](https://bsl.gov.sl/Public%20Notice%20on%20Redenomination.pdf); [NRA employer session, 13February2026](https://nra.gov.sl/news/87).

| Annual chargeable-income slice in new Leones | Steady monthly slice in new Leones | Marginal rate | Official source |
|---|---|---|---|
| Through7,200 | Through600 | 0% | [FA2020 s.21(a)](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2020_d8deee2366.pdf); [Bank conversion](https://bsl.gov.sl/Public%20Notice%20on%20Redenomination.pdf) |
| Above7,200 through14,400 | Above600 through1,200 | 15% | [FA2020 s.21(a)](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2020_d8deee2366.pdf); [Bank conversion](https://bsl.gov.sl/Public%20Notice%20on%20Redenomination.pdf) |
| Above14,400 through21,600 | Above1,200 through1,800 | 20% | [FA2020 s.21(a)](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2020_d8deee2366.pdf); [Bank conversion](https://bsl.gov.sl/Public%20Notice%20on%20Redenomination.pdf) |
| Above21,600 through28,800 | Above1,800 through2,400 | 25% | [FA2020 s.21(a)](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2020_d8deee2366.pdf); [Bank conversion](https://bsl.gov.sl/Public%20Notice%20on%20Redenomination.pdf) |
| Above28,800 | Above2,400 | 30% | [FA2020 s.21(a)](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2020_d8deee2366.pdf); [Bank conversion](https://bsl.gov.sl/Public%20Notice%20on%20Redenomination.pdf) |
| Non-resident employment withholding | Separate25% schedule rate; not a resident marginal band | 25% | [FA2024 s.12(b), Second Schedule PartII](https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2024_0d6d83e684.pdf) |

Tax each slice, not all pay at the highest reached rate. The annual-to-monthly allocation, irregular pay, arrival/departure, multiple employers and annual reconciliation need the prescribed current instructions before filing. The source copy's printed publication chronology and complete subsequent amendment chain remain in the review holds.

## The base

1. Inventory cash and non-cash employment receipts. Baseline s.23 includes ordinary pay, overtime, commissions, bonuses, employment gifts, allowances, consideration for employment conditions, pensions subject to specified exceptions, private vehicle use, housing, utilities, domestic assistants, meals, waived obligations and specified credits/director withdrawals. Start from actual receipts and benefits; a payslip label does not settle tax. [Income Tax Act s.23(1)](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).
2. Value benefits under their specific rule. The general baseline is the higher of employer cost or employee market value unless s.23(2) specifies another value. Housing uses market rent less employee payment; utilities use reimbursement/discharge; a domestic assistant uses total employment income paid for services to the employee less the employee's payment; meals use employer cost less the employee's consideration; debt waiver uses the waived amount. Vehicle valuation needs the current Ninth Schedule, not a guessed percentage. These historical valuation measures are not cleared for current payroll: the opened Finance Act2018 s.12 replaces s.176(9) with market value for all benefits in kind under s.23. Its interaction with the older general/specific measures and later law remains held; do not select an older valuation merely because it gives less tax. [Finance Act2018 s.12, physical5/printed9](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2018_1_b96b9c2841.pdf). [Income Tax Act s.23(1)(c),(2)](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).
3. Test each exclusion separately. Actual employer-paid/reimbursed medical expenses, qualifying employer-requested relocation housing, documented employer-business expenses and supported expense portions of allowances have different conditions. Foreign/temporarily resident appointment/termination/vacation passages and complying-retirement contributions also have specific limits. Small fringe benefits have an administrative-impracticability condition. Do not turn this into a blanket exemption for every allowance or reimbursement. [Income Tax Act s.23(3)(a)-(i), historical baseline](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).
4. Finance Act2026 replaces s.23(3)(h) with the exclusion for any amount of genuine redundancy, termination/loss-of-office/employment or similar payments, and repeals Ninth Schedule paragraph2. That Act is deemed operative from1January2026 unless otherwise provided. Classify the payment from contracts and termination evidence; relabelling ordinary salary or a bonus does not meet the assumption. [Finance Act2026 ss.1,6,15(a)](https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2026_121df05d9b.pdf).
5. The old consolidated-allowance amount appears in baseline s.23(3)(j) as oldLe6,000,000; denomination conversion alone makes that newLe6,000. The provision does not itself state a monthly500 allowance. Authenticate the applicable period and current payroll allocation before applying that shorthand, and preserve the separate expense exclusions. Leave pay also needs the2019 insertion and2021 gross-to-basic wording change reconciled against the older exclusion; the2021 printed section-reference inconsistency is not silently corrected here. [Income Tax Act s.23(3)(j)-(k)](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf); [Bank conversion](https://bsl.gov.sl/Public%20Notice%20on%20Redenomination.pdf); [Finance Act2019 s.5](https://webtestcms.nra.gov.sl/uploads/2019_Finance_Act_1_8136241a71.pdf); [Finance Act2021 s.10](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2021_be1efb0bcc.pdf).
6. Obtain the actual deductible employee NASSIT amount from the [social-contribution workpaper](sl-payroll-social.md), not a percentage of every cash item or the employer's cost. The NRA's February2026 PAYE explanation confirms the employee contribution is deducted before PAYE. For contributions to a complying retirement fund, baseline s.38(1)-(2) distinguishes employer and individual limits; the individual's30% employment-income limit is reduced by contributions made by an employer for their benefit. Section38(3) separately treats an expense or non-complying-fund contribution to acquire pension/annuity rights as a deduction against pension/annuity receipts under Ninth Schedule paragraph4, rather than the same general employment-income deduction. This is not permission to deduct every pension payment twice. Full current limits and interaction remain to be reconciled. [NRA February2026 explanation](https://nra.gov.sl/news/87); [Income Tax Act s.38](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).
7. Apply the correct schedule to the resulting chargeable employment amount, retain each marginal slice and reconcile tax withheld to the payslip/ledger. The opened s.125 makes tax withheld under s.116 on non-resident payments final for that income, without aggregation or refund under that rule; treaty and current-law checks remain separate. Do not substitute a resident annual computation merely because it produces less tax. [Income Tax Act ss.116,125](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf); [Finance Act2024 s.12(b)](https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2024_0d6d83e684.pdf).

## Deadlines and filing

Baseline s.130(1) requires amounts withheld **or that should have been withheld** to be paid within15days after the withholding month. Baseline s.117(6) separately requires the prescribed monthly PAYE/withholding return with gross payments and related withholding. An employer's payment alone does not prove the return is accepted. [Income Tax Act ss.117(6),130(1)](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).

For the opened annual-return framework, distinguish ordinary s.97 obligations from s.98's resident-individual exceptions: income below the nil-rate amount, or income excluding final-withholding receipts consisting only of fully withheld single-employer employment or a fully withheld pension, unless the Commissioner expressly requires a return in writing. The separate2020 amendment says a PAYE taxpayer **may** file and settle/reclaim the specified difference120days after year end. It is not a universal mandatory120-day deadline for all non-PAYE taxpayers. The2020 inserted subsection numbering overlaps the unofficial consolidation; complete current procedure/priority is not cleared. The [company Guide](sl-corporate-income-tax.md) owns the ordinary annual-return clock and2026 format amendment. [Income Tax Act ss.97-98](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf); [Finance Act2020 s.10](https://webtestcms.nra.gov.sl/uploads/Finance_Act_2020_d8deee2366.pdf).

Baseline withholding certificates go to employees within28days after year end or7days after leaving employment; a return filer attaches relevant certificates. Employers retain per-payee payment/withholding records and file the prescribed year-end statement within28days after the assessment year, or further time allowed by the Commissioner (s.128(2)). Current combined electronic reporting, return fields and applicable certificate format remain unverified. [Income Tax Act ss.127-128](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).

Build the workpaper in this order: identify employer/TIN and employee/status/period; reconcile cash/benefits and exclusions; establish eligible deductions; calculate and reconcile withholding; prepare the actual prescribed return and schedules; retain submission acknowledgement, payment reference and employee certificate. **The public forms catalogue's link labelled PAYE Return currently opens tax-clearance guidelines, not a PAYE return.** It was opened and rejected as filing-form evidence. No live portal/field sequence or successful filing is certified. [NRA forms catalogue](https://nra.gov.sl/forms); [actual linked PDF, TCC guidelines](https://webtestcms.nra.gov.sl/uploads/Tax_Clearance_Certificate_Guidelinesv1_8163f3f1c5.pdf).

## Penalties and interest

The2025 replacement s.150(1)(c)-(d) distinguishes monthly late filers and non-filers by taxpayer class. Annual-return amounts are different and remain in the [company Guide](sl-corporate-income-tax.md), together with the source classification thresholds. Apply the actual legal class; do not invent a micro-taxpayer figure. The replacement s.97A classifies filing within30days after the due date as late filing, and filing after30days as non-filing; s.150(1) is expressly subject to s.97A. Preserve that boundary when selecting the monthly penalty column. [Finance Act2025 ss.9-10](https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2025_beb680faed.pdf).

| Monthly return category | Late-filer penalty | Non-filer penalty | Official source |
|---|---|---|---|
| Large | NLe5,000 | NLe10,000 | [FA2025 s.10, s.150(1)(c)-(d)](https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2025_beb680faed.pdf) |
| Medium | NLe2,500 | NLe5,000 | [FA2025 s.10, s.150(1)(c)-(d)](https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2025_beb680faed.pdf) |
| Small | NLe500 | NLe1,000 | [FA2025 s.10, s.150(1)(c)-(d)](https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2025_beb680faed.pdf) |

Section150(3) expressly extends the requirements/penalties to PAYE and withholding, but has internal references needing reconciliation. The opened withholding rules also impose the payer's liability for failure to withhold and restrict employer recovery from the employee. Current late-payment interest, penalty overlap and recovery/appeal priority require their complete later procedural chain. No fixed monthly interest or old redenominated offence fine is guessed. [Finance Act2025 s.10, s.150(3)](https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2025_beb680faed.pdf); [Income Tax Act s.129](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).

## Cross-border points

Use [residence/foreign-income](sl-cross-border.md) for the actual presence exclusions, split-year and temporary-resident conditions. Different payment location or citizenship alone does not change the employment-source or residence answer. The historical consolidation also prints a US-dollar remittance rule for expatriate PAYE; its current operation and distinction from tax residence are held, not ignored or adopted as a universal currency instruction. Treaty relief, foreign employment, credit and social contributions remain separate checks. [Income Tax Act s.130, printed duplicate subsection(4)](https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf).

## Two worked examples that recompute

Assume the source rules and steady monthly allocation are verified applicable, a resident employee has NLe3,000 ordinary employment receipts and an independently established deductible employee contribution of150. Assume no other deduction, allowance exemption, benefit or special-period adjustment. Taxable monthly amount is2,850; marginal PAYE is90+120+150+135 =495. Cash after this contribution and PAYE is2,355. The contribution input is a verified fact, not a newly asserted rate on all gross pay.

```oa-check
name: Ordinary steady monthly employee workpaper
inputs:
  ordinary_employment_receipts: 3000
  verified_employee_deduction: 150
steps:
  - chargeable_monthly: ordinary_employment_receipts-verified_employee_deduction
  - band_15: min(max(chargeable_monthly-600,0),600)*0.15
  - band_20: min(max(chargeable_monthly-1200,0),600)*0.20
  - band_25: min(max(chargeable_monthly-1800,0),600)*0.25
  - band_30: max(chargeable_monthly-2400,0)*0.30
  - paye: band_15+band_20+band_25+band_30
  - cash_after_paye_and_contribution: ordinary_employment_receipts-verified_employee_deduction-paye
expected:
  chargeable_monthly: 2850
  band_15: 90
  band_20: 120
  band_25: 150
  band_30: 135
  paye: 495
  cash_after_paye_and_contribution: 2355
```

Now add a genuine NLe1,000 termination payment proved to satisfy the2026 exclusion, with all other assumptions and the deductible contribution unchanged. Correct ordinary withholding remains495; putting the excluded payment into the salary base instead gives795, an excess300. If the payment is really ordinary remuneration or a bonus, this exclusion assumption fails. The classification decision is evidenced, not chosen to minimise tax.

```oa-check
name: Qualifying termination payment versus ordinary salary treatment
inputs:
  ordinary_receipts: 3000
  verified_employee_deduction: 150
  qualifying_termination: 1000
steps:
  - correct_base: ordinary_receipts-verified_employee_deduction
  - incorrect_base: correct_base+qualifying_termination
  - correct_paye: min(max(correct_base-600,0),600)*0.15+min(max(correct_base-1200,0),600)*0.20+min(max(correct_base-1800,0),600)*0.25+max(correct_base-2400,0)*0.30
  - incorrect_paye: min(max(incorrect_base-600,0),600)*0.15+min(max(incorrect_base-1200,0),600)*0.20+min(max(incorrect_base-1800,0),600)*0.25+max(incorrect_base-2400,0)*0.30
  - excess_withholding: incorrect_paye-correct_paye
expected:
  correct_base: 2850
  incorrect_base: 3850
  correct_paye: 495
  incorrect_paye: 795
  excess_withholding: 300
```

## Ask the client first

Obtain employment/status and arrival/departure facts; each cash/benefit/reimbursement/termination item and supporting evidence; actual employee/employer pension contributions and exemptions; period, other employers and non-employment income; TIN, notices, current return/certificates and payments; and any treaty or foreign-income claim.

## Sources

| Primary source and actual read scope | Official URL | Read on |
|---|---|---|
| NRA-hosted unofficial2017 Income Tax Act consolidation: physical24-26 ss.22-23;35 s.38;61-63 ss.97-99;73-74 s.116/monthly return;77-80 ss.124-130 and neighbours, selectively read. | https://webtestcms.nra.gov.sl/uploads/Income_Tax_Act_2000_as_amended_to_Finance_Act_2017_1_83760e046c.pdf | 2026-11-01 |
| Finance Act2018 s.12, physical5/printed9 replacement of s.176(9), with adjacent section context actually read from the cached official copy. Web reopening returned502; no fresh download claimed. | https://webtestcms.nra.gov.sl/uploads/Finance_Act_2018_1_b96b9c2841.pdf | 2026-11-01 |
| NRA-posted signed Finance Act2020 scan: cover1, commencement2, PAYE annual-return insertion4 and band-table amendment7-8 read; original cover/band scans visually checked. Printed chronology has an unresolved footer issue. | https://webtestcms.nra.gov.sl/uploads/Finance_Act_2020_d8deee2366.pdf | 2026-11-01 |
| Finance Act2019 s.5 leave-allowance insertion and Finance Act2021 s.10 gross/basic change and adjacent provisions read; latter prints section3 while margin says23. | https://webtestcms.nra.gov.sl/uploads/2019_Finance_Act_1_8136241a71.pdf ; https://webtestcms.nra.gov.sl/uploads/Finance_Act_2021_be1efb0bcc.pdf | 2026-11-01 |
| Finance Act2024 s.12(b), physical10/printed18 non-resident withholding table and neighbouring scope read. | https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2024_0d6d83e684.pdf | 2026-11-01 |
| Finance Act2025 ss.9-10, physical8-9/printed8-9 annual/monthly distinction and PAYE reference read. | https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2025_beb680faed.pdf | 2026-11-01 |
| Finance Act2026 ss.1,6,15(a), physical2,6,9; employment exclusion and Ninth Schedule repeal read with neighbours. | https://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2026_121df05d9b.pdf | 2026-11-01 |
| Bank notice11August2021: full one-page denomination table read, new1 = old1,000. | https://bsl.gov.sl/Public%20Notice%20on%20Redenomination.pdf | 2026-11-01 |
| NRA13February2026 employer-session article: full main article read; threshold, contribution method and2026 exclusion corroboration. Not a replacement for full enacted law or return instructions. | https://nra.gov.sl/news/87 | 2026-11-01 |
| NRA public forms catalogue and actual link labelled PAYE Return: clicked destination PDF is TCC guidelines, not accepted as payroll-form evidence. | https://nra.gov.sl/forms ; https://webtestcms.nra.gov.sl/uploads/Tax_Clearance_Certificate_Guidelinesv1_8163f3f1c5.pdf | 2026-11-01 |

Not yet confirmed: Complete operative2026 legal/amendment chain and authentic current consolidation; publication chronology of the2020 source copy; current cumulative/monthly/irregular/partial-year PAYE instructions; consolidated-allowance period/allocation and current cap; leave-pay2019/2021/older-exclusion interaction and printed section reference; benefit/vehicle schedules, the2018 s.176(9) all-benefits market-value interaction with older s.23 methods, and pension limits; annual exception/refund/claim priority and overlapping2020 subsection numbering; current monthly/annual form fields, certificate/calendar integration, electronic acknowledgement/payment route; s.150 internal references and penalty/interest/procedural priority; historical expatriate USD remittance rule; sole-trader/property/capital/special regimes. The old general183-days-in-tax-year shortcut is corrected by the owning cross-border Guide; old flat monthly500allowance treatment and universal120-day annual return are not adopted. No actual filing or accountant attestation is proved. Independent income/PAYE review pending; IT-IND/PR remain partial.

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
