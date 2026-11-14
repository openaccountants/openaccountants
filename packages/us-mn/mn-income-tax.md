---
name: mn-income-tax
description: "Minnesota FormM1: federal AGI base, 2026 brackets and deductions, dependent exemption, state adjustments, independent itemization and annual filing-cycle limits."
version: "0.3"
jurisdiction: US-MN
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
category: state-tax
---

# Minnesota individual income tax, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

## Who this applies to

Full-year Minnesota resident individuals, including employees, sole proprietors and disregarded single-member LLC owners, preparing Form M1. Use `us-form-1040-individual-return`, `us-schedule-c-and-se-computation` and `us-section-179-and-bonus-depreciation` for federal inputs. Minnesota begins with **federal adjusted gross income**, not federal taxable income. The old federal-taxable-income starting point and automatic QBI add-back workflow were wrong for this return. The published **2026** rate/indexing release supplies the amounts below. Annual line mapping and filing mechanics retained from the final **2025-2026 filing cycle** must be checked against final 2026 forms; the November 3,2026 M1 booklet is marked FINAL DRAFT and is not treated as final filing instructions. [Final 2025 booklet](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf); [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf).

## Rates, bands and thresholds

Each rate applies only to income in its band. These are taxable-income amounts after state deductions/exemptions, not gross receipts.

