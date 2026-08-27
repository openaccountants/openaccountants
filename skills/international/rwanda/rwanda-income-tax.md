---
name: rwanda-income-tax
description: Use this skill whenever asked about Rwanda income tax (PIT / PAYE) for employees and self-employed individuals. Trigger on phrases like "how much tax do I pay in Rwanda", "PAYE", "RRA", "income tax declaration", "monthly PAYE return", "casual labourer tax", "flat tax micro-enterprise", "lump-sum tax", "real regime", "RSSB pension", "CBHI / Mutuelle", "benefits in kind", "self-employed tax Rwanda", or any question about filing or computing income tax for an individual taxpayer in Rwanda. Also trigger when preparing or reviewing a PAYE computation, an annual PIT declaration, deciding between micro-enterprise / lump-sum / real regimes, or advising on RSSB social-security contributions. This skill covers PAYE brackets (resident and non-resident), casual-labour rate, micro/lump-sum/real turnover regimes, RSSB pension / occupational hazard / maternity / CBHI / medical contributions, benefits in kind, filing deadlines, and penalties. ALWAYS read this skill before touching any Rwanda income tax work.
version: 0.1
jurisdiction: RW
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rwanda Income Tax -- PAYE & Self-Employed

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Rwanda (Republic of Rwanda) |
| Tax | Personal Income Tax (PIT) / PAYE |
| Currency | Rwandan franc (RWF / FRW) only |
| Tax year | Calendar year (1 January -- 31 December) [PwC, individual] |
| Primary legislation | Law N° 027/2022 of 20/10/2022 establishing taxes on income, as amended (2023) |
| Supporting framework | Tax Procedures Law (penalties, deadlines); Presidential Order N° 086/01 (pension, gazetted 13 Dec 2024) |
| Tax authority | Rwanda Revenue Authority (RRA) |
| Social-security authority | Rwanda Social Security Board (RSSB) |
| Filing portal | RRA e-Tax / domestic taxes portal |
| Annual PIT declaration deadline | 31 March of the following year [RRA notice; PwC, tax-administration] |
| PAYE remittance + return deadline | 15th of the following month [PwC, tax-administration] |
| Validated by | Pending — requires sign-off by a Rwanda-licensed tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

### PAYE / PIT Rate Brackets — Monthly (2023 onward, permanent schedule)

**PAYE / PIT Rate Brackets — Monthly**  _([RRA PIT page; PwC, individual])_

| Monthly taxable income (RWF) | Rate | Cumulative tax at top of band (RWF) |
| --- | --- | --- |
| 0 -- 60,000 | 0% | 0 |
| 60,001 -- 100,000 | 10% | 4,000 |
| 100,001 -- 200,000 | 20% | 24,000 |
| 200,001+ | 30% | -- |

**Same rates apply to residents and non-residents.** [RRA PIT page; PwC, individual]

*Cumulative check: 60k–100k = 40,000 × 10% = 4,000. 100k–200k = 100,000 × 20% = 20,000; cumulative 24,000.* [RRA new-rates guide]

### PAYE / PIT Rate Brackets — Annual equivalent

**PAYE / PIT Rate Brackets — Annual equivalent**  _([RRA PIT page])_

| Annual taxable income (RWF) | Rate | Cumulative tax at top of band (RWF) |
| --- | --- | --- |
| 0 -- 720,000 | 0% | 0 |
| 720,001 -- 1,200,000 | 10% | 48,000 |
| 1,200,001 -- 2,400,000 | 20% | 288,000 |
| 2,400,001+ | 30% | -- |

- **Monthly PAYE calculation** — Monthly PAYE = annual tax ÷ 12, rounded up.  _([RRA new-rates guide])_

*Cumulative check: 720k–1.2M = 480,000 × 10% = 48,000. 1.2M–2.4M = 1,200,000 × 20% = 240,000; cumulative 288,000. Annual bands = monthly bands × 12 (60k/100k/200k → 720k/1.2M/2.4M).* [RRA PIT page]

> **Superseded schedule warning.** A transitional "Year 1" schedule (0% / 20% / 30%, with the 720k–1.2M band taxed at 20%) existed under Law N° 027/2022 but has been **superseded**. The current correct middle-band rate is **10%**, not 20%. [RRA new-rates guide]

### Special-Category Income Rates

**Special-Category Income Rates**

