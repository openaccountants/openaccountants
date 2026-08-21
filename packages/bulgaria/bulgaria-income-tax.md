---
name: bulgaria-income-tax
description: Use this skill whenever asked about Bulgaria personal income tax (данък върху доходите на физическите лица) for self-employed individuals, freelancers, sole traders (ET), and individuals. Trigger on phrases like "how much income tax do I pay in Bulgaria", "flat tax Bulgaria", "10% tax", "GDD", "godishna danachna deklaratsiya", "Art. 50 return", "form 2001", "ZDDFL", "freelancer tax Bulgaria", "self-employed tax Bulgaria", "normative expense deduction", "25% deduction", "40% deduction liberal profession", "ET sole trader 15%", "self-insured contributions", "osiguritelen dohod", "insurable income", "NRA / NAP", "NSSI / NOI", "dividend withholding tax Bulgaria", or any question about filing or computing personal income tax for a self-employed, freelance, sole-trader, or individual client in Bulgaria. Also trigger when preparing or reviewing an annual return (Art. 50 ZDDFL / form 2001) or quarterly advance PIT, computing the 25%/40%/60%/10% normative expense deduction, classifying freelancer/sole-trader bank-statement lines, or advising on social-security and health contributions for self-insured persons. This skill covers the FLAT 10% PIT (15% for sole traders / ET), the 5% final dividend withholding tax, normative expense deductions, child tax relief, social-security and health contributions for employees and self-insured persons, the annual return and quarterly advance forms, penalties, the BGN-to-EUR euro changeover (effective 1 Jan 2026), and interaction with VAT and contributions. ALWAYS read this skill before touching any Bulgarian income tax work.
version: 0.1
jurisdiction: BG
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bulgaria Personal Income Tax (ДДФЛ)

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Bulgaria (Republic of Bulgaria) |
| Tax | Personal Income Tax -- flat rate |
| Currency | BGN (Bulgarian lev) until 31 Dec 2025; **EUR from 1 Jan 2026** at the fixed rate 1 EUR = 1.95583 BGN (PwC, *Other taxes*; BTA) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Personal Income Taxes Act (ZDDFL / ЗДДФЛ). Sole-trader (ET) base determined under the Corporate Income Tax Act (ZKPO / ЗКПО) (PwC, *Income determination*) |
| Supporting legislation | Social Insurance Code (KSO / КСО); Health Insurance Act (ZZO / ЗЗО) |
| Tax authority | National Revenue Agency (NRA / НАП), https://nra.bg |
| Social security administrator | National Social Security Institute (NSSI / НОИ), https://www.nssi.bg |
| Policy oversight | Ministry of Finance, https://www.minfin.bg |
| Filing portal | NRA e-services (electronic filing) |
| Annual return deadline | 30 April of the following year (individuals); 1 March -- 30 June for sole traders / ET (PwC, *Tax administration*) |
| Validated by | Pending -- requires sign-off by a Bulgarian licensed accountant / tax adviser |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rates (2025/2026)

**Bulgaria has a single FLAT personal income tax rate. There are NO progressive brackets.** (PwC, *Taxes on personal income*)

**Tax Rates table**

| Income type | Rate | Base | Source |
| --- | --- | --- | --- |
| Individuals -- all income (employment, freelance / other self-employment, rental, capital gains, other) | **10%** | Annual taxable base | PwC, *Taxes on personal income* |
| Sole traders (ET -- едноличен търговец) | **15%** | Taxable profit determined under the Corporate Income Tax Act (income minus expenses plus tax adjustments) | PwC, *Income determination* |
| Dividends and liquidation proceeds | **5%** (final withholding tax) | Gross dividend / liquidation proceeds, Bulgarian and foreign payers | PwC, *Income determination* |

- **No personal/tax-free allowance band** — The flat 10% applies from the first lev of taxable base. Relief is delivered through normative expense deductions and specific tax reliefs (see Sections 5 and 6), not through a 0% band.

### Normative Expense Deductions (before the 10% PIT, non-ET individuals)

**Normative Expense Deductions table**

| Activity | Statutory deduction from gross | Source |
| --- | --- | --- |
| Freelancers / general self-employment | **25%** | PwC, *Deductions* |
| Liberal professions, royalties / copyright | **40%** | PwC, *Deductions* |
| Rental income (immovable property) | **10%** | PwC, *Deductions* |
| Registered agricultural producers | **60%** | PwC, *Deductions* |

- **Statutory nature of deduction** — These are statutory percentages applied automatically -- they are NOT itemised receipts. Sole traders (ET) do NOT use normative deductions; they deduct actual expenses under the Corporate Income Tax Act base.

### Social Security and Health Contribution Rates (2025, employees -- Category III, born after 1959)

Contributions are levied only on **insurable income** between the statutory monthly minimum and maximum (see Thresholds). Persons born after 31 Dec 1959 pay the 1st-pillar state pension (14.8%) PLUS the 5% 2nd-pillar Universal Pension Fund; the two together make up the pension contribution. (PwC, *Other taxes*; Ministry of Economy)

**Social Security and Health Contribution Rates table**

