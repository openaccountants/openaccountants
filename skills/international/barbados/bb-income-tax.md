---
name: barbados-income-tax
description: Use this skill whenever asked about Barbados personal income tax, NIS contributions, or payroll obligations. Trigger on phrases like "how much tax do I pay in Barbados", "BRA", "Barbados Revenue Authority", "TAMIS", "PAYE Barbados", "NIS contributions", "National Insurance Barbados", "self-employed tax Barbados", "Reverse Tax Credit", "quarterly prepayments", "PIT return", "VAT registration Barbados", or any question about filing or computing income tax for a resident, non-resident, employed, or self-employed individual in Barbados. Also trigger when computing NIS contributions, applying personal allowances, checking filing deadlines, or advising on the Barbados Reverse Tax Credit. This skill covers PIT brackets, NIS rates, personal allowances, PAYE, self-assessment, quarterly prepayments, VAT registration thresholds, penalties, and withholding taxes. ALWAYS read this skill before touching any Barbados income tax or payroll work.
jurisdiction: BB
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# barbados-income-tax

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference table**  _(Source: PwC Worldwide Tax Summaries — Barbados Individual (reviewed 11 January 2026), https://taxsummaries.pwc.com/barbados/individual/taxes-on-personal-income; BRA — https://bra.gov.bb)_

| Field | Value |
| --- | --- |
| Country | Barbados |
| Tax | Personal Income Tax (PIT) |
| Currency | Barbados Dollar (BBD). Fixed peg: 1 USD = 2 BBD. |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act, Cap. 73 |
| Supporting legislation | National Insurance and Social Security Act, Cap. 47; Value Added Tax Act, Cap. 87; Minimum Wage (National and Sectoral Minimum Wage) (No. 2) Order, 2025 |
| Tax authority | Barbados Revenue Authority (BRA) — https://bra.gov.bb |
| Social security authority | National Insurance and Social Security Service (NISSS) — https://www.nis.gov.bb |
| Filing portal | TAMIS — https://tamis.bra.gov.bb |
| Filing deadline | 30 April of the following year |
| Validated by | Pending — requires sign-off by a Barbados-licensed accountant or tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

### PIT Rate Brackets (effective 1 January 2020; confirmed current as of 11 January 2026)

**PIT Rate Brackets**  _(Source: PwC Worldwide Tax Summaries — Barbados Individual, https://taxsummaries.pwc.com/barbados/individual/taxes-on-personal-income)_

| Taxable Income (BBD) | Rate | Cumulative Tax at Top of Band |
| --- | --- | --- |
| 0 -- 50,000 | 12.5% | BBD 6,250 |
| Above 50,000 | 28.5% | -- |

- **No zero-rate band** — There is no zero-rate band. The personal allowance (see Section 1 below) is subtracted first; the residual taxable income falls into these two brackets.  _(Source: PwC Worldwide Tax Summaries — Barbados Individual, https://taxsummaries.pwc.com/barbados/individual/taxes-on-personal-income)_

### Personal Allowances (deducted before applying rate brackets)

**Personal Allowances**  _(Source: PwC Worldwide Tax Summaries — Barbados Individual (Deductions), https://taxsummaries.pwc.com/barbados/individual/deductions)_

| Allowance | BBD | Notes |
| --- | --- | --- |
| Standard individual allowance | 25,000 | All residents |
| Individual aged 60+ receiving a pension | 40,000 | Replaces standard allowance |
| Spouse with no income (fully supported or cohabitant) | 3,000 | Additional allowance for taxpayer |

- **Non-resident allowance restriction** — Non-residents are not entitled to any personal allowances.  _(Source: PwC Worldwide Tax Summaries — Barbados Individual (Deductions), https://taxsummaries.pwc.com/barbados/individual/deductions)_

### Special Flat Rates

**Special Flat Rates**  _(Source: PwC Worldwide Tax Summaries — Barbados Individual (Income Determination), https://taxsummaries.pwc.com/barbados/individual/income-determination)_

| Income Type | Rate | Notes |
| --- | --- | --- |
| Residential rental income | 15% flat | Applied to gross rental receipts |
| Local interest income (> BBD 100) | 15% WHT at source | Final tax — do not re-report on PIT return |
| Local dividends (declared after 30 June 1992) | 15% WHT at source | Final tax — do not re-report on PIT return |
| 50% of royalty income | Exempt | Remaining 50% taxed at marginal rates |
| Capital gains | 0% | Barbados has no capital gains tax |

### NIS Contributions -- Private Sector Employee (Rates effective 1 April 2025)

**NIS Contributions -- Private Sector Employee**  _(Source: NIS Contribution Rates (official) — https://www.nis.gov.bb/contribution-rates/; KPMG Flash Alert 2024-255 — https://kpmg.com/xx/en/our-insights/gms-flash-alert/flash-alert-2024-255.html)_

| Branch | Employee | Employer |
| --- | --- | --- |
| National Insurance | 6.75% | 6.75% |
| Non-Contributory | 2.00% | 2.00% |
| Unemployment | 0.75% | 0.75% |
| Employment Injury | — | 0.75% |
| Severance | — | 0.50% |
| Training Levy | 0.50% | 0.50% |
| Health Service | 1.00% | 1.50% |
| Resilience & Regeneration Fund | 0.25% | 0.25% |
| **TOTAL (component sum)** | **11.25%** | **13.00%** |

- **Employer NIS rate discrepancy note** — The component sum of employer contributions is 13.00%. Several published sources cite the employer headline as "12.75%", which would imply 0.25% less than the sum of components shown above. [RESEARCH GAP — reviewer to confirm whether the 12.75% or 13.00% employer figure is correct under current NIS legislation.] The combined rate cited by NISSS is 24.00% (employee 11.25% + employer 12.75% = 24.00%).  _(Source: NIS Contribution Rates (official) — https://www.nis.gov.bb/contribution-rates/; KPMG Flash Alert 2024-255 — https://kpmg.com/xx/en/our-insights/gms-flash-alert/flash-alert-2024-255.html)_

### NIS Contributions -- Self-Employed (Rates effective 1 April 2025)

**NIS Contributions -- Self-Employed**  _(Source: NIS Contribution Rates (official) — https://www.nis.gov.bb/contribution-rates/)_

| Branch | Rate |
| --- | --- |
| National Insurance | 13.50% |
| Non-Contributory | 2.00% |
| Training Levy | 0.50% |
| Health Service | 1.00% |
| Resilience & Regeneration Fund | 0.25% |
| **TOTAL** | **17.25%** |

### NIS Insurable Earnings Ceiling

**NIS Insurable Earnings Ceiling**  _(Source: https://www.nis.gov.bb/contribution-rates/; KPMG Flash Alert 2024-255 — https://kpmg.com/xx/en/our-insights/gms-flash-alert/flash-alert-2024-255.html)_

| Year | Weekly Maximum (BBD) | Monthly Maximum (BBD) |
| --- | --- | --- |
| 2023 | 1,182 | 5,120 |
| 2024 | 1,201 | 5,200 |
| 2025 | 1,219 | 5,280 |
| 2026 | 1,238 | 5,360 |

- **Ceiling application and age eligibility** — Contributions apply on insurable earnings up to the ceiling only. Age eligibility: 16 -- 67.  _(Source: https://www.nis.gov.bb/contribution-rates/; KPMG Flash Alert 2024-255 — https://kpmg.com/xx/en/our-insights/gms-flash-alert/flash-alert-2024-255.html)_

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP -- do not apply allowances or rates without confirming residency |
| Unknown age (60+ pension allowance) | Use standard allowance (BBD 25,000) |
| Unknown employment type (employed vs self-employed) | STOP -- NIS rates and payment schedule differ |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration status | Not VAT-registered |
| Unknown whether rental is residential vs commercial | Treat as commercial (marginal rates, not flat 15%) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of residency status (resident/non-resident), employment type (employed/self-employed/mixed), and age (for pension allowance).

**Recommended** -- all sales invoices, purchase receipts, NIS payment records (employer schedule or self-employed receipts), prior year PIT return or tax assessment, confirmation of other income sources (rental, interest, dividends).

**Ideal** -- complete income and expenditure account, payslips for the full year (employed), TAMIS prepayment confirmation receipts, employer PAYE certificates, VAT registration details if applicable.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This PIT return was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the wholly-and-exclusively test is met."

### Refusal Catalogue

- **R-BB-1** — Residency status unknown. "Residency determines whether worldwide income is taxable and whether personal allowances apply. This skill cannot compute tax without knowing whether the client is resident, non-domiciled resident, or non-resident. Please confirm before proceeding."
- **R-BB-2** — Non-resident client. "Non-residents are taxed only on Barbados-source income and are not entitled to personal allowances. Withholding tax rules apply to certain non-resident income. Escalate to a licensed Barbados tax practitioner."
- **R-BB-3** — Corporate or partnership structures. "This skill covers individuals (employed and self-employed). Corporate income tax and partnership taxation require separate analysis. Escalate to a licensed practitioner."
- **R-BB-4** — Capital gains. "Barbados has no capital gains tax. If the transaction is labelled as a capital gain but may be recharacterised as income (e.g., property trading), escalate to a licensed practitioner."
- **R-BB-5** — Arrears / BRA enforcement. "Client has outstanding tax arrears, penalty notices, or is subject to BRA enforcement action. The 1%/month compounding interest charge is severe. Do not advise. Escalate to a licensed Barbados tax practitioner immediately."
- **R-BB-6** — Expat / treaty claim. "Tax treaty benefits and expat tax positions require jurisdiction-specific analysis. Out of scope. Escalate to a licensed practitioner."
- **R-BB-7** — VAT return requested. "This skill covers personal income tax and NIS contributions only. For Barbados VAT, use the barbados-vat-return skill (if available) or escalate."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns**

| Pattern | PIT Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Gross business income | Assessable income | Include in self-employment gross |
| PROFESSIONAL FEES, CONSULTANCY FEE, INVOICE PAYMENT | Gross business income | Assessable income | Professional income |
| STRIPE PAYOUT, STRIPE TRANSFER | Gross business income | Assessable income | Platform payout -- match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Gross business income | Assessable income | Platform payout -- verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Gross business income | Assessable income | International platform payout |
| SALARY, WAGES, PAYROLL, EMPLOYER [name] | Employment income | Assessable income (PAYE deducted at source) | Gross salary; PAYE already withheld |
| RENT RECEIVED, RENTAL INCOME, TENANT PAYMENT | Rental income | 15% flat on gross (residential) | Do not mix with employment/self-employment |
| INTEREST, BANK INTEREST (local, > BBD 100) | WHT deducted at source | Final tax -- exclude from PIT return | 15% WHT already applied by paying institution |
| DIVIDEND, DIVIDENDS RECEIVED (local, post-Jun 1992) | WHT deducted at source | Final tax -- exclude from PIT return | 15% WHT already applied |
| ROYALTY, ROYALTIES | 50% exempt; 50% income | Only 50% of royalty is assessable | Flag for reviewer |
| NIS BENEFIT, SICKNESS BENEFIT, MATERNITY BENEFIT, PENSION NIS | Taxable income | Include as assessable income | NIS benefits are taxable in Barbados |
| BRA REFUND, TAX REFUND | EXCLUDE | Not income | Tax refund from prior year |
| GOVERNMENT GRANT, SMALL BUSINESS GRANT | Check nature | Capital grant = EXCLUDE; revenue grant = income | Flag for reviewer |

### 3.2 Expense Patterns (Debits on Bank Statement) -- Fully Deductible

**Fully Deductible Expense Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, COMMERCIAL RENT [business address] | Office rent | Deductible -- actual amount | Dedicated business premises only |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible -- actual amount |  |
| ACCOUNTANT, BOOKKEEPING, TAX PREPARATION, CPA FEES | Accountancy/tax fees | Deductible -- actual amount |  |
| LAWYER, LEGAL FEES, SOLICITOR (business) | Legal fees | Deductible -- actual amount | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible -- actual amount |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS, ADVERTISING | Marketing | Deductible -- actual amount |  |
| TRAINING, COURSE, SEMINAR, CPD, CONFERENCE | Training | Deductible -- actual amount | Must relate to current business |
| PROFESSIONAL BODY, ASSOCIATION FEE, ICAB, ICAEW | Professional subscriptions | Deductible -- actual amount |  |
| TRADE UNION, UNION DUES, NUPW | Trade union subscriptions | Deductible -- up to BBD 240/year | Cap applies per Income Tax Act |
| BANK CHARGE, BANK FEE, SERVICE FEE, MAINTENANCE FEE | Bank charges | Deductible -- actual amount | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE, PROCESSING FEE | Payment processing fees | Deductible -- actual amount |  |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Deductible if below capitalisation threshold | Recurring subscription = operating expense |
| CHARITABLE DONATION (registered, non-exempt charity) | Charitable donations | Up to 10% of assessable income | Spread over 5 years if income > BBD 1 million |
| CHARITABLE DONATION (exempt charity) | Charitable donations | Unlimited deduction | Confirm exempt status |
| MEDICAL EXAM (age 40+) | Preventive health | Deductible -- up to BBD 750/year | Annual exam; age 40+ only |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible -- actual amount | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible -- actual amount |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible -- actual amount |  |
| SOFTWARE LICENCE (perpetual, significant cost) | Capital item | Capitalise -- deduct over useful life | [RESEARCH GAP -- reviewer to confirm Barbados capitalisation threshold] |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities Patterns**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| BL&P, BARBADOS LIGHT, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| BWSL, WATER BILL, BARBADOS WATER | Water | T2 if home office | Business % only if home office |
| FLOW, DIGICEL, LIME, BROADBAND | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| DIGICEL MOBILE, FLOW MOBILE, PHONE BILL | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LIAT, CARIBBEAN AIRLINES, AMERICAN AIRLINES, FLIGHT | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, ACCOMMODATION, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| TAXI, ZR, MINIBUS, RIDESHARE | Local transport | Deductible if business purpose |  |
| FUEL, GAS STATION, ESSO, RUBIS, SHELL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINNER, LUNCH, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | [RESEARCH GAP -- confirm whether Barbados allows partial entertainment deduction; default = fully blocked] |
| GROCERIES, SUPERMARKET, MASSY, EMERALD, SUPER CENTRE | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY | Fines/penalties | NOT deductible | Public policy |
| BRA PAYMENT, INCOME TAX PAYMENT, PIT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |
| NIS EMPLOYEE CONTRIBUTION (employee's share) | NIS | NOT deductible for employee | Employer NIS is deductible for employer only |
| RENTAL ALLOWANCE (post-2014) | Housing allowance | NOT deductible | Abolished after income year 2014 |

### 3.7 Expense Patterns (Debits) -- Capital Items (depreciate over useful life)

**Capital Items**

| Pattern | Category | Notes |
| --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP, IPAD | Computer hardware | Capitalise -- depreciate over useful life |
| PRINTER, SCANNER, COPIER | Office equipment | Capitalise -- depreciate over useful life |
| FURNITURE, DESK, CHAIR, FILING CABINET | Furniture/fittings | Capitalise -- depreciate over useful life |
| VEHICLE, CAR (business) | Motor vehicle | Capitalise -- depreciate over useful life; business % only |

[RESEARCH GAP -- reviewer to confirm Barbados capital allowance rates (straight-line percentages by asset class) under the Income Tax Act, Cap. 73.]

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, PERSONAL LOAN | EXCLUDE | Loan principal movement |
| VAT PAYMENT, BRA VAT | EXCLUDE | VAT liability payment, not expense |
| INCOME TAX PREPAYMENT, BRA PREPAYMENT | Prepayment | Credit against PIT liability; not an expense |
| NIS CONTRIBUTION (employer remittance line) | NIS cost | Deductible for employer; separate from PIT |

### 3.9 Barbados Bank Statement Format Reference

**Bank Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Scotiabank Barbados | TRANSFER, DD, BILL PAYMENT, CHARGES | PDF/CSV; date format DD/MM/YYYY |
| CIBC FirstCaribbean | PAYMENT, TRF, CARD, FEE | PDF; counterparty in description field |
| Republic Bank Barbados | TRANSFER, DEBIT CARD, ONLINE PAYMENT | PDF/CSV |
| Sagicor Bank | TRANSFER, DEBIT, CARD PURCHASE | PDF |
| Bitt / other fintechs | PAYMENT, PAYOUT | CSV; may be BBD or USD |

### 3.10 Barbados Banking Terms

**Barbados Banking Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| CREDIT / CR | Credit to account | Potential income |
| DEBIT / DR | Debit from account | Potential expense |
| DD / DIRECT DEBIT | Direct debit | Regular expense (utility, subscription) |
| ZR / TRANSPORT | Minibus fare | Local transport |
| CAIPO | Corporate Affairs & IP Office | Registration fees -- possibly capital |
| BRA | Barbados Revenue Authority | Tax payment -- not deductible |
| NIS | National Insurance | Contribution remittance |
| FLOW / DIGICEL | Telecommunications providers | Phone/internet -- T2 apportionment |

## Section 4 -- Worked Examples

### Example 1 -- Salaried Employee, Standard Allowance

**Scenario:** Single resident employee, gross salary BBD 60,000 for 2025. PAYE deducted by employer throughout the year. No other income.

**Computation:**
```
Gross salary:               BBD 60,000
Less personal allowance:   (BBD 25,000)
Taxable income:             BBD 35,000

Tax:
  BBD 35,000 × 12.5%  =    BBD  4,375

Total PIT liability:        BBD  4,375
```

**Bank statement lines might include:**
```
15/01/2025  CIBC FIRSTCARIBBEAN  PAYROLL EMPLOYER XYZ LTD  +4,850.00  BBD
15/02/2025  CIBC FIRSTCARIBBEAN  PAYROLL EMPLOYER XYZ LTD  +4,850.00  BBD
```
(Monthly net after PAYE withheld at source.)

**Classification:** Employment income. PAYE withheld by employer monthly and remitted to BRA by the 15th of the following month (BRA — https://bra.gov.bb/Popular-Topics/Employing-People/Guide-to-PAYE). If total PAYE withheld equals liability, no balance due on 30 April.

### Example 2 -- Higher-Income Employee, Two Brackets

**Scenario:** Single resident, gross salary BBD 100,000 for 2025.

**Computation:**
```
Gross salary:               BBD 100,000
Less personal allowance:   (BBD  25,000)
Taxable income:             BBD  75,000

Tax:
  BBD 50,000 × 12.5%  =    BBD  6,250
  BBD 25,000 × 28.5%  =    BBD  7,125

Total PIT liability:        BBD 13,375
```

Source: PwC Worldwide Tax Summaries — Barbados Individual, https://taxsummaries.pwc.com/barbados/individual/taxes-on-personal-income

### Example 3 -- Self-Employed, NIS + PIT

**Scenario:** Self-employed consultant, resident, single, 45 years old. Gross professional fees BBD 80,000. Allowable business expenses BBD 12,000. Tax year 2025.

**PIT computation:**
```
Gross professional income:  BBD 80,000
Less allowable expenses:   (BBD 12,000)
Net self-employment profit: BBD 68,000
Less personal allowance:   (BBD 25,000)
Taxable income:             BBD 43,000

Tax:
  BBD 43,000 × 12.5%  =    BBD  5,375

PIT liability:              BBD  5,375
```

**NIS computation (self-employed, 2025 rates):**
```
2025 insurable earnings ceiling: BBD 5,280/month × 12 = BBD 63,360/year
NIS insurable earnings (lower of net profit BBD 68,000 and ceiling BBD 63,360):
  = BBD 63,360
NIS rate (self-employed, effective 1 April 2025): 17.25%
NIS contribution: BBD 63,360 × 17.25% = BBD 10,929.60
```

**Payment schedule (self-employed):**
```
15 June 2025:      1st prepayment = 25% × prior year PIT
15 September 2025: 2nd prepayment = 25% × prior year PIT
15 December 2025:  3rd prepayment = 25% × prior year PIT
30 April 2026:     Balance of PIT due + NIS due by 15 January 2026
```

Source: PwC Tax Administration — https://taxsummaries.pwc.com/barbados/individual/tax-administration; NIS — https://www.nis.gov.bb/contribution-rates/

### Example 4 -- Minimum Wage Earner, Zero PIT

**Scenario:** Full-time worker at new minimum wage BBD 10.50/hour, 40 hours/week, full year 2025.

**Computation:**
```
Annual gross: BBD 10.50 × 40 hrs × 52 weeks = BBD 21,840
Less personal allowance:                      (BBD 25,000)
Taxable income:                                BBD 0 (negative -- clamp to zero)

PIT liability: BBD 0
```

**Note:** A full-time minimum-wage employee has zero income tax liability because gross earnings (BBD 21,840) fall below the personal allowance (BBD 25,000). (Minimum Wage (National and Sectoral Minimum Wage) (No. 2) Order, 2025 — https://barbadostoday.bb/2025/05/01/minimum-wage-increase-to-kick-in-on-june-1/)

**Reverse Tax Credit eligibility check:**
- Income ≤ BBD 25,000 ✓
- Employed (not self-employed) ✓
- Worked ≥ 4 months ✓
- Earned ≥ BBD 1,000/month (BBD 10.50 × 40 hrs × 4.33 wks ≈ BBD 1,819/month) ✓
- Income tax paid < BBD 500 (paid BBD 0) ✓
→ **Eligible for Reverse Tax Credit up to BBD 1,300.** (BRA — https://bra.gov.bb/Credits-Rebates/Reverse-Tax-Credit)

### Example 5 -- Pensioner Aged 60+, Higher Allowance

**Scenario:** Resident retiree, 65 years old, receiving a pension of BBD 36,000/year plus bank interest of BBD 500 (15% WHT already deducted at source).

**Computation:**
```
Pension income:              BBD 36,000
Bank interest:               EXCLUDE (15% WHT final tax; > BBD 100)
Less personal allowance
  (aged 60+ receiving pension): (BBD 40,000)
Taxable income:              BBD 0 (negative -- clamp to zero)

PIT liability: BBD 0
```

Source: PwC Deductions — https://taxsummaries.pwc.com/barbados/individual/deductions

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`22/03/2025  SCOTIABANK  OWN TRANSFER TO SAVINGS  -5,000.00  BBD`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency Rules

- **Residency determination test** — A person is resident in Barbados if present for more than 182 days in the calendar year (arrival and departure both count), OR if "ordinarily resident" (has permanent accommodation available and has notified the Revenue Commissioner of intent to reside for at least 2 consecutive years).  _(Legislation: Income Tax Act, Cap. 73)_

**Residency status taxation table**  _(Source: PwC Residence — https://taxsummaries.pwc.com/barbados/individual/residence)_

| Status | Taxed on |
| --- | --- |
| Resident + domiciled | Worldwide income |
| Resident + non-domiciled | Barbados-source income + foreign income where benefits are received in Barbados |
| Non-resident | Barbados-source income only; no personal allowances |

### 5.2 Income Inclusion Rules

All assessable income is reported on the PIT return filed via TAMIS. Key rules:

- **Employment income** (salaries, wages, bonuses, commissions, NIS benefits received) is assessable.
- **Self-employment income** is gross receipts minus allowable deductions.
- **Residential rental income** is taxed at 15% flat on gross receipts (not net of expenses). Do not mix with other income lines.
- **Local interest > BBD 100** — 15% WHT is a final tax; exclude from PIT return.
- **Local dividends** (post-30 June 1992) — 15% WHT is a final tax; exclude from PIT return.
- **Royalties** — 50% exempt; include only the other 50% as assessable income.
- **Capital gains** — none; Barbados has no capital gains tax.

Source: PwC Income Determination — https://taxsummaries.pwc.com/barbados/individual/income-determination

### 5.3 Allowable Deductions

- **Wholly and exclusively test** — An expense is deductible if incurred wholly and exclusively in the production of assessable income. Mixed-use expenses must be apportioned.  _(Income Tax Act; PwC Deductions — https://taxsummaries.pwc.com/barbados/individual/deductions)_

**Key deduction caps**  _(Income Tax Act; PwC Deductions — https://taxsummaries.pwc.com/barbados/individual/deductions)_

| Item | Cap |
| --- | --- |
| Trade union subscriptions | BBD 240/year |
| Annual medical exam (age 40+) | BBD 750/year |
| Renewable energy audit / electrical retrofitting | 150% of cost, up to BBD 10,000/year (5-year window) |
| Investment in employer shares (bonus converted) | Lesser of 75% of bonus or BBD 7,500 (5-year lock-up) |
| Charitable donations (registered, non-exempt charity) | Up to 10% of assessable income |
| Charitable donations (exempt charity) | Unlimited |

- **Not deductible items** — NOT deductible: Employee NIS contributions; motor vehicle depreciation (unless business use documented); rental allowances (abolished after income year 2014); fines and penalties; income tax itself.  _(Income Tax Act; PwC Deductions — https://taxsummaries.pwc.com/barbados/individual/deductions)_

### 5.4 PAYE Rules

- **PAYE thresholds and process** — PAYE applies to employees earning more than BBD 481/week or BBD 2,083/month. Employer uses tax codes (e.g., "250W" weekly, "250M" monthly) based on declared allowances. Employer remits PAYE to BRA by the 15th of the following month via TAMIS. Monthly filing via TAMIS using the PAYE Upload Template (Excel). NIS benefits received (sickness, maternity, pension, unemployment) are taxable income for the employee.  _(BRA — https://bra.gov.bb/Popular-Topics/Employing-People/Guide-to-PAYE)_

### 5.5 Self-Employment Filing Rules

- **Who must file, registration, filing** — Who must file — all self-employed persons regardless of income level; any individual with assessable income > BBD 25,000 from employment; pensioners aged 60+ with income > BBD 45,000. Registration — obtain a 13-digit TIN via TAMIS. Sole traders must also complete Form A47:146 and file with a CAIPO Certificate of Registration. Filing — PIT return filed electronically via TAMIS by 30 April each year for the preceding calendar year.  _(BRA — https://bra.gov.bb/About/Services/Registration/Sole-Traders-Partnerships; BRA — https://bra.gov.bb/Popular-Topics/Self-Employment/Filing-Your-Tax-Return)_

### 5.6 Payment Schedules

**Self-employed / >25% business or rental income schedule**  _(Source: PwC Tax Administration — https://taxsummaries.pwc.com/barbados/individual/tax-administration)_

| Instalment | Due Date | Amount |
| --- | --- | --- |
| 1st prepayment | 15 June | 25% of prior year PIT liability |
| 2nd prepayment | 15 September | 25% of prior year PIT liability |
| 3rd prepayment | 15 December | 25% of prior year PIT liability |
| Balance | 30 April | Remainder after prepayments |

*First-year self-employed person: request BRA set an appropriate prepayment amount.*

**Salaried taxpayers with less than 25% from business schedule**  _(Source: PwC Tax Administration — https://taxsummaries.pwc.com/barbados/individual/tax-administration)_

| Payment | Due Date | Amount |
| --- | --- | --- |
| First payment | 30 April | 50% of tax due |
| Second payment | 30 September | 50% of tax due |

### 5.7 NIS Contribution Rules

- **NIS contribution rules** — NIS contributions apply to insurable earnings between zero and the annual ceiling (BBD 63,360 for 2025; BBD 64,320 for 2026). Age eligibility: 16 -- 67. Employee NIS contributions are not deductible from assessable income for PIT purposes. Employer NIS contributions are a business expense. Employer remittance deadline: 15th day of the following month. Self-employed payment deadline: 15 January of the following year (instalments throughout the year permitted). Government permanent employees ("P" category) have different rates: no unemployment or severance levy (see Quick Reference).  _(Legislation: National Insurance and Social Security Act, Cap. 47; NIS — https://www.nis.gov.bb/contribution-rates/)_

### 5.8 Reverse Tax Credit (RTC)

- **Reverse Tax Credit rules** — Refundable credit for low-income employed residents. Self-employed persons are not eligible. Amount: up to BBD 1,300 (equivalent to NIS contributions paid). Eligibility: resident in Barbados; annual income ≤ BBD 25,000 (≤ BBD 2,083.33/month); worked minimum 4 months in the income year; earned at least BBD 1,000/month or BBD 250/week; paid less than BBD 500 in income tax. Directors and persons receiving income from goods/services are excluded. Filing window: within 2 years of the relevant income year. Claimed via TAMIS as a "Reverse Tax Credit" return type.  _(BRA — https://bra.gov.bb/Credits-Rebates/Reverse-Tax-Credit)_

### 5.9 VAT Registration

- **Mandatory VAT registration threshold** — BBD 200,000 in taxable supplies in any 12-month period, or > BBD 16,666.67/month  _(Value Added Tax Act, Cap. 87; BRA — https://bra.gov.bb/Popular-Topics/Value-Added-Tax/Who-Must-Register-for-VAT)_
- **VAT registration details** — Voluntary registration permitted below threshold. Registration deadline: within 21 days of exceeding the threshold, via TAMIS. Standard VAT rate: 17.5%. Also applies to promoters of public entertainment regardless of turnover.  _(Value Added Tax Act, Cap. 87; BRA — https://bra.gov.bb/Popular-Topics/Value-Added-Tax/Who-Must-Register-for-VAT)_

### 5.10 Non-Resident Withholding Taxes

**Non-Resident Withholding Taxes**  _(Source: PwC Withholding Taxes — https://taxsummaries.pwc.com/barbados/corporate/withholding-taxes)_

| Payment Type | Rate | Notes |
| --- | --- | --- |
| Dividends (from non-foreign-source income) | 15% |  |
| Dividends (from untaxed profits) | 25% |  |
| Dividends (from foreign-source income, to non-resident shareholders) | Nil |  |
| Interest to non-residents (effective 1 April 2019) | Nil |  |
| Royalties to non-residents (effective 1 April 2019) | Nil |  |

### 5.11 Penalties and Interest

**Penalties and Interest**  _(Source: PwC Tax Administration — https://taxsummaries.pwc.com/barbados/individual/tax-administration; BRA Income Tax FAQs — https://bra.gov.bb/FAQs/Income-Tax/)_

| Infraction | Penalty |
| --- | --- |
| Late filing of PIT return | BBD 500 + 5% of tax assessed at due date |
| Late payment of tax | 5% of unpaid tax at due date |
| Interest on outstanding tax + penalties | 1% per month (compounding) |

### 5.12 Other Levies

- **Stamp Duty** — Real estate, leases, private company shares: BBD 10 per BBD 1,000 (or part thereof) of value. Mortgages: BBD 3 per BBD 500 (or part thereof). Listed shares: exempt.  _(Income Tax Act / Stamp Duty Act; PwC Other Taxes — https://taxsummaries.pwc.com/barbados/individual/other-taxes)_
- **Training Levy** — Collected via NIS system. Rate: 0.50% each (employee + employer) = 1.00% combined, applied to insurable earnings. Self-employed pay 0.50%.  _(NIS — https://www.nis.gov.bb/contribution-rates/)_
- **Resilience and Regeneration Fund** — Effective 1 April 2025, employee rate 0.25%; employer rate 0.25%; self-employed 0.25%. Applied to gross earnings (not capped at NIS ceiling). (Previously 0.10% employee, nil employer.)  _(PwC Other Taxes — https://taxsummaries.pwc.com/barbados/individual/other-taxes; NIS — https://www.nis.gov.bb/contribution-rates/)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home office deduction rules** — Calculate proportion of home used for business: dedicated room(s) as percentage of total rooms or floor area. Apply that percentage to: rent or mortgage interest, electricity, water, internet, maintenance. Must be a dedicated workspace — a dual-use room (kitchen table, dining room) does NOT qualify. Client must document the calculation and retain records. Conservative default: 0% deduction until reviewer confirms room arrangement. Flag for reviewer: Confirm room count, floor area basis, and that workspace is genuinely dedicated.  _(Legislation: Income Tax Act, Cap. 73)_

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use rules** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Client must maintain a mileage log (business trips vs total mileage). Capital allowance: depreciate over useful life, multiplied by business %. [RESEARCH GAP — reviewer to confirm Barbados capital allowance rates by asset class.] Conservative default: 0% business use until mileage log provided.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use rules** — Business use portion only is deductible. Client must provide a reasonable estimate of business vs personal use. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 Rental Income -- Residential vs Commercial

- **Rental income treatment rules** — Residential rental: 15% flat on gross receipts. No expense deductions allowed against the flat-rate levy. Commercial rental: Include in assessable income at marginal PIT rates; business expenses may be deductible. Flag for reviewer: Confirm whether property is residential or commercial. [RESEARCH GAP — reviewer to confirm the interaction between the 15% flat rental levy and any allowable expense deductions under current BRA practice.]

### 6.5 Royalty Income Split

- **Royalty income split rule** — 50% of royalty income is exempt; only 50% is assessable. Flag for reviewer: Confirm the income is genuinely a royalty (not a fee for service).

### 6.6 Renewable Energy Deduction

- **Renewable energy deduction rule** — A 150% deduction (up to BBD 10,000/year) applies to renewable energy audits and electrical retrofitting costs within a 5-year window. Flag for reviewer: Confirm expenditure qualifies under the relevant provision and the 5-year window has not expired.

### 6.7 Bad Debt Write-Off

- **Bad debt write-off conditions** — Deductible only if: (1) income was previously declared, (2) all reasonable recovery steps taken, (3) debt is genuinely irrecoverable. Flag for reviewer to confirm all three conditions.

### 6.8 NIS Employer Contribution Rate Discrepancy

- **NIS employer rate discrepancy flag** — The component-by-component sum of employer NIS branches yields 13.00%; published sources commonly cite 12.75%. Flag for reviewer: Confirm the applicable employer NIS rate with NIS directly or via current NIS legislation before computing payroll.

## Section 7 -- Excel Working Paper Template

```
BARBADOS PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident / Non-Domiciled Resident / Non-Resident
Employment type: Employed / Self-Employed / Mixed
Age: ______   Receiving pension? Y / N

A. EMPLOYMENT INCOME
  A1. Gross salary / wages                     ___________
  A2. Bonuses / commissions                    ___________
  A3. NIS benefits received (taxable)          ___________
  A4. TOTAL employment income                  ___________

B. SELF-EMPLOYMENT INCOME
  B1. Gross professional / business receipts   ___________
  B2. Less allowable expenses (detail below)   ___________
  B3. Net self-employment profit (B1 - B2)     ___________

  Expense detail:
    B2a. Office rent                           ___________
    B2b. Professional / legal fees             ___________
    B2c. Office supplies / stationery          ___________
    B2d. Software subscriptions                ___________
    B2e. Marketing / advertising               ___________
    B2f. Bank charges / payment fees           ___________
    B2g. Training / CPD / professional subs    ___________
    B2h. Travel (flights, hotel, local)        ___________
    B2i. Telecoms (business %)                 ___________
    B2j. Home office (% of utilities/rent)     ___________
    B2k. Vehicle expenses (business %)         ___________
    B2l. Charitable donations (capped 10%)     ___________
    B2m. Trade union subscriptions (max 240)   ___________
    B2n. Annual medical exam (40+; max 750)    ___________
    B2o. Renewable energy costs (150% / 10k)  ___________
    B2p. Other allowable expenses              ___________
    B2q. TOTAL expenses                        ___________

C. RENTAL INCOME
  C1. Residential rental (gross)               ___________
  C2. Rental tax @ 15% flat (C1 × 15%)        ___________
  C3. Commercial rental (net, if any)          ___________

D. OTHER INCOME (excluded items -- final WHT)
  D1. Local interest (15% WHT applied)         EXCLUDED
  D2. Local dividends (15% WHT applied)        EXCLUDED
  D3. Royalties (50% exempt; 50% below)        ___________

E. ASSESSABLE INCOME
  E1. Employment income (A4)                   ___________
  E2. Net self-employment (B3)                 ___________
  E3. Commercial rental (C3)                   ___________
  E4. 50% of royalties (D3 / 2)               ___________
  E5. TOTAL assessable income                  ___________

F. PERSONAL ALLOWANCE
  F1. Standard allowance                       25,000
      OR aged 60+ with pension                 40,000
  F2. Spouse allowance (if applicable)          3,000
  F3. TOTAL allowances                         ___________

G. TAXABLE INCOME (E5 - F3; minimum zero)      ___________

H. PIT COMPUTATION
  H1. First BBD 50,000 of G × 12.5%           ___________
  H2. Amount of G above BBD 50,000 × 28.5%    ___________
  H3. GROSS PIT LIABILITY (H1 + H2)            ___________

I. CREDITS AND PREPAYMENTS
  I1. Reverse Tax Credit (employed, low income) ___________
  I2. Prepayments (quarterly / salaried)        ___________
  I3. PAYE withheld by employer                 ___________
  I4. TOTAL credits (I1 + I2 + I3)             ___________

J. NET PIT DUE / REFUND (H3 - I4)             ___________

K. NIS CONTRIBUTIONS (if self-employed)
  K1. Insurable earnings (lower of E2 and ceiling) ___________
  K2. 2025 ceiling: BBD 63,360/year            ___________
  K3. NIS rate (self-employed): 17.25%         ___________
  K4. NIS due (K1 × K3)                        ___________

L. RESIDENTIAL RENTAL TAX
  L1. From C2 above                            ___________

REVIEWER FLAGS:
  [ ] Residency status confirmed?
  [ ] Age confirmed (for 40,000 pension allowance)?
  [ ] Residential vs commercial rental confirmed?
  [ ] Royalty income nature confirmed (royalty vs fee)?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] Capital items listed separately for depreciation?
  [ ] Employer NIS rate confirmed (13.00% vs 12.75% gap)?
  [ ] Reverse Tax Credit eligibility confirmed?
  [ ] All T2 items flagged for review?
  [ ] Entertainment expenses excluded?
  [ ] Tax payments excluded from expenses?
```

## Section 8 -- Bank Statement Reading Guide

### Barbados Bank Statement Formats

**Barbados Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Scotiabank Barbados | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description contains counterparty + reference |
| CIBC FirstCaribbean | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant name |
| Republic Bank Barbados | PDF, CSV | Date, Particulars, Withdrawals, Deposits | Shorter descriptions on PDF |
| Sagicor Bank | PDF | Date, Description, Debit, Credit | Less common CSV export |
| Bitt / fintechs | CSV | Date, Counterparty, Amount, Currency | Multi-currency possible; use BBD amounts |

### Key Barbados Banking and Business Terms

**Key Barbados Banking and Business Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| CR / CREDIT | Credit to account | Potential income |
| DR / DEBIT | Debit from account | Potential expense |
| DD / DIRECT DEBIT | Direct debit | Regular expense (utility, subscription) |
| ZR | Minibus (route taxi) | Local transport -- deductible if business |
| CAIPO | Corporate Affairs & IP Office | Registration fees |
| BRA | Barbados Revenue Authority | Tax payment -- not deductible |
| NIS | National Insurance | Contribution -- not deductible for employee |
| TAMIS | Tax Administration Management Information System | Filing/payment reference |
| FLOW | FLOW (C&W) telecom | Phone/internet -- T2 apportionment |
| DIGICEL | Digicel telecom | Phone/internet -- T2 apportionment |
| BL&P | Barbados Light & Power (now Emera Barbados) | Electricity -- T2 if home office |
| BWSL | Barbados Water Authority | Water -- T2 if home office |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm."
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- BARBADOS INCOME TAX
1. Residency: are you resident in Barbados for more than 182 days this year?
2. Domicile: are you domiciled in Barbados, or a non-domiciled resident?
3. Age: are you 60 or over and receiving a pension?
4. Employment type: employed, self-employed, or both?
5. Other income: do you receive rental income? If so, is the property residential or commercial?
6. Royalties: do you receive any royalty payments?
7. Home office: do you work from a dedicated room at home? If so, what percentage of floor area?
8. Vehicle: do you use a car for business? If yes, what percentage is business use? Do you keep a mileage log?
9. Phone/internet: what percentage is business use?
10. NIS (self-employed): total NIS contributions paid in the tax year?
11. Prepayments: did you make any quarterly income tax prepayments to BRA this year?
12. Spouse: do you fully support a spouse with no income?
13. Charitable donations: did you make any charitable donations?
14. Medical exam: if aged 40+, did you have an annual medical exam? Cost?
```

## Section 10 -- Reference Material

### Key Legislation and Authorities

**Key Legislation and Authorities**

| Topic | Reference |
| --- | --- |
| PIT rates | Income Tax Act, Cap. 73; PwC Worldwide Tax Summaries — Barbados Individual |
| Residency rules | Income Tax Act, Cap. 73; PwC — https://taxsummaries.pwc.com/barbados/individual/residence |
| Allowable deductions | Income Tax Act, Cap. 73, s.14 (comparable); PwC — https://taxsummaries.pwc.com/barbados/individual/deductions |
| PAYE | BRA — https://bra.gov.bb/Popular-Topics/Employing-People/Guide-to-PAYE |
| Self-employment filing | BRA — https://bra.gov.bb/Popular-Topics/Self-Employment/Filing-Your-Tax-Return |
| Self-assessment guide | BRA — https://bra.gov.bb/Popular-Topics/Self-Assessment-Self-Employment/Guide-to-Self-Assessment |
| NIS contribution rates | NISSS — https://www.nis.gov.bb/contribution-rates/ |
| NIS self-employed | NISSS — https://www.nis.gov.bb/self-employed/ |
| Reverse Tax Credit | BRA — https://bra.gov.bb/Credits-Rebates/Reverse-Tax-Credit |
| VAT registration | BRA — https://bra.gov.bb/Popular-Topics/Value-Added-Tax/Who-Must-Register-for-VAT |
| Penalties | PwC — https://taxsummaries.pwc.com/barbados/individual/tax-administration |
| Stamp duty | PwC Other Taxes — https://taxsummaries.pwc.com/barbados/individual/other-taxes |
| Minimum wage | Minimum Wage (National and Sectoral Minimum Wage) (No. 2) Order, 2025 |
| TAMIS portal | https://tamis.bra.gov.bb |
| TIN / sole trader registration | BRA — https://bra.gov.bb/About/Services/Registration/Sole-Traders-Partnerships |

### Key Dates Calendar

**Key Dates Calendar**  _(Source: PwC Tax Administration — https://taxsummaries.pwc.com/barbados/individual/tax-administration)_

| Date | Obligation |
| --- | --- |
| 15th of each month | Employer remits PAYE + NIS contributions to BRA/NIS |
| 15 January | Self-employed NIS contributions due for prior year |
| 30 April | PIT return filing deadline; balance of PIT due (all individuals); first payment (50%) for salaried taxpayers |
| 15 June | 1st quarterly income tax prepayment (self-employed / > 25% business income) |
| 30 September | 2nd payment (50% balance) for salaried taxpayers |
| 15 September | 2nd quarterly prepayment (self-employed) |
| 15 December | 3rd quarterly prepayment (self-employed) |

### Minimum Wage Reference

**Minimum Wage Reference**  _(Source: Minimum Wage (National and Sectoral Minimum Wage) (No. 2) Order, 2025; Barbados Today — https://barbadostoday.bb/2025/05/01/minimum-wage-increase-to-kick-in-on-june-1/; WageIndicator — https://wageindicator.org/salary/minimum-wage/barbados)_

| Period | Rate (BBD/hour) | Category |
| --- | --- | --- |
| Before 1 June 2025 | 8.50 | General |
| 1 June 2025 -- 20 January 2026 | 10.50 | General |
| 1 June 2025 -- 20 January 2026 | 11.43 | Security guards |
| From 21 January 2026 | 10.71 | General (2% CPI increase) |
| From 21 January 2026 | 11.66 | Security guards |

### Key Forms and Portals

**Key Forms and Portals**

| Item | Details |
| --- | --- |
| TAMIS portal | https://tamis.bra.gov.bb — file PIT, PAYE, VAT, RTC returns; make payments |
| PIT return | Filed electronically via TAMIS |
| Sole trader registration | Form A47:146 + CAIPO Certificate of Registration |
| PAYE monthly filing | PAYE Upload Template (Excel) via TAMIS |
| NIS employer contributions | Via NIS Portal or TAMIS |
| NIS self-employed payment | Via EZPay+, SurePay, or NIS Portal |

### Test Suite

**Test 1 -- Standard single employee, mid-range.**
Input: Single resident, gross salary BBD 45,000. No other income.
Expected: Taxable income = BBD 20,000 (45,000 − 25,000). PIT = BBD 2,500 (20,000 × 12.5%).

**Test 2 -- Pensioner aged 60+.**
Input: Resident, 63 years old, receiving pension BBD 55,000. No other income.
Expected: Taxable income = BBD 15,000 (55,000 − 40,000). PIT = BBD 1,875 (15,000 × 12.5%).

**Test 3 -- Self-employed, straddling both brackets.**
Input: Single resident, net self-employment profit BBD 90,000. No other income.
Expected: Taxable income = BBD 65,000 (90,000 − 25,000). PIT = BBD 50,000 × 12.5% + BBD 15,000 × 28.5% = BBD 6,250 + BBD 4,275 = BBD 10,525.

**Test 4 -- Self-employed NIS ceiling.**
Input: Self-employed resident, net earnings BBD 90,000, tax year 2025.
Expected: Insurable earnings capped at BBD 63,360 (= BBD 5,280/month × 12). NIS = BBD 63,360 × 17.25% = BBD 10,929.60.

**Test 5 -- Minimum wage, zero PIT.**
Input: Full-time employee at BBD 10.50/hour, 40 hours/week, 52 weeks.
Expected: Gross = BBD 21,840. Taxable income = 0 (below personal allowance of BBD 25,000). PIT = BBD 0. Reverse Tax Credit eligibility: confirm against Section 5.8 criteria.

**Test 6 -- Residential rental flat tax.**
Input: Resident, BBD 30,000 residential rental income (gross).
Expected: Rental tax = BBD 30,000 × 15% = BBD 4,500. This is a flat levy; rental income is NOT added to other income and taxed at marginal rates.

**Test 7 -- Local interest excluded.**
Input: BBD 2,000 bank interest, 15% WHT deducted at source.
Expected: EXCLUDE from PIT return — final tax already applied.

**Test 8 -- Royalty 50% exemption.**
Input: BBD 10,000 royalty income.
Expected: Assessable amount = BBD 5,000 (50% exempt). Add BBD 5,000 to assessable income; remainder is exempt.

**Test 9 -- Late filing penalty.**
Input: PIT return filed 60 days late. Tax assessed = BBD 8,000.
Expected: Fixed penalty BBD 500 + 5% of BBD 8,000 = BBD 400 = BBD 900 total initial penalty. Then 1%/month compounding on outstanding amounts from due date. (BRA FAQs — https://bra.gov.bb/FAQs/Income-Tax/)

## PROHIBITIONS

- NEVER apply personal allowances to a non-resident taxpayer
- NEVER include 15% WHT local interest or dividend income in the PIT return -- it is a final tax
- NEVER tax residential rental income at marginal PIT rates -- it is a 15% flat levy on gross receipts
- NEVER allow employee NIS contributions as a PIT deduction
- NEVER allow income tax payments as a business expense
- NEVER allow fines or penalties as a deduction
- NEVER allow rental allowances (abolished after income year 2014) as a deduction
- NEVER apply the 60+ pension allowance (BBD 40,000) without confirming both age and receipt of a pension
- NEVER compute self-employed NIS on earnings above the applicable annual ceiling
- NEVER apply the Reverse Tax Credit to a self-employed person
- NEVER omit the employer NIS rate research gap flag when computing payroll -- confirm the 12.75% vs 13.00% discrepancy with NIS before finalising
- NEVER present tax calculations as definitive -- always label as estimated and require professional sign-off before filing

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
