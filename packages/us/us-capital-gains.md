---
name: us-capital-gains
description: Work out a US resident individual's 2026 federal tax on capital gains. Covers short-term against long-term holding periods, the 0%, 15% and 20% rates with the 2026 maximum zero rate and 15 percent rate amounts from Rev. Proc. 2025-32 section 4.03, the 25% unrecaptured section 1250 group and the 28% collectibles group, the 3.8% net investment income tax under 26 U.S.C. 1411 with its fixed USD 250,000, 200,000 and 125,000 thresholds, the USD 3,000 (USD 1,500 separate) loss limit and the carryover worksheet, wash sales under section 1091, Form 8949 and Schedule D, the home sale exclusion and installment sales, with a 2025 return section and a sell-now-or-wait decision case. Trigger on "US capital gains tax", "long-term capital gains rate", "Schedule D", "Form 8949", "LTCG 0% bracket", "NIIT", "net investment income tax", "wash sale", "capital loss carryover", "sell shares tax US", "should I sell now or wait". Federal only. For nonresidents see us-nonresident-cgt; for QSBS see us-section-1202-qsbs; for like-kind exchanges see us-section-1031-like-kind-exchange.
version: "2.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US federal capital gains for resident individuals, tax year 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32, 26 U.S.C. 1, 121, 453A, 1031, 1091, 1211, 1212, 1222 and 1411, the 2026 draft Schedule D, Form 8949 and Form 8960, IRS Pub. 550, 523 and 537 (2025), IRS Notice 2023-27 and IRS Topics 409, 701 and 705, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, long-term gain (asset held more than 1 year) and qualified dividends are taxed at 0%, 15% or 20%, depending on where they sit on top of total taxable income. The 0% rate applies up to taxable income of **USD 49,450** (single and married filing separately), **USD 98,900** (joint) or **USD 66,200** (head of household); 20% applies above **USD 545,500**, **USD 613,700**, **USD 306,850** and **USD 579,600** respectively. Short-term gain is ordinary income. Collectibles gain is taxed at up to 28% and unrecaptured section 1250 gain at up to 25%. On top, the 3.8% net investment income tax applies to the smaller of net investment income or modified adjusted gross income above **USD 250,000** (joint), **USD 200,000** (single, head of household) or **USD 125,000** (separate); those thresholds are not indexed. A net capital loss offsets at most **USD 3,000** of other income (**USD 1,500** married filing separately), and the rest carries forward with no time limit.

## Scope and who this is for

In scope: US citizens and resident aliens filing Form 1040 for tax year 2026 who sell capital assets: shares, funds, bonds, digital assets held as investments, collectibles, a main home and investment real estate. It covers the rate on the gain, the net investment income tax (NIIT), the loss limit and carryover, wash sales, the home sale exclusion, installment sales, Form 8949 and Schedule D. A dated section covers 2025 returns still open on extension.

State tax is separate: most states tax capital gains under their own rules. This skill gives the federal answer only.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Nonresident aliens and dual-status years | `us-nonresident-cgt` |
| Qualified small business stock (section 1202), including the tiered exclusion for stock acquired after 4 July 2025 | `us-section-1202-qsbs` |
| Like-kind exchanges of real property (section 1031): deadlines, identification, boot, Form 8824 | `us-section-1031-like-kind-exchange` |
| The ordinary income tax rate schedule, standard deduction, the 2026 return due date and the full Form 1040 | `us-federal-income-tax-return-1040` |
| Digital asset events and Form 1099-DA detail | `us-crypto-tax` |
| NFT collectible status | `us-nft-tax` |
| Paying tax on a large gain during the year | `us-quarterly-estimated-tax` |
| Estates and trusts | `us-form-1041-trust-and-estate-income` |
| Mark-to-market traders, corporations | refer (see the refusal table) |
| State tax on the same gain | the state's income tax skill |

## Ask the client first

1. **Tax year of the sale (2025 or 2026) and filing status**: single, married filing jointly, married filing separately, head of household or qualifying surviving spouse. The rate thresholds and the NIIT threshold both depend on it.
2. **Trade dates of each purchase and sale**, and how the asset was acquired (bought, gift, inheritance, tax-free exchange). This fixes short-term or long-term.
3. **Basis**: Forms 1099-B and 1099-DA, whether basis was reported to the IRS, and any adjustments (reinvested dividends, gift or inheritance values).
4. **Type of asset**: collectible (art, antiques, metals, gems, stamps, coins, alcoholic beverages), depreciated real property, qualified small business stock, digital asset, main home.
5. **Purchases of substantially identical stock or securities in the 30 days before or after a loss sale**, in any account: the client's IRA or Roth IRA, the spouse's accounts and any corporation the client controls.
6. **Other 2026 income**: ordinary taxable income (to place the gain in the bands), modified adjusted gross income and net investment income (for the NIIT), and any capital loss carryover from the 2025 Schedule D.

