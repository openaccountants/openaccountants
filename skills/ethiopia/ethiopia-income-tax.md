---
name: ethiopia-income-tax
description: Use this skill whenever asked about Ethiopia (ET) personal or business income tax. Trigger on phrases like "how much income tax do I pay in Ethiopia", "PAYE Ethiopia", "ETB salary tax", "Schedule A B C D", "Category A taxpayer", "Category B turnover tax", "rental income tax Ethiopia", "Proclamation 1395/2025", "pension contribution Ethiopia", "POESSA", "Ministry of Revenues", "net pay calculation Birr", "minimum alternative tax", or any question about computing or filing income tax for an employee, sole proprietor, or landlord in Ethiopia. Also trigger when reviewing payroll, computing PAYE withholding, classifying business income, or advising on advance tax. This skill covers monthly PAYE brackets, business/rental annual schedules, Category A/B turnover tax, pension contributions, VAT registration interaction, filing deadlines, and the Ethiopian fiscal calendar. ALWAYS read this skill before touching any Ethiopia income tax work.
version: 0.2
jurisdiction: ET
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ethiopia Income Tax: Employment and Self-Employed

## Who this applies to

Individuals with Ethiopian employment, rental, business or other income. The tax year runs 8 July to 7 July. Category A means a body, or any other person with annual turnover of ETB 2,000,000 or more. Category B means individuals, not bodies, below that (art. 3, as replaced). The rates below apply to income derived from 8 July 2025 and stay in force for the year from 8 July 2026; the Schedule D and domestic withholding changes run from 7 August 2025 (Proc. 1395/2025 art. 4). Companies: see [corporate income tax](et-corporate-income-tax.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Employment income, monthly: 0 to 2,000 / 2,001 to 4,000 / 4,001 to 7,000 / 7,001 to 10,000 / 10,001 to 14,000 / over 14,000 (art. 11) | 0% / 15% / 20% / 25% / 30% / 35% | 2026 | https://www.hopr.gov.et/admin/Files/2026/4/8/5fc57d68-d0f6-4bf1-91b4-5b23abd0df72%E1%8C%88%E1%89%A2%20%E1%8C%8D%E1%89%A5%E1%88%AD%20%201395.pdf |
| Rental income of individuals, annual: 0 to 24,000 / 24,001 to 48,000 / 48,001 to 84,000 / 84,001 to 120,000 / 120,001 to 168,000 / over 168,000 (art. 14(2)) | 0% / 15% / 20% / 25% / 30% / 35% | 2026 | same |
| Business income of individuals, same annual bands (art. 19(2)) | 0% / 15% / 20% / 25% / 30% / 35% | 2026 | same |
| Category B gross sales: to 100,000 / to 500,000 / to 1,000,000 / to 1,500,000 / below 2,000,000 (art. 50(3)) | 2% / 3% / 5% / 7% / 9% | 2026 | same |
| Minimum alternative tax, business income below 2.5% of turnover; not for art. 49 gross-sales payers, an entity in liquidation or a body in debt restructuring (art. 23) | 2.5% of turnover | 2026 | same |
| Dividend, resident (art. 57) | 15% | 2026 | same |
| Interest, resident (art. 58); sale on credit and financial-institution deposits go to Schedule C | 10% | 2026 | same |
| Royalty, resident (art. 56): art and culture / other | 5% / 10% | 2026 | same |
| Games of chance (art. 59) | 20% | 2026 | same |
| Gain on shares, bonds and buildings, after a 30% inflation adjustment (art. 61); a private residence held and wholly used for 2 years is out | 15% | 2026 | same |
| Cash receipt limit: over ETB 50,000 must go through bank channels (arts 29(1)(o), 81); breach costs the amount received (art. 88) | ETB 50,000 | 2026 | same |
| Domestic withholding on goods over 20,000 / services of 10,000 (art. 97(1)); 30% if no TIN and licence (art. 97(4)) | 3% | 2026 | same |
| Pension rates: see [social contributions](ethiopia-social-contributions.md) | link | 2026 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%2F2%2F25%2Ffc53f560-b228-4314-b372-da2b26ef4b53_Upploads_04012023090127_%E1%8B%A8%E1%8C%8D%E1%88%8D%20%E1%8B%B5%E1%88%AD%E1%8C%85%E1%89%B5%20%E1%88%A0%E1%88%AB%E1%89%B0%E1%8A%9E%E1%89%BD%20%E1%8C%A1%E1%88%A8%E1%89%B3%20%E1%8A%A0%E1%8B%8B%E1%8C%85%20%E1%89%81%E1%8C%A5%E1%88%AD%201268%20(1).pdf |

Category B professionals (accounting, architecture, consulting, construction, engineering, finance, economics and investment, health care, legal), VAT-registered businesses and those who elect by filing under Schedule C do not use the gross-sales table (art. 50(4)).

## The base

Digital content income is business income when carried on regularly for profit, by an organisation, or with books or deductible costs; otherwise it is Schedule D income (art. 22). A loan used to buy shares in another company gives deductible interest only if that company pays a dividend (art. 86(9)). Donations are capped at 10% of taxable income (art. 26(2)). Category A taxpayers with several businesses keep separate books for each (art. 86(8)). Failing to submit records means assessment on estimate, without the Category B method (art. 86(8) as first inserted).

## Deadlines and filing

1. Category A: file the annual declaration within 4 months of year end; Category B: within 2 months (Proc. 979/2016 art. 83(4), [Amharic print](https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/979.pdf)).
2. Advance tax: Category A and B pay 25% of last year's tax within 30 working days of each quarter end (art. 89(2), (4)). New taxpayers skip this in their first year: Category A pays with the declaration; Category B pays between Hamle 1 and Hamle 30 (art. 89(5)).
3. Employee with more than one employer, or self-withholding: declare within 30 days of year end (art. 87(2)).
4. Schedule D income not already withheld: declare within 2 months of the transaction (Proc. 979/2016 art. 83(7)).
5. Forms: the [Ministry forms page](https://www.mor.gov.et/forms) lists business income and withholding declarations; use the form for your business type.

## Penalties and interest

See the table in [payroll](ethiopia-payroll.md#penalties-and-interest), which holds the Tax Administration Proclamation figures for the whole pack. Disposal not notified under art. 62 draws a Tax Administration penalty (art. 62(8)).

## Cross-border points

Service and construction permanent establishment: over 91 days in a tax year or any one-year period (art. 4(2)(c), (3)). Non-resident rates: insurance premium 15%, royalty 10%, dividend 15%, interest 10%, management or technical fee 15% (art. 52(2)). Offshore transfers count where over 20% of value came from Ethiopian property in the prior 365 days (art. 62). Non-resident digital services are Ethiopian-source (art. 6(6)).

## Two worked examples that recompute

Simple case: monthly salary ETB 10,000 gives tax of ETB 1,650.

```oa-check
name: Monthly salary ETB 10,000
inputs:
  s: 10000
steps:
  - b15: (min(s, 4000) - 2000) * 0.15
  - b20: (min(s, 7000) - 4000) * 0.20
  - b25: (min(s, 10000) - 7000) * 0.25
  - b30: (min(s, 14000) - 10000) * 0.30
  - b35: max(s - 14000, 0) * 0.35
  - tax: b15 + b20 + b25 + b30 + b35
expected:
  tax: 1650.00
```

Decision: a Category B trader with sales of ETB 1,500,000 and profit of ETB 300,000. Gross sales tax is 105,000. Electing Schedule C gives 80,400, so electing saves 24,600, if books are acceptable.

```oa-check
name: Gross sales or net election
inputs:
  sales: 1500000
  p: 300000
steps:
  - gross: sales * 0.07
  - b15: 24000 * 0.15
  - b20: 36000 * 0.20
  - b25: 36000 * 0.25
  - b30: 48000 * 0.30
  - b35: (p - 168000) * 0.35
  - net: b15 + b20 + b25 + b30 + b35
  - saving: gross - net
expected:
  gross: 105000.00
  net: 80400.00
  saving: 24600.00
```

## Ask the client first

- Resident or non-resident, and from when?
- Employee, landlord, trader, professional or digital creator?
- Annual turnover, and is the client VAT registered?
- Are books kept to an acceptable standard?
- More than one employer in the year?

## Sources

| Source | URL | Read on | What was read |
|---|---|---|---|
| Income Tax (Amendment) Proclamation 1395/2025, Federal Negarit Gazette 31st Year No. 64 | https://www.hopr.gov.et/admin/Files/2026/4/8/5fc57d68-d0f6-4bf1-91b4-5b23abd0df72%E1%8C%88%E1%89%A2%20%E1%8C%8D%E1%89%A5%E1%88%AD%20%201395.pdf | 2026-11-01 | Whole text read (English column) |
| Federal Income Tax Proclamation 979/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/979.pdf | 2026-11-01 | Declaration, payment, withholding and exemption articles read in Amharic; article numbers are those before the 1395/2025 renumbering |
| Federal Tax Administration Proclamation 983/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/983.pdf | 2026-11-01 | Penalty articles and art. 37 read in Amharic |
| Tax Administration (Amendment) Proclamation 1434/2026, Federal Negarit Gazette 32nd Year No. 48, 30 July 2026, listed by the Ministry of Revenues | https://www.mor.gov.et/domestic-law-proclamation | 2026-11-01 | Whole text read; adds 17 to the penalty article numbers of 983/2016 |
| Private Organization Employees Pension Proclamation 1268/2022 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%2F2%2F25%2Ffc53f560-b228-4314-b372-da2b26ef4b53_Upploads_04012023090127_%E1%8B%A8%E1%8C%8D%E1%88%8D%20%E1%8B%B5%E1%88%AD%E1%8C%85%E1%89%B5%20%E1%88%A0%E1%88%AB%E1%89%B0%E1%8A%9E%E1%89%BD%20%E1%8C%A1%E1%88%A8%E1%89%B3%20%E1%8A%A0%E1%8B%8B%E1%8C%85%20%E1%89%81%E1%8C%A5%E1%88%AD%201268%20(1).pdf | 2026-11-01 | Arts 2, 10 to 12 read |
| Ministry of Revenues forms list | https://www.mor.gov.et/forms | 2026-11-01 | Titles of the published forms read; the form boxes were not read |

Not yet confirmed: the Council of Ministers income tax regulation that sets the digital service tax rate (capped at 5%) was not found; the e-tax portal steps and the box numbers on the Ministry forms were not read, so no box numbers are given as law; whether a Category B band rate applies to all sales or only the slice in the band (art. 50(3) is read here as all sales); whether the employee 7% pension reduces taxable employment income (the examples do not reduce it); the older taxable-allowance limits, Regulation 410/2017 figures, ETB 15,000 pension ceiling, and other items in the retained working notes below, which come from the earlier version and were not re-read.

### Retained working notes from the earlier version (not re-read against the law)

### Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ethiopia (Federal Democratic Republic of Ethiopia) |
| Tax | Income Tax (PAYE on employment; Schedule B/C/D on other income) |
| Currency | Ethiopian Birr (ETB) only |
| Tax year (fiscal) | 8 July -- 7 July (Hamle 1 -- Sene 30, Ethiopian calendar) |
| Primary legislation | Income Tax Proclamation No. 979/2016, as amended by Income Tax (Amendment) Proclamation No. 1395/2025 (effective 8 July 2025) |
| Supporting legislation | Tax Administration Proclamation No. 983/2016; VAT Proclamation No. 1341/2024 + Regulation 570/2025; Private Organizations Employees' Pension law (the pension fund administration) |
| Tax authority | Ministry of Revenues (MOR), `mor.gov.et` (formerly ERCA) |
| Pension authority | Private Organizations Employees Social Security Agency (the pension fund administration) |
| Filing portal | MOR e-services / regional revenue bureaus |
| Validated by | Pending, requires sign-off by an Ethiopian tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

**Calendar caution.** The Ethiopian calendar runs ~7–8 days behind the Gregorian calendar. Statutory "month-end" deadlines therefore tend to land around the 7th–8th of the following Gregorian month. Always confirm the exact Gregorian date against the Ethiopian month boundary.

#### PAYE, Monthly Employment Income Brackets (effective 8 July 2025)

**PAYE Monthly Employment Income Brackets**

| Monthly taxable income (ETB) | Marginal rate | Quick-calc deduction (ETB) | Cumulative tax at band ceiling |
| --- | --- | --- | --- |
| 0 – 2,000 | 0% (exempt) |, | 0 |
| 2,001 – 4,000 | 15% | 300 | 300 |
| 4,001 – 7,000 | 20% | 500 | 900 |
| 7,001 – 10,000 | 25% | 850 | 1,650 |
| 10,001 – 14,000 | 30% | 1,350 | 2,850 |
| Over 14,000 | 35% | 2,050 |, |

- **PAYE formula**, Monthly tax = (Gross monthly taxable salary × band rate) − quick-calc deduction

> (not confirmed) The quick-calc deduction column (300 / 500 / 850 / 1,350 / 2,050) is **derived by computation** from the published cumulative-tax figures (0 / 300 / 900 / 1,650 / 2,850), using the standard progressive identity. The math reconciles exactly, but the deduction constants were **not found stated verbatim** in an authoritative source. The brackets and marginal rates themselves ARE authoritative. The OLD pre-2025 deductions (60 / 142.50 / 302.50 / 565 / 955 / 1,500) are obsolete, do not use them.

- **Changes vs prior law**, tax-free threshold raised ETB 600 → ETB 2,000/month; lowest positive rate raised 10% → 15%; brackets cut 7 → 6; the 35% top rate now applies above ETB 14,000 (previously above 10,900).
- **Residence/scope**, Residents are taxed on worldwide income; non-residents on Ethiopian-source income; the same rate schedule applies.

#### Business / Self-Employed (Schedule C), Annual Progressive Rates

**Business Schedule C Annual Progressive Rates**

| Annual taxable business income (ETB) | Rate |
| --- | --- |
| 0 – 24,000 | 0% |
| 24,001 – 48,000 | 15% |
| 48,001 – 84,000 | 20% |
| 84,001 – 120,000 | 25% |
| 120,001 – 168,000 | 30% |
| Over 168,000 | 35% |

#### Rental Income (Schedule B), Annual Progressive Rates

**Rental Income Schedule B Annual Progressive Rates**

| Annual taxable rental income (ETB) | Rate |
| --- | --- |
| 0 – 24,000 | 0% |
| 24,001 – 48,000 | 15% |
| 48,001 – 84,000 | 20% |
| 84,001 – 120,000 | 25% |
| 120,001 – 168,000 | 30% |
| Over 168,000 | 35% |

#### Category B, Turnover / Gross-Sales Tax (presumptive)

Applies to non-professional, non-VAT-registered Category B individuals (turnover below ETB 2,000,000).

**Category B gross sales tax table**

| Annual gross sales (ETB) | Rate on turnover |
| --- | --- |
| 0 – 100,000 | 2% |
| 100,001 – 500,000 | 3% |
| 500,001 – 1,000,000 | 5% |
| 1,000,001 – 1,500,000 | 7% |
| 1,500,001 – 2,000,000 | 9% |

#### Pension Contributions (Private Organizations Employees' Pension)

**Pension Contributions table**

| Party | Rate | Base |
| --- | --- | --- |
| Employee | 7% | basic/gross salary, normal working hours |
| Employer | 11% | same base |
| **Total** | **18%** |  |

- **Pension mandatory scope**, Arithmetic check: 7% + 11% = 18%. ✓ Mandatory for Ethiopian citizens; foreign nationals are NOT required to contribute (optional for foreigners of Ethiopian origin only).

#### Other Headline Rates

**Other Headline Rates table**

| Item | Value | Source |
| --- | --- | --- |
| VAT standard rate | 15% | EY VAT alert; haymanotbelay.com |
| VAT registration threshold | turnover > ETB 2,000,000 over any 12 months (Proclamation 1341/2024) | EY VAT alert |

#### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residence status | STOP, confirm resident vs non-resident before applying scope |
| Unknown citizenship (for pension) | STOP, pension obligation depends on Ethiopian citizenship |
| Unknown taxpayer category (A vs B) | Treat as Category A (full books) unless turnover confirmed < ETB 2,000,000 |
| Unknown whether individual is a "listed professional" | Treat as Category A (professionals are always Category A) |
| Unknown pension salary base | Use basic/gross salary; flag the ceiling question (see RESEARCH GAP) |
| Unknown income schedule (employment/business/rental) | STOP, schedule determines the rate table and periodicity |
| Unknown expense business-purpose | Not deductible |

### Section 2 -- Required Inputs and Refusal Catalogue

#### Required Inputs

**Minimum viable**, for employment: monthly gross salary (basic + taxable allowances), citizenship (for pension), residence status. For business/rental: the relevant statements/ledgers for the full fiscal year, plus taxpayer category and turnover.

**Recommended**, payslips, employment contract, pension remittance records, prior-year tax declaration, VAT registration status, breakdown of allowances (which are taxable vs exempt).

**Ideal**, full income and expenditure account, asset register, advance-tax payment confirmations, audited financials (Category A).

**Refusal if minimum is missing, SOFT WARN.** No salary/income figures at all = hard stop. Salary without an allowance breakdown = proceed with reviewer warning: "PAYE was computed treating all stated pay as taxable. The reviewer must confirm which allowances are statutorily exempt before filing."

#### Refusal Catalogue

- **R-ET-1, Residence status unknown**, "Residents are taxed on worldwide income; non-residents only on Ethiopian-source income. This skill cannot scope income without confirmed residence status. Please confirm before proceeding."
- **R-ET-2, Companies / legal persons**, "This skill covers individuals (employees, sole proprietors, landlords). Corporate income tax (30% on companies) and Category A legal-person filings require separate analysis. Escalate to an Ethiopian tax practitioner."
- **R-ET-3, Schedule D investment income**, "Dividend, interest, and royalty withholding (Schedule D) rates were not re-verified in this build and must be confirmed against Proclamation 979/2016 / MOR before computing. Escalate or confirm the rate first."
- **R-ET-4, Penalties / enforcement / arrears**, "Late-filing, late-payment interest, and under-declaration penalty figures are not confirmed in this skill. Do not state penalty numbers. Escalate to an Ethiopian tax practitioner."
- **R-ET-5, VAT return requested**, "This skill covers income tax only. VAT (15%, Proclamation 1341/2024) is out of scope here."
- **R-ET-6, Pension ceiling-dependent computation**, "Several sources report an ETB 15,000/month pension salary cap, but it is not confirmed against the pension fund administration/the proclamation. For high earners where the cap changes the result, flag the figure for reviewer confirmation rather than asserting it."

### Section 3 -- Transaction Pattern Library

Deterministic pre-classifier. Match by case-insensitive substring on the counterparty/description as it appears on the bank statement or payroll register. Most specific match wins. If none match, fall through to Tier 1 rules in Section 5. Amharic terms are given alongside English where commonly seen.

#### 3.1 Income Patterns (Credits)

**Income Patterns table**

| Pattern | Schedule / Line | Treatment | Notes |
| --- | --- | --- | --- |
| SALARY, DEMOZ (ደሞዝ), NET PAY, PAYROLL | Employment (PAYE) | Employment income | Tax via monthly PAYE table; employer withholds |
| ALLOWANCE, ABEL (አበል), TRANSPORT ALLOWANCE | Employment (PAYE) | Taxable unless statutorily exempt | Flag which allowances are exempt |
| CLIENT PAYMENT, INVOICE, GUBA'E, CONSULTANCY FEE | Schedule C (business) | Business income | Sole-proprietor revenue |
| TELEBIRR, CBE BIRR, M-PESA (business inflow) | Schedule C | Business income | Mobile-money business receipts, match to invoices |
| KIRAY (ኪራይ), RENT RECEIVED, HOUSE RENT | Schedule B (rental) | Rental income | Annual progressive table |
| INTEREST, DIVIDEND | Schedule D | Investment income | (not confirmed) |
| TAX REFUND, MOR REFUND | EXCLUDE | Not income | Refund of prior-year tax |
| GRANT, NGO TRANSFER | Check nature | Capital grants EXCLUDE; revenue grants = business income | Confirm grant type |

#### 3.2 Expense Patterns (Debits), Business, Generally Deductible

**Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| SHOP RENT, OFFICE KIRAY, COMMERCIAL RENT | Premises rent | Deductible | Dedicated business premises |
| SALARY PAID, WAGES, STAFF DEMOZ | Staff costs | Deductible | Employer payroll cost |
| ETHIO TELECOM, INTERNET, DATA (business) | Telecoms | Deductible (business %) | Apportion if mixed use |
| ETHIOPIAN ELECTRIC, EEU, WATER (business) | Utilities | Deductible (business %) | 100% if dedicated premises |
| ACCOUNTANT, AUDIT, LEGAL FEES (business) | Professional fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| ADVERTISING, MARKETING, FACEBOOK ADS | Advertising | Deductible |  |
| BANK CHARGE, CBE FEE, COMMISSION | Bank charges | Deductible | Business account |
| FUEL, BENZIN, NAFTA (business %) | Vehicle fuel | Deductible (business %) | Requires log |

#### 3.3 Expense / Withholding Patterns, Statutory (NOT P&L deductions in the normal way)

**Statutory Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| PENSION, the pension fund administration, SOCIAL SECURITY | Pension contribution | Employee 7% withheld pre-PAYE base treatment; employer 11% is an employer cost | Not a Schedule-C "expense" line for an employee |
| PAYE, INCOME TAX, MOR TAX | Income tax remittance | EXCLUDE from deductions | Tax itself is not deductible |
| VAT PAYMENT, MOR VAT | VAT liability | EXCLUDE | Not an income-tax expense |
| ADVANCE TAX, QUARTERLY TAX | Advance income tax | Credit against final liability, not an expense | Category A & B quarterly |

#### 3.4 Expense Patterns, NOT Deductible

**Not Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GROCERIES, SUPERMARKET, PERSONAL, FAMILY | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, MOR PENALTY | Fines/penalties | NOT deductible | Public policy |
| DRAWINGS, OWNER WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |
| ENTERTAINMENT, PARTY, GIFT (non-business) | Entertainment/gifts | NOT deductible | Flag, confirm any business portion |

#### 3.5 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, SAVINGS | EXCLUDE | Own-account movement |
| LOAN, LOAN REPAYMENT, BRIDGE | EXCLUDE | Loan principal movement |
| CAPITAL INJECTION, OWNER CAPITAL | EXCLUDE | Equity movement, not income |

#### 3.6 Ethiopian Banks / Payment Channels, Statement Format Reference

**Banks table**

| Provider | Common Patterns | Notes |
| --- | --- | --- |
| Commercial Bank of Ethiopia (CBE) | TRANSFER, CBE BIRR, COMMISSION, CHARGE | PDF/SMS; date often Ethiopian + Gregorian |
| Awash Bank | TRF, DEBIT, CREDIT, CHARGE | PDF |
| Dashen / Abyssinia / Wegagen | TRANSFER, DEPOSIT, FEE | PDF |
| telebirr (Ethio Telecom) | RECEIVE, SEND, PAYMENT, MERCHANT | Mobile-money statement; clean counterparty |
| M-PESA Ethiopia (Safaricom) | RECEIVED, PAID, WITHDRAW | Mobile-money statement |

### Section 4 -- Worked Examples

All amounts in ETB. PAYE computed as `(gross taxable salary × band rate) − quick-calc deduction`. Employee pension = 7% of basic/gross salary, deducted in addition to PAYE to reach net pay.

#### Example 1, Low earner (15% band)

**Input line:**
`Hamle 2018 ; PAYROLL ; DEMOZ ; gross salary ; +3,000.00 ; ETB`

**Reasoning:**
Gross taxable salary 3,000 falls in the 2,001–4,000 band (15%, deduction 300).
PAYE = 3,000 × 0.15 − 300 = 450 − 300 = **150**.
Employee pension = 3,000 × 7% = **210**.
Net pay = 3,000 − 150 − 210 = **2,640**.

**Classification:** PAYE 150; pension 210; net 2,640.

#### Example 2, Mid earner (20% band)

**Input line:**
`Nehase 2018 ; PAYROLL ; DEMOZ ; gross salary ; +6,000.00 ; ETB`

**Reasoning:**
6,000 is in the 4,001–7,000 band (20%, deduction 500).
PAYE = 6,000 × 0.20 − 500 = 1,200 − 500 = **700**.
Pension = 6,000 × 7% = **420**.
Net pay = 6,000 − 700 − 420 = **4,880**.

**Classification:** PAYE 700; pension 420; net 4,880.

#### Example 3, Upper-mid earner (30% band)

**Input line:**
`Meskerem 2018 ; PAYROLL ; DEMOZ ; gross salary ; +12,000.00 ; ETB`

**Reasoning:**
12,000 is in the 10,001–14,000 band (30%, deduction 1,350).
PAYE = 12,000 × 0.30 − 1,350 = 3,600 − 1,350 = **2,250**.
Pension = 12,000 × 7% = **840**.
Net pay = 12,000 − 2,250 − 840 = **8,910**.

**Classification:** PAYE 2,250; pension 840; net 8,910.

#### Example 4, High earner (35% top band; pension ceiling flagged)

**Input line:**
`Tikimt 2018 ; PAYROLL ; DEMOZ ; gross salary ; +20,000.00 ; ETB`

**Reasoning:**
20,000 is over 14,000 (35%, deduction 2,050).
PAYE = 20,000 × 0.35 − 2,050 = 7,000 − 2,050 = **4,950**.
Pension: if NO ceiling, 20,000 × 7% = 1,400 → net = 20,000 − 4,950 − 1,400 = **13,650**.
Pension: if the widely-reported ETB 15,000 ceiling applies, 15,000 × 7% = 1,050 → net = 20,000 − 4,950 − 1,050 = **14,000**.

> (not confirmed) The pension salary ceiling (reported as ETB 15,000/month) is not verified against the pension fund administration/the proclamation. For earners above the cap this changes net pay. Present both figures and flag for reviewer.

**Classification:** PAYE 4,950; pension 1,050–1,400 (ceiling-dependent); net 13,650–14,000.

#### Example 5, Exempt earner (below threshold)

**Input line:**
`Hidar 2018 ; PAYROLL ; DEMOZ ; gross salary ; +2,000.00 ; ETB`

**Reasoning:**
2,000 is within the 0% band (0–2,000), so PAYE = **0**.
Pension still applies: 2,000 × 7% = **140**.
Net pay = 2,000 − 0 − 140 = **1,860**.

**Classification:** PAYE 0; pension 140; net 1,860.

#### Example 6, Sole proprietor (Schedule C annual)

**Input:** Category A individual consultant, annual taxable business income ETB 200,000 (turnover ETB 600,000).

**Reasoning:**
Schedule C is progressive on annual taxable income. Over 168,000 → top rate 35%.
Tax via the same progressive identity, top band: 200,000 falls over 168,000.
Cumulative tax to 168,000 = (24k@0) + (24k@15%=3,600) + (36k@20%=7,200) + (36k@25%=9,000) + (48k@30%=14,400) = 34,200.
Excess 200,000 − 168,000 = 32,000 × 35% = 11,200.
Income tax = 34,200 + 11,200 = **45,400**.
MAT check: 2.5% × turnover 600,000 = 15,000. Income tax 45,400 > 15,000, so MAT does not bite.

**Classification:** Schedule C income tax = 45,400 (MAT not triggered).

> Cumulative-tax arithmetic verified: 3,600 + 7,200 + 9,000 + 14,400 = 34,200 at ETB 168,000. ✓

### Section 5 -- Tier 1 Rules (When Data Is Clear)

#### 5.1 PAYE Computation (Employment)

- **Monthly PAYE formula**, Monthly PAYE = (gross monthly taxable salary × band rate) − quick-calc deduction. The 0–2,000 band is exempt. Employer is responsible for withholding and monthly remittance.

#### 5.2 Taxable vs Exempt Allowances

- **Taxable vs exempt allowances**, Not all allowances are taxable. Some (e.g. certain transport, hardship, or per-diem allowances within statutory limits) are exempt. Treat all stated pay as taxable by default, and flag the exempt-allowance question for reviewer confirmation against Proclamation 979/2016. (not confirmed)  _(Proclamation 979/2016)_

#### 5.3 Schedule Selection

**Schedule Selection table**

| Income type | Schedule | Periodicity | Rate table |
| --- | --- | --- | --- |
| Employment | "A" (PAYE) | Monthly | Section 1 monthly bands |
| Rental | "B" | Annual | Section 1 rental table |
| Business (individual, keeping books) | "C" | Annual | Section 1 business table |
| Investment (dividend/interest/royalty) | "D" | Withholding | (not confirmed) |

#### 5.4 Taxpayer Categories (Proclamation 1395/2025)

- **Category A**, all legal persons (companies) regardless of turnover; any individual/business with annual turnover > ETB 2,000,000; and all listed professionals (accountants, lawyers, engineers, etc.) regardless of turnover. Full books required.
- **Category B**, unincorporated individuals with annual turnover below ETB 2,000,000, excluding listed professionals and VAT-registered persons.
- **Category C abolished**, Category C (old presumptive small-trader category) was abolished by 1395/2025.

#### 5.5 Category B gross sales tax

- **Category B gross sales tax rule**, Non-professional, non-VAT-registered Category B individuals pay a presumptive gross sales tax on gross sales per the Section 1 turnover table (2% → 9%).

#### 5.6 Minimum Alternative Tax (MAT)

- **MAT rule**, If income tax computed on business income is below 2.5% of annual turnover, the taxpayer pays 2.5% of turnover instead. Applies even where incentives/exemptions exist, and extends to rental and digital side income.

#### 5.7 Pension Contributions

- **Pension contributions rule**, Employee 7% / employer 11% (total 18%) of basic/gross salary for Ethiopian citizens. The employee 7% is withheld and is not part of taxable employment income (deducted before arriving at net pay). Foreign nationals are not required to contribute. Vesting requires a minimum of 10 years' contributions. Remittance is due within 30 days of the relevant month-end.

#### 5.8 Capital Gains

- **Capital gains tax rate**, 15% percent (unchanged by 1395/2025)

#### 5.9 Non-Deductible Items (Business)

**Non-Deductible Items table**

| Item | Reason |
| --- | --- |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Drawings / owner withdrawals | Not an expense |
| VAT liability payments | Separate tax |

#### 5.10 Filing & Payment

**Filing and Payment table**

| Item | Detail | Source |
| --- | --- | --- |
| Advance tax (NEW, 1395/2025) | Category A & B make quarterly advance payments ≈ prior-year tax; due within 30 days after each 3-month cycle | ethiodiasporahub.com; EY alert |

### Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

#### 6.1 Exempt Allowance Determination

- **Exempt allowance determination**, Which allowances (transport, hardship, per-diem, representation) are exempt and to what statutory limit. Default: treat as taxable. Flag for reviewer against Proclamation 979/2016.  _(Proclamation 979/2016)_

#### 6.2 Pension Salary Ceiling

- **Pension salary ceiling**, Whether the ETB 15,000/month base cap applies. Default: compute on full basic salary AND show the capped figure. Flag for reviewer (see RESEARCH GAP).

#### 6.3 Resident vs Non-Resident Scope

- **Resident vs non-resident scope**, Worldwide vs Ethiopian-source. Default: STOP and confirm residence.

#### 6.4 Category A vs B Classification

- **Category A vs B classification**, Turnover threshold (ETB 2,000,000), listed-professional status, VAT registration. Default: Category A. Flag for reviewer.

#### 6.5 Schedule C vs Turnover Tax

- **Schedule C vs gross sales tax**, Whether a Category B individual is on progressive Schedule C (keeps books) or presumptive gross sales tax. Flag for reviewer.

#### 6.6 MAT Application

- **MAT application**, Whether 2.5%-of-turnover MAT overrides computed income tax. Recompute both and present the higher. Flag for reviewer.

#### 6.7 Mixed-Use Expense Apportionment

- **Mixed-use expense apportionment**, Business percentage of vehicle, telecom, utilities, home premises. Default: 0% business use until documented. Flag for reviewer.

#### 6.8 Schedule D Withholding

- **Schedule D withholding**, Dividend/interest/royalty rates. Default: STOP, do not assert a rate. (not confirmed)

### Section 7 -- Excel Working Paper Template

```
ETHIOPIA INCOME TAX -- WORKING PAPER
Fiscal Year: 2025/2026 (8 Jul 2025 – 7 Jul 2026)
Client: ___________________________
Income type: Employment / Business (Sch C) / Rental (Sch B)
Residence: Resident / Non-resident
Citizenship (pension): Ethiopian / Foreign

A. EMPLOYMENT (PAYE), MONTHLY
  A1. Gross salary (basic)                       ___________
  A2. Taxable allowances                         ___________
  A3. Exempt allowances (FLAG)                    (__________)
  A4. Gross taxable salary (A1 + A2)             ___________
  A5. Band rate ____%  Quick-calc deduction ____ ___________
  A6. PAYE = (A4 × rate) − deduction             ___________
  A7. Employee pension (7% × base; ceiling FLAG) ___________
  A8. Net pay = A4 − A6 − A7                      ___________
  A9. Employer pension (11% × base) [memo]       ___________

B. BUSINESS (SCHEDULE C), ANNUAL
  B1. Gross business income                      ___________
  B2. Less: allowable expenses                   (__________)
  B3. Net taxable business income                ___________
  B4. Schedule C tax (progressive)               ___________
  B5. Turnover                                   ___________
  B6. MAT check = 2.5% × B5                       ___________
  B7. Income tax due = max(B4, B6)               ___________

C. RENTAL (SCHEDULE B), ANNUAL
  C1. Gross rent                                 ___________
  C2. Less: allowable expenses                   (__________)
  C3. Net taxable rent                           ___________
  C4. Schedule B tax (progressive)               ___________

D. CATEGORY B TURNOVER TAX (if applicable)
  D1. Annual gross sales                         ___________
  D2. Turnover-tax rate ____%                     ___________
  D3. Turnover tax = D1 × D2                      ___________

REVIEWER FLAGS:
  [ ] Residence status confirmed?
  [ ] Citizenship confirmed (pension obligation)?
  [ ] Exempt allowances identified & limits checked?
  [ ] Pension ceiling (ETB 15,000?) confirmed?
  [ ] Category A vs B confirmed (turnover, profession, VAT)?
  [ ] Schedule C vs gross sales tax confirmed?
  [ ] MAT recomputed and compared?
  [ ] Schedule D rates confirmed (if investment income)?
  [ ] Quick-calc deductions reconciled to cumulative tax?
```

### Section 8 -- Bank Statement Reading Guide

#### Ethiopian Statement Formats

**Ethiopian Statement Formats table**

| Provider | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| CBE | PDF, SMS | Date, Description, Debit, Credit, Balance | Dual Ethiopian/Gregorian dates common |
| Awash / Dashen / Abyssinia | PDF | Date, Particulars, Withdrawal, Deposit, Balance | Counterparty in particulars |
| telebirr | PDF/in-app | Date, Type, Counterparty, Amount, Status | Clean merchant names; receive vs send |
| M-PESA Ethiopia | PDF/SMS | Date, Details, Paid In, Withdrawn, Balance | Mobile-money |

#### Key Amharic / Local Terms

**Key Amharic Local Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| ደሞዝ / DEMOZ | Salary | Employment income (PAYE) |
| አበል / ABEL | Allowance | Taxable unless exempt, flag |
| ኪራይ / KIRAY | Rent | Rental income (Schedule B) or premises expense |
| ግብር / GIBIR | Tax | Tax payment, not deductible |
| ጡረታ / TURETA | Pension | Pension contribution |
| ወለድ / WELED | Interest | Investment income (Schedule D) or bank charge |
| ኮሚሽን / COMMISSION | Bank fee | Deductible (business account) |

### Section 9 -- Onboarding Fallback

If the client provides records but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING, reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present these questions:

```
ONBOARDING QUESTIONS, ETHIOPIA INCOME TAX
1. Income type: employment, business (sole proprietor), or rental?
2. Residence: resident (worldwide income) or non-resident (Ethiopian-source)?
3. Citizenship: Ethiopian or foreign? (determines pension obligation)
4. For employment: gross salary breakdown, basic vs each allowance?
5. For business: annual turnover? Are you a listed professional? VAT-registered?
6. For business: do you keep full books (Schedule C) or expect gross sales tax?
7. Pension: is 7% already deducted? Any salary above ETB 15,000/month?
8. Any investment income (dividends, interest, royalties)? (Schedule D)
9. Any advance-tax payments made this fiscal year?
10. Any capital asset disposals (capital gains)?
```

### Section 10 -- Reference Material

#### Key Legislation & Authorities

**Key Legislation and Authorities table**

| Topic | Reference |
| --- | --- |
| Income tax (base) | Income Tax Proclamation No. 979/2016 |
| Income tax (amendment) | Income Tax (Amendment) Proclamation No. 1395/2025 (eff. 8 Jul 2025) |
| Tax administration / penalties | Tax Administration Proclamation No. 983/2016 |
| VAT | VAT Proclamation No. 1341/2024 + Regulation 570/2025 |
| Pension | Private Organizations Employees' Pension law (the pension fund administration) |
| Tax authority | Ministry of Revenues (MOR), `mor.gov.et` |
| Finance ministry | `mofed.gov.et` |
| Legislative text | Federal Negarit Gazeta |

#### Sources Consulted

- EY / haymanotbelay.com, VAT Proclamation 1341/2024

#### Items NOT Verified in This Build (do not assert)

1. PAYE quick-calc deduction constants, derived (correct math), not published verbatim.
2. ETB 15,000 pension salary ceiling, secondary sources only.
3. Schedule D withholding rates (dividends/interest/royalties).
4. Exact penalty/interest figures (Proclamation 983/2016).
5. Civil-servant minimum wage (ETB 4,800), note: Ethiopia has NO statutory private-sector minimum wage. Source: minimum-wage.org/international/ethiopia.

#### Test Suite

**Test 1, Low earner PAYE.**
Input: gross taxable salary 3,000/month.
Expected: PAYE = 3,000×0.15 − 300 = 150. Pension 210. Net 2,640.

**Test 2, Mid earner PAYE.**
Input: 6,000/month.
Expected: PAYE = 6,000×0.20 − 500 = 700. Pension 420. Net 4,880.

**Test 3, Upper-mid PAYE.**
Input: 12,000/month.
Expected: PAYE = 12,000×0.30 − 1,350 = 2,250. Pension 840. Net 8,910.

**Test 4, Top-band PAYE (no ceiling).**
Input: 20,000/month, no pension cap.
Expected: PAYE = 20,000×0.35 − 2,050 = 4,950. Pension 1,400. Net 13,650.

**Test 5, Exempt earner.**
Input: 2,000/month.
Expected: PAYE = 0. Pension 140. Net 1,860.

**Test 6, Schedule C with MAT check.**
Input: annual taxable business income 200,000, turnover 600,000.
Expected: income tax = 34,200 + (32,000×0.35=11,200) = 45,400. MAT = 2.5%×600,000 = 15,000. Tax due = max(45,400, 15,000) = 45,400.

**Test 7, Category B gross sales tax.**
Input: non-professional, non-VAT, annual gross sales 400,000.
Expected: 400,000 falls in 100,001–500,000 band → 3% × 400,000 = 12,000.

**Test 8, Pension total check.**
Input: employee 7% + employer 11%.
Expected: total = 18%.

### PROHIBITIONS

- NEVER use the obsolete pre-2025 PAYE deductions (60 / 142.50 / 302.50 / 565 / 955 / 1,500)
- NEVER assert the PAYE quick-calc deductions as authoritative without the (not confirmed) caveat
- NEVER assert the ETB 15,000 pension ceiling as confirmed, flag it
- NEVER state Schedule D (dividend/interest/royalty) rates without confirmation
- NEVER state specific penalty or interest figures, they are unverified
- NEVER apply pension contributions to a foreign national without confirming Ethiopian-origin status
- NEVER apply worldwide-income scope without confirming residence
- NEVER treat all allowances as taxable without flagging the exempt-allowance question
- NEVER skip the MAT comparison for business income
- NEVER present tax calculations as definitive, always label as estimated, pending reviewer sign-off
- NEVER confuse the Ethiopian fiscal year (8 Jul – 7 Jul) with a calendar year

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
