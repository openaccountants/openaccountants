---
name: nepal-income-tax
description: Use this skill whenever asked about Nepal income tax for natural persons (individuals and the self-employed). Trigger on phrases like "how much tax do I pay in Nepal", "Nepal income tax slabs", "D-01 return", "PAN income tax", "SSF contribution", "Social Security Fund", "presumptive tax Nepal", "turnover tax", "tax rate FY 2082/83", "natural person tax", "income tax return Nepal", "TDS Nepal", or any question about filing or computing income tax for a resident natural person, sole proprietor, or small business in Nepal. Also trigger when preparing or reviewing a D-01 return, computing the 1% Social Security Tax slab, applying the female-taxpayer rebate, or advising on advance/installment tax. This skill covers natural-person slabs (single/couple), the SST mechanism, SSF contributions, presumptive and turnover-based small-business regimes, deductions/rebates, filing deadlines, and penalties under the Income Tax Act, 2058. ALWAYS read this skill before touching any Nepal income tax work.
jurisdiction: NP
domain: income-tax
tax_year: 2025
reviewed_by: Ashish Bista
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# nepal-income-tax

## Nepal Income Tax -- Natural Persons Skill v0.1

> **Tier 2 — research-verified, pending accountant sign-off.** Figures below are drawn from the Income Tax Act, 2058 (2002), Inland Revenue Department (IRD) guidance, the Social Security Fund (SSF), and the PKF Trunco "Tax Rates for FY 2082-83 (2025-26)" publication. Items marked **[RESEARCH GAP — reviewer to confirm]** could not be locked to a primary source and MUST be confirmed by a Nepali tax professional before filing.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ashish Bista** on 2026-06-06.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Income Tax (Individuals)

- **First 500,000 — 1% (Social Security Tax) slab** — First 1,000,000 at 1%  _(Finance Act 2083)_
- **Next 200,000 (500,001–700,000) at 10% slab** — Next 500,000 (1,000,001–1,500,000) at 10%  _(Finance Act 2083)_
- **Next 300,000 (700,001–1,000,000) at 20% slab** — Next 1,000,000 (1,500,001–2,500,000) at 20%  _(Finance Act 2083)_
- **Next 1,000,000 (1,000,001–2,000,000) at 30% slab** — Next 1,500,000 (2,500,001–4,000,000) at 27%  _(Finance Act 2083)_
- **Next 3,000,000 (2,000,001–5,000,000) at 36% slab** — Above 4,000,000 at 29%  _(Finance Act 2083)_
- **Above 5,000,000 at 39% slab** — N/A — Top tier is now above NPR 4,000,000 at 29%; 39% rate eliminated.  _(Finance Act 2083)_
- **Resident individual — couple: First band at 1% threshold** — NPR 1,000,000 (uniform for all — separate couple slab structure removed)  _(Finance Act 2083)_
- **Resident individual — couple: Remaining bands** — Same as single: 10 / 20 / 27 / 29% — couple slabs eliminated; uniform rates apply.  _(Finance Act 2083)_
- **1% first-band SST — deposit account** — Deposited to separate IRD revenue account (code 11211)  _(IRD revenue codes (PKF/khatapana))_
- **SST exemptions** — Does NOT apply to sole proprietors, pension income, contribution-based pension fund income, or SSF contributors  _(PKF; Baker Tilly)_
- **Slabs unchanged from fiscal year reference** — FY 2083/84 (2026/27)  _(Finance Act 2083)_
- **Income year / fiscal year period** — Shrawan 1 – Ashad end (BS); FY 2083/84 ≈ mid-Jul 2026 – mid-Jul 2027  _(Income Tax Act 2058)_
- **Annual return / instalment due dates** — Advance tax instalments due: Poush end, Chaitra end, Ashad end; final annual return due: Ashwin end  _(Income Tax Act 2058 s. 94 & 96)_
- **Residency test** — 183 days or more in Nepal in any 365-day period  _(Income Tax Act 2058 s. 2(q))_

### _map

**_map**

| Skill | slug | version |
| --- | --- | --- |
| Income Tax (Individuals) | nepal-income-tax | 1.0 |
| Corporate Income Tax | nepal-corporate-tax | 1.0 |
| TDS (Withholding) | nepal-tds | 1.0 |
| Payroll (Salary TDS + SSF) | nepal-payroll | 1.0 |
| VAT (IRD Return) | nepal-vat | 2.1 |

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Nepal (Federal Democratic Republic of Nepal) |
| Tax | Income Tax (आयकर) on natural persons |
| Currency | NPR (Nepalese Rupee) only |
| Tax year | Bikram Sambat fiscal year: Shrawan 1 -- Ashad end (~mid-July to mid-July) |
| Current tax year | FY 2082/83 BS = 2025/26 AD (started ~17 July 2025) |
| Primary legislation | Income Tax Act, 2058 (2002) |
| Supporting rules | Contribution-Based Social Security Act (SSF); annual Finance/Budget Act (slabs); IRD circulars |
| Tax authority | Inland Revenue Department (IRD), ird.gov.np |
| Filing portal | taxpayerportal.ird.gov.np |
| Individual return form | D-01 (natural persons; also presumptive) |
| Filing deadline | Within 3 months of FY end → end of Ashoj (~mid-October); extendable +3 months to end of Poush (~mid-January) |
| Validated by | Pending — requires sign-off by a Nepali tax professional |
| Validation date | Verified by Ashish Bista (ICAN: 1765) on 2026-06-06 |
| Skill version | 0.1 |