| Fund | Total rate | Employer | Employee | Source |
| --- | --- | --- | --- | --- |
| Pension fund (1st pillar, state DOO) | **14.8%** | 8.22% | 6.58% | Ministry of Economy / PwC, *Other taxes* |
| 2nd-pillar Universal Pension Fund (born after 1959) | **5.0%** | 2.8% | 2.2% | Ministry of Economy / PwC, *Other taxes* |
| General Sickness & Maternity Fund | **3.5%** | 2.1% | 1.4% | Ministry of Economy |
| Unemployment Fund | **1.0%** | 0.6% | 0.4% | Ministry of Economy |
| Accident at Work & Occupational Disease Fund | **0.4% -- 1.1%** (by risk class) | 0.4%--1.1% | 0% (employer only) | PwC, *Other taxes* |
| Health Insurance (NZOK / NHIF) | **8.0%** | 4.8% | 3.2% | PwC, *Other taxes* |
| **Social security subtotal (excl. health)** | **24.7% -- 25.4%** | 14.12% -- 14.82% | 10.58% | PwC, *Other taxes* |
| **GRAND TOTAL contribution burden (social security + health)** | **32.7% -- 33.4%** | **18.92% -- 19.62%** | **13.78%** | PwC, *Other taxes*; Ministry of Economy |

> **Arithmetic check (per-fund).** Employee column: pension 6.58 + 2nd-pillar 2.2 + sickness/maternity 1.4 + unemployment 0.4 + accident 0 + health 3.2 = **13.78%**. Employer column (low, 0.4% accident): 8.22 + 2.8 + 2.1 + 0.6 + 0.4 + 4.8 = **18.92%**; (high, 1.1% accident) = **19.62%**. Combined total = 13.78 + 18.92 = **32.70%** to 13.78 + 19.62 = **33.40%**. This reconciles with the PwC aggregate (social security 24.7%--25.4% + health 8.0% = 32.7%--33.4%; employer 18.92%--19.62%, employee 13.78%) and matches the sibling **bulgaria-social-contributions** skill. The earlier "27.3%" figure was incorrect: it omitted the 5% 2nd-pillar Universal Pension Fund from the employee/employer split.

> **[RESEARCH GAP -- reviewer to confirm]** The per-fund EMPLOYER/EMPLOYEE split within the pension funds (e.g. 1st-pillar 8.22%/6.58%, 2nd-pillar 2.8%/2.2%) is taken from the Ministry of Economy / PwC reconciliation; the precise statutory split should be confirmed against the Social Insurance Code (KSO) Art. 6 and the current Public Social Insurance Budget Act for the specific scenario. The work-accident rate (0.4%--1.1%) is keyed to the employer's economic-activity / NACE risk class in the Budget Act annex.

### Self-Insured Persons (freelancers / self-employed registered as SOL, born after 1959)

Self-insured persons pay ALL contributions themselves on a self-declared insurable income between the statutory min and max, reconciled annually against actual income. They do **NOT** pay unemployment or accident-fund contributions. (PwC, *Other taxes*; Ruskov & Kollegen; innovires)

**Self-Insured Persons table**

| Component | Rate | Source |
| --- | --- | --- |
| Pension fund (1st pillar, state DOO) | 14.8% | PwC, *Other taxes*; Ruskov & Kollegen |
| 2nd-pillar Universal Pension Fund (born after 1959) | 5.0% | PwC, *Other taxes*; Ruskov & Kollegen |
| Health insurance (NZOK / NHIF) | 8.0% | PwC, *Other taxes*; Ruskov & Kollegen |
| **Mandatory minimum (pension 14.8 + 2nd pillar 5.0 + health 8.0, maternity opted out)** | **27.8%** | sum (PwC; Ruskov & Kollegen; innovires) |
| General Sickness & Maternity (OPTIONAL) | +3.5% | Ruskov & Kollegen; innovires |
| **With maternity coverage opted in** | **31.3%** | sum |

> **Arithmetic check.** Pension 14.8 + 2nd-pillar 5.0 + health 8.0 = **27.8%** mandatory; + optional maternity 3.5 = **31.3%**. This matches the sibling **bulgaria-social-contributions** skill and Ruskov & Kollegen. The earlier "22.8% / 26.3%" figures were incorrect: they omitted the 5% 2nd-pillar Universal Pension Fund. Persons born before 1 Jan 1960 are outside the 2nd pillar and instead pay a higher 1st-pillar state pension; the mandatory total nets to the same overall figure -- confirm birth year for the correct fund allocation.

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown taxpayer category | STOP -- do not apply a rate until you know individual vs sole trader (ET) |
| Unknown freelancer activity type | 25% normative deduction (general self-employment) |
| Unknown employer accident-fund risk class | Use the low-end 0.4% accident rate (employer total 18.92%) and flag the exact NACE-keyed rate for the reviewer (see caveat) |
| Unknown birth year | Assume born after 1959 (2nd-pillar universal pension applies) |
| Unknown maternity-coverage election (self-insured) | Assume maternity NOT elected -- use 27.8% mandatory minimum |
| Unknown insurable-income band period | Use 1 Apr -- 31 Dec 2025 band (min BGN 1,077 / max BGN 4,130) for full-year modelling |
| Unknown VAT registration status | Assume NOT registered (gross = cost) until turnover confirmed |
| Unknown residency | STOP -- residency determines worldwide vs Bulgarian-source scope |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) taxpayer category (individual/freelancer vs sole trader ET), (b) tax residency (resident vs non-resident), and (c) whether registered as a self-insured person.

**Recommended** -- all sales invoices, freelancer activity type (for the correct normative-deduction %), social-security / health contribution payment records, the declared monthly insurable income, prior-year annual return, VAT registration status.

