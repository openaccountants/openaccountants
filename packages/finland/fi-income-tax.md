---
name: fi-income-tax
description: Use this skill whenever asked about Finland income tax for self-employed individuals or freelancers. Trigger on phrases like "Finland income tax", "Finnish tax", "Verohallinto", "OmaVero", "vero.fi", "elinkeinotulo", "pääomatulo", "ansiotulo", "Finnish tax return", "ennakkoperintä", "municipal tax Finland", "capital income Finland", "state tax Finland", or any question about Finnish income tax filing, rates, or deductions for self-employed persons. Covers progressive state tax, municipal tax, capital income tax, church tax, deductions, and filing via OmaVero. ALWAYS read this skill before touching any Finland income tax work.
version: 1.0
jurisdiction: FI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FI Income Tax

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Finland (Republic of Finland / Suomen tasavalta) |
| Tax | Income Tax (tulovero) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (tuloverolaki 1535/1992); Act on Tax Prepayments (ennakkoperintälaki 1118/1996) |
| Supporting legislation | Business Income Tax Act (laki elinkeinotulon verottamisesta 360/1968); Municipal Tax Act |
| Tax authority | Finnish Tax Administration (Verohallinto / Vero) |
| Filing portal | OmaVero (https://www.vero.fi/omavero) |
| Filing deadline | Self-employed: 1 April of the following year; Employees: mid-April (dates vary, e.g. 15 April, 22 April, 29 April 2025) |
| Validated by | Pending -- requires sign-off by a Finnish KHT/HT auditor or tax adviser |
| Validation date | Pending |
| Skill version | 1.0 |

### Earned Income -- State Tax Brackets (2025)

**Earned Income -- State Tax Brackets (2025)**

| Taxable Earned Income (EUR) | Tax at Lower Limit | Rate on Excess |
| --- | --- | --- |
| 0 -- 21,200 | €0 | 12.64% |
| 21,200 -- 31,500 | €2,679.68 | 19.00% |
| 31,500 -- 52,100 | €4,636.68 | 30.25% |
| 52,100 -- 88,200 | €10,868.18 | 34.00% |
| 88,200 -- 150,000 | €23,142.18 | 41.75% |
| 150,000+ | €48,943.68 | 44.25% |

- **Solidarity tax top bracket** — The top bracket (44.25%) includes a 2 percentage point "solidarity tax" (solidaarisuusvero) on income above €150,000.

### Municipal Tax (kunnallisvero)

- **Municipal tax rate range** — 4.73% -- 10.86% percent (Flat rate set by each municipality, mainland Finland 2025. Average approximately 7.5%. Applied to taxable earned income after municipal deductions (which differ from state deductions).)

### Church Tax (kirkollisvero)

- **Church tax rate range** — 1.0% -- 2.2% percent (Applicable only to members of the Evangelical Lutheran Church or Orthodox Church, depending on parish)

### Capital Income Tax (pääomatulovero)

**Capital Income Tax (pääomatulovero)**

| Capital Income (EUR) | Rate |
| --- | --- |
| 0 -- 30,000 | 30% |
| 30,000+ | 34% |

### Health Insurance Contributions (2025)

**Health Insurance Contributions (2025)**

| Component | Rate | Applies To |
| --- | --- | --- |
| Medical care contribution | 0.51% | All earned income |
| Daily allowance contribution (employee) | 0.88% | Earned income ≥€17,255/year |
| Daily allowance contribution (self-employed) | 1.11% | Earned income ≥€17,255/year |
| Daily allowance (self-employed, low income) | 0.23% | Earned income <€17,255/year |

### Self-Employed Business Income Split

- **Self-Employed Business Income Split** — For self-employed (sole traders / toiminimiyrittäjä), business income is split between earned income and capital income: Capital income portion: 20% of the net assets of the business at the end of the prior year (default). The taxpayer may elect 10% or 0% instead. Earned income portion: The remainder is taxed as earned income at progressive rates plus municipal tax.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown municipality | STOP -- municipal tax rate required |
| Unknown church membership | No church tax |
| Unknown capital income split election | 20% of net assets (statutory default) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration | Assume not VAT-registered |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, municipality of residence, and confirmation of whether self-employed (elinkeinonharjoittaja) or freelancer (ammatinharjoittaja).

**Recommended** -- all sales invoices, purchase invoices/receipts, YEL pension insurance payment confirmations, prior year OmaVero tax decision, asset register for business.

**Ideal** -- complete bookkeeping (single-entry or double-entry), balance sheet if double-entry, prepayment tax (ennakkovero) payment confirmations, travel expense records.

### Refusal Catalogue

- **R-FI-1 -- Municipality unknown** — "Municipal tax rate varies from 4.73% to 10.86%. Cannot compute total tax without knowing the client's municipality. Please confirm."
- **R-FI-2 -- Company or partnership** — "This skill covers sole traders (toiminimi) and freelancers (ammatinharjoittaja) only. Oy (osakeyhtiö), Ky (kommandiittiyhtiö), and Ay (avoin yhtiö) have different rules. Escalate to a Finnish tax adviser."
- **R-FI-3 -- Non-resident taxation** — "Non-resident and dual-resident taxation has separate rules (e.g., flat 35% withholding on employment income). Out of scope."
- **R-FI-4 -- International income / tax treaty** — "Cross-border income subject to Finland's extensive double tax treaty network requires specialist analysis. Escalate."

## Section 3 -- Deductions

### 3.1 Earned Income Deductions (from State Tax)

**3.1 Earned Income Deductions (from State Tax)**

| Deduction | Detail |
| --- | --- |
| Työtulovähennys (earned income deduction) | Granted automatically on wages/business earned income; max ~€2,140 (2025); phases out at higher income |
| Perusvähennys (basic deduction) | Granted on municipal tax; max ~€3,870 (2025); phases out as income rises |
| YEL pension insurance | Fully deductible from personal taxation |

### 3.2 Business Deductions (Self-Employed)

**3.2 Business Deductions (Self-Employed)**

| Category | Treatment |
| --- | --- |
| Office rent (dedicated business premises) | Fully deductible |
| Home office (työhuonevähennys) | Fixed deduction: €940/year if primary workplace; €470/year if secondary; or actual costs pro-rated by area |
| Professional literature, tools | Fully deductible |
| Travel expenses (business trips) | Actual costs or per diem (päiväraha): full day (>10h) €51, partial (>6h) €24 (2025 domestic rates) |
| Kilometre allowance | €0.30/km for own car on business trips (2025) |
| Training and CPD | Deductible if related to current profession |
| Telephone / internet (business portion) | Deductible for documented business use portion |
| Professional memberships | Fully deductible |
| Accounting and legal fees | Fully deductible |
| Marketing, advertising | Fully deductible |
| Bank charges (business account) | Fully deductible |
| Bad debts | Deductible if previously declared as income and irrecoverable |
| Representation / entertainment | 50% deductible (food and beverages for client entertainment) |
| Depreciation | Machinery/equipment: max 25% declining balance; IT equipment: max 25%; Furniture: max 25%; Buildings: 4-7% straight-line |

### 3.3 Non-Deductible Expenses

**3.3 Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Personal living costs | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Commuting (home to permanent workplace) | Personal; separate commuting deduction exists for employees |
| Clothing (unless protective/uniform) | Personal |
| Donations (except to approved universities/research) | Not deductible for self-employed |

## Section 4 -- Worked Examples

### Example 1 -- Freelance Developer, Single, Helsinki

**Input:** Gross business revenue €65,000, allowable expenses €12,000, net business income €53,000. No significant business assets. Municipality: Helsinki (municipal tax 8.50% for 2025). Church member (Evangelical Lutheran, church tax ~1.0%).

**Capital income split:** Net business assets ~€5,000. Capital income = 20% × €5,000 = €1,000 at 30% = €300. Earned income = €53,000 - €1,000 = €52,000.

**State tax on €52,000 earned income:**
Tax at €31,500 limit = €4,636.68
Excess: (€52,000 - €31,500) × 30.25% = €6,201.25
State tax = €10,837.93

**Municipal tax on €52,000:** €52,000 × 8.50% = €4,420 (before municipal deductions; actual will be lower after perusvähennys and other deductions).

**Health insurance:** ~€52,000 × (0.51% + 1.11%) = ~€842.

**Capital income tax:** €1,000 × 30% = €300.

**Approximate total tax:** ~€15,000--€16,000 (effective rate ~28-30%).

### Example 2 -- Capital Income Only

**Input:** Investment income €45,000 (dividends, rental, interest).

**Tax:** First €30,000 at 30% = €9,000. Remaining €15,000 at 34% = €5,100. Total = €14,100.

## Section 5 -- Filing and Payment

### 5.1 Filing

**5.1 Filing**

| Item | Detail |
| --- | --- |
| Self-employed filing deadline | 1 April of the following year (from 2025 onwards) |
| Employee filing deadline | Mid-April (dates vary: 15, 22, or 29 April) |
| Portal | OmaVero (omavero.fi) |
| Pre-populated return | Verohallinto pre-fills income from employers, banks, pension companies |
| Self-employed attachment | Income statement (tuloslaskelma) and balance sheet (tase) if double-entry bookkeeping |
| Record retention | 6 years |

### 5.2 Prepayment Tax (Ennakkovero)

Self-employed persons must pay prepayment tax during the tax year. See the **fi-prepayments** skill for full details.

- Based on estimated income or prior year assessment
- Paid in monthly or bimonthly instalments via OmaVero
- Adjustable during the year through OmaVero
- Residual tax (jäännösvero) due if prepayments insufficient

### 5.3 Penalties

**5.3 Penalties**

| Offence | Penalty |
| --- | --- |
| Late filing | Late filing surcharge (myöhästymismaksu): €50 base + 2% of tax due (max varies) |
| Failure to file | Estimated assessment (arvioverotus) + penalty up to 30% of added tax |
| Late payment of residual tax | Interest: base rate + 7 percentage points (Vero publishes annually) |
| Negligent error | Tax increase (veronkorotus): 2-10% of additional tax |
| Intentional error | Tax increase: 10-40% of additional tax |

## Section 6 -- Interaction with Other Finnish Taxes

**Section 6 -- Interaction with Other Finnish Taxes**

| Tax | Interaction |
| --- | --- |
| VAT (ALV) | Separate system; see Finland VAT skill if applicable. VAT collected is not income; input VAT recovered is not expense. |
| YEL pension insurance | Mandatory for self-employed; deductible from personal income. See **fi-yel-social** skill. |
| Prepayment tax (ennakkovero) | Not an expense; credit against final liability. See **fi-prepayments** skill. |

## Section 7 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Income tax rates | Income Tax Act (tuloverolaki) 1535/1992 |
| Business income | Business Income Tax Act (EVL) 360/1968 |
| Capital income split | Income Tax Act §38 |
| Deductions | Income Tax Act §29-§31, §93-§95; EVL §7-§18 |
| Prepayments | Prepayment Act (ennakkoperintälaki) 1118/1996 |
| Filing deadlines | Verohallinto annual announcement |

### Key Verohallinto Resources

**Key Verohallinto Resources**

| Resource | URL |
| --- | --- |
| OmaVero portal | https://www.vero.fi/omavero |
| Self-employed guide | https://www.vero.fi/en/businesses-and-corporations/about-corporate-taxes/sole-traders/ |
| Tax rates on pay | https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/income/earned-income/tax-rates-on-pay-pensions-and-benefits/ |
| Per diem rates | https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/income/earned-income/work-related-travel/ |

## Prohibitions

- NEVER compute total tax without knowing the client's municipality of residence
- NEVER ignore the earned income / capital income split for self-employed
- NEVER apply employee-specific deductions (e.g., commuting deduction) to self-employed income
- NEVER treat YEL insurance as a business expense -- it is a personal tax deduction
- NEVER treat prepayment tax (ennakkovero) as an expense -- it is a credit against final tax
- NEVER present calculations as definitive -- always label as estimated
- NEVER advise on non-resident, dual-resident, or cross-border tax situations

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
