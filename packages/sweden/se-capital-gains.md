---
name: se-capital-gains
description: "Sweden capital gains tax: 30% on capital income, ISK investment savings account (schablonbeskattning), exit tax on departure. Trigger on: \"Sweden CGT\", \"capital gains Sweden\", \"Sweden 30% capital gains\", \"ISK account Sweden\", \"investeringssparkonto\", \"sell shares Sweden\", \"Sweden exit tax\", \"Sweden capital income tax\"."
version: 1.2
jurisdiction: SE
tax_year: 2026
last_updated: 2026-11-16
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Sweden capital gains v1.2

Built from the law. Not yet approved.

## Who this applies to

Use for a Swedish individual's private shares, securities, investment savings account and home disposals in income year 2026. Qualified closely held shares use [se-closely-held-company-312](se-closely-held-company-312.md); companies, business inventory and treaty residence need their own methods. Establish ownership, residence, asset classification and transaction dates before calculating.

## Rates, bands and thresholds

| Item | Value |
| --- | --- |
| CGT rate | **30%** on capital income (kapitalinkomst)  [IL and 2026 figures](https://data.riksdagen.se/dokument/sfs-1999-1229.text) |
| ISK (investment savings account) | Standard income of 3.55% of the capital base for 2026, taxed at 30% (1.065%), after a tax-free amount on the first SEK 300,000 of combined ISK, capital insurance and PEPP savings  [IL and 2026 figures](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |
| Capital loss offset | Losses on listed shares are deducted in full against gains on listed and unlisted shares and fund units in the same year; 70% of any remainder against other capital income (IL 48 kap. 20-20 a §§)  [IL and 2026 figures](https://data.riksdagen.se/dokument/sfs-1999-1229.text) |
| Home sale | 22/30 of the gain on a privatbostad is taxed at 30% (22% of the gain); 90% of the gain on a näringsfastighet (27%) (IL 45 kap. 33 §, 46 kap. 18 §)  [IL and 2026 figures](https://data.riksdagen.se/dokument/sfs-1999-1229.text) |
| Legislation | Inkomstskattelagen (IL), chapter 41-48  [IL and 2026 figures](https://data.riksdagen.se/dokument/sfs-1999-1229.text) |
| Tax authority | Skatteverket (skatteverket.se)  [Skatteverket](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |

## The base

### Capital gains on shares and securities

- **Rate**: Gains on shares and other securities are capital income taxed at 30%. Gains on eligible unlisted shares in Swedish companies (and foreign companies with comparable income taxation) are taken up at five sixths, an effective 25% (IL 42 kap. 15 a §). This is not universal: the section excludes qualified shares, private housing companies, specified formerly listed shares, companies meeting its 10% listed-company holding test in the current or four preceding years, and gains taxed under 49 a kap.; route these before applying five sixths. Qualified shares in a closely held company (3:12 rules) are in [se-closely-held-company-312](se-closely-held-company-312.md).
- **Losses on listed shares**: Losses on listed shares and other listed delägarrätter (for example equity fund units) are deducted in full against taxable gains in the same year on delägarrätter, listed or unlisted (IL 48 kap. 20 §). Only the part that cannot be used that way is cut to 70% and deducted against other capital income (IL 48 kap. 20 a §, first paragraph).
- **Losses on unlisted shares**: For eligible unlisted shares, five sixths is deductible against gains on shares (IL 48 kap. 20 §). Any remainder: five sixths of 70% against other capital income (20 a §, second paragraph). Qualified close-company shares instead use their two-thirds fraction and the separate close-company method; do not apply five sixths to them.
- **Order**: Full-deductible losses first, then the five-sixths losses (48 kap. 20 §, second paragraph).
- **Other assets**: Losses on listed units in funds holding only Swedish receivables, and on other listed Swedish receivables apart from premium bonds, are deductible in full (48 kap. 21 and 23 §§). Other losses within 48 kap. 24 §: 70%. Do not extend this securities rule to a personal-use asset or another asset category with its own loss rule.
- **Net deficit**: A net capital deficit gives a tax reduction of 30% on the first SEK 100,000 and 21% above that, in the same year only, limited to available tax. The capital-insurance/PEPP and investor-deduction components keep their specific 30% treatment under IL 67 kap. 10 §. That credit is in [se-employee-income-tax](se-employee-income-tax.md).

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

- **ISK**: The ISK is a tax wrapper for investments that replaces ordinary per-transaction CGT with an annual standard-income charge, subject to the exceptions below.
- **Annual schablonbeskattning**: Standard income (schablonintäkt) = capital base × (government borrowing rate at 30 November of the year before + 1 point), at least 1.25% (IL 42 kap. 36 §). For 2026: 2.55% + 1 = 3.55%. The capital base is one quarter of the sum of the account value on the first day of each quarter plus deposits made in that quarter (IL 42 kap. 37 §). Standard income is capital income taxed at 30%.
- **Tax-free amount (from 2026)**: A deduction removes the standard income on the first SEK 300,000 of combined ISK, capital insurance and PEPP savings, ISK first (IL 42 kap. 48 §; SEK 150,000 in 2025). Skatteverket gives it automatically. So for 2026 the tax is 1.065% of the capital base above SEK 300,000, and nil on a base of SEK 300,000 or less.
- **ISK tax treatment of disposals, dividends, contributions**: No CGT on individual disposals within the ISK (IL 42 kap. 42 §). Ordinary dividends within the ISK are not separately taxed. No deduction is allowed for its investment losses or expenses. The exemption does not cover excluded assets under 42 kap. 38 §, deemed disposals under 44 kap. 8 a-8 b §§ or cash interest where its rate at any time in the year exceeds the greater of the preceding November government rate plus 1 percentage point and 1.25% (42 kap. 42 §). SEK cash deposits and withdrawals do not themselves realise a capital gain, but deposits can increase the capital base. Foreign currency paid into the ISK is a deemed disposal under IL 44 kap. 8 b §, subject to its listed transfer/return exceptions. A transfer of investments from an ordinary account into the ISK is a deemed disposal at market value under IL 44 kap. 8 a §; do not treat that transfer as tax-free. Transfers out and excluded/non-investment assets need the specific rules in IL 42 kap. 38-42 §§ and 44 kap. 8 b §.

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

- **Which interest is deductible**: From income year 2026 interest is deductible in capital only on loans with qualifying security or lender (IL 42 kap. 6 a-6 g §§): a credit institution or mortgage lender loan secured on real property, a site-leasehold or a tenant-owner flat (6 b §); a credit institution or securities firm loan secured on listed securities or fund units (6 c §); a pawnbroker loan (6 d §); and a loan secured on the vehicle, boat, ship or aircraft it financed, where seller and lender are both businesses, the asset and borrower are identified in the credit agreement, and the vehicle/ship/aircraft is registered to the borrower or a co-borrower in the specified Swedish or EEA register (6 e §). Qualifying construction finance intended to become a secured home loan also falls within 6 b §. Foreign lenders need the corresponding regulated business and supervision required by 6 b-6 d §§. The lender must be in the EEA or a state with an information-exchange treaty with Sweden, or lend through its permanent establishment in such a state with the loan attributable to it (6 f §). Amounts treated as interest and site-leasehold charges follow the distinct rules in 6 g-8 §§; do not infer their result from an unsecured-consumer-loan label. Interest on unsecured consumer loans and credit cards is not deductible.
- **Effect on a share sale**: Interest on a margin loan secured on listed shares stays deductible against the 30% capital income, or gives the capital deficit credit (30% up to SEK 100,000, 21% above). The deficit credit is in [se-employee-income-tax](se-employee-income-tax.md).

## Real property

- **Privatbostad**: A house, owner flat (ägarlägenhet) or tenant-owner flat (bostadsrätt) used or meant to be used mainly by the owner or a close relative (a two-family house instead requires a substantial part) as a permanent home or holiday home (IL 2 kap. 8 §). A holiday home counts.
- **Gain on a privatbostad**: 22/30 of the gain is taken up in capital and taxed at 30%, so the tax is 22% of the gain. A loss is 50% deductible (IL 45 kap. 33 § for houses and owner flats; 46 kap. 18 § for bostadsrätter, same fractions).
- **Gain on other property (näringsfastighet, näringsbostadsrätt)**: When an individual sells it, 90% of the gain is taken up in capital and taxed at 30%, so 27% of the gain. A loss is 63% deductible (45 kap. 33 §; 46 kap. 18 §).
- **Deferral (uppskov)**: On the sale of a privatbostad in the EEA that was the seller's permanent home (lived there at least one year before the sale, or three of the last five years), tax on the gain can be deferred if they buy a replacement home in the EEA no earlier than the year before and no later than the year after the year of sale, and move in by 2 May of the following year or, for a later purchase, the second year (IL 47 kap. 2-9 §§). The deferred amount is at least SEK 50,000 (SEK 10,000 for the compulsory-disposal cases in 47 kap. 4 §) and at most SEK 3,000,000 times the seller's share of the home (47 kap. 6-8 §§). A cheaper replacement home gives a proportionally smaller deferral (47 kap. 7 § 2). Include any prior deferral in the gain used in that calculation. If foreign-tax credit has already been granted under a tax treaty or the Foreign Tax Credit Act, IL 47 kap. 2 § permits deferral only for the part of the gain attributable to tax that was not credited; obtain the credit allocation before quantifying that deferral. A preliminary deferral is brought back the next year unless the acquisition and move-in conditions in 47 kap. 9 § are met; construction on an earlier-owned property and compulsory disposals need the specific 4-5 a §§ branches. There is no annual charge on a deferral since income year 2021 (Skatteverket). The deferral is taxed when the replacement home is sold or passes to someone else, with exceptions for inheritance or testament to a spouse, cohabiting partner or a child under 18 living at home, and division of property because a cohabiting relationship ends, divorce or the spouse/partner dies (47 kap. 11 §); it can be reversed voluntarily in amounts of at least SEK 20,000, or the whole remaining deferral if smaller (47 kap. 9 a §).

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

## Deadlines and filing

Report an ordinary share disposal on K4, preserving proceeds, allowable cost and the correct share category. Home sales use K5 for a private house or K6 for a private tenant-owner flat, including any deferral claim; do not file a home gain as an ordinary listed-share gain. ISK standard income and its deduction are normally pre-filled. Reconcile every entry to the working paper before approval. [Skatteverket: K4 and netting](https://www.skatteverket.se/privat/skatter/vardepapper/deklareraaktierochovrigavardepapper/kvittningochkvotering.4.7be5268414bea0646945a21.html); [K5](https://www.skatteverket.se/blanketterbroschyrer/blankett/info/2105.4.39f16f103821c58f680006252.html); [K6](https://www.skatteverket.se/privat/fastigheterochbostad/forsaljningavbostad/raknautvinstforlustochskatt/forsaljningavbostadsratt.4.233f91f71260075abe8800033855.html)

Inkomstdeklaration 1 is due 2 May after the income year (SFL 32 kap. 1 §). Under the weekend rule, income year 2026 is due 3 May 2027. File the correct year's return with its attachments and retain the acknowledgement; payment follows the final tax decision. [SFL](https://data.riksdagen.se/dokument/sfs-2011-1244.text); [time-limit Act 2 §](https://data.riksdagen.se/dokument/sfs-1930-173.text).

## Penalties and interest

Late-return fees, tax surcharges and tax-account interest follow the income-return rules in [se-cross-border](se-cross-border.md), not a separate capital-gains schedule. A gain working paper does not establish the whole-return credit or payment balance.

## Cross-border points

Apply the departure and treaty screen under Leaving Sweden above before stating a non-resident's tax. Foreign holdings still require Swedish SEK proceeds and cost. Never import another country's gain or cost figure without reconciling its Swedish treatment.

## Two worked examples that recompute

The three complete prose examples and recomputing blocks above cover listed-share loss restriction, the ISK deduction and a private-home gain. Their inputs are hypothetical and their expected values remain unchanged.

## Ask the client first

1. Residence and any move abroad, ownership share and disposal date.
2. Listed, unlisted, qualified closely held shares, ISK, private home or business property.
3. Complete proceeds, acquisition costs, fees, improvements and same-year gains and losses.
4. ISK quarterly balances and deposits, plus capital insurance and PEPP savings.
5. Loan lender, security and use, and whether a replacement-home deferral is sought.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for the cited capital, ISK, loan, property, loss and deferral provisions and their exceptions: Inkomstskattelag (1999:1229), as amended to SFS 2026:1393: 2 kap. 8 §; 3 kap. 19 §; 42 kap. 6 a-6 g, 15 a, 36-37, 42, 48 §§; 45 kap. 33 §; 46 kap. 18 §; 47 kap. 2-11 §§; 48 kap. 20-24 §§ | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-11-16 |
| Read for the 2026 amounts and capital/ISK/property fractions: Skatteverket, belopp och procent inkomstår 2026 (schablonintäkt på investeringssparkonto, statslåneränta, försäljning privatbostad, försäljning näringsfastighet, uppskov, skattereduktion vid underskott av kapital) | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-11-16 |
| Read for home-sale deferral, its retention and filing steps: Skatteverket, begär uppskov | https://www.skatteverket.se/privat/fastigheterochbostad/forsaljningavbostad/begaruppskov.4.6d02084411db6e252fe80009532.html | 2026-11-16 |
| Read for personal-return filing and weekend adjustment: SFL 32 kap. 1 § and time-limit Act 2 § | https://data.riksdagen.se/dokument/sfs-2011-1244.text ; https://data.riksdagen.se/dokument/sfs-1930-173.text | 2026-11-16 |
| Read for ordinary securities K4 reporting and netting | https://www.skatteverket.se/privat/skatter/vardepapper/deklareraaktierochovrigavardepapper/kvittningochkvotering.4.7be5268414bea0646945a21.html | 2026-11-16 |
| Read for K5 private-house and owner-flat reporting and the deferral claim | https://www.skatteverket.se/blanketterbroschyrer/blankett/info/2105.4.39f16f103821c58f680006252.html | 2026-11-16 |
| Read for K6 private tenant-owner-flat reporting, and K8/K9 alternatives outside that classification | https://www.skatteverket.se/privat/fastigheterochbostad/forsaljningavbostad/raknautvinstforlustochskatt/forsaljningavbostadsratt.4.233f91f71260075abe8800033855.html | 2026-11-16 |

Not yet confirmed: whether an existing deferral is taxed when its owner leaves Sweden in any case other than a sale or transfer of the replacement home (47 kap. 11 b § is repealed; Skatteverket's page says a final deferral lasts while the person owns the home).

> Working paper only. ISK standard income rates change every year; confirm the
> current year rate from Skatteverket. Have a qualified Swedish tax adviser (skatterådgivare)
> review.
