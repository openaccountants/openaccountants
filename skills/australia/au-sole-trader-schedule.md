---
name: au-sole-trader-schedule
description: Australian sole trader business schedule (Business and Professional Items Schedule for Individuals). Covers assessable business income, allowable deductions, home office (fixed rate 70c/hour or actual), motor vehicle (logbook or cents per km at 88c/km), depreciation (instant asset write-off, simplified pooling, general pooling), prepaid expenses, and trading stock.
version: 1.6
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

# AU Sole Trader Schedule

## AU Sole Trader Schedule

## Australia Sole Trader Business Schedule v1.6

## What this file is

**Obligation category:** IT (Income Tax)
**Functional role:** Bookkeeping + Computation
**Status:** Complete

This file covers the Business and Professional Items (BPI) schedule that sole traders attach to their individual income tax return. The BPI schedule feeds into the individual return at "Business income or loss" items.

**Tax year coverage:** This skill targets the 2025–26 income year (1 July 2025 to 30 June 2026). Match the intake and assembly year before calculating.

This workflow prepares working papers and a brief for a credentialed reviewer. A sole trader
can lodge their own return or use a registered tax agent. [ATO, Business, partnership and trust
income](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/income-you-must-declare/business-partnership-and-trust-income).

## Section 1 -- Scope statement

This skill covers:

