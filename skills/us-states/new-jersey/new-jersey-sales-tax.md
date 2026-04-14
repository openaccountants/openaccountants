---
name: new-jersey-sales-tax
description: Use this skill whenever asked about New Jersey sales and use tax. Trigger on phrases like "New Jersey sales tax", "NJ sales tax", "NJ Division of Taxation", "UEZ", "NJ clothing exemption". ALWAYS load us-sales-tax first.
version: 2.0
---

# New Jersey Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | New Jersey |
| State rate | 6.625% |
| Local taxes | None (except Urban Enterprise Zones at 3.3125%) |
| Maximum combined rate | 6.625% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | NJ Division of Taxation |
| Portal | https://www.nj.gov/treasury/taxation/ |
| SST member | No |
| Clothing exemption | Yes -- ALL clothing and footwear exempt |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6.625% | |
| Clothing and footwear | EXEMPT | NJ exempts ALL clothing and footwear |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | TAXABLE | NJ taxes SaaS and digital products |
| Canned software | TAXABLE | |
| Digital goods | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| OTC drugs | EXEMPT | |
| Resale | EXEMPT | |
| Urban Enterprise Zone (UEZ) sales | TAXABLE at 50% rate (3.3125%) | Qualifying retailers in UEZs |

## Section 10 -- Prohibitions

- NEVER treat clothing as taxable in NJ -- ALL clothing and footwear is exempt.
- NEVER forget the UEZ reduced rate program (3.3125%).
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
