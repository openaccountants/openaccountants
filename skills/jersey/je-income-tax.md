---
name: je-income-tax
description: >
  Jersey personal income tax for the 2026 year of assessment, including tax
  residence, the standard and marginal calculations, exemption thresholds,
  independent taxation and return preparation. Use for Jersey individual tax,
  marginal relief, child allowances, pension deductions or moving to Jersey.
  Covers ordinary individual assessments with source links and simplified
  arithmetic examples. Requires separate classification of foreign income,
  relief eligibility and payments already collected. Specialist residence
  concessions, special pension cases and a person's final assessment require
  further verification. This source-cited draft awaits professional review
  and does not establish that the Jersey pack is complete.
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

# Jersey personal income tax: 2026

Tax year: the 2026 year of assessment (1 January to 31 December 2026). Currency is GBP. Authority: Revenue Jersey. Law: Income Tax (Jersey) Law 1961.

## Who this applies to

Establish residence, ordinary residence, income source and the assessment year before calculating income tax. Jersey generally taxes ordinarily resident individuals on worldwide income; resident but not ordinarily resident individuals on Jersey income and foreign income remitted to Jersey; and non-residents on Jersey income subject to exceptions. Arrival, departure and available accommodation can change the result. Read the [residence guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/Pages/ResidencyForJerseyTax.aspx) in context and use `je-cross-border-withholding` for non-resident collection and relief.

