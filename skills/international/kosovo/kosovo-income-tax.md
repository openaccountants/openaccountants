---
name: kosovo-income-tax
description: Use this skill whenever asked about Kosovo personal income tax for self-employed individuals and individuals. Trigger on phrases like "how much tax do I pay in Kosovo", "tatimi mbi te ardhurat personale", "ATK declaration", "TAK return", "annual personal income tax return", "PD form", "quarterly advance payment", "gross-income method", "real-income method", "self-employed tax Kosovo", "Trusti pension contribution", "wage withholding Kosovo", "EDI declaration", or any question about filing or computing personal income tax for a self-employed or employed individual in Kosovo. Also trigger when preparing or reviewing a Kosovo annual PD return, quarterly advance instalment, payroll withholding, computing deductible business expenses, or advising on the gross-income vs real-income method. This skill covers the graduated PIT rates (0%/8%/10%), the self-employed gross-income (3%/9%) and real-income (10%) methods, mandatory pension contributions (Trusti/KPST), payroll withholding, penalties, and interaction with VAT. ALWAYS read this skill before touching any Kosovo income tax work.
version: 0.1
jurisdiction: XK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kosovo Personal Income Tax -- Self-Employed and Individuals

## Kosovo Personal Income Tax -- Self-Employed and Individuals Skill v0.1

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Kosovo (Republika e Kosoves / Republika Kosovo) |
| ISO code | XK (ISO 3166-1 user-assigned code; Kosovo lacks a universally assigned 2-letter code) [caveat: research] |
| Tax | Personal Income Tax (Tatimi mbi te Ardhurat Personale / TAP) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) [PwC Tax administration] |
| Primary legislation | Law No. 08/L-110 on Personal Income Tax, as amended by Law No. 08/L-142 (PIT rate amendment, in force 23 August 2024) [Orbitax; ATK] |
| Supporting legislation | Law No. 06/L-105 on Corporate Income Tax; Law No. 04/L-101 on Pension Funds of Kosovo; Law on VAT (Law No. 05/L-037); Law on Tax Administration and Procedures [Orbitax; PwC] |
| Tax authority | Tax Administration of Kosovo (Administrata Tatimore e Kosoves, ATK/TAK) -- atk-ks.org |
| Filing portal | ATK EDI e-filing portal (edideklarimi.atk-ks.org) |
| Pension administrator | Kosovo Pensions Savings Trust (Trusti / KPST, trusti.org), under the BQK/CBK framework |
| Annual filing deadline | 31 March of the year following the tax year (form PD) [PwC Tax administration] |
| Quarterly advance deadlines | 15 April, 15 July, 15 October, 15 January [PwC Corporate tax administration; ATK] |
| Validated by | Pending -- requires sign-off by a Kosovo-licensed tax adviser / accountant |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rate Brackets -- Personal Income Tax (annual, 2025/2026)

**Tax Rate Brackets -- Personal Income Tax (annual, 2025/2026)**  _(Orbitax; ATK; PwC, last reviewed 13 Jan 2026)_

| Annual taxable income (EUR) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0.00 -- 3,000.00 | 0% | EUR 0.00 |
| 3,000.01 -- 5,400.00 | 8% | EUR 192.00 |
| 5,400.01 and above | 10% | -- |

Brackets are stated as **annual** amounts in the law. ATK applies them via monthly cumulative withholding for primary-employer wages. Rates in force from 23 August 2024 under Law No. 08/L-142, unchanged for 2025 and 2026 [Orbitax; ATK; PwC, last reviewed 13 Jan 2026].

**Arithmetic note (verified):** Tax at top of the 8% band = (5,400 - 3,000) x 8% = 2,400 x 8% = EUR 192.00. Above EUR 5,400, tax = EUR 192.00 + 10% x (income - 5,400.00).

**Kosovo has no standard deduction and no personal/family allowance -- the first EUR 3,000 (0% band) IS the only general relief** [PwC Deductions].

**Secondary-employer wages** are taxed at a **flat 10%** with no 0%/8% bands, since the graduated bands apply only to the primary employer [ATK; PwC].

### Self-Employed Taxation Methods

**Self-Employed Taxation Methods**

| Method | Eligibility | Rate | Reference |
| --- | --- | --- | --- |
| Gross-income (turnover) method -- trade | Annual gross income up to EUR 50,000 [caveat: see RESEARCH GAP below] | 3% of gross receipts (trade, transport, agriculture and similar) | PwC Corporate other taxes / income determination |
| Gross-income (turnover) method -- services | Annual gross income up to EUR 50,000 [caveat: see RESEARCH GAP below] | 9% of gross receipts (services, professional, vocational, entertainment and similar) | PwC Corporate other taxes / income determination |
| Real-income method | Annual gross income over EUR 50,000 (mandatory), or elected voluntarily below the threshold | 10% on net taxable profit; business deductions follow corporate rules | PwC Deductions / Corporate |
| Minimum quarterly payment (gross-income method) | Applies under the gross-income method | EUR 37.50 per quarter | PwC Corporate other taxes |

