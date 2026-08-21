---
name: serbia-income-tax
description: Use this skill whenever asked about Serbia (Republic of Serbia) personal income tax for self-employed individuals, entrepreneurs, freelancers, and employees. Trigger on phrases like "how much tax do I pay in Serbia", "porez na dohodak", "PP GPDG", "annual income tax", "paušalac", "flat-rate entrepreneur", "freelancer self-taxation", "Model A Model B", "non-taxable salary cap", "PIO contributions", "PPP-PD", "self-employed tax Serbia", "frilenseri", "dinar tax", or any question about filing or computing Serbian personal income tax. Also trigger when preparing or reviewing a PP GPDG annual return, a PPDG-1S/PPDG-1R entrepreneur return, a freelancer quarterly self-taxation return, or payroll withholding (PPP-PD), and when computing social security contributions (PIO, health, unemployment). This skill covers the 10% flat employment/entrepreneur tax, freelancer Models A and B, scheduler income taxes (capital gains, dividends, interest, rental, royalties, other), the annual supplementary progressive tax, social contribution rates and base limits, and penalties. ALWAYS read this skill before touching any Serbian income tax work.
version: 0.1
jurisdiction: RS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Serbia Personal Income Tax -- Self-Employed & Individuals

## Serbia Personal Income Tax -- Self-Employed & Individuals Skill v0.1

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Serbia (Republic of Serbia) |
| Tax | Personal income tax (porez na dohodak građana) + mandatory social contributions |
| Currency | RSD (Serbian dinar) only |
| Tax year | Calendar year (1 January -- 31 December); income year 2025 |
| Primary legislation | Law on Personal Income Tax (Zakon o porezu na dohodak građana) |
| Supporting legislation | Law on Mandatory Social Insurance Contributions (Zakon o doprinosima za obavezno socijalno osiguranje); Law on Tax Procedure and Tax Administration (ZPPPA). December 2025 amendments effective 1 Jan 2026 (KPMG Serbia, Dec 2025). |
| Tax authority | Poreska uprava -- Tax Administration of the Republic of Serbia (Ministry of Finance) |
| Filing portal | eTax / ePorezi (eporezi.purs.gov.rs); freelancer portal frilenseri.purs.gov.rs |
| Annual return deadline | 15 May following the income year -- 15 May 2026 for 2025 income (Poreska uprava; KPMG Feb 2026) |
| Validated by | Pending -- requires sign-off by a Serbian tax adviser / licensed accountant |
| Validation date | Pending |
| Skill version | 0.1 |

### Headline Income Tax Rates (2025 income year)

**Headline Income Tax Rates (2025 income year) table**  _(PwC; Eurofast; KPMG Dec 2025)_

| Income type | Rate | Base / notes | Source |
| --- | --- | --- | --- |
| Employment income (monthly withholding) | 10% flat | Gross salary minus non-taxable cap RSD 28,423/month (2025); RSD 34,221/month from 1 Jan 2026 | PwC; Eurofast; KPMG Dec 2025 |
| Self-employment / entrepreneur (actual income, bookkeeping) | 10% flat | On taxable profit | welcometoserbia.gov.rs |
| Self-employment / entrepreneur (flat-rate / paušalno) | 10% | Applied to a deemed lump-sum base set by the Tax Administration; effective tax is a fixed monthly amount; annual base growth capped at 10% through end 2027 | Poreska uprava; NALED |
| Capital gains | 15% | Resident exempt if asset held 10+ consecutive years | PwC income-determination |
| Investment income (dividends, interest, investment fund) | 15% | -- | PwC income-determination |
| Rental / real-estate income | 20% on 75% of gross (25% standard deduction), or on income after documented actual costs | -- | PwC income-determination; audere.rs |
| Royalty / copyright income | 20% | After standard cost deduction of 50%, 43% or 34% depending on royalty type | PwC income-determination |
| Other income | 20% (15% for insurance proceeds) | -- | PwC income-determination |

### Annual Supplementary Tax -- 2025 income (filed 2026)

Applies only if total net income exceeds **3x the average annual salary = RSD 5,439,096** (3 × RSD 1,813,032) (KPMG Feb 2026).

**Annual Supplementary Tax bands table**  _(KPMG Feb 2026)_

| Band | Net income (RSD) | Rate | Cumulative supplementary tax at top of band | Source |
| --- | --- | --- | --- | --- |
| Below threshold | 0 -- 5,439,096 | 0% (not subject to annual tax) | RSD 0 | KPMG Feb 2026 |
| Band 1 | 5,439,096 -- 10,878,192 | 10% | RSD 543,909.60 | KPMG Feb 2026 |
| Band 2 | above 10,878,192 | 15% | -- | KPMG Feb 2026 |

Band 1 width = 10,878,192 − 5,439,096 = RSD 5,439,096; at 10% that is RSD 543,909.60 of tax accumulated by the top of Band 1. PwC expresses Band 2 as "10% then +15% = effective 25% on the top band"; both descriptions are the same marginal 15% supplement layered on the 10% (PwC; KPMG Feb 2026). Personal/dependent deductions and youth relief (Section 1 below and Section 5.10) reduce the base before bands apply.

### Annual Tax Deductions (2025 income)

**Annual Tax Deductions table**  _(KPMG Feb 2026)_

