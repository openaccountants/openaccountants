---
name: ethiopia-income-tax
description: Use this skill whenever asked about Ethiopia (ET) personal or business income tax. Trigger on phrases like "how much income tax do I pay in Ethiopia", "PAYE Ethiopia", "ETB salary tax", "Schedule A B C D", "Category A taxpayer", "Category B turnover tax", "rental income tax Ethiopia", "Proclamation 1395/2025", "pension contribution Ethiopia", "POESSA", "Ministry of Revenues", "net pay calculation Birr", "minimum alternative tax", or any question about computing or filing income tax for an employee, sole proprietor, or landlord in Ethiopia. Also trigger when reviewing payroll, computing PAYE withholding, classifying business income, or advising on advance tax. This skill covers monthly PAYE brackets, business/rental annual schedules, Category A/B turnover tax, pension contributions, VAT registration interaction, filing deadlines, and the Ethiopian fiscal calendar. ALWAYS read this skill before touching any Ethiopia income tax work.
version: 0.1
jurisdiction: ET
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ethiopia Income Tax -- Employment & Self-Employed

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ethiopia (Federal Democratic Republic of Ethiopia) |
| Tax | Income Tax (PAYE on employment; Schedule B/C/D on other income) |
| Currency | Ethiopian Birr (ETB) only |
| Tax year (fiscal) | 8 July -- 7 July (Hamle 1 -- Sene 30, Ethiopian calendar) |
| Primary legislation | Income Tax Proclamation No. 979/2016, as amended by Income Tax (Amendment) Proclamation No. 1395/2025 (effective 8 July 2025) |
| Supporting legislation | Tax Administration Proclamation No. 983/2016; VAT Proclamation No. 1341/2024 + Regulation 570/2025; Private Organizations Employees' Pension law (POESSA) |
| Tax authority | Ministry of Revenues (MOR), `mor.gov.et` (formerly ERCA) |
| Pension authority | Private Organizations Employees Social Security Agency (POESSA) |
| Filing portal | MOR e-services / regional revenue bureaus |
| Validated by | Pending — requires sign-off by an Ethiopian tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

**Calendar caution.** The Ethiopian calendar runs ~7–8 days behind the Gregorian calendar. Statutory "month-end" deadlines therefore tend to land around the 7th–8th of the following Gregorian month. Always confirm the exact Gregorian date against the Ethiopian month boundary.

### PAYE — Monthly Employment Income Brackets (effective 8 July 2025)

**PAYE Monthly Employment Income Brackets**  _(Source: PwC *Taxes on personal income* (Ethiopia); MyWorkpay; PaySpace; EY tax alert 2025-2542. Brackets/rates are authoritative.)_

| Monthly taxable income (ETB) | Marginal rate | Quick-calc deduction (ETB) | Cumulative tax at band ceiling |
| --- | --- | --- | --- |
| 0 – 2,000 | 0% (exempt) | — | 0 |
| 2,001 – 4,000 | 15% | 300 | 300 |
| 4,001 – 7,000 | 20% | 500 | 900 |
| 7,001 – 10,000 | 25% | 850 | 1,650 |
| 10,001 – 14,000 | 30% | 1,350 | 2,850 |
| Over 14,000 | 35% | 2,050 | — |

- **PAYE formula** — Monthly tax = (Gross monthly taxable salary × band rate) − quick-calc deduction  _(PwC *Taxes on personal income*)_

> **[RESEARCH GAP — reviewer to confirm]** The quick-calc deduction column (300 / 500 / 850 / 1,350 / 2,050) is **derived by computation** from the published cumulative-tax figures (0 / 300 / 900 / 1,650 / 2,850), using the standard progressive identity. The math reconciles exactly, but the deduction constants were **not found stated verbatim** in an authoritative source. The brackets and marginal rates themselves ARE authoritative. The OLD pre-2025 deductions (60 / 142.50 / 302.50 / 565 / 955 / 1,500) are obsolete — do not use them.

- **Changes vs prior law** — tax-free threshold raised ETB 600 → ETB 2,000/month; lowest positive rate raised 10% → 15%; brackets cut 7 → 6; the 35% top rate now applies above ETB 14,000 (previously above 10,900).  _(MyWorkpay; PaySpace)_
- **Residence/scope** — Residents are taxed on worldwide income; non-residents on Ethiopian-source income; the same rate schedule applies.  _(PwC, *Taxes on personal income*)_

