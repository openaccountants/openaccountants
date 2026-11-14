---
name: nd-corporate-tax
description: "Compute ordinary North Dakota 2026 corporate income tax under the 1.41%, 3.55% and 4.31% statutory bands, federal starting point and state adjustments. Apply default equal three-factor or valid single-sales election, state NOL, Form 40 estimates and filing; distinguish financial institutions, pass-throughs and severance taxes."
version: "0.4"
jurisdiction: US-ND
category: state-tax
tax_year: 2026
last_updated: 2026-11-14
tier: 2
domain: corporate-tax
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# North Dakota corporate income tax, 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** Ordinary North Dakota corporate tax is 1.41% through USD 25,000, 3.55% on the next USD 25,000 and 4.31% above USD 50,000. Reconcile federal income, state modifications, apportionment/allocation and state losses before applying these bands. The old financial-institution privilege-tax chapter was repealed; it is not a current alternative Form 35 regime. [57-38-30](https://ndlegis.gov/cencode/t57c38.pdf); [repealed chapter](https://ndlegis.gov/cencode/t57c35-3.pdf); [current agency overview](https://www.tax.nd.gov/corporate-income-tax).

## Scope

Ordinary C corporations and LLCs federally taxed as C corporations engaged in business or deriving income from North Dakota. Cooperatives, financial institutions, tax-exempt UBTI and some insurance-company activity may have Form 40 duties but need their specific treatment. Federal corporate computations belong to `us-form-1120-c-corp`; federal income-tax nexus protection belongs to `us-pl-86-272-income-tax-nexus`. Individual owners use `nd-income-tax`, sales use `nd-sales-tax`, and withholding/UI use their separate state owners. Cross-border and transfer pricing remain separate jobs.

## Ask the client first

1. Federal/entity status, tax year, state activities, registration, group chart and all domestic/foreign affiliates.
2. Completed federal return and consolidated/pro-forma schedules, state modifications and source documentation.
3. Business/nonbusiness income, property/payroll/sales by jurisdiction, shipment destinations and taxable status elsewhere.
4. Existing apportionment/water's-edge elections, state NOL by originating FEIN/year, credits and specialist-industry status.
5. Prior/current tax, estimated payments, withholding, extensions, filing channel and account notices.

## The method, step by step

### Rates, bands and thresholds

Current statutory rates apply to the ordinary **2026** computation. Operational line mapping below is explicitly the **2025-2026 filing cycle** until final 2026 Form 40 instructions are read.

