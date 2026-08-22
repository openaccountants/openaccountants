---
name: belarus-income-tax
description: Use this skill whenever asked about Belarus personal income tax (podokhodny nalog / подоходный налог) for individuals, employees, self-employed persons, freelancers, and individual entrepreneurs. Trigger on phrases like "how much income tax do I pay in Belarus", "Belarus PIT", "podokhodny nalog", "13% flat tax", "25% increased rate", "FSZN contributions", "Social Protection Fund", "Belgosstrakh", "Professional Income Tax app", "self-employed Belarus", "individual entrepreneur tax", "BYN salary net pay", "tax declaration deadline 31 March", or any question about computing or filing personal income tax for a Belarusian resident or Belarus-source income. Also trigger when computing net pay from gross BYN salary, applying standard deductions, classifying bank-statement income/expenses, or advising on the annual self-declaration. This skill covers PIT rates (13%/25%/30%), FSZN social contributions, accident insurance, standard deductions, the Professional Income Tax regime, individual entrepreneur taxation, filing forms, deadlines, and penalties. ALWAYS read this skill before touching any Belarus income tax work.
version: 0.1
jurisdiction: BY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belarus Income Tax -- Individuals & Self-Employed

## Belarus Income Tax -- Individuals & Self-Employed Skill v0.1

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Belarus (Republic of Belarus) |
| Tax | Personal income tax (podokhodny nalog / подоходный налог с физических лиц) |
| Currency | BYN (Belarusian ruble) only |
| Tax year | Calendar year (1 January -- 31 December) (Source: revera.legal) |
| Primary legislation | Tax Code of the Republic of Belarus, Special Part (Особенная часть), Chapter 18 — individual income tax |
| Recent amendments | Law No. 47-Z of 13 Dec 2024 (effective 1 Jan 2025); tax-law amendment signed 29 Dec 2025 (effective 2026) (Source: vmp.by; president.gov.by) |
| Tax authority | Ministry of Taxes and Duties of the Republic of Belarus (MNS / МНС — nalog.gov.by) |
| Social contributions | Social Protection Fund (FSZN / ФСЗН — ssf.gov.by); accident insurance via Belgosstrakh |
| Filing portal | MNS electronic declaration services (nalog.gov.by) |
| Annual declaration deadline | 31 March of the year following the tax year (Source: revera.legal) |
| Payment deadline (declared income) | 1 June of the following year (one calculator cites 15 May) [RESEARCH GAP — reviewer to confirm exact 2025 payment date] |
| Validated by | Pending — requires sign-off by a qualified Belarusian tax adviser |
| Validation date | Pending |
| Skill version | 0.1 |

### Personal Income Tax (PIT) Rates -- 2025

**PIT Rates table**

| Income / category | Rate | Notes |
| --- | --- | --- |
| Standard rate (employment, most income) | 13% | Flat rate covering ~98% of employed persons (Source: president.gov.by tax-system page) |
| Increased rate on high income (2025) | 25% | Applies to the portion of total annual income exceeding **BYN 220,000** (raised from BYN 200,000 for 2024) (Source: president.gov.by; eor.by; taxatlas.io) |
| Top rate | 30% | Article 214 §3 sets 30% where calendar-year income exceeds **BYN 500,000** (some summaries cite BYN 600,000) [RESEARCH GAP — reviewer to confirm exact 2025 PIT threshold and whether it applies to all individuals or mainly IEs] (Source: president.gov.by; secondary summaries) |
| Concealed / illegally-derived income | 26% | Penal rate on income concealed from tax authorities or from illegal business activity; figure cited for 2024 [RESEARCH GAP — reviewer to confirm persists for 2025] (Source: GSL) |
| Gambling / lottery winnings | 4% | (Source: GSL) |

**2026 (confirmed by law signed 29 Dec 2025):** the 25% threshold rises from BYN 220,000 to **BYN 350,000**, and the income base for the higher rate is broadened to include share-sale gains, loan interest, rent, supervisory-board remuneration, and lawyer/notary income (Source: president.gov.by event 1767167458). **Do not conflate the 2025 and 2026 thresholds.**

### Self-Employed / Entrepreneur Rates -- 2025

**Self-Employed / Entrepreneur Rates table**

