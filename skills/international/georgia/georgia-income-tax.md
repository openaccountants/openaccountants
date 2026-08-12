---
name: georgia-income-tax
description: Use this skill whenever asked about personal income tax in the country of Georgia (Sakartvelo, GE — NOT the US state). Trigger on phrases like "how much tax do I pay in Georgia", "Georgia flat tax", "20% income tax", "small business status", "1% tax Georgia", "individual entrepreneur", "micro business status", "Georgian rental income tax", "funded pension Georgia", "rs.ge declaration", "Revenue Service of Georgia", "GEL tax", "VAT registration Georgia", or any question about filing or computing income tax for an individual, self-employed person, or individual entrepreneur tax-resident in Georgia. Also trigger when preparing or reviewing an annual income tax declaration, a monthly Small Business turnover declaration, computing the 2%+2% funded pension, or advising on PIT advance instalments. This skill covers the flat 20% PIT, Small Business Status (1%/3%), Micro Business Status (0%), rental and capital-gains rates, withholding taxes, the mandatory funded pension, VAT thresholds, deadlines, and penalties. ALWAYS read this skill before touching any Georgia income tax work.
version: 0.1
jurisdiction: GE
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Gvantsa Amiridze, ACCA
review_status: current
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia (Country) Personal Income Tax — Individuals and Self-Employed

## Georgia (Country) Personal Income Tax — Individuals and Self-Employed Skill v0.1

> **JURISDICTION WARNING.** This skill covers the **COUNTRY of Georgia (Sakartvelo / GE)**, a sovereign state in the South Caucasus — **NOT the US state of Georgia**. Currency is the **Georgian Lari (GEL)**. The tax authority is the **Revenue Service of Georgia** (`rs.ge`). If the client is in the US state of Georgia, STOP and use the US Georgia state skill instead.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Georgia (Sakartvelo), South Caucasus |
| Tax | Personal Income Tax (PIT) — flat rate |
| Currency | GEL (Georgian Lari) only |
| Tax year | Calendar year (1 January – 31 December) [PwC, Tax administration] |
| Primary legislation | Tax Code of Georgia (Law No. 3591, in force since 1 January 2011, as amended) |
| Supporting legislation | Law of Georgia on Funded Pension (No. 3303-რს, in force 1 January 2019; amended by Law No. 4312 of 27 June 2024) |
| Tax authority | Revenue Service of Georgia (sakhelmtsifo shemosavlebis samsakhuri), under the Ministry of Finance |
| Filing portal | `rs.ge` (Revenue Service e-portal) |
| Annual filing deadline | Before 1 April of the following year [PwC, Tax administration] |
| Validated by | Pending — requires sign-off by a qualified Georgian tax professional |
| Validation date | Pending |
| Skill version | 0.1 |

### Personal Income Tax Rate (2025)

- **Flat rate — no progressive brackets** — Georgia applies a single FLAT rate of personal income tax. There are NO progressive brackets.  _(PwC, Taxes on personal income)_

**Personal Income Tax Rate (2025)**  _(PwC, Taxes on personal income / Income determination)_

| Income type | Rate | Base |
| --- | --- | --- |
| Standard personal income (employment, business, most other) | **20%** | Taxable personal income — residents on worldwide income; non-residents on Georgian-source income only [PwC, Taxes on personal income] |
| Residential rental income (individual, NOT claiming deductions) | **5%** | Gross rental income; if deductions are claimed instead, the 20% rate applies [PwC, Income determination] |
| Capital gain — sale of vehicle, or apartment/house with attached land plot (non-business individual) | **5%** | Gain where not exempt; >2-year holding is generally exempt [PwC, Income determination] |

### Special Individual-Entrepreneur Regimes (instead of 20% PIT)

**Special Individual-Entrepreneur Regimes (instead of 20% PIT)**  _(PwC, Taxes on personal income)_

| Status | Rate | Base / Cap | Source |
| --- | --- | --- | --- |
| **Small Business Status** | **1%** of gross turnover; **3%** on turnover above GEL 500,000 | Annual turnover up to GEL 500,000; status revoked from 1 Jan of the third year if the cap is exceeded for two consecutive years | PwC, Taxes on personal income |
| **Micro Business Status** | **0% (exempt)** | Annual turnover below GEL 30,000, no employees | PwC, Taxes on personal income |

> **Agritourism / wine tourism GEL 700,000 variant:** the standard small-business turnover cap is GEL 500,000; a higher cap of GEL 700,000 applies to wine tourism / agrotourism activity. Verify against a primary source before relying on it.

### Withholding Taxes on Passive Income (Final WHT)

**Withholding Taxes on Passive Income (Final WHT)**  _(PwC, Corporate — withholding taxes)_