For a home sale also ask: the dates of ownership and of use as the main home in the 5 years before the sale, any home sale in the prior 2 years that used the exclusion, any rental or home office depreciation, and any reason for an early sale (work, health, unforeseen event). For real estate traded for other real estate: the transfer date, the identification date, where both properties are, and whether a qualified intermediary held the proceeds (then load `us-section-1031-like-kind-exchange`). For a sale paid over time: the payment schedule, stated interest, whether the buyer is related, and any depreciation recapture.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Long-term gain and qualified dividends: maximum zero rate amount, married filing jointly and surviving spouse | USD 98,900 | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum 15 percent rate amount, married filing jointly and surviving spouse (20% above) | USD 613,700 | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum zero rate amount, married filing separately | USD 49,450 | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum 15 percent rate amount, married filing separately | USD 306,850 | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum zero rate amount, head of household | USD 66,200 | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum 15 percent rate amount, head of household | USD 579,600 | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum zero rate amount, all other individuals (single) | USD 49,450 | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum 15 percent rate amount, all other individuals (single) | USD 545,500 | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Rates on adjusted net capital gain | 0%, 15%, 20% | [26 U.S.C. 1(h)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| Maximum rate on unrecaptured section 1250 gain | 25% | [26 U.S.C. 1(h)(1)(E)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| Maximum rate on 28-percent rate gain (collectibles gain and the taxable part of section 1202 gain) | 28% | [26 U.S.C. 1(h)(1)(F) and 1(h)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| Long-term means held more than | 1 year | [26 U.S.C. 1222(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIII-sec1222.htm) |
| Net investment income tax rate | 3.8% | [26 U.S.C. 1411(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| NIIT threshold, joint return or surviving spouse | USD 250,000 | [26 U.S.C. 1411(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| NIIT threshold, married filing separately (half the joint amount) | USD 125,000 | [26 U.S.C. 1411(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| NIIT threshold, any other case (single, head of household) | USD 200,000 | [26 U.S.C. 1411(b)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| Capital loss allowed against other income, per year | USD 3,000 | [26 U.S.C. 1211(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1211.htm) |
| Same, married individual filing a separate return | USD 1,500 | [26 U.S.C. 1211(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1211.htm) |
| Wash sale window, before and after the loss sale | 30 days | [26 U.S.C. 1091(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partVII-sec1091.htm) |
| Home sale exclusion, per sale | USD 250,000 | [26 U.S.C. 121(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm) |
| Home sale exclusion, joint return meeting the joint conditions | USD 500,000 | [26 U.S.C. 121(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm) |
| Home sale ownership and use test, within the 5 years ending on the sale | 2 years | [26 U.S.C. 121(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm) |
| Interest on deferred tax (installment sales): obligation sales price over | USD 150,000 | [26 U.S.C. 453A(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453A.htm) |
| Same: face amount of such obligations arising in, and outstanding at the end of, the year above | USD 5,000,000 | [26 U.S.C. 453A(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453A.htm) |

Conditions on these figures:

- The eight 2026 band figures are "the maximum zero rate amounts and maximum 15 percent rate amounts under § 1(j)(5)(B), as adjusted for inflation", measured against **taxable income** (after deductions), not against the gain alone and not against AGI. The 0% rate applies up to and including the amount. Section 70101 of the One Big Beautiful Bill Act (P.L. 119-21) made the section 1(j) tables permanent, as Rev. Proc. 2025-32 section 3.01 records, so this structure continues for 2026.
- The NIIT thresholds, the 3.8% rate, the USD 3,000 and USD 1,500 loss limits and the home sale amounts are fixed by statute and **not indexed**: the IRS says of the NIIT thresholds that "these threshold amounts are not indexed for inflation" ([NIIT Q&A](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax)). They are the same for 2025 and 2026.
- The 25% and 28% figures are **maximum** rates: if the taxpayer's ordinary bracket is lower, the lower rate applies. The Schedule D Tax Worksheet does this.
- Net short-term gain has no special rate: it is ordinary income at the regular bracket rates in `us-federal-income-tax-return-1040`.

### Step 1: is it a capital asset and a taxable sale?

Almost everything owned for personal or investment use is a capital asset. Losses on personal-use property, such as a car or a main home, are not deductible ([Topic 409](https://www.irs.gov/taxtopics/tc409)).

### Step 2: short-term or long-term

Long-term means held **more than 1 year**; held 1 year or less is short-term ([26 U.S.C. 1222](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIII-sec1222.htm)). For listed securities the holding period begins the day after the trade date of the purchase and ends on the trade date of the sale; settlement dates do not count ([Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf)). Property acquired from a decedent and gifts with carryover basis follow special holding-period rules in Pub. 544: inherited property is treated as long-term, and for a gift taking the donor's basis the donor's holding period is added on ([Topic 409](https://www.irs.gov/taxtopics/tc409)).

### Step 3: gain or loss for each lot

Amount realized minus adjusted basis. Apply the wash sale rule (boundary table) to each loss before netting.

### Step 4: net within each class, then across

Short-term gains and losses net together, and long-term gains and losses net together. A net loss in one class then offsets a net gain in the other. A carried-over loss keeps its character: a long-term carryover reduces long-term gains before short-term gains ([Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf)). Net capital gain is net long-term gain over net short-term loss ([26 U.S.C. 1222(11)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIII-sec1222.htm)).

### Step 5: split the long-term gain into rate groups

- **28% group:** collectibles gain (gain on a collectible as defined in section 408(m), held more than 1 year) plus section 1202 gain (the eligible gain minus the exclusion), less collectibles losses, net short-term loss and long-term carryover ([26 U.S.C. 1(h)(4) and (5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm)).
- **25% group:** unrecaptured section 1250 gain, the part of the gain on depreciated real property that comes from depreciation, not more than the net section 1231 gain, reduced by any net loss in the 28% group ([Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf); [26 U.S.C. 1(h)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm)).
- **0/15/20 group:** all other net capital gain, plus qualified dividends.
- **NFTs:** Notice 2023-27 says the IRS intends to treat an NFT as a collectible when its associated right or asset is a section 408(m) collectible (the "look-through analysis"), until it issues guidance ([Notice 2023-27](https://www.irs.gov/pub/irs-drop/n-23-27.pdf)). This is interim guidance: flag it as uncertain, and see `us-nft-tax`.

### Step 6: stack the gain on top of ordinary income

Ordinary taxable income fills the brackets first; the preferential gain sits on top. Tax at 0% the part of the gain that falls at or below the maximum zero rate amount; at 15% the part between that and the maximum 15 percent rate amount; at 20% the rest. For the 0/15/20 group, with ordinary taxable income O, gain G and band figures Z (zero rate amount) and F (15 percent rate amount):

- at 0%: max(min(O + G, Z) - O, 0)
- at 15%: max(min(O + G, F) - max(O, Z), 0)
- at 20%: max(O + G - max(O, F), 0)

Use the Qualified Dividends and Capital Gain Tax Worksheet in the Form 1040 instructions. Use the Schedule D Tax Worksheet instead if Schedule D line 18 (28% Rate Gain Worksheet) or line 19 (Unrecaptured Section 1250 Gain Worksheet) has an amount, or Form 4952 is filed ([2026 draft Schedule D, line 20](https://www.irs.gov/pub/irs-dft/f1040sd--dft.pdf)).

### Step 7: a net loss and the carryover

If Schedule D line 16 is a loss, line 21 takes the smaller of the loss or USD 3,000 (USD 1,500 married filing separately), to Form 1040 line 7a ([2026 draft Schedule D, line 21](https://www.irs.gov/pub/irs-dft/f1040sd--dft.pdf); [26 U.S.C. 1211(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1211.htm)). The carryover, on the Capital Loss Carryover Worksheet (Pub. 550 Worksheet 4-1):

1. Line 1: taxable income (Form 1040 line 15), as a negative number if it would be below zero.
2. Line 2: the loss allowed on Schedule D line 21, as a positive number.
3. Line 3: line 1 plus line 2; if zero or less, zero.
4. Line 4: the smaller of line 2 or line 3. This is the part of the allowed loss treated as used ([26 U.S.C. 1212(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1212.htm): the lesser of the amount allowed or adjusted taxable income).
5. Short-term carryover: the net short-term loss minus (line 4 plus any net long-term gain). Long-term carryover: the net long-term loss minus (any net short-term gain plus the part of line 4 not absorbed by the short-term loss). So short-term losses are used first, even if they arose after a long-term loss.

When taxable income is low or negative, more of the loss carries forward, up to all of it. The current year's allowable deduction counts as used whether or not it was claimed or a return was filed. A carryover goes to Schedule D line 6 (short-term) or line 14 (long-term) of the next year, with no time limit ([Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf)).

### Step 8: the net investment income tax

On Form 8960: 3.8% of the lesser of (A) net investment income or (B) modified adjusted gross income over the threshold ([26 U.S.C. 1411(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm)). Net investment income includes capital gains, interest, dividends, annuities, royalties, rents, and income from a business that is passive for the taxpayer or that trades financial instruments or commodities. It excludes wages, most self-employment income and gain excluded under section 121 ([NIIT Q&A](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax)). The NIIT counts for estimated tax, so underpaying it can trigger the estimated tax penalty.

### Step 9: report

Form 8949, then Schedule D, then Form 1040 line 7a; Form 8960 for the NIIT. See Filing and payment.

## Boundary and exception table

| Rule | Condition that decides it | Source |
| --- | --- | --- |
| Long-term or short-term | Held **more than** 1 year is long-term; exactly 1 year or less is short-term; the count starts the day after the trade date | [26 U.S.C. 1222](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIII-sec1222.htm); [Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf) |
| 0% and 15% ceilings | Measured on taxable income after deductions, up to and including the amount | [Rev. Proc. 2025-32, section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Wash sale | A loss on stock or securities is disallowed if, within 30 days before or after the sale, the taxpayer buys substantially identical stock or securities, acquires them in a fully taxable trade, acquires a contract or option to buy them, or acquires them for an IRA or Roth IRA. A purchase by the spouse or a controlled corporation also counts | [26 U.S.C. 1091(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partVII-sec1091.htm); [Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf) |
| Wash sale basis | The disallowed loss is added to the basis of the new shares and the old holding period carries over, **except** when the IRA or Roth IRA made the purchase: then the loss is not added to basis | [Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf) |
| Wash sale and digital assets | Section 1091 is written for "stock or securities". Do not apply it, or rule it out, for a digital asset without first checking whether that asset is a security (see `us-crypto-tax`) | [26 U.S.C. 1091](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partVII-sec1091.htm) |
| Home sale, full exclusion | Owned **and** used as the main home for periods totalling 2 years or more in the 5 years ending on the sale; the two periods need not be the same; no other excluded sale in the 2 years before. Joint USD 500,000: either spouse meets ownership, **both** meet use, **neither** excluded a sale in the prior 2 years; otherwise the limit is the sum of each spouse's own limit | [26 U.S.C. 121(a), (b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm); [Topic 701](https://www.irs.gov/taxtopics/tc701) |
| Home sale, partial exclusion | Tests not met, but the main reason for the sale was a change of place of employment, health or unforeseen circumstances: the limit is multiplied by the shorter of the qualifying ownership-and-use period or the time since the last excluded sale, divided by 2 years. One safe harbor is a new workplace at least 50 miles farther from the home than the old one; Pub. 523 lists others (for example a first job at least 50 miles from the home, or the same events for a spouse, co-owner or other resident) | [26 U.S.C. 121(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm); [Pub. 523](https://www.irs.gov/pub/irs-pdf/p523.pdf) |
| Home sale, depreciation and nonqualified use | Gain equal to depreciation allowed or allowable after May 6, 1997 (rental, home office) is not excluded. Gain allocated to periods of nonqualified use after 2008 (not the main home, for example a rental or second home before it became the main home) is not excluded | [26 U.S.C. 121(b)(5), (d)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm); [Pub. 523](https://www.irs.gov/pub/irs-pdf/p523.pdf) |
| Home sale, surviving spouse | USD 500,000 still applies to an unmarried individual whose spouse died, if the sale is no later than 2 years after the death and the joint conditions were met just before it | [26 U.S.C. 121(b)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm) |
| Like-kind exchange | Real property held for business or investment only; property held primarily for sale, shares and other personal property do not qualify; US and foreign real property are not like kind. Deadlines, identification and boot are in `us-section-1031-like-kind-exchange` | [26 U.S.C. 1031(a), (h)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm) |
| Installment sale | Applies when at least one payment is received after the year of sale, unless the taxpayer elects out by the return due date (including extensions) for the year of sale. Not for losses, inventory, or stock and securities traded on an established securities market. Depreciation recapture is taxed in the year of sale | [Topic 705](https://www.irs.gov/taxtopics/tc705) |
| Installment interest | Interest is ordinary income; if the contract does not state adequate interest, part of the principal is treated as interest | [Topic 705](https://www.irs.gov/taxtopics/tc705) |
| Installment, related buyer resells | If a related buyer resells before paying in full and within 2 years of the first sale, the seller is treated as receiving the resale amount. For marketable securities the 2-year limit does not apply | [Pub. 537](https://www.irs.gov/pub/irs-pdf/p537.pdf) |
| Installment, interest on deferred tax | An obligation with a sales price over USD 150,000, when the face amount of such obligations arising during and outstanding at the close of the year is more than USD 5,000,000; interest continues while they remain outstanding | [26 U.S.C. 453A](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453A.htm); [Pub. 537](https://www.irs.gov/pub/irs-pdf/p537.pdf) |
| Loss carryover after joint years | A carryover from a joint return can be used only by the spouse who had the loss if they now file separately. A decedent's loss can be used only on the final return; the estate cannot carry it over | [Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf) |
| NIIT, nonresident and dual-status | Nonresident aliens are not subject to the NIIT. A dual-status individual pays it only for the resident part of the year, and the threshold is not reduced | [NIIT Q&A](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax) |

## Worked cases

The taxpayers are invented. The rates and thresholds are the 2026 figures in the table above; the ordinary 22% and 24% band edges for a single filer (USD 105,700 and USD 201,775) are from [Rev. Proc. 2025-32, section 4.01](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf), as set out in `us-federal-income-tax-return-1040`.

### Case 1, a decision: sell now, or wait until the gain is long-term?

A single filer bought shares on 15 December 2025. On 1 December 2026 they show a USD 30,000 gain. The client's other 2026 taxable income is USD 90,000, all ordinary. Selling on or after 16 December 2026 makes the holding period more than 1 year and keeps the sale in tax year 2026.

- **Sell now (short-term):** the gain is ordinary income on top of USD 90,000. USD 15,700 falls in the 22% band (up to USD 105,700): USD 3,454. The other USD 14,300 is in the 24% band: USD 3,432. Tax on the gain: USD 6,886.
- **Wait (long-term):** ordinary income of USD 90,000 is already above the USD 49,450 zero rate amount, and USD 120,000 is far below USD 545,500, so all USD 30,000 is taxed at 15%: USD 4,500.
- Waiting saves **USD 2,386**. MAGI is below USD 200,000, so there is no NIIT either way.
- **The figure that decides it:** after tax, the long-term sale keeps 85 cents of each dollar of gain. Waiting is better unless the price falls by more than USD 2,386 / 0.85 = **USD 2,807.06** in the 15 days. Recommend waiting unless the client sees a real risk of a larger fall. A hedge such as a put or a short sale against the shares has its own holding period rules in Pub. 550: refer.
- Had the client's ordinary taxable income been, say, USD 20,000, part of the long-term gain would be taxed at 0% and the saving larger; had it been above USD 545,500, the long-term rate would be 20% and the NIIT would likely apply to both options.

```oa-check
name: Sell now short-term or wait for long-term, single 2026
inputs:
  ordinary_income: 90000
  gain: 30000
  top_22: 105700
  top_24: 201775
  zero_top: 49450
  fifteen_top: 545500
steps:
  - st_22: max(min(ordinary_income + gain, top_22) - ordinary_income, 0) * 0.22
  - st_24: max(min(ordinary_income + gain, top_24) - max(ordinary_income, top_22), 0) * 0.24
  - tax_short_term: st_22 + st_24
  - lt_15: max(min(ordinary_income + gain, fifteen_top) - max(ordinary_income, zero_top), 0) * 0.15
  - tax_long_term: lt_15
  - saving_by_waiting: tax_short_term - tax_long_term
  - break_even_price_fall: saving_by_waiting / (1 - 0.15)
expected:
  tax_short_term: 6886.00
  tax_long_term: 4500.00
  saving_by_waiting: 2386.00
  break_even_price_fall: 2807.06
```

### Case 2: joint filers crossing the 20% line, with NIIT

A married couple filing jointly has 2026 ordinary taxable income of USD 560,000 and a USD 100,000 long-term gain on shares (taxable income USD 660,000). MAGI is USD 690,000 and net investment income is the USD 100,000 gain.

- 0%: none, because ordinary income is already above USD 98,900.
- 15%: from USD 560,000 up to USD 613,700, so USD 53,700 x 15% = USD 8,055.
- 20%: the remaining USD 46,300 x 20% = USD 9,260.
- NIIT: MAGI over USD 250,000 is USD 440,000; the lesser of that and USD 100,000 is USD 100,000; x 3.8% = USD 3,800 on Form 8960.
- Total federal tax on the gain: USD 21,115.

```oa-check
name: Joint filers, gain crosses the 20% amount, with NIIT (2026)
inputs:
  ordinary_income: 560000
  gain: 100000
  magi: 690000
  zero_top: 98900
  fifteen_top: 613700
  niit_threshold: 250000
steps:
  - at_0: max(min(ordinary_income + gain, zero_top) - ordinary_income, 0)
  - at_15: max(min(ordinary_income + gain, fifteen_top) - max(ordinary_income, zero_top), 0)
  - at_20: max(ordinary_income + gain - max(ordinary_income, fifteen_top), 0)
  - tax_15: at_15 * 0.15
  - tax_20: at_20 * 0.20
  - niit: min(gain, max(magi - niit_threshold, 0)) * 0.038
  - total: tax_15 + tax_20 + niit
expected:
  at_0: 0.00
  at_15: 53700.00
  at_20: 46300.00
  tax_15: 8055.00
  tax_20: 9260.00
  niit: 3800.00
  total: 21115.00
```

### Case 3: single filer, gain straddles the 0% amount

Taxable income USD 70,000, of which USD 40,000 is long-term gain; ordinary taxable income USD 30,000. 0% room: USD 49,450 - USD 30,000 = USD 19,450 taxed at 0%. The other USD 20,550 x 15% = USD 3,082.50. No NIIT (MAGI below USD 200,000).

```oa-check
name: Single filer, gain straddles the 0% amount (2026)
inputs:
  ordinary_income: 30000
  gain: 40000
  zero_top: 49450
steps:
  - at_0: max(min(ordinary_income + gain, zero_top) - ordinary_income, 0)
  - tax_15: (gain - at_0) * 0.15
expected:
  at_0: 19450.00
  tax_15: 3082.50
```

### Case 4: loss carryover when taxable income is negative

A single filer has a 2026 net short-term capital loss of USD 7,000 and no long-term items. Schedule D line 21 allows USD 3,000; taxable income after it would be minus USD 1,000. Worksheet: line 3 = -1,000 + 3,000 = USD 2,000; line 4 = the smaller of 3,000 and 2,000 = USD 2,000. Short-term carryover to 2027: USD 7,000 - USD 2,000 = **USD 5,000**, not USD 4,000, because USD 1,000 of the allowed loss did no work. By contrast, married filing separately with a USD 10,000 loss and ample income: USD 1,500 allowed, USD 8,500 carried over, keeping its character.

```oa-check
name: Capital loss carryover with negative taxable income (2026)
inputs:
  net_loss: 7000
  limit: 3000
  taxable_income_line_15: -1000
steps:
  - allowed: min(limit, net_loss)
  - line_3: max(taxable_income_line_15 + allowed, 0)
  - line_4: min(allowed, line_3)
  - carryover: net_loss - line_4
expected:
  allowed: 3000.00
  line_4: 2000.00
  carryover: 5000.00
```

### Case 5: joint filers, NIIT on a smaller gain

MAGI USD 300,000 and net investment income USD 80,000. MAGI over the threshold is USD 300,000 - USD 250,000 = USD 50,000, smaller than USD 80,000. NIIT: USD 50,000 x 3.8% = USD 1,900, on Form 8960.

### Case 6: home sale, full and partial exclusion

A single filer owned and lived in the home for 3 of the last 5 years, with no depreciation, no nonqualified use and no excluded sale in the prior 2 years; gain USD 300,000. Excluded USD 250,000; taxable long-term gain USD 50,000, reported on Form 8949 and Schedule D; the excluded part is also outside the NIIT. If instead they had used it for only 12 months and moved for a new job 60 miles farther from the home, with no earlier excluded sale, the limit is USD 250,000 x 12 / 24 = USD 125,000; gain above that is taxable.

### Case 7: wash sale

Bought 100 shares for USD 1,000, sold them for USD 750, and within 30 days bought 100 shares of the same stock for USD 800. The USD 250 loss is disallowed; the new basis is USD 800 + USD 250 = USD 1,050 and the old holding period carries over ([Pub. 550](https://www.irs.gov/pub/irs-pdf/p550.pdf), Example 1). Had the repurchase been in the client's IRA, the loss would not be added to basis.

## 2025 returns (tax year 2025, extended deadline 15 October 2026)

Use the 2025 amounts and the 2025 forms. The NIIT thresholds, the 3.8% rate and the USD 3,000 / USD 1,500 loss limit are the same as for 2026. The IRS states the 2025 amounts in [Topic 409](https://www.irs.gov/taxtopics/tc409) (they come from Rev. Proc. 2024-40):

| Filing status (2025) | 0% up to taxable income of | 15% up to taxable income of | 20% above |
| --- | --- | --- | --- |
| Single | USD 48,350 | USD 533,400 | USD 533,400 |
| Married filing jointly, surviving spouse | USD 96,700 | USD 600,050 | USD 600,050 |
| Married filing separately | USD 48,350 | USD 300,000 | USD 300,000 |
| Head of household | USD 64,750 | USD 566,700 | USD 566,700 |

- 2025 joint example: taxable income USD 120,000, of which USD 30,000 is long-term gain and qualified dividends; ordinary taxable income USD 90,000. 0% room USD 96,700 - USD 90,000 = USD 6,700; the other USD 23,300 x 15% = USD 3,495.
- Form 8949 and Schedule D for 2025 carry boxes G to L for digital asset transactions reported on Form 1099-DA ([2025 Schedule D instructions](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)).
- The extension moved the filing date only; tax was due by the April 2026 filing date, so interest and any late-payment penalty run from then ([IRS extensions page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-CG-QSBS | Qualified small business stock, including stock acquired after 4 July 2025 | Refer to `us-section-1202-qsbs`; check the acquisition date and holding period there before promising any exclusion |
| R-CG-NRA | Nonresident alien or dual-status year | Refer to `us-nonresident-cgt`; the rates and NIIT here assume residence |
| R-CG-1231 | Depreciation recapture on business property, section 1231 netting across several business assets, partnership interests including carried interests | Refer: Pub. 544 and Form 4797, with an accountant |
| R-CG-1031 | Like-kind exchange, especially with boot, related parties, reverse or build-to-suit structures, or a missed identification or exchange deadline | Refer to `us-section-1031-like-kind-exchange` and professional review; a qualified intermediary is needed |
| R-CG-TRADER | Mark-to-market traders, straddles, short sales against the box, options and section 1256 contracts | Refer: special rules in Pub. 550 |
| R-CG-UNSETTLED | NFT collectible status, whether section 1091 applies to a given digital asset, any state's tax on the gain | Do not state as settled: say what is uncertain and name the official source to check |
| R-CG-TRUST | Estate or trust selling assets | Refer to `us-form-1041-trust-and-estate-income`; trusts have their own band figures and NIIT rule |

## Filing and payment

- **Form 8949** lists each sale: boxes A to F for transactions other than digital assets, boxes G to L for digital asset transactions reported (or not) on Form 1099-DA ([2026 draft Form 8949](https://www.irs.gov/pub/irs-dft/f8949--dft.pdf)).
- **Schedule D:** sales with basis reported to the IRS on Form 1099-B or 1099-DA and no adjustments can go straight on line 1a (short-term) or 8a (long-term) without Form 8949. Carryovers go on lines 6 and 14. Line 16 nets the two parts and goes to Form 1040 line 7a; line 21 limits a loss to USD 3,000 or USD 1,500 ([2026 draft Schedule D](https://www.irs.gov/pub/irs-dft/f1040sd--dft.pdf)). The 2026 forms are drafts marked "DRAFT, NOT FOR FILING"; confirm the final line numbers when released.
- **Home sale:** report it if Form 1099-S was received or not all the gain is excluded ([Topic 701](https://www.irs.gov/taxtopics/tc701)).
- **Other forms:** Form 6252 for installment sales in the year of sale and each later year with payments ([Topic 705](https://www.irs.gov/taxtopics/tc705)); Form 8824 for like-kind exchanges; Form 8960 for the NIIT ([2026 draft Form 8960](https://www.irs.gov/pub/irs-dft/f8960--dft.pdf)).
- **Deadlines:** the 2026 return and any tax are due in April 2027 (the date is in `us-federal-income-tax-return-1040`); an extension to October moves filing only, not payment ([IRS extensions page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).
- **Estimated tax:** a large gain or NIIT can require estimated payments or more withholding. The fourth 2026 instalment is due 15 January 2027 ([Form 1040-ES (2026)](https://www.irs.gov/pub/irs-pdf/f1040es.pdf)); the other dates and the safe harbors are in `us-quarterly-estimated-tax`.

## Completion checklist

- Filing status and tax year confirmed; the 2026 table used for 2026 and the 2025 table for 2025.
- Every lot has a trade-date holding period and a basis that ties to the 1099-B or 1099-DA or to records.
- Wash sales checked 30 days either side of each loss sale, including IRA, Roth IRA and spouse accounts.
- Gains split into the 28%, 25% and 0/15/20 groups; the right worksheet chosen.
- Any net loss limited to USD 3,000 (USD 1,500 MFS); the carryover uses the worksheet (line 4) and short-term-first ordering, recorded by character.
- NIIT tested against the fixed thresholds; Form 8960 attached if due.
- Home sale: ownership, use, the 2-year lookback, depreciation after May 6, 1997, nonqualified use and partial exclusion checked.
- Installment election-out decided by the due date; recapture taxed in the year of sale.
- Section 1031, section 1202, nonresident and state points referred.
- For a sell-or-wait question, the holding-period date and the break-even price fall stated.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 4.03 (2026 maximum zero rate and 15 percent rate amounts, all filing statuses), section 3.01 (OBBBA section 70101 makes the section 1(j) tables permanent) and section 4.01 (single 22% and 24% band edges). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 1 (govinfo, 2024 edition). Read for (h)(1) rates 0/15/20, (h)(1)(E) 25%, (h)(1)(F) 28%, (h)(4) 28-percent rate gain, (h)(5) collectibles, (h)(6) unrecaptured section 1250 gain. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm | 2026-11-13 |
| 26 U.S.C. 1411 (govinfo). Read for (a)(1) the 3.8% rate on the lesser of NII or MAGI over the threshold, (b) the USD 250,000, half of it, and USD 200,000 thresholds, (c) the NII definition. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm | 2026-11-13 |
| 26 U.S.C. 1211 (govinfo). Read for (b) the USD 3,000 / USD 1,500 limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1211.htm | 2026-11-13 |
| 26 U.S.C. 1212 (govinfo). Read for (b)(1) carryover by character and (b)(2) the lesser-of rule with adjusted taxable income. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1212.htm | 2026-11-13 |
| 26 U.S.C. 1222 (govinfo). Read for the more-than-1-year test and the netting definitions (1) to (11). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIII-sec1222.htm | 2026-11-13 |
| 26 U.S.C. 1091 (govinfo). Read for (a) the 30-days-before-and-after window for stock or securities. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partVII-sec1091.htm | 2026-11-13 |
| 26 U.S.C. 121 (govinfo). Read for (a) 2 years in 5, (b)(1) USD 250,000, (b)(2) USD 500,000 joint conditions, (b)(4) surviving spouse, (b)(5) nonqualified use after 2008, (c) reduced limit, (d)(6) depreciation after May 6, 1997. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm | 2026-11-13 |
| 26 U.S.C. 1031 (govinfo). Read for (a) real property held for business or investment only and (h) US and foreign property. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm | 2026-11-13 |
| 26 U.S.C. 453A (govinfo). Read for (b) the USD 150,000 and USD 5,000,000 tests. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453A.htm | 2026-11-13 |
| Schedule D (Form 1040) 2026, draft. Read for lines 1a to 22, Form 1040 line 7a, line 20 worksheet choice and line 21 loss limit. | https://www.irs.gov/pub/irs-dft/f1040sd--dft.pdf | 2026-11-13 |
| Form 8949 (2026), draft. Read for boxes A to L, including G to L for Form 1099-DA digital asset transactions. | https://www.irs.gov/pub/irs-dft/f8949--dft.pdf | 2026-11-13 |
| Form 8960 (2026), draft. Read for the form's existence and year only. | https://www.irs.gov/pub/irs-dft/f8960--dft.pdf | 2026-11-13 |
| Instructions for Schedule D (Form 1040) 2025. Read for lines 1a and 8a, the 28% Rate Gain Worksheet references and the digital asset boxes. | https://www.irs.gov/pub/irs-pdf/i1040sd.pdf | 2026-11-13 |
| IRS Pub. 550 (2025). Read for the wash sale rule and Example 1, trade-date holding period, rate groups (28%, unrecaptured section 1250) and Worksheet 4-1 with the carryover rules. | https://www.irs.gov/pub/irs-pdf/p550.pdf | 2026-11-13 |
| IRS Pub. 523 (2025). Read for the 50-mile work safe harbor and other partial-exclusion examples. | https://www.irs.gov/pub/irs-pdf/p523.pdf | 2026-11-13 |
| IRS Pub. 537 (2025). Read for the related-person 2-year resale rule (not for marketable securities) and interest on deferred tax (USD 150,000, USD 5 million). | https://www.irs.gov/pub/irs-pdf/p537.pdf | 2026-11-13 |
| IRS Topic 409, Capital gains and losses. Read for the 2025 band amounts, the 25% and 28% groups, personal-use losses, the loss limit and line 7a. | https://www.irs.gov/taxtopics/tc409 | 2026-11-13 |
| IRS Topic 701, Sale of your home. Read for the 24-month ownership and use tests and when to report. | https://www.irs.gov/taxtopics/tc701 | 2026-11-13 |
| IRS Topic 705, Installment sales. Read for the election out, excluded property and recapture in the year of sale. | https://www.irs.gov/taxtopics/tc705 | 2026-11-13 |
| IRS, Questions and answers on the NIIT. Read for the thresholds "not indexed for inflation", NII categories, excluded home sale gain, nonresident and dual-status rules. | https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax | 2026-11-13 |
| IRS, Net investment income tax page. Read for the 3.8% on the lesser of NII or MAGI over the threshold. | https://www.irs.gov/individuals/net-investment-income-tax | 2026-11-13 |
| IRS Notice 2023-27. Read for the look-through analysis for NFTs. | https://www.irs.gov/pub/irs-drop/n-23-27.pdf | 2026-11-13 |
| Form 1040-ES (2026). Read for the 15 January 2027 fourth instalment date. | https://www.irs.gov/pub/irs-pdf/f1040es.pdf | 2026-11-13 |
| IRS, Get an extension to file your tax return. Read for "until October 15 to file" and "pay any tax you owe by the April filing date". | https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return | 2026-11-13 |

Not yet confirmed: the 2026 Schedule D, Form 8949 and Form 8960 are drafts and their 2026 instructions and the 2026 Pub. 550 were not yet published when read, so line numbers rely on the drafts and the method on the 2025 Pub. 550 and 2025 Schedule D instructions; the 2025 band amounts come from IRS Topic 409, not from a fresh reading of Rev. Proc. 2024-40.