**Ideal** -- complete income and expenditure records, ET profit-and-loss under the CIT-Act base (if sole trader), quarterly advance-PIT payment confirmations, child-relief documentation, employment income details (if also employed).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify income completeness, the correct normative-deduction percentage, and the declared insurable-income base."

### Refusal Catalogue

- **R-BG-1** — Taxpayer category unknown. "The rate depends on category: individuals/freelancers are taxed at 10%; sole traders (ET) at 15% on a CIT-Act profit base. This skill cannot compute tax without knowing the category. Please confirm before proceeding."
- **R-BG-2** — Companies / partnerships. "This skill covers individuals, freelancers, and sole traders (ET) only. Limited companies (OOD/EOOD/AD) file corporate income tax under ZKPO. Escalate to a Bulgarian tax adviser."
- **R-BG-3** — Non-resident income. "Non-resident taxation covers Bulgarian-source income only and may engage withholding and treaty rules. Out of scope. Escalate to a Bulgarian tax adviser."
- **R-BG-4** — Capital gains on real estate / securities. "Specific exemptions and computation rules apply to property and securities disposals. Escalate to a Bulgarian tax adviser."
- **R-BG-5** — Arrears / enforcement. "Client has outstanding public liabilities or is subject to NRA enforcement. Late-payment interest (BNB base + 10 pp in 2025; ECB rate + 8 pp from 2026) accrues continuously. Do not advise. Escalate immediately."
- **R-BG-6** — VAT return requested. "This skill covers personal income tax only. For Bulgarian VAT, use the bulgaria-vat-return skill."
- **R-BG-7** — Payroll / contributions run requested. "For employer payroll processing and contribution remittance, use the bulgaria-payroll and bulgaria-social-contributions skills. This skill covers PIT computation."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement (Cyrillic or Latin). If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. Amounts are in BGN through 31 Dec 2025 and EUR from 1 Jan 2026 (1 EUR = 1.95583 BGN).

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + ПРЕВОД / PREVOD / TRANSFER, ПЛАЩАНЕ / PLASHTANE / PAYMENT, ФАКТУРА / INVOICE | Business income (gross) | Apply normative deduction at the activity rate (25%/40%/60%) before PIT |
| ХОНОРАР / HONORAR, FEES, CONSULTANCY, ГРАЖДАНСКИ ДОГОВОР (civil contract) | Business income | Freelancer fee -- typical self-employment |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Platform payout -- match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Business income | Verify against invoices |
| WISE PAYOUT, WISE TRANSFER, REVOLUT PAYOUT | Business income | Check business vs personal account |
| UPWORK, FIVERR, TOPTAL | Business income | Net of platform commission |
| ЗАПЛАТА / ZAPLATA / SALARY, ВЪЗНАГРАЖДЕНИЕ (employer name) | Employment income | NOT self-employment -- separate base, withheld monthly |
| НАЕМ / NAEM / RENT RECEIVED | Rental income | 10% normative deduction applies |
| ЛИХВА / LIHVA / INTEREST RECEIVED | Investment income | Interest income |
| ДИВИДЕНТ / DIVIDENT / DIVIDEND | Dividend income | 5% FINAL withholding -- usually already taxed at source; EXCLUDE from 10% base |
| ВЪЗСТАНОВЯВАНЕ / NRA REFUND, TAX REFUND | EXCLUDE | Tax refund -- not income |
| СУБСИДИЯ / SUBSIDY, GRANT (capital) | EXCLUDE unless revenue | Capital grants EXCLUDE; revenue grants = business income |

### 3.2 Expense Patterns (Debits) -- Sole Trader (ET) Deductible / Freelancer Context Only

> For non-ET freelancers, individual expenses are NOT itemised -- the statutory normative deduction (25%/40%/60%/10%) replaces actual-expense deductions. The patterns below are for sole traders (ET) computing a CIT-Act profit base, OR for completeness when verifying that a freelancer's claimed activity matches reality.

**Expense Patterns table**

| Pattern | Category | Treatment (ET) | Notes |
| --- | --- | --- | --- |
| НАЕМ ОФИС / OFFICE RENT (commercial) | Office rent | Deductible | Dedicated business premises |
| СЧЕТОВОДИТЕЛ / ACCOUNTANT, ОДИТОР / AUDITOR | Accountancy fees | Deductible |  |
| АДВОКАТ / LAWYER, LEGAL, НОТАРИУС / NOTARY (business) | Legal fees | Deductible | Must be business-related |
| КАНЦЕЛАРСКИ / OFFICE SUPPLIES, STATIONERY | Office supplies | Deductible |  |
| РЕКЛАМА / MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| ОБУЧЕНИЕ / TRAINING, COURSE, SEMINAR, CONFERENCE | Training | Deductible | Must relate to current business |
| БАНКОВА ТАКСА / BANK FEE, ТАКСА ОБСЛУЖВАНЕ | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing | Deductible |  |

### 3.3 Expense Patterns (Debits) -- SaaS and Software (ET)

**SaaS and Software table**

| Pattern | Category | Treatment (ET) | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX, AWS | Software / IT infrastructure | Deductible |  |

### 3.4 Contribution and Tax Patterns (Debits) -- Special Handling