| Deduction | Value (RSD) | Source |
| --- | --- | --- |
| Average annual salary (basis for multiples) | 1,813,032 (implied from the 3x threshold of 5,439,096) | KPMG Feb 2026 |
| Taxpayer personal deduction (40% of avg annual salary) | 725,213 | KPMG Feb 2026 |
| Per-dependent deduction (15% of avg annual salary) | 271,955 per dependent | KPMG Feb 2026 |
| Cap on combined personal + dependent deductions | 50% of taxable income | KPMG Feb 2026 |
| Youth relief (taxpayer under 40 on last day of year) | Additional reduction of 5,439,096 (3x avg annual salary) against employment/self-employment/IP income | KPMG Feb 2026 |

### Social Security Contributions (2025)

**Social Security Contributions table**  _(PwC other-taxes)_

| Contribution | Employee | Employer | Total | Source |
| --- | --- | --- | --- | --- |
| Pension & disability (PIO) | 14% | 10% | 24% | PwC other-taxes; Orbitax |
| Health insurance | 5.15% | 5.15% | 10.3% | PwC other-taxes |
| Unemployment insurance | 0.75% | 0% (employee only) | 0.75% | PwC other-taxes; welcometoserbia.gov.rs |
| **TOTAL** | **19.90%** | **15.15%** | **35.05%** | PwC other-taxes |

Employee column check: 14% + 5.15% + 0.75% = **19.90%**. Employer column check: 10% + 5.15% + 0% = **15.15%**. Total column check: 24% + 10.3% + 0.75% = **35.05%**, and 19.90% + 15.15% = **35.05%**. Self-employed entrepreneurs and freelancers pay **both** portions themselves: PIO 24% + health 10.3% + unemployment 0.75% = 35.05% (welcometoserbia.gov.rs).

**2025 contribution base limits** (reset annually on the published average gross salary): floor **RSD 45,950/month** (35% of average salary); ceiling **RSD 656,425/month** (5x average salary; **RSD 7,877,100/year**) (Orbitax; Eurofast).

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default | Source |
| --- | --- | --- |
| Residency unknown | Treat as resident (worldwide income); flag for reviewer | PwC residence |
| Period spans 2025/2026 | Use RSD 28,423 non-taxable cap for 2025 periods; RSD 34,221 only from 1 Jan 2026 | Eurofast; KPMG Dec 2025 |
| Social base limits, year unknown | Use 2025 floor RSD 45,950 / ceiling RSD 656,425; reset each year | Orbitax |
| Entrepreneur regime unknown | Default to actual-income (bookkeeping) 10%; flat-rate only if eligible and elected | Poreska uprava |
| Flat-rate eligibility unclear | Excluded if VAT-registered or turnover > RSD 6,000,000/yr | Poreska uprava; pausal.rs |
| Rental expense basis unknown | Apply 25% standard deduction (75% taxable at 20%) | audere.rs |
| Royalty cost-deduction class unknown | Use the lowest standard deduction (34%) until type confirmed | PwC income-determination |
| Freelancer model unknown | Compute both Model A and Model B; present the lower tax, flag for reviewer | frilenseri.purs.gov.rs |
| Capital-asset holding period unknown | Treat gain as taxable (no 10-year exemption) | PwC income-determination |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of taxpayer type (employee / entrepreneur-bookkeeping / entrepreneur-flat-rate / freelancer) and residency status (resident vs non-resident).

**Recommended** -- all sales invoices, purchase invoices/receipts, contribution payment records (PIO/health/unemployment), prior-year return or assessment, VAT (PDV) registration status, age (for youth relief and the under-40 annual-tax reduction), number of dependents.

**Ideal** -- complete income and expenditure ledger (entrepreneurs on bookkeeping), flat-rate decision (rešenje) from the Tax Administration (paušalci), freelancer quarterly self-taxation filings, employer PPP-PD records (employees), provisional/installment payment confirmations.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify all income is captured, that deductions are supported by valid documentation, and that the correct regime (employment / entrepreneur / freelancer) was applied."

### Refusal Catalogue

- **R-RS-1** — Taxpayer type unknown. "Serbia taxes employment, entrepreneur, and freelancer income under different rules and rates. This skill cannot compute tax without knowing the taxpayer type. Please confirm before proceeding."
- **R-RS-2** — Companies / legal persons. "This skill covers natural persons (employees, entrepreneurs, freelancers) only. Corporate income tax (porez na dobit pravnih lica) for d.o.o./a.d. companies is out of scope. Escalate to a Serbian tax adviser."
- **R-RS-3** — Non-resident / dual-resident. "Non-resident and dual-resident taxation (Serbian-source only) and tax-treaty relief require specialised analysis. Escalate to a Serbian tax adviser."
- **R-RS-4** — Flat-rate (paušalno) base determination. "The flat-rate monthly tax is a deemed amount set per-taxpayer by the Tax Administration based on activity, location, age and gender. This skill cannot derive that figure; obtain the official decision (rešenje). Escalate to a Serbian tax adviser." [RESEARCH GAP -- the per-taxpayer flat-rate base cannot be reduced to a single national figure; reviewer to confirm from the rešenje.]
- **R-RS-5** — Arrears / enforcement. "Client has outstanding tax arrears or is subject to Tax Administration enforcement. Late-payment interest runs at the NBS reference rate + 10 percentage points and repeat violations can trigger an activity ban of 6 months to 3 years. Do not advise. Escalate to a Serbian tax adviser immediately."
- **R-RS-6** — VAT return requested. "This skill covers personal income tax only. For Serbian VAT (PDV), use the serbia-vat-return skill (if available) or escalate."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Serbian descriptions are often in Cyrillic or Latin script; match Latin transliterations. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns table**

