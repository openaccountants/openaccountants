---
name: slovenia-income-tax
description: Use this skill whenever asked about Slovenia (Slovenija) personal income tax for self-employed individuals (s.p. / samostojni podjetnik) and resident individuals. Trigger on phrases like "how much dohodnina do I pay", "income tax Slovenia", "informativni izračun dohodnine", "IID", "DohDej", "davek od dohodka iz dejavnosti", "normirani odhodki", "lump-sum expenses", "splošna olajšava", "general allowance", "ZPIZ contributions", "ZZZS health", "long-term care contribution", "OZP", "OPSVZ", "minimalna plača", "self-employed tax Slovenia", or any question about filing or computing Slovenian personal income tax for a resident, sole proprietor, or employee. Also trigger when preparing or reviewing an IID or DohDej return, computing the progressive dohodnina scale, social security contributions, or advising on advance-tax (akontacija) installments. This skill covers the 2025 five-band progressive scale, capital-income cedular rates, ZPIZ/ZZZS/unemployment/parental/injury and new long-term-care (ZDOsk-1) contributions, the OZP flat health contribution, the normirani odhodki regime, allowances, forms, deadlines, and penalties. ALWAYS read this skill before touching any Slovenian income tax work.
version: 0.1
jurisdiction: SI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovenia Income Tax -- Self-Employed and Individuals

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Slovenia (Republika Slovenija) |
| Tax | Personal income tax (dohodnina) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Personal Income Tax Act (Zakon o dohodnini, ZDoh-2) (PwC, taxsummaries.pwc.com/slovenia) |
| Supporting legislation | Pension & Disability Insurance Act (ZPIZ-2); Health Care & Health Insurance Act (ZZVZZ); compulsory health contribution under ZVZZNZ (OZP, from 2024); Long-Term Care Act (Zakon o dolgotrajni oskrbi, ZDOsk-1, LTC contribution from 1 July 2025) (KPMG GMS Flash Alert 2025-133) |
| Tax authority | Financial Administration of the Republic of Slovenia (FURS / Finančna uprava Republike Slovenije) (fu.gov.si) |
| Filing portal | eDavki (edavki.durs.si) |
| Social security collection | FURS collects; pension administered by ZPIZ, health by ZZZS (PwC) |
| Self-employed return deadline | 31 March of the following year (DohDej, via eDavki) (FURS) |
| Individual self-assessment deadline | 31 July of the following year where no IID is issued (PwC) |
| Validated by | Pending -- requires sign-off by a Slovenian tax adviser / pooblaščeni računovodja |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rate Brackets -- Progressive Scale (dohodnina) 2025

**Tax Rate Brackets -- Progressive Scale (dohodnina) 2025**  _(official 2025 scale, Zveza računovodij, finančnikov in revizorjev Slovenije (zvezarfr.si); cross-checked against PwC Worldwide Tax Summaries (taxsummaries.pwc.com/slovenia/individual/taxes-on-personal-income))_

| Annual Tax Base (EUR) | Rate | Tax on Lower Limit + Marginal | Cumulative Tax at Top |
| --- | --- | --- | --- |
| 0 -- 9,210.26 | 16% | 16% of base | EUR 1,473.64 |
| 9,210.26 -- 27,089.00 | 26% | 1,473.64 + 26% over 9,210.26 | EUR 6,122.11 |
| 27,089.00 -- 54,178.00 | 33% | 6,122.11 + 33% over 27,089.00 | EUR 15,061.48 |
| 54,178.00 -- 78,016.32 | 39% | 15,061.48 + 39% over 54,178.00 | EUR 24,358.43 |
| 78,016.32+ | 50% | 24,358.43 + 50% over 78,016.32 | -- |

Applies to the annual tax base (net annual income after allowances) for income that falls under the progressive scale (employment, self-employment/business, pension). Capital income is taxed separately (cedularly) -- see below. Arithmetic note: the band-4 top cumulative recomputes to 24,358.42 (15,061.48 + (78,016.32 − 54,178.00) × 39%); the official table publishes 24,358.43. The 1-cent difference is a published rounding artifact -- use the official 24,358.43 as the band-5 base. [RESEARCH GAP -- reviewer to confirm the exact published band-5 base against the FURS Uredba/lestvica for 2025.]

### Capital Income -- Cedular (Separate, Final) Rates 2025

**Capital Income -- Cedular (Separate, Final) Rates 2025**  _(PwC income-determination)_

| Income Type | Rate | Basis |
| --- | --- | --- |
| Dividends | 25% flat, final | Separate from progressive scale (PwC income-determination) |
| Interest | 25% flat, final | Bank deposit interest exempt up to EUR 1,000/year (EU institutions) (PwC) |
| Rental income | 25% flat, final | Cedular schedular tax (PwC income-determination) |
| Capital gains -- held 0–5 yrs | 25% | Final tax by holding period (PwC) |
| Capital gains -- held 5–10 yrs | 20% | Final tax (PwC) |
| Capital gains -- held 10–15 yrs | 15% | Final tax (PwC) |
| Capital gains -- held over 15 yrs | 0% | Exempt (PwC) |