**Contribution and Tax Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| НОИ / NSSI, ОСИГУРОВКИ / OSIGUROVKI, СОЦИАЛНО ОСИГУРЯВАНЕ | Social-security contribution paid | DEDUCTIBLE from the PIT base (self-insured) -- reduces taxable base, not a normal expense |
| ЗДРАВНА ВНОСКА / HEALTH CONTRIBUTION, НЗОК / NZOK | Health contribution paid | DEDUCTIBLE from the PIT base (self-insured) |
| ДАНЪК ВЪРХУ ДОХОДА / INCOME TAX, NRA PIT PAYMENT | PIT payment | EXCLUDE -- income tax is not deductible |
| АВАНСОВ ДАНЪК / ADVANCE PIT, QUARTERLY PIT | Advance PIT paid | Credit against annual liability -- NOT an expense |
| ДДС / DDS / VAT PAYMENT | EXCLUDE | VAT liability payment, not an expense |

### 3.5 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| РЕСТОРАНТ / RESTAURANT, ОБЯД / LUNCH, ВЕЧЕРЯ / DINNER, ENTERTAINMENT | NOT deductible | Personal / representative -- not a business cost for non-ET; restricted for ET |
| ХРАНИТЕЛНИ СТОКИ / GROCERIES, СУПЕРМАРКЕТ, KAUFLAND, LIDL, BILLA, FANTASTICO | NOT deductible | Private living costs |
| ГЛОБА / GLOBA / FINE, ПЕНАЛ / PENALTY, НАКАЗАНИЕ | NOT deductible | Public policy |
| ЛИЧНО ТЕГЛЕНЕ / DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | NOT deductible | Not an expense |

### 3.6 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ВЪТРЕШЕН ПРЕВОД / INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| КРЕДИТ / LOAN REPAYMENT, ПОГАСЯВАНЕ, PERSONAL LOAN | EXCLUDE | Loan principal movement |
| ДИВИДЕНТ ПОЛУЧЕН (5% already withheld) | EXCLUDE from 10% base | Final tax already paid at source |

### 3.7 Bulgarian Banks -- Statement Format Reference

**Bulgarian Banks table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| UniCredit Bulbank | ПРЕВОД, ПЛАЩАНЕ, ТАКСА, КАРТА | PDF/CSV; Cyrillic descriptions; date DD.MM.YYYY |
| DSK Bank | ПРЕВОД, ДИРЕКТЕН ДЕБИТ, ТАКСА | PDF/CSV; counterparty in narrative |
| United Bulgarian Bank (UBB / OBB) | ПРЕВОД, КАРТОВО ПЛАЩАНЕ, ТАКСА | PDF; CSV export available |
| Postbank (Eurobank Bulgaria) | ПРЕВОД, ПЛАЩАНЕ, ЛИХВА | PDF/CSV |
| Revolut / Wise (Business) | PAYMENT, TRANSFER, CARD PAYMENT, FEE | CSV; multi-currency -- watch EUR/BGN; clean Latin names |

## Section 4 -- Worked Examples

All BGN figures apply through 31 Dec 2025; EUR equivalents (1 EUR = 1.95583 BGN) apply from 1 Jan 2026 (PwC, *Other taxes*; BTA).

### Example 1 -- Freelancer client payment (income)

**Input line:**
`15.03.2025 ; UNICREDIT ПРЕВОД ; STUDIO KREBS EOOD ; ХОНОРАР ФАКТУРА 2025-003 ; +9,600.00 ; BGN`

**Reasoning:**
Freelancer professional fee, not VAT-registered. Full BGN 9,600 is gross business income. The 25% normative deduction is applied later at the annual computation, NOT line by line (PwC, *Deductions*).

**Classification:** Gross business income = BGN 9,600.

### Example 2 -- Annual freelancer computation (Art. 50 return, 10% PIT)

**Inputs:** General freelancer (25% normative deduction), gross annual income BGN 48,000. Self-insured, declares insurable income of BGN 2,000/month (within the BGN 1,077--4,130 Apr--Dec band), with maternity coverage opted in (31.3%).

**Reasoning (PwC, *Deductions* / *Taxes on personal income* / *Other taxes*; Ruskov & Kollegen):**
- Normative deduction 25% = BGN 48,000 x 25% = **BGN 12,000**
- Income after normative deduction = 48,000 - 12,000 = **BGN 36,000**
- Annual insurable base = 2,000 x 12 = BGN 24,000; contributions 31.3% = **BGN 7,512**
- Contributions are deductible from the PIT base: 36,000 - 7,512 = **BGN 28,488** (PIT base)
- PIT at flat 10% = 28,488 x 10% = **BGN 2,848.80**

**If BGN 2,700 advance PIT was paid quarterly:** balance due = 2,848.80 - 2,700 = **BGN 148.80**.

**Classification:** PIT base BGN 28,488; PIT due BGN 2,848.80; balance BGN 148.80.

### Example 3 -- Sole trader (ET) at 15%

**Inputs:** Sole trader (ET), taxable profit under the CIT-Act base (income minus actual expenses plus adjustments) = BGN 50,000.

**Reasoning (PwC, *Income determination*):**
ET profit is taxed at **15%**, NOT 10%, and uses actual expenses (not normative deductions). 50,000 x 15% = **BGN 7,500**.

**Classification:** ET tax = BGN 7,500. Filed/paid 1 March -- 30 June.

### Example 4 -- Dividend (5% final withholding)

**Input line:**
`30.06.2025 ; DSK ПРЕВОД ; ALPHA TECH OOD ; ДИВИДЕНТ ; +20,000.00 ; BGN (net after WHT)`

