---
name: massachusetts-sales-tax
description: Use this skill whenever asked about Massachusetts sales and use tax. Trigger on phrases like "Massachusetts sales tax", "MA sales tax", "MA DOR", "ST-9", "Massachusetts clothing exemption". ALWAYS load us-sales-tax first.
version: 2.0
---

# Massachusetts Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Massachusetts |
| State rate | 6.25% |
| Local taxes | None |
| Maximum combined rate | 6.25% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 in sales |
| Tax authority | Massachusetts Department of Revenue (DOR) |
| Portal | https://www.mass.gov/orgs/massachusetts-department-of-revenue |
| SST member | No |
| Clothing exemption | Yes -- under $175/item |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6.25% | |
| Clothing under $175/item | EXEMPT | Per-item threshold |
| Clothing $175+ per item | TAXABLE on amount over $175 | Only excess over $175 is taxed |
| Grocery food | EXEMPT | |
| Prepared food (meals) | TAXABLE at 6.25% | Local option meals tax up to 0.75% additional |
| SaaS | TAXABLE | Massachusetts taxes SaaS |
| Canned software | TAXABLE | |
| Digital goods | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER apply full tax to clothing under $175 -- only the excess over $175 is taxable.
- NEVER forget the local option meals tax (up to 0.75% additional on prepared food).
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
