---
name: us-capital-gains
description: "US federal capital gains tax for residents: short-term vs long-term rates, 2025 0%/15%/20% LTCG brackets by filing status, 3.8% NIIT thresholds and Form 8960 computation, §1202 QSBS including post-OBBBA issuance-date rules, §1031 like-kind exchange, installment sales, wash sale rule, Schedule D, and state-tax caveats. Trigger on: \"US capital gains tax\", \"long-term capital gains US\", \"Schedule D\", \"LTCG rate US\", \"NIIT net investment income tax\", \"QSBS exclusion\", \"1031 exchange\", \"sell US shares tax\", \"US CGT resident\", \"capital loss carryforward US\". For non-residents see us-nonresident-cgt."
version: 1.0
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Capital Gains

## Quick reference

**Quick reference**

| Item | Value |
| --- | --- |
| Short-term gains (held ≤ 12 months) | Ordinary income rates (10%–37%) |
| Long-term gains (held > 12 months) | 0%, 15%, or 20% depending on income |
| Net Investment Income Tax (NIIT) | +3.8% on net investment income above thresholds |
| Maximum effective LTCG rate | **23.8%** (20% + 3.8% NIIT) |
| Annual exemption | None |
| Legislation | IRC §1(h), §1222, §1411 (NIIT) |
| Form | Schedule D + Form 8949 (attached to Form 1040) |

## Long-term capital gains rates (2025)

**Long-term capital gains rates (2025)**  _([Rev. Proc. 2024-40 §2.03; IRS Topic 409](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf))_

| Filing status | 0% | 15% | 20% |
| --- | --- | --- | --- |
| Single | Up to $48,350 | $48,351-$533,400 | Above $533,400 |
| Married filing separately | Up to $48,350 | $48,351-$300,000 | Above $300,000 |
| Married filing jointly / qualifying surviving spouse | Up to $96,700 | $96,701-$600,050 | Above $600,050 |
| Head of household | Up to $64,750 | $64,751-$566,700 | Above $566,700 |

