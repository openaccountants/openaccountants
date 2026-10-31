---
name: zw-income-tax
description: Use this skill whenever asked about Zimbabwe income tax (PAYE, self-employed trade tax, or provisional tax) for individuals. Trigger on phrases like "how much PAYE do I pay", "ZIMRA tax tables", "USD tax bands", "ZiG / ZWG tax", "AIDS levy", "ITF1", "ITF12C", "ITF12B", "QPD provisional tax", "self-employed tax Zimbabwe", "NSSA contributions", "tax-free threshold Zimbabwe", "elderly credit", or any question about filing or computing income tax for an employee or a self-employed trader in Zimbabwe. Also trigger when classifying a Zimbabwean bank statement (USD or ZiG), computing the 3% AIDS levy, or advising on QPD instalments. This skill covers the dual-currency PAYE tables (USD and ZWG), the flat 25% trade/business rate, the AIDS levy, NSSA, provisional tax (QPDs), filing forms/deadlines, and registration/VAT thresholds. ALWAYS read this skill before touching any Zimbabwe income tax work.
jurisdiction: ZW
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# zimbabwe-income-tax

## Zimbabwe Income Tax -- Individual & Self-Employed Skill v0.1

> **Tier 2 (research-verified).** Figures are drawn from ZIMRA Jan-Dec 2025 PAYE tax tables, ZIMRA corporate/individual rate pages, NSSA contribution schedules, and reputable secondary sources (PwC Worldwide Tax Summaries, Lucent, M&J Consultants). Every figure carries an inline citation or an explicit `[RESEARCH GAP -- reviewer to confirm]` marker. This skill has NOT yet been signed off by a registered Zimbabwean tax practitioner.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Zimbabwe (Republic of Zimbabwe) |
| Tax | Income Tax / Pay-As-You-Earn (PAYE) |
| Currency | **Dual currency** -- USD (foreign currency) AND ZiG / ZWG (Zimbabwe Gold). Separate tax tables for each. |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act [Chapter 23:06]; Finance Act (annual) |
| Trade/business rate | Finance Act s.14(2b) -- flat 25% for individuals from trade and investments |
| Tax authority | Zimbabwe Revenue Authority (ZIMRA) -- https://www.zimra.co.zw |
| Filing portal | TaRMS (Tax and Revenue Management System) |
| Social security authority | National Social Security Authority (NSSA) -- https://www.nssa.org.zw |
| Annual filing deadline | 30 April of the following year (ITF1 and ITF12C) -- ZIMRA Public Notice 20 of 2026 (via fingaz.co.zw, 2026-04-18) |
| AIDS Levy | 3% of income tax payable (added after tax computed) -- stated on ZIMRA 2025 PAYE tables |
| Validated by | Pending -- requires sign-off by a registered Zimbabwean tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

### How the dual-currency system works

Zimbabwe taxes income in the currency it is earned. An employee paid in USD is taxed on the **USD PAYE table**; an employee paid in ZiG/ZWG is taxed on the **ZWG PAYE table**. An employee paid in both currencies has each stream taxed under its own table. The **3% AIDS Levy** is then added to the income tax computed (it is a levy ON the tax, not on income). Source: ZIMRA Jan-Dec 2025 PAYE tax tables.

> **ZWG instability note.** The ZiG (introduced April 2024, replacing ZWL) is subject to devaluation, and ZIMRA may revise ZWG bands mid-year by public notice. The USD bands are the more stable reference. Always confirm the current ZWG table against the latest ZIMRA publication before computing in ZiG.

### PAYE Tax Brackets -- USD (Foreign Currency), 2025 -- MONTHLY

