---
name: uk-rental-sa105
description: Use this skill whenever asked about UK property income or rental income for individuals. Trigger on phrases like "SA105", "rental income UK", "property income", "buy-to-let", "letting income", "landlord tax UK", "rent-a-room", "mortgage interest relief", "Section 24", "property allowance", "non-resident landlord scheme", "NRLS", "furnished holiday let", "FHL abolished", "FHL abolition", "repairs deduction", "letting agent fees", "property expenses", "UK property pages", "April 2026 property tax", "property income hike", "MTD ITSA landlord", or any question about computing, filing, or reporting UK property income on a Self Assessment tax return. Covers SA105 form structure, allowable expenses, mortgage interest restriction, Rent-a-Room relief, property income allowance, non-resident landlord scheme, the abolition of FHL rules, and the April 2026 property income rate change announced at Autumn Budget 2025. ALWAYS read this skill before touching any UK rental income work.
version: 1.1
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Power
review_status: current
depends_on:
  - uk-income-tax-sa100
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Rental Sa105

## UK Property Income (SA105) Skill v1.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **James Power** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Rental SA105

- **Property income allowance** — £1,000  _(ITTOIA 2005)_
- **Rent-a-Room threshold** — £7,500/year (£3,750 if joint)  _(ITTOIA ss.784-802)_
- **Mortgage interest deductible as expense?** — NO — tax credit at 20% of finance costs  _(ITA 2007 ss.274A-274D)_
- **FHL status from 2025-26** — Abolished — treated as normal property income  _(Finance Act 2025)_

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Tax | Income Tax on Property Income |
| Currency | GBP only |
| Tax year | 6 April to 5 April (2025-26: 6 April 2025 -- 5 April 2026) |
| Primary legislation | Income Tax (Trading and Other Income) Act 2005 (ITTOIA), Part 3 |
| Supporting legislation | Income Tax Act 2007, ss. 274A-274D (mortgage interest restriction); ITTOIA ss. 784-802 (Rent-a-Room); Finance Act 2025 (FHL abolition); Finance (No. 2) Bill 2024-26 (April 2026 property income rate change — pending enactment) |
| Tax authority | HM Revenue and Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline (online) | 31 January following the tax year |
| Filing deadline (paper) | 31 October following the tax year |
| SA105 form | UK Property supplementary pages to SA100 |
| Validated by | Verified by James Power on 2026-06-03 |
| Skill version | 1.1 |

### Year Comparison — Quick Reference (Prior / Current / Future)

**Year Comparison Quick Reference table**

| Item | 2024-25 (Prior year) | 2025-26 (Current year) | 2026-27 (From 6 April 2026) |
| --- | --- | --- | --- |
| Personal allowance | £12,570 | £12,570 (frozen) | £12,570 (frozen) |
| Basic rate band | £12,571 -- £50,270 | £12,571 -- £50,270 (frozen) | £12,571 -- £50,270 (frozen) |
| Basic rate on property income | 20% | 20% | **TBC — Autumn Budget 2025 announced increase to property income tax from April 2026; specific rates to be confirmed when Finance (No. 2) Bill 2024-26 enacted** (expected basic +2pp ≈ 22%) |
| Higher rate on property income | 40% | 40% | **TBC — see above** (expected higher +2pp ≈ 42%) |
| Additional rate on property income | 45% | 45% | **TBC — pending Finance (No. 2) Bill 2024-26 enactment** |
| Property income allowance | £1,000 | £1,000 (frozen since 2017-18) | £1,000 (frozen) |
| Rent-a-Room threshold | £7,500 | £7,500 (frozen) | £7,500 (frozen) |
| FHL regime | In force (last year) | **Abolished from 6 April 2025** (transitional rules) | Abolished (transitional rules continue) |
| Section 24 mortgage interest restriction | Full restriction — 20% basic rate tax reducer | Same | Same (tax reducer rate may follow new basic rate — TBC) |
| MTD ITSA for landlords | Not in scope | Not in scope | **Phase 1 from 6 April 2026 — gross income > £50,000** |
| MTD ITSA Phase 2 | n/a | n/a | Phase 2 from April 2027 — gross income > £30,000 |