### Business / Self-Employed (Schedule C) — Annual Progressive Rates

**Business Schedule C Annual Progressive Rates**  _(Source: YSA Law Office (Proclamation 1395/2025 overview); PwC *Significant developments*. Annual thresholds = monthly employment bands × 12.)_

| Annual taxable business income (ETB) | Rate |
| --- | --- |
| 0 – 24,000 | 0% |
| 24,001 – 48,000 | 15% |
| 48,001 – 84,000 | 20% |
| 84,001 – 120,000 | 25% |
| 120,001 – 168,000 | 30% |
| Over 168,000 | 30% (REDUCED from 35% by 1395/2025) |

### Rental Income (Schedule B) — Annual Progressive Rates

**Rental Income Schedule B Annual Progressive Rates**  _(Source: EY tax alert 2025-2542; YSA Law Office.)_

| Annual taxable rental income (ETB) | Rate |
| --- | --- |
| 0 – 24,000 | 0% |
| 24,001 – 48,000 | 15% |
| 48,001 – 84,000 | 20% |
| 84,001 – 120,000 | 25% |
| 120,001 – 168,000 | 30% |
| Over 168,000 | 30% (reduced from 35%) |

### Category B — Turnover / Gross-Sales Tax (presumptive)

Applies to non-professional, non-VAT-registered Category B individuals (turnover below ETB 2,000,000).

**Category B Turnover Tax table**  _(EY tax alert 2025-2542)_

| Annual gross sales (ETB) | Rate on turnover |
| --- | --- |
| 0 – 100,000 | 2% |
| 100,001 – 500,000 | 3% |
| 500,001 – 1,000,000 | 5% |
| 1,000,001 – 1,500,000 | 7% |
| 1,500,001 – 2,000,000 | 9% |

### Pension Contributions (Private Organizations Employees' Pension)

**Pension Contributions table**  _(Source: PwC *Other taxes*; 2merkato; countrytaxcalc.)_

| Party | Rate | Base |
| --- | --- | --- |
| Employee | 7% | basic/gross salary, normal working hours |
| Employer | 11% | same base |
| **Total** | **18%** |  |

- **Pension mandatory scope** — Arithmetic check: 7% + 11% = 18%. ✓ Mandatory for Ethiopian citizens; foreign nationals are NOT required to contribute (optional for foreigners of Ethiopian origin only).  _(PwC *Other taxes*; 2merkato)_

### Other Headline Rates

**Other Headline Rates table**

| Item | Value | Source |
| --- | --- | --- |
| Capital gains tax | 15% on disposal of assets (unchanged by 1395/2025) | EY tax alert 2025-2542 |
| Minimum Alternative Tax (MAT) | 2.5% of annual turnover if computed income tax is lower | MyWorkpay; EY alert |
| VAT standard rate | 15% | EY VAT alert; haymanotbelay.com |
| VAT registration threshold | turnover > ETB 2,000,000 over any 12 months (Proclamation 1341/2024) | EY VAT alert |
| Statute of limitations (assessment) | 5 years from declaration filing | PwC *Tax administration* |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residence status | STOP — confirm resident vs non-resident before applying scope |
| Unknown citizenship (for pension) | STOP — pension obligation depends on Ethiopian citizenship |
| Unknown taxpayer category (A vs B) | Treat as Category A (full books) unless turnover confirmed < ETB 2,000,000 |
| Unknown whether individual is a "listed professional" | Treat as Category A (professionals are always Category A) |
| Unknown pension salary base | Use basic/gross salary; flag the ceiling question (see RESEARCH GAP) |
| Unknown income schedule (employment/business/rental) | STOP — schedule determines the rate table and periodicity |
| Unknown expense business-purpose | Not deductible |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — for employment: monthly gross salary (basic + taxable allowances), citizenship (for pension), residence status. For business/rental: the relevant statements/ledgers for the full fiscal year, plus taxpayer category and turnover.

**Recommended** — payslips, employment contract, pension remittance records, prior-year tax declaration, VAT registration status, breakdown of allowances (which are taxable vs exempt).

**Ideal** — full income and expenditure account, asset register, advance-tax payment confirmations, audited financials (Category A).

