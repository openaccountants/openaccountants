---
name: au-rental-property
description: Use this skill whenever asked about Australian rental property income and deductions. Trigger on phrases like "rental income Australia", "negative gearing", "rental deductions", "investment property tax", "Division 40", "Division 43", "capital works deduction", "depreciation schedule", "rental property CGT", "rental withholding", "body corporate fees", "strata levy deduction", "repairs vs improvements", "TR 97/23", "GST on property", "land tax on an investment property", "stamp duty on a rental", or any question about completing the rental property schedule in an Australian individual tax return. This skill covers rental income reporting, deductible expenses, depreciation (Div 40 plant and Div 43 building), negative gearing including the enacted 1 July 2027 limit, CGT on disposal, foreign resident withholding, the GST decision path, the state and territory taxes that attach to property, and common transaction classifications. ALWAYS read this skill before touching any Australian rental property work.
version: "1.6"
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-12
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# AU Rental Property

## AU Rental Property

## AU Rental Property

## Australia Rental Property -- Income & Deductions Skill v1.6

Australia Rental Property -- Income & Deductions Skill v1.6

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax | Income Tax -- Rental Property Schedule |
| Currency | AUD only |
| Tax year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Primary legislation | Income Tax Assessment Act 1997 (ITAA 1997) |
| Supporting legislation | ITAA 1936; TR 97/23 (repairs vs improvements); TR 2026/1 (rental income and deductions for individuals not in business); PCG 2026/2 (apportionment); PCG 2026/3 (holiday homes and section 26-50); [ATO, Rental properties guide 2026](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026) |
| Tax authority | Australian Taxation Office (ATO) |
| Filing portal | myTax / tax agent lodgement (Online Services for Agents) |
| Filing deadline | 31 October (self-lodgement); agent-managed deadlines vary |
| Skill version | 1.6 |

### Select the income year before calculating

The rate and threshold tables immediately below are for **2026-27**. Ask which income year is being
prepared before calculating anything: the second resident bracket was 16 cents in 2024-25 and
2025-26 and is 15 cents from 1 July 2026, and the Medicare levy surcharge thresholds move each
year. For a prior year, use that year's tables on ato.gov.au. [ATO, Tax rates: Australian
resident](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents)

Apply the commencement and application dates in Sections 2 to 8. The CGT summary in
Section 2.8 covers events in 2026-27; use `au-capital-gains.md` for later events.

### Key Thresholds (2026-27)

**Key Thresholds (2026-27)**

