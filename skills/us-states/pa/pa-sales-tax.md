---
name: pa-sales-tax
description: Use this skill whenever asked about Pennsylvania sales and use tax, PA DOR filings, Pennsylvania clothing exemption, Philadelphia sales tax, Allegheny County tax, or any request involving Pennsylvania state sales and use tax compliance. Trigger on phrases like "Pennsylvania sales tax", "PA sales tax", "PA DOR", "PA-3", "Philadelphia tax", "Pennsylvania clothing exemption", or any request involving Pennsylvania sales tax. ALWAYS read this skill before touching any Pennsylvania sales tax work.
version: 2.0
jurisdiction: US-PA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - us-sales-tax
category: us-states
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PA Sales Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| State | Pennsylvania |
| Tax | Sales and Use Tax (state + local) |
| State rate | 6.00% |
| Local rates | Philadelphia 2.00%; Allegheny County 1.00% |
| Maximum combined rate | 8.00% (Philadelphia) |
| Sourcing | Destination-based |
| Primary legislation | Tax Reform Code of 1971, Article II (72 P.S. 7201 et seq.) |
| Tax authority | Pennsylvania Department of Revenue (PA DOR) |
| Filing portal | https://www.revenue.pa.gov |
| Return form | PA-3 |
| SST member | No |
| Economic nexus | $100,000 in gross sales (effective July 1, 2019) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires PA CPA or EA sign-off |
| Skill version | 2.0 |

### Taxability Quick Matrix

**Taxability Quick Matrix**

| Item | Taxable? | Notes |
| --- | --- | --- |
| Tangible personal property | YES | Default taxable |
| SaaS / cloud software | YES | Taxable as canned software; custom software exempt |
| Grocery food | NO | Most food for home consumption exempt |
| Clothing | NO | Most clothing exempt (key PA distinction) |
| General services | NO | Most services exempt unless specifically enumerated |
| Repair/maintenance of TPP | YES | Taxable |
| Cleaning services (commercial) | YES | Taxable |
| Digital products | YES | Taxable (digital downloads) |
| Manufacturing equipment | NO | Exempt (directly used in manufacturing) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Product taxability unknown | Taxable |
| Clothing item unclear | Exempt (most clothing is exempt in PA) |
| Custom vs canned software unknown | Taxable (canned) |
| Philadelphia or Allegheny unclear | State rate only (6%) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — Nexus confirmation, PA sales tax license, filing frequency, products/services sold, whether selling into Philadelphia or Allegheny County.
- **Recommended inputs** — Sales by jurisdiction, exemption certificates, prior PA-3 returns.
- **Ideal inputs** — Complete transaction log, exemption certificate register.

### Refusal Catalogue

- **R-PA-1 -- Audit defense** — Escalate.
- **R-PA-2 -- Complex use tax on construction** — Construction use tax exemptions require specialist analysis. Escalate.

## Section 3 -- Transaction Pattern Library

### 3.1 Taxable Sales

**Taxable Sales**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Electronics / hardware | Taxable at combined rate | TPP |
| SaaS subscription (canned) | Taxable | Canned software |
| Repair services for TPP | Taxable | Enumerated service |
| Cleaning services | Taxable | Enumerated |
| Digital downloads | Taxable |  |

### 3.2 Exempt Sales

**Exempt Sales**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Clothing (most) | Exempt | PA exempts most clothing |
| Grocery food (most) | Exempt | Food for home consumption |
| Custom software | Exempt | Designed for specific customer |
| Prescription medicine | Exempt |  |
| Resale with certificate | Exempt | REV-1220 |

## Section 4 -- Worked Examples

### Example 1 -- Sale in Philadelphia

**Input:** Retailer sells electronics for $1,000 in Philadelphia. Rate: 8.00% (6% + 2%).

**Classification:** Tax = $80.00. Total = $1,080.00.

### Example 2 -- Clothing Sale

**Input:** Retailer sells $200 jacket in Pittsburgh (Allegheny County).

**Reasoning:** Most clothing is exempt in Pennsylvania.

**Classification:** Tax = $0. Clothing exempt.

### Example 3 -- SaaS in PA (Non-Philadelphia)

