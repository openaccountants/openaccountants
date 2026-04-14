---
name: missouri-sales-tax
description: Use this skill whenever asked about Missouri sales and use tax. Trigger on phrases like "Missouri sales tax", "MO sales tax", "RSMo 144", "MyTax Missouri". NOTE -- Missouri was the LAST state to enact economic nexus (Jan 1, 2023). ALWAYS load us-sales-tax first.
version: 2.0
---

# Missouri Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Missouri |
| State rate | 4.225% |
| Local rate range | 0% -- ~6.5% (county + city + special district) |
| Maximum combined rate | ~10.85% |
| Sourcing | Origin-based (intrastate); destination for remote sellers |
| Economic nexus | $100,000 in taxable sales (last state to enact -- Jan 1, 2023) |
| Tax authority | Missouri Department of Revenue (MODOR) |
| Portal | https://mytax.mo.gov |
| SST member | No |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 4.225% + local | |
| Clothing | TAXABLE | No exemption |
| Grocery food | TAXABLE at reduced 1.225% state | Plus local |
| Prepared food | TAXABLE at full rate | |
| SaaS | NOT TAXABLE | Missouri does not tax SaaS |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER say grocery food is exempt -- Missouri taxes it at reduced 1.225% state rate plus full local.
- NEVER treat SaaS as taxable in Missouri.
- NEVER forget Missouri was the last state to enact economic nexus (2023).
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