### Tax Rate Slabs -- Natural Persons, FY 2082/83 (2025/26)

The **first-band rate of 1% is the Social Security Tax (SST)** — a flat, final levy paid into a separate SSF account. It is **not creditable** against other tax and is **waived for employees who contribute to the SSF** (see Section 5.2). The top rates are built by surcharging the 30% bracket: **36% = 30% × 1.20** and **39% = 30% × 1.30** (Income Tax Act mechanism; PKF Trunco FY2082-83).

**Single (individual)** — cumulative tax assumes the 1% SST applies (non-SSF taxpayer).

**Single (individual) slab table**  _(PKF Trunco "Tax Rates for FY 2082-83 (2025-26)"; notarynepal; fewalaw; taxadvisornepal.)_

| Taxable income band (NPR) | Width | Rate | Tax on band | Cumulative tax at top |
| --- | --- | --- | --- | --- |
| 0 -- 500,000 | 500,000 | 1% (SST) | 5,000 | 5,000 |
| 500,001 -- 700,000 | 200,000 | 10% | 20,000 | 25,000 |
| 700,001 -- 1,000,000 | 300,000 | 20% | 60,000 | 85,000 |
| 1,000,001 -- 2,000,000 | 1,000,000 | 30% | 300,000 | 385,000 |
| 2,000,001 -- 5,000,000 | 3,000,000 | 36% | 1,080,000 | 1,465,000 |
| 5,000,001+ | — | 39% | — | — |

**Married couple (electing couple assessment) slab table**  _(PKF Trunco "Tax Rates for FY 2082-83 (2025-26)"; notarynepal; fewalaw; taxadvisornepal.)_

| Taxable income band (NPR) | Width | Rate | Tax on band | Cumulative tax at top |
| --- | --- | --- | --- | --- |
| 0 -- 600,000 | 600,000 | 1% (SST) | 6,000 | 6,000 |
| 600,001 -- 800,000 | 200,000 | 10% | 20,000 | 26,000 |
| 800,001 -- 1,100,000 | 300,000 | 20% | 60,000 | 86,000 |
| 1,100,001 -- 2,000,000 | 900,000 | 30% | 270,000 | 356,000 |
| 2,000,001 -- 5,000,000 | 3,000,000 | 36% | 1,080,000 | 1,436,000 |
| 5,000,001+ | — | 39% | — | — |

> **SSF taxpayers:** Where the employee contributes to the SSF, the 1% SST band is waived. The first NPR 500,000 (single) / 600,000 (couple) is then effectively taxed at 0% for the income-tax computation, and progressive rates begin at the 10% band. Confirm SSF enrolment before deciding whether the 1% applies.

### D-01 Return -- Key Lines (natural person)

**D-01 Return key lines**

| Line | Description |
| --- | --- |
| Assessable income | Employment + business + investment income (Nepal-source for non-residents) |
| Less: approved retirement contribution | Lower of 1/3 of assessable income or NPR 500,000 |
| Less: life insurance premium | Up to NPR 40,000 |
| Less: health insurance premium | Up to NPR 20,000 |
| Less: donations | Up to 5% of adjusted taxable income or NPR 100,000 (lower) |
| Taxable income | Assessable income less allowable deductions |
| Tax per slab | From the single/couple slab table above |
| Less: female-taxpayer rebate | 10% of computed tax (resident women, employment income only) |
| Less: TDS / advance tax / installments | Credits against final liability |
| Tax payable / refund | Net of credits |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown assessment status (single vs couple) | STOP — do not apply a slab table without it |
| Unknown SSF enrolment | Assume NOT SSF-enrolled → apply 1% SST (more tax; reviewer confirms) |
| Unknown residency | Assume resident only if ≥183 days confirmed; else STOP (non-resident flat rate differs) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether female-rebate applies | Do NOT apply the 10% rebate until confirmed |
| Unknown small-business scheme eligibility | Normal-return slab rates (most conservative) |
| Senior-citizen extra exemption | Do NOT apply unless age 65+ confirmed |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — bank statement for the full fiscal year (Shrawan–Ashad) in CSV, PDF, or pasted text, plus confirmation of assessment status (single/couple), residency, and SSF enrolment.

**Recommended** — sales/purchase invoices, salary slips, SSF contribution statements, TDS certificates (E-TDS), PAN, prior-year D-01 or assessment, VAT registration status.

**Ideal** — complete income and expenditure statement, asset/depreciation register, advance/installment tax receipts, life/health insurance and donation receipts, senior-citizen / female-taxpayer status.

**Refusal if minimum is missing — SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This D-01 was produced from bank statement alone. The reviewer must verify that all deductions are supported by valid documentation and that business expenses meet the income-production test of the Income Tax Act, 2058."

### Refusal Catalogue