Mandatory independent taxation applies to everyone from 1 January 2026. The compensatory allowance concerns qualifying couples married or in a civil partnership before 1 January 2022, still together and both Jersey resident since 2021 or earlier. Revenue Jersey applies it automatically where needed. See the [2026 schedule](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) and [2026 Budget summary](https://www.gov.je/taxesmoney/incometax/technical/guidelines/pages/2026budgetsummary.aspx).

## Rates, bands and thresholds

The [2026 allowances schedule](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) and [Income Tax Law, Articles 92A to 92C](https://www.jerseylaw.je/laws/current/l_29_1961) establish the following comparison. The exemption reduces the marginal calculation; it is not also deducted from the standard calculation.

| 2026 item | Rate or amount | Conditions | Source |
|---|---|---|---|
| Standard calculation | 20% | Of chargeable income after allowable expenses and eligible pension deductions | [2026 allowances](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) |
| Marginal calculation | 26% | After those deductions and the applicable exemption threshold; the person pays the lower of the two calculations | [2026 allowances](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) |
| Basic low income threshold | GBP 21,250 | Per individual under independent taxation | [2026 allowances](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) |
| Child addition | GBP 3,950 per qualifying child | Child under 16 or in qualifying school education; higher education has different rules | [2026 allowances](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) |
| Additional child allowance | GBP 5,900 | Subject to the separate qualifying conditions in the schedule: unmarried or not in a civil partnership, or wholly maintaining a totally incapacitated spouse or civil partner; child under 25 on 31 August 2026 | [2026 allowances](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) |
| Standard childcare relief ceiling | GBP 8,050 | Qualifying payments, registered provider, entitlement to child relief; Article 92B limits | [2026 allowances](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) |
| Higher preschool childcare relief ceiling | GBP 20,950 | Pre-school children; same conditions | [2026 allowances](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) |
| Main residence mortgage interest relief | GBP 0 | Phased out | [2026 allowances](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) |

Child relief normally requires a child under 16 or qualifying school education. Higher education has different rules. The additional child allowance requires the family and dependency conditions in the schedule. Childcare relief requires qualifying payments, a registered provider and entitlement to child relief; Article 92B further limits it by qualifying income, net payments and any sharing between claimants. A ceiling is not an automatic deduction.

## The base

Obtain income by source, deductible expenses, approved pension contributions, eligible allowance evidence, foreign taxes and ITIS payments. This guide's numerical examples exclude foreign tax credits, specialist residence regimes and allowance apportionment.

1. Classify taxable income and establish allowable deductions. Use [je-pension-contributions](je-pension-contributions.md) for the aggregate holder-paid approved Jersey scheme deduction under Article 131I. Establish relevant earnings and pre-contribution total income before applying its limits; do not treat all receipts or all pension payments as deductible.
2. Determine the exemption threshold from eligible reliefs, including any required apportionment.
3. Compute the standard and marginal amounts separately. Use zero when the person is exempt, otherwise the lower calculation.
4. Apply applicable foreign tax relief and other assessment adjustments under their specific provisions. Reconcile ITIS payments with the assessment; ITIS is collection on account.
5. Keep long-term care separate in the annual assessment. An ITIS rate already includes it; see `je-payroll` and `je-social-contributions`.

## Deadlines and filing

If Revenue Jersey sends a return, complete it. Current [personal return guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/YourTaxReturn/Pages/GuidanceNotesTaxReturn.aspx) gives midnight 31 May for paper returns and midnight 31 July for online returns. The captured page offers the 2025 assessment return for the 2026 filing cycle. Confirm the notice and published timetable for the relevant assessment year before using these dates in a future-year calendar.

The ordinary Article 131I pension-holder deduction is covered in [je-pension-contributions](je-pension-contributions.md). Special pension cases, the high value residence regime, compensatory allowance computation, non-resident relief formula, assessment rounding and payment-on-account rules remain research gaps. The simplified examples do not produce a final assessment for those cases.

## Penalties and interest

Late-return penalties, abatements, default assessments, appeals and the late-payment surcharge are in [je-income-tax-compliance](je-income-tax-compliance.md). They are not restated here (one figure, one home).

## Cross-border points

Residence and source rules are summarised under "Who this applies to". Non-resident collection, Article 118B categories, landlord deductions and double taxation relief are in `je-cross-border-withholding`. Foreign tax relief is applied at step 4 of the base under its specific provisions; this guide does not compute it.

## Two worked examples that recompute

These illustrative 2026 comparisons assume a full GBP 21,250 threshold, no additional reliefs, no foreign tax and no other adjustments. B is income after allowable expenses and eligible pension deductions. Amounts are exact arithmetic examples, before any assessment rounding.

| B (GBP) | Standard: B x 20% | Marginal: (B - 21,250) x 26% | Income tax comparison |
|---:|---:|---:|---:|
| 21,250 | 4,250 | 0 | 0 |
| 25,000 | 5,000 | 975 | 975 |
| 100,000 | 20,000 | 20,475 | 20,000 |

The [2026 schedule](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) supplies both rates and the threshold. The 26% calculation does not impose a further tax on top of the standard amount.

**Example 1: income GBP 25,000, the marginal calculation decides.** Standard GBP 5,000; marginal (25,000 - 21,250) x 26% = GBP 975. The lower figure, GBP 975, is the tax (derived).

```oa-check
name: Jersey 2026, B GBP 25,000, basic threshold, marginal calculation wins
inputs:
  b: 25000
  threshold: 21250
steps:
  - standard: b * 0.20
  - marginal: max(b - threshold, 0) * 0.26
  - tax: min(standard, marginal)
expected:
  standard: 5000
  marginal: 975
  tax: 975
```

**Example 2: income GBP 100,000, with and without one child addition.** Without a child, standard GBP 20,000 against marginal GBP 20,475: the standard calculation decides and the tax is GBP 20,000. With one qualifying child the threshold rises by GBP 3,950, the marginal calculation falls to (100,000 - 21,250 - 3,950) x 26% = GBP 19,448 (derived), below the standard amount, so the tax is GBP 19,448 (derived). Check the child's eligibility before using the addition.

```oa-check
name: Jersey 2026, B GBP 100,000, effect of one child addition
inputs:
  b: 100000
  threshold: 21250
  child_addition: 3950
steps:
  - standard: b * 0.20
  - marginal_no_child: (b - threshold) * 0.26
  - tax_no_child: min(standard, marginal_no_child)
  - marginal_one_child: (b - threshold - child_addition) * 0.26
  - tax_one_child: min(standard, marginal_one_child)
expected:
  standard: 20000
  marginal_no_child: 20475
  tax_no_child: 20000
  marginal_one_child: 19448
  tax_one_child: 19448
```

## Ask the client first

1. Are you resident, ordinarily resident or non-resident in Jersey for 2026, and when did you arrive or leave?
2. What income did you have, by source, and what allowable expenses relate to it?
3. Did you pay into an approved Jersey pension scheme, and how much (see `je-pension-contributions`)?
4. Which children, childcare costs or other reliefs do you claim, with evidence?
5. Did you pay foreign tax on any of the income?
6. How much was collected through ITIS during the year?

Self-checks:

- Verify residence separately from immigration or housing status.
- Compare both tax calculations and check relief conditions before adding allowances.
- Reconcile income tax, long-term care and ITIS without counting collection twice.

## Sources

Primary pages and relevant statutory sections were read on 11 October 2026; the 2026 allowances page was re-read on 14 November 2026 and its figures matched. The current Income Tax Law capture applies from 17 June 2026; check point-in-time legislation for earlier transactions. See `references.md` for captured source hashes and remaining pack gaps. This is a source-cited draft pending professional review.

| Source | URL | Read on |
|---|---|---|
| Revenue Jersey, 2026 tax allowances and reliefs: read for the 20% and 26% rates, the GBP 21,250 threshold, child, additional child, childcare and mortgage interest figures | https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx | 2026-11-14 |
| Income Tax (Jersey) Law 1961, Arts. 92A to 92C and 131I: read for the exemption threshold, childcare relief limits and pension deduction | https://www.jerseylaw.je/laws/current/l_29_1961 | 2026-10-11 |
| Revenue Jersey, Residency for Jersey income tax: read for residence and ordinary residence | https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/Pages/ResidencyForJerseyTax.aspx | 2026-10-11 |
| Revenue Jersey, 2026 Budget summary: read for independent taxation and the compensatory allowance | https://www.gov.je/taxesmoney/incometax/technical/guidelines/pages/2026budgetsummary.aspx | 2026-10-11 |
| Revenue Jersey, Help with filling out your paper personal tax return: read for the 31 May and 31 July return deadlines | https://www.gov.je/TaxesMoney/IncomeTax/Individuals/YourTaxReturn/Pages/GuidanceNotesTaxReturn.aspx | 2026-10-11 |

Not yet confirmed: the 31 May and 31 July return deadlines are from the page offering the 2025 assessment return (2025-2026 filing cycle); the 2026 assessment timetable is not yet published. Special pension cases, the high value residence regime, the compensatory allowance computation, the non-resident relief formula, assessment rounding and payment-on-account rules are not covered.
