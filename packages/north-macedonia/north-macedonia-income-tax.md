---
name: north-macedonia-income-tax
description: Use this skill whenever asked about North Macedonia (Republic of North Macedonia) personal income tax for self-employed individuals and employees. Trigger on phrases like "how much tax do I pay in Macedonia", "Macedonian income tax", "personal income tax", "данок на личен доход", "MPIN salary declaration", "social contributions Macedonia", "denar payroll", "gross-to-net Macedonia", "self-employed tax Macedonia", "service contract tax", "UJP", "Public Revenue Office", "annual draft tax return", or any question about filing or computing personal income tax (PIT) for an employed or self-employed client in North Macedonia. Also trigger when preparing or reviewing a monthly salary calculation, a service-contract withholding, or an annual self-employed tax balance, computing the 28% social contributions, or advising on the MKD 10,270 personal exemption. This skill covers the flat 10% PIT, the 15%/70% special rates, social-contribution rates and bases, the personal monthly exemption, registration thresholds, forms/deadlines, and interaction with VAT. ALWAYS read this skill before touching any North Macedonia income tax work.
version: 0.1
jurisdiction: MK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# North Macedonia Personal Income Tax -- Individuals & Self-Employed

## North Macedonia Personal Income Tax -- Individuals & Self-Employed Skill v0.1

> **Tier 2 (research-verified) skill.** Figures below are drawn from PwC Worldwide Tax Summaries, the Eurofast North Macedonia Tax Card 2025 / Payroll Guide 2025, and Bloomberg Tax reporting the Public Revenue Office's January 2025 wage-threshold clarification. Several material figures (the 28% contribution split, the MKD 10,270 personal exemption, the MKD 63,154 average salary, and the MKD 31,577 / 1,010,464 / 757,848 contribution bases) could not be re-rendered directly from a machine-readable UJP/Ministry of Finance page during research and should be reconfirmed against the official UJP "contribution bases" table and the State Statistical Office average-salary release before sign-off. Items marked **[RESEARCH GAP — reviewer to confirm]** are unresolved.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | North Macedonia (Republic of North Macedonia) |
| Tax | Personal Income Tax -- PIT (данок на личен доход) |
| Currency | MKD (Macedonian denar) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Law on Personal Income Tax (Закон за данокот на личен доход), Official Gazette 241/2018 and subsequent amendments |
| Supporting legislation | Law on Mandatory Social Insurance Contributions; Law on Value Added Tax; Labour Relations Law (Official Gazette 62/05 and amendments) |
| Tax authority | Public Revenue Office (Управа за јавни приходи -- UJP / PRO), www.ujp.gov.mk; policy set by Ministry of Finance (finance.gov.mk) |
| Filing portal | UJP e-Services / e-Tax (e-Danoci); MPIN salary system for payroll |
| Annual draft return | PRO delivers draft by 30 April; taxpayer confirms/corrects by 31 May of the following year [PwC, Tax administration] |
| Self-employed annual return | 15 March of the following year; final settlement by 30 June [PwC, Tax administration] |
| Validated by | Pending — requires sign-off by a North Macedonia licensed accountant / tax advisor |
| Validation date | Pending |
| Skill version | 0.1 |

### PIT Rate Schedule (2025)

North Macedonia applies a **flat tax**, not progressive brackets. There is no cumulative-bracket table; each income type is taxed at a single rate.

### PIT Rate Schedule (2025)

**PIT Rate Schedule (2025)**

| Income type | Rate | Source |
| --- | --- | --- |
| Employment income | 10% | PwC, Taxes on personal income |
| Self-employment / business income | 10% | PwC, Taxes on personal income |
| Royalties and industrial-property rights | 10% | PwC, Taxes on personal income |
| Sale of own agricultural products | 10% | PwC, Taxes on personal income |
| Rental income | 10% | PwC, Taxes on personal income |
| Income from capital (dividends, interest) | 10% | PwC, Taxes on personal income |
| Capital gains (taxable) | 10% | PwC, Taxes on personal income |
| Insurance income | 10% | PwC, Taxes on personal income |
| Other uncategorised taxable income | 10% | PwC, Taxes on personal income |
| Gains from games of chance | 15% | PwC, Taxes on personal income |
| Income of unproven origin | 70% | PwC, Taxes on personal income |
| Capital gains on securities / investment-fund shares held > 2 years | 0% (exempt) | PwC, Taxes on personal income |
| Gains from termed deposits | 0% (taxation postponed until EU accession) | PwC, Taxes on personal income |

### PIT Rate Schedule (2025)

**There are no progressive bands. The flat 10% is the headline rate for almost all income.** Personal relief takes the form of a fixed monthly exemption (see below), not a 0% band.

### Social Contribution Rates (2025) -- borne entirely by the employee on gross salary

**Social Contribution Rates (2025)**

| Class (Macedonian) | Employee rate | Employer rate | Source |
| --- | --- | --- | --- |
| Pension and disability insurance (Пензиско и инвалидско осигурување) | 18.8% | 0% | PwC, Other taxes |
| Health insurance (Здравствено осигурување) | 7.5% | 0% | PwC, Other taxes |
| Unemployment insurance (Осигурување во случај на невработеност) | 1.2% | 0% | PwC, Other taxes |
| Additional health / disability (work-injury / occupational-disease)* | 0.5% | 0% | PwC, Other taxes |
| **TOTAL mandatory social contributions** | **28.0%** | **0%** | Eurofast Tax Card 2025 |