| Category | Rate | Notes |
| --- | --- | --- |
| Casual labourer | 15% flat, first RWF 60,000/month at 0% | [RRA new-rates guide; Law N° 027/2022] |
| Non-resident (Rwanda-source income) | Same bracket rates as residents | Taxed only on Rwanda-source income [PwC, individual] |
| Capital gains on shares | 10% | [PwC, individual] |
| Corporate Income Tax (if operating via a company) | 28% | Reduced from 30% by the 2022 law [PwC, corporate] |

### Self-Employed Turnover Regimes

**Self-Employed Turnover Regimes**

| Annual turnover (RWF) | Regime | Tax |
| --- | --- | --- |
| < 2,000,000 | Exempt from registration | No income tax registration required [RRA register page] |
| 2,000,001 -- 12,000,000 | Micro-enterprise flat tax | Fixed annual amount (table in §5.7) [PwC, corporate] |
| 12,000,001 -- 20,000,000 | Small-business lump-sum | 3% of annual turnover [PwC, corporate] |
| > 20,000,000 (or by election) | Real regime (actual taxation) | Progressive PIT on net profit; election irrevocable for 3 years [PwC, corporate] |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residence status | Treat as **resident** worldwide-income basis only if confirmed; otherwise STOP and ask |
| Unknown employment vs self-employment | STOP — PAYE and turnover regimes differ fundamentally |
| Unknown turnover band (self-employed) | Use the band the documented turnover falls into; if turnover unknown, STOP |
| Unknown benefit-in-kind value | Apply statutory valuation (housing 20%, vehicle 10% of employment income) [PwC, sample calc] |
| Unknown business-use % (mixed expense, real regime) | 0% deduction |
| Unknown expense category (real regime) | Not deductible |
| Unknown casual vs regular employment | Treat as regular employee (progressive brackets) unless casual status confirmed |
| Minimum-wage floor | **[RESEARCH GAP — reviewer to confirm]** — no enforceable national statutory minimum wage exists; do not assume one |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — for an **employee**: monthly gross salary breakdown (basic + housing + transport + other allowances) and confirmation of resident/non-resident status. For a **self-employed individual**: bank statement for the full tax year (CSV, PDF, or pasted text) plus confirmation of annual turnover and chosen/eligible regime.

**Recommended** — payslips, RSSB contribution records, benefits-in-kind details (housing, vehicle), prior-year PIT declaration or RRA assessment, sales/purchase records (self-employed).

**Ideal** — complete income and expenditure account (real regime), asset register, RSSB statements for all schemes, casual-labour registers, KIFC expert status documentation (if applicable).

**Refusal if minimum is missing — SOFT WARN.** No salary breakdown or no bank statement at all = hard stop. Salary stated as a single gross figure with no allowance split = proceed with reviewer warning: "Benefit-in-kind and RSSB contribution bases depend on the allowance split (housing/transport). This computation assumed [stated assumption]. The reviewer must confirm the allowance breakdown."

### Refusal Catalogue