Capital income is NOT added to the progressive base and is NOT taxed on the 16/26/33/39/50% scale. A secondary source quoted 27.5% for dividends/interest; the authoritative PwC income-determination page confirms 25% -- use 25%.

### Allowances (Olajšave) 2025

**Allowances (Olajšave) 2025**  _(zvezarfr.si official 2025 scale & allowances; PwC deductions page)_

| Allowance | Value (EUR) |
| --- | --- |
| General (basic) personal allowance -- splošna olajšava | 5,260.00 (for total annual income above 16,832.00) |
| Increased general allowance (income ≤ 16,832.00) | 5,260.00 + (19,736.99 − 1.17259 × total annual income) |
| 1st dependent child | 2,838.30 |
| 2nd dependent child | 3,085.52 |
| 3rd dependent child | 5,146.39 |
| 4th dependent child | 7,207.26 |
| 5th dependent child | 9,268.12 |
| Each further child (6th+) | +2,060.87 each |
| Child needing special care | 10,285.40 |
| Other dependent family member | 2,838.30 |
| Young workers (resident under 29, employment income) | 1,367.60 |
| Disability allowance (100% disabled resident) | 18,188.61 |

Sources: zvezarfr.si official 2025 scale & allowances; PwC deductions page. (PwC deductions tables showed 2024 figures at fetch time -- 2025 amounts here come from the Slovenian accountancy association and should be cross-checked against the FURS-published 2025 lestvica.)

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | STOP -- residents taxed on worldwide income, non-residents on Slovenian-source only; cannot proceed without residency |
| Unknown total annual income (for allowance) | Use standard 5,260 general allowance; apply increased-allowance formula ONLY when income ≤ 16,832.00 |
| Income type unclear (progressive vs capital) | Treat employment/business/pension on progressive scale; dividends/interest/rental cedular at 25% |
| Self-employed expense method unknown | Use actual costs (do NOT assume normirani odhodki without confirmation of eligibility and turnover tier) |
| Contribution period spans 1 July 2025 | Use 22.10% / 16.10% before 1 July; add 1pp each side (LTC) from 1 July onward |
| OZP flat health contribution | Apply EUR 37.17/month per insured adult from 1 March 2025 (separate from percentage contributions) |
| Unknown holding period (capital gain) | Treat as 0–5 years → 25% (most conservative, highest tax) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown VAT registration status | Assume below 60,000 threshold unless turnover proves otherwise; confirm before applying VAT |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of tax residency (resident / non-resident), income type (employment, self-employment/s.p., pension, capital), and (for self-employed) whether actual-cost or normirani odhodki accounting applies.

Recommended -- all sales/output invoices, purchase invoices and receipts, monthly OPSVZ/REK contribution statements (self-employed), prior-year IID or DohDej assessment, number and order of dependent children, age (for the under-29 allowance), and VAT registration status.

Ideal -- complete income and expenditure account, fixed-asset register with depreciation schedule, advance-tax (akontacija) payment confirmations, capital-income (dividend/interest/rental) statements with acquisition dates for gains, and the prior-year informative calculation.

Refusal if minimum is missing -- SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that all business expenses are supported by valid documentation and that the income is correctly split between the progressive base and cedular capital income."

### Refusal Catalogue

- **R-SI-1** — Slovenia taxes residents on worldwide income and non-residents only on Slovenian-source income. This skill cannot compute dohodnina without confirmed tax-residency status. Please confirm before proceeding.  _(PwC)_
- **R-SI-2** — This skill covers resident individuals and sole proprietors (s.p.) only. Limited companies (d.o.o.) pay corporate income tax (davek od dohodkov pravnih oseb) under a separate regime. Escalate to a Slovenian tax adviser.
- **R-SI-3** — Capital-gains computations require verified acquisition dates, cost basis, and holding-period mapping to the 25/20/15/0% schedule. Where records are incomplete, escalate to a Slovenian tax adviser.
- **R-SI-4** — The lump-sum expense (normirani odhodki) regime changed twice around 2025 -- restrictive tiered rules from 1 Jan 2025, then raised revenue caps from 2026. The deemed-expense percentage for a given 2025 turnover must be verified against the current ZDoh-2 text / FURS guidance. Do not compute the deemed deduction without that confirmation.
- **R-SI-5** — Client has outstanding tax arrears or is subject to FURS enforcement. Statutory default interest accrues daily and fines can reach EUR 75,000 for serious breaches. Do not advise. Escalate to a Slovenian tax adviser immediately.  _(Commenda)_
- **R-SI-6** — This skill covers personal income tax (dohodnina / DohDej) only. For Slovenian VAT (DDV), use the dedicated VAT skill.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits / Prilivi on Bank Statement)

**3.1 Income Patterns (Credits / Prilivi on Bank Statement)**

