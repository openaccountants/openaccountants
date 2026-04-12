---
name: michigan-sales-tax
description: Use this skill whenever asked about Michigan sales and use tax. Trigger on phrases like "Michigan sales tax", "MI sales tax", "MCL 205.51", "Michigan Treasury". ALWAYS load us-sales-tax first.
version: 2.0
---

# Michigan Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Michigan |
| State rate | 6.00% (flat -- no local sales tax) |
| Local taxes | None |
| Maximum combined rate | 6.00% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Michigan Department of Treasury |
| Portal | https://www.michigan.gov/treasury |
| SST member | Yes (full member) |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6% | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | NOT TAXABLE | Michigan does not tax SaaS |
| Canned software (download) | TAXABLE | Prewritten software is TPP |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | Industrial processing exemption |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER add local tax -- Michigan has no local sales taxes.
- NEVER treat SaaS as taxable in Michigan.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