- **R-RW-1 — Residence status unknown** — "Residence status affects the scope of taxable income (worldwide for residents vs Rwanda-source only for non-residents). This skill cannot compute tax without it. Please confirm before proceeding."  _([PwC, individual])_
- **R-RW-2 — Companies, partnerships, group structures** — "This skill covers individual taxpayers (employees and sole-trader / turnover-regime self-employed). Companies file Corporate Income Tax (28%) separately. Escalate to a Rwanda-licensed practitioner."  _([PwC, corporate])_
- **R-RW-3 — KIFC expert exemption** — "New residents (not resident in the prior 5 years) working as experts for Kigali International Financial Centre (KIFC)-licensed entities may be exempt from PIT on foreign-source income for their first 5 years. This requires specialist confirmation of eligibility. Escalate."  _([PwC; RRA])_
- **R-RW-4 — Capital gains / share disposals** — "Capital gains on shares are taxed at 10% under separate rules. Out of scope for this PAYE/PIT skill. Escalate."  _([PwC, individual])_
- **R-RW-5 — Arrears / RRA enforcement** — "Client has outstanding tax arrears or is subject to RRA enforcement. Administrative fines reach 60% of tax due and late-payment interest accrues monthly (capped at 100% of the tax). Do not advise. Escalate immediately."  _([RRA penalties notice])_
- **R-RW-6 — VAT return requested** — "This skill covers income tax (PIT/PAYE) only. Rwanda VAT is standard-rated at 18% with a registration threshold of RWF 20,000,000/year (or RWF 5,000,000/quarter). Use a dedicated VAT skill."  _([PwC, corporate])_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5. Patterns appear in English, Kinyarwanda, and French because Rwandan bank statements use all three.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MUSHAHARA, SALARY, SALAIRE, PAYE NET, EMPLOYER [name] | Employment income | PAYE should already be withheld at source by employer |
| Client name + TRANSFER, DEPOSIT, KWISHYURA, PAIEMENT | Business income (self-employed) | Turnover for regime test; if VAT-registered, extract net (excl. 18% VAT) |
| FEES, HONORARIES, HONORAIRES, CONSULTANCY, AMAFARANGA Y'AKAZI | Business income | Professional fees |
| MOMO PAYOUT, MTN MOMO, AIRTEL MONEY (business inflow) | Business income | Mobile-money inflow — match to invoices |
| STRIPE / PAYPAL / WISE / UPWORK / FIVERR PAYOUT | Business income | Platform payout — net of platform commission |
| RENT RECEIVED, UBUKODE, LOYER | Rental income | Separate income stream — not turnover for the trading regimes |
| INTEREST, INYUNGU, INTÉRÊTS | Investment income | May be subject to withholding tax |
| DIVIDEND, IMIGABANE, DIVIDENDE | Investment income | Subject to withholding tax |
| RRA REFUND, TAX REFUND | EXCLUDE | Refund of prior tax |
| AGRICULTURE, LIVESTOCK, UBUHINZI, UBWOROZI proceeds | Business income — but see exemption | Agriculture/livestock income exempt up to RWF 12,000,000/period; only excess taxed [RRA register page; PwC] |

### 3.2 Expense Patterns (Debits) — Deductible under the Real Regime Only

**3.2 Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, UBUKODE BW'IBIRO, LOYER BUREAU | Office rent | Deductible (real regime) | Dedicated business premises |
| ACCOUNTANT, AUDITOR, IBARURAMARI | Accountancy fees | Deductible |  |
| LAWYER, AVOCAT, LEGAL | Legal fees | Deductible | Must be business-related |
| OFFICE SUPPLIES, IBIKORESHO BY'IBIRO | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| BANK FEE, AMAFARANGA YA BANKI, FRAIS BANCAIRES | Bank charges | Deductible | Business account only |
| MOMO FEE, MTN/AIRTEL TRANSACTION FEE | Mobile-money fees | Deductible | Business transactions |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE, ZOOM | Software subscription | Deductible | Recurring operating expense |

> Deductions are only relevant under the **real regime**. Micro-enterprise (flat) and lump-sum taxpayers pay on turnover and CANNOT deduct expenses.

### 3.3 Expense Patterns (Debits) — Utilities (Real Regime, may need apportionment)

**3.3 Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| REG (Rwanda Energy Group), EUCL, ELECTRICITY, AMASHANYARAZI | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| WASAC, WATER, AMAZI | Water | T2 if home office |  |
| MTN, AIRTEL, INTERNET, CANALBOX | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |

### 3.4 Expense Patterns (Debits) — Travel (Real Regime)

**3.4 Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RWANDAIR, FLIGHT, INDEGE | Flights | Deductible if business travel | Must be wholly business |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| YEGO MOVES, BOLT, TAXI, MOTO | Local transport | Deductible if business purpose |  |
| FUEL, LISANSI, CARBURANT, SP / ENGEN / KOBIL | Vehicle fuel | T2 — business % only | Requires mileage log |

### 3.5 Expense Patterns (Debits) — NOT Deductible

**3.5 NOT Deductible table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RESTAURANT, ENTERTAINMENT, CLIENT MEAL | NOT deductible | Private/entertainment cost |
| GROCERIES, SUPERMARKET, SIMBA, NAKUMATT, PERSONAL | NOT deductible | Private living costs |
| FINE, PENALTY, IHAZABU, AMENDE | NOT deductible | Public policy |
| RRA PAYMENT, INCOME TAX, PAYE PAYMENT | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | NOT deductible | Not an expense |

### 3.6 RSSB and Statutory Deductions (Special Handling)

