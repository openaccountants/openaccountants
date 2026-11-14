---
name: bangladesh-pit
description: "Compute Bangladesh ordinary individual income tax for assessment year 2026-2027, with current salary relief, category bands, investment rebate, minimum tax and filing windows. Historical salary-component and rebate algorithms are superseded."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bangladesh-pit"
  jurisdiction: "BD"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bangladesh personal income tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For resident individuals and non-resident Bangladeshi citizens within the ordinary band schedule. Tax year: assessment year 2026-2027, normally income year 1 July 2025 to 30 June 2026. The same ordinary bands are enacted for assessment year 2027-2028. Non-Bangladeshi non-residents do not use this band card. Special-rate/final-tax income and wealth/environmental surcharges need separate analysis.

## Ask the client first

- Income and assessment years; citizenship; day counts and residence history.
- Taxpayer category, age, qualifying disability/dependent or gazetted status.
- Each income head, exemptions, salary/benefits, business expenses and losses.
- Eligible investment receipts and applicable scheme conditions.
- Prior filing history, documented source/advance tax, assets and vehicles, intended filing date.

## The method, step by step

### Quick reference and rates, bands and thresholds

Amounts are BDT. These are enacted figures, not the original budget proposal.

| Item and conditions | Amount or rate | Official provision |
|---|---|---|
| General ordinary threshold, AY 2026-2027/2027-2028 | 400,000 at 0% | Finance Act schedule 2, part 1 A: https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf |
| Women or age at least 65, same years | 450,000 at 0% | same |
| Third-gender taxpayer or individual with disability | 525,000 at 0% | same |
| Gazette-listed war-wounded freedom fighter or gazetted injured July uprising fighter | 550,000 at 0% | same |
| Parent/legal guardian of dependent with disability | Add 50,000 per qualifying child/dependent; only one parent claims where both are taxpayers | same |
| First band above the applicable threshold | Next 300,000 at 10% | same |
| Following band | Next 400,000 at 15% | same |
| Following band | Next 500,000 at 20% | same |
| Following band | Next 2,000,000 at 25% | same |
| Balance above those bands | 30% | same |
| Minimum where total income exceeds applicable threshold | 5,000; 1,000 for a new taxpayer, not a location-based floor | same |
| Employment-income exclusion | Lower of 1/3 of employment income or 500,000 (in words on the page); apply to the statutory employment base | Sixth Schedule part 1 paragraph 27 for 1/3: https://nbr.gov.bd/uploads/acts/Income_tax_act_2023.pdf ; cap amended by Act 89 section 135: https://bdlaws.minlaw.gov.bd/act-1718/section-59129.html |
| Investment rebate for resident individual or non-resident Bangladeshi individual | Lowest of 3% of adjusted income A, 10% of eligible investment B (source coefficient 0.10), or 750,000 (7.50 lakh, in words on the page) | Income Tax Act section 78: https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html |

### Establish the base before applying bands

