---
name: maryland-sales-tax
description: Use this skill whenever asked about Maryland sales and use tax. Trigger on phrases like "Maryland sales tax", "MD sales tax", "Maryland Comptroller", "digital advertising tax". ALWAYS load us-sales-tax first.
version: 2.0
---

# Maryland Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Maryland |
| State rate | 6.00% (flat -- no local sales tax) |
| Local taxes | None |
| Maximum combined rate | 6.00% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Comptroller of Maryland |
| Portal | https://www.marylandtaxes.gov |
| SST member | No |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6% | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | TAXABLE | Maryland taxes SaaS and digital products |
| Canned software | TAXABLE | |
| Digital goods | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| OTC drugs | EXEMPT | |
| Resale | EXEMPT | |
| Digital advertising (separate tax) | TAXABLE | Maryland Digital Advertising Gross Revenues Tax -- separate from sales tax |

## Section 10 -- Prohibitions

- NEVER add local taxes -- Maryland has none.
- NEVER confuse the Digital Advertising Tax with sales tax -- they are separate.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