**PAYE Tax Brackets -- USD (Foreign Currency), 2025 -- MONTHLY**  _(ZIMRA USD Jan-Dec 2025 PAYE table (https://www.zimra.co.zw/domestic-taxes/tax-tables?download=4211:usd-jan-dec-2025-tax-tables))_

| Monthly income (USD) | Rate | Deduct (USD) | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 -- 100.00 | 0% | -- | USD 0.00 |
| 100.01 -- 300.00 | 20% | 20.00 | USD 40.00 |
| 300.01 -- 1,000.00 | 25% | 35.00 | USD 215.00 |
| 1,000.01 -- 2,000.00 | 30% | 85.00 | USD 515.00 |
| 2,000.01 -- 3,000.00 | 35% | 185.00 | USD 865.00 |
| 3,000.01 and above | 40% | 335.00 | -- |

- **Deduct method** — Each bracket taxes only its slice. "Deduct" is the ZIMRA shortcut: tax = (income x rate) - deduct.  _(ZIMRA USD Jan-Dec 2025 PAYE table (https://www.zimra.co.zw/domestic-taxes/tax-tables?download=4211:usd-jan-dec-2025-tax-tables))_
- **Tax-free threshold (USD)** — USD 100/month = USD 1,200/year. Top effective rate including AIDS levy = 40% x 1.03 = 41.2%.  _(ZIMRA USD Jan-Dec 2025 PAYE table)_

### PAYE Tax Brackets -- USD, 2025 -- ANNUAL

**PAYE Tax Brackets -- USD, 2025 -- ANNUAL**  _(ZIMRA USD Jan-Dec 2025 PAYE table)_

| Annual income (USD) | Rate | Deduct (USD) | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 -- 1,200 | 0% | -- | USD 0 |
| 1,201 -- 3,600 | 20% | 240 | USD 480 |
| 3,601 -- 12,000 | 25% | 420 | USD 2,580 |
| 12,001 -- 24,000 | 30% | 1,020 | USD 6,180 |
| 24,001 -- 36,000 | 35% | 2,220 | USD 10,380 |
| 36,001 and above | 40% | 4,020 | -- |

> USD daily/weekly/fortnightly tables also exist (e.g. daily tax-free up to USD 3.29; top 40% above USD 98.64). Source: ZIMRA USD 2025 table. Use the table that matches the pay period.

### PAYE Tax Brackets -- ZWG (Zimbabwe Gold), 2025 -- MONTHLY

**PAYE Tax Brackets -- ZWG (Zimbabwe Gold), 2025 -- MONTHLY**  _(ZIMRA ZWG 2025 PAYE table (https://www.zimra.co.zw/domestic-taxes/tax-tables?download=4205:zwg-2025-tax-tables))_

| Monthly income (ZWG) | Rate | Deduct (ZWG) | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 -- 2,800 | 0% | -- | ZWG 0 |
| 2,800.01 -- 8,400 | 20% | 560 | ZWG 1,120 |
| 8,400.01 -- 28,000 | 25% | 980 | ZWG 6,020 |
| 28,000.01 -- 56,000 | 30% | 2,380 | ZWG 14,420 |
| 56,000.01 -- 84,000 | 35% | 5,180 | ZWG 24,220 |
| 84,000.01 and above | 40% | 9,380 | -- |

- **Tax-free threshold (ZWG)** — 2,800/month.  _(ZIMRA ZWG 2025 PAYE table)_

### PAYE Tax Brackets -- ZWG, 2025 -- ANNUAL

**PAYE Tax Brackets -- ZWG, 2025 -- ANNUAL**  _(ZIMRA ZWG 2025 PAYE table)_

| Annual income (ZWG) | Rate | Deduct (ZWG) | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 -- 33,600 | 0% | -- | ZWG 0 |
| 33,601 -- 100,800 | 20% | 6,720 | ZWG 13,440 |
| 100,801 -- 336,000 | 25% | 11,760 | ZWG 72,240 |
| 336,001 -- 672,000 | 30% | 28,560 | ZWG 173,040 |
| 672,001 -- 1,008,000 | 35% | 62,160 | ZWG 290,640 |
| 1,008,001 and above | 40% | 112,560 | -- |

### Other Rates and Credits (2025)

**Other Rates and Credits (2025)**

| Item | Value | Source |
| --- | --- | --- |
| AIDS Levy | 3% of income tax payable | ZIMRA 2025 PAYE tables; ZIMRA corporate tax rates |
| Individuals -- trade & investment income | Flat 25% + 3% AIDS = **25.75% effective** | ZIMRA corporate/business tax rates (Finance Act s.14(2b)) |
| Companies / trusts | 25% + 3% AIDS = **25.75% effective** | ZIMRA corporate tax rates |
| Tax-free bonus / performance award exemption | USD 700 (ZWG equivalent for ZiG earners) | ZIMRA PAYE page |
| Elderly persons' credit (age 55+) | USD 900 / year (or ZWG equivalent) | ZIMRA elderly concession page |
| Blind / disabled persons' credit | USD 900 / year (or ZWG equivalent) | ZIMRA concessions |
| VAT compulsory registration threshold | USD 25,000 (or ZWG equivalent) per rolling 12 months | ZIMRA VAT registration page |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown currency of pay (USD vs ZWG) | STOP -- cannot pick a tax table without the currency of earnings |
| Unknown pay period | Treat as monthly and flag for reviewer |
| Employment vs trade income unclear | Treat as trade income only if clearly a business; otherwise STOP |
| Unknown elderly/disability status | Apply NO credit (claim only on confirmation) |
| Unknown bonus amount vs exemption | Apply exemption only up to confirmed USD 700 ceiling |
| Unknown NSSA insurable earnings | Apply ceiling of USD 700 (or ZWG equivalent) |
| Unknown whether expense is wholly for trade | Not deductible |
| Mixed-use expense, no apportionment basis | 0% deduction |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — the currency the client is paid in (USD and/or ZWG), the pay period, gross earnings, and whether the person is a pure employee (PAYE/FDS) or carries on a trade/profession. For traders: a bank statement for the full tax year (CSV, PDF, or pasted text).
- **Recommended inputs** — payslips or employer PAYE schedules, bonus details, age (for the 55+ credit), disability status, NSSA contribution records, prior-year ITF1/ITF12C or assessment, VAT registration status, QPD payment confirmations.
- **Ideal inputs** — complete income and expenditure account, invoices/receipts supporting every deduction, asset register, provisional tax (QPD) payment proofs, employment income details if combined with trade income.
- **Refusal if minimum is missing -- SOFT WARN** — No currency-of-pay = hard stop (cannot select a table). For traders, no bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from a bank statement alone. The reviewer must verify that all deductions are supported by valid documentation and meet the wholly-and-exclusively test under the Income Tax Act."

### Refusal Catalogue

- **R-ZW-1** — Currency of earnings unknown. "Zimbabwe operates separate USD and ZWG PAYE tables. This skill cannot compute tax without knowing the currency (or currencies) in which the client is paid. Please confirm before proceeding."
- **R-ZW-2** — Companies, partnerships, trusts. "This skill covers individuals (employees and sole traders/professionals) only. Companies, partnerships, and trusts file separately. Escalate to a registered tax practitioner."
- **R-ZW-3** — Non-resident / source-and-residence complexity. "Non-resident taxation, withholding taxes on non-residents, and double-tax-treaty relief require specialised analysis. Out of scope. Escalate to a registered tax practitioner."
- **R-ZW-4** — Capital gains / property disposals. "Capital gains tax on specified assets and immovable property is a separate regime. Out of scope. Escalate to a registered tax practitioner."
- **R-ZW-5** — Presumptive tax / informal sector full schedule. "Presumptive tax categories and exact USD amounts are revised in the annual Finance Act and ZIMRA public notices. This skill carries only headline figures. Confirm the full schedule against the current ZIMRA presumptive-tax public notice. Escalate if precise per-category amounts are needed."
- **R-ZW-6** — Arrears / enforcement / penalties. "Client has outstanding arrears or is subject to ZIMRA enforcement. Late-filing penalties can reach 100% of tax due, plus interest at the prescribed rate. Do not advise. Escalate to a registered tax practitioner immediately."
- **R-ZW-7** — VAT return requested. "This skill covers income tax / PAYE only. Zimbabwe VAT (including fiscalisation under Public Notice 30 of 2025) is out of scope here."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank-statement transaction matches a pattern below, apply the treatment directly. Statements may be in USD or ZiG/ZWG -- read the currency column. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or narration as it appears on the statement. If multiple patterns match, use the most specific. Many Zimbabwean statements mix English and Shona/Ndebele terms -- see Section 8.

### 3.1 Income Patterns (Credits)

**3.1 Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, SALARIES, WAGES, MUHOLO | Employment income -- PAYE table | Apply USD or ZWG table per currency |
| PAYE REFUND, ZIMRA REFUND | EXCLUDE | Refund of prior tax, not income |
| Client name + PAYMENT, DEPOSIT, INV | Trade income (flat 25%) | If VAT-registered, extract net of 15% VAT |
| ECOCASH, ONEMONEY, INNBUCKS (business receipt) | Trade income | Mobile-money receipt -- match to invoices |
| CONSULTANCY, FEES, PROFESSIONAL FEES | Trade income | Self-employed professional -- now on QPD system (see 5.6) |
| STRIPE, PAYPAL, WISE, PAYONEER PAYOUT | Trade income | Platform/forex payout -- usually USD |
| RENT RECEIVED, KIRINGO, RENTAL | Investment income | Separate source; flag for reviewer |
| INTEREST, INTERESSI | Investment income | Interest income |
| DIVIDEND | Investment income | Usually subject to withholding at source |
| BONUS, PERFORMANCE AWARD | Employment income | First USD 700 (or ZWG equiv) exempt -- see 5.4 |
| GOVERNMENT GRANT, NGO GRANT | Check nature | Capital grants EXCLUDE; revenue grants = trade income |

### 3.2 Expense Patterns (Debits) -- Deductible for Traders (wholly & exclusively)

**3.2 Expense Patterns (Debits) -- Deductible for Traders (wholly & exclusively)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RENT, OFFICE RENT, SHOP RENT | Business premises rent | Deductible | Trade premises only |
| ZESA, ZETDC | Electricity | Deductible (business %) | Apportion if home-based |
| TELONE, ECONET, NETONE, TELECEL, LIQUID | Telecoms/data | Deductible (business %) | Default 0% if mixed-use |
| ACCOUNTANT, AUDITOR, BOOKKEEP, ICAZ | Accountancy fees | Deductible |  |
| LEGAL, LAWYER, ATTORNEY (business) | Legal fees | Deductible | Must be trade-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS | Advertising | Deductible |  |
| BANK CHARGE, LEDGER FEE, IMTT* | Bank charges | Deductible (business account) | *IMTT = Intermediated Money Transfer Tax; flag for reviewer on deductibility |
| INSURANCE (business, indemnity) | Insurance | Deductible | Trade cover only |
| FUEL, ZUVA, PUMA, TOTAL, ENGEN | Vehicle fuel | Deductible (business %) | Requires mileage basis |

### 3.3 Expense Patterns (Debits) -- Software / SaaS (Deductible for Traders)

**3.3 Expense Patterns (Debits) -- Software / SaaS (Deductible for Traders)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| MICROSOFT 365, GOOGLE WORKSPACE | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, ZOOM, SLACK, NOTION | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, AWS | Software / cloud | Deductible | Usually USD-denominated |

### 3.4 Expense Patterns (Debits) -- NOT Deductible

**3.4 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GROCERIES, SUPERMARKET, OK, PICK N PAY, TM | Personal | NOT deductible | Private living costs |
| RESTAURANT, ENTERTAINMENT, CLIENT LUNCH | Entertainment | NOT deductible (flag) | Generally disallowed -- reviewer to confirm |
| FINE, PENALTY, SPOT FINE | Fines/penalties | NOT deductible | Public policy |
| ZIMRA PAYMENT, INCOME TAX, PAYE PAID | Tax payments | NOT deductible | Tax is not an expense of earning income |
| DRAWINGS, OWN USE, PERSONAL ATM | Drawings | NOT deductible | Not an expense |
| SCHOOL FEES, MEDICAL (personal) | Personal | NOT deductible | Private |

### 3.5 Statutory / Credit Patterns (Special handling)

**3.5 Statutory / Credit Patterns (Special handling)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NSSA, P35, PENSION CONTRIBUTION | NSSA contribution | Employee 4.5% on capped earnings -- see Section 6 |
| QPD, PROVISIONAL TAX, ITF12B | Provisional tax paid | Credit against final liability, not an expense |
| AIDS LEVY | Part of tax remittance | Not separately deductible |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Own-account movement |
| LOAN REPAYMENT, PRINCIPAL | EXCLUDE | Capital movement (interest may be deductible -- flag) |

### 3.6 Zimbabwean Banks -- Statement Format Reference

**3.6 Zimbabwean Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| CBZ Bank | TRANSFER, RTGS, ZIPIT, CHARGES | PDF/CSV; USD and ZWG accounts separate |
| Stanbic Bank | PAYMENT, TRF, FEE | PDF; merchant in narration |
| Steward Bank | ECOCASH, TRANSFER, CHARGE | Mobile-linked; many EcoCash entries |
| FBC Bank | RTGS, ZIPIT, DEBIT | PDF/CSV |
| Nedbank Zimbabwe | PAYMENT, TRANSFER, FEE | PDF |
| EcoCash (mobile money) | CASH IN/OUT, MERCHANT PAY, P2P | Statement export; high transaction volume |

- **Currency hygiene** — Never mix USD and ZWG figures in one computation. Each currency runs through its own PAYE table and is reported separately.

## Section 4 -- Worked Examples

### Example 1 -- USD Employee, mid-range salary

**Input line:**
`25/03/2025 ; CBZ CREDIT ; ACME ENGINEERING LTD ; SALARY MARCH ; +1,500.00 ; USD`

**Reasoning:**
USD-paid employee, monthly. USD monthly table, band 1,000.01-2,000 at 30%, deduct 85.
Income tax = (1,500 x 30%) - 85 = 450 - 85 = **USD 365.00**.
AIDS levy = 365.00 x 3% = USD 10.95.
Total tax = 365.00 + 10.95 = **USD 375.95**.

**Classification:** PAYE (USD table). Net pay before NSSA = 1,500 - 375.95 = USD 1,124.05.

### Example 2 -- USD Employee, higher salary

**Input line:**
`25/04/2025 ; STANBIC ; HORIZON MINING ; SALARY APRIL ; +2,500.00 ; USD`

**Reasoning:**
USD monthly table, band 2,000.01-3,000 at 35%, deduct 185.
Income tax = (2,500 x 35%) - 185 = 875 - 185 = **USD 690.00**.
AIDS levy = 690.00 x 3% = USD 20.70.
Total tax = **USD 710.70**.

**Classification:** PAYE (USD table). Total tax USD 710.70.

### Example 3 -- ZiG/ZWG Employee

**Input line:**
`25/05/2025 ; FBC ; SADZA RETAIL (PVT) LTD ; MUHOLO MAY ; +50,000.00 ; ZWG`

**Reasoning:**
ZWG-paid employee, monthly. ZWG monthly table, band 28,000.01-56,000 at 30%, deduct 2,380.
Income tax = (50,000 x 30%) - 2,380 = 15,000 - 2,380 = **ZWG 12,620.00**.
AIDS levy = 12,620.00 x 3% = ZWG 378.60.
Total tax = **ZWG 12,998.60**.

**Classification:** PAYE (ZWG table). Total tax ZWG 12,998.60. Do NOT convert to USD -- report in ZWG.

### Example 4 -- USD Employee below threshold

**Input line:**
`25/06/2025 ; STEWARD ; SMALL SHOP ; SALARY JUNE ; +90.00 ; USD`

**Reasoning:**
USD 90/month is below the USD 100 tax-free threshold (band 0-100, 0%).
Income tax = USD 0.00. AIDS levy on zero = USD 0.00.

**Classification:** PAYE (USD table). No tax. Full USD 90.00 retained (before NSSA).

### Example 5 -- Self-employed trader (flat 25%)

**Input (annual summary, USD):**
Gross trade income USD 40,000; allowable expenses USD 16,000.

**Reasoning:**
Individuals from trade and investment are taxed at the **flat 25% business rate** (Finance Act s.14(2b)), NOT the progressive PAYE table.
Taxable income = 40,000 - 16,000 = USD 24,000.
Income tax = 24,000 x 25% = **USD 6,000.00**.
AIDS levy = 6,000 x 3% = USD 180.00.
Total tax = **USD 6,180.00** (effective 25.75%).

**Classification:** ITF12C self-assessment; QPDs payable during the year (Section 5.5).

### Example 6 -- NSSA contribution on USD salary above ceiling

**Input line:**
`30/06/2025 ; CBZ DEBIT ; NSSA P35 ; PENSION JUNE ; -31.50 ; USD`

**Reasoning:**
Employee earns USD 1,000/month, but NSSA insurable earnings are capped at **USD 700/month**.
Total POBS contribution = 9% x 700 = USD 63.00, split equally.
Employee share = 4.5% x 700 = **USD 31.50**; employer share = USD 31.50.

**Classification:** NSSA POBS employee contribution USD 31.50. The USD 1,000 salary is still taxed under the USD PAYE table.

### Example 7 -- Bonus within exemption

**Input line:**
`20/12/2025 ; STANBIC ; ACME ENGINEERING LTD ; ANNUAL BONUS ; +700.00 ; USD`

**Reasoning:**
Tax-free bonus / performance-award exemption is USD 700 (ZIMRA PAYE page).
USD 700 bonus = fully within the exemption.
Taxable portion = USD 0.00. Any bonus ABOVE USD 700 is added to taxable earnings and taxed at the marginal PAYE rate.

**Classification:** Exempt up to USD 700. Flag any excess for inclusion.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Selecting the correct PAYE table

- **Selecting the correct PAYE table** — Use the table matching the currency of pay and the pay period (monthly/annual/fortnightly/weekly/daily). USD earnings → USD table; ZWG earnings → ZWG table. Mixed-currency earners have each stream taxed under its own table. Never convert one currency to the other to "combine" income.  _(Income Tax Act [Chapter 23:06]; ZIMRA 2025 PAYE tables)_

### 5.2 The "deduct" method

- **The deduct method** — tax = (taxable income x band rate) - deduct. This reproduces the cumulative progressive result without manual slicing. Always confirm the income falls in the stated band first.

### 5.3 AIDS Levy

- **AIDS Levy computation** — After computing income tax, add 3% of the income tax payable (not 3% of income). Applies to individuals and companies. If income tax is zero (below threshold), the AIDS levy is also zero.  _(ZIMRA 2025 PAYE tables; ZIMRA corporate tax rates)_

### 5.4 Bonus / performance-award exemption

- **Bonus exemption** — The first USD 700 (ZWG equivalent for ZiG earners) of an annual bonus / performance award is exempt. Only the excess is added to taxable earnings.  _(ZIMRA PAYE page)_

### 5.5 Trade and investment income (self-employed individuals)

- **Trade and investment income taxation** — Individuals carrying on a trade or profession are taxed at a flat 25% on net taxable income (gross business income minus allowable expenses), plus 3% AIDS levy → 25.75% effective. This is NOT the progressive PAYE table -- that table is for employment income only. Companies and trusts are taxed at the same 25% + 3% AIDS = 25.75% effective.  _(ZIMRA corporate/business tax rates (Finance Act s.14(2b)))_

### 5.6 Self-employed professionals -- moved to QPD from 1 Jan 2025

- **Self-employed professionals moved to QPD** — Effective 1 January 2025, self-employed professionals (architects, engineers, legal practitioners, health practitioners, real-estate agents, etc.) were removed from presumptive tax and placed on the Self-Assessment / QPD provisional-tax system. They file provisional returns (ITF12B) and pay QPDs on estimated taxable income at the 25% + AIDS-levy business rate. Non-professional informal traders may still fall under presumptive tax (Section 5.8).  _(Lucent (lucent.co.zw QPD guide); transition confirmed via multiple secondary sources)_

### 5.7 Provisional tax (QPDs)

**5.7 Provisional tax (QPDs)**  _(Lucent QPD guide; ZIMRA Public Notice 17 of 2025)_

| QPD | % of estimated annual tax | Return (ITF12B) due | Payment due |
| --- | --- | --- | --- |
| 1st (Q1) | 10% | 20 March | 25 March |
| 2nd (Q2) | 25% | 20 June | 25 June |
| 3rd (Q3) | 30% | 20 September | 25 September |
| 4th (Q4) | 35% | 15 December | 20 December |

- **QPD totals** — The four instalments sum to 100% of the estimated annual tax (10 + 25 + 30 + 35). The return is submitted ~5 days before each payment date.  _(Lucent QPD guide; ZIMRA Public Notice 17 of 2025)_

### 5.8 Presumptive tax (informal sector -- non-professionals)

- **Presumptive tax details** — Targets informal businesses with turnover generally below USD 60,000/year. Examples cited: restaurant/bottle-store operators USD 300/quarter; cottage-industry operators USD 300/quarter. Cross-border traders: presumptive tax = 10% of the Value for Duty Purposes (VDP) of commercial goods imported. A 2026 budget proposal referenced a 5%-of-turnover "other trades" rate -- not confirmed as enacted for 2025 `[RESEARCH GAP -- reviewer to confirm]`.  _(ZIMRA presumptive-tax notices; figures from research summaries -- `[RESEARCH GAP -- reviewer to confirm the full current schedule against the latest ZIMRA presumptive-tax public notice]`)_

### 5.9 The wholly-and-exclusively test (deductions)

- **Wholly-and-exclusively test** — For traders, an expense is deductible only if incurred wholly and exclusively in the production of income. Mixed-use expenses must be apportioned on a reasonable, documented basis. Personal expenses, drawings, fines, and the tax itself are never deductible.  _(Income Tax Act [Chapter 23:06])_

### 5.10 Final Deduction System (FDS)

- **Final Deduction System (FDS)** — For pure-employment individuals, PAYE is generally a final tax -- most employees do NOT file an annual return. Individuals with non-employment income (trade, multiple employers, investment income) must file the relevant return (ITF1 / ITF12C).  _(PwC Worldwide Tax Summaries (Zimbabwe individual))_

## Section 6 -- NSSA Social Security and Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 NSSA -- Pension and Other Benefits Scheme (POBS)

**6.1 NSSA -- Pension and Other Benefits Scheme (POBS)**  _(NSSA contributions/schemes pages; M&J Consultants 2025 NSSA summary)_

| Component | Rate | On |
| --- | --- | --- |
| Employee | 4.5% | Insurable earnings (capped) |
| Employer | 4.5% | Insurable earnings (capped) |
| **Total POBS** | **9.0%** | Insurable earnings (capped) |

- **POBS totals and ceiling** — The employee and employer columns (4.5% + 4.5%) sum to the 9.0% total. Insurable earnings ceiling: USD 700/month (introduced 2024, in force 2025). Contributions are computed only on earnings up to USD 700. ZWG-paid employees contribute on the ZWG equivalent of USD 700. Worked check: an employee earning USD 1,000 contributes on USD 700 → 9% = USD 63/month total (USD 31.50 each). (See Example 6.) Minimum / floor: `[RESEARCH GAP -- reviewer to confirm]` No explicit statutory minimum floor was confirmed from authoritative sources; verify directly with NSSA if a floor figure is needed.  _(NSSA contributions/schemes pages; M&J Consultants 2025 NSSA summary)_

### 6.2 NSSA -- Accident Prevention and Workers' Compensation Scheme (APWCS)

- **APWCS details** — Employer-only contribution (employees pay nothing). Rate varies by industry risk class -- no single statutory rate. Low-risk sectors (retail, finance, education) roughly 0.5-1% of the wage bill; high-risk (mining, construction) materially higher. `[RESEARCH GAP -- reviewer to confirm]` Exact per-industry class rates must be obtained from NSSA for the specific industry. Do not publish a single APWCS percentage.  _(NSSA schemes page; secondary summaries)_

### 6.3 Home-based business apportionment

- **Home-based business apportionment** — Apportion electricity (ZESA/ZETDC), water, internet, and rent to the business-use percentage. Conservative default: 0% until the reviewer confirms a documented basis (dedicated workspace, floor-area or usage measure).

### 6.4 Vehicle business use

- **Vehicle business use** — Only the business-use percentage of fuel, insurance, and maintenance is deductible; requires a mileage basis. Conservative default: 0% until a mileage log is provided.

### 6.5 Phone / data mixed use

- **Phone / data mixed use** — Business-use portion only (Econet/NetOne/TelOne/Liquid). Conservative default: 0% until the business percentage is confirmed.

### 6.6 IMTT (Intermediated Money Transfer Tax) deductibility

- **IMTT deductibility** — IMTT is levied on electronic transfers. Whether it is deductible against trade income depends on the nature of the transfer. Flag for reviewer to confirm deductibility before including.

### 6.7 Elderly / disability credits

- **Elderly / disability credits** — Age-55+ credit and blind/disabled credit are USD 900/year each (or ZWG equivalent) (ZIMRA concessions). Flag for reviewer to confirm eligibility (age, certified disability) before applying. Default: no credit.  _(ZIMRA concessions)_

### 6.8 ZWG band revisions

- **ZWG band revisions** — ZWG bands may be revised mid-year by ZIMRA public notice owing to devaluation. Flag for reviewer to confirm the ZWG table in force for the period being computed.

## Section 7 -- Excel Working Paper Template

```
ZIMBABWE INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Currency of earnings: USD / ZWG / BOTH
Status: Employee (PAYE/FDS) / Sole trader / Professional (QPD)

A. EMPLOYMENT INCOME -- PAYE (per currency, per period)
  A1. Currency .................................. USD / ZWG
  A2. Pay period ................................ Monthly / Annual / ...
  A3. Gross earnings ............................ ___________
  A4. Less: bonus exemption (max USD 700) ....... ___________
  A5. Taxable earnings (A3 - A4) ................ ___________
  A6. PAYE band rate ............................ ___________
  A7. "Deduct" figure ........................... ___________
  A8. Income tax = (A5 x A6) - A7 ............... ___________
  A9. AIDS levy = A8 x 3% ....................... ___________
  A10. Total PAYE (A8 + A9) ..................... ___________

B. TRADE / PROFESSIONAL INCOME (flat 25%)
  B1. Gross business income ..................... ___________
  B2. Less: allowable expenses (w&e test) ....... ___________
  B3. Taxable trade income (B1 - B2) ............ ___________
  B4. Income tax = B3 x 25% ..................... ___________
  B5. AIDS levy = B4 x 3% ....................... ___________
  B6. Total trade tax (B4 + B5) ................. ___________

C. NSSA (POBS)
  C1. Insurable earnings (capped at USD 700/mo) . ___________
  C2. Employee 4.5% ............................. ___________
  C3. Employer 4.5% ............................. ___________

D. PROVISIONAL TAX (QPDs) -- traders/professionals
  D1. Estimated annual tax ...................... ___________
  D2. Q1 (10%) / Q2 (25%) / Q3 (30%) / Q4 (35%) . ___________
  D3. QPDs paid to date ......................... ___________

E. FINAL POSITION
  E1. Total tax (A10 + B6) ...................... ___________
  E2. Less: QPDs / PAYE already paid ............ ___________
  E3. Less: confirmed credits (elderly/disability) ___________
  E4. Tax due / (refund) (E1 - E2 - E3) ......... ___________

REVIEWER FLAGS:
  [ ] Currency of earnings confirmed?
  [ ] Correct USD vs ZWG table used (and ZWG table in force)?
  [ ] Employment vs trade income correctly split?
  [ ] AIDS levy applied to TAX, not income?
  [ ] Bonus exemption capped at USD 700?
  [ ] NSSA capped at USD 700/month insurable earnings?
  [ ] Elderly/disability credit eligibility confirmed?
  [ ] All Tier 2 apportionments documented?
  [ ] Entertainment / personal / fines excluded?
```

## Section 8 -- Bank Statement Reading Guide

### Zimbabwean Bank Statement Formats

**Zimbabwean Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| CBZ Bank | PDF, CSV | Date, Narration, Debit, Credit, Balance | Separate USD and ZWG accounts |
| Stanbic Bank | PDF, CSV | Value Date, Description, Amount, Balance | Merchant in narration |
| Steward Bank | PDF, CSV | Date, Description, Amount, Balance | Many EcoCash-linked entries |
| FBC Bank | PDF, CSV | Date, Particulars, Debit, Credit | RTGS/ZIPIT references |
| EcoCash | CSV / app export | Date, Type, Counterparty, Amount | High volume; cash-in/out + merchant pay |

### Key Terms (English / Shona / Ndebele)

**Key Terms (English / Shona / Ndebele)**

| Term | Meaning | Classification Hint |
| --- | --- | --- |
| MUHOLO | Salary/wages (Shona) | Employment income -- PAYE |
| HOLO / UMHOLO | Wages (Ndebele) | Employment income -- PAYE |
| RTGS | Real-Time Gross Settlement transfer | Check direction for income/expense |
| ZIPIT | Bank-to-bank instant transfer | Check direction |
| ECOCASH / ONEMONEY / INNBUCKS | Mobile money | Check direction; common for trade receipts |
| IMTT | Intermediated Money Transfer Tax | Transfer tax -- reviewer to confirm deductibility |
| P35 / NSSA | Pension contribution | NSSA POBS -- capped at USD 700 insurable |
| QPD | Quarterly Payment Date (provisional tax) | Credit against liability, not expense |
| VDP | Value for Duty Purposes | Used for cross-border presumptive tax |
| KIRINGO / RENT | Rent | Rental income/expense -- flag |

> **Currency column is critical.** Every line must be tagged USD or ZWG and routed through the correct table. Never net USD and ZWG against each other.

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3), tagging each as USD or ZWG.
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ZIMBABWE INCOME TAX
1. In which currency are you paid -- USD, ZiG/ZWG, or both?
2. Are you an employee (PAYE), a sole trader, or a self-employed professional?
3. What is your pay period -- monthly, weekly, fortnightly, daily?
4. Did you receive a bonus this year? If so, how much (the first USD 700 is exempt)?
5. Are you aged 55 or over, or do you have a certified disability (USD 900/yr credit)?
6. What are your NSSA (P35) contributions for the year?
7. If a trader: do you have invoices/receipts supporting your expenses?
8. Are any expenses mixed business/personal (vehicle, phone, home)? What % is business?
9. Have you paid any provisional tax (QPDs) this year? How much?
10. Are you VAT-registered (turnover over USD 25,000)?
```

## Section 10 -- Reference Material

### Key References

**Key References**

| Topic | Reference |
| --- | --- |
| Income tax framework | Income Tax Act [Chapter 23:06]; annual Finance Act |
| USD PAYE table 2025 | ZIMRA USD Jan-Dec 2025 PAYE table (download 4211) |
| ZWG PAYE table 2025 | ZIMRA ZWG 2025 PAYE table (download 4205) |
| AIDS levy (3% of tax) | ZIMRA 2025 PAYE tables; ZIMRA corporate tax rates |
| Trade/business flat 25% | Finance Act s.14(2b); ZIMRA corporate/business tax rates |
| Provisional tax (QPDs) | ZIMRA Public Notice 17 of 2025; Lucent QPD guide |
| Annual filing deadline (30 Apr) | ZIMRA Public Notice 20 of 2026 (via fingaz.co.zw, 2026-04-18) |
| Forms ITF1 / ITF12C / ITF12B | ZIMRA filing guidance; PN 23 of 2025 (ITF12C) |
| Elderly / disability credits | ZIMRA elderly-concession page |
| VAT registration threshold | ZIMRA VAT registration page |
| NSSA POBS / APWCS | NSSA contributions & schemes pages; M&J 2025 summary |
| FDS (PAYE as final tax) | PwC Worldwide Tax Summaries -- Zimbabwe individual |

### Filing forms and deadlines

**Filing forms and deadlines**

| Item | Detail | Source |
| --- | --- | --- |
| ITF1 | Individual return (non-FDS / multiple-source income) | ZIMRA |
| ITF12C | Self-assessment return (traders / investors) | ZIMRA PN 23 of 2025 |
| ITF12B | Provisional (QPD) return | ZIMRA |
| Annual income-tax return deadline | 30 April following the tax year (year ended 31 Dec 2025 → 30 Apr 2026) | ZIMRA PN 20 of 2026 |
| PAYE remittance | By the 10th of the following month | ZIMRA |

### Penalties and interest

**Penalties and interest**

| Item | Detail | Source |
| --- | --- | --- |
| Late / non-filing of returns | Penalty up to 100% of tax due, plus interest | ZIMRA tax-payment-dates page; ZIMRA FAQs |
| Late payment interest | "Prescribed rate" (compounding) -- exact 2025 % `[RESEARCH GAP -- reviewer to confirm against the current ZIMRA prescribed-rate notice]` | ZIMRA |
| Continued non-compliance | May lead to prosecution | ZIMRA |

### Registration and VAT

**Registration and VAT**

| Item | Detail | Source |
| --- | --- | --- |
| Income-tax registration | Register with ZIMRA via TaRMS; obtain BP number; no de-minimis income threshold | ZIMRA |
| VAT compulsory registration | USD 25,000 (or ZWG equivalent) taxable supplies / rolling 12 months | ZIMRA VAT registration page |
| VAT fiscalisation | All VAT-registered taxpayers (incl. below threshold) must comply -- ZIMRA PN 30 of 2025, eff. 1 Jun 2025 | ZIMRA PN 30 of 2025 |

### Minimum wage (context, not a tax figure)

**Minimum wage (context, not a tax figure)**

| Item | Detail | Source |
| --- | --- | --- |
| National minimum wage | USD 150/month (SI 186 of 2024) -- does not cover all sectors | WageIndicator; SI 186 of 2024 |
| Mining (NEC) | Grade 1 from USD 124.05/mo, rising to USD 266.14/mo by Jul 2025 | NEC schedules |
| Agriculture (NEC) | Grade A1 USD 80/mo; Grade C2 USD 159/mo (Jun 2025) | NEC schedules |

> No single uniform national minimum wage applies across all industries -- most rates are set by sector-specific National Employment Council (NEC) agreements.

### Test Suite

Input: USD, monthly salary USD 1,500.
Expected: income tax = (1,500 x 30%) - 85 = USD 365.00; AIDS levy = USD 10.95; total PAYE = **USD 375.95**.

Input: USD, monthly salary USD 2,500.
Expected: income tax = (2,500 x 35%) - 185 = USD 690.00; AIDS levy = USD 20.70; total PAYE = **USD 710.70**.

Input: ZWG, monthly salary ZWG 50,000.
Expected: income tax = (50,000 x 30%) - 2,380 = ZWG 12,620.00; AIDS levy = ZWG 378.60; total PAYE = **ZWG 12,998.60**.

Input: USD, monthly salary USD 90.
Expected: income tax = USD 0.00; AIDS levy = USD 0.00; total PAYE = **USD 0.00**.

Input: USD, gross trade income USD 40,000, allowable expenses USD 16,000.
Expected: taxable = USD 24,000; income tax = 24,000 x 25% = USD 6,000.00; AIDS levy = USD 180.00; total = **USD 6,180.00**.

Input: USD salary USD 1,000/month.
Expected: insurable earnings capped at USD 700; employee 4.5% = **USD 31.50**; employer 4.5% = USD 31.50; total POBS = USD 63.00.

Input: USD annual bonus USD 700.
Expected: fully exempt; taxable bonus = **USD 0.00**. Excess over USD 700 taxed at the marginal PAYE rate.

Input: USD, monthly salary USD 4,000.
Expected: income tax = (4,000 x 40%) - 335 = 1,600 - 335 = USD 1,265.00; AIDS levy = USD 37.95; total PAYE = **USD 1,302.95**.

## PROHIBITIONS

- NEVER select a PAYE table without confirming the currency of earnings (USD vs ZWG)
- NEVER mix or net USD and ZWG figures in a single computation
- NEVER apply the progressive PAYE table to trade/professional income -- that is the flat 25% rate
- NEVER compute the AIDS levy on income -- it is 3% of the income tax payable
- NEVER apply the bonus exemption above USD 700 (or ZWG equivalent)
- NEVER compute NSSA on earnings above the USD 700 monthly insurable ceiling
- NEVER apply elderly or disability credits without confirming eligibility
- NEVER treat QPD provisional tax or income tax paid as a deductible expense
- NEVER allow entertainment, personal expenses, drawings, or fines as deductions
- NEVER publish a specific APWCS rate or late-payment interest rate without confirming the current NSSA/ZIMRA notice
- NEVER present tax calculations as definitive -- always label as estimated, pending professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
