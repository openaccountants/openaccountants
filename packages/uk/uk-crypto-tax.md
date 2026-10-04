---
name: uk-crypto-tax
description: Use this skill whenever asked about UK cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax UK", "Bitcoin UK tax", "HMRC crypto", "cryptoassets UK", "crypto capital gains UK", "staking tax UK", "mining tax UK", "NFT tax UK", "DeFi tax UK", "SA108 crypto", "crypto CGT", "bed and breakfasting crypto", "S104 pool", "crypto loss UK", "Coinbase UK tax", "Binance UK tax", "Revolut crypto UK", "crypto income UK", "DAC8 UK", "CARF crypto", "crypto reporting 2026", "18% 24% crypto", "HMRC cryptoassets manual", or any question about the income tax, capital gains tax, or reporting treatment of cryptocurrency, tokens, or digital assets for UK tax residents. Covers HMRC's Cryptoassets Manual (CRYPTO10000+), S104 pooling, same-day and 30-day matching rules, DeFi lending/staking, NFTs, mining, SA108 reporting, and the Crypto Asset Reporting Framework (CARF) from 2026. ALWAYS read this skill before touching any UK crypto work.
version: 2.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - uk-capital-gains-sa108
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK tax on cryptoassets for individuals

Tax year 2026/27 (6 April 2026 to 5 April 2027) is the year in force. Returns being filed now are for tax year 2025/26 (online deadline 31 January 2027), on the SA108 form HMRC labels "2026". Where a rule differs between those years, both are shown. This Guide sits alongside the UK Capital Gains Tax and SA108 Guide (uk-capital-gains-sa108), which holds the full rate, allowance, loss and SA108 rules; the crypto points here follow it.

## Scope and who this is for

UK resident individuals who buy, hold, swap, spend, give, lend or stake cryptoassets (exchange tokens such as bitcoin and ether, stablecoins, utility and security tokens, and NFTs), or who receive tokens from mining, staking, airdrops, DeFi or employment. It covers: what is and is not a disposal; allowable costs and fees paid in tokens; the same-day rule, the 30-day rule and Section 104 pools for tokens; forks and airdrops; lost keys, theft and negligible value claims; Income Tax on mining, staking, airdrops and employment tokens; DeFi lending and liquidity pools; the SA108 crypto boxes 13.1 to 13.8; the Cryptoasset Reporting Framework (CARF) from 1 January 2026; and the 2025/26 return.

Out of scope, refer: companies and other businesses holding tokens (Corporation Tax), anyone whose activity may be a trade (the badges of trade decide this, and trading profits replace CGT), trusts, non-residents and people with a split year or a return to the UK within 5 years, the foreign income and gains (FIG) regime, Scottish and Welsh Income Tax bands, VAT on NFTs or crypto businesses, and anyone designing arrangements to avoid tax.

## Ask the client first

- Were you UK resident in the tax year? Any year abroad in the last 5 years?
- Which platforms, wallets and chains did you use? Can you export every transaction (exchange CSVs, wallet addresses, block explorer links)?
- For each disposal: date, token type, number of tokens, sterling value, and fees. Did you swap one token for another, spend tokens, or give any away (to whom)?
- Did you buy the same token on the same day as a sale, or within 30 days after it?
- Did you receive tokens from mining, staking, lending, liquidity pools, airdrops or an employer? Did you have to do anything to get an airdrop?
- Any DeFi loans or liquidity pools? What did the platform give you back (the same token, a receipt token such as aETH or cETH, liquidity tokens, an NFT)? Were the terms a fixed return?
- Any forks, lost private keys, hacks, scams or tokens that are now worthless?
- Your taxable income for the year after the Personal Allowance, any capital losses brought forward, and other gains.
- Are you registered for Self Assessment? Did you use the real time CGT service? Have you given your National Insurance number or UTR to every platform (CARF)?
- Any unpaid tax on crypto from earlier years?

## The method, step by step

