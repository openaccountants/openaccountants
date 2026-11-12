---
name: australia-tax-optimization
description: Use this skill when advising on LEGAL tax minimization strategies for Australian taxpayers — individuals, sole traders, and small business owners. Trigger on phrases like "reduce my tax", "tax planning Australia", "salary vs dividends", "negative gearing", "instant asset write-off", "superannuation strategy", "CGT discount", "trust distribution", "income splitting", "GAAR", "Part IVA", or any question about structuring affairs to legally minimize Australian tax. Covers entity selection, deduction optimization, capital allowances, loss utilization, timing strategies, GST planning, superannuation, and red lines. ALWAYS read this skill before giving Australian tax optimization advice.
version: 1.5
jurisdiction: AU
tax_year: 2025
last_updated: 2026-11-12
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
| Individual top rate | 45% + 2% Medicare levy = 47% effective |
| Company rate (base rate entity) | 25% (aggregated turnover < $50m, ≤80% passive income) |
| Company rate (other) | 30% |
| CGT discount (individuals) | 50% on assets held >12 months |
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

Plus 2% Medicare levy on total taxable income. Medicare levy surcharge (1%–1.5%) applies if no private hospital cover and income exceeds $101,000 (single).

- **2026-27 rates and the standard deduction** — Do not carry 2025-26 rates into 2026-27; the resident scale changed for 2026-27, and the basic tax on $180,000 taxable income in 2025-26 was $47,938 before Medicare levy and offsets. From 2026-27, section 25-130 provides a standard deduction for qualifying assessable labour income: the lesser of $1,000 and that income, reduced by specified actual deductions, to a minimum of zero. It is not an extra $1,000 on top of work expenses; certain insurance premiums and trade, business or professional association memberships are excluded from the reduction.  _([ATO, Tax rates: Australian residents](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents); [ITAA 1997 (Cth) s 25-130](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-130))_

## Section 2 — Income Splitting & Structuring

### Sole Trader vs Company