> **[RESEARCH GAP -- reviewer to confirm]** Most sources (PwC corporate/individual summaries, secondary payroll guides) state the gross-income-method election ceiling is **EUR 50,000** annual gross income. A **EUR 30,000** figure also appears in some sources for the CIT/VAT context (small-business turnover and VAT registration). Confirm against the consolidated text of PIT Law No. 08/L-110 whether the gross-income election ceiling is EUR 50,000 (used here) or EUR 30,000.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Residency status unknown | STOP -- do not compute without confirming Kosovo tax residency (worldwide vs Kosovo-source) |
| Self-employed activity ambiguous between trade (3%) and services (9%) | Apply 9% services rate (conservative) |
| Annual gross income exceeds EUR 50,000 | Real-income method (10% on net profit) -- mandatory above threshold [caveat: see RESEARCH GAP] |
| Secondary employment | Withhold flat 10% (no 0%/8% bands) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Pension contribution base above EUR 24,000/year | Do not contribute on the excess (cap applies) |
| Unknown VAT registration status | Assume not registered until turnover/registration confirmed |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) Kosovo tax residency, (b) employment vs self-employed status, and (c) for self-employed, the taxation method (gross-income 3%/9% or real-income 10%).

**Recommended** -- all sales invoices, purchase invoices/receipts, Trusti/KPST pension contribution records, prior-year PD return or ATK assessment, VAT registration status, payroll WM/WR records if an employer.

**Ideal** -- complete income and expenditure account, fixed-asset register, quarterly advance-payment confirmations (QS/QL), employment-income certificates, evidence of activity classification (trade vs services).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This Kosovo PIT computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation, that the correct taxation method (gross-income vs real-income) was applied, and that pension contributions reconcile to Trusti/KPST records."

### Refusal Catalogue

- **R-XK-1 -- Residency unknown** — Residents are taxed on worldwide income; non-residents only on Kosovo-source income [PwC Residence]. This skill cannot compute tax without confirming Kosovo tax residency. Please confirm before proceeding.  _(PwC Residence)_
- **R-XK-2 -- Companies / partnerships** — This skill covers individuals and self-employed sole proprietors only. Corporate income tax (Law No. 06/L-105), partnerships, and group structures file separately. Escalate to a Kosovo-licensed accountant.  _(Law No. 06/L-105)_
- **R-XK-3 -- Cross-border / treaty** — Non-resident and treaty-relief taxation, foreign tax credits, and permanent-establishment analysis are out of scope. Escalate to a Kosovo-licensed accountant.
- **R-XK-4 -- Capital gains / property disposals** — Capital gains and immovable-property disposal computations require specialised analysis. Escalate to a Kosovo-licensed accountant.
- **R-XK-5 -- Arrears / enforcement** — Client has outstanding tax arrears or is subject to ATK enforcement. Late-payment interest accrues monthly up to ten years and understatement penalties run 15%-25%. Do not advise. Escalate to a Kosovo-licensed accountant immediately.
- **R-XK-6 -- VAT return requested** — This skill covers personal income tax only. For Kosovo VAT (standard 18%, reduced 8%; registration above EUR 30,000 turnover), use a dedicated Kosovo VAT skill.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. Albanian terms are shown alongside English equivalents.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFER, DEPOZITE, PAGESE, PAYMENT RECEIVED | Business income (gross receipts) | If VAT-registered, extract net (excl. 18% VAT) |
| HONORAR, FATURA, FEES, CONSULTANCY, KESHILLIM | Business income | Professional/consultancy fees -- self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Platform payout -- match to invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Business income | Platform payout -- verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Business income | International platform payout |
| UPWORK, FIVERR, TOPTAL | Business income | Freelance platform -- net of platform commission |
| PAGA, RROGA, SALARY, EMPLOYER [name] | Employment income | Primary vs secondary employment matters for withholding |
| QIRA, RENT RECEIVED | Rental income | Taxed as rental income (see 5.7) |
| INTERES, INTEREST RECEIVED | Investment income | Interest on Kosovo government bonds is EXEMPT [PwC] |
| DIVIDENDE, DIVIDEND | EXCLUDE | Dividends are EXEMPT from PIT (resident and non-resident) [PwC] |
| KTHIM TATIMI, TAX REFUND, ATK REFUND | EXCLUDE | Tax refund from prior year |
| GRANT, SUBVENCION, GOVERNMENT GRANT | Check nature | Capital grants EXCLUDE; revenue grants = business income |

### 3.2 Expense Patterns (Debits) -- Fully Deductible (real-income method only)

Deductions apply **only under the real-income (10%) method**. Under the gross-income (3%/9%) method, tax is on gross receipts and **no expense deductions are taken**.

