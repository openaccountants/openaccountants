---
name: je-pension-contributions
description: >
  Jersey pension-holder contribution deductions under Article 131I, checked
  for 2026 against current law and Revenue Jersey guidance. Use for approved
  Jersey pension contributions, relevant earnings, the annual deduction cap
  or the higher-income restriction. Covers holder-paid occupational pension,
  retirement annuity and retirement trust contributions with aggregate
  limits, classified income inputs and worked examples. Requires confirmation
  of scheme approval, the assessment year and each income source before
  calculation. Overseas schemes, employer deductions, salary sacrifice,
  withdrawals and transfers require separate advice. This source-cited draft
  awaits professional review; the deduction is not the amount of tax saved.
jurisdiction: JE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-11-10
version: 1.1
review_status: pending_review
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Jersey pension-contribution deductions: 2026

## Scope and approval

Calculate the pension holder's allowable deduction after confirming the assessment year, approved scheme status and income classifications. [Income Tax (Jersey) Law 1961, Articles 130 and 131I](https://www.jerseylaw.je/laws/current/l_29_1961) cover the holder's contributions to approved Jersey occupational pension schemes, approved Jersey retirement annuity contracts and approved Jersey retirement trust schemes. Approval under Articles 131, 131B or 131CA must be established; a product described as a pension is insufficient evidence.

Aggregate qualifying contributions actually paid by the same holder in the same year of assessment across those approved schemes. The [Revenue Jersey guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx) gives a GBP 50,000 deduction ceiling, reduced for higher income and limited by relevant earnings. It is one aggregate deduction ceiling, not a separate allowance for each scheme or a limit on how much can be paid into a pension fund.

Employer-paid contributions are subject to the separate Article 131H rules. Do not include them as holder-paid contributions merely because they benefit that holder. Employer deduction computation, overseas schemes, salary sacrifice, refunds, withdrawals and pension transfers require separate classification and provisions; this guide's formula does not decide them.

## Establish the inputs

All amounts below are GBP for one holder and one assessment year. Unknown or unclassified inputs must be resolved before calculation; do not substitute zero.