**3.6 RSSB and Statutory Deductions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RSSB PENSION, PENSIYO | Statutory contribution | Employee 6% / Employer 6% (see §3.x and Section 1) [EY; PwC, other-taxes] |
| RSSB OCCUPATIONAL, OCCUPATIONAL HAZARD | Statutory contribution | Employer 2% only [PwC, other-taxes] |
| RSSB MATERNITY | Statutory contribution | Employee 0.3% / Employer 0.3% [PwC, other-taxes] |
| RSSB MEDICAL, RAMA | Statutory contribution | Employer 7.5% / Employee 7.5% of basic salary (public sector / opt-in) [RRA medical notice] |
| CBHI, MUTUELLE, MUTUELLE DE SANTÉ | Statutory contribution | Employee 0.5% of net salary [PwC, other-taxes] |

### 3.7 Exclusions (Neither Income nor Expense)

**3.7 Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, INGUZANYO, PRÊT | EXCLUDE | Loan principal movement |
| VAT PAYMENT, RRA VAT | EXCLUDE | VAT liability payment, not expense |

### 3.8 Rwandan Banks / Channels — Statement Format Reference

**3.8 Rwandan Banks / Channels table**

| Channel | Common Patterns | Notes |
| --- | --- | --- |
| Bank of Kigali (BK) | TRANSFER, RTGS, CHARGES, MUSHAHARA | PDF/CSV; date format DD/MM/YYYY |
| I&M Bank Rwanda | PAYMENT, TRF, FEE | PDF/CSV; counterparty in description field |
| Equity Bank Rwanda | TRANSFER, DEBIT, CHARGE | PDF |
| MTN MoMo / Airtel Money | MOMO PAYMENT, CASH IN, CASH OUT, FEE | CSV/SMS export; very common for micro-enterprises |
| BPR / Cogebanque | TRANSFER, VIREMENT, FRAIS | PDF; French terms common |

## Section 4 -- Worked Examples

### Example 1 — Monthly PAYE, regular resident employee

**Input line:**
`28/02/2025 ; BK SALARY CREDIT ; EMPLOYER KIGALI TECH LTD ; MUSHAHARA FEB ; +XXX ; RWF`
Stated: monthly taxable employment income = **RWF 350,000** (resident, regular employee).

**Reasoning (monthly brackets):**
- 0 – 60,000 @ 0% = 0
- 60,001 – 100,000: 40,000 × 10% = 4,000
- 100,001 – 200,000: 100,000 × 20% = 20,000
- 200,001 – 350,000: 150,000 × 30% = 45,000
- **Total monthly PAYE = 0 + 4,000 + 20,000 + 45,000 = RWF 69,000** [RRA PIT page]

**Classification:** PAYE withheld = RWF 69,000. Net of tax (before RSSB) = 350,000 − 69,000 = RWF 281,000.

### Example 2 — Annual PIT, self-employed real regime

**Input:** Resident sole trader, **annual net taxable profit = RWF 9,000,000** (real regime, turnover above RWF 20,000,000).

**Reasoning (annual brackets):**
- 0 – 720,000 @ 0% = 0
- 720,001 – 1,200,000: 480,000 × 10% = 48,000
- 1,200,001 – 2,400,000: 1,200,000 × 20% = 240,000
- 2,400,001 – 9,000,000: 6,600,000 × 30% = 1,980,000
- **Total annual PIT = 0 + 48,000 + 240,000 + 1,980,000 = RWF 2,268,000** [RRA PIT page]

**Classification:** PIT due = RWF 2,268,000, declared by 31 March of the following year.

### Example 3 — Micro-enterprise flat tax

**Input:** Self-employed, **annual turnover = RWF 6,500,000** (falls in the 4,000,001 – 7,000,000 band).

**Reasoning:** Micro-enterprise flat-tax regime. Turnover RWF 4,000,001 – 7,000,000 → fixed annual tax of **RWF 120,000**. No expense deductions permitted. [PwC, corporate]

**Classification:** Flat tax = RWF 120,000 for the year.

### Example 4 — Small-business lump-sum tax

**Input:** Self-employed, **annual turnover = RWF 16,000,000** (band 12,000,001 – 20,000,000).

**Reasoning:** Lump-sum regime = 3% of annual turnover. 16,000,000 × 3% = **RWF 480,000**. [PwC, corporate]

**Classification:** Lump-sum tax = RWF 480,000.

### Example 5 — Casual labourer

**Input:** Casual labourer, **monthly income = RWF 150,000**.

**Reasoning:** Casual-labour flat rate of 15%, with the first RWF 60,000/month at 0%.
- First 60,000 @ 0% = 0
- Remaining 90,000 × 15% = 13,500
- **Total = RWF 13,500** [RRA new-rates guide]

**Classification:** Tax withheld = RWF 13,500.