1. **Residence and scope.** Confirm UK residence and that the activity is not a trade. If it may be a trade, refer ([CRYPTO21150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21150)).
2. **List every event.** Split into income receipts (mining, staking, lending returns, airdrops for a service, employment tokens) and disposals (sales, swaps, spending, gifts, fees paid in tokens) ([CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100); [receiving cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets)).
3. **Income first.** Value income tokens in sterling when received. That value is taxed as income and becomes the CGT cost of those tokens.
4. **Convert everything to sterling** at the time of each transaction.
5. **Match each disposal** in this order, per token type: tokens acquired the same day; then tokens acquired in the next 30 days; then the Section 104 pool at average cost ([CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200)). NFTs are not pooled or matched.
6. **Gain or loss** = proceeds (market value for gifts, swaps and fees) less matched cost and allowable costs ([CRYPTO22150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22150)).
7. **Losses and claims.** Set same-year losses off in full; brought-forward losses only down to the allowance; consider negligible value claims ([if you make a loss](https://www.gov.uk/capital-gains-tax/losses)).
8. **Allowance and rates.** Deduct the £3,000 annual exempt amount; add taxable gains to taxable income; 18% within the basic rate band, 24% above ([CGT rates](https://www.gov.uk/capital-gains-tax/rates)).
9. **Report and pay.** SA108 if a reporting test is met (crypto in boxes 13.1 to 13.8); income on the main return; pay by 31 January after the tax year.

## Rates, allowances and thresholds by year

### CGT rates and annual exempt amount ([CGT rates and allowances](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances); [CGT rates](https://www.gov.uk/capital-gains-tax/rates))

| Disposal date | Individuals: within basic rate band / above | Trustees; personal representatives | Annual exempt amount: individuals / most trustees |
| --- | --- | --- | --- |
| 6 April 2026 to 5 April 2027 (2026/27) | 18% / 24% | 24% | £3,000 / £1,500 |
| 6 April 2025 to 5 April 2026 (2025/26) | 18% / 24% | 24% | £3,000 / £1,500 |
| 30 October 2024 to 5 April 2025 | 18% / 24% | 24% | £3,000 / £1,500 (one allowance for the whole of 2024/25) |
| 6 April 2024 to 29 October 2024 | 10% / 20% | 20% | (as above) |

- Crypto is taxed at the same main rates as other assets. The 2026/27 basic rate band is £37,700 of taxable income (income after the Personal Allowance).
- The allowance can be set against the gains charged at the highest rates. It is not transferable and cannot be carried forward. No allowance is due for a year in which the FIG regime or Overseas Workday Relief is claimed.
- 2024/25 only: the return did not automatically apply the new rates to disposals on or after 30 October 2024, so an adjustment was needed ([2024/25 adjustment](https://www.gov.uk/guidance/work-out-your-capital-gains-tax-adjustment-for-the-2024-to-2025-tax-year)). Check this on any amended or late 2024/25 return.

### Income Tax, 2026/27 (England, Wales and Northern Ireland) ([Income Tax rates](https://www.gov.uk/income-tax-rates))

| Band | Taxable income | Rate |
| --- | --- | --- |
| Personal Allowance | Up to £12,570 | 0% |
| Basic rate | £12,571 to £50,270 | 20% |
| Higher rate | £50,271 to £125,140 | 40% |
| Additional rate | Over £125,140 | 45% |

The Personal Allowance goes down by £1 for every £2 of adjusted net income above £100,000. Scotland has different bands: refer.

### Other thresholds

| Item | Figure | Source |
| --- | --- | --- |
| SA108 needed if chargeable assets disposed of were worth more than | £50,000 | [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf) |
| SA108 needed if gains before losses were more than | £3,000 | [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf) |
| Trading and miscellaneous income allowance | up to £1,000 a tax year | [receiving cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets) |
| Miscellaneous income from all sources: contact HMRC | between £1,000 and £2,500 | same |
| Miscellaneous income from all sources: register for Self Assessment | over £2,500 | same |
| Capital loss claim window | 4 years after the end of the tax year of disposal | [if you make a loss](https://www.gov.uk/capital-gains-tax/losses) |
| Negligible value claim: earliest date it can take effect | not more than 2 years before the start of the tax year of the claim | [TCGA 1992 s.24](https://www.legislation.gov.uk/ukpga/1992/12/section/24) |
| CARF: penalty for inaccurate or missing details given to a UK platform | up to £300 | [information for platforms](https://www.gov.uk/guidance/information-youll-need-to-give-to-uk-cryptoasset-service-providers) |
| CARF: first platform report | 1 January 2027 to 31 May 2027, for calendar year 2026 | [reporting user data](https://www.gov.uk/guidance/reporting-cryptoasset-user-and-transaction-data) |

## The rules in detail

### What is a disposal ([CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100); [selling cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets))

| Event | Treatment |
| --- | --- |
| Selling tokens for money | Disposal |
| Exchanging one type of token for another (including stablecoins) | Disposal of the tokens given up, at the sterling value of what is received |
| Paying for goods or services with tokens | Disposal |
| Giving tokens away (not to a spouse or civil partner) | Disposal at the sterling value given away, even though nothing was received |
| Gift to a spouse or civil partner | No gain, no loss; the recipient takes over the cost (see uk-capital-gains-sa108 for the separation rule) |
| Donation to charity | No CGT, unless it is a "tainted donation" |
| Moving tokens between addresses you beneficially own | Not a disposal |
| Mixer or tumbler returning the same type of token | Not a disposal; getting a different token back is a disposal |
| Fee paid in tokens | A disposal of the fee tokens at market value (see below) |
| Theft | Not a disposal, so no loss ([CRYPTO22450](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22450)) |
| Losing the private key | Not a disposal; a negligible value claim may be possible ([CRYPTO22400](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22400)) |

Where Income Tax has already been charged on the value of tokens, that amount is not taxed again as a gain (TCGA 1992 s.37): the later gain is only the rise in value since receipt.

### Allowable costs and fees ([CRYPTO22150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22150); [CRYPTO22280](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22280))

- **Allowable:** the sterling price paid (through the pool), transaction fees for putting the transaction on the ledger, advertising for a buyer or seller, professional costs of a contract, and the cost of a valuation or apportionment needed to work out the gain.
- **Not allowable:** costs already deducted for Income Tax, and mining costs such as equipment and electricity (they are not incurred wholly and exclusively to acquire the tokens).
- **Exchange fees:** a fee to buy tokens is a cost of acquisition; a fee to sell is a cost of disposal. Depositing or withdrawing sterling is not an allowable cost. A fee on a token-for-token swap relates to both tokens: HMRC accepts a 50/50 split between the token given up and the token acquired, and a fee may only be deducted once.
- **Fees paid in tokens** are a disposal of the fee tokens at market value, and that market value is also a cost of the main transaction. Where the fee token is the same type as the tokens sold on the same day, the same-day rule makes it one disposal.

### Matching and Section 104 pools ([CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200); [selling cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets))

| Order | Match the disposal against | Law |
| --- | --- | --- |
| First | Tokens of the same type acquired on the same day, by the same person in the same capacity | TCGA 1992 s.105 |
| Second | Tokens of the same type acquired in the 30 days after the disposal, earliest disposal first | TCGA 1992 s.106A |
| Third | The Section 104 pool for that token type, at average cost | TCGA 1992 s.104 |

- **One pool per token type.** Holding bitcoin, ether and litecoin means three pools, each with its own pooled allowable cost. Each acquisition adds its cost; each disposal from the pool takes the same proportion of pooled cost. HMRC's example: 100 tokens at £2 (£200) plus 300 at £1 (£300) gives 400 tokens costing £500, £1.25 each; selling 200 uses a cost of £250.
- **Same day.** All acquisitions of a token type on one day are one acquisition, and all disposals one disposal. Any excess on either side then goes to the 30-day rule, then to the pool.
- **30 days.** Tokens bought in the 30 days after a sale do not enter the pool; they are matched to the earlier sale. Any excess over the tokens sold in the preceding 30 days goes into the pool. For the UK residence condition on the 30-day rule and the full share-matching rules, see uk-capital-gains-sa108 and [CG51560](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg51560).
- **No other method.** First-in first-out, last-in first-out and choosing which tokens were sold are not used for fungible tokens.
- **NFTs** are separately identifiable, so they are not pooled and no matching rules apply. Each NFT is its own asset with its own cost.

### Forks and airdrops ([CRYPTO22300](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22300); [CRYPTO22350](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22350); [CRYPTO21250](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21250))

- **Hard fork.** Receiving the new tokens is not a disposal of the original tokens. The new tokens go into their own pool, and the pooled cost of the original tokens is split between the two pools on a just and reasonable basis (TCGA 1992 s.52(4)). HMRC does not prescribe a method and can challenge one that is not just and reasonable. If the exchange does not recognise the new tokens, all cost may stay with the original tokens if that is just and reasonable, or a negligible value claim may be considered. A soft fork creates no new tokens.
- **Airdrop, Income Tax.** Not always taxable. Income Tax may not apply if the tokens were received without doing anything in return and not as part of a trade or business involving exchange tokens or mining. An airdrop given in return for, or in expectation of, a service is taxed as miscellaneous income (or as a trade receipt).
- **Airdrop, CGT.** Airdropped tokens join an existing pool of that token if the person already holds it; otherwise they start a new pool. A later disposal may give a chargeable gain even if no Income Tax arose on receipt. If Income Tax was charged, that value is the cost. If not, HMRC's manual does not state the cost; TCGA 1992 s.17(2) disapplies market value for an acquisition with no corresponding disposal and no consideration, which points to a nil cost ([TCGA 1992 s.17](https://www.legislation.gov.uk/ukpga/1992/12/section/17)). Use nil unless advised otherwise, and refer where it matters.

### Losses, lost keys, fraud and negligible value ([CRYPTO22500](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22500); [if you make a loss](https://www.gov.uk/capital-gains-tax/losses); [TCGA 1992 s.24](https://www.legislation.gov.uk/ukpga/1992/12/section/24))

- **Loss claims.** Report a loss on the return (or by letter if never registered for Self Assessment) within 4 years after the end of the tax year of disposal. Same-year losses come off same-year gains in full; brought-forward losses only bring gains down to the allowance; the rest carries forward. No carry-back, except in the year of death. A loss on a disposal to a connected person can only be used against gains on disposals to that person.
- **Negligible value claim.** If tokens become worthless or of negligible value while you own them, you can claim to be treated as selling and immediately reacquiring them at the value stated (which may be £nil), crystallising a loss. Because tokens are pooled, the claim must cover the whole Section 104 pool, not individual tokens. The claim states the asset, the value and the date. An earlier date can be used only if you owned the tokens then, they were already of negligible value then, and the date is not more than 2 years before the start of the tax year in which the claim is made. Make the claim when reporting the loss.
- **Lost private key.** Not a disposal. If there is no prospect of recovering the key or the tokens, a negligible value claim may be made.
- **Theft and scams.** Theft is not a disposal (you still own the asset and can try to recover it), so no loss. If you paid for tokens you never received, you may not be able to claim a loss. Tokens received that later become worthless may support a negligible value claim; tokens worthless when acquired do not.

### Income Tax on tokens received ([receiving cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets); [CRYPTO21100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21100); [CRYPTO21150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21150); [CRYPTO21200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200); [CRYPTO21300](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21300))

| Source | Treatment |
| --- | --- |
| Mining, not a trade | Sterling value at receipt is miscellaneous income, less appropriate expenses |
| Staking (proof-of-stake rewards), not a trade | Same as mining |
| Mining or staking that is a trade | Trade receipts; depends on degree of activity, organisation, risk and commerciality: refer |
| Lending and liquidity pool returns, not a trade | Income if the return is revenue in nature; see DeFi below |
| Airdrop for a service or in expectation of one | Miscellaneous income (or trade receipt) |
| Airdrop received for nothing, outside a trade | Income Tax may not apply; CGT on later disposal |
| Employment | Tokens are "money's worth": Income Tax and National Insurance on their value |

- **Allowance and registration.** Up to £1,000 a year of trading and miscellaneous income is covered by the allowance, and crypto income counts towards it. Tell HMRC if total miscellaneous income from all sources is between £1,000 and £2,500; register for Self Assessment if it is over £2,500.
- **Employment tokens.** Exchange tokens like bitcoin are readily convertible assets, so a UK employer must operate PAYE and National Insurance on its best estimate of their value. If the tokens are not readily convertible and the employer has not operated PAYE, the employee pays through Self Assessment.
- **Later sale.** Tokens taxed as income take their sterling value at receipt as their CGT cost; only the later rise in value is a gain.
- **Losses.** A trader may use trading losses (helpsheet HS227). Miscellaneous income losses may be carried forward against later miscellaneous income.

### DeFi lending and liquidity pools ([CRYPTO61110](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61110); [CRYPTO61212](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61212); [CRYPTO61214](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61214); [CRYPTO61620](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61620); [CRYPTO61650](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61650))

- **The return is not interest.** HMRC does not treat cryptoassets as money, so rules that apply to interest do not apply.
- **Revenue or capital.** The return is income (miscellaneous income under ITTOIA 2005 ss.687-689, if not a trade) where it pays the lender for the service of lending, for example an agreed 5% a year paid periodically. It is capital (CGT) where the lender's return comes from the uncertain growth in value of an asset, for example disposing of a liquidity token for an unknown amount. Factors: whether the return is known when the deal is made, who pays it, whether it is paid periodically or once, and the length of the loan. No single factor decides it; refer if unclear.
- **Is lending a disposal?** Only if beneficial ownership passes. If the platform or borrower can deal with the tokens as it wants, that strongly indicates it does; if it is restricted from dealing with them, it indicates not. Read the platform's terms.
- **Lender to borrower.** The lender disposes of tokens for a right to get tokens back. A known quantity is valued in sterling when the loan is made (TCGA 1992 s.48(1)); any part of the return taxed as income is excluded (s.37). When the loan is repaid, the tokens received are a second disposal (s.22(1)), picking up any change in value during the loan. An unknown return is a separate right valued at market value; a loss on it may be set against the gain on making the loan by election.
- **Liquidity provider receiving another token** (for example ether for aETH, cETH or liquidity tokens): a token-for-token exchange, so a disposal at the market value of the token received, and withdrawal is another exchange and disposal. If more than one type of token goes in, apportion on a just and reasonable basis.
- **Possible reform, not law.** HMRC has been developing a "no gain, no loss" approach for cryptoasset loans and liquidity pools. As at its November 2025 response, the government was still assessing it and the case for legislation ([DeFi consultation outcome](https://www.gov.uk/government/consultations/the-taxation-of-decentralised-finance-involving-the-lending-and-staking-of-cryptoassets/outcome/the-taxation-of-decentralised-finance-defi-involving-the-lending-and-staking-of-cryptoassets-summary-of-responses)). Apply the current rules above and check for any later change before filing.

### NFTs

- An NFT is a chargeable asset. Buying one with tokens is a disposal of those tokens. Selling, swapping or giving one away is a disposal of the NFT at its own cost (no pooling) ([CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200)).
- Creating and selling NFTs, and royalties, may be trading or miscellaneous income: refer. VAT on NFTs is out of scope.

### Cryptoasset Reporting Framework (CARF) from 1 January 2026 ([SI 2025/744](https://www.legislation.gov.uk/uksi/2025/744/made); [Finance Act 2026 s.275](https://www.legislation.gov.uk/ukpga/2026/11/section/275); [reporting user data](https://www.gov.uk/guidance/reporting-cryptoasset-user-and-transaction-data); [information for platforms](https://www.gov.uk/guidance/information-youll-need-to-give-to-uk-cryptoasset-service-providers); [CRYPTO10410](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10410))

The law as enacted:

- **Regulations.** The Reporting Cryptoasset Service Providers (Due Diligence and Reporting Requirements) Regulations 2025 (SI 2025/744) came into force on 1 January 2026. UK reporting cryptoasset service providers (exchanges, wallet apps that exchange tokens, NFT marketplaces, portfolio managers) must carry out due diligence on users, report to HMRC each calendar year by 31 May following, and notify users that their information will be reported.
- **UK residents are included.** Finance Act 2026 s.275 (in force 18 March 2026) applies the reporting duty to users resident in the UK (and entities with UK-resident controlling persons), not only to residents of other CARF countries. "Resident" means resident for income tax or corporation tax purposes.
- **First report.** Between 1 January 2027 and 31 May 2027, covering 1 January 2026 to 31 December 2026; then by 31 May each year for the previous calendar year. Users must be notified by 31 January following the first calendar year reported (31 January 2027 for 2026).
- **Overseas platforms.** Where the platform's country also follows CARF, that country's tax authority shares the information with HMRC.

What the client must do:

- Give every platform used (UK or not) full name, date of birth, home address and country, and tax identification number (for UK residents, the National Insurance number or UTR).
- Give accurate details. Inaccurate or missing details given to a UK platform can mean a penalty of up to £300 (SI 2025/744 reg. 13 limits it to deliberate failures or failures to take reasonable care); the penalty for non-UK platforms could be higher. A platform may also refuse further service.
- Assume HMRC will match platform data to the tax record. It does not change how gains or income are taxed. HMRC says that if tax is unpaid and it finds out, the penalty can be up to 100% of the tax due plus interest, and much higher for offshore matters.
- To put earlier years right, use the Cryptoasset Disclosure Service ([tell HMRC about unpaid tax on cryptoassets](https://www.gov.uk/guidance/tell-hmrc-about-unpaid-tax-on-cryptoassets)). Years to disclose: 4 if reasonable care was taken, up to 6 if careless, up to 20 if deliberate. Current and last year's income and gains go on the Self Assessment return instead.

The UK rules implement the OECD CARF through the regulations above. Questions about the EU's own rules (DAC8) for EU platforms: refer.

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Swap ETH for USDC | Disposal of the ETH at the sterling value of the USDC | [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100) |
| Move tokens from exchange to own hardware wallet | Not a disposal (beneficial ownership kept); any fee paid in tokens is a small disposal | [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100); [CRYPTO22280](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22280) |
| Sell and buy back the same token 10 days later | The buy-back is matched to the sale, not the pool | [CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200) |
| Buy back 31 days later | Outside the 30-day rule; the sale is matched to the pool | same |
| Gift to adult child | Disposal at market value; a loss is clogged | [if you make a loss](https://www.gov.uk/capital-gains-tax/losses) |
| Staking rewards, not a trade | Income at sterling value on receipt; that value is the CGT cost | [CRYPTO21200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200) |
| Airdrop for signing up and promoting | Miscellaneous income | [CRYPTO21250](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21250) |
| Hard fork | Split the original pool cost on a just and reasonable basis | [CRYPTO22300](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22300) |
| Tokens stolen by a hacker | Not a disposal; no loss | [CRYPTO22450](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22450) |
| Project collapsed, token worthless | Negligible value claim on the whole pool | [CRYPTO22500](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22500) |
| DeFi return agreed at a fixed rate, paid periodically | Points to income | [CRYPTO61214](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61214) |
| Deposit ETH, receive liquidity tokens | Token-for-token exchange: disposal | [CRYPTO61620](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61620) |
| Proceeds £50,000 or less and gains £3,000 or less, no claims | No SA108 needed for these disposals | [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf) |

## Worked cases

### Case A: same-day, 30-day and pool, 2026/27 ([CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200))

- Pool before: 10 ETH, pooled cost £15,000 (£1,500 each).
- 1 May 2026: sells 4 ETH for £8,000 (£2,000 each) and buys 1 ETH the same day for £2,100.
- 20 May 2026: buys 2 ETH for £3,800.
- Same day: 1 ETH sold (£2,000) matched to the 1 bought (£2,100): loss £100.
- 30 days: 2 ETH sold (£4,000) matched to the 20 May purchase (£3,800): gain £200.
- Pool: 1 ETH sold (£2,000) at pool cost £1,500: gain £500.
- Net gain £600. Pool after: 9 ETH costing £13,500. The same-day and 20 May tokens never enter the pool.

### Case B: fee paid in tokens (HMRC's example, [CRYPTO22280](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22280))

- Pool: 10,000 tokens costing £20,000. Sells 1,000 for £5,000 and pays a fee of 1 token (market value £5).
- Same day, same token, so one disposal of 1,001 tokens: proceeds £5,005; pooled cost 1,001/10,000 of £20,000 = £2,002; fee £5; gain £2,998.
- HMRC also accepts proceeds £5,000 less cost £2,002, the same £2,998 gain.

### Case C: staking income then sale, 2026/27 ([receiving cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets); [CRYPTO21200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200))

- Higher-rate taxpayer, no other trading or miscellaneous income, no expenses. Staking (not a trade) gives 0.5 ETH worth £1,800 in total when received.
- Income: the £1,000 allowance covers the first £1,000; £800 taxable at 40% = £320. Income over £1,000 but not over £2,500: if not already in Self Assessment, contact HMRC.
- Sells the 0.5 ETH in March 2027 for £2,200 (no other ETH held). CGT cost £1,800; gain £400, within the £3,000 allowance if no other gains.

### Case D: rate band, 2026/27 ([CGT rates](https://www.gov.uk/capital-gains-tax/rates))

- Taxable income after the Personal Allowance £30,000. Crypto gains £20,000, no losses.
- After the £3,000 allowance: £17,000. Basic rate band left: £37,700 less £30,000 = £7,700 at 18% = £1,386. The other £9,300 at 24% = £2,232. Total CGT £3,618.

### Case E: hard fork ([CRYPTO22300](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22300))

- Pool: 2 BTC costing £40,000. A fork gives 2 new tokens (NEW). Just after the fork, the 2 BTC are worth £100,000 and the 2 NEW £1,000.
- Splitting by market value (one just and reasonable method; HMRC prescribes none): NEW pool cost £40,000 x 1,000 / 101,000 = £396; BTC pool £39,604. No disposal on the fork.

### Case F: negligible value claim made in 2026/27 ([CRYPTO22500](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22500); [TCGA 1992 s.24](https://www.legislation.gov.uk/ukpga/1992/12/section/24))

- Pool of 5,000 XYZ tokens costing £4,000; the project collapsed and the tokens have been worthless since June 2025.
- Claim on the whole pool at £nil: allowable loss £4,000. An earlier effective date can go back no further than 6 April 2024 (2 years before the start of 2026/27), so a June 2025 date is allowed, putting the loss in 2025/26 if claimed as at that date.

### Case G: 2025/26 return being filed now ([SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf); [SA108 2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf))

- 40 crypto disposals in 2025/26, proceeds £60,000, allowable costs £58,000, gains £2,500, losses £500. No other disposals.
- Net gains £2,000, within the £3,000 allowance: no tax. But proceeds are more than £50,000, so the SA108 is needed: box 13.1 = 40, 13.2 = £60,000, 13.3 = £58,000, 13.4 = £2,500, 13.5 = £500. Do not deduct the allowance in the boxes.

## When to refuse or refer

- The activity may be a trade (frequent, organised, commercial dealing, or mining or staking run as a business).
- Non-residents, split years, a return to the UK within 5 years, FIG regime or remittance questions.
- Companies, partnerships, trusts or estates holding tokens.
- DeFi arrangements where the terms are unclear or involve collateral or borrowing; wrapped, bridged or liquid staking tokens.
- Scottish or Welsh taxpayers (Income Tax bands differ), and employment-related tokens where the employer did not operate PAYE.
- Records missing or not reconstructable: do not guess a cost. Refer, or use a nil cost only with the client's informed agreement and a note on the return.
- Earlier years with unpaid tax: advise a disclosure; refer if the behaviour may be deliberate or offshore.
- Refuse any request to hide, backdate or restructure transactions to avoid tax, or to omit platform data HMRC will receive.

## Filing and payment

### Deadlines ([Self Assessment deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines); [real time CGT service](https://www.gov.uk/report-and-pay-your-capital-gains-tax/print))

| Tax year | Register by | Paper return | Online return and tax due |
| --- | --- | --- | --- |
| 2025/26 | 5 October 2026 | 31 October 2026 | 31 January 2027 |
| 2026/27 | 5 October 2027 | 31 October 2027 | 31 January 2028 |

- If you register after 5 October 2026 for 2025/26, the filing deadline is 3 months from HMRC's notice, but tax is still due by 31 January 2027. To pay through your tax code, file online by 30 December 2026.
- UK residents not in Self Assessment can report gains through the real time CGT service: for a 2025/26 gain, report by 31 December 2026 and pay by 31 January 2027. If you are in Self Assessment, the gain also goes on the return (SA108 boxes 13.7 and 13.8).
- Crypto income (mining, staking, DeFi returns, airdrops for a service) goes in the miscellaneous or trading income parts of the return, not on the SA108.

### The 2025/26 SA108 being filed now ([SA108 2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf); [SA108 notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf))

- Rates for 2025/26: 18% within the basic rate band, 24% above; allowance £3,000. The SA108 is needed if proceeds were more than £50,000, gains before losses were more than £3,000, or a loss or other claim is made. Reporting a crypto disposal is not in itself a reason to file the SA108.
- The crypto section has been on the return since 2024/25. Report in sterling. Send computations for each gain or loss. The 2026/27 SA108 has not yet been published; use the same structure for planning and check the new form when it appears.

| Box | What goes in |
| --- | --- |
| 13.1 | Number of disposals (ignore disposals made as a trustee or in another capacity) |
| 13.2 | Disposal proceeds, before reliefs, claims or elections |
| 13.3 | Allowable costs, including purchase price |
| 13.4 | Gains in the year, before losses (after reliefs that reduce gains); includes gains within box 13.7 |
| 13.5 | Losses in the year; includes losses within box 13.7 |
| 13.6 | Claim or election code (for example NVC for a negligible value claim; see uk-capital-gains-sa108 for the list) |
| 13.7 | Total gains or losses on crypto reported on real time returns; references go in box 54 |
| 13.8 | Tax already paid on the box 13.7 gains |

### Records ([selling cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets); [how long to keep records](https://www.gov.uk/keeping-your-pay-tax-records/how-long-to-keep-your-records))

- For each pool and transaction: token type, date, number disposed of and left, sterling value, bank statements, pooled cost before and after each disposal. Also keep wallet addresses. For income tokens: type, date received, number, sterling value.
- Keep records for at least 22 months after the end of the tax year if the return is on time, or 15 months after sending a late return. Self-employed people (including crypto traders) must keep business records for longer: refer.

## Completion checklist

- [ ] UK residence confirmed; trade, trust, company and non-resident cases referred.
- [ ] Every transaction from every platform and wallet collected and converted to sterling at the time.
- [ ] Income tokens (mining, staking, DeFi income, service airdrops, employment) valued at receipt; £1,000 allowance and registration thresholds checked.
- [ ] Disposals include swaps, spending, gifts and fees paid in tokens; own-wallet transfers, theft and lost keys excluded.
- [ ] Matching done per token type: same day, next 30 days, then pool; NFTs kept separate; pool records updated.
- [ ] Allowable costs only (no mining costs, nothing already deducted for Income Tax); swap fees split once.
- [ ] Forks: pool cost split on a just and reasonable basis. Airdrops: pooled, cost settled.
- [ ] DeFi: beneficial ownership and revenue-or-capital tested against the platform's terms.
- [ ] Losses claimed within 4 years; negligible value claims made on whole pools, date within the 2-year limit.
- [ ] Allowance £3,000 deducted; rate band worked from taxable income against £37,700 (2026/27).
- [ ] SA108 tests checked; boxes 13.1 to 13.8 completed for 2025/26 with computations; real time returns cross-referenced.
- [ ] Client told about CARF: details given to every platform; HMRC will receive 2026 data from 2027.
- [ ] Earlier unpaid tax: Cryptoasset Disclosure Service considered.
- [ ] Figures labelled as estimates until records are confirmed.

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
