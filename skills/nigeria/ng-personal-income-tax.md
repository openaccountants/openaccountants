---
name: ng-personal-income-tax
description: 'Compute Nigerian resident individual income tax for 2026: current progressive bands, eligible deductions and rent relief, employment benefits, sole-trader expenses, capital allowances, losses, credits and filing. Separates historical 2025 PITA computations and corrects the CRA base. Use for PAYE, direct assessment, professional and online earnings, with cross-border and transition holds stated explicitly.'
jurisdiction: NG
tax_year: 2026
last_updated: '2026-11-16'
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: '1.1'
type: computation
category: international
---

# Nigeria personal income tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This is the personal-tax computation home for individuals, employees, sole traders and partners, using the Nigeria Tax Act (NTA) in force from 1 January2026. [ng-income-tax](ng-income-tax.md) remains a companion for bank-narration classification; it is not a competing current rate table. [ng-payroll](ng-payroll.md) runs employee payroll, [ng-cgt](ng-cgt.md) computes gains and [ng-return-assembly](ng-return-assembly.md) produces the return package.

An individual is not a small company and has no company-turnover exemption. Resident individuals' worldwide income, profits and gains are chargeable whether remitted or not, subject to actual statutory relief. Residence is not just a day count: domicile, available permanent home, habitual abode, substantial economic/immediate family ties, the183-day rule and Nigerian diplomats are alternatives in the definition. Non-residents need source/PE/SEP and treaty analysis. State allocation is a separate NTAA question. [NTA sections 12,13,17,28 and201](https://nass.gov.ng/documents/download/11249); [NTAA section 3 and First Schedule](https://nass.gov.ng/documents/download/11250).

