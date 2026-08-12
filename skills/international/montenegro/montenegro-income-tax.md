---
name: montenegro-income-tax
description: Use this skill whenever asked about Montenegro personal income tax (porez na dohodak fizičkih lica) for self-employed individuals, sole proprietors (preduzetnik), and employees. Trigger on phrases like "how much tax do I pay in Montenegro", "Montenegro income tax", "GPP-FL", "IOPPD", "prirez", "municipal surtax", "Europe Now", "Evropa sad", "self-employed tax Montenegro", "Montenegro payroll", "pension contribution Montenegro", "PIO", "Montenegro net salary", or any question about computing or filing personal income tax, payroll withholding, or social contributions for an individual or sole proprietor in Montenegro. Also trigger when preparing or reviewing a GPP-FL annual return or an IOPPD monthly payroll report, computing employee/employer social contributions, or advising on the progressive 0/9/15% rate structure and the 13/15% municipal surtax. This skill covers PIT rate bands (employment monthly vs self-employment annual), the post-Europe-Now-2 contribution structure, municipal surtax, residency, VAT registration threshold, forms, and deadlines. ALWAYS read this skill before touching any Montenegro income tax work.
version: 0.1
jurisdiction: ME
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro Personal Income Tax -- Self-Employed

## Montenegro Personal Income Tax -- Self-Employed Skill v0.1

> **Tier 2 (research-verified).** Figures below are drawn from PwC Worldwide Tax Summaries (reviewed 27 March 2026), KPMG Montenegro, and Orbitax. They have NOT yet been signed off by a Montenegrin licensed accountant. Treat every computed liability as an estimate pending professional review.

## Section 1 -- Quick Reference

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Montenegro (Crna Gora) — ISO 3166-1 alpha-2: ME |
| Tax | Personal Income Tax (porez na dohodak fizičkih lica) |
| Currency | EUR only (Montenegro uses the euro unilaterally) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Law on Personal Income Tax (Zakon o porezu na dohodak fizičkih lica) |
| Supporting legislation | Law on Contributions for Mandatory Social Insurance (Zakon o doprinosima za obavezno socijalno osiguranje); Law on Local Self-Government Financing (surtax/prirez); Law on Tax Administration (Zakon o poreskoj administraciji) |
| Reform context | "Europe Now" (Evropa sad) effective 1 Jan 2022; "Europe Now 2" effective 1 Oct 2024 |
| Tax authority | Revenue and Customs Administration of Montenegro (Uprava prihoda i carina Crne Gore) |
| Social insurance | Same Revenue and Customs Administration; Pension & Disability Insurance Fund (Fond PIO); Employment Bureau |
| Filing portal | eprijava.tax.gov.me / www.poreskauprava.gov.me |
| Annual return deadline | 30 April of the following year (Form GPP-FL) |
| Monthly payroll report deadline | 15th of the following month (Form IOPPD) |
| Validated by | Pending — requires sign-off by a Montenegrin licensed accountant |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rate Brackets (2025; rates unchanged into 2026 per PwC review 27 March 2026)

- **Two different bases** — Employment (salary) brackets are applied per MONTH on gross salary. Self-employment / business (entrepreneur) brackets are applied per YEAR on annual income. Do not mix the two thresholds.  _(PwC)_

**Employment Income — MONTHLY gross salary**  _(PwC, reviewed 27 Mar 2026)_

| Monthly Gross (EUR) | Rate | Cumulative Tax at Top of Band |
| --- | --- | --- |
| 0 -- 700.00 | 0% | EUR 0.00 |
| 700.01 -- 1,000.00 | 9% | EUR 27.00 |
| 1,000.01+ | 15% | -- |

> Check: at EUR 1,000 gross, PIT = (1,000 − 700) × 9% = EUR 27.00. At EUR 1,500 gross, PIT = 27.00 + (1,500 − 1,000) × 15% = 27.00 + 75.00 = **EUR 102.00**.

**Self-Employment / Business (Entrepreneur) Income — ANNUAL**  _(PwC, reviewed 27 Mar 2026)_

| Annual Income (EUR) | Rate | Cumulative Tax at Top of Band |
| --- | --- | --- |
| 0 -- 8,400.00 | 0% | EUR 0.00 |
| 8,400.01 -- 12,000.00 | 9% | EUR 324.00 |
| 12,000.01+ | 15% | -- |

> Check: at EUR 12,000 annual, PIT = (12,000 − 8,400) × 9% = EUR 324.00. At EUR 20,000 annual, PIT = 324.00 + (20,000 − 12,000) × 15% = 324.00 + 1,200.00 = **EUR 1,524.00**.

**Other Income — flat 15%**  _(PwC, reviewed 27 Mar 2026)_

| Income Type | Rate |
| --- | --- |
| Rental (property) income | 15% flat |
| Dividends | 15% flat |
| Interest | 15% flat |
| Royalties | 15% flat |
| Capital gains | 15% flat |

