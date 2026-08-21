---
name: nl-individual-return
description: Use this skill whenever asked about Newfoundland and Labrador provincial individual income tax. Trigger on phrases like "Newfoundland tax", "NL provincial tax", "Newfoundland T1", "Labrador tax", "Newfoundland brackets", "HST Newfoundland", "Newfoundland credits", or any question about computing Newfoundland and Labrador provincial tax for an individual return. This skill covers NL's eight-bracket tax system, HST at 15%, provincial credits, and filing requirements. ALWAYS read this skill before touching any Newfoundland and Labrador individual tax return work.
version: "1.0"
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NL Individual Return

## Section 1 -- Quick Reference

**Section 1 Quick Reference**

| Field | Value |
| --- | --- |
| Province | Newfoundland and Labrador (Canada) |
| Tax | Provincial Personal Income Tax |
| Currency | CAD only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | Income Tax Act, 2000 (Newfoundland and Labrador) |
| Tax authority | Canada Revenue Agency (administers on behalf of NL) |
| Filing portal | CRA My Account / NETFILE / paper T1 |
| Filing deadline | 30 April 2026 (15 June 2026 if self-employed; balance due 30 April) |
| Skill version | 1.0 |

### Newfoundland & Labrador Provincial Tax Rates (2025)

**Newfoundland & Labrador Provincial Tax Rates (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 43,198 | 8.7% |
| 43,199 -- 86,395 | 14.5% |
| 86,396 -- 154,244 | 15.8% |
| 154,245 -- 215,943 | 17.3% |
| 215,944 -- 275,870 | 18.3% |
| 275,871 -- 551,739 | 19.8% |
| 551,740 -- 1,103,478 | 20.8% |
| 1,103,479+ | 21.3% |

### Key NL Features

**Key NL Features**

| Feature | Detail |
| --- | --- |
| Harmonized sales tax (HST) | 15% (5% federal + 10% provincial) |
| Basic personal amount (2025) | $10,818 |
| Spousal/equivalent amount | $10,818 |
| Age amount | $4,037 |
| NL Low-Income Tax Reduction | Eliminates provincial tax below ~$22,000 |
| NL Seniors' Benefit | Up to $1,516/year (income-tested) |
| NL Income Supplement | $60/month for low-income individuals |
| Temporary Residential Energy Rebate | Varies by year |

### Combined Federal + NL Marginal Rates (2025)

**Combined Federal + NL Marginal Rates (2025)**

| Taxable Income (CAD) | Combined Rate |
| --- | --- |
| 0 -- 43,198 | 23.7% |
| 43,199 -- 57,375 | 29.5% |
| 57,376 -- 86,395 | 35% |
| 86,396 -- 114,750 | 36.3% |
| 114,751 -- 154,244 | 41.8% |
| 154,245 -- 158,468 | 43.3% |
| 158,469 -- 215,943 | 46.3% |
| 215,944 -- 220,000 | 47.3% |
| 220,001 -- 275,870 | 51.3% |
| 275,871 -- 551,739 | 52.8% |
| 551,740 -- 1,103,478 | 53.8% |
| 1,103,479+ | 54.3% |

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
| Form NL428 | NL Tax and Credits |
| Form NL479 | NL Credits (refundable) |

### 2.2 Provincial Non-Refundable Credits (Form NL428)

**Provincial Non-Refundable Credits (Form NL428)**

| Credit | Amount (2025) | Rate |
| --- | --- | --- |
| Basic personal amount | $10,818 | 8.7% |
| Spousal / common-law partner | $10,818 | 8.7% |
| CPP/EI contributions | Actual | 8.7% |
| Age amount | $4,037 | 8.7% |
| Pension income | Up to $1,000 | 8.7% |
| Disability | $7,483 | 8.7% |
| Tuition | Actual | 8.7% |
| Medical expenses | Excess over 3% of net income | 8.7% |
| Donations | First $200 at 8.7%; excess at 18.3% | Non-refundable |
| Volunteer firefighter / SAR | $3,000 | 8.7% |

### 2.3 NL Refundable Credits (Form NL479)

**NL Refundable Credits (Form NL479)**

| Credit | Detail |
| --- | --- |
| Low-Income Tax Reduction | Eliminates provincial tax for low-income; phases out above ~$22,000 |
| NL Seniors' Benefit | Up to $1,516/year for age 65+; income-tested |
| NL Income Supplement | $60/month for individuals with income under threshold |
| Resort Property Investment Tax Credit | 45% of eligible investment |
| Direct Equity Tax Credit | 35% of investment in eligible NL businesses |

## Section 3 -- Computation Method

### Step 1: Calculate Taxable Income

- **Calculate Taxable Income** — Same as federal taxable income (Line 26000).

### Step 2: Apply NL Bracket Rates

- **Apply NL Bracket Rates** — Apply each rate to the corresponding portion of income through all 8 brackets.

### Step 3: Subtract Non-Refundable Tax Credits

- **Subtract Non-Refundable Tax Credits** — Total credit amounts × 8.7% (lowest bracket rate).

### Step 4: Apply Low-Income Tax Reduction

- **Apply Low-Income Tax Reduction** — Reduces or eliminates tax for low-income earners.

### Step 5: Net Provincial Tax

- **Net Provincial Tax** — After credits and reductions.

### Step 6: Apply Refundable Credits

- **Apply Refundable Credits** — Subtract Seniors' Benefit, Income Supplement, etc.

## Section 4 -- HST Considerations

**HST Considerations**

| Item | Detail |
| --- | --- |
| HST rate | 15% (5% federal + 10% provincial) |
| HST registrant | Full ITC available for business purchases |
| Small supplier threshold | $30,000 in 4 consecutive quarters |
| Insurance premiums | Subject to 15% Insurance Companies Tax (separate from HST) |

## Section 5 -- Income Types and Dividend Tax Credits

### 5.1 NL Dividend Tax Credit

**NL Dividend Tax Credit**

| Dividend Type | Federal Gross-Up | NL Credit Rate |
| --- | --- | --- |
| Eligible dividends (public corps) | 38% gross-up | 6.3% of taxable amount |
| Non-eligible dividends (CCPCs) | 15% gross-up | 3.2% of taxable amount |

### 5.2 Capital Gains

- 50% inclusion rate for all capital gains; the proposed 66.67% increase and $250,000 threshold were cancelled March 21, 2025
- Combined top rate on capital gains (50% inclusion): ~27.15% (up to $250K)

### 5.3 Self-Employment and Fishing Income

**Self-Employment and Fishing Income**

| Income Type | Form | Notes |
| --- | --- | --- |
| Business income | T2125 | Standard self-employment |
| Professional income | T2125 | Lawyers, accountants, engineers, etc. |
| Fishing income | T2121 | Significant in NL economy |
| Farming income | T2042 | Less common in NL |

## Section 6 -- Edge Cases

### 6.1 Eight Bracket Complexity

NL has the most tax brackets of any Canadian province. At high income levels (over $1.1M), the combined rate reaches 54.3% -- among the highest in Canada. Income splitting and deferral strategies are particularly relevant.

**Planning Strategies for Eight Bracket Complexity**

| Planning Strategy | Benefit in NL |
| --- | --- |
| Pension income splitting (T1032) | Up to 50% of pension income taxed in lower-bracket spouse |
| RRSP contributions | Deduction at up to 54.3%; withdrawal at lower marginal rate |
| Incorporation (CCPC) | Small business rate ~26% vs personal 54.3% |
| Charitable donations | NL credit at 18.3% (over $200 at top rate) |
| Capital gains timing | Realize gains in lower-income years |

### 6.2 Offshore Oil & Gas Workers

Workers on offshore platforms (e.g., Hibernia, Terra Nova, Hebron) who maintain NL residency are taxed as NL residents. International maritime workers may have treaty implications.

**Offshore Oil & Gas Workers considerations**

| Consideration | Detail |
| --- | --- |
| Rotational schedules | 14/14 or 21/21 common -- residency still NL if ties maintained |
| Employment income | Fully taxable in NL (province of residence on Dec 31) |
| Living-away-from-home benefits | May be taxable if not at a remote work site |
| Northern/remote site rules | Some offshore platforms qualify; verify with employer |

### 6.3 Labrador Benefits

Residents of Labrador and other prescribed zones qualify for the federal Northern Residents Deduction:
- Basic residency amount: $11.00/day
- Northern zone (most of Labrador): full amount
- Intermediate zone (some coastal areas): 50% of amount
- Travel benefit: deduction for 2 trips/year per household member

### 6.4 Fishers

Fishing income reported on T2121. NL has specific provisions for self-employed fishers:
- EI fishing benefits available (separate from regular EI)
- Capital cost allowance on fishing vessels and gear
- Fuel costs fully deductible as business expense
- Licensing fees deductible
- Net fishing income subject to both federal and NL provincial tax
- CPP contributions required on net fishing income

### 6.5 NL Direct Equity Tax Credit

**NL Direct Equity Tax Credit**

| Element | Detail |
| --- | --- |
| Credit rate | 35% of eligible investment |
| Maximum investment | $50,000/year |
| Maximum credit | $17,500/year |
| Eligible businesses | NL-based small businesses (approved by NL government) |
| Hold period | Minimum 5 years |
| Carry-forward | 7 years |

## Section 6 -- Prohibitions

- NEVER apply other provincial rates to an NL resident
- NEVER separate HST into components for filing -- NL uses harmonized HST
- NEVER claim NL credits without confirming NL residency on December 31
- NEVER simplify the eight-bracket structure into fewer brackets
- NEVER ignore the Low-Income Tax Reduction for eligible filers
- NEVER present tax calculations as definitive -- always label as estimated

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