**3.2 Expense Patterns (Debits) -- Fully Deductible (real-income method only)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| QIRA ZYRE, OFFICE RENT, RENT [commercial address] | Office rent | Deductible | Dedicated business premises |
| SIGURIM PROFESIONAL, PROFESSIONAL INDEMNITY | Professional insurance | Deductible |  |
| KONTABILIST, ACCOUNTANT, AUDITOR, BOOKKEEP | Accountancy fees | Deductible |  |
| AVOKAT, LAWYER, LEGAL, NOTER | Legal fees | Deductible | Must be business-related |
| ZYRE, OFFICE SUPPLIES, STATIONERY | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, REKLAMA | Marketing/advertising | Deductible |  |
| TRAJNIM, TRAINING, COURSE, SEMINAR | Training | Deductible | Must relate to current business |
| TARIFE BANKE, BANK FEE, BANK CHARGE | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN | IT infrastructure | Deductible | Capitalise large items (see 3.7) |

### 3.3 Expense Patterns (Debits) -- SaaS and Software (real-income method)

**3.3 Expense Patterns (Debits) -- SaaS and Software (real-income method)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment, real-income method)

**3.4 Expense Patterns (Debits) -- Utilities (may need apportionment, real-income method)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| KEK, KESCO, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| UJESJELLES, WATER | Water | T2 if home office | Apportion for home use |
| IPKO, KUJTESA, VALA, TELEKOM, BROADBAND | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBILE, GSM | Phone | T2 | Business-use portion only |

### 3.5 Expense Patterns (Debits) -- Travel (real-income method)

**3.5 Expense Patterns (Debits) -- Travel (real-income method)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| WIZZ AIR, AIR PRISTINA, EASYJET, FLIGHT | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| TAXI, BOLT, UBER | Local transport | Deductible if business purpose |  |
| KARBURANT, FUEL, PETROL, NAFTE | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING, PARKIM | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORANT, RESTAURANT, DINNER, CLIENT MEAL, ARGETIM | Entertainment | NOT deductible | Treat as entertainment by default |
| PERSONAL, USHQIM, GROCERIES, SUPERMARKET, VIVA FRESH | Personal expenses | NOT deductible | Private living costs |
| GJOBE, FINE, PENALTY, MULTA | Fines/penalties | NOT deductible | Public policy |
| ATK PAYMENT, TATIM, INCOME TAX | Tax payments | NOT deductible | Income tax cannot reduce income |
| TERHEQJE, DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (real-income method, depreciate)

Depreciation under the real-income method follows corporate rules (Law No. 06/L-105). Specific category rates are **[RESEARCH GAP -- reviewer to confirm exact depreciation pool rates against the CIT Law and ATK guidance]**.

**3.7 Expense Patterns (Debits) -- Capital Items (real-income method, depreciate)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | Capitalise + depreciate | Rate per CIT Law [RESEARCH GAP] |
| PRINTER, SCANNER, COPIER | Office equipment | Capitalise + depreciate | Rate per CIT Law [RESEARCH GAP] |
| MOBILJE, FURNITURE, DESK, CHAIR | Furniture/fittings | Capitalise + depreciate | Rate per CIT Law [RESEARCH GAP] |
| VETURE, VEHICLE, CAR (business) | Motor vehicle | Capitalise + depreciate | Business % only |

### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER INTERN, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| KREDI, LOAN REPAYMENT, PRINCIPAL | EXCLUDE | Loan principal movement |
| TRUSTI, KPST, PENSION, CONTRIBUTION | Pension deduction | Mandatory 5% employee portion deductible for PIT (see 5.6) |
| TVSH, VAT PAYMENT | EXCLUDE | VAT liability payment, not expense |
| KESTI, ADVANCE PAYMENT, QS, QL | Advance tax paid | Credit against annual liability, not an expense |

### 3.9 Kosovo Banks -- Statement Format Reference

**3.9 Kosovo Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| ProCredit Bank | TRANSFER, PAGESE, TARIFA | PDF/CSV; description holds counterparty + reference |
| Raiffeisen Bank Kosovo | PAYMENT, TRANSFER, FEE | PDF/CSV; merchant in description |
| Banka Kombetare Tregtare (BKT) | TRANSFER, DEBIT DIRECT, TARIFE | PDF; Albanian-language descriptions common |
| TEB Bank | PAGESE, KARTE, TRANSFER | PDF/CSV |
| NLB Banka | TRANSFER, PAGESE, KOMISION | PDF; shorter descriptions |

## Section 4 -- Worked Examples

All amounts in EUR. Tax recomputed end-to-end.

### Example 1 -- Self-Employed, Real-Income Method, Net Profit Computation

**Inputs:** Resident sole proprietor, real-income method. Gross receipts EUR 60,000 (over the EUR 50,000 threshold, so real-income is mandatory). Allowable business expenses EUR 22,000. Mandatory self-employed pension contribution paid EUR 1,200.

**Reasoning:**
Net taxable profit = 60,000 - 22,000 = EUR 38,000. The real-income method applies a flat 10% on net taxable profit [PwC Deductions/Corporate].

**Computation:** PIT = 38,000 x 10% = **EUR 3,800.00**.