| Pattern | Destination | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + NAKAZILO, PLAČILO, PLACILO RAČUNA | Business income (progressive base) | Self-employment revenue | If VAT-registered, extract net (excl. 22% DDV) |
| HONORAR, STORITVE, SVETOVANJE, PROVIZIJA | Business income | Professional / consultancy fees | Typical s.p. income |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Platform payout | Match to underlying invoices |
| PAYPAL, WISE PAYOUT, REVOLUT PAYOUT | Business income | Platform payout | Verify business vs personal account |
| UPWORK, FIVERR, TOPTAL | Business income | Freelance platform | Net of platform commission |
| PLAČA, PLACA, OD MZP, SALARY, EMPLOYER [name] | Employment income (progressive base) | NOT self-employment -- separate income line |  |
| NAJEMNINA, RENT RECEIVED | Capital income -- rental | Cedular 25% (separate, final) | Not on progressive scale (PwC) |
| OBRESTI, INTEREST | Capital income -- interest | Cedular 25%; exempt up to EUR 1,000 bank deposit | (PwC) |
| DIVIDENDA, DIVIDEND | Capital income -- dividend | Cedular 25% (final) | (PwC) |
| FURS VRAČILO, TAX REFUND, VRACILO DOHODNINE | EXCLUDE | Not income | Prior-year tax refund |
| SUBVENCIJA, DOTACIJA, GRANT | Check nature | Revenue grant = business income; capital grant EXCLUDE |  |

### 3.2 Expense Patterns (Debits / Odlivi) -- Deductible (actual-cost s.p.)

**3.2 Expense Patterns (Debits / Odlivi) -- Deductible (actual-cost s.p.)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| NAJEMNINA PISARNE, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| ZAVAROVANJE (poklicno), PROFESSIONAL INDEMNITY | Professional insurance | Deductible | Business-related only |
| RAČUNOVODJA, RACUNOVODSTVO, ACCOUNTANT | Accountancy fees | Deductible |  |
| ODVETNIK, PRAVNE STORITVE, LEGAL | Legal fees | Deductible | Must be business-related |
| PISARNIŠKI MATERIAL, OFFICE SUPPLIES | Office supplies | Deductible |  |
| OGLAŠEVANJE, GOOGLE ADS, META ADS, MARKETING | Marketing/advertising | Deductible |  |
| IZOBRAŽEVANJE, TEČAJ, SEMINAR, KONFERENCA | Training/CPD | Deductible | Must relate to current business |
| BANČNI STROŠKI, BANK FEE, NLB STROŠEK | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, PROVIZIJA | Payment processing fees | Deductible |  |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE, NOTION | Software subscription | Deductible | Recurring = operating expense |
| ANTHROPIC, OPENAI, GITHUB, AWS, DIGITALOCEAN | IT infrastructure / SaaS | Deductible | Capitalise if a durable asset over de-minimis |

### 3.3 Expense Patterns (Debits) -- Utilities (may need apportionment)