| Regime | Rate | Notes |
| --- | --- | --- |
| Professional Income Tax (PIT app regime) — lower band | 10% | On income up to BYN 60,000 received from Belarusian organisations/IEs and from individuals (Source: help.solarstaff.com; spex.by) |
| Professional Income Tax — upper band | 20% | On the excess above BYN 60,000 (Source: help.solarstaff.com) |
| Professional Income Tax — pensioners | 8% | Reduced rate for pensioners (Source: help.solarstaff.com) |
| Individual Entrepreneur (general regime) | 20% | Standard rate on IE net income (Source: arzinger.by; allfordmorisson.by) |
| Individual Entrepreneur — high income | 30% | Where annual income exceeds ~BYN 500,000 (Art. 214 §3) (Source: GSL) |
| Individual Entrepreneur — alternate figure | 16% | A 16% rate also appears in sources for IEs / unexplained income [RESEARCH GAP — reviewer to confirm which applies in 2025] (Source: chandrawatpartners.com) |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| PIT rate for ordinary resident employee/individual | 13% flat (Source: president.gov.by) |
| 25% increased-rate threshold | BYN 220,000 for 2025; BYN 350,000 for 2026 (Source: president.gov.by) |
| Employer social cost | 34% FSZN + ~0.6% Belgosstrakh ≈ 34.6% on top of gross (Source: G-P; eor.by) |
| Employee withholding | 13% PIT + 1% FSZN ≈ 14% of gross (Source: payslip.com; recruitment.by) |
| Self-employed default regime | Professional Income Tax: 10% up to BYN 60,000, 20% above (8% pensioners) (Source: help.solarstaff.com) |
| Unknown residency | STOP — do not apply worldwide-income treatment without confirming >183-day presence |
| Unknown whether monthly income ≤ BYN 1,164 | No personal deduction (deduction only available below threshold) |
| Unknown expense business purpose (IE) | Not deductible |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — Bank statement for the full tax year (CSV, PDF, or pasted text) in BYN, plus confirmation of (a) tax residency (>183 days in Belarus in the calendar year), (b) status (employee / self-employed under Professional Income Tax / individual entrepreneur), and (c) whether any income was NOT taxed at source by a Belarusian tax agent.
- **Recommended inputs** — Payroll slips (employer withholding records), FSZN contribution records, Professional Income Tax app receipts, marital/dependant status (for standard deductions), prior-year declaration.
- **Ideal inputs** — Full income and expenditure records, evidence supporting standard and social/property deductions, foreign-source income statements, prior assessments.
- **Refusal if minimum is missing** — SOFT WARN. No bank statement at all = hard stop. Bank statement without supporting records = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify residency, that all income taxed at source is correctly excluded from the self-declaration, and that any deductions claimed are supported."

### Refusal Catalogue

- **R-BY-1 -- Residency unknown** — Belarus taxes residents (>183 days/year) on worldwide income and non-residents on Belarus-source income only. This skill cannot compute tax without confirming residency status. Please confirm before proceeding.  _(revera.legal)_
- **R-BY-2 -- Companies and legal entities** — This skill covers individuals, self-employed persons, and individual entrepreneurs only. Corporate profit tax (налог на прибыль) for legal entities is out of scope. Escalate to a Belarusian tax adviser.
- **R-BY-3 -- High-income / 25%-30% bracket near threshold** — Income approaching or exceeding BYN 220,000 (2025) engages the increased 25% rate, and the 30% top-rate trigger is not fully reconciled in this skill [RESEARCH GAP]. Escalate to a Belarusian tax adviser for high-income returns.
- **R-BY-4 -- HTP / special regimes** — High-Tech Park (HTP) residents historically benefited from a reduced 9% PIT; current treatment is unconfirmed [RESEARCH GAP]. Free Economic Zone, Great Stone, and other special regimes are out of scope. Escalate.
- **R-BY-5 -- Arrears / enforcement / concealed income** — Concealed or undeclared income is taxed at a penal 26% rate plus administrative/criminal liability. Do not advise on concealment or enforcement matters. Escalate to a Belarusian tax adviser immediately.  _(GSL)_
- **R-BY-6 -- VAT or corporate filing requested** — This skill covers personal income tax only. For Belarus VAT (НДС) or corporate profit tax, use the appropriate dedicated skill.
- **R-BY-7 -- Cross-border / sanctions complexity** — Belarus is under significant Western sanctions affecting cross-border payments, dividends, and banking. Domestic statutory rates are unchanged, but cross-border treatment requires specialist advice. Escalate.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Belarusian statements are typically in Russian; common terms are given in both. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ЗАРПЛАТА, ZARPLATA, ОПЛАТА ТРУДА, SALARY, AVANS | Employment income — PIT withheld at source by employer | Already taxed; exclude from self-declaration. Verify employer withheld 13% PIT + 1% FSZN |
| ГОНОРАР, HONORAR, ОПЛАТА УСЛУГ, FEES, PROFESSIONAL FEES | Self-employment / professional income | Professional Income Tax (10%/20%) or IE income depending on status |
| ВОЗНАГРАЖДЕНИЕ, VOZNAGRAZHDENIE, CONSULTANCY | Self-employment income | Confirm regime (PIT app vs IE) |
| STRIPE PAYOUT, PAYPAL, WISE TRANSFER, REVOLUT | Platform payout (foreign-source likely) | May be self-declared income if not via Belarusian tax agent; sanctions may restrict |
| UPWORK, FIVERR, FREELANCE PLATFORM | Freelance income | Self-employment income — match to PIT-app receipts |
| АРЕНДА ПОЛУЧЕНА, ARENDA, RENT RECEIVED | Rental income | Self-declared if not taxed at source |
| ПРОЦЕНТЫ, PROCENTY, INTEREST RECEIVED | Interest income | Check taxability; from 2026 loan interest enters the higher-rate base |
| ДИВИДЕНДЫ, DIVIDENDY, DIVIDEND | Dividend income | Resident dividend = 13% (see Section 5.7); usually withheld by payer |
| ВЫИГРЫШ, VYIGRYSH, LOTTERY, GAMBLING WIN | Winnings | Taxed at 4% (Source: GSL) |
| ВОЗВРАТ НАЛОГА, NALOG REFUND, TAX REFUND | EXCLUDE | Refund from prior year, not income |
| ПОСОБИЕ, POSOBIE, BENEFIT, FSZN PAYMENT | EXCLUDE / check | State benefits generally not PIT income [reviewer to confirm specific benefit] |