| Pattern | Schedule / Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + UPLATA, PRENOS, PLAĆANJE, PAYMENT RECEIVED | Business income | Entrepreneur Box: business revenue | If VAT-registered, extract net (excl. 20% PDV) |
| HONORAR, NAKNADA, FEES, CONSULTANCY | Business income | Entrepreneur/freelancer revenue | Professional fees |
| AUTORSKI HONORAR, ROYALTY, COPYRIGHT | Royalty/copyright | Freelancer self-taxation (Model A/B) or royalty schedule | Income from abroad → freelancer self-taxation |
| STRIPE, PAYPAL, WISE, PAYONEER PAYOUT | Foreign-source income | Freelancer self-taxation (income from abroad) | Match to underlying invoices; quarterly self-tax |
| UPWORK, FIVERR, TOPTAL | Foreign-source income | Freelancer self-taxation | Net of platform commission |
| ZARADA, PLATA, SALARY, EMPLOYER [name] | Employment income | 10% withheld at source (PPP-PD) | Already taxed by employer; do not double-count |
| ZAKUP, KIRIJA, RENT RECEIVED | Rental income | 20% on 75% of gross or actual-cost basis | Real-estate income |
| KAMATA, INTEREST RECEIVED | Investment income | 15% | Interest income |
| DIVIDENDA, DIVIDEND | Investment income | 15% | Dividend income |
| POVRAĆAJ POREZA, TAX REFUND | EXCLUDE | Not income | Refund from prior period |
| SUBVENCIJA, GRANT, DRŽAVNA POMOĆ | Check nature | EXCLUDE if capital grant; revenue grant = business income | Confirm nature with reviewer |

### 3.2 Expense Patterns (Debits) -- Deductible Business Expenses (entrepreneur bookkeeping)

**3.2 Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ZAKUP KANCELARIJE, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| OSIGURANJE (poslovno), PROFESSIONAL INSURANCE | Business insurance | Deductible | Must be business-related |
| KNJIGOVODSTVO, RAČUNOVODSTVO, ACCOUNTANT, BOOKKEEPING | Accountancy fees | Deductible | -- |
| ADVOKAT, LAWYER, LEGAL, NOTAR | Legal/notary fees | Deductible | Must be business-related |
| KANCELARIJSKI MATERIJAL, OFFICE SUPPLIES | Office supplies | Deductible | -- |
| MARKETING, GOOGLE ADS, META ADS, REKLAMA | Marketing/advertising | Deductible | -- |
| OBUKA, KURS, SEMINAR, CONFERENCE | Training | Deductible | Must relate to current business |
| BANKARSKA PROVIZIJA, BANK FEE, NAKNADA | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing | Deductible | -- |
| DOMEN, HOSTING, AWS, CLOUDFLARE | IT infrastructure | Deductible | Capitalise if a long-life asset; otherwise expense |

### 3.3 Expense Patterns (Debits) -- SaaS / Software

**3.3 Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible | -- |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN | Software subscription | Deductible | -- |
| Perpetual software licence (long-life) | Capital item | Capitalise / depreciate | Flag for reviewer; [RESEARCH GAP -- statutory depreciation rates not in research data; reviewer to confirm] |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**3.4 Expense Patterns table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| EPS, ELEKTRODISTRIBUCIJA, STRUJA | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| VODOVOD, VODA | Water | T2 if home office | As above |
| SBB, YETTEL, A1, TELEKOM, MTS, INTERNET | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBILNI, MOBILE | Phone | T2 | Business-use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**3.5 Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR SERBIA, WIZZ AIR, RYANAIR, AVIO | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel | -- |
| TAXI, CARGO, BOLT, YANDEX | Local transport | Deductible if business purpose | -- |
| GORIVO, BENZIN, NIS, FUEL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING | Parking | T2 -- business % only | -- |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORAN, RUČAK, VEČERA, ENTERTAINMENT | Entertainment | NOT deductible | Private/representation; confirm statutory limit with reviewer |
| LIČNO, NAMIRNICE, SUPERMARKET, MAXI, IDEA | Personal expenses | NOT deductible | Private living costs |
| KAZNA, PENAL, FINE, PREKRŠAJ | Fines/penalties | NOT deductible | Public policy |
| POREZ, INCOME TAX, PIB UPLATA | Tax payments | NOT deductible | Income tax cannot reduce income |
| ISPLATA VLASNIKU, DRAWINGS, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Exclusions (Neither Income nor Expense)

**3.7 Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNI PRENOS, OWN ACCOUNT, IZMEĐU RAČUNA | EXCLUDE | Own-account transfer |
| OTPLATA KREDITA, LOAN REPAYMENT | EXCLUDE | Loan principal movement |
| DOPRINOSI, PIO, ZDRAVSTVO, NEZAPOSLENOST | Contributions schedule | Mandatory contributions -- handled separately, not a general expense line |
| PDV UPLATA, VAT PAYMENT | EXCLUDE | VAT liability payment, not expense |