- **Threshold basis** — Long-term capital gain thresholds are based on taxable income after deductions, not gross income or AGI. The preferential brackets stack on top of ordinary income when calculating tax.  _([IRC §1(h); IRS Topic 409](https://www.irs.gov/taxtopics/tc409))_

## Net Investment Income Tax (NIIT) — §1411

An additional **3.8%** applies to the lesser of net investment income or the excess of MAGI over the §1411 threshold. Net investment income generally includes capital gains, dividends, interest, rental income, royalties, and passive activity income. 2025 individual thresholds are:
- Single / head of household: $200,000
- Married filing jointly / qualifying surviving spouse: $250,000
- Married filing separately: $125,000

- **NIIT threshold — Single / Head of household** — $200,000  _([IRC §1411; 2025 Instructions for Form 8960](https://www.irs.gov/instructions/i8960))_
- **NIIT threshold — MFJ / qualifying surviving spouse** — $250,000  _([IRC §1411; 2025 Instructions for Form 8960](https://www.irs.gov/instructions/i8960))_

## Net Investment Income Tax (NIIT) — §1411

- **NIIT threshold — Married filing separately** — $125,000  _([IRC §1411; 2025 Instructions for Form 8960](https://www.irs.gov/instructions/i8960))_

## Net Investment Income Tax (NIIT) — §1411

- **NIIT rate** — 3.8%  _([IRC §1411; 2025 Instructions for Form 8960](https://www.irs.gov/individuals/net-investment-income-tax))_
- **NIIT computation basis** — NIIT applies at 3.8% to the lesser of net investment income or the excess of modified adjusted gross income over the applicable §1411 threshold.  _([IRC §1411; 2025 Instructions for Form 8960](https://www.irs.gov/instructions/i8960))_

## Capital loss rules

- **Loss netting order** — Short-term losses offset short-term gains first; long-term losses offset long-term gains first
- **Cross-type netting** — Net losses of either type can offset the other after netting within type
- **Annual ordinary income offset limit** — $3,000 USD (per year, net capital loss deductible against ordinary income)
- **Loss carryforward** — Unused losses carry forward indefinitely (retaining their short/long-term character)

## Key exclusions and deferral rules

### §1202 QSBS — Qualified Small Business Stock

- **QSBS exclusion** — For QSBS issued on or before July 4, 2025, the usual post-2010 rule can exclude 100% of eligible gain after a holding period of more than 5 years, capped at the greater of $10 million or 10 times basis. For QSBS issued after July 4, 2025, P.L. 119-21 §70431 creates a tiered exclusion: 50% after 3 years, 75% after 4 years, and 100% after 5 years, capped at the greater of $15 million or 10 times basis, with inflation indexing after 2026.  _([IRC §1202; P.L. 119-21 §70431](https://www.congress.gov/bill/119th-congress/house-bill/1/text))_
- **QSBS company eligibility asset ceiling** — Issuer must be a domestic C corporation meeting the §1202 active-business and prohibited-business rules. The aggregate gross-assets ceiling is $50 million for stock issued on or before July 4, 2025, and $75 million for stock issued after July 4, 2025, with inflation indexing after 2026.  _([IRC §1202(d); P.L. 119-21 §70431](https://www.congress.gov/bill/119th-congress/house-bill/1/text))_
- **Original purchaser requirement** — Taxpayer must be the original purchaser (not secondary market)  _(§1202)_
- **California non-conformity** — California does not conform — QSBS gains are taxable in CA  _(§1202)_

### §1031 Like-Kind Exchange

- **Deferral on real property** — Gains on sale of real property can be deferred by reinvesting in like-kind property  _(§1031)_
- **Identification and closing deadlines** — Must identify replacement property within 45 days; close within 180 days  _(§1031)_
- **Exclusions from §1031** — Does NOT apply to securities, personal property, or foreign real property  _(§1031)_

### §121 Principal Residence Exclusion

- **Principal residence exclusion — Single** — $250,000 USD  _(§121)_
- **Principal residence exclusion — MFJ** — $500,000 USD  _(§121)_
- **Ownership and use test** — Must have owned and used as primary residence for 2 of the last 5 years  _(§121)_

### Installment sales (§453)

- **Recognition over payment period** — Gain can be recognised over the payment period if proceeds received in instalments  _(§453)_
- **Imputed interest** — Interest imputed on deferred principal  _(§453)_

## Wash sale rule (§1091)

- **Wash sale disallowance** — A capital loss on stock or securities is disallowed if the taxpayer acquires the same or substantially identical stock or securities within 30 days before or after the sale. The disallowed loss is added to the basis of the replacement shares. Current §1091 wash-sale language is stock/securities focused; do not extend it to every digital-asset transaction without separate law review.  _([IRC §1091; IRS Publication 550](https://www.irs.gov/publications/p550))_

## Collectibles and §1250 recapture

- **Collectibles maximum rate** — 28% percent (Under §408(m), long-term capital gains on "collectibles" are taxed at a maximum rate of 28% instead of the standard 20% maximum rate. An NFT may qualify as a collectible if it represents: A work of art; A rug or antique; A metal or gem; A stamp or coin; An alcoholic beverage; Any other tangible personal property specified by the IRS. IRS Notice 2023-27 provides a look-through framework: if the NFT represents a right to a collectible (e.g., digital art), it may be taxed at the 28% collectibles rate. If it represents a non-collectible asset (e.g., event tickets, in-game items with utility), the standard long-term rates apply.)  _(§408(m); IRS Notice 2023-27)_
- **§1250 unrecaptured depreciation maximum rate** — 25% percent (on the depreciation recapture portion of real property)  _(§1250)_

## State taxes

Most states tax capital gains as ordinary income at state rates. Key notes:
- **No broad individual income tax**: TX, FL, NV, WY, SD, AK, NH.
- **Washington**: no broad individual income tax, but a separate capital gains excise tax can apply to long-term capital gains above the annual exemption. Do not classify WA as simply "no capital gains tax" without checking the WA capital gains rules.
- **CA**: taxes capital gains as ordinary income at up to 13.3% + QSBS does not conform

## Sources

- IRC §1(h), §1221, §1222 (capital gains and losses)
- IRC §1202 (QSBS), §1031 (like-kind exchange), §121 (principal residence), §1411 (NIIT)
- IRS Publication 550 (Investment Income and Expenses)
- IRS Topic 409 and Rev. Proc. 2024-40 (2025 LTCG thresholds)
- 2025 Instructions for Form 8960 (NIIT thresholds and computation)
- P.L. 119-21 §70431 (post-OBBBA QSBS expansion)
- Schedule D instructions (IRS.gov)

> Working paper only. Confirm current-year rate thresholds from IRS inflation adjustments
> before computing. State CGT treatment requires separate analysis.

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