### 3.2 Expense Patterns (Debits) -- Deductible Only for Individual Entrepreneurs (general regime)

Note: salaried employees and Professional Income Tax (app) users generally cannot deduct business expenses — the 10%/20% PIT-app rates apply to gross receipts. The deductions below apply only to IEs on the general 20% regime computing **net** income.

**IE-deductible expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| АРЕНДА ОФИСА, ARENDA OFISA, OFFICE RENT | Office rent | IE-deductible | Business premises |
| БУХГАЛТЕР, BUHGALTER, ACCOUNTANT, AUDIT | Accountancy fees | IE-deductible |  |
| ЮРИСТ, YURIST, ADVOKAT, LEGAL | Legal fees | IE-deductible | Must be business-related |
| КАНЦТОВАРЫ, KANCTOVARY, OFFICE SUPPLIES | Office supplies | IE-deductible |  |
| РЕКЛАМА, REKLAMA, MARKETING, GOOGLE ADS | Marketing/advertising | IE-deductible |  |
| БАНКОВСКАЯ КОМИССИЯ, BANK FEE, КОМИССИЯ | Bank charges | IE-deductible | Business account |
| ХОСТИНГ, HOSTING, DOMAIN, CLOUD | IT infrastructure | IE-deductible |  |

### 3.3 Expense Patterns (Debits) -- Software / SaaS (IE general regime)

**Software/SaaS expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| 1С, 1C, MICROSOFT, GOOGLE WORKSPACE | Software subscription | IE-deductible | Recurring operating expense |
| ADOBE, CANVA, FIGMA, NOTION, ZOOM | Software subscription | IE-deductible |  |
| ANTHROPIC, OPENAI, GITHUB | Software subscription | IE-deductible |  |

### 3.4 Expense Patterns (Debits) -- NOT Deductible / Exclude

**NOT deductible expense patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| РЕСТОРАН, RESTORAN, КАФЕ, ENTERTAINMENT | NOT deductible | Personal/entertainment |
| ПРОДУКТЫ, PRODUKTY, СУПЕРМАРКЕТ, GROCERIES | NOT deductible | Private living costs |
| ШТРАФ, SHTRAF, FINE, PENALTY, ПЕНЯ | NOT deductible | Public policy |
| ПОДОХОДНЫЙ НАЛОГ, PIT PAYMENT, INCOME TAX | NOT deductible | Tax payment, not an expense |
| ЛИЧНЫЙ ПЕРЕВОД, PERSONAL TRANSFER, DRAWINGS | NOT deductible | Drawings |

### 3.5 Mandatory Contributions and Tax Movements (Not Ordinary Expenses)

**Mandatory contributions / tax movements table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ФСЗН, FSZN, СОЦСТРАХ, SOCIAL PROTECTION FUND | Social contribution | Employee 1% withheld; self/IE pays own FSZN (see Section 5.4) |
| БЕЛГОССТРАХ, BELGOSSTRAKH, ACCIDENT INSURANCE | Accident insurance | Employer-paid ~0.6% (Source: G-P) |
| ПОДОХОДНЫЙ, PIT WITHHELD | Tax movement | PIT remitted to MNS — not a deductible expense |
| ВНУТРЕННИЙ ПЕРЕВОД, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| ПОГАШЕНИЕ КРЕДИТА, LOAN REPAYMENT | EXCLUDE | Loan principal movement |

### 3.6 Belarusian Banks -- Statement Format Reference

**Belarusian Banks table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Belarusbank (Беларусбанк) | ЗАЧИСЛЕНИЕ, СПИСАНИЕ, ОПЛАТА | Largest state bank; Russian-language descriptions; DD/MM/YYYY |
| Belagroprombank (Белагропромбанк) | ПЕРЕВОД, ОПЛАТА УСЛУГ | State bank |
| Belinvestbank (Белинвестбанк) | ПЛАТЕЖ, КОМИССИЯ |  |
| Priorbank (Приорбанк) | TRANSFER, PAYMENT, КАРТА | Often bilingual |
| Alfa-Bank Belarus (Альфа-Банк) | ОПЛАТА, ПЕРЕВОД, CARD | Clean counterparty names |

