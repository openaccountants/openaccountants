---
name: dc-sales-tax
description: Use this skill whenever asked about District of Columbia sales tax, DC OTR filings. Trigger on phrases like "DC sales tax", "District of Columbia sales tax", "OTR". ALWAYS load us-sales-tax first.
version: 2.0
---

# District of Columbia Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | District of Columbia |
| General rate | 6.00% |
| Restaurant meals/liquor | 10.00% |
| Transient accommodations | 14.95% |
| Parking | 18.00% |
| Local taxes | None -- DC is a single jurisdiction |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Office of Tax and Revenue (OTR) |
| Portal | https://mytax.dc.gov |
| SST member | No |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6% | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food/restaurant meals | TAXABLE 10% | Higher rate |
| Liquor for on-premises | TAXABLE 10% | |
| Transient accommodations | TAXABLE 14.95% | |
| Parking | TAXABLE 18% | |
| SaaS | TAXABLE | DC taxes SaaS and digital goods |
| Digital goods | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER use the general 6% rate for restaurant meals -- the rate is 10%.
- NEVER forget the 14.95% transient accommodation rate.
- NEVER forget the 18% parking rate.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