### Example 6 — RSSB pension contribution (2025)

**Input line:**
`05/03/2025 ; BK DEBIT ; RSSB PENSION FEB ; ; -XXX ; RWF`
Stated contribution base (basic + housing + transport) = **RWF 400,000/month**.

**Reasoning:** From 1 January 2025 the pension scheme is 6% employee / 6% employer (total 12%), and the base now includes basic + housing + transport allowances. [EY; PwC, other-taxes; Presidential Order N° 086/01]
- Employee 6% × 400,000 = 24,000
- Employer 6% × 400,000 = 24,000
- **Total remitted = RWF 48,000** (24,000 deducted from employee + 24,000 employer)

**Classification:** Employee deduction = RWF 24,000; employer cost = RWF 24,000.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residence and Scope

- **Residence and scope** — Residents are taxed on worldwide income; non-residents only on Rwanda-source income. The same bracket rates apply to both.  _([PwC, individual])_

### 5.2 PAYE Computation (Employment Income)

- **PAYE computation** — Employers withhold PAYE monthly using the monthly bracket table (Section 1). Monthly PAYE = annual tax ÷ 12, rounded up. PAYE return and remittance are due by the 15th of the following month.  _([PwC, tax-administration; RRA new-rates guide])_

### 5.3 Benefits in Kind

**Benefits in Kind table**

| Benefit | Statutory valuation | Source |
| --- | --- | --- |
| Housing benefit | 20% of total employment income | [PwC, sample calc] |
| Vehicle benefit | 10% of total employment income | [PwC, sample calc] |

- **BIK addition rule** — Add the valued benefit to taxable employment income before applying the brackets.

### 5.4 Casual Labour

- **Casual labour rate** — 15% flat, with the first RWF 60,000/month at 0%  _([RRA new-rates guide; Law N° 027/2022])_

### 5.5 KIFC Expert Exemption

- **KIFC expert exemption** — New residents (not resident in the prior 5 years) working as experts/professionals for KIFC-licensed entities are exempt from PIT on foreign-source income for their first 5 years of residence. Eligibility requires specialist confirmation — see R-RW-3.  _([PwC; RRA])_

### 5.6 Self-Employed Registration

- **Registration exemption threshold** — An individual must register for income tax on starting taxable activity, except where annual turnover is below RWF 2,000,000 (exempt from registration).  _([RRA register page])_

### 5.7 Micro-Enterprise Flat Tax (turnover RWF 2,000,001 – 12,000,000)

**Micro-Enterprise Flat Tax table**  _([PwC, corporate])_

| Annual turnover (RWF) | Annual flat tax (RWF) |
| --- | --- |
| 2,000,001 – 4,000,000 | 60,000 |
| 4,000,001 – 7,000,000 | 120,000 |
| 7,000,001 – 10,000,000 | 210,000 |
| 10,000,001 – 12,000,000 | 300,000 |

- **No deductions** — No expense deductions.  _([PwC, corporate])_

### 5.8 Small-Business Lump-Sum Tax (turnover RWF 12,000,001 – 20,000,000)

- **Lump-sum tax formula** — Tax = 3% of annual turnover. No expense deductions.  _([PwC, corporate])_

### 5.9 Real Regime (turnover > RWF 20,000,000, or by election)

- **Real regime rule** — Actual taxation on net profit using the annual progressive brackets, with proper accounting and deductible expenses. Election into the real regime is irrevocable for 3 years.  _([PwC, corporate])_

### 5.10 Agriculture / Livestock Exemption

- **Agriculture/livestock exemption threshold** — Income/turnover from agricultural and livestock activities is exempt up to RWF 12,000,000 per tax period; only the excess is taxable.  _([RRA register page; PwC, corporate])_

### 5.11 RSSB Social-Security Contributions (2025)

**RSSB Social-Security Contributions table**

| Scheme | Employee | Employer | Total | Base | Source |
| --- | --- | --- | --- | --- | --- |
| Pension (from 1 Jan 2025) | 6% | 6% | 12% | Basic + housing + transport allowances | [EY; PwC; Presidential Order N° 086/01] |
| Occupational hazards | 0% | 2% | 2% | Gross pay | [PwC, other-taxes] |
| Maternity leave | 0.3% | 0.3% | 0.6% | Excludes transport allowance | [PwC, other-taxes] |
| Medical (RSSB / formerly RAMA) | 7.5% | 7.5% | 15% | Basic salary (public sector / opt-in, min. 7 employees) | [RRA medical notice] |
| CBHI / Mutuelle | 0.5% | 0% | 0.5% | Net salary (after PAYE and RSSB deductions) | [PwC, other-taxes] |

