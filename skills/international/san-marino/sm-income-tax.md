---
name: sm-income-tax
description: >
  Prepare 2026 San Marino personal IGR by residence, source and income category, separating ordinary progressive income from business/professional and other separately taxed receipts. Reconcile wage or pension bases, documented deductions, family entitlement, the new SMaC tax credits and foreign-tax evidence before filing. Includes synthetic official-calculator comparisons and arithmetic controls. This source-cited draft replaces the approximate 2025 summary and the old expense-deduction description. Special residence schemes, complete capital/property categories, mixed-income implementation, full relief ordering and live return fields remain partial. Named San Marino accountant review remains open.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.2
sources:
  - url: "https://www.consigliograndeegenerale.sm/on-line/documento17086436.html"
    title: "Official coordinated IGR archive; selected personal income, tariff and SMaC provisions"
    as_of: "2026-10-24"
  - url: "https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html"
    title: "Law 141/2025 reform and commencement"
    as_of: "2026-10-24"
  - url: "https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33"
    title: "Authentic DD 156/2026; current personal amendments"
    as_of: "2026-10-24"
  - url: "https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49158490.html"
    title: "ISS revised 2026 contribution circular 2187/UC/2026"
    as_of: "2026-10-24"
  - url: "https://www.pa.sm/portalepa/servlet/portalepa.hic.servizi.HGCalcoloIGRLegge141_2025?MPasso=1&MTipo=G&profondita=1"
    title: "Official public 2026 IGR calculator; synthetic observations only"
    as_of: "2026-10-24"
---

# San Marino personal income tax v0.2

## Scope, period and questions

For tax year 2026, establish where the person was registered, physically present and had their centre of vital interests; collect the dates, family facts and each income category. IGR 10 uses registered residence for most of the period, actual stay for most of the period, or the centre of vital interests. The former two-limb address/183-day summary was incomplete. Residents are subject to relevant worldwide income; nonresidents to the domestic-source categories. A treaty outcome needs the actual treaty and facts. [IGR 1,5,9–10][law], read with [DD 156/2026, articles 2 and 19][october]

Use the 2026 reform, not an unmodified 2025 calculation. [Law 141/2025, article 54][reform] applies the new provisions from tax year 2026 while preserving the earlier-period regime. The official coordinated archive has distinct December 2025 editions and does not include all subsequent 2026 amendments.

## Separate the income baskets first

IGR 12 excludes exempt income and income subject to separate taxation or final withholding from the ordinary aggregate. IGR 13(1)(a) puts the covered professional/business income into separate taxation. The temporary rate for that category is **18% in tax years 2026–2030**, replacing 17%; this is not a flat rate for every individual's salary, pension, rental or investment receipt. IGR 17(1-bis) uses the combined business/professional and other relevant income to establish the progressive bands for those other receipts. Obtain the category and timing evidence before adding unlike income. [IGR 12–13 and 17][law]; [Law 141/2025, article 54(6)][reform]

Foreign dividends, other capital receipts, property gains, arrears, termination payments and special residence regimes need their own category rules. DD 156 updates capital income and foreign residential rents: article 22(2-quater) uses **60% of the relevant foreign residential rent**, not a universal property allowance. This Guide does not complete those separate bases or treaty outcomes. [IGR 13,19–23 and 25][law]; [DD 156/2026, articles 5–9][october]

## Ordinary progressive tariff

Apply each rate only to the slice in that band. These are the 2026 ordinary bands, not approximate alternatives. Annex C schedules the first indexed revaluation for **tax year 2028**, then every two years subject to its cost-of-living limit and six-percentage-point cap; no 2026 indexed thresholds are inferred. [IGR Annex C, Table 1][law]; [Law 141/2025, Annex C amendment][reform]

| Taxable-income slice, EUR | Marginal rate |
|---|---:|
| First 10,000 | 9% |
| Above 10,000 through 18,000 | 13% |
| Above 18,000 through 28,000 | 17% |
| Above 28,000 through 38,000 | 21% |
| Above 38,000 through 50,000 | 25% |
| Above 50,000 through 65,000 | 28% |
| Above 65,000 through 80,000 | 31% |
| Above 80,000 | 35% |