- **R-NP-1** — Assessment status unknown. "Single vs couple assessment changes the slab thresholds. This skill cannot compute tax without it. Please confirm before proceeding."
- **R-NP-2** — Companies / partnerships. "This skill covers resident natural persons and sole proprietors only. Private/public companies and partnership firms file separate returns at entity rates. Escalate to a Nepali tax professional."
- **R-NP-3** — Non-resident taxation. "Non-resident natural persons are taxed at a flat rate on Nepal-source income [RESEARCH GAP — reviewer to confirm rate, commonly cited as 25%]. Out of scope for the resident slab tables. Escalate to a Nepali tax professional."
- **R-NP-4** — Capital gains / property disposals. "Capital gains on land, buildings, or shares have separate rates and are outside the natural-person slab computation. Escalate to a Nepali tax professional."
- **R-NP-5** — Arrears / enforcement. "Client has outstanding tax arrears or is subject to IRD enforcement. Late-payment interest under §119 accrues monthly. Do not advise. Escalate to a Nepali tax professional immediately."
- **R-NP-6** — VAT return requested. "This skill covers income tax (D-01) only. Nepal VAT is a separate return — escalate or use a dedicated VAT skill."
- **R-NP-7** — Excluded professionals using a small-business scheme. "Doctors, engineers, auditors/accountants, lawyers, consultants, sportspersons, and actors CANNOT use presumptive or turnover-based schemes. They must file normal returns at slab rates. Do not apply a presumptive/turnover computation for these professions."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5. Match by case-insensitive substring on the counterparty/description. If multiple match, use the most specific. Nepali bank statements frequently mix Nepali (Devanagari/romanised) and English terms.

### 3.1 Income Patterns (Credits)

**Income patterns table**

| Pattern | D-01 Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED, BHUKTANI | Business income | Core self-employment revenue |
| PARAMARSHA, CONSULTANCY, PROFESSIONAL FEE, SEWA SHULKA | Business income | Service fees |
| ESEWA, KHALTI, IMEPAY PAYOUT | Business income | Digital-wallet settlement — match to invoices |
| FONEPAY, CONNECTIPS SETTLEMENT | Business income | Payment-gateway settlement |
| UPWORK, FIVERR, PAYONEER, WISE PAYOUT | Business income (foreign-source) | Freelance platform — confirm FX and remittance docs |
| TALAB, SALARY, PARISHRAMIK, [employer] | Employment income | Goes to assessable employment income, not business |
| GHAR BHADA, RENT RECEIVED | Rental/investment income | Separate head; often subject to TDS |
| BYAJ, INTEREST RECEIVED | Investment income | Bank interest, usually TDS-deducted |
| LAABHANSH, DIVIDEND | Investment income | Dividend (5% TDS, final) [verify rate vs IRD] |
| TAX REFUND, IRD REFUND | EXCLUDE | Prior-year refund, not income |

### 3.2 Expense Patterns (Debits) -- Deductible Business Expenses

**Deductible business expenses table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| KARYALAYA BHADA, OFFICE RENT | Office rent | Deductible | Dedicated business premises (rent TDS may apply) |
| LEKHAPAL, AUDITOR, ACCOUNTANT, CA FEE | Accountancy/audit fees | Deductible | Business-related |
| KANUNI, LAWYER, LEGAL, ADVOCATE | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Advertising | Deductible |  |
| TRAINING, SEMINAR, CONFERENCE | Training | Deductible | Must relate to current business |
| BANK CHARGE, SERVICE CHARGE, SPEJJEZ | Bank charges | Deductible | Business account only |
| ESEWA FEE, KHALTI FEE, GATEWAY FEE | Payment-processing fees | Deductible |  |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN | IT infrastructure | Deductible | Capitalise if a long-lived asset |

### 3.3 Expense Patterns (Debits) -- Software / SaaS

**Software / SaaS table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, ZOOM, SLACK | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN | Software subscription | Deductible |  |

### 3.4 Expense Patterns (Debits) -- Utilities (apportion if mixed/home use)

**Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| NEA, NEPAL ELECTRICITY, BIDYUT | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| KHANEPANI, WATER BOARD | Water | T2 if home office | Apportion |
| NTC, NCELL, WORLDLINK, VIANET, SUBISU | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| BUDDHA AIR, YETI AIRLINES, NEPAL AIRLINES | Flights | Deductible if business travel | Wholly business purpose |
| HOTEL, BOOKING.COM, RESORT | Accommodation | Deductible if business travel |  |
| PATHAO, INDRIVE, TAXI | Local transport | Deductible if business purpose |  |
| PETROL, DIESEL, FUEL, NOC, PUMP | Vehicle fuel | T2 — business % only | Requires logbook |
| PARKING | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**Not deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, BHOJANALAYA, PARTY, ENTERTAINMENT | Entertainment/personal meals | NOT deductible | Private/entertainment |
| BHANSAGHAR, GROCERIES, SUPERMARKET, BHATBHATENI | Personal living | NOT deductible | Private cost |
| FINE, JARIWANA, PENALTY | Fines/penalties | NOT deductible | Public policy |
| IRD PAYMENT, INCOME TAX, KAR BHUKTANI | Income tax paid | NOT deductible | Tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (depreciate, do not expense)