*Column checks — Pension: 6 + 6 = 12 ✓. Occupational: 0 + 2 = 2 ✓. Maternity: 0.3 + 0.3 = 0.6 ✓. Medical: 7.5 + 7.5 = 15 ✓. CBHI: 0.5 + 0 = 0.5 ✓.*

**Pension phasing:** doubled from the previous 6% total (3%/3%) to 12% (6%/6%) on 1 Jan 2025. From January 2027, +2% per year, reaching **20% total (10% employee / 10% employer) by 2030**. [EY; PwC, other-taxes]

> A secondary payroll source claimed an 8%/4% pension split; this is **contradicted** by EY, PwC, and the Presidential Order, which all state an equal **6%/6%** split. Use 6%/6%.

### 5.12 Filing Deadlines

**Filing Deadlines table**

| Item | Deadline | Source |
| --- | --- | --- |
| Annual PIT declaration | 31 March of following year | [RRA notice; PwC, tax-administration] |
| PAYE return + remittance | 15th of the following month | [PwC, tax-administration] |
| Trading licence (patente) declaration | 31 January | [PwC, other-taxes] |

- **Annual-return filing exemptions** — Annual-return filing exemptions (no annual return required): annual turnover < RWF 2,000,000; recipients of only employment income (PAYE already withheld); recipients of only withholding-taxed investment income; non-residents whose Rwanda-source income has had WHT applied.  _([PwC, individual])_

### 5.13 Record Keeping

- **Record keeping** — Records must be kept 10 years; returns remain open to audit for 5 years.  _([PwC, individual])_

### 5.14 Penalties and Interest (Tax Procedures Law)

**Late declaration AND late payment table**

| Delay | Fine (% of tax due) |
| --- | --- |
| ≤ 30 days | 20% |
| 31 – 60 days | 40% |
| > 60 days | 60% |

**Declared on time but paid late table**

| Delay | Fine (% of tax due) |
| --- | --- |
| ≤ 30 days | 5% |
| 31 – 60 days | 10% |

- **Late-payment interest** — Late-payment interest: non-compounding, charged monthly from the day after the due date until payment; capped at 100% of the tax amount.  _([RRA penalties notice])_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (Real Regime)

- **Home office deduction rule** — - Calculate proportion of home used for business (dedicated room/floor area as a percentage of the whole). - Apply that percentage to rent, electricity (REG/EUCL), water (WASAC), internet. - A dual-use room does NOT qualify. **Conservative default:** 0% deduction until reviewer confirms the arrangement.

### 6.2 Motor Vehicle Business Use (Real Regime)

- **Motor vehicle business use rule** — - Only the business-use percentage of fuel, insurance, and maintenance is deductible. - Client must maintain a mileage log. **Conservative default:** 0% business use until a mileage log is provided.

### 6.3 Phone / Internet Mixed Use (Real Regime)

- **Phone/internet mixed use rule** — - Business-use portion only; client must provide a reasonable estimate. **Conservative default:** 0% deduction until business percentage is confirmed.

### 6.4 Benefit-in-Kind Edge Cases

- **Benefit-in-kind edge cases** — - Confirm whether housing/transport allowances are cash allowances (part of the RSSB pension base) or benefits in kind (statutory 20%/10% valuation). - **Flag for reviewer:** the allowance split materially affects both PAYE and RSSB.  _([PwC, sample calc; EY])_

### 6.5 Regime Election

- **Regime election flag** — - Electing into the real regime is irrevocable for 3 years — flag the long-term consequences for reviewer sign-off.  _([PwC, corporate])_

### 6.6 Agriculture / Livestock Threshold

- **Agriculture/livestock threshold flag** — - Confirm the split between exempt (first RWF 12,000,000) and taxable agricultural income.  _([RRA register page])_

### 6.7 KIFC Expert Status

- **KIFC expert status flag** — - Confirm prior-5-year non-residence and KIFC-licensed employer before applying the foreign-source exemption.  _([PwC; RRA])_

## Section 7 -- Excel Working Paper Template

