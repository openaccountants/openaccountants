---
name: au-individual-return
description: Use this skill whenever asked about Australian individual income tax for sole traders. Trigger on phrases like "how much tax do I pay in Australia", "Australian tax return", "sole trader tax", "ABN tax", "Medicare levy", "LITO", "PAYG", "tax brackets Australia", "BAS", "instant asset write-off", "home office deduction", "HELP repayment", "HECS debt", "small business income tax offset", "motor vehicle deduction", or any question about filing or computing income tax for an Australian sole trader. Covers 2025–26 Stage 3 tax rates, Medicare levy and surcharge, LITO, business income computation, allowable deductions, depreciation, instant asset write-off, small business income tax offset, HELP/HECS repayments, and final tax computation. ALWAYS read this skill before touching any Australian income tax work.
version: 2.7
jurisdiction: AU
tax_year: 2025
tax_year_notes: "Retained for 2025-26 returns; use 2026-27 values only where expressly labelled and relevant to the requested year."
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# AU Individual Return

## AU Individual Return

## AU Individual Return

## Asset-threshold currency

- **Asset-threshold currency** -- For 2025–26, eligible small business entities using simplified depreciation can deduct assets costing less than $20,000 when first used or installed ready for taxable use. The permanent threshold was enacted on 26 August 2026; schedule 2 commences on 1 October 2026 and applies to specified first use or installation from 1 July 2026. The acquisition date alone does not establish the first-use year or a second deduction. Check prior claims and business use.  _([Tax Reform No. 2 Act 2026, schedule 2](https://www.legislation.gov.au/C2026A00071/asmade/text))_

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Detail |
| --- | --- |
| Country | Australia |
| Tax | Income tax + Medicare levy + HELP repayments (if applicable) |
| Currency | AUD only |
| Tax year | 1 July 2025 -- 30 June 2026 |
| Primary legislation | Income Tax Assessment Act 1997 (ITAA 1997); Income Tax Assessment Act 1936 (ITAA 1936) |
| Supporting legislation | Taxation Administration Act 1953; Medicare Levy Act 1986; Higher Education Support Act 2003 |
| Tax authority | Australian Taxation Office (ATO) |
| Filing portal | myTax (via myGov) or registered tax agent |
| Filing deadline | 2 November 2026 for standard self-lodgement (31 October is Saturday); tax-agent dates depend on the applicable programme |
| Contributor | Open Accountants Community |
| Skill version | 2.7 |

### Tax Rates -- Full-Year Resident Individual (2025-26, Stage 3) [T1]

Use this table for ordinary income of a full-year resident. If residency started or ended during the year, apply the [part-year tax-free threshold](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/adjustments/part-year-tax-free-threshold).

| Taxable Income (AUD) | Rate | Tax on This Band |
| --- | --- | --- |
| 0 -- 18,200 | 0% | Tax-free threshold |
| 18,201 -- 45,000 | 16% | Max $4,288 |
| 45,001 -- 135,000 | 30% | Max $27,000 |
| 135,001 -- 190,000 | 37% | Max $20,350 |
| 190,001+ | 45% |  |

### Medicare Levy [T1]

**Medicare Levy [T1]**

| Item | Value |
| --- | --- |
| Rate | 2% of taxable income |
| Low-income threshold (single) | $28,011 (no levy at or below this amount), with phase-in up to $35,013 for taxpayers without seniors and pensioners tax offset eligibility ([2026 Medicare levy](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026)) |
| Low-income threshold (family) | $47,238 + $4,338 per dependent child |
| Surcharge (no appropriate private hospital cover) | Single 2025–26 thresholds start above $101,000 of income for surcharge purposes, at 1% to 1.5%. Check family and part-year rules below ([2026 Medicare levy surcharge](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/medicare-and-private-health-insurance/medicare-levy-surcharge)) |

### Low Income Tax Offset (LITO) [T1]

The non-refundable LITO reduces income tax for eligible Australian resident individuals. Check entitlement before applying the table. [ATO low income tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset)

| Taxable Income (AUD) | LITO |
| --- | --- |
| Up to $37,500 | $700 |
| $37,501 -- $45,000 | $700 less 5c per $1 over $37,500 |
| $45,001 -- $66,667 | $325 less 1.5c per $1 over $45,000 |
| $66,668+ | $0 |

### Small Business Income Tax Offset (SBITO) [T1]

**Small Business Income Tax Offset (SBITO) [T1]**

| Item | Value |
| --- | --- |
| Rate | 16% of income tax on business income |
| Cap | $1,000 |
| Eligibility | An individual carrying on an eligible business as a sole trader, or with an eligible share of net small business income from a partnership or trust. The business must have aggregated turnover below $5 million ([ITAA 1997 Subdiv 328-F](https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_7/document_7.html)) |

For positive taxable income, multiply basic income tax by eligible net small business income divided by taxable income, limiting the fraction to 100%. Apply the 16% rate to that result, subject to the $1,000 annual cap. [ATO calculation and income conditions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/concessions-offsets-and-rebates/small-business-income-tax-offset)

### Key Deduction Rate Lookups

**Key Deduction Rate Lookups**

| Item | Rate/threshold | Claim handling |
| --- | --- | --- |
| Home office -- fixed rate method | 70 cents per hour (2024-25 and 2025-26) | T2 -- method choice, hours, and records/substantiation required |
| Motor vehicle -- cents per km method | 88 cents per km (max 5,000 km) | T2 -- method choice and business-km support required |
| Instant asset write-off (small business) | Eligible asset cost strictly less than $20,000; taxable-use deduction only | T1 only after eligibility, simplified-depreciation choices, first-use dates and cost are confirmed; otherwise escalate. [ITAA 1997, ss 328-180, 328-185 and 328-210](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html); [2025-26 thresholds, ITTPA s 328-180](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Superannuation (deductible personal contribution) | General concessional cap $30,000 in 2025–26 and $32,500 in 2026–27 | Count all concessional contributions. Apply the separate deduction rules, including a valid acknowledged notice and any applicable age conditions ([ATO concessional contributions cap](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap)) |

### Conservative Defaults [T1]

**Conservative Defaults [T1]**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | Establish residency before choosing rates or lodgment treatment |
| Unknown business-use percentage | Leave the amount out of the estimate until records support the business-use share |
| Unknown expense category | Confirm the expense and its purpose before assigning a label or deduction |
| Unknown depreciation effective life | Identify the asset and applicable date, then check the available statutory effective-life choices |
| Unknown private health insurance status | Verify qualifying hospital cover and dates before computing surcharge |
| Unknown aggregated turnover | Establish aggregated turnover before applying a small business concession |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full financial year (1 July to 30 June), confirmation of ABN/TFN, and whether the taxpayer is an Australian resident.

**Recommended** -- all tax invoices issued, purchase receipts, PAYG payment summaries or income statements (via myGov), prior year tax return, BAS lodgments.

**Receipts and substantiation (critical)** -- for deduction claims, keep written evidence (receipt or tax invoice) showing supplier name, cost, date, and nature of expense, plus records of business-use apportionment. A bank or credit-card statement alone is generally not sufficient evidence. Keep most business records for at least 5 years from the later of preparation or receipt of the record and completion of the relevant transaction or act. Apply longer periods where required for assets, losses, disputes and other exceptions. [ATO business record retention](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/record-keeping-for-business/detailed-business-record-keeping-requirements/running-your-business-records/income-tax-return-records-business)

**Ideal** -- complete bookkeeping records, depreciation schedule, motor vehicle logbook, home office hours log, private health insurance statement, HELP debt balance.

### Refusal Catalogue

- **R-AU-1 -- Companies and trusts** -- Companies lodge company tax returns. Trusts lodge trust returns. This skill covers individual sole traders only.  _(R-AU-1)_
- **R-AU-2 -- Non-residents** -- Non-resident tax rates and rules differ significantly. Out of scope.  _(R-AU-2)_
- **R-AU-3 -- Capital gains tax events** -- CGT events require specialised computation (cost base, discounts, exemptions). Out of scope.  _(R-AU-3)_
- **R-AU-4 -- Complex depreciation (effective life disputes)** -- Where the ATO effective life is contested or the asset has no published rate, escalate.  _(R-AU-4)_
- **R-AU-5 -- Partnership or PSI (Personal Services Income)** -- PSI rules and partnership allocations require separate analysis. Escalate.  _(R-AU-5)_

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

Use descriptions as reconciliation clues. Confirm the source and character of a payment before applying a return label.

| Pattern | Tax Label | Treatment | Notes |
| --- | --- | --- | --- |
| ABN INCOME, CLIENT PAYMENT, [client name] | Business income (Item P8) | Gross business income | Core sole trader income |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Revenue | Match to underlying invoices |
| PAYPAL TRANSFER | Business income | Revenue | Report gross before fees |
| DIRECT CREDIT [client name] | Business income | Revenue | Bank transfer from client |
| INTEREST, SAVINGS INTEREST | Interest income (item 10) | Report gross interest separately from P8 | Consider interest derived in the course of business when calculating net small business income for the offset |
| DIVIDEND, DISTRIBUTION | Check payment type | Use item 11 for reportable company dividends and item 13 for reportable partnership or trust distributions | Use the dividend or distribution statement, including eligible franking credits |
| FRANKING CREDIT | Gross-up dividend | Include eligible credits in assessable income and as a tax offset | Check applicable holding-period, related-payment and dividend washing rules ([ATO 2026 dividend instructions](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/income-questions-1-12-individual-tax-return-2026/11-dividends-2026)) |
| ATO REFUND, TAX REFUND | Check breakdown | Exclude the repayment of income tax | Check for separately assessable interest or a taxable recoupment |
| CENTRELINK, JOBSEEKER, YOUTH ALLOWANCE | Government payment (item 5 for JobSeeker and taxable Youth Allowance) | Check the particular payment and its tax status | Use item 6 for reportable government pensions and allowances listed there |
| SUPERANNUATION (lump sum or pension) | Item 7 or 8 | Check | Depends on age and components |
| OWN TRANSFER, SAVINGS | EXCLUDE | Internal | Between own accounts |
| RENTAL INCOME | Rental income (item 21) or business income | Use item 21 for rent outside a rental business | Identify whether the taxpayer carries on a business of renting property before choosing the label |

### 3.2 Expense Patterns (Debits on Bank Statement)

Verify the expense and its business purpose. Claim only the eligible business portion supported by records and check capital items under the applicable rules.

| Pattern | Deduction Category | Tier | Treatment |
| --- | --- | --- | --- |
| RENT, OFFICE RENT, SERVICED OFFICE | Business expense -- occupancy | T1 | Fully deductible if dedicated business premises |
| HOME OFFICE, WORK FROM HOME | Business home office expenses (P8) | T2 | Fixed rate 70c/hr (2024-25 and 2025-26) OR actual cost method. See Tier 2. |
| PETROL, FUEL, CALTEX, BP, SHELL, AMPOL | Business motor vehicle expenses (P8) | T2 | Cents/km (88c, max 5,000 km) OR logbook method |
| CAR INSURANCE, REGO, SERVICE | Motor vehicle | T2 | Use the business portion under the logbook method for a car or actual-cost method for another vehicle. The cents-per-kilometre method already covers these costs |
| TOLL, CITYLINK, LINKT | Motor vehicle or travel | T1 | Business travel tolls: deductible under either method |
| FLIGHT, QANTAS, VIRGIN, JETSTAR | Business travel (P8) | T1 | Apportion eligible fares for mixed business and private travel |
| ACCOMMODATION, HOTEL | Travel | T1 | Deductible if business travel with overnight stay |
| MEALS (business travel, overnight) | Travel | T1 | Reasonable amount while travelling overnight |
| MEALS (client entertainment) | Entertainment | T1 | Usually excluded under Division 32. Check specific statutory exceptions when facts support one |
| INSURANCE, PROFESSIONAL INDEMNITY | Business expense -- insurance | T1 | Check that the policy covers the business before claiming the eligible premium |
| INCOME PROTECTION INSURANCE | Other deductions (D15) | T1 | Claim eligible personally paid premiums for replacing assessable income. Exclude components covering injury, trauma, death or other capital benefits and premiums paid through super |
| ACCOUNTING, TAX AGENT, BAS AGENT | Tax affairs (D10) or business expense (P8) | T1 | Classify by the service supplied. Enter eligible tax-return or activity-statement work at D10 and business bookkeeping at P8. Tax advice must be from a recognised tax adviser |
| OFFICE SUPPLIES, OFFICEWORKS | Business expense | T1 | Verify business use and check the treatment of any capital item |
| SOFTWARE, SUBSCRIPTION, XERO, MYOB | Business expense -- IT | T1 | Claim the business portion of an eligible operating subscription and assess capital software separately |
| GOOGLE ADS, META ADS, FACEBOOK ADS | Business expense -- advertising | T1 | Verify that the advertising relates to the business before claiming |
| PHONE, TELSTRA, OPTUS, VODAFONE | Business expense -- telecom | T2 | Business portion only |
| INTERNET, NBN | Business expense -- telecom | T2 | Business portion only (or included in home office fixed-rate method) |
| TRAINING, COURSE, SELF-EDUCATION | Business training expenses (P8). Use D4 for eligible employment self-education only | T1 | Deductible if directly related to current income-producing activity. NOT deductible if for new career. |
| COMPUTER, LAPTOP, EQUIPMENT (under $20,000) | Potential instant asset write-off | T1 | Confirm eligibility, required simplified-depreciation choices and first taxable use; test full statutory cost, then deduct only the taxable-purpose amount. [ITAA 1997, ss 328-180, 328-185 and 328-210](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html); [2025-26 thresholds, ITTPA s 328-180](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| COMPUTER, LAPTOP, EQUIPMENT ($20,000 or more) | Small business pool or applicable depreciation regime | T1 | If simplified depreciation applies, allocate covered assets to its pool and check the low-pool-value rule; otherwise apply the relevant Division 40 rules. [ITAA 1997, ss 328-180, 328-185 and 328-210](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html); [2025-26 thresholds, ITTPA s 328-180](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| SUPER CONTRIBUTION, SUNSUPER, AUSTRALIAN SUPER | Personal super contributions (D12) | T1 | Deductible amount depends on statutory eligibility and a valid acknowledged notice. Check the separate concessional caps |
| ATO TAX, INCOME TAX, PAYG INSTALMENT | EXCLUDE | Not deductible | Tax payments are not deductions |
| GST PAYMENT, BAS PAYMENT | GST and other BAS amounts | T1 | Reconcile the BAS components. Exclude GST payable and remove input credits to which you are entitled when working out income tax |
| PRIVATE HEALTH, MEDIBANK, BUPA, NIB, HCF | MLS and private health insurance rebate | T1 | Premiums are private. Test appropriate hospital cover and the days the taxpayer and relevant dependants were covered |
| PERSONAL, GROCERY, ENTERTAINMENT | EXCLUDE | Not deductible | Personal expenses |
| DONATION, CHARITY, DGR | Gifts or donations (D9) | T1 | Check DGR status, evidence and whether the transfer is genuinely a gift. Eligible gifts made from 1 July 2024 can be below $2. Political gifts and fundraising contributions have separate rules. [ATO gifts and donations](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/gifts-and-donations) |

### 3.3 SaaS Subscriptions

**3.3 SaaS Subscriptions**

Classify subscription charges by the actual business use. The deductible operating expense is the business portion. Check separately for capital software and any amount already covered by the work-from-home fixed rate. [ATO small business guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE | Fully deductible business expense | Operating expense |
| SLACK, ZOOM, NOTION, FIGMA, GITHUB | Fully deductible | Same |
| AWS, HEROKU, DIGITAL OCEAN | Fully deductible | Hosting costs |
| CANVA (AU entity) | Fully deductible | Australian company |
| XERO, MYOB | Fully deductible (cost of managing tax affairs or business expense) | Accounting software |
| SPOTIFY, NETFLIX | NOT deductible | Personal entertainment |

### 3.4 Internal Transfers and Exclusions

**3.4 Internal Transfers and Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER, SAVINGS, TERM DEPOSIT | EXCLUDE | Internal movement |
| MORTGAGE, HOME LOAN | Exclude repayments of principal | Consider apportioning eligible mortgage interest as an occupancy expense only if the area is a place of business |
| ATM, CASH | T2 -- ask | Default exclude |
| HECS REPAYMENT, HELP | NOT a deduction | Compulsory repayment is not a tax deduction |

## Section 4 -- Worked Examples

### Example 1 -- Standard Sole Trader (Graphic Designer)

**Input:** ABN income AUD 92,000. Business expenses: software AUD 3,600, advertising AUD 1,200, accounting AUD 1,100, office supplies AUD 800. Home office 1,200 hours at 70c/hr. Car 4,000 business km at 88c/km. Assume all amounts are on the appropriate GST basis, the taxpayer is a full-year resident, the business qualifies for SBITO, records support the deductions and there is no Medicare levy exemption. No other income or HELP debt, no MLS and no other offsets or PAYG credits.

**Computation:**
- Business income: AUD 92,000
- Expenses: 3,600 + 1,200 + 1,100 + 800 = AUD 6,700
- Home office: 1,200 x 0.70 = AUD 840
- Motor vehicle: 4,000 x 0.88 = AUD 3,520
- Total deductions: 6,700 + 840 + 3,520 = AUD 11,060
- Taxable income: 92,000 - 11,060 = AUD 80,940
- Tax: 0 + 4,288 + (80,940 - 45,000) x 30% = 4,288 + 10,782 = AUD 15,070
- Medicare: 80,940 × 2% = AUD 1,618.80
- LITO: $0 (income > $66,667)
- SBITO: business is 100% of income, so 16% x 15,070
  gives AUD 2,411.20 of eligible small business income tax offset, capped at AUD 1,000
- Estimated tax and levy: AUD 15,070 − 1,000 + 1,618.80 = AUD 15,688.80

### Example 2 -- Instant Asset Write-Off

**Input:** Small business entity (turnover < $10M). Purchases laptop AUD 2,800 and monitor AUD 950. Both under $20,000.

**Classification:** Both items are immediately deductible under the instant asset write-off. Assuming both assets were first used for business in 2025–26, are wholly business-use, qualify for simplified depreciation and were not previously deducted, the total deduction is AUD 3,750. Record the first-use date and prior-claim check in the asset register.

### Example 3 -- Motor Vehicle (Logbook vs Cents/Km)

**Input:** Total km: 20,000. Business km: 12,000 (60%). Car costs: fuel AUD 4,800, insurance AUD 1,600, rego AUD 800, service AUD 1,200, depreciation AUD 4,000. Total AUD 12,400.

**Computation:**
- Cents/km: min(12,000, 5,000) x $0.88 = AUD 4,400 (capped at 5,000 km)
- Logbook: 12,400 x 60% = AUD 7,440
- The logbook method gives the larger deduction if the car is eligible and the business-use percentage and costs are supported. If a new logbook is required, keep it for at least 12 continuous representative weeks.
- [T2] Flag: confirm logbook exists and is valid.

### Example 4 -- Home Office (Fixed Rate vs Actual)

**Input:** Works from home 1,600 recorded hours a year. The taxpayer uses a home office covering one-quarter of the home. They have $2,400 in annual electricity bills and records that support $600 in additional business electricity. Usage records separately establish 80% business use for $1,200 of internet and $960 of phone costs. Calculate $400 of eligible business furniture decline in value.

**Computation:**
- Fixed rate: 1,600 x $0.70 = AUD 1,120 (covers electricity, gas, phone, internet, stationery, computer consumables)
- Actual cost: $600 of additional business electricity + $960 internet ($1,200 × 80%) + $768 phone ($960 × 80%) + $400 furniture decline in value = $2,728. Use business energy consumption and tariff records to establish the $600.
- Fixed rate plus eligible furniture decline in value is $1,520. On these facts the actual method gives $1,208 more.
- The fixed rate can be combined with eligible decline in value and other expenses it does not cover, such as qualifying cleaning. Separately test occupancy costs under the place-of-business rules. [ATO home-based business guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-home-based-business-expenses/home-based-business-expenses-sole-trader-or-partnership)
- [T2] Flag: confirm method choice and occupancy costs if actual.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Business Income [T1]

- **Business income treatment** -- Include ordinary and statutory business income in the year derived or otherwise assessable. Exclude GST payable on taxable supplies under ITAA 1997 s 17-5.

### 5.2 General Deduction [T1]

- **General deduction** -- A deduction for any loss or outgoing to the extent it is incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business. Must not be private, domestic, or capital in nature.  _(ITAA 1997 s8-1)_

### 5.3 Depreciation [T1]

- **Diminishing value** -- Base value × (qualifying days / 365) × (applicable 150% or 200% factor / effective life). For general Division 40 depreciation, use 150% for assets held before 10 May 2006 and generally 200% for assets first held on or after that date. Check reacquisition, rollover and other special rules before choosing the factor. Apply the statutory base value, qualifying days divided by 365, taxable-use adjustment and decline limits. Prime cost uses its separate cost/effective-life formula, with adjustments where required. These are tax calculations, separate from accounting depreciation. [ITAA 1997, ss 40-25, 40-70, 40-72 and 40-75](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).
- **Prime cost (straight line)** -- Cost × (qualifying days / 365) × (100% / effective life), subject to statutory adjustments and limits. Count days from start time for which the asset was used or installed ready for use. _(ITAA 1997 ss 40-60 and 40-75)_
- **Small business entity simplified depreciation** -- Eligible entities choosing Subdivision 328-D generally pool covered assets not individually deductible under s 328-180, including assets costing exactly $20,000. Apply the taxable-use, ordinary pool-rate and low-pool-value rules below.
- **Instant asset write-off** -- Assets costing less than $20,000 (assets first used or installed ready for use 1 July 2023 to 30 June 2026; extension made law by the Treasury Laws Amendment (Strengthening Financial Systems and Other Measures) Act 2025) can be immediately deducted by small business entities. For later first use, apply the enacted permanent threshold and commencement details in Asset-threshold currency above.  _(ITAA 1997 s 328-180)_

#### Simplified depreciation rules

To enter simplified depreciation or claim an individual new-asset deduction, confirm the eligibility and choice conditions in Subdivision 328-D. An existing general small business pool continues under that Subdivision for the year and later years even if the entity is no longer a small business entity or does not choose it for the year. New assets first used in such a year cannot be allocated to that pool until a year when the entity is eligible and chooses the Subdivision (s 328-220). For an individual asset deduction, confirm small business entity status and the required simplified-depreciation choice in both the year you started to hold the asset and the first taxable-use year (s 328-180(1)(a) and (ab)). Check first use or installation ready for taxable use, prior claims and statutory exclusions. Test the asset's full statutory cost, after applicable GST adjustments but before private-use apportionment, against the strict less-than-$20,000 threshold. The deduction is limited to taxable use. Covered assets not individually deductible under s 328-180 generally enter the small business pool; exactly $20,000 is included. General Division 40 rules apply when simplified depreciation does not apply or an exception requires them.

For ordinary pool depreciation, use 30% of the opening pool balance and 15% of the taxable-purpose adjustable value of assets first used or installed ready for taxable use during the year; relevant later cost additions have their own 15% rule. Do not assign 15% merely because a previously used asset enters the opening pool. First check s 328-210: opening pool balance plus taxable-purpose new-asset amounts and cost additions, less relevant taxable-purpose termination values, with the statutory adjustments. If that amount is more than zero and less than $20,000, deduct it instead of ordinary pool depreciation and close the pool at zero. Test before ordinary depreciation, not against the smaller closing balance after it. Check exclusions and special rules, including assets outside Division 40, relevant primary-production assets, leases and existing pools. [ITAA 1997, ss 328-175 to 328-220](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html).

For the temporary 2025-26 asset threshold, you must also have first acquired the asset at or after 7.30 pm ACT time on 12 May 2015. The temporary asset threshold and pool threshold are supported by [ITTPA 1997, s 328-180(4)(d) and (6)(e)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html); check the acquisition and first-use conditions. For later first use and pool assessments, apply the permanent threshold's specific application rules in [Tax Reform No. 2 Act 2026, schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text).

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

#### Worked general depreciation checks

Assume eligible, unpooled assets, correctly established costs/base values and effective lives, valid method choices and no special rule or cap changing the results.

For 2 assets with a $1,000 base value, a 25-year effective life and 365 qualifying days, the pre-10 May 2006 factor gives $60 decline and the ordinary later-acquisition factor gives $80. At 80% taxable use, estimated deductions are $48 and $64.

```oa-check
name: Acquisition date changes the general diminishing-value factor
inputs:
  base_value: 1000
  effective_life: 25
  qualifying_days: 365
  legacy_factor_percent: 150
  later_factor_percent: 200
  taxable_use_percent: 80
steps:
  - legacy_decline: pct(base_value, legacy_factor_percent) / effective_life * qualifying_days / 365
  - later_decline: pct(base_value, later_factor_percent) / effective_life * qualifying_days / 365
  - legacy_deduction: pct(legacy_decline, taxable_use_percent)
  - later_deduction: pct(later_decline, taxable_use_percent)
expected:
  legacy_decline: 60
  later_decline: 80
  legacy_deduction: 48
  later_deduction: 64
```

As a separate first-year prime-cost example, cost is $1,825, effective life is 5 years and there are 100 qualifying days. Decline is $100; at 80% taxable use the estimated deduction is $80. [ITAA 1997, ss 40-25, 40-70, 40-72 and 40-75](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

```oa-check
name: Prime cost uses cost and qualifying days before taxable-use apportionment
inputs:
  cost: 1825
  effective_life: 5
  qualifying_days: 100
  taxable_use_percent: 80
steps:
  - decline: cost / effective_life * qualifying_days / 365
  - deduction: pct(decline, taxable_use_percent)
expected:
  decline: 100
  deduction: 80
```

### 5.4 Superannuation [T1]

- **Personal deductible super contributions** -- The general concessional cap is $30,000 in 2025–26 and $32,500 in 2026–27. It includes employer and deductible personal contributions, and carry-forward rules can increase an individual's cap. Apply the deduction rules separately. Give the fund a valid notice by the earlier of lodging the contribution year's return and the end of the next income year. Receive its acknowledgement before claiming. Check whether the fund still holds the contribution, any rollover or withdrawal and applicable age conditions. [ATO personal contributions](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/how-to-save-more-in-your-super/personal-super-contributions) and [ATO concessional cap](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap).

### 5.5 HELP/HECS Repayment [T1]

Use the 2025-26 thresholds for this return workflow. Use the separately labelled 2026-27 thresholds only for that requested year. The following is the domestic compulsory-repayment calculation for a person liable under section 154-1, with a HELP debt on the relevant 1 June. The family Medicare-levy reduction or exemption in section 154-1(2), referring specifically to section 8 of the Medicare Levy Act, can remove that liability. Do not treat every Medicare exemption as a HELP exemption. Foreign residents may also have an overseas levy based on assessed worldwide income under sections 154-16, 154-17 and 154-32. [Higher Education Support Act 2003, ss 154-1 to 154-20 and 154-32](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html).

**Repayment income.** Start with taxable income, disregarding the assessable FHSS released amount. Add total net investment losses, the applicable reportable fringe benefits total, exempt foreign income as defined in section 154-5 and reportable superannuation contributions. For this purpose, exempt foreign income is net income exempt under ITAA 1936 section 23AF or 23AG, with capital losses and outgoings disregarded. HELP repayments are not deductible. [Higher Education Support Act 2003, s 154-5](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html).

| Income year | Minimum repayment income | Second threshold | Source |
| --- | ---: | ---: | --- |
| 2025-26 | $67,000 | $125,000 | [HESA ss 154-10 and 154-20](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html) |
| 2026-27 | $69,528 | $129,717 | [2026-27 indexation notice, entries for ss 154-10 and 154-20](https://www.legislation.gov.au/C2026G00249/asmade/2026-04-21/text/original/pdf) |

**Calculation for both years.** Calculate 15% of repayment income above the minimum up to the second threshold, plus 17% of repayment income above the second threshold. The compulsory repayment is the least of that marginal sum, 10% of total repayment income and the repayable debt for the income year. Determine that debt under section 154-15, allowing for relevant payments and amounts already assessed. At or below the minimum, there is no domestic compulsory repayment. Do not use the former whole-income percentage scale. [HESA ss 154-1, 154-15 and 154-20](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html).

The first slice reaches $8,700 in 2025-26 and $9,028.35 in 2026-27. Retain the statutory arithmetic before any applicable assessment rounding; the displayed $9,028 shorthand is not the exact 2026-27 first-slice amount. The 10% cap first becomes smaller than the marginal sum at whole-dollar repayment income of $179,286 in 2025-26 and $186,051 in 2026-27. [HESA ss 154-20 and 154-25](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html) and [2026-27 notice](https://www.legislation.gov.au/C2026G00249/asmade/2026-04-21/text/original/pdf).

**Worked example: repayment-income adjustments, 2025-26.** A resident has $70,000 taxable income including a $10,000 assessable FHSS released amount and $15,000 net section 23AG exempt foreign income. There are no other additions, no section 154-1(2) relief and $20,000 repayable debt. Repayment income is $75,000 and the compulsory repayment before assessment rounding is $1,200.

```oa-check
name: HELP repayment income excludes FHSS and adds defined exempt foreign income
inputs:
  taxable_income: 70000
  assessable_fhss: 10000
  net_exempt_foreign_income: 15000
  minimum: 67000
  second_threshold: 125000
  repayable_debt: 20000
steps:
  - repayment_income: taxable_income - assessable_fhss + net_exempt_foreign_income
  - marginal_sum: pct(max(min(repayment_income, second_threshold) - minimum, 0), 15) + pct(max(repayment_income - second_threshold, 0), 17)
  - compulsory_repayment: min(marginal_sum, pct(repayment_income, 10), repayable_debt)
expected:
  repayment_income: 75000
  marginal_sum: 1200
  compulsory_repayment: 1200
```

**Worked example: debt cap, 2026-27.** A liable resident has repayment income of $150,000 and $50 repayable debt, with no section 154-1(2) relief. The marginal sum is $12,476.46, the 10% cap is $15,000 and the debt cap limits the repayment to $50.

```oa-check
name: HELP 2026-27 exact first slice and repayable debt cap
inputs:
  repayment_income: 150000
  minimum: 69528
  second_threshold: 129717
  repayable_debt: 50
steps:
  - first_slice: pct(second_threshold - minimum, 15)
  - marginal_sum: first_slice + pct(repayment_income - second_threshold, 17)
  - ten_percent_cap: pct(repayment_income, 10)
  - compulsory_repayment: min(marginal_sum, ten_percent_cap, repayable_debt)
expected:
  first_slice: 9028.35
  marginal_sum: 12476.46
  ten_percent_cap: 15000
  compulsory_repayment: 50
```

**Worked example: income cap, 2026-27.** A liable resident has repayment income of $186,051 and $50,000 repayable debt, with no section 154-1(2) relief. The marginal sum is $18,605.13. The 10% cap reduces the compulsory repayment before assessment rounding to $18,605.10.

```oa-check
name: HELP 2026-27 total income cap at its first whole-dollar boundary
inputs:
  repayment_income: 186051
  minimum: 69528
  second_threshold: 129717
  repayable_debt: 50000
steps:
  - marginal_sum: pct(second_threshold - minimum, 15) + pct(repayment_income - second_threshold, 17)
  - ten_percent_cap: pct(repayment_income, 10)
  - compulsory_repayment: min(marginal_sum, ten_percent_cap, repayable_debt)
expected:
  marginal_sum: 18605.13
  ten_percent_cap: 18605.10
  compulsory_repayment: 18605.10
```

### 5.6 Filing and Penalties [T1]

**5.6 Filing and Penalties [T1]**

| Item | Value |
| --- | --- |
| Self-lodge deadline | 2 November 2026 (31 October is Saturday; check extensions) |
| Tax agent deadline | Check the client's recorded due date and applicable program. Dates depend on lodgment history, client circumstances and concessions, including some earlier deadlines and the 5 June concession ([ATO agent lodgment due dates](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/individuals-and-trusts)) |
| Failure to lodge on time | $364 per 28-day period or part, up to five base units ($1,820, derived: 5 x $364) for the applicable period from 1 July 2026; apply relevant multipliers and remission rules. [Crimes (Amount of a Penalty Unit) Instrument 2026](https://www.legislation.gov.au/F2026N00424/asmade/2026-06-15/text/original/pdf); [ATO FTL penalty](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty) |
| Shortfall penalty (reasonable care not taken) | Base rate 25% of the shortfall or affected part ([ATO statement penalties](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements)) |
| Shortfall penalty (recklessness) | Base rate 50% of the shortfall or affected part ([ATO statement penalties](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements)) |
| General Interest Charge (GIC) | Rate set quarterly and published on the ATO website; calculated daily and compounded |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office [T2]

**6.1 Home Office [T2] methods table**

| Method | What It Covers | Additional Claims |
| --- | --- | --- |
| Fixed rate (70c/hr, 2024-25 and 2025-26) | Electricity, gas, phone, internet, stationery, computer consumables | Separately consider eligible decline in value, cleaning and occupancy expenses where the place-of-business test is met |
| Actual cost | Each expense claimed individually at actual business % | No fixed rate component |

- **Home office records and occupancy expenses** -- For the fixed rate, keep contemporaneous records of actual business hours worked from home and evidence of each covered expense incurred. For actual costs, keep bills and evidence of additional business use and apportionment. To claim occupancy costs, establish that the area has the character of a place of business. Consider suitability for domestic use, use by clients, other premises and the extent of business use. Apportion qualifying rent, mortgage interest, rates, home insurance or land tax over the area and period used for business. [ATO home-based business guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-home-based-business-expenses/home-based-business-expenses-sole-trader-or-partnership)

### 6.2 Motor Vehicle [T2]

**6.2 Motor Vehicle [T2] methods table**

| Method | How It Works | Records |
| --- | --- | --- |
| Cents per km (88c in 2025–26) | Maximum 5,000 business kilometres per eligible car. Expense receipts are unnecessary for this method | Keep a reasonable, explainable calculation of business kilometres |
| Logbook | Business % of eligible actual costs and decline in value | Representative logbook for at least 12 consecutive weeks. It can generally be used for up to 5 income years. Retain odometer and expense records and adjust for changes in use |

- Choose one method for each eligible car per income year. For other vehicles, use documented actual business costs. Eligible business parking and tolls can be separate deductions. The cents-per-kilometre rate already covers roadside assistance. [ATO motor vehicle methods](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-motor-vehicle-expenses/motor-vehicle-expense-calculation-methods)

### 6.3 Private Health Insurance (Medicare Levy Surcharge) [T2]

- **MLS applicability** -- Apply the 2025–26 thresholds to income for surcharge purposes. Check family circumstances, any reduced-income exception and how many days the taxpayer and relevant dependants lacked appropriate private hospital cover or an exemption. The rate applies to the statutory surcharge base. [ATO 2026 MLS instructions](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/medicare-and-private-health-insurance/medicare-levy-surcharge)

**MLS Rate table**

| Income | MLS Rate |
| --- | --- |
| $101,001 -- $118,000 | 1% |
| $118,001 -- $158,000 | 1.25% |
| $158,001+ | 1.5% |

The 2025–26 family base threshold is $202,000. The next tier boundaries are $236,000 and $316,000. Increase each by $1,500 per dependent child after the first. An appropriate policy is registered Australian private hospital cover with excess no more than $750 for single cover or $1,500 otherwise.

- **PHI rebate** -- PHI rebate: income-tested offset that reduces PHI premiums. Claimed via reduced premiums or tax offset. Confirm PHI status and income level.

### 6.4 Personal Services Income (PSI) [T2]

- **PSI rules** -- If income is mainly a reward for personal efforts/skills and not from conducting a personal services business, PSI rules limit deductions. Cannot claim rent, mortgage interest, certain home office costs against PSI. For self-assessment as a personal services business, the results test must be met for at least 75% of PSI. Otherwise the unrelated clients, employment or business premises test can support self-assessment only if less than 80% of PSI comes from the same entity and its associates. Check whether a determination applies if self-assessment is unavailable. [ATO personal services business tests](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/personal-services-income/working-out-if-the-psi-rules-apply/self-assessing-as-a-psb)

## Section 7 -- Excel Working Paper Template

```
AUSTRALIAN INDIVIDUAL TAX RETURN -- Working Paper
Tax Year: 2025-26

A. INCOME
  A1. Business income (ABN income)                 ___________
  A2. Employment income (per income statement)     ___________
  A3. Interest income                              ___________
  A4. Dividend income (grossed up with franking)   ___________
  A5. Rental income (net)                          ___________
  A6. Other income                                 ___________
  A7. TOTAL ASSESSABLE INCOME                      ___________

B. DEDUCTIONS
  B1. Business expenses (direct)                   ___________
  B2. Home office (70c/hr or actual)               ___________
  B3. Motor vehicle (88c/km or logbook)            ___________
  B4. Travel (flights, accommodation)              ___________
  B5. Self-education                               ___________
  B6. Depreciation / instant asset write-off       ___________
  B7. Personal super contributions                 ___________
  B8. Income protection insurance                  ___________
  B9. Cost of managing tax affairs                 ___________
  B10. Donations (DGR)                             ___________
  B11. Other deductions                            ___________
  B12. TOTAL DEDUCTIONS                            ___________

C. TAXABLE INCOME (A7 - B12)                       ___________

D. TAX COMPUTATION
  D1. Tax on taxable income (Stage 3 rates)        ___________
  D2. Medicare levy (2%)                           ___________
  D3. Medicare levy surcharge (if applicable)      ___________
  D4. HELP/HECS repayment (if applicable)          ___________
  D5. Other liabilities subtotal (D2 + D3 + D4)   ___________
  D6. Less: LITO                                   ___________
  D7. Less: SBITO (16%, max $1,000)                ___________
  D8. Less: Franking credits offset                ___________
  D9. Less: PHI rebate offset                      ___________
  D10. Less: PAYG instalment credit               ___________
  D11. Less: PAYG withholding (employment)         ___________
  D12. TAX DUE / (REFUND)                          ___________

Apply non-refundable offsets against eligible income tax first. Add other liabilities and apply refundable credits and applicable PAYG credits. Reconcile PAYG instalment credits to the assessment and activity statements.

REVIEWER FLAGS:
  [ ] Residency status confirmed?
  [ ] Home office method and hours verified?
  [ ] Motor vehicle method confirmed?
  [ ] Instant asset write-off eligibility (SBE < $10M)?
  [ ] Super contribution notice of intent lodged?
  [ ] PHI status confirmed (MLS)?
  [ ] HELP debt status confirmed?
  [ ] All T2 items flagged?
```

## Section 8 -- Bank Statement Reading Guide

### Australian Bank Statement Formats

**Australian Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| CBA, ANZ, Westpac, NAB | CSV, PDF | Date, Description, Debit, Credit, Balance |
| Macquarie, Suncorp, Bendigo | CSV | Date, Narrative, Amount |
| Up, ING, Ubank | CSV | Date, Description, Amount |
| Wise, Revolut | CSV | Date, Description, Amount, Currency |

### Key Australian Banking Terms

**Key Australian Banking Terms**

| Term | Classification Hint |
| --- | --- |
| Direct Credit | Incoming payment -- could be income |
| Direct Debit | Regular outgoing -- likely expense |
| EFTPOS | Point-of-sale purchase |
| BPAY | Bill payment |
| Osko / PayID | Fast payment -- check direction |
| ATM | Cash withdrawal -- ask purpose |
| Interest Paid | Income -- report separately |
| Dividend | Income -- check franking |

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- AUSTRALIA INDIVIDUAL RETURN
1. Are you an Australian resident for tax purposes?
2. Do you have an active ABN and TFN?
3. Are you registered for GST?
4. What is your aggregated turnover? (for small business concessions)
5. Do you work from home? How many hours per year? Method preference (70c or actual)?
6. Do you use a vehicle for business? Method preference (cents/km or logbook)?
7. Any assets purchased this year? Cost?
8. Do you have private health insurance? Full year?
9. Do you have a HELP/HECS debt?
10. Are you also employed (PAYG income)?
11. Any personal super contributions made?
12. Prior year tax return / depreciation schedule available?
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**  _(ITAA 1997; Medicare Levy Act 1986; Higher Education Support Act 2003)_

| Topic | Reference |
| --- | --- |
| Assessable income | ITAA 1997 s6-1, s6-5 |
| General deduction | ITAA 1997 s8-1 |
| Capital vs revenue | ITAA 1997 s8-1(2)(a) |
| Depreciation | ITAA 1997 Div 40 |
| Small business entity | ITAA 1997 Div 328 |
| Instant asset write-off | ITAA 1997 s328-180 |
| Home office | ATO Practical Compliance Guideline PCG 2023/1 |
| Motor vehicle | ITAA 1997 s28-13, s28-15; cents-per-km rate set by Income Tax Assessment (Cents per Kilometre Deduction Rate for Car Expenses) Determination 2024 (F2024L00697): 88c for 2024-25 and 2025-26 |
| Superannuation deduction | ITAA 1997 Div 290 |
| Medicare levy | Medicare Levy Act 1986 |
| HELP repayments | Higher Education Support Act 2003 |
| LITO | ITAA 1997 ss 61-110 and 61-115 |
| SBITO | ITAA 1997 ss 328-355 to 328-375 |

### Interaction with GST [T1]

**Interaction with GST [T1]**

| Scenario | Income Tax Treatment |
| --- | --- |
| GST payable on taxable supplies | Exclude the GST payable from assessable income under Division 17 |
| Input tax credits | Reduce the income tax deduction or statutory asset cost by the credits to which you are entitled |
| Neither registered nor required to register for GST | Use gross figures where there is no GST payable or input tax credit entitlement |
| GST on private portion | Exclude the private amount from the deduction. Determine entitlement and statutory asset cost before applying any required taxable-use apportionment |

## PROHIBITIONS

- NEVER allow private or domestic expenses as business deductions
- Check Division 32 before deducting entertainment expenses. Apply an exception only if its requirements are met.
- NEVER claim more than 5,000 km under the cents-per-km method
- Claim eligible home occupancy expenses only to the extent they relate to a place of business.
- NEVER forget to lodge notice of intent for personal super contributions
- NEVER claim HELP repayments as a deduction
- NEVER claim private health insurance premiums as a deduction
- NEVER apply the instant asset write-off without confirming small business entity status
- NEVER include income tax or GST payments as business deductions
- Apply Divisions 17 and 27 to GST payable and eligible input tax credits.
- NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or registered tax agent in your jurisdiction) before filing or acting upon.

> [Contributor history](https://github.com/openaccountants/openaccountants/commits/fc090e8e95bae53674c2df8398b218b0c528a7c3/skills/australia/au-individual-return.md).

## Sources

Transaction labels, deductions, part-year residency, SBITO and PSI conditions rechecked on 2026-11-27. The rate and lodgment evidence below records its original read date.

- [Income Tax Rates Act 1986, Schedule 7](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [2026 Medicare levy](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026). (read 2026-11-22)
- [Small business income tax offset, Subdivision 328-F](https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_7/document_7.html) and [2026 Medicare levy surcharge](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/medicare-and-private-health-insurance/medicare-levy-surcharge). (read 2026-11-22)
- [2026 business schedule P8](https://www.ato.gov.au/api/public/content/d4e347b76aca4585a9fd567df1931c8e?v=80e95725), [government payments](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/income-questions-1-12-individual-tax-return-2026/5-australian-government-allowances-and-payments-2026), [tax affairs costs](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/deduction-questions-d1-d10-individual-tax-return-2026/d10-cost-of-managing-tax-affairs-2026) and [other deductions](https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/deduction-questions-d11-d15-supplementary-tax-return-2026/d15-other-deductions-not-claimable-elsewhere-in-your-tax-return-2026). (read 2026-11-22)
- [ATO home-based businesses](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-home-based-business-expenses/home-based-business-expenses-sole-trader-or-partnership), [actual method](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/actual-cost-method) and [fixed rate record keeping](https://www.ato.gov.au/Individuals/Income-deductions-offsets-and-records/Deductions-you-can-claim/Working-from-home-expenses/Fixed-rate-method---67-cents/?anchor=Recordkeepingforthefixedratemethod). (read 2026-11-22)
- [ATO business records](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/record-keeping-for-business/detailed-business-record-keeping-requirements/running-your-business-records/income-tax-return-records-business), [agent lodgment](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/individuals-and-trusts) and [tax estimate](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/mytax-2026-estimate). (read 2026-11-22)
- [ATO gifts and donations](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/gifts-and-donations) and [ITAA 1997 s 30-15](https://www.legislation.gov.au/C2004A05138/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html). (read 2026-11-22)
- [Taxation Administration Act 1953, Schedule 1 s 45-30](https://www.legislation.gov.au/C1953A00001/2026-05-21/2026-05-21/text/original/epub/OEBPS/document_2/document_2.html) and [ITAA 1997, Divisions 17, 27 and 32](https://www.legislation.gov.au/C2004A05138/2026-06-27/2026-06-27/text/original/pdf/1). (read 2026-11-22)

Read 2026-11-12 for the depreciation correction:

- [ITAA 1997, ss 40-25, 40-70, 40-72, 40-75 and 40-95](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html): eligibility, date-specific factors, formulas and effective-life selection. Selected sections of retained current compilation 268 read 2026-11-12.
- [Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025, Schedule 2](https://www.legislation.gov.au/F2025L01097/asmade/text): asset-specific Table A and Table B lives; select the applicable dated determination. Selected Table A/Table B categories read 2026-11-12.

- [ITAA 1997, ss 328-175, 328-180, 328-185, 328-190, 328-210 and 328-220](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) -- read 2026-11-12 for selected simplified-depreciation eligibility, cost, allocation, rates, low-pool-value and continuing-pool rules.
- [ITTPA 1997, s 328-180(4)(d) and (6)(e)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) -- read 2026-11-12 for the temporary 2025-26 asset and pool thresholds.
- [Tax Reform No. 2 Act 2026, schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text) -- read 2026-11-12 for the permanent threshold application from July 2026.

- [Higher Education Support Act 2003, ss 154-1, 154-5, 154-10, 154-15, 154-20, 154-25 and 154-32](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html) and [2026-27 indexation notice](https://www.legislation.gov.au/C2026G00249/asmade/2026-04-21/text/original/pdf) -- selected HELP liability, income, thresholds and caps read 2026-11-12.

Not yet confirmed: the meaning of an unidentified bank entry. Use the underlying documents to classify it. If the treatment remains uncertain, say ‘Check this point with one of our partner accountants.’
