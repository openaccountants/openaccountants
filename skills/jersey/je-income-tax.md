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
last_updated: 2026-11-10
version: 1.1
review_status: pending_review
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Jersey personal income tax: 2026

## Scope and inputs

Establish residence, ordinary residence, income source and the assessment year before calculating income tax. Jersey generally taxes ordinarily resident individuals on worldwide income; resident but not ordinarily resident individuals on Jersey income and foreign income remitted to Jersey; and non-residents on Jersey income subject to exceptions. Arrival, departure and available accommodation can change the result. Read the [residence guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/IncomeTaxCircumstances/Pages/ResidencyForJerseyTax.aspx) in context and use `je-cross-border-withholding` for non-resident collection and relief.

Obtain income by source, deductible expenses, approved pension contributions, eligible allowance evidence, foreign taxes and ITIS payments. Currency is GBP. This guide's numerical examples exclude foreign tax credits, specialist residence regimes and allowance apportionment.

## Rates and allowances

The [2026 allowances schedule](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) and [Income Tax Law, Articles 92A to 92C](https://www.jerseylaw.je/laws/current/l_29_1961) establish the following comparison. The exemption reduces the marginal calculation; it is not also deducted from the standard calculation.

| 2026 item | Treatment |
|---|---|
| Standard calculation | 20% of chargeable income after allowable expenses and eligible pension deductions |
| Marginal calculation | 26% after those deductions and the applicable exemption threshold |
| Basic low income threshold | GBP 21,250 |
| Child addition | GBP 3,950 per qualifying child |
| Additional child allowance | GBP 5,900, subject to the separate qualifying conditions |
| Standard childcare relief ceiling | GBP 8,050 |
| Higher preschool childcare relief ceiling | GBP 20,950 |
| Main residence mortgage interest relief | GBP 0 |

Child relief normally requires a child under 16 or qualifying school education. Higher education has different rules. The additional child allowance requires the family and dependency conditions in the schedule. Childcare relief requires qualifying payments, a registered provider and entitlement to child relief; Article 92B further limits it by qualifying income, net payments and any sharing between claimants. A ceiling is not an automatic deduction.

Mandatory independent taxation applies to everyone from 1 January 2026. The compensatory allowance concerns qualifying couples married or in a civil partnership before 1 January 2022, still together and both Jersey resident since 2021 or earlier. Revenue Jersey applies it automatically where needed. See the [2026 schedule](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) and [2026 Budget summary](https://www.gov.je/taxesmoney/incometax/technical/guidelines/pages/2026budgetsummary.aspx).

## Calculation and examples

1. Classify taxable income and establish allowable deductions. Use [je-pension-contributions](je-pension-contributions.md) for the aggregate holder-paid approved Jersey scheme deduction under Article 131I. Establish relevant earnings and pre-contribution total income before applying its limits; do not treat all receipts or all pension payments as deductible.
2. Determine the exemption threshold from eligible reliefs, including any required apportionment.
3. Compute the standard and marginal amounts separately. Use zero when the person is exempt, otherwise the lower calculation.
4. Apply applicable foreign tax relief and other assessment adjustments under their specific provisions. Reconcile ITIS payments with the assessment; ITIS is collection on account.
5. Keep long-term care separate in the annual assessment. An ITIS rate already includes it; see `je-payroll` and `je-social-contributions`.

These illustrative 2026 comparisons assume a full GBP 21,250 threshold, no additional reliefs, no foreign tax and no other adjustments. B is income after allowable expenses and eligible pension deductions. Amounts are exact arithmetic examples, before any assessment rounding.

| B (GBP) | Standard: B x 20% | Marginal: (B - 21,250) x 26% | Income tax comparison |
|---:|---:|---:|---:|
| 21,250 | 4,250 | 0 | 0 |
| 25,000 | 5,000 | 975 | 975 |
| 100,000 | 20,000 | 20,475 | 20,000 |

The [2026 schedule](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/AllowancesReliefs/Pages/2026TaxAllowances.aspx) supplies both rates and the threshold. The 26% calculation does not impose a further tax on top of the standard amount.

## Returns and limits

If Revenue Jersey sends a return, complete it. Current [personal return guidance](https://www.gov.je/TaxesMoney/IncomeTax/Individuals/YourTaxReturn/Pages/GuidanceNotesTaxReturn.aspx) gives midnight 31 May for paper returns and midnight 31 July for online returns. The captured page offers the 2025 assessment return for the 2026 filing cycle. Confirm the notice and published timetable for the relevant assessment year before using these dates in a future-year calendar.

The ordinary Article 131I pension-holder deduction is covered in [je-pension-contributions](je-pension-contributions.md). Special pension cases, the high value residence regime, compensatory allowance computation, non-resident relief formula, assessment rounding and payment-on-account rules remain research gaps. The simplified examples do not produce a final assessment for those cases.

## Self-checks and provenance

- Verify residence separately from immigration or housing status.
- Compare both tax calculations and check relief conditions before adding allowances.
- Reconcile income tax, long-term care and ITIS without counting collection twice.

Primary pages and relevant statutory sections were read on 11 October 2026. The current Income Tax Law capture applies from 17 June 2026; check point-in-time legislation for earlier transactions. See `references.md` for captured source hashes and remaining pack gaps. This is a source-cited draft pending professional review.

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