### 3.8 Serbian Banks -- Statement Format Reference

**3.8 Serbian Banks table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banca Intesa | PRENOS, UPLATA, ISPLATA, NAKNADA | PDF/CSV; description in Cyrillic or Latin |
| OTP banka (ex-Société Générale) | TRANSFER, PLAĆANJE, PROVIZIJA | PDF/CSV |
| Raiffeisen banka | PRENOS, KARTICA, NAKNADA | PDF/CSV |
| NLB Komercijalna banka | UPLATA, ISPLATA, TROŠAK | PDF; larger retail base |
| UniCredit Bank Srbija | TRANSFER, CARD, FEE | PDF/CSV |
| Wise / Revolut (freelancers) | PAYMENT, TRANSFER, PAYOUT | CSV; multi-currency -- convert to RSD |

## Section 4 -- Worked Examples

### Example 1 -- Employment salary (2025 monthly withholding)

**Input line:**
`05/03/2025 ; INTESA UPLATA ; POSLODAVAC D.O.O. ; ZARADA FEB 2025 ; +107,992.30 ; RSD`

**Reasoning:**
Net salary received. Gross salary is RSD 150,000/month. 2025 non-taxable cap = RSD 28,423 (Eurofast; KPMG Dec 2025).
- PIT base = 150,000 − 28,423 = 121,577. PIT = 121,577 × 10% = **RSD 12,157.70**.
- Gross 150,000 is between floor 45,950 and ceiling 656,425, so contributions apply on full gross. Employee contributions = 150,000 × 19.90% = **RSD 29,850.00**.
- Net = 150,000 − 12,157.70 − 29,850.00 = **RSD 107,992.30**.

Check: 12,157.70 + 29,850.00 = 42,007.70; 150,000 − 42,007.70 = 107,992.30 ✓

**Classification:** Employment income, already taxed at source via PPP-PD. Net pay RSD 107,992.30. Do not re-tax.

### Example 2 -- Entrepreneur on bookkeeping (actual income, 10%)

**Input:** Sole entrepreneur, VAT-registered. Annual taxable profit (revenue net of PDV, less allowable expenses) = RSD 2,400,000.

**Reasoning:**
- Income tax = 2,400,000 × 10% = **RSD 240,000** (welcometoserbia.gov.rs).
- Entrepreneur pays full combined contributions on the contribution base (here using profit as the base, subject to the 2025 floor/ceiling): PIO 24% + health 10.3% + unemployment 0.75% = 35.05%. On RSD 2,400,000 = **RSD 841,200** (welcometoserbia.gov.rs). [RESEARCH GAP -- the precise contribution base for bookkeeping entrepreneurs (taxable profit vs an elected base, with floor/ceiling) should be confirmed by the reviewer.]

**Classification:** Income tax RSD 240,000; contributions ~RSD 841,200 (subject to base-determination check).

### Example 3 -- Freelancer self-taxation, Model A (quarterly)

**Input line (one quarter, income from abroad):**
`30/06/2025 ; WISE PAYOUT ; UPWORK ESCROW ; Q2 FREELANCE ; +600,000.00 ; RSD`

**Reasoning (Model A):** standardized quarterly deduction RSD 96,000; 20% tax on the excess; PIO 24% and health 10.3% on the same taxable base (Eurofast; frilenseri.purs.gov.rs).
- Taxable base = 600,000 − 96,000 = 504,000.
- Tax = 504,000 × 20% = **RSD 100,800**.
- PIO = 504,000 × 24% = **RSD 120,960**; health = 504,000 × 10.3% = **RSD 51,912**.
- Total Model A burden = 100,800 + 120,960 + 51,912 = **RSD 273,672**.

**Classification:** File the freelancer self-taxation return for Q2. (See Example 4 for the Model B comparison before choosing.)

### Example 4 -- Freelancer self-taxation, Model B (same quarter)

**Reasoning (Model B):** standardized quarterly deduction RSD 57,900 **plus** 34% of gross quarterly income; 10% tax; PIO 24% (minimum payment applies) and health 10.3% (Eurofast; frilenseri.purs.gov.rs).
- Deduction = 57,900 + (600,000 × 34%) = 57,900 + 204,000 = 261,900.
- Taxable base = 600,000 − 261,900 = 338,100.
- Tax = 338,100 × 10% = **RSD 33,810**.
- PIO = 338,100 × 24% = **RSD 81,144** (subject to a minimum-contribution floor); health = 338,100 × 10.3% = **RSD 34,824.30**.
- Total Model B burden (before any PIO minimum top-up) = 33,810 + 81,144 + 34,824.30 = **RSD 149,778.30**.

**Comparison:** For this quarter Model B (RSD 149,778.30) is cheaper than Model A (RSD 273,672), driven by the 34%-of-gross deduction. Default is to present the lower-tax model and flag for reviewer; Model B's PIO minimum-payment rule may raise the result. [RESEARCH GAP -- the Model B minimum PIO contribution amount is not in the research data; reviewer to confirm on frilenseri.purs.gov.rs.]

### Example 5 -- Rental income (real estate)

**Input line:**
`10/04/2025 ; OTP UPLATA ; ZAKUPAC ; ZAKUP STAN APR ; +80,000.00 ; RSD`

