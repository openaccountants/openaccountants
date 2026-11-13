---
name: nd-income-tax
description: "Compute North Dakota 2026 individual income tax for residents with wages, sole proprietorship or pass-through income, using official 2026 indexed schedules, federal taxable income and state modifications. Trigger on ND-1, North Dakota wages, resident income tax, capital gains, qualified dividends and estimates."
version: "0.3"
jurisdiction: US-ND
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
domain: income-tax
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# North Dakota individual income tax, 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** North Dakota starts with federal taxable income, then applies state adjustments and its indexed 0%, 1.95%, 2.50% schedule. The official 2026 ND-1ES publishes 2026 brackets even though the main individual landing page still displays 2025. Wages and sole-proprietor profit enter through the federal return; no separate state standard deduction is invented. [2026 ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf); [57-38-30.3](https://ndlegis.gov/cencode/t57c38.pdf).

## Scope

Full-year resident individuals with wages, sole-proprietorship or pass-through income. Nonresident/part-year allocation, farm averaging, fiduciary and corporation returns require separate schedules/skills. Federal figures and deductions belong to `us-federal-income-tax-return-1040`; this skill does not restate federal amounts. `nd-return-assembly` and `nd-estimated-tax` remain separate, older 2025 jobs; do not use their old figures as 2026 authority.

## Ask the client first

1. Residence and move dates, filing status, spouse's residence and tax-year end.
2. Completed federal return, federal taxable income including any negative pre-zero amount, wages and business schedules.
3. State additions/subtractions, investment income, reservation/military/zone eligibility and supporting statements.
4. Other-state income/taxes, nonresident schedules and credit documentation.
5. North Dakota withholding, estimates, carryovers, notices and extension/payment history.

## The method, step by step

### Rates, bands and thresholds

These are **2026** schedules printed on page 2 of the official 2026 ND-1ES, not inferred from withholding or inflated from 2025.

