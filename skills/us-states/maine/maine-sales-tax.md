---
name: maine-sales-tax
description: Use this skill whenever asked about Maine sales and use tax. Trigger on phrases like "Maine sales tax", "ME sales tax", "MRS", "36 M.R.S. §1811". ALWAYS load us-sales-tax first.
version: 2.0
---

# Maine Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Maine |
| State rate | 5.50% (general); 8.00% (short-term auto rental); 9.00% (lodging/prepared food) |
| Local taxes | None |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Maine Revenue Services (MRS) |
| Portal | https://www.maine.gov/revenue |
| SST member | No |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 5.50% | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE 9.00% | Higher rate |
| Lodging | TAXABLE 9.00% | Higher rate |
| Short-term auto rental | TAXABLE 8.00% | |
| SaaS | NOT TAXABLE | Maine does not tax SaaS |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER use the 5.50% rate for prepared food or lodging -- they have higher rates (9%).
- NEVER forget the 8% short-term auto rental rate.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
