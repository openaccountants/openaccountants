---
name: uk-capital-gains-sa108
description: Use this skill whenever asked about UK capital gains tax for individuals. Trigger on phrases like "SA108", "capital gains tax", "CGT UK", "annual exempt amount", "disposal", "chargeable gain", "crypto CGT UK", "share sale UK", "property disposal CGT", "PPR relief", "principal private residence", "BADR", "BADR 18%", "Business Asset Disposal Relief", "Entrepreneurs' Relief", "Investors Relief 18%", "carried interest April 2026", "CGT 18% 24%", "bed and breakfasting", "30-day rule", "Section 104 pool", "negligible value claim", "CGT losses", "60-day reporting", "residential property CGT", or any question about computing, filing, or reporting capital gains on the UK Self Assessment return. Covers SA108 form, CGT rates, reliefs, crypto as CGT asset, share matching rules, property CGT reporting, and loss treatment. ALWAYS read this skill before touching any UK CGT work.
version: 2.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - uk-income-tax-sa100
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Capital Gains Tax for individuals and the SA108 pages

Tax year 2026/27 (6 April 2026 to 5 April 2027) is the year in force. Returns being filed now are for tax year 2025/26, on the SA108 form HMRC labels "2026". Where a rule changed between those years, both are shown. Rates for 2024/25 are kept because that year changed part-way through and amended returns still turn on it.

## Scope and who this is for

Individuals who are UK resident and make gains or losses on chargeable assets: shares and funds outside ISAs, cryptoassets, property that is not (or not wholly) the main home, business assets, and personal possessions. It covers the annual exempt amount, rates, Business Asset Disposal Relief (BADR), Investors' Relief, the share matching rules, Private Residence Relief (PRR) and Letting Relief, losses and negligible value claims, gifts and connected persons, when the SA108 is needed, the 60-day UK property return, crypto, and the 2025/26 SA108 box map.