**Refusal if minimum is missing — SOFT WARN.** No salary/income figures at all = hard stop. Salary without an allowance breakdown = proceed with reviewer warning: "PAYE was computed treating all stated pay as taxable. The reviewer must confirm which allowances are statutorily exempt before filing."

### Refusal Catalogue

- **R-ET-1 — Residence status unknown** — "Residents are taxed on worldwide income; non-residents only on Ethiopian-source income. This skill cannot scope income without confirmed residence status. Please confirm before proceeding."
- **R-ET-2 — Companies / legal persons** — "This skill covers individuals (employees, sole proprietors, landlords). Corporate income tax (30% on companies) and Category A legal-person filings require separate analysis. Escalate to an Ethiopian tax practitioner."
- **R-ET-3 — Schedule D investment income** — "Dividend, interest, and royalty withholding (Schedule D) rates were not re-verified in this build and must be confirmed against Proclamation 979/2016 / MOR before computing. Escalate or confirm the rate first."
- **R-ET-4 — Penalties / enforcement / arrears** — "Late-filing, late-payment interest, and under-declaration penalty figures are not confirmed in this skill. Do not state penalty numbers. Escalate to an Ethiopian tax practitioner."
- **R-ET-5 — VAT return requested** — "This skill covers income tax only. VAT (15%, Proclamation 1341/2024) is out of scope here."
- **R-ET-6 — Pension ceiling-dependent computation** — "Several sources report an ETB 15,000/month pension salary cap, but it is not confirmed against POESSA/the proclamation. For high earners where the cap changes the result, flag the figure for reviewer confirmation rather than asserting it."

## Section 3 -- Transaction Pattern Library

Deterministic pre-classifier. Match by case-insensitive substring on the counterparty/description as it appears on the bank statement or payroll register. Most specific match wins. If none match, fall through to Tier 1 rules in Section 5. Amharic terms are given alongside English where commonly seen.

### 3.1 Income Patterns (Credits)

**Income Patterns table**

| Pattern | Schedule / Line | Treatment | Notes |
| --- | --- | --- | --- |
| SALARY, DEMOZ (ደሞዝ), NET PAY, PAYROLL | Employment (PAYE) | Employment income | Tax via monthly PAYE table; employer withholds |
| ALLOWANCE, ABEL (አበል), TRANSPORT ALLOWANCE | Employment (PAYE) | Taxable unless statutorily exempt | Flag which allowances are exempt |
| CLIENT PAYMENT, INVOICE, GUBA'E, CONSULTANCY FEE | Schedule C (business) | Business income | Sole-proprietor revenue |
| TELEBIRR, CBE BIRR, M-PESA (business inflow) | Schedule C | Business income | Mobile-money business receipts — match to invoices |
| KIRAY (ኪራይ), RENT RECEIVED, HOUSE RENT | Schedule B (rental) | Rental income | Annual progressive table |
| INTEREST, DIVIDEND | Schedule D | Investment income | [RESEARCH GAP — Schedule D rate to confirm] |
| TAX REFUND, MOR REFUND | EXCLUDE | Not income | Refund of prior-year tax |
| GRANT, NGO TRANSFER | Check nature | Capital grants EXCLUDE; revenue grants = business income | Confirm grant type |

### 3.2 Expense Patterns (Debits) — Business, Generally Deductible

**Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| SHOP RENT, OFFICE KIRAY, COMMERCIAL RENT | Premises rent | Deductible | Dedicated business premises |
| SALARY PAID, WAGES, STAFF DEMOZ | Staff costs | Deductible | Employer payroll cost |
| ETHIO TELECOM, INTERNET, DATA (business) | Telecoms | Deductible (business %) | Apportion if mixed use |
| ETHIOPIAN ELECTRIC, EEU, WATER (business) | Utilities | Deductible (business %) | 100% if dedicated premises |
| ACCOUNTANT, AUDIT, LEGAL FEES (business) | Professional fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| ADVERTISING, MARKETING, FACEBOOK ADS | Advertising | Deductible |  |
| BANK CHARGE, CBE FEE, COMMISSION | Bank charges | Deductible | Business account |
| FUEL, BENZIN, NAFTA (business %) | Vehicle fuel | Deductible (business %) | Requires log |

