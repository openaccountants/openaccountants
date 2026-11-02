---
name: pg-income-tax
description: Use this skill whenever asked about Papua New Guinea (PNG) personal income tax for employees and self-employed individuals. Trigger on phrases like "how much tax do I pay in PNG", "salary or wages tax", "SWT", "PAYE Papua New Guinea", "Kina income tax", "provisional tax", "annual income tax return", "IRC return", "fortnightly tax", "superannuation contribution", "Nambawan Super", "Nasfund", "GST registration", "self-employed tax PNG", or any question about filing or computing income tax for an employee or sole trader in Papua New Guinea. Also trigger when computing fortnightly salary/wages tax, provisional tax instalments, or superannuation, and when reading a PNG bank statement to classify business income and expenses. This skill covers resident and non-resident rate brackets, SWT/PAYE mechanics, provisional tax, superannuation, GST interaction, filing deadlines, penalties, and the new Income Tax Act 2025 regime effective 1 January 2026. ALWAYS read this skill before touching any PNG income tax work.
jurisdiction: PG
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# papua-new-guinea-income-tax

## Papua New Guinea Income Tax -- Employee & Self-Employed Skill v0.1

## REGIME-CHANGE WARNING -- two regimes in play

REGIME-CHANGE WARNING -- two regimes in play.
- 2025 tax year is governed by the Income Tax Act 1959 (as amended), with salary/wages tax rates set by the Income Tax (Salary or Wages Tax)(Rates)(2025 Budget) Act 2024.
- A new Income Tax Act 2025 entered into force on 1 January 2026 (first returns due in 2027). It rewrites and simplifies the law and introduces a narrow 15% CGT regime, changes to benefit valuations, and salary-packaging limits. The individual rate brackets and thresholds below are not reported to have changed under the new Act, but author/reviewer must re-verify 2026 figures against the Act text before publishing 2026-specific advice. [RESEARCH GAP — reviewer to confirm whether the new Income Tax Act 2025 alters individual brackets/thresholds for 2026; Act text at https://www.parliament.gov.pg/uploads/acts/25A-11.pdf]
- The bracket figures in this skill are confirmed current as of the PwC Worldwide Tax Summaries review dated 27 March 2026.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Papua New Guinea (Independent State of Papua New Guinea) |
| Tax | Personal Income Tax / Salary or Wages Tax (SWT) |
| Currency | Papua New Guinea Kina (PGK / K) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation (2025) | Income Tax Act 1959 (as amended); Income Tax (Salary or Wages Tax)(Rates)(2025 Budget) Act 2024 |
| New legislation (from 2026) | Income Tax Act 2025 (in force 1 January 2026) |
| Tax authority | Internal Revenue Commission (IRC) — irc.gov.pg |
| Tax-free threshold (residents) | PGK 20,000 (effective 1 Jan 2024) — PwC PNG Individual, reviewed 27 Mar 2026 |
| Top marginal rate | 42% on income over PGK 250,000 — PwC PNG Individual |
| SWT remittance | Withheld fortnightly; remitted monthly to IRC before the 7th of the following month — PwC PNG Individual, Tax administration |
| Annual return deadline (via tax agent) | 30 June of the following year — PwC PNG Individual, Tax administration |
| Annual return deadline (self-lodged) | 28 February of the following year — PwC PNG Individual, Tax administration |
| Validated by | Pending — requires sign-off by a PNG-registered tax agent / CPA PNG |
| Validation date | Pending |
| Skill version | 0.1 |

### Resident Tax Rate Brackets (2024 onward; applies to 2025)

- **Threshold elimination rule** — Tax-free threshold: PGK 20,000. The former 22% first band was eliminated for residents when the threshold rose to PGK 20,000 (effective 1 Jan 2024). Do not use older tables showing a 22% resident first bracket.  _(PwC PNG Individual, Taxes on personal income (reviewed 27 March 2026))_

**Resident Tax Rate Brackets (2024 onward; applies to 2025)**  _(PwC Worldwide Tax Summaries — PNG Individual, Taxes on personal income (reviewed 27 March 2026). Cross-check against the Income Tax (Salary or Wages Tax)(Rates)(2025 Budget) Act 2024 (IRC).)_

| Taxable income (PGK) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 -- 20,000 | 0% (nil) | K 0 |
| 20,001 -- 33,000 | 30% | K 3,900 |
| 33,001 -- 70,000 | 35% | K 16,850 |
| 70,001 -- 250,000 | 40% | K 88,850 |
| Over 250,000 | 42% | -- |

### Non-Resident Tax Rate Brackets

- **Non-resident threshold rule** — Non-residents do not receive the tax-free threshold. The first Kina is taxed at 22%.  _(PwC Worldwide Tax Summaries — PNG Individual, Taxes on personal income (reviewed 27 March 2026))_

**Non-Resident Tax Rate Brackets**  _(PwC Worldwide Tax Summaries — PNG Individual, Taxes on personal income (reviewed 27 March 2026))_

| Taxable income (PGK) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 -- 20,000 | 22% | K 4,400 |
| 20,001 -- 33,000 | 30% | K 8,300 |
| 33,001 -- 70,000 | 35% | K 21,250 |
| 70,001 -- 250,000 | 40% | K 93,250 |
| Over 250,000 | 42% | -- |

### Superannuation (Compulsory) — Contribution Rates

**Superannuation (Compulsory) — Contribution Rates**  _(PwC Worldwide Tax Summaries — PNG Individual, Other taxes (reviewed 27 March 2026); Superannuation (General Provisions) Act)_

| Party | Rate | Base |
| --- | --- | --- |
| Employee | 6.0% | Gross basic salary (after-tax) |
| Employer | 8.4% | Gross basic salary (pre-tax) |
| **Combined** | **14.4%** | Gross basic salary excl. overtime, bonus, commission |

No published Kina floor/ceiling on the contribution base was found. [RESEARCH GAP — reviewer to confirm: treat as "no stated contribution cap" rather than assuming one.]

### Other Key Rates

**Other Key Rates**

| Item | Rate / Threshold | Source |
| --- | --- | --- |
| GST | 10% on most goods and services | PwC PNG Individual, Other taxes |
| GST registration threshold | Annual turnover PGK 250,000 (voluntary below) | PwC PNG Individual, Other taxes; IRC GST page |
| Corporate income tax | 30% (resident companies; PNG PEs of non-residents) | PwC PNG Corporate, Taxes on corporate income; IRC |
| Capital gains tax (from 1 Jan 2026) | 15% — narrow; extractive/resource interests | PwC "Income Tax Act 2025"; KPMG Guide 2025 |
| Minimum wage (2025) | PGK 3.50 / hour | ILO; WageIndicator |
| Minimum wage (from 1 Jan 2026) | PGK 5.00 / hour (K5.25 in 2027; K5.50 in 2028) | ILO; WageIndicator |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | STOP — residency determines whether the K20,000 threshold applies |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether income already SWT-taxed at source | Treat as final-taxed employment income (no return) until confirmed |
| Unknown whether superannuation applies | Apply 6%/8.4% only for PNG-citizen employees > 59 days in any 3-month period |
| Unknown asset / depreciation life | Flag for reviewer — capital allowance rates not set in this skill |
| Unknown GST registration status | Assume not registered (turnover below PGK 250,000) until confirmed |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable — bank statement (and/or payslips) for the full tax year in CSV, PDF, or pasted text, plus confirmation of residency status (resident / non-resident) and income type (employment only / self-employment / mixed).

Recommended — payslips showing fortnightly SWT withheld, superannuation statements (Nambawan Super / Nasfund), sales and purchase invoices, prior year assessment or return, GST registration status.

Ideal — complete income and expenditure account, asset register, provisional tax payment confirmations, employer SWT remittance records, full payroll detail.

Refusal if minimum is missing — SOFT WARN. No bank statement or payslip at all = hard stop. Bank statement alone (no payslips/invoices) = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that SWT was correctly withheld at source and that all deductions claimed are supported by valid documentation."

### Refusal Catalogue

- **R-PG-1 — Residency unknown** — Residency determines whether the PGK 20,000 tax-free threshold applies (residents) or whether the first Kina is taxed at 22% (non-residents). This skill cannot compute tax without confirmed residency status. Please confirm before proceeding.
- **R-PG-2 — Companies, partnerships, trusts** — This skill covers individuals (employees and sole traders) only. Companies (30% CIT), partnerships, and trusts file separate returns. Escalate to a PNG-registered tax agent.
- **R-PG-3 — Extractive / resource interests and CGT** — Disposals of taxable assets tied to mining, petroleum, or resource rights — including indirect disposals via a 10% or greater beneficial-ownership change — fall under the new 15% CGT regime (from 1 Jan 2026) and are out of scope. Escalate to a PNG-registered tax agent.
- **R-PG-4 — Mixed expatriate / foreign-source income** — Expatriate packages, double-tax-treaty relief, and foreign-source income require specialised analysis. Out of scope. Escalate to a PNG-registered tax agent.
- **R-PG-5 — Arrears / IRC enforcement** — Client has outstanding tax arrears or is subject to IRC enforcement. Late-payment penalties (20% p.a.) and additional tax for failure to furnish (up to 100% of tax) are severe. Do not advise. Escalate to a PNG-registered tax agent immediately.
- **R-PG-6 — GST return requested** — This skill covers income tax / salary or wages tax only. PNG GST (10%) is a separate return. Escalate or use a dedicated PNG GST skill.
- **R-PG-7 — 2026 return under the new Act** — Returns for the 2026 tax year are governed by the Income Tax Act 2025 (in force 1 Jan 2026, first returns due 2027), which may change benefit valuations, salary-packaging limits, and introduces CGT. Do not finalise a 2026 computation from this 2025-based skill without reviewer confirmation against the Act text.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. Many PNG employees are taxed entirely at source under SWT (final tax) — for those, no income tax return is required and the patterns are used only to confirm there is no untaxed side income.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Business income (self-employment) | If GST-registered, extract net (excl. 10% GST) |
| FEES, PROFESSIONAL FEES, CONSULTANCY, SERVICES | Business income | Typical sole-trader income |
| SALARY, WAGES, PAY, [employer name], FORTNIGHT | Employment income — SWT at source | Usually final-taxed; confirm SWT withheld |
| RENT RECEIVED, RENTAL | Rental income | Non-employment income — annual return required |
| INTEREST, INTERESSI | Investment income | Non-employment income — annual return required |
| DIVIDEND | Investment income | Non-employment income — annual return required |
| IRC REFUND, TAX REFUND | EXCLUDE | Tax refund from prior year |
| GOVERNMENT GRANT, CAPITAL GRANT | EXCLUDE unless revenue grant | Capital grants EXCLUDE; revenue grants = business income |
| SUPER WITHDRAWAL, NAMBAWAN, NASFUND (credit in) | EXCLUDE / flag | Super distribution — taxed under withdrawal-tax table, not ordinary income |

### 3.2 Expense Patterns (Debits) — Deductible Business Expenses (self-employed only)

**3.2 Expense Patterns (Debits) — Deductible Business Expenses (self-employed only)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, RENT [commercial address] | Office rent | Deductible | Dedicated business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible |  |
| ACCOUNTANT, AUDITOR, BOOKKEEP, CPA, TAX AGENT | Accountancy fees | Deductible |  |
| LAWYER, LEGAL, NOTARY (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, ADVERTISING, GOOGLE ADS, FACEBOOK ADS | Marketing/advertising | Deductible |  |
| TRAINING, COURSE, SEMINAR, CONFERENCE | Training | Deductible | Must relate to current business |
| BANK FEE, SERVICE FEE, BSP CHARGE, KINA BANK CHARGE | Bank charges | Deductible | Business account only |
| INTERNET, DIGICEL DATA, TELIKOM, HOSTING, DOMAIN | IT / communications | Deductible (business %) | Apportion if mixed use |

### 3.3 Expense Patterns (Debits) — Utilities (may need apportionment)

**3.3 Expense Patterns (Debits) — Utilities (may need apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| PNG POWER, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| WATER PNG, EDA RANU, WATER | Water | T2 if home office | Apportion |
| DIGICEL, BMOBILE, VODAFONE, TELIKOM | Telecoms/phone | T2 | Business use portion only; default 0% if mixed |

### 3.4 Expense Patterns (Debits) — Travel

**3.4 Expense Patterns (Debits) — Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR NIUGINI, PNG AIR, FLIGHT | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, LODGE, GUESTHOUSE, BOOKING.COM | Accommodation | Deductible if business travel |  |
| TAXI, PMV, HIRE CAR | Local transport | Deductible if business purpose |  |
| FUEL, PETROL, DIESEL, PUMA, MOBIL | Vehicle fuel | T2 — business % only | Requires mileage log |

### 3.5 Expense Patterns (Debits) — NOT Deductible

**3.5 Expense Patterns (Debits) — NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINNER, ENTERTAINMENT, CLIENT MEAL | Entertainment | Generally not deductible | Flag for reviewer |
| GROCERIES, SUPERMARKET, STOP N SHOP, RH, PERSONAL | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, INFRINGEMENT | Fines/penalties | NOT deductible | Public policy |
| IRC PAYMENT, INCOME TAX, SWT PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.6 Exclusions (Neither Income nor Expense)

**3.6 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, LOAN PRINCIPAL | EXCLUDE | Loan principal movement |
| SUPER CONTRIBUTION, NAMBAWAN, NASFUND (debit out) | Superannuation | 6% employee contribution — not a business expense |
| GST PAYMENT, IRC GST | EXCLUDE | GST liability payment, not expense |
| PROVISIONAL TAX, PT INSTALMENT | Credit against liability | Not an expense — offset against assessed tax |

### 3.7 PNG Banks — Statement Format Reference

**3.7 PNG Banks — Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BSP (Bank South Pacific) | TRANSFER, EFT, DD, SO, FEE | PDF/CSV; largest PNG bank; description holds counterparty + reference |
| Kina Bank | PAYMENT, TRF, CARD, CHARGE | PDF/CSV |
| Westpac PNG | TRANSFER, DIRECT DEBIT, FEE | PDF; date format DD/MM/YYYY |
| ANZ PNG | PAYMENT, EFTPOS, TRF, CHARGE | PDF/CSV |

## Section 4 -- Worked Examples

All amounts in Papua New Guinea Kina (PGK / K).

### Example 1 -- Salary credit (employee, SWT final tax)

**Input line:**
`14/03/2025 ; BSP EFT CREDIT ; HIGHLANDS COFFEE LTD ; FORTNIGHT PAY ENDING 13/03 ; +2,450.00 ; PGK`

**Reasoning:**
Net fortnightly salary already taxed under SWT at source. SWT is a final tax for an employee whose only income is fully-taxed employment income — no annual income tax return is required. The K2,450 is net pay; gross and SWT appear on the payslip, not the bank statement.

**Classification:** Employment income, SWT final tax. No further income tax due. EXCLUDE from any self-employment computation.

### Example 2 -- Sole-trader client payment (GST-registered)

**Input line:**
`20/03/2025 ; KINA BANK TRANSFER IN ; MOROBE TRADING LTD ; INV-0042 ; +1,100.00 ; PGK`

**Reasoning:**
Payment for services. Client is GST-registered (turnover over PGK 250,000), so K1,100 includes 10% GST. Net business income = K1,000 (K1,100 ÷ 1.10). K100 is GST collected — a liability to IRC, excluded from income.

**Classification:** Business income = K1,000. GST K100 excluded.

### Example 3 -- Superannuation contribution (employee 6%)

**Input line:**
`14/03/2025 ; BSP DD ; NAMBAWAN SUPER ; MEMBER CONTRIBUTION ; -147.00 ; PGK`

**Reasoning:**
Employee superannuation contribution is 6.0% of gross basic salary. For a fortnight where gross basic salary is K2,450, the employee contribution is 6% × 2,450 = K147.00 (the employer separately contributes 8.4% × 2,450 = K205.80). Source: PwC PNG Individual, Other taxes. The employee contribution is not a business expense.

**Classification:** Superannuation (employee 6%). Confirm gross basic salary excludes overtime/bonus/commission.

### Example 4 -- Fuel (mixed-use vehicle)

**Input line:**
`02/04/2025 ; ANZ CARD ; PUMA ENERGY WAIGANI ; FUEL ; -180.00 ; PGK`

**Reasoning:**
Vehicle fuel for a sole trader. Only the business-use percentage is deductible, and only with a mileage log. Tier 2 — conservative default is 0% deduction until the business percentage is documented.

**Classification:** T2. Default K0 deductible until mileage log confirms business %.

### Example 5 -- Income tax / provisional tax payment (not deductible)

**Input line:**
`28/09/2025 ; BSP TRANSFER ; INTERNAL REVENUE COMMISSION ; PROVISIONAL TAX 2025 ; -3,000.00 ; PGK`

**Reasoning:**
Provisional tax is a payment on account against the year's assessed income tax — it is not a business expense. It is credited against the final assessed liability, not deducted from income. Provisional tax is due no earlier than 30 September of the year of income.

**Classification:** Provisional tax paid (credit against assessed tax). NOT a deduction.

### Example 6 -- Resident sole trader, full-year tax computation

**Inputs:** Resident sole trader. Gross business income K120,000; allowable expenses K35,000 → taxable income K85,000.

**Reasoning (resident brackets):**
- 0 – 20,000 at 0% = K0
- 20,001 – 33,000 at 30% = 30% × 13,000 = K3,900
- 33,001 – 70,000 at 35% = 35% × 37,000 = K12,950
- 70,001 – 85,000 at 40% = 40% × 15,000 = K6,000
- Total income tax = 0 + 3,900 + 12,950 + 6,000 = K22,850

If K3,000 provisional tax was already paid (Example 5), balance due on assessment = 22,850 − 3,000 = K19,850.

**Classification:** Income tax K22,850; balance due K19,850 after provisional tax credit.

### Example 7 -- Internal transfer (exclude)

**Input line:**
`15/05/2025 ; BSP TRANSFER ; OWN ACCOUNT - SAVINGS ; ; -2,000.00 ; PGK`

**Reasoning:**
Transfer between the client's own accounts. Neither income nor expense.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency and the Tax-Free Threshold

- **Residency threshold rule** — Residents receive a PGK 20,000 tax-free threshold (effective 1 Jan 2024). Non-residents receive no threshold — the first Kina is taxed at 22%. Residency must be confirmed before any rate table is applied (see R-PG-1).  _(PwC PNG Individual, Taxes on personal income)_

### 5.2 Salary or Wages Tax (SWT / PAYE)

- **SWT mechanics** — SWT is assessed fortnightly using standard fortnightly tax tables, regardless of actual pay frequency. It operates as a final tax for employees whose only income is fully-taxed employment income — those employees do not lodge an annual return. The employer withholds SWT each fortnight and remits monthly to IRC before the 7th day of the following month.  _(PwC PNG Individual, Tax administration; IRC SWT guidance)_

### 5.3 Who Must Lodge an Annual Return

- **Annual return requirement** — Anyone with non-salary income must lodge an annual income tax return, including the self-employed and anyone with interest, dividends, rental, trust distribution, or partnership income.  _(PwC PNG Individual, Tax administration)_

### 5.4 Provisional Tax (self-employed / non-salary income)

- **Provisional tax threshold** — Provisional tax applies to non-salary/wages income exceeding PGK 100.  _(PwC PNG Individual, Tax administration)_
- **Provisional tax amount basis** — It is generally set equal to the prior year's assessed income tax (reducible by application lodged before the due date).  _(PwC PNG Individual, Tax administration)_
- **Provisional tax due date** — Provisional tax payment is due no earlier than 30 September of the year of income.  _(PwC PNG Individual, Tax administration)_
- **Assessment payment due date** — Tax shown on a notice of assessment is due within 30 days of service of the notice.  _(PwC PNG Individual, Tax administration)_

### 5.5 Filing Deadlines (individuals)

**5.5 Filing Deadlines (individuals)**  _(PwC PNG Individual, Tax administration)_

| Lodgement method | Deadline |
| --- | --- |
| Through a registered tax agent | 30 June of the following year |
| Self-lodged (no tax agent) | 28 February of the following year |

### 5.6 Dependant Rebates — REPEALED

- **Dependant rebates repealed** — Dependant rebates have been repealed as a simplification measure and are no longer available for 2025 declarations. Do not apply them. (Historical, now-defunct detail: 1st dependant 15% of gross tax, max K450/min K45; 2nd & 3rd dependants 10% each, max K300/min K30; overall cap K1,050/yr; no rebate beyond 3 dependants.)  _(PwC PNG Individual, Other tax credits and incentives)_

### 5.7 Superannuation

**5.7 Superannuation rules**

| Rule | Detail |
| --- | --- |
| Employer obligation | Mandatory for employers with **15 or more** employees — must register with an authorised fund |
| Employee coverage | Compulsory for **PNG-citizen** employees working **> 59 days in any 3-month period**; voluntary for non-citizens |
| Employee contribution | **6.0%** of gross basic salary (after-tax) |
| Employer contribution | **8.4%** of gross basic salary (pre-tax) |
| Contribution base | Gross **basic** salary — excludes overtime, bonus, commission |
| Contribution ceiling | None found — [RESEARCH GAP — reviewer to confirm no salary cap on the contribution base] |

- **Superannuation legislation and funds** — Legislation: Superannuation (General Provisions) Act. Main authorised funds: Nambawan Super (public sector), Nasfund (private sector).  _(Superannuation (General Provisions) Act)_

**Superannuation withdrawal/distribution tax (concessional, by membership length)**  _(PwC PNG Individual, Other taxes)_

| Membership length | Withdrawal tax |
| --- | --- |
| Under 5 years | Marginal rate |
| 5 – 9 years | Lesser of 15% or marginal rate |
| 9 – 15 years | Lesser of 8% or marginal rate |
| Over 15 years | 2% |

### 5.8 GST Interaction

**5.8 GST Interaction**  _(PwC PNG Individual, Other taxes; IRC GST page)_

| Scenario | Income Tax Treatment |
| --- | --- |
| GST-registered, GST collected on sales | NOT income — exclude from business income |
| GST-registered, input GST recovered | NOT an expense — exclude |
| Not GST-registered (turnover < PGK 250,000) | All GST paid on purchases is part of the gross cost (deductible as expense) |

- **GST rate and registration threshold** — GST rate 10%; registration threshold turnover PGK 250,000.  _(PwC PNG Individual, Other taxes; IRC GST page)_

### 5.9 Non-Deductible Expenses

**5.9 Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Entertainment (client meals, events) | Generally blocked — flag for reviewer |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax / SWT itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |
| Superannuation employee contribution | Personal contribution, not a business expense |
| Provisional tax | Credit against assessed tax, not a deduction |

### 5.10 Penalties

**5.10 Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| Late lodgement of income tax return | Additional tax up to **100% of the tax** for failure to furnish | KPMG PNG Tax Profile; IRC practice |
| Late payment of income tax / provisional tax | **20% per annum** late-payment penalty | KPMG PNG Tax Profile |
| SWT (PAYE) non-compliance | Commonly **20% flat additional tax plus 20% interest** on unremitted amounts; remittance due before the 7th of the following month | KPMG PNG Tax Profile; SmartBiz Pacific (IRC practice) |

Caveat: these percentages come from Big-4 profile + secondary IRC-practice sources, not a directly-parsed IRC penalty schedule. [RESEARCH GAP — reviewer to re-confirm exact penalty percentages against the current statute text, including penalty provisions carried into the Income Tax Act 2025.]

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (self-employed)

- Calculate the proportion of the home used for business (dedicated room(s) as a percentage of total rooms or floor area).
- Apply that percentage to rent, electricity (PNG Power), water (Water PNG / Eda Ranu), and internet.
- A dual-use room does not qualify.

Conservative default: 0% deduction until reviewer confirms the room arrangement.
Flag for reviewer: Confirm room count, floor-area basis, and that the workspace is genuinely dedicated.

### 6.2 Motor Vehicle Business Use (self-employed)

- Only the business-use percentage of fuel, insurance, and running costs is deductible.
- Client must maintain a mileage log (business vs total mileage).

Conservative default: 0% business use until a mileage log is provided.
Flag for reviewer: Confirm the business percentage is documented and reasonable.

### 6.3 Phone / Internet Mixed Use

- Business-use portion only (Digicel, bmobile, Telikom).

Conservative default: 0% deduction until the business percentage is confirmed.

### 6.4 Capital Allowances / Depreciation

- Business assets are depreciated, not expensed. This skill does not set PNG capital-allowance rates.

Conservative default: flag any asset purchase for the reviewer.
Flag for reviewer: [RESEARCH GAP — PNG depreciation/capital-allowance rates not captured in this skill; reviewer to apply the correct Income Tax Act schedule.]

### 6.5 Entertainment

- Generally non-deductible; reviewer to confirm whether any narrow business exception applies.

### 6.6 Residency Edge Cases

- Part-year residents, expatriates, and those present under specific day-count tests require reviewer judgement on which threshold/rate table applies.

## Section 7 -- Excel Working Paper Template

```
PAPUA NEW GUINEA INCOME TAX -- WORKING PAPER
Tax Year: 2025  (Income Tax Act 1959 regime)
Client: ___________________________
Residency: Resident / Non-resident
Income type: Employment only / Self-employed / Mixed
Currency: PGK (Kina)

A. EMPLOYMENT INCOME (SWT at source)
  A1. Gross salary/wages (per payslips)          ___________
  A2. SWT withheld (fortnightly, final tax)      ___________
  A3. Net employment income                       ___________
  (If A1 is the ONLY income and fully SWT-taxed -> no annual return required)

B. SELF-EMPLOYMENT / BUSINESS INCOME
  B1. Gross business income (net of GST if reg.) ___________
  B2. Rental income                               ___________
  B3. Interest / dividends                        ___________
  B4. TOTAL non-employment income                 ___________

C. ALLOWABLE BUSINESS DEDUCTIONS (self-employed)
  C1. Office rent                                 ___________
  C2. Professional insurance                      ___________
  C3. Accountancy / legal / tax-agent fees        ___________
  C4. Office supplies                             ___________
  C5. Marketing / advertising                     ___________
  C6. Training                                    ___________
  C7. Bank charges                                ___________
  C8. Telecoms (business %)                       ___________
  C9. Travel (flights, accommodation, transport)  ___________
  C10. Home office (% of utilities/rent)          ___________
  C11. Vehicle (business %)                       ___________
  C12. Capital allowances (reviewer-set rates)    ___________
  C13. TOTAL deductions                           ___________

D. TAXABLE INCOME (B4 - C13; add A1 if return required) ___________

E. TAX COMPUTATION (pass to deterministic engine)
  E1. Income tax (resident or non-resident table) ___________
  E2. Less: provisional tax paid                  ___________
  E3. Balance due / refund (E1 - E2)              ___________

F. SUPERANNUATION (if applicable)
  F1. Gross basic salary (excl. OT/bonus/comm.)   ___________
  F2. Employee contribution 6.0%                  ___________
  F3. Employer contribution 8.4%                  ___________

REVIEWER FLAGS:
  [ ] Residency confirmed (threshold applies?)?
  [ ] Income fully SWT-taxed at source (no return)?
  [ ] GST registration status confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] Capital-allowance rates applied correctly?
  [ ] Provisional tax credited (not deducted)?
  [ ] Superannuation base excludes OT/bonus/commission?
  [ ] 2026 work: re-checked against Income Tax Act 2025?
```

## Section 8 -- Bank Statement Reading Guide

### PNG Bank Statement Formats

**PNG Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BSP (Bank South Pacific) | PDF, CSV | Date, Description, Debit, Credit, Balance | Largest PNG bank; description holds counterparty + reference |
| Kina Bank | PDF, CSV | Date, Narrative, Amount, Balance | Card transactions show merchant |
| Westpac PNG | PDF | Date, Particulars, Withdrawals, Deposits | Date format DD/MM/YYYY |
| ANZ PNG | PDF, CSV | Value Date, Description, Amount, Balance | EFTPOS shows merchant name |

### Key PNG Banking / Payroll Terms

**Key PNG Banking / Payroll Terms**

| Term | Meaning | Classification Hint |
| --- | --- | --- |
| SWT | Salary or Wages Tax | PAYE withheld at source — final tax |
| EFT / TRF | Electronic transfer | Check direction for income/expense |
| DD | Direct debit | Regular expense (utility, subscription, super) |
| SO | Standing order | Regular expense (rent, loan) |
| PMV | Public Motor Vehicle | Local transport fare — possible business travel |
| EFTPOS | Card payment at terminal | Expense — check merchant |
| FORTNIGHT / FN | Two-week pay period | Salary credit — employment income |
| Nambawan / Nasfund | Superannuation funds | Super contribution (6%) or withdrawal |
| IRC | Internal Revenue Commission | Tax payment — not deductible |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- PAPUA NEW GUINEA INCOME TAX
1. Residency: are you a PNG resident or non-resident for tax?
2. Income type: employment only, self-employed, or mixed?
3. If employed: is all your salary taxed under SWT at source (payslips show SWT)?
4. Do you have any non-salary income (business, rental, interest, dividends)?
5. GST: is your business turnover over PGK 250,000 / are you GST-registered?
6. Home office: dedicated room or shared space? If dedicated, what % of floor area?
7. Vehicle: do you use a car for business? What % is business use? Mileage log?
8. Phone/internet: what % is business use?
9. Superannuation: which fund (Nambawan/Nasfund) and your gross basic salary?
10. Provisional tax: total amount paid in the tax year?
11. Will the return be lodged via a registered tax agent (30 June) or self-lodged (28 Feb)?
```

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References**

| Topic | Reference |
| --- | --- |
| Income tax (2025) | Income Tax Act 1959 (as amended) — IRC |
| Salary/wages tax rates (2025) | Income Tax (Salary or Wages Tax)(Rates)(2025 Budget) Act 2024 — IRC |
| New regime (from 2026) | Income Tax Act 2025 — Parliament of PNG (https://www.parliament.gov.pg/uploads/acts/25A-11.pdf) |
| Rate brackets / thresholds | PwC Worldwide Tax Summaries — PNG Individual (reviewed 27 Mar 2026) |
| SWT, provisional tax, deadlines | PwC PNG Individual, Tax administration |
| Superannuation | Superannuation (General Provisions) Act; PwC PNG Individual, Other taxes |
| GST | IRC GST page; PwC PNG Individual, Other taxes |
| CGT (from 2026) | PwC "Income Tax Act 2025"; KPMG Guide to Income Tax Bill 2025 |
| Penalties | KPMG PNG Tax Profile; IRC "Know your taxes" |
| Tax authority | Internal Revenue Commission (IRC) — irc.gov.pg |

### Source URLs

- PwC PNG Individual — Taxes on personal income: https://taxsummaries.pwc.com/papua-new-guinea/individual/taxes-on-personal-income
- PwC PNG Individual — Tax administration: https://taxsummaries.pwc.com/papua-new-guinea/individual/tax-administration
- PwC PNG Individual — Other taxes: https://taxsummaries.pwc.com/papua-new-guinea/individual/other-taxes
- PwC PNG Individual — Other tax credits and incentives: https://taxsummaries.pwc.com/papua-new-guinea/individual/other-tax-credits-and-incentives
- PwC PNG Corporate — Taxes on corporate income: https://taxsummaries.pwc.com/papua-new-guinea/corporate/taxes-on-corporate-income
- PwC "Income Tax Act 2025": https://www.pwc.com/pg/en/publications/income-tax-act-2025.html
- KPMG Guide to Income Tax Bill 2025: https://kpmg.com/pg/en/home/insights/2025/03/kpmg_guide_to_income_tax_bill_2025.html
- Income Tax Act 2025 (full text): https://www.parliament.gov.pg/uploads/acts/25A-11.pdf
- IRC SWT page: https://irc.gov.pg/taxpayer-information-kit/salary-or-wages-tax
- IRC SWT rates PDF (2025 Budget Act): https://static.irc.gov.pg/2025/January/9RMCiB-media-incometax-salaryorwagestaxratesact2024.pdf
- ILO — new national minimum wage for PNG: https://www.ilo.org/resource/news/ilo-welcomes-new-national-minimum-wage-papua-new-guinea

### Test Suite

All figures recomputed end-to-end against the resident/non-resident bracket tables in Section 1.

Input: Resident, taxable income K85,000.
Expected: 0 (first 20,000) + 3,900 (30% × 13,000) + 12,950 (35% × 37,000) + 6,000 (40% × 15,000) = income tax K22,850.

Input: Resident, taxable income K33,000.
Expected: 0 + 30% × 13,000 = K3,900 (matches cumulative-tax column).

Input: Resident, taxable income K70,000.
Expected: 3,900 + 12,950 = K16,850 (matches cumulative-tax column).

Input: Resident, taxable income K300,000.
Expected: 88,850 (cumulative at 250,000) + 42% × 50,000 = 88,850 + 21,000 = K109,850.

Input: Non-resident, taxable income K85,000.
Expected: 4,400 (22% × 20,000) + 3,900 (30% × 13,000) + 12,950 (35% × 37,000) + 6,000 (40% × 15,000) = K27,250 (= resident K22,850 + K4,400 lost threshold).

Input: Gross basic fortnight salary K2,450 (excl. OT/bonus/commission).
Expected: Employee 6% = K147.00; Employer 8.4% = K205.80; combined 14.4% = K352.80.

Input: Employee, only income is salary fully taxed under SWT at source.
Expected: No annual income tax return required; SWT is the final tax.

Input: Resident sole trader, income tax K22,850, provisional tax paid K3,000.
Expected: Provisional tax credited against assessed tax → balance due 22,850 − 3,000 = K19,850. Provisional tax is NOT deducted from income.

## PROHIBITIONS

- NEVER apply a rate table without knowing residency (residents get the K20,000 threshold; non-residents do not)
- NEVER apply the eliminated 22% first band to a resident
- NEVER apply repealed dependant rebates
- NEVER treat provisional tax as a deduction — it is a credit against assessed tax
- NEVER treat the employee superannuation contribution as a business expense
- NEVER allow income tax or SWT itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER include GST collected on sales in business income for a GST-registered client
- NEVER require an annual return from an employee whose only income is fully SWT-taxed at source
- NEVER finalise a 2026 computation from this 2025-based skill without reviewer confirmation against the Income Tax Act 2025
- NEVER present tax calculations as definitive — always label as estimated and pass to the deterministic engine

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
