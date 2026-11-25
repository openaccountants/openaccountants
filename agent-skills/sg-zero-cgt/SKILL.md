---
name: sg-zero-cgt
description: "Use this skill when asked about capital gains in Singapore for Year of Assessment 2026 and 2027. Trigger on CGT Singapore, capital gains Singapore, sell shares Singapore, Singapore no capital gains tax, investment gains Singapore, crypto gains Singapore, Singapore property gains, trading in properties, badges of trade Singapore, seller's stamp duty, SSD Singapore, dispose assets Singapore. Singapore has no general capital gains tax. Trading gains are income, and certain disposals of residential property within the holding period bear seller's stamp duty (16%, 12%, 8%, 4% for property bought on or after 4 July 2025). Covers the capital versus trading test IRAS applies, shares and digital tokens, property and SSD."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sg-zero-cgt"
  jurisdiction: "SG"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# Singapore: no capital gains tax, and where gains are still taxed

> **General reference only.** The capital versus trading line is fact-specific. Have a qualified Singapore tax adviser review high-frequency or leveraged activity.

## Scope

For individuals, genuine capital gains are generally outside income tax. Special rules apply to covered foreign asset disposals by certain group entities under section 10L. IRAS treats gains from selling a property, shares and financial instruments as generally not taxable, but gains from trading (buying and selling with a profit-seeking motive) are income under section 10(1)(a) of the Income Tax Act 1947. Separately, seller's stamp duty (SSD) under the Stamp Duties Act applies to residential property sold within a set holding period. Applies to residents and non-residents. Crypto trading as a business: `singapore-crypto-tax`. Rates on taxable income: `sg-income-tax`.

## Ask the client first

1. **What was sold**, when bought, when sold, price and market value.
2. **How often** the client buys and sells this kind of asset, and why this one was sold.
3. **How it was financed** and whether the client could have held it long term.
4. **Is buying and selling the client's business** or closely related to it (developer, dealer, trader)?
5. For residential property: **date of purchase** (decides the SSD table) and holding period.

## The method, step by step