### 3.3 Expense / Withholding Patterns — Statutory (NOT P&L deductions in the normal way)

**Statutory Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| PENSION, POESSA, SOCIAL SECURITY | Pension contribution | Employee 7% withheld pre-PAYE base treatment; employer 11% is an employer cost | Not a Schedule-C "expense" line for an employee |
| PAYE, INCOME TAX, MOR TAX | Income tax remittance | EXCLUDE from deductions | Tax itself is not deductible |
| VAT PAYMENT, MOR VAT | VAT liability | EXCLUDE | Not an income-tax expense |
| ADVANCE TAX, QUARTERLY TAX | Advance income tax | Credit against final liability — not an expense | Category A & B quarterly |

### 3.4 Expense Patterns — NOT Deductible

**Not Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GROCERIES, SUPERMARKET, PERSONAL, FAMILY | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, MOR PENALTY | Fines/penalties | NOT deductible | Public policy |
| DRAWINGS, OWNER WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |
| ENTERTAINMENT, PARTY, GIFT (non-business) | Entertainment/gifts | NOT deductible | Flag — confirm any business portion |

### 3.5 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, SAVINGS | EXCLUDE | Own-account movement |
| LOAN, LOAN REPAYMENT, BRIDGE | EXCLUDE | Loan principal movement |
| CAPITAL INJECTION, OWNER CAPITAL | EXCLUDE | Equity movement, not income |

### 3.6 Ethiopian Banks / Payment Channels — Statement Format Reference

**Banks table**

| Provider | Common Patterns | Notes |
| --- | --- | --- |
| Commercial Bank of Ethiopia (CBE) | TRANSFER, CBE BIRR, COMMISSION, CHARGE | PDF/SMS; date often Ethiopian + Gregorian |
| Awash Bank | TRF, DEBIT, CREDIT, CHARGE | PDF |
| Dashen / Abyssinia / Wegagen | TRANSFER, DEPOSIT, FEE | PDF |
| telebirr (Ethio Telecom) | RECEIVE, SEND, PAYMENT, MERCHANT | Mobile-money statement; clean counterparty |
| M-PESA Ethiopia (Safaricom) | RECEIVED, PAID, WITHDRAW | Mobile-money statement |

## Section 4 -- Worked Examples

All amounts in ETB. PAYE computed as `(gross taxable salary × band rate) − quick-calc deduction`. Employee pension = 7% of basic/gross salary, deducted in addition to PAYE to reach net pay.

### Example 1 — Low earner (15% band)

**Input line:**
`Hamle 2018 ; PAYROLL ; DEMOZ ; gross salary ; +3,000.00 ; ETB`

**Reasoning:**
Gross taxable salary 3,000 falls in the 2,001–4,000 band (15%, deduction 300).
PAYE = 3,000 × 0.15 − 300 = 450 − 300 = **150**.
Employee pension = 3,000 × 7% = **210**.
Net pay = 3,000 − 150 − 210 = **2,640**.

**Classification:** PAYE 150; pension 210; net 2,640.

### Example 2 — Mid earner (20% band)

**Input line:**
`Nehase 2018 ; PAYROLL ; DEMOZ ; gross salary ; +6,000.00 ; ETB`

**Reasoning:**
6,000 is in the 4,001–7,000 band (20%, deduction 500).
PAYE = 6,000 × 0.20 − 500 = 1,200 − 500 = **700**.
Pension = 6,000 × 7% = **420**.
Net pay = 6,000 − 700 − 420 = **4,880**.

**Classification:** PAYE 700; pension 420; net 4,880.

### Example 3 — Upper-mid earner (30% band)

**Input line:**
`Meskerem 2018 ; PAYROLL ; DEMOZ ; gross salary ; +12,000.00 ; ETB`

**Reasoning:**
12,000 is in the 10,001–14,000 band (30%, deduction 1,350).
PAYE = 12,000 × 0.30 − 1,350 = 3,600 − 1,350 = **2,250**.
Pension = 12,000 × 7% = **840**.
Net pay = 12,000 − 2,250 − 840 = **8,910**.

**Classification:** PAYE 2,250; pension 840; net 8,910.

### Example 4 — High earner (35% top band; pension ceiling flagged)

