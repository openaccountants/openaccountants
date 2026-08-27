---
name: nb-individual-return
description: Use this skill whenever asked about New Brunswick provincial individual income tax. Trigger on phrases like "New Brunswick tax", "NB provincial tax", "New Brunswick T1", "New Brunswick brackets", "HST New Brunswick", "New Brunswick credits", or any question about computing New Brunswick provincial tax for an individual return. This skill covers New Brunswick's four-bracket tax system, HST at 15%, provincial credits, and filing requirements. ALWAYS read this skill before touching any New Brunswick individual tax return work.
version: "1.0"
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NB Individual Return

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Province | New Brunswick (Canada) |
| Tax | Provincial Personal Income Tax |
| Currency | CAD only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | New Brunswick Income Tax Act |
| Tax authority | Canada Revenue Agency (administers on behalf of New Brunswick) |
| Filing portal | CRA My Account / NETFILE / paper T1 |
| Filing deadline | 30 April 2026 (15 June 2026 if self-employed; balance due 30 April) |
| Skill version | 1.0 |

### New Brunswick Provincial Tax Rates (2025)

**New Brunswick Provincial Tax Rates (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 49,958 | 9.4% |
| 49,959 -- 99,916 | 14% |
| 99,917 -- 185,064 | 16% |
| 185,065+ | 19.5% |

### Key New Brunswick Features

**Key New Brunswick Features**

| Feature | Detail |
| --- | --- |
| Harmonized sales tax (HST) | 15% (5% federal + 10% provincial) |
| Basic personal amount (2025) | $13,044 |
| Spousal/equivalent amount | $13,044 |
| Age amount | $5,493 |
| NB Low-Income Tax Reduction | Eliminates provincial tax for income below ~$22,000 (single) |
| NB Child Tax Benefit | $250/child (income-tested) |
| NB Seniors' Home Renovation Tax Credit | 10% of eligible expenses (max $10,000) |
| NB Tuition Rebate (for graduates staying in NB) | 50% of tuition rebated over 3 years |

### Combined Federal + New Brunswick Marginal Rates (2025)

**Combined Federal + New Brunswick Marginal Rates (2025)**

| Taxable Income (CAD) | Combined Rate |
| --- | --- |
| 0 -- 49,958 | 24.4% |
| 49,959 -- 57,375 | 29% |
| 57,376 -- 99,916 | 34.5% |
| 99,917 -- 114,750 | 36.5% |
| 114,751 -- 158,468 | 42% |
| 158,469 -- 185,064 | 45% |
| 185,065 -- 220,000 | 48.5% |
| 220,001+ | 52.5% |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency province on Dec 31 | Do not compute -- confirm province |
| Unknown marital/family status | Single, no dependants |

## Section 2 -- Classification and Filing

### 2.1 T1 Structure

**T1 Structure**

| Schedule | Purpose |
| --- | --- |
| T1 General | Federal return |
| Form NB428 | New Brunswick Tax and Credits |
| Form NB479 | New Brunswick Credits (refundable) |

### 2.2 Provincial Non-Refundable Credits (Form NB428)

**Provincial Non-Refundable Credits (Form NB428)**

| Credit | Amount (2025) | Rate |
| --- | --- | --- |
| Basic personal amount | $13,044 | 9.4% |
| Spousal / common-law partner | $13,044 | 9.4% |
| CPP/EI contributions | Actual | 9.4% |
| Age amount | $5,493 | 9.4% |
| Pension income | Up to $1,000 | 9.4% |
| Disability | $9,834 | 9.4% |
| Tuition | Actual | 9.4% |
| Medical expenses | Excess over 3% of net income | 9.4% |
| Donations | First $200 at 9.4%; excess at 19.5% | Non-refundable |

### 2.3 New Brunswick Refundable Credits (Form NB479)

**New Brunswick Refundable Credits (Form NB479)**

| Credit | Detail |
| --- | --- |
| NB Low-Income Tax Reduction | Eliminates provincial tax for low-income earners |
| NB Child Tax Benefit | $250/child; income-tested |
| Seniors' Home Renovation Credit | 10% on up to $10,000 eligible expenses |
| Tuition Rebate | 50% of tuition over 3 years for NB graduates working in NB |
| Small Business Investor Tax Credit | 50% of eligible investment (max $125,000 investment) |

## Section 3 -- Computation Method

### Step 1: Calculate Taxable Income

- **Calculate Taxable Income** — Same as federal taxable income (Line 26000).  _(Line 26000)_

### Step 2: Apply New Brunswick Bracket Rates

- **Apply New Brunswick Bracket Rates** — First $49,958 × 9.4%; $49,959 to $99,916 × 14%; $99,917 to $185,064 × 16%; Above $185,064 × 19.5%

### Step 3: Subtract Non-Refundable Tax Credits

- **Subtract Non-Refundable Tax Credits** — Total credit amounts × 9.4% (lowest bracket rate).

### Step 4: Apply Low-Income Tax Reduction

- **Apply Low-Income Tax Reduction** — If eligible, reduces or eliminates provincial tax.

### Step 5: Net Provincial Tax

- **Net Provincial Tax** — Gross provincial tax less credits and low-income reduction.

### Step 6: Apply Refundable Credits

- **Apply Refundable Credits** — Subtract applicable refundable credits.

## Section 4 -- HST Considerations

**HST Considerations**

| Item | Detail |
| --- | --- |
| HST rate | 15% (5% federal + 10% provincial) |
| HST registrant (business) | Full input tax credit (ITC) available |
| Small supplier threshold | $30,000 in 4 consecutive quarters |
| New Housing Rebate | Provincial portion: 36% rebate on homes up to $350,000 |
| Point-of-sale rebates | Children's clothing, footwear, diapers, feminine hygiene |

## Section 5 -- Income Types and Dividend Tax Credits

### 5.1 New Brunswick Dividend Tax Credit

**New Brunswick Dividend Tax Credit**

| Dividend Type | Federal Gross-Up | NB Credit Rate |
| --- | --- | --- |
| Eligible dividends (public corps) | 38% gross-up | 14% of taxable amount |
| Non-eligible dividends (CCPCs) | 15% gross-up | 2.75% of taxable amount |

### 5.2 Capital Gains

- **Capital gains inclusion rate** — 50% inclusion rate for all capital gains; the proposed 66.67% increase and $250,000 threshold were cancelled March 21, 2025
- **Lifetime Capital Gains Exemption** — $1,250,000 on qualifying small business shares (2025)

### 5.3 NB Small Business Investor Tax Credit

**NB Small Business Investor Tax Credit**

| Element | Detail |
| --- | --- |
| Credit rate | 50% of eligible investment |
| Maximum investment | $125,000 per investor per year |
| Maximum credit | $62,500 per year |
| Eligible businesses | NB-based small businesses (approved by NB government) |
| Carry-forward | 7 years for unused credits |
| Hold period | Must hold investment for at least 4 years |

## Section 6 -- Edge Cases

### 6.1 NB Tuition Rebate

- **NB Tuition Rebate** — Available to graduates of designated NB post-secondary institutions who live and work in NB. Rebate is 50% of tuition paid, claimed over 3 years (20%/20%/10% or until limit reached). Maximum $10,000 lifetime rebate.

**NB Tuition Rebate details**

| Element | Detail |
| --- | --- |
| Eligible programs | Degrees/diplomas from designated NB institutions |
| Maximum lifetime rebate | $10,000 |
| Claim schedule | ~33% per year over 3 years |
| Residency | Must be NB resident and working in NB |
| Application | Automatic through T1 filing (claimed on NB479) |

### 6.2 Low-Income Tax Reduction

- **Low-Income Tax Reduction** — Eliminates NB provincial tax for individuals with income below approximately $22,000 (single). Phases out between ~$22,000 and ~$25,000. Adjusted for family size.

**Low-Income Tax Reduction thresholds**

| Filing Status | Threshold (approximate) |
| --- | --- |
| Single | $22,005 |
| Single + 1 dependant | $28,459 |
| Couple (no dependants) | $28,459 |
| Couple + 1 child | $32,457 |

### 6.3 Interprovincial Truckers/Workers

- **Interprovincial Truckers/Workers** — Workers who live in NB but earn income in other provinces: all income taxed at NB rates if resident on Dec 31. No provincial allocation for employment income.

### 6.4 Seniors' Home Renovation Credit

**Seniors' Home Renovation Credit**

| Element | Detail |
| --- | --- |
| Credit rate | 10% of eligible expenses |
| Maximum expenses | $10,000 per year |
| Maximum credit | $1,000 per year |
| Eligibility | 65+ or supporting a senior; NB resident |
| Eligible expenses | Ramps, grab bars, walk-in tubs, stairlifts, widening doorways |
| Non-eligible | Routine maintenance, appliances, landscaping |

### 6.5 Bilingual Province Considerations

New Brunswick is Canada's only officially bilingual province. CRA services and all tax forms are available in both English and French. No tax implications -- administrative convenience only.

## Section 7 -- Worked Example

### Single taxpayer, employment income $70,000 (2025)

**Single taxpayer, employment income $70,000 (2025)**

| Step | Calculation | Amount |
| --- | --- | --- |
| Taxable income |  | $70,000 |
| NB tax on first $49,958 | $49,958 × 9.4% | $4,696 |
| NB tax on $49,959 -- $70,000 | $20,042 × 14% | $2,806 |
| Gross NB provincial tax |  | $7,502 |
| Less: Basic personal credit | $13,044 × 9.4% | ($1,226) |
| Less: CPP credit | ~$3,867 × 9.4% | ($364) |
| Less: EI credit | ~$1,049 × 9.4% | ($99) |
| Net NB provincial tax |  | $5,813 |
| Federal tax (for reference) |  | $10,252 |
| Total combined tax (approx.) |  | $16,065 |
| Effective combined rate |  | ~22.9% |

## Section 6 -- Prohibitions

- **Prohibitions** — NEVER apply other provincial rates to a New Brunswick resident; NEVER separate HST into GST + PST -- New Brunswick uses harmonized HST; NEVER claim NB credits without confirming NB residency on December 31; NEVER ignore the four-bracket structure; NEVER claim the Tuition Rebate without confirming NB post-secondary graduation and NB residency; NEVER present tax calculations as definitive -- always label as estimated

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