### Social Contribution Rates (2025) -- borne entirely by the employee on gross salary

*The 0.5% component is labelled "additional health insurance" by PwC and "disability" by the Eurofast Tax Card; both agree on the 0.5% rate and the 28% total.

**Arithmetic check:** 18.8 + 7.5 + 1.2 + 0.5 = **28.0%** (employee column). Employer column: 0 + 0 + 0 + 0 = **0%**. North Macedonia has **no separate employer-side social contribution** — the entire burden sits on the employee's gross salary and is withheld/remitted by the employer [PwC; Eurofast Tax Card 2025].

### Contribution Bases (2025)

**Contribution Bases (2025)**

| Base | Amount (per month) | Basis | Source |
| --- | --- | --- | --- |
| National average gross salary (reference) | MKD 63,154 | State Statistical Office figure published Jan 2025 | PwC, Other taxes |
| Minimum contribution base (floor) | MKD 31,577 | 50% of average gross salary (63,154 × 0.50) | Bloomberg Tax citing PRO |
| Maximum contribution base — employees (ceiling) | MKD 1,010,464 | 16 average gross salaries (63,154 × 16) | Bloomberg Tax citing PRO |
| Maximum contribution base — self-employed | MKD 757,848 | 12 average gross salaries (63,154 × 12) | Bloomberg Tax citing PRO |

### Contribution Bases (2025)

**Arithmetic check:** 63,154 × 0.50 = 31,577 ✓ · 63,154 × 16 = 1,010,464 ✓ · 63,154 × 12 = 757,848 ✓. Ceiling (1,010,464) ≥ floor (31,577) ✓.

### Personal Exemption & Wage Reference Figures (2025)

**Personal Exemption & Wage Reference Figures (2025)**

| Item | Amount | Source |
| --- | --- | --- |
| Monthly personal tax-free exemption (salary only) | MKD 10,270 / month | Eurofast Tax Card 2025 |
| Minimum gross wage (effective March 2025) | MKD 36,037 / month (net ≈ MKD 24,379; hourly ≈ MKD 207) | Pepeljugoski law office |
| Business-activity registration threshold | MKD 1,000,000 total annual income | PwC, Income determination |
| VAT registration threshold | MKD 2,000,000 turnover | Company Formation Macedonia |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown income type | Treat as "other income" at flat 10% — do NOT assume an exemption applies |
| Unknown whether income is salary | Do NOT apply the MKD 10,270 exemption (it is salary-only) |
| Unknown employment vs service-contract status | Service contract (PIT only, no social contributions on it) [Eurofast] |
| Unknown gross-vs-net of a salary figure | STOP — ask whether the figure is gross or net before computing |
| Unknown contribution base relief | Apply contributions on actual gross between the floor and ceiling |
| Unknown self-employed contribution ceiling | Use self-employed maximum base MKD 757,848/month |
| Unknown allowance-style base reduction | Do NOT apply (use full gross) until reviewer confirms the income category |
| Unknown VAT registration status | Assume not registered (no VAT split) until confirmed |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — for a salary computation: the gross monthly salary in MKD and confirmation that the figure is gross. For self-employment: the annual net business income (tax balance) or a full-year bank statement in CSV, PDF, or pasted text, plus confirmation of resident status.

**Recommended** — payslips / MPIN declarations for the year, the income category for each receipt (employment, service contract, rental, royalty, agricultural, capital, capital gain), SSC payment records, prior-year tax balance, VAT registration status.

**Ideal** — complete income and expenditure account for self-employed clients, asset register, prior-year annual accounts / tax balance, evidence supporting any base reductions (agricultural sales, IP rights, property lease deductions).

**Refusal if minimum is missing — SOFT WARN.** No salary figure / no bank statement at all = hard stop. A salary figure with no gross/net confirmation = hard stop (the entire computation hinges on it). A bank statement without supporting invoices for a self-employed client = proceed with reviewer warning: "This computation was produced from the bank statement alone. The reviewer must verify the income categorisation and that any base reductions or deductible contributions are supported."

### Refusal Catalogue

