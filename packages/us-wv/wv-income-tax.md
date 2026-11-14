---
name: wv-income-tax
description: Use this skill whenever asked about West Virginia individual income tax, West Virginia Form IT-140, West Virginia graduated tax rates, West Virginia self-employment income tax at the state level, West Virginia 2026 rate cut, or any West Virginia personal income tax question for sole proprietors. Trigger on phrases like "West Virginia income tax", "WV income tax", "Form IT-140", "West Virginia tax brackets", "WV 4.58%", "W.Va. Code §11-21", or any request involving West Virginia state individual income tax computation or filing.
version: "0.2"
jurisdiction: US-WV
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: situation-rules
category: state-tax
---

# West Virginia individual income tax (2026)

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

**Answer first:** West Virginia's 2026 individual rates are 2.11% to 4.58%, retroactive to January 1, 2026. Start with federal AGI, apply state modifications, subtract the earned-income exclusion if eligible and personal exemptions, then compute tax. The earlier statement that there is no personal exemption deduction was wrong. [Tax Division 2026 rate notice](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx); [§11-21-16](https://code.wvlegislature.gov/11-21-16/).

## Scope

Full-year West Virginia resident individuals, especially sole proprietors and disregarded single-member LLCs, using IT-140. Residents report all income; part-year and nonresident allocation is identified below for referral. Currency USD, calendar tax year 2026. The 2025-2026 filing cycle booklet supplies the latest read form layout; its 2025 rates and indexed credit tables must not be used for 2026. Corporate returns belong to `wv-corporate-tax`; wage withholding and unemployment to `wv-payroll`; sales/use to `wv-sales-tax`. Federal Schedule C and self-employment calculations belong to `us-schedule-c-and-se-computation`.

## Ask the client first

1. Filing status, dependents and whether another taxpayer can claim the filer?
2. Domicile, dates in West Virginia, permanent homes and income earned in each state?
3. Federal AGI, Schedule C results, state refunds, municipal bond interest and U.S. obligation interest?
4. Social Security, pension type, age/disability and each spouse's ownership of income?
5. Other-state tax, property-tax payments, special credits and pass-through income?
6. Withholding, dated estimated payments and the prior full-year tax liability?

## The method, step by step

### Rates, bands and thresholds

The ordinary schedule covers single, head of household, surviving spouse and married joint filers. MFS means married filing separately. SB 392 enacted a further reduction; do not apply another 5% reduction to these published rates.

