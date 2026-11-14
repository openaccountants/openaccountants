---
name: mo-corporate-tax
description: "Missouri MO-1120: 4% corporate tax, federal liability deduction, receipts apportionment, 2026 estimates, specie subtraction and explicit PTE/special-regime limits."
version: "0.2"
jurisdiction: US-MO
category: state-tax
tax_year: 2026
last_updated: 2026-11-14
tier: 2
type: computation
---

# Missouri corporate income and franchise tax, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

## Who this applies to

Corporations filing Missouri MO-1120, including federally taxable unrelated business income, with Missouri source income and sufficient nexus. This skill owns the corporate/franchise job; `mo-income-tax` owns individual owners, `mo-payroll` employer withholding/UI and `mo-sales-tax` sales/use. Federal computation belongs to `us-form-1120-c-corp`; use the actual federal return, not an invented Missouri federal rate. Published 2026 MO-1120ES supplies current estimates. Annual return mapping is the final **2025-2026 filing cycle**, pending final 2026 MO-1120/MO-MS.

The annual booklet requires a return for each year a corporation must file federally and its Missouri-source gross income is 100 or more. Federal tax-exempt organizations generally do not send federal 990 copies or MO-1120 merely because they exist; taxable UBTI and other federally taxable income are exceptions. Insurance, express companies and other statutory exempt taxpayers have special regimes. Register for a Missouri Tax ID through MyTax Missouri/business registration. [Annual booklet, p.2](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf).

## Rates, bands and thresholds

