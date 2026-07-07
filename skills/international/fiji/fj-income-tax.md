---
name: fiji-income-tax
description: Use this skill whenever asked about Fiji income tax for self-employed individuals, sole traders, and wage earners. Trigger on phrases like "how much tax do I pay in Fiji", "FRCS income tax return", "PIT return", "Personal Income Tax Return for Business Individual", "self-employed tax Fiji", "provisional tax", "SRT", "Social Responsibility Tax", "ECAL", "FNPF contribution", "chargeable income", "tax-free threshold", "allowable deductions", "VAT registration Fiji", or any question about filing or computing income tax for an individual or sole trader in Fiji. Also trigger when preparing or reviewing a Fiji PIT return, computing deductible business expenses, or advising on provisional tax, FNPF, or the FJD 30,000 tax-free threshold. This skill covers resident and non-resident rates, SRT, ECAL, FNPF, the business-individual return, provisional tax, penalties, and interaction with VAT and FNPF. ALWAYS read this skill before touching any Fiji income tax work.
jurisdiction: FJ
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# fiji-income-tax

## Fiji Income Tax -- Self-Employed Skill v0.1

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Fiji (Republic of Fiji) |
| Tax | Personal Income Tax (PIT) + Social Responsibility Tax (SRT) + Environment & Climate Adaptation Levy (ECAL) |
| Currency | Fijian Dollar (FJD / $) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Residency test | Domicile in Fiji, OR present 183+ days in any 12-month period |
| Resident basis | Worldwide income |
| Non-resident basis | Fiji-sourced income only |
| Primary legislation | Income Tax Act 2015; Tax Administration Act 2009 |
| Tax authority | Fiji Revenue & Customs Service (FRCS) |
| Filing portal | Taxpayer Online Service (TPOS) |
| Filing deadline | 31 March of the following year (3 months after year end) [statutory default; FRCS has extended in specific years] |
| Validated by | Pending — requires sign-off by a Fiji-licensed tax practitioner / accountant |
| Validation date | Pending |
| Skill version | 0.1 |

### Resident Individual Income Tax Bands (Year of Assessment 2022 Onwards — current for 2025)