**Reasoning (PwC, *Income determination*):**
Dividends carry a **5% final withholding tax**. On gross BGN 20,000 the WHT is BGN 1,000 and net received is BGN 19,000. Because the tax is final, the dividend is **EXCLUDED** from the 10% taxable base -- do not tax it again.

**Classification:** 5% WHT = BGN 1,000 (final). Exclude from the 10% annual base.

### Example 5 -- Employee monthly payroll (10% PIT on net base)

**Inputs:** Employee (Category III, born after 1959), gross monthly remuneration BGN 3,000 (within the BGN 1,077--4,130 Apr--Dec insurable band). Employee contribution rate **13.78%** (PwC, *Other taxes*; Ministry of Economy).

**Reasoning (PwC, *Other taxes*; Ministry of Economy):**
The monthly PIT base = gross pay minus mandatory EMPLOYEE social-security and health contributions; the 10% is then applied and withheld by the employer:
- Employee contributions = 3,000 x 13.78% = **BGN 413.40**
- Monthly PIT base = 3,000 - 413.40 = **BGN 2,586.60**
- PIT at 10% = **BGN 258.66**
- Net pay = 3,000 - 413.40 - 258.66 = **BGN 2,327.94**

**Classification:** Monthly PIT withheld BGN 258.66; reconciled by the employer by 31 January. (Employer-side cost adds employer contributions of 18.92%--19.62% per the Section 1 table.)

### Example 6 -- Child tax relief (2 children)

**Inputs:** Individual with 2 dependent children, annual taxable base before relief BGN 30,000.

**Reasoning (PwC, *Deductions*):**
Child relief for two children reduces the annual taxable base by **BGN 12,000**. New base = 30,000 - 12,000 = BGN 18,000. Tax saving = 12,000 x 10% = **BGN 1,200**. (One child = BGN 6,000 reduction; three+ = BGN 18,000; disabled child = BGN 12,000.)

**Classification:** Reduced base BGN 18,000; tax saving BGN 1,200.

### Example 7 -- Internal transfer (exclude)

**Input line:**
`12.05.2025 ; UBB ПРЕВОД ; OWN ACCOUNT - СПЕСТЯВАНИЯ ; ; -5,000.00 ; BGN`

**Reasoning:** Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Flat-Rate Principle

- **Flat-rate principle** — Bulgaria applies a single flat **10%** PIT to virtually all individual income (employment, freelance/other self-employment, rental, capital gains, other), with **no progressive bands and no tax-free allowance** (PwC, *Taxes on personal income*). The two exceptions are sole traders (ET) at **15%** and dividends at **5%** final withholding (PwC, *Income determination*).  _(Personal Income Taxes Act (ZDDFL))_

### 5.2 Normative Expense Deductions (non-ET individuals)

**Normative Expense Deductions table (5.2)**  _(ZDDFL (PwC, *Deductions*))_

| Activity | Normative deduction |
| --- | --- |
| General freelance / self-employment | 25% |
| Liberal professions, royalties / copyright | 40% |
| Rental income (immovable property) | 10% |
| Registered agricultural producers | 60% |

- **Deduction application** — Freelancers and self-employed individuals (non-ET) deduct a STATUTORY normative percentage from gross income BEFORE the 10% PIT -- they do not itemise receipts.  _(ZDDFL (PwC, *Deductions*))_

### 5.3 Sole Trader (ET) Base

- **Sole trader ET base** — Sole traders compute taxable profit under the CIT-Act base (income minus ACTUAL expenses plus tax adjustments) and pay **15%**. They do NOT use normative deductions and file/pay 1 March -- 30 June.  _(ZDDFL referring to the Corporate Income Tax Act (ZKPO) (PwC, *Income determination*))_

### 5.4 Contributions Reduce the PIT Base

- **Contributions reduce PIT base** — For employees, the monthly PIT base = gross pay minus mandatory EMPLOYEE social-security and health contributions, and the 10% is withheld monthly with an annual reconciliation by 31 January (Ministry of Economy). For self-insured persons, contributions actually paid are deductible from the annual PIT base.  _(ZDDFL; Social Insurance Code (KSO); Health Insurance Act (ZZO))_

### 5.5 Insurable-Income Bands

**Insurable-Income Bands table**  _(Public Social Insurance Budget Act; KSO)_

| Band (2025) | 1 Jan -- 31 Mar | 1 Apr -- 31 Dec | Source |
| --- | --- | --- | --- |
| Minimum monthly insurable income (employees) | BGN 933 (EUR 477.04) | BGN 1,077 (EUR 550.66) | Eurofast |
| Maximum monthly insurable income (cap) | BGN 3,750 (EUR 1,917.34) | BGN 4,130 (EUR 2,111.64) | PwC, *Other taxes* |
| Self-employed minimum base | -- | BGN 1,077 (EUR 550.66) | PwC, *Other taxes* |
| Self-employed maximum base | -- | BGN 4,130 (EUR 2,111.64) | PwC, *Other taxes* |

- **2026 insurable-income figures** — maximum monthly insurable income EUR 2,111.64; self-employed minimum EUR 550.66  _(PwC, *Other taxes*)_

### 5.6 Dividends

- **Dividend final withholding treatment** — Dividends and liquidation proceeds (Bulgarian and foreign payers) carry a **5% FINAL** withholding tax. Once withheld, they are excluded from the 10% annual base -- no double taxation.  _(ZDDFL (PwC, *Income determination*))_

### 5.7 Child Tax Relief