1. Establish residence using section 2(45): presence at least 183 days in the income year, or at least 90 days that year plus at least 365 days in the preceding 4 years. Never use the old 182-day shorthand (https://bdlaws.minlaw.gov.bd/act-1429/section-51794.html). Residents' worldwide income and non-residents' Bangladesh-source income are subject to section 26 and the specific exclusions (https://bdlaws.minlaw.gov.bd/act-1429/section-51818.html). A foreign customer does not alone make a service performed in Bangladesh foreign-earned exempt income.
2. Separate employment, rent, agriculture, business/profession, capital gains, financial assets and other sources under section 30. Determine the applicable computation for each head before aggregation. Keep relief under [IT/freelancer](bd-it-freelancer-tax.md) separate from taxable domestic income. Refer property/capital-gain/loss computations where the applicable detailed provisions have not been applied.
3. For ordinary employment use the statutory employment-income base and the aggregate exclusion above. Do not deduct the old separate house-rent, medical, conveyance or leave-fare limits on top. Basic pay, house rent, medical, conveyance, bonuses and other benefits enter the employment analysis; exclusions for particular benefits must be separately sourced.
4. Apply ordinary bands to aggregated ordinary income using the taxpayer's category threshold. Do not subtract the threshold and then apply a second full exemption. Check special-rate/final-tax income separately.
5. Rebate A excludes exempt income, reduced-rate income, partnership/AOP share income and income subject to final tax liability. Rebate B includes only qualifying investments/expenditure under Sixth Schedule part 3, subject to each instrument's limits. Do not use the old income-tiered rebate or a percentage-of-income investment cap. Insurance, approved/recognized funds, savings/deposit schemes, securities and donations require instrument-specific qualification; an investment label alone is insufficient (https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html).
6. Deduct the available rebate, then enforce the applicable ordinary minimum when income exceeds the threshold. Test other statutory minimum tax, surcharge and special regimes before deducting supported source/advance tax under section 173. A missing certificate is not a supported credit (https://bdlaws.minlaw.gov.bd/act-1429/section-52003.html). A credit excess is a reconciliation item, not an automatic cash refund.

### Filing, payment and timing adjustments

Section 166 covers income above the threshold, prior assessments, specified roles/entities, exemption/reduced-rate income, registration and proof-of-return requirements, with express exceptions. A TIN or exempt income is not proof of a positive tax bill. Use https://etaxnbr.gov.bd for individual e-Return and retain the filed return, payment challan/reference and acknowledgement. Reconcile the income, exempt-income, investment, assets/liabilities and living-expense schedules applicable to the person; do not invent portal box numbers.

The current section 170 replaced the old universal November deadline. For ordinary individuals/HUFs the following applies across the assessment year; amounts are based on tax payable under section 173(2), after source/advance tax, not gross receipts.

| Filing window and condition | Adjustment | Official provision |
|---|---|---|
| 1 July to 30 September | Incentive: lower of 5% of section 173(2) tax payable or 25,000 (in words on the page) | Section 170(1)(a): https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html |
| 1 October to 31 December | No timing incentive or additional tax | same |
| 1 January to 31 March | Additional tax: higher of 2% of section 173(2) tax payable or 3,000 (in words on the page) | same |
| 1 April to 30 June | Additional tax: higher of 5% of section 173(2) tax payable or 5,000 (in words on the page) | same |
| Individual who has never filed | May file by 30 June after the income-year end, paying tax at the applicable rate | Section 170(1)(b): https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html |
| Qualifying overseas individual on higher-study leave, deputation/lien or lawful earning visa and permit | File within 90 days after return to Bangladesh | Section 170(1)(c): https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html |
| Listed day is a government holiday | Immediately following working day | Section 170(3): https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html |

Pay the applicable tax and surcharge by filing under section 173. Do not substitute an assumed automatic January extension. Other penalties, arrears and notices require the relevant current section and are not replaced by these timing adjustments.

## Worked cases

### Salary example, correcting the old component-exemption method

Illustrative ordinary resident general-category employee, no special income, surcharge, source credit or additional minimum-tax regime. Annual basic 720,000, house rent 360,000, medical 72,000, conveyance 30,000 and bonus 120,000 total 1,302,000. Aggregate employment exclusion is 434,000, leaving 868,000. Ordinary band tax is 55,200. Assume 300,000 investment has already been checked as eligible: rebate is 26,040; liability is 29,160. October filing has no timing adjustment. These computed figures are derived from the provisions above.

```oa-check
name: Ordinary salary with current aggregate exclusion
inputs:
  basic: 720000
  house_rent: 360000
  medical: 72000
  conveyance: 30000
  bonus: 120000
  eligible_investment: 300000
steps:
  - gross: basic + house_rent + medical + conveyance + bonus
  - exclusion: min(gross / 3, 500000)
  - income: gross - exclusion
  - band_10: min(max(income - 400000, 0), 300000) * 0.10
  - band_15: min(max(income - 700000, 0), 400000) * 0.15
  - gross_tax: band_10 + band_15
  - rebate: min(income * 0.03, eligible_investment * 0.10, 750000)
  - tax: max(gross_tax - rebate, 5000)
expected:
  gross: 1302000
  income: 868000
  gross_tax: 55200
  rebate: 26040
  tax: 29160
```

### Decision: filing now versus after the neutral window

An ordinary existing filer has liability 33,000 after rebate and documented source tax 10,000. Section 173(2) payable is 23,000. October filing requires 23,000; January filing adds 3,000, producing 26,000. The choice costs 3,000, derived. This example is not the special never-filed case.

```oa-check
name: Existing filer timing choice after documented source tax
inputs:
  liability: 33000
  source_tax: 10000
steps:
  - payable: liability - source_tax
  - january_addition: max(payable * 0.02, 3000)
  - october_total: payable
  - january_total: payable + january_addition
  - difference: january_total - october_total
expected:
  payable: 23000
  october_total: 23000
  january_addition: 3000
  january_total: 26000
  difference: 3000
```

## When to refuse or refer

Do not infer an exemption, rebate instrument, credit or residence. Refer non-Bangladeshi non-residents, HUF-specific issues, capital gains/property computations, loss set-off, high-wealth or multiple-vehicle surcharges, treaty claims and statutory minimum/final-tax regimes before finalizing. Do not use the old calculator as legal authority.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for Finance Act schedule 2, part 1 paragraph A: AY 2026-2027/2027-2028 bands, category thresholds, dependent increment, non-resident exclusion and minimum tax; later-year bands were read but are not applied | https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf | 2026-11-14 |
| Read for Income Tax Act section 78, investment formula and income exclusions | https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html | 2026-11-14 |
| Read for Income Tax Act section 170, complete individual windows, first-filer/overseas and holiday exceptions | https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html | 2026-11-14 |
| Read for Income Tax Act section 173, payable tax and source/advance tax credits | https://bdlaws.minlaw.gov.bd/act-1429/section-52003.html | 2026-11-14 |
| Read for original Sixth Schedule part 1 paragraph 27 one-third salary exclusion, with its cap superseded by the following 2026 amendment | https://nbr.gov.bd/uploads/acts/Income_tax_act_2023.pdf | 2026-11-14 |
| Read for Finance Act 89 section 135, services banking proviso and salary cap amendment | https://bdlaws.minlaw.gov.bd/act-1718/section-59129.html | 2026-11-14 |
| Read for Income Tax Act section 2(15), (24), (45), periods and residence | https://bdlaws.minlaw.gov.bd/act-1429/section-51794.html | 2026-11-14 |
| Read for Income Tax Act section 26, resident/non-resident scope | https://bdlaws.minlaw.gov.bd/act-1429/section-51818.html | 2026-11-14 |
| Read for Income Tax Act section 166, filing triggers and exceptions | https://bdlaws.minlaw.gov.bd/act-1429/section-51996.html | 2026-11-14 |

Not yet confirmed: Current live e-Return field labels, taxpayer-specific rebate-instrument caps and conditions, detailed special-head/loss computations, surcharge and treaty computations, and non-routine penalties are not supplied here. The old separate salary-component limits, tiered investment rebate, geographical minimum tax and automatic January extension are superseded rather than usable alternatives.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bangladesh-pit` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bangladesh-pit. If neither is available, confirm every figure against the official source pages cited above before relying on it.