**Input line:**
`Tikimt 2018 ; PAYROLL ; DEMOZ ; gross salary ; +20,000.00 ; ETB`

**Reasoning:**
20,000 is over 14,000 (35%, deduction 2,050).
PAYE = 20,000 × 0.35 − 2,050 = 7,000 − 2,050 = **4,950**.
Pension: if NO ceiling, 20,000 × 7% = 1,400 → net = 20,000 − 4,950 − 1,400 = **13,650**.
Pension: if the widely-reported ETB 15,000 ceiling applies, 15,000 × 7% = 1,050 → net = 20,000 − 4,950 − 1,050 = **14,000**.

> **[RESEARCH GAP — reviewer to confirm]** The pension salary ceiling (reported as ETB 15,000/month) is not verified against POESSA/the proclamation. For earners above the cap this changes net pay. Present both figures and flag for reviewer.

**Classification:** PAYE 4,950; pension 1,050–1,400 (ceiling-dependent); net 13,650–14,000.

### Example 5 — Exempt earner (below threshold)

**Input line:**
`Hidar 2018 ; PAYROLL ; DEMOZ ; gross salary ; +2,000.00 ; ETB`

**Reasoning:**
2,000 is within the 0% band (0–2,000), so PAYE = **0**.
Pension still applies: 2,000 × 7% = **140**.
Net pay = 2,000 − 0 − 140 = **1,860**.

**Classification:** PAYE 0; pension 140; net 1,860.

### Example 6 — Sole proprietor (Schedule C annual)

**Input:** Category A individual consultant, annual taxable business income ETB 200,000 (turnover ETB 600,000).

**Reasoning:**
Schedule C is progressive on annual taxable income. Over 168,000 → top rate 30% (reduced from 35%).
Tax via the same progressive identity, top band: 200,000 falls over 168,000.
Cumulative tax to 168,000 = (24k@0) + (24k@15%=3,600) + (36k@20%=7,200) + (36k@25%=9,000) + (48k@30%=14,400) = 34,200.
Excess 200,000 − 168,000 = 32,000 × 30% = 9,600.
Income tax = 34,200 + 9,600 = **43,800**.
MAT check: 2.5% × turnover 600,000 = 15,000. Income tax 43,800 > 15,000, so MAT does not bite.

**Classification:** Schedule C income tax = 43,800 (MAT not triggered).

> Cumulative-tax arithmetic verified: 3,600 + 7,200 + 9,000 + 14,400 = 34,200 at ETB 168,000. ✓

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 PAYE Computation (Employment)

- **Monthly PAYE formula** — Monthly PAYE = (gross monthly taxable salary × band rate) − quick-calc deduction. The 0–2,000 band is exempt. Employer is responsible for withholding and monthly remittance.  _(PwC *Taxes on personal income*)_

### 5.2 Taxable vs Exempt Allowances

- **Taxable vs exempt allowances** — Not all allowances are taxable. Some (e.g. certain transport, hardship, or per-diem allowances within statutory limits) are exempt. Treat all stated pay as taxable by default, and flag the exempt-allowance question for reviewer confirmation against Proclamation 979/2016. **[RESEARCH GAP — reviewer to confirm exact exempt-allowance limits.]**  _(Proclamation 979/2016)_

### 5.3 Schedule Selection

**Schedule Selection table**

| Income type | Schedule | Periodicity | Rate table |
| --- | --- | --- | --- |
| Employment | "A" (PAYE) | Monthly | Section 1 monthly bands |
| Rental | "B" | Annual | Section 1 rental table |
| Business (individual, keeping books) | "C" | Annual | Section 1 business table |
| Investment (dividend/interest/royalty) | "D" | Withholding | [RESEARCH GAP — confirm Schedule D rates] |

### 5.4 Taxpayer Categories (Proclamation 1395/2025)

- **Category A** — all legal persons (companies) regardless of turnover; any individual/business with annual turnover > ETB 2,000,000; and all listed professionals (accountants, lawyers, engineers, etc.) regardless of turnover. Full books required.  _(EY alert 2025-2542; apexfinancials.et)_
- **Category B** — unincorporated individuals with annual turnover below ETB 2,000,000, excluding listed professionals and VAT-registered persons.  _(EY alert 2025-2542; apexfinancials.et)_
- **Category C abolished** — Category C (old presumptive small-trader category) was abolished by 1395/2025.  _(EY alert 2025-2542; apexfinancials.et)_