**Reasoning:** Rental income taxed at 20% on 75% of gross after the 25% standard deduction, unless documented actual costs are higher (PwC income-determination; audere.rs).
- Taxable = 80,000 × 75% = 60,000.
- Tax = 60,000 × 20% = **RSD 12,000**. Effective rate = 12,000 / 80,000 = 15%.

**Classification:** Rental income, RSD 12,000 tax for the month (standard-deduction basis).

### Example 6 -- Annual supplementary tax (2025 income, high earner)

**Input:** Resident, total net income for 2025 = RSD 12,000,000. Taxpayer is 45 (no youth relief). Claims only the personal deduction. No dependents.

**Reasoning (KPMG Feb 2026):**
- Threshold = RSD 5,439,096 (3x avg annual salary). Income exceeds it, so the annual tax applies.
- Personal deduction RSD 725,213 (cannot exceed 50% of taxable income; 725,213 < 6,000,000, so allowed in full). Taxable income for the annual tax = 12,000,000 − 725,213 = 11,274,787.
- Band 1 (5,439,096 → 10,878,192): width 5,439,096 × 10% = **RSD 543,909.60**.
- Band 2 (above 10,878,192): 11,274,787 − 10,878,192 = 396,595 × 15% = **RSD 59,489.25**.
- Annual supplementary tax = 543,909.60 + 59,489.25 = **RSD 603,398.85**.

Check: 543,909.60 + 59,489.25 = 603,398.85 ✓

**Classification:** File Form PP GPDG by 15 May 2026; supplementary tax due RSD 603,398.85 (in addition to tax already withheld during the year).

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency

- **Residency taxation basis** — Resident individuals are taxed on worldwide income; non-residents on Serbian-source income only. Default to resident and flag if uncertain.  _(PwC residence)_

### 5.2 Employment Income -- 10% Flat

- **Employment income taxation** — 10% flat PIT on gross salary minus the monthly non-taxable cap: RSD 28,423 for 2025, rising to RSD 34,221 from 1 Jan 2026 (CPI-indexed each 1 February). Withheld monthly at source by the employer and reported on PPP-PD with each salary payment.  _(PwC; Eurofast; KPMG Dec 2025)_

### 5.3 Social Security Contributions

- **Social Security Contributions rule** — Split: employee 19.90% (PIO 14% + health 5.15% + unemployment 0.75%) and employer 15.15% (PIO 10% + health 5.15%; no employer unemployment). Combined 35.05% of gross. 2025 base limits: floor RSD 45,950/month, ceiling RSD 656,425/month (RSD 7,877,100/year). Self-employed/entrepreneurs and freelancers pay the full 35.05% themselves.  _(PwC other-taxes; Orbitax; Eurofast; welcometoserbia.gov.rs)_

### 5.4 Entrepreneur Income Tax -- 10%

- **Entrepreneur income tax rule** — 10% on either actual taxable profit (bookkeeping) or a deemed flat-rate (paušalno) base set by the Tax Administration. Flat-rate base annual growth is capped at 10% through end 2027. Default to bookkeeping unless flat-rate is elected and the client qualifies.  _(Poreska uprava; NALED)_

### 5.5 Flat-Rate (Paušalac) Eligibility

- **Flat-rate eligibility rule** — Annual turnover must not exceed RSD 6,000,000 (calendar year) and must not exceed RSD 8,000,000 over a rolling 365 days; the entrepreneur cannot be VAT-registered. The actual monthly tax is a per-taxpayer deemed amount -- see R-RS-4.  _(pausal.rs; NALED)_

### 5.6 Freelancer Self-Taxation (copyright / income from abroad) -- quarterly

- **Freelancer self-taxation models** — Two models: **Model A:** standardized deduction RSD 96,000/quarter (RSD 32,000/month); 20% tax on the excess; PIO 24% and health 10.3% on the same base. **Model B:** standardized deduction RSD 57,900/quarter plus 34% of gross quarterly income; 10% tax; PIO 24% (minimum payment applies) and health 10.3%. Filed quarterly via the frilenseri portal (within 30 days of quarter end).  _(Eurofast; frilenseri.purs.gov.rs)_

### 5.7 Capital Gains and Investment Income

- **Capital gains and investment income rule** — Capital gains: 15% (resident exemption if the asset is held 10+ consecutive years). Dividends, interest and investment-fund income: 15%.  _(PwC income-determination)_

### 5.8 Rental, Royalty and Other Income

**5.8 Rental, Royalty and Other Income table**  _(PwC; audere.rs)_

| Income type | Rate | Base | Source |
| --- | --- | --- | --- |
| Rental / real estate | 20% | 75% of gross (25% standard deduction) or income after documented actual costs | PwC; audere.rs |
| Royalty / copyright | 20% | After standard cost deduction 50% / 43% / 34% by type | PwC income-determination |
| Other income | 20% | -- | PwC income-determination |
| Insurance proceeds | 15% | -- | PwC income-determination |

### 5.9 VAT (PDV) Interaction

- **VAT interaction rule** — VAT registration is mandatory above RSD 8,000,000 turnover over 12 months; standard rate 20%, reduced rate 10%. Flat-rate entrepreneurs cannot enter the VAT system. For VAT-registered entrepreneurs, report income net of PDV and exclude collected PDV from business income.  _(taxadvisorserbia.com)_

### 5.10 Annual Supplementary Tax