| Item | Rule / amount in USD | Official source |
| --- | --- | --- |
| Corporate income tax | 4% of Missouri taxable income; rate in force for 2020 onward | [2026 MO-1120ES worksheet](https://dor.mo.gov/forms/MO-1120ES_2026.pdf); [corporate FAQ](https://dor.mo.gov/faq/taxation/business/corporation-income.html) |
| Ordinary corporate filing income threshold | Missouri-source gross income 100 or more, with federal filing requirement and nexus | [Annual booklet, p.2](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf) |
| Corporate federal-income-tax deduction | 50% of eligible current-year federal liability, subject to group allocation | [143.171.3](https://revisor.mo.gov/main/OneSection.aspx?section=143.171); [annual Part 3](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf) |
| Corporate estimates | Expected Missouri tax 250 or more | [2026 MO-1120ES](https://dor.mo.gov/forms/MO-1120ES_2026.pdf) |
| Large-corporation estimate boundary | In any preceding 3 years, federal taxable income of at least one million dollars **and** Missouri taxable income of at least one hundred thousand dollars | [2026 MO-1120ES /143.761.6](https://dor.mo.gov/forms/MO-1120ES_2026.pdf) |
| Ordinary corporation franchise tax | Zero; no ordinary franchise return for tax years beginning on/after January 1,2016 | [DOR franchise phase-out bulletin](https://dor.mo.gov/pdf/TaxBulletin-10-26-15.pdf) |
| Specie capital-gain subtraction | Gold/silver specie gain included in federal taxable income, beginning 2026; separate from general corporate capital-gain trigger | [Current specie FAQ](https://dor.mo.gov/faq/taxation/individual/specie_subtraction.html) |

The individual general capital-gain subtraction does **not** automatically exempt all 2026 corporate gains. Section 143.121.3(14)(b) starts the corporate general exclusion in the year following a reduction of the top individual rate to 4.5% or less. The published 2026 individual schedule remains 4.7%, so this pack does not apply that corporate exclusion. The separate 2026 specie rule can apply. [143.121](https://revisor.mo.gov/main/OneSection.aspx?section=143.121); [2026 MO-1040ES](https://dor.mo.gov/forms/MO-1040ES_2026.pdf).

## The base

Start with federal taxable income after federal NOL/special deductions: final 2025 MO-1120 line 1 uses federal 1120 line 30. Add Missouri and other-state corporate income taxes deducted federally, including qualifying income-based franchise taxes, but the instructions exclude St. Louis/Kansas City earnings taxes from this particular add-back. Add other Missouri modifications; subtract eligible modifications; then deduct 50% of the eligible federal-income-tax liability. This yields all-source Missouri taxable income **before** apportionment. An estimate using federal gross receipts or cash profit alone is insufficient. [Annual booklet, pp.4-5, Part 1-3](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf).

The federal-tax deduction is liability after statutory credit adjustments, not estimated federal payments. The annual Part 3 adds the specified federal tax and foreign-tax-credit amounts, then takes 50%. If federally consolidated but Missouri separate, allocate 50% of consolidated eligible federal tax by separate-company federal taxable income divided by total **positive** separate-company taxable incomes; do not include loss companies in that denominator. Follow 12 CSR10-2.090/2.165 and attach consolidated Schedule J, pro forma federal return and income statements. A consolidated Missouri return requires federal consolidation and initial/new-member MO-22 consents; do not invent mandatory unitary combined filing. [Annual booklet, pp.3-4,9](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf); [143.171](https://revisor.mo.gov/main/OneSection.aspx?section=143.171).

Modifications include non-Missouri governmental-bond interest net of specified related expenses, qualifying U.S.-obligation income, included state income-tax refunds, agricultural-disaster relief, grant and historical basis adjustments. Missouri's business-interest rules can subtract current expense disallowed federally under 163(j) and add back a later federal carryforward deduction, preventing duplication. Historical bonus-depreciation adjustments in this booklet relate to property purchased July 1,2002-June 30,2003; do not impose a blanket current-year bonus add-back based on another state's rule. Track actual current federal/state conformity and vintage schedules. [Annual Part 1/2, pp.8-9](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf).

There is no freestanding Missouri NOL generated simply by negative state additions/subtractions. Federal NOL and separate-company schedules control, with Missouri modification, apportionment and vintage rules. For a loss used in another year, retain loss-year amount, prior utilization, current use, federal consolidated and separate-company computations and any required MO-5090. Do not state a new Missouri 20-year carryforward for every 2026 operating loss or reproduce federal loss limits here. [Annual booklet, pp.3,8-12](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf); [corporate FAQ, NOL questions](https://dor.mo.gov/faq/taxation/business/corporation-income.html).

For 2026 specie gains, use the final 2026 subtraction line once published. For an unusual short tax year beginning and ending 2026 filed before those forms exist, DOR expressly permits a statement and 2025 MO-1120 Page 3 Part 2 line 7. That exception is not permission to reuse 2025 forms for every calendar 2026 filing. Individuals do not duplicate this subtraction. [DOR specie instructions](https://dor.mo.gov/faq/taxation/individual/specie_subtraction.html).

## Deadlines and filing

Ordinary MO-1120 is due the 15th day of the fourth month after year end; calendar 2025 was April 15,2026, while calendar 2026 ordinarily is April 15,2027 subject to closed days/relief. An approved federal extension extends Missouri filing when the box is checked and federal 7004 attached; it does not extend payment. Use MO-7004 with timely estimated tax if a balance is expected. Qualified farmers' cooperatives and special federal-return filers have exceptions; confirm the actual entity instead of assuming the ordinary deadline. [Annual booklet, pp.2-4](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf).

File through approved e-file or the balance-due/refund paper address. Attach the federal return/pro forma, all modifications, MO-MS/MO-NAI/MO-C when applicable, MO-TC and certified credit support, and subsidiary payment allocation/MO-851 for a group. Net dividends included federally can require the Missouri dividend deduction and MO-C allocation; do not deduct the same dividends twice. Low-income-housing credit recapture follows the federal recapture proportion. Amend on MO-1120 marked amended, completing the full corrected return and reason. Federal changes generally require Missouri correction within 90 days as instructed. [Annual booklet, pp.3-5,9-12](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf).

2026 corporation estimates use MO-1120ES on the 15th of months 4,6,9 and 12: ordinary calendar dates April 15, June 15, September 15, December 15, adjusted for closed days. They are not individual January installments. The published penalty exceptions include timely cumulative 90% current tax or 100% prior 12-month return that showed liability, with annualized/actual-period alternatives. The prior-year and current-rates-on-prior-base exceptions are unavailable to the specified large corporations; use MO-2220 and 143.761. Material later changes have revised first-payment dates; equal installments and whole-dollar rounding follow the actual worksheet. Include a credit in the estimate only after purchase/agency approval. [2026 MO-1120ES, instructions and worksheet](https://dor.mo.gov/forms/MO-1120ES_2026.pdf).

## Penalties and interest

The final annual booklet states 5% late filing per month of unpaid tax up to 25%,5% late payment regardless of filing extension, and calendar 2026 simple interest 7%. Use MO-2220 for estimate additions and obtain the rate applicable to each later calendar period. Failure to file/pay can also jeopardize the charter after the statutory 90-day period; do not assume administrative dissolution removes tax liability. [Annual booklet, pp.2,6-7](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf).

## Cross-border points

When income is not 100% Missouri, use MO-MS. The ordinary Method 2A receipts-factor workflow separates apportionable income from specifically supported nonapportionable income on MO-NAI. Goods generally source where received by the purchaser; services source by the ultimate beneficiary's location. For multi-location corporate beneficiaries, the booklet provides a location ratio, then states ratio, then 50% fallback where reasonable determination is not possible. Document why a fallback is needed. In-state/out-of-state real-property rents and intangible receipts have their own rules. Do not default to equal property/payroll/sales factors. [Annual MO-MS instructions, pp.10-12](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf).

Taxability in another state needs actual tax or jurisdiction to impose it; voluntary minimal registration fees alone do not establish apportionment eligibility. Public Law 86-272 can protect limited tangible-goods solicitation from net-income tax but does not create an all-tax exemption. Use the state's Business Activity Questionnaire/Form 4458 where appropriate. Partnership factors flow through at the corporation's ownership share. Transportation/mileage and broadcaster/approved alternative methods are special; alternative-method petitions generally need filing at least 60 days before year end. NOL allocation can alter the final percentage, so multiplying every item by a simple sales ratio is not sufficient for complex cases. [Annual booklet, pp.5,10-12](https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf).

Partnership MO-1065, S corporation MO-1120S, nonresident owner withholding/composite filings and elected MO-PTE are distinct from C corporation 4% tax. This skill identifies their routing but does not compute the elected PTE base, owner credit, election deadline or estimate relief without final 2026 support. Missouri has no ordinary post 2015 corporate franchise tax, but banks, insurance, local earnings/profits taxes and sector gross-receipts regimes are not thereby exempt. Retain these as explicit partial gaps.

## Two worked examples that recompute

**Invented Missouri-only corporation.** Federal taxable income 500,000 already includes a deduction for Missouri/other-state corporate income taxes 20,000. No other modifications, dividends, loss or credits. Eligible current-year federal income-tax-liability input from the federal computation is 100,000. Add 20,000 and subtract 50,000 federal-tax deduction: state base 470,000, tax 18,800. No additional ordinary franchise tax is added.

```oa-check
name: Missouri corporate federal liability deduction
inputs:
  federal_taxable: 500000
  income_tax_addback: 20000
  eligible_federal_tax: 100000
steps:
  - federal_deduction: eligible_federal_tax * 0.50
  - state_base: federal_taxable + income_tax_addback - federal_deduction
  - tax: state_base * 0.04
expected:
  federal_deduction: 50000
  state_base: 470000
  tax: 18800
```

**Estimate decision.** Same invented corporation has a prior 12-month Missouri return showing tax 20,000 and is not a large corporation. Current expected tax 18,800 gives 90% target 16,920 and four installments 4,230, versus prior-year protection 20,000/four=5,000 each. Choosing the current-year method reduces the planned protected amount by 3,080 but requires monitoring actual current tax; full annual balance remains 18,800 before credits/payments. This compares safe harbours, not elective final tax rates.

```oa-check
name: Missouri corporate estimate method decision
inputs:
  current_tax: 18800
  prior_tax: 20000
  installments: 4
steps:
  - current_target: current_tax * 0.90
  - current_installment: current_target / installments
  - prior_installment: prior_tax / installments
  - target_difference: prior_tax - current_target
expected:
  current_target: 16920
  current_installment: 4230
  prior_installment: 5000
  target_difference: 3080
```

## Ask the client first

1. Tax year/end, legal entity and federal classification, Missouri-source gross income, nexus activities and registration IDs?
2. Federal return, eligible liability/credit schedules, state tax deductions and Missouri addition/subtraction support?
3. Consolidated federal/Missouri elections, member consents, pro forma company returns and positive-income allocation?
4. Receipts and ultimate customer/beneficiary locations, taxable states, nonapportionable items, partnership factors and special industry?
5. Loss vintages/use, dividends, specie gain, approved credits/recapture, prior liability, large-corporation status and dated payments?
6. PTE election, nonresident owners, composite/withholding obligations, local profits tax or bank/insurance regime?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Final 2025 MO-1120 instructions. Read for 2025-2026 filing cycle: filing threshold, registration, base/modifications, groups, losses, dividends, MO-MS sourcing, returns and penalties. | https://dor.mo.gov/forms/MO-1120%20Instructions_2025.pdf | 2026-11-13 |
| 2026 MO-1120ES. Read for 4% rate,250 estimate threshold, dates, safe harbours, large-corporation restrictions and approved credits. | https://dor.mo.gov/forms/MO-1120ES_2026.pdf | 2026-11-13 |
| Corporate FAQ. Read for 4% current rate and separate-company/NOL requirements. | https://dor.mo.gov/faq/taxation/business/corporation-income.html | 2026-11-13 |
| 143.171. Read for the fifty percent corporate same-year federal liability deduction. | https://revisor.mo.gov/main/OneSection.aspx?section=143.171 | 2026-11-13 |
| 143.121. Read for individual versus corporate capital-gain trigger and 2026 specie distinction. | https://revisor.mo.gov/main/OneSection.aspx?section=143.121 | 2026-11-13 |
| 2026 MO-1040ES. Read for individual top rate 4.7%, relevant to corporate general capital-gain trigger. | https://dor.mo.gov/forms/MO-1040ES_2026.pdf | 2026-11-13 |
| Specie FAQ. Read for 2026 corporate subtraction and express short-year pre-publication procedure. | https://dor.mo.gov/faq/taxation/individual/specie_subtraction.html | 2026-11-13 |
| DOR franchise phase-out bulletin. Read for zero ordinary franchise tax and no report from 2016. | https://dor.mo.gov/pdf/TaxBulletin-10-26-15.pdf | 2026-11-13 |

Not yet confirmed: final 2026 MO-1120/MO-MS/MO-C/MO-NAI/MO-2220 forms, detailed elected MO-PTE/owner/composite and nonresident withholding calculations, complex group/NOL/dividend/foreign/conformity/sector-credit cases, alternative industries, banks/insurance and local profits taxes;2027 interest. This is a new core corporate owner, not complete PTE coverage.