**Input:** Business subscribes to canned SaaS product. $500/month. Located outside Philadelphia/Allegheny.

**Classification:** Tax = $30.00/month (6% state rate). Canned software is taxable.

### Example 4 -- Custom Software

**Input:** Business pays $50,000 for custom-developed software.

**Classification:** Tax = $0. Custom software is exempt in PA.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Rate Structure

- **State rate** — 6.00%
- **Philadelphia combined rate** — +2.00% = 8.00%
- **Allegheny County combined rate** — +1.00% = 7.00%
- **State rate** — 6.00%

### 5.2 Filing Frequency

**Filing Frequency**

| Frequency | Criteria | Due Date |
| --- | --- | --- |
| Monthly | Tax liability > $75/month | 20th of following month |
| Quarterly | Tax liability $75 or less/month | 20th after quarter end |
| Semi-annual | Very low volume | 20th after period end |

### 5.3 Economic Nexus

- **Economic nexus threshold** — $100,000 in gross sales into PA USD (Effective July 1, 2019. No transaction count test.)

### 5.4 Marketplace Facilitator

- **Marketplace facilitator collection requirement** — Required to collect and remit. Effective April 1, 2020.

### 5.5 Vendor Discount

- **Vendor discount** — 1% of tax collected for timely filing. Maximum $25/month for monthly filers.

### 5.6 Penalties

**Penalties**

| Penalty | Rate |
| --- | --- |
| Late filing | 5% per month (max 25%) |
| Late payment | 3% per month (max 18%) |
| Interest | Federal underpayment rate + 3% |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Custom vs Canned Software

- **Custom vs canned software treatment** — Custom software (designed for a specific customer) is exempt. Canned/prewritten software is taxable. Mixed situations require analysis. Flag for reviewer.

### 6.2 Construction Exemptions

- **Construction machinery/equipment exemption** — Certain building machinery and equipment used in construction may qualify for exemption. Complex rules. Flag for reviewer.

## Section 7 -- Working Paper Template

```
PENNSYLVANIA SALES TAX WORKING PAPER (PA-3)
Business: _______________  License: ___________
Period: ___________

A. GROSS SALES                                   ___________
B. EXEMPT SALES (clothing, food, resale)         ___________
C. TAXABLE SALES (A - B)                         ___________
D. STATE TAX (C x 6%)                            ___________
E. LOCAL TAX (Philadelphia 2% / Allegheny 1%)    ___________
F. TOTAL TAX                                     ___________
G. VENDOR DISCOUNT (if timely)                   ___________
H. NET REMITTANCE                                ___________
```

## Section 8 -- Bank Statement Reading Guide

**Bank Statement Reading Guide**

| Narration | Classification Hint |
| --- | --- |
| PA DOR / REVENUE PA | Tax payment -- exclude |
| AMAZON / SHOPIFY / STRIPE | Marketplace or processor |

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- PENNSYLVANIA SALES TAX
1. Do you have a PA sales tax license?
2. Filing frequency (monthly / quarterly / semi-annual)?
3. Do you sell into Philadelphia or Allegheny County?
4. Nexus type?
5. Products or services sold?
6. Do you sell clothing (exempt in PA)?
7. Do you sell software (custom or canned)?
8. Sell to exempt entities?
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Sales tax imposition | 72 P.S. 7202 |
| Exemptions | 72 P.S. 7204 |
| Clothing exemption | 72 P.S. 7204(26) |
| Software taxability | PA DOR guidance |
| Economic nexus | Act 13 of 2019 |
| Local taxes | Philadelphia Code; Allegheny County |

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 2.0 | April 2026 | Full rewrite to v2.0; taxability matrix; clothing exemption; custom vs canned software |
| 1.0 | 2025 | Initial version |

## PROHIBITIONS

- NEVER charge sales tax on most clothing in Pennsylvania -- clothing is generally exempt
- NEVER treat custom software as taxable -- only canned/prewritten software is taxable
- NEVER forget the Philadelphia (2%) and Allegheny County (1%) local surtaxes
- NEVER treat grocery food as taxable -- most food for home consumption is exempt
- NEVER present calculations as definitive -- direct client to qualified CPA or EA

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