| Item | Amount or rule | Official source |
| --- | --- | --- |
| Ordinary taxable income not over $10,000 | 2.11% of taxable income | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| Ordinary taxable income over $10,000 through $25,000 | $211 + 2.81% of excess over $10,000 | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| Ordinary taxable income over $25,000 through $40,000 | $632.50 + 3.16% of excess over $25,000 | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| Ordinary taxable income over $40,000 through $60,000 | $1,106.50 + 4.22% of excess over $40,000 | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| Ordinary taxable income over $60,000 | $1,950.50 + 4.58% of excess over $60,000 | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| MFS taxable income not over $5,000 | 2.11% of taxable income | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| MFS taxable income over $5,000 through $12,500 | $105.50 + 2.81% of excess over $5,000 | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| MFS taxable income over $12,500 through $20,000 | $316.25 + 3.16% of excess over $12,500 | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| MFS taxable income over $20,000 through $30,000 | $553.25 + 4.22% of excess over $20,000 | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| MFS taxable income over $30,000 | $975.25 + 4.58% of excess over $30,000 | [2026 notice; §11-21-4j](https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx) |
| Personal exemption | $2,000 per allowable exemption; dependent claiming no exemptions gets $500 | [§11-21-16](https://code.wvlegislature.gov/11-21-16/) |
| Social Security included in federal AGI | Full subtraction in 2026 at all income levels | [§11-21-12(c)(8)(A)-(F)](https://code.wvlegislature.gov/11-21-12/) |
| Senior/disability modification | Up to $8,000 per eligible person, reduced by the specified other modifications; no double deduction | [§11-21-12(c)(9)-(10)](https://code.wvlegislature.gov/11-21-12/) |
| Estimated payments, 2025-2026 filing cycle | $600 or more net liability, unless below 10% of estimated tax; penalty safe harbor smaller of 90% current or 100% prior full-year tax | [Booklet pp.21-22](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf) |

### The base and return sequence

1. Complete the federal return first. Schedule C profit, a properly allowed self-employed health-insurance deduction, retirement contributions and the deductible self-employment-tax component already feed federal AGI. A home office expense affects Schedule C first. Do not deduct any of them twice; see `us-schedule-c-and-se-computation`, `us-self-employed-health-insurance` and `us-self-employed-retirement`. Federal standard/itemized deductions and the QBI deduction occur after AGI and are not automatically state deductions. [Booklet p.24](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).
2. Transfer federal AGI to IT-140. Add other-state municipal obligation interest; subtract qualifying U.S. obligation interest and state income-tax refunds included in federal AGI. Apply the remaining Schedule M modifications from the supporting documents. For 2026 subtract the Social Security amount included in federal AGI in full, including higher-income filers who had only a partial subtraction in 2025. [§11-21-12](https://code.wvlegislature.gov/11-21-12/).
3. The 2025-2026 filing cycle layout is IT-140 line 1 AGI, line 2 additions, line 3 subtractions, line 4 WV AGI, line 5 low-income earned-income exclusion, line 6 exemption deduction, line 7 taxable income. Line 6 is an actual deduction. There is no general standard deduction. Use the final 2026 form before transcribing line numbers. [Booklet pp.22-24](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).
4. Apply the relevant rate schedule. The final tax-table lookup can differ from the exact schedule result; do not use the 2025 lookup table to compute a 2026 return. Compute credit eligibility separately, then reconcile withholding and estimates to the balance/refund. On the read layout, line 8 is tax, line 9 credits from RECAP and line 15 withholding. [Booklet pp.24-25](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).
5. For low-income families, calculate modified federal AGI and family size on IT-140W and multiply tax by the applicable table percentage. This is not a flat $40 per exemption. The 2026 indexed credit and exclusion values remain unconfirmed. The senior citizen property-tax credit is distinct from the income modification; obtain the property-tax records and current SCTC/HEPTC instructions before claiming it. [Booklet pp.11-12,19-21](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).

### Residency and cross-border points

The booklet describes residence as more than 30 days with intent to make WV the permanent residence, or physical presence for more than 183 days. It also describes a domiciliary nonresident exception for less than 30 days plus an outside permanent home. Do not combine those descriptions into the old cumulative test of a 30-day abode AND 183 days. Refer close domicile cases for the statutory test. Part-year/nonresidents use Schedule A and allocate income from the federal return; do not treat gross receipts as the allocation numerator. [Booklet pp.17-18](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).

A full-year resident of Kentucky, Maryland, Ohio, Pennsylvania or Virginia with only WV wages may use the special nonresident wage treatment; business profit is not protected by wage reciprocity. A resident credit for income tax paid to another state uses Schedule E and is limited to WV tax attributable to the same income. Multi-state credits and allocation need review. [Booklet pp.17-19 and Schedule E](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).

### Filing, payment and penalties

Calendar 2026 IT-140 is due April 15, 2027 under the fourth-month rule in [§11-21-51(a)](https://code.wvlegislature.gov/11-21-51/). The latest read booklet accepts the federal filing extension, requires the extension information/attachment, and permits WV 4868 if only a state extension is needed; payment is not extended. [Booklet p.22](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).

Use approved e-file software and retain its acceptance, or the current signed paper IT-140 with required schedules. MyTaxes at https://mytaxes.wvtax.gov supports payments; keep the period, payment confirmation and bank reconciliation. For the 2025-2026 filing cycle, IT-140ES installment dates are April 15, June 15, September 15 and January 15 following the year. The return's estimates credit includes installments, carryforward overpayments and extension payments. [Booklet pp.22,50](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).

The read 2025-2026 filing cycle instructions impose late filing at 5% per month or part, up to 25%; late payment at 0.5% per month or part, up to 25%, plus interest. Do not add independently computed monthly penalties without checking concurrent-penalty rules. Interest is period-specific, not the federal underpayment rate assumed in the old skill. For installment underpayment use IT-210; dated payments matter even if the return eventually shows a refund. [Booklet pp.21-22](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Standard vs itemized federal deduction or QBI | Neither flows through AGI as a WV deduction; no duplicate subtraction |
| Federal Schedule C loss or hobby reclassification | Reconcile federal AGI and state modifications; no independent state hobby deduction invented here |
| Age 65/disability and pension or Social Security subtraction | Reduce the senior modification for the specified other modifications; allocate between spouses by ownership |
| 2025 Social Security treatment | Higher-income filers used the partial phaseout-stage subtraction; 2026 full subtraction must not be back-applied |
| Federal joint return, state separate returns | State separate treatment can be elected under §11-21-51(b); split actual income and deductions rather than halves by assumption |
| Estate, trust, corporate, severance or municipal B&O tax | Separate job; IT-140 does not discharge it |

## Worked cases

**Case 1:** A resident sole proprietor has federal AGI $122,000, no state modifications, one exemption and no credits or earned-income exclusion. Taxable income is $120,000. Tax is $1,950.50 + $60,000 x 4.58% = $4,698.50. Omitting the exemption would overstate exact-schedule tax by $91.60.

```oa-check
name: WV 2026 ordinary schedule with personal exemption
inputs:
  agi: 122000
  exemption: 2000
steps:
- ti: max(agi - exemption, 0)
- tax: 1950.50 + (ti - 60000) * 0.0458
- omission_cost: exemption * 0.0458
expected:
  ti: 120000
  tax: 4698.5
  omission_cost: 91.6
```
**Case 2, decision both ways:** Spouses may file state-separately despite a federal joint return, subject to the state requirements. With taxable incomes already separately determined after exemptions of $80,000 and $20,000, joint tax on $100,000 is $3,782.50. Separate tax is $3,265.25 + $553.25 = $3,818.50, so joint saves $36. If each has $50,000, separate total is $3,782.50, tying joint. These figures exclude credits and use exact rate schedules; ownership, residency and credit eligibility can change the choice. [§11-21-51(b)](https://code.wvlegislature.gov/11-21-51/).

```oa-check
name: WV joint or separate state return decision
inputs:
  high: 80000
  low: 20000
  equal: 50000
steps:
- joint: 1950.50 + (high + low - 60000) * 0.0458
- separate_high: 975.25 + (high - 30000) * 0.0458
- separate_low: 316.25 + (low - 12500) * 0.0316
- separate_total: separate_high + separate_low
- joint_saving: separate_total - joint
- balanced_separate: 2 * (975.25 + (equal - 30000) * 0.0458)
expected:
  joint: 3782.5
  separate_high: 3265.25
  separate_low: 553.25
  separate_total: 3818.5
  joint_saving: 36
  balanced_separate: 3782.5
```

## When to refuse or refer

Refer nonresident/part-year allocation, domicile disputes, partnership/S-corporation modifications, state NOLs or federal/state depreciation differences, amended returns, IT-141 fiduciaries, historic rehabilitation/neighborhood investment credits, property-tax credits and other specialist claims. Municipal B&O and severance are separate taxes; corporate net income uses `wv-corporate-tax`. Do not produce a final 2026 low-income credit without the 2026 table.

## Filing and payment

Prepare the tax reconciliation, current-year form set, payment instruction and acceptance record. Have the qualified reviewer resolve every flagged modification or credit before filing. An amended federal return can require an amended WV return; the read booklet requires reporting the final federal change within 90 days. [Booklet p.18](https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf).

## Completion checklist

- 2026 rate schedule selected, including MFS status where required.
- AGI modifications documented; exemption actually deducted; Social Security not subtracted twice.
- Federal figures loaded from their owner skills.
- Other-state income, credits and payments reconciled by period.
- Final 2026 form and credit-table gaps resolved before a filing output.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| Tax Division 2026 rate-cut page. Read for SB 392 effective dates, both schedules and updated withholding. | https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx | 2026-11-13 |
| West Virginia Code §11-21-16. Read for personal exemptions and dependent exception. | https://code.wvlegislature.gov/11-21-16/ | 2026-11-13 |
| West Virginia Code §11-21-12. Read for AGI modifications, Social Security transition and senior coordination. | https://code.wvlegislature.gov/11-21-12/ | 2026-11-13 |
| West Virginia Code §11-21-51. Read for return deadline, residents and joint/separate choices. | https://code.wvlegislature.gov/11-21-51/ | 2026-11-13 |
| IT-140 booklet, 2025-2026 filing cycle. Read for pp.11-12 and17-29: residence, form mapping, modifications, credit structure, estimates and penalties; not 2026 indexed values. | https://tax.wv.gov/Documents/PIT/2025/it140.PersonalIncomeTaxFormsAndInstructions.2025.pdf | 2026-11-13 |

Not yet confirmed: final 2026 IT-140 layout, tax lookup table, family-credit percentages/income bands, low-income earned-income exclusion and property-credit amounts; 2026 interest notices; current depreciation/conformity and state NOL differences; specialist credits. The old $40-per-exemption family credit and senior-credit $50,000/$100,000 eligibility assertion are not confirmed and must not be used. The old rate-history table mislabeled enactment years and is not usable historical guidance. Future trigger reductions require the next effective-year notice; the 2026 notice confirms only the rates above.
