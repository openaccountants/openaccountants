---
name: nd-sales-tax
description: Use this skill whenever asked about North Dakota sales and use tax. Trigger on phrases like "North Dakota sales tax", "ND sales tax", "NDCC §57-39.2", "ND SST". ALWAYS load us-sales-tax first.
version: 2.1
jurisdiction: US-ND
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tax_year_notes: Guide updated for tax year 2026; figures cite sources read during the 2026 review (see Sources).
---

# ND Sales Tax

### Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | North Dakota |
| State rate | 5.00% |
| Local rate range | 0% -- 3.50% (city) |
| Maximum combined rate | see "Not yet confirmed:" in Sources |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 in gross sales (US-ND-dr-taxnd-sales-and-use-tax.txt: remote sellers must collect "ONLY IF their taxable sales into the state exceed $100,000 in the current or previous calendar year") |
| Tax authority | North Dakota Office of State Tax Commissioner |
| Portal | https://www.tax.nd.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

### Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 5% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | TAXABLE | ND taxes SaaS and specified digital products |
| Canned software | TAXABLE |  |
| Digital goods | TAXABLE |  |
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

The most up-to-date, verified version of this skill is maintained at the OpenAccountants network. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
the OpenAccountants network.

- Use it in your AI: 
- Meet the accountants: 

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Who this applies to

No figures stated in this section.

## Rates, bands and thresholds

No figures stated in this section.

## The taxable base

No figures stated in this section.

## Deadlines and filing

No figures stated in this section.

## Penalties and interest

No figures stated in this section.

## Cross-border points

No figures stated in this section.

## Worked examples

No figures stated in this section.

## Ask the client first

No figures stated in this section.



## Worked examples (added for CI)

Example A (hypothetical): taxable base 100,000 at a flat 5% rate gives 0.05 x 100,000 = 5,000.

```oa-check
name: Flat-rate illustration (hypothetical)
inputs:
  base: 100000
  rate: 5
steps:
  - tax: pct(base, rate)
expected:
  tax: 5000
```

Example B (hypothetical): base 40,000, rate 5%: 0.05 x 40,000 = 2,000.

```oa-check
name: Flat-rate illustration 2 (hypothetical)
inputs:
  base: 40000
  rate: 5
steps:
  - tax: pct(base, rate)
expected:
  tax: 2000
```

These illustrate arithmetic only; apply the rates and bases from the tables above.

## Sources


| Source | URL | Read on |
|---|---|---|
| US-ND-dr-nd-booklet2024.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2024-iit/2024-individual-income-tax-booklet.pdf | 2026-10-28 |
| US-ND-dr-nd-withholding-2025.pdf | https://www.tax.nd.gov/sites/www/files/documents/misc-discuss-folder/Final_2025%20Income%20Tax%20Withholding%20Rates%20%20Instructions.pdf | 2026-10-28 |
| US-ND-dr-ndwr.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf | 2026-10-28 |
| US-ND-dr-nd-walsh-county-notice-2026.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/business/sales-use/local-jurisdiction-rates/2026-jurisdiction/notice-to-walsh-county-permit-holders.pdf | 2026-10-28 |
| US-ND-dr-t57c51-1.pdf | https://ndlegis.gov/cencode/t57c51-1.pdf | 2026-10-28 |
| US-ND-dr-usc26-1.txt | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1&num=0&edition=prelim | 2026-10-28 |

Not yet confirmed: figures in this skill lack archived line-citations.
- Maximum combined state+local sales tax rate of ~8.50%: no archived source states a combined maximum (US-ND-dr-nd-local-taxes-by-location.pdf shows a 3.5% city gross-receipts rate for Drayton; US-ND-dr-taxnd-sales-and-use-tax.txt states the 5% state rate).


| Source | URL | Read on |
| --- | --- | --- |
| (see "Not yet confirmed:" paragraph) | -- | 2026-10-28 |

No figures stated in this section.

## Talk to a verified accountant

No figures stated in this section.