> Note: Under the real-income method PwC states a flat 10% on net profit. This skill does **not** apply the 0%/8%/10% graduated wage brackets to self-employed business profit under the real-income method; the graduated bands govern **employment wages**. Reviewer to confirm interaction where an individual has both wage and business income. **[RESEARCH GAP -- reviewer to confirm aggregation rule]**

### Example 2 -- Self-Employed, Gross-Income Method, Services (9%)

**Input line:**
`12/03/2025 ; PROCREDIT TRANSFER IN ; KLIENTI SH.P.K. ; PAGESE FATURA 2025-014 ; +4,500.00 ; EUR`

**Reasoning:**
Annual gross receipts EUR 41,000 (under EUR 50,000), services activity. Gross-income method at 9% applies to gross receipts; no expense deductions [PwC]. Quarterly tax is 9% of that quarter's gross receipts, subject to a minimum of EUR 37.50.

**Computation (annual):** PIT = 41,000 x 9% = **EUR 3,690.00**. Each quarter pays 9% of quarterly gross receipts (minimum EUR 37.50).

**Classification:** This single credit (EUR 4,500) is gross business income; quarter's tax on it = 4,500 x 9% = EUR 405.00 (> EUR 37.50 minimum, so EUR 405.00 applies).

### Example 3 -- Self-Employed, Gross-Income Method, Trade (3%)

**Reasoning:**
Resident sole proprietor, retail trade, annual gross receipts EUR 30,000 (under EUR 50,000). Trade activity uses the 3% gross-income rate [PwC].

**Computation:** PIT = 30,000 x 3% = **EUR 900.00**. Compare quarterly: 900 / 4 = EUR 225.00 per quarter, each above the EUR 37.50 minimum.

### Example 4 -- Primary Employment Wage Withholding (graduated brackets)

**Input line:**
`31/01/2025 ; RAIFFEISEN ; EMPLOYER ABC SH.A. ; PAGA JANAR (NET) ; +1,140.00 ; EUR`

**Reasoning:**
Annual gross wage EUR 14,400 (EUR 1,200/month) from the primary employer. First the mandatory employee pension of 5% is withheld and is **deductible** for PIT [PwC Other taxes]; PIT is then computed on the graduated annual brackets.

**Computation (annual basis):**
- Gross wage: EUR 14,400.00
- Employee pension 5%: 14,400 x 5% = EUR 720.00 (deductible; pensionable cap EUR 24,000/yr not exceeded)
- PIT base: 14,400 - 720 = EUR 13,680.00
- PIT: 0% on first 3,000 = EUR 0; 8% on 3,000.01-5,400 = EUR 192.00; 10% on (13,680 - 5,400) = 8,280 x 10% = EUR 828.00
- Total annual PIT = 192.00 + 828.00 = **EUR 1,020.00**
- Net annual = 14,400 - 720 - 1,020 = **EUR 12,660.00** (employer also remits its own 5% pension)

> **[RESEARCH GAP -- reviewer to confirm]** Whether the employee pension contribution reduces the PIT base before applying the brackets is treated here per PwC "mandatory employee contribution is tax-deductible for PIT". Confirm the exact ATK monthly cumulative-withholding mechanics (commonly EUR 250/month at 0%, 250.01-450 at 8%, over 450 at 10%) against the current ATK withholding tables/calculator.

### Example 5 -- Secondary Employment (flat 10%)

**Input line:**
`28/02/2025 ; TEB BANK ; EMPLOYER XYZ ; PAGA DYTESORE SHKURT ; +500.00 ; EUR`

**Reasoning:**
Wage from a **secondary** employer. Graduated 0%/8% bands apply only to the primary employer; secondary-employer wages are withheld at a **flat 10%** [ATK; PwC].

**Computation:** PIT withheld = 500 x 10% = **EUR 50.00** per the gross secondary wage for that period.

### Example 6 -- Mandatory Pension Contribution (Trusti/KPST)

**Input line:**
`15/02/2025 ; BKT ; TRUSTI KPST ; KONTRIBUT PENSIONAL JANAR ; -120.00 ; EUR`

**Reasoning:**
On a gross wage of EUR 1,200, total mandatory pension = 10% = EUR 120.00 (5% employee EUR 60.00 + 5% employer EUR 60.00) remitted to Trusti/KPST [PwC Other taxes; BQK]. Only the employee 5% (EUR 60.00) is PIT-deductible.

**Classification:** Employee 5% (EUR 60.00) = PIT deduction; employer 5% (EUR 60.00) = employer cost, not a PIT deduction for the individual.

### Example 7 -- Dividend Received (Exempt)

**Input line:**
`20/04/2025 ; NLB BANKA ; KOMPANIA SH.P.K. ; DIVIDENDE 2024 ; +2,000.00 ; EUR`

**Reasoning:**
Dividends received by residents and non-residents are **exempt** from PIT [PwC Income determination].

**Classification:** EXCLUDE. EUR 0 added to taxable income.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency and Scope