## Section 4 -- Worked Examples

All figures in BYN. Tax year 2025. PIT verified arithmetic shown inline.

### Example 1 -- Standard Salaried Employee (income above deduction threshold)

**Input line:**
`25/03/2025 ; БЕЛАРУСБАНК ЗАЧИСЛЕНИЕ ; РАБОТОДАТЕЛЬ ООО "АЛЬФА" ; ЗАРПЛАТА МАРТ ; +2,580.00 ; BYN`

**Reasoning:**
This is net salary already credited. Reconstruct from a gross of BYN 3,000/month. Monthly income BYN 3,000 exceeds BYN 1,164, so NO standard personal deduction applies. PIT = 3,000 × 13% = BYN 390.00. Employee FSZN = 3,000 × 1% = BYN 30.00. Net = 3,000 − 390 − 30 = **BYN 2,580.00**. Employer separately pays FSZN 34% (BYN 1,020) + Belgosstrakh ~0.6% (BYN 18). (Source: president.gov.by; ssf.gov.by; G-P)

**Classification:** Employment income, PIT withheld at source. Excluded from any self-declaration.

### Example 2 -- Low-Income Employee with Standard Deduction and One Child

**Input line:**
`25/04/2025 ; БЕЛИНВЕСТБАНК ; РАБОТОДАТЕЛЬ ; ЗАРПЛАТА ; +978.24 ; BYN`

**Reasoning:**
Gross monthly salary BYN 1,100. Because 1,100 ≤ BYN 1,164, the BYN 192 personal deduction applies; plus BYN 56 for one child under 18. Taxable base = 1,100 − 192 − 56 = BYN 852.00. PIT = 852 × 13% = BYN 110.76. Employee FSZN = 1,100 × 1% = BYN 11.00. Net = 1,100 − 110.76 − 11.00 = **BYN 978.24**. (Source: eor.by; by.icalculator.com)

**Classification:** Employment income with standard + child deduction applied.

### Example 3 -- Self-Employed under Professional Income Tax (PIT app)

**Input line:**
`12/06/2025 ; ПРИОРБАНК ; ООО "КЛИЕНТ" ; ОПЛАТА УСЛУГ ; +5,000.00 ; BYN`

**Reasoning:**
Freelancer registered under the Professional Income Tax regime, total annual income BYN 80,000 received from Belarusian organisations. First BYN 60,000 at 10% = BYN 6,000. Excess BYN 20,000 at 20% = BYN 4,000. Annual Professional Income Tax = **BYN 10,000**. Tax is assessed and paid monthly via the official app; no separate annual return is required; receipts are generated per payment. (Source: help.solarstaff.com; spex.by)

**Classification:** Self-employment income, Professional Income Tax regime.

### Example 4 -- High-Income Individual Crossing the 25% Threshold (2025)

**Input (annual aggregate):**
Total 2025 income BYN 250,000.

**Reasoning:**
For 2025, income up to BYN 220,000 is taxed at 13%, and the portion above BYN 220,000 at 25%. First 220,000 × 13% = BYN 28,600. Excess 30,000 × 25% = BYN 7,500. Total PIT = **BYN 36,100**. (Source: president.gov.by; eor.by) Note: if this were 2026, the 25% threshold would be BYN 350,000 and the whole BYN 250,000 would be at 13% = BYN 32,500 — **do not conflate years.**

**Classification:** High-income individual; 25% increased rate engaged for 2025. Flag for reviewer (R-BY-3).

### Example 5 -- Individual Entrepreneur (general 20% regime)

**Input (annual):**
IE gross receipts BYN 90,000; documented deductible business expenses BYN 30,000.

**Reasoning:**
IE on the general regime taxes net income. Net = 90,000 − 30,000 = BYN 60,000. PIT = 60,000 × 20% = **BYN 12,000**. The 30% rate would apply only on income above ~BYN 500,000 [RESEARCH GAP — threshold]. (Source: arzinger.by; GSL) Note: a 16% figure also appears in some sources for IEs [RESEARCH GAP — reviewer to confirm applicable 2025 rate].

**Classification:** Individual entrepreneur, general regime. Flag for reviewer.

### Example 6 -- Own-Account Transfer (Exclude)

**Input line:**
`15/05/2025 ; АЛЬФА-БАНК ; ВНУТРЕННИЙ ПЕРЕВОД — НАКОПИТЕЛЬНЫЙ ; ; -2,000.00 ; BYN`

**Reasoning:**
Transfer between the taxpayer's own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Flat 13% Standard Rate

