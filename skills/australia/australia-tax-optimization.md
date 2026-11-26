---
name: australia-tax-optimization
description: Use this skill when advising on LEGAL tax minimization strategies for Australian taxpayers — individuals, sole traders, and small business owners. Trigger on phrases like "reduce my tax", "tax planning Australia", "salary vs dividends", "negative gearing", "instant asset write-off", "superannuation strategy", "CGT discount", "trust distribution", "income splitting", "GAAR", "Part IVA", or any question about structuring affairs to legally minimize Australian tax. Covers entity selection, deduction optimization, capital allowances, loss utilization, timing strategies, GST planning, superannuation, and red lines. ALWAYS read this skill before giving Australian tax optimization advice.
version: 1.6
jurisdiction: AU
tax_year: 2025
tax_year_notes: "Figures are for 2025-26; use 2026-27 values only where expressly labelled and relevant to the requested year."
last_updated: 2026-11-26
depends_on:
  - bookkeeping-workflow-base
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
---

# Australia Tax Optimization

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD |
| Tax year | 1 July – 30 June (2025–26) |
| Primary legislation | Income Tax Assessment Act 1997 (ITAA 1997); Income Tax Assessment Act 1936 (ITAA 1936) |
| Anti-avoidance | Part IVA, ITAA 1936 (General Anti-Avoidance Rule) |
| Tax authority | Australian Taxation Office (ATO) |
| Filing deadline | 31 October (self-lodgers); agent-lodged extensions vary |
| Individual top marginal rate | 45% basic income tax above $190,000, generally plus the 2% Medicare levy [ATO, resident tax rates](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents) |
| Company rate (base rate entity) | 25% (aggregated turnover < $50m, ≤80% passive income) |
| Company rate (other) | 30% |
| CGT discount (individuals) | Generally 50% after the asset was acquired at least 12 months before the CGT event, subject to eligibility [ATO, CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount) |
| GST rate | 10% |
| Superannuation guarantee | 12% (2025–26) |

### Individual Tax Brackets (2025–26)

**Individual Tax Brackets (2025–26)**

| Taxable Income (AUD) | Rate | Cumulative Tax |
| --- | --- | --- |
| 0 – 18,200 | 0% | $0 |
| 18,201 – 45,000 | 16% | $4,288 |
| 45,001 – 135,000 | 30% | $31,288 |
| 135,001 – 190,000 | 37% | $51,638 |
| 190,001+ | 45% | — |

The ordinary Medicare levy is 2% of taxable income, with reductions and exemptions. The 2025–26 Medicare levy surcharge is 1%–1.5% when surcharge income exceeds the relevant threshold and appropriate private patient hospital cover is absent for the relevant days. The base thresholds are $101,000 for singles and $202,000 for families, with a $1,500 family threshold increase for each dependent child after the first. Calculate the surcharge separately from the levy.

- **2026-27 rates and the standard deduction** — Do not carry 2025-26 rates into 2026-27; the resident scale changed for 2026-27, and the basic tax on $180,000 taxable income in 2025-26 was $47,938 before Medicare levy and offsets. From 2026-27, section 25-130 provides a standard deduction for qualifying assessable labour income: the lesser of $1,000 and that income, reduced by specified actual deductions, to a minimum of zero. It is not an extra $1,000 on top of work expenses; certain insurance premiums and trade, business or professional association memberships are excluded from the reduction.  _([ATO, Tax rates: Australian residents](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents); [ITAA 1997 (Cth) s 25-130](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-130))_

## Section 2 — Income Splitting & Structuring

### Sole Trader vs Company

