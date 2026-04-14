---
name: iowa-sales-tax
description: Use this skill whenever asked about Iowa sales and use tax. Trigger on phrases like "Iowa sales tax", "IA sales tax", "IDR", "Iowa Code §423", "Iowa LOST". ALWAYS load us-sales-tax first.
version: 2.0
---

# Iowa Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Iowa |
| State rate | 6.00% |
| Local option (LOST) | Up to 1.00% (county voter-approved) |
| Maximum combined rate | 7.00% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 in gross revenue |
| Tax authority | Iowa Department of Revenue (IDR) |
| Portal | https://tax.iowa.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6% + LOST | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | TAXABLE | Iowa taxes SaaS and specified digital products |
| Canned software | TAXABLE | |
| Digital goods (specified) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER forget the Local Option Sales Tax (LOST) which adds up to 1%.
- NEVER treat SaaS as nontaxable in Iowa -- Iowa taxes it.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