**Resident Individual Income Tax Bands**  _(Source: FRCS Tax Rates page (table header "Year of Assessment 2022 Onwards") — https://frcs.org.fj/tax-rates-and-codes/ ; FRCS Personal Income Tax page — https://frcs.org.fj/our-services/taxation/individuals/personal-income-tax/)_

| Chargeable income (FJD) | Income tax | Cumulative tax at top |
| --- | --- | --- |
| 0 -- 30,000 | Nil (tax-free threshold) | $0 |
| 30,001 -- 50,000 | 18% of excess over 30,000 | $3,600 |
| 50,001 -- 270,000 | 3,600 + 20% of excess over 50,000 | $47,600 |
| 270,001 -- 300,000 | 47,600 + 20% of excess over 270,000 | $53,600 |
| 300,001 -- 350,000 | 53,600 + 20% of excess over 300,000 | $63,600 |
| 350,001 -- 400,000 | 63,600 + 20% of excess over 350,000 | $73,600 |
| 400,001 -- 450,000 | 73,600 + 20% of excess over 400,000 | $83,600 |
| 450,001 -- 500,000 | 83,600 + 20% of excess over 450,000 | $93,600 |
| 500,001 -- 1,000,000 | 93,600 + 20% of excess over 500,000 | $193,600 |
| 1,000,001+ | 193,600 + 20% of excess over 1,000,000 | -- |

- **Effective marginal rate** — Effective marginal income-tax rate is a flat 20% on all chargeable income above $50,000. SRT and ECAL (below) add further tax above $270,000.  _(FRCS Tax Rates page — https://frcs.org.fj/tax-rates-and-codes/)_

### Social Responsibility Tax (SRT) — additional tax on chargeable income above FJD 270,000

SRT applies ONLY to the portion of chargeable income exceeding $270,000.

**SRT table**  _(Source: FRCS Tax Rates page (SRT column) — https://frcs.org.fj/tax-rates-and-codes/ ; FRCS SRT overview — https://frcs.org.fj/our-services/taxation/individuals/social-responsibility-tax-srt/)_

| Chargeable income (FJD) | SRT | Cumulative SRT at top |
| --- | --- | --- |
| 270,001 -- 300,000 | 18% of excess over 270,000 | $5,400 |
| 300,001 -- 350,000 | 5,400 + 19% of excess over 300,000 | $14,900 |
| 350,001 -- 400,000 | 14,900 + 20% of excess over 350,000 | $24,900 |
| 400,001 -- 450,000 | 24,900 + 21% of excess over 400,000 | $35,400 |
| 450,001 -- 500,000 | 35,400 + 22% of excess over 450,000 | $46,400 |
| 500,001 -- 1,000,000 | 46,400 + 23% of excess over 500,000 | $161,400 |
| 1,000,001+ | 161,400 + 24% of excess over 1,000,000 | -- |

[RESEARCH GAP — reviewer to confirm] First SRT band (270,001–300,000): FRCS current tax-rates summary shows 18%, while a superseded FRCS 2020/2021 PAYE PDF showed 13% for that band (the 2024 budget restructured SRT). The 18% figure from the current FRCS tax-rates page is treated as authoritative for 2025 here; confirm against the live FRCS PAYE/SRT/ECAL table before publishing/filing.

### Environment & Climate Adaptation Levy (ECAL) on income

- **ECAL on personal income** — flat 5% of chargeable income exceeding $270,000 (reduced from 10% to 5%). Applies above the $270,000 threshold across all higher bands.  _(Source: FRCS 2020/2021 PAYE PDF (each ECAL row "5% of excess over 270,000") — https://www.frcs.org.fj/wp-content/uploads/2020/10/2020-2021-PAYE-Final-Tax.pdf ; reduction 10%→5% confirmed via FRCS SRT page — https://frcs.org.fj/our-services/taxation/individuals/social-responsibility-tax-srt/)_

Note: ECAL also applies separately as a 5% levy on prescribed services (a consumption levy distinct from the income levy) — out of scope for this personal income tax skill.

### Non-Resident Individuals

- **Non-resident flat rate** — Flat 20% on Fiji-sourced chargeable income from the first dollar — no tax-free threshold.  _(Source: FRCS Personal Income Tax page — https://frcs.org.fj/our-services/taxation/individuals/personal-income-tax/)_

### FNPF — Fiji National Provident Fund (mandatory social security / pension)

Compulsory contribution on gross wages, effective 1 January 2024 (reverted from pandemic-era reduced rate):

**FNPF rates**  _(Source: FNPF Employers page — https://myfnpf.com.fj/employers/ ; FBC News (18% restoration) — https://www.fbcnews.com.fj/news/fnpf-18-contribution-restored-civil-service-pay-review/)_

| Party | Rate of gross wages |
| --- | --- |
| Employee | 8% |
| Employer | 10% |
| **Total** | **18%** |

Component check: 8% (employee) + 10% (employer) = 18% total ✓. Contributions calculated on gross earnings, payable monthly.

- **Compulsory contribution wage ceiling** — [RESEARCH GAP — reviewer to confirm] — no compulsory cap was confirmed on FNPF's official site; state as none/unconfirmed rather than assuming one.
- **Voluntary / additional contribution cap** — FJD 250,000 per financial year, effective 1 February 2025 (gazetted 31 Jan 2025)  _(FNPF — https://myfnpf.com.fj/2025/02/19/fnpf-reverts-to-old-voluntary-and-additional-contribution-limit/)_
- **FNPF employee contribution deductibility** — Employee FNPF contributions are deductible when computing taxable income. [RESEARCH GAP — reviewer to confirm] deductibility limits/conditions against current FRCS individual guidance.

### Other Headline Rates (context)

**Other Headline Rates**

| Tax | Rate | Source |
| --- | --- | --- |
| Corporate income tax | 25% | https://frcs.org.fj/tax-rates-and-codes/ |
| Capital Gains Tax | 10% | https://frcs.org.fj/tax-rates-and-codes/ |
| Fringe Benefit Tax | 20% | https://frcs.org.fj/tax-rates-and-codes/ |
| VAT (standard) | 15% (from 1 Aug 2024) | https://frcs.org.fj/tax-rates-and-codes/ |
| VAT registration threshold | Turnover > FJD 100,000 | FRCS VAT Guide — https://www.frcs.org.fj/wp-content/uploads/2023/11/VAT-Guide-01.11.2-Online-version.pdf |
| National minimum wage | FJD 5.00/hr (from 1 Apr 2025) | Fiji Govt — https://www.fiji.gov.fj/Media-Centre/News/ |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP — do not apply a rate table without confirming resident vs non-resident |
| Unknown whether income exceeds $270,000 | Assume below until confirmed; apply SRT/ECAL only when confirmed above |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration | Not registered (turnover under $100,000) |
| Unknown asset useful life / depreciation rate | Flag for reviewer; do not guess a rate |
| Unknown whether expense is entertainment/personal | Treat as not deductible |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of residency status (resident/non-resident) and taxpayer type (sole trader / business individual, or wage earner).

Recommended -- all sales invoices, purchase invoices/receipts, FNPF contribution records, prior year PIT return or FRCS assessment, VAT registration status, TIN.

Ideal -- complete income and expenditure account, asset/depreciation register, provisional tax payment confirmations, employment income details (for combined employment + business income, PIT class "B").

Refusal if minimum is missing -- SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This Fiji PIT computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and meet the wholly-and-exclusively test under the Income Tax Act 2015."

### Refusal Catalogue

- **R-FJ-1** — Residency status unknown. "Residency determines whether the tax-free threshold and progressive bands apply (resident) or a flat 20% from the first dollar applies (non-resident). This skill cannot compute tax without confirming residency. Please confirm before proceeding."
- **R-FJ-2** — Companies / partnerships. "This skill covers individuals and sole traders only. Companies (25% CIT) and partnerships file separate returns. Escalate to a Fiji-licensed practitioner."
- **R-FJ-3** — High earners above FJD 270,000. "Chargeable income above $270,000 triggers SRT and ECAL in addition to income tax, and the first SRT band rate is currently unconfirmed in this skill. Flag for reviewer before computing — do not finalise SRT/ECAL without confirming the live FRCS table."
- **R-FJ-4** — Capital gains / asset disposals. "Capital Gains Tax (10%) computations require specialised analysis. Out of scope. Escalate to a Fiji-licensed practitioner."
- **R-FJ-5** — Arrears / enforcement. "Client has outstanding tax arrears or is subject to FRCS debt management action. Late-payment penalty (25%) plus 5% per month interest is severe. Do not advise. Escalate to a Fiji-licensed practitioner immediately."
- **R-FJ-6** — VAT return requested. "This skill covers income tax (PIT/SRT/ECAL) only. Fiji VAT (15%, threshold FJD 100,000) is a separate workflow."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns**

| Pattern | PIT Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Gross business income | Business income | If VAT-registered, extract net (excl. 15% VAT) |
| FEES, PROFESSIONAL FEES, CONSULTANCY | Gross business income | Business income | Typical for self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Gross business income | Business income | Platform payout — match to invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Gross business income | Business income | Platform payout — verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Gross business income | Business income | International platform payout |
| UPWORK, FIVERR, TOPTAL | Gross business income | Business income | Freelance platform — net of commission |
| SALARY, WAGES, PAY, EMPLOYER [name] | Employment income | Employment income | NOT self-employment; combined-income return (PIT "B") |
| RENT RECEIVED, RENTAL | Other income | Rental income | Not self-employment income |
| INTEREST, INTEREST RECEIVED | Other income | Investment income | Interest income |
| DIVIDEND, DIVIDENDS | Other income | Investment income | Dividend income |
| FRCS REFUND, TAX REFUND | EXCLUDE | Not income | Tax refund from prior year |
| GOVERNMENT GRANT, GOVT ASSISTANCE | EXCLUDE unless revenue grant | Check nature | Capital grants EXCLUDE; revenue grants = business income |

### 3.2 Expense Patterns (Debits) -- Fully Deductible

**Fully Deductible Expense Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, RENT [commercial address] | Office rent | Deductible | Dedicated business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible |  |
| ACCOUNTANT, AUDITOR, BOOKKEEP, CA FEES | Accountancy fees | Deductible |  |
| LAWYER, LEGAL, SOLICITOR (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | Deductible |  |
| TRAINING, CPD, COURSE, SEMINAR, CONFERENCE | Training | Deductible | Must relate to current business |
| BANK FEE, SERVICE FEE, MAINTENANCE FEE | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Deductible | Small recurring spend = expense; large purchases = capital |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software Expense Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| Perpetual software licence (high value) | Capital item | Capitalise / depreciate | Flag depreciation rate for reviewer |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities Expense Patterns**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| EFL, ENERGY FIJI, FIJI ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| WATER AUTHORITY, WAF | Water | T2 if home office | Business portion only |
| VODAFONE, DIGICEL, TELECOM FIJI, BROADBAND | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel Expense Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| FIJI AIRWAYS, AIR FIJI, FLIGHT | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, RESORT, AIRBNB | Accommodation | Deductible if business travel |  |
| TAXI, BUS, FERRY | Local transport | Deductible if business purpose |  |
| FUEL, PETROL, DIESEL, TOTAL, MOBIL | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARKING | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**Not Deductible Expense Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINNER, LUNCH, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private/entertainment — flag for reviewer |
| GROCERIES, SUPERMARKET, MH, NEW WORLD, RB PATEL | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, INFRINGEMENT | Fines/penalties | NOT deductible | Public policy |
| FRCS PAYMENT, INCOME TAX, TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (Depreciation)

**Capital Items Expense Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | Capitalise & depreciate | **[RESEARCH GAP — confirm FRCS depreciation rate]** |
| PRINTER, SCANNER, COPIER | Office equipment | Capitalise & depreciate | **[RESEARCH GAP — confirm rate]** |
| FURNITURE, DESK, CHAIR | Furniture/fittings | Capitalise & depreciate | **[RESEARCH GAP — confirm rate]** |
| VEHICLE, CAR (business) | Motor vehicle | Capitalise & depreciate, business % only | **[RESEARCH GAP — confirm rate]** |

Note: Fiji depreciation/wear-and-tear rates under the Income Tax Act 2015 were not extracted in research. Do NOT guess depreciation rates — flag every capital item for the reviewer to apply the correct FRCS rate.

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, LOAN PRINCIPAL | EXCLUDE | Loan principal movement |
| FNPF, PROVIDENT FUND CONTRIBUTION | FNPF deduction | Deductible separately (employee portion), NOT a business expense line |
| VAT PAYMENT, FRCS VAT | EXCLUDE | VAT liability payment, not expense |
| PROVISIONAL TAX, PT INSTALMENT | Provisional tax paid | Credit against liability — not an expense |

### 3.9 Fijian Banks -- Statement Format Reference

**Fijian Banks Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| ANZ Fiji | TRANSFER, DD, EFTPOS, FEE | PDF/CSV; date format DD/MM/YYYY |
| BSP (Bank South Pacific) Fiji | PAYMENT, TFR, DIRECT DEBIT, CHARGE | PDF/CSV; counterparty in description |
| Westpac Fiji | TRANSFER, DEBIT, CARD, FEE | PDF; merchant in description |
| HFC Bank | TRANSFER, DEPOSIT, WITHDRAWAL | PDF; shorter descriptions |
| Bred Bank Fiji | PAYMENT, TRANSFER, FEE | PDF/CSV |

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (VAT-registered)

Input line:
`15/03/2025 ; BSP TRANSFER IN ; PACIFIC TRADING LTD ; PAYMENT INV-2025-003 ; +1,150.00 ; FJD`

Reasoning:
Client payment for services. The sole trader is VAT-registered (turnover > $100,000), so $1,150 includes 15% VAT. Net business income = 1,150 / 1.15 = $1,000.00. VAT of $150 is collected on behalf of FRCS (excluded from income — it is a liability).

Classification: Business income = $1,000.00. VAT $150.00 excluded.

### Example 2 -- SaaS Subscription (Fully Deductible)

Input line:
`01/04/2025 ; ANZ DD ; ADOBE SYSTEMS ; CREATIVE CLOUD APR ; -69.00 ; FJD`

Reasoning:
Monthly SaaS subscription, recurring, business use. Fully deductible operating expense. If VAT-registered, claim net of recoverable input VAT.

Classification: Deductible business expense = $69.00 (or net if VAT-registered with recoverable input VAT).

### Example 3 -- Entertainment (Flagged, Not Deductible)

Input line:
`22/04/2025 ; WESTPAC CARD ; OCEAN TERRACE RESTAURANT ; CLIENT DINNER ; -180.00 ; FJD`

Reasoning:
Client entertainment / meal. Treated as not deductible under the conservative default; entertainment is private in nature. No deduction without explicit reviewer confirmation.

Classification: NOT deductible. Exclude from expenses.

### Example 4 -- FNPF Employee Contribution

Input line:
`10/01/2025 ; BSP DD ; FNPF CONTRIBUTION ; DEC 2024 ; -240.00 ; FJD`

Reasoning:
Fiji National Provident Fund employee contribution (8% of gross wages). Deductible from taxable income as an FNPF deduction, NOT as a business expense line. (On $3,000 gross monthly wage, 8% employee share = $240.00.)

Classification: FNPF deduction = $240.00. Not a business expense.

### Example 5 -- Resident Sole Trader, Tax-Free Threshold

Input: Resident sole trader. Net business profit (chargeable income) = $25,000.

Reasoning:
$25,000 is below the $30,000 tax-free threshold, so income tax = Nil. No SRT or ECAL (income well below $270,000). FNPF/VAT separate.

Classification: Income tax due = $0.00 (within tax-free threshold).

### Example 6 -- Resident Sole Trader, Mid-Range

Input: Resident sole trader. Chargeable income = $80,000.

Reasoning:
$80,000 falls in the 50,001–270,000 band. Tax = 3,600 + 20% × (80,000 − 50,000) = 3,600 + 20% × 30,000 = 3,600 + 6,000 = $9,600. No SRT/ECAL (below $270,000).

Classification: Income tax = $9,600.00.

### Example 7 -- Non-Resident Individual

Input: Non-resident. Fiji-sourced chargeable income = $40,000.

Reasoning:
Non-residents pay a flat 20% from the first dollar, no tax-free threshold. Tax = 20% × 40,000 = $8,000.00.

Classification: Income tax = $8,000.00.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The Wholly and Exclusively Test

- **Wholly and Exclusively Test** — An expense is deductible only if incurred in the production of assessable income. Mixed-use expenses must be apportioned on a reasonable, documented basis. Private and domestic expenditure is not deductible.  _(Income Tax Act 2015)_

### 5.2 Revenue Recognition

- **Revenue Recognition** — All business income is assessable. For VAT-registered sole traders, report income net of the 15% VAT collected. VAT collected on sales is NOT income — it is a liability to FRCS.  _(Source: FRCS VAT page — https://frcs.org.fj/our-services/taxation/value-added-tax-vat/)_

### 5.3 Resident vs Non-Resident

**Resident vs Non-Resident**  _(Source: FRCS Personal Income Tax page — https://frcs.org.fj/our-services/taxation/individuals/personal-income-tax/)_

| Status | Basis | Threshold | Rate |
| --- | --- | --- | --- |
| Resident | Worldwide income | $30,000 tax-free | Progressive (see Section 1) |
| Non-resident | Fiji-sourced only | None | Flat 20% from first dollar |

### 5.4 Capital vs Revenue

- **Capital vs Revenue** — Capital items (equipment, vehicles, furniture) are not deducted in full in the year of purchase — they are depreciated. [RESEARCH GAP — reviewer to confirm depreciation/wear-and-tear rates from the Income Tax Act 2015 / FRCS guidance.] Do not apply a depreciation rate without confirmation.

### 5.5 FNPF Deduction

- **FNPF Deduction** — Employee FNPF contributions (8% of gross wages) are deductible when computing taxable income. [RESEARCH GAP — reviewer to confirm any caps/conditions.] Employer contributions (10%) are a cost of employing staff, not a personal deduction.  _(Source: FNPF Employers page — https://myfnpf.com.fj/employers/)_

### 5.6 Non-Deductible Expenses

**Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Entertainment / private meals | Private in nature (conservative default) |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Capital expenditure | Depreciated, not expensed |
| Drawings / personal withdrawals | Not an expense |

### 5.7 SRT and ECAL (Income above FJD 270,000)

**SRT and ECAL**  _(Source: FRCS SRT page — https://frcs.org.fj/our-services/taxation/individuals/social-responsibility-tax-srt/)_

| Tax | Applies to | Computation |
| --- | --- | --- |
| SRT | Chargeable income > $270,000 | See SRT table, Section 1 (first band rate flagged as RESEARCH GAP) |
| ECAL | Chargeable income > $270,000 | Flat 5% of excess over $270,000 |

- **SRT/ECAL additional and flag** — These are ADDITIONAL to income tax. Flag any client with chargeable income above $270,000 for the reviewer (R-FJ-3).  _(Source: FRCS SRT page — https://frcs.org.fj/our-services/taxation/individuals/social-responsibility-tax-srt/)_

### 5.8 VAT Interaction

**VAT Interaction**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (registered) | NOT income — exclude (net reporting) |
| Input VAT recovered (registered) | NOT an expense — exclude |
| Not VAT-registered (turnover ≤ $100,000) | Gross amounts are income/expense; no VAT split |

- **VAT registration mandatory threshold** — VAT registration is mandatory once annual gross turnover exceeds FJD 100,000 (register within 21 days). VAT standard rate is 15% (from 1 Aug 2024).  _(Source: FRCS VAT Guide — https://www.frcs.org.fj/wp-content/uploads/2023/11/VAT-Guide-01.11.2-Online-version.pdf)_

### 5.9 Provisional Tax

- **Provisional Tax** — Business/self-employed taxpayers are subject to provisional tax (advance instalments toward the year's liability).  _(Source: FRCS Provisional Tax page — https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/provisional-tax/)_

[RESEARCH GAP — reviewer to confirm] exact provisional-tax instalment percentages and due dates from the FRCS Provisional Tax page before relying on them.

### 5.10 Filing Deadline and Penalties

**Filing Deadline and Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| PIT return deadline | 31 March of following year (3 months after 31 Dec year end); statutory default, FRCS has extended in specific years (e.g. 31 May) | FRCS File On Time — https://frcs.org.fj/about-us/cis-2025-2028/key-tax-obligations/file-on-time/ |
| Late lodgement penalty | 20% of tax owing (return filed late with tax payable) | Tax Administration Act 2009 s.43; FRCS Talk Tax Sole-traders — https://www.frcs.org.fj/wp-content/uploads/2018/02/99.Talk-Tax-Soletraders-v2.pdf |
| Late payment penalty | 25% of tax not paid on time | Tax Administration Act 2009 s.44; FRCS (as above) |
| Interest on arrears | 5% per month of unpaid tax thereafter | FRCS Debt Management — https://frcs.org.fj/our-services/taxation/debt-management-service/debt-management-services-dms/ |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home Office Deduction** — Calculate proportion of home used for business (dedicated room(s) as % of total rooms or floor area). Apply that percentage to: rent, electricity (EFL), water (WAF), internet. Must be a dedicated workspace — a dual-use room does NOT qualify. Client must document the calculation and retain records. Conservative default: 0% deduction until reviewer confirms room arrangement. Flag for reviewer: Confirm room count, floor-area basis, and that workspace is genuinely dedicated.  _(Income Tax Act 2015)_

### 6.2 Motor Vehicle Business Use

- **Motor Vehicle Business Use** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Client must maintain a mileage log (business vs total). Depreciation rate to be confirmed ([RESEARCH GAP]), multiplied by business %. Conservative default: 0% business use until mileage log provided. Flag for reviewer: Confirm business percentage is documented and reasonable, and confirm depreciation rate.

### 6.3 Phone / Internet Mixed Use

- **Phone / Internet Mixed Use** — Business use portion only (Vodafone, Digicel, Telecom Fiji). Client must provide a reasonable estimate of business vs personal use. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 Bad Debt Write-Off

- **Bad Debt Write-Off** — Deductible only if: (1) income was previously declared as assessable, (2) all reasonable recovery steps taken, (3) debt is genuinely irrecoverable. Flag for reviewer to confirm all three conditions.

### 6.5 Capital Item Depreciation Rate

- **Capital Item Depreciation Rate** — Fiji depreciation/wear-and-tear rates not extracted in research ([RESEARCH GAP]). Reviewer must apply the correct FRCS rate per asset class before any depreciation deduction.

### 6.6 SRT / ECAL High-Earner Computation

- **SRT / ECAL High-Earner Computation** — Any chargeable income above $270,000 triggers SRT and ECAL. First SRT band rate unconfirmed ([RESEARCH GAP] — 18% vs 13%). Flag for reviewer to confirm against the live FRCS PAYE/SRT/ECAL table.

### 6.7 Provisional Tax Instalments

- **Provisional Tax Instalments** — Exact instalment % and dates not extracted ([RESEARCH GAP]). Flag for reviewer to confirm from the FRCS Provisional Tax page.

## Section 7 -- Excel Working Paper Template

FIJI INCOME TAX -- PIT WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident / Non-resident
Taxpayer type: Sole trader / Combined employment+business (PIT "B") / Wage earner

A. GROSS BUSINESS INCOME
  A1. Client payments (net of VAT if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, etc.)       ___________
  A3. Other business income                          ___________
  A4. TOTAL business income                          ___________

B. ALLOWABLE BUSINESS DEDUCTIONS
  B1. Office rent                                    ___________
  B2. Professional insurance                         ___________
  B3. Accountancy / legal fees                       ___________
  B4. Office supplies / stationery                   ___________
  B5. Software subscriptions                         ___________
  B6. Marketing / advertising                        ___________
  B7. Bank charges / payment processing fees         ___________
  B8. Training                                       ___________
  B9. Travel (flights, hotels, transport)            ___________
  B10. Telecoms (business % of phone/internet)       ___________
  B11. Home office (% of utilities/rent)             ___________
  B12. Vehicle expenses (business %)                 ___________
  B13. Other allowable expenses                      ___________
  B14. TOTAL deductions                              ___________

C. NET BUSINESS PROFIT (A4 - B14)                    ___________

D. OTHER INCOME
  D1. Employment income                              ___________
  D2. Rental income                                  ___________
  D3. Investment income (interest/dividends)         ___________
  D4. TOTAL other income                             ___________

E. DEDUCTIONS FROM TOTAL INCOME
  E1. Depreciation (capital allowances)  [confirm rate] ________
  E2. FNPF employee contribution (8%)                ___________
  E3. TOTAL deductions                               ___________

F. CHARGEABLE INCOME (C + D4 - E3)                   ___________

G. TAX COMPUTATION (pass to deterministic engine)
  G1. Income tax (resident bands / 20% non-resident) ___________
  G2. SRT (if chargeable income > 270,000)           ___________
  G3. ECAL 5% (if chargeable income > 270,000)       ___________
  G4. Less: provisional tax paid                     ___________
  G5. Tax due / refund                               ___________

REVIEWER FLAGS:
  [ ] Residency status confirmed?
  [ ] VAT registration status confirmed (turnover vs $100k)?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] Depreciation rates confirmed (RESEARCH GAP)?
  [ ] FNPF deduction confirmed?
  [ ] Chargeable income > $270,000? (SRT/ECAL + first-band RESEARCH GAP)
  [ ] Provisional tax schedule confirmed (RESEARCH GAP)?
  [ ] Entertainment/personal excluded?
  [ ] Capital items depreciated (not expensed)?

## Section 8 -- Bank Statement Reading Guide

### Fijian Bank Statement Formats

**Fijian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| ANZ Fiji | PDF, CSV | Date, Description, Debit, Credit, Balance | Common; description holds counterparty + reference |
| BSP (Bank South Pacific) | PDF, CSV | Date, Particulars, Withdrawal, Deposit, Balance | Largest local bank |
| Westpac Fiji | PDF | Date, Description, Amount, Balance | Card transactions show merchant |
| HFC Bank | PDF | Date, Particulars, Withdrawals, Deposits | Shorter descriptions |
| Bred Bank Fiji | PDF, CSV | Date, Description, Amount, Currency |  |

### Key Fiji Banking / Tax Terms

**Key Fiji Banking / Tax Terms**

| Term | Meaning | Classification Hint |
| --- | --- | --- |
| EFTPOS | Card payment terminal | Expense — check merchant |
| DD / Direct Debit | Recurring debit | Regular expense (utility, subscription) |
| TFR / Transfer | Transfer | Check direction for income/expense |
| FNPF | Fiji National Provident Fund | Pension contribution (deduction) |
| FRCS | Fiji Revenue & Customs Service | Tax authority — tax payments not deductible |
| ECAL | Environment & Climate Adaptation Levy | Income levy (>$270k) or service levy |
| SRT | Social Responsibility Tax | High-earner surcharge (>$270k) |
| VAT | Value Added Tax (15%) | Exclude collected VAT from income |
| EFL | Energy Fiji Limited | Electricity (utility expense) |
| WAF | Water Authority of Fiji | Water (utility expense) |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

ONBOARDING QUESTIONS -- FIJI INCOME TAX
1. Residency: resident (worldwide income, $30k tax-free) or non-resident (Fiji-source, flat 20%)?
2. Taxpayer type: sole trader only, employment + business income (PIT "B"), or wage earner?
3. VAT registration: registered? Annual gross turnover above or below FJD 100,000?
4. Home office: dedicated room or shared space? If dedicated, what % of floor area?
5. Vehicle: do you use a car for business? If yes, what % is business use? Mileage log kept?
6. Phone/internet: what % is business use?
7. FNPF: total employee contributions paid in the tax year?
8. Provisional tax: total amount paid in the tax year?
9. Any other income (employment, rental, dividends, interest)?
10. Any capital assets purchased during the year (with cost)?
11. Is chargeable income expected to exceed FJD 270,000? (triggers SRT + ECAL)

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference / Source |
| --- | --- |
| Income tax rates (residents) | FRCS Tax Rates — https://frcs.org.fj/tax-rates-and-codes/ |
| Personal income tax / residency | FRCS PIT page — https://frcs.org.fj/our-services/taxation/individuals/personal-income-tax/ |
| Social Responsibility Tax | FRCS SRT page — https://frcs.org.fj/our-services/taxation/individuals/social-responsibility-tax-srt/ |
| ECAL on income | FRCS 2020/2021 PAYE PDF — https://www.frcs.org.fj/wp-content/uploads/2020/10/2020-2021-PAYE-Final-Tax.pdf |
| FNPF contributions | FNPF Employers — https://myfnpf.com.fj/employers/ |
| FNPF voluntary cap (FJD 250,000) | FNPF — https://myfnpf.com.fj/2025/02/19/fnpf-reverts-to-old-voluntary-and-additional-contribution-limit/ |
| VAT (15%, $100k threshold) | FRCS VAT Guide — https://www.frcs.org.fj/wp-content/uploads/2023/11/VAT-Guide-01.11.2-Online-version.pdf |
| Provisional tax | FRCS Provisional Tax — https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/provisional-tax/ |
| Filing deadline (31 March) | FRCS File On Time — https://frcs.org.fj/about-us/cis-2025-2028/key-tax-obligations/file-on-time/ |
| Penalties / interest (20% / 25% / 5%) | Tax Administration Act 2009 ss.43–44; FRCS Talk Tax Sole-traders — https://www.frcs.org.fj/wp-content/uploads/2018/02/99.Talk-Tax-Soletraders-v2.pdf |
| Business-individual return form | FRCS — https://www.frcs.org.fj/wp-content/uploads/2023/03/PERSONAL-INCOME-TAX-RETURN-FOR-BUSINESS-INDIVIDUAL.pdf |
| Minimum wage (FJD 5.00/hr) | Fiji Govt — https://www.fiji.gov.fj/Media-Centre/News/ |

### Forms

**Forms**

| Form | Use |
| --- | --- |
| Personal Income Tax Return for Business Individual | Sole traders / combined employment + business income (PIT class "B"). Source: FRCS — https://www.frcs.org.fj/wp-content/uploads/2023/03/PERSONAL-INCOME-TAX-RETURN-FOR-BUSINESS-INDIVIDUAL.pdf |
| Standard individual PIT return | Salary/wage earners; many settled via PAYE as final tax |
| Filing channel | Taxpayer Online Service (TPOS) — FRCS |

### RESEARCH GAPS — Reviewer Must Confirm Before Publishing

1. First SRT band rate (270,001–300,000): FRCS summary shows 18%; superseded 2020/21 PDF showed 13%. Confirm against live FRCS PAYE/SRT/ECAL table.
2. FNPF compulsory contribution wage ceiling: not confirmed on FNPF's official site — state as none/unconfirmed.
3. Provisional tax instalment rate/schedule: pull exact figures from the FRCS Provisional Tax page.
4. Depreciation / wear-and-tear rates (Income Tax Act 2015): not extracted; do not apply a rate without confirmation.
5. Live FRCS PAYE/SRT/ECAL table (https://frcs.org.fj/our-services/calculators/paye-tax-tables/) returned 404 to automated fetch — verify the current-year table manually.

### Test Suite

Test 1 -- Resident, within tax-free threshold.
Input: Resident, chargeable income $25,000.
Expected: Income tax = $0.00 (below $30,000 threshold). No SRT/ECAL.

Test 2 -- Resident, lower band.
Input: Resident, chargeable income $45,000.
Expected: 18% × (45,000 − 30,000) = 18% × 15,000 = $2,700.00.

Test 3 -- Resident, mid band.
Input: Resident, chargeable income $80,000.
Expected: 3,600 + 20% × (80,000 − 50,000) = 3,600 + 6,000 = $9,600.00. No SRT/ECAL.

Test 4 -- Resident, top of the flat-20% range.
Input: Resident, chargeable income $270,000.
Expected: 3,600 + 20% × (270,000 − 50,000) = 3,600 + 44,000 = $47,600.00. No SRT/ECAL (not above $270,000).

Test 5 -- Non-resident.
Input: Non-resident, Fiji-sourced chargeable income $40,000.
Expected: 20% × 40,000 = $8,000.00 (no tax-free threshold).

Test 6 -- VAT-registered income, net reporting.
Input: VAT-registered. Client payment $1,150 gross (incl. 15% VAT).
Expected: Business income = $1,000.00; VAT $150.00 excluded.

Test 7 -- FNPF employee contribution.
Input: Gross monthly wage $3,000, employee FNPF 8%.
Expected: FNPF deduction = $240.00 (8% × 3,000). Employer adds 10% = $300.00; total 18% = $540.00.

Test 8 -- High earner (escalation).
Input: Resident, chargeable income $400,000.
Expected: STOP / flag for reviewer (R-FJ-3) — SRT and ECAL apply above $270,000 and the first SRT band rate is a RESEARCH GAP. Do not finalise without confirming the live FRCS table.

## PROHIBITIONS

- NEVER apply a rate table without confirming residency status (resident vs non-resident)
- NEVER apply the $30,000 tax-free threshold to a non-resident
- NEVER finalise SRT or ECAL without confirming the live FRCS table (first SRT band is a RESEARCH GAP)
- NEVER apply a depreciation rate to a capital item without reviewer confirmation (rates are a RESEARCH GAP)
- NEVER allow entertainment or personal expenses as a deduction
- NEVER allow income tax itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER include VAT collected on sales in business income for a VAT-registered trader
- NEVER expense a capital item in full — it must be depreciated
- NEVER treat FNPF as a business expense line — it is a deduction from total income
- NEVER use current year income for provisional tax — always confirm the FRCS basis (RESEARCH GAP)
- NEVER present tax calculations as definitive — always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