Out of scope, refer: companies (Corporation Tax on gains), trusts and estates beyond the rates noted, non-residents except the reporting rule, the foreign income and gains (FIG) regime, carried interest from 6 April 2026, EIS/SEIS/VCT reliefs, gift hold-over and rollover relief computations, and anyone who buys and sells property as a trade (Income Tax, not CGT: [tax when you sell property](https://www.gov.uk/tax-sell-property/print)).

## Ask the client first

- Were you UK resident in the tax year? Have you been non-resident in the last 5 years? (Non-residents only pay on UK land and property, subject to the return-within-5-years rule.)
- What did you dispose of, and on what date was the contract made, and (for property) the completion date?
- What did you pay, when, and what buying, selling and improvement costs do you have evidence for?
- Was anything given away, sold cheaply, or sold to a relative, business partner, your company or a trust you set up?
- Any transfer to or from your spouse or civil partner? Were you living together at any point in that tax year?
- Did you buy the same shares or tokens again on the same day or within 30 days after a sale?
- For a home: dates you lived there, any periods away and why, any letting (whole house, or a lodger sharing with you), any exclusive business use, garden size, other homes and any nomination to HMRC.
- For a business or company sale: how long you owned it, your shareholding and voting rights, whether you were an officer or employee, and how much BADR you have claimed before.
- For shares you subscribed for as an outside investor: issue date, whether paid in cash, and whether you or anyone connected with you was ever an officer or employee.
- Any capital losses from earlier years, or shares or other assets that have become worthless?
- Your taxable income for the year after the Personal Allowance, and any Gift Aid or pension contributions that extend your basic rate band.
- Did you already file a Capital Gains Tax on UK property return or use the real time CGT service this year? Payment references?

## The method, step by step

1. **Residence and scope.** Confirm UK residence and that each item is a chargeable asset (not an ISA, gilt, private car, or chattel under the £6,000 rule) ([what you pay it on](https://www.gov.uk/capital-gains-tax/print)).
2. **Disposal date.** Use the contract date; a conditional contract is made when the condition is met ([TCGA 1992 s.28](https://www.legislation.gov.uk/ukpga/1992/12/section/28)). For a rate or relief change, check the anti-forestalling rule first ([CG10250](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg10250)).
3. **Proceeds.** Use actual proceeds, or market value for gifts, bargains not at arm's length and disposals to connected persons ([TCGA 1992 s.17](https://www.legislation.gov.uk/ukpga/1992/12/section/17); [s.18](https://www.legislation.gov.uk/ukpga/1992/12/section/18)).
4. **Cost.** Match shares and tokens (same day, next 30 days, then the Section 104 pool), then add allowable costs.
5. **Reliefs on the asset.** PRR and Letting Relief for a home; spouse transfers at no gain/no loss.
6. **Losses.** Set current-year losses against current-year gains in full; use brought-forward losses only to bring gains down to the annual exempt amount.
7. **Annual exempt amount.** Deduct £3,000, against the gains charged at the highest rate first ([CGT rates](https://www.gov.uk/capital-gains-tax/rates)).
8. **Rates.** Add taxable gains to taxable income (after the Personal Allowance). Use the basic rate band first against BADR or Investors' Relief gains, then against other gains at 18%; the rest at 24% ([BADR: work out your tax](https://www.gov.uk/business-asset-disposal-relief/print)).
9. **Report and pay.** 60-day return for UK residential property with tax to pay; then the SA108 if any reporting test is met; pay by 31 January after the tax year.

## Rates, allowances and thresholds by year

### Annual exempt amount ([CGT rates and allowances](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances))

| Tax year | Individuals, personal representatives, trustees for disabled people | Most other trustees |
| --- | --- | --- |
| 2026/27 | £3,000 | £1,500 |
| 2025/26 | £3,000 | £1,500 |
| 2024/25 | £3,000 | £1,500 |
| 2023/24 | £6,000 | £3,000 |
| 2022/23 | £12,300 | £6,150 |

- The allowance is not transferable and cannot be carried forward. No allowance is due for a year in which the FIG regime or Overseas Workday Relief is claimed.
- Personal representatives get the full allowance for the tax year of death and the following 2 tax years.

### Rates by disposal date ([CGT rates and allowances](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances); [TCGA 1992 s.1H](https://www.legislation.gov.uk/ukpga/1992/12/section/1H))

| Disposal date | Individuals: within basic rate band / above | Residential property | BADR or Investors' Relief gains | Trustees and personal representatives | Carried interest (individuals) |
| --- | --- | --- | --- | --- | --- |
| 6 April 2026 onwards (2026/27) | 18% / 24% | 18% / 24% | 18% | 24% | Not CGT: Income Tax and National Insurance |
| 6 April 2025 to 5 April 2026 (2025/26) | 18% / 24% | 18% / 24% | 14% | 24% | 32% |
| 30 October 2024 to 5 April 2025 | 18% / 24% | 18% / 24% | 10% | 24% | 18% / 28% |
| 6 April 2024 to 29 October 2024 | 10% / 20% | 18% / 24% | 10% | 20% (residential 24%) | 18% / 28% |

- From 30 October 2024 residential property and other assets are taxed at the same main rates. Before 30 October 2024, residential property was 18%/24% and other assets 10%/20%.
- 2024/25 split year: the 2024/25 return did not automatically calculate the new main rates for disposals on or after 30 October 2024, so an adjustment was needed ([2024/25 adjustment](https://www.gov.uk/guidance/work-out-your-capital-gains-tax-adjustment-for-the-2024-to-2025-tax-year)). Check this on any 2024/25 amendment or late return.
- The 2026/27 basic rate band is £37,700 ([CGT rates](https://www.gov.uk/capital-gains-tax/rates)). Taxable income means income after the Personal Allowance and other reliefs.

### BADR and Investors' Relief limits ([BADR](https://www.gov.uk/business-asset-disposal-relief/print); [HS308 2026](https://www.gov.uk/government/publications/investors-relief-2020-hs308/investors-relief-2026-hs308))

| Item | Rule |
| --- | --- |
| BADR lifetime limit | £1 million of qualifying gains (disposals from 11 March 2020) |
| Investors' Relief lifetime limit | £1 million for disposals on or after 30 October 2024; £10 million for disposals on or before 29 October 2024 |
| BADR and IR rate | 10% to 5 April 2025; 14% from 6 April 2025 to 5 April 2026; 18% from 6 April 2026 (for contracts straddling these dates, the rate can follow completion: see the anti-forestalling rows in the boundary table) |
| Gains above the limit | Charged at the normal rates |

### Reporting and other thresholds ([SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf); [what you pay it on](https://www.gov.uk/capital-gains-tax/print))

| Threshold | Figure |
| --- | --- |
| SA108 needed if chargeable assets disposed of were worth more than | £50,000 (2023/24 onwards) |
| SA108 needed if gains before losses were more than | £3,000 (the annual exempt amount) |
| Chattels (tangible movable property): gain exempt if the consideration does not exceed | £6,000; above that, the chargeable gain is capped at five-thirds of the excess over £6,000 ([TCGA 1992 s.262](https://www.legislation.gov.uk/ukpga/1992/12/section/262)) |
| Anti-forestalling: no excluded-contract claim needed if total gains under excluded contracts do not exceed | £100,000 ([CG10250](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg10250)) |
| Late 60-day property return, first penalty | £100 ([FA 2009 Sch 55 para 3](https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/3)) |

## The rules in detail

### When the SA108 is needed ([SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf); [work out if you need to pay](https://www.gov.uk/capital-gains-tax/print))

Fill in the SA108 if any one of these applies:

- chargeable assets sold or disposed of were worth more than £50,000 in total;
- chargeable gains before taking off losses were more than £3,000;
- you want to claim an allowable capital loss, or make any capital gains claim or election for the year;
- you have gains from an earlier year taxable in this year, or you are making a FIG regime claim.

You do not need to include: private cars; chattels disposed of for £6,000 or less each (TCGA 1992 s.262(1): exempt where the consideration "does not exceed £6,000"; losses are computed as if proceeds below £6,000 were £6,000, and sets sold to the same or connected people are treated as one asset: refer); ISA and PEP investments; gilts and Premium Bonds; your main home if full PRR covers the whole gain; betting and lottery winnings; personal injury or PPI compensation; foreign currency for personal use.

If you are registered for Self Assessment and your gains are under the allowance, you still report if the total proceeds were more than £50,000. Before 2023/24 the test was 4 times the allowance. Tax is not billed: you must work it out and report.

### Working out a gain; market value; gifts and connected persons ([market value](https://www.gov.uk/capital-gains-tax/print); [TCGA 1992 s.17](https://www.legislation.gov.uk/ukpga/1992/12/section/17); [s.18](https://www.legislation.gov.uk/ukpga/1992/12/section/18))

- **Gain** = proceeds less allowable costs: purchase price, incidental costs of buying and selling (fees, Stamp Duty, SDLT, SDRT), and improvement costs still reflected in the asset when sold. Normal maintenance such as decorating is not allowable, nor is loan interest on a home.
- **Disposal** includes a sale, a gift, a swap, and compensation such as an insurance payout. A part-disposal counts.
- **Market value replaces the price** for gifts (other than to a spouse, civil partner or charity), sales for less than worth to help the buyer, and other disposals not by way of a bargain at arm's length (s.17). Inherited assets take the value at death; assets held on 31 March 1982 use that date's value.
- **Connected persons.** A disposal to a connected person is always treated as not at arm's length, so market value applies (s.18(2)). A loss on it can only be set against gains on other disposals to the same person while still connected (s.18(3)): a "clogged loss", recorded separately and carried forward.
- **Who is connected:** your and your spouse's or civil partner's brothers, sisters, parents, grandparents and other ancestors, children and other descendants, and their spouses or civil partners; business partners (except genuine commercial partnership acquisitions); a company you control alone or with relatives; trustees of a settlement where you or a connected person is the settlor ([SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf)).
- **Spouse or civil partner.** No CGT on a gift or sale to a spouse or civil partner unless you were separated and did not live together at all in that tax year, or the goods were for their business to sell. The recipient takes over your cost. You cannot claim a loss on these transfers ([gifts to your spouse or charity](https://www.gov.uk/capital-gains-tax/gifts); [losses](https://www.gov.uk/capital-gains-tax/losses)).
- **Charity.** No CGT on a gift to charity. A sale to charity for more than cost but less than market value is taxed using the price the charity pays.
- **Valuations.** HMRC can check a valuation; use the post-transaction valuation check form and allow at least 3 months. Tick SA108 box 53 and explain any estimate or valuation in box 54.

### Share matching and the Section 104 holding ([HS284 2026](https://www.gov.uk/government/publications/shares-and-capital-gains-tax-hs284-self-assessment-helpsheet/hs284-shares-and-capital-gains-tax-2026); [CG51560](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg51560))

Shares of the same class in the same company are matched in this order:

| Order | Match against | Rule |
| --- | --- | --- |
| First | Shares acquired on the same day as the disposal | TCGA 1992 s.105(1) |
| Second | Shares acquired in the 30 days after the day of disposal ("bed and breakfasting") | TCGA 1992 s.106A(5); only if the seller was UK resident when they reacquired |
| Third | The Section 104 holding (all other shares of that class, at average cost) | TCGA 1992 s.104 |
| Then | Any shares left over: later acquisitions, earliest first | HS284 |

- The 30-day rule needs shares of the same class, acquired by the same person in the same capacity. A reacquisition as trustee, or new shares from a rights or bonus issue, is not matched.
- **Bed and ISA.** Shares held in an ISA are outside CGT, and the 30-day rule needs the same capacity, so a sale followed by a purchase inside an ISA is normally matched to the Section 104 holding, not to the ISA purchase. If the result depends on this, check with HMRC.
- **Section 104 average cost.** Add up the cost of the holding and divide by the number of shares. On a part sale the cost is shares sold divided by shares held, times the pool cost. HMRC's example: 100 shares at 80p (£80) plus 300 at £1.20 (£360) gives 400 shares costing £440, an average of £1.10; selling 150 uses a cost of £165 ([tax when you sell shares](https://www.gov.uk/tax-sell-shares/print)).
- Unit trusts, OEICs and investment trusts follow the same rules. Accumulation-unit notional distributions taxed as income are added to cost.
- Employee scheme shares, EIS/SEIS/VCT shares and reorganisations have their own rules: refer (HS285, HS287, HS297, HS298).

### Cryptoassets ([selling cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets); [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100); [receiving cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets))

| Event | Treatment |
| --- | --- |
| Selling tokens for money | Disposal |
| Exchanging one type of token for another | Disposal of the tokens given up |
| Paying for goods or services with tokens | Disposal |
| Giving tokens away (not to a spouse, civil partner or charity) | Disposal at the sterling value given away |
| Moving tokens between wallets or addresses you beneficially own | Not a disposal |
| Mixer or tumbler returning the same type of token | Not a disposal; a different token back is a disposal |
| Tokens received from mining, staking, lending or DeFi (not a trade) | Income when received; later CGT only on the rise in value since receipt |
| Tokens received as employment income | Income Tax and National Insurance, often through PAYE |

- Pool each type of token separately at average cost. HMRC's example: 100 tokens at £2 (£200) plus 300 at £1 (£300) gives 400 costing £500, £1.25 each; selling 200 uses a cost of £250.
- Tokens bought on the same day as a sale, or within 30 days after it, are matched as for shares, not pooled.
- Allowable costs include transaction fees, advertising, contracts, valuations and the pooled cost. Mining equipment and electricity, and costs already deducted for Income Tax, are not allowable.
- Keep, for each pool: token type, dates, number disposed of and left, sterling values, bank statements, pooled cost before and after each disposal. Exchange reports are not tax calculations.
- Report in sterling in the SA108 crypto section (boxes 13.1 to 13.8), available from 2024/25 returns. Earlier unpaid tax: the Cryptoasset Disclosure Service.
- Airdrops, forks, DeFi lending and liquidity pools, and anything that may be a trade: refer to the Cryptoassets Manual.

### Private Residence Relief and Letting Relief ([tax when you sell your home](https://www.gov.uk/tax-sell-home/print); [HS283 2026](https://www.gov.uk/government/publications/private-residence-relief-hs283-self-assessment-helpsheet/hs283-private-residence-relief-2026); [TCGA 1992 s.222](https://www.legislation.gov.uk/ukpga/1992/12/section/222); [s.223](https://www.legislation.gov.uk/ukpga/1992/12/section/223))

**Full relief, automatically, if all apply:** one home, lived in as the main home for the whole ownership; no part let out (a lodger does not count); no part used exclusively for business; grounds including buildings under 5,000 square metres; not bought just to make a gain.

**Partial relief.** Relief = gain × (periods of residence, plus periods treated as residence, plus the final 9 months) ÷ period of ownership. Ownership starts no earlier than 31 March 1982.

| Period | Treated as residence? |
| --- | --- |
| Final 9 months of ownership | Always, if the home was the only or main residence at some point |
| Final 36 months | If you are disabled or in long-term residential care and have no other relevant home right |
| Up to the first 2 years | If the home was being built or renovated, or the old home could not be sold, and you moved in within 2 years |
| Absences for any reason | Up to 3 years in total |
| Working in employment all of whose duties are outside the UK | Any length |
| Work elsewhere in the UK (location or employer requirement) | Up to 4 years in total |
| The above absences | Only if the home was your main residence before and after, unless work (yours or your spouse's) prevented return (s.223(3A)-(3B)) |

- **Garden and grounds:** relief up to 0.5 of a hectare including the site of the house; a larger area only if required for reasonable enjoyment of the house given its size and character. Land already fenced off or being developed at sale does not qualify.
- **Two or more homes:** one main residence at a time; a married couple or civil partners living together have one between them. Nominate by writing to HMRC within 2 years of each new combination of homes, signed by all owners. From 6 April 2015 an overseas home can be nominated only if you lived in it for at least 90 days in the tax year.
- **Nominal occupation.** Relief needs genuine residence as a home; short, token stays are open to challenge. Keep evidence of actual residence.
- **Letting Relief** applies only where you lived in the home at the same time as your tenant (shared occupancy). It does not apply where the whole house was let. It is the lowest of: the PRR due; £40,000; the gain arising from the letting. It does not cover gains while the home was empty.
- Sales before 6 April 2020 had an 18-month final period; before 6 April 2014, 36 months. Use them only for old-year corrections.
- Claim codes on the SA108: PRR (no Letting Relief) or LET (Letting Relief claimed).

### Business Asset Disposal Relief ([BADR](https://www.gov.uk/business-asset-disposal-relief/print); [HS275 2026](https://www.gov.uk/government/publications/entrepreneurs-relief-hs275-self-assessment-helpsheet/hs275-business-asset-disposal-relief-2026); [TCGA 1992 s.169N](https://www.legislation.gov.uk/ukpga/1992/12/section/169N))

| What is sold | Conditions (throughout the 2 years up to the disposal, unless stated) |
| --- | --- |
| All or part of your business (sole trader or partner) | You owned the business (directly or through the partnership). Assets of a continuing business qualify only as part of a disposal of part of the business. Letting of property is not a business for BADR. |
| Assets after the business closes | You owned the business for 2 years up to cessation, and you dispose of the assets within 3 years after it ceased |
| Shares or securities in your "personal company" | You are an officer or employee of the company or a group company; it is a trading company or holding company of a trading group; you hold at least 5% of the ordinary shares and 5% of the voting rights, and are entitled to at least 5% of either (a) distributable profits and assets on a winding up, or (b) proceeds if the company is sold |
| EMI option shares | Bought after 5 April 2013, option granted at least 2 years before the sale; the 5% test does not apply |
| Shares after the company stops trading | Sold within 3 years of it ceasing to trade |
| Personal asset used by your partnership or personal company ("associated disposal") | Made with a qualifying disposal of at least 5% of your partnership interest or shares; asset in business use for 2 years to withdrawal; owned 3 years if acquired on or after 13 June 2016; rent reduces the relief |

- **Rate** 14% for disposals from 6 April 2025 to 5 April 2026 and 18% from 6 April 2026 (10% before), on gains up to the £1 million lifetime limit. Gains over the limit are taxed at the normal rates.
- **Order:** the basic rate band is used first against BADR gains, and the annual exempt amount against gains charged at 24%, then any remainder against BADR gains.
- **Goodwill** sold to a close company in which you and relevant connected persons hold 5% or more does not qualify, unless you sell those shares within 28 days to a company where you hold less than 5%.
- **Dilution election:** where a share issue takes you below 5%, you may elect to be treated as selling and reacquiring just before the issue, and may elect to defer that gain.
- **Claim** on the return (SA108 box 50, total must not exceed £1 million; box 50.1 lifetime total claimed to date), or in writing / HS275 claim form. Deadline: the first anniversary of 31 January after the tax year of disposal: 31 January 2028 for 2025/26; 31 January 2029 for 2026/27. Spouses and civil partners each have their own limit.
- Trustees may qualify by reference to a qualifying beneficiary; personal representatives only for disposals made in the deceased's lifetime.

### Investors' Relief ([HS308 2026](https://www.gov.uk/government/publications/investors-relief-2020-hs308/investors-relief-2026-hs308))

- For outside investors in unlisted trading companies. The shares must be ordinary shares issued on or after 17 March 2016, subscribed for in cash and fully paid up, held for at least 3 years up to the disposal, in a trading company (or holding company of a trading group) none of whose shares are listed.
- Neither you nor anyone connected with you may be an officer or employee of the company or a connected company (an unpaid director may still qualify: CG63550).
- Rates as BADR: 10% before 6 April 2025, 14% for 2025/26, 18% from 6 April 2026. Lifetime limit £1 million for disposals on or after 30 October 2024 (£10 million for disposals on or before 29 October 2024), separate from BADR.
- A mixed holding (some shares not qualifying or not yet held 3 years) only gets relief on the qualifying proportion.
- Claim by the same deadline as BADR (31 January 2028 for 2025/26). SA108 box 49; do not include BADR gains there.

### Carried interest ([what you pay it on](https://www.gov.uk/capital-gains-tax/print); [CGT rates and allowances](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances))

From 6 April 2026 carried interest is not subject to CGT: HMRC says "You'll pay Income Tax and National Insurance contributions on carried interest you receive from 6 April 2026 instead." For 2025/26 individuals paid 32% CGT on carried interest gains (SA108 boxes 13 to 13C). Anything about the 2026/27 regime: refer.

### Losses and negligible value claims ([if you make a loss](https://www.gov.uk/capital-gains-tax/losses); [TCGA 1992 s.24](https://www.legislation.gov.uk/ukpga/1992/12/section/24); [negligible value claims](https://www.gov.uk/guidance/negligible-value-agreements); [TCGA 1992 s.62](https://www.legislation.gov.uk/ukpga/1992/12/section/62))

- **Same-year losses** are deducted from same-year gains in full, even if that wastes the annual exempt amount.
- **Brought-forward losses** are used only if gains are still above the allowance, and only to bring them down to the allowance; the rest carries forward with no time limit. Losses from before 5 April 1996 are used after later losses.
- **Claim** a loss on the return, or by letter if never registered for Self Assessment, within 4 years after the end of the tax year of disposal. An unclaimed loss cannot be used.
- **No carry-back**, except losses in the tax year of death, which can be set against gains of the 3 previous tax years, latest first (s.62(2)).
- **Connected persons:** a loss on a disposal to a connected person is clogged (see above). No loss is allowed on a transfer to a spouse or civil partner.
- **Negligible value claim.** If an asset has become of negligible value while you owned it, you can claim to be treated as selling and immediately reacquiring it at that value, creating an allowable loss. The claim can take effect at an earlier date only if you owned the asset then, it was already of negligible value then, and that date is not more than 2 years before the start of the tax year in which the claim is made (s.24(2)). An asset that was worthless when you acquired it does not qualify (except after a chain of no gain/no loss transfers). No claim is possible on or after the date a company is dissolved. Use claim code NVC.
- For quoted shares, HMRC's negligible value list shows securities already accepted; a claim is still needed. For unquoted shares, provide evidence (liquidator's letter, statement of affairs, balance sheet).
- **Losses against income:** some losses on shares subscribed for in qualifying trading companies can be set against income (SA108 boxes 41 to 44; HS286): refer. Trading losses can be set against gains (box 46).
- Entire loss or destruction of an asset is itself a disposal (s.24(1)); insurance or other compensation may be a disposal too.

### Non-residents, death and other boundaries ([what you pay it on](https://www.gov.uk/capital-gains-tax/print); [CGT rates and allowances](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances))

- **Non-residents** pay CGT on UK land and property (residential and non-residential) and on indirect disposals of UK property-rich companies, and must report every such disposal within 60 days even with no tax to pay. They do not pay on other UK assets unless they return to the UK within 5 years of leaving. For a former home, only gains since 5 April 2015 are taxed. Non-residents selling UK residential property get the allowance in most cases.
- **Death:** assets are acquired by the personal representatives at market value at death, and the deceased is not treated as disposing of them (s.62(1)). Beneficiaries later selling use that value.
- **Overseas assets** of a UK resident are chargeable; foreign tax may be credited: refer.
- **Property dealing** as a trade is Income Tax, not CGT.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Disposal on 29 vs 30 October 2024 (non-residential asset) | 10%/20% up to 29 October; 18%/24% from 30 October | [CGT rates and allowances](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |
| BADR disposal on 5 vs 6 April 2026 | 14% vs 18% | [BADR](https://www.gov.uk/business-asset-disposal-relief/print) |
| Contract before 6 April 2025, completion on or after 6 April 2026 (BADR/IR) | Rate follows completion unless it is an "excluded contract" (no purpose of a tax advantage from the timing rule; wholly commercial if connected); claim needed if excluded-contract gains exceed £100,000 | [CG10250](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg10250) |
| Contract before 30 October 2024, completion on or after 6 April 2025 (BADR/IR) | Rate follows completion (14% for completion in 2025/26) unless it is an "excluded contract"; same claim rule. Check this on 2025/26 returns being filed now | [CG10250](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg10250) |
| Contract made before 30 October 2024, completed on or after it | Same anti-forestalling rule for the main rate rise and the Investors' Relief limit cut | [CG10250](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg10250) |
| Property: exchange in one tax year, completion in the next | Tax year and rate follow the contract date (s.28, subject to anti-forestalling); the 60-day deadline runs from completion | [TCGA 1992 s.28](https://www.legislation.gov.uk/ukpga/1992/12/section/28); [report and pay](https://www.gov.uk/report-and-pay-your-capital-gains-tax/if-you-sold-a-property-in-the-uk-on-or-after-6-april-2020) |
| Repurchase on day 30 vs day 31 after a share sale | Day 30: matched to the repurchase; day 31: Section 104 holding | [CG51560](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg51560) |
| Repurchase while non-resident | 30-day rule does not apply | [CG51560](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg51560) |
| Shareholding exactly 5% of shares and votes | Meets "at least 5%" (with the 5% economic test) | [BADR](https://www.gov.uk/business-asset-disposal-relief/print) |
| Owned the business or shares 1 year 11 months | No BADR: 2 years needed (1 year before 6 April 2019) | [HS275 2026](https://www.gov.uk/government/publications/entrepreneurs-relief-hs275-self-assessment-helpsheet/hs275-business-asset-disposal-relief-2026) |
| Qualifying gain takes lifetime BADR above £1 million | Excess taxed at 18%/24% | [TCGA 1992 s.169N](https://www.legislation.gov.uk/ukpga/1992/12/section/169N) |
| Investors' Relief shares held 2 years 11 months | No relief: at least 3 years needed | [HS308 2026](https://www.gov.uk/government/publications/investors-relief-2020-hs308/investors-relief-2026-hs308) |
| Whole home let to tenants | PRR for residence periods and final 9 months; no Letting Relief | [HS283 2026](https://www.gov.uk/government/publications/private-residence-relief-hs283-self-assessment-helpsheet/hs283-private-residence-relief-2026) |
| One lodger sharing your living space | Not letting; full PRR can still apply | [tax when you sell your home](https://www.gov.uk/tax-sell-home/print) |
| Grounds over 0.5 of a hectare | Relief only for the area needed for reasonable enjoyment of the house | [TCGA 1992 s.222](https://www.legislation.gov.uk/ukpga/1992/12/section/222) |
| Gift to spouse, but separated all tax year | Normal rules: market value disposal | [gifts to your spouse or charity](https://www.gov.uk/capital-gains-tax/gifts) |
| Proceeds £50,000 exactly, gains under the allowance | Not "more than" £50,000: SA108 not needed on that test | [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf) |
| UK resident, UK home sale fully covered by PRR | No 60-day return and no SA108 entry needed | [report and pay](https://www.gov.uk/report-and-pay-your-capital-gains-tax/print); [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf) |
| Non-resident, UK property sale at a loss | 60-day return still required | [report and pay](https://www.gov.uk/report-and-pay-your-capital-gains-tax/print) |

## Worked cases

Cases are estimates for illustration. Each assumes no other gains, losses or reliefs unless stated.

### Case A: rate band, 2026/27 (HMRC's own examples, [CGT rates](https://www.gov.uk/capital-gains-tax/rates))

- Taxable income (after the Personal Allowance) £20,000; taxable gains £12,600. Less £3,000 allowance leaves £9,600. £20,000 + £9,600 = £29,600, within the £37,700 basic rate band, so all at 18%: CGT £1,728.
- Same income, gains £52,600. Less £3,000 leaves £49,600. £20,000 + £49,600 = £69,600, above £37,700. Band left: £37,700 − £20,000 = £17,700 at 18% (£3,186); the other £31,900 at 24% (£7,656). CGT £10,842.

### Case B: former home let out as a whole, sold in 2026/27 ([tax when you sell your home](https://www.gov.uk/tax-sell-home/print); [HS283 2026](https://www.gov.uk/government/publications/private-residence-relief-hs283-self-assessment-helpsheet/hs283-private-residence-relief-2026))

- Gain £120,000; owned 15 years; lived there 7.5 years, then let the whole house for 7.5 years.
- PRR: 7.5 years + final 9 months = 8.25 years of 15, 55% of the gain: £66,000. Chargeable gain £54,000.
- Letting Relief: none, because the whole house was let and the owner did not live there with the tenants.
- Higher-rate taxpayer, no other gains: £54,000 − £3,000 = £51,000 × 24% = £12,240.
- A Capital Gains Tax on UK property return and payment are due within 60 days of completion; the gain and the tax already paid then go on the 2026/27 SA108.

### Case C: shares sold and bought back within 30 days, 2025/26 ([HS284 2026](https://www.gov.uk/government/publications/shares-and-capital-gains-tax-hs284-self-assessment-helpsheet/hs284-shares-and-capital-gains-tax-2026))

- Holding of 9,500 shares. Sold 4,000 on 30 August 2025 for £6,000; bought 500 on 11 September 2025 for £850 (within 30 days, UK resident).
- 500 shares are matched to the 11 September purchase: proceeds 500 ÷ 4,000 × £6,000 = £750, cost £850, loss £100.
- The other 3,500 are matched to the Section 104 holding at average cost.
- Listed shares go in SA108 boxes 23 to 30 on the 2025/26 return.

### Case D: BADR above the lifetime limit, 2026/27 ([BADR](https://www.gov.uk/business-asset-disposal-relief/print); [TCGA 1992 s.169N](https://www.legislation.gov.uk/ukpga/1992/12/section/169N))

- Qualifying sale of personal-company shares on 1 June 2026 (unconditional contract and completion that day): gain £400,000. BADR already claimed in earlier years: £700,000. Taxable income uses the whole basic rate band.
- Lifetime limit left: £1 million − £700,000 = £300,000 at 18%: £54,000.
- Excess £100,000 at normal rates. The £3,000 allowance goes against the gain at 24% first: £97,000 × 24% = £23,280.
- Total CGT £77,280. Claim BADR by 31 January 2029 (box 50, box 50.1 lifetime total).

### Case E: crypto pool, 2026/27 ([selling cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets); [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf))

- Bought 100 tokens at £2 (£200), later 300 at £1 (£300): pool of 400 costing £500, £1.25 each. No same-day or 30-day purchases.
- Sells 200 tokens for £700. Cost £250; gain £450.
- Only disposal in the year: proceeds not more than £50,000 and gains not more than £3,000, so no tax and no SA108 entry needed on these facts. Keep the pool records.

### Case F: gift to a connected person at a loss ([TCGA 1992 s.18](https://www.legislation.gov.uk/ukpga/1992/12/section/18); [if you make a loss](https://www.gov.uk/capital-gains-tax/losses))

- A parent gives unlisted shares that cost £40,000 to their daughter when they are worth £30,000.
- The disposal is at market value (£30,000), giving a loss of £10,000.
- Because the daughter is connected, the loss is clogged: it can only be set against gains on later disposals to her while still connected. It cannot reduce the parent's other gains. Record it separately and carry it forward (SA108 box 47).

### Case G: 2025/26 return with a UK property already reported ([SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf); [CG-APP18-320](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg-app18-320))

- UK resident sold a buy-to-let (completed in 2025/26), filed the 60-day return and paid; later in the year sold listed shares at a gain.
- On the SA108 "2026": the property goes in the residential section, with box 6 including the gain and box 9 the gain reported on the UK property return, box 10 the tax already charged; the shares in boxes 23 to 30. Put the UK property return reference in box 54.
- The return recalculates the whole year's CGT; any further tax is due by 31 January 2027. If the year's total is less than tax already charged, it is an "initial overpayment" to be claimed back.

## When to refuse or refer

- **Refuse to compute** without the acquisition cost, dates and proceeds; ask for evidence. If records are lost, they must be recreated and shown as estimates (box 53).
- **Refuse to apply PRR** without evidence of genuine residence, or Letting Relief where the whole home was let.
- **Refuse** to treat a transfer between your own wallets or accounts as a disposal, or to set a connected-person loss against other gains.
- **Refer** where residence is uncertain or the client was non-resident, left or returned to the UK within 5 years, or claims the FIG regime or Overseas Workday Relief.
- **Refer** BADR or Investors' Relief where the trading status, the 5% tests, associated disposals, goodwill to a close company, or a contract that straddles 6 April 2025 or 6 April 2026 is in doubt.
- **Refer** carried interest (Income Tax from 6 April 2026), employee share schemes, EIS/SEIS/VCT, gift hold-over, rollover and incorporation relief, share reorganisations and takeovers.
- **Refer** crypto airdrops, forks, DeFi lending and liquidity pools, and any activity that may be a trade.
- **Refer** trusts, estates in administration, divorce transfers, and property development or dealing.
- **Refer** negligible value claims on unquoted shares, and any claim for losses against income.
- Where it is unknown whether the buyer or recipient is connected, treat them as connected: market value applies and any loss is clogged.
- Where the rate band is unknown, compute at 24% and say so. Where the date near a rate change is unknown, use the higher rate. Label every figure as an estimate until the client confirms the facts.

## Filing and payment

### 60-day return for UK property ([report and pay](https://www.gov.uk/report-and-pay-your-capital-gains-tax/if-you-sold-a-property-in-the-uk-on-or-after-6-april-2020); [reporting and paying](https://www.gov.uk/capital-gains-tax/print); [FA 2009 Sch 55 para 3](https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/3))

- **UK residents:** report and pay any CGT due on UK residential property within 60 days of completion (completions on or after 27 October 2021; 30 days for 6 April 2020 to 26 October 2021), using a Capital Gains Tax on UK property account. No return is needed if total gains are under the allowance.
- **Non-residents:** report every disposal of UK property or land, residential or not, within 60 days, even with no tax to pay.
- Details needed: address, acquisition date, exchange date, completion date, values at acquisition and disposal, costs, reliefs claimed. Joint owners each report their own share.
- If you cannot use the online service, the paper route gives a 14-character payment reference starting with "X".
- Late reporting or payment: interest and penalties. The first late-filing penalty is £100.
- If registered for Self Assessment, the sale must also go on the SA108 for the year, with the tax already paid.

### Real time CGT service (non-property gains) ([report and pay](https://www.gov.uk/report-and-pay-your-capital-gains-tax/print))

UK residents not in Self Assessment can report other gains through the real time service (for 2025/26 and 2026/27 disposals): report by 31 December after the tax year and pay by 31 January. For a 2025/26 gain: report by 31 December 2026, pay by 31 January 2027. Not for UK residential property, clients, trusts or estates. If already in Self Assessment, the gain also goes on the return.

### The 2025/26 SA108 being filed now ([SA108 2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf); [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf); [Self Assessment deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines))

- Deadlines for the 2025/26 return: paper by 31 October 2026; online by 31 January 2027; tax due by 31 January 2027. If you register after 5 October 2026, the filing deadline is 3 months from HMRC's notice, but tax is still due 31 January 2027.
- Rates for 2025/26: 18%/24%; BADR and Investors' Relief 14%; carried interest 32%; allowance £3,000.
- A BADR or IR sale contracted before 30 October 2024 but completed in 2025/26 takes the 14% rate unless it is an excluded contract; include any excluded-contract claim in the return ([CG10250](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg10250)).
- The 2026/27 SA108 has not yet been published; use the same structure for planning and check the new form when it appears.
- Send computations for each gain or loss with the pages. Do not deduct the annual exempt amount in the boxes; HMRC's calculation gives it automatically.

### SA108 box map for 2025/26 ([SA108 2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf); [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf))

| Section | Boxes | What goes in |
| --- | --- | --- |
| Residential property and carried interest | 3 to 13C | Number of disposals, proceeds, costs, gains (6) and losses (7); 9 and 10 for gains and tax on Capital Gains Tax on UK property returns; 11 and 12 for real time returns; 13 to 13C carried interest |
| Cryptoassets | 13.1 to 13.8 | Number of disposals, proceeds, costs, gains, losses, claim code, real time returns and tax paid |
| Other property, assets and gains | 14 to 22 | Includes all gains where BADR is claimed; 17.1 non-residential land and buildings; 17.2 to 17.4 split of BADR gains |
| Listed shares and securities | 23 to 30 | Disposals, proceeds, costs, gains, losses, claims |
| Unlisted shares and securities | 31 to 44 | As above, plus SEIS reinvestment and losses set against income |
| Losses and adjustments | 45 to 48 | Losses brought forward used (45), income losses set against gains (46), losses to carry forward (47), losses used against an earlier year (48) |
| Reliefs | 49, 50, 50.1 | Investors' Relief gains; BADR gains (not over £1 million); lifetime BADR claimed to date |
| Adjustments and non-resident CGT | 51 to 52.5 | Adjustments to CGT; non-resident CGT on UK property |
| Other information | 53, 54 | Estimates or valuations; details, references of UK property and real time returns, claims |

Claim codes (boxes 8, 13.6, 20, 28, 36): PRR, LET, GHO (gift hold-over), ROR, PRO (provisional rollover), ESH, BAD, INV, NVC, EOT, OTH, MUL (more than one).

## Completion checklist

- [ ] Residence status confirmed for the year; non-resident or returning cases referred.
- [ ] Every disposal listed with contract date, completion date, proceeds (or market value) and evidenced costs.
- [ ] Connected-person and gift disposals at market value; clogged losses recorded separately.
- [ ] Shares and tokens matched: same day, next 30 days, then pool; pool records updated.
- [ ] PRR worked by periods, final 9 months included; Letting Relief only for shared occupancy.
- [ ] BADR / Investors' Relief conditions checked for the full period; lifetime totals checked; anti-forestalling checked for contracts across a rate date.
- [ ] Current-year losses set off first; brought-forward losses only down to £3,000; loss claims within 4 years.
- [ ] Rate band worked from taxable income after the Personal Allowance; allowance set against the 24% gains first.
- [ ] 60-day return filed and paid for UK residential property; reference numbers noted for box 54.
- [ ] SA108 reporting tests checked (more than £50,000 proceeds; more than £3,000 gains; any claim).
- [ ] Right SA108 section and box for each asset, including crypto (13.1 to 13.8).
- [ ] Claims and deadlines diaried: BADR/IR by 31 January 2028 for 2025/26; return and payment by 31 January 2027.
- [ ] Computations, valuations and estimates attached; figures labelled as estimates until confirmed.

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
