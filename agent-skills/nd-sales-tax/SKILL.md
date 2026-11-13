---
name: nd-sales-tax
description: "Use this skill whenever asked about North Dakota sales and use tax. Trigger on phrases like \"North Dakota sales tax\", \"ND sales tax\", \"NDCC §57-39.2\", \"ND SST\". ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nd-sales-tax"
  jurisdiction: "US-ND"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# ND Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | North Dakota |
| State rate | 5.00% | https://ndlegis.gov/cencode/t57c39-2.pdf (57-39.2-02.1) |
| Local rate range | 0% -- 3.50% (city) |
| Maximum combined rate | ~8.50% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 in gross sales delivered into ND in the previous or current calendar year; no transaction count test | https://ndlegis.gov/cencode/t57c39-2.pdf (57-39.2-02.2) |
| Tax authority | North Dakota Office of State Tax Commissioner |
| Portal | https://www.tax.nd.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 5% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| Canned software | TAXABLE | Sale, lease or rental of prewritten software, including software delivered electronically or by load and leave (N.D.C.C. 57-39.2-02.1(1)(g)) |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Prohibition -- SaaS taxability** -- NEVER treat SaaS as nontaxable in North Dakota.  _(Section 10 -- Prohibitions)_
- **Prohibition -- computation** -- NEVER compute any number.  _(Section 10 -- Prohibitions)_

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

Not yet confirmed: whether remotely accessed software (SaaS) and digital goods such as downloads and streaming are taxable. Chapter 57-39.2 as read on 2026-11-13 lists prewritten software delivered electronically as taxable but contains no provision on remote access or specified digital products, so the earlier "TAXABLE" rows for SaaS and digital goods were removed until a Tax Commissioner source is found.

## Worked examples (oa-check)

Example A: a $1,000 taxable sale at the 5% state rate before local tax gives $50.00 of state tax. Example B: a remote seller with $120,000 of gross sales delivered into North Dakota in 2025 exceeds the $100,000 threshold by $20,000 and must hold a permit and collect from the earlier of 1 January 2026 or 60 days after the threshold was met.

```oa-check
name: ND state sales tax 5% on 1,000
inputs:
  price: 1000
steps:
  - state_tax: pct(price, 5)
expected:
  state_tax: 50.00
```

```oa-check
name: ND remote seller threshold test
inputs:
  prior_year_sales: 120000
steps:
  - excess: max(prior_year_sales - 100000, 0)
expected:
  excess: 20000
```


## Sources

| # | Source | URL | Read on |
| --- | --- | --- | --- |
| 1 | N.D.C.C. chapter 57-39.2 (57-39.2-02.1 rate and taxable items, 57-39.2-02.2 remote sellers) | https://ndlegis.gov/cencode/t57c39-2.pdf | 2026-11-13 |

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nd-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nd-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
