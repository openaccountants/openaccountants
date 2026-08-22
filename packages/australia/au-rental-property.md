---
name: au-rental-property
description: Use this skill whenever asked about Australian rental property income and deductions. Trigger on phrases like "rental income Australia", "negative gearing", "rental deductions", "investment property tax", "Division 40", "Division 43", "capital works deduction", "depreciation schedule", "rental property CGT", "rental withholding", "body corporate fees", "strata levy deduction", "repairs vs improvements", "TR 97/23", or any question about completing the rental property schedule in an Australian individual tax return. This skill covers rental income reporting, deductible expenses, depreciation (Div 40 plant and Div 43 building), negative gearing, CGT on disposal, non-resident withholding, and common transaction classifications. ALWAYS read this skill before touching any Australian rental property work.
version: "1.1"
jurisdiction: AU
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Rental Property

## Australia Rental Property -- Income & Deductions Skill v1.0

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax | Income Tax -- Rental Property Schedule |
| Currency | AUD only |
| Tax year | 1 July 2024 -- 30 June 2025 |
| Primary legislation | Income Tax Assessment Act 1997 (ITAA 1997) |
| Supporting legislation | ITAA 1936; Tax Ruling TR 97/23 (repairs vs improvements); TD 2024/3 (car expenses); PS LA 2008/4 (non-commercial losses) |
| Tax authority | Australian Taxation Office (ATO) |
| Filing portal | myTax / tax agent lodgement (Online Services for Agents) |
| Filing deadline | 31 October (self-lodgement); agent-managed deadlines vary |
| Skill version | 1.0 |

### Key Thresholds (2024-25)

**Key Thresholds (2024-25)**

| Item | Value |
| --- | --- |
| Tax-free threshold | $18,200 |
| Medicare levy | 2% of taxable income |
| Medicare levy surcharge (no PHI) | 1% -- 1.5% above $93,000 (single) |
| CGT discount (individuals, 12+ months) | 50% |
| Div 43 rate (post-Sep 1987 residential) | 2.5% of construction cost |
| Div 43 rate (post-Feb 1992 short-term traveller) | 4% |
| Low-value asset pool threshold | $1,000 (Div 40) |
| Immediate deduction threshold (Div 40) | $300 |

### Individual Marginal Tax Rates (2024-25)

**Individual Marginal Tax Rates (2024-25)**

| Taxable Income (AUD) | Rate | Cumulative Tax at Top |
| --- | --- | --- |
| 0 -- 18,200 | 0% | $0 |
| 18,201 -- 45,000 | 16% | $4,288 |
| 45,001 -- 135,000 | 30% | $31,288 |
| 135,001 -- 190,000 | 37% | $51,638 |
| 190,001+ | 45% | -- |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown apportionment (private vs rental) | 0% deductible |
| Unknown whether repair or improvement | Treat as improvement (capitalise) |
| Unknown construction cost for Div 43 | Do not claim -- obtain quantity surveyor report |
| Unknown settlement date for CGT | Do not compute -- obtain contract |
| Unknown cost base | Do not compute CGT -- escalate |

## Section 2 -- Classification Rules

### 2.1 Rental Income

- **All gross rental income** — All gross rental income is assessable. Report at Item 21 (Rent) on the Individual Tax Return.

**Rental Income Types**

| Income Type | Treatment |
| --- | --- |
| Rent received from tenant | Assessable -- full amount received or receivable |
| Bond forfeited (retained for damage) | Assessable in year retained |
| Insurance payout (loss of rent) | Assessable |
| Reimbursement from tenant (excess utilities) | Assessable |
| Key money / lease premium | Assessable |

### 2.2 Negative Gearing

- **Negative gearing** — Where total deductions exceed gross rental income, the net rental loss reduces other assessable income (salary, business income). There is no cap on negative gearing for existing or new properties (as of 2025 law).

### 2.3 Deductible Expenses (Immediate)

**Deductible Expenses (Immediate)**