- **Sole trader taxation** — all profit taxed at individual marginal rates (up to 47%). Simple structure, ABN-based. Losses offset other personal income (subject to non-commercial loss rules, s 35-10 ITAA 1997). No separate return.  _(s 35-10 ITAA 1997)_
- **Company (Pty Ltd) taxation** — profits taxed at 25% (base rate entity) or 30%. Profits retained in the company are not taxed again until distributed. Franking credits attached to dividends prevent double taxation. Division 7A (ITAA 1936, ss 109C–109T) treats loans and payments to shareholders/associates as unfranked dividends unless complying loan agreements are in place.  _(Division 7A, ITAA 1936, ss 109C–109T)_
- **Marginal rate comparison** — In 2025–26, $100,000 of resident taxable income falls in the 30% bracket before Medicare. Compare the whole entity and shareholder position, including when profits will be distributed.
- **Model the whole position** — Do not recommend incorporation from profit alone: include company tax, personal tax on remuneration and distributions, superannuation, payroll obligations, administration and access to cash. Company money retained after tax is not the shareholder's after-tax spending money, base rate entity status must be checked for the year, and the personal services income rules can attribute an individual's income back to them regardless of the entity.  _([TR 2022/3](https://www.ato.gov.au/law/view/view.htm?docid=TXR%2FTR20223%2FNAT%2FATO%2F00001))_

### Salary vs Dividends (Company Directors)

- **Salary** — deductible to the company, taxed to the individual, triggers PAYG withholding and super guarantee (12%). Generates assessable income for super contribution purposes.
- **Franked dividends** — not deductible to the company, carry franking credits. Grossed-up amount included in individual return, franking credit offset applied. No super guarantee obligation.
- **Salary and dividends** — Model combined company and personal tax and the effect of existing income. The full-year resident tax-free threshold is $18,200. Salary and franked dividends have distinct PAYG, super and company tax consequences.
- **Division 7A before drawing on company cash** — Review private company payments, loans and debt forgiveness under Division 7A, including loan documentation, deadlines, benchmark interest and minimum repayments, before treating an advance as tax-free access to profits.  _([ATO, Division 7A calculator and decision tool](https://www.ato.gov.au/calculators-and-tools/division-7a-calculator-and-decision-tool))_

### Family Trusts

Discretionary (family) trusts may distribute income to eligible beneficiaries. Make a valid income distribution resolution by 30 June for a standard year unless the deed requires an earlier date. Check capital gain and franked distribution entitlement rules separately.

- **Section 100A reimbursement agreements** — Check the reimbursement agreement, benefit to another person, tax reduction purpose and ordinary family or commercial dealing exception. Where section 100A applies, the beneficiary is deemed never to have been presently entitled for these tax purposes, and the trustee is generally assessed under section 99A.  _(ITAA 1936 ss 99A and 100A)_
- **How section 100A operates** — Inspect the deed, beneficiary eligibility, valid resolutions made by the applicable deadline and who receives the economic benefit. Keep contemporaneous records.  _([TR 2022/4](https://www.ato.gov.au/law/view/document?docid=TXR/TR20224/NAT/ATO/00001))_
- **Family trust election** — An election can change the applicable trust loss tests and affect eligibility for franking credits under the holding-period rules. Test each under its own provisions. Consider family trust distribution tax before making an election.
- **Resident minors** — For 2025–26, eligible income is tax free up to $416, taxed at 66% of the excess over $416 from $417 to $1,307, and taxed at 45% of the whole eligible amount from $1,308. Check excepted income, excepted persons and residency.  _([ATO, Tax rates if you're under 18](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-if-you-re-under-18-years-old))_

### Superannuation as Income Splitting

- **Spouse contributions** — Subject to eligibility, the offset is 18% of the lesser of eligible contributions and $3,000 reduced by the spouse's relevant income over $37,000. The maximum offset is $540 and relevant income must be below $40,000.
- **Contribution splitting** — For taxed splittable contributions, the maximum is generally the lesser of 85% of eligible concessional contributions and the applicable concessional cap. Check when to apply, the receiving spouse's eligibility and whether the fund offers splitting.

## Section 3 — Deductions Most People Miss

**Deductions Most People Miss**

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Home office running expenses | s 8-1 ITAA 1997, PCG 2023/1 | Fixed rate 70c per hour for 2025–26, or actual cost. Keep records of all hours worked from home and evidence of covered expenses. Phone and internet are covered by the fixed rate |
| Self-education expenses | s 8-1 | Must have sufficient connection to current income-earning activities. The former $250 reduction does not apply to expenses incurred from 1 July 2022 |
| Phone and internet | s 8-1 | For eligible expenses outside the working-from-home fixed rate, apportion work use. A representative 4-week record can support the calculation with evidence of cost |
| Income protection insurance | s 8-1 | Premiums for policies replacing lost income are deductible |
| Professional memberships and subscriptions | s 8-1 | CPA Australia, CA ANZ, industry bodies |
| Tax agent fees | s 25-5 | Cost of managing tax affairs including prior-year amendments |
| Union fees | s 8-1 | Full deduction |
| Tools and equipment (≤$300) | s 40-80(2) | The immediate decline-in-value deduction requires predominantly non-business assessable income use. Check the $300 tests for sets and identical or substantially identical assets and apportion private use |
| Travel between workplaces | s 8-1 | Deductible (but NOT home-to-work commuting) |
| Donations to DGRs | Div 30 | Deductible gifts to Deductible Gift Recipients |
| Prepaid deductible expenses | [ITAA 1936 ss 82KZL and 82KZM](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) | For an individual's non-business expenditure, the eligible service period must be no more than 12 months and end by the end of the following income year. Check the exceptions and separate agreement rules below |

- **Self-education $250 reduction removed** — The $250 reduction no longer applies to self-education expenses incurred from 1 July 2022; the expense must still connect with current income-earning activities.  _([ATO, Self-education expenses](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/education-training-and-seminars/self-education-expenses))_

## Section 4 — Capital Allowances Optimization

### Instant Asset Write-Off (2025–26)

- **Instant asset write-off eligibility** -- For 2025-26, eligible entities choosing simplified depreciation can deduct the taxable-purpose amount of qualifying assets whose full statutory cost is less than $20,000. Confirm the holding-year choice, first taxable use or readiness, acquisition conditions and prior claims. [ITTPA 1997, s 328-180(4)(d)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).
- **Simplified depreciation pool** -- Covered assets not individually deductible, including those costing exactly $20,000, generally enter the pool. Use the statutory rates and pre-depreciation low-pool-value test below.
- **Ongoing $20,000 threshold from 1 July 2026** — The Treasury Laws Amendment (Tax Reform No. 2) Act 2026, assented to on 26 August 2026 with schedules commencing 1 October 2026, makes the $20,000 instant asset write-off threshold ongoing, with application provisions covering assets first used or installed from 1 July 2026. Simplified depreciation eligibility and the taxable-use rules still apply, and a deduction reduces taxable income without reimbursing the purchase price.  _([Treasury Laws Amendment (Tax Reform No. 2) Act 2026](https://www.legislation.gov.au/C2026A00071/asmade/text))_

To enter simplified depreciation or claim an individual new-asset deduction, confirm the eligibility and choice conditions in Subdivision 328-D. An existing general small business pool continues under that Subdivision for the year and later years even if the entity is no longer a small business entity or does not choose it for the year. New assets first used in such a year cannot be allocated to that pool until a year when the entity is eligible and chooses the Subdivision (s 328-220). Check aggregated-turnover eligibility, the required choices for the holding and first taxable-use years, first use or installation ready for taxable use, prior claims and statutory exclusions. Test the asset's full statutory cost, after applicable GST adjustments but before private-use apportionment, against the strict less-than-$20,000 threshold. The deduction is limited to taxable use. Covered assets not individually deductible under s 328-180 generally enter the small business pool; exactly $20,000 is included. General Division 40 rules apply when simplified depreciation does not apply or an exception requires them.

For ordinary pool depreciation, use 30% of the opening pool balance and 15% of the taxable-purpose adjustable value of assets first used or installed ready for taxable use during the year; relevant later cost additions have their own 15% rule. Do not assign 15% merely because a previously used asset enters the opening pool. First check s 328-210: opening pool balance plus taxable-purpose new-asset amounts and cost additions, less relevant taxable-purpose termination values, with the statutory adjustments. If that amount is more than zero and less than $20,000, deduct it instead of ordinary pool depreciation and close the pool at zero. Test before ordinary depreciation, not against the smaller closing balance after it. Check exclusions and special rules, including assets outside Division 40, relevant primary-production assets, leases and existing pools. [ITAA 1997, ss 328-175 to 328-220](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html).

For 2025-26, the temporary asset threshold and pool threshold are supported by [ITTPA 1997, s 328-180(4)(d) and (6)(e)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html); check the acquisition and first-use conditions. For later first use and pool assessments, apply the permanent threshold's specific application rules in [Tax Reform No. 2 Act 2026, schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text).

#### Small business pool boundary checks

Assume an eligible entity chose simplified depreciation for 2025-26 and the required holding year. Costs are correctly adjusted for GST, new assets were acquired and first used for taxable purposes in 2025-26, cost equals initial adjustable value and no exclusion, cap or other special rule changes the result.

With no other pool amounts, a wholly business-use asset costing $19,999 can qualify for the individual write-off. A wholly business-use asset costing exactly $20,000 enters the pool: the pre-depreciation pool amount is $20,000, which is not less than the threshold. Its 15% deduction is $3,000 and closing balance is $17,000. Do not then write off that closing balance in the same year.

```oa-check
name: Exactly 20000 remains in the ordinary small business pool
inputs:
  below_cost: 19999
  exact_cost: 20000
  taxable_use_percent: 100
  first_year_rate: 15
steps:
  - below_asset_deduction: pct(below_cost, taxable_use_percent)
  - pre_depreciation_pool: pct(exact_cost, taxable_use_percent)
  - pool_deduction: pct(pre_depreciation_pool, first_year_rate)
  - closing_pool: pre_depreciation_pool - pool_deduction
expected:
  below_asset_deduction: 19999
  pre_depreciation_pool: 20000
  pool_deduction: 3000
  closing_pool: 17000
```

For the statutory pool example, opening balance $28,500 plus 80% of a new $21,000 asset, less $29,600 taxable-purpose termination value, gives $15,700 before ordinary depreciation. It is positive and below $20,000, so the pool deduction is $15,700 and closing balance is zero. Separately, a $30,000 asset with 60% taxable use fails the individual cost test even though its taxable amount is $18,000; with no other pool amounts, that $18,000 can instead qualify for the low-pool-value deduction.

```oa-check
name: Low pool value uses the statutory amount before depreciation
inputs:
  opening_pool: 28500
  new_asset_cost: 21000
  new_asset_taxable_percent: 80
  taxable_termination_value: 29600
  mixed_asset_cost: 30000
  mixed_asset_taxable_percent: 60
steps:
  - new_taxable_amount: pct(new_asset_cost, new_asset_taxable_percent)
  - low_pool_amount: opening_pool + new_taxable_amount - taxable_termination_value
  - pool_deduction: low_pool_amount
  - closing_pool: low_pool_amount - pool_deduction
  - mixed_asset_pool_amount: pct(mixed_asset_cost, mixed_asset_taxable_percent)
expected:
  new_taxable_amount: 16800
  low_pool_amount: 15700
  pool_deduction: 15700
  closing_pool: 0
  mixed_asset_pool_amount: 18000
```

### General Depreciation

**General Depreciation Methods**

| Method | How It Works |
| --- | --- |
| Diminishing value | Base value × (qualifying days / 365) × (applicable 150% or 200% factor / effective life) |
| Prime cost (straight-line) | Generally cost × (qualifying days / 365) × (100% / effective life), with statutory adjustments |

For general Division 40 depreciation, use 150% for assets held before 10 May 2006 and generally 200% for assets first held on or after that date. Check reacquisition, rollover and other special rules before choosing the factor. Apply the statutory base value, qualifying days divided by 365, taxable-use adjustment and decline limits. Prime cost uses its separate cost/effective-life formula, with adjustments where required. These are tax calculations, separate from accounting depreciation. [ITAA 1997, ss 40-25, 40-70, 40-72 and 40-75](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

- **Effective life determination** -- Choose the applicable Commissioner determination under s 40-95, including its contract-date/start-time rules, or a valid self-assessed life. The [2025 determination, Schedule 2](https://www.legislation.gov.au/F2025L01097/asmade/text) is the current instrument at 12 November 2026, but the latest instrument does not automatically replace the life for an existing asset. [ITAA 1997, s 40-95](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

### Motor Vehicles

- **Car cost limit for depreciation (2025–26)** — $69,674 AUD (Only the business-use portion of this amount can be depreciated)
- **Business-use substantiation** — Business-use percentage must be substantiated via logbook (minimum continuous 12-week period, valid for 5 years) or cents-per-km method (88c/km for 2025–26, max 5,000 business km = $4,400; 91c/km from 2026–27).

## Section 5 — Loss Utilization

### Individual/Sole Trader Losses

- **Loss carry forward** — Tax losses carry forward indefinitely (s 36-15 ITAA 1997). No carry-back for individuals.  _(s 36-15 ITAA 1997)_
- **Non-commercial losses (Division 35)** — Ordinarily, both adjusted taxable income below $250,000 and one activity test are required to offset the loss against other income. The tests are assessable activity income of at least $20,000, a tax profit in 3 of 5 years including the current year, at least $500,000 of qualifying real property, or at least $100,000 of qualifying other assets. The primary production and professional arts exception and Commissioner discretion are separate pathways.  _(Division 35)_

### Company Losses

- **Continuity of ownership test (COT)** — Carry forward subject to continuity of ownership test (COT) — same persons must maintain >50% voting, dividend, and capital rights (s 165-12). If COT fails, the same business test (SBT) may save losses if the company carries on the same business (s 165-13). The similar business test was enacted in 2019 and can apply to relevant losses from income years starting on or after 1 July 2015 (s 165-211).  _(s 165-12; s 165-13)_

### Loss Carry-Back (Companies)

- **Temporary loss carry-back (claims for 2020–21 to 2022–23)** — Eligible corporate tax entities with aggregated turnover below $5 billion could choose to carry back eligible losses from 2019–20 to 2022–23 on their 2020–21, 2021–22 or 2022–23 return, subject to the statutory conditions.
- **Corporate loss carry-back from 2026-27** — The Tax Reform No. 2 Act's loss carry-back regime applies to assessments for income years starting on or after 1 July 2026, following its 1 October 2026 commencement. Eligible corporate tax entities that are not significant global entities can carry qualifying losses to either or both of the preceding two income years, subject to the choice, lodgement and franking conditions.  _([Treasury Laws Amendment (Tax Reform No. 2) Act 2026](https://www.legislation.gov.au/C2026A00071/asmade/text))_

## Section 6 — Timing Strategies

**Timing Strategies**

| Strategy | Detail |
| --- | --- |
| Determine income derivation by year end | Under the receipts method, consider when payment was received. Under the earnings method, consider when a recoverable debt arose. Check the contract and the appropriate method [TR 98/1](https://www.ato.gov.au/law/view/document?docid=TXR/TR981/NAT/ATO/00001) |
| Eligible prepayments before year end | Test the taxpayer, service period, choices and agreement rules below before bringing forward a deduction. Paying before 30 June alone does not qualify |
| Bring forward asset purchases | Use instant asset write-off before 30 June deadline. Asset must be first used or installed ready for use |
| Concessional super contribution | Maximise contributions before 30 June — $30,000 cap (2025–26). Carry-forward unused cap available if total super balance <$500,000 |
| Capital gains harvest | Realise capital losses before 30 June to offset gains. Wash sale rules: ATO will scrutinise buybacks of substantially similar assets |
| Defer capital gains | For eligible individuals and trusts, the 50% discount generally requires acquisition at least 12 months before the CGT event [ATO, CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount) |
| Small business CGT concessions | Div 152: 15-year exemption, 50% active asset reduction, retirement exemption ($500k lifetime cap), rollover. Maximum net asset value no more than $6m or aggregated turnover below $2m, subject to the other Division 152 conditions [ATO, small business CGT concessions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions) |

The ordinary 12 month rule applies to otherwise deductible non-business expenditure of individuals and to qualifying small or medium business entities that have not chosen section 82KZMD. The eligible service period must be no more than 12 months and end by the last day of the income year following the year the expenditure is incurred. Otherwise, non-excluded expenditure is spread over the eligible service period under section 82KZM. Use the statutory service period, which starts no earlier than incurrence and is capped at 10 years; the payment date alone does not establish it. [ITAA 1936 ss 82KZL, 82KZM and 82KZMA](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

First establish that the expense is deductible. Excluded expenditure includes amounts strictly less than $1,000; its exclusion from these timing rules does not create a deduction for private or capital costs. The separate agreement rules in sections 82KZME and 82KZMF can require spreading even where the ordinary 12 month test is met. Check their conditions and exceptions, including the specified rental insurance and acquisition-loan interest exception in section 82KZME(5); it does not cover every rental expense or borrowing purpose. [ITAA 1936 ss 82KZL and 82KZME-82KZMF](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

For example, assume an individual's otherwise deductible non-business expense incurred on 25 June 2026 is not excluded expenditure and no separate agreement rule or other exception applies. Services run from 1 September 2026 to 31 August 2027. Although that is 12 months, it ends after 30 June 2027. Section 82KZM spreads the deduction over that service period; none falls in 2025-26.

## Section 7 — GST Optimization

**GST Optimization**

| Topic | Detail |
| --- | --- |
| Registration threshold | Mandatory if current or projected GST turnover ≥$75,000 ($150,000 for non-profits). Voluntary registration below threshold to claim input tax credits |
| Cash vs accrual reporting | Cash basis available if aggregated turnover <$10m. Defers GST on income until payment received |
| Input tax credits | Claim GST on business purchases. Apportionment required for mixed (business/private) use |
| GST-free supplies | Exports, health, education, some food — no GST charged, but input credits still claimable. Valuable for exporters |
| Going concern | Sale of a business as a going concern is GST-free (Div 38) — avoids cash flow impact on business transfers |
| Margin scheme (property) | GST calculated on margin (sale price minus purchase price) rather than full sale price. Buyer cannot claim input credits |
| Tax periods | Usually quarterly below $20m unless reporting monthly by election or direction. Eligible voluntarily registered entities can generally elect annual reporting below $75,000, or $150,000 for non-profits |

- **Conditions, not elections** — Going-concern and margin-scheme treatment depend on their own conditions and agreement between the parties; neither is an automatic election that makes a sale cheaper. Establish registration, creditable purpose and valid tax invoices before claiming credits.

## Section 8 — Superannuation & Social Security Optimization

### Superannuation (Retirement)

**Superannuation (Retirement)**

| Strategy | Detail | Legislation |
| --- | --- | --- |
| Concessional contributions | Cap $30,000/year (2025–26). Tax-deductible for self-employed. Taxed at 15% in the fund | s 291-20 ITAA 1997 |
| Carry-forward unused cap | Unused concessional cap from up to 5 prior years if total super balance <$500,000 at prior 30 June | s 291-170 |
| Non-concessional contributions | Cap $120,000/year (or $360,000 under bring-forward rule over 3 years). Not deductible, but earnings taxed at max 15% in super | s 292-85 |
| Salary sacrifice | Pre-tax super contributions reduce assessable income. Counted towards concessional cap |  |
| Spouse contribution offset | Contribute to low-income spouse's super for tax offset up to $540 | s 290-230 |
| Government co-contribution | For 2025–26, eligible personal after-tax contributions attract 50c per dollar, up to $500 at relevant income of $47,488 or less, tapering to zero at $62,488 | Superannuation (Government Co-contribution for Low Income Earners) Act 2003 [ATO, government contributions](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/government-contributions) |
| Division 293 tax | Additional 15% contributions tax on individuals with income + concessional contributions >$250,000 | Div 293 |

- **2026-27 concessional cap** — The general concessional cap is $32,500 for 2026-27, up from $30,000 in 2025-26. Count contributions across all funds, including employer and salary sacrifice amounts, and check fund receipt dates and the actual unused amounts before relying on the carry-forward. Before claiming a personal contribution deduction, lodge the notice of intent and obtain the fund's acknowledgement, and weigh contributions tax, Division 293 and preservation against the personal tax saving.  _([ATO, Concessional contributions cap](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap); [ATO, Personal super contributions](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/how-to-save-more-in-your-super/personal-super-contributions))_

### Medicare Levy Surcharge Avoidance

- **Medicare levy surcharge** — Compare policy premiums with the calculated surcharge. Check that appropriate private patient hospital cover extends to all dependants for the relevant days and apply the thresholds in section 1.

## Section 9 — Investment & Retirement

**Investment & Retirement**

| Strategy | Detail |
| --- | --- |
| CGT 50% discount | Eligible individuals and trusts generally apply the 50% discount after capital losses where the asset was acquired at least 12 months before the CGT event [ATO, CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount) |
| Negative gearing | Apply deductible expenditure and loss rules for the transaction year and ownership structure. For excess residential rental deductions from 2027–28, check the new restrictions and transitional rules below [Tax Reform No. 1 Act 2026, Schedule 2](https://www.legislation.gov.au/C2026A00049/asmade/text) |
| Franking credits | Australian company dividends carry franking credits. Excess credits refundable for individuals and super funds |
| Super in retirement phase | Eligible retirement-phase earnings may be exempt. The general transfer balance cap is $2m in 2025–26 and $2.1m in 2026–27. Personal caps can differ [ATO, transfer balance cap](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/transfer-balance-cap) |
| Transition to retirement (TTR) | A qualifying member can start a TTR income stream at preservation age. Before it enters retirement phase, investment earnings generally remain taxable in the fund at up to 15% [ATO, transition to retirement](https://www.ato.gov.au/individuals-and-families/jobs-and-employment-types/working-as-an-employee/leaving-the-workforce/transition-to-retirement) |

- **Model the transaction year** — The Tax Reform No. 1 Act changes CGT from 1 July 2027 and restricts excess residential rental deductions from 2027-28, with transitional rules and exceptions, and the working Australians tax offset also starts in 2027-28. Model capital gains and rental deductions for the actual year of the transaction and keep a dated comparison with assumptions, eligibility evidence, implementation deadlines and whole-year tax and cash effects.  _([Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/asmade/text))_

## Section 10 — Red Lines (GAAR & Scrutiny Triggers)

### Part IVA (General Anti-Avoidance Rule)

- **Part IVA GAAR** — ITAA 1936, Part IVA (ss 177A–177J). The Commissioner can cancel a tax benefit arising from a scheme if the dominant purpose (assessed objectively) was to obtain the tax benefit. Penalties: 50% shortfall (scheme); 25% if reasonably arguable position.  _(ITAA 1936, Part IVA (ss 177A–177J))_

### ATO Scrutiny Triggers

**ATO Scrutiny Triggers**

| Trigger | Risk |
| --- | --- |
| Trust distributions with reimbursement agreements | Assess s 100A conditions and the ordinary dealing exception. Where it applies, present entitlement is disregarded for the relevant tax and the trustee is generally assessed under s 99A |
| Division 7A non-complying loans | Deemed unfranked dividend |
| Non-commercial losses offset against other income | Check the income requirement with any one activity test, or a separate exception or exercise of discretion |
| Large work-related deductions vs income | Risk of audit |
| Wash sales | Part IVA can cancel a tax benefit from a wash sale when its scheme, tax benefit and dominant-purpose tests are met |
| Artificial income splitting via interposed entities | Part IVA application |
| Personal services income (PSI) through company or trust | PSI rules attribute income back to individual (Div 86–87) |
| Salary sacrifice and Division 293 | Assess Division 293 income with relevant low-tax contributions. Salary sacrifice counts towards the concessional cap and cannot satisfy compulsory employer super |
| Contractor vs employee misclassification | Super guarantee charge, penalties |
| Cryptocurrency — unreported disposal events | ATO data-matching from exchanges |

### Absolute Prohibitions

- **NEVER advise backdating trust distribution resolutions past 30 June** — NEVER advise backdating trust distribution resolutions past 30 June
- **NEVER advise sham contracting arrangements** — NEVER advise sham contracting arrangements
- **NEVER advise fabricating deductions or inflating claims** — NEVER advise fabricating deductions or inflating claims
- **NEVER structure arrangements with the dominant purpose of tax avoidance** — NEVER structure arrangements with the dominant purpose of tax avoidance
- **NEVER advise ignoring Division 7A requirements for private company loans** — NEVER advise ignoring Division 7A requirements for private company loans

## Section 11 — Annual Tax Planning Calendar

**Annual Tax Planning Calendar**

| When | Action |
| --- | --- |
| July | New FY starts. Review prior year's unused concessional super cap. Lodge prior-year BAS |
| August–September | Obtain prior-year tax assessment. Review loss carry-forward position |
| October | Self-lodger deadline (31 Oct). Review investment portfolio for CGT planning |
| November–December | Mid-year tax review. Adjust PAYG instalments if income changed materially |
| January | Under the quarterly rules through 2025–26, December-quarter super is generally due on 28 January. From 1 July 2026, apply payday super receipt deadlines. Review Division 7A loan repayments |
| February–March | Lodge Q2 BAS. Model year-end tax position. Begin pre-30 June planning |
| April–May | Execute prepayment strategies. Make concessional super contributions. Review asset purchases for instant write-off |
| June | Finalise trust distribution resolutions by the applicable deadline. Ensure funds receive intended contributions in time. Check prepayment, capital loss and PAYG variation rules |

## Section 12 — Cash Impact Examples

### Example 1 — Sole Trader Incorporates

**Before:** In 2025–26 a full-year resident sole trader with $180,000 taxable income pays $47,938 basic tax and $3,600 ordinary Medicare levy, totalling $51,538. Assume no offsets or Medicare levy surcharge.

**After:** Assume the base rate entity deducts $80,000 salary and $12,000 employer super, including $2,400 above compulsory 12% super on $80,000 of ordinary time earnings. Its $88,000 taxable profit gives $22,000 company tax. The owner pays $14,788 basic tax plus $1,600 Medicare levy, or $16,388. Company and personal tax total $38,388 for the year, $13,150 below the sole trader total. Future distributions and tax inside super are outside this comparison.

### Example 2 — Maximising Super Contributions

An eligible resident makes a $30,000 personal contribution, lodges a valid notice and obtains fund acknowledgement. Assume no other concessional contributions, offsets, surcharge or Division 293 tax. A $30,000 deduction reduces taxable income from $120,000 to $90,000. Basic tax falls by $9,000 and ordinary Medicare levy by $600. The fund's 15% tax is $4,500, giving a $5,100 combined saving on these assumptions.

### Example 3 — Instant Asset Write-Off

An eligible small business using simplified depreciation buys and first uses 3 laptops at $2,500 each and a vehicle at $18,000. Assume full taxable use, GST-adjusted costs, required choices and no exclusions. The immediate deduction is $25,500. At a constant 30% marginal income-tax rate the deduction reduces basic tax by $7,650 before any levy or offsets. The incremental first-year benefit compared with ordinary depreciation depends on the deductions available in that year.

### Example 4 — Negative Gearing Investment Property

A resident employee earns $120,000 in 2025–26 and receives $25,000 rent with $35,000 of allowable expenses. The $10,000 loss reduces taxable income to $110,000. Basic tax falls by $3,000 and the ordinary Medicare levy by $200, assuming no offsets or surcharge. An approved PAYG withholding variation can change what the payer withholds during the year. The assessment determines any refund.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by Ryan Duguid.

## Sources

- [ITAA 1936 ss 82KZL-82KZMF](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html): eligible service period, taxpayer/choice conditions, excluded expenditure, following-income-year limit and separate agreement rules and exceptions. Selected sections of current compilation 193 read 2026-11-12.

- [ITAA 1936 ss 82KZL-82KZMF, compilation 191](https://www.legislation.gov.au/C1936A00027/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_2/document_2.html): provisions applying to the June 2026 example, read 2026-11-12. The selected provisions agree with current compilation 193.

Read 2026-11-12 for the depreciation correction:

- [ITAA 1997, ss 40-25, 40-70, 40-72, 40-75 and 40-95](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html): eligibility, date-specific factors, formulas and effective-life selection. Selected sections of retained current compilation 268 read 2026-11-12.
- [Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025, Schedule 2](https://www.legislation.gov.au/F2025L01097/asmade/text): asset-specific Table A and Table B lives; select the applicable dated determination. Selected Table A/Table B categories read 2026-11-12.

- [ITAA 1997, ss 328-175, 328-180, 328-185, 328-190, 328-210 and 328-220](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) -- read 2026-11-12 for selected simplified-depreciation eligibility, cost, allocation, rates, low-pool-value and continuing-pool rules.
- [ITTPA 1997, s 328-180(4)(d) and (6)(e)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) -- read 2026-11-12 for the temporary 2025-26 asset and pool thresholds.
- [Tax Reform No. 2 Act 2026, schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text) -- read 2026-11-12 for the permanent threshold application from July 2026.
- [ATO, resident rates](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents); [ATO, fixed-rate work from home deduction](https://www.ato.gov.au/Individuals/Income-deductions-offsets-and-records/Deductions-you-can-claim/Working-from-home-expenses/Fixed-rate-method---67-cents/); [ATO, government super contributions](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/government-contributions); [ATO, Payday Super deadlines](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/payment-deadlines-for-payday-super); [ATO, PAYG withholding variation](https://www.ato.gov.au/forms-and-instructions/payg-withholding-variation-application). Read 2026-11-22.