- **Residency and Scope** — Residents are taxed on worldwide income; non-residents only on Kosovo-source income. Confirm residency before any computation.  _(Law No. 08/L-110; PwC Residence / Taxes on personal income)_

### 5.2 Graduated PIT Rates (employment / general income)

**5.2 Graduated PIT Rates (employment / general income)**  _(Orbitax; ATK)_

| Annual taxable income (EUR) | Rate |
| --- | --- |
| 0.00 -- 3,000.00 | 0% |
| 3,000.01 -- 5,400.00 | 8% |
| 5,400.01+ | 10% |

- **No standard deduction / allowance** — In force from 23 August 2024 (Law No. 08/L-142), unchanged for 2025/2026. No standard deduction; no personal/family allowance.  _(Orbitax; ATK; PwC Deductions)_

### 5.3 Self-Employed -- Gross-Income (Turnover) Method

- **Gross-income method trade rate** — 3% on gross receipts for trade, transport, agriculture and similar  _(PwC Corporate other taxes / income determination)_
- **Gross-income method services rate** — 9% on gross receipts for services, professional, vocational, entertainment and similar  _(PwC Corporate other taxes / income determination)_
- **Minimum quarterly payment and no deductions** — Minimum quarterly payment EUR 37.50; no expense deductions (tax is on gross receipts). For annual gross income up to EUR 50,000 [RESEARCH GAP -- see Section 1] the gross-income method may apply.  _(PwC Corporate other taxes / income determination)_

### 5.4 Self-Employed -- Real-Income Method

- **Real-income method** — For annual gross income over EUR 50,000 (mandatory) [RESEARCH GAP -- see Section 1], or elected voluntarily below the threshold: 10% on net taxable profit; business deductions follow corporate rules (Law No. 06/L-105).  _(PwC Deductions / Corporate)_

### 5.5 Exempt Income

**5.5 Exempt Income**

| Item | Treatment | Reference |
| --- | --- | --- |
| Dividends (resident and non-resident recipients) | Exempt from PIT | PwC Income determination |
| Interest on Kosovo government bonds | Exempt | PwC Income determination |

### 5.6 Mandatory Pension Contributions

**5.6 Mandatory Pension Contributions**  _(PwC Other taxes; BQK)_

| Party | Rate | Base | Cap | Reference |
| --- | --- | --- | --- | --- |
| Employee | 5% of gross wage | Gross wage | EUR 24,000/yr pensionable earnings | PwC Other taxes; BQK |
| Employer | 5% of gross wage | Gross wage | EUR 24,000/yr pensionable earnings | PwC Other taxes; BQK |
| **Total mandatory** | **10%** | Gross wage | EUR 24,000/yr | -- |

**Verification:** employee 5% + employer 5% = 10% total. Confirmed.

- Floor: statutory minimum wage. Cap: pensionable earnings above EUR 24,000/year are not subject to contributions [BQK].
- Only the **mandatory employee 5%** is PIT-deductible. Voluntary supplementary contributions (up to 15% each, max 30% combined including the mandatory portion) are **not** PIT-deductible above the mandatory rate [PwC Other taxes].
- Self-employed individuals are also obliged to pay pension contributions [ATK; payroll guides].
- Kosovo has **no separate general social-security or state health-insurance payroll tax** beyond the mandatory pension contribution **[RESEARCH GAP -- reviewer to confirm no health-insurance contribution introduced for 2026]**.

### 5.7 Rental Income

- **Rental income taxation** — Where rental is an **economic activity**, rental income is taxed at **10% of gross rent per quarter** [PwC Corporate other taxes]. Otherwise classified as rental income under PIT (3%/9% gross-income or real-income treatment per classification). **[RESEARCH GAP -- reviewer to confirm exact rental withholding/quarterly rate and classification.]**  _(PwC Corporate other taxes)_

### 5.8 Charitable Donations

- **Charitable donations deduction** — Charitable donations/sponsorships are deductible up to 10% of taxable income (an additional 10% may be possible under other laws), for real/accrual-basis taxpayers only.  _(PwC Deductions)_

### 5.9 Inheritances / Gifts; Wealth Tax

- **Inheritances/gifts and wealth tax** — Inheritances/gifts to spouse, children, or parents are exempt. For other recipients, amounts over EUR 5,000 are taxed at PIT rates (0-10%). There is no net wealth tax.  _(PwC Other taxes)_

### 5.10 VAT Interaction

**5.10 VAT Interaction**

| Scenario | PIT Treatment |
| --- | --- |
| VAT collected on sales (registered, standard 18%) | NOT income -- exclude from business receipts |
| Input VAT recovered (registered) | NOT an expense -- exclude (real-income method) |
| Non-registered (below EUR 30,000 turnover) | VAT paid on purchases is part of the gross cost |

- **VAT rates and registration threshold** — VAT: standard rate 18%, reduced rate 8%; mandatory registration above EUR 30,000 annual turnover (importers/exporters always).  _(PwC; Grant Thornton)_