| Payment | Rate | Notes | Source |
| --- | --- | --- | --- |
| Dividends to individuals | **5%** | Final WHT | PwC, Corporate — withholding taxes |
| Interest to individuals / non-residents without PE | **5%** | Final WHT | PwC, Corporate — withholding taxes |
| Royalties | **5%** | Domestic WHT rate | PwC, Corporate — withholding taxes |
| Service fees to non-residents | **10%** | Domestic WHT rate | PwC, Corporate — withholding taxes |
| Interest / royalties / other Georgian-source income to non-residents in offshore / "black-listed" jurisdictions | **15%** | Penal rate | PwC, Corporate — withholding taxes |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown regime (standard vs Small/Micro Business Status) | Standard individual taxed at flat **20%** PIT [PwC] |
| Foreign-source income of a Georgian resident | Treat as **taxable at 20%** until the specific income type is confirmed exempt — do NOT assume exemption |
| Unknown pension participation | Assume employee is **enrolled** (2% employee + 2% employer) unless over the age cut-off or validly opted out |
| Unknown VAT status | Assume **VAT registration required** once rolling 12-month turnover crosses **GEL 100,000** |
| Unknown rental-income basis | Default to **5%** only if the individual is NOT claiming deductions; otherwise 20% |
| Unknown capital-gains holding period | Default to **taxable at 5%** unless a >2-year holding (exemption) is documented |
| Unknown residency | STOP — do not apply resident worldwide treatment without confirming the 183-day test |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — Minimum viable — bank statement for the full tax year (CSV, PDF, or pasted text) in GEL, plus confirmation of (1) tax residency (183-day test), and (2) which regime applies: standard 20% PIT, Small Business Status (1%/3%), or Micro Business Status (0%).
- **Recommended inputs** — Recommended — Individual Entrepreneur registration certificate and status confirmation, all sales invoices, monthly turnover declarations already filed, funded-pension participation status, VAT registration confirmation, prior-year annual declaration.
- **Ideal inputs** — Ideal — complete income/turnover ledger split into cash / POS / bank-transfer lines (as required for the Small Business monthly form), asset register, advance-instalment payment confirmations, and any foreign-source income documentation.
- **Refusal if minimum missing** — Refusal if minimum is missing — SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices/declarations = proceed with reviewer warning: "This computation was produced from a bank statement alone. The reviewer must verify the applicable regime, confirm turnover splits (cash/POS/transfer) for Small Business Status, and confirm that funded-pension and VAT obligations are correctly reflected."

### Refusal Catalogue

- **R-GE-1 — Wrong Georgia** — Confirm this is the COUNTRY of Georgia (Sakartvelo), not the US state. The two have entirely different tax systems. If this is the US state, stop and use the US Georgia state skill.
- **R-GE-2 — Residency unknown** — Tax residency (183+ days physical presence in any continuous 12-month period ending in the current tax year) determines whether the individual is taxed on worldwide or only Georgian-source income. Confirm residency before computing.  _([PwC, Residence])_
- **R-GE-3 — Companies / legal entities** — This skill covers individuals, the self-employed, and registered Individual Entrepreneurs only. Georgian LLCs (შპს) and other legal persons file corporate tax (the Estonian-model distributed-profits regime). Escalate to a qualified Georgian accountant.
- **R-GE-4 — Capital gains / property disposals** — Capital-gains treatment on property/vehicle sales depends on holding-period exemptions (>2 years) and business vs non-business character. Confirm the facts before applying the 5% rate; escalate complex disposals.  _([PwC, Income determination])_
- **R-GE-5 — Foreign-source / cross-border income** — Treatment of a resident's foreign-source income varies by category and treaty. Do not assume exemption. Escalate to a qualified Georgian accountant for cross-border facts.
- **R-GE-6 — Arrears / enforcement** — Client has outstanding tax arrears or is subject to Revenue Service enforcement. Late-payment interest accrues under the Tax Code [RESEARCH GAP — exact rate not confirmed from a primary source]. Do not advise; escalate to a qualified Georgian accountant immediately.
- **R-GE-7 — VAT return requested** — This skill covers personal income tax only. For Georgian VAT (18%), use the georgia-vat skill if available, or escalate.

## Section 3 — Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Georgian statements may show descriptions in Georgian (Mkhedruli) script, transliteration, or English; common transliterations are given. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

