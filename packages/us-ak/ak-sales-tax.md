---
name: ak-sales-tax
description: Use this skill whenever asked about Alaska sales and use tax. Trigger on phrases like "Alaska sales tax", "AK sales tax", "Alaska local sales tax", "ARSSTC", "Alaska Remote Seller Sales Tax Commission", "Alaska economic nexus", "do I charge sales tax in Alaska". ALWAYS load us-sales-tax first.
version: 1.0
jurisdiction: US-AK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - us-sales-tax
category: state
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AK Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Alaska |
| State sales tax rate | 0% (no statewide sales tax) |
| State individual income tax | None |
| Local sales tax | Yes -- levied by boroughs and cities only |
| Local rate range | ~1% -- 7.5% (varies by municipality) |
| Sourcing | Destination-based for remote sellers (ARSSTC Uniform Code) |
| Remote-seller administrator | Alaska Remote Seller Sales Tax Commission (ARSSTC) |
| Economic nexus | $100,000 statewide gross sales (current or prior calendar year) |
| 200-transaction threshold | Removed effective January 1, 2025 |
| Marketplace facilitators | Must collect/remit on behalf of third-party sellers |
| State tax authority (income/corporate) | https://www.tax.alaska.gov |
| Remote-seller portal | https://arsstc.org |
| Skill version | 1.0 |

## Section 2 -- How Alaska sales tax actually works

Alaska is one of five U.S. states with **no statewide sales tax** (the others are Delaware, Montana, New Hampshire, and Oregon). It is also one of the states with **no individual income tax**. For a sole proprietor, that means:

- **Income side:** federal return only. There is no Alaska personal income tax return. The Alaska Permanent Fund Dividend (PFD) is taxable on the **federal** return but has no Alaska income-tax consequence.
- **Sales side:** there is no state sales tax, but **local jurisdictions (boroughs and incorporated cities) may levy their own sales tax.** Some large areas levy none (e.g., the Municipality of Anchorage and Fairbanks city have no general sales tax), while many smaller communities do (e.g., Juneau, Sitka, Kodiak, Nome, Wasilla, Kenai).

There is therefore no single "Alaska rate." The rate, base, exemptions, and filing cadence are set by **each municipality**.

## Section 3 -- Two collection regimes

- **In-state sellers (physical presence in a municipality)** — Register directly with the local municipality where you have a physical location and collect that municipality's tax under its local code.
- **Remote sellers (no physical presence)** — Register once with the Alaska Remote Seller Sales Tax Commission (ARSSTC), which administers a single Uniform Code on behalf of participating municipalities. File one consolidated return through the ARSSTC portal; tax is sourced to the buyer's delivery location (destination-based) using each member jurisdiction's rate and exemptions.

## Section 4 -- Economic nexus (remote sellers)

- **Economic nexus threshold for remote sellers** — $100,000 USD statewide gross sales (In the current or previous calendar year, delivered into Alaska)
- **200-transaction threshold elimination** — The former 200-transaction prong was eliminated effective January 1, 2025 -- the dollar threshold is now the only test.
- **Statewide measurement** — The threshold is measured against statewide sales into all Alaska jurisdictions combined, not per-municipality.
- **Marketplace facilitators** — Marketplace facilitators (Amazon, Etsy, etc.) collect and remit for their third-party sellers; sales made through a registered marketplace generally do not create a separate registration duty for the seller, but still count toward the seller's threshold measurement.

## Section 5 -- Transaction pattern library

Because the base is set locally, treat the following as **defaults to verify against the specific municipality's code**:

**Transaction pattern library**

| Pattern | Typical treatment | Notes |
| --- | --- | --- |
| General tangible goods | TAXABLE at local rate | Only where a local tax exists |
| Grocery / unprepared food | Often EXEMPT | Many municipalities exempt; some do not |
| Professional services | Often TAXABLE | Several Alaska municipalities tax services |
| SaaS / digital goods | Verify locally | Treatment varies by municipality |
| Resale | EXEMPT with certificate | Per local code |
| Sales above a price cap | Partially exempt | Some municipalities cap taxable amount per sale |

## Section 10 -- Prohibitions

- **Prohibition: single statewide rate assumption** — NEVER assume a single statewide Alaska sales-tax rate -- there is none.
- **Prohibition: assuming no sales tax for remote sellers** — NEVER assume "no sales tax in Alaska" for a remote seller -- local tax applies via ARSSTC once the $100,000 threshold is met.
- **Prohibition: 200-transaction test after 2025** — NEVER apply the 200-transaction test for periods on or after January 1, 2025.
- **Prohibition: computing numbers** — NEVER compute any number; confirm the rate and base with the specific municipality or the ARSSTC member-rate table.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Local Alaska sales-tax rules are set by individual municipalities and change frequently; always confirm the current rate, base, and filing rules with the relevant borough or city, or with ARSSTC for remote sellers. All outputs must be reviewed and signed off by a qualified professional before filing.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
