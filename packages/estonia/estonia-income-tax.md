---
name: estonia-income-tax
description: Use this skill whenever asked about Estonia personal income tax for self-employed individuals (FIE) and resident individuals. Trigger on phrases like "how much tax do I pay in Estonia", "Estonian income tax return", "Form A", "Form E", "tuludeklaratsioon", "TSD", "FIE", "ettevõtluskonto", "entrepreneur account", "basic exemption", "maksuvaba tulu", "tax hump", "social tax", "sotsiaalmaks", "funded pension", "II pillar", "unemployment insurance", "töötuskindlustus", "flat 22% tax", "self-employed tax Estonia", or any question about filing or computing personal income tax for a resident or self-employed (FIE) client in Estonia. Also trigger when preparing or reviewing a Form A / Form E return, computing FIE business deductions, running payroll withholding via TSD, advising on FIE social-tax advance payments, or comparing the entrepreneur-account simplified regime. This skill covers the flat 22% income tax rate, the income-dependent basic exemption and its 2026 reform, social tax, unemployment-insurance premiums, funded (II) pension, the entrepreneur-account regime, payroll (TSD) declarations, filing deadlines, penalties, and interaction with VAT. ALWAYS read this skill before touching any Estonian income tax work.
version: 0.1
jurisdiction: EE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia Personal Income Tax -- Self-Employed (FIE) & Individuals

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Estonia (Republic of Estonia) |
| Tax | Personal Income Tax (tulumaks) + Social Tax (sotsiaalmaks) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (Tulumaksuseadus, TuMS) |
| Supporting legislation | Social Tax Act (Sotsiaalmaksuseadus, SMS); Unemployment Insurance Act (Töötuskindlustuse seadus); Funded Pensions Act (Kogumispensionide seadus); Value-Added Tax Act (Käibemaksuseadus); Taxation Act (Maksukorralduse seadus, MKS) |
| Tax authority | Estonian Tax and Customs Board -- Maksu- ja Tolliamet (EMTA) |
| Social-security bodies | Sotsiaalkindlustusamet (Social Insurance Board); Eesti Töötukassa (Unemployment Insurance Fund); Pensionikeskus (funded-pension register) |
| Filing portal | e-MTA (https://www.emta.ee) |
| Filing deadline | Form A + Form E: 30 April of the following year (e.g. 30 April 2026 for tax year 2025); e-filing opens 15 February [EMTA, Income tax returns for 2025] |
| Validated by | Pending -- requires sign-off by an Estonian-qualified tax professional |
| Validation date | Pending |
| Skill version | 0.1 |

### Personal Income Tax Rate (2025 and 2026)

**Personal Income Tax Rate table**

| Tax Year | Rate | Applies To | Source |
| --- | --- | --- | --- |
| 2025 | **22%** | All resident individual income (employment, business/FIE income, capital, rental) | [EMTA, Tax rates] -- raised from 20% to 22% effective 1 Jan 2025 |
| 2026 | **22%** | Same -- all resident individual income | [Estonian Chamber of Commerce; EMTA, Tax rates] |

- **Flat rate, no brackets** — Estonia has a proportional (flat) personal income tax. There are no brackets and no local income taxes. The only relief is the basic exemption.

STALE-FIGURE WARNING. Some 2024-2025 secondary sources (EY, Estonian Chamber of Commerce headlines) state that income tax would rise to 24% from 2026 and that a temporary 2% defence/security tax would apply. Both were cancelled -- the defence/security tax was abolished (19 June 2025) and the Riigikogu cancelled the 24% income-tax rise in December 2025. The personal income tax rate stays 22% for 2026. (VAT did rise to 24% from 1 July 2025 -- that is a separate tax; see Section 5.7.)

### Basic Exemption (maksuvaba tulu)

**Basic Exemption table**

| Category | Tax Year | Annual (EUR) | Monthly (EUR) | Notes | Source |
| --- | --- | --- | --- | --- | --- |
| General | 2025 | up to 7,848 | up to 654 | **Income-dependent ("tax hump")** -- full amount only if annual income <= 14,400 | [EMTA, Calculation of basic exemption] |
| General -- taper | 2025 | see formula | -- | Income 14,400-25,200: BE = 7,848 - 7,848/10,800 x (annual income - 14,400). **Zero above 25,200** | [EMTA, Calculation of basic exemption] |
| Pensionable age | 2025 | 9,312 | 776 | Fixed, **not** income-dependent (persons born 1961 or earlier); applied automatically by the Social Insurance Board | [EMTA, Tax rates] |
| General | 2026 | 8,400 | 700 | **The income taper is abolished** -- flat 8,400 EUR/yr for everyone regardless of income | [EMTA, Tax rates] |
| Pensionable age | 2026 | 9,312 | 776 | Fixed, not income-dependent | [EMTA, Tax rates] |

2025 taper worked check: at income 14,400 EUR, BE = 7,848 - 7,848/10,800 x 0 = 7,848. At income 25,200 EUR, BE = 7,848 - 7,848/10,800 x 10,800 = 7,848 - 7,848 = 0. The taper is linear over the 10,800 EUR band. [EMTA, Calculation of basic exemption]

### Contributions Snapshot (2025)

**Contributions Snapshot table**

| Contribution | Rate | Paid by | Notes | Source |
| --- | --- | --- | --- | --- |
| Social tax (sotsiaalmaks) | 33% (20% pension + 13% health) | Employer (on top of gross); FIE on own profit | Min monthly base 820 EUR -> min obligation 270.60 EUR/mo (2025). No ceiling for employees | [EMTA, Social tax] |
| Unemployment insurance -- employee | 1.6% | Employee (withheld) | Rate fixed 2025-2028. Pensionable-age persons exempt. FIE not subject | [EMTA, Unemployment insurance premiums] |
| Unemployment insurance -- employer | 0.8% | Employer | Still payable for pensionable-age workers. FIE not subject | [EMTA, Unemployment insurance premiums] |
| Funded (II) pension -- employee | 2% default (or 4% / 6% by election) | Employee (withheld); state adds 4% from the 33% social tax | Mandatory for residents born after 31 Dec 1982; voluntary otherwise. 4%/6% election possible since 1 Jan 2024 | [PwC Estonia, Other taxes] |

- **Total employer on-cost** — 33% social tax + 0.8% unemployment insurance = ~33.8% on top of gross  _([EMTA, Social tax])_
- **2026 social-tax floor** — minimum monthly base 886 EUR -> minimum obligation 292.38 EUR/mo (886 x 33%)  _([EMTA, Social tax])_

### FIE (Self-Employed) Key Figures

**FIE Key Figures table**

| Item | Value | Source |
| --- | --- | --- |
| Income tax on business profit | 22% on profit (income minus allowable deductions) | [EMTA, Self-employed -- income tax] |
| Social tax on business profit | 33% on the same profit; social tax itself is **not** deductible from the income-tax base | [EMTA, Self-employed -- social tax] |
| FIE social-tax annual ceiling (2025) | **35,085.60 EUR** = 886 x 10 x 12 x 33% | [EMTA, Self-employed -- social tax] |
| FIE quarterly social-tax advance (2025) | **811.80 EUR** each = 820 x 3 x 33% | [EMTA, Self-employed -- social tax] |
| Advance due dates | 15th of the last month of each quarter (15 Mar, 15 Jun, 15 Sep, 15 Dec) | [EMTA, Self-employed -- social tax] |
| Advance exemptions | Students, pensioners, and those simultaneously employed (Class 1 social tax already paid) | [EMTA, Self-employed -- social tax] |

FIE ceiling worked check (2025): 886 x 10 = 8,860; x 12 = 106,320; x 33% = 35,085.60.
FIE quarterly advance worked check (2025): 820 x 3 = 2,460; x 33% = 811.80.

### Key Thresholds

**Key Thresholds table**

| Item | Value | Source |
| --- | --- | --- |
| VAT registration (resident) | Mandatory once taxable turnover exceeds **40,000 EUR** in a calendar year; EU-wide SME cross-border threshold 100,000 EUR | [EMTA, Obligation to register] |
| Entrepreneur account (ettevõtluskonto) max annual receipts | **40,000 EUR/yr**; above this, register as FIE or company and become VAT-liable | [EMTA, Entrepreneur account] |
| Minimum wage 2025 | 886 EUR/month; 5.31 EUR/hour | [ERR News; EMTA] |
| Minimum wage 2026 | 946 EUR/month; 5.67 EUR/hour | [ERR News] |

> [RESEARCH GAP -- reviewer to confirm] The 2026 minimum wage of 946 EUR is reported to take effect 1 April 2026 (not 1 January) per the tripartite agreement -- verify the exact effective date in the final government regulation. The 5.31 EUR/hour 2025 hourly figure is derived/secondary -- confirm against the official regulation. The 2025 minimum wage (886 EUR) coincides numerically with the 2026 social-tax minimum base (886 EUR) but they are distinct concepts (see Section 10).
>
> [RESEARCH GAP -- reviewer to confirm] One EMTA-derived figure cited a 2026 FIE social-tax ceiling of 36,867.60 EUR -- recompute from the confirmed 2026 minimum wage before relying on it. Note the 2025 ceiling formula above uses the 886 EUR base while the 2025 quarterly advance uses the 820 EUR floor; confirm the exact statutory base used for each before wiring formulas.

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown tax year | Use 2025 (the operative year, filed by 30 April 2026); confirm if near a 2025/2026 boundary, since basic-exemption rules differ materially |
| Unknown residency | STOP -- do not apply resident rates without confirming Estonian tax residency |
| Basic-exemption application unknown | If the employee has NOT filed an application with the employer, withhold 22% on full gross (no monthly BE) |
| 2025 basic exemption, income above 25,200 | EUR 0 exemption |
| 2026 basic exemption (under pension age) | Flat 8,400 EUR/yr |
| Funded-pension rate unknown | Assume 2% (statutory default) for residents born after 1982; 0% for non-members. Verify in Pensionikeskus before assuming 4%/6% |
| FIE social tax base | 33% on profit after deductions, subject to the 2025 annual cap of 35,085.60 EUR; quarterly advances 811.80 EUR unless exempt |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Pensionable-age status unknown | Do NOT apply the 9,312 EUR fixed exemption or the UI exemption without confirming date of birth |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — Bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (1) tax year, (2) Estonian tax residency, (3) status (employed individual / FIE self-employed / entrepreneur-account holder), and (4) date of birth (drives pensionable-age exemption, funded-pension mandatory status, and UI exemption).
- **Recommended** — All sales invoices, purchase invoices/receipts, social-tax advance payment records, prior-year Form A / Form E, funded-pension (II pillar) membership and elected rate from Pensionikeskus, VAT registration status.
- **Ideal** — Complete income and expenditure account, FIE asset/expense register, advance-payment confirmations, TSD monthly declarations for the year (if an employer), employment income details (if mixed), entrepreneur-account statement.
- **Refusal if minimum is missing** — SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This Form E / Form A was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and incurred in the production of business income."

### Refusal Catalogue

- **R-EE-1** — Tax year not confirmed. "The 2025 and 2026 rules differ materially (basic-exemption taper vs fixed, social-tax floor). This skill cannot reliably compute tax without knowing the tax year. Confirm before proceeding."
- **R-EE-2** — Residency unknown. "Residency determines whether resident rules (flat 22% with basic exemption) or non-resident rules apply. This skill covers resident natural persons. Confirm Estonian tax residency before proceeding."
- **R-EE-3** — Companies (OÜ/AS) and distributed-profit tax. "This skill covers resident individuals and sole proprietors (FIE) only. Estonian companies (OÜ, AS) are taxed on distributed profits under a separate corporate regime. Escalate to an Estonian-qualified tax adviser."
- **R-EE-4** — Capital gains / securities / property disposals. "Capital-gains specifics, the investment-account regime, and property disposals were not researched in this skill. Out of scope. Escalate to an Estonian-qualified tax adviser."
- **R-EE-5** — Non-resident income / treaty relief. "Non-resident and dual-resident taxation, and double-tax-treaty relief, were not researched in this skill and have different rules. Escalate to an Estonian-qualified tax adviser."
- **R-EE-6** — Fringe-benefit tax. "Employer fringe-benefit (erisoodustus) taxation was not researched in this skill. Escalate to an Estonian-qualified tax adviser."
- **R-EE-7** — Arrears / enforcement. "Client has outstanding tax arrears. Late-payment interest runs at 0.06%/day (~21.9%/year) and is uncapped until paid. Do not advise on settlement strategy. Escalate to an Estonian-qualified tax adviser immediately."
- **R-EE-8** — VAT return requested. "This skill covers personal income tax (Form A / Form E) and payroll (TSD) only. For Estonian VAT (KMD), use the dedicated Estonia VAT skill. Note: standard VAT rose to 24% on 1 July 2025."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Estonian statements frequently mix Estonian and English terms. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. "Form E" refers to the FIE business-income declaration filed with Form A.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | Form Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + ÜLEKANNE, MAKSE, TRANSFER, PAYMENT | Form E (business income) | Business income | If VAT-registered, extract net (excl. 24% VAT from 1 Jul 2025) |
| ARVE, TASU, HONORAR, TEENUSTASU, FEES, CONSULTANCY | Form E | Business income | Professional/service fees -- typical for FIE |
| STRIPE PAYOUT, STRIPE TRANSFER | Form E | Business income | Platform payout -- match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Form E | Business income | Platform payout -- verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Form E | Business income | International platform payout |
| REVOLUT PAYOUT | Form E | Business income | Check business vs personal Revolut |
| UPWORK, FIVERR, TOPTAL | Form E | Business income | Freelance platform -- net of platform commission |
| PALK, TÖÖTASU, SALARY, EMPLOYER [name] | Form A (employment income) | Employment income | NOT FIE income -- employer already withheld via TSD |
| ÜÜR, RENT RECEIVED | Form A (rental income) | Rental income | Resident rental income, taxed at 22% |
| INTRESS, INTEREST RECEIVED | Form A (investment income) | Interest income |  |
| DIVIDEND, DIVIDENDID | Form A (investment income) | Dividend income | Often already taxed at company level -- flag |
| PENSION, PENSIONIAMET | Form A (pension income) | Pension income | Pensionable-age basic exemption may apply |
| EMTA TAGASTUS, TAX REFUND | EXCLUDE | Not income | Tax refund from prior year |
| TOETUS, GRANT, EAS, KREDEX | EXCLUDE unless revenue grant | Check nature | Capital grants EXCLUDE; revenue/operating grants = Form E |

### 3.2 Expense Patterns (Debits) -- Allowable FIE Business Deductions (Form E)

**Allowable FIE Deductions table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| KONTORIÜÜR, BÜROORENT, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| KINDLUSTUS (professional/business), INSURANCE | Business insurance | Deductible | Business liability cover |
| RAAMATUPIDAJA, ACCOUNTANT, AUDIITOR, BOOKKEEP | Accountancy fees | Deductible |  |
| ADVOKAAT, JURIST, LAWYER, LEGAL (business) | Legal fees | Deductible | Must be business-related |
| KONTORITARBED, OFFICE SUPPLIES, STATIONERY | Office supplies | Deductible |  |
| TURUNDUS, REKLAAM, MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| KOOLITUS, TRAINING, COURSE, SEMINAR, CONFERENCE | Training | Deductible | Must relate to current business |
| LIIKMEMAKS, PROFESSIONAL BODY, SUBSCRIPTION | Professional subscriptions | Deductible |  |
| PANGATEENUS, PANGATASU, BANK FEE | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Deductible | Recurring = operating expense |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| SOFTWARE LICENCE (perpetual, durable) | Durable asset | Flag for reviewer | Confirm treatment vs immediate deduction |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ELEKTER, ELEKTRILEVI, EESTI ENERGIA, ENEFIT | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| VESI, VEEVÄRK, GAAS | Water/gas | T2 if home office | Business portion only |
| TELIA, ELISA, TELE2, INTERNET, BROADBAND | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| MOBIIL, MOBILE, TELEFON | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR BALTIC, RYANAIR, WIZZ AIR, LUFTHANSA, FINNAIR | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTELL, HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| BOLT, UBER, TAKSO, TAXI | Local transport | Deductible if business purpose |  |
| KÜTUS, FUEL, NESTE, CIRCLE K, ALEXELA | Vehicle fuel | T2 -- business % only | Requires mileage / use log |
| PARKIMINE, PARKING, EUROPARK | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORAN, RESTAURANT, LÕUNA, MEELELAHUTUS, ENTERTAINMENT | Entertainment / meals | NOT deductible (FIE) | Private/representation cost -- block for FIE business income |
| TOIDUKAUP, GROCERIES, SELVER, RIMI, MAXIMA, COOP, PRISMA | Personal expenses | NOT deductible | Private living costs |
| TRAHV, FINE, PENALTY, VIIVIS | Fines/penalties/interest | NOT deductible | Public policy |
| EMTA TULUMAKS, INCOME TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| SOTSIAALMAKS, SOCIAL TAX | Social tax | NOT deductible from income-tax base | FIE social tax is its own charge; track separately (5.4) |
| VÄLJAVÕTT, DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Durable Business Assets (FIE)

**Durable Business Assets table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| SÜLEARVUTI, LAPTOP, ARVUTI, MACBOOK | Computer hardware | Flag for reviewer | FIE asset treatment is a research gap (see 6.4) |
| PRINTER, SKANNER, KOOPIAMASIN | Office equipment | Flag for reviewer |  |
| MÖÖBEL, LAUD, TOOL, FURNITURE | Furniture/fittings | Flag for reviewer |  |
| AUTO, VEHICLE, CAR (business) | Motor vehicle | T2 -- business % only | Mixed-use; flag for reviewer |

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OMA KONTO, INTERNAL TRANSFER, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LAEN, LOAN REPAYMENT, PRINCIPAL | EXCLUDE | Loan principal movement |
| KÄIBEMAKS, KMD MAKSE, VAT PAYMENT | EXCLUDE | VAT liability payment, not expense |
| SOTSIAALMAKSU AVANSS, SOCIAL TAX ADVANCE (FIE) | Track separately (credit against liability) | FIE quarterly advance -- not a Form E business expense |

### 3.9 Estonian Banks -- Statement Format Reference

**Estonian Banks Statement Format table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Swedbank | ÜLEKANNE, MAKSE, OTSEKORRALDUS, KAARDIMAKSE, TEENUSTASU | PDF/CSV; date format DD.MM.YYYY |
| SEB | ÜLEKANNE, KAARDIMAKSE, PÜSIMAKSE | PDF/CSV; counterparty in description |
| LHV Pank | MAKSE, KAARDIMAKSE, TEENUSTASU, ETTEVÕTLUSKONTO | CSV; clean names; **hosts the entrepreneur account** |
| Luminor | ÜLEKANNE, MAKSE, PÜSIMAKSE, KAARDIMAKSE | PDF/CSV |
| Wise / Revolut Business | TRANSFER, CARD PAYMENT, CONVERSION, PAYMENT | CSV; multi-currency -- use EUR amounts |

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (VAT-registered FIE)

Input line:
15.03.2025 ; LHV ÜLEKANNE ; STUUDIO KASK OÜ ; ARVE 2025-003 ; +1,240.00 ; EUR

Reasoning:
Client payment for services. The FIE is VAT-registered. Standard VAT is 24% from 1 July 2025 (was 22% before). For a 24% invoice, EUR 1,240 includes VAT, so net business income = 1,240 / 1.24 = EUR 1,000.00 (Form E). The EUR 240.00 is VAT collected -- excluded from income (a liability to EMTA).

Classification: Form E business income = EUR 1,000.00. VAT EUR 240.00 excluded. If the supply dated before 1 July 2025, VAT is 22%, so net = 1,240 / 1.22 = EUR 1,016.39 -- confirm the supply date. If not VAT-registered, the full EUR 1,240 is business income. [EMTA VAT pages]

### Example 2 -- SaaS Subscription (Fully Deductible)

Input line:
01.04.2025 ; SEB KAARDIMAKSE ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD ; -29.99 ; EUR

Reasoning:
Monthly SaaS subscription, recurring, used in the business. Fully deductible as a Form E operating expense. For a VAT-registered FIE, the net amount (excl. recoverable input VAT) is the expense; otherwise the gross amount.

Classification: Form E deduction = EUR 29.99 (or net if VAT-registered with recoverable input VAT).

### Example 3 -- Personal Groceries (Not Deductible)

Input line:
22.04.2025 ; SWEDBANK KAARDIMAKSE ; RIMI EESTI ; OST ; -64.20 ; EUR

Reasoning:
Supermarket purchase. Private living cost. Not incurred for the production of business income. No deduction, no apportionment.

Classification: NOT deductible. Exclude from Form E.

### Example 4 -- FIE Social-Tax Quarterly Advance

Input line:
14.03.2025 ; SWEDBANK ÜLEKANNE ; EMTA SOTSIAALMAKSU AVANSS ; Q1 2025 ; -811.80 ; EUR

Reasoning:
FIE quarterly social-tax advance (820 x 3 x 33% = 811.80 for 2025), due 15 March. This is not a deduction against business profit -- it is a payment toward the FIE's own social-tax liability and is reconciled on assessment. Track it separately as a payment on account.

Classification: Social-tax advance payment (credit against liability) = EUR 811.80. NOT a Form E expense. [EMTA, Self-employed -- social tax]

### Example 5 -- Employee Net Pay (Monthly Payroll, 2025)

Input: Resident employee, gross monthly wage EUR 2,000, born after 1982 (funded pension 2% default), basic-exemption application filed with this employer (monthly BE 654 EUR), single employer.

Reasoning (employee deductions, in order):
1. Unemployment insurance (employee) = 2,000 x 1.6% = 32.00
2. Funded pension (II pillar) = 2,000 x 2% = 40.00
3. Income-tax base = gross - UI - pension - basic exemption = 2,000 - 32.00 - 40.00 - 654.00 = 1,274.00
4. Income tax = 1,274.00 x 22% = 280.28
5. Net pay = 2,000 - 32.00 - 40.00 - 280.28 = 1,647.72

Employer on-cost (on top of gross):
- Social tax = 2,000 x 33% = 660.00
- Unemployment insurance (employer) = 2,000 x 0.8% = 16.00
- Total employer cost = 2,000 + 660.00 + 16.00 = 2,676.00

Classification: Net pay EUR 1,647.72; employer pays EUR 660.00 social tax + EUR 16.00 UI; income tax withheld EUR 280.28. All declared on Form TSD by 10 April 2025. [EMTA, Income from employment; Social tax; Unemployment insurance premiums]

### Example 6 -- FIE Annual Computation (2025)

Input: Resident FIE, business income EUR 50,000, allowable business deductions EUR 20,000, no other income, born after 1982.

Reasoning:
- Business profit = 50,000 - 20,000 = 30,000.00 (Form E)
- Social tax = 30,000 x 33% = 9,900.00 (below the 2025 ceiling of 35,085.60). Social tax is NOT deducted from the income-tax base.
- Basic exemption: annual income 30,000 > 25,200, so basic exemption = 0 (2025 taper).
- Income tax = 30,000 x 22% = 6,600.00
- Total Estonian tax = 6,600.00 income tax + 9,900.00 social tax = 16,500.00

Classification: Form E profit EUR 30,000.00; income tax EUR 6,600.00; social tax EUR 9,900.00. Quarterly advances paid during the year (4 x 811.80 = 3,247.20) are credited against the social-tax liability; the balance is settled on assessment. [EMTA, Self-employed -- income tax / social tax]

### Example 7 -- Entrepreneur Account (ettevõtluskonto)

Input line:
10.05.2025 ; LHV ETTEVÕTLUSKONTO ; KLIENT MAKSE ; +500.00 ; EUR

Reasoning:
Receipts paid into an LHV entrepreneur account are taxed by a single business income tax of 20% of gross receipts (split 22/55 income tax + 33/55 social tax) -- this single charge covers both income tax and social tax. No expense deductions are allowed. The 40% rate for receipts over 25,000 EUR was abolished from 1 Jan 2025. Receipts are capped at 40,000 EUR/yr; above that the holder must register as a FIE or company. LHV deducts and remits the tax automatically.

Tax on this receipt: 500.00 x 20% = 100.00 (of which income tax 500 x 20% x 22/55 = 40.00; social tax 500 x 20% x 33/55 = 60.00). Check: 40.00 + 60.00 = 100.00.

Classification: Entrepreneur-account business income tax EUR 100.00, remitted by LHV. No separate Form E. [EMTA, Entrepreneur account]

> [RESEARCH GAP -- reviewer to confirm] Entrepreneur-account mechanics are bank-specific (LHV only); the 22%/24%/26% rate that applies when a 4%/6% funded-pension election is in place should be verified per individual before use. [EMTA, Entrepreneur account]

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Flat Rate and Scope

- **Flat rate and scope** — Legislation: Income Tax Act (Tulumaksuseadus, TuMS). Personal income tax is a flat 22% for both 2025 and 2026 on all resident individual income. There are no brackets and no local income taxes. The planned 24% rate (2026) and the temporary defence/security tax were both cancelled.  _([EMTA, Tax rates; Estonian Chamber of Commerce])_

### 5.2 Basic Exemption (maksuvaba tulu)

**Basic Exemption scenarios table**

| Scenario | Treatment | Source |
| --- | --- | --- |
| 2025, income <= 14,400 | Full 7,848 EUR/yr | [EMTA, Calculation of basic exemption] |
| 2025, income 14,400-25,200 | BE = 7,848 - 7,848/10,800 x (income - 14,400) | [EMTA, Calculation of basic exemption] |
| 2025, income > 25,200 | EUR 0 | [EMTA, Calculation of basic exemption] |
| 2026, under pension age | Fixed 8,400 EUR/yr (700 EUR/mo) regardless of income -- "tax hump" abolished | [EMTA, Tax rates] |
| Pensionable age (both years) | Fixed 9,312 EUR/yr (776 EUR/mo), applied automatically by the Social Insurance Board | [EMTA, Tax rates] |

- **Payroll monthly exemption application** — For payroll, the monthly exemption (max 654 EUR/mo in 2025; 700 EUR/mo in 2026) is applied by the employer only if the employee has filed an application with that employer; otherwise withhold 22% on full gross.  _([EMTA, Tax rates])_

### 5.3 Social Tax (sotsiaalmaks)

- **Social tax rate** — 33% (20% pension insurance + 13% health insurance). Paid by the employer on top of gross wage; FIE pay it on their own business profit.  _([EMTA, Social tax])_
- **Minimum monthly base** — Minimum monthly base 820 EUR in 2025 -> minimum obligation 270.60 EUR/mo. 2026 base 886 EUR -> 292.38 EUR/mo.  _([EMTA, Social tax])_
- **No ceiling / FIE ceiling / non-deductibility** — No ceiling for employees. FIE annual maximum = 35,085.60 EUR (2025). Social tax is not deductible from the income-tax base.  _([EMTA, Self-employed -- social tax])_

### 5.4 Unemployment Insurance Premiums

**Unemployment Insurance Premiums table**

| Premium | Rate | Payer | Notes |
| --- | --- | --- | --- |
| Employee | 1.6% | Employee (withheld) | Rate fixed 2025-2028; pensionable-age persons exempt; no ceiling |
| Employer | 0.8% | Employer | Still payable for pensionable-age workers; no ceiling |

- **FIE exemption from UI** — FIE/self-employed are not subject to unemployment-insurance premiums.  _([EMTA, Unemployment insurance premiums])_

### 5.5 Funded (II Pillar) Pension

- **Funded pension default and elective rates** — Default employee contribution 2% (withheld); the state adds 4% from the 33% social tax. Members may elect 4% or 6% (since 1 Jan 2024).  _([PwC Estonia, Other taxes])_
- **Mandatory membership** — Mandatory for residents born after 31 Dec 1982; voluntary otherwise. Always verify membership and elected rate in Pensionikeskus before assuming a rate.

### 5.6 FIE Business Income (Form E)

- **Business profit computation** — Business profit = business income - allowable business deductions (Form E). Form E must be filed even if no business income was earned.  _([EMTA, Self-employed -- income tax])_
- **Income tax on profit** — Income tax = profit x 22%. Apply basic exemption per Section 5.2 (income-dependent in 2025).
- **Social tax on profit** — Social tax = profit x 33%, subject to the 2025 annual ceiling of 35,085.60 EUR. Social tax is not deductible from the income-tax base.
- **Quarterly advances** — Quarterly social-tax advances of 811.80 EUR each (2025) are due on the 15th of the last month of each quarter (15 Mar, 15 Jun, 15 Sep, 15 Dec), unless the FIE is exempt (student, pensioner, or simultaneously employed with Class 1 social tax paid).  _([EMTA, Self-employed -- income tax / social tax])_

### 5.7 VAT Interaction

**VAT Interaction table**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (VAT-registered) | NOT income -- exclude from Form E business income |
| Input VAT recovered (VAT-registered) | NOT an expense -- exclude from deductions |
| Foreign VAT (non-reclaimable) | IS an expense -- full gross is the cost |

- **VAT standard and reduced rates** — VAT standard rate 24% (permanent from 1 July 2025; was 22% before). Reduced rates 13% (incl. accommodation from 1 Jan 2025) and 9%.  _([EMTA VAT pages; EY tax-changes alert])_
- **VAT registration threshold** — Mandatory registration once taxable turnover exceeds 40,000 EUR in a calendar year; EU-wide SME cross-border threshold 100,000 EUR.  _([EMTA, Obligation to register])_
- **VAT return (KMD) deadline** — VAT return (KMD): due the 20th of the following month.  _([EMTA, Obligation to register])_

### 5.8 Entrepreneur Account (ettevõtluskonto)

- **Regime description** — Legislation: Income Tax Act (TuMS). A simplified regime taxing amounts received (gross receipts), bundling income tax + social tax. A single business income tax of 20% of gross receipts (split 22/55 income tax + 33/55 social tax) covers both. No expense deductions.

**Funded-pension rate vs business income tax rate table**

| Funded-pension rate | Business income tax rate on receipts |
| --- | --- |
| Not contributing | 20% |
| Contributing 2% | 22% |
| Contributing 4% | 24% |
| Contributing 6% | 26% |

- **Abolished 40% rate and cap** — The 40% rate for receipts over 25,000 EUR was abolished from 1 Jan 2025. Covers receipts up to 40,000 EUR/yr. Above that, register as a FIE or company and become VAT-liable. Operated only via LHV Pank.  _([EMTA, Entrepreneur account])_

### 5.9 Payroll (TSD) and Minimum Wage

**Payroll (TSD) and Minimum Wage table**

| Item | Detail | Source |
| --- | --- | --- |
| Income tax withholding | 22% monthly after applying the monthly basic exemption (max 654 EUR/mo in 2025) if the employee filed an application | [EMTA, Tax rates] |
| Monthly declaration | Form TSD (annexes 1, 2): withheld income tax, social tax, unemployment premiums, funded pension. Due 10th of the following month | [EMTA, Income and social taxes] |
| Minimum wage 2025 | 886 EUR/month; 5.31 EUR/hour | [ERR News; EMTA] |
| Minimum wage 2026 | 946 EUR/month; 5.67 EUR/hour (effective date to confirm -- see Section 1 research gap) | [ERR News] |

### 5.10 Filing Deadlines and Penalties

**Filing Deadlines and Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Annual return (Form A + Form E) | File by 30 April following the tax year; e-filing opens 15 February | [EMTA, Income tax returns for 2025] |
| Additional income tax due (individual) | Payable by **1 October** of the year following the tax year | [EMTA, Income tax returns for 2025] |
| Refunds | Paid out from early March | [EMTA, Income tax returns for 2025] |
| Monthly employer return (TSD) | Due 10th of the following month | [EMTA, Income and social taxes] |
| VAT return (KMD) | Due 20th of the following month | [EMTA, Obligation to register] |
| Late-payment interest | **0.06% per day (~21.9%/year)** on all arrears (income tax, social tax, VAT) from the day after the due date until payment; reducible up to 50% under an approved instalment plan | [EMTA, Payment of interests] |

> [RESEARCH GAP -- reviewer to confirm] Non-filing penalty payments (sunniraha) and incorrect-return penalties were not researched in this skill. Do not quote a specific penalty amount; flag for reviewer.

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (FIE)

- **Home office deduction rules** — Legislation: Income Tax Act (TuMS) -- business-purpose test. Calculate the proportion of the home used for business (dedicated room(s) as a percentage of total rooms or floor area). Apply that percentage to rent, electricity, water/gas, internet, and maintenance. Must be a genuinely dedicated workspace; a dual-use room does not qualify. Client must document the calculation and retain supporting records. Conservative default: 0% deduction until reviewer confirms the room arrangement. Flag for reviewer: Confirm room count, floor-area basis, and that the workspace is genuinely dedicated.

### 6.2 Motor Vehicle Business Use (FIE)

- **Motor vehicle business use rules** — Only the business-use percentage of fuel, insurance, and maintenance is deductible. Client must maintain a use/mileage log (business trips vs total). Conservative default: 0% business use until a log is provided. Flag for reviewer: Confirm the business percentage is documented and reasonable.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use rules** — Business-use portion only; client must provide a reasonable estimate. Conservative default: 0% deduction until the business percentage is confirmed.

### 6.4 Durable Business Asset Treatment (FIE)

- **Durable business asset rules** — A FIE may deduct documented business expenses; the treatment of durable assets (immediate deduction vs spreading) was not researched in this skill. Conservative default: Flag for reviewer; do not auto-deduct in full or auto-capitalise. Flag for reviewer: [RESEARCH GAP -- reviewer to confirm FIE durable-asset deduction mechanics with EMTA.]

### 6.5 Funded (II Pillar) Pension Rate

- **Funded pension rate reviewer notes** — Default 2% for residents born after 1982; members may have elected 4% or 6% since 1 Jan 2024. The entrepreneur-account tax rate (20/22/24/26%) depends on this election. Conservative default: 2% (statutory default); 0% for non-members. Verify in Pensionikeskus before applying 4%/6%. Flag for reviewer: Confirm the individual's actual funded-pension rate before computing.

### 6.6 2025 Basic-Exemption Taper Band

- **2025 taper band reviewer notes** — For 2025 income between 14,400 and 25,200, the exemption tapers by formula and is sensitive to total annual income (including non-FIE income). Conservative default: Compute from the taper formula; if income > 25,200, BE = 0. Flag for reviewer: Confirm total annual income from all sources before applying the 2025 taper.

### 6.7 Pensionable-Age Status

- **Pensionable-age status reviewer notes** — The fixed 9,312 EUR exemption and the UI employee exemption depend on having reached pensionable age (born 1961 or earlier for the fixed exemption). Conservative default: Assume not pensionable age unless confirmed. Flag for reviewer: Confirm date of birth before applying any pensionable-age treatment.

## Section 7 -- Excel Working Paper Template

ESTONIA PERSONAL INCOME TAX -- FORM A / FORM E WORKING PAPER
Tax Year: 2025 / 2026   (CONFIRM -- rules differ)
Client: ___________________________
Residency: Resident / Non-resident
Date of birth: ____________   Pensionable age: Yes / No
Funded-pension rate: 0% / 2% / 4% / 6%
Basic-exemption application filed with employer? Yes / No

A. FORM E -- GROSS FIE BUSINESS INCOME
  A1. Client payments (net of VAT if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, etc.)       ___________
  A3. Other business income / revenue grants        ___________
  A4. TOTAL gross business income                    ___________

B. FORM E -- DEDUCTIBLE BUSINESS EXPENSES
  B1. Office rent                                    ___________
  B2. Business insurance                             ___________
  B3. Accountancy / legal fees                       ___________
  B4. Office supplies                                ___________
  B5. Software subscriptions                         ___________
  B6. Marketing / advertising                        ___________
  B7. Bank charges / payment processing fees         ___________
  B8. Training / professional subscriptions          ___________
  B9. Travel (flights, hotels, transport)            ___________
  B10. Telecoms (business % of phone/internet)       ___________
  B11. Home office (% of utilities/rent)             ___________
  B12. Vehicle expenses (business %)                 ___________
  B13. Business assets (FLAG for reviewer)           ___________
  B14. Other allowable expenses                      ___________
  B15. TOTAL deductible expenses                     ___________

C. NET BUSINESS PROFIT (A4 - B15)                   ___________

D. FORM A -- OTHER INCOME
  D1. Employment income (already withheld via TSD)   ___________
  D2. Rental income                                  ___________
  D3. Investment income (interest, dividends)        ___________
  D4. Pension income                                 ___________
  D5. TOTAL other income                             ___________

E. TOTAL ANNUAL INCOME (C + D5)                     ___________

F. BASIC EXEMPTION
  F1. 2025: if E<=14,400 -> 7,848;
      if 14,400<E<=25,200 -> 7,848 - 7,848/10,800 x (E-14,400);
      if E>25,200 -> 0
      2026 (under pension age): 8,400
      Pensionable age: 9,312                          ___________

G. INCOME TAX
  G1. Income-tax base (E - F1, floor 0)              ___________
  G2. Income tax = G1 x 22%                           ___________
  G3. Less: advance payments / amounts withheld       ___________
  G4. Income tax due (by 1 Oct) / refund             ___________

H. SOCIAL TAX (FIE -- tracked separately)
  H1. Social tax = C x 33% (cap 35,085.60 in 2025)   ___________
  H2. Less: quarterly advances paid                   ___________
  H3. Social tax balance                              ___________

REVIEWER FLAGS:
  [ ] Tax year confirmed (2025 vs 2026)?
  [ ] Residency confirmed?
  [ ] Date of birth confirmed (pensionable age / pension status)?
  [ ] Funded-pension rate confirmed (0/2/4/6%)?
  [ ] 2025 taper band income confirmed (if 14,400-25,200)?
  [ ] Basic-exemption application status confirmed?
  [ ] VAT registration status confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with log?
  [ ] Phone/internet business % confirmed?
  [ ] FIE durable-asset treatment confirmed?
  [ ] Social tax excluded from income-tax base?
  [ ] All T2 items flagged for review?

## Section 8 -- Bank Statement Reading Guide

### Estonian Bank Statement Formats

**Estonian Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Swedbank | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; date format DD.MM.YYYY |
| SEB | PDF, CSV | Date, Beneficiary/Payer, Amount, Balance | Card transactions show merchant |
| LHV Pank | CSV, PDF | Date, Counterparty, Amount, Description | Clean data; hosts the entrepreneur account (ettevõtluskonto) |
| Luminor | PDF, CSV | Date, Description, Amount, Balance |  |
| Wise / Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Multi-currency -- use EUR amounts |

### Key Estonian Banking / Tax Terms

**Key Estonian Banking / Tax Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| ÜLEKANNE / TRF | Transfer | Check direction for income/expense |
| MAKSE | Payment | Check direction and counterparty |
| OTSEKORRALDUS | Direct debit | Regular expense (utility, subscription) |
| PÜSIMAKSE | Standing order | Regular expense (rent, loan) |
| KAARDIMAKSE / KAART | Card payment | Expense -- check merchant |
| LAEKUMINE | Incoming receipt | Potential income |
| TEENUSTASU | Service fee / bank charge | Deductible (business account) or platform fee |
| INTRESS | Interest | Interest income (Form A) or bank charge |
| ARVE | Invoice | Reference to a sales/purchase invoice |
| PALK / TÖÖTASU | Salary / wages | Employment income (Form A) |
| ÜÜR | Rent | Rental income/expense -- check direction |
| TULUMAKS | Income tax | Tax payment -- not deductible |
| SOTSIAALMAKS | Social tax | FIE charge -- track separately, not a deduction |
| KÄIBEMAKS / KMD | VAT | VAT liability payment -- exclude |
| TAGASTUS | Refund | Tax refund (exclude) |
| SULARAHA / ATM | Cash withdrawal | Ask what cash was spent on |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ESTONIA PERSONAL INCOME TAX
1. Which tax year? (2025 or 2026 -- the rules differ materially.)
2. Are you an Estonian tax resident?
3. Status: self-employed (FIE), employed, entrepreneur account, or a mix?
4. Date of birth? (affects pensionable-age exemption and funded-pension status)
5. Funded (II pillar) pension rate: 0%, 2%, 4%, or 6%?
6. Did you file a basic-exemption application with your employer?
7. Total annual income from ALL sources? (needed for the 2025 basic-exemption taper)
8. VAT registered? Standard rate 24% from 1 Jul 2025; threshold 40,000 EUR turnover.
9. Home office: dedicated room or shared space? If dedicated, what % of floor area?
10. Vehicle: do you use a car for business? What % is business use? Do you keep a log?
11. Phone/internet: what % is business use?
12. FIE social-tax advances paid during the year?
13. Any other income (employment, rental, dividends, interest, pension)?
14. Any equipment / durable assets purchased during the year?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**  _(Key Legislation / Authority References table)_

| Topic | Reference |
| --- | --- |
| Income tax rate (flat 22%) | Income Tax Act (TuMS); EMTA tax rates |
| Basic exemption | TuMS; EMTA "Calculation of basic exemption" |
| Social tax (33%) | Social Tax Act (SMS); EMTA "Social tax" |
| Unemployment insurance | Unemployment Insurance Act; EMTA |
| Funded pension (II pillar) | Funded Pensions Act; PwC |
| FIE business income | TuMS; EMTA "Self-employed persons -- income tax" |
| Entrepreneur account | TuMS; EMTA "Entrepreneur account" |
| VAT | Value-Added Tax Act (Käibemaksuseadus); EMTA |
| Filing & deadlines | EMTA "Income tax returns for 2025" |
| Penalties & interest | Taxation Act (MKS); EMTA "Payment of interests" |

### Authoritative Sources

**Authoritative Sources**  _(Authoritative Sources table)_

| Title | Publisher | URL |
| --- | --- | --- |
| Tax rates | EMTA | https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates |
| Calculation of basic exemption | EMTA | https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption |
| Social tax | EMTA | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax |
| Self-employed persons -- social tax | EMTA | https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/social-tax |
| Self-employed persons -- income tax | EMTA | https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/income-tax |
| Unemployment insurance premiums | EMTA | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums |
| Entrepreneur account | EMTA | https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/entrepreneur-account |
| Income tax returns for 2025 | EMTA | https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/income-tax-returns-2025 |
| Payment of interests | EMTA | https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests |
| Obligation to register (VAT) | EMTA | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer/obligation-register-taxable-person |
| Estonia -- Individual -- Other taxes | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/estonia/individual/other-taxes |
| Significant tax changes in Estonia 2025-2026 | EY Estonia | https://www.ey.com/en_ee/insights/tax/significant-tax-changes-in-estonia-in-2025-2026 |
| Security Tax Abolished; VAT and Income Tax (income rise later cancelled) | Estonian Chamber of Commerce and Industry | https://www.koda.ee/en/news/security-tax-abolished-vat-and-income-tax-rise-24 |
| Estonia's 946 EUR minimum wage agreement | ERR News (Estonian Public Broadcasting) | https://news.err.ee/1609943096/employers-and-unions-agree-on-946-as-estonia-s-new-minimum-wage |

### Important Distinction -- Two Separate EUR 886 Figures

**Important Distinction -- Two Separate EUR 886 Figures**  _([ERR News; EMTA]; [EMTA, Social tax])_

| Figure | What it is | Year | Source |
| --- | --- | --- | --- |
| 886 EUR/month | Minimum **wage** (miinimumpalk) | 2025 | [ERR News; EMTA] |
| 886 EUR/month | Social-tax **monthly base** (820 EUR in 2025) | 2026 | [EMTA, Social tax] |

- **886 EUR figures are separate legal concepts** — These coincide numerically but are separate legal figures and must not be conflated when wiring formulas.  _([ERR News; EMTA]; [EMTA, Social tax])_

### Test Suite

Input: Gross 2,000 EUR/mo, born after 1982 (pension 2%), basic-exemption application filed (BE 654/mo), single employer.
Expected: UI 32.00, pension 40.00, income-tax base 1,274.00, income tax 280.28, net pay 1,647.72. Employer cost = 2,000 + 660.00 social tax + 16.00 UI = 2,676.00.

Input: Gross 2,000 EUR/mo, born after 1982 (pension 2%), NO application filed.
Expected: UI 32.00, pension 40.00, income-tax base = 2,000 - 32 - 40 = 1,928.00, income tax = 1,928.00 x 22% = 424.16, net pay = 2,000 - 32 - 40 - 424.16 = 1,503.84.

Input: Business income 50,000, deductions 20,000, born after 1982, no other income.
Expected: profit 30,000; basic exemption 0 (income > 25,200); income tax = 30,000 x 22% = 6,600.00; social tax = 30,000 x 33% = 9,900.00 (below cap); total Estonian tax 16,500.00.

Input: 2025, total annual income 18,000 (single income stream).
Expected: BE = 7,848 - 7,848/10,800 x (18,000 - 14,400) = 7,848 - 7,848/10,800 x 3,600 = 7,848 - 2,616.00 = 5,232.00. Income-tax base = 18,000 - 5,232.00 = 12,768.00; income tax = 12,768.00 x 22% = 2,808.96.

Input: 2026, under pension age, total income 45,000 (FIE net 32,000 + employment 13,000).
Expected: 2026 basic exemption = 8,400 (fixed, no taper); income-tax base = 45,000 - 8,400 = 36,600.00; income tax = 36,600.00 x 22% = 8,052.00. (In 2025 the exemption would have been 0 because income > 25,200.)

Input: 2026, pensionable age, total income 12,000 (pension + small FIE).
Expected: basic exemption = 9,312 (pensionable age, fixed); income-tax base = 12,000 - 9,312 = 2,688.00; income tax = 2,688.00 x 22% = 591.36.

Input: 2025, entrepreneur account, receipts 30,000, no 4%/6% pension election.
Expected: business income tax = 30,000 x 20% = 6,000.00 (bundles income tax + social tax). Below 40,000 -- no FIE/company registration required. (40% rate over 25,000 abolished from 1 Jan 2025.)

Input: Business profit 120,000.
Expected: uncapped social tax = 120,000 x 33% = 39,600.00, but it is capped at 35,085.60; income tax = 120,000 x 22% = 26,400.00 (basic exemption 0).

Input: 2025, FIE, EUR 64.20 supermarket purchase claimed as expense.
Expected: remove from Form E. Not deductible -- private living cost.

Input: FIE attempts to deduct social tax of 9,900 from profit before computing income tax.
Expected: reject. Social tax is not deductible from the income-tax base; income tax is computed on profit before social tax.

## PROHIBITIONS

- **Confirm residency before computing tax** — NEVER compute Estonian tax without confirming residency (resident vs non-resident)
- **Monthly basic exemption requires employer application** — NEVER apply the monthly basic exemption in payroll unless the employee filed an application with that employer
- **Basic exemption taper above 14,400 in 2025** — NEVER apply the full 7,848 EUR (2025) basic exemption when annual income exceeds 14,400 -- use the taper; zero above 25,200
- **8,400 EUR exemption is 2026-only** — NEVER apply the fixed 8,400 EUR basic exemption to a 2025 computation -- that is the 2026 figure
- **Confirm date of birth before pensionable-age/UI exemptions** — NEVER apply the pensionable-age exemption or UI exemption without confirming date of birth
- **Income tax rate remains 22% for 2026** — NEVER use the cancelled 24% income-tax rate or the defence/security tax for 2026 -- the rate stays 22%
- **Social tax not deductible from FIE base** — NEVER deduct social tax from the FIE income-tax base
- **No deduction of income tax, fines, penalties, interest** — NEVER deduct income tax itself, fines, penalties, or late-payment interest
- **Exclude VAT collected from Form E business income** — NEVER include VAT collected on sales in Form E business income for VAT-registered persons
- **Social-tax advance / VAT payment not a business expense** — NEVER treat an FIE quarterly social-tax advance, or a VAT payment, as a Form E business expense
- **Confirm funded-pension rate election** — NEVER assume a 4%/6% funded-pension rate without confirming membership and election in Pensionikeskus
- **Do not conflate minimum wage with social-tax base** — NEVER conflate the 886 EUR minimum wage with the social-tax monthly base
- **Label calculations as estimated** — NEVER present tax calculations as definitive -- always label as estimated and pass the income-tax base to the deterministic engine

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