```
RWANDA INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residence: Resident / Non-resident
Taxpayer type: Employee (PAYE) / Self-employed (Micro / Lump-sum / Real)

A. EMPLOYMENT INCOME (PAYE PATH)
  A1. Basic salary (annual or monthly)           ___________
  A2. Housing allowance / benefit (20% if BIK)   ___________
  A3. Transport allowance                        ___________
  A4. Vehicle benefit (10% if BIK)               ___________
  A5. Other taxable allowances                   ___________
  A6. TOTAL taxable employment income            ___________
  A7. PAYE (apply bracket table)                 ___________

B. SELF-EMPLOYMENT — REGIME TEST
  B1. Annual turnover                            ___________
  B2. Regime (Exempt <2M / Micro / Lump-sum 3% / Real)  ______
  B3. Micro flat tax OR Lump-sum 3% OR Real-regime net profit  ______

C. REAL REGIME — NET PROFIT (if applicable)
  C1. Gross business income (net of 18% VAT if registered)  ____
  C2. Less: deductible business expenses          ___________
  C3. Net taxable profit (C1 - C2)                ___________
  C4. PIT (apply annual bracket table)            ___________

D. RSSB CONTRIBUTIONS (employee side)
  D1. Pension 6% of (basic+housing+transport)     ___________
  D2. Maternity 0.3% (excl. transport)            ___________
  D3. Medical 7.5% of basic (if applicable)       ___________
  D4. CBHI 0.5% of net salary                     ___________
  D5. TOTAL employee RSSB                         ___________

E. NET PAY (employee)
  E1. Gross - PAYE - employee RSSB                ___________

REVIEWER FLAGS:
  [ ] Residence status confirmed?
  [ ] Employee vs self-employed confirmed?
  [ ] Turnover band / regime confirmed?
  [ ] Allowance split (housing/transport) confirmed?
  [ ] Benefit-in-kind valuation confirmed (housing 20% / vehicle 10%)?
  [ ] Real-regime deductions supported by documents?
  [ ] Agriculture/livestock exemption applied correctly?
  [ ] KIFC expert status (if claimed) verified?
  [ ] Casual-labour 15% applied only where genuinely casual?
```

## Section 8 -- Bank Statement Reading Guide

### Rwandan Statement Formats

**Rwandan Statement Formats table**

| Channel | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Bank of Kigali (BK) | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description holds counterparty + reference |
| I&M Bank Rwanda | PDF, CSV | Value Date, Description, Amount, Balance |  |
| Equity Bank Rwanda | PDF | Date, Particulars, Withdrawals, Deposits |  |
| MTN MoMo / Airtel Money | CSV / SMS export | Date, Counterparty, Amount, Type, Fee | Dominant for micro-enterprises; cash-in / cash-out lines |
| BPR / Cogebanque | PDF | Date, Libellé, Débit, Crédit | French terms common |

### Key Kinyarwanda / French Banking Terms

**Key Kinyarwanda / French Banking Terms table**

| Term | Language | English | Classification Hint |
| --- | --- | --- | --- |
| MUSHAHARA | Kinyarwanda | Salary | Employment income |
| KWISHYURA / KWISHYUZA | Kinyarwanda | Payment | Check direction |
| KWIMURA / TRANSFER | Kinyarwanda | Transfer | Check direction |
| INYUNGU | Kinyarwanda | Interest / profit | Investment income (or bank charge) |
| AMAFARANGA YA BANKI | Kinyarwanda | Bank charges | Deductible (real regime) |
| UBUKODE | Kinyarwanda | Rent | Rental income or office rent expense |
| INGUZANYO | Kinyarwanda | Loan | Exclude (principal) |
| VIREMENT | French | Transfer | Check direction |
| FRAIS | French | Fees / charges | Deductible (real regime) |
| LOYER | French | Rent | Rental income or rent expense |
| SALAIRE | French | Salary | Employment income |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement / payslip but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- RWANDA INCOME TAX
1. Are you a Rwanda tax resident, or non-resident with Rwanda-source income?
2. Are you an employee (PAYE) or self-employed? Both?
3. If self-employed: what is your annual turnover (for the regime test)?
4. If employed: what is your salary split (basic / housing / transport / other)?
5. Do you receive any benefits in kind (employer housing or vehicle)?
6. Are you a casual labourer (irregular day work) or a regular employee?
7. Do you have agricultural or livestock income?
8. Do any KIFC-related expat exemptions apply to you?
9. What RSSB schemes do you contribute to (pension / medical / maternity / CBHI)?
10. Do you have any other income (rental, interest, dividends)?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References table**

