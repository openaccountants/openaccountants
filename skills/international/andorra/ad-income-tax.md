---
name: andorra-income-tax
description: Use this skill whenever asked about Andorra personal income tax (IRPF — Impost sobre la Renda de les Persones Físiques) for residents or self-employed individuals. Trigger on phrases like "how much tax do I pay in Andorra", "IRPF Andorra", "income tax return Andorra", "declaració IRPF", "self-employed Andorra", "autònom Andorra", "compte propi", "CASS contributions", "social security Andorra", "move to Andorra taxes", "Andorra tax residency", "183 days Andorra", or any question about computing, filing, or planning income tax for an Andorran tax resident. Also trigger when reviewing IRPF deductions (housing, dependants, education), CASS social security brackets, IGI registration thresholds, or non-resident withholding (IRNR) on Andorra-source income. This skill covers IRPF rates and brackets, the bonificació mechanism, savings base exemption, CASS contribution tables for employed and self-employed workers, IGI (indirect tax) obligations, penalties, real-estate capital gains, and double taxation agreements. ALWAYS read this skill before touching any Andorra income tax work.
jurisdiction: AD
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# andorra-income-tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Andorra (Principat d'Andorra) |
| Tax | IRPF — Impost sobre la Renda de les Persones Físiques |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Llei 5/2014, del 24 d'abril, de l'impost sobre la renda de les persones físiques |
| Tax authority | Departament de Tributs i de Fronteres (DTF) |
| Filing portal | Seu Electrònica / e-tramits.ad |
| Filing deadline | 1 April -- 30 September of the following year (e-tramits.ad) |
| Social security authority | Caixa Andorrana de Seguretat Social (CASS) |
| Minimum wage (SMI 2025) | EUR 1,447.33/month gross (5.2% increase from 2024; augelegalfiscal.com) |
| Validated by | Pending — requires sign-off by a licensed Andorran tax advisor or equivalent |
| Validation date | Pending |
| Skill version | 0.1 |

### IRPF Rate Brackets -- General Tax Base (Base General) 2025

**IRPF Rate Brackets -- General Tax Base (Base General) 2025**  _(e-tramits.ad; invicoandorra.com; andorra-solutions.com)_

| Annual Taxable Income (EUR) | Nominal Rate | Bonificació | Net Tax on Band | Cumulative Tax at Top of Band |
| --- | --- | --- | --- | --- |
| 0 -- 24,000 | 0% | n/a | EUR 0 | EUR 0 |
| 24,001 -- 40,000 | 10% | Up to EUR 800 | EUR 800 on full EUR 16,000 band | EUR 800 |
| Above 40,000 | 10% | None | 10% × excess | EUR 800 + 10% × (income − 40,000) |

Covers employment income, self-employment/business income, rental income.
Source: e-tramits.ad; invicoandorra.com; andorra-solutions.com

**Mechanism for the 5% effective band (24,001–40,000):** The law imposes a 10% rate but grants a bonificació (bonus rebate) of up to EUR 800 for income in this band. EUR 16,000 × 10% = EUR 1,600 gross tax; EUR 1,600 − EUR 800 = EUR 800 net tax → effective rate ~5% on the band. (invicoandorra.com; andorra-solutions.com)

**Key point:** There is no separate personal allowance — the EUR 24,000 zero-rate band IS the personal allowance.

### IRPF Rate -- Savings Tax Base (Base de l'Estalvi) 2025