## Establish wage, pension and business bases

For wages, reconcile gross cash and taxable benefits under IGR 24–25, the **7% gross-wage forfait capped at 2,800**, and the legally deductible compulsory contributions under article 15. Do not compute 7% on wages already reduced by contributions. The [official 2026 calculator][calculator] confirmed this ordering in synthetic gross annual wage cases of 11,000, 30,000 and 50,000 on 24 October 2026. Its default contribution deduction is **9.9%**, composed of pension 6.9%, mandatory FONDISS 2.5% and the stated CIG/unemployment/solidarity component 0.5%; its instruction requires removing components absent from the payslip. That tax-base input is not a universal cash social-contribution total. [IGR 15 and 24][law]; [ISS 2026 circular, pages 1 and 10][iss]

Resident pensions use marginal forfait deductions of 20% on the first 13,000, 12% on the next 6,500, 9% on the next 6,500 and 7% above 26,000. Do not apply the top applicable percentage to the whole pension or substitute the salary forfait. [IGR 26][law]

Business/professional bases need actual accounts, inherent costs, timing, asset and loss workpapers. Article 30(4), replaced by DD 156 article 10, limits annual loss use to 70% of relevant taxable business income, with no time limit on carryforward. Do not retain the superseded explicit net-compulsory-contribution phrase as the current statutory wording. Full loss/contribution ordering and special adjustments need a taxpayer-specific conclusion. [IGR 27–30][law]; [DD 156/2026, article 10][october]

IGR 14 and Annexes A/B require the actual eligible documented expenses and payment trail; no duplicate claim. DD 156 changes selected family-care/voluntary-pension conditions in Annex A. Do not apply every personal expense as a deduction or confuse a deduction from income with a credit against tax. [IGR 14–16 and Annex A/B][law]; [DD 156/2026, article 17][october]

## Family credits

For fiscal residents, article 16 provides annual credits of **250 for an eligible dependent spouse**, **250 per eligible dependent child**, and **125 for the specified other dependent relatives**. Apply the actual relationship, dependency, residence/cohabitation and age/study/unemployment conditions; allocate by qualifying months. The article 16(3) income test for the specified non-child relatives refers to the social-pension amount, which is not quantified here. Nonresidents do not receive the family credits. [IGR 16(1)–(4)][law]

Child credit belongs to one parent or 50% each. DD 156 extends the rule to guardians according to the judicial decree; combined claims over 100% are corrected to 50% each. Other relatives have their separate allocation rule. The 20% uplift applies where the number of dependents exceeds two or the stated disability/permanent-illness condition applies. Two eligible children alone do not trigger that uplift. Obtain the other claimant's allocation and any judicial/medical evidence. Medical and residential-rent credits under 16(7-bis) have separate bases/caps and are not completed here. [IGR 16(5)–(8)][law]; [DD 156/2026, article 3][october]

## SMaC credit for ordinary income

The reformed article 16(8-bis) and Annex E provide a **tax credit**, limited to tax due, for qualifying wages, assimilated income and pensions of residents and nonresidents. Article 16(8-ter) extends it to the specified other ordinary income of residents, with explicit category exclusions. It is not a universal income deduction. Special documentation exceptions in 16(8-quater) require their own conditions. [IGR 16 and Annex E][law]; [Law 141/2025][reform]

At taxable income up to **8,360**, the no-SMaC portion is at most **752.40**, limited to tax. It decreases proportionately to zero at **16,720**. The documented SMaC portion increases with actual taxable income, reaching at most **1,900** at **42,500** and above, with a maximum required eligible spend of **10,000**. Above 8,360, the required spend starts at a minimum of 500. Use the actual-income interpolation and the percentage rounded **down to two decimal places** required by E3. The table values below are endpoints, not a fixed credit for every income inside a row. [Annex E3 and Table 1][law]