- **Annual supplementary tax rule** — For 2025 income, the annual tax applies only if total net income exceeds RSD 5,439,096 (3x avg annual salary of RSD 1,813,032). Band 1: 10% on income from 3x to 6x (5,439,096 → 10,878,192). Band 2: 15% on income above 6x (10,878,192). Personal deduction RSD 725,213 and per-dependent deduction RSD 271,955 (combined deductions capped at 50% of taxable income). Youth relief: taxpayers under 40 on the last day of the year get an additional RSD 5,439,096 reduction against employment/self-employment/IP income.  _(KPMG Feb 2026)_

### 5.11 Filing, Forms and Deadlines

**5.11 Filing, Forms and Deadlines table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| PP GPDG | Annual personal income tax return (supplementary annual tax); pre-filled on eTax/ePorezi, verified/corrected and submitted | 15 May following the income year (15 May 2026 for 2025); tax payable by the same date | Poreska uprava; KPMG Feb 2026 |
| PPP-PD | Aggregate withholding return for salaries (PIT + contributions), filed electronically with each salary payment | On/before the date of income payment | PwC tax-administration |
| PP OPO / freelancer self-taxation return | Self-assessed income tax + contributions on copyright/income from abroad, via frilenseri portal | Quarterly (within 30 days of quarter end) | frilenseri.purs.gov.rs |
| PPDG-1S / PPDG-1R | Annual entrepreneur returns -- flat-rate (1S) and actual-income/bookkeeping (1R) | Annual; self-employment income returns electronic-only from 2026 | KPMG Dec 2025 |

### 5.12 Minimum Wage (2025)

- **Minimum wage rule** — Minimum net wage: RSD 308/hour from 1 Jan 2025, raised to RSD 337/hour from 1 Oct 2025; monthly net depends on working hours (e.g. ~RSD 49,280 at 160h to ~RSD 56,672 at 184h, at RSD 308). Check: 308 × 160 = 49,280 ✓; 308 × 184 = 56,672 ✓.  _(WageIndicator; tsg.rs; advokatibeograd.rs)_

### 5.13 Penalties

**5.13 Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Failure to file | 20%-75% of tax determined in control; minimum RSD 400,000 (legal person) / RSD 80,000 (entrepreneur) | PwC; ekapija.com |
| Failure to pay | 10%-50% of tax determined in control; minimum RSD 250,000 (legal person) / RSD 50,000 (entrepreneur) | PwC income-determination |
| Late-payment interest | NBS reference rate + 10 percentage points per annum; deferred/installment-tax interest at NBS reference rate alone | ZPPPA |
| Repeat violations | Two offence charges within two years can trigger an activity ban of 6 months to 3 years (plus monetary penalty) | PwC income-determination |

[RESEARCH GAP -- specific monetary fines for individuals (non-entrepreneur natural persons) under the Law on Personal Income Tax are not in the research data; reviewer to confirm from the statute.]

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Choosing Freelancer Model A vs Model B

- Model B's 34%-of-gross deduction favours higher-revenue quarters; Model A's flat RSD 96,000 favours lower-revenue quarters.
- Model B carries a minimum PIO contribution; verify the current-quarter minimum before concluding which model is cheaper.
- **Conservative default:** compute both, present the lower total, flag for reviewer. Re-verify standardized amounts on frilenseri.purs.gov.rs before filing.

### 6.2 Entrepreneur Contribution Base

- The contribution base for bookkeeping entrepreneurs interacts with the floor (RSD 45,950) and ceiling (RSD 656,425).
- **Flag for reviewer:** confirm whether contributions are on taxable profit or an elected base, and whether the annual ceiling (RSD 7,877,100) applies.

### 6.3 Flat-Rate vs Bookkeeping Election

- Flat-rate is unavailable if VAT-registered or turnover exceeds RSD 6,000,000.
- The deemed monthly tax comes from the Tax Administration decision (rešenje), not from a formula.
- **Flag for reviewer:** confirm eligibility and obtain the rešenje.

### 6.4 Home Office / Mixed-Use Apportionment

- Only the business-use portion of electricity, water, internet and phone is deductible (entrepreneurs on bookkeeping).
- **Conservative default:** 0% until a documented basis is provided.

### 6.5 Vehicle Business Use

- Only the business-use percentage of fuel, maintenance and depreciation is deductible; requires a mileage log.
- **Conservative default:** 0% until a mileage log is provided.

### 6.6 Royalty Cost-Deduction Class

- Standard cost deduction is 50%, 43% or 34% depending on the royalty type.
- **Conservative default:** lowest deduction (34%) until type confirmed.

### 6.7 Capital-Asset Holding Period (capital gains)

- 10+ consecutive years of holding gives a resident exemption.
- **Flag for reviewer:** confirm acquisition date and continuous holding.

### 6.8 Annual-Tax Deduction Cap and Youth Relief

- Combined personal + dependent deductions are capped at 50% of taxable income.
- Youth relief requires the taxpayer to be under 40 on the last day of the year.
- **Flag for reviewer:** confirm age, dependents, and the 50% cap interaction.

## Section 7 -- Excel Working Paper Template

SERBIA PERSONAL INCOME TAX -- WORKING PAPER
Income Year: 2025
Client: ___________________________
Taxpayer type: Employee / Entrepreneur-bookkeeping / Entrepreneur-flat-rate / Freelancer
Residency: Resident / Non-resident
Age (under 40 on 31 Dec?): _______   Dependents: _______