### 5.5 Category B Turnover Tax

- **Category B Turnover Tax rule** — Non-professional, non-VAT-registered Category B individuals pay a presumptive turnover tax on gross sales per the Section 1 turnover table (2% → 9%).  _(EY alert 2025-2542)_

### 5.6 Minimum Alternative Tax (MAT)

- **MAT rule** — If income tax computed on business income is below 2.5% of annual turnover, the taxpayer pays 2.5% of turnover instead. Applies even where incentives/exemptions exist, and extends to rental and digital side income.  _(MyWorkpay; EY alert)_

### 5.7 Pension Contributions

- **Pension contributions rule** — Employee 7% / employer 11% (total 18%) of basic/gross salary for Ethiopian citizens. The employee 7% is withheld and is not part of taxable employment income (deducted before arriving at net pay). Foreign nationals are not required to contribute. Vesting requires a minimum of 10 years' contributions. Remittance is due within 30 days of the relevant month-end.  _(PwC *Other taxes*; 2merkato)_

### 5.8 Capital Gains

- **Capital gains tax rate** — 15% percent (unchanged by 1395/2025)  _(EY alert 2025-2542)_

### 5.9 Non-Deductible Items (Business)

**Non-Deductible Items table**

| Item | Reason |
| --- | --- |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Drawings / owner withdrawals | Not an expense |
| VAT liability payments | Separate tax |

### 5.10 Filing & Payment

**Filing and Payment table**

| Item | Detail | Source |
| --- | --- | --- |
| Fiscal year | 8 July – 7 July | PwC |
| Employees (employment only) | No personal return; employer withholds & remits PAYE monthly (by end of following month, calendar-shifted) | PwC *Tax administration* |
| Business (Category A & B) | Annual income tax declaration after fiscal year-end | PwC |
| Advance tax (NEW, 1395/2025) | Category A & B make quarterly advance payments ≈ prior-year tax; due within 30 days after each 3-month cycle | ethiodiasporahub.com; EY alert |
| Statute of limitations | 5 years from declaration filing | PwC |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Exempt Allowance Determination

- **Exempt allowance determination** — Which allowances (transport, hardship, per-diem, representation) are exempt and to what statutory limit. Default: treat as taxable. Flag for reviewer against Proclamation 979/2016.  _(Proclamation 979/2016)_

### 6.2 Pension Salary Ceiling

- **Pension salary ceiling** — Whether the ETB 15,000/month base cap applies. Default: compute on full basic salary AND show the capped figure. Flag for reviewer (see RESEARCH GAP).

### 6.3 Resident vs Non-Resident Scope

- **Resident vs non-resident scope** — Worldwide vs Ethiopian-source. Default: STOP and confirm residence.

### 6.4 Category A vs B Classification

- **Category A vs B classification** — Turnover threshold (ETB 2,000,000), listed-professional status, VAT registration. Default: Category A. Flag for reviewer.

### 6.5 Schedule C vs Turnover Tax

- **Schedule C vs turnover tax** — Whether a Category B individual is on progressive Schedule C (keeps books) or presumptive turnover tax. Flag for reviewer.

### 6.6 MAT Application

- **MAT application** — Whether 2.5%-of-turnover MAT overrides computed income tax. Recompute both and present the higher. Flag for reviewer.

### 6.7 Mixed-Use Expense Apportionment

- **Mixed-use expense apportionment** — Business percentage of vehicle, telecom, utilities, home premises. Default: 0% business use until documented. Flag for reviewer.

### 6.8 Schedule D Withholding

- **Schedule D withholding** — Dividend/interest/royalty rates. Default: STOP — do not assert a rate. [RESEARCH GAP — reviewer to confirm.]

## Section 7 -- Excel Working Paper Template

