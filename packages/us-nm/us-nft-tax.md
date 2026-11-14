---
name: us-nft-tax
description: Work out the 2026 US federal tax on non-fungible tokens (NFTs) for collectors, traders and creators. Covers NFTs as property, capital or ordinary character by holder, the look-through test in Notice 2023-27 that the IRS intends to use to decide when an NFT is a collectible taxed at up to 28 percent, holding periods, basis with gas and marketplace fees, NFT-for-crypto swaps, creators' sales and secondary royalties as ordinary and self-employment income above the USD 400 floor, Form 1099-DA for specified NFTs in 2026 (optional reporting with a USD 600 de minimis), wash sales, gifts, and donations with a qualified appraisal above USD 5,000. Trigger on "NFT tax", "sold an NFT", "NFT collectible 28%", "NFT royalties", "minting NFT tax", "gas fees NFT", "NFT creator self-employment". Federal only.
version: "2.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
type: situation-rules
---

# US tax on NFTs: collectors, collectibles and creators, tax year 2026

> **Source-cited draft.** Built from Notice 2014-21, Notice 2023-27, 26 U.S.C. 1(h), 408(m), 1091 and 1402 (2024 edition), CCA 202302012 and the 2026 Instructions for Form 1099-DA, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** An NFT is a digital asset and is taxed as **property**. A **collector or trader** has capital gain or loss on a sale or swap: short-term if held one year or less, long-term if more. A long-term gain is taxed at up to **28%** instead of 15% or 20% if the NFT is a **collectible**; the IRS has said it intends to decide that by **looking through** to the NFT's associated right or asset (an NFT certifying a gem or a physical artwork is a collectible; one tied to a purely digital file or an in-game item generally is not), but final guidance has not been issued. A **creator** selling their own NFTs in a business has **ordinary income** and **self-employment tax** on the profit, royalties included.

## Scope and who this is for

In scope: US citizens and resident aliens filing a 2026 Form 1040 who buy, sell, swap, mint, create, receive, give or donate NFTs.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Fungible crypto (the ETH or SOL used to buy NFTs), basis by wallet, Form 8949 digital asset boxes, Form 1099-DA in general | `us-crypto-tax` |
| Capital gain rate bands, the 28% collectibles group, the net investment income tax, the loss limit | `us-capital-gains` |
| A creator's Schedule C and Schedule SE in full | `us-schedule-c-and-se-computation` |
| Gift tax returns | `us-estate-gift-706-709` |
| Charitable deduction limits | `us-charitable-giving-strategies` |
| NFTs that may be securities, fractionalised NFTs, play-to-earn businesses, state tax | Refer |

## Ask the client first

