---
name: my-income-tax
description: Use this skill whenever asked about Malaysia income tax for self-employed individuals or sole proprietors. Trigger on phrases like "Malaysia income tax", "LHDN", "Lembaga Hasil Dalam Negeri", "hasil.gov.my", "Form B", "Form BE", "Section 4(a)", "personal reliefs Malaysia", "chargeable income Malaysia", "tax deductions Malaysia", "Malaysian tax return", "e-Filing Malaysia", or any question about Malaysian income tax rates, filing, reliefs, or deductions for self-employed or business individuals. Covers progressive tax rates, business income, personal reliefs, deductions, and filing via e-Filing. ALWAYS read this skill before touching any Malaysia income tax work.
version: 1.0
jurisdiction: MY
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: MUHAMMAD HANIS MAT HUSSIN
review_status: current
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MY Income Tax

## Malaysia Income Tax -- Self-Employed Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Malaysia |
| Tax | Income Tax (Cukai Pendapatan) |
| Currency | MYR (Malaysian Ringgit / RM) only |
| Year of Assessment (YA) | Calendar year (1 January -- 31 December); YA 2025 = income earned in 2025 |
| Primary legislation | Income Tax Act 1967 (ITA 1967) |
| Tax authority | Lembaga Hasil Dalam Negeri Malaysia (LHDN) / Inland Revenue Board |
| Filing portal | MyTax e-Filing (https://mytax.hasil.gov.my) |
| Filing deadline -- employees | Form BE: 30 April (e-Filing: 15 May) |
| Filing deadline -- self-employed | Form B: 30 June (e-Filing: 15 July) |
| Validated by | Pending -- requires sign-off by a Malaysian tax agent |
| Validation date | Pending |
| Skill version | 1.0 |

### Progressive Tax Rates -- Resident Individuals (YA 2025)

**Progressive Tax Rates -- Resident Individuals (YA 2025)**

| Chargeable Income (RM) | Rate | Tax on Band | Cumulative Tax |
| --- | --- | --- | --- |
| 0 -- 5,000 | 0% | RM 0 | RM 0 |
| 5,001 -- 20,000 | 1% | RM 150 | RM 150 |
| 20,001 -- 35,000 | 3% | RM 450 | RM 600 |
| 35,001 -- 50,000 | 6% | RM 900 | RM 1,500 |
| 50,001 -- 70,000 | 11% | RM 2,200 | RM 3,700 |
| 70,001 -- 100,000 | 19% | RM 5,700 | RM 9,400 |
| 100,001 -- 400,000 | 25% | RM 75,000 | RM 84,400 |
| 400,001 -- 600,000 | 26% | RM 52,000 | RM 136,400 |
| 600,001 -- 2,000,000 | 28% | RM 392,000 | RM 528,400 |
| Above 2,000,000 | 30% | -- | -- |

### Non-Resident Tax Rate

- **Non-resident tax rate** — Flat 30% on all Malaysian-sourced income (no personal reliefs or deductions available).  _(ITA 1967)_

### Residency Test

- **Residency test** — Present in Malaysia for ≥182 days in a calendar year, or qualifying periods under Section 7 ITA 1967.  _(Section 7 ITA 1967)_

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | Non-resident (30% flat) until confirmed |
| Unknown business-use % | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown relief eligibility | Do not claim |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Required Inputs** — Minimum viable -- bank statement for the full year, confirmation of business type (sole proprietor, partnership, or professional), and residency status. Recommended -- all sales invoices, purchase invoices/receipts, EPF/SOCSO/EIS statements, prior year Form B and tax assessment (Borang J), business registration (SSM). Ideal -- complete accounting records (income statement and balance sheet), capital allowance schedule, partnership agreement (if applicable), prior year tax computation.

### Refusal Catalogue

- **R-MY-1** — Residency unknown. "Resident and non-resident individuals are taxed at very different rates. Cannot proceed without confirming residency status."
- **R-MY-2** — Company (Sdn Bhd) or LLP. "This skill covers sole proprietors and partnerships only. Companies file under corporate income tax (Form C). Escalate to a tax agent."
- **R-MY-3** — Cross-border income. "Foreign-sourced income remitted to Malaysia may be exempt or subject to tax under recent amendments. Escalate to a specialist."
- **R-MY-4** — Real property gains. "Real Property Gains Tax (RPGT) is a separate regime. Out of scope."

## Section 3 -- Business Income (Section 4(a) ITA 1967)

### 3.1 Computation of Adjusted Income

**Computation of Adjusted Income**

| Step | Description |
| --- | --- |
| Gross business income | Total revenue from business activities |
| Less: Allowable expenses (Section 33) | Expenses wholly and exclusively incurred in the production of income |
| = Adjusted income | Business profit before capital allowances |
| Less: Capital allowances (Schedule 3) | Depreciation per tax rules |
| Less: Unabsorbed losses brought forward | Prior year business losses (max 10 consecutive YA carry-forward from YA 2019) |
| = Statutory income from business |  |

### 3.2 Allowable Deductions (Section 33)

**Allowable Deductions (Section 33)**

| Category | Treatment |
| --- | --- |
| Cost of goods sold | Fully deductible |
| Staff salaries and EPF contributions | Fully deductible |
| Office rent (business premises) | Fully deductible |
| Utilities (business premises) | Fully deductible |
| Professional fees (accounting, legal) | Fully deductible |
| Marketing, advertising | Fully deductible |
| Travel (business purpose) | Fully deductible |
| Insurance (business-related) | Fully deductible |
| Bad debts (specific provision, written off) | Deductible |
| Repairs and maintenance | Deductible (revenue nature only) |
| Double deduction | Promotion of exports, approved training, disabled employee costs, R&D |

### 3.3 Capital Allowances (Schedule 3)

**Capital Allowances (Schedule 3)**

| Asset Category | Initial Allowance | Annual Allowance |
| --- | --- | --- |
| Heavy machinery / general plant | 20% | 14% |
| Office equipment, furniture | 20% | 10% |
| Motor vehicles (max RM100,000 cost; RM200,000 if on-the-road price ≤RM150,000) | 20% | 20% |
| Computer, IT equipment | 20% | 40% |
| Small value assets (each ≤RM2,000, total ≤RM20,000/YA) | 100% | -- |

### 3.4 Non-Deductible Expenses

**Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Private/domestic expenses | Not business-related |
| Income tax itself | Tax on income |
| Entertainment (50% restriction applies to most) | 50% disallowed unless for promotional purposes |
| Capital expenditure (non-qualifying) | Must go through capital allowance |
| Fines and penalties | Public policy |
| Donations (unless to approved institutions) | Not deductible under Section 33; separate relief may apply |

## Section 4 -- Personal Reliefs (YA 2025)

**Personal Reliefs (YA 2025)**

| Relief | Amount (RM) |
| --- | --- |
| Individual and dependent relatives | 9,000 |
| Disabled individual (additional) | 7,000 |
| Spouse (no income or electing joint assessment) | 4,000 |
| Disabled spouse (additional) | 6,000 |
| Child (unmarried, under 18) | 2,000 per child |
| Child (18+, full-time education in Malaysia) | 2,000 per child |
| Child (18+, full-time education overseas at degree level) | 8,000 per child |
| Disabled child (additional) | 8,000 per child |
| Medical expenses (self, spouse, child -- serious illness) | max 10,000 |
| Medical expenses (parents) | max 8,000 |
| Life insurance + EPF | max 7,000 |
| Education and medical insurance | max 4,000 |
| Lifestyle (books, internet, computer, sports, courses) | max 2,500 |
| EV charging facilities | max 2,500 |
| Private Retirement Scheme (PRS) | max 3,000 |
| SOCSO/EIS contributions | max 350 |
| SSPN (National Education Savings Scheme) | max 8,000 |
| Education fees (self -- Masters/doctorate, approved courses) | max 7,000 |
| Breastfeeding equipment (once per 2 YA) | max 1,000 |
| Child care / kindergarten (child ≤6 years) | max 3,000 |

## Section 5 -- Filing

### 5.1 Forms

**Forms**

| Form | Who Files | Deadline |
| --- | --- | --- |
| Form BE | Individuals with employment income only | 30 April (e-Filing: 15 May) |
| Form B | Individuals with business income (sole proprietors, partnerships, freelancers) | 30 June (e-Filing: 15 July) |
| Form P | Partnership declaration (filed by precedent partner) | 30 June |
| Form M | Non-resident individuals | 30 June |

### 5.2 Filing Process

- **Filing Process** — 1. Register for e-Filing at mytax.hasil.gov.my (first-time users) 2. Obtain Tax Identification Number (TIN) from LHDN 3. Complete Form B with business income, personal reliefs, and tax computation 4. Submit electronically via MyTax portal 5. Pay any balance of tax due (after deducting CP500 instalments paid)

### 5.3 Penalties

**Penalties**

| Offence | Penalty |
| --- | --- |
| Late filing | Surcharge under Section 112(3): RM200 -- RM20,000 or imprisonment ≤6 months |
| Late payment | 10% increase on tax unpaid after due date (Section 103(3)) |
| Additional penalty | Further 5% on amount still unpaid 60 days after due date |
| Incorrect return | Penalty equal to the amount of tax undercharged (Section 113) |
| Wilful evasion | Fine RM1,000 -- RM20,000 or imprisonment ≤3 years, plus 300% penalty (Section 114) |

## Section 6 -- Worked Examples

### Example 1 -- Freelance Designer, Resident

Input: Gross business revenue RM150,000, allowable expenses RM45,000, capital allowances RM5,000. Single, no dependants. EPF voluntary RM7,000. Lifestyle relief RM2,500.

Computation:
- Adjusted income: RM150,000 - RM45,000 = RM105,000
- Statutory income: RM105,000 - RM5,000 = RM100,000
- Total income: RM100,000
- Less reliefs: Individual RM9,000 + EPF/life insurance RM7,000 + Lifestyle RM2,500 = RM18,500
- Chargeable income: RM81,500

Tax:
- First RM70,000: RM3,700
- Next RM11,500 at 19%: RM2,185
- Total tax: RM5,885

### Example 2 -- Non-Resident Consultant

Input: Malaysian-sourced consulting income RM200,000.

Tax: RM200,000 × 30% = RM60,000. No reliefs available.

## Section 7 -- Interaction with Other Systems

**Interaction with Other Systems**

| System | Interaction |
| --- | --- |
| CP500 (prepayment instalments) | See **my-pcb** skill for self-employed instalment payments |
| EPF/SOCSO/EIS | See **my-epf-socso** skill for contribution rates and obligations |
| SST (Sales and Services Tax) | Separate regime; not covered by this skill |

## Section 8 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Income tax rates | ITA 1967, Schedule 1 |
| Business income | ITA 1967, Section 4(a) |
| Allowable deductions | ITA 1967, Section 33 |
| Capital allowances | ITA 1967, Schedule 3 |
| Personal reliefs | ITA 1967, Sections 45A-49 |
| Filing and payment | ITA 1967, Sections 77-107 |
| Penalties | ITA 1967, Sections 112-114 |

### Key LHDN Resources

**Key LHDN Resources**

| Resource | URL |
| --- | --- |
| MyTax e-Filing | https://mytax.hasil.gov.my |
| Tax rates | https://www.hasil.gov.my/en/individual/individual-life-cycle/income-declaration/tax-rate/ |
| Tax reliefs | https://www.hasil.gov.my/en/individual/individual-life-cycle/income-declaration/tax-reliefs/ |
| Contact centre | 03-8911 1000 / HASiL Care Line |

## Prohibitions

- **Prohibitions** — - NEVER apply resident tax rates without confirming 182-day residency requirement - NEVER claim personal reliefs for non-resident taxpayers - NEVER allow entertainment expenses at full deduction -- 50% is disallowed unless qualifying promotion - NEVER claim capital expenditure as a revenue expense - NEVER treat CP500 instalment payments as expenses -- they are credits against final tax - NEVER present calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