**Capital items table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | Capitalise & depreciate | Pool-based depreciation [RESEARCH GAP — reviewer to confirm pool rates under Schedule 2] |
| PRINTER, SCANNER, COPIER | Office equipment | Capitalise & depreciate | As above |
| FURNITURE, DESK, CHAIR | Furniture/fittings | Capitalise & depreciate | As above |
| VEHICLE, CAR, BIKE (business) | Motor vehicle | Capitalise & depreciate (business %) | As above |

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, KARJA, EMI (principal) | EXCLUDE (principal) | Interest portion may be deductible if business loan |
| SSF, SOCIAL SECURITY, EPF, CIT | Retirement deduction | Goes to the retirement-contribution deduction, not business expense |
| VAT PAYMENT, IRD VAT | EXCLUDE | VAT liability, not an income-tax expense |
| ADVANCE TAX, INSTALLMENT TAX | Tax credit | Credit against final liability, not an expense |

### 3.9 Nepali Banks -- Statement Format Reference

**Bank statement format table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Nepal Rastra Bank-regulated commercial banks (NABIL, NIC ASIA, Global IME, Nepal Investment Mega) | TRANSFER, DEPOSIT, CHARGE, FONEPAY, CONNECTIPS | PDF/CSV; date often in BS and/or AD |
| eSewa / Khalti / IME Pay (wallet statements) | LOAD, PAYMENT, CASHBACK, SETTLEMENT | CSV; wallet top-ups are not income |
| connectIPS | INTERBANK TRANSFER | Clearing rail; check underlying purpose |

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (business income)

**Input line:**
`2082-05-10 ; FONEPAY CREDIT ; HIMAL TRADE CONCERN ; INV 2082-014 ; +118,000.00 ; NPR`

**Reasoning:**
Settlement of a sales invoice. If the client is VAT-registered, the NPR 118,000 includes 13% VAT. Net of VAT = 118,000 / 1.13 = NPR 104,424.78; VAT = NPR 13,575.22 (a liability to IRD, excluded from income). If not VAT-registered, the full NPR 118,000 is business income.

**Classification:** Business income = NPR 104,424.78 (VAT-registered) or NPR 118,000 (non-VAT). VAT excluded.

### Example 2 -- SaaS Subscription (deductible)

**Input line:**
`2082-04-25 ; CARD PAYMENT ; ADOBE ; CREATIVE CLOUD ; -4,200.00 ; NPR`

**Reasoning:**
Recurring monthly software subscription used for the business. Fully deductible as an operating expense.

**Classification:** Deductible business expense = NPR 4,200.00.

### Example 3 -- Entertainment / Personal Meal (blocked)

**Input line:**
`2082-06-02 ; CARD ; BHATBHATENI SUPERSTORE ; ; -9,800.00 ; NPR`

**Reasoning:**
Supermarket spend is personal living cost. Not incurred in the production of business income. No partial deduction.

**Classification:** NOT deductible. Exclude entirely.

### Example 4 -- SSF / Retirement Contribution

**Input line:**
`2082-04-31 ; DD ; SOCIAL SECURITY FUND ; SSF CONTRIBUTION ; -6,600.00 ; NPR`

**Reasoning:**
Approved retirement-fund contribution. Deductible as a retirement contribution (not a business expense), capped at the lower of one-third of assessable income or NPR 500,000 (combined EPF/CIT/SSF). Confirm the annual aggregate against the cap.

**Classification:** Retirement-contribution deduction = NPR 6,600.00 (subject to annual cap).

### Example 5 -- Salary received (employment income, not business)

**Input line:**
`2082-05-01 ; CREDIT ; KATHMANDU TECH PVT LTD ; TALAB SHRAWAN ; +60,000.00 ; NPR`

**Reasoning:**
Monthly salary. This is employment (remuneration) income, assessed under the same slab table but as employment income, with employer TDS already withheld. Do NOT treat as self-employment business income.

**Classification:** Employment income = NPR 60,000.00 (TDS credit per salary slip).

### Example 6 -- Presumptive small taxpayer (full-year computation)

**Scenario:**
Resident sole proprietor running a retail shop in Kathmandu Metropolitan City. Annual turnover NPR 2,400,000 (≤ NPR 3,000,000), business income only, not an excluded profession.

**Reasoning:**
Turnover ≤ NPR 3,000,000 → eligible for the presumptive (fixed) tax. Location = Metropolitan City → fixed annual tax NPR 7,500 (PKF Trunco; notarynepal). No slab computation; filed on Form D-01 (presumptive). If there had been zero transactions in the year, no presumptive tax would be due (FY 2082/83 update).

**Classification:** Fixed presumptive tax = NPR 7,500 for the year.

### Example 7 -- Full natural-person computation (single, non-SSF)

**Scenario:**
Single resident freelancer, NOT SSF-enrolled. Assessable business income NPR 1,500,000. Allowable business expenses NPR 300,000. Life-insurance premium paid NPR 40,000. No SSF/retirement contribution.

**Step 1 — Taxable income:**
1,500,000 − 300,000 (expenses) − 40,000 (life insurance) = NPR 1,160,000.

**Step 2 — Apply single slabs (1% SST applies, non-SSF):**
- 0–500,000 @ 1% = 5,000
- 500,001–700,000 (200,000) @ 10% = 20,000
- 700,001–1,000,000 (300,000) @ 20% = 60,000
- 1,000,001–1,160,000 (160,000) @ 30% = 48,000

