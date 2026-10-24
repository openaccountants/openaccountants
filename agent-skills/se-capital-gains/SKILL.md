---
name: se-capital-gains
description: "Sweden capital gains tax: 30% on capital income, ISK investment savings account (schablonbeskattning), exit tax on departure. Trigger on: \"Sweden CGT\", \"capital gains Sweden\", \"Sweden 30% capital gains\", \"ISK account Sweden\", \"investeringssparkonto\", \"sell shares Sweden\", \"Sweden exit tax\", \"Sweden capital income tax\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/se-capital-gains"
  jurisdiction: "SE"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# SE Capital Gains

## Quick reference

**Quick reference**

| Item | Value |
| --- | --- |
| CGT rate | **30%** on capital income (kapitalinkomst) |
| ISK (investment savings account) | Standard income of 3.55% of the capital base for 2026, taxed at 30% (1.065%), after a tax-free amount on the first SEK 300,000 of combined ISK, capital insurance and PEPP savings |
| Capital loss offset | Losses on listed shares are deducted in full against gains on listed and unlisted shares and fund units in the same year; 70% of any remainder against other capital income (IL 48 kap. 20-20 a §§) |
| Home sale | 22/30 of the gain on a privatbostad is taxed at 30% (22% of the gain); 90% of the gain on a näringsfastighet (27%) (IL 45 kap. 33 §, 46 kap. 18 §) |
| Legislation | Inkomstskattelagen (IL), chapter 41–48 |
| Tax authority | Skatteverket (skatteverket.se) |

## Capital gains on shares and securities

- **Rate**: Gains on shares and other securities are capital income taxed at 30%. Gains on unlisted shares in Swedish companies (and comparable foreign companies) are taken up at five sixths, an effective 25% (IL 42 kap. 15 a §). Qualified shares in a closely held company (3:12 rules) are in [se-closely-held-company-312](se-closely-held-company-312.md).
- **Losses on listed shares**: Losses on listed shares and other listed delägarrätter (for example equity fund units) are deducted in full against taxable gains in the same year on delägarrätter, listed or unlisted (IL 48 kap. 20 §). Only the part that cannot be used that way is cut to 70% and deducted against other capital income (IL 48 kap. 20 a §, first paragraph).
- **Losses on unlisted shares**: Five sixths deductible against gains on shares (IL 48 kap. 20 §). Any remainder: five sixths of 70% against other capital income (20 a §, second paragraph).
- **Order**: Full-deductible losses first, then the five-sixths losses (48 kap. 20 §, second paragraph).
- **Other assets**: Losses on listed units in funds holding only Swedish receivables, and on other listed Swedish receivables apart from premium bonds, are deductible in full (48 kap. 21 and 23 §§). Any other capital loss: 70% (48 kap. 24 §).
- **Net deficit**: A net capital deficit gives a tax reduction of 30% on the first SEK 100,000 and 21% above that, in the same year only. That credit is in [se-employee-income-tax](se-employee-income-tax.md).

**Example (2026).** Gains on listed shares SEK 50,000. Losses on listed shares SEK 80,000. No other capital items. SEK 50,000 of the loss is deducted in full against the gains. The remaining SEK 30,000 is cut to 70%: SEK 21,000, a capital deficit. Tax reduction 30% × 21,000 = SEK 6,300, set against that year's tax on earned income.

```oa-check
name: Listed share losses above listed share gains (2026)
inputs:
  listed_gains: 50000
  listed_losses: 80000
steps:
  - full_offset: min(listed_gains, listed_losses)
  - remainder: listed_losses - full_offset
  - deficit: remainder * 0.70
  - tax_reduction: min(deficit, 100000) * 0.30 + max(deficit - 100000, 0) * 0.21
expected:
  full_offset: 50000.00
  remainder: 30000.00
  deficit: 21000.00
  tax_reduction: 6300.00
```

## ISK: investment savings account (investeringssparkonto)

- **ISK**: The ISK is a tax wrapper for investments that replaces per-transaction CGT with an annual flat fee
- **Annual schablonbeskattning**: Standard income (schablonintäkt) = capital base × (government borrowing rate at 30 November of the year before + 1 point), at least 1.25% (IL 42 kap. 36 §). For 2026: 2.55% + 1 = 3.55%. The capital base is one quarter of the sum of the account value on the first day of each quarter plus deposits made in that quarter (IL 42 kap. 37 §). Standard income is capital income taxed at 30%.
- **Tax-free amount (from 2026)**: A deduction removes the standard income on the first SEK 300,000 of combined ISK, capital insurance and PEPP savings, ISK first (IL 42 kap. 48 §; SEK 150,000 in 2025). Skatteverket gives it automatically. So for 2026 the tax is 1.065% of the capital base above SEK 300,000, and nil on a base of SEK 300,000 or less.
- **ISK tax treatment of disposals, dividends, contributions**: No CGT on individual disposals within the ISK (IL 42 kap. 42 §). Dividends within the ISK: not separately taxed. Contributions in/out: no tax event.

For an active investor the ISK replaces 30% tax on each gain and dividend with one annual charge on the account value.

**Example (2026).** An ISK with a capital base of SEK 800,000, no capital insurance or PEPP. Standard income 800,000 × 3.55% = SEK 28,400. Deduction 300,000 × 3.55% = SEK 10,650. Taxable capital income SEK 17,750. Tax at 30% = SEK 5,325.