- **R-MK-1 — Gross/net of salary unknown** — "The whole gross-to-net calculation depends on whether the figure is the gross salary (бруто плата) or the net salary (нето плата). This skill cannot compute tax without that confirmation. Please confirm before proceeding."
- **R-MK-2 — Companies / legal entities** — "This skill covers individuals and sole self-employed persons only. Profit tax for companies (corporate income tax) is a separate regime. Escalate to a North Macedonia licensed accountant."
- **R-MK-3 — Non-resident / cross-border income** — "Non-resident taxation, double-tax-treaty relief, and foreign-salary positions require specialised analysis. Out of scope here (note: salary received from abroad must be reported by 31 March of the following year [PwC]). Escalate to a licensed accountant."  _(PwC)_
- **R-MK-4 — Income of unproven origin** — "Income of unproven origin is taxed at 70% and triggers a formal PRO assessment. Do not self-classify. Escalate to a licensed accountant immediately."
- **R-MK-5 — Games of chance / gambling** — "Gains from games of chance are taxed at a special 15% rate with their own reporting. Confirm the exact nature before applying any rate. Escalate if material."
- **R-MK-6 — VAT return requested** — "This skill covers personal income tax and social contributions only. For North Macedonia VAT (DDV-04), use the dedicated VAT skill."
- **R-MK-7 — Arrears / enforcement** — "Client has outstanding tax arrears or is subject to PRO enforcement. Assessed tax under a Tax Assessment resolution must be paid within 15 days of delivery [PwC]; specific penalty amounts under the PIT Law for individuals are a research gap. Escalate to a licensed accountant."  _(PwC)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Macedonian terms are given alongside Latin transliterations and English. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Income category | Treatment | Notes |
| --- | --- | --- | --- |
| ПЛАТА, PLATA, SALARY, НЕТО ПЛАТА | Employment income | 10% PIT via MPIN | Gross-to-net already applied by employer; net hits account |
| ХОНОРАР, HONORAR, ДОГОВОР НА ДЕЛО, SERVICE CONTRACT, FEE | Service-contract income | 10% PIT, NO social contributions | Withheld/declared by payer if a legal entity [Eurofast] |
| ФАКТУРА, INVOICE, UPLATA OD KLIENT, CLIENT PAYMENT | Self-employment / business income | 10% on net income (tax balance) | If VAT-registered, extract net (excl. 18% VAT) |
| STRIPE PAYOUT, PAYPAL, WISE PAYOUT, REVOLUT | Business income | 10% on net income | Platform payout — match to invoices |
| UPWORK, FIVERR, TOPTAL | Business income | 10% on net income | Freelance platform — net of platform commission |
| КИРИЈА, KIRIJA, RENT RECEIVED, ЗАКУП | Rental income | 10% (after lease base reduction) | Unfurnished 10% deduction; furnished 15% deduction [PwC] |
| КАМАТА, KAMATA, INTEREST RECEIVED | Income from capital | 10% | Interest income |
| ДИВИДЕНДА, DIVIDENDA, DIVIDEND | Income from capital | 10% | Dividend income |
| АВТОРСКИ ПРАВА, ROYALTY, IP RIGHTS | Royalties / IP | 10% on 90% of gross (base = 90%) | IP-rights base reduced to 90% of gross [PwC] |
| ЗЕМЈОДЕЛСКИ ПРОИЗВОДИ, AGRICULTURAL SALE | Agricultural sales | 10% on 80% of gross (20% reduction) | Own agricultural products base reduced by 20% [PwC] |
| ИГРИ НА СРЕЌА, LOTARIJA, GAMES OF CHANCE, WINNINGS | Games of chance | 15% special rate | NOT 10% — special rate [PwC] |
| ПОВРАТ НА ДАНОК, TAX REFUND | EXCLUDE | Not income | PRO refund from prior period |
| ГРАНТ, GRANT, SUBVENCIJA | Check nature | Capital grant EXCLUDE; revenue grant taxable | Confirm nature before classifying |

### 3.2 Expense / Deduction Patterns (Debits) -- Self-Employed Business Costs

For self-employed individuals taxed on net business income (tax balance), ordinary business costs reduce the net income before applying 10%. Match these as deductible business expenses.

### 3.2 Expense / Deduction Patterns (Debits) -- Self-Employed Business Costs

**3.2 Expense / Deduction Patterns (Debits) -- Self-Employed Business Costs**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| КАНЦЕЛАРИСКА КИРИЈА, OFFICE RENT | Office rent | Deductible business cost | Dedicated business premises |
| СМЕТКОВОДИТЕЛ, ACCOUNTANT, BOOKKEEP | Accountancy fees | Deductible business cost |  |
| АДВОКАТ, LAWYER, LEGAL (business) | Legal fees | Deductible business cost | Must be business-related |
| МАРКЕТИНГ, GOOGLE ADS, META ADS, ADVERTISING | Marketing/advertising | Deductible business cost |  |
| СОФТВЕР, SOFTWARE, GOOGLE WORKSPACE, MICROSOFT 365, ADOBE | Software subscription | Deductible business cost | Recurring subscription = operating expense |
| ANTHROPIC, OPENAI, GITHUB, AWS, HOSTING, DOMAIN | IT infrastructure | Deductible business cost |  |
| БАНКАРСКА ПРОВИЗИЈА, BANK FEE, CHARGE | Bank charges | Deductible business cost | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible business cost |  |
| ОБУКА, TRAINING, COURSE, SEMINAR, CONFERENCE | Training | Deductible business cost | Must relate to current business |

### 3.3 Expense Patterns (Debits) -- Mixed Use (Reviewer Judgement)

**3.3 Expense Patterns (Debits) -- Mixed Use (Reviewer Judgement)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ЕВН, EVN, ЕЛЕКТРИЧНА ЕНЕРГИЈА, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| МАКЕДОНСКИ ТЕЛЕКОМ, A1, TELEKOM, BROADBAND | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| МОБИЛЕН, MOBILE, A1 MOBILE | Phone | T2 | Business-use portion only |
| ГОРИВО, GORIVO, FUEL, OKTA, MAKPETROL, PETROL | Vehicle fuel | T2 — business % only | Requires mileage log |
| ПАРКИНГ, PARKING | Parking | T2 — business % only |  |

### 3.4 Expense Patterns (Debits) -- NOT Deductible / Not a Business Cost

**3.4 Expense Patterns (Debits) -- NOT Deductible / Not a Business Cost**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| РЕСТОРАН, RESTAURANT, ENTERTAINMENT, CLIENT MEAL | Entertainment | Reviewer judgement — default NOT deductible | Confirm wholly-and-exclusively basis |
| ЛИЧНО, PERSONAL, СУПЕРМАРКЕТ, SUPERMARKET, RAMSTORE | Personal expenses | NOT deductible | Private living costs |
| КАЗНА, KAZNA, FINE, PENALTY | Fines/penalties | NOT deductible | Public policy |
| ДАНОК, TAX PAYMENT, PIT PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| ПОДИГНУВАЊЕ, DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