> **Regime note.** The treatment of business income depends on the regime. Under **Small Business Status**, business receipts go into the **monthly turnover declaration** (cash / POS / transfer lines) taxed at 1% (3% above GEL 500,000) — there is no expense deduction. Under **standard 20% PIT**, business profit is income minus allowable deductions. Patterns below tag the destination as "Turnover (SBS)" or "Income (20%)" where it matters.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Destination | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT, ჩარიცხვა (charitskhva), გადარიცხვა (gadaritskhva) | Turnover (SBS) / Income (20%) | Business income | If VAT-registered, 18% VAT is excluded from income/turnover |
| HONORARI, FEES, SERVICE FEE, მომსახურება (momsakhureba) | Turnover (SBS) / Income (20%) | Business / service income | Typical self-employed receipt |
| STRIPE PAYOUT, STRIPE TRANSFER | Turnover (SBS) / Income (20%) | Platform payout | Match to underlying invoices |
| PAYPAL, WISE PAYOUT, PAYONEER | Turnover (SBS) / Income (20%) | Platform payout | Verify against invoices |
| UPWORK, FIVERR, FREELANCE | Turnover (SBS) / Income (20%) | Freelance platform | Net of platform commission |
| SALARY, ANAZGHAureba, ხელფასი (khelpasi), EMPLOYER [name] | Employment income | NOT self-employment | Employer normally withholds 20% PIT + 2% pension at source |
| KIRA, RENT, ქირა (kira) | Rental income | Residential rental | 5% if no deductions claimed, else 20% |
| INTEREST, INTERESI, პროცენტი (protsenti) | Investment income | Interest | Usually subject to 5% final WHT at source |
| DIVIDEND, DIVIDENDI, დივიდენდი | Investment income | Dividend | Usually 5% final WHT at source |
| TAX REFUND, RS.GE REFUND, დაბრუნება (dabruneba) | EXCLUDE | Not income | Refund of prior tax |
| GRANT, GOVERNMENT, სახელმწიფო (sakhelmtsipo) | Check nature | Capital grants EXCLUDE; revenue grants = income | Confirm with reviewer |

### 3.2 Expense Patterns (Debits) — Deductible only under standard 20% PIT (NOT under Small/Micro Business Status)

**3.2 Expense Patterns (Debits) — Deductible only under standard 20% PIT (NOT under Small/Micro Business Status)**

| Pattern | Category | Treatment (20% regime) | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, KIRA (commercial) | Office rent | Deductible | Dedicated business premises |
| ACCOUNTANT, AUDIT, BUKHRALTERI | Accountancy fees | Deductible |  |
| LAWYER, ADVOKATI, LEGAL | Legal fees | Deductible | Must be business-related |
| OFFICE SUPPLIES, STATIONERY | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK | Marketing/advertising | Deductible |  |
| BANK FEE, SAKOMISIO, საკომისიო | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE, ANTHROPIC, OPENAI, GITHUB | Software subscription | Deductible | Recurring = operating expense |
| INTERNET, MAGTICOM, SILKNET, TELEKOM | Telecoms/broadband | Deductible (business portion) | Default 0% if mixed personal/business |
| MOBILE, GEOCELL, MAGTI, BEELINE | Phone | Deductible (business portion) | Business use only; default 0% if mixed |

> Under Small Business Status (1%/3%) and Micro Business Status (0%), tax is on **turnover**, so expense deductibility is irrelevant — record expenses for bookkeeping only.

### 3.3 Expense Patterns (Debits) — NOT Deductible (and irrelevant under SBS/Micro)

**3.3 Expense Patterns (Debits) — NOT Deductible (and irrelevant under SBS/Micro)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, CAFE, ENTERTAINMENT | Entertainment | Generally NOT deductible | Confirm with reviewer under 20% regime |
| PERSONAL, GROCERIES, SUPERMARKET, NIKORA, CARREFOUR, SPAR | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, JARIMA, ჯარიმა | Fines/penalties | NOT deductible | Public policy |
| RS.GE PAYMENT, INCOME TAX, PIT | Tax payments | NOT deductible | Tax cannot reduce its own base |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.4 Exclusions (Neither Income nor Expense)

**3.4 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN, SESEKHI, სესხი (principal movement) | EXCLUDE | Loan principal, not income/expense |
| PENSION CONTRIBUTION, FUNDED PENSION, საპენსიო (sapensio) | Pension contribution | 2% employee contribution — tracked separately, not a business expense |
| VAT PAYMENT, DGG, დღგ (VAT) | EXCLUDE | VAT liability payment, not expense |
| PIT ADVANCE, INSTALMENT | Advance tax paid | Credit against annual liability — not an expense |

### 3.5 Georgian Banks — Statement Format Reference

**3.5 Georgian Banks — Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Bank of Georgia (saqartvelos banki) | ჩარიცხვა, გადარიცხვა, საკომისიო, TRANSFER | PDF/CSV; descriptions often bilingual GE/EN; dates DD/MM/YYYY |
| TBC Bank | TRANSFER, PAYMENT, FEE, ქირა, ხელფასი | PDF/CSV; clean English exports available via internet bank |
| Liberty Bank | TRANSFER, DEPOSIT, CHARGE | PDF; commonly used for salary/state payments |
| ProCredit Bank | TRANSFER, SEPA, FEE | PDF/CSV; business-focused |
| Wise / Revolut (foreign) | TRANSFER, CONVERSION, FEE | CSV; multi-currency — convert non-GEL to GEL at the transaction-date rate |

## Section 4 — Worked Examples

> All amounts in GEL. All tax figures are estimates pending professional review.

### Example 1 — Standard self-employed individual, 20% PIT

**Input line:**
`12/03/2025 ; TBC TRANSFER IN ; SHPS ALPHA ; PAYMENT INV-2025-007 ; +5,000.00 ; GEL`

**Reasoning:**
Business receipt for a standard (non-SBS) self-employed individual. Not VAT-registered. The full GEL 5,000 is business income taxed at the flat 20% PIT after allowable deductions. [PwC, Taxes on personal income]