**Gaming / Gambling Winnings — progressive**  _(PwC, reviewed 27 Mar 2026)_

| Winnings (EUR) | Rate | Cumulative Tax at Top of Band |
| --- | --- | --- |
| 0 -- 50.00 | 0% | EUR 0.00 |
| 50.01 -- 1,500.00 | 10% | EUR 145.00 |
| 1,500.01+ | 15% | -- |

> Check: at EUR 1,500 winnings, tax = (1,500 − 50) × 10% = EUR 145.00.

### Municipal Surtax (Prirez)

- **Surtax basis** — The municipal surtax is levied ON the PIT amount assessed, NOT on income. It is a tax-on-tax.  _(PwC)_

**Municipal Surtax Rate Table**

| Municipality | Surtax Rate (of PIT due) |
| --- | --- |
| Podgorica | 15% |
| Cetinje | 15% |
| All other municipalities | 13% |

> Effective top marginal rate in Podgorica/Cetinje = 15% PIT × 1.15 = **17.25%**. In other municipalities = 15% × 1.13 = **16.95%**.

### Social Contributions (post-Europe-Now-2, effective 1 October 2024) (PwC)

**Social Contributions Table**  _(PwC)_

| Contribution | Employee | Employer | Total |
| --- | --- | --- | --- |
| Pension & disability insurance (PIO) | 10.0% | 0.0% | 10.0% |
| Unemployment insurance | 0.5% | 0.5% | 1.0% |
| Health insurance | 0.0% (abolished 1 Jan 2022) | 0.0% (abolished 1 Jan 2022) | 0.0% |
| **TOTAL** | **10.5%** | **0.5%** | **11.0%** |

> Column check — Employee: 10.0 + 0.5 + 0.0 = **10.5%**. Employer: 0.0 + 0.5 + 0.0 = **0.5%**. Total: 10.0 + 1.0 + 0.0 = **11.0%** (= 10.5 + 0.5). Confirmed.

- **Employer pension abolition** — Employer share of pension/disability was abolished from 1 October 2024 under Europe Now 2.  _(PwC)_
- **Health contribution abolition** — Compulsory health insurance contributions were abolished from 1 January 2022 under Europe Now 1 (previously 8.5% employee + 2.3% employer = 10.8%); health is now funded from general taxation.  _(Orbitax/KPMG)_
- **Pension/disability contribution ceiling** — EUR 68,765 EUR (2024 figure, indexed by PIO Fund; [RESEARCH GAP — reviewer to confirm the 2025/2026 indexed ceiling with the PIO Fund.])  _(PwC)_

### Conservative Defaults

**Conservative Defaults Table**

| Ambiguity | Default |
| --- | --- |
| Unknown contribution structure / vintage | Use post-Europe-Now-2 (Oct 2024): employee 10.5%, employer 0.5%, no health contribution |
| Surtax basis | Apply surtax to the PIT amount, never to income |
| Unknown municipality | 13% surtax (the most common rate); flag for reviewer |
| Salary vs self-employment band confusion | Salary = monthly bands; self-employment = annual bands |
| Unknown residency | STOP — do not determine worldwide vs source taxation without residency |
| Unknown expense category | Not deductible |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Pre-reform contribution rates seen in a source | Treat as STALE — do not use |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — For an employee: monthly gross salary and the municipality of employment. For a sole proprietor (preduzetnik): bank statement for the full tax year (CSV, PDF, or pasted text) plus the municipality and confirmation of residency.
- **Recommended** — All sales/purchase invoices, IOPPD monthly reports filed during the year, prior-year GPP-FL return, VAT registration status, confirmation of which Europe-Now contribution vintage applies to the period.
- **Ideal** — Complete income and expenditure account, asset register, contribution-base records (for the EUR 68,765 ceiling check), proof of any other income (rental, dividends, interest), and confirmation of centre-of-interests for residency.
- **Refusal if minimum is missing** — SOFT WARN. No bank statement (for a sole proprietor) at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the business-purpose test is met."

### Refusal Catalogue

- **R-ME-1 -- Municipality unknown** — The municipal surtax (prirez) is 13% in most municipalities but 15% in Podgorica and Cetinje. This skill will default to 13% and flag it, but please confirm the municipality before finalising.
- **R-ME-2 -- Companies / corporate income tax** — This skill covers personal income tax for individuals and sole proprietors only. Corporate income tax (porez na dobit) on companies (d.o.o., a.d.) is a separate regime. Escalate to a Montenegrin licensed accountant.
- **R-ME-3 -- Non-resident / cross-border income** — Non-resident and dual-resident taxation, treaty relief, and foreign-source income require specialised analysis. Residents are taxed on worldwide income; non-residents on Montenegro-source income only. Out of scope. Escalate to a licensed accountant.
- **R-ME-4 -- Pension/disability ceiling cases** — Income above the annual contribution base ceiling (EUR 68,765, 2024 figure) requires the indexed current-year ceiling, which must be confirmed with the PIO Fund. Escalate to a licensed accountant before relying on a capped figure.
- **R-ME-5 -- Arrears / enforcement** — Client has outstanding tax/contribution arrears or is subject to Revenue and Customs Administration enforcement. Default interest and misdemeanor fines apply and exact amounts could not be confirmed in research. Do not advise. Escalate to a licensed accountant immediately.
- **R-ME-6 -- VAT return requested** — This skill covers personal income tax and payroll withholding only. Montenegro VAT (PDV, standard 21%) is a separate skill/regime.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier for a sole proprietor (preduzetnik) bank statement. When a transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. Montenegrin (Crna Gora) statement text mixes Montenegrin/Serbian and English. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns Table**