A. EMPLOYMENT (monthly, if applicable)
  A1. Gross salary                               ___________
  A2. Less non-taxable cap (28,423 / 34,221)     ___________
  A3. PIT base (A1 - A2)                          ___________
  A4. PIT @ 10% (A3 x 10%)                        ___________
  A5. Employee contributions @ 19.90% on A1*      ___________
      (*subject to floor 45,950 / ceiling 656,425)
  A6. Net pay (A1 - A4 - A5)                       ___________

B. ENTREPRENEUR -- BOOKKEEPING (annual, if applicable)
  B1. Revenue (net of PDV)                        ___________
  B2. Less allowable expenses                     ___________
  B3. Taxable profit (B1 - B2)                    ___________
  B4. Income tax @ 10% (B3 x 10%)                 ___________
  B5. Contributions @ 35.05% on base*             ___________
      (*confirm base + ceiling 7,877,100/yr)

C. FREELANCER -- compute BOTH models (quarterly)
  Model A: deduction 96,000; base = gross - 96,000
    C1. Tax @ 20%                                 ___________
    C2. PIO @ 24% + health @ 10.3%                ___________
  Model B: deduction 57,900 + 34% of gross
    C3. Tax @ 10%                                 ___________
    C4. PIO @ 24% (min applies) + health @ 10.3%  ___________
  C5. Chosen model (lower total) -- FLAG          ___________

D. SCHEDULER INCOME (if applicable)
  D1. Capital gains @ 15%                          ___________
  D2. Dividends/interest/fund @ 15%                ___________
  D3. Rental @ 20% on 75% of gross                 ___________
  D4. Royalty @ 20% after 50/43/34% deduction      ___________
  D5. Other @ 20% (insurance 15%)                  ___________

E. ANNUAL SUPPLEMENTARY TAX (PP GPDG, if net income > 5,439,096)
  E1. Total net income                            ___________
  E2. Less personal deduction (725,213)           ___________
  E3. Less dependents (271,955 each)              ___________
      (E2+E3 capped at 50% of taxable income)
  E4. Less youth relief (5,439,096 if under 40)   ___________
  E5. Taxable base                                ___________
  E6. Band 1 @ 10% (5,439,096 -> 10,878,192)      ___________
  E7. Band 2 @ 15% (above 10,878,192)             ___________
  E8. Annual supplementary tax (E6 + E7)          ___________

REVIEWER FLAGS:
  [ ] Taxpayer type confirmed?
  [ ] Residency confirmed?
  [ ] Correct non-taxable cap for period (2025 vs 2026)?
  [ ] Contribution base + floor/ceiling confirmed?
  [ ] Freelancer model chosen + Model B PIO minimum checked?
  [ ] Flat-rate rešenje obtained (if paušalac)?
  [ ] Royalty cost-deduction class confirmed?
  [ ] Annual-tax 50% deduction cap + youth relief checked?

## Section 8 -- Bank Statement Reading Guide

### Serbian Bank Statement Formats

**Serbian Bank Statement Formats**  _(Section 8)_

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banca Intesa | PDF, CSV | Datum, Opis, Zaduženje, Odobrenje, Stanje | Most common; description holds counterparty + reference |
| OTP banka | PDF, CSV | Datum valute, Opis, Iznos, Stanje | Card transactions show merchant |
| Raiffeisen banka | PDF, CSV | Datum, Opis transakcije, Iznos | -- |
| NLB Komercijalna | PDF | Datum, Opis, Isplata, Uplata | Large retail base; Cyrillic common |
| UniCredit Srbija | PDF, CSV | Value Date, Description, Amount | Mixed Latin/Cyrillic |
| Wise / Revolut | CSV | Date, Counterparty, Amount, Currency | Freelancers; convert FX to RSD |

### Key Serbian Banking / Tax Terms

**Key Serbian Banking / Tax Terms**  _(Section 8)_

| Term | English | Classification Hint |
| --- | --- | --- |
| UPLATA | Credit / deposit (in) | Potential income |
| ISPLATA | Payment / withdrawal (out) | Expense -- check counterparty |
| PRENOS / TRANSFER | Transfer | Check direction; may be own-account |
| ZARADA / PLATA | Salary | Employment income (already withheld) |
| HONORAR / NAKNADA | Fee / honorarium | Business or freelancer income |
| AUTORSKI HONORAR | Author's/copyright fee | Royalty / freelancer self-taxation |
| ZAKUP / KIRIJA | Rent | Rental income or office-rent expense |
| KAMATA | Interest | Investment income (15%) |
| DIVIDENDA | Dividend | Investment income (15%) |
| DOPRINOSI / PIO | Contributions / pension | Mandatory contributions schedule |
| PROVIZIJA / NAKNADA (banke) | Bank fee/commission | Deductible (business account) |
| POREZ | Tax | Tax payment -- not deductible |
| KAZNA / PREKRŠAJ | Fine / offence | Not deductible |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