- **Standard PIT rate** — 13%  _(Tax Code, Special Part, Chapter 18; Article 214)_
- **Flat rate description** — Belarus levies a flat 13% personal income tax (podokhodny nalog) on most income of residents; this rate covers ~98% of employed persons.  _(president.gov.by tax-system page)_

### 5.2 Increased Rates (25% and 30%)

**25% threshold by year table**

| Year | 25% applies to portion above | Source |
| --- | --- | --- |
| 2024 | BYN 200,000 | president.gov.by |
| 2025 | BYN 220,000 | president.gov.by; eor.by |
| 2026 | BYN 350,000 (broadened base) | president.gov.by event 1767167458 |

- **25%/30% application rule** — The 25% rate is applied only to the portion of total annual income above the threshold, not to the whole. A 30% top rate exists for the highest incomes; Article 214 §3 cites BYN 500,000 (some summaries say BYN 600,000) [RESEARCH GAP — reviewer to confirm exact 2025 PIT trigger and scope].  _(Article 214 §3)_

### 5.3 Tax Residency

- **Tax residency rule** — Tax residency is based on physical presence of more than 183 days in a calendar year (1 Jan – 31 Dec). Residents are taxed on worldwide income; non-residents on Belarus-source income only.  _(Tax Code, Special Part; revera.legal; taxatlas.io)_

### 5.4 Social Contributions (FSZN) and Accident Insurance

**Employer/employee FSZN and Belgosstrakh table**  _(Decree No. 40 (24.09.2024); ssf.gov.by)_

| Contribution | Payer | Rate | Base | Source |
| --- | --- | --- | --- | --- |
| FSZN — pension (employer) | employer | 28% | gross salary | ssf.gov.by; G-P |
| FSZN — social insurance (employer) | employer | 6% | gross salary | ssf.gov.by; G-P |
| **FSZN total (employer)** | **employer** | **34%** | **gross salary** | **ssf.gov.by; G-P** |
| FSZN — pension (employee) | employee | 1% | gross salary | payslip.com; recruitment.by |
| Accident insurance (Belgosstrakh) | employer | ~0.6% standard (range ~0.1%–0.9% by occupational risk class) [RESEARCH GAP — range varies by source] | gross salary | G-P; eor.by |

- **Employer total on-cost reconciliation** — Employer total = 28% + 6% = **34%** ✓. Combined employer on-cost ≈ 34% + 0.6% = **34.6%** of gross.  _(ssf.gov.by; G-P)_

**Self-employed/IE FSZN table**  _(ssf.gov.by)_

| Self-employed / IE FSZN | Payer | Rate | Base | Source |
| --- | --- | --- | --- | --- |
| Pension (mandatory) | self | 29% | self-determined base, not below minimum wage, not above 5× average wage | ssf.gov.by [RESEARCH GAP — confirm split/base] |
| Social insurance (sickness) | self | 6% | same base | ssf.gov.by [RESEARCH GAP] |
| **Self-employed total** | **self** | **35%** | **chosen base** | **ssf.gov.by** |

- **Self-employed total reconciliation** — Self-employed total = 29% + 6% = **35%** ✓. The social (sickness) portion is voluntary for some categories; the pension portion is mandatory. Minimum annual contribution is tied to the minimum wage [RESEARCH GAP — confirm 2025 mechanics from ssf.gov.by].  _(ssf.gov.by)_

### 5.5 Employee Withholding (Tax Agent Mechanics)

- **Tax agent withholding mechanics** — Employers act as tax agents, withholding 13% PIT (plus the increased rate where annual income crosses the threshold) and the 1% employee FSZN from each salary payment, and remitting both to the authorities. Total employee deduction ≈ 13% + 1% = **14%** of gross (before standard deductions).  _(payslip.com; recruitment.by)_

### 5.6 Standard Monthly Deductions (2025)

**Standard Monthly Deductions table**

| Deduction | Amount (BYN/month) | Condition | Source |
| --- | --- | --- | --- |
| Standard personal deduction | 192 | Only if monthly taxable income ≤ BYN 1,164 | eor.by; by.icalculator.com |
| Per child under 18 / per dependent | 56 | Each | eor.by |
| Enhanced per-child deduction | 107 | Parents with 2+ children, single parents, widows/widowers, guardians/foster parents, parents of disabled children | eor.by |
| Special-category deduction | 272 | Disability groups I–II, Chernobyl-affected persons, certain veterans | eor.by; by.icalculator.com |

### 5.7 Dividends to Resident Individuals

**Dividends table**

| Scenario | Rate | Source |
| --- | --- | --- |
| Standard resident dividend | 13% | spex.by; vmp.by |
| Reduced (profits not distributed 3 years) | 6% | Valid through 31 Dec 2025; abolished from 1 Jan 2026 [RESEARCH GAP — exact 3- vs 5-year retention conditions differ between sources] (spex.by) |
| Historic 0% (not distributed 5 years) | 0% | Historic (spex.by) |
| Dividends to non-residents | 25% (raised from 15%) | Effective 2025 (vmp.by) |