### 5.11 Filing, Advance Payments, Deadlines

**5.11 Filing, Advance Payments, Deadlines**

| Item | Detail | Reference |
| --- | --- | --- |
| Annual return (form PD) | Due 31 March of the following year; calendar tax year | PwC Tax administration |
| Quarterly advance (QS, gross-income 3%/9%) | Due 15 April, 15 July, 15 October, 15 January | ATK |
| Quarterly advance (QL, real-income / economic-activity income over EUR 30,000) | Instalment = 1/4 of 110% of prior-year liability (or estimate in first/loss year); same quarterly dates | ATK; PwC Corporate tax administration |
| Employer payroll filing/remittance (WM/WR) | By the 15th of the following month | PwC Tax administration |
| New-hire reporting | Notify ATK at least one day before start | PwC Tax administration |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (real-income method)

- Apportion rent and utilities by business-use proportion; dedicated workspace required.
- **Conservative default:** 0% until reviewer confirms arrangement.
- **Flag for reviewer:** floor-area basis and dedicated-use confirmation.

### 6.2 Motor Vehicle Business Use (real-income method)

- Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible; mileage log required.
- **Conservative default:** 0% business use until log provided.

### 6.3 Phone / Internet Mixed Use (real-income method)

- Business-use portion only; reasonable estimate required.
- **Conservative default:** 0% until business percentage confirmed.

### 6.4 Activity Classification (3% vs 9%)

- If activity sits between trade (3%) and services (9%), apply 9% by default.
- **Flag for reviewer:** confirm the predominant activity and applicable rate.

### 6.5 Method Election Near the Threshold

- Below EUR 50,000 gross, the taxpayer may elect the real-income method; above EUR 50,000 it is mandatory [RESEARCH GAP -- see Section 1].
- **Flag for reviewer:** confirm gross-income figure and any election filed with ATK.

### 6.6 Pension Cap and Minimum-Wage Floor

- Apply the EUR 24,000/year pensionable cap; use minimum wage as the floor.
- **Flag for reviewer:** re-confirm the cap and floor against current BQK/Trusti regulation, especially as the minimum wage rises in 2026.

### 6.7 Capital Asset Depreciation

- Real-income method follows CIT depreciation pools; exact rates are a **[RESEARCH GAP]**.
- **Flag for reviewer:** confirm pool rates and balancing charges/allowances on disposal.

## Section 7 -- Excel Working Paper Template

```
KOSOVO PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident (worldwide) / Non-resident (Kosovo-source)
Status: Employed / Self-employed
If self-employed -- Method: Gross-income (3% / 9%) / Real-income (10%)

A. BUSINESS INCOME
  A1. Gross receipts (net of VAT if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, Wise)     ___________
  A3. Other business income                        ___________
  A4. TOTAL gross receipts                         ___________

GROSS-INCOME METHOD (3% / 9%) -- skip Section B
  G1. Rate (3% trade / 9% services)                ___________
  G2. PIT = A4 x rate                              ___________
  G3. Quarterly = G2 / 4 (min EUR 37.50/qtr)       ___________

REAL-INCOME METHOD (10%) -- complete Section B
B. ALLOWABLE DEDUCTIONS (real-income only)
  B1. Office rent                                  ___________
  B2. Professional insurance                       ___________
  B3. Accountancy / legal fees                     ___________
  B4. Office supplies                              ___________
  B5. Software subscriptions                       ___________
  B6. Marketing / advertising                      ___________
  B7. Bank / payment processing fees               ___________
  B8. Training                                     ___________
  B9. Travel                                       ___________
  B10. Telecoms (business %)                       ___________
  B11. Home office (business %)                    ___________
  B12. Vehicle (business %)                        ___________
  B13. Depreciation (per CIT rules)                ___________
  B14. Charitable donations (max 10% of income)    ___________
  B15. TOTAL deductions                            ___________

C. NET TAXABLE PROFIT (A4 - B15)                   ___________
  C1. PIT (real-income) = C x 10%                  ___________

EMPLOYMENT INCOME (graduated brackets)
D. WAGE COMPUTATION
  D1. Gross annual wage (primary employer)         ___________
  D2. Employee pension 5% (cap EUR 24,000 base)    ___________
  D3. PIT base = D1 - D2                           ___________
  D4. 0% on 0-3,000                                = 0.00
  D5. 8% on 3,000.01-5,400 (max EUR 192.00)        ___________
  D6. 10% on amount over 5,400                     ___________
  D7. PIT on primary wage = D5 + D6                ___________
  D8. Secondary wage x 10% (flat)                  ___________

E. ADVANCE PAYMENTS / CREDITS
  E1. Quarterly advances paid (QS / QL)            ___________
  E2. Wage tax already withheld                    ___________

F. ANNUAL RECONCILIATION (form PD)
  F1. Total PIT liability                          ___________
  F2. Less advances/withholding (E1 + E2)          ___________
  F3. Tax due / refund (F1 - F2)                   ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Method (gross-income vs real-income) confirmed?
  [ ] Activity classification (3% vs 9%) confirmed?
  [ ] Gross income vs EUR 50,000 threshold confirmed? [RESEARCH GAP]
  [ ] Pension cap EUR 24,000 and minimum-wage floor applied?
  [ ] Only mandatory 5% employee pension deducted for PIT?
  [ ] Primary vs secondary employment split correct (flat 10% on secondary)?
  [ ] Dividends / govt-bond interest excluded (exempt)?
  [ ] VAT excluded from receipts/expenses if registered?
  [ ] All T2 items flagged?
```