```oa-check
name: ISK capital base SEK 800,000 (2026)
inputs:
  capital_base: 800000
  borrowing_rate: 0.0255
  tax_free_base: 300000
steps:
  - schablon_rate: max(borrowing_rate + 0.01, 0.0125)
  - standard_income: capital_base * schablon_rate
  - deduction: min(standard_income, tax_free_base * schablon_rate)
  - taxable_capital: standard_income - deduction
  - tax: taxable_capital * 0.30
expected:
  standard_income: 28400.00
  deduction: 10650.00
  taxable_capital: 17750.00
  tax: 5325.00
```

## Interest on loans (from 2026)

- **Which interest is deductible**: From income year 2026 interest is deductible in capital only on loans with qualifying security or lender (IL 42 kap. 6 a-6 g §§): a credit institution or mortgage lender loan secured on real property, a site-leasehold or a tenant-owner flat (6 b §); a credit institution or securities firm loan secured on listed securities or fund units (6 c §); a pawnbroker loan (6 d §); and a loan secured on the vehicle, boat, ship or aircraft it financed, where seller and lender are both businesses (6 e §). The lender must be in the EEA or a state with an information-exchange treaty with Sweden (6 f §). Interest on unsecured consumer loans and credit cards is not deductible.
- **Effect on a share sale**: Interest on a margin loan secured on listed shares stays deductible against the 30% capital income, or gives the capital deficit credit (30% up to SEK 100,000, 21% above). The deficit credit is in [se-employee-income-tax](se-employee-income-tax.md).

## Real property

- **Privatbostad**: A house, owner flat (ägarlägenhet) or tenant-owner flat (bostadsrätt) used or meant to be used mainly by the owner or a close relative as a permanent home or holiday home (IL 2 kap. 8 §). A holiday home counts.
- **Gain on a privatbostad**: 22/30 of the gain is taken up in capital and taxed at 30%, so the tax is 22% of the gain. A loss is 50% deductible (IL 45 kap. 33 § for houses and owner flats; 46 kap. 18 § for bostadsrätter, same fractions).
- **Gain on other property (näringsfastighet, näringsbostadsrätt)**: When an individual sells it, 90% of the gain is taken up in capital and taxed at 30%, so 27% of the gain. A loss is 63% deductible (45 kap. 33 §; 46 kap. 18 §).
- **Deferral (uppskov)**: On the sale of a privatbostad in the EEA that was the seller's permanent home (lived there at least one year before the sale, or three of the last five years), tax on the gain can be deferred if they buy a replacement home in the EEA no earlier than the year before and no later than the year after the year of sale, and move in by 2 May of the following year or, for a later purchase, the second year (IL 47 kap. 2-9 §§). The deferred amount is at least SEK 50,000 and at most SEK 3,000,000 times the seller's share of the home (47 kap. 6-8 §§). A cheaper replacement home gives a proportionally smaller deferral (47 kap. 7 § 2). There is no annual charge on a deferral since income year 2021 (Skatteverket). The deferral is taxed when the replacement home is sold or passes to someone else, with exceptions for inheritance by a spouse, partner or child under 18 and for division of property between spouses or partners (47 kap. 11 §); it can be reversed voluntarily in amounts of at least SEK 20,000 (47 kap. 9 a §).

**Example (2026).** A single owner sells a privatbostad with a gain of SEK 1,000,000 and claims no deferral. Taxable 22/30 × 1,000,000 = SEK 733,333.33. Tax at 30% = SEK 220,000, which is 22% of the gain.

```oa-check
name: Privatbostad gain SEK 1,000,000, no deferral (2026)
inputs:
  gain: 1000000
steps:
  - taxable: gain * 22 / 30
  - tax: taxable * 0.30
expected:
  taxable: 733333.33
  tax: 220000.00
```

## Leaving Sweden

- **No exit charge on private gains**: Leaving Sweden does not by itself tax an individual's unrealised gains on privately held shares or a home. A later sale of shares can still be taxed in Sweden under the ten-year rule (IL 3 kap. 19 §), subject to a treaty; see [se-cross-border](se-cross-border.md).
- **Home sale deferral after moving**: A final deferral stays in place as long as the person owns the replacement home (Skatteverket, begär uppskov). IL 47 kap. 11 b § was repealed by SFS 2020:1068, and no rule left in 47 kap. taxes a deferral because its owner moves abroad.

## Sources

| Source | URL | Read on |
|---|---|---|
| Inkomstskattelag (1999:1229), as amended to SFS 2026:1393: 2 kap. 8 §; 3 kap. 19 §; 42 kap. 6 a-6 g, 15 a, 36-37, 42, 48 §§; 45 kap. 33 §; 46 kap. 18 §; 47 kap. 2-11 §§; 48 kap. 20-24 §§ | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-23 |
| Skatteverket, belopp och procent inkomstår 2026 (schablonintäkt på investeringssparkonto, statslåneränta, försäljning privatbostad, försäljning näringsfastighet, uppskov, skattereduktion vid underskott av kapital) | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-23 |
| Skatteverket, begär uppskov | https://www.skatteverket.se/privat/fastigheterochbostad/forsaljningavbostad/begaruppskov.4.6d02084411db6e252fe80009532.html | 2026-10-23 |

Not yet confirmed: whether an existing deferral is taxed when its owner leaves Sweden in any case other than a sale or transfer of the replacement home (47 kap. 11 b § is repealed; Skatteverket's page says a final deferral lasts while the person owns the home).

> Working paper only. ISK standard income rates change every year; confirm the
> current year rate from Skatteverket. Have a qualified Swedish tax adviser (skatterådgivare)
> review.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `se-capital-gains` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/se-capital-gains. If neither is available, confirm every figure against the official source pages cited above before relying on it.