### SA105 Key Boxes (2024-25 and 2025-26)

**SA105 Key Boxes table**

| Box | Description | Section |
| --- | --- | --- |
| Box 3 | Joint property income indicator | Header |
| Box 4 | Rent-a-Room relief (rents ≤£7,500) | Rent-a-Room |
| Box 5 | Total rents and income from property (FHL section) | FHL — abolished from 2025-26 |
| Box 20 | Total rents and other income from property | Property income |
| Box 20.1 | Property income allowance (£1,000) | Allowance |
| Box 24 | Rent, rates, insurance and ground rents | Expenses |
| Box 25 | Property repairs and maintenance | Expenses |
| Box 26 | Loan interest and other financial costs | Expenses |
| Box 27 | Legal, management and other professional fees | Expenses |
| Box 28 | Costs of services provided, including wages | Expenses |
| Box 29 | Other allowable property expenses | Expenses |
| Box 30 | Private use adjustment | Expenses |
| Box 36 | Replacement of domestic items relief | Expenses |
| Box 37 | Rent-a-Room exempt amount | Relief |
| Box 38 | Adjusted profit for the year | Computed |
| Box 39 | Loss brought forward from earlier years | Losses |
| Box 40 | Taxable profit (Box 38 minus Box 39) | Final |

Note: Box layout for 2026-27 is expected to be substantially similar but TBC — confirm against HMRC's published 2026-27 SA105 when released.

### Income Tax Rates — 2024-25 (Prior Year)

**Income Tax Rates 2024-25 table**

| Band | Taxable income | Rate |
| --- | --- | --- |
| Personal allowance | Up to £12,570 | 0% |
| Basic rate | £12,571 -- £50,270 | 20% |
| Higher rate | £50,271 -- £125,140 | 40% |
| Additional rate | Over £125,140 | 45% |

### Income Tax Rates — 2025-26 (Current Year)

**Income Tax Rates 2025-26 table**

| Band | Taxable income | Rate |
| --- | --- | --- |
| Personal allowance | Up to £12,570 | 0% |
| Basic rate | £12,571 -- £50,270 | 20% |
| Higher rate | £50,271 -- £125,140 | 40% |
| Additional rate | Over £125,140 | 45% |

Property income is added to all other income and taxed at the marginal rate.

### Income Tax Rates on Property Income — 2026-27 (From 6 April 2026)

**STATUS: TBC — Autumn Budget 2025 announced increase to property income tax from April 2026; specific rates to be confirmed when Finance (No. 2) Bill 2024-26 enacted.**

The Autumn Budget 2025 announced that property income will be taxed at differential (dividend-style) rates from 6 April 2026, with the basic rate expected to rise by 2pp and the higher rate by 2pp relative to current employment-income rates.

**Income Tax Rates on Property Income 2026-27 table**

| Band | Taxable property income | Rate (expected — TBC) |
| --- | --- | --- |
| Personal allowance | Up to £12,570 | 0% |
| Basic rate (property) | £12,571 -- £50,270 | ~22% (TBC) |
| Higher rate (property) | £50,271 -- £125,140 | ~42% (TBC) |
| Additional rate (property) | Over £125,140 | TBC |

DO NOT use the expected rates above for any client computation until Finance (No. 2) Bill 2024-26 receives Royal Assent and HMRC publishes the confirmed rates. Until then, treat all 2026-27 property income tax computations as ESTIMATED and clearly flag them as TBC.

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown property use (residential vs commercial) | Treat as residential (mortgage interest restriction applies) |
| Unknown whether jointly owned | STOP — affects share of income/expenses |
| Unknown residency status | STOP — NRLS rules differ |
| Unknown repair vs improvement | Treat as improvement (not deductible) |
| Unknown private use percentage | 100% private (no deduction) |
| Unknown 2026-27 rates | Flag as TBC pending Finance (No. 2) Bill 2024-26 enactment; do not finalise figures |