ONBOARDING QUESTIONS -- SERBIA PERSONAL INCOME TAX
1. Taxpayer type: employee, entrepreneur on bookkeeping, flat-rate entrepreneur (paušalac), or freelancer?
2. Residency: Serbian tax resident (worldwide income) or non-resident (Serbian-source only)?
3. Period: does any income fall on/after 1 Jan 2026 (different non-taxable cap)?
4. VAT (PDV): are you registered? Turnover over the last 12 months?
5. Age: were you under 40 on 31 December of the income year? (youth relief / annual-tax reduction)
6. Dependents: how many?
7. If flat-rate: do you have the Tax Administration decision (rešenje) with your monthly amount?
8. If freelancer: which self-taxation model (A or B) and what is gross income per quarter?
9. Other income: rental, dividends, interest, royalties, capital gains?
10. Contributions: amounts of PIO / health / unemployment paid in the year?

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References**  _(Section 10)_

| Topic | Reference | Source |
| --- | --- | --- |
| Personal income tax | Law on Personal Income Tax (Zakon o porezu na dohodak građana) | PwC |
| Social contributions | Law on Mandatory Social Insurance Contributions | PwC other-taxes |
| Procedure & penalties | Law on Tax Procedure and Tax Administration (ZPPPA) | ZPPPA (English) |
| 2026 amendments | Dec 2025 amendments effective 1 Jan 2026 | KPMG Serbia (Dec 2025) |
| Tax authority | Poreska uprava (purs.gov.rs); eTax/ePorezi (eporezi.purs.gov.rs); frilenseri.purs.gov.rs | Poreska uprava |

### 2025 vs 2026 Boundary -- Important

**2025 vs 2026 Boundary -- Important**  _(Section 10)_

| Item | 2025 | From 1 Jan 2026 | Source |
| --- | --- | --- | --- |
| Non-taxable monthly salary cap | RSD 28,423 | RSD 34,221 | Eurofast; KPMG Dec 2025 |
| Social base floor | RSD 45,950 | Resets on new average salary [confirm] | Orbitax |
| Social base ceiling | RSD 656,425 | Resets on new average salary [confirm] | Orbitax |
| Self-employment returns | Paper/electronic | Electronic-only | KPMG Dec 2025 |

### 2025 vs 2026 Boundary -- Important

[RESEARCH GAP -- 2026 social base floor/ceiling and the 2026 average annual salary for the annual tax are not in the research data; confirm the current-year figures with the Tax Administration before computing 2026 payroll or the 2026 annual return.]

### Test Suite

### Test 1 -- Employment net pay (2025).

Input: Gross salary RSD 150,000/month, single employee, 2025.
Expected: PIT base = 121,577; PIT = RSD 12,157.70; employee contributions = RSD 29,850.00; net = RSD 107,992.30.

### Test 2 -- Entrepreneur bookkeeping tax.

Input: Taxable profit RSD 2,400,000.
Expected: Income tax = RSD 240,000 (10%). Contributions ~RSD 841,200 at 35.05% (subject to base check).

### Test 3 -- Freelancer Model A (one quarter).

Input: Gross quarterly income RSD 600,000.
Expected: Base = 504,000; tax = RSD 100,800 (20%); PIO = RSD 120,960 (24%); health = RSD 51,912 (10.3%); total = RSD 273,672.

### Test 4 -- Freelancer Model B (same quarter).

Input: Gross quarterly income RSD 600,000.
Expected: Deduction = 261,900; base = 338,100; tax = RSD 33,810 (10%); PIO = RSD 81,144 (before min); health = RSD 34,824.30; total = RSD 149,778.30 (before any PIO minimum top-up). Model B is cheaper than Model A here.

### Test 5 -- Rental income.

Input: Monthly rent RSD 80,000, standard deduction.
Expected: Taxable 60,000 (75%); tax = RSD 12,000 (20%); effective 15%.

### Test 6 -- Annual supplementary tax (2025).

Input: Total net income RSD 12,000,000; age 45; personal deduction only; no dependents.
Expected: Taxable base = 11,274,787; Band 1 = RSD 543,909.60; Band 2 = RSD 59,489.25; annual tax = RSD 603,398.85.

### Test 7 -- Below annual-tax threshold.

Input: Total net income RSD 5,000,000.
Expected: Below RSD 5,439,096 threshold -- no annual supplementary tax; PP GPDG not required on this basis.

### Test 8 -- Flat-rate ineligible (turnover).

Input: Entrepreneur turnover RSD 7,000,000/year.
Expected: Exceeds RSD 6,000,000 -- flat-rate unavailable; bookkeeping at 10% applies; also approaching the RSD 8,000,000 VAT threshold.

## PROHIBITIONS

- NEVER compute tax without confirming the taxpayer type (employee / entrepreneur / freelancer)
- NEVER apply the RSD 34,221 non-taxable cap to 2025 periods -- use RSD 28,423 through 2025
- NEVER invent the flat-rate (paušalno) monthly amount -- it comes from the Tax Administration rešenje
- NEVER tax employment income twice -- salary received net is already withheld via PPP-PD
- NEVER omit the Model B minimum PIO contribution check before declaring it the cheaper model
- NEVER include collected PDV (VAT) in business income for VAT-registered entrepreneurs
- NEVER apply contributions above the ceiling (RSD 656,425/month; RSD 7,877,100/year for 2025)
- NEVER allow income tax, fines, or personal expenses as deductions
- NEVER ignore the 50% cap on combined personal + dependent annual-tax deductions
- NEVER present tax calculations as definitive -- always label as estimated and pending reviewer sign-off

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