| Pattern | Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + UPLATA, DOZNAKA, PRENOS, PAYMENT RECEIVED | Business income (annual SE band) | Business income | If VAT-registered (21%), extract net (excl. VAT) |
| HONORAR, NAKNADA, FEES, CONSULTANCY | Business income | Business income | Professional fees — typical for sole proprietor |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Business income | Platform payout — match to invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Business income | Business income | Platform payout — verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Business income | Business income | International platform payout |
| UPWORK, FIVERR, TOPTAL | Business income | Business income | Freelance platform — net of platform commission |
| ZARADA, PLATA, SALARY, EMPLOYER [name] | Employment income (monthly band) | Employment income | NOT self-employment — taxed on monthly salary bands |
| ZAKUP, KIRIJA, RENT RECEIVED | Other income (flat 15%) | Rental income | Flat 15%, not the SE band |
| KAMATA, INTEREST RECEIVED | Other income (flat 15%) | Investment income | Interest income, flat 15% |
| DIVIDENDA, DIVIDEND | Other income (flat 15%) | Investment income | Dividend income, flat 15% |
| POVRAĆAJ POREZA, TAX REFUND | EXCLUDE | Not income | Prior-year tax refund |
| SUBVENCIJA, GRANT, DRŽAVNA POMOĆ | Check nature | Check nature | Capital grants EXCLUDE; revenue grants = business income |

### 3.2 Expense Patterns (Debits) -- Fully Deductible

**Fully Deductible Expenses Table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ZAKUP KANCELARIJE, OFFICE RENT, POSLOVNI PROSTOR | Office rent | Deductible | Dedicated business premises |
| OSIGURANJE, PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible | Business-related |
| RAČUNOVOĐA, ACCOUNTANT, KNJIGOVODSTVO, REVIZOR | Accountancy fees | Deductible |  |
| ADVOKAT, LAWYER, PRAVNE USLUGE, NOTAR | Legal fees | Deductible | Must be business-related |
| KANCELARIJSKI MATERIJAL, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, REKLAMA | Marketing/advertising | Deductible |  |
| OBUKA, TRAINING, SEMINAR, KONFERENCIJA | Training/CPD | Deductible | Must relate to current business |
| BANKARSKA NAKNADA, BANK FEE, PROVIZIJA | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| POŠTARINA, POSTAGE, POŠTA CRNE GORE | Postage | Deductible | Business correspondence |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN | IT infrastructure | Deductible | If recurring service |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software Expenses Table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| Perpetual software licence (high value) | Capital item | Capitalise/depreciate | Flag for reviewer — depreciation rate is a T2 item |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities Expenses Table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ELEKTROPRIVREDA, EPCG, STRUJA | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| VODOVOD, WATER | Water | T2 if home office | Business portion only |
| CRNOGORSKI TELEKOM, M:TEL, ONE, TELENOR | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| MOBILNI, MOBILE | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel Expenses Table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR MONTENEGRO, RYANAIR, WIZZ AIR, AVIO KARTA | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB, SMJEŠTAJ | Accommodation | Deductible if business travel |  |
| TAKSI, TAXI, BOLT | Local transport | Deductible if business purpose |  |
| GORIVO, BENZIN, FUEL, JUGOPETROL | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARKING, PARKIRANJE | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**Not Deductible Expenses Table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORAN, RUČAK, VEČERA, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private/entertainment — flag, do not deduct |
| LIČNO, NAMIRNICE, SUPERMARKET, MARKET | Personal expenses | NOT deductible | Private living costs |
| KAZNA, PENALTY, MANDATNA KAZNA, PARKING FINE | Fines/penalties | NOT deductible | Public policy |
| POREZ, INCOME TAX, TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| ISPLATA VLASNIKU, DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items

**Capital Items Table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, RAČUNAR | Computer hardware | Capitalise/depreciate | Annual depreciation rate is a T2 item — flag for reviewer |
| ŠTAMPAČ, PRINTER, SKENER | Office equipment | Capitalise/depreciate | Flag for reviewer |
| NAMJEŠTAJ, FURNITURE, STO, STOLICA | Furniture/fittings | Capitalise/depreciate | Flag for reviewer |
| VOZILO, AUTOMOBIL, CAR (business) | Motor vehicle | Capitalise/depreciate | Business % only; flag for reviewer |