- **Child tax relief amounts** — The annual taxable base is reduced by: **BGN 6,000 / EUR 3,067.75** (one child), **BGN 12,000 / EUR 6,135.50** (two), **BGN 18,000 / EUR 9,203.25** (three or more), and **BGN 12,000 / EUR 6,135.50** for a disabled child (PwC, *Deductions*; EUR at 1 EUR = 1.95583 BGN). Only one parent may claim; usable monthly in advance via the employer or through the annual/quarterly return.  _(ZDDFL (PwC, *Deductions*))_

### 5.8 Filing and Payment

**Filing and Payment table**  _(ZDDFL (PwC, *Tax administration*))_

| Item | Detail |
| --- | --- |
| Annual return (Art. 50, form 2001) -- individuals | Due 30 April of the following year (2025 return due 30 April 2026) |
| Annual return -- sole traders (ET) | File/pay 1 March -- 30 June of the following year |
| Quarterly advance PIT (freelance/rental/other) | By end of the month following each of Q1--Q3; **no Q4 advance for individuals** |
| Corrective return | One penalty-free corrective return by 30 September of the following year |
| Early-filing discount | 5% off tax due, **capped at BGN 500 / EUR 255.65**, if filed electronically and paid by 31 March with no outstanding public liabilities |
| Employees -- single Bulgarian employer | Not required to file an annual return if fully taxed via monthly withholding and reconciled by the employer by 31 January |

### 5.9 VAT Interaction

**VAT Interaction table**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT registration threshold | Turnover above **BGN 100,000 (EUR 51,130)** over the relevant/previous calendar year (PwC, *Income determination*) |
| VAT collected on sales (registered) | NOT income -- exclude from the gross base |
| Input VAT recovered (registered) | NOT an expense (ET) -- exclude |
| Not VAT-registered | Gross (VAT-inclusive) amount is the cost/income |

### 5.10 Non-Deductible / Excluded Items

**Non-Deductible / Excluded Items table**

| Item | Reason |
| --- | --- |
| Income tax itself | Tax on income |
| Fines and penalties | Public policy |
| Personal living expenses | Not business-related |
| Drawings / personal withdrawals | Not an expense |
| Dividends already taxed at 5% | Final tax -- exclude from 10% base |
| VAT liability payments | Not an expense |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Correct Normative-Deduction Percentage

- **Normative deduction percentages by activity** — 25% (general), 40% (liberal professions / royalties), 60% (registered agricultural producers), 10% (rental) -- the activity classification drives a materially different result (PwC, *Deductions*). **Conservative default:** 25% (general self-employment) until activity confirmed. **Flag for reviewer:** Confirm the activity matches the claimed deduction percentage.  _(PwC, *Deductions*)_

### 6.2 Self-Insured Maternity-Coverage Election

- **Maternity coverage election** — Opting into the General Sickness & Maternity fund adds 3.5% (27.8% -> 31.3% per the component arithmetic in Section 1). **Conservative default:** Maternity NOT elected (27.8%). **Flag for reviewer:** Confirm the election and the correct self-insured total (see Section 1 caveat).

### 6.3 Birth Year and Pension Allocation

- **Birth year pension allocation** — Persons born before 1960 pay the full pension contribution to the state fund; those born after 1959 redirect 5% to the 2nd-pillar universal fund. The TOTAL is unchanged, but allocation differs (Ministry of Economy). **Conservative default:** Born after 1959 (universal fund applies).  _(Ministry of Economy)_

### 6.4 Declared Insurable Income (self-insured)

- **Declared insurable income reconciliation** — Self-insured persons declare an insurable income within the min/max band; the year-end reconciliation against actual income can create an additional contribution liability (Ruskov & Kollegen). **Flag for reviewer:** Confirm the declared base and the annual reconciliation.  _(Ruskov & Kollegen)_

### 6.5 Sole Trader (ET) Expense Substantiation

- **ET expense substantiation** — ET actual-expense deductions under the CIT-Act base require valid documentation and adjustment for non-deductible items. **Flag for reviewer:** Confirm expense substantiation and CIT-Act adjustments.

### 6.6 Employer Accident-Fund Risk Class

- **Employer accident fund risk class** — The accident fund (0.4%--1.1%) is employer-only and varies by economic-activity risk class, moving the employer total within the published band. **Flag for reviewer:** Confirm the employer's risk class before finalising employer cost (see Section 1 caveat).

### 6.7 Residency Determination

- **Residency determination rule** — Resident (permanent address with centre of vital interests, OR >183 days in any 12-month period) = worldwide income; non-resident = Bulgarian-source only (PwC, *Taxes on personal income*). **Flag for reviewer:** Confirm residency where presence is borderline.  _(PwC, *Taxes on personal income*)_

## Section 7 -- Excel Working Paper Template