| Expense | Treatment | Notes |
| --- | --- | --- |
| Interest on investment loan | Deductible | Must trace loan purpose to rental property |
| Council rates | Deductible | Apportioned if part-private |
| Water rates / charges | Deductible |  |
| Body corporate / strata fees | Deductible | Includes admin fund and sinking fund contributions |
| Land tax | Deductible |  |
| Property management fees | Deductible | Agent commissions, letting fees |
| Insurance (landlord, building, contents) | Deductible |  |
| Advertising for tenants | Deductible |  |
| Pest control | Deductible |  |
| Gardening / lawn mowing (if provided to tenant) | Deductible |  |
| Tax agent fee (rental schedule portion) | Deductible |  |
| Travel to property (removed from 1 Jul 2017) | NOT deductible | Unless carrying on a rental property business |

### 2.4 Repairs vs Improvements (TR 97/23)

**Repairs vs Improvements (TR 97/23)**

| Characteristic | Repair (immediate deduction) | Improvement (capitalise) |
| --- | --- | --- |
| Restores to original condition | Yes | No |
| Replaces with substantially same materials | Yes | No -- better quality/different character |
| Initial repair on acquisition | NOT deductible (capital) | Capital -- add to cost base |
| Replaces entire structure (e.g. full roof) | Capital (replacement) | Capital |
| Example: patching cracked tiles | Repair | -- |
| Example: replacing all tiles with stone | -- | Improvement |
| Example: replacing broken tap with same model | Repair | -- |
| Example: full kitchen renovation | -- | Improvement |

### 2.5 Division 40 -- Plant & Equipment Depreciation

Applies to removable/mechanical assets within the property.

**Division 40 Effective Lives**

| Asset | Effective Life (ATO) | Decline Method |
| --- | --- | --- |
| Hot water system | 12 years | Diminishing value or prime cost |
| Carpet | 8 years | Either |
| Blinds / curtains | 8 years | Either |
| Oven / cooktop | 12 years | Either |
| Air conditioning (split system) | 10 years | Either |
| Dishwasher | 8 years | Either |
| Smoke alarm | 6 years | Either |
| Ceiling fan | 10 years | Either |

- **Diminishing value rate** — 200% ÷ effective life
- **Prime cost rate** — 100% ÷ effective life
- **Limitation (from 1 Jul 2017)** — For residential rental properties, only the first owner (or entity that had the asset newly installed) can claim Div 40 deductions. Subsequent owners cannot claim plant & equipment depreciation on existing assets -- they inherit zero depreciable value for previously used items (unless an exception applies, e.g., refurbishment by new owner).

### 2.6 Division 43 -- Capital Works Deduction

Applies to the structural elements (building itself, fixed improvements).

**Division 43 Capital Works Deduction Rates**

| Construction Date | Rate | Notes |
| --- | --- | --- |
| Before 18 July 1985 | 0% | No deduction available |
| 18 Jul 1985 -- 15 Sep 1987 | 4% | Residential/non-residential |
| After 15 Sep 1987 (residential) | 2.5% | 40-year write-off |
| After 15 Sep 1987 (short-term traveller) | 4% | Certain accommodation |

- **Base** — Original construction cost (obtain from quantity surveyor report or builder records). NOT the purchase price of the property.
- **Undeducted construction cost** — Undeducted construction cost passes to new owner on sale -- the new owner continues the 2.5% deduction on the remaining undeducted amount.

### 2.7 Interest Deductibility

- **Nexus requirement** — The loan must have a clear nexus to producing rental income. Key rules follow in the table.

**Interest Deductibility Scenarios**

| Scenario | Deductible? |
| --- | --- |
| Loan to purchase rental property | Yes -- full interest |
| Loan to renovate rental property | Yes -- full interest |
| Refinanced loan (same purpose, same or lower amount) | Yes |
| Loan redrawn for personal use | No -- apportioned |
| Line of credit (mixed purpose) | Must trace each drawdown |
| Interest on loan while property vacant (available for rent) | Yes |
| Interest during construction period | Deductible from date available for rent (or capitalised to cost base) |

### 2.8 CGT on Disposal

**CGT on Disposal Elements**