> [RESEARCH GAP — reviewer to confirm] Statutory tax-depreciation rates for sole-proprietor assets under Montenegrin PIT/CIT rules were not confirmed from an authoritative source in this research pass. Do not apply a depreciation percentage without reviewer confirmation.

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions Table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNI PRENOS, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| OTPLATA KREDITA, LOAN REPAYMENT, KREDIT | EXCLUDE | Loan principal movement |
| DOPRINOSI, PIO, SOCIAL CONTRIBUTION | Contributions line | Social contributions — track separately, not a business cost line for an employee |
| PDV, VAT PAYMENT | EXCLUDE | VAT liability payment, not expense |

### 3.9 Montenegrin Banks -- Statement Format Reference

**Statement Format Reference Table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| CKB (Crnogorska komercijalna banka) | UPLATA, ISPLATA, PRENOS, NAKNADA | PDF/CSV; date format DD.MM.YYYY |
| NLB Banka | DOZNAKA, TRAJNI NALOG, KARTICA | PDF/CSV; counterparty in description |
| Erste Bank Montenegro | PRENOS, DIREKTNO ZADUŽENJE, PROVIZIJA | PDF; CSV export available |
| Hipotekarna banka | UPLATA, ISPLATA, NAKNADA | PDF |
| Universal Capital Bank | TRANSFER, PAYMENT, FEE | CSV; cleaner counterparty names |

## Section 4 -- Worked Examples

### Example 1 -- Employee Monthly Salary, Podgorica (above 0% band)

**Input line:**
`31/03/2025 ; CKB UPLATA ; POSLODAVAC DOO ; ZARADA MART 2025 ; +1,200.00 ; EUR`

**Reasoning:**
Employment income, EUR 1,200 gross/month, employed in Podgorica (15% surtax).

- PIT: 0% on first 700 = 0.00; 9% on (1,000 − 700 = 300) = 27.00; 15% on (1,200 − 1,000 = 200) = 30.00. PIT = 27.00 + 30.00 = **EUR 57.00**.
- Surtax (Podgorica 15% of PIT): 57.00 × 15% = **EUR 8.55**.
- Employee social contributions: 1,200 × 10.5% = **EUR 126.00**.
- Net pay = 1,200.00 − 57.00 − 8.55 − 126.00 = **EUR 1,008.45**.

**Classification:** Employment income, monthly bands. Net pay EUR 1,008.45.

### Example 2 -- Employee at the 0% Threshold (minimum-wage band)

**Input line:**
`30/04/2025 ; NLB DOZNAKA ; POSLODAVAC DOO ; ZARADA APRIL ; +700.00 ; EUR`

**Reasoning:**
Gross EUR 700/month falls entirely within the 0% PIT band (PwC: first EUR 700 taxed at 0%).

- PIT = **EUR 0.00**. Surtax = 0% of 0 = **EUR 0.00**.
- Employee social contributions: 700 × 10.5% = **EUR 73.50**.
- Net pay = 700.00 − 0.00 − 73.50 = **EUR 626.50**.

**Classification:** Employment income, fully within the 0% band. Only social contributions apply.

### Example 3 -- Sole Proprietor Annual Profit (other municipality, 13% surtax)

**Input:** Annual business income EUR 20,000; allowable expenses already netted; municipality with 13% surtax.

**Reasoning (self-employment ANNUAL bands):**
- PIT: 0% on first 8,400 = 0.00; 9% on (12,000 − 8,400 = 3,600) = 324.00; 15% on (20,000 − 12,000 = 8,000) = 1,200.00. PIT = 324.00 + 1,200.00 = **EUR 1,524.00**.
- Surtax (13% of PIT): 1,524.00 × 13% = **EUR 198.12**.
- Total PIT + surtax = 1,524.00 + 198.12 = **EUR 1,722.12**.

**Classification:** Self-employment income, annual bands. Total PIT + surtax EUR 1,722.12 (contributions computed separately — see Tier 1).

### Example 4 -- Rental Income (flat 15%)

**Input line:**
`05/02/2025 ; ERSTE PRENOS ; ZAKUPAC ; ZAKUP STANA FEB ; +500.00 ; EUR`

**Reasoning:**
Rental income is taxed at a flat 15% (PwC), not on the progressive SE bands. (Any statutory standardised cost deduction against rental income is a reviewer item.)

- PIT on gross 500: 500 × 15% = **EUR 75.00** (before any allowable cost deduction — flag for reviewer).

**Classification:** Other income, flat 15%. [RESEARCH GAP — reviewer to confirm] whether a standardised expense allowance reduces the rental base.

### Example 5 -- Software Subscription (Deductible)