| Filing status and North Dakota taxable income, USD | 2026 rate / tax | Official source |
| --- | --- | --- |
| Single through 49,575 | 0% | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Single over 49,575 through 250,400 | 1.95% of excess over 49,575 | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Single over 250,400 | 3,916.09 + 2.50% of excess over 250,400 | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Joint/qualifying surviving spouse through 82,800 | 0% | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Joint over 82,800 through 304,850 | 1.95% of excess over 82,800 | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Joint over 304,850 | 4,329.98 + 2.50% of excess over 304,850 | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Separate through 41,400 | 0% | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Separate over 41,400 through 152,425 | 1.95% of excess over 41,400 | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Separate over 152,425 | 2,164.99 + 2.50% of excess over 152,425 | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Head of household through 66,400 | 0% | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Head over 66,400 through 277,600 | 1.95% of excess over 66,400 | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Head over 277,600 | 4,118.40 + 2.50% of excess over 277,600 | [2026 p 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |
| Qualifying net long-term capital gain/qualified dividend adjustment | 40%, subject to state allocation and nonduplication conditions | [57-38-30.3(2)(d)](https://ndlegis.gov/cencode/t57c38.pdf); [2025-2026 instructions](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |
| Individual estimates | Prior net tax at least 1,000 and current expected balance at least 1,000, plus federal estimate and insufficient-withholding tests | [2026 ND-1ES p 1](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf) |

1. Establish resident filing duty and status. Residents generally include all income; part-year/nonresident ND-1NR applies where required. Wage reciprocity with Minnesota/Montana does not exempt nonwage business/rental income. Do not apply a withholding wage table to the final return.
2. Begin with federal taxable income, not AGI. For the **2025-2026 filing-cycle mapping**, ND-1 line 1b retains a negative federal taxable-income calculation even when federal line 15 displays zero. Federal standard/itemized and business deductions are already incorporated; avoid deducting them twice.
3. Reconcile state adjustments from current law and the labelled form instructions. Other-state/local-obligation interest generally enters the state addition. Protected US-obligation income may be subtracted, but agency securities and repurchase agreements are not all protected. State contribution-credit adjustments prevent double benefits. A generic state-income-tax-refund subtraction is not established merely because the federal treatment differs.
4. Qualifying capital gains and qualified dividends have distinct 40% state exclusions. Apply the capital-gain worksheet, netting and ND allocation; do not exclude a gain twice through reservation/other exclusions. Reservation income requires enrollment, residence and sourcing facts under the stated statute, not simply a Native American name or business location.
5. Federal depreciation, including bonus depreciation, enters the federal starting point; verify any state modification rather than creating a second deduction or a blanket addback. Check military pay/retirement, railroad retirement, Social Security, eligible peace-officer retirement, CollegeSAVE and Schedule ND-1SA items where facts apply. Renaissance Zone/new-business exemptions require program eligibility. The ordinary method identifies these adjustments without supplying unverified specialist amounts. Oil/gas production taxes remain separate; do not treat them as individual income-tax withholding.
6. Apply the correct 2026 schedule, then credits, including supported other-state tax credit/ND-1CR and ND-1TC. Reconcile withholding and estimates to account records. The official 2026 estimate worksheet refers to 2025 instructions for adjustment/credit mapping; final 2026 return line numbers still need checking.

### Preserved 2025-2026 filing-cycle reference

The former current-rate table is retained here as **2025 figures only**, never as 2026 computation.

| Status | 2025 zero band / middle-band ceiling / top base | Official source |
| --- | --- | --- |
| Single | 48,475 /244,825 /3,828.83; positive rates 1.95% and 2.50% | [2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |
| Joint/surviving spouse | 80,975 /298,075 /4,233.45; positive rates 1.95% and 2.50% | [2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |
| Separate | 40,475 /149,025 /2,116.73; positive rates 1.95% and 2.50% | [2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |
| Head | 64,950 /271,450 /4,026.75; positive rates 1.95% and 2.50% | [2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |

### Form mapping, 2025-2026 filing cycle only

The read 2025 booklet maps federal taxable income to line 1b, other-state bond interest to line 3, qualifying capital gain to line 6, reservation income to line 7, CollegeSAVE to line 12, qualified dividends to line 13, state taxable income to line 18, tax to line 20, other-state credit to line 21, marriage credit to line 22, other credits to line 23, net tax to line 25, withholding to line 26 and estimates/extension payments to line 27. The old generic line 2/3 additions/subtractions and line 6/14/17/18/22 summary was not the actual 2025 form. Reconcile the federal return, ND-1SA, ND-1TC, ND-1CR, W-2/1099 state withholding and TAP estimate records; final 2026 lines remain unconfirmed. [2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf).

That booklet permits CollegeSAVE contributions to a qualifying Bank of North Dakota account up to USD 5,000, or USD 10,000 jointly, regardless of account ownership, subject to the actual contribution/rollover conditions. These are labelled **2025-2026 filing-cycle** amounts; confirm 2026 continuation before claiming. The former April 15/October 15, 2026 filing/extension dates likewise describe the 2025 return cycle, not tax year 2026.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Resident wage earner | Federal taxable income plus/minus state adjustments; employer withholding is a payment, not final tax |
| Sole proprietor/single-member LLC | Federal business result enters the federal starting point; no separate state self-employment tax is established here |
| Other-state income | Compute state credit only after residency, source and overlapping-tax limits are supported |
| Reservation/zone/military or farm income | Verify specific eligibility and allocation; farm averaging uses ND-1FA |
| Estate/trust, corporation or amendment | Separate return/workflow; do not adapt ordinary resident line mapping without review |

## Worked cases

**Case 1.** Invented 2026 single resident with final North Dakota taxable income USD 100,000 and no credits: (100,000-49,575)×1.95%= USD 983.29. The same taxable income in the preserved 2025 case gave USD 1,004.74 using the verified 2025 cutoff **48,475**. Use the year-specific table, not a guessed rounded cutoff.

```oa-check
name: ND 2026 single taxable income 100000
inputs:
  taxable_income: 100000
  zero_cutoff: 49575
steps:
  - tax: round(max(taxable_income - zero_cutoff, 0) * 0.0195, 2)
expected:
  tax: 983.29
```

**Case 2, status/year boundary.** Invented 2026 joint resident taxable income USD 350,000: published top base 4,329.98 + 2.5% of 45,150 = USD 5,458.73. The preserved 2025 case was USD 5,531.58 using 298,075/4,233.45. At exactly USD 82,800 in 2026 the joint regular tax is zero, although filing or other obligations can remain.

```oa-check
name: ND 2026 joint top band and zero-band boundary
inputs:
  taxable_income: 350000
  top_cutoff: 304850
  top_base_tax: 4329.98
steps:
  - tax: round(top_base_tax + (taxable_income - top_cutoff) * 0.025, 2)
  - at_zero_band_top: 82800 * 0
expected:
  tax: 5458.73
  at_zero_band_top: 0
```

## When to refuse or refer

Refer nonresident/part-year allocations, reservation/zone eligibility, farm averaging, fiduciaries, corporate returns, specialized credits, amended returns and disputed conformity. North Dakota's rolling federal starting point does not make every federal credit a state credit. The old blanket local-income-tax prohibition and blanket refund adjustment are unconfirmed and must not decide a return.

## Filing and payment

Use ND-1 with required schedules and federal attachments through supported income-tax e-filing or the applicable paper process. Use ND TAP for account payments, retain the return's acceptance and separately confirm that payment posted. Do not assume an account payment files the return.

Calendar 2026 ordinary filing/payment is generally April 15, 2027, with weekend/holiday relief. Federal extension generally extends the individual state filing date; without one, apply on Form 101 by the original date. Extension does not remove interest on unpaid tax; the read 2025 instructions allow penalty relief for payment within a valid extension, subject to the actual conditions. Recheck final 2026 procedures.

For 2026 estimates, all four ND-1ES conditions apply: federal estimated-payment duty; 2025 net tax at least USD 1,000; expected 2026 balance after withholding at least USD 1,000; withholding below the lesser of 90% current/100% prior net tax. A qualifying farmer uses the stated 66 2/3% rule. New-resident/prior-return exceptions and separate-filing changes affect the prior-year route. Ordinary installments are April 15, June 15, September 15, 2026 and January 15, 2027; eligible farmers/late-source-income cases have separate timing. The official estimate form states 12% annual underpayment interest; no estimate penalty is invented.

Under 57-38-45, timely-filed unpaid tax generally incurs 5% or USD 5 minimum; late filing adds 5% per month/part, maximum 25%, with statutory minimum/conditions. Ordinary delinquency interest is 1% per month/part starting after the due month; extension interest is 12% annual. Apply actual assessment/relief rules rather than a generic federal penalty.

## Completion checklist

- Resident/status and federal taxable-income starting point established.
- Current state modifications and any specialist schedules supported.
- 2026 return brackets distinguished from withholding and 2025 comparison.
- Credits, withholding, estimates and extension reconciled.
- Final form mapping, acceptance and payment confirmed.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 ND-1ES. Read for all 2026 status schedules, four estimate tests, safe-harbor exceptions, deadlines and 12% interest. | https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es- 2026%20final.pdf |2026-11-13 |
| N.D.C.C.57-38, especially 30.3,34,45,62-63. Read for federal base, state adjustments/exclusions, credit, filing and estimate framework. | https://ndlegis.gov/cencode/t57c38.pdf |2026-11-13 |
| 2025 individual booklet,2025-2026 filing cycle. Read for retained 2025 schedules/examples, actual ND-1 mapping, federal negative amount, adjustments, extensions and penalties. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf |2026-11-13 |
| Current individual page. Read for landing page's 2025 schedule distinction; not the source of 2026 amounts. | https://www.tax.nd.gov/individual-income-tax |2026-11-13 |

Not yet confirmed: final 2026 ND-1 line mapping, CollegeSAVE limits and full specialized zone/reservation/credit computations; the legacy blanket local-income-tax prohibition and generic refund adjustment. Ancillary `nd-return-assembly`, `nd-estimated-tax` and `nd-cross-border-tax` still retain their separate 2025 scope; do not treat their figures as 2026 updates.