### 3.5 Statutory Items (Neither ordinary income nor ordinary expense)

**3.5 Statutory Items (Neither ordinary income nor ordinary expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ПРИДОНЕСИ, PRIDONESI, SOCIAL CONTRIBUTIONS, ПИО, ФЗОМ | Social contributions (28%) | Deductible from the PIT base on employment income [Eurofast]; on salary, withheld via MPIN before PIT |
| INTERNAL TRANSFER, OWN ACCOUNT, СОПСТВЕНА СМЕТКА | EXCLUDE | Own-account transfer |
| КРЕДИТ, LOAN, ОТПЛАТА НА КРЕДИТ, LOAN REPAYMENT | EXCLUDE | Loan principal movement |
| ДДВ, DDV, VAT PAYMENT | EXCLUDE | VAT liability payment, not an income-tax expense |

### 3.6 Macedonian Banks -- Statement Format Reference

**3.6 Macedonian Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| NLB Banka | ТРАНСФЕР, УПЛАТА, ИСПЛАТА, ПРОВИЗИЈА | PDF/CSV; date format DD.MM.YYYY |
| Komercijalna Banka | TRANSFER, NALOG, NAKNADA | PDF; counterparty in description field |
| Stopanska Banka | УПЛАТА, ИСПЛАТА, ТРОШОК | PDF/CSV |
| Halkbank / Sparkasse / ProCredit | PAYMENT, TRANSFER, FEE | CSV available; clean counterparty names |
| Revolut / Wise (held by MK residents) | PAYMENT, TRANSFER, CONVERSION | CSV; multi-currency — use MKD-equivalent amounts |

## Section 4 -- Worked Examples

> All examples use the 2025 methodology: **monthly salary PIT = (gross − 28% social contributions − MKD 10,270 personal exemption) × 10%** [Eurofast Payroll Guide 2025]. Each figure is recomputed end-to-end below.

### Example 1 -- Employee at the national average gross salary

**Input line:**
`25/03/2025 ; NLB PLATA ; DELOVNO DRUSTVO XYZ DOOEL ; PLATA MART ; +41,950.79 ; MKD`

**Reasoning:**
Gross salary MKD 63,154 (the 2025 average). Gross is above the floor (31,577) and below the ceiling (1,010,464), so contributions apply on the full gross.
- Social contributions: 63,154 × 28% = **MKD 17,683.12**
- After contributions: 63,154 − 17,683.12 = **MKD 45,470.88**
- Less personal exemption: 45,470.88 − 10,270 = **MKD 35,200.88** (PIT base)
- PIT at 10%: 35,200.88 × 0.10 = **MKD 3,520.09**
- Net pay: 45,470.88 − 3,520.09 = **MKD 41,950.79**

**Classification:** Contributions MKD 17,683.12; PIT MKD 3,520.09; net pay MKD 41,950.79. (Reconciles to the credit line.)

### Example 2 -- Minimum-wage employee

**Input line:**
`25/04/2025 ; KOMERCIJALNA ; FIRMA ABC ; NETO PLATA ; +24,378.98 ; MKD`

**Reasoning:**
Minimum gross wage MKD 36,037 (effective March 2025). Above the floor, below the ceiling.
- Social contributions: 36,037 × 28% = **MKD 10,090.36**
- After contributions: 36,037 − 10,090.36 = **MKD 25,946.64**
- Less personal exemption: 25,946.64 − 10,270 = **MKD 15,676.64** (PIT base)
- PIT at 10%: 15,676.64 × 0.10 = **MKD 1,567.66**
- Net pay: 25,946.64 − 1,567.66 = **MKD 24,378.98** ≈ MKD 24,379 (matches published minimum-wage net)

**Classification:** Contributions MKD 10,090.36; PIT MKD 1,567.66; net pay MKD 24,379.

### Example 3 -- Higher-paid employee (below the ceiling)

**Input line:**
`25/05/2025 ; STOPANSKA ; TECH DOO ; PLATA MAJ ; +78,787.00 ; MKD`

**Reasoning:**
Gross salary MKD 120,000. Still below the ceiling (1,010,464), so contributions on full gross.
- Social contributions: 120,000 × 28% = **MKD 33,600.00**
- After contributions: 120,000 − 33,600 = **MKD 86,400.00**
- Less personal exemption: 86,400 − 10,270 = **MKD 76,130.00** (PIT base)
- PIT at 10%: 76,130 × 0.10 = **MKD 7,613.00**
- Net pay: 86,400 − 7,613 = **MKD 78,787.00**

**Classification:** Contributions MKD 33,600; PIT MKD 7,613; net pay MKD 78,787.

### Example 4 -- Service-contract (договор на дело) income -- PIT only, no contributions

**Input line:**
`12/06/2025 ; NLB ; AGENCIJA MEDIA DOO ; HONORAR DOGOVOR NA DELO ; +45,000.00 ; MKD`

**Reasoning:**
Service-contract income paid by a legal entity to an individual is subject **only to PIT — no social contributions** [Eurofast Tax Card 2025]. The MKD 10,270 salary exemption does **not** apply (it is salary-only). The payer withholds/declares.
- PIT at 10%: 45,000 × 0.10 = **MKD 4,500.00**
- Net to individual: 45,000 − 4,500 = **MKD 40,500.00**

**Classification:** PIT MKD 4,500; no contributions; net MKD 40,500. File via the monthly PIT calculation by the 10th, pay by the 15th of the following month [PwC].

### Example 5 -- Self-employed annual net business income

**Input:** Self-employed individual keeping accounting records; annual net income (tax balance) for 2025 = MKD 800,000.

**Reasoning:**
Self-employment / business income is taxed at the flat 10% on net income from the tax balance [PwC]. No dedicated lump-sum/presumptive PIT regime was located **[RESEARCH GAP — reviewer to confirm whether a presumptive regime exists for small craftsmen/entrepreneurs]**. Contributions are computed separately on a contribution base capped at the self-employed maximum (MKD 757,848/month).
- Annual PIT: 800,000 × 0.10 = **MKD 80,000.00**

Filing: annual accounts + annual tax return by **15 March** of the following year; final settlement by **30 June**; monthly advance payments equal one-twelfth of the prior year's liability [PwC].

**Classification:** Annual PIT MKD 80,000 (excl. social contributions, computed separately).

### Example 6 -- Games-of-chance winnings (special 15% rate)

**Input line:**
`30/07/2025 ; HALKBANK ; LOTARIJA NA MK ; DOBIVKA IGRI NA SREKA ; +100,000.00 ; MKD`

**Reasoning:**
Gains from games of chance are taxed at the **special 15% rate**, not 10% [PwC].
- PIT at 15%: 100,000 × 0.15 = **MKD 15,000.00**

**Classification:** PIT MKD 15,000 at the games-of-chance rate. Do NOT apply 10% and do NOT apply the salary exemption.

### Example 7 -- Salary above the contribution ceiling

**Input:** Gross monthly salary MKD 1,200,000 (above the employee ceiling base of MKD 1,010,464).

**Reasoning:**
Contributions are capped: they apply only on the ceiling base, not the full gross.
- Contributions: 1,010,464 × 28% = **MKD 282,929.92** (capped)
- After contributions: 1,200,000 − 282,929.92 = **MKD 917,070.08**
- Less personal exemption: 917,070.08 − 10,270 = **MKD 906,800.08** (PIT base)
- PIT at 10%: 906,800.08 × 0.10 = **MKD 90,680.01**
- Net pay: 917,070.08 − 90,680.01 = **MKD 826,390.07**

**Classification:** Contributions MKD 282,929.92 (capped at the ceiling); PIT MKD 90,680.01; net pay MKD 826,390.07. Note PIT itself is NOT capped — only the contribution base is.

### 5.1 The Flat 10% Rule

- **The Flat 10% Rule** — PIT is a flat 10% on virtually all income types — employment, self-employment/business, rental, capital (dividends/interest), taxable capital gains, royalties, agricultural sales, insurance, and other uncategorised income — for tax year 2025 [PwC]. Two special rates override the flat rate: 15% on games-of-chance gains and 70% on income of unproven origin [PwC].  _(Law on Personal Income Tax (Official Gazette 241/2018 and amendments))_

### 5.2 Gross-to-Net Salary Computation

- **Order of operations for salary** — 1. Start from gross salary (бруто плата). 2. Deduct 28% social contributions (on gross between floor and ceiling). 3. Deduct the MKD 10,270 monthly personal exemption. 4. Apply 10% PIT to the remainder (the PIT base). 5. Net pay = gross − contributions − PIT. All payments (net wage, contributions, PIT) are remitted concurrently via a single encrypted payment order — the MPIN salary declaration [Eurofast].  _(Law on Mandatory Social Insurance Contributions; Eurofast Payroll Guide 2025)_

### 5.3 Social Contributions

- **Social Contributions rule** — Total mandatory contributions are 28% of gross salary (pension/disability 18.8%, health 7.5%, unemployment 1.2%, additional/disability 0.5%), all borne by the employee and withheld/remitted by the employer; there is no separate employer-side contribution [PwC; Eurofast Tax Card 2025]. Contributions are levied on gross salary between a floor of MKD 31,577/month and a ceiling of MKD 1,010,464/month for 2025 [Bloomberg Tax citing PRO]. For self-employed persons the maximum contribution base is MKD 757,848/month (12 average salaries) [Bloomberg Tax citing PRO]. Contributions on employment income are fully deductible when computing the PIT base [Eurofast Tax Card 2025].  _(Law on Mandatory Social Insurance Contributions)_

### 5.4 The Personal Exemption (salary only)

- **Personal exemption rule** — The 2025 monthly personal tax-free exemption is MKD 10,270, deducted from salary before applying 10% PIT [Eurofast]. Apply it only to salary/employment income — do not assume it applies to service contracts, business income, rental, or other categories (see Conservative Defaults).  _(Eurofast Tax Card 2025)_

### 5.5 Income-Category Base Reductions

**5.5 Income-Category Base Reductions**  _(Law on Personal Income Tax (per PwC, Income determination))_

| Income category | Base | Source |
| --- | --- | --- |
| Sale of own agricultural products | Gross reduced by 20% (base = 80%) | PwC, Income determination |
| Royalties / industrial-property rights | Base = 90% of gross | PwC, Income determination |
| Unfurnished property lease | 10% deduction from gross rent | PwC, Income determination |
| Furnished property lease | 15% deduction from gross rent | PwC, Income determination |

### 5.5 Income-Category Base Reductions

- **Mutual exclusivity note** — Apply 10% PIT to the reduced base. Do not stack the salary exemption on top of these — they are mutually exclusive categories.  _(Law on Personal Income Tax (per PwC, Income determination))_

### 5.6 Capital Gains

- **Capital Gains rule** — Taxable capital gains are taxed at 10%. Exempt: capital gains on securities and investment-fund shares held longer than two years (0%); gains from termed deposits are not taxed until EU accession [PwC].  _(Law on Personal Income Tax (per PwC))_

### 5.7 Self-Employed / Business Income

- **Self-Employed / Business Income rule** — Self-employed individuals who keep accounting records are taxed at 10% on net income from the tax balance. They file annual accounts and an annual tax return by 15 March of the following year, with final settlement by 30 June; monthly advance payments equal one-twelfth of the prior year's liability [PwC]. No dedicated lump-sum/presumptive regime for small entrepreneurs/craftsmen was located [RESEARCH GAP — reviewer to confirm].  _(Law on Personal Income Tax (per PwC))_

### 5.8 Registration & VAT Interaction

**5.8 Registration & VAT Interaction**

| Trigger | Requirement | Source |
| --- | --- | --- |
| Total annual income > MKD 1,000,000 | Register a business activity by 15 January of the following year | PwC, Income determination |
| Turnover > MKD 2,000,000 (prior year or expected) | VAT registration required | Company Formation Macedonia |
| VAT return (DDV-04) | File within 25 days after period end; pay within 30 days | Company Formation Macedonia |

### 5.8 Registration & VAT Interaction

- **VAT net income note** — For VAT-registered self-employed clients, report business income net of VAT (VAT collected is a liability, not income).

### 5.9 Filing & Deadlines

**5.9 Filing & Deadlines**

| Item | Detail | Source |
| --- | --- | --- |
| Annual draft return (pre-filled by PRO) | PRO delivers draft by 30 April; taxpayer confirms/corrects by 31 May; if no action, becomes final automatically | PwC, Tax administration |
| Self-employed annual accounts + return | 15 March of the following year; final settlement by 30 June | PwC, Tax administration |
| Monthly PIT (service-contract & other non-salary income) | File by the 10th of the following month; pay by the 15th | PwC, Tax administration |
| MPIN salary declaration | Submitted concurrently with monthly net-salary payment | Eurofast Payroll Guide 2025 |
| Foreign-salary reporting | By 31 March of the following year | PwC, Tax administration |
| VAT return (DDV-04) | Within 25 days after period; VAT paid within 30 days | Company Formation Macedonia |

### 5.10 Assessments & Penalties

**5.10 Assessments & Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| PRO denial of draft return | A Tax Assessment Form (resolution) is issued; assessed tax payable within 15 days of delivery | PwC, Tax administration |
| Administrative penalties (general) | Eurofast Tax Card lists administrative penalties for companies; **specific MKD penalty amounts for individuals/self-employed under the PIT Law were not located** | **[RESEARCH GAP — reviewer to confirm from PIT Law / UJP penalty schedule]** |

### 6.1 Home Office / Mixed-Use Premises (self-employed)

- Calculate the proportion of the home used for business and apply it to utilities, rent, and internet.
- Must be a genuinely dedicated workspace.
- **Conservative default:** 0% deduction until the reviewer confirms the arrangement.
- **Flag for reviewer:** Confirm the floor-area basis and that the workspace is dedicated.

### 6.2 Motor Vehicle Business Use (self-employed)

- Only the business-use percentage of fuel, insurance, and maintenance is deductible; requires a mileage log.
- **Conservative default:** 0% business use until a mileage log is provided.

### 6.3 Phone / Internet Mixed Use

- Business-use portion only; client must give a reasonable estimate.
- **Conservative default:** 0% deduction until the business percentage is confirmed.

### 6.4 Income Categorisation (which rate / which reduction)

- Whether a receipt is salary, service-contract income, business income, rental, royalty, or "other" changes the rate base, whether the MKD 10,270 exemption applies, and whether contributions are due.
- **Flag for reviewer:** Confirm the legal category of each material receipt before applying a reduction or exemption.

### 6.5 Entertainment / Client Hospitality (self-employed)

- North Macedonia's specific deductibility limits for entertainment were not pinned to an authoritative figure **[RESEARCH GAP — reviewer to confirm]**.
- **Conservative default:** Treat as NOT deductible until the reviewer confirms the wholly-and-exclusively basis.

### 6.6 Contribution Base Floor/Ceiling Edge Cases

- For very low salaries (below the MKD 31,577 floor) contributions may be computed on the floor base rather than actual gross.
- **Conservative default:** Apply the floor base where gross < floor; flag for reviewer.

### 6.7 Allowance-Style Base Reductions

- Agricultural (20%), IP rights (base 90%), lease (10%/15%) reductions depend on correct categorisation and documentation.
- **Flag for reviewer:** Confirm category and supporting evidence before applying a reduction.

## Section 7 -- Excel Working Paper Template

```
NORTH MACEDONIA PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Resident: Yes / No
Computation type: Salary (gross-to-net) / Service contract / Self-employed / Other

-------------------------------------------------------------
PART A -- MONTHLY SALARY (gross-to-net)
  A1. Gross salary (MKD)                          ___________
  A2. Contribution base (A1, capped 31,577..1,010,464) _______
  A3. Social contributions = A2 x 28%             ___________
        Pension/disability 18.8%   ____________
        Health 7.5%                ____________
        Unemployment 1.2%          ____________
        Additional/disability 0.5% ____________
  A4. Salary after contributions (A1 - A3)        ___________
  A5. Personal exemption                          ( 10,270  )
  A6. PIT base (A4 - A5)                           ___________
  A7. PIT = A6 x 10%                               ___________
  A8. NET PAY (A4 - A7)                            ___________

-------------------------------------------------------------
PART B -- SERVICE CONTRACT (договор на дело)
  B1. Gross fee (MKD)                              ___________
  B2. PIT = B1 x 10%   (NO contributions, NO exemption) ______
  B3. Net to individual (B1 - B2)                  ___________

-------------------------------------------------------------
PART C -- SELF-EMPLOYED (annual)
  C1. Net business income (tax balance)            ___________
  C2. Annual PIT = C1 x 10%                         ___________
  C3. Contributions (separate, base capped 757,848/mo) _______
  C4. Monthly advance = prior-year liability / 12  ___________

-------------------------------------------------------------
PART D -- OTHER CATEGORY INCOME (apply base reduction first)
  D1. Rental (less 10% unfurnished / 15% furnished) _________
  D2. Royalty / IP (base = 90% of gross)           ___________
  D3. Agricultural (base = 80% of gross)           ___________
  D4. Games of chance (rate = 15%, not 10%)        ___________
  D5. PIT on D1-D3 = base x 10%; on D4 = base x 15% ________

REVIEWER FLAGS:
  [ ] Gross vs net of salary confirmed?
  [ ] Income category confirmed for each receipt?
  [ ] Personal exemption applied to salary ONLY?
  [ ] Contributions capped at correct ceiling (employee vs self-employed)?
  [ ] Base reductions (agri/IP/lease) supported by evidence?
  [ ] Games-of-chance at 15% (not 10%)?
  [ ] VAT-registered? Income reported net of VAT?
  [ ] Service-contract income carries PIT only (no contributions)?
  [ ] RESEARCH GAP items reconfirmed against UJP?
```

## Section 8 -- Bank Statement Reading Guide

### Macedonian Bank Statement Formats

**Macedonian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| NLB Banka | PDF, CSV | Датум (Date), Опис (Description), Задолжување (Debit), Одобрување (Credit), Состојба (Balance) | Most common; description contains counterparty + reference |
| Komercijalna Banka | PDF, CSV | Date, Description, Amount, Balance | Counterparty in description field |
| Stopanska Banka | PDF | Датум, Опис, Износ | Shorter descriptions |
| Halkbank / ProCredit / Sparkasse | PDF, CSV | Date, Description, Amount, Balance | CSV export available |
| Revolut / Wise (MK resident) | CSV | Date, Counterparty, Amount, Currency, Reference | Multi-currency — use MKD-equivalent |

### Key Macedonian Banking & Tax Terms

**Key Macedonian Banking & Tax Terms**

| Term (Macedonian) | Transliteration | English | Classification Hint |
| --- | --- | --- | --- |
| Бруто плата | Bruto plata | Gross salary | Starting point for gross-to-net |
| Нето плата | Neto plata | Net salary | Amount that hits the account |
| Придонеси | Pridonesi | Contributions | The 28% social contributions |
| Данок на личен доход | Danok na licen dohod | Personal income tax | The PIT |
| Хонорар / Договор на дело | Honorar / Dogovor na delo | Fee / Service contract | PIT only, no contributions |
| Кирија / Закуп | Kirija / Zakup | Rent / Lease | Rental income (base reduction) |
| Камата | Kamata | Interest | Income from capital |
| Дивиденда | Dividenda | Dividend | Income from capital |
| Авторски права | Avtorski prava | Royalties / IP | Base = 90% of gross |
| Игри на среќа | Igri na sreka | Games of chance | Special 15% rate |
| Провизија / Трошок | Provizija / Trošok | Fee / Charge | Bank charge (business cost) |
| Уплата / Исплата | Uplata / Isplata | Inbound / Outbound payment | Check direction for income/expense |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement or salary figure but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1) — including treating ambiguous receipts as "other income" at 10% with no exemption.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- NORTH MACEDONIA PERSONAL INCOME TAX
1. Is the salary figure GROSS (бруто) or NET (нето)?
2. Employment status: employee (MPIN salary), service contract (договор на дело), or self-employed with accounting records?
3. For each material receipt: which category — salary, service contract, business, rental, royalty, agricultural, capital, capital gain, or games of chance?
4. Are you VAT-registered (turnover > MKD 2,000,000)?
5. Self-employed: what is the net business income (tax balance) for the year, and what was the prior-year liability (for monthly advances)?
6. Home office / vehicle / phone: any business-use percentage you can document?
7. Did total annual income exceed MKD 1,000,000 (business-registration trigger)?
8. Any income from abroad (foreign salary reportable by 31 March)?
9. Any games-of-chance winnings (taxed at 15%)?
```

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References**

| Topic | Reference | Source |
| --- | --- | --- |
| PIT rates & categories | Law on Personal Income Tax (Official Gazette 241/2018 & amendments) | PwC, Taxes on personal income |
| Social contributions | Law on Mandatory Social Insurance Contributions | PwC, Other taxes |
| Income determination / base reductions | Law on Personal Income Tax | PwC, Income determination |
| Filing & administration | Law on Personal Income Tax; UJP procedures | PwC, Tax administration |
| VAT | Law on Value Added Tax | Company Formation Macedonia |
| Minimum wage | Labour Relations Law (Official Gazette 62/05 & amendments) | Pepeljugoski law office |
| Tax authority | Public Revenue Office (UJP / PRO), www.ujp.gov.mk | UJP |
| Policy | Ministry of Finance, finance.gov.mk | Ministry of Finance |

### Key 2025 Figures (with provenance)

**Key 2025 Figures (with provenance)**

| Figure | Value | Source |
| --- | --- | --- |
| Flat PIT rate | 10% | PwC |
| Games-of-chance rate | 15% | PwC |
| Income-of-unproven-origin rate | 70% | PwC |
| Total social contributions | 28% (18.8 + 7.5 + 1.2 + 0.5) | PwC; Eurofast Tax Card 2025 |
| National average gross salary | MKD 63,154/month | PwC; Eurofast |
| Contribution floor | MKD 31,577/month | Bloomberg Tax citing PRO |
| Contribution ceiling (employees) | MKD 1,010,464/month | Bloomberg Tax citing PRO |
| Contribution ceiling (self-employed) | MKD 757,848/month | Bloomberg Tax citing PRO |
| Personal monthly exemption (salary) | MKD 10,270/month | Eurofast Tax Card 2025 |
| Minimum gross wage (Mar 2025) | MKD 36,037/month (net ≈ 24,379) | Pepeljugoski law office |
| Business-registration threshold | MKD 1,000,000 annual income | PwC |
| VAT registration threshold | MKD 2,000,000 turnover | Company Formation Macedonia |

### Research Caveats

- The 28% split, MKD 10,270 exemption, MKD 63,154 average salary, and MKD 31,577 / 1,010,464 / 757,848 bases come from PwC, Eurofast Tax Card 2025, and Bloomberg Tax (reporting the PRO's January 2025 clarification) rather than directly from a machine-readable UJP/Ministry page. **Reconfirm against the official UJP "contribution bases" table and the State Statistical Office average-salary release before publication.**
- The 0.5% component is "additional health insurance" (PwC) vs "disability" (Eurofast); both agree on 0.5% and a 28% total.
- Self-employed return deadline: treat **15 March** as operative (one secondary source said "end of February / 15 March electronically").
- No presumptive/lump-sum PIT regime for small entrepreneurs/craftsmen was found **[RESEARCH GAP — reviewer to confirm]**.
- Specific MKD penalty amounts under the PIT Law for individuals **[RESEARCH GAP — reviewer to confirm]**.
- Minimum wage MKD 36,037 was effective from March 2025; a further revision took effect 1 March 2026 (out of scope for the 2025 skill).
- Overall research confidence: **medium**.

### Test Suite

**Test 1 -- Average-salary employee.**
Input: Gross MKD 63,154/month, employee.
Expected: Contributions = 17,683.12 (63,154 × 0.28); after-contributions 45,470.88; PIT base 35,200.88 (− 10,270); PIT 3,520.09; net pay 41,950.79.

**Test 2 -- Minimum-wage employee.**
Input: Gross MKD 36,037/month, employee.
Expected: Contributions = 10,090.36; after-contributions 25,946.64; PIT base 15,676.64; PIT 1,567.66; net pay 24,378.98 (≈ 24,379).

**Test 3 -- Higher-paid employee (below ceiling).**
Input: Gross MKD 120,000/month.
Expected: Contributions = 33,600.00; after-contributions 86,400.00; PIT base 76,130.00; PIT 7,613.00; net pay 78,787.00.

**Test 4 -- Salary above the contribution ceiling.**
Input: Gross MKD 1,200,000/month.
Expected: Contributions capped = 1,010,464 × 0.28 = 282,929.92; after-contributions 917,070.08; PIT base 906,800.08; PIT 90,680.01; net pay 826,390.07. (PIT is NOT capped; only the contribution base is.)

**Test 5 -- Service contract.**
Input: Service-contract fee MKD 45,000 from a legal entity.
Expected: PIT = 4,500 (10%); NO social contributions; NO MKD 10,270 exemption; net 40,500.

**Test 6 -- Self-employed annual.**
Input: Net business income MKD 800,000.
Expected: Annual PIT = 80,000 (10%); contributions computed separately on a base capped at MKD 757,848/month; advances = prior-year liability ÷ 12.

**Test 7 -- Games of chance (special rate).**
Input: Winnings MKD 100,000.
Expected: PIT = 15,000 (15%, not 10%); no exemption.

**Test 8 -- Wrong rate applied (negative test).**
Input: An agent computes games-of-chance winnings at 10%.
Expected: REJECT. Games of chance are 15% [PwC]. Recompute at 15%.

**Test 9 -- Exemption misapplied (negative test).**
Input: An agent deducts the MKD 10,270 exemption from service-contract income.
Expected: REJECT. The exemption is salary-only; service-contract income gets neither contributions nor the exemption.

## PROHIBITIONS

- NEVER compute a salary net figure without confirming the input is GROSS, not net
- NEVER apply the MKD 10,270 personal exemption to anything other than salary/employment income
- NEVER add a separate employer-side social contribution — North Macedonia has none; the full 28% is on the employee
- NEVER apply 10% to games-of-chance winnings — they are taxed at 15%
- NEVER self-classify income of unproven origin (70%) — escalate
- NEVER apply social contributions to service-contract (договор на дело) income — it is PIT-only
- NEVER cap the PIT itself at the contribution ceiling — only the contribution base is capped
- NEVER stack a category base reduction (agri/IP/lease) on top of the salary exemption — categories are mutually exclusive
- NEVER report VAT collected as income for VAT-registered self-employed clients
- NEVER present a figure marked [RESEARCH GAP] as confirmed — flag it for the reviewer
- NEVER present tax calculations as definitive — always label as estimated

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
