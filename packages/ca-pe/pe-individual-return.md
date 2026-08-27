---
name: pe-individual-return
description: Use this skill whenever asked about Prince Edward Island provincial individual income tax. Trigger on phrases like "PEI tax", "Prince Edward Island tax", "PE provincial tax", "PEI T1", "PEI brackets", "HST PEI", "PEI surtax", "PEI credits", or any question about computing PEI provincial tax for an individual return. This skill covers PEI's four-bracket tax system with surtax, HST at 15%, provincial credits, and filing requirements. ALWAYS read this skill before touching any PEI individual tax return work.
version: "1.0"
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PE Individual Return

## Prince Edward Island Individual Tax Return -- Provincial T1 Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Province | Prince Edward Island (Canada) |
| Tax | Provincial Personal Income Tax |
| Currency | CAD only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | Income Tax Act (Prince Edward Island) |
| Tax authority | Canada Revenue Agency (administers on behalf of PEI) |
| Filing portal | CRA My Account / NETFILE / paper T1 |
| Filing deadline | 30 April 2026 (15 June 2026 if self-employed; balance due 30 April) |
| Skill version | 1.0 |

### PEI Provincial Tax Rates (2025)

**PEI Provincial Tax Rates (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 32,656 | 9.65% |
| 32,657 -- 64,313 | 13.63% |
| 64,314 -- 105,000 | 16.65% |
| 105,001+ | 18% |

### PEI Surtax

**PEI Surtax**

| Provincial Tax Threshold | Surtax Rate |
| --- | --- |
| Provincial basic tax > $12,500 | 10% of provincial tax exceeding $12,500 |

### Key PEI Features

**Key PEI Features**

| Feature | Detail |
| --- | --- |
| Harmonized sales tax (HST) | 15% (5% federal + 10% provincial) |
| Basic personal amount (2025) | $13,500 |
| Spousal/equivalent amount | $13,500 |
| Age amount | $4,959 |
| PEI Low-Income Tax Reduction | Reduces/eliminates tax for low-income residents |
| PEI Sales Tax Credit | $110/adult; income-tested |
| PEI Volunteer Firefighter Credit | $500 |

### Combined Federal + PEI Marginal Rates (2025)

**Combined Federal + PEI Marginal Rates (2025)**

| Taxable Income (CAD) | Combined Rate |
| --- | --- |
| 0 -- 32,656 | 24.65% |
| 32,657 -- 57,375 | 28.63% |
| 57,376 -- 64,313 | 34.13% |
| 64,314 -- 105,000 | 37.15% |
| 105,001 -- 114,750 | 38.5% |
| 114,751 -- 158,468 | 44% |
| 158,469 -- 220,000 | 47% |
| 220,001+ | 51% |

### Combined Federal + PEI Marginal Rates (2025)

Note: rates above do not include surtax effect. With surtax, effective top rate increases by approximately 1.8%.

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
| Form PE428 | PEI Tax and Credits |
| Form PE479 | PEI Credits (refundable) |

### 2.2 Provincial Non-Refundable Credits (Form PE428)

**Provincial Non-Refundable Credits (Form PE428)**

| Credit | Amount (2025) | Rate |
| --- | --- | --- |
| Basic personal amount | $13,500 | 9.65% |
| Spousal / common-law partner | $13,500 | 9.65% |
| CPP/EI contributions | Actual | 9.65% |
| Age amount | $4,959 | 9.65% |
| Pension income | Up to $1,000 | 9.65% |
| Disability | $8,777 | 9.65% |
| Tuition | Actual | 9.65% |
| Medical expenses | Excess over 3% of net income | 9.65% |
| Donations | First $200 at 9.65%; excess at 18% | Non-refundable |
| Volunteer firefighter | $500 | 9.65% |

### 2.3 PEI Surtax Calculation

- **PEI Surtax Calculation** — Surtax = (Basic provincial tax − $12,500) × 10% CAD (Applies when basic provincial tax exceeds $12,500; typically affects taxable incomes above approximately $140,000.)

### 2.4 PEI Refundable Credits (Form PE479)

**PEI Refundable Credits (Form PE479)**

| Credit | Detail |
| --- | --- |
| PEI Sales Tax Credit | $110/adult; income-tested; phases out above $30,000 (single) |
| Low-Income Tax Reduction | Eliminates/reduces tax for incomes below ~$20,000 |
| Seniors Independence Initiative | Home care/modification assistance (not a tax credit per se) |
| Community Development Equity Tax Credit | 35% of eligible investment |

## Section 3 -- Computation Method

### Step 1: Calculate Taxable Income

- **Calculate Taxable Income** — Same as federal taxable income (Line 26000).

### Step 2: Apply PEI Bracket Rates

- **Apply PEI Bracket Rates** — First $32,656 × 9.65%; $32,657 to $64,313 × 13.63%; $64,314 to $105,000 × 16.65%; Above $105,000 × 18%

### Step 3: Subtract Non-Refundable Tax Credits

- **Subtract Non-Refundable Tax Credits** — Total credit amounts × 9.65% (lowest bracket rate).

### Step 4: Calculate Surtax

- **Calculate Surtax** — If basic provincial tax > $12,500: add 10% of excess.

### Step 5: Apply Low-Income Tax Reduction

- **Apply Low-Income Tax Reduction** — Reduces or eliminates tax for low-income earners.

### Step 6: Net Provincial Tax

- **Net Provincial Tax** — After surtax addition and credit reductions.

### Step 7: Apply Refundable Credits

- **Apply Refundable Credits** — Subtract Sales Tax Credit and other refundable amounts.

## Section 4 -- HST Considerations

**HST Considerations**

| Item | Detail |
| --- | --- |
| HST rate | 15% (5% federal + 10% provincial) |
| HST registrant | Full ITC available for business purchases |
| Small supplier threshold | $30,000 in 4 consecutive quarters |
| Real property (new residential) | Provincial new housing rebate available |

## Section 5 -- Income Types and Dividend Tax Credits

### 5.1 PEI Dividend Tax Credit

**PEI Dividend Tax Credit**

| Dividend Type | Federal Gross-Up | PE Credit Rate |
| --- | --- | --- |
| Eligible dividends (public corps) | 38% gross-up | 10.5% of taxable amount |
| Non-eligible dividends (CCPCs) | 15% gross-up | 1.8% of taxable amount |

### 5.2 Capital Gains

- **50% inclusion rate** — 50% inclusion rate for all capital gains; the proposed 66.67% increase and $250,000 threshold were cancelled March 21, 2025
- **Lifetime Capital Gains Exemption** — $1,250,000 CAD (on qualifying small business shares)
- **Combined top rate on capital gains (50% inclusion)** — ~25.5%

### 5.3 Filing Deadlines and Instalments

**Filing Deadlines and Instalments**

| Item | Detail |
| --- | --- |
| Filing deadline | 30 April 2026 (self-employed: 15 June 2026) |
| Balance due | 30 April 2026 regardless of filing deadline |
| Instalment threshold | Net tax owing > $3,000 in current year AND either of prior 2 years |
| Instalment schedule | Quarterly: March 15, June 15, September 15, December 15 |
| Interest on late balance | Prescribed rate (compounded daily) |

## Section 6 -- Edge Cases

### 6.1 PEI Surtax Impact

The surtax is unique to PEI among Atlantic provinces. It effectively creates a higher marginal rate for high-income earners:

### 6.1 PEI Surtax Impact

**PEI Surtax Impact**

| Basic Provincial Tax | Effective Surtax | Total Effective Top Rate |
| --- | --- | --- |
| $12,500 or less | None | 18% (top bracket only) |
| $15,000 | ($15,000 - $12,500) × 10% = $250 | ~18.2% effective |
| $20,000 | ($20,000 - $12,500) × 10% = $750 | ~18.5% effective |
| $30,000+ | Significant | ~19.8% effective on top bracket |

### 6.2 Seasonal Workers

PEI has significant seasonal employment (fishing, tourism, agriculture). Workers may have:
- EI benefits during off-season (taxable)
- Intermittent T4s from multiple employers
- Provincial tax applies to total income regardless of seasonal pattern

### 6.3 Small Province Considerations

PEI has a small population (~170,000) -- fewer provincial-specific programs compared to larger provinces. Federal credits (GST/HST credit, Canada Workers Benefit) are particularly important for low-income PEI residents.

### 6.4 Inter-Provincial Commuters

Workers commuting to Nova Scotia or New Brunswick for employment are taxed as PEI residents if resident on Dec 31 in PEI. No provincial tax allocation for employment income earned in other provinces.

### 6.5 Community Development Equity Tax Credit

**Community Development Equity Tax Credit**

| Element | Detail |
| --- | --- |
| Credit rate | 35% of eligible investment |
| Maximum investment | $20,000/year |
| Maximum credit | $7,000/year |
| Eligible businesses | PEI-based community development corporations |
| Hold period | 5 years minimum |
| Carry-forward | 4 years |

### 6.6 PEI Property Transfer Tax

- **PEI Property Transfer Tax** — When acquiring property in PEI, a Real Property Transfer Tax of 1% of the greater of purchase price or assessed value applies. This is not an income tax but relevant context for property investors -- it adds to cost base for CGT purposes.

## Section 6 -- Prohibitions

- **NEVER apply other provincial rates to a PEI resident** — NEVER apply other provincial rates to a PEI resident
- **NEVER separate HST into components for filing** — NEVER separate HST into components for filing -- PEI uses harmonized HST
- **NEVER ignore the surtax calculation** — NEVER ignore the surtax calculation for higher-income earners
- **NEVER claim PEI credits without confirming residency** — NEVER claim PEI credits without confirming PEI residency on December 31
- **NEVER omit the surtax from the computation** — NEVER omit the surtax from the computation -- it applies in addition to bracket rates
- **Prohibition 6** — NEVER present tax calculations as definitive -- always label as estimated

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