**IRPF Rate -- Savings Tax Base (Base de l'Estalvi) 2025**  _(invicoandorra.com; andorrainc.com)_

| Annual Savings Income (EUR) | Rate |
| --- | --- |
| 0 -- 3,000 | 0% (exempt) |
| Above 3,000 | 10% on excess |

### CASS Contribution Rates (salaried employees and self-employed)

**CASS Contribution Rates**  _(remotepeople.com; en.wikipedia.org/wiki/Caixa_Andorrana_de_Seguretat_Social)_

| Branch | Employee | Employer | Self-Employed (Compte Propi) |
| --- | --- | --- | --- |
| General Branch | 3.0% | 7.0% | 10.0% |
| Retirement Branch | 3.5% | 8.5% | 12.0% |
| **Total** | **6.5%** | **15.5%** | **22.0%** |

Employer handles full remittance of both employee and employer shares monthly.
No explicit published ceiling for salaried employee contribution base — applies to full actual gross salary. [RESEARCH GAP — reviewer to confirm ceiling directly with CASS: public@cass.ad / +376 870 870]

### CASS Self-Employed Monthly Contribution Brackets (2025)

**CASS Self-Employed Monthly Contribution Brackets (2025)**  _(cass.ad/cotitzacions-del-treballadors-per-compte-propi; elysiumconsultingfirm.com)_

| % of Base | Monthly Base (EUR) | Monthly Quota (EUR) | Applicable Bracket |
| --- | --- | --- | --- |
| 25% | 668.13 | 146.99 | Net income < EUR 6,000 + specific conditions |
| 50% | 1,525.33 | 335.57 | Net income EUR 6,000 -- 12,000 |
| 62.5% | 1,670.33 | 367.47 | Net income EUR 12,000 -- 18,000 |
| 75% | 2,004.39 | 440.97 | Net income EUR 18,000 -- 24,000 |
| 100% | 2,672.52 | 587.95 | Standard rate |
| 125% | 3,340.65 | 734.94 | Net income > EUR 40,000 |
| 137.5% | 3,674.72 | 808.44 | Net income > EUR 50,000 |

Reference base (100%): EUR 2,672.52/month — official CASS website (cass.ad, updated 30 January 2025).
Note: Secondary sources citing Decree 16/2025 (published 29 January 2025) use EUR 2,560.99 as the 100% base. The cass.ad official page should be used as the filing reference.

Monthly quota = monthly base × 22%. Verify: EUR 2,672.52 × 22% = EUR 587.95 ✓; EUR 3,340.65 × 22% = EUR 734.94 ✓; EUR 3,674.72 × 22% = EUR 808.44 ✓

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP — do not compute IRPF without confirming ≥183-day presence or principal economic interests |
| Unknown spousal income | Do not apply the EUR 40,000 spousal threshold uplift |
| Unknown CASS bracket | Apply 100% base (EUR 587.95/month) — highest safe assumption for standard rate |
| Unknown IGI registration status | Assume not registered if turnover < EUR 40,000 |
| Unknown housing deduction basis | 0% — do not apply without mortgage/rental documentation |
| Unknown dependent status | 0 dependants — do not apply deductions without documentation |
| Unknown capital gains holding period | Apply highest applicable rate |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — full-year bank statement (CSV, PDF, or pasted text) plus confirmation of: (1) fiscal residency status (≥183 days in AD, or principal economic interests in AD), (2) employment or self-employment status, (3) family situation (single / married or de facto partner / dependent children or ascendants), (4) NRT (Número de Registre Tributari).

**Recommended** — all sales invoices, purchase invoices/receipts, CASS contribution payment records, prior-year IRPF declaration, employer IRPF withholding certificate (if employed), mortgage or rental contract (if claiming housing deduction), tuition receipts (if claiming education deduction).

**Ideal** — complete income and expenditure account, asset register, CASS annual declaration, all documentation for deductions, employer withholding certificate showing total income and tax withheld.

**Refusal if minimum is missing — SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This IRPF declaration was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the wholly-and-exclusively test is met."

### Refusal Catalogue

- **R-AD-1** — Residency status unclear. "Andorran fiscal residency requires ≥183 days physical presence, or principal economic interests in Andorra, or primary family ties in Andorra. This skill cannot determine tax liability without confirming residence status. Please confirm before proceeding."  _(e-tramits.ad)_
- **R-AD-2** — Non-resident income (IRNR). "Non-resident Andorran source income is taxed under the IRNR regime at flat 10% (payer withholds). Scope of this skill is limited to fiscal residents. For IRNR analysis, use the dedicated IRNR section below or escalate to a licensed Andorran advisor."
- **R-AD-3** — Corporate / entity income. "This skill covers natural persons (IRPF) only. Andorran companies and branches file under the Impost de Societats (IS) at 10%. Escalate to an Andorran advisor."
- **R-AD-4** — Complex capital gains (real estate). "Real-estate capital gains require verification of purchase date, cost base, notarial fees, and reinvestment details. Out of scope for automated classification. Escalate to a licensed Andorran advisor."
- **R-AD-5** — Arrears / enforcement. "Client has outstanding IRPF or CASS arrears or is subject to DTF enforcement. Late payment surcharges of 10%–20% plus formal sanctions (EUR 500–EUR 20,000) may apply. Do not advise on quantum without advisor involvement. Escalate immediately."
- **R-AD-6** — IGI return requested. "This skill covers IRPF (direct tax) only. For IGI (indirect tax / VAT equivalent), use the andorra-igi skill."
- **R-AD-7** — Inheritance, gifts, wealth. "Andorra has no inheritance tax, gift tax, or wealth tax. These are out of scope. Simply note the absence and confirm no filing required."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier for Andorran bank statements. When a transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description. If multiple patterns match, use the most specific. All amounts are in EUR.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | IRPF Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFERÈNCIA, PAGAMENT, INGRÉS, PAYMENT | General base — business income | Full credit = gross revenue | If IGI-registered, extract net (excl. 4.5% IGI) |
| HONORARIS, FEES, PROFESSIONAL FEES, CONSULTORIA | General base — business income | Professional fees | Typical for autònom |
| STRIPE PAYOUT, STRIPE TRANSFER | General base — business income | Platform payout | Match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | General base — business income | Platform payout | Verify against invoices |
| WISE PAYOUT, WISE TRANSFER | General base — business income | International payout | Use EUR equivalent |
| REVOLUT PAYOUT | General base — business income | Check if business or personal Revolut |  |
| SALARI, NÒMINA, SALARY, EMPLOYER [name] | General base — employment income | Employment income | Employer withholds IRPF and CASS |
| LLOGUER, RENDA, RENT RECEIVED | General base — rental income | Rental income |  |
| INTERESSOS, INTEREST RECEIVED | Savings base | Investment income | First EUR 3,000/year exempt |
| DIVIDEND ANDORRÀ, DIVIDEND ANDORRAN | EXEMPT | Dividends from Andorran companies: fully exempt | Already taxed at corporate level (andorrainc.com) |
| DIVIDEND, DIVIDEND ESTRANGER | Savings base | Foreign dividends: savings base, first EUR 3,000 exempt |  |
| PLUSVÀLUA, CAPITAL GAIN | Savings base or general (depends on asset) | Flag for reviewer classification | Holding period critical |
| DTF DEVOLUCIÓ, TAX REFUND, DEVOLUCIÓ IMPOST | EXCLUDE | Not income — prior year refund |  |
| SUBVENCIÓ, GRANT, GOVERN | Check nature | Revenue grants = income; capital grants = EXCLUDE |  |

### 3.2 Expense Patterns (Debits) -- Fully Deductible (Business Expenses)

**3.2 Expense Patterns (Debits) -- Fully Deductible (Business Expenses)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LLOGUER OFICINA, OFFICE RENT, DESPATX [commercial] | Office rent | Fully deductible | Dedicated business premises |
| ASSEGURANÇA PROFESSIONAL, PROFESSIONAL INDEMNITY | Professional insurance | Fully deductible |  |
| GESTOR, ASSESSOR, COMPTABLE, ACCOUNTANT, ACCA | Accountancy / advisory fees | Fully deductible |  |
| ADVOCAT, NOTARI, LEGAL, LAWYER (business) | Legal/notarial fees | Fully deductible | Must be business-related |
| MATERIAL OFICINA, STATIONERY, OFFICE SUPPLIES | Office supplies | Fully deductible |  |
| PUBLICITAT, MARKETING, GOOGLE ADS, META ADS | Marketing / advertising | Fully deductible |  |
| FORMACIÓ, CPD, CURS, SEMINAR, TRAINING | Training / CPD | Fully deductible | Must relate to current activity |
| COL·LEGI PROFESSIONAL, PROFESSIONAL BODY, SUBSCRIPTION | Professional subscriptions | Fully deductible |  |
| COMISSIÓ BANCÀRIA, COMISSIONS, BANK FEE, BANK CHARGE | Bank charges | Fully deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Fully deductible |  |
| DOMINI, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Fully deductible (if under capitalisation threshold) | Recurring hosting = expense |
| CORREUS, MISSATGERIA, POSTAGE (business) | Postage / courier | Fully deductible | Business correspondence |

### 3.3 Expense Patterns (Debits) -- SaaS and Software (Fully Deductible if Recurring Subscription)

**3.3 Expense Patterns (Debits) -- SaaS and Software (Fully Deductible if Recurring Subscription)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Fully deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Fully deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Fully deductible |  |
| SOFTWARE LLICÈNCIA (perpetual, high value) | Capital item | Capitalise — flag for reviewer | Perpetual licence = asset; rate [RESEARCH GAP — reviewer to confirm Andorran depreciation schedule] |

### 3.4 Expense Patterns (Debits) -- Utilities (May Need Apportionment)

**3.4 Expense Patterns (Debits) -- Utilities (May Need Apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| FEDA (Forces Elèctriques d'Andorra), ELECTRICITAT | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| ANDORRA TELECOM, TELEFON, INTERNET, FIBRA | Telecoms / broadband | T2 | Business use portion only; default 0% if mixed |
| MÒBIL, MOBILE, PHONE | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**3.5 Expense Patterns (Debits) -- Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| VUELO, AVIÓ, RYANAIR, VUELING, IBERIA | Flights | Deductible if wholly business travel |  |
| HOTEL, BOOKING.COM, AIRBNB (business) | Accommodation | Deductible if wholly business travel |  |
| TAXI, TRANSFER, BOLT, UBER | Local transport | Deductible if business purpose |  |
| GASOLINERA, GASOLINA, FUEL, CARBURANT | Vehicle fuel | T2 — business % only | Requires mileage log |
| APARCAMENT, PARKING | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINAR, SOPAR, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | No partial deduction |
| PERSONAL, SUPERMERCATS, SUPERMERCAT, CONSUM, LIDL | Personal expenses | NOT deductible | Private living costs |
| MULTA, SANCIÓ, FINE, PENALTY | Fines / penalties | NOT deductible | Public policy |
| DTF PAGAMENT, IRPF PAGAMENT, TAX PAYMENT | Income tax payments | NOT deductible | Tax on income cannot reduce income |
| RETIRADA, EXTRACCIÓ, ATM (personal) | Drawings | NOT deductible | Not an expense |
| QUOTA SOCIAL, PARTICIPACIÓ (own company) | Capital investment | NOT deductible | Capital outflow |

### 3.7 Exclusions (Neither Income nor Expense)

**3.7 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERÈNCIA PRÒPIA, ENTRE COMPTES, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| RETORN PRÉSTEC, AMORTITZACIÓ PRÉSTEC, LOAN REPAYMENT | EXCLUDE | Loan principal movement |
| CASS, COTITZACIÓ CASS, SEGURETAT SOCIAL | CASS deduction line | Deductible in IRPF (6.5% employee share or self-employed quota), NOT as a business expense |
| IGI PAGAMENT, CFR IGI | EXCLUDE | IGI liability payment — not an expense |
| INGRÉS PROPI, TRANSFERÈNCIA INTERNA | EXCLUDE | Internal transfer |

### 3.8 Andorran Banks -- Statement Format Reference

**3.8 Andorran Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Crèdit Andorrà | TRANSFERÈNCIA, DOMICILIACIÓ, COMISSIÓ | PDF/CSV; description contains counterparty + reference |
| Banca Privada d'Andorra (BPA) | TRANSFER, TRF, CARRER | PDF; dates DD/MM/YYYY |
| MoraBanc | TRANSFERÈNCIA, REBUT, COMISSIÓ | PDF/CSV; merchant name in description |
| Andbanc | TRANSFERÈNCIA, D.D., COMISSIONS | PDF/CSV |
| Vall Banc | INGRÉS, CÀRREC, DOMICILIACIÓ | PDF |
| Revolut Business | PAYMENT, TRANSFER, CARD PAYMENT | CSV; clean counterparty names; multi-currency — use EUR |
| Wise Business | TRANSFER, CONVERSION, FEE | CSV; multi-currency — use EUR amounts |

## Section 4 -- Worked Examples

### Example 1 -- Single Resident Autònom, Mid-Range Income

**Profile:** Single, no dependants, self-employed consultant, Andorran resident (≥183 days).
**Gross business revenue:** EUR 55,000
**Business expenses (deductible):** EUR 9,000
**CASS quota (100% bracket):** EUR 587.95/month × 12 = EUR 7,055.40/year
**General expenses deduction:** 3% × (EUR 55,000 − EUR 9,000 − EUR 7,055.40) = 3% × EUR 38,944.60 = EUR 1,168.34 → capped at **EUR 400**

**Computation**

| Step | Amount (EUR) |
| --- | --- |
| Gross revenue | 55,000.00 |
| Less: business expenses | (9,000.00) |
| Less: CASS self-employed quota (deductible) | (7,055.40) |
| Sub-total | 38,944.60 |
| Less: general expenses deduction (capped) | (400.00) |
| IRPF general base (taxable) | 38,544.60 |
| Tax on EUR 0–24,000 at 0% | 0.00 |
| Tax on EUR 24,001–38,544.60 (band of EUR 14,544.60): 10% = EUR 1,454.46 minus bonificació EUR 800 (partial band) | 654.46 |
| **Total IRPF due** | **654.46** |

Bonificació note: The EUR 800 bonificació applies when income exceeds EUR 40,000 (using the full band). Here income is EUR 38,544.60 — within the EUR 24,001–40,000 band. The bonificació is proportionally available up to EUR 800. At full band occupancy: EUR 16,000 × 10% − EUR 800 = EUR 800 at EUR 40,000. At EUR 38,544.60, taxable in band = EUR 14,544.60; gross tax EUR 1,454.46; bonificació = EUR 800 (maximum); net tax = EUR 654.46.

**Representative bank statement lines used:**
```
15/01/2025 ; Crèdit Andorrà TRANSFERÈNCIA ENTRADA ; CLIENT GLOBAL SA ; FACTURA 2025-001 ; +5,450.00 ; EUR
03/02/2025 ; MoraBanc CÀRREC ; ANDORRA TELECOM ; FIBRA OPTICA FEB ; -89.00 ; EUR
01/03/2025 ; Crèdit Andorrà CÀRREC ; GOOGLE WORKSPACE ; SUB MAR 2025 ; -12.00 ; EUR
10/03/2025 ; Andbanc CÀRREC ; CASS QUOTA FEB ; COTITZACIÓ ; -587.95 ; EUR
```

### Example 2 -- Resident with Spouse (Zero Income Partner)

**Profile:** Married, spouse earns EUR 0, single earner. Gross employment income EUR 36,000.
**Employer withholds IRPF** (no provisional tax for employee).
**Spousal relief:** If spouse earns zero, the effective zero-rate band rises to EUR 40,000 (lavallassociats.com; andorra-solutions.com).

**Computation**

| Step | Amount (EUR) |
| --- | --- |
| Gross employment income | 36,000.00 |
| Less: employee CASS (6.5%) | (2,340.00) |
| Less: general expenses deduction (3% × EUR 33,660 = EUR 1,009.80, capped) | (400.00) |
| IRPF general base | 33,260.00 |
| Applied threshold with spousal relief = EUR 40,000 | — |
| Income EUR 33,260 is below EUR 40,000 spousal threshold | 0.00 |
| **Total IRPF due** | **0.00** |

Without spousal relief: EUR 33,260 − EUR 24,000 = EUR 9,260 in 10% band; gross tax EUR 926 − EUR 800 bonificació = EUR 126 due. The spousal relief eliminates this entirely.

**Representative bank statement lines used:**
```
28/02/2025 ; Vall Banc INGRÉS ; EMPRESA XYZ SL ; NÒMINA FEB 2025 ; +3,000.00 ; EUR
```

### Example 3 -- Savings Base (Foreign Dividends)

**Computation**

| Step | Amount (EUR) |
| --- | --- |
| Foreign dividends received | 8,000.00 |
| Less: savings base exemption | (3,000.00) |
| Taxable savings base | 5,000.00 |
| IRPF at 10% | 500.00 |
| **Total savings base IRPF due** | **500.00** |

**Profile:** Resident, receives EUR 8,000 in foreign dividends, no other savings income.

Note: Andorran company dividends = EUR 0 IRPF (fully exempt). Only foreign dividends are on the savings base. (andorrainc.com)

**Representative bank statement line:**
```
15/04/2025 ; MoraBanc INGRÉS ; BROKER INTERNACIONAL SA ; DIVIDEND ACCIÓ XYZ ; +8,000.00 ; EUR
```

### Example 4 -- New Autònom (Start-of-Activity CASS Reduction)

**Profile:** Single, first year of self-employment (newly registered, not previously registered for ≥36 months). Net income for year EUR 18,000. Eligible for 25% CASS base.

**CASS (first 12 months, 25% base, start-of-activity regime):**
25% base = EUR 668.13/month. Only general branch (10%): EUR 668.13 × 10% = EUR 66.81/month.
Annual CASS = EUR 66.81 × 12 = EUR 801.72.
(Note: no pension points accrued; limited health coverage — elysiumconsultingfirm.com)

**IRPF computation**

| Step | Amount (EUR) |
| --- | --- |
| Gross revenue | 18,000.00 |
| Less: business expenses (assumed EUR 2,000) | (2,000.00) |
| Less: CASS paid | (801.72) |
| Sub-total | 15,198.28 |
| Less: general expenses deduction (3% capped at EUR 400) | (400.00) |
| IRPF general base | 14,798.28 |
| Tax on EUR 0–14,798.28 at 0% (below EUR 24,000 threshold) | 0.00 |
| **Total IRPF due** | **0.00** |

### Example 5 -- High-Income Autònom (125% CASS Bracket)

**Profile:** Single, no dependants. Net income EUR 48,000. CASS at 125% bracket (net income > EUR 40,000).

**CASS:** EUR 734.94/month × 12 = EUR 8,819.28/year

**IRPF computation**

| Step | Amount (EUR) |
| --- | --- |
| Net business profit | 48,000.00 |
| Less: CASS quota | (8,819.28) |
| Less: general expenses deduction (3% × EUR 39,180.72 = EUR 1,175.42, capped at EUR 400) | (400.00) |
| IRPF general base | 38,780.72 |
| Tax on EUR 0–24,000 at 0% | 0.00 |
| Tax on EUR 24,001–38,780.72: band = EUR 14,780.72; gross 10% = EUR 1,478.07; minus bonificació EUR 800 | 678.07 |
| **Total IRPF due** | **678.07** |

### Example 6 -- Real-Estate Capital Gain (Held 3 Years, Resident)

**Profile:** Resident sells apartment purchased 3 years ago. Purchase price EUR 200,000; sale price EUR 250,000. Gain = EUR 50,000.

Holding period 2–10 years: rate is 10% (decreasing by 1% per year from year 2; at year 3 = approximately 9%, but confirm exact schedule with DTF [RESEARCH GAP — exact year-by-year rate step-down not fully confirmed from reviewed sources]).

Using 10% conservative:

**Computation**

| Step | Amount (EUR) |
| --- | --- |
| Sale price | 250,000.00 |
| Less: purchase price | (200,000.00) |
| Capital gain | 50,000.00 |
| IRPF at 10% (conservative; reviewer to confirm exact year-3 rate) | 5,000.00 |
| **Estimated IRPF on gain** | **5,000.00** |

Reinvestment exemption: if reinvesting in primary residence within 6 months → EUR 0 IRPF. Flag for reviewer.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Fiscal Residency Test

- **Fiscal residency test** — A natural person is an Andorran fiscal resident if any one of the following is satisfied: physically present in Andorra for more than 183 days in the calendar year (border data is used to verify), OR their principal centre of economic interests is in Andorra, OR their primary family ties are in Andorra. If residency is uncertain: STOP and apply Refusal R-AD-1.  _(Llei 5/2014 (IRPF); e-tramits.ad)_

### 5.2 Income Classification

**5.2 Income Classification**

| Base | Included Income |
| --- | --- |
| General base (base general) | Employment income; self-employment / business income; rental income |
| Savings base (base de l'estalvi) | Interest; foreign dividends; financial capital gains |

- **Andorran company dividends exclusion** — Andorran company dividends: fully exempt. Do not include in either base.  _(andorrainc.com)_

### 5.3 IRPF Rate Application (General Base)

- **IRPF rate application steps** — 1. Compute net income in general base (revenue minus deductible expenses minus CASS). 2. Apply EUR 400 general expenses deduction (capped; 3% of income up to EUR 400). 3. Apply any family/housing deductions (see 5.5). 4. Apply zero-rate band: EUR 0–24,000 = EUR 0 tax. 5. Band EUR 24,001–40,000: gross tax 10% on band income, minus bonificació up to EUR 800. 6. Above EUR 40,000: 10% on excess, no bonificació. 7. Spousal relief: if spouse earns EUR 0, the zero-rate threshold rises to EUR 40,000 for the filing taxpayer.

### 5.4 Wholly-and-Exclusively Test

- **Wholly-and-exclusively test** — An expense is deductible only if incurred wholly and exclusively in the production of income. Mixed-use expenses must be apportioned. The apportionment method must be reasonable and documented.  _(General principle of Andorran IRPF; andorra-solutions.com)_

### 5.5 Key Deductions (2025)

**5.5 Key Deductions (2025)**  _(lavallassociats.com; aaa.ad; andorra-solutions.com)_

| Deduction | Amount (EUR) | Conditions |
| --- | --- | --- |
| General expenses deduction | 3% of income, max EUR 400/year | All residents automatically |
| Employee CASS contributions (6.5%) | Actual amount paid | Employed persons; fully deductible |
| Self-employed CASS quota | Actual quota paid | Autònom; fully deductible |
| Dependent child/ascendant | EUR 750 per dependent | Dependent: age <25 or >65, lives with taxpayer, earns <EUR 12,000/year |
| Additional dependent child (2025 new) | EUR 1,000 per dependent child | Child under 25, lives with taxpayer, earns below SMI (EUR 1,447.33/month) |
| Higher education supplement (2025 new) | EUR 300 per enrolled dependent | Dependent enrolled in university; requires tuition documentation |
| Primary residence acquisition (2025 new) | 50% of amounts paid, max EUR 5,000/year | Mortgage principal + interest + acquisition costs for primary home |
| Affordable rental investment (2025 new) | 50% of amounts paid, max EUR 5,000/year | Property rented at ≤EUR 12.45/m²; requires rental contract |
| Disability deductions | [RESEARCH GAP — reviewer to confirm exact amounts with DTF] | Various; confirm at impostos@govern.ad |

Maximum combined new child deduction per eligible child under 25 earning below SMI with university enrollment: EUR 1,000 + EUR 300 = EUR 1,300.

### 5.6 Non-Deductible Expenses

**5.6 Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Entertainment (client meals, events) | Personal consumption; not business purpose |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself (IRPF) | Tax on income |
| Drawings / personal withdrawals | Not an expense |
| Capital expenditure (undepreciated) | Must be depreciated — rate schedule [RESEARCH GAP — reviewer to confirm Andorran depreciation rates] |

### 5.7 Capital Gains Treatment

- **Share disposals (resident individuals)** — Taxpayer owns ≤25% of company: exempt. Shares held ≥10 years (any ownership %): exempt. Shares held 5–10 years: 50% reduction → effective ~5%. Shares held <5 years (ownership >25%): standard savings base rate 10%.  _(andorrainc.com; goldenharbors.com)_

**Real-estate capital gains (resident individuals)**  _(andorrainc.com; goldenharbors.com)_

| Holding Period | Rate |
| --- | --- |
| Within 2 years of purchase | 15% (10% + 5% speculative surcharge) |
| 2–10 years | 10% (declining by 1%/year from year 2; exact year-by-year schedule [RESEARCH GAP — reviewer to confirm with DTF]) |
| After 10 years | 0% (full exemption) |
| Reinvestment in primary residence within 6 months | Full exemption |

- **Non-residents capital gains rate** — Non-residents: 15% within 2 years, 10% thereafter; no 10-year exemption.  _(andorrainc.com; goldenharbors.com)_

### 5.8 IGI (Indirect Tax / VAT Equivalent)

- **IGI registration threshold** — Self-employed must register for IGI if annual turnover exceeds EUR 40,000 (agricultural: EUR 150,000 threshold).  _(loyalbusinessconsulting.com; andorra-solutions.com; gestoriabonconsellandorra.com)_

**5.8 IGI Rates**  _(loyalbusinessconsulting.com; andorra-solutions.com; gestoriabonconsellandorra.com)_

| IGI Rate | Applies To |
| --- | --- |
| 0% | Medical, education, financial, postal services |
| 1% | Food, books, newspapers |
| 2.5% | Transport, cultural events |
| 4.5% | Standard rate (most goods and services) |
| 9.5% | Banking / financial services |

- **IGI filing frequency** — Turnover < EUR 250,000/year: semi-annual (July and January). Turnover EUR 250,000–EUR 3,600,000/year: quarterly (April, July, October, January). Turnover ≥ EUR 3,600,000/year: monthly. Simplified regime available for turnover ≤ EUR 100,000.  _(loyalbusinessconsulting.com; andorra-solutions.com; gestoriabonconsellandorra.com)_

### 5.9 Withholding at Source

**5.9 Withholding at Source**  _(andorra-solutions.com; remotepeople.com)_

| Income Type | Withholding Rate |
| --- | --- |
| Employment income (residents) | Personalised schedule calculated by DTF — not a fixed rate |
| Savings/capital income (residents) | 10%; taxpayer can request reduction if total savings income < EUR 3,000 |
| Non-residents (IRNR) | 10% at source on employment income, professional fees, rentals |
| Non-resident bank interest, dividends from Andorran sources | Exempt from withholding |

### 5.10 IRPF Filing Obligations

- **Filing obligation triggers** — Must file IRPF if any of the following: earns income from economic activities (self-employment, business) — any amount; receives employment or real-estate income totalling ≥ EUR 24,000; receives savings/investment income not subject to withholding exceeding EUR 3,000; has capital gains or losses to report.  _(e-tramits.ad)_
- **Filing window** — 1 April – 30 September of the year following the tax year. For tax year 2025: file 1 April 2026 – 30 September 2026.  _(e-tramits.ad)_

Online (preferred): Seu Electrònica at e-tramits.ad using MIL credentials or electronic certificate
In-person (by appointment): Departament de Tributs i de Fronteres, Baixada del Molí 26, AD500 Andorra la Vella. Hours: Mon–Thu 08:00–15:00, Fri 08:00–14:30
Contact: impostos@govern.ad / Tel: 147 or +376 885 005

### 5.11 CASS Payment Rules (Self-Employed)

- **CASS payment rules** — Pay by bank transfer between the 10th and 15th of each month. Annual income declaration: January (ordinary). Adaptive declarations permitted: April, July, October. Registration: within 30 calendar days of starting activity. Deregistration: within 30 days of ceasing activity. Late payment surcharges: up to 1 month late = 5%; 1–6 months = 10%; over 6 months = 20%. Formal sanctions: EUR 500–EUR 20,000 depending on severity.  _(cass.ad; elysiumconsultingfirm.com)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home office deduction rules** — Calculate proportion of home used for business: dedicated room(s) as percentage of total floor area. Apply that percentage to: rent or mortgage interest, electricity (FEDA), internet (Andorra Telecom), maintenance. Must be a dedicated workspace — a dual-use room (kitchen table, living room) does NOT qualify. Client must document the calculation and retain records. Conservative default: 0% deduction until reviewer confirms dedicated workspace arrangement. Flag for reviewer: Confirm room count, floor area basis, and that workspace is genuinely dedicated and used exclusively for business.  _(IRPF deductions framework (Llei 5/2014))_

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use rules** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Client must maintain a mileage log (business trips vs total mileage). Depreciation rate: [RESEARCH GAP — reviewer to confirm Andorran depreciation rates for motor vehicles]. Conservative default: 0% business use until mileage log provided. Flag for reviewer: Confirm business percentage is documented with mileage log and is reasonable.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use rules** — Business use portion only; client must provide reasonable estimate. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 Spousal Income Verification

- **Spousal income verification** — Spousal relief (EUR 40,000 threshold) requires spouse/de facto partner to have EUR 0 income. Do not apply without written confirmation. Flag for reviewer: Confirm spouse earns zero from all sources for the tax year.

### 6.5 Dependent Child / Ascendant Deductions

- **Dependent deduction conditions** — Each qualifying dependent: age <25 or >65, lives with taxpayer, earns <EUR 12,000/year. Additional EUR 1,000 (2025): child under 25, earns below SMI (EUR 1,447.33/month). Education EUR 300 (2025): enrolled in university — requires tuition documentation. Flag for reviewer: Confirm ages, cohabitation, income levels, and obtain enrollment documentation for education deduction.

### 6.6 Housing Deduction (2025 New Measure)

- **Housing deduction conditions** — 50% of mortgage principal + interest + acquisition costs; max EUR 5,000/year. Only for primary residence acquisition. Requires mortgage statements and purchase documentation. Flag for reviewer: Confirm property is primary residence, obtain all mortgage/acquisition documents, verify EUR 5,000 annual cap not exceeded.

### 6.7 Capital Gains Holding Period

- **Holding period measurement** — Holding period is measured from notarial deed date of acquisition to notarial deed date of sale. Notarial records are the authoritative source. Flag for reviewer: Obtain copies of both purchase and sale deeds to confirm exact holding period.

### 6.8 IGI / Income Interaction

- **IGI/income interaction rules** — If self-employed and IGI-registered: income for IRPF = net of IGI collected (exclude the 4.5% from revenue). If not IGI-registered (below EUR 40,000 threshold): no IGI collected, full invoice amount = IRPF income. Flag for reviewer: Confirm IGI registration status and that the correct net/gross basis is used.

### 6.9 Active Residency Financial Deposit (Self-Employed)

- **Active residency deposit rules** — Self-employed active residency requires a EUR 50,000 financial deposit with an Andorran bank. This deposit is non-refundable as a cash refund but remains invested (not a cost but a capital lockup). The deposit itself is NOT deductible for IRPF purposes. Flag for reviewer: Confirm client has active residency; note deposit is a balance sheet item, not a P&L expense.

## Section 7 -- Excel Working Paper Template

```
ANDORRA INCOME TAX (IRPF) -- WORKING PAPER
Tax year: 2025
Client: ___________________________
NRT: ___________________________
Status: Employed / Self-Employed (Autònom) / Both
Family situation: Single / Married (partner earns EUR ___) / Dependants: ___

A. GENERAL TAX BASE (BASE GENERAL)

A1. EMPLOYMENT INCOME
  Gross salary / nòmina                          ___________
  Less: employee CASS (6.5%)                     ___________
  Net employment income                          ___________

A2. SELF-EMPLOYMENT INCOME (AUTÒNOM)
  Gross revenue (net of IGI if registered)       ___________
  Less: deductible business expenses             ___________
  Less: CASS self-employed quota paid            ___________
  Net self-employment income                     ___________

A3. RENTAL INCOME
  Gross rental receipts                          ___________
  Less: allowable expenses (mortgage interest,
        repairs, insurance, depreciation)        ___________
  Net rental income                              ___________

A4. TOTAL GENERAL BASE (A1 + A2 + A3)           ___________

B. DEDUCTIONS FROM GENERAL BASE
  B1. General expenses deduction (3%, max EUR 400)  ___________
  B2. Dependent child / ascendant (EUR 750 each)    ___________
  B3. Additional child deduction 2025 (EUR 1,000)   ___________
  B4. Education supplement 2025 (EUR 300)           ___________
  B5. Primary residence acquisition (50%, max EUR 5,000) ___________
  B6. Affordable rental investment (50%, max EUR 5,000)  ___________
  B7. TOTAL DEDUCTIONS                              ___________

C. TAXABLE GENERAL BASE (A4 - B7)               ___________
  (If spouse earns EUR 0, apply EUR 40,000 threshold)

D. IRPF ON GENERAL BASE
  D1. EUR 0–24,000 at 0%                         0.00
  D2. EUR 24,001–40,000: gross 10% minus bonificació (max EUR 800) ___________
  D3. Above EUR 40,000 at 10%                    ___________
  D4. TOTAL IRPF GENERAL BASE (D1 + D2 + D3)    ___________

E. SAVINGS TAX BASE (BASE DE L'ESTALVI)
  E1. Interest income                            ___________
  E2. Foreign dividends                          ___________
  E3. Financial capital gains                    ___________
  E4. Less: EUR 3,000 exemption                  (3,000.00)
  E5. Taxable savings base (if positive)         ___________
  E6. IRPF on savings base at 10%               ___________

F. TOTAL IRPF DUE (D4 + E6)                     ___________
  Less: withholding tax already deducted at source  ___________
  NET IRPF PAYABLE / (REFUNDABLE)               ___________

G. CASS SUMMARY
  G1. Employee CASS paid (6.5% of gross salary)  ___________
  G2. Employer CASS paid (15.5% — not taxpayer cost)  ___________
  G3. Self-employed CASS quota paid (from bracket table)  ___________

REVIEWER FLAGS:
  [ ] Residency confirmed (≥183 days or principal economic interests)?
  [ ] NRT verified?
  [ ] Spousal income confirmed (if applying EUR 40,000 threshold)?
  [ ] Dependent ages, cohabitation, and income documented?
  [ ] Education enrollment documentation obtained?
  [ ] Housing deduction primary-residence status confirmed?
  [ ] IGI registration status confirmed?
  [ ] CASS bracket appropriate to net income level?
  [ ] All T2 items flagged for review?
  [ ] Capital items treated correctly (not expensed)?
  [ ] Entertainment and personal expenses excluded?
```

## Section 8 -- Bank Statement Reading Guide

### Andorran Bank Statement Formats

**Andorran Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Crèdit Andorrà | PDF, CSV | Data, Descripció, Càrrec, Abonament, Saldo | Most common; description contains counterparty + reference |
| MoraBanc | PDF, CSV | Data valor, Concepte, Import, Saldo | Card transactions show merchant name |
| Andbanc | PDF, CSV | Data, Detall, Dèbit, Crèdit, Saldo |  |
| Banca Privada d'Andorra (BPA) | PDF | Data, Descripció, Import |  |
| Vall Banc | PDF | Data, Concepte, Càrrec, Abonament |  |
| Revolut Business | CSV | Date, Counterparty, Amount, Currency | Clean data; multi-currency possible — use EUR |
| Wise Business | CSV | Date, Description, Amount, Currency | Multi-currency; conversion fees are separate line |

### Key Andorran / Catalan Banking Terms

**Key Andorran / Catalan Banking Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFERÈNCIA / TRF | Transfer | Check direction: abonament (credit) = income; càrrec (debit) = expense |
| DOMICILIACIÓ / DOMICILIAT | Direct debit | Regular expense (utility, subscription, insurance) |
| ORDRE PERMANENT | Standing order | Regular expense (rent, loan) |
| TARGETA / PAGAMENT TARGETA | Card payment | Expense — check merchant name |
| INGRÉS / ABONAMENT | Credit / deposit | Potential income |
| COMISSIÓ / COMISSIONS | Bank commission / charges | Deductible (business account only) |
| INTERESSOS CREDITORS | Credit interest | Savings base income |
| INTERESSOS DEUTORS | Debit interest (overdraft) | Potentially deductible business finance cost |
| RETIRADA / EXTRACCIÓ | Cash withdrawal | Ask what cash was spent on |
| SALDO | Balance | Not income or expense |
| PRÉSTEC / AMORTITZACIÓ | Loan / repayment | Loan principal = exclude; interest = check deductibility |
| IMPOST IRPF | Income tax payment | NOT deductible |
| CASS COTITZACIÓ | CASS contribution | IRPF deduction — separate line in working paper |
| IGI LIQUIDACIÓ | IGI payment | NOT an income tax expense — exclude |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING — reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ANDORRA IRPF
1. Fiscal residency: have you been physically present in Andorra for ≥183 days in 2025?
   If no, do you have your principal economic interests or family ties in Andorra?
2. Employment status: employed by an Andorran employer, self-employed (autònom), or both?
3. NRT (Número de Registre Tributari): please provide your NRT.
4. Family situation: single, married/de facto partner? Does your partner earn income?
   Do you have dependent children (under 25) or dependent ascendants (over 65)?
   If yes, do they live with you and earn below EUR 12,000/year?
   Are any of them enrolled in university in 2025?
5. Home office: dedicated room or shared space? If dedicated, what % of floor area?
6. Vehicle: do you use a car for business? If yes, what % is business use? Do you keep a mileage log?
7. Phone/internet: what % is business use?
8. CASS contributions: total amount paid in 2025? Which bracket were you on?
9. IGI registration: are you registered for IGI? What is your annual turnover?
10. Housing: did you purchase a primary residence in 2025? Do you have a mortgage?
    Do you own property rented at affordable rates (≤EUR 12.45/m²)?
11. Capital gains: did you sell any shares, real estate, or other assets in 2025?
12. Any other income (foreign dividends, interest, foreign employment)?
```

## Section 10 -- Reference Material

### Key Legislation and Authorities

**Key Legislation and Authorities**

| Topic | Reference |
| --- | --- |
| IRPF primary legislation | Llei 5/2014, del 24 d'abril, de l'impost sobre la renda de les persones físiques |
| IRPF rates and brackets | e-tramits.ad (official filing portal); invicoandorra.com; andorra-solutions.com |
| IRPF deductions (2025 measures) | lavallassociats.com; aaa.ad |
| CASS contribution rates | cass.ad/cotitzacions-del-treballadors-per-compte-propi (official) |
| CASS self-employed reduced regimes | elysiumconsultingfirm.com (citing Decree 16/2025) |
| IGI legislation | Llei 11/2012 (IGI) |
| Non-resident income tax (IRNR) | elysiumconsultingfirm.com/en/publications/the-non-resident-income-tax-nrit-irnr-in-andorra |
| Double taxation agreements | elysiumconsultingfirm.com/en/publications/double-taxation-agreements-dta-in-andorra-2025-update |
| Minimum wage (SMI 2025) | augelegalfiscal.com/en/minimum-wage-2025/ |
| Criminal tax offences | Llei 15/2017; elysiumconsultingfirm.com/en/publications/tax-offence-in-andorra |
| Filing contact | impostos@govern.ad / Tel: 147 or +376 885 005 |
| CASS contact | public@cass.ad / +376 870 870 |

### Double Taxation Agreements in Force (end-2025)

21 DTAs following the OECD Model Convention:
France (2015), Spain (2016), Luxembourg (2016), Portugal (2016), Liechtenstein (2016), UAE (2017), Malta (2017), Cyprus (2019), San Marino (2021), Hungary (2022), Monaco (2023), Czech Republic (2023), Croatia (2023), Iceland (2024), Netherlands (2024), South Korea (2025), Lithuania (2025), Montenegro (2025), Latvia (2025), Romania (2025), United Kingdom (2025).

Source: elysiumconsultingfirm.com/en/publications/double-taxation-agreements-dta-in-andorra-2025-update

### Other Andorran Taxes (Context)

**Other Andorran Taxes (Context)**

| Tax | Rate | Notes |
| --- | --- | --- |
| Corporate tax (IS) | 10% flat; 5% for new companies with net income ≤ EUR 50,000 |  |
| IGI (indirect / VAT equivalent) | 4.5% standard; 0% / 1% / 2.5% / 9.5% special | See Section 5.8 |
| Inheritance / gift tax | None | No filing required |
| Wealth tax | None | No filing required |
| Branch remittance tax | None |  |
| Real-estate transfer tax (ITP) | [RESEARCH GAP — confirm rate with DTF; separate from IRPF gain] |  |

### Penalties and Sanctions

**Administrative (IRPF/IGI):**
- Failure to file / failure to pay (no loss to treasury): EUR 150–EUR 3,000 (immigrantinvest.com)
- Underpayment of tax (loss to treasury): 50%–150% of unpaid tax amount (immigrantinvest.com)
- Late payment interest rate (2025): 4.06% per annum (updated annually)

**Criminal tax fraud (Llei 15/2017):**
- Basic offence: evasion ≥ EUR 75,000 AND ≥ 5% of total liability → 3 months to 3 years' imprisonment + fine 1×–4× defrauded amount
- Aggravated offence: evasion ≥ EUR 150,000 AND ≥ 5% of total liability (or organised crime) → 1–5 years' imprisonment + fine 1×–4× defrauded amount
- Voluntary regularisation before proceedings: eliminates criminal liability

Source: elysiumconsultingfirm.com/en/publications/tax-offence-in-andorra-origin-functioning-and-application

### Research Gaps and Confidence Notes

**Research Gaps and Confidence Notes**

| Topic | Confidence | Action Required |
| --- | --- | --- |
| IRPF brackets and rates (general base) | High — multiple sources confirm | Review annually for budget changes |
| Savings base EUR 3,000 exemption | High | Review annually |
| CASS employee 6.5% / employer 15.5% split | High | Review annually |
| CASS self-employed brackets (100% base = EUR 2,672.52) | Medium-High — official cass.ad vs Decree 16/2025 discrepancy noted | Use cass.ad as filing reference; verify directly |
| CASS ceiling for salaried employees | NOT CONFIRMED | Verify directly with CASS (public@cass.ad) |
| 2025 deduction changes (housing, children, education) | High — lavallassociats.com; aaa.ad | Confirm operative date in Llei 5/2014 amendment |
| Exact year-by-year real-estate CGT rate step-down | Low | Confirm exact schedule with DTF |
| Andorran depreciation rates for capital assets | NOT CONFIRMED | Confirm with DTF or qualified Andorran advisor |
| Real-estate transfer tax (ITP) | NOT CONFIRMED | Confirm rate and filing with DTF |
| Disability deductions exact amounts | NOT CONFIRMED | Confirm with DTF: impostos@govern.ad |

### Test Suite

Input: Single, gross revenue EUR 20,000, expenses EUR 2,000, CASS at 50% bracket (EUR 335.57/month × 12 = EUR 4,026.84).
Expected: Net income = EUR 20,000 − EUR 2,000 − EUR 4,026.84 = EUR 13,973.16. Less general deduction (3% = EUR 419.19, capped EUR 400) = EUR 13,573.16. Below EUR 24,000 → IRPF EUR 0.

Input: Single, no dependants, gross revenue EUR 50,000, expenses EUR 10,000, CASS 100% bracket (EUR 587.95 × 12 = EUR 7,055.40).
Expected: Net = EUR 50,000 − EUR 10,000 − EUR 7,055.40 = EUR 32,944.60. Less EUR 400 deduction = EUR 32,544.60. Tax: EUR 0 on EUR 0–24,000; band EUR 24,001–32,544.60 = EUR 8,544.60 × 10% = EUR 854.46 minus bonificació EUR 800 = EUR 54.46. Total IRPF = EUR 54.46.

Input: Single, gross revenue EUR 75,000, expenses EUR 15,000, CASS 125% bracket (EUR 734.94 × 12 = EUR 8,819.28).
Expected: Net = EUR 75,000 − EUR 15,000 − EUR 8,819.28 = EUR 51,180.72. Less EUR 400 = EUR 50,780.72. Tax: EUR 0 on EUR 0–24,000; EUR 24,001–40,000 (EUR 16,000): EUR 1,600 − EUR 800 = EUR 800; EUR 40,001–50,780.72 (EUR 10,780.72) × 10% = EUR 1,078.07. Total IRPF = EUR 1,878.07.

Input: Married, spouse EUR 0 income. Taxpayer employment income EUR 38,000. Employee CASS: EUR 38,000 × 6.5% = EUR 2,470. Net = EUR 38,000 − EUR 2,470 = EUR 35,530. Less EUR 400 = EUR 35,130. Spousal relief raises threshold to EUR 40,000. EUR 35,130 < EUR 40,000 → IRPF EUR 0.

Input: Foreign dividends EUR 12,000, no other savings income.
Expected: Taxable savings base = EUR 12,000 − EUR 3,000 = EUR 9,000. IRPF at 10% = EUR 900.

Input: Dividend from Andorran SL EUR 5,000.
Expected: Fully exempt. IRPF EUR 0. Do not include in any base.

Input: Self-employed, net income EUR 45,000 → 125% bracket.
Expected: EUR 734.94/month × 12 = EUR 8,819.28/year. Verify: EUR 3,340.65 × 22% = EUR 734.94 ✓.

Input: First-time registrant, month 1. Only general branch at 10% on 25% base = EUR 668.13 × 10% = EUR 66.81.
Expected: Monthly CASS = EUR 66.81. Annual (12 months) = EUR 801.72. No pension points.

## PROHIBITIONS

- **Fiscal residency confirmation required** — NEVER compute IRPF without confirming fiscal residency status (≥183 days or principal economic interests)  _(PROHIBITIONS)_
- **Spousal threshold requires written confirmation** — NEVER apply the EUR 40,000 spousal threshold without written confirmation that spouse earns EUR 0  _(PROHIBITIONS)_
- **Andorran dividends exempt from any base** — NEVER include Andorran company dividends in any tax base — they are fully exempt  _(PROHIBITIONS)_
- **IRPF not deductible as business expense** — NEVER deduct IRPF itself as a business expense  _(PROHIBITIONS)_
- **Fines and penalties not deductible** — NEVER deduct fines or penalties  _(PROHIBITIONS)_
- **Entertainment expenses not deductible** — NEVER allow entertainment expenses as a deduction  _(PROHIBITIONS)_
- **IGI excluded from IRPF income** — NEVER include IGI collected in income for IRPF (net revenue basis for IGI-registered traders)  _(PROHIBITIONS)_
- **Bonificació cap enforcement** — NEVER apply the bonificació above EUR 800 — the cap is EUR 800  _(PROHIBITIONS)_
- **CASS always deductible from IRPF income** — NEVER omit the CASS contribution as a deduction from IRPF income — it is always deductible  _(PROHIBITIONS)_
- **Use official CASS base figure** — NEVER use the secondary-source CASS base (EUR 2,560.99) for filing — use the official cass.ad figure (EUR 2,672.52) or verify directly  _(PROHIBITIONS)_
- **CASS ceiling for salaried employees not confirmed** — NEVER confirm CASS ceiling for salaried employees without checking directly with CASS — no authoritative ceiling found  _(PROHIBITIONS)_
- **Calculations must be labeled estimated** — NEVER present tax calculations as definitive — always label as estimated and require reviewer sign-off  _(PROHIBITIONS)_
- **Advisor review required before filing** — NEVER file without a qualified Andorran advisor reviewing all figures  _(PROHIBITIONS)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