- **C: qualifying contributions paid.** Reconcile the holder's payments to each approved scheme and aggregate the actual contributions paid during the assessment year. Article 131I permits an expense deduction for that year, subject to its limits.
- **R: relevant earnings before the pension deduction.** [Article 130C](https://www.jerseylaw.je/laws/current/l_29_1961) includes income assessed to tax from employment or office emoluments excluding pension income; Schedule D income immediately derived from the individual's trade, profession or vocation, including a partner personally acting in a partnership; and the Jersey land-dealing income charged under Schedule A by Article 51(1)(b). Gross business receipts are not automatically assessed earnings. Ordinary investment income and company distributions in the official examples do not enter R. Do not classify all property income alike: the statutory land-dealing category differs from ordinary passive rental income.
- **T: total income before approved pension contributions.** Establish total income under [Article 4 and Article 131I(3)](https://www.jerseylaw.je/laws/current/l_29_1961). For this restriction, calculate T before deducting the total approved pension contributions paid, including any contributions ultimately disallowed. T can include taxable investment, distribution or property income that is outside R. Establish other allowable expenses under their own provisions; gross receipts, R and T are different inputs.

The [general pension guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx) also lists main-residence interest payments and ordinary annual contributions among amounts disregarded for this income test. The captured current Article 131I(3) expressly requires total income before approved pension contributions. Resolve the treatment of those additional items under the applicable year's Article 4 and deduction provisions, or obtain Revenue Jersey confirmation, before using them to establish T. The ordinary examples below do not settle that source difference.

Keep evidence of approval, payment dates, the reconciliation of actual payments to C and the income schedules supporting R and T. Retain the full contribution amount separately from the allowable deduction for return preparation. Follow the relevant return and assessment instructions in [je-income-tax](je-income-tax.md); the current personal-return page concerns the 2025 assessment return filed in 2026, not a verified timetable for filing 2026 income.

## Deduction calculation

[Article 131I and the official examples](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx) establish the GBP 150,000 higher-income threshold and GBP 50,000 ceiling:

1. Calculate excess income E as the positive excess of T over GBP 150,000. At exactly GBP 150,000, E is zero.
2. Calculate the fixed ceiling as GBP 50,000 less E and the relevant-earnings ceiling as R less E.
3. The allowable deduction D is limited by C and both ceilings. If either ceiling is zero or negative, no positive deduction is available. The illustrative formula uses a zero floor to represent no allowable deduction; Article 131I does not express that floor as a separate formula.
4. Deduct D once from relevant earnings when preparing the income-tax computation. Do not subtract D before establishing T for the restriction. Use [je-income-tax](je-income-tax.md) for the standard/marginal comparison, other reliefs and reconciliation of tax collected.

For verified non-negative C, R and T, the illustrative arithmetic is:

```text
E = max(0, T - 150,000)
D = max(0, min(C, 50,000 - E, R - E))
```

D is an expense deduction, not a refund or the cash tax saved. The tax effect depends on the holder's full assessment. The formula does not authorise a payment, establish approval or resolve a special residence regime.

## Worked examples and boundaries

The first six rows reconcile the [published examples](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx) using the supplied, classified inputs. The remaining rows are synthetic boundaries for the same current rule. Amounts are exact arithmetic before assessment rounding.

| Case | R (GBP) | T (GBP) | C (GBP) | E (GBP) | D (GBP) |
|---|---:|---:|---:|---:|---:|
| Official example 1, after stated subscriptions | 179,500 | 179,500 | 44,000 | 29,500 | 20,500 |
| Official examples 2 and 5, holder A | 100,000 | 160,000 | 50,000 | 10,000 | 40,000 |
| Official example 3 | 150,000 | 200,000 | 50,000 | 50,000 | 0 |
| Official example 4 | 160,000 | 170,000 | 20,000 | 20,000 | 20,000 |
| Official example 5, holder B | 40,000 | 40,000 | 50,000 | 0 | 40,000 |
| Official example 6 | 25,000 | 170,000 | 20,000 | 20,000 | 5,000 |
| Exactly at the higher-income threshold | 150,000 | 150,000 | 50,000 | 0 | 50,000 |
| One penny above the threshold | 150,000 | 150,000.01 | 50,000 | 0.01 | 49,999.99 |
| Relevant-earnings ceiling binds first | 30,000 | 170,000 | 40,000 | 20,000 | 10,000 |
| No relevant earnings | 0 | 145,000 | 10,000 | 0 | 0 |
| Excess exceeds relevant earnings | 15,000 | 170,000 | 20,000 | 20,000 | 0 |
| Excess exceeds the fixed ceiling | 201,000 | 201,000 | 50,000 | 51,000 | 0 |

Official example 1 starts with GBP 180,000 and deducts GBP 500 subscriptions before computing excess from GBP 179,500. Its contributions are GBP 14,000 plus GBP 30,000, totalling GBP 44,000. The resulting deduction is GBP 20,500. This reproduces that example's stipulated expense treatment; it does not establish that any subscription is deductible. Using unadjusted T of GBP 180,000 would instead produce GBP 20,000, which is a different input assumption.

The two holders in official example 5 are calculated separately. That example does not establish a transfer of unused limits between spouses or schemes. For 2026 independent taxation, read the conditions in [je-income-tax](je-income-tax.md).

## Self-checks, period and limits

- Confirm approval and distinguish holder payments from employer payments.
- Use assessed relevant earnings, including the specific statutory land-dealing category, and establish total income separately.
- Aggregate all qualifying holder contributions for the year, including disallowed contributions when establishing the pre-contribution income basis.
- At T of GBP 200,000 or more, the fixed deduction ceiling is exhausted. A zero relevant-earnings ceiling also permits no positive deduction.
- Reconcile D to the full income-tax assessment without treating it as tax collected or a refund.

Primary sections and official guidance were read on 11 October 2026. The current law capture applies from 17 June 2026; Article 130C's recorded substitution is L.5/2024 and Article 131I(3)'s latest recorded amendment is L.3/2016. Check point-in-time law for earlier transactions. [references.md](references.md) records the captured sources and outstanding pack coverage.

Complete scheme approval conditions, overseas treatment, employer deductions, salary sacrifice, carry-forward or other special relief, pension income, withdrawals, transfers, non-resident and special residence cases remain outside this bounded computation. Assessment rounding is not established here. This source-cited draft remains `tier: 2` and `pending_review`.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
