---
name: mb-individual-return
description: Use this skill whenever asked about Manitoba provincial individual income tax. Trigger on phrases like "Manitoba tax", "MB provincial tax", "Manitoba T1", "Manitoba brackets", "RST Manitoba", "Manitoba health levy", "Manitoba education property tax credit", or any question about computing Manitoba provincial tax for an individual return. This skill covers Manitoba's three-bracket tax system, RST at 7%, health and education levy, provincial credits, and filing requirements. ALWAYS read this skill before touching any Manitoba individual tax return work.
version: "1.0"
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MB Individual Return

## Manitoba Individual Tax Return -- Provincial T1 Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Province | Manitoba (Canada) |
| Tax | Provincial Personal Income Tax |
| Currency | CAD only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | The Income Tax Act (Manitoba) |
| Tax authority | Canada Revenue Agency (administers on behalf of Manitoba) |
| Filing portal | CRA My Account / NETFILE / paper T1 |
| Filing deadline | 30 April 2026 (15 June 2026 if self-employed; balance due 30 April) |
| Skill version | 1.0 |

### Manitoba Provincial Tax Rates (2025)

**Manitoba Provincial Tax Rates (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 47,000 | 10.8% |
| 47,001 -- 100,000 | 12.75% |
| 100,001+ | 17.4% |

### Key Manitoba Features

**Key Manitoba Features**

| Feature | Detail |
| --- | --- |
| Retail sales tax (RST) | 7% |
| GST | 5% federal (no HST -- GST + RST are separate) |
| Basic personal amount (2025) | $15,780 |
| Spousal/equivalent amount | $15,780 |
| Age amount (65+) | Combined with federal |
| Education Property Tax Credit | Up to $700 (homeowners/renters; income-tested reduction above $23,800) |
| Manitoba Personal Tax Credit (Primary Caregiver) | Up to $1,400 |
| School Tax Rebate | Portion of property tax rebated (varies annually) |
| Manitoba Health and Post-Secondary Education Tax Levy (payroll) | Employer-paid: 2.15% on payroll > $2.5M |

### Combined Federal + Manitoba Marginal Rates (2025)

**Combined Federal + Manitoba Marginal Rates (2025)**

| Taxable Income (CAD) | Combined Rate |
| --- | --- |
| 0 -- 47,000 | 25.8% |
| 47,001 -- 57,375 | 25.8% |
| 57,376 -- 100,000 | 33.25% |
| 100,001 -- 114,750 | 37.9% |
| 114,751 -- 158,468 | 43.4% |
| 158,469 -- 220,000 | 46.4% |
| 220,001+ | 50.4% |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency province on Dec 31 | Do not compute -- confirm province |
| Unknown marital/family status | Single, no dependants |
| Unknown homeowner/renter status | Do not claim Education Property Tax Credit |

## Section 2 -- Classification and Filing

### 2.1 T1 Structure

**T1 Structure**

| Schedule | Purpose |
| --- | --- |
| T1 General | Federal return |
| Form MB428 | Manitoba Tax and Credits |
| Schedule MB(S12) | Manitoba Tax calculation |
| Form MB479 | Manitoba Credits (refundable) |

### 2.2 Provincial Non-Refundable Credits (Form MB428)

**Provincial Non-Refundable Credits (Form MB428)**

| Credit | Amount (2025) | Rate |
| --- | --- | --- |
| Basic personal amount | $15,780 | 10.8% |
| Spousal / common-law partner | $15,780 | 10.8% |
| CPP/EI contributions | Actual | 10.8% |
| Pension income | Up to $1,000 | 10.8% |
| Disability | $9,945 | 10.8% |
| Tuition | Actual | 10.8% |
| Medical expenses | Excess over 3% of net income | 10.8% |
| Donations | First $200 at 10.8%; excess at 17.4% | Non-refundable |
| Fitness (children under 16) | Up to $500/child | 10.8% |

### 2.3 Manitoba Refundable Credits (Form MB479)

**Manitoba Refundable Credits (Form MB479)**

| Credit | Detail |
| --- | --- |
| Education Property Tax Credit | Up to $700; reduced by 2% of net income over $23,800 |
| School Tax Rebate | Percentage of school taxes paid (announced annually in budget) |
| Primary Caregiver Tax Credit | Up to $1,400 for qualifying caregivers |
| Personal Tax Credit (low income) | Additional relief for incomes under $12,500 |
| Community Enterprise Development Tax Credit | 45% of approved investments |
| Fertility Treatment Tax Credit | 40% of eligible fertility treatment costs |

## Section 3 -- Computation Method

### Step 1: Calculate Taxable Income

- **Calculate Taxable Income** — Same as federal taxable income (Line 26000).

### Step 2: Apply Manitoba Bracket Rates

- **Apply Manitoba Bracket Rates** — First $47,000 × 10.8%; $47,001 to $100,000 × 12.75%; Above $100,000 × 17.4%

### Step 3: Subtract Non-Refundable Tax Credits

- **Subtract Non-Refundable Tax Credits** — Total credit amounts × 10.8%.

### Step 4: Net Provincial Tax

- **Net Provincial Tax** — Gross provincial tax less non-refundable credits.

### Step 5: Apply Refundable Credits

- **Apply Refundable Credits** — Subtract Education Property Tax Credit, Primary Caregiver Credit, etc.

## Section 4 -- RST Considerations

**RST Considerations**

| Item | Detail |
| --- | --- |
| RST rate | 7% on most goods and specified services |
| Services subject to RST | Insurance premiums, telecom, hotel accommodation, electricity |
| Exemptions | Basic groceries, prescription drugs, children's clothing, residential heating |
| Application | RST is separate from GST (not combined into HST) |
| Business input | RST is NOT recoverable as input tax credit (except on certain goods for resale) |
| Impact on income tax | RST paid on business purchases is part of the deductible expense |

## Section 5 -- Health and Post-Secondary Education Tax Levy

This is an EMPLOYER payroll tax, not an individual tax. Included for context:

## Section 5 -- Health and Post-Secondary Education Tax Levy

**Health and Post-Secondary Education Tax Levy rates**

| Annual Payroll | Rate |
| --- | --- |
| Up to $2,000,000 | 0% (exempt) |
| $2,000,001 -- $2,500,000 | 4.3% on amount over $2M |
| Over $2,500,000 | 2.15% on total payroll |

## Section 6 -- Income Types and Dividend Tax Credits

### 6.1 Manitoba Dividend Tax Credit

**Manitoba Dividend Tax Credit**

| Dividend Type | Federal Gross-Up | MB Credit Rate |
| --- | --- | --- |
| Eligible dividends (public corps) | 38% gross-up | 8% of taxable amount |
| Non-eligible dividends (CCPCs) | 15% gross-up | 0.78% of taxable amount |

### 6.1 Manitoba Dividend Tax Credit

Note: Manitoba has one of the lowest non-eligible dividend credits in Canada, making CCPC dividends relatively more expensive for MB residents.

### 6.2 Capital Gains

50% inclusion rate for all capital gains; the proposed 66.67% increase and $250,000 threshold were cancelled March 21, 2025
Combined top rate on eligible capital gains: ~25.2% (50% inclusion, top bracket)
Lifetime Capital Gains Exemption: $1,250,000 on qualifying small business shares

### 6.3 Self-Employment Income

Self-employed Manitoba residents pay:
CPP contributions: both employer and employee portions (11.9% on pensionable earnings $3,500 -- $71,300)
EI: optional for self-employed (special benefits only)
No separate Manitoba payroll tax on self-employment income (employer levy only)

## Section 7 -- Edge Cases

### 7.1 Manitoba Pension Income

Manitoba does not have a separate provincial pension income splitting provision -- federal pension income splitting (T1032) reduces taxable income which flows through to provincial calculation.

### 7.2 Northern Residents

Federal Northern Residents Deduction applies for prescribed zones in northern Manitoba (Thompson, Churchill, The Pas, and other northern communities). Reduces taxable income for both federal and provincial purposes.

### 7.2 Northern Residents

**Northern Residents Deduction Rates**

| Zone | Deduction Rate |
| --- | --- |
| Northern (Churchill, remote communities) | $11.00/day (full) |
| Intermediate (some mid-north towns) | $5.50/day (half) |

### 7.3 Farm Income

Manitoba agricultural producers may claim:
Manitoba Farm and Small Business Tax Credit for eligible property taxes on farmland
Deferral of grain sales proceeds (ITA s. 76)
AgriStability/AgriInvest payments taxable

### 7.4 Education Property Tax Credit Detail

**Education Property Tax Credit Detail**

| Element | Detail |
| --- | --- |
| Maximum credit | $700 per household |
| Based on | School taxes paid (homeowner) or 20% of rent paid (renter) |
| Reduction | 2% of net income over $23,800 |
| Eliminated at | Income ~$58,800 (single homeowner at max) |
| Claim method | On Form MB479 |
| Seniors supplement | Additional amount for 65+ |

### 7.5 Community Enterprise Development Tax Credit

**Community Enterprise Development Tax Credit**

| Element | Detail |
| --- | --- |
| Credit rate | 45% of eligible investment |
| Maximum investment | $30,000 per year |
| Maximum credit | $13,500 per year |
| Eligible entities | Manitoba community development corporations |
| Hold period | Minimum 3 years |
| Carry-forward | 5 years |

## Section 7 -- Prohibitions

NEVER apply other provincial rates to a Manitoba resident
NEVER combine RST and GST into HST -- Manitoba does not have HST
NEVER claim Education Property Tax Credit without confirming Manitoba residency and property tax or rent paid
NEVER ignore the three-bracket structure
NEVER confuse the employer Health and Education Levy with individual tax liability
NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CGA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
