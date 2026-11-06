---
name: me-sales-tax
description: "Use this skill whenever asked about Maine sales and use tax. Trigger on phrases like \"Maine sales tax\", \"ME sales tax\", \"MRS\", \"36 M.R.S. §1811\". ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/me-sales-tax"
  jurisdiction: "US-ME"
  tax_year: "2025"
  last_updated: "2026-11-03"
---

# ME Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Maine |
| State rate | 5.50% (general); 8.00% (prepared food); 9.00% (lodging); 10.00% (short-term auto rental) |
| Local taxes | None |
| Sourcing | Destination-based |
| Economic nexus | More than $100,000 in gross sales delivered into Maine in the previous or current calendar year (same test for marketplace facilitators). No transaction-count test. 36 MRSA s.1754-B(1-B)(B) and (K) |
| Tax authority | Maine Revenue Services (MRS) |
| Portal | https://www.maine.gov/revenue |
| SST member | No |
| Skill version | 2.1 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 5.50% |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE 8.00% | Higher rate |
| Lodging | TAXABLE 9.00% | Higher rate |
| Short-term auto rental | TAXABLE 10.00% |  |
| SaaS | NOT TAXABLE | Maine does not tax SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Prohibition on using 5.50% for prepared food or lodging** -- NEVER use the 5.50% rate for prepared food or lodging -- they have higher rates (8% prepared food, 9% lodging).  _(Section 10 -- Prohibitions)_
- **Prohibition on forgetting short-term auto rental rate** -- NEVER forget the 10% short-term auto rental rate.  _(Section 10 -- Prohibitions)_
- **Prohibition on computing numbers** -- NEVER compute any number.  _(Section 10 -- Prohibitions)_

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Checked examples

```oa-check
name: Prepared food at 8%
inputs:
  sale: 100
steps:
  - tax: sale * 0.08
expected:
  tax: 8.00
```

```oa-check
name: Short-term auto rental at 10%
inputs:
  rental: 300
steps:
  - tax: rental * 0.10
expected:
  tax: 30.00
```

## Sources

1. 36 MRSA s.1811(1)(D), read 2026-11-01 -- https://legislature.maine.gov/statutes/36/title36sec1811.html
2. 36 MRSA s.1754-B(1-B)(B) and (K), read 2026-11-03 -- https://legislature.maine.gov/statutes/36/title36sec1754-B.html (the earlier transaction-count test was removed by PL 2021, c.181, Pt. B, ss.4 and 5, for sales from 1 January 2022; LD 1216 fiscal summary, 130th Legislature: https://legislature.maine.gov/doc/6615)

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-03. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `me-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/me-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