| Taxable-income endpoint | Total maximum credit | No-SMaC portion | Documented SMaC portion | Required spend |
|---:|---:|---:|---:|---:|
| 8,360 | 752.40 | 752.40 | 0 | 0 |
| 10,450 | 925 | 564.30 | 360.70 | 1,125 |
| 12,540 | 1,000 | 376.20 | 623.80 | 1,750 |
| 14,630 | 1,075 | 188.10 | 886.90 | 2,375 |
| 16,720 | 1,150 | 0 | 1,150 | 3,000 |
| 20,900 | 1,300 | 0 | 1,300 | 4,250 |
| 25,080 | 1,450 | 0 | 1,450 | 5,500 |
| 29,260 | 1,600 | 0 | 1,600 | 6,750 |
| 33,440 | 1,700 | 0 | 1,700 | 8,000 |
| 37,970 | 1,800 | 0 | 1,800 | 9,250 |
| 42,500 and above | 1,900 | 0 | 1,900 | 10,000 |

For income between two listed endpoints, preserve the actual calculation, not just the endpoint row. At taxable income 24,930 the official calculator returned maximum credit 1,444.62, required spend 5,455.14 and percentage 26.48%, rather than the 25,080 endpoint's 1,450. At taxable income 9,141 it returned no-SMaC 682.11, documented portion 134.79, required spend 733.55 and total 816.90. First-band minimum-spend and partial-credit rounding should be checked with the official program and actual certificate; these observations do not validate every boundary or rounding combination. [Annex E3][law]; [official public calculator][calculator]

Classify the actual purchases under E1 before using spend: eligible fuel has a 1,500 limit; online purchases require a San Marino supplier seat, branch or PE. Utilities and damage insurance have a limited actual-home exception for residents, not a blanket all-invoice entitlement. E2, replaced by DD 156, permits eligible dependent spending and the specified excess spending of cohabiting spouse/nondependent cohabitants, subject to each person's limit and exclusions. The cohabitant definition includes the specified second-degree relatives/affinity and de facto partners. Obtain each person's own spending/limit and avoid duplication. [Annex E1–E3][law]; [DD 156/2026, article 18][october]

## Business SMaC and mixed income

IGR 17(1-ter) credits qualifying business/professional SMaC spending against the specified separate tax: taxable income up to 25,000 uses 18% of eligible spend capped at 5,000; above 50,000 uses 9% capped at 10,000. Between 25,000 and 50,000 the credit cap is 900 and the prescribed percentage uses the changing spend denominator, rounded down to four decimals; retain a separate calculation rather than extending 18% through the band. DD 156 adds **17(1-quater)**: a person with business/professional and wage/assimilated/pension income elects in the declaration between the article 16(8-bis) credit and article 17(1-ter) credit. Do not claim both automatically. The article 17(1-bis) band-stacking rule is preserved. [IGR 17][law]; [DD 156/2026, article 4][october]

## Foreign tax, withholding and filing

Article 18 requires final, nonrefundable foreign tax on the relevant declared income, with a separate limit for each State. For ordinary nonbusiness income, the ceiling is domestic net tax multiplied by foreign income divided by aggregate income. Business/professional income has the separate foreign-gross-receipts/total-receipts fraction of the relevant net tax after admitted losses. Partially included foreign income requires corresponding foreign-tax proration. Preserve payment/finality evidence and the declaration-year/31 December rule, later-payment timing and three-year correction provisions. An omitted return or undeclared foreign income bars the credit under 18(6); no general unused-credit carryforward is established here. [IGR 18][law]

Reconcile actual payroll withholding and other creditable payments, distinguishing final withholding. Article 101 annualises anticipated income and permits requested credits; the year-end adjustment is collected through February of the next period. The employer's IGR G certificate has the statutory **15 April** transmission deadline. A single-employer/pension return exemption applies only if article 84's conditions are met. Otherwise the general return and balance deadline is **31 July following the income year**, with the article 93 holiday/office-closure rule. Do not retain the old approximate 30 June deadline. [IGR 84–85,93,101 and 124][law]

