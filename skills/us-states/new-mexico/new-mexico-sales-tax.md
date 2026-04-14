---
name: new-mexico-sales-tax
description: Use this skill whenever asked about New Mexico Gross Receipts Tax (GRT). Trigger on phrases like "New Mexico GRT", "Gross Receipts Tax", "NM sales tax", "NMSA §7-9". NM has a GRT, not a traditional sales tax. ALWAYS load us-sales-tax first.
version: 2.0
---

# New Mexico Gross Receipts Tax (GRT) Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | New Mexico |
| Tax type | Gross Receipts Tax (GRT) -- NOT a traditional sales tax; tax on the SELLER |
| State GRT rate | 5.125% |
| Local add-on range | 0% -- ~4.1875% |
| Maximum combined rate | ~9.3125% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 in taxable gross receipts |
| Tax authority | New Mexico Taxation and Revenue Department (TRD) |
| Portal | https://tap.state.nm.us |
| SST member | No |
| Skill version | 2.0 |

**CRITICAL: NM GRT taxes virtually ALL services and most transactions. One of the broadest tax bases in the US (similar to Hawaii GET). Tax is on the seller, not the buyer.**

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | Deductible from gross receipts |
| Prepared food | TAXABLE | |
| ALL services (including professional) | TAXABLE | NM taxes virtually all services |
| SaaS | TAXABLE | |
| Digital goods | TAXABLE | |
| Healthcare services | DEDUCTIBLE | Specific healthcare deductions available |
| Manufacturing equipment | DEDUCTIBLE | Deduction from gross receipts |
| Prescription drugs | EXEMPT | |
| Resale | DEDUCTIBLE | |

## Section 10 -- Prohibitions

- NEVER call NM's tax a "sales tax" without noting it is a GRT on the seller.
- NEVER assume services are exempt -- NM taxes virtually ALL services.
- NEVER confuse "deduction" with "exemption" -- NM uses deductions from gross receipts.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
