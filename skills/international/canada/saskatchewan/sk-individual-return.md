---
name: sk-individual-return
description: Use this skill whenever asked about Saskatchewan provincial individual income tax. Trigger on phrases like "Saskatchewan tax", "SK provincial tax", "Saskatchewan T1", "Saskatchewan brackets", "PST Saskatchewan", "Saskatchewan credits", or any question about computing Saskatchewan provincial tax for an individual return. This skill covers Saskatchewan's three-bracket tax system, PST at 6%, provincial credits, and filing requirements. ALWAYS read this skill before touching any Saskatchewan individual tax return work.
version: "1.0"
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SK Individual Return

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Province | Saskatchewan (Canada) |
| Tax | Provincial Personal Income Tax |
| Currency | CAD only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | The Saskatchewan Income Tax Act, 2000 |
| Tax authority | Canada Revenue Agency (administers on behalf of Saskatchewan) |
| Filing portal | CRA My Account / NETFILE / paper T1 |
| Filing deadline | 30 April 2026 (15 June 2026 if self-employed; balance due 30 April) |
| Skill version | 1.0 |

### Saskatchewan Provincial Tax Rates (2025)

**Saskatchewan Provincial Tax Rates (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 52,057 | 10.5% |
| 52,058 -- 148,734 | 12.5% |
| 148,735+ | 14.5% |

### Key Saskatchewan Features

**Key Saskatchewan Features**

| Feature | Detail |
| --- | --- |
| Provincial sales tax (PST) | 6% |
| GST | 5% federal (no HST -- GST + PST are separate) |
| Basic personal amount (2025) | $17,661 |
| Spousal/equivalent amount | $17,661 |
| Age amount (65+) | $5,061 |
| Senior supplementary amount | $1,622 (for those 65+ with income < $86,810) |
| Saskatchewan Low-Income Tax Credit (SLITC) | Refundable; up to $388/adult + $150/child |
| Graduate Retention Program | Tuition rebate up to $20,000 over 7 years |
| Active Families Benefit | $150/child (for sport/cultural activities) |

### Combined Federal + Saskatchewan Marginal Rates (2025)

**Combined Federal + Saskatchewan Marginal Rates (2025)**

| Taxable Income (CAD) | Combined Rate |
| --- | --- |
| 0 -- 52,057 | 25.5% |
| 52,058 -- 57,375 | 25.5% |
| 57,376 -- 114,750 | 31% |
| 114,751 -- 148,734 | 38.5% |
| 148,735 -- 158,468 | 40.5% |
| 158,469 -- 220,000 | 43.5% |
| 220,001+ | 47.5% |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency province on Dec 31 | Do not compute provincial tax -- confirm province |
| Unknown marital status | Single (no spousal credit) |
| Unknown number of dependants | Zero |

## Section 2 -- Classification and Filing

### 2.1 T1 Structure

**T1 Structure**

| Schedule | Purpose |
| --- | --- |
| T1 General | Federal return |
| Form SK428 | Saskatchewan Tax and Credits |
| Schedule SK(S12) | Saskatchewan Tax calculation |

### 2.2 Provincial Non-Refundable Credits (Form SK428)

**Provincial Non-Refundable Credits (Form SK428)**

| Credit | Amount (2025) | Rate |
| --- | --- | --- |
| Basic personal amount | $17,661 | 10.5% |
| Spousal / common-law partner | $17,661 | 10.5% |
| CPP/EI contributions | Actual | 10.5% |
| Age amount | $5,061 | 10.5% |
| Pension income amount | Up to $1,000 | 10.5% |
| Disability amount | $12,651 | 10.5% |
| Tuition | Actual tuition | 10.5% |
| Medical expenses | Excess over 3% of net income (or $2,517) | 10.5% |
| Donations | First $200 at 10.5%; excess at 14.5% | Non-refundable |

### 2.3 Saskatchewan Refundable Credits

**Saskatchewan Refundable Credits**

| Credit | Detail |
| --- | --- |
| Saskatchewan Low-Income Tax Credit | $388/adult + $150/child; income-tested |
| Saskatchewan Sales Tax Credit | Built into federal GST/HST credit |
| Graduate Retention Program (GRP) | Up to $20,000 rebate of tuition over 7 years post-graduation |
| Active Families Benefit | $150/child for eligible activities |

## Section 3 -- Computation Method

### Step 1: Calculate Taxable Income

- **Calculate Taxable Income** — Same as federal taxable income (Line 26000).  _(Line 26000)_

### Step 2: Apply Saskatchewan Bracket Rates

- **Apply Saskatchewan Bracket Rates** — First $52,057 × 10.5%; $52,058 to $148,734 × 12.5%; Above $148,734 × 14.5%

### Step 3: Subtract Non-Refundable Tax Credits

- **Subtract Non-Refundable Tax Credits** — Total credit amounts × lowest bracket rate (10.5%).

### Step 4: Net Provincial Tax

- **Net Provincial Tax** — Result = Saskatchewan tax payable.

### Step 5: Apply Refundable Credits

- **Apply Refundable Credits** — Subtract applicable refundable credits.

## Section 4 -- PST Considerations

**PST Considerations**

| Item | Detail |
| --- | --- |
| PST rate | 6% on most goods and some services |
| Exemptions | Basic groceries, prescription drugs, children's clothing (under 15) |
| Application | PST is separate from GST (not combined into HST) |
| Business input | PST is NOT recoverable as input tax credit -- it's a cost |
| Impact on income tax | PST paid on business purchases is part of the expense cost (fully deductible) |

## Section 5 -- Transaction Patterns and Income Types

### 5.1 Income Types

**Income Types**

| Income Source | Reporting | Notes |
| --- | --- | --- |
| T4 Employment income | Line 10100 | Main source for most SK residents |
| T4A Pension / retirement | Line 11500/13000 | May qualify for pension income amount |
| T5 Investment income | Various lines | Eligible dividends get enhanced gross-up and dividend tax credit |
| T3 Trust income | Line 10400 | Various character allocations |
| T2125 Self-employment | Line 13500 | Net business income |
| T776 Rental income | Line 12600 | Net rental income |
| Capital gains (Schedule 3) | Line 12700 | 50% inclusion rate |
| Farm income (T2042) | Line 14100 | Saskatchewan-specific: significant agriculture sector |

### 5.2 Saskatchewan-Specific Dividend Tax Credit

**Saskatchewan-Specific Dividend Tax Credit**

| Dividend Type | Federal Gross-Up | SK Credit Rate |
| --- | --- | --- |
| Eligible dividends (public corps) | 38% gross-up | 11% of taxable amount |
| Non-eligible dividends (CCPCs) | 15% gross-up | 2.105% of taxable amount |

### 5.3 Capital Gains

- **Capital Gains for Saskatchewan residents** — Capital gains for Saskatchewan residents follow federal rules: 50% inclusion rate for individuals (first $250,000 of net gains); 66.67% inclusion for gains above $250,000 (effective June 2024); Capital gains on qualified small business corporation shares eligible for Lifetime Capital Gains Exemption ($1,250,000 in 2025)

## Section 6 -- Edge Cases

### 6.1 Farm Income

- **Farm Income** — Saskatchewan has significant agricultural activity. Farm losses may be restricted under Section 31 (restricted farm losses limited to $2,500 + 50% of next $30,000 = max $17,500 per year). Full farm losses available if farming is chief source of income. Saskatchewan farmers may benefit from: - Cash vs accrual accounting election for farming - AgriStability and AgriInvest payments (taxable) - Deferral of proceeds on grain deliveries to next year (ITA s. 76) - Saskatchewan Farm and Ranch Water Infrastructure Program (non-taxable grants in some cases)  _(ITA s. 76; Section 31)_

### 6.2 Resource Income

- **Resource Income** — Saskatchewan resource surcharge may apply to corporations with Saskatchewan resource income. Not applicable to individuals directly. However, individuals receiving royalties from potash, oil, or uranium properties report as other income.

### 6.3 Northern Residents Deduction

- **Northern Residents Deduction** — Residents of prescribed northern zones in Saskatchewan (e.g., northern communities above ~54th parallel) may claim the northern residents deduction: Basic residency amount: $11.00/day ($4,015/year for full-year residents); Additional 50% if in prescribed northern zone (vs intermediate zone); Travel benefits: deduction for up to 2 trips per household member

### 6.4 Graduate Retention Program (GRP) Detail

**Graduate Retention Program (GRP) Detail**

| Element | Detail |
| --- | --- |
| Eligibility | Graduates of eligible Saskatchewan post-secondary institutions |
| Maximum rebate | Up to $20,000 of tuition rebated |
| Claim period | 7 years from graduation |
| Annual maximum | Non-refundable credit limited to SK tax otherwise payable |
| Residency requirement | Must be resident in SK and file SK return |
| Not transferable | Cannot be transferred to spouse/parent |

### 6.5 Saskatchewan Pension Plan (SPP)

- **Saskatchewan Pension Plan (SPP)** — Voluntary supplemental pension for SK residents. Contributions deductible as RRSP contributions (reduces RRSP room). Maximum contribution $7,000/year.

## Section 7 -- Worked Example

### Single taxpayer, employment income $85,000 (2025)

**Single taxpayer, employment income $85,000 (2025)**

| Step | Calculation | Amount |
| --- | --- | --- |
| Taxable income |  | $85,000 |
| SK tax on first $52,057 | $52,057 × 10.5% | $5,466 |
| SK tax on $52,058 -- $85,000 | $32,943 × 12.5% | $4,118 |
| Gross SK provincial tax |  | $9,584 |
| Less: Basic personal credit | $17,661 × 10.5% | ($1,854) |
| Less: CPP credit | ~$3,867 × 10.5% | ($406) |
| Less: EI credit | ~$1,049 × 10.5% | ($110) |
| Net SK provincial tax |  | $7,214 |
| Federal tax (for reference) |  | $12,252 |
| Total combined tax (approx.) |  | $19,466 |
| Effective combined rate |  | ~22.9% |

## Section 6 -- Prohibitions

- **Prohibitions** — NEVER apply Alberta flat rate or other provincial rates to a Saskatchewan resident; NEVER combine PST and GST into HST -- Saskatchewan does not have HST; NEVER claim Graduate Retention Program without confirming graduation from eligible Saskatchewan institution; NEVER ignore the three-bracket structure -- Saskatchewan is NOT a flat-rate province; NEVER present tax calculations as definitive -- always label as estimated

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