**Input line:**
`01/04/2025 ; CKB KARTICA ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD APR ; -29.99 ; EUR`

**Reasoning:**
Monthly SaaS subscription, recurring, business use. Fully deductible as an operating expense against business income. For VAT-registered sole proprietors, the net (excl. recoverable 21% VAT) is the expense.

**Classification:** Deductible business expense EUR 29.99 (or net of recoverable VAT if VAT-registered).

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`15/05/2025 ; CKB INTERNI PRENOS ; SOPSTVENI RAČUN - ŠTEDNJA ; ; -2,000.00 ; EUR`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Employment Income — Monthly Progressive PIT

- **Employment monthly PIT rule** — Salary is taxed monthly: 0% on the first EUR 700 gross, 9% on EUR 700.01–1,000, 15% above EUR 1,000. The employer withholds PIT and employee contributions and remits monthly (PAYE-style). The 0% band on the first EUR 700 means most minimum-wage and low earners pay no PIT.  _(Law on Personal Income Tax (Zakon o porezu na dohodak fizičkih lica); PwC, reviewed 27 Mar 2026)_

### 5.2 Self-Employment / Business Income — Annual Progressive PIT

- **Self-employment annual PIT rule** — Entrepreneur (preduzetnik) income is taxed annually: 0% up to EUR 8,400, 9% on EUR 8,400.01–12,000, 15% above EUR 12,000. Apply to net annual business income after allowable expenses.  _(Law on Personal Income Tax; PwC)_

> [RESEARCH GAP — reviewer to confirm] Whether the EUR 700 monthly 0% band is also reflected proportionally in self-employment computations versus the EUR 8,400 annual band should be confirmed by the accountant reviewer.

### 5.3 Other Income — Flat 15%

- **Other income flat rate** — Rental, dividend, interest, royalty, and capital-gains income are taxed at a flat 15%. These do not use the progressive bands.  _(PwC)_

### 5.4 Gaming / Gambling Winnings — Progressive

- **Gaming winnings progressive rate** — 0% up to EUR 50, 10% on EUR 50.01–1,500, 15% above EUR 1,500.  _(PwC)_

### 5.5 Municipal Surtax (Prirez)

- **Surtax computation rule** — Surtax is charged ON the PIT amount: 13% in most municipalities, 15% in Podgorica and Cetinje. It is a tax-on-tax — never add it to the income rate. Effective top marginal = 17.25% (Podgorica/Cetinje) or 16.95% (other municipalities).  _(Law on Local Self-Government Financing; PwC)_

### 5.6 Social Contributions

**Social Contributions Table**  _(Law on Contributions for Mandatory Social Insurance)_

| Item | Employee | Employer |
| --- | --- | --- |
| Pension & disability (PIO) | 10.0% | 0.0% (abolished Oct 2024) |
| Unemployment | 0.5% | 0.5% |
| Health | 0.0% (abolished Jan 2022) | 0.0% (abolished Jan 2022) |
| **Total** | **10.5%** | **0.5%** |

- **Pension/disability contribution ceiling** — EUR 68,765 EUR (2024 figure, indexed by PIO Fund; [RESEARCH GAP — reviewer to confirm the 2025/2026 indexed ceiling with the PIO Fund.])  _(PwC)_

> A possible employer "labor fund" / professional-rehabilitation-of-disabled-persons levy and chamber/union contributions appear in some guides but were NOT confirmed on PwC for the current period. [RESEARCH GAP — reviewer to confirm with the Revenue and Customs Administration before relying on them.]

### 5.7 Payroll Burden Summary

- **Employer total payroll burden** — Only 0.5% unemployment insurance on top of gross salary (pension/disability and health employer shares abolished).  _(PwC)_
- **Employee total deductions** — 10.5% social contributions + progressive PIT (0/9/15%) + municipal surtax on the PIT amount.  _(PwC)_

### 5.8 Non-Deductible Expenses (Sole Proprietors)

**Non-Deductible Expenses Table**

| Expense | Reason |
| --- | --- |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Drawings / owner withdrawals | Not an expense |
| Private-portion of mixed-use costs | Only business portion deductible |

### 5.9 VAT Interaction

- **Standard VAT (PDV) rate** — 21%  _(PwC)_
- **Mandatory VAT registration threshold** — EUR 30,000 EUR (taxable turnover in preceding 12 months; register within 10 days; voluntary registration allowed below)  _(PwC)_

**VAT Interaction Table**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (registered) | NOT income — exclude |
| Input VAT recovered (registered) | NOT an expense — exclude |
| Not VAT-registered | Gross amount is the cost/income |

### 5.10 Residency

- **Resident test** — Resident if present at least 183 days in the tax year, OR has domicile / centre of personal and economic interests in Montenegro. Residents are taxed on worldwide income; non-residents on Montenegro-source income only.  _(Law on Personal Income Tax; PwC)_

### 5.11 Filing Deadlines and Penalties

