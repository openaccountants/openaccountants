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
type: computation
last_updated: 2026-11-14
version: 1.2
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Jersey pension-contribution deductions: 2026

Tax year: the 2026 year of assessment. Currency is GBP. Authority: Revenue Jersey. Law: Income Tax (Jersey) Law 1961, Articles 130 to 131I.

## Who this applies to

Calculate the pension holder's allowable deduction after confirming the assessment year, approved scheme status and income classifications. [Income Tax (Jersey) Law 1961, Articles 130 and 131I](https://www.jerseylaw.je/laws/current/l_29_1961) cover the holder's contributions to approved Jersey occupational pension schemes, approved Jersey retirement annuity contracts and approved Jersey retirement trust schemes. Approval under Articles 131, 131B or 131CA must be established; a product described as a pension is insufficient evidence.

Aggregate qualifying contributions actually paid by the same holder in the same year of assessment across those approved schemes. The [Revenue Jersey guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx) gives a GBP 50,000 deduction ceiling, reduced for higher income and limited by relevant earnings. It is one aggregate deduction ceiling, not a separate allowance for each scheme or a limit on how much can be paid into a pension fund.

Employer-paid contributions are subject to the separate Article 131H rules. Do not include them as holder-paid contributions merely because they benefit that holder. Employer deduction computation, overseas schemes, salary sacrifice, refunds, withdrawals and pension transfers require separate classification and provisions; this guide's formula does not decide them.

## Rates, bands and thresholds