## Section 2 -- Allowable Expenses

### 2.1 Fully Deductible Revenue Expenses

**Fully Deductible Revenue Expenses table**

| Expense | SA105 Box | Notes |
| --- | --- | --- |
| Letting agent fees / management charges | Box 27 | Percentage of rent or fixed fee |
| Insurance (buildings, landlord liability, rent guarantee) | Box 24 | Property-specific insurance only |
| Council tax (if paid by landlord) | Box 24 | Only when landlord contractually pays |
| Ground rent / service charges | Box 24 | Leasehold obligations |
| Water rates (if paid by landlord) | Box 24 | Metered or unmetered |
| Accountancy fees (property accounts) | Box 27 | Attributable to property business |
| Legal fees (tenancy agreements, debt recovery) | Box 27 | Revenue legal costs only |
| Advertising for tenants | Box 29 | Online listings, newspaper ads |
| Travel to property (inspections, repairs) | Box 29 | Mileage at 45p/mile (first 10,000) then 25p |
| Stationery and postage | Box 29 | Property business related |
| Telephone costs (property business calls) | Box 29 | Apportioned if personal phone |

### 2.2 Repairs vs Improvements

**Repairs vs Improvements table**

| Deductible (Repairs) | NOT Deductible (Improvements) |
| --- | --- |
| Replacing broken boiler with equivalent | Installing central heating where none existed |
| Repainting after tenant departure | Adding an extension or conservatory |
| Fixing leaking roof (like-for-like) | Converting loft into habitable room |
| Replacing rotten window frames (like-for-like) | Upgrading single glazing to double glazing |
| Re-plastering damaged walls | Rewiring entire property (if improvement) |

- **HMRC principle for repair vs improvement** — Does it restore the asset to its original condition (repair) or improve/enhance it (capital)?

### 2.3 Replacement of Domestic Items Relief (Box 36)

From April 2016, for residential lets:
- Claim the cost of replacing a domestic item (furniture, furnishings, appliances, kitchenware)
- The ORIGINAL purchase cost is NOT deductible — only replacements
- If the replacement is an improvement, only the cost of an equivalent replacement is deductible
- Domestic items include: beds, sofas, carpets, curtains, white goods, televisions, crockery

### 2.4 Mortgage Interest Restriction (Section 24)

From 2020-21, finance costs for residential property are **fully restricted**:

**Mortgage Interest Restriction table**

| Component | Treatment (2024-25, 2025-26) | Treatment (2026-27) |
| --- | --- | --- |
| Mortgage interest | NOT deductible as an expense | NOT deductible as an expense (unchanged) |
| Arrangement fees (revenue portion) | NOT deductible as an expense | NOT deductible as an expense (unchanged) |
| Tax credit | 20% of the lower of: (a) finance costs, (b) property profits, (c) adjusted total income | Rate may follow new basic rate — TBC pending Finance (No. 2) Bill 2024-26 |

- **Restriction applies to** — Individual landlords (not companies); Residential property lettings only; Partnerships of individuals
- **Restriction does NOT apply to** — Companies (corporate landlords can still deduct interest); Commercial property lettings; Previously Furnished Holiday Lets — but FHL regime is abolished from April 2025

**Box 26** on SA105 still captures finance costs, but HMRC computes the basic rate reduction separately on the tax computation.

### 2.5 Property Income Allowance (£1,000)

- **Property income allowance rules** — If gross property income is £1,000 or less: no need to report or register for Self Assessment. If gross property income exceeds £1,000: choose between claiming the £1,000 allowance (no expenses deducted) or deducting actual expenses. Cannot claim both the allowance and expenses. Cannot claim if income is from a connected person (employer, family company). Allowance remains £1,000 across 2024-25, 2025-26 and 2026-27 (frozen since 2017-18)