1. **Collector, trader or creator?** For creators: is it a business (regular, continuous, for profit)?
2. **For each NFT sold or swapped:** what was bought (and with what crypto), when, the dollar value paid, gas and marketplace fees, the date and value received on sale.
3. **What each NFT represents:** a digital image or file, a right to a physical item (art, gems, metal, wine, coins, stamps), virtual land, an in-game item, a ticket or membership, a share of revenue.
4. **For creators:** sales (first sales and secondary royalties), minting and gas costs, platform fees, and other business costs.
5. **Gifts and donations** of NFTs, with values and appraisals.
6. **Forms received:** Form 1099-DA, 1099-K, 1099-NEC or 1099-MISC from any marketplace.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Maximum rate on long-term collectibles gain (28-percent rate gain) | 28% | [26 U.S.C. 1(h)(4) and (5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| Long-term holding period: held more than | 1 year | [26 U.S.C. 1(h)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| No self-employment tax if net earnings are less than | USD 400 | [26 U.S.C. 1402(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm) |
| Net earnings factor for self-employment tax | 92.35% | [Schedule SE (Form 1040) 2026](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Self-employment tax rate | 15.3% | [IRS, Self-employment tax](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) |
| Form 1099-DA, optional method for specified NFTs: no report if a customer's yearly gross proceeds do not exceed | USD 600 | [Instructions for Form 1099-DA (2026)](https://www.irs.gov/pub/irs-pdf/i1099da.pdf) |
| Donated NFT: qualified appraisal required above | USD 5,000 | [CCA 202302012](https://www.irs.gov/pub/irs-wd/202302012.pdf) |
| Donated NFT: appraisal attached to the return for a claim of more than | USD 500,000 | [26 U.S.C. 170(f)(11)(D)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |

The 0%, 15% and 20% bands and the net investment income tax are owned by `us-capital-gains`; the 2026 Social Security wage base by `us-schedule-c-and-se-computation`.

### Step 1: classify the NFT and the holder

1. An NFT is a digital asset and is property; general property tax principles apply. There is no NFT-specific Code section. Source: [Notice 2014-21](https://www.irs.gov/pub/irs-drop/n-14-21.pdf).
2. **Collector or trader:** the NFT is a capital asset; a sale or exchange gives capital gain or loss.
3. **Creator in a business:** NFTs the creator makes and sells are not capital assets (self-created property and inventory are excluded by section 1221(a)(1) and (3)), so the income is ordinary.
4. **Possible securities:** an NFT that gives a share of profits, or a fractional interest, may be a security; refer (R-NFT-SEC).

### Step 2: is it a collectible? (Notice 2023-27)

5. A **collectible** is any work of art, rug or antique, metal or gem, stamp or coin, alcoholic beverage, or other tangible personal property the Secretary specifies (section 408(m)(2), read without 408(m)(3) for section 1(h)). Source: [26 U.S.C. 408(m)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408.htm).
6. **Look-through analysis:** "Pending the issuance of that guidance, the IRS intends to determine whether an NFT constitutes a collectible" by looking at its **associated right or asset**: an NFT is a collectible if that right or asset is a section 408(m) collectible. An NFT that certifies ownership of a gemstone is a collectible; one that represents a right to a plot of virtual land is not. Notice 2023-27 asks for comments on when a digital file (for example digital art) is a "work of art". Source: [Notice 2023-27](https://www.irs.gov/pub/irs-drop/n-23-27.pdf).
7. **Status:** this is a statement of intent, not a regulation. Apply it as the IRS's announced position and flag digital-art cases for the reviewer: the Notice leaves open whether a purely digital artwork is a "work of art".

| What the NFT represents | Likely status under the look-through test |
| --- | --- |
| Ownership of a physical artwork, gem, coin, stamp, precious metal or wine | Collectible: long-term gain at up to 28% |
| Purely digital image, video or music file | Open: Notice 2023-27 asks for comments on whether it is a work of art; flag |
| Virtual land, in-game item, ticket, membership, domain name | Generally not a collectible: 0%, 15% or 20% |

### Step 3: gain or loss for a collector

8. **Basis** = what was paid in US dollars, including gas and marketplace fees to acquire. Paying with crypto is itself a disposition of that crypto (`us-crypto-tax`): the NFT's basis is the fair market value of the crypto given. An NFT received as payment has a basis equal to its value when received.
9. **Amount realized** = the value of what is received (dollars or crypto) less selling gas and marketplace fees. Swapping one NFT for another is a sale of the first.
10. **Holding period:** one year or less is short-term (ordinary rates); more than one year is long-term (0%, 15% or 20%, or up to 28% for a collectible). Collectibles gain is a separate group on the Schedule D worksheet (`us-capital-gains`). The 28% is a maximum: a taxpayer whose ordinary rate is lower pays the lower rate.
11. **Report** on Form 8949 with the digital asset boxes G to L and Schedule D (`us-crypto-tax`).
12. **Wash sales:** section 1091 applies to "stock or securities", so it does not disallow a loss on an NFT that is property (unless the NFT is a security). Source: [26 U.S.C. 1091](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partVII-sec1091.htm).

### Step 4: creators

13. **Sales by a creator** in a trade or business are ordinary income at the dollar value of what is received, on Schedule C. **Secondary-sale royalties** paid by a smart contract are also ordinary income when received, and part of the business income if the creator's NFT activity is a business; a creator who is not in a business reports them as other income or on Schedule E.
14. **Costs:** minting and gas fees, platform fees, software and art costs are business expenses for a creator in a business (or capitalised to inventory where inventory rules apply). There is no NFT-specific ruling on gas fees; positions rest on general deduction and capitalisation rules (sections 162, 263 and 1012).
15. **Self-employment tax:** net earnings from the business times 92.35% are taxed at 15.3% (12.4% only up to the wage base), unless net earnings are less than USD 400. Source: [26 U.S.C. 1402](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm); full computation in `us-schedule-c-and-se-computation`.

### Step 5: Form 1099-DA for NFTs in 2026

16. A **specified NFT** is a digital asset that is indivisible, unique and does not directly or indirectly give the holder an interest in certain excluded property. A broker (for example a custodial marketplace) may use an **optional method** for specified NFTs: it reports aggregate proceeds and need not report a customer whose total gross proceeds from specified NFT sales do not exceed **USD 600** for the year. First sales by a creator or minter are reported separately from other NFT sales. Source: [Instructions for Form 1099-DA (2026)](https://www.irs.gov/pub/irs-pdf/i1099da.pdf).
17. A Form 1099-DA is an information return and does not change the character of the income; a sale with no form is still reported.

### Step 6: gifts and donations

18. **Gift:** not a disposition for the donor; the donee takes the donor's basis (or the lower value, for losses). Gifts to one person above the annual exclusion need Form 709 (`us-estate-gift-706-709`). Valuation of a unique NFT is often the hard part.
19. **Donation:** for an NFT held more than one year as a capital asset, the deduction is generally its fair market value (lower limits apply to some gifts of tangible personal property and to collectibles not used by the charity; check them in `us-charitable-giving-strategies`); held one year or less, the lower of basis and value. For a claim above **USD 5,000** a **qualified appraisal** and Form 8283 Section B are required; the IRS treats crypto as not exempt from the appraisal rule, and the same section 170(f)(11) regime applies to an NFT. An appraisal is attached to the return for a claim of more than USD 500,000. Source: [CCA 202302012](https://www.irs.gov/pub/irs-wd/202302012.pdf); [26 U.S.C. 170(f)(11)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| NFT bought with ETH | Two events: the ETH is disposed of (gain or loss), and the NFT's basis is the ETH's value |
| NFT held exactly one year and sold | Short-term: long-term needs more than one year |
| NFT tied to a physical gold bar, held two years | Collectible under the look-through test: up to 28% |
| NFT of a purely digital artwork, held two years | Open under Notice 2023-27; flag, and show the 28% and 15% or 20% outcomes |
| Creator's first sale of their own NFT | Ordinary income, Schedule C if a business |
| Creator with net earnings of USD 350 | No self-employment tax (below USD 400); income still taxable |
| Sold at a loss and bought a similar NFT next day | Loss allowed (no wash sale rule for property) |
| Customer's NFT sales on one marketplace total USD 450 in 2026 | The broker may not issue a Form 1099-DA under the optional method; still report |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| What a digital-art NFT represents | Show both rates; do not assume the lower one |
| Acquisition gas fees | Basis without them until records are found |
| Whether a creator is in a business | Ask about regularity and profit motive; do not drop self-employment tax without facts |
| Value of an NFT given or donated | No deduction or gift value until appraised or reliably priced |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| NFT tied to a physical collectible | 28% maximum rate |
| Large secondary royalties | Ordinary and possibly self-employment income each year |
| Donated NFT claimed above USD 5,000 without an appraisal | Deduction can be denied |
| Fractional or revenue-share NFTs | Possibly securities: refer |
| Many marketplace and wallet transactions | Reconstruct with the `us-crypto-tax` method |

## Worked cases

Amounts are invented; rates are the 2026 statutory rates.

**Case 1, a decision: is it a collectible?** A single collector with 2026 taxable income of USD 300,000 before the sale (in the 15% long-term band and a 35% ordinary bracket) sells, after 3 years, an NFT bought for USD 10,000 for USD 60,000 (net of fees): long-term gain USD 50,000. If the NFT represents ownership of a physical painting (a collectible under the look-through test), the gain is taxed at 28% = USD 14,000. If it represents virtual land (not a collectible), at 15% = USD 7,500. A purely digital artwork falls between the two under the open question in Notice 2023-27: show both figures (a USD 6,500 difference), and report at the rate the reviewer accepts.

```oa-check
name: NFT long-term gain, collectible or not (2026)
inputs:
  proceeds: 60000
  basis: 10000
steps:
  - gain: proceeds - basis
  - tax_if_collectible: gain * 0.28
  - tax_if_not_collectible: gain * 0.15
  - difference: tax_if_collectible - tax_if_not_collectible
expected:
  gain: 50000.00
  tax_if_collectible: 14000.00
  tax_if_not_collectible: 7500.00
  difference: 6500.00
```

**Case 2: a creator's sales and royalties.** A digital artist in a business sells her own NFTs for USD 20,000 in 2026 and receives USD 3,000 of secondary royalties; gas and platform fees are USD 1,500. She has no wages. Net Schedule C profit: USD 21,500. Self-employment tax: 21,500 x 92.35% x 15.3% = USD 3,037.85, of which half (USD 1,518.93) is deductible on Schedule 1. Income tax on the profit follows at ordinary rates.

```oa-check
name: NFT creator self-employment tax (2026)
inputs:
  sales: 20000
  royalties: 3000
  fees: 1500
steps:
  - net_profit: sales + royalties - fees
  - se_tax: net_profit * 0.9235 * 0.153
  - deductible_half: se_tax * 0.5
expected:
  net_profit: 21500.00
  se_tax: 3037.85
  deductible_half: 1518.93
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NFT-SEC | Fractional, revenue-sharing or investment-contract NFTs | Refer: possible securities treatment |
| R-NFT-VALUE | Gift or donation of a unique NFT with no market price | Refer to a qualified appraiser |
| R-NFT-P2E | Play-to-earn or NFT-based gaming at business scale | Refer: business and inventory questions |
| R-NFT-RECORDS | No records of what was paid, in what token, and when | Reconstruct first (`us-crypto-tax`, R-CRYPTO-1) |
| R-NFT-STATE | State tax | The state skill |

## Filing and payment

- Report on the **2026 Form 1040**, due **15 April 2027** (extension to 15 October 2027 for filing only): the digital asset question, Form 8949 and Schedule D for sales, Schedule C and Schedule SE for creators, Form 8283 for donations.
- Form 709 for gifts above the annual exclusion, due 15 April 2027.
- No tax is withheld on NFT sales: pay through 2026 estimated tax (`us-quarterly-estimated-tax`).

## Completion checklist

- [ ] Each NFT classified: collector or creator; what its associated right or asset is.
- [ ] Collectible status decided under Notice 2023-27, with open digital-art cases flagged.
- [ ] Basis includes acquisition gas and fees; the crypto used to pay treated as disposed of.
- [ ] Holding periods checked (more than one year for long-term).
- [ ] Creators: sales and royalties on Schedule C, costs supported, self-employment tax computed.
- [ ] Forms 1099-DA reconciled; sales with no form still reported.
- [ ] Gifts and donations valued; qualified appraisal above USD 5,000.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Notice 2023-27. Read for the look-through analysis ("the IRS intends to determine whether an NFT constitutes a collectible"), the gemstone and virtual land examples and the request for comments. | https://www.irs.gov/pub/irs-drop/n-23-27.pdf | 2026-11-13 |
| Notice 2014-21. Read for property treatment of virtual currency. | https://www.irs.gov/pub/irs-drop/n-14-21.pdf | 2026-11-13 |
| 26 U.S.C. 1 (govinfo). Read for (h)(4) "28-percent rate gain" and (h)(5) collectibles gain, held more than 1 year. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm | 2026-11-13 |
| 26 U.S.C. 408 (govinfo). Read for (m)(2), the list of collectibles. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408.htm | 2026-11-13 |
| 26 U.S.C. 1091 (govinfo). Read for "stock or securities". | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partVII-sec1091.htm | 2026-11-13 |
| 26 U.S.C. 1402 (govinfo). Read for (b) "less than $400". | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm | 2026-11-13 |
| 26 U.S.C. 170 (govinfo). Read for (f)(11) appraisals above $5,000 and attachment above $500,000. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm | 2026-11-13 |
| Schedule SE (Form 1040) 2026. Read for line 4a, 92.35%. | https://www.irs.gov/pub/irs-pdf/f1040sse.pdf | 2026-11-13 |
| IRS, Self-employment tax. Read for the 15.3% rate. | https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes | 2026-11-13 |
| Instructions for Form 1099-DA (2026). Read for specified NFTs, the optional method and the $600 de minimis, and first sales by a creator or minter. | https://www.irs.gov/pub/irs-pdf/i1099da.pdf | 2026-11-13 |
| CCA 202302012. Read for the qualified appraisal requirement for donated cryptocurrency. | https://www.irs.gov/pub/irs-wd/202302012.pdf | 2026-11-13 |

Not yet confirmed: the IRS has not issued the guidance promised in Notice 2023-27, so collectible status rests on its announced look-through approach and the treatment of purely digital art is open; there is no NFT-specific ruling on gas fees or creator royalties, so those positions rest on general rules.