**Filing Deadlines and Penalties Table**

| Item | Detail |
| --- | --- |
| Annual PIT return (GPP-FL) | 30 April of the following year (PwC/forms) |
| Monthly payroll report (IOPPD) + payment | 15th of the following month (Rivermate) |
| Late payment of tax/contributions | Statutory default interest accrues; fines and audit exposure. [RESEARCH GAP — reviewer to confirm exact default-interest rate and fine amounts from the Tax Administration Law and Law on Contributions.] |
| Non-compliance / repeated | Intensified inspections, possible restrictions on business operations, misdemeanor fines for failure to file/register (Rivermate). [RESEARCH GAP — reviewer to confirm fine amounts.] |

### 5.12 Minimum Wage (context, not a tax figure)

- **Dual-tier NET minimum wage** — Dual-tier NET minimum wage since Sept 2024: EUR 670 net/month for jobs requiring up to a high-school diploma; EUR 800 net/month for jobs requiring a university degree / higher qualification; reviewed every 6 months by the Government. Minimum wage is stated NET; the gross equivalent depends on the contribution gross-up and must be computed, not assumed.  _(RemotePeople)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (Sole Proprietor)

- **Home office deduction rules** — Calculate proportion of home used for business (dedicated room(s) as % of total floor area). Apply that percentage to rent, electricity (EPCG), water (Vodovod), internet, maintenance. A dual-use room does NOT qualify. Conservative default: 0% deduction until reviewer confirms arrangement. Flag for reviewer: Confirm room count, floor-area basis, dedicated workspace.

### 6.2 Motor Vehicle Business Use

- **Motor vehicle deduction rules** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Client must maintain a mileage log. Conservative default: 0% business use until mileage log provided. Flag for reviewer: Confirm business percentage and the applicable depreciation rate. [RESEARCH GAP — reviewer to confirm depreciation rate.]

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use rule** — Business use portion only; client provides a reasonable estimate. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 Asset Depreciation Rates

- **Asset depreciation rule** — Statutory tax-depreciation rates for sole-proprietor assets were not confirmed in research. Flag for reviewer: Confirm the correct depreciation method/rate for each asset class before capitalising. [RESEARCH GAP — reviewer to confirm.]

### 6.5 Rental-Income Standardised Cost Deduction

- **Rental standardised cost deduction rule** — Some regimes allow a standardised percentage deduction against gross rental income before the 15% flat tax. Flag for reviewer: Confirm whether a standardised cost deduction applies and at what percentage. [RESEARCH GAP — reviewer to confirm.]

### 6.6 Contribution Ceiling Application

- **Contribution ceiling application rule** — Pension/disability is capped at an annual base (EUR 68,765, 2024 figure). Flag for reviewer: Confirm the current-year indexed ceiling and apply the cap for high earners. [RESEARCH GAP — reviewer to confirm with PIO Fund.]

### 6.7 Europe-Now Vintage / Stale-Rate Risk

- **Stale rate risk rule** — Many EOR/payroll guides still publish PRE-REFORM contribution rates (employee 15% pension + 8.5% health; employer 5.5% + 2.3%). These are STALE. Flag for reviewer: Confirm the period falls under the post-1-Oct-2024 structure (employee 10.5%, employer 0.5%, no health). If the period straddles a reform date, escalate.

## Section 7 -- Excel Working Paper Template

```
MONTENEGRO PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Type: Employee / Sole Proprietor (preduzetnik)
Municipality: ______________  (Surtax: 13% / 15% Podgorica-Cetinje)
Residency: Resident (worldwide) / Non-resident (ME-source)

=== A. EMPLOYMENT INCOME (monthly bands) ===
  A1. Monthly gross salary                       ___________
  A2. PIT  [0% to 700; 9% 700.01-1,000; 15% >1,000]  ___________
  A3. Municipal surtax (A2 x 13% or 15%)         ___________
  A4. Employee contributions (A1 x 10.5%)        ___________
  A5. NET PAY (A1 - A2 - A3 - A4)                ___________
  A6. Employer contributions (A1 x 0.5%)         ___________

=== B. SELF-EMPLOYMENT INCOME (annual bands) ===
  B1. Gross business income (net of VAT if reg.) ___________
  B2. Less: allowable expenses                   ___________
  B3. Net annual profit (B1 - B2)                ___________
  B4. PIT [0% to 8,400; 9% 8,400.01-12,000; 15% >12,000] ___________
  B5. Municipal surtax (B4 x 13% or 15%)         ___________
  B6. Total PIT + surtax (B4 + B5)               ___________

=== C. OTHER INCOME (flat 15%) ===
  C1. Rental income (x 15%)                      ___________
  C2. Dividends (x 15%)                          ___________
  C3. Interest (x 15%)                           ___________
  C4. Royalties / capital gains (x 15%)          ___________

=== D. CONTRIBUTION CEILING CHECK ===
  D1. Annual contribution base                   ___________
  D2. Ceiling (EUR 68,765 - confirm indexed)     ___________
  D3. Contributions capped above D2?  Y / N

REVIEWER FLAGS:
  [ ] Municipality confirmed (surtax 13% vs 15%)?
  [ ] Residency confirmed (worldwide vs source)?
  [ ] Post-Oct-2024 contribution structure confirmed?
  [ ] Salary on MONTHLY bands, SE on ANNUAL bands?
  [ ] VAT registration status confirmed?
  [ ] Contribution ceiling applied for high earners?
  [ ] Depreciation rates confirmed for capital items?
  [ ] Rental standardised-cost deduction confirmed?
  [ ] No stale pre-reform rates used?
```

