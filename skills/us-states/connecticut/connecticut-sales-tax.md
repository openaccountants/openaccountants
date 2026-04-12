---
name: connecticut-sales-tax
description: Use this skill whenever asked about Connecticut sales and use tax, luxury tax, DRS filings. Trigger on phrases like "Connecticut sales tax", "CT sales tax", "DRS", "luxury tax Connecticut". ALWAYS load us-sales-tax first.
version: 2.0
---

# Connecticut Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Connecticut |
| State rate | 6.35% (standard); 7.75% (luxury items over $5,000) |
| Local taxes | None -- no local sales taxes |
| Maximum rate | 7.75% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 AND 200 transactions (AND test) |
| Tax authority | Connecticut DRS |
| Portal | https://portal.ct.gov/DRS |
| SST member | No |
| Skill version | 2.0 |

**UNIQUE: Luxury rate 7.75% on vehicles, jewelry, clothing, handbags, luggage, footwear over $5,000. AND test for nexus like NY.**

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6.35% | |
| Luxury items >$5,000 | TAXABLE 7.75% | Vehicles, jewelry, clothing, etc. |
| Clothing under $50/item | EXEMPT | |
| Clothing $50-$999 | TAXABLE 6.35% | |
| Clothing $1,000+ | TAXABLE 7.75% | Luxury rate |
| Grocery food | EXEMPT | |
| Prepared food/meals | TAXABLE 7.35% | Special restaurant rate |
| SaaS | TAXABLE | Computer/data processing services |
| Computer/data processing services | TAXABLE at 1% | Special reduced rate |
| Digital goods | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER forget the 7.75% luxury rate on items over $5,000.
- NEVER forget the clothing exemption under $50.
- NEVER assume nexus with only one threshold -- CT requires BOTH $100K AND 200 transactions.
- NEVER ignore the 1% rate on computer/data processing services.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