1. **Start from capital.** IRAS: gains from selling a property in Singapore, and profits from buying and selling shares or other financial instruments (including digital tokens), are generally viewed as capital or personal investment and not taxed. Personal insurance payouts of a capital nature are generally outside tax. Insurance payments replacing taxable profits or paid as remuneration can be taxable.
2. **Test for trading.** For property IRAS looks at: frequency of transactions; reasons for buying and selling; financial means to hold long term; holding period. The same badges of trade apply to shares and tokens (frequency, similarity to the taxpayer's business, holding period, borrowing, work done to the asset before sale).
3. **If taxable**, use the return field for the source of income. IRAS directs individuals to report taxable property sale gains under "Other Income". Declare self-employment or business trading profits in the relevant trade or business section and use any required appendix. Non-taxable individual capital gains are not declared.
4. **Residential property SSD.** For ordinary residential property acquired on or after 4 July 2025, SSD applies to qualifying disposals before the fourth acquisition anniversary. Use the higher of sale price and market value at disposal. Round down the duty to the whole dollar, subject to a S$1 minimum per dutiable instrument. Determine the acquisition and disposal dates under section 22A, commonly the dates the relevant options are exercised or the contracts are made. Property acquired earlier uses its own table.

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| General capital gains tax for individuals | None | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/gains-from-sale-of-property-shares-and-financial-instruments |
| SSD, residential bought on or after 4 Jul 2025, held up to 1 year | 16% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-(ssd)-for-residential-property |
| Held more than 1 year, up to 2 years | 12% | same |
| Held more than 2 years, up to 3 years | 8% | same |
| Held more than 3 years, with disposal before the fourth acquisition anniversary | 4% | same |
| Disposal on or after the fourth acquisition anniversary | No SSD under the ordinary four-year holding rule | [IRAS example 3](https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-(ssd)-for-residential-property) |
| SSD, residential bought 11 Mar 2017 to 3 Jul 2025: up to 1 / 2 / 3 years | 12% / 8% / 4%; none on or after the third acquisition anniversary | same |

## Boundary and exception table

| Scenario | Treatment |
| --- | --- |
| Long-term investor sells shares after years | Capital, not taxed |
| Active trader buying and selling shares frequently | May be trading income, taxed |
| Property developer selling units | Trading income, taxed |
| Investor sells long-held investment property | Capital, generally not taxed; SSD only if within the holding period |
| Frequent property flipping | Assess the trading facts. Calculate SSD separately if the statutory holding rule applies |
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

Case 2, decision: sell in year 4 or wait until the fourth anniversary? The same property, acquired 1 August 2025, could be sold on 1 October 2028 at 4% or on 1 August 2029 with no SSD. Assume S$1,600,000 is the earlier sale price and it equals or exceeds market value. The earlier sale incurs S$64,000 of SSD. Compare that saving with the holding costs and sale price uncertainty over the 10 months to the anniversary.

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
| SSD relief or a special acquisition date (for example, an inherited interest or compulsory acquisition) | "An inherited interest generally uses the deceased’s acquisition date. Check the statutory relief and acquisition rules for the transaction." |

## Filing and payment

Report gains in the relevant individual return field as described above. The seller pays any SSD through myTax Portal (Stamp Duty Login). For a contract executed in Singapore, stamp within 14 days after execution to avoid late payment penalties. Check the special timing rules for instruments executed abroad.

## Completion checklist

- Asset, dates, price and market value recorded.
- Badges of trade tested and the conclusion written down.
- SSD table chosen by purchase date and holding period computed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for IRAS treatment of gains from sale of property, shares and financial instruments (including digital tokens), the trading criteria and reporting (page updated 27 February 2026) | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/gains-from-sale-of-property-shares-and-financial-instruments | 2026-11-14 |
| Read for SSD rates by purchase date and holding period, the 4 July 2025 change, base and rounding | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-(ssd)-for-residential-property | 2026-11-14 |
| Read for trade income and insurance receipts on revenue account | https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr10- | 2026-11-24 |
| Read for property disposal timing and holding period expiry | https://sso.agc.gov.sg/Act/SDA1929?ProvIds=pr22A-&ValidDate=20261122&ViewType=Advance | 2026-11-24 |
| Read for residential SSD holding periods | https://sso.agc.gov.sg/SL/SDA1929-S209-2010?DocDate=20250703&ProvIds=pr9-&ValidDate=20250704 | 2026-11-24 |
| Read for the First Schedule rounding rule | https://sso.agc.gov.sg/Act/SDA1929?ProvIds=Sc1-&ViewType=Advance | 2026-11-24 |
| Read for the 4 July 2025 residential SSD rates | https://sso.agc.gov.sg/SL-Supp/S480-2025/Published/20250703?DocDate=20250703&ViewType=Advance | 2026-11-24 |
| Read for business income filing | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/filing-responsibilities-of-self-employed-persons-%28including-individual-partners%29 | 2026-11-24 |
| Read for insurance receipts on capital or revenue account | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses/tax-treatment-of-business-expenses-%28g-l%29 | 2026-11-24 |
| Read for when and where a document is executed for stamping | https://www.iras.gov.sg/taxes/stamp-duty/for-property/basics-of-stamp-duty-for-property/learning-the-basics-for-properties | 2026-11-24 |
| Read for digital token investment and trading | https://www.iras.gov.sg/media/docs/default-source/e-tax/etaxguide_cit_income-tax-treatment-of-digital-tokens_091020.pdf | 2026-11-24 |
| Read for corporate share disposal exemption from 1 January 2026 | https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr13W-&ViewType=Within&WiAl=1 | 2026-11-24 |
| Read for foreign asset disposal gains of relevant group entities | https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr10L-&ValidDate=20261122&ViewType=Advance | 2026-11-24 |

The official digital-token guide and sections 13W and 10L govern the referred cases. The residential SSD declaration is a separate form. Not yet confirmed: availability of the old individual income-tax property-disposal questionnaire.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sg-zero-cgt` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sg-zero-cgt. If neither is available, confirm every figure against the official source pages cited above before relying on it.