## Section 8 -- Bank Statement Reading Guide

### Kosovo Bank Statement Formats

**Kosovo Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| ProCredit Bank | PDF, CSV | Date, Description, Debit, Credit, Balance | Description holds counterparty + reference |
| Raiffeisen Bank Kosovo | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant |
| BKT (Banka Kombetare Tregtare) | PDF | Date, Pershkrimi, Debi, Kredi | Albanian-language descriptions common |
| TEB Bank | PDF, CSV | Date, Description, Amount, Balance |  |
| NLB Banka | PDF | Date, Pershkrimi, Amount, Balance | Shorter descriptions |

### Key Albanian Banking / Tax Terms

**Key Albanian Banking / Tax Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFER / TRANSFERIM | Transfer | Check direction for income/expense |
| PAGESE | Payment | Expense or income depending on direction |
| PAGA / RROGA | Wage / salary | Employment income (primary vs secondary) |
| QIRA | Rent | Rental income or office-rent expense |
| FATURA | Invoice | Business income (incoming) |
| HONORAR | Fee / honorarium | Professional self-employment income |
| TARIFA / KOMISION | Fee / commission | Bank charge (deductible, real-income) |
| INTERES | Interest | Interest income (govt-bond interest exempt) |
| DIVIDENDE | Dividend | EXEMPT -- exclude |
| KONTRIBUT PENSIONAL / TRUSTI / KPST | Pension contribution | Mandatory 5% employee portion deductible |
| TVSH | VAT | Exclude from income tax |
| TATIM / ATK | Tax / tax authority | Tax payment -- not deductible |
| GJOBE | Fine | Not deductible |
| TERHEQJE | Withdrawal | Possible drawings -- ask |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- KOSOVO PERSONAL INCOME TAX
1. Are you a Kosovo tax resident (taxed on worldwide income)?
2. Are you employed, self-employed, or both?
3. If self-employed: what is your annual gross income? (Threshold EUR 50,000)
4. If self-employed: is your activity trade (3%) or services (9%)?
5. Have you elected the real-income (10%) method, or use the gross-income method?
6. Are you VAT-registered? (Threshold EUR 30,000 turnover)
7. If employed: is this your primary or a secondary employer?
8. Pension: how much was paid to Trusti/KPST during the year (employee portion)?
9. Quarterly advances paid (QS/QL) during the year?
10. Any exempt income (dividends, Kosovo govt-bond interest)?
11. Any capital assets purchased during the year (real-income method)?
12. Any rental income, and is it an economic activity?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference |
| --- | --- |
| PIT rates and rules | Law No. 08/L-110, as amended by Law No. 08/L-142 (in force 23 Aug 2024) [Orbitax; ATK] |
| Corporate / small-business gross-receipts rules | Law No. 06/L-105 [PwC Corporate] |
| Pension contributions | Law No. 04/L-101; BQK pension framework [BQK] |
| VAT | Law No. 05/L-037 [PwC; Grant Thornton] |
| Penalties / procedure | Law on Tax Administration and Procedures |
| Filing portal | ATK EDI (edideklarimi.atk-ks.org) |

### Key Figures (with provenance)

**Key Figures (with provenance)**

| Figure | Value | Reference |
| --- | --- | --- |
| PIT 0% band | EUR 0 -- 3,000/yr | Orbitax; ATK; PwC |
| PIT 8% band | EUR 3,000.01 -- 5,400/yr | Orbitax; ATK; PwC |
| PIT 10% band | EUR 5,400.01+/yr | Orbitax; ATK; PwC |
| Tax at top of 8% band | EUR 192.00 | Computed: 2,400 x 8% |
| Secondary-employer wage rate | Flat 10% | ATK; PwC |
| Gross-income method ceiling | EUR 50,000/yr [RESEARCH GAP] | PwC; secondary guides |
| Gross-income trade rate | 3% | PwC |
| Gross-income services rate | 9% | PwC |
| Gross-income minimum quarterly | EUR 37.50 | PwC |
| Real-income method rate | 10% on net profit | PwC |
| Mandatory pension (employee + employer) | 5% + 5% = 10% | PwC Other taxes; BQK |
| Pensionable earnings cap | EUR 24,000/yr | BQK |
| Voluntary pension cap | Up to 15% each (30% combined incl. mandatory) | PwC Other taxes |
| VAT standard / reduced rate | 18% / 8% | PwC; Grant Thornton |
| VAT registration threshold | EUR 30,000 turnover/yr | PwC; Grant Thornton |
| CIT / small-business turnover threshold | EUR 30,000/yr | PwC Corporate |
| Quarterly advance trigger (economic activity) | over EUR 30,000/yr | ATK; PwC |
| Quarterly advance instalment | 1/4 of 110% of prior-year liability | ATK; PwC Corporate tax admin |
| Gift/inheritance taxable threshold (non-close family) | over EUR 5,000 | PwC Other taxes |
| Charitable donation deduction | up to 10% of taxable income | PwC Deductions |
| Minimum wage (2025) | EUR 350/month gross (effective 1 Oct 2024) | Government Decision; Playroll |
| Minimum wage (from 1 Jan 2026) | EUR 425/month gross | Government Decision 10/273; Playroll |
| Minimum wage (from 1 Jul 2026) | EUR 500/month gross | Government Decision 10/273; Playroll |