| Filing status | 5.35% band | 6.80% band | 7.85% band | 9.85% band | Official source |
| --- | --- | --- | --- | --- | --- |
| Single | 0-33,310 | over 33,310-109,430 | over 109,430-203,150 | over 203,150 | [2026 rates](https://www.revenue.state.mn.us/minnesota-income-tax-rates-and-brackets); [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| MFJ / qualifying surviving spouse | 0-48,700 | over 48,700-193,480 | over 193,480-337,930 | over 337,930 | [2026 rates](https://www.revenue.state.mn.us/minnesota-income-tax-rates-and-brackets); [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| MFS | 0-24,350 | over 24,350-96,740 | over 96,740-168,965 | over 168,965 | [2026 rates](https://www.revenue.state.mn.us/minnesota-income-tax-rates-and-brackets); [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| Head of household | 0-41,010 | over 41,010-164,800 | over 164,800-270,060 | over 270,060 | [2026 rates](https://www.revenue.state.mn.us/minnesota-income-tax-rates-and-brackets); [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |

| Deduction / boundary | 2026 amount in USD | Official source |
| --- | --- | --- |
| Standard deduction single/MFS | 15,300 | [2026 indexing,290.0123](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| Standard deduction MFJ/QSS | 30,600 | [2026 indexing,290.0123](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| Standard deduction HOH | 23,000 | [2026 indexing,290.0123](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| Additional standard deduction for each qualifying age/blind condition | 1,600 married/QSS;2,000 single/HOH | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| Dependent taxpayer's standard-deduction inputs | Greater of 1,300 or earned income+350, limited to applicable standard deduction under worksheet | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf); [annual worksheet](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf) |
| Dependent exemption | 5,300 per qualifying dependent; reduces income, not tax; no taxpayer/spouse personal exemption | [2026 indexing,290.0121](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| Exemption reduction starts above AGI | Single 244,500; MFJ/QSS366,700; HOH305,600; MFS183,350 | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| Deduction limitation AGI thresholds | First 244,400; second 337,800; MFS122,200/168,900;80% limitation at 1,107,750 | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| Estimate trigger | Expected tax due after withholding/credits 500 or more | [Final annual booklet, p.22](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf) |

## The base

Begin with FAGI. Schedule C/1099-NEC profit, rents, interest and capital gains flow through the federal computation; federal SE-tax and self-employed health-insurance deductions already reflected in FAGI are not deducted a second time. The federal QBI deduction is below FAGI, so it is not a deduction to subtract again or add back to FAGI. Minnesota uses its own standard or itemized deduction and dependent exemptions. A federal standard deduction does not prohibit Minnesota itemization; MFS standard deduction is unavailable if the spouse itemizes. [Final annual instructions, lines 1-6](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf).

Use Schedule M1M for additions/subtractions and applicable nonconformity schedules. Non-Minnesota municipal bond interest excluded federally can require an addition; U.S.-obligation interest and an included state income-tax refund may qualify for subtraction. Do not say non-Minnesota municipal interest is already in federal taxable income. Track actual bond/fund composition. Minnesota itemized deductions are computed on Schedule M1SA rather than by automatically carrying federal ScheduleA or adding every state tax to FAGI. [M1M/M1SA instructions in final annual booklet](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf).

Federal bonus depreciation requires the applicable Minnesota addition and subsequent recovery, not a wholesale replacement with straight-line MACRS. Maintain vintage schedules and suspended-loss adjustments; `us-section-179-and-bonus-depreciation` owns federal amounts. State conformity changed during the 2026 session and requires current Minnesota nonconformity schedules, not an assumed historical USD25,000 section 179 cap. Final 2026 details are pending below. [2025 annual booklet, lines 2/7](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf); [updated corporate booklet for entity distinction](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

Choose the larger allowed Minnesota standard deduction or M1SA deduction after limitations. In the indexed standard-deduction worksheet the first AGI layer above 244,400 through 337,800 is reduced at 3%, the next excess at 10%, limited to 80% of the deduction; use half the first two AGI boundaries for MFS. At the indexed upper limitation of 1,107,750 the statutory 80% limit applies. Use the current worksheet for boundaries, additions for age/blindness and dependent restrictions. Exemption reduction uses its own filing-status thresholds, not these deduction thresholds. [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf); [annual worksheets](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf).

Tax the resulting taxable income, then check Schedule M1MT state alternative minimum tax, Schedule NIIT if applicable, nonrefundable credits and refundable credits separately. Capital gains have no preferential ordinary Minnesota rate, but the separate net-investment-income tax is not eliminated by using the ordinary brackets. Do not claim a USD5,300 “personal credit” or compute a state credit simply as a percentage of federal EIC. Working Family/Child credits use Minnesota Schedule M1CWFC; K-12 education uses M1ED and the education-subtraction rules; dependent-care credit uses M1CD; marriage credit uses M1MA. Each needs actual qualifying children, expenses, income and residency facts. State credit formulas and 2026 changes are unresolved below rather than guessed. [Annual booklet](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf).

Social Security subtraction is not automatic for every recipient and is not the old one-line provisional-income assertion. Minnesota has simplified and alternate methods; choose the allowable result using M1M. Published 2026 simplified phase-out thresholds are 110,780 MFJ/QSS,86,410 single/HOH,55,390 MFS. Alternate maximum inputs are 5,840/4,560/2,920, with their own 88,630/69,250/44,315 phase-out thresholds. These are state subtraction amounts, not federal benefit limits. [2026 indexing,290.0132 subd. 26](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf).

## Deadlines and filing

Ordinary calendar-year M1 filing/payment is April 15 following the tax year, adjusted for closed days or published relief. For the verified 2025-2026 filing cycle, 2025 payment was due April 15,2026 and filing by October 15,2026 avoided the ordinary late-filing penalty. Filing later does not extend payment; a federal extension is not a condition for the state's ordinary six-month filing allowance. Final 2026 instructions are pending, so April 15,2027 is the ordinary statutory date, subject to official changes. [Annual instructions, p.10](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf).

Use Minnesota e-Services/payment system or the authorized return channel; paper filing includes required federal return and state schedules. Reconcile M1W withholding, estimated payments/extension payments and M1REF refundable credits against actual records. Use M15 for estimate underpayment; “M14” is not the current all-purpose quarterly return. The usual individual estimate schedule is April 15, June 15, September 15, January 15 following year, subject to closed days and special annualization/farmer rules; use the actual-year voucher and M15 instructions. Do not apply corporation installment dates. Retain confirmations and receipts for deduction/credit claims. [Annual booklet, pp.10,18,21-23](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf); [individual estimates statute](https://www.revisor.mn.gov/statutes/cite/289A.25).

## Penalties and interest

The verified 2025-2026 annual booklet gives 4% late-payment penalty,5% late-filing penalty after the filing allowance, and an additional 5% extended-delinquency charge under its conditions. Its worksheet can waive the first late-payment charge where less than 10% remains unpaid and filing is timely within the allowance; apply the exact worksheet, not a generic filing-extension rule. Interest in calendar 2026 is 7% on the relevant unpaid tax/penalty balance; later calendar rates must be obtained separately. Estimate underpayment is a separate M15 computation and can arise despite a refund. [Annual booklet, pp.21-23](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf).

## Cross-border points

Minnesota domicile and statutory residency are distinct tests. A nondomiciliary can be resident when maintaining a Minnesota abode and physically present 183 days or more, subject to actual statutory exceptions;183 days alone is not a universal presumption. Full-year residents generally report worldwide income. M1CR credit for tax paid to another state needs the other return and limitations. Michigan and North Dakota wage reciprocity exists; Wisconsin reciprocity has not been reinstated. [Annual booklet, pp.6-8](https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf); [2026 withholding booklet, pp.4-5](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).

Refer full M1NR part-year/nonresident allocation, M1X amendments, military/split-residence cases, M706 estate tax, MinnesotaCare and specialized state AMT/NIIT or business credits beyond supported facts. Entity/PTE work belongs to `mn-corporate-and-pte`; employer collections belong to `mn-payroll`. Referrals preserve these distinct jobs rather than inventing missing slugs.

## Two worked examples that recompute

**Resident standard-deduction estimate.** Invented single resident, FAGI100,000, no additions/subtractions/dependents, no credits or preferences, standard deduction 15,300. Taxable income 84,700; bracket arithmetic is 1,782.085+(84,700-33,310)x.068=5,276.605, approximately 5,276.61. Annual filing uses the published tax table below the table cutoff, so this rate-schedule planning illustration can differ slightly from return-table tax. It is not payroll withholding.

```oa-check
name: Minnesota single 2026 rate schedule estimate
inputs:
  agi: 100000
  standard: 15300
steps:
  - taxable: agi - standard
  - first_band: 33310 * 0.0535
  - tax: round(first_band + (taxable - 33310) * 0.068, 2)
expected:
  taxable: 84700
  tax: 5276.61
```

**State itemization decision independent of federal choice.** Same single taxpayer, allowed Minnesota itemized expenses 20,000 after applicable limits. Assume federal standard deduction was chosen. Minnesota can still itemize. State taxable income becomes 80,000, bracket tax 4,957.01 versus 5,276.61 with the state standard deduction, saving 319.60 before credits. The USD5,300 dependent exemption is not claimed merely for the taxpayer themselves.

```oa-check
name: Minnesota independent itemization decision
inputs:
  agi: 100000
  standard: 15300
  allowed_itemized: 20000
steps:
  - standard_taxable: agi - standard
  - itemized_taxable: agi - allowed_itemized
  - standard_tax: round(33310 * 0.0535 + (standard_taxable - 33310) * 0.068, 2)
  - itemized_tax: round(33310 * 0.0535 + (itemized_taxable - 33310) * 0.068, 2)
  - saving: standard_tax - itemized_tax
expected:
  itemized_taxable: 80000
  itemized_tax: 4957.01
  saving: 319.6
```

## Ask the client first

1. Tax year, domicile/abode/day count, moves and all states where income arose?
2. Filing status, spouse's itemization, ages/blindness, dependent eligibility and FAGI?
3. Federal return and Schedule C/E/K-1, Minnesota additions/subtractions, depreciation vintages and nonconformity records?
4. Allowed Minnesota itemized expenses, benefits/pensions, children/education/care costs and supporting credit documents?
5. Other-state returns, Minnesota withholding, dated estimates, prior-year liability, notices and PTE credits actually paid?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 inflation-adjusted amounts. Read for all individual brackets/deduction/exemption/phase-out and Social Security state inputs. | https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf | 2026-11-13 |
| 2026 rate schedules. Read for four filing-status marginal-rate schedules. | https://www.revenue.state.mn.us/minnesota-income-tax-rates-and-brackets | 2026-11-13 |
| Final 2025 M1 booklet. Read for 2025-2026 filing cycle: residency, federal AGI, deductions, schedules, credits, filing, payments, penalties and estimates. | https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-25.pdf | 2026-11-13 |
| 2026 withholding booklet. Read for Michigan/North Dakota reciprocity and withholding versus return distinction. | https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf | 2026-11-13 |
| Individual estimates statute. Read for individual estimate rule and distinction from corporations. | https://www.revisor.mn.gov/statutes/cite/289A.25 | 2026-11-13 |
| Updated 2025 corporate booklet. Read for 2026-session conformity update and entity distinction only. | https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf | 2026-11-13 |

Not yet confirmed: final 2026 M1/M1M/M1SA/M1MT/M1CWFC/M1CD/M1ED/M1MA/M15 forms and all credit/NIIT/AMT computations, detailed 2026 nonconformity, final return-table amounts and 2027 interest rate; full nonresident/part-year/military/amended cases. Draft 2026 form line numbers are not final filing instructions.
