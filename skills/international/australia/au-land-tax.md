---
name: au-land-tax
description: >
  Use this skill whenever asked about Australian state or territory land tax.
  Trigger on phrases like "land tax", "unimproved value", "site value",
  "land tax threshold", "principal place of residence exemption",
  "foreign owner surcharge", "absentee owner surcharge",
  "land tax objection", "Valuer-General", "surcharge land tax",
  "land tax deductible", or any question about annual state taxes on land
  ownership in NSW, VIC, QLD, SA, WA, TAS, ACT, or NT. Covers the nature of
  land tax, aggregation, thresholds and rates by state, surcharges, trusts,
  companies, exemptions, objections, GL treatment, and deductibility.
  ALWAYS read this skill before advising on Australian land tax.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026 land tax year (1 Jan 2026 or 30 Jun 2025 ownership date per state)"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Land Tax

## Australia -- State & Territory Land Tax Skill v1.0

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax | Land tax (state/territory annual tax on land ownership) |
| Currency | AUD only |
| Tax year | Calendar year (1 Jan) or financial year (1 Jul) depending on state |
| Primary legislation | State Land Tax Acts (e.g. Land Tax Act 1956 (NSW), Land Tax Act 2005 (VIC)) |
| Tax authorities | Revenue NSW; SRO Victoria; QRO Queensland; RevenueSA; RevenueWA; SRO Tasmania; ACT Revenue Office |
| Valuation authority | Valuer-General of each state/territory |
| Assessment basis | Unimproved value (NSW, WA) or site value (VIC, SA, TAS) or average unimproved value (ACT) of freehold land |
| Filing portal | State revenue office online portals |
| Skill version | 1.0 |

### 2025-26 Land Tax Thresholds & Base Rates (Summary)

**2025-26 Land Tax Thresholds & Base Rates (Summary)**