| Item / condition | Rate or rule | Official source |
| --- | --- | --- |
| ND taxable income through USD 25,000 | 1.41% | [57-38-30](https://ndlegis.gov/cencode/t57c38.pdf); [Tax Commissioner rate table](https://www.tax.nd.gov/corporate-income-tax) |
| Over 25,000 through 50,000 | 352.50 + 3.55% of excess over 25,000 | [57-38-30](https://ndlegis.gov/cencode/t57c38.pdf); [Tax Commissioner rate table](https://www.tax.nd.gov/corporate-income-tax) |
| Over 50,000 | 1,240 + 4.31% of excess over 50,000 | [57-38-30](https://ndlegis.gov/cencode/t57c38.pdf); [Tax Commissioner rate table](https://www.tax.nd.gov/corporate-income-tax) |
| Water's-edge election | Additional 3.5% of ND taxable income; five consecutive years | [57-38.4](https://ndlegis.gov/cencode/t57c38-4.pdf); [Form 40 p3-4](https://www.tax.nd.gov/sites/default/files/documents/forms/business/corporate-income/2025-corp/28714-corp-income-tax-booklet-2025.pdf) |
| Default apportionment | Equally weighted property, payroll and sales; not double-weighted sales | [57-38.1-09(1)](https://ndlegis.gov/cencode/t57c38-1.pdf) |
| Optional single-sales factor | Original timely return; binding five years; renewal or default-period conditions | [57-38.1-09(4)](https://ndlegis.gov/cencode/t57c38-1.pdf) |
| Estimate duty | Both prior tax and expected current tax **exceed** USD 5,000 | [57-38-62](https://ndlegis.gov/cencode/t57c38.pdf); [2026 Form 40-ES](https://www.tax.nd.gov/sites/www/files/documents/forms/business/corporate-income/2025-corp/28716-form-40-es-2026.pdf) |
| Ordinary estimate safe harbor | Lesser of 90% current / 100% prior tax, subject to prior-return/period conditions | [57-38-62](https://ndlegis.gov/cencode/t57c38.pdf); [2026 Form 40-ES](https://www.tax.nd.gov/sites/www/files/documents/forms/business/corporate-income/2025-corp/28716-form-40-es-2026.pdf) |
| Zero ordinary taxable income, no additional liability | Zero under the graduated income-tax schedule; filing duty can remain | [57-38-30](https://ndlegis.gov/cencode/t57c38.pdf); [who files](https://www.tax.nd.gov/corporate-income-tax) |

1. Establish filing/nexus and entity status. A federal S election ordinarily leads to Form 60, with nonresident withholding/composite and built-in-gain/excess-passive exceptions to examine. Certain former financial institutions have a specific 57-38-01.35 election. Do not state that every S corporation always owes zero entity tax. No general corporate franchise computation is imposed by these ordinary income-tax provisions; annual registration fees, industry taxes and other state/local duties remain separate.
2. Establish unitary status before the federal starting point. The agency requires worldwide combined reporting for a unitary business unless a valid water's-edge election applies. Evaluate same-line, vertically integrated and centralized-management facts. Federal consolidation and state combination are different: use required pro-forma/by-company figures and schedules. Water's-edge is not simply an election to include every US company and exclude every foreign company; the statute defines the included group. Complex Joyce/Finnigan, foreign affiliates, captive REIT/RIC and special addbacks require specialist review.
3. Start with federal taxable income, then apply **57-38-01.3**, not the old NOL reference to 01.4. Reconcile state/local/foreign income-tax deductions, non-North-Dakota state-bond interest, protected US-obligation income, federal NOL/special deductions and other applicable additions/subtractions. Use Schedule SA in the read form mapping for adjustments. Do not automatically create a bonus-depreciation subtraction: identify the actual year's conformity and adjustment provision. The agency describes rolling federal taxable-income conformity, including income/deduction changes; federal tax credits do not automatically become state credits.
4. Separate business apportionment from nonbusiness allocation and attribute expenses consistently. Default business income uses equal property/payroll/sales factors; omit a factor when its denominator is zero as the instructions direct. Property uses average owned property at original cost and rented property at eight times net annual rent; payroll follows the statutory location tests and sales follow the applicable receipts rule. Under the **2025-2026 mapping**, Schedule FACT (or CR for the applicable group) supports the factor, not Schedule SA. Carry the specified six-digit factor.
5. For tangible goods, analyze destination plus throwback when shipped from North Dakota and not taxable in the destination state; the separate US-government rule also applies. Services/other receipts under 57-38.1-17 generally follow income-producing activity/cost of performance when activity spans states. Do not infer market sourcing merely from a remote customer or classify every SaaS/license as a service: identify the transaction and special rules. Financial institutions, transportation, railroads, pipelines and other industries require their applicable administrative rules or alternative-apportionment authority under 57-38.1-18.
6. Verify a timely single-sales-factor election for a non-pass-through taxpayer, group applicability and the full five-year lock. At expiry, renew immediately or use the default for three taxable years before a new election. The statute's historical double/six-weighted transitional methods are not the ordinary new 2026 election. Compare actual facts over the binding period; five times one year's illustrative saving is not a forecast.
7. Compute state NOL after apportionment/allocation and eligible income exemptions. Section 57-38-01.3(3) makes a separate state loss available for the same carryforward period as an identical federal loss; origin year matters. The read Form 40 instructions prohibit carryback for state losses arising after 2002, require accumulated state loss less previously used loss, and distinguish capital losses. The old blanket twenty-year rule and universal federal-style 80% limit are not established here. The old claim that rates and NOL value will remain stable, and that no other planning consideration exists, is not a legal guarantee. Track originating FEIN: the agency warns that an NOL cannot transfer to a surviving/different corporation on merger/dissolution. Ownership-change limits and carryovers require actual schedules, not a federal NOL copied to line 12.
8. Apply ordinary tax and, if elected, water's-edge surtax to the proper base; then supported state credits and payments. New/expanding-business exemption and Renaissance Zone require approval, related-income limits and supporting schedules/property-tax clearance. Do not award an Opportunity Zone or other credit by analogy. Oil/gas production/extraction taxes are separate; income-tax withholding on royalties is also distinct from severance payments. Do not automatically credit severance tax against Form 40.

### Ordinary rate arithmetic retained from the old skill

At final ND taxable income 10,000 / 25,000 / 50,000 / 100,000 / 500,000 / 1,000,000 / 5,000,000, ordinary tax is respectively **141 / 352.50 / 1,240 / 3,395 / 20,635 / 42,185 / 214,585**. The old 5,000,000 summary amount 214,685 was an arithmetic error. Effective rates are derived tax/income, not separate statutory rates. [57-38-30](https://ndlegis.gov/cencode/t57c38.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Private bank/financial institution | Chapter 57-35.3 was repealed in 2013; current Form 40/special apportionment or specific S-election transition applies, not a current net-worth Form 35 tax |
| Insurance company | Distinguish gross-premium-tax business from other business activities that may require Form 40 |
| Bank of North Dakota | Specialized state-instrumentality analysis; the old blanket no-return conclusion is not confirmed here |
| Tax-exempt organization/cooperative | UBTI/patronage and special due dates/return type require the read form's conditions |
| Pass-through owner | Form 58/60 and nonresident obligations; assess individual ND-1 separately rather than taxing gross K-1 at the top rate |
| Oil/gas, coal, tobacco/liquor or local property tax | Separate regimes; coal conversion is not the same job as coal extraction |
| Foreign group, transfer pricing, captive REIT/RIC, Indian Country | Preserve specialist referral; no ordinary worksheet resolves immunity or income shifting |

The old definitive absence-of-PTET claim and related comparative planning conclusions are **not yet confirmed for 2026** from a comprehensive current state source. The old SALT-cap/corporate-rate numbers and hypothetical federal savings belong to federal skills, not this state computation. Refer entity conversion/double-taxation and owner deduction planning to the relevant federal owners before recommending an election.

## Worked cases

**Prairie Print Shop, Inc., preserved Case A.** Bismarck corporation with final ND taxable income USD 20,000, no adjustments/credits or other liability: ordinary tax 282. No separate income-tax minimum is invented. If prior tax is 282, the prior-year limb of the ordinary estimate test is not met even if future circumstances change. Filing can still be required.

```oa-check
name: ND Prairie Print Shop ordinary low-band corporate tax
inputs:
  nd_taxable_income: 20000
steps:
  - tax: round(nd_taxable_income * 0.0141, 2)
expected:
  tax: 282
```

**Red River Equipment, Inc., preserved Case B with corrected conditions.** Federal taxable income 2,000,000 plus a supported 50,000 state addition less a **hypothetically verified** 10,000 state subtraction gives 2,040,000. The 10,000 is an invented supported adjustment, not an automatic federal-bonus-depreciation subtraction. Property 5m/10m = 0.5, payroll 3m/5m = 0.6, sales 8m/20m = 0.4. Default average 0.5 produces 1,020,000 and **43,047** tax. Valid single-sales election 0.4 gives 816,000 and **34,254.60**, a one-year illustrative difference **8,792.40**. Holding everything constant for five years gives 43,962, not a prediction.

```oa-check
name: ND Red River equal factors versus valid single-sales election
inputs:
  federal_income: 2000000
  supported_addition: 50000
  supported_subtraction: 10000
  property_factor: 0.5
  payroll_factor: 0.6
  sales_factor: 0.4
steps:
  - adjusted_income: federal_income + supported_addition - supported_subtraction
  - default_factor: (property_factor + payroll_factor + sales_factor) / 3
  - default_income: adjusted_income * default_factor
  - default_tax: 1240 + (default_income - 50000) * 0.0431
  - elected_income: adjusted_income * sales_factor
  - elected_tax: 1240 + (elected_income - 50000) * 0.0431
  - saving: default_tax - elected_tax
  - constant_five_year_difference: saving * 5
  - prior_year_quarter_if_43047: default_tax / 4
expected:
  adjusted_income: 2040000
  default_factor: 0.5
  default_income: 1020000
  default_tax: 43047
  elected_income: 816000
  elected_tax: 34254.60
  saving: 8792.40
  constant_five_year_difference: 43962
  prior_year_quarter_if_43047: 10761.75
```

The original estimate illustration inconsistently substituted prior tax **40,849**, yielding **10,212.25** each quarter, after computing 43,047. If 40,849 is separately evidenced prior liability, that installment can be correct; if prior liability is 43,047, the equal prior-year installment is 10,761.75. Do not silently interchange the two. Ordinary fourth installment is **January 15 of the following year**, not December 15.

**Bakken Software Solutions, Inc., preserved Case C.** Ordinary S corporation with 400,000 pass-through income and none of the special entity-tax cases has no ordinary Form 40 tax, but Form 60/nonresident owner duties remain. Owner tax is computed from federal taxable income/status/modifications in `nd-income-tax`; the old 10,000 estimate obtained by taxing all 400,000 at the top rate is not a complete individual computation. Its hypothetical PTET/federal SALT saving and conversion comparison are not established state rules and must not be used as a 2026 recommendation.

**Bakken Crude Operators, Inc., preserved Case D.** Given final ND taxable income 5,000,000 after separately substantiated 3,000,000 severance expense and no additional state adjustment, ordinary Form 40 tax is **214,585**. Do not claim a severance credit merely from that expense. Adding only the assumed separate severance payment gives 3,214,585, not the old unsupported “5m+” overall-tax conclusion; other taxes need their own computations. The old oil/gas percentage summary is unconfirmed here, and no severance rate is supplied by this income-tax skill.

## When to refuse or refer

Refer specialized banks/insurance, state instrumentalities, transportation, foreign unitary groups, Joyce/Finnigan, transfer pricing, captive structures, NOL ownership changes, tribal immunity, federal controversies, local property and specialist credits. `nd-cross-border-tax` and `nd-transfer-pricing` remain distinct jobs; their existence does not establish current ordinary corporate amounts. Refuse requests to estimate federal savings from an unconfirmed state PTET assumption.

## Filing and payment

Ordinary calendar-year 2026 Form 40 and payment are generally due April 15, 2027, subject to business-day relief. Fiscal ordinary returns use the fifteenth day of the fourth following month; cooperatives, exempt UBTI and foreign corporations without a permanent US office have special deadlines. Under the **2025-2026 filing-cycle instructions**, a federal extension grants the state one additional calendar month beyond the federal extended date; attach the federal extension and mark the return. Without a federal extension, request Form 101 before the applicable deadline. **Form 40-EXT is an extension payment voucher**, not the application. Extension does not extend payment; the instructions charge 12% annual extension interest while allowing stated penalty relief for tax paid within a valid extension. Recheck final 2026 mapping.

File an original Form 40 through approved MeF software or the permitted paper process with complete federal return and schedules. The read instructions say **ND TAP provides corporate payments, not Form 40 return filing**. Use 40-PV for an ordinary paper payment, 40-ES for estimates, 40-EXT for extension payment, 40-UT for underpayment and 40X for amendment. Schedule SA reconciles adjustments; FACT/CR supports apportionment; WW/WE supports combined reporting; TC/credit schedules support credits. Form 58/60 and their K-1s are separate pass-through returns. Retain acceptance, attachments and independent payment confirmation.

For 2026 ordinary estimates, both current expected and prior net tax must exceed 5,000. The annual required amount is generally the lesser of 90% current or 100% prior tax with prior-full-year/return conditions. Equal ordinary installments fall April 15, June 15, September 15, 2026 and January 15, 2027; fiscal/short-period cases require the statute/form instructions. Sections 62-63 and the current agency deadline page govern the dates where a voucher's year wording is ambiguous.

Ordinary delinquency under 57-38-45 generally includes 5% or USD 5 minimum unpaid-tax penalty, late-filing increments of 5% per month/part up to 25% and 1% monthly/part interest excluding the due month; valid extensions have the stated interest/penalty conditions. Estimated-tax interest is assessed under the relevant state rules/Form 40-UT. The old blanket negligence 25%, fraud 75% and semiannually reset interest assertions are not confirmed; do not import federal percentages. Evaluate fraudulent filing and criminal exposure under actual state law.

## Completion checklist

- Entity, nexus, group method and special-industry status resolved.
- Federal starting point and each state adjustment documented.
- Allocation, factors and any elections supported by actual schedules and dates.
- State NOL origin/remaining use, exemptions and credits reconciled.
- Required estimates/extension, return acceptance and payment credited correctly.

## Disclaimer

Informational and computational material only. A qualified professional must review all facts, legal conclusions and filing outputs before use. This skill does not constitute tax, legal or financial advice.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Chapter 57-38. Read for corporate adjustments/NOL in 01.3, special financial transition, rates, filing, penalties and estimates. | https://ndlegis.gov/cencode/t57c38.pdf | 2026-11-13 |
| Chapter 57-38.1. Read for allocation, equal factors, single-sales election/renewal, TPP destination/throwback, other receipts and alternative apportionment. | https://ndlegis.gov/cencode/t57c38-1.pdf | 2026-11-13 |
| Chapter 57-38.4. Read for water's-edge included group, five-year election and 3.5% surtax. | https://ndlegis.gov/cencode/t57c38-4.pdf | 2026-11-13 |
| Chapter 57-35.3. Read for explicit 2013 repeal of financial-institution privilege tax. | https://ndlegis.gov/cencode/t57c35-3.pdf | 2026-11-13 |
| Current corporate overview. Read for filing population, current ordinary rates and combined reporting. | https://www.tax.nd.gov/corporate-income-tax | 2026-11-13 |
| 2025 Form 40 instructions, 2025-2026 filing cycle. Read for federal base, adjustments, financial institutions, unitary groups, NOL origin, actual schedule mapping, extension and MeF/payment distinction. | https://www.tax.nd.gov/sites/default/files/documents/forms/business/corporate-income/2025-corp/28714-corp-income-tax-booklet-2025.pdf | 2026-11-13 |
| 2026 Form 40-ES, published in the agency's 2025-corp folder. Read for both USD 5,000 tests and 90%/100% safe harbor. | https://www.tax.nd.gov/sites/www/files/documents/forms/business/corporate-income/2025-corp/28716-form-40-es-2026.pdf | 2026-11-13 |
| Current corporate deadline page. Read for January fourth installment and ordinary/extended filing dates. | https://www.tax.nd.gov/corporate-income-tax-deadlines | 2026-11-13 |
| 2025 Form 60 instructions, 2025-2026 filing cycle. Read for ordinary S corporation return and special entity/nonresident-owner obligations. | https://www.tax.nd.gov/sites/www/files/documents/forms/business/s-corp-partner/2025-s-partner/28717-s-corporation-income-tax-booklet-2025.pdf | 2026-11-13 |

Not yet confirmed: final 2026 Form 40/60 line mapping and operational changes; comprehensive 2026 PTET absence; specialist bank/insurance/state-instrumentality treatment; special-industry and SaaS/intangible sourcing; NOL ownership-change and origin-year limitations beyond the cited ordinary rule; legacy negligence/fraud percentages and severance-rate assertions. The labelled 2025-2026 filing-cycle instructions do not establish unpublished final 2026 form details.