```
ETHIOPIA INCOME TAX -- WORKING PAPER
Fiscal Year: 2025/2026 (8 Jul 2025 – 7 Jul 2026)
Client: ___________________________
Income type: Employment / Business (Sch C) / Rental (Sch B)
Residence: Resident / Non-resident
Citizenship (pension): Ethiopian / Foreign

A. EMPLOYMENT (PAYE) — MONTHLY
  A1. Gross salary (basic)                       ___________
  A2. Taxable allowances                         ___________
  A3. Exempt allowances (FLAG)                    (__________)
  A4. Gross taxable salary (A1 + A2)             ___________
  A5. Band rate ____%  Quick-calc deduction ____ ___________
  A6. PAYE = (A4 × rate) − deduction             ___________
  A7. Employee pension (7% × base; ceiling FLAG) ___________
  A8. Net pay = A4 − A6 − A7                      ___________
  A9. Employer pension (11% × base) [memo]       ___________

B. BUSINESS (SCHEDULE C) — ANNUAL
  B1. Gross business income                      ___________
  B2. Less: allowable expenses                   (__________)
  B3. Net taxable business income                ___________
  B4. Schedule C tax (progressive)               ___________
  B5. Turnover                                   ___________
  B6. MAT check = 2.5% × B5                       ___________
  B7. Income tax due = max(B4, B6)               ___________

C. RENTAL (SCHEDULE B) — ANNUAL
  C1. Gross rent                                 ___________
  C2. Less: allowable expenses                   (__________)
  C3. Net taxable rent                           ___________
  C4. Schedule B tax (progressive)               ___________

D. CATEGORY B TURNOVER TAX (if applicable)
  D1. Annual gross sales                         ___________
  D2. Turnover-tax rate ____%                     ___________
  D3. Turnover tax = D1 × D2                      ___________

REVIEWER FLAGS:
  [ ] Residence status confirmed?
  [ ] Citizenship confirmed (pension obligation)?
  [ ] Exempt allowances identified & limits checked?
  [ ] Pension ceiling (ETB 15,000?) confirmed?
  [ ] Category A vs B confirmed (turnover, profession, VAT)?
  [ ] Schedule C vs turnover tax confirmed?
  [ ] MAT recomputed and compared?
  [ ] Schedule D rates confirmed (if investment income)?
  [ ] Quick-calc deductions reconciled to cumulative tax?
```

## Section 8 -- Bank Statement Reading Guide

### Ethiopian Statement Formats

**Ethiopian Statement Formats table**

| Provider | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| CBE | PDF, SMS | Date, Description, Debit, Credit, Balance | Dual Ethiopian/Gregorian dates common |
| Awash / Dashen / Abyssinia | PDF | Date, Particulars, Withdrawal, Deposit, Balance | Counterparty in particulars |
| telebirr | PDF/in-app | Date, Type, Counterparty, Amount, Status | Clean merchant names; receive vs send |
| M-PESA Ethiopia | PDF/SMS | Date, Details, Paid In, Withdrawn, Balance | Mobile-money |

### Key Amharic / Local Terms

**Key Amharic Local Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| ደሞዝ / DEMOZ | Salary | Employment income (PAYE) |
| አበል / ABEL | Allowance | Taxable unless exempt — flag |
| ኪራይ / KIRAY | Rent | Rental income (Schedule B) or premises expense |
| ግብር / GIBIR | Tax | Tax payment — not deductible |
| ጡረታ / TURETA | Pension | Pension contribution |
| ወለድ / WELED | Interest | Investment income (Schedule D) or bank charge |
| ኮሚሽን / COMMISSION | Bank fee | Deductible (business account) |

## Section 9 -- Onboarding Fallback

If the client provides records but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present these questions:

```
ONBOARDING QUESTIONS — ETHIOPIA INCOME TAX
1. Income type: employment, business (sole proprietor), or rental?
2. Residence: resident (worldwide income) or non-resident (Ethiopian-source)?
3. Citizenship: Ethiopian or foreign? (determines pension obligation)
4. For employment: gross salary breakdown — basic vs each allowance?
5. For business: annual turnover? Are you a listed professional? VAT-registered?
6. For business: do you keep full books (Schedule C) or expect turnover tax?
7. Pension: is 7% already deducted? Any salary above ETB 15,000/month?
8. Any investment income (dividends, interest, royalties)? (Schedule D)
9. Any advance-tax payments made this fiscal year?
10. Any capital asset disposals (capital gains)?
```

## Section 10 -- Reference Material

### Key Legislation & Authorities

**Key Legislation and Authorities table**