## Section 3 -- Rent-a-Room Relief

**Rent-a-Room Relief table**

| Feature | Detail (2024-25, 2025-26, 2026-27) |
| --- | --- |
| Threshold | £7,500 per year (£3,750 if letting jointly) — frozen across all three years |
| Requirement | Must let furnished accommodation in your only or main home |
| If income ≤ threshold | Put 'X' in Box 4; no further property pages needed |
| If income > threshold | Option 1: Tax on excess (income minus £7,500 in Box 37, no expenses); Option 2: Normal profit calculation (ignore Box 37) |
| Cannot combine with | Property income allowance (choose one or the other) |
| Does NOT apply to | Unfurnished rooms, separate self-contained flats, non-main-residence |

## Section 4 -- Furnished Holiday Lets (FHL) -- Abolished from 6 April 2025

### Pre-April 2025 (2024-25 — Prior Year)

- **FHL status requirements** — FHL status required meeting ALL of: Available for letting ≥210 days per year; Actually let ≥105 days per year; Not let to the same person for >31 consecutive days (total such lets <155 days)

FHL benefits included: full mortgage interest deduction, capital allowances on furniture, CGT reliefs (Entrepreneurs'/BADR, rollover), pension-relevant earnings.

### From 6 April 2025 (2025-26 — Current Year)

- **FHL regime abolished** — The FHL regime is **abolished** by Finance Act 2025: All former FHLs are treated as standard residential property; Mortgage interest restriction (Section 24) applies; No capital allowances on furniture (replacement of domestic items relief instead); CGT: no BADR, no rollover relief (standard residential CGT rates apply); Not pension-relevant earnings  _(Finance Act 2025)_

**Transitional provisions (2025-26):** Overlap relief and brought-forward FHL losses remain available in 2025-26.

### From 6 April 2026 (2026-27 — Future Year)

- **FHL transitional rules continuing effects** — FHL transitional rules continue to affect 2026-27 returns where: Brought-forward FHL losses pre-6-April-2025 are still being utilised against UK property business profits; Capital allowances pools established under the FHL regime continue to run off; CGT computations on disposal of former FHL properties still reference pre-abolition base costs

Confirm any residual FHL transitional position with the taxpayer's prior accountant or prior-year computations before finalising 2026-27 figures.

## Section 5 -- Non-Resident Landlord Scheme (NRLS)

**NRLS table**

| Feature | Detail |
| --- | --- |
| Applies to | Landlords whose "usual place of abode" is outside the UK |
| Withholding | Letting agent or tenant must withhold basic rate tax (20%) from rent and pay to HMRC quarterly |
| HMRC approval | Non-resident can apply to receive rent gross (form NRL1) if tax affairs are up to date |
| Annual return | Non-resident must still file SA100 + SA105 (or SA700 for companies) |
| Expenses | Same rules apply — agent may deduct allowable expenses before withholding |
| 2026-27 note | Withholding rate may change if 2026-27 basic rate on property income is enacted — TBC |

## Section 6 -- Transaction Pattern Library

### 6.1 Income Patterns (Credits)

**Income Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TENANT RENT, STANDING ORDER [tenant name] | Box 20 -- rental income | Monthly rent receipts |
| LETTING AGENT DEPOSIT, FOXTONS, OPENRENT | Box 20 -- rental income | Agent-collected rent (gross up if agent deducts fees) |
| AIRBNB PAYOUT, BOOKING.COM | Box 20 -- rental income | Short-term platform income; may also be Rent-a-Room eligible |
| TENANT DEPOSIT (via DPS, TDS, mydeposits) | EXCLUDE | Refundable deposit — not income unless forfeited |
| DEPOSIT RETENTION, DAMAGE DEDUCTION | Box 20 -- rental income | Retained deposit = income in the year retained |
| HMRC REFUND, TAX REFUND | EXCLUDE | Not rental income |

### 6.2 Expense Patterns (Debits)

**Expense Patterns table**

| Pattern | SA105 Box | Notes |
| --- | --- | --- |
| MORTGAGE, NATIONWIDE, BARCLAYS MORTGAGE | Box 26 (finance costs) | Subject to Section 24 restriction — 20% credit only (2026-27 rate TBC) |
| BUILDINGS INSURANCE, LANDLORD INSURANCE | Box 24 | Fully deductible |
| LETTING AGENT FEE, MANAGEMENT FEE | Box 27 | Fully deductible |
| PLUMBER, ELECTRICIAN, BUILDER [repair] | Box 25 | Deductible if repair; capital if improvement |
| GAS SAFETY, ELECTRICAL CERTIFICATE, EPC | Box 29 | Regulatory compliance — fully deductible |
| COUNCIL TAX (landlord-paid void period) | Box 24 | Deductible during void periods between tenants |
| GROUND RENT, SERVICE CHARGE | Box 24 | Leasehold costs |
| CLEANING, END OF TENANCY CLEAN | Box 29 | Between-tenant cleaning |
| JOHN LEWIS, CURRY'S [replacement appliance] | Box 36 | Replacement of domestic items relief |
| ACCOUNTANT, TAX RETURN FEE | Box 27 | Property portion only |
| FURNITURE, BED, SOFA [replacement] | Box 36 | Replacement only — not first purchase |

### 6.3 Exclusions

**Exclusions table**

| Pattern | Treatment |
| --- | --- |
| MORTGAGE CAPITAL REPAYMENT | EXCLUDE — not an expense |
| PROPERTY PURCHASE, STAMP DUTY, SOLICITOR (acquisition) | EXCLUDE — capital cost (relevant to CGT on disposal) |
| PERSONAL USE EXPENSES | EXCLUDE — private use |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE |

## Section 7 -- Worked Examples

### Example 1 -- Basic Buy-to-Let (2024-25 — Prior Year)

**Input:** Annual rent £12,000. Mortgage interest £4,000. Agent fees £1,200. Insurance £300. Repairs £800. No other property income. Basic rate taxpayer.

**Computation:**
```
Box 20: £12,000
Box 24: £300 (insurance)
Box 25: £800 (repairs)
Box 26: £4,000 (finance costs — restricted)
Box 27: £1,200 (agent fees)

Profit before finance costs: £12,000 - £300 - £800 - £1,200 = £9,700
Finance cost deduction: £0 (fully restricted for residential)
Property profit: £9,700
Tax at 20% (basic rate): £1,940
Finance cost tax credit: 20% × £4,000 = £800
Net tax on property income: £1,940 - £800 = £1,140
```

### Example 2 -- Same Buy-to-Let (2025-26 — Current Year)

**Input:** As Example 1, unchanged in 2025-26 (rates and allowances frozen). Annual rent £12,000. Mortgage interest £4,000. Agent fees £1,200. Insurance £300. Repairs £800. Basic rate taxpayer.

**Computation:** Identical to Example 1 — basic rate of 20% and 20% finance cost credit unchanged.
```
Property profit: £9,700
Tax at 20%: £1,940
Finance cost tax credit: 20% × £4,000 = £800
Net tax on property income: £1,140
```

If the property was previously an FHL (pre-6-April-2025), confirm any brought-forward FHL loss in Box 39 and that capital allowances pools have been correctly transitioned.

### Example 3 -- Same Buy-to-Let (2026-27 — From 6 April 2026, TBC)

**Input:** As Example 1. Basic rate taxpayer.

**Computation (PRELIMINARY — flagged TBC):**
```
Property profit: £9,700
Tax at expected ~22% (basic rate on property income — TBC pending Finance (No. 2) Bill 2024-26): ~£2,134
Finance cost tax credit: expected ~22% × £4,000 = ~£880 (rate of credit TBC)
Net tax on property income: ~£1,254 (TBC)

Estimated additional tax versus 2025-26: ~£114 (≈ 10% increase in tax on this rental profit)
```

**STATUS: TBC — Autumn Budget 2025 announced increase to property income tax from April 2026; specific rates to be confirmed when Finance (No. 2) Bill 2024-26 enacted.** Do not present these figures as final. Re-run once Royal Assent confirms the exact rates and the credit rate for Section 24.

### Example 4 -- Rent-a-Room (Under Threshold)

**Input:** Rents out furnished spare bedroom in main home. Annual income £6,000. (Same in all three years — threshold frozen at £7,500.)

**Computation:** Income £6,000 < £7,500 threshold. Put 'X' in Box 4. No further SA105 needed. Tax = £0 on this income.

### Example 5 -- Rent-a-Room (Over Threshold)

**Input:** Spare room income £10,000.

**Option A (Rent-a-Room exemption method):**
```
Taxable = £10,000 - £7,500 = £2,500
No expenses can be deducted alongside
```

**Option B (Normal calculation):**
```
If actual expenses are £4,000: profit = £10,000 - £4,000 = £6,000
```
Option A (£2,500 taxable) is better than Option B (£6,000 taxable).

For 2026-27, the calculation is identical; the only change is the tax rate applied to the taxable amount (TBC).

### Example 6 -- Higher Rate Taxpayer with Section 24 Restriction (2025-26)

**Input:** Total income £80,000 (employment) + £15,000 rent. Mortgage interest £8,000. Other expenses £3,000.

**Computation:**
```
Property profit: £15,000 - £3,000 = £12,000
Taxed at 40% (higher rate): £4,800
Finance cost tax credit: 20% × £8,000 = £1,600
Net tax on property: £4,800 - £1,600 = £3,200

Effective tax rate on rent: £3,200 / £15,000 = 21.3%
Without Section 24: tax would be (£15,000 - £3,000 - £8,000) × 40% = £1,600
Section 24 cost to this taxpayer: £1,600 extra
```

For 2026-27, the higher rate on property income is expected to rise (~42% TBC), increasing the net tax — flag for taxpayer planning.

## Section 8 -- Losses

**Losses table**

| Rule | Detail |
| --- | --- |
| Property losses | Can only be carried forward against future property profits |
| Cannot be set against | Employment income, trading income, or other non-property income |
| Carry forward | Indefinite — no time limit |
| Capital allowances creating loss | Can create or increase a property loss |
| Multiple properties | All UK properties pooled into one property business |
| Box 39 | Losses brought forward from earlier years |
| FHL transitional losses | Pre-6-April-2025 FHL losses absorbed into the UK property business loss pool; carry forward indefinitely against UK property profits in 2025-26, 2026-27 and beyond |

## Section 9 -- Edge Cases

### 9.1 Void Periods

- **Void periods deduction rule** — Expenses incurred between tenants (council tax, insurance, marketing) remain deductible provided the property is available for letting and the landlord is actively seeking a new tenant.

### 9.2 Mixed-Use Property

- **Mixed-use apportionment** — If the landlord lives in part of the property and lets another part, apportion expenses by floor area or rooms. Only the letting portion is deductible.

### 9.3 Cash Basis vs Traditional Accounting

- **Cash basis default and election** — Default for property income from 2017-18: cash basis (income when received, expenses when paid). Can elect traditional (accruals) accounting by ticking Box 20.2.
- **Threshold for mandatory cash basis** — £150,000 gross receipts

### 9.4 Property Income Allowance vs Expenses

- **Comparison rule** — If gross rental income is low (near £1,000), compare: claiming £1,000 allowance (no expenses) vs deducting actual expenses. Choose whichever gives the lower taxable amount.

### 9.5 Residential Property Developer Tax (RPDT)

- **RPDT scope** — RPDT continues at 4% on profits from UK residential property development. Applies to large corporate developers only (annual allowance £25m). Out of scope for individual landlords filing SA105 — flagged here for awareness only.

## Section 10 -- From 6 April 2026 (Forward-Looking Changes)

This section consolidates upcoming changes affecting UK property income that practitioners must flag to landlord clients during 2025-26 planning conversations.

### 10.1 Property Income Rate Change (Autumn Budget 2025)

- **Property income rate change details** — **STATUS: TBC — Autumn Budget 2025 announced increase to property income tax from April 2026; specific rates to be confirmed when Finance (No. 2) Bill 2024-26 enacted.** - HM Treasury announced at Autumn Budget 2025 that property income will be taxed at differential (dividend-style) rates from 6 April 2026. - Expected direction: basic rate +2pp (≈22%), higher rate +2pp (≈42%). Additional rate TBC. - Expected impact: ~10% increase in net tax on a typical basic-rate buy-to-let profit; larger impact at higher rate. - Section 24 finance cost tax reducer rate (currently 20%) may follow the new basic rate — TBC. - Action: do NOT finalise any 2026-27 client projection until Royal Assent. Caveat all 2026-27 projections as estimated.

### 10.2 Frozen Allowances and Thresholds

**Frozen Allowances and Thresholds table**

| Item | Amount | Frozen since |
| --- | --- | --- |
| Property income allowance | £1,000 | 2017-18 |
| Rent-a-Room threshold | £7,500 | 2016-17 |
| Personal allowance | £12,570 | 2021-22 |
| Higher rate threshold | £50,270 | 2021-22 |
| Additional rate threshold | £125,140 | 2023-24 |

Fiscal drag will continue to pull more landlords into higher and additional rate bands in 2026-27.

### 10.3 FHL Abolition — Continuing Transitional Impact

- **FHL abolition continuing impact** — FHL regime was abolished from 6 April 2025 by Finance Act 2025. The abolition continues to affect 2025-26 and 2026-27 returns through: Brought-forward FHL losses absorbed into the UK property business; Capital allowances pools running off (writing-down allowances continue on existing pools); CGT consequences on disposal of former FHL properties — no BADR, no rollover from 2025-26 disposals onwards; No new claims for FHL pension-relevant earnings

### 10.4 Making Tax Digital for Income Tax Self Assessment (MTD ITSA)

- **Phase 1 — from 6 April 2026** — Mandatory for self-employed individuals AND landlords with combined gross income > £50,000; Quarterly digital updates of income and expenses to HMRC via MTD-compatible software; Annual final declaration replaces aspects of the current SA100/SA105 cycle; Property income reported alongside trading income within a single MTD ITSA submission flow
- **Phase 2 — from 6 April 2027** — Threshold drops to gross income > £30,000; Significantly more landlords brought into scope

- Identify landlord clients with gross rental income > £50,000 — flag for MTD onboarding before April 2026
- Identify landlord clients with gross rental income > £30,000 — flag for April 2027 onboarding
- Discuss MTD-compatible software selection (HMRC publishes a list of approved providers)
- Plan quarterly update cadence and record-keeping changes (digital records required)

### 10.5 Section 24 Finance Cost Restriction — Continues

- **Section 24 continuation** — Section 24 mortgage interest restriction remains fully in force. The 20% basic rate tax reducer continues, though the rate at which the reducer applies in 2026-27 may follow any new basic rate on property income (TBC).

## PROHIBITIONS

- **Prohibition list** — NEVER deduct mortgage interest as an expense for residential property — it is a basic rate tax credit only (Section 24); NEVER allow the initial purchase cost of domestic items — only replacements qualify under Box 36; NEVER combine Rent-a-Room relief with the property income allowance; NEVER allow improvement costs as revenue deductions — these are capital; NEVER ignore the non-resident landlord scheme for overseas landlords; NEVER pool UK and overseas property into one computation — they are separate property businesses; NEVER apply FHL rules for 2025-26 onwards — the regime is abolished; NEVER present 2026-27 property income tax figures as final until Finance (No. 2) Bill 2024-26 receives Royal Assent — always label as TBC; NEVER assume the Section 24 tax reducer rate for 2026-27 is 20% without checking the enacted rate; NEVER present property income computations as definitive — always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