## Section 8 -- Bank Statement Reading Guide

### Montenegrin Bank Statement Formats

**Bank Statement Formats Table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| CKB (Crnogorska komercijalna banka) | PDF, CSV | Datum, Opis, Zaduženje, Uplata, Saldo | Most common; date format DD.MM.YYYY |
| NLB Banka | PDF, CSV | Datum valute, Opis, Iznos, Saldo | Counterparty in description |
| Erste Bank Montenegro | PDF, CSV | Datum, Opis transakcije, Iznos, Stanje | CSV export available |
| Hipotekarna banka | PDF | Datum, Opis, Isplata, Uplata | Shorter descriptions |
| Universal Capital Bank | CSV | Date, Counterparty, Amount, Reference | Cleaner counterparty names |

### Key Montenegrin Banking / Tax Terms

**Key Terms Table**

| Term | English | Classification Hint |
| --- | --- | --- |
| UPLATA | Inflow / credit | Potential income |
| ISPLATA | Outflow / payment | Expense — check counterparty |
| PRENOS / DOZNAKA | Transfer | Check direction for income/expense |
| TRAJNI NALOG | Standing order | Regular expense (rent, loan) |
| DIREKTNO ZADUŽENJE | Direct debit | Regular expense (utility, subscription) |
| KARTICA | Card payment | Expense — check merchant |
| ZARADA / PLATA | Salary / wage | Employment income (monthly bands) |
| HONORAR / NAKNADA | Fee / honorarium | Business income |
| ZAKUP / KIRIJA | Rent | Rental income (flat 15%) or office rent expense |
| KAMATA | Interest | Interest income (flat 15%) or bank charge |
| PROVIZIJA / NAKNADA | Charge / commission | Bank charge (deductible) |
| DOPRINOSI / PIO | Contributions / pension | Social contributions — track separately |
| PDV | VAT | VAT — exclude from income/expense |
| POREZ / PRIREZ | Tax / surtax | Tax payment (not deductible) |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- MONTENEGRO INCOME TAX
1. Are you an employee, a sole proprietor (preduzetnik), or both?
2. Which municipality? (surtax is 15% in Podgorica/Cetinje, 13% elsewhere)
3. Are you a Montenegro tax resident (183+ days or centre of interests here)?
4. For employees: monthly gross salary?
5. For sole proprietors: total annual business income and expenses?
6. Are you VAT-registered (turnover over EUR 30,000 / standard 21%)?
7. Any other income (rental, dividends, interest, royalties, capital gains)?
8. Home office: dedicated room or shared space? If dedicated, what % of floor area?
9. Vehicle: business use? If yes, what % is business? Mileage log kept?
10. Phone/internet: what % is business use?
11. Which period — does it fall entirely after 1 Oct 2024 (Europe Now 2)?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation Table**

| Topic | Reference |
| --- | --- |
| PIT rates (employment/SE/other/gaming) | Law on Personal Income Tax; PwC (reviewed 27 Mar 2026) |
| Social contributions | Law on Contributions for Mandatory Social Insurance; PwC |
| Municipal surtax (prirez) | Law on Local Self-Government Financing; PwC |
| Health contribution abolition (Jan 2022) | Europe Now 1; Orbitax / KPMG |
| Employer pension share abolition (Oct 2024) | Europe Now 2; PwC |
| Residency (183 days / centre of interests) | Law on Personal Income Tax; PwC |
| VAT registration (EUR 30,000; 21%) | PwC |
| Contribution ceiling (EUR 68,765, 2024) | PwC (indexed by PIO Fund) |
| Annual return (GPP-FL) | Revenue and Customs Administration; deadline 30 April |
| Monthly payroll report (IOPPD) | Revenue and Customs Administration; deadline 15th of following month (Rivermate) |
| Filing portal | eprijava.tax.gov.me / www.poreskauprava.gov.me |

### Forms

**Forms Table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| GPP-FL (Obrazac GPP-FL, Schedule A) | Annual PIT return for sole proprietors and individuals with reportable income | 30 April of the following year |
| IOPPD (Obrazac IOPPD) | Monthly report on calculated and paid PIT and social contributions (payroll/withholding) | 15th of the following month; contributions paid simultaneously |
| Annual income statement to employee | Employer summary of annual earnings and withheld taxes/contributions | Annual (end of tax year) |