**Tax = 5,000 + 20,000 + 60,000 + 48,000 = NPR 133,000.**

No female rebate (not confirmed female with employment-only income). Tax payable before TDS/advance-tax credits = **NPR 133,000.**

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The Income-Production Test

- **Income-production test** — A business expense is deductible only if incurred in the production of income. Mixed-use expenses must be apportioned on a reasonable, documented basis. Private and capital expenditure is excluded.  _(Income Tax Act, 2058)_

### 5.2 The 1% Social Security Tax (SST) and SSF Interaction

- **SST first slab rule** — The first slab rate of 1% on resident natural persons with remuneration income is the SST — a flat, final levy into a separate SSF account; it is not creditable.  _(SSF rules; Wikipedia "Social Security Fund (Nepal)"; lawsagar; primelawnepal)_
- **SSF enrolled — 1% waived** — For employees enrolled in the SSF, the 1% SST is waived because it is already captured within the 11% employee SSF contribution (see Section 6 contribution table).  _(SSF rules; Wikipedia "Social Security Fund (Nepal)"; lawsagar; primelawnepal)_
- **Confirm SSF enrolment** — Always confirm SSF enrolment before deciding whether the 1% band applies.  _(SSF rules; Wikipedia "Social Security Fund (Nepal)"; lawsagar; primelawnepal)_

### 5.3 Deductions and Rebates (FY 2082/83)

**Deductions and rebates table**

| Item | Figure | Source |
| --- | --- | --- |
| Female-taxpayer rebate | 10% reduction on computed tax (resident women, employment/remuneration income only) | notarynepal |
| Senior-citizen extra exemption (age 65+) | Additional NPR 100,000 added to the basic exemption | sanjeev-shrestha; taxconsultantnepal |
| Remote-area allowance | NPR 10,000 – 50,000 (category A–E) | notarynepal |
| Approved retirement contribution (EPF/CIT/SSF combined) | Lower of 1/3 of assessable income or NPR 500,000 | notarynepal |
| Life-insurance premium | Up to NPR 40,000/yr | notarynepal |
| Health (medical) insurance premium | Up to NPR 20,000/yr | notarynepal |
| Donation | Up to 5% of adjusted taxable income or NPR 100,000 (lower) | Income Tax Act, 2058 |

### 5.4 Couple vs Single Assessment

- **Couple election** — A married couple may elect couple assessment, which raises the first (SST/exempt) band to NPR 600,000 and the 10% band ceiling accordingly (see Section 1). The election is per the slab table; confirm the couple is eligible and has elected.  _(Section 1 slab table)_

### 5.5 Depreciation / Capital Allowances