| Topic | Reference |
| --- | --- |
| Income tax (PIT/PAYE) rates and rules | Law N° 027/2022 of 20/10/2022 establishing taxes on income, as amended (2023) |
| Income Tax Law PDF | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| RRA PIT page | https://www.rra.gov.rw/en/taxes-fees/domestic-taxes/income-tax/personal-income-tax-pit-1 |
| RRA new PAYE rates guide | RRA news item 1669 |
| RRA register for income tax | https://www.rra.gov.rw/en/taxes-fees/domestic-taxes/income-tax/register-for-income-tax |
| RRA medical scheme notice | RRA news item 469 |
| RRA penalties / deadline notice | RRA news item 2481 |
| Pension contributions (2025) | Presidential Order N° 086/01 (gazetted 13 Dec 2024); EY tax alert |
| PwC — taxes on personal income | https://taxsummaries.pwc.com/rwanda/individual/taxes-on-personal-income |
| PwC — tax administration | https://taxsummaries.pwc.com/rwanda/individual/tax-administration |
| PwC — corporate other taxes (social contributions, VAT) | https://taxsummaries.pwc.com/rwanda/corporate/other-taxes |
| PwC — corporate income (flat-tax table, CIT 28%) | https://taxsummaries.pwc.com/rwanda/corporate/taxes-on-corporate-income |

### Related Context Rates

**Related Context Rates table**

| Item | Rate / threshold | Source |
| --- | --- | --- |
| VAT standard rate | 18% | [PwC, corporate] |
| VAT registration threshold | RWF 20,000,000/year, or RWF 5,000,000 in a calendar quarter | [PwC, corporate] |
| Corporate Income Tax | 28% | [PwC, corporate] |
| Capital gains on shares | 10% | [PwC, individual] |
| Trading licence (patente) district fee | RWF 100,000 – 2,000,000 (by turnover) | [PwC, other-taxes] |
| National minimum wage | **[RESEARCH GAP — reviewer to confirm]** — no enforceable current statutory figure; 1973/74 order (~RWF 100/day) is obsolete | [minimum-wage.org; WageIndicator] |

### Test Suite

**Test 1 — Monthly PAYE, regular employee.**
Input: Resident, monthly taxable income RWF 350,000.
Expected: PAYE = 4,000 + 20,000 + 45,000 = **RWF 69,000**.

**Test 2 — Annual PIT, real regime.**
Input: Net taxable profit RWF 9,000,000.
Expected: PIT = 48,000 + 240,000 + 1,980,000 = **RWF 2,268,000**.

**Test 3 — Micro-enterprise flat tax.**
Input: Turnover RWF 6,500,000.
Expected: Flat tax **RWF 120,000** (band 4,000,001–7,000,000).

**Test 4 — Lump-sum tax.**
Input: Turnover RWF 16,000,000.
Expected: 16,000,000 × 3% = **RWF 480,000**.

**Test 5 — Casual labourer.**
Input: Monthly income RWF 150,000.
Expected: First 60,000 @ 0% + 90,000 × 15% = **RWF 13,500**.

**Test 6 — Pension contribution (2025).**
Input: Pension base RWF 400,000/month.
Expected: Employee 6% = RWF 24,000; employer 6% = RWF 24,000; total RWF 48,000.

**Test 7 — Below registration threshold.**
Input: Self-employed turnover RWF 1,500,000.
Expected: Exempt from income-tax registration; no annual return required.

**Test 8 — Top-band monthly PAYE.**
Input: Monthly taxable income RWF 1,000,000.
Expected: 4,000 + 20,000 + (800,000 × 30% = 240,000) = **RWF 264,000**.

## PROHIBITIONS

- NEVER apply the worldwide-income basis without confirming residence status
- NEVER use the superseded 20% middle-band ("Year 1") schedule — the current middle band is 10%
- NEVER allow expense deductions for micro-enterprise (flat) or lump-sum (3%) taxpayers — those regimes tax turnover, not profit
- NEVER apply an 8%/4% pension split — the 2025 split is 6%/6%
- NEVER omit housing/transport allowances from the pension contribution base (they are now included from 2025)
- NEVER allow income tax itself, fines, or penalties as deductions
- NEVER include VAT collected on sales in turnover/income for VAT-registered self-employed
- NEVER apply the casual-labour 15% rate to a regular employee
- NEVER assume a national minimum wage figure — none is reliably enforceable
- NEVER present tax calculations as definitive — always label as estimated and pending reviewer sign-off

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