### 5.8 Professional Income Tax Regime (Self-Employed)

**Authority:** MNS official Professional Income Tax mobile app.

**Professional Income Tax bands table**

| Band | Rate | Source |
| --- | --- | --- |
| Income up to BYN 60,000 (from Belarusian orgs/IEs and individuals) | 10% | help.solarstaff.com; spex.by |
| Excess above BYN 60,000 | 20% | help.solarstaff.com |
| Pensioners | 8% | help.solarstaff.com |

- **Receipt and filing mechanics** — Receipts are generated in the official app on each payment received; tax is assessed and paid monthly via the app; **no separate annual return is required.**  _(help.solarstaff.com)_

### 5.9 Individual Entrepreneur (General Regime)

- **IE general regime rule** — Registered IEs on the general regime pay PIT at 20% on net income, with 30% applying above ~BYN 500,000 annual income (Art. 214 §3). The simplified single-tax / USN regimes were largely phased out for IEs across 2023–2025. A 16% figure also appears in some sources for IEs / unexplained income [RESEARCH GAP — reviewer to confirm the applicable 2025 rate].  _(arzinger.by; allfordmorisson.by; GSL)_

### 5.10 Filing Deadlines and Penalties

**Filing Deadlines and Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Annual self-declaration | Income NOT taxed at source (foreign-source, non-tax-agent income, certain property/share sales) | revera.legal |
| Declaration deadline | 31 March of the following year | revera.legal; eor.by |
| Payment of declared tax | 1 June of the following year (one calculator cites 15 May) [RESEARCH GAP — verify] | revera.legal |
| Late filing | Administrative fines in base amounts (bazovaya velichina, BYN 42 in 2025); scale with delay [RESEARCH GAP — confirm exact multiples] | — |
| Concealed/undeclared income | Penal 26% rate plus administrative/criminal liability | GSL |
| Late payment | Late-payment interest (peni) on overdue tax based on the National Bank refinancing rate | — |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 The 30% Top-Rate Threshold

The exact BYN threshold for the 30% top rate in the PIT context for 2025 is unresolved — Article 214 §3 cites BYN 500,000 but some summaries say BYN 600,000, and it is unclear whether 30% applies to all individuals or mainly IEs on general taxation. **Conservative default:** flag for reviewer; do not auto-apply 30% [RESEARCH GAP].

### 6.2 Individual Entrepreneur Deductible Expenses

IE net-income computation requires applying the wholly-and-exclusively (business-purpose) test to each expense. Personal, entertainment, and capital items require judgement. **Conservative default:** not deductible until reviewer confirms business purpose and documentation.

### 6.3 Self-Employed / IE FSZN Base

The self-determined contribution base (not below minimum wage, not above 5× average wage), the mandatory-pension vs voluntary-social split, and the 29%/6% structure need confirmation from ssf.gov.by. **Flag for reviewer** [RESEARCH GAP].

### 6.4 Foreign-Source Income and Double Taxation

Residents are taxed on worldwide income. Foreign-source income must be self-declared. Treaty relief / foreign tax credits and sanctions-affected flows require specialist analysis. **Flag for reviewer.**

### 6.5 HTP (High-Tech Park) Residents

HTP employees historically benefited from a reduced 9% PIT; reporting indicates the generally-established 13% rate applied in some 2025 cases. **Conservative default:** apply 13% and flag for reviewer to confirm current HTP treatment [RESEARCH GAP].

### 6.6 Dividend Reduced-Rate Conditions

The 6% reduced dividend rate's exact retention conditions (3 vs 5 years) differ between sources, and it is abolished from 1 Jan 2026. **Flag for reviewer** [RESEARCH GAP].

### 6.7 Property / Share Disposals

Capital gains on property and share disposals have specific rules (and from 2026 share-sale gains enter the higher-rate base). **Flag for reviewer.**

## Section 7 -- Excel Working Paper Template