| Topic | Reference |
| --- | --- |
| Income tax (base) | Income Tax Proclamation No. 979/2016 |
| Income tax (amendment) | Income Tax (Amendment) Proclamation No. 1395/2025 (eff. 8 Jul 2025) |
| Tax administration / penalties | Tax Administration Proclamation No. 983/2016 |
| VAT | VAT Proclamation No. 1341/2024 + Regulation 570/2025 |
| Pension | Private Organizations Employees' Pension law (POESSA) |
| Tax authority | Ministry of Revenues (MOR), `mor.gov.et` |
| Finance ministry | `mofed.gov.et` |
| Legislative text | Federal Negarit Gazeta |

### Sources Consulted

- PwC — `taxsummaries.pwc.com/ethiopia/individual/` (personal income, other taxes, tax administration, significant developments)
- EY tax alert 2025-2542 — `taxnews.ey.com/news/2025-2542-ethiopia-issues-a-new-income-tax-proclamation`
- MyWorkpay — `myworkpay.com/blogs/ethiopia-new-income-tax-law-2025`
- PaySpace — `payspace.com/blog/ethiopia-income-tax-amendments-key-payroll-changes-2025/`
- YSA Law Office — Proclamation 1395/2025 overview
- countrytaxcalc.com/tax-calculator/ethiopia/
- 2merkato — Private Organization Employees Pension
- EY / haymanotbelay.com — VAT Proclamation 1341/2024

### Items NOT Verified in This Build (do not assert)

1. PAYE quick-calc deduction constants — derived (correct math), not published verbatim.
2. ETB 15,000 pension salary ceiling — secondary sources only.
3. Schedule D withholding rates (dividends/interest/royalties).
4. Exact penalty/interest figures (Proclamation 983/2016).
5. Civil-servant minimum wage (ETB 4,800) — note: Ethiopia has NO statutory private-sector minimum wage. Source: minimum-wage.org/international/ethiopia.

### Test Suite

**Test 1 — Low earner PAYE.**
Input: gross taxable salary 3,000/month.
Expected: PAYE = 3,000×0.15 − 300 = 150. Pension 210. Net 2,640.

**Test 2 — Mid earner PAYE.**
Input: 6,000/month.
Expected: PAYE = 6,000×0.20 − 500 = 700. Pension 420. Net 4,880.

**Test 3 — Upper-mid PAYE.**
Input: 12,000/month.
Expected: PAYE = 12,000×0.30 − 1,350 = 2,250. Pension 840. Net 8,910.

**Test 4 — Top-band PAYE (no ceiling).**
Input: 20,000/month, no pension cap.
Expected: PAYE = 20,000×0.35 − 2,050 = 4,950. Pension 1,400. Net 13,650.

**Test 5 — Exempt earner.**
Input: 2,000/month.
Expected: PAYE = 0. Pension 140. Net 1,860.

**Test 6 — Schedule C with MAT check.**
Input: annual taxable business income 200,000, turnover 600,000.
Expected: income tax = 34,200 + (32,000×0.30=9,600) = 43,800. MAT = 2.5%×600,000 = 15,000. Tax due = max(43,800, 15,000) = 43,800.

**Test 7 — Category B turnover tax.**
Input: non-professional, non-VAT, annual gross sales 400,000.
Expected: 400,000 falls in 100,001–500,000 band → 3% × 400,000 = 12,000.

**Test 8 — Pension total check.**
Input: employee 7% + employer 11%.
Expected: total = 18%.

## PROHIBITIONS

- NEVER use the obsolete pre-2025 PAYE deductions (60 / 142.50 / 302.50 / 565 / 955 / 1,500)
- NEVER assert the PAYE quick-calc deductions as authoritative without the [RESEARCH GAP] caveat
- NEVER assert the ETB 15,000 pension ceiling as confirmed — flag it
- NEVER state Schedule D (dividend/interest/royalty) rates without confirmation
- NEVER state specific penalty or interest figures — they are unverified
- NEVER apply pension contributions to a foreign national without confirming Ethiopian-origin status
- NEVER apply worldwide-income scope without confirming residence
- NEVER treat all allowances as taxable without flagging the exempt-allowance question
- NEVER skip the MAT comparison for business income
- NEVER present tax calculations as definitive — always label as estimated, pending reviewer sign-off
- NEVER confuse the Ethiopian fiscal year (8 Jul – 7 Jul) with a calendar year

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
