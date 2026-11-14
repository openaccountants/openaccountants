---
name: sg-zero-cgt
description: "Use this skill when asked about capital gains in Singapore for Year of Assessment 2026 and 2027. Trigger on CGT Singapore, capital gains Singapore, sell shares Singapore, Singapore no capital gains tax, investment gains Singapore, crypto gains Singapore, Singapore property gains, trading in properties, badges of trade Singapore, seller's stamp duty, SSD Singapore, dispose assets Singapore. Singapore has no capital gains tax, but gains from trading are income, and residential property sold soon after purchase bears seller's stamp duty (16%, 12%, 8%, 4% for property bought on or after 4 July 2025). Covers the capital versus trading test IRAS applies, shares and digital tokens, property and SSD."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sg-zero-cgt"
  jurisdiction: "SG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Singapore: no capital gains tax, and where gains are still taxed

> **General reference only.** The capital versus trading line is fact-specific. Have a qualified Singapore tax adviser review high-frequency or leveraged activity.

## Scope

Singapore does not tax capital gains. IRAS treats gains from selling a property, shares and financial instruments as generally not taxable, but gains from trading (buying and selling with a profit-seeking motive) are income under section 10(1)(a) of the Income Tax Act 1947. Separately, seller's stamp duty (SSD) under the Stamp Duties Act applies to residential property sold within a set holding period. Applies to residents and non-residents. Crypto trading as a business: `singapore-crypto-tax`. Rates on taxable income: `sg-income-tax`.

## Ask the client first

1. **What was sold**, when bought, when sold, price and market value.
2. **How often** the client buys and sells this kind of asset, and why this one was sold.
3. **How it was financed** and whether the client could have held it long term.
4. **Is buying and selling the client's business** or closely related to it (developer, dealer, trader)?
5. For residential property: **date of purchase** (decides the SSD table) and holding period.

## The method, step by step

1. **Start from capital.** IRAS: gains from selling a property in Singapore, and profits from buying and selling shares or other financial instruments (including digital tokens), are generally viewed as capital or personal investment and not taxed. Insurance payouts are capital receipts.
2. **Test for trading.** For property IRAS looks at: frequency of transactions; reasons for buying and selling; financial means to hold long term; holding period. The same badges of trade apply to shares and tokens (frequency, similarity to the taxpayer's business, holding period, borrowing, work done to the asset before sale).
3. **If trading**, the gain is income: report it under "Other Income" in the return (individuals) and tax it at the normal rates. If capital, it is not declared.
4. **Residential property SSD.** If bought on or after 4 July 2025 and sold within 4 years, SSD is due at the rate for the holding period on the higher of price and market value, rounded down to the dollar. Property bought earlier uses its own table.

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Capital gains tax | None | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/gains-from-sale-of-property-shares-and-financial-instruments |
| SSD, residential bought on or after 4 Jul 2025, held up to 1 year | 16% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-(ssd)-for-residential-property |
| Held more than 1 year, up to 2 years | 12% | same |
| Held more than 2 years, up to 3 years | 8% | same |
| Held more than 3 years, up to 4 years | 4% | same |
| Held more than 4 years | No SSD | same |
| SSD, residential bought 11 Mar 2017 to 3 Jul 2025: up to 1 / 2 / 3 years | 12% / 8% / 4%; none after 3 years | same |

## Boundary and exception table

| Scenario | Treatment |
| --- | --- |
| Long-term investor sells shares after years | Capital, not taxed |
| Active trader buying and selling shares frequently | May be trading income, taxed |
| Property developer selling units | Trading income, taxed |
| Investor sells long-held investment property | Capital, generally not taxed; SSD only if within the holding period |
| Frequent property flipping | Trading income, taxed, and SSD |
| Digital tokens held as investment | Generally not taxed; trading as a business is taxed (see `singapore-crypto-tax`) |
| Company selling shares in a subsidiary | Refer: companies have their own rules for share disposals and for foreign asset gains |

## Worked cases

Case 1. A buyer bought a condominium on 1 August 2025 and sells it on 1 June 2026 for S$1,500,000 (market value S$1,480,000). Held up to 1 year: SSD 16% of the higher figure, S$1,500,000, is S$240,000. The gain itself is not taxed unless the buyer is trading in properties.

```oa-check
name: SSD on resale within 1 year, bought after 4 July 2025
inputs:
  price: 1500000
  market_value: 1480000
steps:
  - base: max(price, market_value)
  - ssd: floor(base * 0.16)
expected:
  base: 1500000
  ssd: 240000
```

Case 2, decision: sell in year 3 or wait past year 4? The same property, bought 1 August 2025, could be sold on 1 October 2028 (more than 3 years, up to 4: 4%) or after 1 August 2029 (no SSD). At S$1,600,000 the earlier sale costs S$64,000 of SSD; waiting costs nothing. The figure that decides it is whether the extra year's holding cost and price risk exceed S$64,000.

```oa-check
name: SSD in year 4 versus after 4 years
inputs:
  price: 1600000
steps:
  - ssd_year4: floor(price * 0.04)
  - ssd_after: 0
  - saving_by_waiting: ssd_year4 - ssd_after
expected:
  ssd_year4: 64000
  saving_by_waiting: 64000
```

## When to refuse or refer

| Trigger | Message |
| --- | --- |
| Many disposals a year, borrowing to buy, or activity close to the client's business | "This may be trading income. The facts need an adviser's review before saying it is untaxed." |
| A company or group disposing of shares or foreign assets | "Companies have specific rules for share disposals and for gains on foreign assets; refer." |
| Additional buyer's stamp duty or stamp duty on purchase | "Out of scope here; refer." |
| SSD exemptions or remissions (for example, inheritance, compulsory acquisition) | "Check the exemptions in the Stamp Duties Act and the remission rules; refer." |

## Filing and payment

Taxable trading gains go under "Other Income" in the individual return (see `sg-income-tax`); non-taxable gains are not declared. SSD is paid by the seller through IRAS's e-Stamping.

## Completion checklist

- Asset, dates, price and market value recorded.
- Badges of trade tested and the conclusion written down.
- SSD table chosen by purchase date and holding period computed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for IRAS treatment of gains from sale of property, shares and financial instruments (including digital tokens), the trading criteria and reporting (page updated 27 February 2026) | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/gains-from-sale-of-property-shares-and-financial-instruments | 2026-11-14 |
| Read for SSD rates by purchase date and holding period, the 4 July 2025 change, base and rounding | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-(ssd)-for-residential-property | 2026-11-14 |

Not yet confirmed: the 2020 IRAS crypto guidance cited in the old file (see `singapore-crypto-tax`); the IRAS property disposal questionnaire mentioned in the old file; the company rules on share disposals (section 13W) and on foreign asset gains (section 10L), not opened today.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sg-zero-cgt` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sg-zero-cgt. If neither is available, confirm every figure against the official source pages cited above before relying on it.
