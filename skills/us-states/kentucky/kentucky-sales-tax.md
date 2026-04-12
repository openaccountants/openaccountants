---
name: kentucky-sales-tax
description: Use this skill whenever asked about Kentucky sales and use tax. Trigger on phrases like "Kentucky sales tax", "KY sales tax", "KRS §139". ALWAYS load us-sales-tax first.
version: 2.0
---

# Kentucky Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Kentucky |
| State rate | 6.00% (flat, uniform statewide) |
| Local taxes | None |
| Maximum combined rate | 6.00% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Kentucky Department of Revenue |
| Portal | https://revenue.ky.gov |
| SST member | Yes -- Full Member |
| Services taxation | Expanded effective Jan 1, 2023 -- many services now taxable |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6% | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | TAXABLE | Kentucky taxes SaaS as of 2023 expansion |
| Canned software | TAXABLE | |
| Digital goods | TAXABLE | |
| Many services (expanded 2023) | TAXABLE | Including landscaping, janitorial, security, fitness, cosmetic surgery, pet care, and more |
| Professional services (legal, accounting, medical) | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER forget Kentucky's 2023 services expansion -- many services previously exempt are now taxable.
- NEVER add local taxes -- Kentucky has none.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