| 2026 item | Amount | Conditions | Source |
|---|---|---|---|
| Fixed deduction ceiling | GBP 50,000 less any higher income excess | One aggregate ceiling per holder per year across all approved schemes | [Revenue Jersey pension deductions](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx) |
| Higher-income threshold | GBP 150,000 of total income | Excess is the amount of total income (before approved pension contributions) above GBP 150,000; it reduces both ceilings | [Income Tax Law, Art. 131I(3)](https://www.jerseylaw.je/laws/current/l_29_1961) |
| Relevant-earnings ceiling | Relevant earnings less any higher income excess | Relevant earnings as defined in Article 130C | [Income Tax Law, Art. 130C](https://www.jerseylaw.je/laws/current/l_29_1961) |
| Ceiling exhausted | Total income of GBP 200,000 or more | The fixed ceiling reaches zero (derived from the two figures above) | [Revenue Jersey pension deductions](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx) |

## The base

All amounts below are GBP for one holder and one assessment year. Unknown or unclassified inputs must be resolved before calculation; do not substitute zero.

- **C: qualifying contributions paid.** Reconcile the holder's payments to each approved scheme and aggregate the actual contributions paid during the assessment year. Article 131I permits an expense deduction for that year, subject to its limits.
- **R: relevant earnings before the pension deduction.** [Article 130C](https://www.jerseylaw.je/laws/current/l_29_1961) includes income assessed to tax from employment or office emoluments excluding pension income; Schedule D income immediately derived from the individual's trade, profession or vocation, including a partner personally acting in a partnership; and the Jersey land-dealing income charged under Schedule A by Article 51(1)(b). Gross business receipts are not automatically assessed earnings. Ordinary investment income and company distributions in the official examples do not enter R. Do not classify all property income alike: the statutory land-dealing category differs from ordinary passive rental income.
- **T: total income before approved pension contributions.** Establish total income under [Article 4 and Article 131I(3)](https://www.jerseylaw.je/laws/current/l_29_1961). For this restriction, calculate T before deducting the total approved pension contributions paid, including any contributions ultimately disallowed. T can include taxable investment, distribution or property income that is outside R. Establish other allowable expenses under their own provisions; gross receipts, R and T are different inputs.

The [general pension guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx) also lists main-residence interest payments and ordinary annual contributions among amounts disregarded for this income test. The captured current Article 131I(3) expressly requires total income before approved pension contributions. Resolve the treatment of those additional items under the applicable year's Article 4 and deduction provisions, or obtain Revenue Jersey confirmation, before using them to establish T. The ordinary examples below do not settle that source difference.

### Deduction calculation

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

## Deadlines and filing

Keep evidence of approval, payment dates, the reconciliation of actual payments to C and the income schedules supporting R and T. Retain the full contribution amount separately from the allowable deduction for return preparation. Follow the relevant return and assessment instructions in [je-income-tax](je-income-tax.md); the current personal-return page concerns the 2025 assessment return filed in 2026, not a verified timetable for filing 2026 income.

## Penalties and interest

This guide sets no penalty of its own. Return, assessment and payment penalties are in [je-income-tax-compliance](je-income-tax-compliance.md).

## Cross-border points

Overseas schemes, non-resident and special residence cases remain outside this bounded computation. Only approved Jersey schemes under Articles 131, 131B or 131CA are in scope.

## Two worked examples that recompute

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

**Example 1: official example 1, the fixed ceiling binds.**

```oa-check
name: Jersey 2026 pension deduction, official example 1 (T and R GBP 179,500, C GBP 44,000)
inputs:
  r: 179500
  t: 179500
  c: 44000
steps:
  - e: max(0, t - 150000)
  - d: max(0, min(c, 50000 - e, r - e))
expected:
  e: 29500
  d: 20500
```

**Example 2: official example 6, the relevant-earnings ceiling binds.** Salary GBP 25,000 plus a GBP 145,000 company distribution: the distribution enters T but not R.

```oa-check
name: Jersey 2026 pension deduction, official example 6 (R GBP 25,000, T GBP 170,000, C GBP 20,000)
inputs:
  r: 25000
  t: 170000
  c: 20000
steps:
  - e: max(0, t - 150000)
  - d: max(0, min(c, 50000 - e, r - e))
expected:
  e: 20000
  d: 5000
```

## Ask the client first

1. Is each scheme an approved Jersey scheme under Article 131, 131B or 131CA, with evidence?
2. How much did you (not your employer) actually pay into each scheme during the 2026 year of assessment?
3. What are your relevant earnings: employment, self-employment or partnership, and any land-dealing income?
4. What is your total income before pension contributions, including investment, distribution and property income?
5. Are any contributions salary sacrifice, employer-paid, overseas, refunds or transfers?

Self-checks:

- Confirm approval and distinguish holder payments from employer payments.
- Use assessed relevant earnings, including the specific statutory land-dealing category, and establish total income separately.
- Aggregate all qualifying holder contributions for the year, including disallowed contributions when establishing the pre-contribution income basis.
- At T of GBP 200,000 or more, the fixed deduction ceiling is exhausted. A zero relevant-earnings ceiling also permits no positive deduction.
- Reconcile D to the full income-tax assessment without treating it as tax collected or a refund.

## Sources

Primary sections and official guidance were read on 11 October 2026; the Revenue Jersey guidance page was re-read on 14 November 2026 and its figures and examples 1 and 6 matched. The current law capture applies from 17 June 2026; Article 130C's recorded substitution is L.5/2024 and Article 131I(3)'s latest recorded amendment is L.3/2016. Check point-in-time law for earlier transactions. [references.md](references.md) records the captured sources and outstanding pack coverage.

| Source | URL | Read on |
|---|---|---|
| Revenue Jersey, Deductions for pension contributions: read for the GBP 50,000 ceiling, the GBP 150,000 threshold and official examples 1 to 6 | https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/pages/deductionsforpensioncontributions.aspx | 2026-11-14 |
| Income Tax (Jersey) Law 1961, Arts. 4, 130, 130C, 131, 131B, 131CA, 131H and 131I: read for approval, relevant earnings, total income and the deduction | https://www.jerseylaw.je/laws/current/l_29_1961 | 2026-10-11 |
| Revenue Jersey, 2026 tax allowances and reliefs: read for the retirement annuity relief line | https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx | 2026-11-14 |

Not yet confirmed: whether main-residence interest and ordinary annual contributions are disregarded in T (guidance says yes; Article 131I(3) as captured does not say so). Complete scheme approval conditions, overseas treatment, employer deductions, salary sacrifice, carry-forward or other special relief, pension income, withdrawals, transfers, non-resident and special residence cases remain outside this bounded computation. Assessment rounding is not established here.