```
BULGARIA INCOME TAX -- ANNUAL COMPUTATION WORKING PAPER
Tax Year: 2025  (BGN; EUR from 1 Jan 2026 at 1 EUR = 1.95583 BGN)
Client: ___________________________
Category: Individual/Freelancer (10%)  /  Sole trader ET (15%)
Residency: Resident / Non-resident
Self-insured: Yes / No   Maternity opted in: Yes / No   Born after 1959: Yes / No

A. GROSS INCOME (non-ET individuals)
  A1. Freelance / self-employment income          ___________
  A2. Rental income                                ___________
  A3. Other income (excl. dividends taxed at 5%)   ___________
  A4. TOTAL gross income                           ___________

B. NORMATIVE EXPENSE DEDUCTION
  B1. Activity %: 25 / 40 / 60 (rental 10)         ___________
  B2. Deduction (A4 x B1, by activity)             ___________
  B3. Income after normative deduction (A4 - B2)   ___________

C. CONTRIBUTIONS (deductible from base)
  C1. Social-security contributions paid           ___________
  C2. Health contributions paid                     ___________
  C3. TOTAL contributions (C1 + C2)                ___________

D. RELIEFS
  D1. Child relief (6,000 / 12,000 / 18,000)       ___________
  D2. Other statutory reliefs                       ___________

E. TAXABLE BASE (B3 - C3 - D1 - D2)               ___________

F. TAX COMPUTATION (pass to deterministic engine)
  F1. PIT at 10% (individuals) on E               ___________
      -- OR ET profit (CIT-Act base) x 15%        ___________
  F2. Less: advance PIT paid (Q1-Q3)              ___________
  F3. Less: early-filing 5% discount (cap 500)    ___________
  F4. Tax due / refund                             ___________

G. DIVIDENDS (separate -- 5% final WHT)
  G1. Gross dividends                              ___________
  G2. 5% WHT (final -- excluded from F)            ___________

REVIEWER FLAGS:
  [ ] Category confirmed (individual 10% vs ET 15%)?
  [ ] Correct normative-deduction % confirmed?
  [ ] Residency confirmed?
  [ ] Self-insured rate / maternity election confirmed?
  [ ] Declared insurable base + annual reconciliation confirmed?
  [ ] Employer accident-fund risk class confirmed (payroll)?
  [ ] Dividends excluded from 10% base?
  [ ] Income tax / fines / drawings excluded?
  [ ] Section 1 contribution-rate caveat reviewed?
```

## Section 8 -- Bank Statement Reading Guide

### Bulgarian Bank Statement Formats

**Bulgarian Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| UniCredit Bulbank | PDF, CSV | Дата, Описание, Дебит, Кредит, Салдо | Most common; Cyrillic; DD.MM.YYYY |
| DSK Bank | PDF, CSV | Дата, Основание, Сума, Салдо | Counterparty in narrative |
| United Bulgarian Bank (UBB/OBB) | PDF, CSV | Date, Description, Amount, Balance | CSV export available |
| Postbank (Eurobank) | PDF, CSV | Дата, Описание, Сума |  |
| Revolut / Wise Business | CSV | Date, Counterparty, Amount, Currency, Reference | Multi-currency; watch EUR/BGN |

### Key Bulgarian Banking / Tax Terms

**Key Bulgarian Banking / Tax Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| ПРЕВОД (prevod) | Transfer | Check direction for income/expense |
| ПЛАЩАНЕ (plashtane) | Payment | Expense or income -- check counterparty |
| ХОНОРАР (honorar) | Professional fee | Freelance income |
| ЗАПЛАТА (zaplata) | Salary | Employment income (separate base) |
| НАЕМ (naem) | Rent | Income (10% deduction) or expense |
| ЛИХВА (lihva) | Interest | Interest income or bank charge |
| ДИВИДЕНТ (divident) | Dividend | 5% final WHT -- exclude from 10% base |
| ОСИГУРОВКИ (osigurovki) | Social-security contributions | Deductible from PIT base |
| ЗДРАВНА ВНОСКА (zdravna vnoska) | Health contribution | Deductible from PIT base |
| ТАКСА (taksa) | Fee / charge | Bank charge (ET deductible) |
| КАРТА (karta) | Card payment | Expense -- check merchant |
| ГЛОБА (globa) | Fine | NOT deductible |
| ДДС (DDS) | VAT | Exclude -- VAT liability |
| АВАНСОВ ДАНЪК (avansov danak) | Advance tax | Credit against liability |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- BULGARIA INCOME TAX
1. Category: individual/freelancer (10%) or sole trader / ET (15%)?
2. Residency: resident in Bulgaria, or non-resident?
3. Freelancer activity type (for the normative deduction %): general (25%),
   liberal profession/royalties (40%), agricultural producer (60%), rental (10%)?
4. Are you registered as a self-insured person? If yes, what monthly insurable
   income do you declare, and have you opted into maternity coverage (3.5%)?
5. Were you born before 1960 or after 1959?
6. VAT registered? (turnover over BGN 100,000 / EUR 51,130?)
7. Social-security and health contributions actually paid during the year?
8. Quarterly advance PIT paid (Q1-Q3)?
9. Dependent children (for child relief)?
10. Any dividends received (taxed separately at 5%)?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References table**

| Topic | Reference | Source |
| --- | --- | --- |
| Flat 10% PIT; residency | Personal Income Taxes Act (ZDDFL) | PwC, *Taxes on personal income* |
| Sole trader (ET) 15% base | ZDDFL + Corporate Income Tax Act (ZKPO) | PwC, *Income determination* |
| Dividends 5% final WHT | ZDDFL | PwC, *Income determination* |
| Normative deductions; child relief | ZDDFL | PwC, *Deductions* |
| Social security / health contributions | Social Insurance Code (KSO); Health Insurance Act (ZZO) | Ministry of Economy; PwC, *Other taxes* |
| Insurable-income bands | Public Social Insurance Budget Act | PwC, *Other taxes*; Eurofast |
| Filing, advance PIT, deadlines, early-filing discount | ZDDFL | PwC, *Tax administration* |
| Penalties / late-payment interest | ZDDFL; Ministry of Finance | Ministry of Finance; Orbitax |
| Euro changeover (1 Jan 2026, 1 EUR = 1.95583 BGN) | Euro accession measures | PwC, *Other taxes*; BTA |

