---
name: hi-income-tax
description: "Hawaii resident wage earners, sole proprietors and disregarded LLC owners: N-11 taxable income, 2026 standard deductions, all filing-status rate schedules, N-15 routing, estimated payments and state adjustments."
version: "0.2"
jurisdiction: US-HI
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Hawaii individual income tax, tax year 2026

> **General reference only.** Built from the official sources identified below. Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply this material to the taxpayer's actual facts and the law for the relevant period, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of any federal tax implications. Federal computations belong to the linked federal skills.

**Answer first.** Hawaii taxes resident wages and business income. For 2026, standard deductions increase to USD 8,000 single/separate, USD 16,000 joint/surviving spouse and USD 12,000 head of household; the 2025 rate schedules continue. Compute Hawaii adjustments before applying the state deduction and exemptions. GET is a separate business tax: `hi-sales-tax`. State payroll is `hi-payroll`; corporate returns are `hi-corporate-tax`.

## Scope

Full-year resident individuals use Form N-11. This includes ordinary W-2 wages and Schedule C profit of a sole proprietor or disregarded single-member LLC. Residents are taxed on all-source income. Nonresidents and part-year residents use N-15; detailed allocation is outside this skill. Every individual doing business in Hawaii must file even if the business has no taxable income. Employee services alone are excluded from that special business-filing rule. Source: [2025 N-11 instructions, Who Must File and Residency Status](https://files.hawaii.gov/tax/forms/current/n11ins.pdf).

2026 rates and deductions are confirmed by [DOTAX Announcement 2024-03, Tax Year 2026](https://files.hawaii.gov/tax/news/announce/ann24-03.pdf). Form-line references and ancillary return instructions below are the verified **2025-2026 filing cycle**, not a claim that a final 2026 N-11 has been read.

## Ask the client first

1. Filing status, age, dependents and any certified disability, including whether someone else can claim the taxpayer.
2. Residence dates and all places where wages, business, rent and investment income arose.
3. Federal AGI and supporting schedules, including state bond interest, Social Security, pensions and reserve/Guard pay.
4. Hawaii versus federal depreciation schedules, retirement contributions, health insurance and home-office amounts.
5. Hawaii itemized deductions and the federal filing choice; obtain the underlying receipts rather than reusing the federal total.
6. Withholding, estimated payments, prior-year tax and credit eligibility, including food/excise and other-state tax credits.

## The method, step by step

### Rates, bands and thresholds

The schedules below use DOTAX's published whole-dollar base amounts. Below USD 100,000 taxable income, use the official tax table rather than these formulas. [DOTAX rate schedules, caution and Schedules I to III](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/).

| Single or married separate taxable income (USD) | Tax formula | Official source |
|---|---|---|
| 0 through 9,600 | 1.4% of taxable income | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 9,600 through 14,400 | USD 134 + 3.2% of excess over USD 9,600 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 14,400 through 19,200 | USD 288 + 5.5% of excess over USD 14,400 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 19,200 through 24,000 | USD 552 + 6.4% of excess over USD 19,200 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 24,000 through 36,000 | USD 859 + 6.8% of excess over USD 24,000 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 36,000 through 48,000 | USD 1,675 + 7.2% of excess over USD 36,000 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 48,000 through 125,000 | USD 2,539 + 7.6% of excess over USD 48,000 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 125,000 through 175,000 | USD 8,391 + 7.9% of excess over USD 125,000 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 175,000 through 225,000 | USD 12,341 + 8.25% of excess over USD 175,000 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 225,000 through 275,000 | USD 16,466 + 9% of excess over USD 225,000 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 275,000 through 325,000 | USD 20,966 + 10% of excess over USD 275,000 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 325,000 | USD 25,966 + 11% of excess over USD 325,000 | [Schedule 1](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |

| Joint or qualifying surviving spouse taxable income (USD) | Tax formula | Official source |
|---|---|---|
| 0 through 19,200 | 1.4% of taxable income | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 19,200 through 28,800 | USD 269 + 3.2% of excess over USD 19,200 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 28,800 through 38,400 | USD 576 + 5.5% of excess over USD 28,800 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 38,400 through 48,000 | USD 1,104 + 6.4% of excess over USD 38,400 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 48,000 through 72,000 | USD 1,718 + 6.8% of excess over USD 48,000 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 72,000 through 96,000 | USD 3,350 + 7.2% of excess over USD 72,000 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 96,000 through 250,000 | USD 5,078 + 7.6% of excess over USD 96,000 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 250,000 through 350,000 | USD 16,782 + 7.9% of excess over USD 250,000 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 350,000 through 450,000 | USD 24,682 + 8.25% of excess over USD 350,000 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 450,000 through 550,000 | USD 32,932 + 9% of excess over USD 450,000 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 550,000 through 650,000 | USD 41,932 + 10% of excess over USD 550,000 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 650,000 | USD 51,932 + 11% of excess over USD 650,000 | [Schedule 2](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |

| Head of household taxable income (USD) | Tax formula | Official source |
|---|---|---|
| 0 through 14,400 | 1.4% of taxable income | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 14,400 through 21,600 | USD 202 + 3.2% of excess over USD 14,400 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 21,600 through 28,800 | USD 432 + 5.5% of excess over USD 21,600 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 28,800 through 36,000 | USD 828 + 6.4% of excess over USD 28,800 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 36,000 through 54,000 | USD 1,289 + 6.8% of excess over USD 36,000 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 54,000 through 72,000 | USD 2,513 + 7.2% of excess over USD 54,000 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 72,000 through 187,500 | USD 3,809 + 7.6% of excess over USD 72,000 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 187,500 through 262,500 | USD 12,587 + 7.9% of excess over USD 187,500 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 262,500 through 337,500 | USD 18,512 + 8.25% of excess over USD 262,500 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 337,500 through 412,500 | USD 24,699 + 9% of excess over USD 337,500 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 412,500 through 487,500 | USD 31,449 + 10% of excess over USD 412,500 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |
| Over 487,500 | USD 38,949 + 11% of excess over USD 487,500 | [Schedule 3](https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/) |

| Other item | Amount and conditions | Official source |
|---|---|---|
| 2026 standard deduction, single or separate | USD 8,000, subject to dependent and separate-return limitations | [Announcement 2024-03](https://files.hawaii.gov/tax/news/announce/ann24-03.pdf) |
| 2026 standard deduction, joint or surviving spouse | USD 16,000 | [Announcement 2024-03](https://files.hawaii.gov/tax/news/announce/ann24-03.pdf) |
| 2026 standard deduction, head of household | USD 12,000 | [Announcement 2024-03](https://files.hawaii.gov/tax/news/announce/ann24-03.pdf) |
| Regular personal exemption | USD 1,144 per allowable exemption; add an exemption for each taxpayer/spouse aged 65 or older; dependent claimant cannot claim own exemption | [HRS 235-54(a)](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf) |
| Certified blind, deaf or totally disabled person | USD 7,000 instead of that person's regular exemptions; obtain certification and check spouse/dependent interaction | [HRS 235-54(c)](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf) |
| Estimated tax filing floor | Tax liability below USD 500 is excused from estimates | [HRS 235-97(a)(6)](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf) |

1. Start with federal AGI. For Schedule C, self-employment tax and associated federal adjustments, load `us-schedule-c-and-se-computation`; federal retirement, health insurance, home office and QBI figures belong to `us-self-employed-retirement`, `us-self-employed-health-insurance`, `us-qbi-deduction` and that computation skill. Do not restate federal amounts.
2. Prepare Hawaii additions and subtractions. HRS 235-7(b)(2) generally includes other-state municipal interest unless specifically exempt; qualifying U.S. obligation interest is subtracted to the extent in federal AGI. Social Security and first-tier railroad benefits included federally are subtracted. Qualifying employer-funded pension distributions can be excluded; employee-funded deferred compensation and IRA distributions require tracing and are not automatically exempt. The reserve/Guard exclusion has its own pay-based cap. Sources: [HRS 235-7](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf); [N-11 instructions, lines 11 to 18](https://files.hawaii.gov/tax/forms/current/n11ins.pdf).
3. Reconcile federal and Hawaii depreciation. The verified N-11 instructions do not adopt federal bonus depreciation; prepare separate state depreciation and gain schedules. Do not replace MACRS with an unsupported blanket straight-line rule. Self-employed health insurance, retirement and home-office items already in federal AGI are starting-point inputs, subject to Hawaii conformity and adjustments; they are not an unconditional no-add-back guarantee. Source: [N-11 instructions, other additions and depreciation](https://files.hawaii.gov/tax/forms/current/n11ins.pdf).
4. Subtract allowable Hawaii itemized deductions or the 2026 standard deduction. Hawaii itemization is evaluated separately from the federal election; married-separate and dependent limitations matter. Then subtract personal exemptions, flooring taxable income at zero. The federal QBI deduction is below AGI and is not automatically a Hawaii deduction. Source: [N-11 instructions, lines 22 to 26](https://files.hawaii.gov/tax/forms/current/n11ins.pdf).
5. Compute tax using the table below USD 100,000 or the appropriate schedule at/above that amount, then apply substantiated Hawaii credits and subtract withholding/estimates. The 2025-2026 filing-cycle line map is N-11 line 10 federal AGI, lines 11/12 additions and total, lines 13 to 18 subtractions, line 20 Hawaii AGI, line 22 itemized or line 23 standard deduction, line 24 income less deduction, line 25 exemptions, line 26 taxable income and line 27 tax. Confirm the final 2026 form before entering lines. Source: [N-11 instructions, line-by-line instructions](https://files.hawaii.gov/tax/forms/current/n11ins.pdf).
6. Reconcile GET once: gross business receipts and deductible business tax expense must agree with the federal Schedule C working paper. GET is not an income-tax credit. Use `hi-sales-tax` for the separate gross-receipts liability.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Below USD 100,000 taxable income | Mandatory DOTAX tax-table lookup; do not return a marginal-formula estimate as final tax |
| Nonresident or part-year resident | N-15 and source/residence allocation; retain all dates and refer complex allocations |
| Other-state income tax paid | Evaluate Hawaii resident credit with supporting other-state return; never assume dollar-for-dollar relief |
| Certified disability or taxpayer claimed as dependent | Apply the special exemption and deduction limitations before computing |
| Partnership or S corporation | Separate N-20/N-35 and pass-through schedules; this is not a corporate return |
| Food/excise credit | Establish year, residency, modified income and eligible exemptions; the old flat USD 110/50,000 claim is not usable without confirmation |
| Bank descriptions STATE OF HI TAX, HAWAII DOTAX, HI TAX REFUND or HITAX PMT | Reconcile to the actual account and return; descriptions alone do not identify tax type or deductibility |

## Worked cases

**Case 1: single resident wage earner.** Invented taxpayer, under 65, no dependents, credits or state adjustments, federal AGI USD 150,000. Standard deduction USD 8,000 and exemption USD 1,144 produce taxable income USD 140,856. Schedule I: USD 8,391 + 7.9% x USD 15,856 = USD 9,643.624, or USD 9,643.62 before return rounding. Withholding is a payment against this liability, not a reduction of taxable income.

```oa-check
name: Hawaii 2026 single resident wages
inputs:
  agi: 150000
steps:
  - taxable: max(agi - 8000 - 1144, 0)
  - tax: 8391 + (taxable - 125000) * 0.079
expected:
  taxable: 140856
  tax: 9643.624
```

**Case 2, a decision: standard or itemized.** Invented joint resident couple under 65, no dependents, Hawaii AGI USD 300,000 and an independently verified allowable Hawaii itemized deduction of USD 20,000 after all limitations. Two exemptions total USD 2,288. Standard deduction yields taxable income USD 281,712 and tax USD 19,287.248. Itemization yields USD 277,712 and tax USD 18,971.248. Choose itemized deductions, saving USD 316 before credits. Both results use Schedule II's USD 16,782 plus 7.9% above USD 250,000.

```oa-check
name: Hawaii 2026 joint deduction decision
inputs:
  agi: 300000
  itemized: 20000
steps:
  - standard_taxable: agi - 16000 - 2 * 1144
  - itemized_taxable: agi - itemized - 2 * 1144
  - standard_tax: 16782 + (standard_taxable - 250000) * 0.079
  - itemized_tax: 16782 + (itemized_taxable - 250000) * 0.079
  - saving: standard_tax - itemized_tax
expected:
  standard_taxable: 281712
  itemized_taxable: 277712
  standard_tax: 19287.248
  itemized_tax: 18971.248
  saving: 316
```

## When to refuse or refer

Refer complex N-15 allocations, credit eligibility, pension rollovers and mixed employee/employer contributions, capital-gain alternative tax, farms, losses, partnership/S-corporation schedules and unresolved conformity. TAT, conveyance and estate tax are separate jobs. Do not file from the 2025 form line map before checking the 2026 form.

## Filing and payment

HRS 235-97(b) sets the return and balance due on the twentieth day of the fourth month after year end: **20 April 2027** for calendar 2026. The verified instructions allow an automatic six-month filing extension, with payment conditions; it does not extend payment. The 2025-2026 filing-cycle instructions require the properly estimated balance paid by the original due date, no delinquent prior balances, and filing within the extension. Source: [HRS 235-97 and 235-98](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf); [N-11 instructions, extension conditions](https://files.hawaii.gov/tax/forms/current/n11ins.pdf).

Use Hawaii Tax Online at https://hitax.hawaii.gov/ or an authorized electronic filing channel; select individual income, period, resident N-11 and payment type. Enter the prepared state schedules, verify credits and payments, submit, save acceptance, and separately save the payment confirmation. The verified 2025 instructions use **N-200V**, not the old N-1 voucher label, for individual estimated payments. Statutory calendar dates are 20 April, 20 June, 20 September and 20 January following the year, shifted under applicable nonbusiness-day rules. The verified instructions test expected net tax of at least USD 500 and withholding/credits below the smaller of 60% current tax or 100% preceding full-year tax, with a prior-year zero-liability full-year-resident exception. Source: [HRS 235-97](https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf); [N-11 instructions, estimated tax](https://files.hawaii.gov/tax/forms/current/n11ins.pdf).

Late filing is 5% per month or part, maximum 25%; interest is two-thirds of 1% per month or part on unpaid tax and penalties. N-210 addresses estimated-tax underpayment. Source: [N-11 instructions, penalties and interest](https://files.hawaii.gov/tax/forms/current/n11ins.pdf).

## Completion checklist

- Resident N-11 versus N-15 established; employee income included even where the old skill focused on self-employment.
- 2026 deduction used, filing status verified and final-year form lines checked.
- Federal/state depreciation, pension and municipal interest reconciled; federal figures loaded from their owner skills.
- Mandatory tax table used where applicable; credits and payment references documented.
- Extension and estimated-payment tests applied separately from tax computation.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| DOTAX Announcement 2024-03. Read for Act 46 tables, 2025 brackets, 2026 standard deductions and unchanged 2026 brackets. | https://files.hawaii.gov/tax/news/announce/ann24-03.pdf | 2026-11-13 |
| DOTAX schedules after December 31, 2024. Read for mandatory table caution and all three complete rate schedules. | https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/ | 2026-11-13 |
| HRS chapter 235, compilation as of December 31, 2025. Read sections 235-7, 235-51 to 54, 235-92, 235-97 and 235-98 for modifications, exemptions, filing and estimates. | https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf | 2026-11-13 |
| 2025 N-11 instructions. Read Who Must File, Residency Status, extension, estimated tax, lines 10 to 27, pensions, depreciation and penalties. This is the 2025-2026 filing cycle. | https://files.hawaii.gov/tax/forms/current/n11ins.pdf | 2026-11-13 |

Not yet confirmed: final 2026 N-11/N-15 forms and line numbers; 2026 filing thresholds replacing old 2025 USD 5,544 single/separate, USD 6,688 single 65+, USD 11,088 joint under 65, USD 12,232 joint with one 65+ and USD 7,568 head-of-household figures; 2026 reserve/Guard exclusion cap (2025 instructions give USD 8,636); final 2026 credit schedules including the old food/excise USD 110 per exemption and USD 50,000 AGI claim; 2026 conformity legislation affecting QBI, depreciation, self-employed health insurance, retirement or home-office adjustments. These gaps are not instructions to reuse old thresholds. Old Everlance and TurboTax citations were secondary and are not retained as authority.