| Element | Treatment |
| --- | --- |
| Cost base | Purchase price + stamp duty + legal fees + capital improvements - Div 43 deductions claimed |
| Capital proceeds | Sale price - agent commission - legal fees on sale |
| Net capital gain | Proceeds - cost base |
| 50% CGT discount | Available if held 12+ months (individuals/trusts only) |
| Main residence exemption (partial) | Available if property was main residence for part of ownership period |
| 6-year absence rule | Treat as main residence for up to 6 years of absence if no other main residence claimed |
| Non-residents | No 50% discount (from 8 May 2012 for gains accruing after that date) |

### 2.9 Non-Resident Rental Withholding

**Non-Resident Rental Withholding Rules**

| Rule | Detail |
| --- | --- |
| Applies to | Non-resident landlords receiving Australian rental income |
| Rate | Payer (tenant/agent) must withhold amounts as directed by ATO |
| FRCGW (foreign resident CGT withholding) | 12.5% of sale price if property value ≥ $750,000 (buyer withholds) |
| Clearance certificate | Resident vendor obtains to avoid FRCGW at settlement |

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

- **Gross Rental Income** — Sum all assessable rental receipts for the financial year.

### Step 2: Immediate Deductions

- **Immediate Deductions** — Sum all allowable expenses (interest, rates, insurance, management fees, repairs, body corporate, etc.).

### Step 3: Depreciation (Div 40 + Div 43)

- **Depreciation** — Add capital works deduction (2.5% of construction cost) and plant depreciation (per ATO effective life schedules).

### Step 4: Net Rental Income / Loss

- **Net Rental Income / Loss** — Gross income − deductions − depreciation = net rental income (or loss if negative gearing).

### Step 5: Report on Tax Return

- **Reporting outcome** — Positive: included in assessable income and taxed at marginal rates. Negative: offsets other assessable income (salary, business) dollar-for-dollar.

## Section 5 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Form | Individual Tax Return (ITR) -- Rental Property Schedule (Item 21) |
| Reporting | Per-property basis (complete separate schedule for each property) |
| Joint ownership | Each co-owner reports their share (typically 50/50 for joint tenants) |
| Records retention | 5 years from date of lodgement (longer if CGT applies -- keep until 5 years after disposal) |
| Quantity surveyor report | Recommended for all post-1985 properties to substantiate Div 43 and Div 40 claims |

## Section 6 -- Edge Cases

### 6.1 Property Vacant

- **Vacancy deduction rule** — Expenses are deductible during vacancy ONLY if the property is genuinely available for rent (advertised, not restricted in availability). If withheld from the market (e.g., reserved for personal use or holiday), deductions are denied for that period.

### 6.2 Part-Year Rental / Part-Private Use

- **Apportionment rule** — Apportion all expenses on a time basis (days rented or available ÷ 365). Interest remains fully deductible if the property was available for the full year even if vacant.

### 6.3 Holiday Homes

- **Holiday home deduction limitation** — If the property is available for rent at below-market rates, or restricted to holiday periods only, or rented to relatives at reduced rates -- deductions are limited to income received (no negative gearing). ATO scrutinises holiday letting closely.

### 6.4 Subdivision and Development

- **Subdivision profit treatment** — If a rental property is subdivided, the profit on sale of subdivided lots may be ordinary income (not CGT) if the taxpayer has a profit-making intention. Escalate to specialist.

### 6.5 Deceased Estates

- **Deceased estate rental treatment** — Rental property passing through an estate: the legal personal representative (LPR) reports rental income in the estate return until the property is transferred to a beneficiary. CGT is deferred until the beneficiary disposes.

## Section 7 -- Prohibitions

- **Prohibitions** — NEVER claim travel to a residential rental property as a deduction (removed from 1 July 2017 for non-business landlords); NEVER claim Div 40 plant depreciation for a subsequent owner of residential property (post-2017 rule) unless the asset was newly installed by that owner; NEVER claim Div 43 without evidence of construction cost (quantity surveyor report or original builder records); NEVER deduct loan principal repayments; NEVER deduct expenses relating to periods of genuine private use without apportionment; NEVER claim the CGT 50% discount for a non-resident individual; NEVER omit prior Div 43 deductions from the cost base on disposal (reduces cost base); NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