**Classification:** Income (20% regime) = GEL 5,000. If this individual's annual taxable profit is, say, GEL 5,000 net, PIT = 5,000 × 20% = **GEL 1,000**.

### Example 2 — Small Business Status receipt (1% turnover tax)

**Input line:**
`05/04/2025 ; BANK OF GEORGIA ; CLIENT BETA ; momsakhureba ; +8,000.00 ; GEL`

**Reasoning:**
Individual Entrepreneur with **Small Business Status**. Tax is on turnover, not profit: 1% on annual turnover up to GEL 500,000. This GEL 8,000 receipt goes on the **monthly turnover declaration** (transfer line). [PwC, Taxes on personal income]

**Classification:** Turnover (SBS) = GEL 8,000. Tax on this receipt = 8,000 × 1% = **GEL 80**. No expense deduction applies.

### Example 3 — Small Business Status above the GEL 500,000 cap (3%)

**Reasoning:**
A Small Business Status holder reaches GEL 520,000 of annual turnover. The first GEL 500,000 is taxed at 1% and the GEL 20,000 excess at 3%. [PwC, Taxes on personal income]

**Computation:**
- 500,000 × 1% = GEL 5,000
- 20,000 × 3% = GEL 600
- **Total turnover tax = GEL 5,600**

If turnover exceeds GEL 500,000 for **two consecutive years**, Small Business Status is revoked from 1 January of the third year. Flag for reviewer.

### Example 4 — Residential rental income (5%, no deductions)

**Input line:**
`01/02/2025 ; LIBERTY BANK ; TENANT ; kira tebervali ; +1,200.00 ; GEL`

**Reasoning:**
Individual rents out residential space and does NOT claim deductions, so the preferential 5% rate applies to gross rent. (If deductions were claimed, the 20% rate would apply.) [PwC, Income determination]

**Classification:** Rental income = GEL 1,200/month → GEL 14,400/year. Tax = 14,400 × 5% = **GEL 720** for the year.

### Example 5 — Employee salary with funded pension (2% + 2%)

**Reasoning:**
An enrolled employee earns gross salary GEL 3,000/month. Employer withholds 20% PIT and the 2% employee funded-pension contribution; the employer also pays a 2% employer contribution (employer cost, not deducted from the employee). The state adds a co-contribution depending on the annual income band. [PwC; National Bank of Georgia]

**Computation (one month, GEL 3,000 gross):**
- Employee funded pension (2%): 3,000 × 2% = GEL 60
- PIT (20% of gross salary): 3,000 × 20% = GEL 600 [RESEARCH GAP — confirm whether the 2% employee pension reduces the PIT base; this example applies PIT to gross. Reviewer to confirm the precise ordering under the Tax Code.]
- Employer funded pension (2%, employer cost): 3,000 × 2% = GEL 60 (not deducted from employee)
- **Employee net pay ≈ 3,000 − 600 − 60 = GEL 2,340**

State co-contribution: this employee's annualised income is 36,000, which falls in the GEL 24,000–60,000 band, so the state adds **1%** (= GEL 30 on this month's GEL 3,000). [PwC, Other taxes]

### Example 6 — Dividend received (5% final WHT)

**Input line:**
`20/06/2025 ; TBC ; SHPS GAMMA ; dividend ; +4,750.00 ; GEL`

**Reasoning:**
Dividend paid to an individual is subject to 5% final withholding tax. If GEL 4,750 was received net after 5% WHT, the gross was 4,750 / 0.95 = GEL 5,000 and GEL 250 WHT was withheld at source. No further PIT is due — it is final. [PwC, Corporate — withholding taxes]

**Classification:** Investment income, final WHT settled. Exclude from PIT base. Confirm whether the figure is gross or net with the reviewer.

## Section 5 — Tier 1 Rules (When Data Is Clear)

### 5.1 Flat Rate of Personal Income Tax

- **Flat rate of PIT** — Personal income is subject to a single flat rate of **20%**. There are no progressive brackets and no general tax-free personal allowance. Do not invent brackets.  _(Tax Code of Georgia [PwC, Taxes on personal income])_

### 5.2 Residency and Scope

- **Residency test and scope** — Tax residency = physical presence of 183 days or more in any continuous 12-month period ending in the current tax year. Residency is determined per tax period; days do not carry forward. Residents are taxed on worldwide income; non-residents only on Georgian-source income. Foreign-source income of a resident is, under Georgia's territorial-leaning rules, often exempt in practice — but treatment varies by income type. Default to taxable at 20% until the specific type is confirmed exempt.  _(Tax Code of Georgia [PwC, Residence])_

### 5.3 Small Business Status (Individual Entrepreneur)