Obtain the current forms, attachment circular, actual 2027 calendar and payment receipts. Business advances have a separate statutory route; use the [corporate procedure discussion](sm-corporate-income-tax.md) only after checking the person's actual article 124 scope. Late-return validity under 93/137, correction windows under 93-bis and sanctions need separate case analysis. DD 156 article 16 gives specified exclusive-personal-income late-return charges of 100, reduced to 50 within thirty days, while the ordinary charge is 400/200. Category and legal validity matter; a reduced fine is not proof a late return preserves relief. [IGR 93–94,124,137–139][law]; [DD 156/2026, article 16][october]

## Worked controls

### Official synthetic annual wage 30,000

Assume all three default deductible contribution components apply, no benefits/other income/family credits, and enough verified eligible SMaC spend for the maximum credit. The public program returned these figures on 24 October 2026. This is a tax calculation, not a net-pay computation from universal cash contributions. The credit is interpolated between the 20,900 and 25,080 endpoints; full-credit output is kept separate from rounding a partial-spend percentage.

```oa-check
name: San Marino official 2026 synthetic wage and SMaC interpolation
inputs:
  gross_wage: 30000
  verified_tax_deductible_contribution_rate: 0.099
  lower_income_endpoint: 20900
  upper_income_endpoint: 25080
  lower_credit: 1300
  upper_credit: 1450
  lower_spend: 4250
  upper_spend: 5500
steps:
  wage_forfait: min(gross_wage * 0.07, 2800)
  deductible_contributions: gross_wage * verified_tax_deductible_contribution_rate
  taxable_wage: gross_wage - wage_forfait - deductible_contributions
  tariff_tax: 10000 * 0.09 + 8000 * 0.13 + (taxable_wage - 18000) * 0.17
  endpoint_fraction: (taxable_wage - lower_income_endpoint) / (upper_income_endpoint - lower_income_endpoint)
  maximum_credit: round(lower_credit + endpoint_fraction * (upper_credit - lower_credit), 2)
  required_eligible_spend: round(lower_spend + endpoint_fraction * (upper_spend - lower_spend), 2)
  stated_credit_percentage: floor(maximum_credit / required_eligible_spend * 10000) / 100
  annual_igr_after_full_credit: tariff_tax - maximum_credit
expected:
  wage_forfait: 2100
  deductible_contributions: 2970
  taxable_wage: 24930
  tariff_tax: 3118.10
  maximum_credit: 1444.62
  required_eligible_spend: 5455.14
  stated_credit_percentage: 26.48
  annual_igr_after_full_credit: 1673.48
```

### Lower ordinary income and nonrefundable credit

Assume 8,000 eligible ordinary taxable wage income after all base deductions, no other income or credit. Tax is 720; the no-SMaC maximum 752.40 is limited to tax, so there is no negative tax/refund from this credit.

```oa-check
name: San Marino low taxable wage credit limited to tax
inputs:
  taxable_wage: 8000
  first_band_rate: 0.09
  no_smac_credit_cap: 752.40
steps:
  tariff_tax: taxable_wage * first_band_rate
  usable_credit: min(tariff_tax, no_smac_credit_cap)
  net_igr: tariff_tax - usable_credit
expected:
  tariff_tax: 720
  usable_credit: 720
  net_igr: 0
```

### Full tariff at 85,000

Assume ordinary taxable income 85,000 and calculate before credits; this does not establish SMaC or family eligibility.

```oa-check
name: San Marino all eight ordinary marginal bands
inputs:
  ordinary_taxable_income: 85000
steps:
  tariff_tax_before_credits: 10000 * 0.09 + 8000 * 0.13 + 10000 * 0.17 + 10000 * 0.21 + 12000 * 0.25 + 15000 * 0.28 + 15000 * 0.31 + (ordinary_taxable_income - 80000) * 0.35
expected:
  tariff_tax_before_credits: 19340
```

### Exclusive business category

Assume 20,000 established taxable professional/business income, no wages, other receipts, losses or relief; all 5,000 spending is eligible under 17(1-ter). Separate 18% tax is 3,600; credit 900; tax after this credit 2,700. The mixed-income election is outside this example.