- **Form:** Business and professional items schedule for individuals 2026
- **Entity types:** Sole proprietors operating a business or profession in their individual capacity
- The applicable items on the issued 2026 schedule, including the P21 trading stock election. [ATO 2026 BPI instructions](https://www.ato.gov.au/forms-and-instructions/business-and-professional-items-schedule-2026-instructions/instructions-to-complete-the-bpi-schedule-2026).

This skill does NOT cover:

- Partnerships (use partnership schedule)
- Companies, trusts, or superannuation funds
- Primary production-specific items (though basic rules noted)
- Personal services income (PSI) determinations in detail -- flag for reviewer

## Section 2 -- Filing requirements

### 2.1 Who must lodge

- **Who must lodge** -- Any individual who carried on a business as a sole trader during the income year. Even if the business made a loss, the schedule must be lodged.  _(ITAA 1997 s 4-15, ATO instructions for BPI schedule)_

### 2.2 Due dates

**Due dates**

| Lodgement type | Due date |
| --- | --- |
| Self-lodgers | 2 November 2026 (31 October falls on Saturday; check applicable extensions) |
| Tax agent lodgement | Per the ATO tax agent lodgement programme (2026–27 programme, depending on client category) |

### 2.3 ABN requirement

- **ABN requirement:** Check ABN entitlement, GST registration and withholding consequences separately. An ABN is not compulsory for every business activity. A tax invoice must meet GST requirements, and eligible payments without an ABN can attract 47% withholding subject to exceptions. [ABR](https://www.abr.gov.au/business-super-funds-charities/applying-abn/abn-entitlement).

## Section 3 -- Rates and thresholds

**Rates and thresholds**  _(ITAA 1997 Div 328; [ATO simplified depreciation guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business))_

| Item | Amount / Rate | Source |
| --- | --- | --- |
| Instant asset write-off threshold | For 2025–26, eligible small business entities using simplified depreciation can deduct assets costing less than $20,000 when first used or installed ready for taxable use. The permanent threshold was enacted on 26 August 2026; schedule 2 commences on 1 October 2026 and applies to specified first use or installation from 1 July 2026. [Tax Reform No. 2 Act 2026, schedule 2](https://www.legislation.gov.au/C2026A00071/asmade/text). | ITAA 1997 Subdivision 328-D |
| Small business entity threshold | Aggregated turnover < $10M | ITAA 1997 s 328-110 |
| Cents per km rate (motor vehicle) | 88 cents per km (2024-25 and 2025-26); 91 cents (2026-27) | ATO cents per kilometre method |
| Cents per km cap | 5,000 business km per car per year | ITAA 1997 s 28-25 |
| Home office fixed rate | 70 cents per hour for 2024–25 and 2025–26; 67 cents for 2022–23 and 2023–24. Check the published rate for 2026–27 before use. | [ATO fixed rate method](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method) |
| Trading stock threshold (change in value) | A qualifying business with aggregated turnover below $50 million can elect to skip a stocktake if its reasonable estimate of the opening-to-closing difference is $5,000 or less. | [ATO simplified trading stock rules](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/accounting-for-trading-stock/simplified-trading-stock-rules) |
| Prepaid expenses | Eligible businesses with aggregated turnover below $50 million can apply the 12-month rule to otherwise deductible prepayments. The eligible service period must be 12 months or less and end by the last day of the next income year. | [ATO deductions for prepaid expenses 2026](https://www.ato.gov.au/law/view/document?docid=SAV%2FDPE) |

- **Instant asset write-off threshold:** For 2025–26, eligible small business entities using simplified depreciation can deduct assets costing less than $20,000 when first used or installed ready for taxable use. The permanent threshold was enacted on 26 August 2026; schedule 2 commences on 1 October 2026 and applies to specified first use or installation from 1 July 2026. [Tax Reform No. 2 Act 2026, schedule 2](https://www.legislation.gov.au/C2026A00071/asmade/text).
- **Small business entity threshold** -- Aggregated turnover < $10M  _(ITAA 1997 s 328-110)_
- **Cents per km rate (motor vehicle)** -- 88 cents per km for 2024–25 and 2025–26; 91 cents per km for 2026–27. Check the applicable rate for later years. [ATO cents per kilometre method](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/cars-transport-and-travel/motor-vehicle-and-car-expenses/expenses-for-a-car-you-own-or-lease/cents-per-kilometre-method).
- **Cents per km cap** -- 5,000 business km per car per year  _(ITAA 1997 s 28-25)_
- **Home office fixed rate** -- 70 cents per hour for 2024–25 and 2025–26. Check the ATO's published rate for any other year.
- **Trading stock threshold (change in value):** Apply the same $5,000 test to eligible businesses with aggregated turnover below $50 million.
- **Prepaid expenses:** Apply the 12-month rule and check the exclusions in section 5.3.

## Section 4 -- Computation rules

### 4.1 Business income (P8)

- **Business income (P8)** -- Identify amounts derived in the year using the applicable receipts or earnings method. Include assessable sales, commissions, subsidies and insurance recoveries. Check whether a grant is exempt or non-assessable non-exempt, including any eligible COVID-19 support payments. Check specific income provisions for capital receipts, including business subsidies and depreciating-asset balancing adjustments. Apply the CGT rules where relevant and use the applicable return labels, including P1 when required for personal services income. [ATO TR 98/1](https://www.ato.gov.au/law/view/document?PiT=99991231235958&docid=TXR%2FTR981%2FNAT%2FATO%2F00001) · [ITAA 1997, ss 6-5, 15-10 and 20-20](https://www.legislation.gov.au/C2004A05138/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_1/document_1.html) · [ATO business income exclusions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/assessable-income/what-income-to-exclude).

### 4.2 Cost of sales / Cost of goods sold

- **Cost of goods sold**: Step 1. Opening stock + Purchases - Closing stock = Cost of goods sold. Step 2. Trading stock can be valued at cost, market selling value, or replacement value (ITAA 1997 s 70-45). The method can differ item by item. Step 3. If a qualifying business with aggregated turnover below $50 million reasonably estimates that year-end trading stock differs from opening stock by $5,000 or less (s 328-285), the taxpayer can elect to use the same value as opening stock (no stocktake required).  _(ITAA 1997 s 70-45)_ [ATO simplified trading stock rules](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/accounting-for-trading-stock/simplified-trading-stock-rules).

The P21 notification concerns an elected closing value below the lowest ordinary valuation under section 70-50. Enter Y at P21 label P when the election requires notice. [ATO 2026 P21 instructions](https://www.ato.gov.au/forms-and-instructions/business-and-professional-items-schedule-2026-instructions/instructions-to-complete-the-bpi-schedule-2026/trading-stock-election-p21).

### 4.3 Allowable deductions

- **General deduction provision** -- Deductions must satisfy the general deduction provision: incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business for that purpose. Losses and outgoings of a capital, private, or domestic nature are not deductible (subject to specific provisions).  _(ITAA 1997 s 8-1)_

**Key deduction categories on the schedule**

| Schedule area | Category | Notes |
| --- | --- | --- |
| P8 expenses | Motor vehicle expenses | Use the year-specific expense label and method |
| P8 expenses | Depreciation | Reconcile to the depreciation schedule |
| P8 expenses | Repairs and maintenance | Distinguish capital expenditure |
| P8 expenses | Interest | Use the correct domestic/overseas label and business portion |
| P8 expenses | Rent | Business premises; assess home occupancy separately |
| P8 expenses | Other expenses | Classify into specific P8 expense labels where available |

P9 records business loss activity details. P10 and later items request separate business information. Use the applicable labels in the [ATO 2026 BPI instructions](https://www.ato.gov.au/forms-and-instructions/business-and-professional-items-schedule-2026-instructions/instructions-to-complete-the-bpi-schedule-2026).

### 4.4 Motor vehicle expenses

Two methods are available for eligible cars an individual sole trader holds. Apply the actual business expenses rules for other vehicles.

#### Method 1 -- Cents per kilometre

- **Cents per kilometre method** -- Claim the current rate per business km, up to 5,000 km per car per year. 2025-26: 88c, maximum claim = 5,000 x $0.88 = $4,400 per car. 2026-27: 91c, maximum = $4,550. This rate includes all car expenses, including fuel and depreciation. No logbook or written evidence of individual trips required, but must be able to show how the estimate was calculated.  _(ATO cents per kilometre method; ITAA 1997 s 28-25)_

#### Method 2 -- Logbook

- **Logbook method** -- Keep a representative logbook for at least 12 continuous weeks or the entire holding period if the car was held for less than 12 weeks. Retain annual odometer and expense records. A representative logbook can generally be used for 5 income years. Estimate business kilometres and divide by total kilometres travelled whilst holding the car in the year. Apply that percentage to eligible car expenses. Where section 40-230 applies, reduce the adjusted first element of the cost of a car designed mainly to carry passengers to the car limit for the year you first held it if the cost exceeds the limit. The limits are $69,674 for 2024–25 and 2025–26 and $69,883 for 2026–27. [ITAA 1997, ss 28-90 to 28-125](https://www.legislation.gov.au/C2004A05138/2025-07-01/2025-07-01/text/original/epub/OEBPS/document_1/document_1.html) · [ITAA 1997, s 40-230](https://www.legislation.gov.au/C2004A05138/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_2/document_2.html) · [ATO 2026–27 car limits](https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/car-thresholds-from-1-july).

### 4.5 Depreciation

#### Small business simplified depreciation (if SBE)

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

#### General depreciation (non-SBE or election out of simplified)

- **General depreciation** -- Choose the applicable Commissioner-determined effective life under s 40-95 or a valid self-assessed life. Start at first use or installation ready for use, rather than automatically at purchase. For general Division 40 depreciation, use 150% for assets held before 10 May 2006 and generally 200% for assets first held on or after that date. Check reacquisition, rollover and other special rules before choosing the factor. Apply the statutory base value, qualifying days divided by 365, taxable-use adjustment and decline limits. Prime cost uses its separate cost/effective-life formula, with adjustments where required. These are tax calculations, separate from accounting depreciation. [ITAA 1997, ss 40-25, 40-70, 40-72 and 40-75](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html). [2025 effective-life determination, Schedule 2](https://www.legislation.gov.au/F2025L01097/asmade/text).

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

### 4.6 Home office expenses

#### Fixed rate method (70 cents per hour for 2025–26) -- PCG 2023/1

- **Fixed rate method** -- Covers energy expenses (electricity, gas), phone, internet, stationery and computer consumables. Do substantive business work from home, incur at least one covered running expense, record actual hours as you work and keep evidence for each type of covered expense incurred. The rate covers those expenses for the year. Do not also claim those costs separately. Claim qualifying occupancy expenses separately only when an area of the home is a place of business. [ATO guidance for sole traders working from home](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-home-based-business-expenses/home-based-business-expenses-sole-trader-or-partnership).

#### Actual cost method

- **Actual cost method** -- Work out each additional running expense incurred for business and keep records supporting its business portion. Use the actual usage or another reasonable basis for the particular expense, such as energy use and hours worked or the business share of phone and internet use. For separately deductible occupancy expenses, the usual calculation uses the floor area of the place of business and the period it was used. [ATO guidance for sole traders working from home](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-home-based-business-expenses/home-based-business-expenses-sole-trader-or-partnership).

### 4.7 Net business income or loss (P8)

- **Net business income or loss (P8):** Subtract deductible expenses from the applicable P8 income and apply the tax adjustments. Transfer P8 label Z to supplementary return question 15 label C for non-primary-production net income or loss. If any business activity made a loss, complete P3 and P9 and test Division 35 for that activity. The adjusted-income requirement is less than $250,000 before relying on the assessable-income, profits, real-property or other-assets tests. Assess statutory exceptions and Commissioner discretion separately. Otherwise defer the activity's loss. [ATO 2026 transfer instructions](https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/income-questions-13-24-supplementary-tax-return-2026/15-net-income-or-loss-from-business-2026) · [ITAA 1997 s 35-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/35-10).

## Section 5 -- Edge cases and special rules

### 5.1 Personal services income (PSI)

- **Personal services income (PSI):** Screen each amount for whether it is mainly, ordinarily more than half, a reward for personal effort or skills. Then apply the separate personal services business tests. The 80% source-concentration rule is not the definition of PSI; consider the results test and other tests/determination rules in their proper order. Refer uncertain cases for review. [ITAA 1997 s 84-5 and TR 2022/3](https://www.ato.gov.au/law/view/document?docid=TXR/TR20223/NAT/ATO/00001).

### 5.2 Mixed-use assets

- **Mixed-use assets** -- Assets used partly for private and partly for business purposes: claim only the business-use percentage. Maintain records of the split (e.g., logbook for car, diary for home office).

### 5.3 Prepaid expenses (SBE)

- **Prepaid expenses:** The 12-month rule applies to eligible otherwise deductible expenses for qualifying businesses with aggregated turnover below $50 million. The eligible service period must be 12 months or less and end by 30 June of the following income year for a 30 June balancer. Prepayments under tax shelter arrangements are subject to separate rules. A qualifying 12-month policy incurred and paid in May 2026 and covering May 2026 through April 2027 meets the timing tests for a deduction in 2025-26. [ATO deductions for prepaid expenses 2026](https://www.ato.gov.au/law/view/document?docid=SAV%2FDPE).

### 5.4 Capital vs revenue

- **Capital vs revenue** -- Establish the character of the advantage sought and the circumstances of the expenditure, including whether it adds to the business structure or pays for operating it. A new asset or enduring benefit can indicate capital expenditure. Capital expenditure is excluded under s 8-1 and may qualify under other provisions, such as depreciation or a CGT cost base. Consider this distinction for website development, major software and business restructuring. [ATO TR 2016/3](https://www.ato.gov.au/law/view/document?DocID=TXR%2FTR20163%2FNAT%2FATO%2F00001&PiT=99991231235958).

### 5.5 Hobby vs business

- **Hobby vs business** -- The ATO may deny deductions if the activity is a hobby, not a business. Indicators of a business: intention to make a profit, repetition and regularity, business-like organisation, size and scale, business plan.  _(ATO guidelines, TR 97/11)_

## Section 6 -- Self-checks

Before delivering output, verify:

- [ ] All income items trace to source documents (invoices, bank statements)
- [ ] Deductions satisfy s 8-1 nexus to assessable income
- [ ] Motor vehicle method is consistently applied (not both methods for same car)
- [ ] Depreciation method matches SBE or general rules as applicable
- [ ] Instant asset write-off threshold ($20,000) is correctly applied
- [ ] Home office hours are supported by records (if fixed rate method)
- [ ] Non-commercial loss rules checked if a loss is reported
- [ ] PSI risk flagged if applicable
- [ ] Trading stock valuation method is documented
- [ ] Rates and thresholds match the 2025–26 income year
- [ ] Output format matches the base skill spec

## Section 7 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill.

> [Original contributor credit](https://github.com/openaccountants/openaccountants/blob/fc090e8e95bae53674c2df8398b218b0c528a7c3/skills/australia/au-sole-trader-schedule.md).

## Sources

Not yet confirmed: the working from home fixed rate for 2026-27.

Check this point with one of our partner accountants.

Read 2026-11-12 for the depreciation correction:

- [ITAA 1997, ss 40-25, 40-70, 40-72, 40-75 and 40-95](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html): eligibility, date-specific factors, formulas and effective-life selection. Selected sections of retained current compilation 268 read 2026-11-12.
- [Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025, Schedule 2](https://www.legislation.gov.au/F2025L01097/asmade/text): asset-specific Table A and Table B lives; select the applicable dated determination. Selected Table A/Table B categories read 2026-11-12.

- [ITAA 1997, ss 328-175, 328-180, 328-185, 328-190, 328-210 and 328-220](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) -- read 2026-11-12 for selected simplified-depreciation eligibility, cost, allocation, rates, low-pool-value and continuing-pool rules.
- [ITTPA 1997, s 328-180(4)(d) and (6)(e)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) -- read 2026-11-12 for the temporary 2025-26 asset and pool thresholds.
- [Tax Reform No. 2 Act 2026, schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text) -- read 2026-11-12 for the permanent threshold application from July 2026.