- **Depreciation pooling** — Business assets are pooled and depreciated under the Income Tax Act, 2058 (Schedule 2). Capital items are NOT expensed in full in the year of purchase. [RESEARCH GAP — reviewer to confirm pool categories and rates from the Act's Schedule 2 / PKF Trunco PDF before computing depreciation.]  _(Income Tax Act, 2058, Schedule 2)_

### 5.6 Non-Deductible Items

**Non-deductible items table**

| Item | Reason |
| --- | --- |
| Personal living expenses | Not business-related |
| Entertainment of a private nature | Not in production of income |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Capital expenditure | Depreciated, not expensed |
| Drawings / personal withdrawals | Not an expense |

### 5.7 Small-Business Regimes

- **Presumptive tax eligibility** — Presumptive (fixed) tax — turnover ≤ NPR 3,000,000 and income ≤ NPR 300,000, Nepal-source business income only, not an excluded profession.  _(PKF Trunco FY2082-83; notarynepal; commonlaw.com.np)_

**Presumptive (fixed) tax by location**  _(PKF Trunco FY2082-83; notarynepal; commonlaw.com.np)_

| Location | Fixed presumptive tax (NPR) |
| --- | --- |
| Metropolitan / Sub-Metropolitan City | 7,500 |
| Municipality | 4,000 |
| Rural Municipality (Gaunpalika) | 2,500 |

- **Zero transactions rule** — Zero transactions in the year → no presumptive tax (FY 2082/83 update). Filed on Form D-01.  _(PKF Trunco FY2082-83; notarynepal; commonlaw.com.np)_
- **Turnover-based tax eligibility** — Turnover-based tax — turnover NPR 3,000,000 to NPR 10,000,000, profit ≤ NPR 1,000,000.  _(PKF Trunco FY2082-83; notarynepal; commonlaw.com.np)_

**Turnover-based tax rates**  _(PKF Trunco FY2082-83; notarynepal; commonlaw.com.np)_

| Business type | Rate on turnover |
| --- | --- |
| Low-margin goods (gas, cigarettes, etc.) | 0.25% |
| Other goods / trade / products | 0.30% – 1.00% (commonly 0.75%) |
| Service business | 2.00% |

- **Excluded professionals cannot use small-business schemes** — Excluded professionals (doctors, engineers, auditors/accountants, lawyers, consultants, sportspersons, actors) cannot use (a) or (b); they file normal returns at slab rates.  _(PKF Trunco FY2082-83; notarynepal; commonlaw.com.np)_

### 5.8 Withholding Tax (TDS) — common rates

> **[RESEARCH GAP — reviewer to confirm each rate against IRD / PKF Trunco PDF before relying on it.]** Values below are standard Act rates that could not be confirmed line-by-line from the binary PDF.

**TDS common rates table**

| Payment | Rate | Note |
| --- | --- | --- |
| Dividend | 5% (final) | [verify] |
| Interest (bank/financial) | 5%–15% | depends on payee [verify] |
| Rent (house/land), natural person | 10% | commercial rent [verify] |
| Service fee | 15% | [verify] |
| Commission | 15% | [verify] |
| Contract/agreement payments | 1.5% | [verify] |
| Meeting/sitting fees, casual | 15% | [verify] |

### 5.9 Filing, Advance Tax and Deadlines

**Filing and deadlines table**

| Item | Detail | Source |
| --- | --- | --- |
| Individual / presumptive return | Form D-01 | taxadvisornepal; notarynepal |
| Annual return deadline | Within 3 months of FY end → end of Ashoj (~mid-October) | taxadvisornepal; estartupnepal |
| Extension | Up to +3 months on application → end of Poush (~mid-January) | taxadvisornepal |
| Advance/installment tax | 3 installments: end of Poush 40%, end of Chaitra 70%, end of Ashad 100% | Income Tax Act §94 |
| Employer TDS deposit | Monthly, by 25th of the following Nepali month | notarynepal |
| Online filing | taxpayerportal.ird.gov.np | IRD |

### 5.10 Registration Thresholds

**Registration thresholds table**

| Item | Threshold | Source |
| --- | --- | --- |
| PAN | Mandatory for all taxpayers before filing | notarynepal |
| VAT registration — goods only | Turnover > NPR 5,000,000 | nepsetrading; bizsewa |
| VAT registration — services / mixed | Turnover > NPR 3,000,000 | nepsetrading |
| VAT standard rate | 13% | notarynepal |

## Section 6 -- SSF Contributions and Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Social Security Fund (SSF) Contribution Table

- **Basis and registration deadline** — Computed on basic salary only (allowances excluded). Employer must register a new employee with the SSF within 3 months of joining.  _(Wikipedia "Social Security Fund (Nepal)"; lawsagar; primelawnepal; companydartanepal)_

**SSF contribution table**  _(Wikipedia "Social Security Fund (Nepal)"; lawsagar; primelawnepal; companydartanepal)_

| Contributor | Rate | Components |
| --- | --- | --- |
| Employee | 11% of basic salary | 10% Provident Fund + 1% Social Security Tax |
| Employer | 20% of basic salary | 10% Provident Fund + 8.33% Gratuity + 1.67% additional/SSF |
| **Total** | **31% of basic salary** | 20% PF + 8.33% Gratuity + 1.67% additional + 1% SST |

**Arithmetic check:** Employee 10 + 1 = 11. Employer 10 + 8.33 + 1.67 = 20. Total 11 + 20 = 31 (= 20 PF + 8.33 + 1.67 + 1 = 31). ✓

> **[RESEARCH GAP — reviewer to confirm]** the component sub-breakdown (8.33% gratuity, 1.67%, and per-scheme allocation: medical/maternity ~1%, accident/disability ~1.4%, dependent-family, old-age) against an official SSF circular before publishing as exact.

Sources: Wikipedia "Social Security Fund (Nepal)"; lawsagar; primelawnepal; companydartanepal.

### 6.2 Home Office Deduction

- **Home office deduction rules** — Apportion utilities/rent by the dedicated business-use area (floor area or room count). A dual-use space (living room, kitchen) does not qualify. Conservative default: 0% until the arrangement is confirmed. Flag for reviewer: confirm dedicated area basis and documentation.

### 6.3 Motor Vehicle Business Use

- **Motor vehicle business use rules** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Requires a logbook (business vs total km). Conservative default: 0% until logbook provided.

### 6.4 Phone / Internet Mixed Use

- **Phone/internet mixed use rules** — Business-use portion only. Conservative default: 0% until business percentage confirmed.

### 6.5 Female-Taxpayer Rebate Eligibility

- **Female-taxpayer rebate eligibility rules** — 10% rebate applies to resident women with employment/remuneration income only. Flag for reviewer: confirm the income is employment-only and the taxpayer qualifies before applying.

### 6.6 Small-Business Scheme Eligibility

- **Small-business scheme eligibility rules** — Confirm turnover and profit thresholds AND that the taxpayer is not an excluded professional before applying presumptive or turnover-based tax. Flag for reviewer: scheme choice materially changes the computation.

### 6.7 Bad Debt Write-Off

- **Bad debt write-off rules** — Deductible only if income was previously declared, recovery steps taken, and the debt is genuinely irrecoverable. Flag for reviewer to confirm all conditions.

## Section 7 -- Excel Working Paper Template

```
NEPAL INCOME TAX -- D-01 WORKING PAPER
Fiscal Year (BS): 2082/83        AD: 2025/26
Client: ___________________________   PAN: __________
Assessment: Single / Couple    Resident: Y/N    SSF-enrolled: Y/N

A. ASSESSABLE INCOME
  A1. Business income (net of VAT if registered)   ___________
  A2. Employment income (talab)                    ___________
  A3. Rental income                                ___________
  A4. Investment income (interest, dividend)       ___________
  A5. TOTAL assessable income                      ___________

B. ALLOWABLE BUSINESS EXPENSES (production-of-income test)
  B1. Office rent                                  ___________
  B2. Accountancy / audit / legal fees             ___________
  B3. Office supplies / stationery                 ___________
  B4. Software subscriptions                       ___________
  B5. Advertising / marketing                      ___________
  B6. Bank / payment-processing charges            ___________
  B7. Travel (business)                            ___________
  B8. Utilities (business %)                       ___________
  B9. Home office (% of utilities/rent)            ___________
  B10. Vehicle (business %)                        ___________
  B11. Depreciation (Schedule 2 pools)             ___________
  B12. Other allowable expenses                    ___________
  B13. TOTAL business expenses                     ___________

C. RETIREMENT & INSURANCE DEDUCTIONS
  C1. Approved retirement (lower of 1/3 income or 500,000) ___________
  C2. Life insurance (max 40,000)                  ___________
  C3. Health insurance (max 20,000)                ___________
  C4. Donation (max 5% / 100,000)                  ___________
  C5. Senior-citizen extra exemption (if 65+)      ___________
  C6. TOTAL deductions                             ___________

D. TAXABLE INCOME (A5 - B13 - C6)                  ___________

E. TAX COMPUTATION (pass to deterministic engine — single/couple slabs)
  E1. SST band (1% — waive if SSF-enrolled)        ___________
  E2. Progressive slab tax                         ___________
  E3. Gross tax                                    ___________
  E4. Less: female-taxpayer rebate (10%, if eligible) ___________
  E5. Less: TDS / advance / installment credits    ___________
  E6. Tax payable / refund                         ___________

REVIEWER FLAGS:
  [ ] Assessment status confirmed (single/couple)?
  [ ] Residency confirmed (≥183 days)?
  [ ] SSF enrolment confirmed (1% SST waived or applied)?
  [ ] Female-rebate eligibility confirmed?
  [ ] Senior-citizen exemption confirmed (65+)?
  [ ] Home office / vehicle / phone business % confirmed?
  [ ] Depreciation pools/rates confirmed (Schedule 2)?
  [ ] Small-business scheme eligibility confirmed?
  [ ] Retirement contribution within cap?
```

## Section 8 -- Bank Statement Reading Guide

### Nepali Bank Statement Formats

**Bank statement formats table**

| Source | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Commercial banks (NABIL, NIC ASIA, Global IME, Nepal Investment Mega) | PDF, CSV | Date (BS/AD), Description, Debit, Credit, Balance | Description holds counterparty + reference |
| eSewa / Khalti / IME Pay | CSV | Date, Type, Amount, Remarks | Wallet load ≠ income; settlement may be income |
| connectIPS / Fonepay | CSV/PDF | Date, Channel, Amount, Reference | Clearing rail; check underlying purpose |

### Key Nepali Banking / Tax Terms

**Key terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| भुक्तानी / BHUKTANI | Payment | Check direction for income/expense |
| तलब / TALAB / PARISHRAMIK | Salary / remuneration | Employment income |
| बहाल / GHAR BHADA / KIRAYA | Rent | Rental income or office-rent expense |
| ब्याज / BYAJ | Interest | Investment income (often TDS-deducted) |
| लाभांश / LAABHANSH | Dividend | Investment income |
| कर / KAR | Tax | Tax payment (not deductible) |
| जरिवाना / JARIWANA | Fine / penalty | Not deductible |
| कर्जा / KARJA / EMI | Loan | Principal excluded; business interest may deduct |
| सेवा शुल्क / SEWA SHULKA | Service charge / fee | Business income or bank charge — check context |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present these questions to the client:

```
ONBOARDING QUESTIONS -- NEPAL INCOME TAX
1. Assessment status: single or electing couple assessment?
2. Residency: were you in Nepal 183+ days this fiscal year?
3. Are you enrolled in the Social Security Fund (SSF)?
4. Profession: are you a doctor, engineer, auditor/accountant, lawyer,
   consultant, sportsperson, or actor? (affects small-business schemes)
5. Annual turnover and profit (for presumptive/turnover scheme eligibility)?
6. Female taxpayer with employment income only? (10% rebate)
7. Age 65+? (senior-citizen extra exemption)
8. Home office: dedicated space? What % of floor area?
9. Vehicle/phone/internet: what % is business use? Logbook kept?
10. Retirement contributions (EPF/CIT/SSF), life and health insurance paid?
11. TDS certificates and advance/installment tax receipts?
12. PAN and VAT registration status?
```

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Legislation references table**

| Topic | Reference |
| --- | --- |
| Income tax rates / slabs | Income Tax Act, 2058 + annual Finance Act; PKF Trunco FY2082-83 |
| Allowable deductions | Income Tax Act, 2058 |
| Depreciation | Income Tax Act, 2058, Schedule 2 [RESEARCH GAP — confirm rates] |
| Advance/installment tax | Income Tax Act, 2058, §94 |
| Non-filing penalty | Income Tax Act, 2058, §117 |
| Installment underpayment | Income Tax Act, 2058, §118 |
| Late-payment interest | Income Tax Act, 2058, §119 |
| False/misleading statement | Income Tax Act, 2058, §120 |
| SSF contributions | Contribution-Based Social Security Act; SSF (ssf.gov.np) |
| Filing portal / deadlines | IRD (ird.gov.np; taxpayerportal.ird.gov.np) |

### Penalties & Interest (Income Tax Act, 2058)

**Penalties and interest table**

| Provision | Charge | Source |
| --- | --- | --- |
| §117 — Non-filing / failure to maintain documents | NPR 100 per month OR 0.10% of assessable income, whichever is higher | actnepal §117 |
| §118 — Underpayment of installment tax | Interest (normal rate) on shortfall vs required installment | actnepal §118 |
| §119 — Late payment of tax | Interest at the normal rate, per month/part-month, on unpaid tax (normal rate commonly cited at 15% p.a. [RESEARCH GAP — confirm vs IRD circular]) | actnepal §119 |
| §120 — False/misleading statement | 50%–100% of underpaid tax depending on intent | actnepal §120 |
| §90 — Withholding return non-filing | 2.5% per annum (per month/part-month) of the tax amount | rpandeyassociates |
| Installment return penalty | NPR 5,000 per return OR 0.01% of income, whichever higher | rpandeyassociates |

### Minimum Wage (effective Shrawan 1, 2082 BS = 17 July 2025)

**Minimum wage table**

| Item | Amount (NPR) |
| --- | --- |
| Monthly minimum wage | 19,550 (= 12,170 basic + 7,380 dearness allowance) |
| Daily minimum wage | 754 (= 469 basic + 285 dearness allowance) |

**Arithmetic check:** 12,170 + 7,380 = 19,550 ✓; 469 + 285 = 754 ✓. ~13% rise from NPR 17,300/month. Source: PKF Trunco Flash Alert on Minimum Wages; lawgandhi; wageindicator.

### Non-Residents & Capital Gains (supplementary)

**Non-residents and capital gains table**

| Item | Treatment | Status |
| --- | --- | --- |
| Non-resident natural person | Flat 25% on Nepal-source income | [RESEARCH GAP — confirm vs PKF Trunco PDF] |
| Listed shares (resident) | 5% | [RESEARCH GAP — confirm] |
| Land/buildings owned >5 yrs | 5% | [RESEARCH GAP — confirm] |
| Land/buildings owned ≤5 yrs | 7.5% | [RESEARCH GAP — confirm] |

### Test Suite

**Test 1 — Single, non-SSF, mid-range.**
Input: Single, NOT SSF-enrolled, taxable income NPR 1,160,000.
Expected: 5,000 (1% on 500k) + 20,000 (10% on 200k) + 60,000 (20% on 300k) + 48,000 (30% on 160k) = **NPR 133,000.**

**Test 2 — Single at exactly the top of the 20% band.**
Input: Single, taxable income NPR 1,000,000.
Expected: cumulative tax = **NPR 85,000** (5,000 + 20,000 + 60,000).

**Test 3 — Married/couple at top of 30% band.**
Input: Couple assessment, taxable income NPR 2,000,000.
Expected: cumulative tax = **NPR 356,000** (6,000 + 20,000 + 60,000 + 270,000).

**Test 4 — Female-taxpayer rebate.**
Input: Single resident woman, employment income only, computed tax NPR 133,000.
Expected: rebate 10% = 13,300; tax after rebate = **NPR 119,700.**

**Test 5 — SSF taxpayer (1% SST waived).**
Input: Single, SSF-enrolled, taxable income NPR 700,000.
Expected: 0–500,000 at 0% (SST waived) + 200,000 @ 10% = **NPR 20,000.** (vs NPR 25,000 if non-SSF.)

**Test 6 — Presumptive small taxpayer, metro.**
Input: Sole proprietor, Kathmandu Metropolitan City, turnover NPR 2,400,000, not an excluded profession.
Expected: fixed presumptive tax = **NPR 7,500** (Form D-01).

**Test 7 — Turnover-based service business.**
Input: Service business, turnover NPR 6,000,000, profit ≤ NPR 1,000,000.
Expected: turnover tax = 2.00% × 6,000,000 = **NPR 120,000.**

**Test 8 — Excluded professional cannot use presumptive.**
Input: Lawyer, turnover NPR 2,000,000.
Expected: REJECT presumptive/turnover scheme → file normal return at slab rates.

## PROHIBITIONS

- **Prohibitions list** — - NEVER apply a slab table without knowing single vs couple assessment. - NEVER apply the 1% SST band to an SSF-enrolled employee — it is waived. - NEVER apply the 10% female rebate without confirming employment-only income and eligibility. - NEVER apply a presumptive or turnover scheme to an excluded professional (doctor, engineer, auditor/accountant, lawyer, consultant, sportsperson, actor). - NEVER treat employment salary (talab) as self-employment business income. - NEVER allow personal living, entertainment, fines, or income tax itself as a business deduction. - NEVER expense a capital item in full — depreciate it under Schedule 2. - NEVER include VAT collected on sales in business income for VAT-registered clients. - NEVER treat advance/installment tax as a business expense — it is a credit. - NEVER rely on a figure marked [RESEARCH GAP] without reviewer confirmation. - NEVER present tax calculations as definitive — always label as estimated.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