```
BELARUS PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency (>183 days?): Yes / No
Status: Employee / Self-employed (PIT app) / Individual Entrepreneur

A. EMPLOYMENT INCOME (taxed at source — informational)
  A1. Gross annual salary                         ___________
  A2. PIT withheld (13%)                           ___________
  A3. Employee FSZN withheld (1%)                  ___________
  A4. Net salary received                          ___________

B. SELF-DECLARED INCOME (not taxed at source)
  B1. Foreign-source income                        ___________
  B2. Income from non-tax-agent payers             ___________
  B3. Rental income                                ___________
  B4. Other declarable income                      ___________
  B5. TOTAL self-declared income                   ___________

C. STANDARD DEDUCTIONS (monthly, only if income <= BYN 1,164)
  C1. Personal deduction (BYN 192/mo eligible?)    ___________
  C2. Child/dependant (BYN 56 each)                ___________
  C3. Enhanced child (BYN 107)                     ___________
  C4. Special category (BYN 272)                   ___________
  C5. TOTAL deductions                             ___________

D. PIT COMPUTATION (pass to deterministic engine)
  D1. Taxable base (B5 - C5, or per-month)         ___________
  D2. Portion <= BYN 220,000 @ 13%                 ___________
  D3. Portion > BYN 220,000 @ 25% (2025)           ___________
  D4. Total PIT                                    ___________

E. SELF-EMPLOYED / IE (if applicable)
  E1. Professional Income Tax: <=60k @10%          ___________
  E2. Professional Income Tax: >60k @20% (8% pens) ___________
  E3. IE net income @ 20%                          ___________
  E4. FSZN (self) 35% on chosen base               ___________

F. CONTRIBUTIONS (employer side — informational)
  F1. Employer FSZN 34%                            ___________
  F2. Belgosstrakh ~0.6%                           ___________

REVIEWER FLAGS:
  [ ] Residency (>183 days) confirmed?
  [ ] Status (employee / PIT-app / IE) confirmed?
  [ ] 25%/30% threshold — correct YEAR applied (220k 2025 / 350k 2026)?
  [ ] 30% top-rate trigger flagged [RESEARCH GAP]?
  [ ] Standard deduction only applied where income <= BYN 1,164?
  [ ] Income taxed at source correctly EXCLUDED from self-declaration?
  [ ] Self-employed FSZN base confirmed [RESEARCH GAP]?
  [ ] HTP / special regime confirmed?
  [ ] Foreign-source income / sanctions considered?
```

## Section 8 -- Bank Statement Reading Guide

### Belarusian Bank Statement Formats

**Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Belarusbank (Беларусбанк) | PDF, sometimes CSV | Дата, Описание, Дебет, Кредит, Остаток | Largest state bank; Russian-language; DD/MM/YYYY |
| Belagroprombank (Белагропромбанк) | PDF | Дата, Назначение, Сумма | State bank |
| Belinvestbank (Белинвестбанк) | PDF, CSV | Дата операции, Описание, Сумма |  |
| Priorbank (Приорбанк) | PDF, CSV | Date, Description, Amount, Balance | Often bilingual |
| Alfa-Bank Belarus (Альфа-Банк) | CSV | Дата, Контрагент, Сумма, Валюта | Clean counterparty names |

### Key Russian / Belarusian Banking and Tax Terms