**3.3 Expense Patterns (Debits) -- Utilities (may need apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ELEKTRO, ELEKTRIKA, ENERGIJA | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| TELEKOM, A1, TELEMACH, INTERNET | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBITEL, MOBILE | Phone | T2 | Business-use portion only |

### 3.4 Expense Patterns (Debits) -- Travel

**3.4 Expense Patterns (Debits) -- Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LETALSKA, RYANAIR, WIZZ AIR, EASYJET | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| BOLT, UBER, TAXI | Local transport | Deductible if business purpose |  |
| GORIVO, PETROL, OMV, MOL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKIRNINA, PARKING | Parking | T2 -- business % only |  |

### 3.5 Expense Patterns (Debits) -- NOT Deductible

**3.5 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAVRACIJA, KOSILO, VEČERJA, ENTERTAINMENT | Entertainment | Restricted/not deductible | Confirm wholly-business; private element blocked |
| OSEBNO, ŽIVILA, MERCATOR, LIDL, SPAR, HOFER | Personal / groceries | NOT deductible | Private living costs |
| KAZEN, GLOBA, FINE, PENALTY | Fines/penalties | NOT deductible | Public policy |
| FURS DOHODNINA, INCOME TAX PAYMENT | Income tax payment | NOT deductible | Income tax cannot reduce income |
| DVIG, OSEBNI DVIG, ATM (personal) | Drawings | NOT deductible | Not a business expense |

### 3.6 Exclusions (Neither Income nor Expense)

**3.6 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNI PRENOS, MED RAČUNI, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| KREDIT, POSOJILO, LOAN REPAYMENT | EXCLUDE (principal) | Loan principal movement; interest may be deductible |
| ZPIZ, ZZZS, PRISPEVKI, OPSVZ, SOCIAL CONTRIBUTIONS | Social contribution payment | Deductible from the s.p. base (NOT a normal trading expense line) |
| OZP, OBVEZNI ZDRAVSTVENI PRISPEVEK | OZP flat health contribution | EUR 37.17/month per insured adult from 1 Mar 2025 |
| DDV, VAT PAYMENT | EXCLUDE | VAT liability payment, not an expense |
| AKONTACIJA DOHODNINE, ADVANCE TAX | Advance tax (credit against liability) | Not an expense -- credited against final dohodnina |

### 3.7 Slovenian Banks -- Statement Format Reference

**3.7 Slovenian Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| NLB (Nova Ljubljanska banka) | NAKAZILO, TRAJNIK, SDD, BREMENITEV, DOBROPIS | PDF/CSV; date format DD.MM.YYYY |
| NKBM / Nova KBM | PLAČILO, TRAJNIK, PROVIZIJA | PDF/CSV |
| SKB banka | NAKAZILO, BREMENITEV, STROŠEK | PDF |
| Intesa Sanpaolo Bank (SI) | PLAČILO, TRAJNIK, KARTICA | PDF/CSV |
| Revolut / Wise (business) | PAYMENT, TRANSFER, CONVERSION, FEE | CSV; multi-currency -- use EUR amounts |

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (VAT-registered s.p.)

Input line: `15.03.2025 ; NLB NAKAZILO ; STUDIO KREBS D.O.O. ; PLAČILO RAČUNA 2025-003 ; +1,220.00 ; EUR`

Reasoning: Client payment for services. The s.p. is VAT-registered, so EUR 1,220 includes 22% DDV. Net = 1,220 / 1.22 = EUR 1,000.00 (business income, progressive base). EUR 220.00 is VAT collected -- excluded from income (a liability to FURS).

Classification: Business income = EUR 1,000.00. VAT EUR 220.00 excluded.

### Example 2 -- SaaS Subscription (Deductible)

Input line: `01.04.2025 ; NLB SDD ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD APR ; -29.99 ; EUR`

Reasoning: Monthly SaaS subscription, recurring operating expense. Fully deductible against business income (actual-cost method). For VAT-registered s.p., net of recoverable input VAT is the expense; otherwise the gross EUR 29.99 is the cost.

Classification: Deductible expense = EUR 29.99 (or net if VAT-recoverable).

### Example 3 -- Dividend Received (Cedular, Not Progressive)

Input line: `30.04.2025 ; NLB DOBROPIS ; DIVIDENDA XYZ D.D. ; ; +800.00 ; EUR`

Reasoning: Dividend income is taxed cedularly at a flat 25%, final and SEPARATE from the progressive scale (PwC income-determination). It is NOT added to the business/employment base. Tax = 800 × 25% = EUR 200.00 (typically withheld at source).

Classification: Capital income -- dividend. Cedular 25% = EUR 200.00. Do NOT add to progressive base.

### Example 4 -- Self-Employed Social Contributions Paid

Input line: `20.05.2025 ; NLB SDD ; FURS PRISPEVKI OPSVZ ; APRIL 2025 ; -260.00 ; EUR`

Reasoning: Self-employed social security contributions (OPSVZ). The self-employed person pays both employee and employer shares on the contribution base (minimum base ~237.02 EUR/month in 2025; minimum base = 60% of average gross wage) (Crowe; tax-checker). These reduce the self-employment base but are tracked separately from ordinary trading expenses. [RESEARCH GAP -- reviewer to confirm the exact 2025 minimum monthly contribution amount against the FURS contribution brochure.]

Classification: Social contributions (deductible from s.p. base). Track separately, not as a trading-expense line.

### Example 5 -- OZP Flat Health Contribution

Input line: `05.05.2025 ; NLB SDD ; OBVEZNI ZDRAVSTVENI PRISPEVEK ; ZZZS ; -37.17 ; EUR`

Reasoning: The compulsory health contribution (OZP) is a FLAT monthly amount of EUR 37.17 per insured adult from 1 March 2025 (was EUR 35.00 from Jan 2024–Feb 2025), adjusted annually on 1 March by average wage growth (ZDS). It is NOT a percentage and is separate from the 6.36%/6.56% ZZZS percentage contributions.

Classification: OZP flat health contribution = EUR 37.17. Separate from percentage contributions.

### Example 6 -- Internal Transfer (Exclude)

Input line: `15.06.2025 ; NLB INTERNI PRENOS ; LASTNI RAČUN - VARČEVANJE ; ; -2,000.00 ; EUR`

Reasoning: Transfer between own accounts. Neither income nor expense. Exclude entirely.

Classification: EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency and Scope

- **Residency and Scope** — Residents are taxed on worldwide income; non-residents only on Slovenian-source income. Confirm residency before any computation.  _(ZDoh-2 (PwC))_

### 5.2 The Progressive Scale (dohodnina)

**5.2 The Progressive Scale (dohodnina)**  _(zvezarfr.si official 2025 scale; PwC)_

| Annual Tax Base (EUR) | Rate |
| --- | --- |
| 0 -- 9,210.26 | 16% |
| 9,210.26 -- 27,089.00 | 26% |
| 27,089.00 -- 54,178.00 | 33% |
| 54,178.00 -- 78,016.32 | 39% |
| 78,016.32+ | 50% |

The 2025 annual scale is applied to the tax base (net annual income after allowances) for employment, self-employment/business, and pension income.

### 5.3 Capital Income -- Cedular Treatment

- **Capital Income -- Cedular Treatment** — Dividends, interest, and rental income are taxed at a flat 25% as final tax, separate from the progressive scale. Bank deposit interest is exempt up to EUR 1,000/year (EU institutions). Capital gains are taxed by holding period: 25% (0–5 yrs), 20% (5–10 yrs), 15% (10–15 yrs), 0% (>15 yrs)  _(PwC income-determination)_

### 5.4 General and Family Allowances

- **General and Family Allowances** — General (basic) allowance for 2025: EUR 5,260.00 for total annual income above EUR 16,832.00. For total annual income ≤ EUR 16,832.00, an increased allowance applies: 5,260.00 + (19,736.99 − 1.17259 × total annual income). Family allowances apply per Section 1 (1st child 2,838.30; 2nd 3,085.52; etc.). Young workers (resident under 29) get an extra EUR 1,367.60 on employment income; 100%-disabled resident allowance is EUR 18,188.61.  _(zvezarfr.si; PwC)_

### 5.5 Social Security Contributions -- Employment

**Employee contributions (pre-1 July 2025)**  _(PwC other-taxes; KPMG Flash Alert 2025-133)_

| Class | Rate (pre-1 July 2025) |
| --- | --- |
| Pension & disability (ZPIZ) | 15.50% |
| Health (ZZZS) | 6.36% |
| Unemployment | 0.14% |
| Parental protection | 0.10% |
| **Total (pre-1 July 2025)** | **22.10%** |
| + Long-term care (ZDOsk-1, from 1 July 2025) | +1.00% |
| **Total (from 1 July 2025)** | **23.10%** |

Verification: 15.50 + 6.36 + 0.14 + 0.10 = 22.10%; +1.00% LTC = 23.10%. (PwC other-taxes; KPMG Flash Alert 2025-133.)

**Employer contributions (pre-1 July 2025)**  _(PwC other-taxes; KPMG)_

| Class | Rate (pre-1 July 2025) |
| --- | --- |
| Pension & disability (ZPIZ) | 8.85% |
| Health (ZZZS) | 6.56% |
| Unemployment | 0.06% |
| Parental protection | 0.10% |
| Injury at work / occupational disease | 0.53% |
| **Total (pre-1 July 2025)** | **16.10%** |
| + Long-term care (ZDOsk-1, from 1 July 2025) | +1.00% |
| **Total (from 1 July 2025)** | **17.10%** |

Verification: 8.85 + 6.56 + 0.06 + 0.10 + 0.53 = 16.10%; +1.00% LTC = 17.10%. (PwC other-taxes; KPMG.) Contributions are due on the day wages/salaries are paid (PwC).

### 5.6 OZP Flat Health Contribution

- **OZP flat health contribution** — EUR 37.17/month per insured adult from 1 March 2025 (was EUR 35.00 from Jan 2024–Feb 2025). Adjusted annually on 1 March by average gross wage growth. Replaced the abolished voluntary supplementary health insurance.  _(ZDS)_

### 5.7 Long-Term Care Contribution (ZDOsk-1)

- **Long-Term Care Contribution (ZDOsk-1)** — From 1 July 2025, a new LTC contribution applies: 1% employee + 1% employer of gross salary; self-employed pay 2% (both shares); pensioners pay 1% of net pension. First applied to July 2025 payroll.  _(KPMG Flash Alert 2025-133)_

### 5.8 Self-Employed (s.p.) -- Income Tax and Contributions

- **Self-employed income tax and contributions** — Self-employed pay both income tax (on the progressive scale, via DohDej) and the full social contributions themselves. Minimum contribution base: 60% of the average gross wage (≈ EUR 237.02/month minimum contribution in 2025, rising to ≈ EUR 303.11 in 2026 as the base moves toward 60% of average wage). [RESEARCH GAP -- confirm the exact 2025 minimum figure and base percentage against the FURS contribution brochure.] Maximum contribution base: 3.5 × the insured's average monthly wage.  _(Crowe; tax-checker)_

### 5.9 normirani odhodki (Lump-Sum Expense) Regime

- **normirani odhodki regime** — Optional regime with 80% deemed expenses, subject to revenue caps. 2025: full-time s.p. revenue cap EUR 60,000 (EUR 50,000 part-time); a reformed tiered system applies the 80% deemed-expense rate only within lower turnover tiers. A November 2025 law later raised the caps to EUR 120,000 / EUR 50,000 effective from 2026. For a given 2025 turnover, the precise tiered deemed-expense percentage and contribution-base treatment MUST be verified against current ZDoh-2 / FURS guidance before computing. [RESEARCH GAP -- reviewer to confirm 2025 tier percentages.]  _(ZDoh-2 (Sibiz))_

### 5.10 Minimum Wage and Holiday Allowance

- **Minimum Wage and Holiday Allowance** — 2025 minimum gross monthly wage: EUR 1,277.72 (+1.9% over 2024's EUR 1,253.90); rises to EUR 1,481.88 for 2026. Holiday allowance (regres): statutory annual payment at least equal to the minimum wage; tax/contribution-exempt up to a cap tied to the average wage.  _(WageIndicator; SeeNews; Sibiz)_

### 5.11 Non-Deductible Expenses (Self-Employed Actual-Cost)

**5.11 Non-Deductible Expenses (Self-Employed Actual-Cost)**

| Expense | Reason |
| --- | --- |
| Personal / private living costs | Not business-related |
| Fines and penalties | Public policy |
| Income tax (dohodnina) itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |
| Private-use portion of mixed expenses | Apportion -- only business % deductible |

### 5.12 VAT Interaction

**5.12 VAT Interaction**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (registered) | NOT income -- exclude from business revenue |
| Input VAT recovered (registered) | NOT an expense -- exclude from cost |
| Non-registered (below 60,000 threshold) | Gross amounts are income/cost (no VAT line) |

- **VAT registration threshold** — EUR 60,000 annual taxable turnover from 2025 (was 50,000)  _(Taxually)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 normirani odhodki Election and Tier

- **normirani odhodki election and tier** — The choice between actual-cost and normirani odhodki, and the applicable 2025 tier, materially changes the tax base. Conservative default: use actual costs until eligibility, turnover tier, and the 2025 deemed-expense percentage are confirmed. Flag for reviewer: confirm 2025 turnover, full-time vs part-time status, and current ZDoh-2 tier rules.

### 6.2 Home Office Deduction

- **Home Office Deduction** — Calculate the proportion of the home used exclusively for business (dedicated room/floor area). Apply that percentage to rent, electricity, heating, internet, maintenance. A dual-use room does NOT qualify. Conservative default: 0% until reviewer confirms the arrangement.

### 6.3 Motor Vehicle Business Use

- **Motor Vehicle Business Use** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Client must maintain a mileage log. Conservative default: 0% business use until a log is provided.

### 6.4 Phone / Internet Mixed Use

- **Phone / Internet Mixed Use** — Business-use portion only; client must provide a reasonable estimate. Conservative default: 0% until business percentage confirmed.

### 6.5 Capital Gains Holding-Period Mapping

- **Capital Gains Holding-Period Mapping** — Mapping a disposal to the correct 25/20/15/0% band depends on verified acquisition and disposal dates. Flag for reviewer: confirm acquisition date, cost basis, and disposal proceeds.

### 6.6 Contribution-Period Split Across 1 July 2025

- **Contribution-Period Split Across 1 July 2025** — Payroll periods spanning 1 July 2025 mix the pre-LTC (22.10%/16.10%) and post-LTC (23.10%/17.10%) rates; the LTC contribution first applied to July 2025 payroll. Flag for reviewer: confirm which payroll month(s) include the LTC contribution.

### 6.7 Increased vs Standard General Allowance

- **Increased vs Standard General Allowance** — The increased general allowance applies only where total annual income ≤ EUR 16,832.00; the formula is income-sensitive. Flag for reviewer: confirm total annual income before selecting the allowance formula.

## Section 7 -- Excel Working Paper Template

```
SLOVENIA INCOME TAX -- DohDej / IID WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident / Non-resident
Income method (s.p.): Actual cost / normirani odhodki

A. BUSINESS / SELF-EMPLOYMENT INCOME (progressive base)
  A1. Client payments (net of DDV if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, etc.)      ___________
  A3. Other business income                         ___________
  A4. TOTAL business income                         ___________

B. DEDUCTIBLE EXPENSES (actual-cost method)
  B1. Office rent                                   ___________
  B2. Professional insurance                        ___________
  B3. Accountancy / legal fees                      ___________
  B4. Office supplies                               ___________
  B5. Software subscriptions                        ___________
  B6. Marketing / advertising                       ___________
  B7. Bank charges / payment processing fees        ___________
  B8. Training / professional development            ___________
  B9. Travel                                         ___________
  B10. Telecoms (business % only)                    ___________
  B11. Home office (% of utilities/rent)             ___________
  B12. Vehicle expenses (business %)                 ___________
  B13. Depreciation (fixed-asset register)           ___________
  B14. TOTAL deductible expenses                     ___________
  [If normirani odhodki: use deemed % instead --
   confirm 2025 tier before computing]

C. NET BUSINESS PROFIT (A4 - B14)                    ___________

D. OTHER PROGRESSIVE-BASE INCOME
  D1. Employment income                              ___________
  D2. Pension income                                 ___________
  D3. TOTAL other progressive income                 ___________

E. GROSS PROGRESSIVE INCOME (C + D3)                 ___________

F. ALLOWANCES
  F1. General allowance (5,260 / increased formula)  ___________
  F2. Family allowances (children/dependents)        ___________
  F3. Young-worker / disability allowance             ___________
  F4. TOTAL allowances                               ___________

G. ANNUAL TAX BASE (E - F4)                          ___________

H. PROGRESSIVE TAX (pass to deterministic engine,
   16/26/33/39/50% scale)                            ___________
  H1. Less: advance tax (akontacija) paid            ___________
  H2. Tax due / refund                               ___________

I. CAPITAL INCOME (cedular, SEPARATE -- do NOT add to G)
  I1. Dividends @ 25%                                ___________
  I2. Interest @ 25% (less 1,000 deposit exemption)  ___________
  I3. Rental @ 25%                                   ___________
  I4. Capital gains @ holding-period rate            ___________

J. SOCIAL CONTRIBUTIONS (self-employed)
  J1. ZPIZ/ZZZS/unemployment/parental/LTC            ___________
  J2. OZP flat health (37.17/month from Mar 2025)    ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Income split progressive vs cedular confirmed?
  [ ] normirani odhodki tier confirmed (if elected)?
  [ ] General allowance formula correct for income band?
  [ ] Contribution period split across 1 July 2025 (LTC)?
  [ ] OZP flat contribution applied separately?
  [ ] Home office / vehicle / phone business % documented?
  [ ] Capital-gains holding period verified?
  [ ] VAT (DDV) handled (60,000 threshold)?
```

## Section 8 -- Bank Statement Reading Guide

### Slovenian Bank Statement Formats

**Slovenian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| NLB (Nova Ljubljanska banka) | PDF, CSV | Datum, Opis, Breme, Dobro, Stanje | Most common; description holds counterparty + reference |
| NKBM / Nova KBM | PDF, CSV | Datum, Namen, Znesek, Stanje | Card transactions show merchant |
| SKB banka | PDF | Datum, Opis prometa, Breme, Dobro | Shorter descriptions |
| Intesa Sanpaolo Bank (SI) | PDF, CSV | Datum, Opis, Znesek, Stanje |  |
| Revolut / Wise Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency possible |

### Key Slovenian Banking Terms

**Key Slovenian Banking Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| NAKAZILO | Transfer | Check direction for income/expense |
| TRAJNIK / SDD | Direct debit | Regular expense (utility, subscription) |
| BREME / BREMENITEV | Debit | Outgoing -- expense |
| DOBRO / DOBROPIS | Credit | Incoming -- potential income |
| PLAČILO / PLACILO | Payment | Expense -- check counterparty |
| PROVIZIJA | Commission / fee | Bank charge (deductible) or platform fee |
| OBRESTI | Interest | Capital income (cedular 25%) or bank charge |
| NAJEMNINA | Rent | Rental income (cedular) or office rent (expense) |
| PLAČA / PLACA | Salary | Employment income (progressive base) |
| DVIG | Cash withdrawal | Ask what cash was spent on |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- SLOVENIA INCOME TAX
1. Tax residency: Slovenian resident or non-resident?
2. Income types: self-employment (s.p.), employment, pension, capital?
3. If self-employed: actual-cost accounting or normirani odhodki (lump-sum)?
4. 2025 total annual turnover (for normirani odhodki cap/tier and VAT threshold)?
5. VAT (DDV) registered? (threshold EUR 60,000 from 2025)
6. Number and order of dependent children; any dependent family members?
7. Age (for the under-29 young-worker allowance) and any disability status?
8. Total annual income (to choose standard vs increased general allowance)?
9. Home office: dedicated room? If yes, what % of floor area?
10. Vehicle/phone/internet: any business use? What %? Mileage log kept?
11. Capital income: dividends, interest, rental, or asset disposals (with acquisition dates)?
12. Social contributions (OPSVZ) and advance tax (akontacija) paid during the year?
```

## Section 10 -- Reference Material

### Key Legislation and Authority References

**Key Legislation and Authority References**

| Topic | Reference |
| --- | --- |
| Personal income tax (rates, base, allowances) | Personal Income Tax Act (ZDoh-2) (PwC) |
| Pension & disability contributions | ZPIZ-2; administered by ZPIZ (PwC) |
| Health contributions | ZZVZZ; administered by ZZZS (PwC) |
| OZP flat health contribution | ZVZZNZ (from 2024); EUR 37.17/month from 1 Mar 2025 (ZDS) |
| Long-term care contribution | Long-Term Care Act (ZDOsk-1), from 1 July 2025 (KPMG 2025-133) |
| Collection / portal | FURS; eDavki (edavki.durs.si) (FURS) |
| normirani odhodki regime | ZDoh-2 (Sibiz) |
| Penalties / default interest | Compliance summary (Commenda) -- verify vs ZDavP-2 |

### Forms and Deadlines

**Forms and Deadlines**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Informativni izračun dohodnine (IID) | Pre-filled annual income tax assessment issued by FURS to most resident individuals (employment/pension income) | FURS issues by end March / early April; taxpayer objects within 15 days of receipt (receipt deemed 15 days after dispatch) if data incorrect; otherwise IID becomes final (FURS) |
| Davek od dohodka iz dejavnosti (DohDej) | Annual self-employment business-income return (s.p.; actual-cost or normirani odhodki) | 31 March for the prior calendar year, via eDavki (FURS) |
| Self-assessed annual return (no IID) | For residents who do not receive a pre-filled IID (e.g. certain foreign-source income) | 31 July of the year following the tax year (PwC) |
| Monthly contribution statement (OPSVZ/REK) | Monthly calculation & payment of self-employed social contributions | File by the 15th, pay by the 20th of the month for the prior month (FURS) [RESEARCH GAP -- re-confirm exact dates against the current FURS calendar] |

- **Advance PIT installment threshold** — Advance PIT (akontacija) is paid in monthly installments where the advance exceeds EUR 400.  _(FURS)_

### Penalties

**Penalties**

| Type | Amount |
| --- | --- |
| Late/non-filing or non-payment | Fines from EUR 400 for minor infractions, up to EUR 75,000 for serious/repeated non-compliance by legal entities (Commenda) |
| Late payment interest | Statutory default interest accrues daily from the due date (reference rate + statutory margin) (Commenda) |

Penalty bands are from a compliance-advisory summary, not the literal ZDavP-2 text -- verify exact statutory ranges if precise figures are needed.

### Thresholds Summary

**Thresholds Summary**

| Threshold | Value | Source |
| --- | --- | --- |
| VAT (DDV) registration (domestic) | EUR 60,000 annual taxable turnover (from 2025; was 50,000) | Taxually |
| normirani odhodki revenue cap (2025) | EUR 60,000 full-time s.p. (EUR 50,000 part-time); raised to 120,000/50,000 from 2026 | Sibiz |
| Self-employed minimum contribution base | 60% of average gross wage (≈ EUR 237.02/month minimum in 2025) [RESEARCH GAP -- confirm] | Crowe; tax-checker |
| Self-employed maximum contribution base | 3.5 × insured's average monthly wage | tax-checker |
| Bank deposit interest exemption | EUR 1,000/year (EU institutions) | PwC |
| 2025 minimum gross monthly wage | EUR 1,277.72 | WageIndicator |

### Test Suite

Input: business income EUR 50,000, deductible expenses EUR 20,000, general allowance EUR 5,260, no other progressive income.
Net profit = 50,000 − 20,000 = EUR 30,000. Tax base = 30,000 − 5,260 = EUR 24,740.
Expected tax (progressive): base falls in band 2. Tax = 1,473.64 + (24,740 − 9,210.26) × 26% = 1,473.64 + 15,529.74 × 26% = 1,473.64 + 4,037.73 = EUR 5,511.37.

Employee social contributions = 2,500 × 22.10% = EUR 552.50.
Monthly general-allowance relief = 5,260 / 12 = EUR 438.33.
Monthly tax base = 2,500 − 552.50 − 438.33 = EUR 1,509.17.
Monthly bracket thresholds: 9,210.26/12 = 767.52 (16% band), 27,089/12 = 2,257.42 (26% band).
Advance tax = 767.52 × 16% + (1,509.17 − 767.52) × 26% = 122.80 + 741.65 × 26% = 122.80 + 192.83 = EUR 315.63.
Net pay (before OZP) = 2,500 − 552.50 − 315.63 = EUR 1,631.87. After OZP (37.17) = EUR 1,594.70.
(Employer additionally pays 2,500 × 16.10% = EUR 402.50 on top.) [RESEARCH GAP -- the exact monthly akontacija formula/order of allowance application should be confirmed against FURS payroll guidance; figures here apply the scale on a 1/12 basis.]

Employee contributions = 2,500 × 23.10% = EUR 577.50 (includes 1% LTC = EUR 25.00).
Employer contributions = 2,500 × 17.10% = EUR 427.50.

Input: dividend EUR 5,000.
Expected: 5,000 × 25% = EUR 1,250 final tax. NOT added to progressive base.

Input: bank deposit interest EUR 1,400 (EU institution).
Expected: taxable = 1,400 − 1,000 exemption = EUR 400; tax = 400 × 25% = EUR 100.

Input: gain EUR 10,000 on securities held 7 years.
Expected: 5–10 year band → 20% = EUR 2,000 final tax.

Input: s.p. turnover EUR 40,000, elects normirani odhodki.
Expected: STOP and flag -- confirm the 2025 tiered deemed-expense percentage and contribution-base treatment before computing (R-SI-4). Do not assume a flat 80% without confirming the tier.

## PROHIBITIONS

- NEVER compute dohodnina without confirmed tax residency
- NEVER add capital income (dividends/interest/rental/gains) to the progressive base -- it is cedular at 25% (or the holding-period CG rate)
- NEVER assume the increased general allowance without confirming total annual income ≤ EUR 16,832.00
- NEVER apply a flat 80% normirani odhodki deduction without confirming the 2025 turnover tier and eligibility
- NEVER apply post-LTC contribution rates (23.10%/17.10%) before 1 July 2025, nor pre-LTC rates after it
- NEVER treat the OZP flat health contribution (EUR 37.17/month) as a percentage or merge it with ZZZS percentage contributions
- NEVER allow income tax itself, fines, penalties, or drawings as a business deduction
- NEVER include VAT (DDV) collected on sales in business income for a registered s.p.
- NEVER present the band-5 base or any progressive figure as definitive where flagged as a [RESEARCH GAP]
- NEVER present tax calculations as definitive -- always label as estimated and route to a qualified reviewer

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
