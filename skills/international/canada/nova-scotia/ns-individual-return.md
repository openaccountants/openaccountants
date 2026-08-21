---
name: ns-individual-return
description: Use this skill whenever asked about Nova Scotia provincial individual income tax. Trigger on phrases like "Nova Scotia tax", "NS provincial tax", "Nova Scotia T1", "Nova Scotia brackets", "HST Nova Scotia", "Nova Scotia credits", "Nova Scotia surtax", or any question about computing Nova Scotia provincial tax for an individual return. This skill covers Nova Scotia's five-bracket tax system, HST at 15%, provincial credits, and filing requirements. ALWAYS read this skill before touching any Nova Scotia individual tax return work.
version: "1.0"
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NS Individual Return

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Province | Nova Scotia (Canada) |
| Tax | Provincial Personal Income Tax |
| Currency | CAD only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | Income Tax Act (Nova Scotia) |
| Tax authority | Canada Revenue Agency (administers on behalf of Nova Scotia) |
| Filing portal | CRA My Account / NETFILE / paper T1 |
| Filing deadline | 30 April 2026 (15 June 2026 if self-employed; balance due 30 April) |
| Skill version | 1.0 |

### Nova Scotia Provincial Tax Rates (2025)

**Nova Scotia Provincial Tax Rates (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 29,590 | 8.79% |
| 29,591 -- 59,180 | 14.95% |
| 59,181 -- 93,000 | 16.67% |
| 93,001 -- 150,000 | 17.5% |
| 150,001+ | 21% |

### Key Nova Scotia Features

**Key Nova Scotia Features**

| Feature | Detail |
| --- | --- |
| Harmonized sales tax (HST) | 15% (5% federal + 10% provincial) |
| Basic personal amount (2025) | $8,481 |
| Spousal/equivalent amount | $8,481 |
| Age amount | $4,141 |
| Nova Scotia Affordable Living Tax Credit | Refundable; up to $255/individual |
| Nova Scotia Child Benefit (NSCB) | $150/child (income-tested) |
| Nova Scotia Poverty Reduction Credit | $250/adult + $200/child |
| Surtax | None (eliminated) |

### Combined Federal + Nova Scotia Marginal Rates (2025)

**Combined Federal + Nova Scotia Marginal Rates (2025)**

| Taxable Income (CAD) | Combined Rate |
| --- | --- |
| 0 -- 29,590 | 23.79% |
| 29,591 -- 57,375 | 29.95% |
| 57,376 -- 59,180 | 35.45% |
| 59,181 -- 93,000 | 37.17% |
| 93,001 -- 114,750 | 38% |
| 114,751 -- 150,000 | 43.5% |
| 150,001 -- 158,468 | 47% |
| 158,469 -- 220,000 | 50% |
| 220,001+ | 54% |

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
| Form NS428 | Nova Scotia Tax and Credits |
| Form NS479 | Nova Scotia Credits (refundable) |

### 2.2 Provincial Non-Refundable Credits (Form NS428)

**Provincial Non-Refundable Credits (Form NS428)**

| Credit | Amount (2025) | Rate |
| --- | --- | --- |
| Basic personal amount | $8,481 | 8.79% |
| Spousal / common-law partner | $8,481 | 8.79% |
| CPP/EI contributions | Actual | 8.79% |
| Age amount | $4,141 | 8.79% |
| Pension income | Up to $1,000 | 8.79% |
| Disability | $8,015 | 8.79% |
| Tuition | Actual | 8.79% |
| Medical expenses | Excess over 3% of net income | 8.79% |
| Donations | First $200 at 8.79%; excess at 21% | Non-refundable |
| Volunteer firefighter / SAR | $3,000 | 8.79% |

### 2.3 Nova Scotia Refundable Credits (Form NS479)

**Nova Scotia Refundable Credits (Form NS479)**

| Credit | Detail |
| --- | --- |
| Affordable Living Tax Credit | $255/individual; $60/child; income-tested |
| Poverty Reduction Credit | $250/adult + $200/child; income < $16,000 (single) |
| Nova Scotia Child Benefit | $150/child quarterly; income-tested |
| Graduate Scholarship Tax Credit | Rebate on first 3 years of income tax for NS university/college graduates |
| Digital Media Tax Credit | For qualifying digital media companies (corporate) |

## Section 3 -- Computation Method

### Step 1: Calculate Taxable Income

- **Calculate Taxable Income** — Same as federal taxable income (Line 26000).  _(Line 26000)_

### Step 2: Apply Nova Scotia Bracket Rates

- **Apply Nova Scotia Bracket Rates** — First $29,590 × 8.79%; $29,591 to $59,180 × 14.95%; $59,181 to $93,000 × 16.67%; $93,001 to $150,000 × 17.5%; Above $150,000 × 21%

### Step 3: Subtract Non-Refundable Tax Credits

- **Subtract Non-Refundable Tax Credits** — Total credit amounts × 8.79% (lowest bracket rate).

### Step 4: Net Provincial Tax

- **Net Provincial Tax** — Gross provincial tax less credits.

### Step 5: Apply Refundable Credits

- **Apply Refundable Credits** — Subtract applicable refundable credits.

## Section 4 -- HST Considerations

**HST Considerations**

| Item | Detail |
| --- | --- |
| HST rate | 15% (5% federal + 10% provincial) |
| HST registrant (business) | Full input tax credit (ITC) available for HST paid on business purchases |
| Small supplier threshold | $30,000 in 4 consecutive quarters |
| Point-of-sale rebate | Provincial portion rebated on certain items (children's clothing, books, etc.) |
| New Housing Rebate | Provincial rebate on new homes up to $481,500 (36% of provincial HST) |

## Section 5 -- Income Types and Dividend Tax Credits

### 5.1 Nova Scotia Dividend Tax Credit

**Nova Scotia Dividend Tax Credit**

| Dividend Type | Federal Gross-Up | NS Credit Rate |
| --- | --- | --- |
| Eligible dividends (public corps) | 38% gross-up | 8.85% of taxable amount |
| Non-eligible dividends (CCPCs) | 15% gross-up | 2.99% of taxable amount |

### 5.2 Capital Gains

- 50% inclusion rate for all capital gains; the proposed 66.67% increase and $250,000 threshold were cancelled March 21, 2025
- Lifetime Capital Gains Exemption: $1,250,000 on qualifying small business shares (2025)
- Principal residence exemption: fully exempt from CGT

### 5.3 Self-Employment Income

Self-employed Nova Scotians report on T2125. Combined federal + NS rate on business income ranges from 23.79% to 54%. CPP contributions required (both employer and employee portions: 2 × 5.95% = 11.9% on pensionable earnings $3,500 -- $71,300).

## Section 6 -- Edge Cases

### 6.1 Nova Scotia Graduate Scholarship

Graduates of Nova Scotia post-secondary institutions may claim a tax credit equal to their provincial tax for the first 3 years of post-graduation employment in NS (up to total tuition paid). Must apply through NS Department of Finance.

### 6.1 Nova Scotia Graduate Scholarship

**Nova Scotia Graduate Scholarship Detail**

| Element | Detail |
| --- | --- |
| Eligible programs | Degrees/diplomas from NS universities and NSCC |
| Maximum benefit | Up to total tuition paid at NS institution |
| Duration | First 3 taxation years after graduation |
| Residency | Must live and work in NS |
| Application | Separate application to NS Dept of Finance (not automatic) |

### 6.2 Cost of Living Credit (Temporary)

NS has periodically introduced temporary cost-of-living credits. Check current year budget for any one-time payments.

### 6.3 Highest Combined Rate

At 54% combined marginal rate (over $220K), Nova Scotia has one of the highest combined rates in Canada. Tax planning considerations:
- Income splitting with spouse (pension income splitting via T1032)
- Incorporation of professional practice (small business rate ~26% combined)
- RRSP contributions (full deduction at marginal rate, withdrawal at lower rate)
- Charitable donations (NS credit at 21% on amounts over $200)

### 6.4 NS Affordable Living Tax Credit Detail

**NS Affordable Living Tax Credit Detail**

| Element | Detail |
| --- | --- |
| Individual amount | $255 |
| Spouse/partner | $255 |
| Per child under 19 | $60 |
| Income threshold (reduction starts) | $30,000 (individual); $34,000 (family) |
| Reduction rate | 5% of income over threshold |
| Paid via | Quarterly payments through CRA |

### 6.5 Disability Amount Transfer

- **Disability Amount Transfer** — A Nova Scotia resident supporting a dependant with a disability may claim the unused portion of the dependant's NS disability credit ($8,015 × 8.79%). The dependant must first use the credit against their own provincial tax.  _($8,015 × 8.79%)_

### Single taxpayer, employment income $75,000 (2025)

**Single taxpayer, employment income $75,000 (2025)**

| Step | Calculation | Amount |
| --- | --- | --- |
| Taxable income |  | $75,000 |
| NS tax on first $29,590 | $29,590 × 8.79% | $2,601 |
| NS tax on $29,591 -- $59,180 | $29,590 × 14.95% | $4,424 |
| NS tax on $59,181 -- $75,000 | $15,820 × 16.67% | $2,637 |
| Gross NS provincial tax |  | $9,662 |
| Less: Basic personal credit | $8,481 × 8.79% | ($745) |
| Less: CPP credit | ~$3,867 × 8.79% | ($340) |
| Less: EI credit | ~$1,049 × 8.79% | ($92) |
| Net NS provincial tax |  | $8,485 |
| Federal tax (for reference) |  | $11,252 |
| Total combined tax (approx.) |  | $19,737 |
| Effective combined rate |  | ~26.3% |

## Section 7 -- Worked Example

## Section 6 -- Prohibitions

- **Prohibitions** — - NEVER apply other provincial rates to a Nova Scotia resident - NEVER separate HST into GST + PST for filing purposes -- Nova Scotia uses harmonized HST - NEVER claim Nova Scotia credits without confirming NS residency on December 31 - NEVER ignore the five-bracket structure - NEVER present tax calculations as definitive -- always label as estimated

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