**5.3 Small Business Status (Individual Entrepreneur)**  _([Tax Code of Georgia; rs.ge preferential-tax guidance. Corrected by Gvantsa Amiridze (ACCA, Georgia)](https://www.rs.ge/PersonsPreferentialTax?cat=2&tab=1))_

| Condition | Rule |
| --- | --- |
| Tax base | Gross **turnover** (not profit) |
| Rate up to the turnover cap | **1%** |
| Turnover cap | **GEL 500,000**/year standard; **GEL 700,000**/year for wine tourism and agrotourism |
| Rate above the cap | **3%**, charged on the **excess only** — not on total turnover |
| Revocation | If turnover exceeds the cap for two consecutive years, status is revoked from 1 January of the third year |
| Filing | Monthly turnover declaration by the 15th of the following month (zero declaration required even with no income; missing one incurs a GEL 100 fine per declaration) |

### 5.4 Micro Business Status

**5.4 Micro Business Status**  _(Tax Code of Georgia [PwC, Taxes on personal income])_

| Condition | Rule |
| --- | --- |
| Tax | **0% (exempt)** on business income |
| Turnover cap | Below **GEL 30,000** per year |
| Employees | None permitted |

### 5.5 Rental and Capital-Gains Rates

**5.5 Rental and Capital-Gains Rates**  _(Tax Code of Georgia [PwC, Income determination])_

| Item | Rate |
| --- | --- |
| Residential rental income, individual NOT claiming deductions | **5%** on gross rent |
| Residential rental income, deductions claimed | **20%** |
| Gain on sale of vehicle or apartment/house with land (non-business, not exempt) | **5%** |
| Same asset held **>2 years** | Generally **exempt** [confirm holding-period mechanics — see caveats] |

### 5.6 Withholding Taxes (Final)

**5.6 Withholding Taxes (Final)**  _(Tax Code of Georgia [PwC, Corporate — withholding taxes])_

| Payment | Rate |
| --- | --- |
| Dividends to individuals | 5% (final) |
| Interest to individuals / non-residents without PE | 5% (final) |
| Royalties | 5% |
| Service fees to non-residents | 10% |
| Income to non-residents in black-listed jurisdictions | 15% |

### 5.7 Mandatory Funded Pension

**5.7 Mandatory Funded Pension**  _(Law of Georgia on Funded Pension (No. 3303-რს) [National Bank of Georgia; PwC, Other taxes])_

| Contributor | Rate | Cap |
| --- | --- | --- |
| **Employee** | 2% | No cap |
| **Employer** | 2% | No cap |
| **State co-contribution** | 2% if annual income < GEL 24,000; 1% if GEL 24,000–60,000; 0% above GEL 60,000 | State co-contribution ceases once accumulated annual income reaches GEL 60,000 [PwC, Other taxes — GEL 24,000/60,000 thresholds sourced to PwC, not directly confirmed from the NBG English page] |
| **Self-employed (voluntary)** | 4% of annual income (own contribution; no separate employer share) | — |

- **Scheme structure** — The scheme operates on a 2% + 2% + up to 2% basis on gross (untaxed) salary income.  _(Law of Georgia on Funded Pension (No. 3303-რს) [National Bank of Georgia; PwC, Other taxes])_
- **Arithmetic check** — Arithmetic check (employee + employer columns): employee 2% + employer 2% = 4% mandatory payroll cost, plus a state co-contribution of 0–2% on top. There is no aggregate "total" cap on the employee or employer 2% — only the state co-contribution is income-capped at GEL 60,000.
- **Participation** — Participation: mandatory for employees who had NOT reached age 60 (men) / 55 (women) when the law took effect (1 January 2019); older employees and the self-employed participate voluntarily.

### 5.8 No General Social Security

- **No general social security** — Georgia has NO general social security / social insurance contributions. The funded pension is the only mandatory payroll-linked levy.  _([PwC, Other taxes])_

### 5.9 VAT Interaction

**5.9 VAT Interaction**  _(Tax Code of Georgia [Andersen in Georgia])_

| Item | Rule |
| --- | --- |
| Standard VAT rate | **18%** |
| Mandatory registration threshold | **GEL 100,000** of taxable turnover in any continuous 12-month period (register within 2 business days of exceeding) |
| VAT declaration | Monthly, by the 15th of the following month |
| Effect on income | VAT collected on sales is NOT income; for a VAT-registered person, report income/turnover net of VAT |

> The GEL 100,000 VAT threshold is **independent** of the GEL 500,000 Small Business Status cap. A Small Business Status holder can still be required to register for VAT.

### 5.10 Filing, Instalments, and Penalties

**5.10 Filing, Instalments, and Penalties**  _(Tax Code of Georgia [PwC, Tax administration])_

| Item | Detail |
| --- | --- |
| Annual individual income tax declaration | Due **before 1 April** of the year following the tax year (commonly cited as 31 March / by 1 April) [PwC — exact wording: "before 1 April"] |
| Self-employed PIT advance instalments | Four instalments: **15 May, 15 July, 15 September, 15 December** [PwC, Tax administration] |
| Small Business / Individual Entrepreneur turnover declaration | **Monthly**, by the 15th of the following month; zero declaration required [JustAdvisors] |
| Property/asset-sale (capital gain) declaration | By the 15th day of the month following the transaction month (monthly basis since January 2024) [PwC, Tax administration] |
| Monthly VAT declaration | By the 15th of the following month [Andersen in Georgia] |
| Employer PIT/pension monthly reporting & remittance | Generally by the 15th of the following month [PwC, Tax administration] |
| Late filing penalty | 5% of tax due if ≤2 months late; 10% of tax due if >2 months late; nil if tax due is zero |
| Late payment interest | 0.05% per day on the principal tax debt, from the day after the payment deadline |

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Regime Selection (Standard vs Small vs Micro Business Status)

- **Regime selection guidance** — Choosing 1% Small Business Status vs 20% standard PIT depends on margins, expense levels, and turnover trajectory. Confirm the Individual Entrepreneur is correctly registered and that the chosen status is active for the tax year. Conservative default: standard 20% PIT until status registration is confirmed. Flag for reviewer: confirm registration, active status, and turnover proximity to the GEL 30,000 (Micro) / GEL 500,000 (Small) caps.

### 6.2 Foreign-Source Income of Residents

- **Foreign-source income guidance** — Treatment varies by income type; some foreign-source income is exempt under Georgia's source rules, but this is not automatic. Conservative default: treat as taxable at 20% until the specific category is confirmed exempt. Flag for reviewer: confirm category-by-category treatment and any applicable treaty.

### 6.3 Rental Income — 5% vs 20%

- **Rental income guidance** — The 5% rate applies only where the individual does NOT claim deductions; claiming deductions forces the 20% rate. Conservative default: 5% on gross residential rent if no deductions are claimed. Flag for reviewer: confirm whether deductions are being claimed and whether the property is residential.

### 6.4 Capital-Gains Exemption Holding Period

- **Capital gains holding period guidance** — Gains on a vehicle or apartment/house with land held >2 years are generally exempt; otherwise 5% applies. Conservative default: taxable at 5% unless the >2-year holding is documented. Flag for reviewer: confirm acquisition date, holding period, and non-business character. [Exact >2-year mechanics — see caveats.]

### 6.5 Funded-Pension Participation and PIT-Base Ordering

- **Funded-pension participation guidance** — Confirm whether the worker is enrolled (age cut-off, opt-out status for the self-employed). Confirm the precise interaction between the 2% employee contribution and the 20% PIT base. Conservative default: assume enrolment; apply PIT to gross salary. Flag for reviewer: confirm enrolment and PIT-base ordering. [RESEARCH GAP — see Section 5.7 / Example 5.]

### 6.6 VAT Registration Trigger

- **VAT registration trigger guidance** — Monitor rolling 12-month turnover against the GEL 100,000 threshold; registration is due within 2 business days of crossing it. Flag for reviewer: confirm whether and when the threshold was crossed and that registration was timely.

## Section 7 — Excel Working Paper Template

```
GEORGIA (COUNTRY) PERSONAL INCOME TAX — WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency (183-day test): Resident / Non-resident
Regime: Standard 20% PIT / Small Business 1%(3%) / Micro Business 0%
Currency: GEL

A. BUSINESS INCOME / TURNOVER
  A1. Client payments (net of 18% VAT if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, Wise, etc.)    ___________
  A3. Other business income                            ___________
  A4. TOTAL business income / turnover                 ___________

B. DEDUCTIONS  (STANDARD 20% REGIME ONLY — leave blank for SBS/Micro)
  B1. Office rent                                      ___________
  B2. Accountancy / legal fees                         ___________
  B3. Software subscriptions                           ___________
  B4. Marketing / advertising                          ___________
  B5. Bank / payment processing fees                   ___________
  B6. Telecoms (business %)                             ___________
  B7. Other allowable expenses                         ___________
  B8. TOTAL deductions                                 ___________

C. NET BUSINESS PROFIT (A4 - B8)  [20% regime]         ___________

D. OTHER INCOME
  D1. Employment income (gross salary)                 ___________
  D2. Residential rental income (gross)                ___________
  D3. Capital gains (vehicle / property, if taxable)   ___________
  D4. Dividends / interest / royalties (note: 5% final
      WHT usually settled at source — exclude if final) ___________

E. TAX COMPUTATION (pass to deterministic engine)
  STANDARD 20% PIT:
    E1. PIT base (C + D1 + applicable other)           ___________
    E2. PIT @ 20%                                       ___________
  SMALL BUSINESS STATUS:
    E3. Turnover up to 500,000 @ 1%                     ___________
    E4. Turnover above 500,000 @ 3%                     ___________
  RENTAL @ 5% (if no deductions): D2 × 5%               ___________
  CAPITAL GAIN @ 5% (if taxable): D3 × 5%               ___________

F. FUNDED PENSION (employees / voluntary self-employed)
  F1. Employee 2% of gross salary                      ___________
  F2. Employer 2% of gross salary (employer cost)      ___________
  F3. State co-contribution (2%/1%/0% by income band)  ___________
  F4. Self-employed voluntary 4% (if applicable)       ___________

G. CREDITS / PAYMENTS
  G1. PIT advance instalments paid                     ___________
  G2. WHT already withheld at source (final items)     ___________
  G3. Tax due / refund                                 ___________

REVIEWER FLAGS:
  [ ] COUNTRY of Georgia confirmed (not US state)?
  [ ] Residency (183-day) confirmed?
  [ ] Regime (20% / SBS / Micro) confirmed and registered?
  [ ] Foreign-source income treatment confirmed?
  [ ] Rental 5% vs 20% basis confirmed?
  [ ] Capital-gains holding period (>2yr exemption) confirmed?
  [ ] Funded-pension enrolment and PIT-base ordering confirmed?
  [ ] VAT registration (GEL 100,000) status confirmed?
  [ ] Small Business monthly declarations filed (cash/POS/transfer)?
```

## Section 8 — Bank Statement Reading Guide

### Georgian Bank Statement Formats

**Georgian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Bank of Georgia | PDF, CSV | Date, Description, Debit, Credit, Balance | Bilingual GE/EN; description holds counterparty + reference |
| TBC Bank | PDF, CSV | Date, Description, Amount, Balance | Clean English exports via internet bank |
| Liberty Bank | PDF | Date, Particulars, Withdrawals, Deposits | Often used for salary/state payments |
| ProCredit Bank | PDF, CSV | Date, Description, Amount, Balance | Business-focused; SEPA references |
| Wise / Revolut | CSV | Date, Counterparty, Amount, Currency, Reference | Multi-currency — convert to GEL at transaction-date rate |

### Key Georgian Banking / Tax Terms

**Key Georgian Banking / Tax Terms**

| Term (transliteration) | Georgian | English | Classification Hint |
| --- | --- | --- | --- |
| gadaritskhva | გადარიცხვა | Transfer | Check direction for income/expense |
| charitskhva | ჩარიცხვა | Credit / deposit | Potential income |
| khelpasi | ხელფასი | Salary | Employment income |
| kira | ქირა | Rent | Rental income (5% / 20%) |
| momsakhureba | მომსახურება | Service | Business / service income |
| sakomisio | საკომისიო | Commission / fee | Bank charge (deductible under 20% regime) |
| protsenti | პროცენტი | Interest | Interest income (5% WHT) |
| dividendi | დივიდენდი | Dividend | Dividend (5% final WHT) |
| sapensio | საპენსიო | Pension | Funded-pension contribution |
| DGG / dghg | დღგ | VAT | Exclude from income |
| jarima | ჯარიმა | Fine / penalty | Not deductible |
| seskhi | სესხი | Loan | Principal movement — exclude |

## Section 9 — Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING — reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS — GEORGIA (COUNTRY) INCOME TAX
1. Is this the COUNTRY of Georgia (Sakartvelo), not the US state? (confirm)
2. Tax residency: were you physically present 183+ days in any continuous 12-month period ending in this tax year?
3. Regime: standard 20% PIT, Small Business Status (1%/3%), or Micro Business Status (0%)? Are you a registered Individual Entrepreneur?
4. Approximate annual turnover (relevant to the GEL 30,000 / 100,000 / 500,000 thresholds)?
5. Are you VAT-registered (turnover over GEL 100,000 in any 12-month period)?
6. Employment income: any salary? If so, are you enrolled in the funded pension (born before/after the age cut-off)?
7. Rental income: any residential rent received? Do you intend to claim deductions (20%) or not (5%)?
8. Capital gains: did you sell a vehicle or apartment/house with land? Acquisition date / holding period?
9. Passive income: dividends, interest, royalties? (these usually carry 5% final WHT at source)
10. Foreign-source income: any income from outside Georgia?
11. PIT advance instalments paid this year (15 May / 15 Jul / 15 Sep / 15 Dec)?
```

## Section 10 — Reference Material

### Key Legislation and Authority References

**Key Legislation and Authority References**

| Topic | Reference |
| --- | --- |
| Flat 20% PIT; Small/Micro Business Status | Tax Code of Georgia (Law No. 3591) [PwC, Taxes on personal income] |
| Residency (183-day rule) | Tax Code of Georgia [PwC, Residence] |
| Rental and capital-gains 5% rates | Tax Code of Georgia [PwC, Income determination] |
| Withholding taxes (5% / 10% / 15%) | Tax Code of Georgia [PwC, Corporate — withholding taxes] |
| Funded pension (2%+2%+state) | Law on Funded Pension No. 3303-რს [National Bank of Georgia; matsne.gov.ge] |
| VAT (18%, GEL 100,000 threshold) | Tax Code of Georgia [Andersen in Georgia] |
| Deadlines and instalments | Tax Code of Georgia [PwC, Tax administration; JustAdvisors] |
| Minimum wage | Presidential Decree No. 351 (1999): GEL 20/month private, GEL 115/month public [CXC Global] — effectively obsolete; market wages far higher |
| Penalties / late-payment interest | Tax Code of Georgia — late filing 5% of tax due (≤2 months) / 10% (>2 months), nil if no tax is due; late payment 0.05% per overdue day |

### Sources

1. PwC Worldwide Tax Summaries — Georgia, Individual: Taxes on personal income — https://taxsummaries.pwc.com/georgia/individual/taxes-on-personal-income
2. PwC Worldwide Tax Summaries — Georgia, Individual: Other taxes (pension, VAT, social security) — https://taxsummaries.pwc.com/georgia/individual/other-taxes
3. PwC Worldwide Tax Summaries — Georgia, Individual: Income determination — https://taxsummaries.pwc.com/georgia/individual/income-determination
4. PwC Worldwide Tax Summaries — Georgia, Individual: Tax administration — https://taxsummaries.pwc.com/georgia/individual/tax-administration
5. PwC Worldwide Tax Summaries — Georgia, Individual: Residence — https://taxsummaries.pwc.com/georgia/individual/residence
6. PwC Worldwide Tax Summaries — Georgia, Corporate: Withholding taxes — https://taxsummaries.pwc.com/georgia/corporate/withholding-taxes
7. National Bank of Georgia — Funded Pension Scheme — https://nbg.gov.ge/en/page/funded-pension-scheme
8. Legislative Herald of Georgia (matsne.gov.ge) — On Funded Pension — https://www.matsne.gov.ge/en/document/view/4280127
9. Andersen in Georgia — Rules for Mandatory and Voluntary VAT Registration — https://ge.andersen.com/rules-for-mandatory-and-voluntary-vat-registration-in-georgia/
10. JustAdvisors — Small Business in Georgia 2025: Updated Tax Declaration — https://en.justadvisors.ge/blog/finance/deklaration_pe_2025
11. CXC Global — Georgia Payroll & Benefits guide (minimum wage) — https://www.cxcglobal.com/global-hiring-guide/georgia/payroll-and-benefits-in-georgia/

> **Research caveats (reviewer to confirm against primary sources):** (1) exact penalty / late-payment interest amounts under the Tax Code of Georgia; (2) precise treatment/exemption of resident foreign-source income by category; (3) capital-gains exemption holding-period (>2 years) mechanics for property/vehicles; (4) whether the annual-return deadline is "31 March" or "before 1 April" (PwC says "before 1 April"); (5) the GEL 24,000 / 60,000 state pension co-contribution thresholds are sourced to PwC, not directly confirmed from the NBG English page (which states only the 2%+2%+2% principle); (6) the agritourism GEL 700,000 small-business variant; (7) whether the 2% employee pension contribution reduces the 20% PIT base. No FX rate was fixed — convert GEL at current rates as needed.

### Test Suite

Input: Resident, standard regime, net business profit GEL 40,000, no other income.
Expected: PIT base = GEL 40,000. PIT = 40,000 × 20% = **GEL 8,000**.

Input: Individual Entrepreneur, Small Business Status, annual turnover GEL 120,000.
Expected: Turnover tax = 120,000 × 1% = **GEL 1,200** (filed across monthly declarations). No expense deduction.

Input: Small Business Status, annual turnover GEL 520,000.
Expected: 500,000 × 1% = 5,000; 20,000 × 3% = 600; total = **GEL 5,600**. Flag two-consecutive-year revocation risk.

Input: Micro Business Status, turnover GEL 22,000, no employees.
Expected: Tax = **GEL 0** (exempt). Confirm turnover stays below GEL 30,000.

Input: Individual, residential rent GEL 14,400/year, no deductions claimed.
Expected: Tax = 14,400 × 5% = **GEL 720**.

Input: Dividend GEL 5,000 gross paid to an individual.
Expected: WHT = 5,000 × 5% = **GEL 250**, final. Net received GEL 4,750. Excluded from PIT base (final WHT).

Input: Employee gross salary GEL 3,000/month, enrolled.
Expected: Employee 2% = GEL 60; employer 2% = GEL 60; PIT 20% of gross = GEL 600; net pay ≈ GEL 2,340 (subject to PIT-base ordering caveat). Annualised income GEL 36,000 → state co-contribution 1%.

Input: Client is in Atlanta, Georgia, USA.
Expected: STOP. This skill is for the country of Georgia only. Redirect to the US Georgia state skill.

## PROHIBITIONS

- NEVER confuse the COUNTRY of Georgia (GE) with the US state of Georgia — confirm jurisdiction first
- NEVER invent progressive brackets — Georgian PIT is a single flat 20%
- NEVER apply expense deductions under Small Business Status or Micro Business Status — those regimes tax turnover, not profit
- NEVER assume a resident's foreign-source income is exempt without confirming the specific income type
- NEVER apply the 5% rental rate when the individual is claiming deductions (then it is 20%)
- NEVER treat the 5% / 10% / 15% withholding items as additional PIT when they are final WHT settled at source
- NEVER omit the funded pension for an enrolled employee (2% employee + 2% employer)
- NEVER state a penalty or late-payment interest figure as fact — those are RESEARCH GAPS pending confirmation
- NEVER include VAT collected on sales as income for a VAT-registered person
- NEVER present tax calculations as definitive — always label as estimated, pending professional review

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