| Chargeable annual income slice | Rate from 2026 | Primary source |
| --- | --- | --- |
| First NGN 800,000 | 0% | [NTA section 58 and Fourth Schedule](https://nass.gov.ng/documents/download/11249) |
| Next NGN 2,200,000 | 15% | same |
| Next NGN 9,000,000 | 18% | same |
| Next NGN 13,000,000 | 21% | same |
| Next NGN 25,000,000 | 23% | same |
| Balance above NGN 50,000,000 | 25% | same |
| Rent deduction, genuine tenant's own annual rent | 20% of actual rent, capped at NGN 500,000; claim and evidence required | [NTA sections 30 to32](https://nass.gov.ng/documents/download/11249) |

These are marginal slices of chargeable income, not rates on turnover or the whole salary. The NTA method has no CRA deduction and no old PITA minimum-tax floor. Minimum-wage employment income has a separate statutory exemption; it does not exempt every person with small business turnover. [NTA sections 28 to30,58 and162](https://nass.gov.ng/documents/download/11249).

## Ask the client first

1. Income period AND year of assessment, prior returns, residence/home/day facts, state allocation, all employments, partnership/business status and Tax ID.
2. Gross receipts before withholding, business costs with evidence, capital assets and use, losses, all employment cash and benefits, bonuses, pensions, rent, investment and digital receipts, gains and foreign income.
3. Actual NHF, approved health-insurance and pension remittances, mortgage interest, life/annuity premiums and year, tenant rent/landlord details and receipts; no assumed deduction.
4. PAYE/WHT receipts, payer schedules, instalment payments, foreign-tax evidence and treaty residence, refunds/set-offs already claimed; do not count one credit twice.
5. Commencement/cessation, special compensation, gifts/inheritance, mixed-use assets, residence changes, historic allowances and any disputed tax-authority notice.

## The method, step by step

### Fix the period and authority first

Do not confuse the current law date, income year, basis period and assessment year. Employment uses actual-year earnings under section 26, including bonus on payment and the specified post-cessation rule. Trade basis and cessation have their own rules; gains and other income can use a preceding-year basis. [NTA sections 22 to28](https://nass.gov.ng/documents/download/11249). The Government's June2026 transition announcement says earlier liabilities/accounting periods before commencement remain under earlier law while new administration applies to returns due from 2026. The operative full transition document was not retrieved; an ambiguous 2026 assessment of2025 income or straddling period requires a documented resolution, not automatic use of new rates. [Federal Government announcement](https://fmino.gov.ng/federal-government-issues-transition-guidelines-for-tax-acts-2025/).

Under NTAA section 3 the relevant State or FCT authority generally administers resident individuals; NRS administers the listed special classes including armed-forces/police personnel other than civilians, foreign-service officers and non-residents. FCT residents are not automatically NRS taxpayers. For Nigerian employment the First Schedule refers to principal residence on1 January of the year of assessment, or entry into the employment where relevant; it is not a universal snapshot in the preceding income year. Obtain the actual residence timeline and apply the appropriate Schedule paragraph, including other employments, pensions, business and no-principal-residence cases. [NTAA section 3 and First Schedule](https://nass.gov.ng/documents/download/11250).

### Build income and deduct business costs in order

Reconstruct gross income, including WHT withheld by customers and PAYE withheld by an employer. Withholding is a credit where creditable, not a reduction of receipts. Separate final-taxed and exempt items before aggregation. For a business, deduct properly evidenced expenses wholly and exclusively incurred to produce the income; distinguish repairs from improvements, owner drawings from staff costs, and private from business use. Add back depreciation, capital/private expenditure, income taxes, unsupported provisions, penalties and other statutory disallowances. Convert foreign-currency expenditure using the Act's official-rate rule, not a convenient unverified rate. [NTA sections 20,21 and28](https://nass.gov.ng/documents/download/11249).

Prepare capital allowances from asset class, qualifying expenditure, ownership/use, previous claims, disposal and the remaining period. The current First Schedule is different from the old PITA initial/annual tables; use [ng-cit's current allowance method](ng-cit.md) with the individual rules in section 28. Do not expense a laptop outright and also claim allowances. Mixed-use car, home office and generator claims need support for the actual business proportion, not an arbitrary half. Losses carry to subsequent qualifying income until recouped under section 28; digital/virtual-asset losses stay in that business. Maintain commencement/cessation and loss schedules rather than inventing estimates. If records are insufficient, section 29 permits a prescribed presumptive method; it does not authorise the agent to create a turnover tax. [NTA sections 20 to29 and First Schedule](https://nass.gov.ng/documents/download/11249).

### Employment benefits and eligible deductions

For an employer-owned benefit asset, annual benefit is5% of acquisition cost; use market value at acquisition only where cost cannot be ascertained. Do not choose the higher value. Hired assets use annual rent/hire and other benefits actual cost, subject to employee contributions and statutory exclusions. Staff-general canteen meals/meal vouchers, protective/uniform/work equipment and qualifying relocation are excluded. Employer-provided accommodation uses annual rental value capped at20% of gross employment income excluding that rental value; apply the statutory valuation and occupied fraction. [NTA section 14](https://nass.gov.ng/documents/download/11249). A cash meal or housing allowance is not automatically exempt merely because a non-cash benefit can be excluded.

Claim actual eligible NHF, NHIS and approved PRA pension contributions; interest on an owner-occupied residential development/acquisition loan, not principal or a business-property loan; and qualifying life/annuity premiums for self/spouse paid in the preceding assessment year. An adult child's premium or arbitrary private health policy is not automatically eligible. Test the precise scheme and evidence with the owning [pension-and-statutory-contributions](ng-pension-nhf-social-contributions.md) skill. Spouses are separate taxpayers; the permitted spouse premium is not a joint return. [NTA sections 30 to32](https://nass.gov.ng/documents/download/11249); [JRB Guidelines paragraph 8](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf).

For rent, record the taxpayer's own portion, property, period, landlord name and Tax ID/NIN/contact details. For the2026 assessment year the JRB specifies actual rent in2026, including a time apportionment for multi-year rent. Calculate the table's relief on that amount; a homeowner has no fictional rent deduction. Deductions must be claimed in writing and substantiated; use the earlier of neither an estimate nor an unsupported ceiling. [NTA sections 30 to32](https://nass.gov.ng/documents/download/11249); [JRB Guidelines paragraph 9](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf).

Compute non-negative chargeable income, apply slices once across all taxable sources, then subtract evidenced credits. Retain precision through the working paper and apply the actual filing system's rounding at the final field; rounding does not authorise hiding a balance. If credits exceed liability, show an overpayment for validation/set-off/refund, not a promised cash repayment. [NTA sections 28,30 and58](https://nass.gov.ng/documents/download/11249); [NTAA sections 49,51 and55](https://nass.gov.ng/documents/download/11250).

### Foreign income, exemptions and credits

Classify foreign professional/content-creator receipts as business income where appropriate; there is no general online-income turnover exemption. Current resident worldwide treatment differs from the old remittance-based instruction. Section162's specified foreign dividends, interest, rent and royalties brought through approved channels are not a blanket exemption for foreign fees or commissions. PRA-qualified pensions/gratuities, death/injury and loss-of-job compensation have their own conditions; use ng-cgt for compensation rather than exempt all lump sums. [NTA sections 12,28,50 and162](https://nass.gov.ng/documents/download/11249); [JRB Guidelines paragraphs 15 to21](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf).

For a qualifying foreign-tax credit, both unilateral and treaty methods cap credit at the lower of actual qualifying foreign tax and Nigerian tax attributable to that foreign income. Attributable tax uses the statutory foreign-income/total-income proportion. A foreign tax is not also a business deduction where prohibited. Treaty relief needs a qualifying treaty, residence/beneficial ownership and the relevant article; a treaty claim under section 121 has its own2-year claim and adjustment rules. Route an actual foreign-income file to [ng-non-resident-cross-border](ng-non-resident-cross-border.md), and confirm that file's limits before adopting a result. [NTA sections 119 to121](https://nass.gov.ng/documents/download/11249).

### Preserve historical2025 computations without misusing them

For an actual2025 PITA case, the former six marginal bands were first300k at7%, next300k11%, next500k15%, next500k19%, next1.6m21%, balance above 3.2m24%. CRA was the greater of NGN 200,000 and1% of the legally defined gross income, plus20% of that income. Finance Act 2020 defined the base AFTER non-taxable/final-taxed items, listed exempt contributions, allowable business expenses and capital allowances. It was not20% of raw business receipts. The old child/dependent/meal/utility reliefs were removed in2011, not by Finance Act 2020. Finance Act 2021 changed the life-premium provision; do not assume the current annuity deduction applied in2025. [PITA2011 amendment section 5/Sixth Schedule](https://nass.gov.ng/documents/download/5958); [Finance Act 2020 sections 29/30](https://www.iirs.im.gov.ng/document/docs/FINANCE_ACT_2020.pdf); [Finance Act 2021 section 23](https://lirs.gov.ng/assets/docs/Finance-Act-2021-Gazetted.pdf).

The historical minimum-tax exception for minimum-wage-or-lower EMPLOYMENT did not cover every self-employed person. The old capital-allowance table and specific minimum-tax base still require the complete historical law; do not substitute an old rule copied from a sibling or label a conditional example a verified liability.

## Boundary and exception table

| Situation | Action |
| --- | --- |
| Mixed employment, business, rent and gains | Compute the components separately then aggregate taxable amounts once; credit PAYE/WHT once. |
| Fees with actual10% WHT deducted | Preserve the actual supported receipt; current nominal professional-fee rate is determined in ng-wht. An over-deduction is not corrected by inventing a smaller receipt. |
| Director's non-employment fees, stock options or termination | Classify the payment first; ng-wht handles director withholding, ng-payroll handles employment and ng-cgt handles compensation. Obtain option exercise/disposal valuation. |
| Voluntary pension, high contribution or private medical policy | Obtain scheme approval/remittance and deduction conditions; no automatic rejection merely because pension exceeds8% or an invented20% ceiling. |
| Gift, inheritance, cryptocurrency or loss | Apply ng-cgt and period-specific law; Finance Act 2023 included digital assets under the old gains regime, so they were not simply outside tax. |
| Non-resident, foreign employer, treaty, state change, foreign tax or cross-border split payroll | Refer with all dates and income evidence. Do not assume a183-day count or remittance alone decides liability. |
| Home office/car/generator, unverified carryforward or asset disposal | Evidence the business use, prior allowances and loss origin; hold the disputed component. |

## Worked cases

**Current2026 independent professional.** Gross fees NGN 12m, allowable costs3.5m, confirmed qualifying capital allowances160k as an input (not an unverified laptop classification), eligible actual pension480k/life120k/NHIS60k. Before rent, chargeable income is7.68m and tax1,172,400. As a genuine tenant paying2.5m annual rent, eligible rent relief500k reduces chargeable income to7.18m and tax1,082,400:90k tax saved. If actual evidenced WHT credits are1.2m, the respective overpayments are27,600 and117,600 for reconciliation, not automatic cash refunds. The input1.2m is an actual receipt assumption, not an instruction to withhold10% on current fees.

```oa-check
name: Nigeria current professional tenant versus no rent
inputs:
  fees: 12000000
  costs: 3500000
  confirmed_allowances: 160000
  pension: 480000
  life: 120000
  nhis: 60000
  rent: 2500000
  evidenced_credit: 1200000
steps:
  - before_rent: fees - costs - confirmed_allowances - pension - life - nhis
  - rent_relief: min(rent * 0.20, 500000)
  - tenant_income: max(0, before_rent - rent_relief)
  - tax_without_rent: 2200000 * 0.15 + (before_rent - 3000000) * 0.18
  - tax_with_rent: 2200000 * 0.15 + (tenant_income - 3000000) * 0.18
  - saved: tax_without_rent - tax_with_rent
  - overpayment_without_rent: evidenced_credit - tax_without_rent
  - overpayment_with_rent: evidenced_credit - tax_with_rent
expected:
  before_rent: 7680000
  rent_relief: 500000
  tenant_income: 7180000
  tax_without_rent: 1172400
  tax_with_rent: 1082400
  saved: 90000
  overpayment_without_rent: 27600
  overpayment_with_rent: 117600
```

**Original Adaeze Okonkwo case,2025 Lagos sole IT consultant.** Preserve fees12m, actual WHT receipts1.2m, operating costs3.5m, laptop cost800k, pension480k, life120k, NHIS60k, single. The old file assumed laptop allowance500k and computed CRA2.6m from raw receipts, producing tax929,600/refund270,400. Correct the CRA base while keeping the500k allowance explicitly CONDITIONAL pending confirmation of the old asset class and allowance rules: defined gross income7.34m, CRA1.668m, chargeable5.672m, tax1,153,280, conditional overpayment46,720. If the allowance is different, recompute the CRA and tax; do not file this conditional result. The allowance is not approved by keeping its old arithmetic.

```oa-check
name: Adaeze Okonkwo historical CRA correction conditional allowance
inputs:
  receipts: 12000000
  operating_costs: 3500000
  unconfirmed_allowance_input: 500000
  eligible_contributions: 660000
  evidenced_credit: 1200000
steps:
  - defined_gross: receipts - operating_costs - unconfirmed_allowance_input - eligible_contributions
  - cra: max(200000, defined_gross * 0.01) + defined_gross * 0.20
  - chargeable: defined_gross - cra
  - tax: 300000 * 0.07 + 300000 * 0.11 + 500000 * 0.15 + 500000 * 0.19 + 1600000 * 0.21 + (chargeable - 3200000) * 0.24
  - conditional_overpayment: evidenced_credit - tax
expected:
  defined_gross: 7340000
  cra: 1668000
  chargeable: 5672000
  tax: 1153280
  conditional_overpayment: 46720
```

## When to refuse or refer

Stop a final computation for unresolved period/residence, missing income or cost evidence, unsupported losses/allowances/deductions, unidentified credits or a disputed treaty/valuation. Show a partial working paper with held items, not a guessed filing number. Refer specialist non-resident, trust, partnership, litigation, stock-option and split-pay cases. Do not submit a return, sign a declaration or guarantee a refund from this skill. Do not replace the client's facts with conservative-looking assumptions: an unsupported expense disallowance, fictitious deduction or false authority mapping can all be wrong.

## Filing and payment

Register for Tax ID and verify the relevant authority. JRB paragraph 11 requires annual filing by 31 March of the assessment year for the preceding income basis, including employees and nil-tax individuals. NTAA section 13 requires a self-assessment, all-source income, relief/computation, business audited statements OR taxpayer-attested accounts, and payment evidence. Employer filing does not replace the employee's own return. Use the authority's actual prescribed form: the JRB Appendix2 has PartsA identity, B general information, C employment/business details, D annual income, E deductions, F chargeable income, G bands, H credits, I net, J declaration and K official use. PartF repeats deduction references that are not clearly separated in PartE: reconcile the actual form and deduct each eligible amount once. Treat a legacy "FormA" label as a routing aid, not proof that every portal uses the same fields. [NTAA sections 4,13,14,33 and85](https://nass.gov.ng/documents/download/11250); [JRB paragraph 11/Appendices](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf).

Map each working-paper line to those fields, attach schedules and receipts, preview the tax/period, arrange authorised payment and keep its reference, then have the authorised filer submit and save acknowledgement. Payment is separate from filing. NTAA section 49 makes self-assessed tax payable by filing; an approved instalment arrangement is not an automatic quarterly schedule. Refund claims require audit and the section 55 process, which requires payment within 90 days of the authority's decision after audit, with a set-off option, not within 90 days of filing. Keep records6 years after the assessment year under section 31. Current late-filing, payment, registration and deduction sanctions are administered under NTAA; load ng-return-assembly/ng-wht for the relevant obligation rather than apply old PITA penalty tables. [NTAA sections 31,49,55,65,100 to107](https://nass.gov.ng/documents/download/11250).

## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| National Assembly NTA: sections 12 to15,20 to32,50,58,119 to121,162,201; First/Fourth Schedules | https://nass.gov.ng/documents/download/11249 | 2026-11-16 |
| NTAA: sections 3 to8,13 to15,31,33,49,51,55,65,85,100 to107 and First Schedule residence paragraphs | https://nass.gov.ng/documents/download/11250 | 2026-11-16 |
| JRB2026 PIT Guidelines: operative paragraphs 1 to26 and Appendices1/2 computation/return structure | https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf | 2026-11-16 |
| PITA2011 amendment: section 5 consolidated-relief allowance and Sixth Schedule; Assembly scan/OCR, bands cross-checked in LIRS Gazette | https://nass.gov.ng/documents/download/5958 | 2026-11-16 |
| LIRS historical PITA2011 Gazette: Sixth Schedule bands and consolidated-relief allowance | https://lirs.gov.ng/assets/docs/PITA-Ammendment.pdf | 2026-11-16 |
| Finance Act 2020: sections 29/30 gross-income definition and employment minimum-tax exception | https://www.iirs.im.gov.ng/document/docs/FINANCE_ACT_2020.pdf | 2026-11-16 |
| Finance Act 2021: section 23 life-premium amendment | https://lirs.gov.ng/assets/docs/Finance-Act-2021-Gazetted.pdf | 2026-11-16 |
| Government transition announcement, not the full operative Guidelines | https://fmino.gov.ng/federal-government-issues-transition-guidelines-for-tax-acts-2025/ | 2026-11-16 |

Not yet confirmed: complete historical PITA capital-allowance table/method, its2/3 cap, pool/disposal and carryforward treatment, the laptop's claimed500k allowance and historical minimum-tax base; full transition Guidelines and an ambiguous2026 assessment on2025 income; historical remitted foreign fees/commissions relief, foreign-capital brought-in treatment and treaty-specific exemption; exact current authenticated state portal fields/rounding, presumptive-tax regulations, routine quarterly advance dates and state extensions; former PITA late-return/failure-to-deduct penalties, automatic credit refund or carry into the next payroll year. No personal child/dependent/meal/utility allowance, blanket healthcare deduction or arbitrary voluntary-pension ceiling is authorised here. Current digital-assets inclusion and original prohibitions against netting WHT receipts, treating capex as expenses, omitting other income or fabricating facts are retained above.
