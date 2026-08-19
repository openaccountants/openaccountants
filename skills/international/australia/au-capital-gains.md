---
name: au-capital-gains
description: "Use this skill for any Australian resident's capital gains tax question. Trigger on: \"CGT Australia\", \"capital gains Australia\", \"sell shares Australia\", \"50% CGT discount\", \"cost base Australia\", \"small business CGT concessions\", \"SBCGT\", \"active asset test\", \"15-year exemption\", \"retirement exemption CGT\", \"CGT rollover\", \"CGT event A1\", \"main residence exemption\", \"Australian CGT\", \"sell my Australian company\", \"dispose of property Australia\". Covers CGT events, cost base, 50% discount, SBCGT concessions, main residence exemption. For non-residents selling Australian assets see au-nonresident-cgt."
version: 1.1
jurisdiction: AU
tax_year: 2025
tax_year_notes: "2025-26; includes 1 July 2027 CGT reform alert (Tax Reform No. 1 Act 2026)"
last_updated: 2026-08-20
review_status: pending_review
depends_on: - au-individual-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Capital Gains

> **Law-change alert (passed June 2026, applies from 1 July 2027).** The *Treasury Laws Amendment (Tax Reform No. 1) Act 2026* replaces the 50% CGT discount for individuals, trusts and partnerships with **cost-base indexation plus a 30% minimum tax rate** for capital gains **accruing from 1 July 2027**. Assets held on 30 June 2027 (including pre-CGT assets) are deemed sold and re-acquired on 1 July 2027, splitting every later disposal into pre- and post-1-July-2027 gain components across four asset-based categories (residential vs non-residential × pre vs post). The 50% discount is retained for **new residential dwellings**; the small business 50% active-asset reduction is being expanded (announced: turnover test $2m → $10m). Everything below describes the law that still applies to gains accruing **up to 30 June 2027** — for disposals after that date, or timing decisions straddling it, escalate to a qualified adviser and check the current ATO guidance.

## Section 1 — Quick Reference

**Section 1 — Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia |
| Tax year | 1 July 2024 – 30 June 2025 |
| CGT rate | No separate rate — net capital gain added to taxable income, taxed at marginal rate |
| Effective max rate | ~23.25% (47% marginal × 50% discount, for assets held >12 months) |
| 50% general discount | Yes — assets held >12 months by individuals and trusts |
| Annual exemption | None (unlike UK) |
| Primary legislation | ITAA 1997, Parts 3-1 and 3-3 |
| Tax authority | Australian Taxation Office (ato.gov.au) |
| Form | Schedule 3 attached to Individual Tax Return (ITR) |
| Verified by | Pending — Australian CPA/CA sign-off required |

## Section 2 — What Triggers CGT

CGT applies when a **CGT event** occurs. The most common:

**CGT Events**

| Event | What it is |
| --- | --- |
| A1 | Disposal of a CGT asset (sale, gift, transfer) |
| B1 | Use and enjoyment before title passes |
| C1 | Loss/destruction of asset |
| C2 | Cancellation, surrender, expiry of a right/option |
| D1 | Creation of contractual/statutory rights over asset |
| G1 | Return of capital exceeding cost base |

- **CGT assets** — shares, units, land, buildings, goodwill, rights, options, crypto assets, foreign currency (above threshold)
- **Exempt assets** — main residence (principal private residence, PPR), motor vehicles, personal-use assets acquired for <$10,000, certain compensation amounts

## Section 3 — Capital Gain Calculation

- **Capital gain formula** — Capital gain = Capital proceeds − Cost base
- **Cost base (5 elements)** — 1. Original acquisition cost 2. Incidental acquisition costs (stamp duty, legal fees, brokerage) 3. Non-deductible ownership costs (e.g. rates, insurance on investment property) 4. Capital expenditure to increase/preserve value 5. Incidental disposal costs (agent fees, legal fees)
- **Reduced cost base** — used to calculate capital losses = elements 1, 2, 4, 5 only (not 3)
- **Capital loss treatment** — Capital loss: if proceeds < reduced cost base. Losses can only be offset against capital gains (not other income). Unused losses carry forward indefinitely.

## Section 4 — The 50% General Discount

- **50% general discount eligibility** — If an individual (or trust) holds a CGT asset for more than 12 months before disposal, only 50% of the capital gain is included in taxable income.
- **Discounted capital gain formula** — Discounted capital gain = Capital gain × 50%
- **12-month clock** — The 12-month clock starts the day AFTER acquisition and ends on the day of disposal
- **Discount mechanics** — The discount reduces the gain, not the tax rate
- **Order of application** — Discount is applied AFTER offsetting capital losses
- **Companies exclusion** — Does NOT apply to companies (companies pay 30% or 25% on full gain)
- **Non-residents exclusion** — Does NOT apply to non-residents (since 8 May 2012)

## Section 5 — Small Business CGT Concessions (SBCGT)

Four concessions apply if the taxpayer satisfies the basic conditions:

- **Basic conditions** — 1. Net assets do not exceed $6 million (including related party assets), OR 2. Aggregated turnover < $2 million (small business entity) 3. Asset is an active asset: used in the business for at least half the ownership period (or 7.5 years if held >15 years)

The four concessions (can be combined):

**The four concessions**

| Concession | What it does | Conditions |
| --- | --- | --- |
| 15-year exemption | Entire gain exempt from CGT | Asset held ≥15 years + taxpayer aged ≥55 and retiring, or permanently incapacitated |
| 50% active asset reduction | Reduce capital gain by 50% | Basic conditions only |
| Retirement exemption | Exempt up to $500,000 lifetime | Must be contributed to super if under 55 |
| Small business rollover | Defer gain up to 2 years | Must acquire replacement asset or incur capex within 2 years |

- **Stacking concessions** — Stacking concessions: 50% discount → 50% active asset reduction → retirement/rollover can apply to the remaining amount. Effective rate on a large gain can approach zero if all concessions apply.

## Section 6 — Main Residence (PPR) Exemption

- **Main residence exemption** — A dwelling that is the taxpayer's main residence throughout ownership is fully CGT-exempt.
- **Partial exemptions apply when** — - Dwelling used for income-producing purposes for part of ownership - Dwelling was not main residence for part of the period (e.g. rented out) - Adjacent land exceeds 2 hectares
- **6-year absence rule** — If you move out but do not nominate another property as main residence, you can treat the dwelling as your main residence for up to 6 years (while renting it out). Resets each time you move back in.

## Section 7 — CGT and Foreign Assets

- **Worldwide gains taxed** — Australian tax residents are taxed on worldwide capital gains, including gains on: - Foreign shares - Foreign real property - Foreign businesses
- **Foreign tax credits** — Foreign tax credits available for foreign CGT paid on the same gain (Form IT 1205 / Schedule 25A).
- **Exit CGT** — When you cease to be an Australian tax resident, you are treated as having disposed of most CGT assets at market value on the day before you stop being a resident. Exception: taxable Australian property (TAP) — no deemed disposal, but AU retains taxing rights when actually sold.

## Section 8 — Sources

- ITAA 1997 Part 3-1 (CGT events), Part 3-3 (CGT concessions), Div 152 (SBCGT)
- ATO: ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax
- ATO CGT Guide 2025

> **Working paper only — not a filed return.** Have a qualified Australian CPA/CA review before filing. SBCGT eligibility requires detailed analysis of the active asset test and aggregated turnover.

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
