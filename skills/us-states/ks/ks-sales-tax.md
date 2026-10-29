---
name: ks-sales-tax
description: Use this skill whenever asked about Kansas sales and use tax. Trigger on phrases like "Kansas sales tax", "KS sales tax", "KDOR", "K.S.A. §79-3603", "Kansas grocery tax". ALWAYS load us-sales-tax first.
version: 2.3
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# KS Sales Tax

> **Source-cited draft.** Built from K.S.A. 79-3603, 79-3603d, 79-3606, 79-3615 and 79-2968 (Kansas Revisor / kslegislature.gov) and KDOR sales-tax pages, read on 2026-10-28. No accountant has reviewed it. Do not file from it without review by a qualified Kansas professional.

Tax year: the calendar year. Authority: Kansas Department of Revenue (KDOR). Governing act: the Kansas Retailers' Sales Tax Act (K.S.A. 79-3603 and the sections cited below).

See also: `us-sales-tax` (load first), `ks-corporate-income-tax`, `ks-cross-border`.

## Who this applies to

- **Every retailer** selling tangible personal property at retail in Kansas, or furnishing services taxable under the act, must collect the tax: "there is hereby levied and there shall be collected and paid a tax at the rate of 6.5%" (K.S.A. 79-3603).
- **Sellers of food and food ingredients** collect at the reduced rates under K.S.A. 79-3603d (see Rates below).
- **Remote and out-of-state sellers**: a retailer with more than $100,000 of cumulative gross receipts from sales to Kansas customers in the current or preceding calendar year is a retailer doing business in Kansas and must collect (K.S.A. 79-3702(h)(1)(G)). See Cross-border points.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| State rate, general tangible personal property and taxable services | **6.5%** | 2026 | [K.S.A. 79-3603](https://ksrevisor.gov/statutes/chapters/ch79/079_036_0003.html) |
| Food and food ingredients, unprepared | **0%** state (4% from Jan 1, 2023; 2% from Jan 1, 2024; 0% from Jan 1, 2025 "and thereafter") | 2026 | [K.S.A. 79-3603d](https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_036_0000_article/079_036_0003d_section/079_036_0003d_k/) |
| Prepared food | Stays at the full 79-3603 rate unless sold without eating utensils and meeting a 79-3603d(b) condition | 2026 | K.S.A. 79-3603d(b) |
| Late-filing / late-payment penalty | **1% of the unpaid balance per month or fraction thereof, not exceeding 24% in the aggregate** | 2026 | [K.S.A. 79-3615](https://ksrevisor.gov/statutes/chapters/ch79/079_036_0015.html) |
| Economic-nexus threshold, remote sellers | More than **$100,000** of cumulative gross receipts from sales to Kansas customers in the current or immediately preceding calendar year | 2026 | [K.S.A. 79-3702(h)(1)(G)](https://ksrevisor.gov/statutes/chapters/ch79/079_037_0002.html) |
| Interest on unpaid tax | The federal IRC § 6621(a)(2) underpayment rate in effect on July 1 of the preceding year, **plus one percentage point** (the statute reads § 6621 as in effect on September 1, 1996) | 2026 | [K.S.A. 79-2968](https://ksrevisor.gov/statutes/chapters/ch79/079_029_0068.html) |

Local sales taxes are added on top of the state rate; local rate tables are on the KDOR sales-tax rate-change page (see Sources). The maximum combined state-plus-local rate is **not yet confirmed**, see Not yet confirmed.

## The taxable base

- **Base is gross receipts** from retail sales of tangible personal property and from taxable services (K.S.A. 79-3603; 79-3603d for food).
- **Food and food ingredients (unprepared):** taxed at 0% state from January 1, 2025 (K.S.A. 79-3603d(a)(3)). Local rates still apply. NEVER forget the phase-down history: 6.5% → 4% (2023) → 2% (2024) → 0% (2025 onward).
- **Prepared food carve-out:** the 79-3603d reduced rates "shall not apply to prepared food unless sold without eating utensils provided by the seller and described below", bakery items, unheated food sold by weight or volume as a single item, and food that ordinarily requires additional cooking (K.S.A. 79-3603d(b)). Prepared food sold with eating utensils stays at the full 6.5% state rate.
- **Exemptions confirmed in K.S.A. 79-3606 include:**
  - Prescription drugs: "all sales of drugs dispensed pursuant to a prescription order by a licensed practitioner" (79-3606(p)).
  - Manufacturing machinery: "all sales of machinery and equipment that are used in this state as an integral or essential part of an integrated production operation by a manufacturing or processing plant or facility" (79-3606(kk)).
  - Ingredient / component part: property that becomes "an ingredient or component part of tangible personal property or services produced, manufactured or compounded for ultimate sale at retail" (79-3606(m)).
- **Not yet confirmed:** the taxability of clothing, canned/downloaded software, SaaS, professional services, and general sales for resale, see Not yet confirmed before answering a client question on these.
- **Prohibition, grocery food state tax:** NEVER apply state tax to unprepared grocery food as of 2025, the state rate is 0%. Local tax may still apply.

## Deadlines and filing

- Returns and payment are due per the KDOR retailers' sales tax filing schedule; filing frequency depends on the taxpayer's tax liability. The exact current form IDs and filing frequencies are **not yet confirmed**, see Not yet confirmed.
- The KDOR sales and use tax page and rate-change notices are the authority for current filing mechanics (see Sources).

## Penalties and interest

- **Late return or late payment:** "there shall be added to the tax an additional amount equal to 1% of the unpaid balance of the tax due for each month or fraction thereof during which such failure continues, not exceeding 24% in the aggregate" (K.S.A. 79-3615(d), for taxable years ending after December 31, 2001).
- **Interest:** "there shall be added to the unpaid balance of the tax, interest at the rate per month prescribed by subsection (a) of K.S.A. 79-2968" (K.S.A. 79-3615(a)); 79-2968 sets the annual rate at the federal IRC § 6621(a)(2) underpayment rate in effect on July 1 of the preceding year, plus one percentage point.
- **Example:** a $500 balance left unpaid for 3 full months bears a penalty of 3 x 1% x $500 = $15, plus interest (K.S.A. 79-3615(d)).
- **Post-audit penalty cap:** where an assessment follows a field audit on a filed, fully paid return, the penalty is 1% per month not exceeding 10% of the unpaid balance (K.S.A. 79-3615, final paragraph).

## Cross-border points

- **Sourcing is destination-based** for retail sales other than leases: a sale is sourced to the seller's business location when the buyer receives the product there; otherwise to where the buyer (or the buyer's donee) receives it; then to the buyer's address in the seller's records, then to the address obtained at the sale ([K.S.A. 79-3670(a)](https://ksrevisor.gov/statutes/chapters/ch79/079_036_0070.html)). Local tax follows that location.
- **Remote sellers:** more than $100,000 of cumulative gross receipts from sales to Kansas customers in the current or preceding calendar year makes the seller a retailer doing business in Kansas; a seller crossing the line for the first time in the current year collects on sales above $100,000 (K.S.A. 79-3702(h)(1)(G)).
- Kansas membership of the Streamlined Sales Tax agreement is listed under Not yet confirmed.
- Sales for resale across state lines need an exemption certificate analysis (see ingredient/component exemption, 79-3606(m)).

## Worked examples

Client facts in these examples are hypothetical. Only rates from the confirmed table above are used.

### Example 1: general retail sale, state rate only

A Kansas retailer (hypothetical) sells $1,000 of furniture. The state tax is 6.5% of $1,000 = $65 (K.S.A. 79-3603). Local tax, if any, is additional and must be read from the KDOR rate tables.

```oa-check
name: KS state sales tax on general retail sale
inputs:
  sale: 1000
  state_rate: 0.065
steps:
  - state_tax: sale * state_rate
expected:
  state_tax: 65
```

### Example 2: grocery basket after the 2025 phase-down

A grocery store (hypothetical) sells $100 of unprepared food and food ingredients in 2026. The state rate is 0% (K.S.A. 79-3603d(a)(3)), so state tax is $0. Local rates, if any, are not confirmed here.

```oa-check
name: KS state sales tax on groceries 2026
inputs:
  sale: 100
  state_rate: 0.0
steps:
  - state_tax: sale * state_rate
expected:
  state_tax: 0
```

## Ask the client first

1. **What is being sold?** Tangible personal property, a taxable service, unprepared food (0% state), or prepared food (full rate unless a 79-3603d(b) condition applies)?
2. **Where does the buyer receive the goods?** Kansas sources to the place of receipt (K.S.A. 79-3670), which sets the local rate.
3. **Does the buyer hold an exemption certificate?** Prescription drugs, integrated-production machinery, and ingredient/component purchases are exempt under K.S.A. 79-3606.
4. **Is the seller an out-of-state/remote seller, and did its Kansas sales exceed $100,000 this year or last year?** (K.S.A. 79-3702(h)(1)(G)).
5. **What is the filing frequency and current return form?** Confirm on the KDOR sales-tax pages (not yet confirmed here).

## Sources

| Source | URL | Read on |
|---|---|---|
| K.S.A. 79-3603 (state rate 6.5%) | https://ksrevisor.gov/statutes/chapters/ch79/079_036_0003.html | 2026-10-28 |
| K.S.A. 79-3603d (food and food ingredients: 4% from 2023, 2% from 2024, 0% from Jan 1, 2025; prepared-food carve-out) | https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_036_0000_article/079_036_0003d_section/079_036_0003d_k/ | 2026-10-28 |
| K.S.A. 79-3606 (exemptions, incl. prescription drugs (p), integrated-production machinery (kk), ingredient/component part (m)) | https://ksrevisor.gov/statutes/chapters/ch79/079_036_0006.html | 2026-10-28 |
| K.S.A. 79-3615 (1% a month, up to 24% aggregate, plus interest; post-audit 10% cap) | https://ksrevisor.gov/statutes/chapters/ch79/079_036_0015.html | 2026-10-28 |
| K.S.A. 79-2968 (interest: IRC § 6621(a)(2) underpayment rate on July 1 of the preceding year plus one point) | https://ksrevisor.gov/statutes/chapters/ch79/079_029_0068.html | 2026-10-29 |
| K.S.A. 79-3702 (retailer doing business in Kansas; $100,000 remote-seller threshold in (h)(1)(G)) | https://ksrevisor.gov/statutes/chapters/ch79/079_037_0002.html | 2026-10-29 |
| K.S.A. 79-3670 (sourcing rules) | https://ksrevisor.gov/statutes/chapters/ch79/079_036_0070.html | 2026-10-29 |
| KDOR Sales (Retailers) tax page (6.5% state rate since July 1, 2015, plus local taxes) | https://www.ksrevenue.gov/bustaxtypessales.html | 2026-10-28 |
| KDOR sales tax rate changes | https://www.ksrevenue.gov/salesratechanges.html | 2026-10-28 |

Not yet confirmed: the maximum combined state and local rate (previously carried as ~11.50%; confirm against the KDOR rate-change page); Kansas's status as a Streamlined Sales Tax member; the current return form IDs (previously carried as ST-1/ST-10) and the Kansas Revenue Portal e-filing route (the KDOR form URLs tried returned 404 pages); the 2026 value of the K.S.A. 79-2968 interest rate; the taxability of clothing, SaaS, canned/downloaded software, professional services and sales for resale (previously carried in a transaction-pattern table as taxable/not taxable without archived sources); local sales-tax rates and the current filing-frequency schedule.

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