### Penalties

**Penalties**

| Type | Amount | Reference |
| --- | --- | --- |
| Tax understatement / under-declaration | 15% to 25% of under-declared tax (by magnitude) | Law on Tax Administration and Procedures |
| Late filing | Fixed mandatory administrative fines (set per the Law on Tax Administration and Procedures) | Law on Tax Administration and Procedures |
| Late payment interest | Monthly rate set annually above commercial bank lending rates; accrues up to a maximum of ten years from the due date | Law on Tax Administration and Procedures |
| Amendment window | Amended returns may be filed within three years of the mandatory filing date | Law on Tax Administration and Procedures |

### Forms

**Forms**

| Form | Purpose | Deadline |
| --- | --- | --- |
| PD -- Annual Personal Income Tax declaration | Annual reconciliation of personal income | 31 March of following year |
| QS -- Quarterly statement (gross-income 3%/9%) | Quarterly tax on gross receipts | 15 Apr, 15 Jul, 15 Oct, 15 Jan |
| QL -- Quarterly advance instalment (real-income) | Advance for economic-activity income over EUR 30,000 | 15 Apr, 15 Jul, 15 Oct, 15 Jan |
| WM / WR -- Monthly wage withholding statements | Employer reports PIT + pension withheld | By the 15th of following month |
| Rental withholding / rental tax | Rental income (economic activity) | Per quarterly schedule; reconciled in annual return |

> **[RESEARCH GAP -- reviewer to confirm]** Exact EDI form codes (especially the individual annual declaration code) were not pinned to an ATK source page in research; verify the precise form codes on the ATK portal. The ATK official site returned a TLS certificate error during research; ATK figures were corroborated via Orbitax and PwC.

### Test Suite

Input: Resident sole proprietor, real-income method, gross receipts EUR 60,000, deductions EUR 22,000.
Expected: Net profit = EUR 38,000. PIT = 38,000 x 10% = **EUR 3,800.00**.

Input: Self-employed services, annual gross receipts EUR 41,000 (under EUR 50,000).
Expected: PIT = 41,000 x 9% = **EUR 3,690.00**.

Input: Self-employed trade, annual gross receipts EUR 30,000.
Expected: PIT = 30,000 x 3% = **EUR 900.00**; quarterly = EUR 225.00 (above EUR 37.50 min).

Input: Primary-employer gross wage EUR 14,400/yr; employee pension 5%.
Expected: Pension = EUR 720.00; PIT base = EUR 13,680.00; PIT = 192.00 + (8,280 x 10% = 828.00) = **EUR 1,020.00**.

Input: Secondary-employer wage EUR 500.
Expected: PIT = 500 x 10% = **EUR 50.00**.

Input: Gross wage EUR 1,200/month.
Expected: Total pension = EUR 120.00 (employee EUR 60.00 + employer EUR 60.00); only employee EUR 60.00 deductible for PIT.

Input: Dividend received EUR 2,000.
Expected: EXCLUDE -- EUR 0 added to taxable income.

Input: Annual taxable income exactly EUR 5,400.
Expected: PIT = 0 + (2,400 x 8% = 192.00) = **EUR 192.00**.

## PROHIBITIONS

- NEVER compute Kosovo PIT without confirming tax residency
- NEVER apply expense deductions under the gross-income (3%/9%) method -- it taxes gross receipts
- NEVER apply the graduated 0%/8% bands to secondary-employer wages -- use flat 10%
- NEVER include exempt dividends or Kosovo government-bond interest in taxable income
- NEVER deduct voluntary pension contributions above the mandatory 5% employee portion for PIT
- NEVER contribute pension on pensionable earnings above EUR 24,000/year
- NEVER include VAT collected on sales in business receipts for VAT-registered taxpayers
- NEVER allow fines, penalties, drawings, or income tax itself as a deduction
- NEVER use current-year income for quarterly advances -- use 1/4 of 110% of prior-year liability
- NEVER present tax calculations as definitive -- always label as estimated and flag every [RESEARCH GAP] for reviewer confirmation

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
