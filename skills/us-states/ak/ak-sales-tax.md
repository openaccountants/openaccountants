---
name: ak-sales-tax
description: Use this skill whenever asked about Alaska sales and use tax. Trigger on phrases like "Alaska sales tax", "AK sales tax", "Alaska local sales tax", "ARSSTC", "Alaska Remote Seller Sales Tax Commission", "Alaska economic nexus", "do I charge sales tax in Alaska". ALWAYS load us-sales-tax first.
version: 1.0
jurisdiction: US-AK
tax_year: 2026
tax_year_notes: Local rates cite the ARSSTC rate sheet effective 2025-12-01, the current sheet for 2026; no statewide rate exists.
last_updated: 2026-11-04
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - us-sales-tax
category: state
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AK Sales Tax

## Who this applies to

Sole proprietors and small sellers in Alaska, and remote sellers shipping into Alaska. Alaska is one of five U.S. states with **no statewide sales tax** (the others are Delaware, Montana, New Hampshire, and Oregon). It is also one of the states with **no individual income tax**. For a sole proprietor, that means:

- **Income side:** federal return only. There is no Alaska personal income tax return. The Alaska Permanent Fund Dividend (PFD) is taxable on the **federal** return but has no Alaska income-tax consequence.
- **Sales side:** there is no state sales tax, but **local jurisdictions (boroughs and incorporated cities) may levy their own sales tax.** Some areas levy none (the ARSSTC member-rate sheet shows no general sales tax for the Fairbanks North Star Borough itself), while many communities do (e.g., Juneau 5%, Sitka 5%, Nome 5%, Wasilla 2.5%, Kodiak City 7%).

There is therefore no single "Alaska rate." The rate, base, exemptions, and filing cadence are set by **each municipality**.

### Quick reference

| Field | Value |
| --- | --- |
| Jurisdiction | Alaska |
| State sales tax rate | None (no statewide sales tax levied) |
| State individual income tax | None |
| Local sales tax | Yes -- levied by boroughs and cities only |
| Local rate range | 2% -- 7.85% combined total (ARSSTC rate sheet effective 12-1-2025; single-jurisdiction levies run 1% -- 7%) |
| Sourcing | Destination-based for remote sellers (ARSSTC Uniform Code) |
| Remote-seller administrator | Alaska Remote Seller Sales Tax Commission (ARSSTC) |
| Economic nexus | $100,000 statewide gross sales (current or prior calendar year) |
| 200-transaction threshold | Repealed effective January 1, 2025 |
| Marketplace facilitators | Must register and collect/remit to ARSSTC once the threshold is met |
| Skill version | 1.0 |

## Rates, bands and thresholds

- **State sales tax rate** -- None; Alaska levies no statewide sales tax
- **Local rate range** -- combined borough + city totals range from 2% (e.g., Aniak) to 7.85% (Homer City, under Kenai Peninsula Borough: 3% borough + 4.85% city) per the ARSSTC rate sheet effective 12-1-2025. Single-jurisdiction levies range from 1% to 7% across the 107 municipalities reporting a general sales tax, with "typical" rates of 2% to 5% per Alaska Tax Facts. Levied by boroughs and incorporated cities only.
- **Economic nexus threshold for remote sellers** -- $100,000 USD statewide gross sales in the current or previous calendar year, from property, products or services delivered in Alaska, including the seller's marketplace facilitator's statewide gross sales
- **200-transaction threshold elimination** -- The transaction thresholds were repealed effective January 1, 2025 (Uniform Code Section 040(A)) -- the $100,000 dollar threshold is now the only test.
- **Statewide measurement** -- The threshold is measured against statewide sales into all Alaska jurisdictions combined, not per-municipality.
- **Marketplace facilitators** -- Marketplace facilitators with economic nexus into Alaska must collect and remit local sales taxes to the ARSSTC; their statewide gross sales count toward the remote seller's $100,000 threshold measurement.

### Two collection regimes

- **In-state sellers (physical presence in a municipality)** -- Register directly with the local municipality where you have a physical location and collect that municipality's tax under its local code.
- **Remote sellers (no physical presence)** -- Register once with the Alaska Remote Seller Sales Tax Commission (ARSSTC), which administers a single Uniform Code on behalf of participating municipalities. File one consolidated return through the ARSSTC portal; tax is sourced to the buyer's delivery location (destination-based) using each member jurisdiction's rate and exemptions.

## The taxable base

Because the base is set locally, treat the following as **defaults to verify against the specific municipality's code**:

| Pattern | Typical treatment | Notes |
| --- | --- | --- |
| General tangible goods | TAXABLE at local rate | Only where a local tax exists |
| Grocery / unprepared food | Often EXEMPT | Many municipalities exempt; some do not |
| Professional services | Often TAXABLE | Several Alaska municipalities tax services |
| SaaS / digital goods | Verify locally | Treatment varies by municipality |
| Resale | EXEMPT with certificate | Per local code |
| Sales above a price cap | Partially exempt | Some municipalities cap taxable amount per sale |

## Deadlines and filing