| Item | Value |
| --- | --- |
| Tax-free threshold | $18,200 |
| Medicare levy | 2% of taxable income |
| Medicare levy surcharge (no PHI) | 1%, 1.25% or 1.5% where income for MLS purposes exceeds $105,000 single or $210,000 family in 2026-27 ($101,000 and $202,000 in 2025-26) |
| CGT discount (eligible resident individuals, 12+ months) | 50% for CGT events before 1 July 2027; residency and other conditions apply. See Section 2.8 and [ITAA 1997, s 115-100](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| Div 43 rate (post-Sep 1987 residential) | 2.5% of construction cost |
| Div 43 rate (post-Feb 1992 short-term traveller) | 4% |
| Low-value asset pool threshold | $1,000 (Div 40) |
| Immediate deduction threshold (Div 40) | $300 |

### Individual Marginal Tax Rates (2026-27)

**Individual Marginal Tax Rates (2026-27)**

| Taxable Income (AUD) | Rate | Cumulative Tax at Top |
| --- | --- | --- |
| 0 -- 18,200 | 0% | $0 |
| 18,201 -- 45,000 | 15% | $4,020 |
| 45,001 -- 135,000 | 30% | $31,020 |
| 135,001 -- 190,000 | 37% | $51,370 |
| 190,001+ | 45% | -- |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown apportionment (private vs rental) | 0% deductible |
| Unknown whether repair or improvement | Treat as improvement (capitalise) |
| Unknown construction cost for Div 43 | Do not claim -- obtain quantity surveyor report |
| Unknown CGT contract/event date | Do not compute -- obtain the contract and establish the CGT event timing |
| Unknown cost base | Do not compute CGT -- escalate |

## Section 2 -- Classification Rules

### 2.1 Rental Income

- **Gross rent and receipt year** -- For ordinary individual rental-property reporting, declare gross rent in the income year the tenant pays the owner or their agent/property manager, before fees and expenses deducted by the agent. A later transfer from the agent to the owner does not move the income into another year. Ordinarily report each owner's legal share; very limited cases with sufficient evidence of a different equitable interest need the separate check in Section 6.2. Check the derivation basis separately for a rental business. [ATO, rental income you must declare](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-income-you-must-declare).
- **Return year and field** -- Use the matching-year return's Rent section and any required rental schedule. The ATO Rental properties 2026 guide and myTax 2026 instructions concern 2025-26. **Not yet confirmed:** the final 2026-27 return labels and fields; do not carry Item 21 forward without checking that form.

**Rental Income Types**

| Income Type | Treatment |
| --- | --- |
| Rent paid by tenant | For ordinary individual letting, declare gross rent by the co-ownership share established in Section 6.2 in the year paid to the owner or agent; do not substitute unpaid rent receivable or the later net bank remittance. [ATO, rental income](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-income-you-must-declare) |
| Bond forfeited (retained for damage) | Assessable in year retained |
| Insurance payout (loss of rent) | Assessable |
| Reimbursement from tenant (excess utilities) | Assessable |
| Key money / lease premium | Assessable |


#### Worked receipt-year check

For an ordinary individual landlord, assume a tenant pays $2,400 gross rent to the property manager on 30 June 2027. The manager deducts a $180 management fee and $120 of deductible rental repairs, then remits $2,100 to the co-owners on 5 July 2027. This taxpayer's legal interest is 50%. The owner's estimated rental income is $1,200 in 2026-27, with the $150 share of expenses considered separately; the $1,050 net cash share is not the gross rent. Assume the stated expenses are deductible in that year and there is no private use. [ATO, rental income and completing your tax return](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-income-you-must-declare).

```oa-check
name: Rent paid to the agent before financial year end
inputs:
  agent_receipt_year: 2027
  agent_receipt_month: 6
  gross_rent: 2400
  management_fee: 180
  deductible_repairs: 120
  legal_share_percent: 50
steps:
  - income_year_start: agent_receipt_year - 1 + floor((agent_receipt_month + 5) / 12)
  - rental_income: pct(gross_rent, legal_share_percent)
  - expense_share: pct(management_fee + deductible_repairs, legal_share_percent)
  - net_cash_share: rental_income - expense_share
expected:
  income_year_start: 2026
  rental_income: 1200
  expense_share: 150
  net_cash_share: 1050
```

### 2.2 Negative Gearing

For 2026-27, an otherwise allowable individual rental loss can reduce other assessable income, subject to the ordinary deduction rules and other restrictions in this guide. The following enacted restriction applies for **2027-28 and later income years**. Act 49 Schedule 2 commenced on 27 June 2026; Act 71 Schedule 4 commenced on 1 October 2026 and extends the exceptions below. [Act 49, Schedule 2 item 5](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html) and [Act 71, Schedule 4](https://www.legislation.gov.au/C2026A00071/asmade/text).

| Test | Treatment from 2027-28 |
| --- | --- |
| General restriction | Under s 26-155(1), otherwise deductible residential-accommodation expenses exceeding the relevant assessable residential-accommodation income are not deductible for that year. The excess is quarantined, may be applied under the s 102-5 net capital gain method and, to the extent unused, carries into the next year's residential calculation. Do not treat the restriction as permanent forfeiture. [ITAA 1997, s 26-155](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Pre-Budget ownership interest | Test the ownership interest **last acquired before 7:30 pm, ACT legal time, on 12 May 2026**, not merely whether the property was held at that time. For an acquisition under contract, the interest starts when the contract is entered into for this test. An earlier contract settling later can qualify; acquisition exactly at the cut-off does not. Establish each interest's acquisition history. [ITAA 1997, s 26-155(2)(a) and (3)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| New residential dwelling | The exception is taxpayer-relative and depends on requirements determined by legislative instrument under s 26-160(4). A marketing description such as 'new build' does not establish the statutory exception. Identify and apply the relevant instrument before claiming it. [ITAA 1997, ss 26-155(2)(b) and 26-160(3)-(5)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Other non-quarantined dwellings | Amounts covered by a Ministerial activity/purpose determination under s 26-155(2)(c) are excluded from the restricted calculation. Identify an applicable determination rather than assuming all affordable or social housing qualifies. [ITAA 1997, s 26-155(2)(c) and (3A)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Certain entities and fringe benefits | The restriction does not apply to a widely held unit trust within the specified definition or a complying superannuation entity. Disregard amounts to the extent they relate to providing a fringe benefit; this is an amounts-based exception. [ITAA 1997, s 26-155(4)-(5)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Mixed residential interests | Exclude both the income and deductions for non-quarantined interests from the initial restricted calculation. Reduce the resulting excess by the specified net non-quarantined residential profit and gains realised from residential revenue assets. Apply trust attribution and bankruptcy modifications where relevant. [ITAA 1997, s 26-155(2) and (6)-(9)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| First-income-use deemed acquisition | Disregard the effect of s 118-192(2) when testing the pre-Budget acquisition and new-dwelling exceptions as directed by s 26-155(3AA)-(3AB). A CGT market-value reset does not itself remove those exceptions. [ITAA 1997, s 26-155](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |

Qualifying changes of ownership can preserve an exception:

| Change | Conditions to check |
| --- | --- |
| Surviving spouse | Interest acquired from the deceased spouse as surviving joint tenant or estate beneficiary. The deceased spouse's pre-Budget acquisition or new-dwelling status can carry through for the acquired interest. [ITAA 1997, s 26-156](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Deceased non-spouse co-owner | The survivor and deceased must have held interests in the same dwelling as joint tenants or tenants in common, with the deceased interest acquired through survivorship or the estate. **Both** the survivor's existing interest and the deceased's interest must satisfy the corresponding pre-Budget or new-dwelling condition. [ITAA 1997, s 26-157](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Relationship breakdown | A specified order, agreement or award under s 126-5(1)(a)-(f) involving the taxpayer and spouse/former spouse is required. The transferor can be the spouse/former spouse, a company or a trustee. Check the transferor's relevant pre-Budget acquisition or new-dwelling status. A transfer between spouses alone is insufficient. [ITAA 1997, s 26-158](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |

For this restriction, 'residential dwelling' excludes caravans/mobile homes (including mobile tiny homes), hotels, motels, inns, hostels, boarding houses, student accommodation connected with a school or other education institution and boats or other marine vessels. Associated land and structures available to occupants are included as specified in s 26-160(2). [ITAA 1997, s 26-160](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

Before projecting a 2027-28 loss, obtain the ownership interests and contract dates, property/use category, entity status, fringe-benefit facts, inheritance or relationship-breakdown history and the applicable new-dwelling or purpose instrument. **Not yet confirmed:** applicable instruments under ss 26-155(2)(c) and 26-160(4), and any later amendment affecting these pinned October 2026 provisions.

For residential capital gains from 1 July 2027, use the matching-year s 102-5 method and the separate capital gains guide. Quarantined expenditure is excluded from the cost base and reduced cost base to the extent s 26-155 prevents deduction; do not add it automatically to either base. [ITAA 1997, ss 110-38(8A) and 110-55(9JA)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).

#### Worked quarantine check

Assume an individual has one established residential investment within s 26-155, with no applicable exception. All expenses stated are otherwise deductible. In 2027-28, residential income is $42,000 and expenses are $54,000. With no non-quarantined residential profit, revenue-asset gain, relevant capital gain, trust attribution or bankruptcy modification, the estimated current deduction is $42,000 and $12,000 carries forward. In 2028-29, residential income is $50,000 and current expenses are $20,000. The carried $12,000 is absorbed in that year's residential calculation, leaving estimated net residential income of $18,000. [ITAA 1997, s 26-155(1)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

```oa-check
name: Residential excess carries forward rather than offsetting salary
inputs:
  first_year_income: 42000
  first_year_otherwise_deductible: 54000
  second_year_income: 50000
  second_year_current_expenses: 20000
steps:
  - first_year_deduction: min(first_year_otherwise_deductible, first_year_income)
  - first_year_carry: max(first_year_otherwise_deductible - first_year_income, 0)
  - second_year_available_expenses: second_year_current_expenses + first_year_carry
  - second_year_deduction: min(second_year_available_expenses, second_year_income)
  - second_year_net_income: second_year_income - second_year_deduction
  - second_year_carry: max(second_year_available_expenses - second_year_income, 0)
expected:
  first_year_deduction: 42000
  first_year_carry: 12000
  second_year_deduction: 32000
  second_year_net_income: 18000
  second_year_carry: 0
```

### 2.3 Deductible Expenses (Immediate)

**Deductible Expenses (Immediate)**

| Expense | Treatment | Notes |
| --- | --- | --- |
| Interest on investment loan | Deductible | Must trace loan purpose to rental property |
| Council rates | Deductible | Apportioned if part-private |
| Water rates / charges | Deductible |  |
| Body corporate / strata fees | Ordinary administration and general maintenance contributions may be deductible | Special levies funding a particular capital improvement are not immediately deductible. Check capital-works eligibility and timing after work is completed and charged to the fund. [ATO common property expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/common-property-expenses) |
| Land tax | Deductible |  |
| Property management fees | Deductible | Agent commissions, letting fees |
| Insurance (landlord, building, contents) | Deductible |  |
| Advertising for tenants | Deductible |  |
| Pest control | Deductible |  |
| Gardening / lawn mowing (if provided to tenant) | Deductible |  |
| Tax agent fee (rental schedule portion) | Deductible |  |
| Travel related to residential rental accommodation | Generally denied for a non-business individual under s 26-31 | The business test and specified entity exceptions require checking; see below. [ITAA 1997, s 26-31](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |

- **Borrowing expenses** -- Loan establishment fees, lenders mortgage insurance, loan valuation fees and mortgage stamp duty may qualify under s 25-25. Apply the $100 test to the combined income-producing amounts or proportions of borrowing expenditure incurred in the income year, not to one fee or the unadjusted private-use cost. A qualifying total of $100 or less is deductible in that year. Otherwise use the statutory day-based calculation over the shortest of the original loan term, the actual borrowing-to-repayment period and 5 years. Adjust for part years and income-producing use; an early repayment can bring forward the eligible remaining deduction. Apply the selected income year's rental-loss restrictions separately. [ITAA 1997, s 25-25(1)-(6)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-25).

For example, a $150 borrowing fee with 50% income-producing use gives a $75 qualifying amount. Assuming no other qualifying borrowing expenditure in that income year, s 25-25(6) allows that $75 in the year incurred. At the boundary, a $200 fee with the same use gives $100; a $202 fee gives $101 and falls outside that immediate-deduction exception.

```oa-check
name: Borrowing expense income-use threshold
inputs:
  borrowing_fee: 150
  boundary_fee: 200
  above_boundary_fee: 202
  income_use_percent: 50
steps:
  - qualifying_amount: pct(borrowing_fee, income_use_percent)
  - boundary_qualifying_amount: pct(boundary_fee, income_use_percent)
  - above_boundary_qualifying_amount: pct(above_boundary_fee, income_use_percent)
expected:
  qualifying_amount: 75
  boundary_qualifying_amount: 100
  above_boundary_qualifying_amount: 101
```

- **Travel exceptions** -- Section 26-31 does not deny otherwise eligible travel necessarily incurred in carrying on a business to produce assessable income. Its entity exception applies if, at any time in the income year, the taxpayer is a corporate tax entity, a non-SMSF superannuation plan, a managed investment trust, a public unit trust within s 102P or a unit trust/partnership whose members all meet the specified categories at that time. Establish the actual business/entity facts and ordinary deduction requirements. [ITAA 1997, s 26-31(1)-(2)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

### 2.4 Repairs vs Improvements (TR 97/23)

**Repairs vs Improvements (TR 97/23)**  _([TR 97/23](https://www.ato.gov.au/law/view/document?docid=TXR/TR9723/NAT/ATO/00001))_

| Characteristic | Repair (immediate deduction) | Improvement (capitalise) |
| --- | --- | --- |
| Restores the efficiency of an existing function without changing its character | May be a repair, including minor incidental improvement | Substantial improvement or a new/additional function is capital |
| Uses the same, different or modern materials | Material choice alone does not determine the result; assess function and the relevant entirety | Different or better materials do not automatically make the work an improvement |
| Remedies defects, damage or deterioration present on acquisition | Initial repair expenditure is capital under s 25-10; eligible later deterioration may be separable under TR 97/23 paragraphs 63-66 | Check Division 40, Division 43 and CGT cost-base eligibility for the actual work |
| Replaces a roof | Can be a repair where it restores part of the building without an improvement; the roof is not automatically the relevant entirety | Initial repairs, improvements and replacement of the relevant entirety are capital; apply [TR 97/23](https://www.ato.gov.au/law/view/document?docid=TXR/TR9723/NAT/ATO/00001) to the facts |
| Example: patching cracked tiles | Repair | -- |
| Example: replacing all tiles with stone | Assess the actual effect; different material alone is not decisive | Capital if the work substantially improves the property or replaces the relevant entirety |
| Example: replacing broken tap with same model | Repair | -- |
| Example: full kitchen renovation | Actual repair work may be deductible if independently separable and its cost accurately quantified | Capital improvements and inseparable repair/improvement work are not deductible under s 25-10 |

- **Identify the entirety and the cause** -- Apply the income-producing-use and capital tests before claiming any example above. Identify the relevant entirety, its condition when acquired, the cause of the deterioration and the work's effect on function and character. A first repair after acquisition is not necessarily an initial repair. Separate actual repair costs from improvement costs only where the work can be separated and its cost accurately quantified; there is no deduction for a notional repair that was not carried out. [TR 97/23, paragraphs 4-5, 16, 35, 43-57 and 59-66](https://www.ato.gov.au/law/view/document?docid=TXR/TR9723/NAT/ATO/00001).

### 2.5 Division 40 -- Plant & Equipment Depreciation

**Division 40 Effective Lives**  _(Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025, Table A, Residential property operators (67110). [2025 determination, Schedule 2 Table A](https://www.legislation.gov.au/F2025L01097/asmade))_

| Asset | Effective Life (ATO) | Decline Method |
| --- | --- | --- |
| Hot water system (gas or electric) | 12 years | Diminishing value or prime cost |
| Hot water system (solar) | 15 years | Either |
| Carpet | 8 years | Either |
| Internal blinds | 10 years | Either |
| Curtains | 6 years | Either |
| Oven / cooktop | 12 years | Either |
| Air conditioning (split system) | 10 years | Either |
| Dishwasher | 8 years | Either |
| Smoke alarm | 6 years | Either |
| Ceiling fan | 5 years | Either |

The table follows Table A, Residential property operators (67110), in the *Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025*. Choose the applicable determination under section 40-95, including its contract-date and start-time rules, or a valid self-assessed life; do not automatically reset an existing asset register. See [2025 determination, Schedule 2 Table A](https://www.legislation.gov.au/F2025L01097/asmade).

- **Diminishing value rate** -- 200% ÷ effective life
- **Prime cost rate** -- 100% ÷ effective life
- **Second-hand and prior-private-use restriction** -- Subject to commencement/transitional rules, s 40-27 reduces the deduction for decline attributable to residential-accommodation income outside a business where the taxpayer did not hold the asset at its first use/installation, or the specified prior residential/private-use tests apply. Prior private use can matter even for the first owner. This can reduce the relevant deduction to nil; it does not reset the asset's tax value to zero. Establish contract/acquisition dates, first use, prior residence/non-taxable use and the relevant application rules. [ITAA 1997, s 40-27(1)-(2)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) and [ATO, second-hand asset limits](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/rental-expenses).
- **Exceptions to test** -- The business-purpose boundary and specified entity exception in s 40-27(3) can change the result. The entity categories are corporate tax entities, non-SMSF superannuation plans, managed investment trusts, public unit trusts within s 102P and qualifying all-member unit trusts/partnerships. For assets supplied with new residential premises, apply all conditions in (4)-(5), including the asset's location, prior residence and prior-holder deduction conditions and the limited 6-month rule. Ordinary refurbishment alone does not establish this exception. Subsection (6) addresses assets allocated to a low-value pool; check the separate pool-allocation rules. A newly acquired appliance can qualify in an older building if its own facts meet the deduction rules. [ITAA 1997, s 40-27(2)-(6)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) and [ATO, new and second-hand assets](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/rental-expenses).

### 2.6 Division 43 -- Capital Works Deduction

**Division 43 Capital Works Deduction Rates**

| Construction Date | Rate | Notes |
| --- | --- | --- |
| Before 18 July 1985 | 0% | No deduction available |
| 18 Jul 1985 -- 15 Sep 1987 | 4% | Residential/non-residential |
| After 15 Sep 1987 (residential) | 2.5% | 40-year write-off |
| After 15 Sep 1987 (short-term traveller) | 4% | Certain accommodation |

- **Base** -- Original construction cost (obtain from quantity surveyor report or builder records). NOT the purchase price of the property.
- **Successor owner and annual base** -- A sale does not restart the capital works period. Calculate the new owner's deduction from the eligible original construction-expenditure pool attributable to their area, using the applicable rate, qualifying days and use adjustments. The statutory undeducted construction expenditure is a cap, not the base to multiply by 2.5%. It can reflect statutory reductions even where a previous owner claimed no deduction. Check construction dates, completion, qualifying use and any conditional 4% rate rather than assuming 2.5% universally. [ITAA 1997, ss 43-15, 43-115, 43-210, 43-215 and 43-230 to 43-240](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) and [ATO, changes in building ownership](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/rental-expenses#Changesinbuildingownership).


#### Worked successor-owner check

Assume the buyer owns the whole relevant area of a completed, eligible residential building throughout 2026-27, with 365 qualifying income-producing days, no private use and a 2.5% rate. The original eligible construction expenditure attributable to that area is $400,000 and the correctly determined undeducted balance is $300,000. The estimated annual deduction is $10,000, not $7,500. The purchase does not restart the write-off period. As a separate cap illustration, if the statutory balance were only $6,000 on otherwise identical assumptions, the deduction would be limited to $6,000. [ITAA 1997, ss 43-15 and 43-210](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

```oa-check
name: Successor capital works use original eligible expenditure with a cap
inputs:
  original_eligible_construction: 400000
  undeducted_balance: 300000
  rate_percent: 2.5
  qualifying_days: 365
  separate_cap_balance: 6000
steps:
  - annual_formula_amount: pct(original_eligible_construction, rate_percent) * qualifying_days / 365
  - deduction: min(annual_formula_amount, undeducted_balance)
  - separate_cap_deduction: min(annual_formula_amount, separate_cap_balance)
expected:
  annual_formula_amount: 10000
  deduction: 10000
  separate_cap_deduction: 6000
```

### 2.7 Interest Deductibility

- **Nexus requirement** -- The loan must have a clear nexus to producing rental income. Key rules follow in the table.
- **Mixed-purpose loans and redraws** -- Each redraw is a separate borrowing whose interest follows the use of the funds. Ordinary principal repayments on a mixed-purpose debt reduce its rental and private portions proportionately. TR 2000/2 recognises exceptions: recouped borrowed funds repaid to the account reduce the portion previously used for that purpose, with any excess over that debt portion reducing the remaining uses proportionately; qualifying refinancing into 2 separate accounts or sub-accounts for amounts equivalent to the existing income-producing and private portions preserves those respective purposes. Trace each drawdown, recoupment, repayment and refinancing. [TR 2000/2, paragraphs 15-18 and 43-47](https://www.ato.gov.au/law/view/document?docid=TXR/TR20002/NAT/ATO/00001).

**Interest Deductibility Scenarios**

| Scenario | Deductible? |
| --- | --- |
| Loan to purchase rental property | Income-producing portion only, subject to the nexus, private-use and year-specific restrictions |
| Loan to renovate rental property | Income-producing portion only; apply the pre-income conditions below where relevant |
| Refinanced loan (same purpose, same or lower amount) | Yes |
| Loan redrawn for personal use | No -- apportioned |
| Line of credit (mixed purpose) | Must trace each drawdown |
| Interest on loan while property vacant (available for rent) | May be deductible if the income nexus continues; apply private-use and vacant-land restrictions below |
| Interest before rent starts, including construction/renovation | May be deductible before the property is available for rent; test the income nexus, purpose and applicable restrictions below. Do not automatically defer or capitalise it. [TR 2004/4, paragraphs 8-9](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20044/NAT/ATO/00001&PiT=99991231235958) |

- **Pre-income interest** -- TR 2004/4 paragraph 9 requires that the expense is not too soon/preliminary, is not private or domestic, retains the necessary connection despite the period before income, is incurred with the income-producing end in view and is accompanied by continuing efforts towards that end. Borrowing for a capital asset does not by itself make the interest capital. Eligible renovation-loan interest can start when borrowed; changed private purpose can end deductibility. [TR 2004/4, paragraphs 8-9](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20044/NAT/ATO/00001&PiT=99991231235958) and [ATO, interest on loans](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/rental-expenses).
- **Vacant-land distinction** -- Apply s 26-102 to otherwise deductible land-holding costs, including acquisition-loan interest, with its structure/use and exception tests. The ATO distinguishes costs of repairing, renovating or constructing a structure, and associated interest/borrowing costs, from vacant-land holding costs. Those expenses still require their own deduction/nexus analysis. Commercial availability alone does not settle every interest claim. [ITAA 1997, s 26-102](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) and [ATO, deductions for vacant land](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/rental-expenses).

### 2.8 CGT on Disposal

This summary covers CGT events in 2026-27. For a sale under contract, the CGT event is generally the contract date, not settlement. Use the separate capital gains guide for events from 1 July 2027 and their transition rules. [ITAA 1997, ss 104-10 and 115-100](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).

| Element | Treatment |
| --- | --- |
| Capital proceeds | Money and market value of other property received or receivable for the disposal. For an ordinary arm's length cash sale, use the sale price before agent commission and selling legal fees; check market-value substitution where applicable. [ATO, capital proceeds](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/capital-proceeds-from-disposing-of-assets) |
| Cost base | Include eligible acquisition costs, incidental buying and selling costs, capital improvements and other applicable cost base elements. Exclude deductible or recouped amounts and apply capital works adjustments; do not count the same expense twice. [ATO, cost base](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cost-base-of-asset) |
| Capital works adjustment | Generally reduce the cost base for Div 43 amounts deducted or still deductible, including eligible expenditure incurred by a previous owner. Check the acquisition/expenditure date exceptions and the exception where construction expenditure cannot be determined. [ATO, capital works adjustments](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cost-base-adjustments-for-capital-works) |
| Property gain or loss | Capital gain = capital proceeds minus cost base. Test a capital loss against the **reduced cost base**, which differs from the cost base. A property gain is not yet the taxpayer's net capital gain. [ATO, rental CGT](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/other-tax-considerations) |
| Net capital gain | Apply allowable current-year capital losses, then unapplied prior-year net capital losses, before any CGT discount and applicable concessions. Include the resulting net capital gain in assessable income. Capital losses cannot offset ordinary rental income. [ATO, capital losses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/using-capital-losses-to-reduce-capital-gains) and [CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount) |
| 50% CGT discount | Generally available to eligible resident individuals and trusts for events before 1 July 2027 where the 12-month test and other conditions are met. Exclude acquisition and disposal days when testing the holding period; apply foreign/temporary resident and trust-beneficiary rules. Companies do not receive this discount. [ITAA 1997, Div 115](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| Foreign or temporary resident individual | Do not automatically deny every discount. For an asset acquired after 8 May 2012, foreign/temporary residence throughout the discount testing period gives a 0% discount; eligible Australian-resident days can support a partial discount. Earlier acquisitions require the pre-8 May 2012 rules, including the optional market-value method where eligible. That method can permit a full 50% discount if the qualifying pre-8 May 2012 excess equals or exceeds the gain. [ATO, foreign resident discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/cgt-discount-for-foreign-residents) and [ITAA 1997, s 115-115](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| Main residence exemption | Check actual residence, income-producing periods and any first-income-use market-value rule. Being a main residence for part of ownership does not itself establish an exemption. See [ATO, home used for rental or business](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/using-your-home-for-rental-or-business). A foreign resident at disposal generally cannot claim a full or partial exemption or the first-income-use rule unless the life events test is met. [ATO, foreign residents' main residence](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents) |
| Absence choice | The dwelling must first have been the taxpayer's main residence. The income-producing limit is 6 years per qualifying absence, with a new maximum after it again becomes and ceases to be the main residence; non-income-producing absence can be indefinite. Another dwelling generally cannot be treated as the main residence during that choice, subject to the changing-residences overlap exception. Foreign-resident disposal restrictions still apply. [ATO, former home](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/treating-former-home-as-main-residence) and [ITAA 1997, s 118-145](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |

For the cost base date exception, check assets acquired at or before 7:30 pm ACT time on 13 May 1997 and capital expenditure incurred by 30 June 1999. Establish what is deductible at the relevant time under [TD 2005/47](https://www.ato.gov.au/law/view/document?DocID=TXD/TD200547/NAT/ATO/00001&PiT=99991231235958), including deduction and CGT amendment periods. The ATO's insufficient-information practice requires both insufficient information about the amount and nature of construction expenditure and no claim for that expenditure under Div 43 or another provision. Keep evidence of the applicable exception. [PS LA 2006/1 (GA)](https://www.ato.gov.au/law/view/document?DocID=PSR/GA20061/NAT/ATO/00001&PiT=99991231235958) and [ITAA 1997, ss 110-45 and 110-55](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).

#### Worked CGT checks

These are fabricated estimates for contracts entered on 1 February 2027, before the 1 July 2027 changes. They assume ordinary arm's length investment property sales, no main residence exemption, no rollover and no separate depreciating-asset proceeds.

An individual who has been an Australian resident, not a temporary resident, throughout ownership acquired the property on 1 July 2016. Eligible buying costs are $30,000, improvements $50,000 and selling costs $20,000. Div 43 adjustments total $12,000: $10,000 claimed and $2,000 still deductible within the amendment period. The $900,000 sale price is the capital proceeds. Apply $12,000 current-year capital losses and $20,000 prior-year net capital losses before the 50% discount. Assume no other gains, losses or concessions. The estimated net capital gain is $90,000. [ATO, cost base](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cost-base-of-asset), [capital works](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cost-base-adjustments-for-capital-works) and [CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount).

```oa-check
name: Rental sale costs and claimable capital works before losses and discount
inputs:
  purchase_price: 600000
  buying_costs: 30000
  improvements: 50000
  selling_costs: 20000
  capital_works_adjustment: 12000
  capital_proceeds: 900000
  current_year_losses: 12000
  prior_year_net_capital_losses: 20000
steps:
  - cost_base: purchase_price + buying_costs + improvements + selling_costs - capital_works_adjustment
  - capital_gain: capital_proceeds - cost_base
  - gain_after_losses: capital_gain - current_year_losses - prior_year_net_capital_losses
  - net_capital_gain: gain_after_losses - pct(gain_after_losses, 50)
expected:
  cost_base: 688000
  capital_gain: 212000
  gain_after_losses: 180000
  net_capital_gain: 90000
```

A foreign-resident individual acquired Australian real property on 1 January 2005 and was a foreign resident throughout ownership. Assume the property qualifies for discount treatment, its cost base was $400,000 on 8 May 2012 and remains $400,000 at sale, with no Div 43 adjustment or other cost base change. Its 8 May 2012 market value was $700,000. The taxpayer chooses the eligible market-value method under s 115-115(4). On sale for $650,000, the $300,000 pre-8 May 2012 excess exceeds the $250,000 capital gain, so the full 50% discount applies. With no capital losses or other concessions, the estimated net capital gain is $125,000. [ITAA 1997, s 115-115(4), table item 1](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) and [ATO, foreign resident discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/cgt-discount-for-foreign-residents).

```oa-check
name: Eligible foreign resident pre-May-2012 market-value method
inputs:
  cost_base: 400000
  may_2012_market_value: 700000
  capital_proceeds: 650000
steps:
  - capital_gain: capital_proceeds - cost_base
  - pre_may_2012_excess: may_2012_market_value - cost_base
  - eligible_gain: min(pre_may_2012_excess, capital_gain)
  - discount_amount: pct(eligible_gain, 50)
  - net_capital_gain: capital_gain - discount_amount
expected:
  capital_gain: 250000
  pre_may_2012_excess: 300000
  eligible_gain: 250000
  discount_amount: 125000
  net_capital_gain: 125000
```

### 2.9 Foreign-Resident Rental Income and Property-Sale Withholding

FRCGW concerns a property disposal. Do not apply its sale-price rate to ordinary rent. Australian rental income is declared in the foreign-resident owner's Australian tax return; assess deductions and any PAYG instalments separately. This is distinct from withholding on interest, dividends or royalties. [ATO, foreign and temporary resident income](https://www.ato.gov.au/api/public/content/0-9fc0474e-7b95-4e02-8b6a-580471487f4c) and [rental tax considerations](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/other-tax-considerations).

| Rule | Detail |
| --- | --- |
| Property-sale FRCGW | For contracts signed from 1 January 2025, the general rate is 15% of market value, with no property value threshold. In an arm's length sale, market value is usually the sale price. For contracts from 1 July 2017 to 31 December 2024, the rate was 12.5% where the value was $750,000 or more. Apply certificates, variations and other applicable exclusions. [ATO, FRCGW overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview) |
| Purchaser's obligation | Where FRCGW applies, the purchaser withholds and pays the ATO at or before settlement. The withholding is a credit towards the vendor's tax assessment, not the final CGT liability. [ATO, FRCGW overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview) and [variations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-residents-capital-gains-withholding-variations) |
| Clearance certificate | An Australian resident vendor generally supplies a valid ATO certificate to the purchaser at or before settlement to avoid FRCGW. Foreign residents cannot use a resident clearance certificate. Check specific legislative-instrument exceptions and apply early. [ATO, clearance certificates](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/australian-residents-and-clearance-certificates) |
| Variation | A foreign resident vendor may apply for a reduced rate where the standard withholding is too high relative to estimated Australian tax on the disposal. Obtain and give the variation notice to the purchaser at or before settlement. [ATO, variations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-residents-capital-gains-withholding-variations) |

**Not yet confirmed:** Any separate collection notice, retention duty or agency obligation affecting a tenant or property manager must be checked against the applicable notice and authority. Do not infer such a duty, its amount or its absence from FRCGW guidance alone.

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| REAL ESTATE AGENT [name], RENT COLLECTION | Assessable rental income | Net of agent commission (report gross; deduct commission separately) |
| TENANT [name], RENT PAYMENT, BOND TRANSFER | Assessable rental income | Bond held in trust is NOT income until forfeited |
| [INSURER] CLAIM PAYOUT, LOSS OF RENT | Assessable | Insurance for lost rent |
| AIRBNB PAYOUT, STAYZ PAYOUT | Assessable | Short-term rental income |

### 3.2 Expense Patterns (Debits) -- Immediate Deductions

**Expense Patterns (Debits) -- Immediate Deductions**

| Pattern | Category | Treatment |
| --- | --- | --- |
| [COUNCIL NAME] RATES, COUNCIL RATES | Council rates | Fully deductible |
| WATER CORP, SA WATER, SYDNEY WATER | Water rates | Fully deductible |
| BODY CORPORATE, STRATA LEVY, OWNERS CORP | Body corporate fees | Fully deductible (admin + sinking fund) |
| [STATE] LAND TAX, REVENUE NSW, SRO VIC | Land tax | Fully deductible |
| [AGENT NAME] MANAGEMENT FEE, LETTING FEE | Property management | Fully deductible |
| [INSURER] LANDLORD INSURANCE, BUILDING INS | Insurance | Fully deductible |
| PLUMBER, ELECTRICIAN, [TRADESPERSON] REPAIR | Repair (if restoring) | Deductible if repair per TR 97/23 |
| BUNNINGS, HARDWARE (minor repair materials) | Repair materials | Deductible if repair nature |
| PEST CONTROL, TERMITE INSPECTION | Pest control | Fully deductible |

### 3.3 Expense Patterns (Debits) -- Capital (Depreciate)

**Expense Patterns (Debits) -- Capital (Depreciate)**

| Pattern | Category | Treatment |
| --- | --- | --- |
| KITCHEN RENOVATION, BATHROOM RENO | Capital improvement | Add to cost base; Div 43 if structural |
| NEW HOT WATER SYSTEM (replacement-upgrade) | Div 40 asset | Depreciate over 12 years |
| NEW AIR CONDITIONER (split system install) | Div 40 asset | Depreciate over 10 years |
| NEW CARPET (full replacement, better quality) | Capital improvement | Div 40 for first owner; cost base for subsequent |

### 3.4 Loan / Interest Patterns

**Loan / Interest Patterns**

| Pattern | Category | Treatment |
| --- | --- | --- |
| [BANK] HOME LOAN INTEREST, INVESTMENT LOAN INT | Interest expense | Deductible (if loan traces to rental property) |
| [BANK] LOAN REPAYMENT, PRINCIPAL + INTEREST | Mixed | Only interest portion deductible -- NOT principal |
| [BANK] OFFSET ACCOUNT INTEREST | Interest saving | Reduces deductible interest (net interest method) |
| [BANK] LINE OF CREDIT DRAWDOWN | Capital movement | NOT income; trace use of funds |

### 3.5 Exclusions

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BOND LODGEMENT, RTA BOND, RTBA | EXCLUDE | Bond held in trust -- not income |
| MORTGAGE PRINCIPAL REPAYMENT | EXCLUDE | Capital repayment -- not deductible |
| PERSONAL USE period expenses | APPORTION | Deduct only rental-use portion |

## Section 4 -- Computation Method

### Step 1: Gross Rental Income

- **Gross Rental Income** -- Sum all assessable rental receipts for the financial year.

### Step 2: Immediate Deductions

- **Immediate Deductions** -- Sum all allowable expenses (interest, rates, insurance, management fees, repairs, body corporate, etc.).

### Step 3: Depreciation (Div 40 + Div 43)

- **Depreciation** -- Calculate eligible Div 43 using the original eligible expenditure, applicable rate, qualifying days/use and remaining-expenditure cap in Section 2.6; add eligible Div 40 depreciation under the applicable rules.

### Step 4: Net Rental Income / Loss

- **Net Rental Income / Loss** -- Gross income − deductions − depreciation = net rental income (or loss if negative gearing).

### Step 5: Report on Tax Return

- **Reporting outcome** -- For 2026-27, include positive rental income and apply an otherwise allowable individual rental loss against other assessable income. For 2027-28 and later, apply the restrictions, exceptions and carry-forward treatment in Section 2.2 before reporting a deductible loss. Use the matching-year tax rates.

## Section 5 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Form | Matching-year Individual Tax Return Rent section and required rental schedule. **Not yet confirmed:** final 2026-27 labels/fields; verify before using Item 21 |
| Reporting | Per-property basis (complete separate schedule for each property) |
| Joint ownership | Each co-owner reports their share (typically 50/50 for joint tenants) |
| Records retention | 5 years from date of lodgement (longer if CGT applies -- keep until 5 years after disposal) |
| Quantity surveyor report | Recommended for all post-1985 properties to substantiate Div 43 and Div 40 claims |

## Section 6 -- Edge Cases

### 6.1 Property Vacant

- **Vacancy deduction rule** -- For ordinary vacant letting periods, establish continuing rental purpose and genuine availability on commercial terms, then exclude private use and apply the relevant denial/apportionment rules. A vacant room in the owner's home has the specific treatment in Section 6.2. Pre-income interest requires the separate analysis in Section 2.7; holiday-home ownership expenses require the Section 6.3 screen first. [PCG 2026/2, paragraphs 13-17](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20262/NAT/ATO/00001&PiT=99991231235958) and [TR 2004/4, paragraph 9](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20044/NAT/ATO/00001&PiT=99991231235958).

### 6.2 Part-Year Rental / Part-Private Use

- **Classify before apportioning** -- First apply specific denials, including Section 6.3 for a holiday home. Otherwise eligible costs solely attributable to rental activity, such as letting fees, platform commissions, rental advertising and guest-stay cleaning, do not need the ownership-expense fraction. Allocate mixed ownership/use expenses on a fair and reasonable basis using the applicable time and area factors. Use the actual days in the relevant year. Full-year advertising does not establish full deductibility. [PCG 2026/2, paragraphs 10-17 and 29-43](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20262/NAT/ATO/00001&PiT=99991231235958).
- **Room in the owner's home** -- Under the ATO's accepted method, an unoccupied room remains private as part of the home: its eligible 'days held to produce income' are zero even when advertised. Combine actual income-producing days with the relevant area fraction for shared ownership expenses. Keep the direct rental costs separate. These compliance methods do not create a deduction where another rule denies it. [PCG 2026/2, paragraphs 15 and 33-43](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20262/NAT/ATO/00001&PiT=99991231235958).
- **Co-owners and domestic arrangements** -- Co-owners usually allocate income and expenses by their legal interests. TR 2026/1 recognises very limited cases where sufficient evidence establishes a different equitable interest; obtain that evidence and specialist advice before changing the ordinary split. One owner paying the bills alone does not establish a different interest. A rental business partnership needs separate analysis, and shared family household costs are not automatically commercial rent. [TR 2026/1, paragraphs 22-26](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20261/NAT/ATO/00001&PiT=99991231235958).  _([ATO, Rental income you must declare](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-income-you-must-declare))_

#### Worked room-in-home allocation

For 2026-27, assume one individual lets an exclusive 20 m² guest area in their 100 m² home for 100 paid days. Assume no additional common-area allocation in this simplified case. The room is advertised but empty for another 50 days and is part of the owner's private home when unoccupied. Otherwise eligible annual shared ownership expenses are $18,250; costs solely for the rental activity are $600 and gross rent is $8,000. Applying the accepted area/time method, eligible held days are zero, estimated ownership deductions are $1,000 and direct rental costs remain $600. Estimated net rental income is $6,400. [PCG 2026/2, paragraphs 10-17 and 29-43](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20262/NAT/ATO/00001&PiT=99991231235958).

```oa-check
name: Room-in-home ownership fraction excludes advertised empty days
inputs:
  exclusive_guest_area: 20
  whole_home_area: 100
  paid_rental_days: 100
  advertised_unoccupied_days: 50
  days_in_year: 365
  annual_ownership_expenses: 18250
  direct_rental_expenses: 600
  gross_rent: 8000
steps:
  - area_fraction: exclusive_guest_area / whole_home_area
  - eligible_held_days: advertised_unoccupied_days * 0
  - eligible_days: paid_rental_days + eligible_held_days
  - ownership_deduction: annual_ownership_expenses * area_fraction * eligible_days / days_in_year
  - total_deduction: ownership_deduction + direct_rental_expenses
  - net_rental_income: gross_rent - total_deduction
expected:
  area_fraction: 0.2
  eligible_held_days: 0
  ownership_deduction: 1000
  total_deduction: 1600
  net_rental_income: 6400
```

### 6.3 Holiday Homes

- **Apply the leisure-facility screen first** -- If the property is used or held for holidays/recreation, s 26-50 can deny specified ownership/use outgoings in full, including relevant interest, rates, insurance and maintenance. Check all applicable statutory exceptions. Rental advertising and cleaning after guest stays require separate ordinary-deduction analysis; the ownership/use denial does not automatically deny those direct rental costs. [ITAA 1997, s 26-50](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) and [TR 2026/1, paragraphs 30-40](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20261/NAT/ATO/00001&PiT=99991231235958).
- **Main use and a clear change** -- For the rental-income exception, test whether the property is used or held mainly to produce the specified income at all times in the year or relevant part-year period. Assess objective use and how it is held, including potential private use and peak-season access; a day-count majority alone is insufficient. Part-year relief requires the statutory conditions, and TR 2026/1 describes a definite and sustained change rather than a one-off stay or regular seasonal pattern. Keep advertisements, agent agreements, bookings and commercial-rent/access evidence. [ITAA 1997, s 26-50(3)-(4) and (7)-(8)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) and [TR 2026/1, paragraphs 37-47](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20261/NAT/ATO/00001&PiT=99991231235958).
- **Reduced rent for family or friends** -- For a below-market arrangement with a private/domestic purpose, exclude the private element on a fair and reasonable basis after applying any specific denial. Where otherwise deductible expenses exceed rent, the ATO accepts limiting those deductions to rent derived for the arrangements described in PCG 2026/2 paragraphs 44-47. Establish the facts before applying that approach. [PCG 2026/2, paragraphs 44-47](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20262/NAT/ATO/00001&PiT=99991231235958).
- **TR 2026/1 and the 2026 compliance guidelines** -- TR 2026/1 sets out when rental receipts are assessable, when outgoings are deductible and how to apportion mixed use for individuals not in business. PCG 2026/2 gives the apportionment methods the ATO accepts, and PCG 2026/3 its compliance approach to section 26-50 for holiday homes that are also let. Read them before claiming a loss on a property with any private use.  _([ATO, What's new in the rental properties guide 2026](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/whats-new-in-the-rental-properties-guide))_  _([ITAA 1997 (Cth) s 26-50](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/26-50); [ATO, How to claim rental expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/how-to-claim-rental-expenses))_

#### Worked holiday-home denial screen

For 2026-27, assume an individual's holiday home is used or held mainly for private recreation and no s 26-50 exception applies for any part of the year. Gross rent is $5,000. Otherwise current ownership/use outgoings of $18,000 fall within the denial. Separate rental advertising of $100 and cleaning after paying guest stays of $400 satisfy the ordinary deduction rules and are not ownership/use outgoings caught by that screen. Estimated deductions are $500 and net rental income is $4,500. The denied ownership costs do not become deductible merely because rent was received. [ITAA 1997, s 26-50](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) and [TR 2026/1, paragraphs 30-40](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20261/NAT/ATO/00001&PiT=99991231235958).

```oa-check
name: Holiday ownership denial precedes direct rental cost calculation
inputs:
  gross_rent: 5000
  ownership_outgoings: 18000
  rental_advertising: 100
  guest_cleaning: 400
steps:
  - ownership_denied: ownership_outgoings
  - ownership_deduction: ownership_outgoings - ownership_denied
  - direct_rental_deduction: rental_advertising + guest_cleaning
  - total_deduction: ownership_deduction + direct_rental_deduction
  - net_rental_income: gross_rent - total_deduction
expected:
  ownership_denied: 18000
  ownership_deduction: 0
  total_deduction: 500
  net_rental_income: 4500
```

### 6.4 Subdivision and Development

- **Subdivision profit treatment** -- If a rental property is subdivided, the profit on sale of subdivided lots may be ordinary income (not CGT) if the taxpayer has a profit-making intention. Escalate to specialist.

### 6.5 Deceased Estates

- **Deceased estate rental treatment** -- Rental property passing through an estate: the legal personal representative (LPR) reports rental income in the estate return until the property is transferred to a beneficiary. CGT is deferred until the beneficiary disposes.

## Section 7 -- Prohibitions

- **Prohibitions** -- NEVER claim residential rental travel without applying the business/entity tests in Section 2.3; NEVER decide Div 40 eligibility from first/subsequent ownership alone: apply prior-use, application and exception tests in Section 2.5; NEVER claim Div 43 without evidence of construction cost (quantity surveyor report or original builder records); NEVER deduct loan principal repayments; NEVER apply a blanket time fraction or rental-income cap before the denial and cost-classification tests in Sections 6.2-6.3; NEVER assume a foreign-resident individual has no CGT discount: apply the residency history and pre-8 May 2012 rules in Section 2.8; NEVER calculate a disposal using only Div 43 amounts actually claimed: establish the statutory adjustment, claimable amounts and exceptions in Section 2.8; NEVER present tax calculations as definitive -- always label as estimated

## Section 8 -- Which tax applies, and where its rules live

A property transaction can touch four separate regimes at once. Work out which apply before
calculating anything, because the answer to one changes the inputs to another.

### 8.1 Decision table by event

**Decision table by event**

| Event | Income tax | GST | CGT | State or territory |
| --- | --- | --- | --- | --- |
| Buying a residential investment property | Borrowing costs, and holding costs once available for rent | Generally input taxed on an existing residential premises, so no credit on the purchase. New residential premises may be taxable and may trigger GST at settlement | Establishes the cost base | Transfer duty, and possibly foreign purchaser surcharge duty |
| Holding and renting it out | Rental income assessable, deductions under Section 2, Div 40 and Div 43 | Residential rent is input taxed, so no GST on rent and no credits on expenses | Apply the Div 43 cost base adjustment for deductions claimed or still deductible, subject to the exceptions in Section 2.8 | Land tax, and possibly a foreign owner or vacancy surcharge |
| Renovating | Repair deductible, improvement capital | Credits depend on whether the premises remain input taxed | Capital work enters the cost base or Div 43 | Nil, unless it changes the land tax position |
| Short-stay or holiday letting | Apportionment for private use and periods not genuinely available | Commercial residential premises can be taxable rather than input taxed. Test this, do not assume | Main residence exemption can be lost or reduced | Some jurisdictions apply short-stay levies |
| Buying or holding a commercial property | Rent assessable, deductions available | Generally taxable, so GST on rent and credits on expenses, subject to registration. A going concern or margin scheme may apply on sale | Cost base as normal | Transfer duty and land tax |
| Selling | Balancing adjustments on Div 40 assets | See `au-gst-property.md`. GST at settlement can require the purchaser to withhold | The CGT calculation. See `au-capital-gains.md` | Duty is payable by the purchaser, not the vendor |
| Selling as a foreign resident | Rental income to the date of sale | As above | Apply the residency-history discount rules, including eligible pre-8 May 2012 market-value treatment; main residence relief generally requires the foreign-resident life events test. See Section 2.8 | As above |

### 8.2 The GST decision path

1. **Is the supply residential premises?** Existing residential premises are input taxed: no GST
   on the sale or the rent, and no credits on related acquisitions.
2. **Are they new residential premises?** New residential premises are generally taxable, which
   changes both the GST on sale and the purchaser's withholding obligation at settlement.
3. **Are they commercial residential premises?** Hotels, motels and similar are taxable, not input
   taxed. Short-stay accommodation sits near this boundary and needs the actual facts.
4. **Is it commercial property?** Generally taxable, subject to registration and turnover.
5. **Does an entity-level test change the answer?** Registration, the $75,000 threshold, and
   whether the activity amounts to an enterprise all sit upstream of the supply classification.
6. **Does a special rule apply on sale?** The margin scheme, the going concern exemption and GST
   at settlement each have their own conditions.

The full rules are in `au-gst-property.md` and `australia-gst.md`. Do not decide a property GST
question from this file alone.

### 8.3 State and territory taxes are not federal, and are not uniform

Land tax, transfer duty, foreign purchaser and foreign owner surcharges, and vacancy or short-stay
levies are imposed by each state and territory under its own Act. Thresholds, rates, exemptions,
aggregation rules, trust surcharges and the definition of a principal place of residence all
differ. A rule from one jurisdiction must never be applied to another.

Establish the jurisdiction first, then read that jurisdiction's own guidance:

**Jurisdiction revenue authorities**

| Jurisdiction | Revenue authority |
| --- | --- |
| New South Wales | Revenue NSW, https://www.revenue.nsw.gov.au/ |
| Victoria | State Revenue Office Victoria, https://www.sro.vic.gov.au/ |
| Queensland | Queensland Revenue Office, https://qro.qld.gov.au/ |
| Western Australia | RevenueWA (Department of Treasury and Finance), https://www.wa.gov.au/organisation/department-of-treasury-and-finance |
| South Australia | RevenueSA, https://www.revenuesa.sa.gov.au/ |
| Tasmania | State Revenue Office Tasmania, https://www.sro.tas.gov.au/ |
| Australian Capital Territory | ACT Revenue Office, https://www.revenue.act.gov.au/ |
| Northern Territory | Territory Revenue Office, https://treasury.nt.gov.au/dtf/territory-revenue-office |

Land tax paid on an income-producing property is generally deductible in the year it is incurred.
Transfer duty on the purchase is not deductible; it is a cost base element. See `au-land-tax.md`
and `au-stamp-duty.md` for the jurisdiction-specific detail.

### 8.4 Related guides

**Related guides**

| Question | Guide |
| --- | --- |
| GST on a property sale, margin scheme, GST at settlement | `au-gst-property.md` |
| CGT calculation, losses, discount, the 1 July 2027 changes | `au-capital-gains.md` |
| Land tax by jurisdiction | `au-land-tax.md` |
| Transfer duty by jurisdiction | `au-stamp-duty.md` |
| Reporting the rental schedule in the return | `au-individual-return.md` |
| Deductions and offsets generally | `au-deductions-offsets.md` |
| Foreign resident disposals | `au-nonresident-cgt.md` |
| Property held in a trust or SMSF | `au-trust-distributions.md`, `au-smsf.md` |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by Ryan Duguid.

## Sources

These sources support selected receipt-year, borrowing expense, repair, travel, asset, interest, capital works, 2027 restriction, disposal/foreign-resident and private/holiday-use boundaries in Sections 2.1-2.9 and 6.1-6.3 and their cross-references. They do not establish the currency of every other rule or return field in this guide.

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| ITAA 1997, s 25-25(1)-(6), corroborated against compilation 268 volume 1. Read the aggregate income-producing $100 threshold, day-based method, loan-period definition, private-use apportionment and early repayment. | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-25 | 2026-11-12 |
| ATO TR 97/23. Read selected paragraphs 4-5, 16, 35, 43-57 and 59-66 for function/materials, separable actual repairs, initial repairs and later deterioration. | https://www.ato.gov.au/law/view/document?docid=TXR/TR9723/NAT/ATO/00001 | 2026-11-12 |
| ATO TR 2000/2. Read paragraphs 15-18 and 43-47 for ordinary proportional repayments, recouped-fund and refinancing exceptions and interest tracing. | https://www.ato.gov.au/law/view/document?docid=TXR/TR20002/NAT/ATO/00001 | 2026-11-12 |
| ITAA 1997 compilation 268, volume 3. Read for selected operative cost base, proceeds, discount, foreign-resident market-value and absence provisions, including ss 110-25, 110-35, 110-38(8A), 110-45, 110-55 including (9JA), 115-100, 115-105, 115-115, 116-20 and 118-145. The general individual/trust discount is time-limited to events before 1 July 2027. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2026-11-12 |
| ATO capital proceeds. Read for money/property proceeds, market-value substitutions and specified reductions. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/capital-proceeds-from-disposing-of-assets | 2026-11-12 |
| ATO cost base. Read for the 5 elements, buying/selling incidental costs and reduced cost base differences. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cost-base-of-asset | 2026-11-12 |
| ATO capital works adjustments. Read for claimed/claimable treatment and date/information exceptions. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cost-base-adjustments-for-capital-works | 2026-11-12 |
| ATO TD 2005/47. Read for paragraphs 1-4 and the omitted-claim example on deduction and CGT amendment periods. | https://www.ato.gov.au/law/view/document?DocID=TXD/TD200547/NAT/ATO/00001&PiT=99991231235958 | 2026-11-12 |
| ATO PS LA 2006/1 (GA). Read for sections 1-3, including both insufficient-information conditions. | https://www.ato.gov.au/law/view/document?DocID=PSR/GA20061/NAT/ATO/00001&PiT=99991231235958 | 2026-11-12 |
| ATO Rental properties 2026, rental expenses. Read selected travel, interest/renovation, vacant-land, second-hand asset and capital works subsections, linked interpretations, the annual deduction base and changes in building ownership. This annual guide concerns 2025-26; selected statutes and rulings are considered separately for 2026-27. | https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/rental-expenses | 2026-11-12 |
| ATO Rental properties 2026, other tax considerations. Read for contract timing, gain/loss definitions, cost base, depreciating-asset apportionment and PAYG instalments. | https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/other-tax-considerations | 2026-11-12 |
| ATO capital losses and CGT discount. Read for losses before discount, the 12-month test and exclusions. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/using-capital-losses-to-reduce-capital-gains | 2026-11-12 |
| ATO CGT discount. Read for eligibility, acquisition/disposal day exclusion and discount calculation. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount | 2026-11-12 |
| ATO CGT discount for foreign residents, updated 9 October 2026. Read for post-8 May 2012 residence apportionment and the earlier-asset market-value method, including a possible full 50% discount. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/cgt-discount-for-foreign-residents | 2026-11-12 |
| ATO foreign-resident main residence exemption. Read for disposal status, life events test and denial of partial/first-income-use relief where the test is not met. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents | 2026-11-12 |
| ATO former home main residence. Read for income/non-income absence choices and the changing-residences exception. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/treating-former-home-as-main-residence | 2026-11-12 |
| ATO home used for rental or business. Read for partial exemption and first-income-use valuation routing. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/using-your-home-for-rental-or-business | 2026-11-12 |
| ATO foreign and temporary resident income, PDF pages 10-11. Read for Australian-source rental declaration separately from interest/dividend/royalty withholding. | https://www.ato.gov.au/api/public/content/0-9fc0474e-7b95-4e02-8b6a-580471487f4c | 2026-11-12 |
| ATO FRCGW overview. Read for property-sale scope, market-value base, contract-date rates and purchaser settlement obligations. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview | 2026-11-12 |
| ATO resident clearance certificates. Read for resident eligibility, settlement timing and legislative-instrument exceptions. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/australian-residents-and-clearance-certificates | 2026-11-12 |
| ATO FRCGW variations, updated 9 October 2026. Read for eligibility, notice timing, credit and return treatment. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-residents-capital-gains-withholding-variations | 2026-11-12 |
| ATO rental income you must declare, updated 21 May 2026. Read for Rental income and completing your tax return, gross rent before agent costs, tenant-to-agent payment timing and legal ownership share. | https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-income-you-must-declare | 2026-11-12 |
| ITAA 1997 compilation 268, volume 2, retained 1 October 2026 text. Read s 40-27(1)-(6) and selected ss 43-15, 43-115, 43-210, 43-215 and 43-230 to 43-240, including formula image alt text, original-expenditure base, use adjustments and the undeducted cap. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html | 2026-11-12 |
| ITAA 1997 compilation 268, volume 1. Read selected ss 26-31, 26-50, 26-102 and 26-155 to 26-160 for travel/entity exceptions, leisure-facility denial, vacant-land holding costs and the 2027 restriction boundaries. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| Act 49 as made. Read s 2 Schedule 2 commencement and Schedule 2 item 5 application to 2027-28 and later years. | https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-12 |
| Act 71 as made. Read s 2 and Schedule 4, including inherited/co-owner/relationship-breakdown extensions and application. | https://www.legislation.gov.au/C2026A00071/asmade/text | 2026-11-12 |
| ATO TR 2026/1, authorised PDF. Read selected paragraphs 20-48 for ordinary deductions, the holiday-home denial screen, separate direct rental costs and a clear change in main use. | https://www.ato.gov.au/law/view/pdf?DocId=TXR%2FTR20261%2FNAT%2FATO%2F00001&filename=law%2Fview%2Fpdf%2Fpbr%2Ftr2026-001.pdf&PiT=99991231235958 | 2026-11-12 |
| ATO PCG 2026/2, authorised PDF. Read paragraphs 10-17 and 29-47 for accepted direct/time/area methods, empty rooms in the owner's home and non-market family/friend arrangements. These are compliance methods, not an independent deduction entitlement. | https://www.ato.gov.au/law/view/pdf?DocId=COG%2FPCG20262%2FNAT%2FATO%2F00001&filename=law%2Fview%2Fpdf%2Fcog%2Fpcg2026-002.pdf&PiT=99991231235958 | 2026-11-12 |
| ATO TR 2004/4, authorised PDF. Read paragraphs 7-9 for use of borrowings, the character of interest and all listed pre-income nexus conditions. | https://www.ato.gov.au/law/view/pdf?DocId=TXR%2FTR20044%2FNAT%2FATO%2F00001&filename=law%2Fview%2Fpdf%2Fpbr%2Ftr2004-004c3.pdf&PiT=99991231235958 | 2026-11-12 |

Not yet confirmed: Applicable new-dwelling/purpose instruments and later changes to the selected October 2026 provisions remain unverified. Other numerical rules, commencement details and return fields outside the selected scope above need their own current primary-source check. The final 2026-27 return labels and fields have not been verified. Separate rental collection and agency obligations remain unresolved in Section 2.9.