| State/Territory | Assessment Date | Threshold (General) | Base Rate Above Threshold | Foreign/Absentee Surcharge |
| --- | --- | --- | --- | --- |
| NSW | 31 December | $1,075,000 | $100 + 1.6% above threshold | 5% (foreign owner surcharge) |
| VIC | 31 December | $50,000 | Tiered flat + % | 4% (absentee owner surcharge) |
| QLD | 30 June | $600,000 (individual) / $350,000 (company/trust/absentee) | $500 + 1c per $1 above (individuals); absentees use a separate scale from $1,450 + 1.7c | 3% (absentee/foreign surcharge) |
| SA | 30 June | **$936,000 (general, 2026-27, in force from 1 Jul 2026)** / $25,000 (trust). 2025-26: $833,000 | $0.50 per $100 above the threshold | None (SA's foreign surcharge applies to duty, not land tax) |
| WA | 30 June | $300,000 | $300 flat then 0.25% above $420,000 | None |
| TAS | 1 July | $125,000 | $50 + 0.45% above | 2% (foreign investor land tax surcharge) |
| ACT | Quarterly (1 Jul, 1 Oct, 1 Jan, 1 Apr) | No threshold (residential only) | Fixed charge + AUV rating factor | 0.75% (foreign ownership surcharge) |
| NT | -- | No land tax | -- | -- |

**AUDIT FLASH POINT** -- The NSW foreign owner surcharge is 5% of unimproved value, charged in addition to general land tax. It applies to residential land owned by foreign persons. Verify foreign status via the Surcharge Assist Tool before advising.

## Section 2 -- The Nature of Land Tax

### 2.1 What Land Tax Is

- **Land tax** — An annual state/territory tax on the ownership of freehold land. It is levied on the unimproved value (or site value) of land, not the improved value (i.e. the value of buildings and structures is excluded).
- **Assessment date** — Liability is determined by ownership at a fixed date each year (31 December for NSW/VIC; 30 June for QLD/SA/WA; 1 July for TAS; quarterly for ACT).
- **No federal land tax** — The Commonwealth does not levy land tax. It is purely a state/territory revenue measure.

### 2.2 Land Tax vs Stamp Duty vs Council Rates

**Land Tax vs Stamp Duty vs Council Rates**

| Feature | Land Tax | Stamp Duty | Council Rates |
| --- | --- | --- | --- |
| What triggers it | Owning land at assessment date | Buying/acquiring land | Owning/occupying property |
| Frequency | Annual | One-off per transaction | Quarterly/annual |
| Basis | Unimproved/site value | Dutiable value (price paid) | Unimproved or improved value (council choice) |
| Levied by | State revenue office | State revenue office | Local council |
| Deductible against rental income | Yes (see Section 9) | Yes (cost base, not immediate deduction) | Yes |

### 2.3 How Land Value Is Determined

- **Valuer-General** — Each state/territory Valuer-General determines the unimproved value or site value of land. The valuation is conducted on a rolling cycle (annual in most states).
- **Unimproved value vs site value** — Unimproved value (NSW, WA) is the value of the land assuming no improvements. Site value (VIC, SA, TAS) is similar but may include some site works. ACT uses Average Unimproved Value (AUV) over up to 5 years.
- **Land component only** — Land tax is assessed on the land component only. The building, fixtures, and chattels are excluded from the valuation base.

## Section 3 -- Assessment Cycle & Payment Plans

The cycle: Valuer-General determines land value (annual); revenue office issues assessment notice (NSW Jan--Apr, VIC Jan--May, QLD Aug--Oct, SA Sep--Nov, WA Sep--Jan, TAS Oct--Dec, ACT quarterly); payment due 30--90 days from issue; 60-day objection window from notice issue in most states.

- **Payment plans** — All state revenue offices offer payment plans for land tax. Interest and penalty tax may apply to late payments. Contact the relevant revenue office before the due date to arrange.

## Section 4 -- Thresholds and Rates by State (2025-26)

### 4.1 New South Wales (NSW)

**NSW Land Tax Rates (2026 land tax year -- assessed 31 Dec 2025)**

| Land Value | Rate |
| --- | --- |
| Up to $1,075,000 | Nil |
| $1,075,001 to $6,571,000 | $100 + 1.6% of value above $1,075,000 |
| Above $6,571,000 | $87,070 + 2.0% of value above $6,571,000 |

- **Foreign owner surcharge** — 5% of unimproved value for foreign persons owning residential land. Charged in addition to general land tax.
- **Trusts** — Trustees are assessed at general rates but receive no tax-free threshold unless the trust is a fixed trust with a principal place of residence exemption.

### 4.2 Victoria (VIC)

**VIC Land Tax General Rates (2026 land tax year -- assessed 31 Dec 2025)**

| Total Taxable Value | Land Tax Payable |
| --- | --- |
| < $50,000 | Nil |
| $50,000 to < $100,000 | $500 |
| $100,000 to < $300,000 | $975 |
| $300,000 to < $600,000 | $1,350 + 0.3% of amount > $300,000 |
| $600,000 to < $1,000,000 | $2,250 + 0.6% of amount > $600,000 |
| $1,000,000 to < $1,800,000 | $4,650 + 0.9% of amount > $1,000,000 |
| $1,800,000 to < $3,000,000 | $11,850 + 1.65% of amount > $1,800,000 |
| $3,000,000 and over | $31,650 + 2.65% of amount > $3,000,000 |

**VIC Trust Surcharge Rates** -- $25,000 threshold; $82 + 0.375% above $25,000 to $50,000; then tiered up to $31,650 + 2.65% above $3,000,000.

- **Absentee owner surcharge** — 4% of site value for absentee owners. Charged in addition to general or trust rates.
- **Trusts** — Trustees pay trust surcharge rates (lower threshold of $25,000).

### 4.3 Queensland (QLD)

**QLD Land Tax Rates -- Individuals (2025-26 land tax year -- assessed 30 Jun 2025)**

| Total Taxable Value | Rate |
| --- | --- |
| $600,000 to $999,999 | $500 + 1c per $1 above $600,000 |
| $1,000,000 to $4,999,999 | $4,500 + 1.65c per $1 above $1,000,000 |
| $5,000,000 to $9,999,999 | $62,500 + 1.75c per $1 above $5,000,000 |
| $10,000,000 or more | $150,000 + 2.25c per $1 above $10,000,000 |

**QLD Companies & Trusts** -- $350,000 threshold; $1,450 + 1.7c per $1 above $350,000 to $2,249,999; then tiered up to $187,500 + 2.75c per $1 above $10,000,000.

- **Absentee/foreign surcharge** — **3%** applied as (taxable value − $350,000) × 3%, in addition to land tax, for absentee individuals (foreign individuals without a permanent visa who do not usually live in Australia), foreign companies and trustees of foreign trusts. Applies from $350,000 of taxable value. Absentees are also assessed on a separate rate scale ($1,450 + 1.7c per $1 above $350,000, rising to 2.5c above $10m) and cannot claim the home or primary production exemptions.  _(QRO Land tax rates for absentees)_
- **Trusts** — Trustees have a $350,000 threshold (same as companies). Special disability trusts use individual threshold ($600,000).

### 4.4 South Australia (SA)

**SA Land Tax General Rates (2025-26 land tax year -- assessed 30 Jun 2025)**

| Total Taxable Site Value | Amount of Tax |
| --- | --- |
| Up to $936,000 | Nil |
| $936,001 to $1,504,000 | $0.50 per $100 above $936,000 |
| $1,338,001 to $1,946,000 | $2,525 + $1.00 per $100 above $1,338,000 |
| $1,946,001 to $3,116,000 | $8,605 + $2.00 per $100 above $1,946,000 |
| $3,116,001 and over | $32,005 + $2.40 per $100 above $3,116,000 |

**SA Land Tax Trust Rates (2026-27)** -- $25,000 threshold; $125 + $0.50 per $100 above $25,000 to $936,000; then $4,680 + $1.00 per $100 above $936,000 to $1,504,000, tiering up at the top band. 2025-26 general threshold was $833,000; RevenueSA indexed thresholds 12.44% for 2026-27.

- **Trust threshold** — Trusts have a $25,000 threshold (no general tax-free threshold).
- **Foreign surcharge** — SA does not levy a foreign owner land tax surcharge; foreign purchasers pay a stamp duty surcharge instead.

### 4.5 Western Australia (WA)

**WA Land Tax Rates (2025-26 land tax year -- assessed 30 Jun 2025)**

| Aggregated Taxable Value | Rate |
| --- | --- |
| $0 to $300,000 | Nil |
| $300,001 to $420,000 | $300 |
| $420,001 to $1,000,000 | $300 + 0.25c per $1 above $420,000 |
| $1,000,001 to $5,000,000 | $1,750 + 0.65c per $1 above $1,000,000 |
| $5,000,001 to $11,000,000 | $28,000 + 1.8c per $1 above $5,000,000 |
| $11,000,001 and over | $186,550 + 2.67c per $1 above $11,000,000 |
- **Foreign surcharge** — WA does not levy a foreign owner land tax surcharge.

### 4.6 Tasmania (TAS)

**TAS Land Tax Rates (2025-26 land tax year -- assessed 1 Jul 2025)**

| Total Land Value | Rate |
| --- | --- |
| $0 to $124,999.99 | Nil |
| $125,000 to $499,999.99 | $50 + 0.45% of value above $125,000 |
| $500,000 and above | $1,737.50 + 1.5% of value above $500,000 |

- **Foreign investor land tax surcharge (FILTS)** — 2% of assessed land value for foreign investors. Charged in addition to general land tax.
- **Trusts** — Trustees pay the same rates as individuals.

### 4.7 Australian Capital Territory (ACT)

**ACT Land Tax Rates (2026-27 land tax year)**

| Component | Detail |
| --- | --- |
| Fixed charge | $1,778 (from 1 Jul 2026) |
| Variable charge | Rating factor applied to Average Unimproved Value (AUV) |

**ACT AUV Rating Factors** -- 0.54% up to $150,000; $810 + 0.64% above $150,000 to $275,000; $1,610 + 1.24% above $275,000 to $1,000,000; $10,600 + 1.25% above $1,000,000 to $2,000,000; $23,100 + 1.26% above $2,000,000.

- **Assessment basis** — Quarterly (1 Jul, 1 Oct, 1 Jan, 1 Apr). Applies to residential properties that are not the principal place of residence.
- **Foreign ownership surcharge** — 0.75% of AUV for foreign persons.

### 4.8 Northern Territory (NT)

- **No land tax** — The Northern Territory does not levy a general land tax. Stamp duty and council rates apply, but there is no annual land tax.

## Section 5 -- Aggregation Rules

- **Aggregation** — All land owned by the same entity (individual, company, trust) within a state is aggregated. The threshold applies to the total taxable value of all land holdings, not per property.
- **Joint ownership** — Each joint owner is assessed on their proportional share of the land value.
- **Cross-border holdings** — Land tax is state-based. A NSW resident owning property in QLD is assessed separately in each state. There is no national aggregation.

## Section 6 -- Trusts, Companies, and Individuals

- **Individuals** — Full threshold, general rates, PPR exemption available.
- **Companies** — Reduced or no threshold, company/trust rates, no PPR exemption.
- **Trusts** — Reduced threshold (VIC/SA $25,000; QLD $350,000; NSW/WA none unless fixed trust with PPR). Trust surcharge rates apply in VIC and SA. Special disability trusts use individual threshold in QLD.

## Section 7 -- Exemptions

### 7.1 Principal Place of Residence (PPR) Exemption

- **PPR exemption** — Owner-occupied principal place of residence is exempt in all states that levy land tax. The property must be the owner's main residence at the assessment date.
- **Moving out rule** — If the owner moves out and rents the property, the PPR exemption is lost from the next assessment date. Some states allow a limited absence (e.g. 6 years in NSW for CGT, but land tax has its own rules -- verify per state).
- **Deceased estate rule** — Most states allow a 2-year exemption period after the death of the owner, during which the deceased estate continues to receive the PPR exemption.

### 7.2 Primary Production Exemption

- **Primary production exemption** — Land used for primary production (farming, grazing, horticulture) is exempt or concessionally taxed in most states. Evidence of commercial farming activity is required.

### 7.3 Other Exemptions

Other exemptions include: residential tenancy/build-to-rent concessions (VIC, QLD, NSW); charitable and religious institutions (all states); retirement villages (most states); caravan parks (some states); Crown leasehold (ACT).

## Section 8 -- Objection Rights and Time Limits

- **Objection window** — 60 days from the issue date of the assessment notice in most states (NSW, VIC, QLD, SA, WA, TAS). ACT has its own objection process.
- **Grounds for objection** — Incorrect land value (object to Valuer-General), incorrect ownership details, incorrect exemption application, or incorrect aggregation.
- **Valuation objections** — Objections to the land value itself must be lodged with the Valuer-General, not the revenue office. The revenue office processes objections to the assessment calculation.
- **Late objections** — Late objections may be accepted with reasons, but discretion is limited. Lodge within the 60-day window.

## Section 9 -- Land Tax as a Deductible Expense

- **Deductibility** — Land tax paid on investment properties is fully deductible against rental income in the year it is paid. This applies to all states and territories.
- **Cross-reference** — See `au-rental-property` for the full rental property deduction schedule. Land tax is listed as a deductible expense under Section 2.3 of that skill.
- **PPR portion** — Land tax on a principal place of residence is NOT deductible (no income-producing purpose).
- **Timing** — Deduct when paid, not when assessed. If a payment plan is used, deduct each instalment in the year paid.

## Section 10 -- GL Sweep Table

**GL Sweep Table**

| Transaction | Debit | Credit | Notes |
| --- | --- | --- | --- |
| Land tax assessment received | Land Tax Expense (P&L) | Land Tax Payable (BS) | Book on receipt of assessment notice |
| Payment of land tax | Land Tax Payable (BS) | Bank (BS) | Clear liability |
| Valuation notice received | No journal | -- | Record in fixed asset register; update land value |
| Objection lodged | No journal | -- | Track as contingent reduction |
| Objection allowed (refund) | Bank (BS) | Land Tax Expense (P&L) | Reverse over-accrual |
| Objection allowed (credit) | Land Tax Payable (BS) | Land Tax Expense (P&L) | Reduce liability and expense |
| Foreign surcharge assessed | Land Tax Expense (P&L) | Land Tax Payable (BS) | Separate line item for surcharge |
| Payment plan instalment | Land Tax Payable (BS) | Bank (BS) | Track instalment schedule |

## Section 11 -- Worked Examples

### Example 1 -- Aggregated Portfolio Crossing the NSW Threshold

**Facts:** Individual owns two investment properties in NSW. Property A land value $800,000. Property B land value $600,000. Total $1,400,000.

Total aggregated land value $1,400,000; threshold $1,075,000; amount above threshold $325,000. Land tax = $100 + (1.6% x $325,000) = **$5,300**. Without aggregation, each property alone would be below the threshold.

### Example 2 -- PPR Exemption Saving (VIC)

**Facts:** Individual owns a home in Melbourne (site value $800,000) and lives in it as their principal place of residence.

Without PPR exemption: $2,250 + (0.6% x $200,000) = $2,250 + $1,200 = $3,450. With PPR exemption: **$0**. The exemption saves $3,450 per year.

### Example 3 -- Foreign Owner Surcharge (NSW)

**Facts:** Foreign person owns a residential investment property in NSW with unimproved value $1,200,000.

General land tax: $100 + (1.6% x $125,000) = $2,100. Foreign surcharge (5%): 5% x $1,200,000 = $60,000. **Total: $62,100**. The foreign surcharge dwarfs the general land tax. Foreign owners must also check FIRB approval and surcharge duty on acquisition.

### Example 4 -- Primary Production Claim (SA)

**Facts:** Individual owns a 50-hectare grazing property in SA with site value $950,000. The property is used for commercial sheep grazing.

Without primary production exemption (2026-27 threshold $936,000): 0.5% x ($950,000 - $936,000) = **$70**. With exemption: **$0**. (Under the 2025-26 threshold of $833,000 the same land attracted $585 -- indexation matters, so always confirm the year.) Evidence of commercial farming activity (ABN, income records, stocking rates) is required.

### Example 5 -- Trust Aggregation (TAS)

**Facts:** Trustee of a family trust owns two investment properties in TAS. Property A land value $400,000. Property B land value $220,000. Total $620,000.

First tier ($125,000 to $499,999.99): $50 + 0.45% x $375,000 = $1,737.50. Second tier: $1,737.50 + 1.5% x $120,000 = **$3,537.50**. The trust aggregates both properties.

## Section 12 -- Refusal Catalogue

**Refusal Catalogue**

| Code | Scenario | Refusal / Referral |
| --- | --- | --- |
| R-AU-LT-01 | Objections to land valuations | Refer to Valuer-General of the relevant state. Do not advise on valuation disputes. |
| R-AU-LT-02 | Trust deed land tax clauses | Legal advice required. Do not interpret trust deeds for land tax purposes. |
| R-AU-LT-03 | Cross-border land holdings | Complex multi-state aggregation rules apply. Refer to specialist. |
| R-AU-LT-04 | Primary production concessions requiring farming evidence | Requires ABN, income records, stocking rates, and business plans. Refer to specialist. |
| R-AU-LT-05 | Retirement village / charitable exemptions | Complex eligibility tests. Refer to specialist or revenue office ruling. |
| R-AU-LT-06 | Build-to-rent concessions | Complex eligibility and ongoing compliance. Refer to specialist. |
| R-AU-LT-07 | Deceased estate land tax beyond 2-year exemption | Estate administration and land tax interaction is complex. Refer to specialist. |
| R-AU-LT-08 | Foreign person status determination | FIRB and surcharge rules are complex. Use the Surcharge Assist Tool or refer to specialist. |

## Section 13 -- Provenance

**Provenance**

| Source | URL |
| --- | --- |
| Land Tax Act 1956 (NSW) | legislation.nsw.gov.au |
| Revenue NSW -- Land tax thresholds and rates | revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/thresholds-and-rates |
| Revenue NSW -- Surcharge land tax | revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/surcharge-land-tax |
| Land Tax Act 2005 (VIC) | legislation.vic.gov.au |
| SRO Victoria -- Land tax current rates | sro.vic.gov.au/about-us/rates-and-statistics/current-rates/land-tax-current-rates |
| Land Tax Act 2010 (QLD) | legislation.qld.gov.au |
| QRO -- Land tax | qro.qld.gov.au/land-tax |
| Land Tax Act 1936 (SA) | legislation.sa.gov.au |
| RevenueSA -- Rates and thresholds | revenuesa.sa.gov.au/landtax/rates-and-thresholds |
| Land Tax Assessment Act 2002 (WA) | legislation.wa.gov.au |
| RevenueWA -- Land tax assessment | wa.gov.au/organisation/department-of-treasury-and-finance/land-tax-assessment |
| Land Tax Act 2000 (TAS) | legislation.tas.gov.au |
| SRO Tasmania -- Rates of land tax | sro.tas.gov.au/land-tax/rates-of-land-tax |
| Rates Act 2004 (ACT) | legislation.act.gov.au |
| ACT Revenue Office -- How land tax is calculated | revenue.act.gov.au/rates-and-property-charges/land-tax/how-land-tax-is-calculated |
| NT Government -- Property taxes | nt.gov.au/property/land/buying-and-selling-land/land-taxes |

## Section 14 -- Prohibitions

- **Prohibitions** — NEVER advise on land tax without verifying the current threshold and rate from the state revenue office; NEVER confuse land tax with stamp duty or council rates; NEVER assume the PPR exemption applies without verifying occupancy at the assessment date; NEVER advise on trust land tax without confirming the trust type and threshold rules; NEVER calculate land tax per property -- always aggregate; NEVER advise foreign owners without checking FIRB status and surcharge rules; NEVER present land tax calculations as definitive -- always label as estimated and recommend verification against the revenue office calculator.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
