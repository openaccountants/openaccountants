---
name: minnesota-sales-tax
description: Use this skill whenever asked about Minnesota sales and use tax. Trigger on phrases like "Minnesota sales tax", "MN sales tax", "M.S. 297A", "Minnesota DOR". NOTE -- Minnesota EXEMPTS clothing. ALWAYS load us-sales-tax first.
version: 2.0
---

# Minnesota Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Minnesota |
| State rate | 6.875% |
| Local rate range | 0% -- ~2% |
| Maximum combined rate | ~8.875% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Minnesota Department of Revenue (MNDOR) |
| Portal | https://www.revenue.state.mn.us |
| SST member | Yes (full member) |
| Clothing exemption | Yes -- ALL clothing exempt |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6.875% + local | |
| Clothing and footwear | EXEMPT | Minnesota exempts ALL clothing |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | NOT TAXABLE | |
| Canned software (download) | TAXABLE | |
| Digital goods | TAXABLE | Specified digital products |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | Capital equipment refund program |
| Prescription drugs | EXEMPT | |
| OTC drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER treat clothing as taxable in Minnesota -- ALL clothing is exempt.
- NEVER treat SaaS as taxable.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