### CRITICAL Stale-Data Warning

Many EOR/payroll secondary guides (e.g. Rivermate, some 2025/2026 guides) still list PRE-REFORM social contribution rates — employee 15% pension + 8.5% health, employer 5.5% pension + 2.3% health + labour-fund levy. **These are OUTDATED.** The Europe Now reforms abolished health contributions (1 Jan 2022) and the employer pension/disability share, and cut the employee pension rate to 10% (1 Oct 2024). PwC (reviewed 27 March 2026), KPMG Montenegro, and Orbitax confirm the current structure: **employee 10.5% total, employer 0.5% only, no health contribution.** Always use the post-reform figures.

### Sources

**Sources Table**

| Title | Publisher |
| --- | --- |
| Montenegro — Individual — Taxes on personal income | PwC Worldwide Tax Summaries (reviewed 27 Mar 2026) — taxsummaries.pwc.com/montenegro/individual/taxes-on-personal-income |
| Montenegro — Individual — Other taxes (social security, VAT) | PwC Worldwide Tax Summaries (reviewed 27 Mar 2026) — taxsummaries.pwc.com/montenegro/individual/other-taxes |
| Montenegro — Individual — Residence | PwC Worldwide Tax Summaries (reviewed 27 Mar 2026) — taxsummaries.pwc.com/montenegro/individual/residence |
| Montenegro Abolishes Compulsory Health Insurance Contributions | Orbitax — orbitax.com/news/archive.php/Montenegro-Abolishes-Compulsor-49057 |
| Novelties in Personal Taxation and Labor Law in 2022 (Europe Now) | KPMG Montenegro |
| Minimum Wage in Montenegro for 2025 (dual-tier EUR 670 / EUR 800 net) | RemotePeople |
| Employment Taxes in Montenegro (IOPPD monthly deadline) | Rivermate (deadlines only; contribution rates treated as partly stale, cross-checked against PwC) |

### Test Suite

**Test 1 -- Employee, Podgorica, EUR 1,200 gross/month.**
Input: monthly gross EUR 1,200; Podgorica (15% surtax).
Expected: PIT = 27.00 + 30.00 = EUR 57.00; surtax = 57.00 × 15% = EUR 8.55; contributions = 1,200 × 10.5% = EUR 126.00; **net pay = EUR 1,008.45**.

**Test 2 -- Employee at the 0% band, EUR 700 gross/month.**
Input: monthly gross EUR 700.
Expected: PIT = EUR 0.00; surtax = EUR 0.00; contributions = 700 × 10.5% = EUR 73.50; **net pay = EUR 626.50**.

**Test 3 -- Sole proprietor, EUR 20,000 annual profit, other municipality (13%).**
Input: annual net profit EUR 20,000; 13% surtax.
Expected: PIT = 324.00 + 1,200.00 = EUR 1,524.00; surtax = 1,524.00 × 13% = EUR 198.12; **total PIT + surtax = EUR 1,722.12**.

**Test 4 -- Sole proprietor at the SE 0% ceiling, EUR 8,400 annual.**
Input: annual net profit EUR 8,400.
Expected: PIT = EUR 0.00 (entirely within 0% band); surtax = EUR 0.00.

**Test 5 -- Rental income, EUR 500/month, flat 15%.**
Input: gross rent EUR 500 (one month).
Expected: PIT = 500 × 15% = EUR 75.00 (before any standardised cost deduction — flag for reviewer).

**Test 6 -- Gaming winnings EUR 1,500.**
Input: winnings EUR 1,500.
Expected: tax = (1,500 − 50) × 10% = EUR 145.00.

**Test 7 -- Employer payroll burden, EUR 1,000 gross/month.**
Input: monthly gross EUR 1,000.
Expected: employer contributions = 1,000 × 0.5% = EUR 5.00 (unemployment only); no employer pension/health.

## PROHIBITIONS

- **Prohibitions list** — - NEVER apply the salary monthly bands to self-employment income, or the annual SE bands to a salary — they are different bases - NEVER add the municipal surtax to the income rate — it is a tax ON the PIT amount (13% / 15%) - NEVER use pre-Europe-Now contribution rates (e.g. 15% employee pension, 8.5% health, employer 5.5%/2.3%) — they are STALE - NEVER apply a health-insurance contribution — it was abolished 1 Jan 2022 - NEVER charge an employer pension/disability contribution for periods after 1 Oct 2024 — it was abolished - NEVER determine worldwide vs source taxation without confirming residency - NEVER apply an asset depreciation rate without reviewer confirmation (research gap) - NEVER include VAT collected on sales as income for a VAT-registered client - NEVER allow fines, penalties, income tax, or owner drawings as deductions - NEVER present tax calculations as definitive — always label as estimated, pending professional review

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