- **In-state sellers** -- physical-presence sales are remitted directly to the jurisdiction where the physical location sits, not through the ARSSTC system; register with that municipality on its own cadence.
- **Remote sellers** -- register with ARSSTC within 30 days of meeting the economic threshold; submit one filing template covering all member jurisdictions through the filing portal (https://arsstc.munirevs.com/); file monthly unless otherwise arranged with ARSSTC, and file even when no tax was collected in the period. Sellers under $100,000 taxable dollars or 12 transactions annually statewide may qualify for reduced filing frequency. Keep sales and exemption records for three years.
- Filing cadences for in-state sellers are set by each municipality; confirm the current calendar with the relevant borough/city or ARSSTC.

## Penalties and interest

Penalty and interest rules are set by each municipality's code and by the ARSSTC Uniform Code for remote sellers; the ARSSTC filing software calculates sales tax, timely filing compensation, penalties and interest. Specific penalty and interest amounts are listed in the not-yet-confirmed note at the end of this guide. Confirm late-filing and late-payment consequences with the relevant borough/city or ARSSTC before advising a client.

## Cross-border points

- Remote sellers with no physical presence in Alaska still owe local sales tax via ARSSTC once the statewide economic-nexus threshold is met.
- Tax is sourced to the buyer's delivery location (destination-based) under the ARSSTC Uniform Code.
- NEVER assume "no sales tax in Alaska" for a remote seller -- local tax applies via ARSSTC once the threshold is met.

## Worked examples

Alaska has no statewide rate; the examples below use single-jurisdiction rates from the ARSSTC rate sheet effective 2025-12-01 (read 2026-11-01). Hypothetical client facts.

Example 1: a remote seller delivers goods to a customer in Juneau. Juneau levies 5%. On a $1,000 sale the local tax is 0.05 x 1,000 = $50, collected and remitted through ARSSTC.

```oa-check
name: Remote sale delivered to Juneau (hypothetical)
inputs:
  sale: 1000
  rate: 5
steps:
  - tax: pct(sale, rate)
expected:
  tax: 50
```

Example 2: a sale delivered to Kodiak City (7%). On the same $1,000 sale the local tax is 0.07 x 1,000 = $70.

```oa-check
name: Sale delivered to Kodiak City (hypothetical)
inputs:
  sale: 1000
  rate: 7
steps:
  - tax: pct(sale, rate)
expected:
  tax: 70
```

Confirm the current rate with the specific municipality or the ARSSTC member-rate table before filing.

## Ask the client first

- Where is the buyer's delivery location, and does that borough/city levy a sales tax?
- Is the seller physically present in an Alaska municipality, or selling remotely?
- Have statewide sales into Alaska reached the economic-nexus threshold in the current or prior calendar year?
- Are sales made through a marketplace that already collects and remits?

### Prohibitions

- **Prohibition: single statewide rate assumption** -- NEVER assume a single statewide Alaska sales-tax rate -- there is none.
- **Prohibition: assuming no sales tax for remote sellers** -- NEVER assume "no sales tax in Alaska" for a remote seller -- local tax applies via ARSSTC once the $100,000 threshold is met.
- **Prohibition: 200-transaction test after 2025** -- NEVER apply the 200-transaction test for periods on or after January 1, 2025.
- **Prohibition: computing numbers** -- NEVER compute any number; confirm the rate and base with the specific municipality or the ARSSTC member-rate table.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| ARSSTC Sales Tax Rate Sheet effective 12-1-2025 (member jurisdiction rates) | https://arsstc.org/wp-content/uploads/2025/11/ARSSTC-Sales-Tax-Rate-Sheet-12-1-25.xlsx | 2026-11-01 |
| ARSSTC notice: Remote Sales -- Repeal of Transaction Thresholds (effective January 1, 2025) | https://arsstc.org/wp-content/uploads/2024/09/Threshold-Change-for-Sellers.pdf | 2026-11-01 |
| ARSSTC For Businesses/Sellers (registration, physical presence, filing duties) | https://arsstc.org/business-sellers/ | 2026-11-01 |
| ARSSTC FAQs for Sellers | https://arsstc.org/faqs-for-sellers/ | 2026-11-01 |
| Alaska Tax Facts (Office of the State Assessor) | https://www.commerce.alaska.gov/web/dcra/officeofthestateassessor/alaskataxfacts.aspx | 2026-11-01 |

Not yet confirmed: the specific penalty and interest amounts and rates under individual municipal codes and the ARSSTC Uniform Code; the filing cadence and deadlines for in-state sellers in each municipality; per-municipality taxable-base, exemption, and price-cap detail; whether a marketplace seller selling only through marketplace facilitator platforms must register separately with the ARSSTC; whether the Municipality of Anchorage levies a general sales tax (Anchorage does not appear on the archived ARSSTC member-rate sheet).

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Local Alaska sales-tax rules are set by individual municipalities and change frequently; always confirm the current rate, base, and filing rules with the relevant borough or city, or with ARSSTC for remote sellers. All outputs must be reviewed and signed off by a qualified professional before filing.

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

<!-- openaccountants-cta-block -->