### Penalties

**Penalties table**

| Type | Amount | Source |
| --- | --- | --- |
| Non-submission / late filing of annual PIT return | Fine up to **BGN 500 / EUR 255.65**; doubled on repeat (up to BGN 1,000) | Ministry of Finance |
| Late-payment interest (2025) | **BNB base rate + 10 pp p.a.** (approx. 11.81% p.a. at end-2025) | Orbitax |
| Late-payment interest (from 1 Jan 2026) | **ECB main refinancing rate + 8 pp p.a.** (replaces the BNB+10 formula; Council of Ministers decree of 23 Dec 2025) | Penkov, Markov & Partners |

### 2026 Confirmed Changes

**2026 Confirmed Changes table**

| Change | Detail | Source |
| --- | --- | --- |
| Euro adoption | From 1 Jan 2026, EUR replaces BGN at 1 EUR = 1.95583 BGN | PwC, *Other taxes*; BTA |
| Minimum wage 2026 | BGN 1,213 / **EUR 620.20** per month; minimum hourly EUR 3.74 (~12.6% increase) | BTA |
| Maximum insurable income 2026 | EUR 2,111.64/month | PwC, *Other taxes* |
| Self-employed minimum base 2026 | EUR 550.66/month | PwC, *Other taxes* |
| Late-payment interest formula | ECB rate + 8 pp (replaces BNB + 10 pp) | Penkov, Markov & Partners |

> **[RESEARCH GAP -- reviewer to confirm]** NRA/NSSI primary-source pages (nra.bg, nssi.bg) were not directly fetched; figures rely on PwC Worldwide Tax Summaries and official Ministry of Economy/Finance pages (authoritative and mutually consistent). The exact 2026 insurable-income bands beyond those published in EUR should be re-verified against the finalised 2026 Public Social Insurance Budget Act. Late-payment interest fluctuates with the BNB/ECB base rate each half-year.

### Test Suite

**Test 1 -- General freelancer, full computation.**
Input: General freelancer (25% deduction), gross BGN 48,000; self-insured base BGN 2,000/mo with maternity (31.3%); advance PIT BGN 2,700 paid.
Expected: Normative deduction BGN 12,000; after deduction BGN 36,000; contributions (24,000 x 31.3%) BGN 7,512; PIT base BGN 28,488; PIT BGN 2,848.80; balance due BGN 148.80.

**Test 2 -- Sole trader (ET) at 15%.**
Input: ET, CIT-Act taxable profit BGN 50,000.
Expected: Tax = BGN 7,500 (15%). Files/pays 1 March -- 30 June.

**Test 3 -- Dividend, 5% final WHT.**
Input: Gross dividend BGN 20,000.
Expected: WHT BGN 1,000 (final); net BGN 19,000; EXCLUDE from the 10% base.

**Test 4 -- Employee monthly PIT.**
Input: Gross BGN 3,000/mo; employee contributions 13.78% (Category III, born after 1959).
Expected: Contributions BGN 413.40; PIT base BGN 2,586.60; PIT BGN 258.66; net BGN 2,327.94.

**Test 5 -- Child relief (2 children).**
Input: Base before relief BGN 30,000; 2 children.
Expected: Reduce base by BGN 12,000 -> base BGN 18,000; tax saving BGN 1,200.

**Test 6 -- Liberal profession deduction.**
Input: Royalty income BGN 40,000, liberal-profession activity (40% deduction).
Expected: Deduction BGN 16,000; income after deduction BGN 24,000 (then less contributions before 10%).

**Test 7 -- Early-filing discount.**
Input: PIT due BGN 4,000; filed electronically and paid by 31 March, no arrears.
Expected: 5% discount = BGN 200 (below the BGN 500 cap); pay BGN 3,800.

## PROHIBITIONS

- **ET taxation rate** — NEVER apply the 10% rate to a sole trader (ET) -- ET profit is taxed at 15% on a CIT-Act base
- **Freelancer expense deduction method** — NEVER itemise individual expenses for a non-ET freelancer -- use the statutory normative deduction (25%/40%/60%/10%)
- **Dividend taxation** — NEVER tax a dividend at 10% -- it carries a 5% FINAL withholding tax and is excluded from the 10% base
- **Insurable income contribution band** — NEVER apply contributions outside the statutory min/max insurable-income band
- **Non-deductible items** — NEVER allow income tax itself, fines, or drawings as a deduction
- **No tax-free allowance** — NEVER assume a tax-free allowance band -- Bulgaria has none; the flat 10% applies from the first lev
- **2nd-pillar Universal Pension Fund inclusion** — NEVER omit the 5% 2nd-pillar Universal Pension Fund from the employee/employer contribution totals (born after 1959) -- the reconciled rates are employee 13.78%, employer 18.92%--19.62%, self-insured 27.8% (31.3% with optional maternity); the precise per-fund split remains a Section 1 [RESEARCH GAP] for the reviewer
- **Currency handling** — NEVER mix BGN and EUR figures -- BGN through 31 Dec 2025, EUR from 1 Jan 2026 at 1 EUR = 1.95583 BGN
- **Calculation presentation** — NEVER present tax calculations as definitive -- always label as estimated and pass to the deterministic engine / reviewer

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
