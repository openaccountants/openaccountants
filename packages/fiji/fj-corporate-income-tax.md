---
name: fj-corporate-income-tax
description: "Compute Fiji company income tax for 2026: chargeable income, listed-company rates, advances, non-resident payments and August amendments."
jurisdiction: FJ
tax_year: 2026
last_updated: 2026-11-16
version: 0.1
type: situation-rules
category: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Fiji Corporate Income Tax v0.1

## Scope

Use this for the ordinary company-income-tax computation and payment calendar in Fiji for tax year 2026. Resident companies include companies incorporated, formed or settled in Fiji or with any part of central management and control in Fiji. Their gross income includes worldwide sources; non-residents include Fiji-source income. A branch's Fiji taxable income must be identified before applying the company rate. [Income Tax Act, sections 2 and 14(3)](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

### Quick reference

| Item | Rate, base or deadline and conditions | Official source |
|---|---|---|
| Ordinary companies | 25% of chargeable income, before available credits. The old 20% ordinary rate is not the 2026 rule. | [LN 55/2023, regulation 3(b), Schedule paragraph 3(c)](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| SPSE-listed companies | 15% through the end of the seventh tax year from listing; 25% for more than seven tax years. The old 10% rule ended with tax year 2022 and is not a new-equity-only rate. | [LN 55/2023, regulation 2 and Schedule paragraph 3](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Return and balance payment | File within three months after year-end, including a company with a net loss; income tax is payable on the return due date unless another date is prescribed. Calendar-year 2026 normally ends with a 31 March 2027 return/payment date, subject to a valid extension. | [Income Tax Act, sections 104 and 108](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| Company advances | Last day of the sixth, ninth and twelfth months of the tax year; normally one-third multiplied by (the preceding assessed tax after foreign credit minus the part of that tax paid by withholding). Subtract withholding before dividing, not after. The small-advance single-payment exception is for non-companies. | [Income Tax Act, section 110(1)-(3)](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [Act 5/2024, section 5](https://frcs.org.fj/files/2024/08/Act-5-Income-Tax-Budget-Amendment-Act-2024.pdf) |
| New/unassessed company estimate | Each advance is one-third of estimated tax excluding tax collected by withholding, with the estimate filed by the first advance due date. | [Act 5/2024, section 5, replacing section 110(4)-(6)](https://frcs.org.fj/files/2024/08/Act-5-Income-Tax-Budget-Amendment-Act-2024.pdf) |
| Ordinary loss carryforward | Four tax years for losses incurred by 31 December 2018; eight for losses from 1 January 2019; oldest loss used first. Apply the substituted/transitional-year split in section 30(3A). | [Income Tax Act, section 30](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| International-flight aviation losses | From 1 August 2026, a company in the aviation sector offering international flights has a 15-year limit for losses incurred on or after 1 January 2019. This is not every company's limit. | [Act 14/2026, sections 1 and 3](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-14-Income-Tax-Budget-Amendment-No.-2-Act-2026.pdf?ver=1794354122) |
| Non-resident interest | Domestic 10% of gross Fiji-source interest within section 10, subject to exempt income, effective PE connection and the applicable treaty. | [Income Tax Act, section 10 and Rates Regulations Schedule paragraph 5(b)](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| Non-resident royalties and service fees | Domestic 15% of gross Fiji-source royalties, management fees, natural resource amounts and professional/independent-service fees within section 10, subject to its exemptions/PE conditions and treaty. Do not select a vague 5%-15% range. | [Income Tax Act, section 10 and Rates Regulations Schedule paragraph 5(a)](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| Dividends | No dividend charge under current non-resident withholding section 10; dividends received are exempt under Exempt Income Regulations Schedule Part 5(1). This does not turn salary, service fees or all shareholder receipts into dividends. | [Income Tax Act, sections 10 and 115, Exempt Income Regulations Schedule Part 5](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [Act 9/2025, section 2, dividend-definition change](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-9-Income-Tax-Budget-Amendment-Act-2025.pdf?ver=1794354122) |
| Withholding payment | Remit by the end of the calendar month following the month withholding was required; withholding itself is triggered by the earliest section 116 event, not just cash transfer. | [Income Tax Act, sections 116-117](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |

## Ask the client first

Obtain residence and management facts, financial/tax year and any approved substituted period, accounts and tax adjustments, tax-loss vintages, listing date and history, foreign income/tax evidence, prior assessment and withholding/advance credits, incentive approvals, related parties, non-resident contracts and treaty facts. Ask separately about inventory write-offs, new sports-facility expenditure, reorganisation, international aviation and all contractors reported after the August amendment.

## The method, step by step

1. **Fix residence, source and year.** Apply sections 2 and 14. A company's approved substituted year is not automatically the calendar year; section 36 determines the applicable law and treatment of a transition period. Companies normally use accrual accounting under section 37. [Income Tax Act, sections 2, 14 and 36-37](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).
2. **Reconcile accounts to chargeable income.** Gross income less deductions allowed by law is the section 13 base. Exclude exempt income and income subject to the distinct final taxes under sections 9-11. Test revenue expenses, trading stock, depreciation, intangibles and repairs under section 21. Add back private/capital costs unless specifically allowed, distributions, reserves, tax, fines and other section 22 disallowances. A payment deduction requiring withholding is deferred until the withheld tax is paid to FRCS. Do not deduct accounting depreciation and tax depreciation twice. [Income Tax Act, sections 13-14 and 21-22](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).
3. **Apply losses and supported incentives.** Track year-by-year use and expiry, including the special aviation rule in the table. Do not assume a hotel/tourism tax holiday, film rebate or other activity incentive merely from the business description: retain the original skill's incentive route, but apply it only after retrieving the exact regulation, approval, qualifying expenditure and continuing conditions. Those incentive amounts are not confirmed here. From 1 August 2026, section 25(22) allows a 150% deduction for expenditure on establishing a new sports facility; do not claim a deduction and the same expenditure again without reconciling the total treatment. An inventory/trading-stock write-off exceeding FJD 250,000 needs prior CEO approval under new section 40(7A). [Income Tax Act, section 30](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [Act 14/2026, sections 2-4](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-14-Income-Tax-Budget-Amendment-No.-2-Act-2026.pdf?ver=1794354122).
4. **Apply the correct company rate, then credits.** Use the listing history, not the amount of new equity, to choose the listed-company rate. Reconcile foreign tax credits, withholding credits and advances to evidence and statutory eligibility before deducting them. For the ordinary examples below all credits are assumed established and no special incentive is claimed. [Income Tax Act, section 8](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [LN 55/2023, regulations 2-3](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf).
5. **Calculate and calendar advances.** For a calendar-year company the ordinary advance dates are 30 June, 30 September and 31 December. Use the assessed-tax formula or the statutory estimate path as applicable; file an estimate/revision, reconcile earlier underpayments or overpayments and retain its basis. Do not copy the consolidation's obsolete one-ninth estimate wording: the enacted 2024 amendment prescribes one-third for tax year 2025 onwards. An underestimated current-year liability can create the section 110(11) shortfall penalty; its reasonable-care exception is not an automatic waiver. [Income Tax Act, section 110](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [Act 5/2024, section 5](https://frcs.org.fj/files/2024/08/Act-5-Income-Tax-Budget-Amendment-Act-2024.pdf).
6. **File and reconcile the balance.** Use FRCS's current approved company return and filing manner under Tax Administration Act section 3. Reconcile gross income, allowable adjustments, loss schedule, applicable rate, credits and advances to the return; retain the filed return, assessment and payment evidence. Obtain the actual approved return before entering figures because this skill has not verified live TPOS screen/box names. An extension must be evidenced, not assumed from having a tax agent. [Income Tax Act, sections 104 and 108](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [Tax Administration Act, section 3](https://frcs.org.fj/files/2026/06/TAX-ADMINISTRATION-ACT-2009-Revised-1-August-2025.pdf).
7. **Check non-resident payments and reporting.** Classify the payment and source before using the table. Section 10 excludes specified effectively connected PE income and exempt income; the former is instead taxed under section 8. Section 116 can require withholding when an amount is credited, capitalised or otherwise made available. Retain withholding certificates and pay on time. From 1 August 2026, a required Provisional Tax summary must include all contractors, including valid Certificate of Exemption holders, and gross payments whether tax was withheld or not. This does not itself make every contractor subject to a new rate. [Income Tax Act, sections 10, 113 and 115-121](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [Act 14/2026, section 7](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-14-Income-Tax-Budget-Amendment-No.-2-Act-2026.pdf?ver=1794354122).
8. **Treat exceptional transactions separately.** The 2026 changes add a defined equity-crowdfunding/small-offer/innovation-hub capital-gain exemption, a discretionary limited-minority reorganisation deferral and notification when a proposed capital-asset transfer fails or is incomplete. Do not treat these as a blanket exemption of business profits or an automatic reorganisation relief. Retrieve the transaction facts and the operative sections before advice. [Act 14/2026, sections 5-6 and 8](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-14-Income-Tax-Budget-Amendment-No.-2-Act-2026.pdf?ver=1794354122).

### Penalties and cross-border checks

Late filing and payment are separate defaults under Tax Administration Act sections 43-44. Those provisions distinguish tax-payable returns, monthly default and other documents; do not quote a single flat penalty for all cases. Estimated-tax shortfalls are separately governed by Income Tax Act section 110(11)-(12). Do not apply an expired emergency waiver. [Tax Administration Act, sections 43-44](https://frcs.org.fj/files/2026/06/TAX-ADMINISTRATION-ACT-2009-Revised-1-August-2025.pdf); [Income Tax Act, section 110](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

For non-resident companies, identify PE income and source before using the ordinary company rate. For branch profit remittances, section 10(6) deems after-tax earnings paid/credited to the head office a dividend: read this with the current dividend exemption and do not invent a separate branch-profits surcharge. Treaties require the actual effective agreement, residence, recipient and income article, rather than an assumed reduction. The 2025 amendment to section 140 also addresses international tax agreements. [Income Tax Act, sections 10 and 140](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [Act 9/2025, section 8](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-9-Income-Tax-Budget-Amendment-Act-2025.pdf?ver=1794354122).

## Worked cases

**Ordinary company.** Established chargeable income is FJD 100,000. The company is not listed and has no special regime. Gross tax is FJD 25,000. It has evidenced advances of FJD 18,000 and no other credits, leaving FJD 7,000. The base is chargeable income, not turnover. [LN 55/2023, Schedule paragraph 3(c)](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [Income Tax Act, section 8](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

```oa-check
name: Fiji ordinary company balance after advances
inputs:
  chargeable_income: 100000
  advances_paid: 18000
steps:
  gross_tax: chargeable_income * 0.25
  balance: gross_tax - advances_paid
expected:
  gross_tax: 25000
  balance: 7000
```

**Listed-company limit.** For the same FJD 200,000 chargeable income, a company within its seventh tax year from SPSE listing has FJD 30,000 gross tax. A company past that limit has FJD 50,000. These are alternative established listing histories, not a taxpayer election or rates applied only to new-equity profit. [LN 55/2023, regulation 2 and Schedule paragraph 3](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf).

```oa-check
name: Fiji listing-period rate comparison
inputs:
  chargeable_income: 200000
steps:
  within_seventh_tax_year: chargeable_income * 0.15
  more_than_seven_tax_years: chargeable_income * 0.25
  difference: more_than_seven_tax_years - within_seventh_tax_year
expected:
  within_seventh_tax_year: 30000
  more_than_seven_tax_years: 50000
  difference: 20000
```

**Advance-tax order.** The preceding assessed liability after foreign credit is FJD 30,000, of which FJD 3,000 was paid by withholding. Each ordinary advance is (30,000 - 3,000) / 3 = FJD 9,000. Subtracting all withholding from each one-third would incorrectly produce FJD 7,000 per instalment. These are established prior-assessment facts, not a current-year estimate. [Act 5/2024, section 5, replacing section 110(3)](https://frcs.org.fj/files/2024/08/Act-5-Income-Tax-Budget-Amendment-Act-2024.pdf).

```oa-check
name: Fiji advance withholding is subtracted before division
inputs:
  preceding_assessed_tax_after_foreign_credit: 30000
  part_paid_by_withholding: 3000
steps:
  each_advance: (preceding_assessed_tax_after_foreign_credit - part_paid_by_withholding) / 3
  total_advances: each_advance * 3
expected:
  each_advance: 9000
  total_advances: 27000
```

## When to refuse or refer

Do not finalise a return from turnover alone, infer a treaty rate without the agreement, treat every shareholder payment as an exempt dividend, claim an unverified incentive, or silently set unverified foreign credits to the amount paid abroad. Stop the affected computation for unknown source/residence, PE attribution, tax-loss restrictions, insurance withholding, special incentive approvals, disputed deductions or transaction relief. A filing/payment extension must be supported by the actual authority.

## Sources

| Source | What was read | Read on |
|---|---|---|
| [Income Tax Act and Regulations, FRCS revision to August 2025](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) | Sections 2, 8, 10, 12-14, 21-22, 30, 36-37, 104, 108, 110, 113 and 115-121; Rates Schedule paragraph 5 and Exempt Income Schedule Part 5. The rates appendix still reproduces superseded company/individual tables; LN 55/2023 controls those rates. | 2026-11-16 |
| [LN 55/2023 in official Gazette bundle](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) | Regulation 1 commencement, regulation 2 listed-company transition and regulation 3(b) replacement company-rate table. | 2026-11-16 |
| [Income Tax amendment, Act 5/2024](https://frcs.org.fj/files/2024/08/Act-5-Income-Tax-Budget-Amendment-Act-2024.pdf) | Section 5: enacted one-third advances/estimates and tax year 2025 onwards, resolving the consolidation's obsolete estimate wording. | 2026-11-16 |
| [Income Tax amendment, Act 9/2025](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-9-Income-Tax-Budget-Amendment-Act-2025.pdf?ver=1794354122) | Entire four-page Act: dividend definition, e-money deposits, deductions, vehicle benefits and international-agreement changes with distinct commencement. | 2026-11-16 |
| [Income Tax amendment, Act 14/2026](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-14-Income-Tax-Budget-Amendment-No.-2-Act-2026.pdf?ver=1794354122) | Entire three-page Act: commencement and sports deduction, aviation losses, inventory approval, capital gains, reorganisation, contractor reporting and failed transfers. | 2026-11-16 |
| [Tax Administration Act, FRCS revision](https://frcs.org.fj/files/2026/06/TAX-ADMINISTRATION-ACT-2009-Revised-1-August-2025.pdf) | Section 3 approved return/form and sections 43-44 distinguishing filing/payment defaults; no expired waiver assumed. | 2026-11-16 |

Not yet confirmed: exact current hotel/tourism and film-production incentive amounts and eligibility; every special incentive/regulation outside the ordinary regime; restrictions beyond section 30 affecting a particular acquired loss/company; exact current TPOS company return fields and tax-agent extension programme; 2026 insurance-premium withholding (the rates webpage and later 2025-specific amendment need reconciliation for 2026); transaction-specific treaty rates and foreign-credit computations; any claimed branch surcharge outside the sections read. These are excluded from the computed results above.