**Banking and Tax Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| ЗАЧИСЛЕНИЕ / Zachislenie | Credit / incoming | Potential income — check source |
| СПИСАНИЕ / Spisanie | Debit / outgoing | Expense or transfer |
| ЗАРПЛАТА / Zarplata | Salary | Employment income (taxed at source) |
| АВАНС / Avans | Salary advance | Employment income |
| ГОНОРАР / Honorar | Fee / honorarium | Self-employment income |
| ПЕРЕВОД / Perevod | Transfer | Check direction & whether own-account |
| ОПЛАТА / Oplata | Payment | Expense — check counterparty |
| КОМИССИЯ / Komissiya | Commission / bank fee | IE-deductible bank charge |
| ФСЗН / FSZN | Social Protection Fund | Social contribution |
| ПОДОХОДНЫЙ НАЛОГ / Podokhodny nalog | Personal income tax | PIT — not an expense |
| ШТРАФ / ПЕНЯ — Shtraf / Penya | Fine / late-payment interest | NOT deductible |
| ДИВИДЕНДЫ / Dividendy | Dividends | Investment income (13% resident) |
| БАЗОВАЯ ВЕЛИЧИНА / Bazovaya velichina | Base amount (BYN 42 in 2025) | Used for fines/fees thresholds |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items and [RESEARCH GAP] items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- BELARUS PERSONAL INCOME TAX
1. Were you present in Belarus more than 183 days in the calendar year (tax resident)?
2. Status: employee, self-employed under the Professional Income Tax app, or registered individual entrepreneur?
3. Did you receive any income NOT taxed at source by a Belarusian employer/tax agent (foreign income, rent, etc.)?
4. Total annual income — is any portion above BYN 220,000 (2025 increased-rate threshold)?
5. Monthly salary — was any month at or below BYN 1,164 (for the standard personal deduction)?
6. How many children under 18 / dependants do you support? Any special category (disability, Chernobyl, veteran)?
7. If self-employed: total income from Belarusian organisations/IEs vs from individuals (10%/20% bands)?
8. If individual entrepreneur: gross receipts and documented business expenses?
9. Are you a High-Tech Park (HTP) resident?
10. Any dividends, winnings, or property/share disposals during the year?
```

## Section 10 -- Reference Material

### Key Legislation and Authority References

**Legislation/Authority References table**

| Topic | Reference | Source |
| --- | --- | --- |
| PIT rates and base | Tax Code, Special Part, Chapter 18; Article 214 | president.gov.by |
| 25%/30% increased rates | Article 214 §3; Law No. 47-Z (2024); amendment 29 Dec 2025 | president.gov.by; vmp.by |
| Social contributions | Decree No. 40 (24.09.2024); FSZN legislation | ssf.gov.by |
| Accident insurance | Belgosstrakh mandatory insurance | G-P; eor.by |
| Standard deductions | Tax Code, Chapter 18 (2025 amounts) | eor.by |
| Professional Income Tax | MNS Professional Income Tax app regime | help.solarstaff.com |
| IE general regime | Tax Code; 2023–2025 reforms | arzinger.by; allfordmorisson.by |
| Declaration & deadlines | Tax Code; MNS | revera.legal |

### Key Statutory Amounts (2025)

**Statutory Amounts table**

| Item | Value | Source |
| --- | --- | --- |
| Minimum wage (from 1 Jan 2025) | BYN 726/month (≈ BYN 4.54/hour) | WageIndicator |
| Minimum wage (from 1 Jan 2026) | BYN 858/month | take-profit.org |
| Base amount (bazovaya velichina, from 1 Jan 2025) | BYN 42 (Council of Ministers Decree No. 848, 16 Nov 2024) [RESEARCH GAP — confirm on pravo.by] | search corroboration |
| Transfer-pricing / controlled-transaction threshold | BYN 400,000 per counterparty per year (from 2025) | vmp.by |

### Thresholds Summary

**Thresholds Summary table**

| Item | Value | Source |
| --- | --- | --- |
| Tax residency | >183 days in Belarus in a calendar year | revera.legal |
| Standard personal deduction cap | Monthly income ≤ BYN 1,164 for BYN 192 deduction | eor.by |
| 25% rate (2025) | Income above BYN 220,000 | president.gov.by |
| 25% rate (2026) | Income above BYN 350,000 | president.gov.by |
| 30% rate | Income above ~BYN 500,000 [RESEARCH GAP] | GSL |
| Professional Income Tax band | BYN 60,000 (10% below / 20% above; 8% pensioners) | help.solarstaff.com |

### Test Suite

Input: Gross BYN 3,000/month; monthly income > BYN 1,164 (no personal deduction).
Expected: PIT = 3,000 × 13% = BYN 390.00. Employee FSZN = 3,000 × 1% = BYN 30.00. Net = BYN 2,580.00. Employer FSZN = BYN 1,020.00; Belgosstrakh ≈ BYN 18.00.

Input: Gross BYN 1,100/month (≤ 1,164); one child.
Expected: Base = 1,100 − 192 − 56 = BYN 852.00. PIT = 852 × 13% = BYN 110.76. FSZN = BYN 11.00. Net = BYN 978.24.

Input: Annual income BYN 250,000.
Expected: 220,000 × 13% = BYN 28,600 + 30,000 × 25% = BYN 7,500 = total PIT BYN 36,100.

Input: Same BYN 250,000 but tax year 2026.
Expected: Below BYN 350,000 threshold → entirely at 13% = BYN 32,500. (Confirms 2025 vs 2026 thresholds must not be conflated.)

Input: BYN 80,000 from Belarusian organisations (non-pensioner).
Expected: 60,000 × 10% = BYN 6,000 + 20,000 × 20% = BYN 4,000 = total BYN 10,000.

Input: Gross BYN 90,000; deductible expenses BYN 30,000.
Expected: Net = BYN 60,000; PIT = 60,000 × 20% = BYN 12,000. (30% only above ~BYN 500,000 [RESEARCH GAP].)

Input: Gross BYN 3,000.
Expected: FSZN 34% (28% + 6%) = BYN 1,020.00; Belgosstrakh ~0.6% = BYN 18.00; total employer on-cost ≈ BYN 1,038.00 (34.6%).

## PROHIBITIONS

- NEVER apply worldwide-income treatment without confirming >183-day residency
- NEVER conflate the 2025 (BYN 220,000) and 2026 (BYN 350,000) 25%-rate thresholds
- NEVER auto-apply the 30% top rate — the threshold is unresolved [RESEARCH GAP]; flag for reviewer
- NEVER apply the standard BYN 192 personal deduction where monthly income exceeds BYN 1,164
- NEVER include income already taxed at source by a Belarusian tax agent in the annual self-declaration
- NEVER treat employee FSZN (1%) or employer FSZN (34%) as a deductible business expense
- NEVER allow fines, penalties, or peni as a deduction
- NEVER allow income tax (podokhodny nalog) itself as a deduction
- NEVER deduct IE business expenses without confirming business purpose and documentation
- NEVER advise on concealment of income — concealed income carries a penal 26% rate plus criminal liability
- NEVER present tax calculations as definitive — always label as estimated and pending reviewer sign-off

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. This is a Tier-2 (research-verified) skill at medium confidence: several figures carry [RESEARCH GAP] markers and must be reconciled against the Tax Code Special Part and pravo.by before reliance.

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