```oa-check
name: San Marino exclusive business income and eligible SMaC credit
inputs:
  established_business_taxable_income: 20000
  covered_separate_rate: 0.18
  eligible_smac_spend: 5000
steps:
  separate_igr: established_business_taxable_income * covered_separate_rate
  eligible_credit: min(separate_igr, min(eligible_smac_spend, 5000) * 0.18)
  net_separate_igr: separate_igr - eligible_credit
expected:
  separate_igr: 3600
  eligible_credit: 900
  net_separate_igr: 2700
```

### Personal foreign-tax limit

Assume article 18(1) ordinary nonbusiness income only, one foreign State, total income 60,000 including foreign income 15,000, already established domestic net tax 10,000 and final nonrefundable eligible foreign tax 3,000, with full declaration/timing compliance. The ceiling is 2,500, leaving 500 uncredited; no automatic carryforward is assumed.

```oa-check
name: San Marino personal nonbusiness foreign tax ceiling
inputs:
  established_domestic_net_tax: 10000
  total_income: 60000
  included_foreign_income: 15000
  eligible_final_foreign_tax: 3000
steps:
  state_credit_limit: established_domestic_net_tax * included_foreign_income / total_income
  allowed_foreign_credit: min(eligible_final_foreign_tax, state_credit_limit)
  uncredited_foreign_tax: eligible_final_foreign_tax - allowed_foreign_credit
expected:
  state_credit_limit: 2500
  allowed_foreign_credit: 2500
  uncredited_foreign_tax: 500
```

### Two parents, two eligible children

Assume two fiscal resident parents, two eligible dependent children throughout twelve months, a valid 50/50 choice, enough tax and no disability/permanent-illness or other dependents. The credit is 250 for each parent. Two dependents do not satisfy the more-than-two uplift condition.

```oa-check
name: San Marino two-child family credit shared without uplift
inputs:
  eligible_children: 2
  annual_credit_per_child: 250
  qualifying_months: 12
  months_in_year: 12
  parent_share: 0.50
steps:
  whole_child_credit: eligible_children * annual_credit_per_child * qualifying_months / months_in_year
  credit_for_each_parent: whole_child_credit * parent_share
expected:
  whole_child_credit: 500
  credit_for_each_parent: 250
```

## Limits and referral

IT-PIT remains partial: complete capital/property/separate income classifications, special residence, all base adjustments, healthcare/rental relief, family-income thresholds, mixed-income ordering, foreign payment-year corrections, every SMaC boundary and live forms remain open. Record the exact unresolved fact/rule and refer before filing. The arithmetic controls establish assumed calculations, not entitlement or independent review.

## Sources

Read 24 October 2026: selected IGR articles 1,5,9–18,24–26,30,84–85,93–94,101,124,137–139 and Annex C/E in the official coordinated archive; relevant reform provisions of Law 141/2025; all twenty articles of authentic DD 156/2026. The December 2025 archive editions are dated aids, not a complete 2026 consolidation. ISS circular 2187/UC/2026 pages 1,4,5 and 10 were visually checked; other pages OCR-read. The public tax calculator was exercised with three synthetic wage amounts only, with no authentication, personal data, declaration, filing or payment. Its results are guidance alongside the law and do not validate every fact pattern. Earlier approximate wording remains in Git history. The dated pack record identifies independent source-review scope and limits; named local accountant review remains open.

[law]: https://www.consigliograndeegenerale.sm/on-line/documento17086436.html
[reform]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html
[october]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33
[iss]: https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49158490.html
[calculator]: https://www.pa.sm/portalepa/servlet/portalepa.hic.servizi.HGCalcoloIGRLegge141_2025?MPasso=1&MTipo=G&profondita=1

## Source-review status

See the [independent source-review record](../../../docs/research/2026-10-24-san-marino-pack-review.md) for its exact revision, scope and findings. Named San Marino accountant review remains open. This record is separate from comprehensive coverage, named professional approval and live filing.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