- **Sole trader taxation** — all profit taxed at individual marginal rates (up to 47%). Simple structure, ABN-based. Losses offset other personal income (subject to non-commercial loss rules, s 35-10 ITAA 1997). No separate return.  _(s 35-10 ITAA 1997)_
- **Company (Pty Ltd) taxation** — profits taxed at 25% (base rate entity) or 30%. Profits retained in the company are not taxed again until distributed. Franking credits attached to dividends prevent double taxation. Division 7A (ITAA 1936, ss 109C–109T) treats loans and payments to shareholders/associates as unfranked dividends unless complying loan agreements are in place.  _(Division 7A, ITAA 1936, ss 109C–109T)_
- **Rule of thumb — incorporation threshold** — incorporation typically benefits when taxable profit consistently exceeds ~$100,000, allowing retention at 25% vs 47% marginal. Below $45,000 profit, sole trader is usually superior (16% marginal vs 25% corporate + extraction costs).
- **Model the whole position** — Do not recommend incorporation from profit alone: include company tax, personal tax on remuneration and distributions, superannuation, payroll obligations, administration and access to cash. Company money retained after tax is not the shareholder's after-tax spending money, base rate entity status must be checked for the year, and the personal services income rules can attribute an individual's income back to them regardless of the entity.  _([TR 2022/3](https://www.ato.gov.au/law/view/view.htm?docid=TXR%2FTR20223%2FNAT%2FATO%2F00001))_

### Salary vs Dividends (Company Directors)

- **Salary** — deductible to the company, taxed to the individual, triggers PAYG withholding and super guarantee (12%). Generates assessable income for super contribution purposes.
- **Franked dividends** — not deductible to the company, carry franking credits. Grossed-up amount included in individual return, franking credit offset applied. No super guarantee obligation.
- **Optimal mix** — pay enough salary to cover super guarantee obligations and utilise the tax-free threshold ($18,200); distribute remaining as franked dividends. Model the combined company + personal tax.
- **Division 7A before drawing on company cash** — Review private company payments, loans and debt forgiveness under Division 7A, including loan documentation, deadlines, benchmark interest and minimum repayments, before treating an advance as tax-free access to profits.  _([ATO, Division 7A calculator and decision tool](https://www.ato.gov.au/calculators-and-tools/division-7a-calculator-and-decision-tool))_

### Family Trusts

Discretionary (family) trusts allow income distribution to adult family members in lower brackets. The trustee resolution must be made before 30 June. Key constraints:

- **Section 100A reimbursement agreements** — trust distributions to low-income beneficiaries who redirect funds back to the primary earner are void.  _(Section 100A (ITAA 1936))_
- **How section 100A operates** — Section 100A applies where a reimbursement agreement exists: it treats the beneficiary as not presently entitled for tax purposes and exposes the trustee to tax on that share. It does not make every distribution to a lower-income beneficiary void. Inspect the deed, beneficiary eligibility, valid resolutions made before 30 June and who receives the economic benefit; never backdate a resolution.  _([TR 2022/4](https://www.ato.gov.au/law/view/document?docid=TXR/TR20224/NAT/ATO/00001))_
- **Family Trust Election (FTE)** — required to access franking credits and carry forward losses.
- **Minor beneficiaries penalty rates** — Minor beneficiaries (under 18) taxed at penalty rates on unearned income (Division 6AA) — effectively 66% on amounts above $416.  _(Division 6AA)_

### Superannuation as Income Splitting

- **Spouse contributions** — up to $3,000 contribution to a low-income spouse's super fund → tax offset of up to $540 (18% of $3,000). Spouse must earn <$40,000.
- **Contribution splitting** — up to 85% of concessional contributions from the prior year can be rolled to a spouse's super account (not a deduction, but shifts wealth tax-efficiently).

## Section 3 — Deductions Most People Miss

**Deductions Most People Miss**

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Home office running expenses | s 8-1 ITAA 1997 | Fixed rate 67c/hour (revised method from 1 July 2022) or actual cost. Must keep contemporaneous records (timesheets, diary) |
| Self-education expenses | s 8-1 | Must have sufficient connection to current income-earning activities. The former $250 reduction does not apply to expenses incurred from 1 July 2022 |
| Phone and internet | s 8-1 | Apportion business use %. ATO accepts a representative 4-week diary |
| Income protection insurance | s 8-1 | Premiums for policies replacing lost income are deductible |
| Professional memberships and subscriptions | s 8-1 | CPA Australia, CA ANZ, industry bodies |
| Tax agent fees | s 25-5 | Cost of managing tax affairs including prior-year amendments |
| Union fees | s 8-1 | Full deduction |
| Tools and equipment (≤$300) | s 8-1 | Immediately deductible if cost ≤$300 and used for income |
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
- **Non-commercial loss rules (Division 35) — four tests** — business losses can only offset non-business income if one of four tests is met: 1. Assessable income ≥$20,000 from the activity; 2. Profit in 3 of the last 5 years (including current year); 3. Real property used ≥$500,000; 4. Other assets used ≥$100,000. If no test is met AND adjusted taxable income >$250,000, loss is quarantined. Commissioner discretion may apply.  _(Division 35)_
- **Income requirement comes first** — The ordinary pathway needs both the income requirement (adjusted taxable income below $250,000) and one of the four activity tests; the exceptions and the Commissioner's discretion are separate pathways. A loss is not deferred only when income exceeds the threshold and all four tests fail.  _([ITAA 1997 (Cth) s 35-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/35-10))_

### Company Losses

- **Continuity of ownership test (COT)** — Carry forward subject to continuity of ownership test (COT) — same persons must maintain >50% voting, dividend, and capital rights (s 165-12). If COT fails, the same business test (SBT) may save losses if the company carries on the same business (s 165-13). SBT was broadened in 2015 to a "similar business test."  _(s 165-12; s 165-13)_

### Loss Carry-Back (Companies)

- **Temporary loss carry-back (2019-20 to 2022-23)** — The temporary regime for companies with aggregated turnover below $5 billion ended with the 2022-23 income year; do not model it for later years.
- **Corporate loss carry-back from 2026-27** — The Tax Reform No. 2 Act's loss carry-back regime applies to assessments for income years starting on or after 1 July 2026, following its 1 October 2026 commencement. Eligible corporate tax entities that are not significant global entities can carry qualifying losses to either or both of the preceding two income years, subject to the choice, lodgement and franking conditions.  _([Treasury Laws Amendment (Tax Reform No. 2) Act 2026](https://www.legislation.gov.au/C2026A00071/asmade/text))_

## Section 6 — Timing Strategies

**Timing Strategies**

| Strategy | Detail |
| --- | --- |
| Defer income to next FY | Delay invoicing until after 30 June if cash-basis taxpayer. For accrual-basis, delay delivery/completion |
| Eligible prepayments before year end | Test the taxpayer, service period, choices and agreement rules below before bringing forward a deduction. Paying before 30 June alone does not qualify |
| Bring forward asset purchases | Use instant asset write-off before 30 June deadline. Asset must be first used or installed ready for use |
| Concessional super contribution | Maximise contributions before 30 June — $30,000 cap (2025–26). Carry-forward unused cap available if total super balance <$500,000 |
| Capital gains harvest | Realise capital losses before 30 June to offset gains. Wash sale rules: ATO will scrutinise buybacks of substantially similar assets |
| Defer capital gains | Hold assets >12 months to access 50% CGT discount (individuals and trusts) |
| Small business CGT concessions | Div 152: 15-year exemption, 50% active asset reduction, retirement exemption ($500k lifetime cap), rollover. Net assets <$6m or aggregated turnover <$2m |

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
| Tax periods | Monthly, quarterly, or annual BAS. Quarterly if turnover <$20m. Annual election available if turnover <$75,000 |

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
| Government co-contribution | Contribute to low-income earner's super; government matches up to $500 (income <$45,400) | s 12A SGAA |
| Division 293 tax | Additional 15% contributions tax on individuals with income + concessional contributions >$250,000 | Div 293 |

- **2026-27 concessional cap** — The general concessional cap is $32,500 for 2026-27, up from $30,000 in 2025-26. Count contributions across all funds, including employer and salary sacrifice amounts, and check fund receipt dates and the actual unused amounts before relying on the carry-forward. Before claiming a personal contribution deduction, lodge the notice of intent and obtain the fund's acknowledgement, and weigh contributions tax, Division 293 and preservation against the personal tax saving.  _([ATO, Concessional contributions cap](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap); [ATO, Personal super contributions](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/how-to-save-more-in-your-super/personal-super-contributions))_

### Medicare Levy Surcharge Avoidance

- **MLS avoidance** — Private hospital cover avoids 1%–1.5% MLS if income >$101,000 (single) or >$202,000 (family). Cost of basic hospital cover is often less than the MLS.

## Section 9 — Investment & Retirement

**Investment & Retirement**

| Strategy | Detail |
| --- | --- |
| CGT 50% discount | Individuals and trusts — hold assets >12 months for 50% discount on net capital gain |
| Negative gearing | Investment property/share portfolio borrowing costs exceed income → net loss offsets other income. No cap in Australia |
| Franking credits | Australian company dividends carry franking credits. Excess credits refundable for individuals and super funds |
| Super in pension phase | Earnings on assets supporting income streams in pension phase are tax-free (up to transfer balance cap of $1.9m, indexed) |
| Transition to retirement (TTR) | Access super as income stream from preservation age while still working. Earnings in TTR taxed at 15% (not tax-free) |

- **Model the transaction year** — The Tax Reform No. 1 Act changes CGT from 1 July 2027 and restricts excess residential rental deductions from 2027-28, with transitional rules and exceptions, and the working Australians tax offset also starts in 2027-28. Model capital gains and rental deductions for the actual year of the transaction and keep a dated comparison with assumptions, eligibility evidence, implementation deadlines and whole-year tax and cash effects.  _([Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/asmade/text))_

## Section 10 — Red Lines (GAAR & Scrutiny Triggers)

### Part IVA (General Anti-Avoidance Rule)

- **Part IVA GAAR** — ITAA 1936, Part IVA (ss 177A–177J). The Commissioner can cancel a tax benefit arising from a scheme if the dominant purpose (assessed objectively) was to obtain the tax benefit. Penalties: 50% shortfall (scheme); 25% if reasonably arguable position.  _(ITAA 1936, Part IVA (ss 177A–177J))_

### ATO Scrutiny Triggers

**ATO Scrutiny Triggers**

| Trigger | Risk |
| --- | --- |
| Trust distributions to low-income beneficiaries with reimbursement agreements | s 100A — voided, trustee taxed at top rate |
| Division 7A non-complying loans | Deemed unfranked dividend |
| Non-commercial losses claimed without meeting 4 tests | Loss quarantined, amended assessment |
| Large work-related deductions vs income | Risk of audit |
| Wash sales around 30 June | CGT loss disallowed |
| Artificial income splitting via interposed entities | Part IVA application |
| Personal services income (PSI) through company or trust | PSI rules attribute income back to individual (Div 86–87) |
| Excessive salary sacrifice to reduce Division 293 exposure | ATO scrutiny, potential SG shortfall |
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
| January | Superannuation guarantee due (Q2). Review Division 7A loan repayments |
| February–March | Lodge Q2 BAS. Model year-end tax position. Begin pre-30 June planning |
| April–May | Execute prepayment strategies. Make concessional super contributions. Review asset purchases for instant write-off |
| June (before 30 June) | **Critical month.** Finalise trust distribution resolutions. Make super contributions (allow processing time — contribute by ~25 June). Prepay expenses. Realise capital losses. Lodge PAYG variation if needed |

## Section 12 — Cash Impact Examples

### Example 1 — Sole Trader Incorporates

**Before:** Sole trader, $180,000 net profit. Tax: ~$51,067 + $3,600 Medicare = $54,667.

**After:** Pty Ltd, pays $80,000 salary + $12,000 super. Retains $88,000 in company at 25% = $22,000 company tax. Personal tax on $80,000 salary: ~$16,788 + $1,600 Medicare = $18,388. **Total tax: $40,388. Saving: ~$14,279.**

### Example 2 — Maximising Super Contributions

Sole trader, $120,000 profit. Claims $30,000 concessional super contribution (deductible). Taxable income drops to $90,000. Tax saving at 30% marginal: $9,000 less 15% super tax ($4,500) = **net saving $4,500 + compounding in super environment.**

### Example 3 — Instant Asset Write-Off

Small business buys 3 laptops at $2,500 each and a vehicle at $18,000. Total: $25,500 immediately deductible (each asset <$20,000). At 30% marginal rate = **$7,650 cash saving in the year of purchase** vs multi-year depreciation.

### Example 4 — Negative Gearing Investment Property

Employee earns $120,000. Investment property: $25,000 rent less $35,000 expenses (interest, rates, depreciation) = $10,000 net loss. Taxable income: $110,000. Tax saving at 30% marginal: **$3,000 cash refund via PAYG variation.**

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
