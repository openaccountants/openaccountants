---
name: uk-crypto-tax
description: Use this skill whenever asked about UK cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax UK", "Bitcoin UK tax", "HMRC crypto", "cryptoassets UK", "crypto capital gains UK", "staking tax UK", "mining tax UK", "NFT tax UK", "DeFi tax UK", "SA108 crypto", "crypto CGT", "bed and breakfasting crypto", "S104 pool", "crypto loss UK", "Coinbase UK tax", "Binance UK tax", "Revolut crypto UK", "crypto income UK", "DAC8 UK", "CARF crypto", "crypto reporting 2026", "18% 24% crypto", "HMRC cryptoassets manual", or any question about the income tax, capital gains tax, or reporting treatment of cryptocurrency, tokens, or digital assets for UK tax residents. Covers HMRC's Cryptoassets Manual (CRYPTO10000+), S104 pooling, same-day and 30-day matching rules, DeFi lending/staking, NFTs, mining, SA108 reporting, and the Crypto Asset Reporting Framework (CARF) from 2026. ALWAYS read this skill before touching any UK crypto work.
version: 2.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - uk-capital-gains-sa108
category: crypto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
type: situation-rules
---

# UK tax on cryptoassets for individuals

Use sterling values at each transaction. Establish whether a receipt is income and whether beneficial ownership changes before calculating a capital gain. Current year: 2026/27; the return being filed for 2025/26 uses SA108 labelled 2026. The [UK capital gains Guide](uk-capital-gains-sa108.md) supplies the wider CGT rules; the conditions below apply to crypto too.

## Scope and who this is for

UK-resident individuals investing personally in exchange tokens, stablecoins, utility/security tokens and NFTs. This Guide covers disposals, costs, matching, losses, mining/staking/airdrop/employment receipts, DeFi, CARF and filing. UK-resident worldwide gains are generally within CGT ([TCGA s.1A](https://www.legislation.gov.uk/ukpga/1992/12/section/1A)). Do not classify an unknown token or uncertain trading activity automatically as an investment. Security-token contractual rights require their own analysis.

For trading businesses, companies, partnerships, trusts, estates, non-residence, split years, temporary non-residence, FIG/remittance questions, Scottish or Welsh income calculations and NFT/business VAT: **no usable specialist conclusion is supplied here. Check this point with one of our partner accountants.** The historic trustee/estate figures below are reference figures, not permission to compute those returns.

## Ask the client first

- Residence and years abroad; whose tokens and in what capacity?
- Every exchange, wallet, chain and transaction export; date, quantity, token, sterling value, fees and evidence of acquisition cost. Include swaps, spending, gifts and fee tokens.
- Same-day and subsequent purchases; complete activity in the following 30 days, including across the tax-year end.
- Mining, staking, airdrop conditions, employment and other trading/miscellaneous receipts; expenses, connected payers and allowance elections.
- DeFi contracts: who can deal with the assets, what right/token is received, whether the return is fixed, and repayment/withdrawal terms?
- Forks, lost keys, theft, scams and worthless assets; evidence of ownership and when value fell.
- Taxable income after allowances, rate-band extensions, other gains, current/prior losses, claims, Self Assessment status, earlier unpaid tax and real-time reports.

Do not invent a nil cost, use a daily closing price as though it were the transaction value, or choose income/CGT simply because it gives more tax. Reconstruct missing evidence; if material uncertainty remains, stop that computation. Check this point with one of our partner accountants.

## The method, step by step

### 1. Rates and the order of the computation

These are ordinary crypto investment rates, not carried-interest or business-relief rates. A disposal date normally follows the unconditional contract; contracts straddling the October 2024 change can engage anti-forestalling rules. Do not decide the applicable rate solely from settlement or contract date in those cases: Check this point with one of our partner accountants. ([TCGA s.28](https://www.legislation.gov.uk/ukpga/1992/12/section/28), [FA 2025 Sch.2](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2))

| Period | Individual: gains using unused basic band / other gains | Ordinary trustees / personal representatives | Individual AEA / most trustees | Official source |
| --- | --- | --- | --- | --- |
| 2026/27 | 18% / 24% | 24% | £3,000 / £1,500 | [HMRC rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances); [TCGA s.1H](https://www.legislation.gov.uk/ukpga/1992/12/section/1H), [s.1K](https://www.legislation.gov.uk/ukpga/1992/12/section/1K) |
| 2025/26 | 18% / 24% | 24% | £3,000 / £1,500 | [HMRC rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |
| 30 October 2024–5 April 2025 | 18% / 24% | 24% | £3,000 / £1,500 for the whole 2024/25 year | [HMRC rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |
| 6 April–29 October 2024 | 10% / 20% | 20% | The same single annual allowance | [HMRC rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |

For an ordinary gain, subtract the matched acquisition cost and allowable disposal costs. Deduct current-year allowable losses first, then the AEA, then brought-forward losses only as far as needed to eliminate taxable gains; retain unused prior losses. Allocate the AEA in the most beneficial way, including against higher-rate gains. It is not compulsorily split pro rata between the two 2024/25 windows. No AEA is due for a year with a foreign gain claim, foreign income claim or foreign employment election; historic remittance-basis years also need separate treatment. The AEA cannot be transferred or carried forward. Disabled-person trustees and personal representatives have special allowance rules: Check this point with one of our partner accountants. ([TCGA s.1K](https://www.legislation.gov.uk/ukpga/1992/12/section/1K), [HMRC losses](https://www.gov.uk/capital-gains-tax/losses), [HMRC allowances](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances))

In 2026/27, use the **£37,700 taxable-income basic band**, not £50,270 after already deducting the Personal Allowance. Apply 18% to ordinary taxable gains within the unused band and 24% to the rest; include other gains that consume it and any evidenced band extensions. For late/amended 2024/25 returns, HMRC's return did not automatically apply the higher post-change rates: use its [adjustment guidance](https://www.gov.uk/guidance/work-out-your-capital-gains-tax-adjustment-for-the-2024-to-2025-tax-year). ([TCGA s.1I](https://www.legislation.gov.uk/ukpga/1992/12/section/1I), [ITA s.10](https://www.legislation.gov.uk/ukpga/2007/3/section/10), [CGT rates](https://www.gov.uk/capital-gains-tax/rates))

For ordinary non-savings crypto income in England/Northern Ireland in 2026/27:

| Item | Amount / condition | Official source |
| --- | --- | --- |
| Standard Personal Allowance | £12,570, subject to eligibility and taper | [ITA s.35](https://www.legislation.gov.uk/ukpga/2007/3/section/35) |
| Basic rate | 20% on the first £37,700 of taxable income after allowances | [FA 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2); [ITA s.10](https://www.legislation.gov.uk/ukpga/2007/3/section/10) |
| Higher rate | 40% above that band up to the £125,140 higher-rate limit | [FA 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2); [ITA s.10](https://www.legislation.gov.uk/ukpga/2007/3/section/10); [HMRC income rates](https://www.gov.uk/income-tax-rates) |
| Additional rate | 45% above £125,140 | [FA 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2); [HMRC income rates](https://www.gov.uk/income-tax-rates) |
| Allowance taper | Reduced by £1 per £2 of adjusted net income above £100,000, reaching nil at £125,140 | [ITA s.35](https://www.legislation.gov.uk/ukpga/2007/3/section/35); [HMRC income rates](https://www.gov.uk/income-tax-rates) |

The familiar £50,270 gross-income boundary assumes a full £12,570 allowance; it is not the taxable-income basic band. Historic income-tax computations, Scottish/Welsh rates, National Insurance and payments on account need the applicable year's complete income calculation. Check this point with one of our partner accountants.

### 2. Identify disposals and allowable cost

| Event | Treatment and condition | Source |
| --- | --- | --- |
| Sale, swap (including stablecoins), spending | Disposal; value non-cash consideration in sterling | [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100) |
| Ordinary gift | Market value; a connected-person loss is restricted to gains on disposals to that same person while connected, subject to s.18(4) | [TCGA s.17](https://www.legislation.gov.uk/ukpga/1992/12/section/17), [s.18](https://www.legislation.gov.uk/ukpga/1992/12/section/18) |
| Spouse/civil partner | A disposal on a no-gain/no-loss basis when married/partners and living together; recipient takes over the tax cost. Separation/agreement/order cases have separate statutory limbs: Check this point with one of our partner accountants. | [TCGA s.58](https://www.legislation.gov.uk/ukpga/1992/12/section/58) |
| Charity | Generally no CGT on donation; exceptions include a tainted donation and a sale to charity for more than acquisition cost | [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100) |
| Own wallets | No disposal only if beneficial ownership is retained throughout | [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100) |
| Mixer/tumbler | Same type returned without an ownership-changing exchange: no disposal; different type returned: disposal | [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100) |

Allowable costs are confined by [TCGA s.38](https://www.legislation.gov.uk/ukpga/1992/12/section/38): acquisition consideration wholly and exclusively for the asset, qualifying transaction/professional/advertising/valuation costs and incidental disposal costs. HMRC includes ledger transaction fees. No deduction twice or for an expense already allowed for Income Tax. Mining equipment/electricity costs are not CGT acquisition costs of the mined tokens; trade expenses and capital allowances need a separate analysis. Fees for depositing/withdrawing sterling are not allowable. ([CRYPTO22150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22150))

A swap fee relates to both assets: apportion justly and reasonably; HMRC accepts 50/50. Deduct the sale part now and add the acquisition part to the new asset's cost; never deduct the whole twice. ([TCGA s.52](https://www.legislation.gov.uk/ukpga/1992/12/section/52), [CRYPTO22150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22150))

A fee **paid in tokens** also disposes of those fee tokens at market value. Their matched cost is separate from the market value of the service, which is a qualifying cost only where the underlying transaction qualifies. Same-type tokens disposed of on the same day/in the same capacity are aggregated; different fee-token types need separate computations. ([CRYPTO22280](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22280))

### 3. Match before using a pool

Apply separately for each token type, beneficial owner and capacity. Fungible tokens come within [TCGA s.104(3)](https://www.legislation.gov.uk/ukpga/1992/12/section/104); [CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200) applies the matching rules:

| Priority | Identify the tokens disposed of with | Source |
| --- | --- | --- |
| First | Same type acquired by the same person in the same capacity on the same day; aggregate that day's acquisitions and disposals | [TCGA s.105](https://www.legislation.gov.uk/ukpga/1992/12/section/105) |
| Second | Same type acquired in the same capacity in the next 30 days; earliest disposal first. The rule does not apply to an acquisition while non-UK-resident or treaty non-resident | [TCGA s.106A](https://www.legislation.gov.uk/ukpga/1992/12/section/106A) |
| Third | The relevant Section 104 pool | [TCGA s.104](https://www.legislation.gov.uk/ukpga/1992/12/section/104) |

Only unmatched acquisitions enter the pool. Pool-disposal cost = quantity disposed / quantity in pool × pooled cost; reduce both quantity and cost. For example, 100 tokens at £2 plus 300 at £1 = 400 costing £500; 200 sold use £250 cost, leaving 200/£250. A purchase 31 days later escapes the 30-day limb but does not automatically prove that the pool is the right match: where no holding can cover the disposal, later acquisitions can be matched in date order under s.105(2). Do not elect FIFO/LIFO or specific identification instead of the statutory order. ([CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200), [s.105](https://www.legislation.gov.uk/ukpga/1992/12/section/105))

NFTs are separately identifiable: no Section 104 pooling or fungible-token matching. Keep each NFT's own cost; paying tokens for an NFT disposes of the payment tokens. NFT creation, royalties, VAT and unusual rights: Check this point with one of our partner accountants. ([CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200))

### 4. Forks, airdrops and losses

A hard fork does not itself dispose of the original holding. New fungible tokens have a separate pool; split existing allowable cost justly and reasonably under [TCGA s.43](https://www.legislation.gov.uk/ukpga/1992/12/section/43) and [s.52(4)](https://www.legislation.gov.uk/ukpga/1992/12/section/52). No prescribed formula or automatic nil basis. If an exchange does not recognise the fork, leaving all cost in the original pool must still be just and reasonable, or a qualifying negligible-value claim may be considered. A soft fork normally creates no new tokens. ([CRYPTO22300](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22300))

Airdrops are not automatically income. An award in return for, or expectation of, a service is miscellaneous income or a trade receipt; receipt without doing anything in return and outside a relevant trade/business may escape Income Tax. A later disposal can still produce a gain. Fungible airdrop tokens join the relevant existing pool or start one. **No-income airdrop acquisition cost is held:** s.17(2)'s no-corresponding-disposal/no-consideration condition must be established; do not assume nil or market value. Check this point with one of our partner accountants. ([CRYPTO21250](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21250), [CRYPTO22350](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22350), [TCGA s.17](https://www.legislation.gov.uk/ukpga/1992/12/section/17))

- Lost key: not itself a disposal. A negligible-value claim may be possible if there is no prospect of recovering the key/access. ([CRYPTO22400](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22400))
- Theft: HMRC does not treat it as a disposal or allow a loss simply for theft. Paying for tokens never delivered is not automatically an allowable capital loss. If received tokens become worthless, consider a claim; tokens already worthless when acquired do not satisfy the ordinary “became negligible while owned” condition. The statutory no-gain/no-loss chain is a separate possible limb. ([CRYPTO22450](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22450), [TCGA s.24](https://www.legislation.gov.uk/ukpga/1992/12/section/24))
- Negligible value: claimant must still own an asset satisfying s.24's conditions; for pooled tokens claim for the **whole pool**. State the asset, value and effective date. It deems a sale/reacquisition at the claimed value. An earlier date requires ownership and negligible value then, no earlier than two years before the beginning of the claim tax year. Evidence of a project collapse alone is not proof of every condition. ([TCGA s.24](https://www.legislation.gov.uk/ukpga/1992/12/section/24), [CRYPTO22500](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22500))
- Notify HMRC of a quantified allowable capital loss, normally within four years after the loss tax year. Ordinary deadlines: 2024/25→5 April 2029; 2025/26→5 April 2030; 2026/27→5 April 2031. A person outside Self Assessment can notify by letter. Do not confuse this loss-notification deadline with the earlier-date limit for a negligible-value claim. Prior allowable losses carry forward subject to the ordering above. Death carry-back, trading and miscellaneous income-loss relief are held for specialist computation. Check this point with one of our partner accountants. ([TCGA s.16](https://www.legislation.gov.uk/ukpga/1992/12/section/16), [TMA s.43](https://www.legislation.gov.uk/ukpga/1970/9/section/43), [HMRC losses](https://www.gov.uk/capital-gains-tax/losses))

### 5. Income receipts

Non-trading mining and proof-of-stake rewards are miscellaneous income at sterling value when received, less appropriate expenses; the trade question depends on activity, organisation, risk and commerciality. Do not automatically impose trade NIC on miscellaneous receipts or deduct hardware “depreciation” without the applicable business rules. ([CRYPTO21150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21150), [CRYPTO21200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200), [ITTOIA s.687](https://www.legislation.gov.uk/ukpga/2005/5/section/687))

The **£1,000 trading allowance** is shared across relevant trade receipts and miscellaneous income, not per coin/platform. Full relief for income within it has statutory conditions and an opt-out. Above it, partial relief requires an election and replaces expense deductions; the allowance must be allocated across relevant sources. Check exclusions: rent-a-room interactions, payments by an employer or spouse/civil partner's employer, a firm in which the individual/connected person is a partner, or a close company in which the individual/associate is a participator. Do not grant the allowance automatically. ([ITTOIA ss.783A–783AQ](https://www.legislation.gov.uk/ukpga/2005/5/part/6A/chapter/1))

HMRC instructs people with total miscellaneous income from all sources between **£1,000 and £2,500** to contact HMRC; above **£2,500**, register for Self Assessment. These instructions do not remove another obligation to file or the need to make a relief election. ([Receiving cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets))

Employment tokens are money's worth subject to Income Tax/NIC. Where they are readily convertible assets, including exchange tokens like bitcoin, the employer operates PAYE/NIC using its best value estimate. Non-readily-convertible tokens without PAYE require employee Self Assessment. Reconcile what was paid; employment/NIC computations are held. Check this point with one of our partner accountants. ([CRYPTO21100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21100), [Receiving cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets))

For service/reward tokens, establish the market-value acquisition basis under [TCGA s.17(1)(b)](https://www.legislation.gov.uk/ukpga/1992/12/section/17); after income receipt, a later sale normally taxes only the subsequent rise, with matching still applied. This is not a rule that s.37 itself establishes every token's acquisition cost: **s.37 excludes income amounts from disposal consideration**. ([Receiving cryptoassets](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets), [TCGA s.37](https://www.legislation.gov.uk/ukpga/1992/12/section/37))

### 6. DeFi lending and liquidity pools

HMRC does not treat the lending return as interest because it does not treat cryptoassets as money. Determine revenue versus capital from the whole arrangement: service remuneration points to income; growth in a capital asset points to capital. An agreed 5% annual return, periodic payments, who pays, method of realisation, term and certainty are factors; none alone decides. A speculative return or an LP token alone does not establish capital treatment. ([CRYPTO61110](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61110), [CRYPTO61212](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61212), [CRYPTO61214](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61214))

Read the contract. A disposal on lending/staking arises if beneficial ownership passes; unrestricted ability to deal with tokens is a strong indicator, not a conclusive standalone test. Retained beneficial ownership means no disposal of the principal merely because tokens are lent. ([CRYPTO61620](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61620))

Where a loan disposes of tokens for an ascertainable quantity due back, value that quantity in sterling at the loan date under s.48; exclude the amount to be taxed as income under s.37 where applicable. Satisfaction disposes of the repayment right under s.22 and can recognise the intervening sterling-value change; the income exclusion must also be considered there. An unascertainable return can involve a separate right, valuation and loss election: **no usable calculation/election conclusion here. Check this point with one of our partner accountants.** ([TCGA s.48](https://www.legislation.gov.uk/ukpga/1992/12/section/48), [s.37](https://www.legislation.gov.uk/ukpga/1992/12/section/37), [s.22](https://www.legislation.gov.uk/ukpga/1992/12/section/22), [CRYPTO61620](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61620), [CRYPTO61650](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61650))

When beneficial ownership of deposited tokens passes in exchange for beneficial ownership of an LP/receipt token, there is a token exchange. Disposal proceeds are the sterling market value of the received token; its acquisition cost is the sterling market value of the transferred tokens. Allocate proceeds justly and reasonably between multiple deposited token types. Exchanging LP tokens back on withdrawal is another disposal at the value received. Do not equate every deposit with this fact pattern. ([CRYPTO61620](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61620), [CRYPTO61650](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61650))

Collateral, borrowing, wrapped/bridged/liquid-staking tokens, “impermanent loss”, unrecognised rights or proposed DeFi reform: **no usable specialist outcome or automatic separate relief is supplied. Check this point with one of our partner accountants.** Do not apply a proposed no-gain/no-loss regime without operative legislation. The old consultation narrative is not an exemption.

### 7. CARF: calendar years, not tax years

The UK regulations commenced **1 January 2026**, part-way through 2025/26. FA 2026 s.275 extends reporting to UK-resident users and entities with UK-resident controlling persons; residence means Income Tax/Corporation Tax residence. Use the statutory reporting-provider definition and exemptions; not every wallet/custodian is automatically a reporting provider. ([SI 2025/744 regs.1–3](https://www.legislation.gov.uk/uksi/2025/744/made), [FA 2026 s.275](https://www.legislation.gov.uk/ukpga/2026/11/section/275))

| Requirement | Date / scope | Official source |
| --- | --- | --- |
| First platform report | By 31 May 2027 for 1 January–31 December 2026; later reports by 31 May after the calendar year | [Reg.6](https://www.legislation.gov.uk/uksi/2025/744/regulation/6/made); [HMRC reporting](https://www.gov.uk/guidance/reporting-cryptoasset-user-and-transaction-data) |
| First user notification | By 31 January after the first calendar year reported: 31 January 2027 for a user first reported for 2026 | [Reg.8](https://www.legislation.gov.uk/uksi/2025/744/regulation/8/made); [FA 2026 s.275](https://www.legislation.gov.uk/ukpga/2026/11/section/275) |
| User self-certification penalty | Up to £300 for failure to provide valid self-certification, if deliberate or due to failure to take reasonable care; reasonable-excuse rule applies | [Regs.5,13,20](https://www.legislation.gov.uk/uksi/2025/744/made) |

The former “reports open 1 January 2027” statement is withdrawn: HMRC's 2 November 2026 update says the online service will not be available on that date. The deadline remains 31 May. A report summarises reportable transactions; a platform report does not replace the user's tax return. ([HMRC reporting](https://www.gov.uk/guidance/reporting-cryptoasset-user-and-transaction-data))

Individuals must provide name, date of birth, home address and country, and tax identification number (UK: NI number or UTR); no TIN is required where the user is not eligible for one. Give accurate details to every provider used, including overseas providers. Where the overseas country follows CARF, its authority shares information with HMRC. Do not promise a particular exchange date or foreign penalty. DAC8 and provider-level reporting/penalties are specialist holds. Check this point with one of our partner accountants. ([HMRC user information](https://www.gov.uk/guidance/information-youll-need-to-give-to-uk-cryptoasset-service-providers))

## Boundary and exception table

| Situation | Apply / stop condition |
| --- | --- |
| ETH→USDC | Swap is a disposal even if the stablecoin barely changes value; method 2 |
| Hardware-wallet transfer plus fee | Principal not disposed of if ownership retained; fee tokens separately tested; method 2 |
| Buy back 10 days later / 31 days later | Same-day priority, residence, capacity and available pool matter; method 3 |
| Gift to adult child | Market-value disposal and connected-loss restriction, not an ordinary usable loss; method 2 |
| Staking reward / promotional airdrop | Receipt classification and allowance conditions before tax; methods 4–5 |
| Fork / hack / collapsed project | Cost split, ownership and claim evidence differ; method 4 |
| Fixed DeFi rate / LP token | Neither alone settles income/capital or ownership; method 6 |
| Proceeds not over £50,000, gains not over £3,000 | These two triggers alone fail; check every other SA108 trigger below |

## Worked cases

These keep the original facts. Ordinary individual cases assume entitlement to the stated AEA, no specialist relief and no omitted transactions affecting matching; further factual assumptions are explicit. Apply the linked rules above, not a different year.

**A - same-day/30-day/pool, 2026/27.** Opening 10 ETH/£15,000. Sell 4 for £8,000 on 1 May 2026; buy 1 that day for £2,100 and 2 on 20 May for £3,800, same owner/capacity and UK residence throughout. Match 1: £2,000−£2,100=−£100; 2: £4,000−£3,800=£200; pool 1: £2,000−£1,500=£500. Net gain **£600**; pool left **9 ETH/£13,500**. Matched purchases do not enter it. [Matching source](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200).

**B - fee tokens.** Opening 10,000 tokens/£20,000; sell 1,000 for £5,000 and pay 1 same-type token worth £5 as the disposal fee that day. No competing acquisitions. Aggregate 1,001 tokens: proceeds £5,005; pool cost £2,002; fee £5; gain **£2,998**. HMRC accepts the alternative £5,000−£2,002 giving the same result. Pool left 8,999/£17,998. [HMRC example](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22280).

**C - staking then sale, 2026/27.** Higher-rate taxpayer, non-trade 0.5 ETH rewards worth £1,800 at receipt; no other relevant trade/miscellaneous income or expenses. Additional explicit conditions: no allowance exclusion, a valid partial-relief election, and the whole taxable receipt remains in the 40% band. (£1,800−£1,000)×40%=**£320**. At £1,800 miscellaneous income HMRC says contact it if not otherwise required to file; obtain the election rather than assuming relief. Sell the 0.5 ETH in March 2027 for £2,200, no other ETH/matching purchases: basis £1,800 under the service-reward valuation, gain **£400**, no CGT if the £3,000 AEA is otherwise unused. Without those allowance/election facts, the £320 is **not a usable conclusion**. Check this point with one of our partner accountants. [Staking](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200), [allowance law](https://www.legislation.gov.uk/ukpga/2005/5/part/6A/chapter/1), [TCGA s.17](https://www.legislation.gov.uk/ukpga/1992/12/section/17).

**D - band, 2026/27.** Taxable income after PA £30,000; crypto gains £20,000, no losses, no band extensions/other gains. £17,000 after AEA. £7,700 at 18%=£1,386; £9,300 at 24%=£2,232; total **£3,618**. [Rate calculation](https://www.gov.uk/capital-gains-tax/rates).

**E - fork.** 2 BTC pool/£40,000; fork produces 2 NEW; respective holding values immediately after fork £100,000/£1,000. If that is a just and reasonable valuation basis, NEW cost £40,000×1,000/101,000=**£396.04** and BTC **£39,603.96** (nearest pound: £396/£39,604). No disposal merely on the fork. This is an illustration, not HMRC's prescribed method. [Fork source](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22300).

**F - negligible value, claim in 2026/27.** 5,000 XYZ/£4,000; collapse, worthless since June 2025. If acquired while valuable, still owned, the whole pool qualifies and negligible value/ownership at the elected date are evidenced: nil proceeds give **£4,000 loss**. A June 2025 effective date falls in 2025/26 and is within the earliest possible **6 April 2024** limit for a 2026/27 claim. Collapse by itself does not establish eligibility. Check this point with one of our partner accountants. [TCGA s.24](https://www.legislation.gov.uk/ukpga/1992/12/section/24), [whole-pool rule](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22500).

**G - filed 2025/26.** 40 crypto disposals, £60,000 proceeds, £58,000 costs, £2,500 gains and £500 losses; no others. Reconcile £60,000−£58,000=£2,000=£2,500−£500. No CGT with unused £3,000 AEA, but proceeds exceed £50,000: SA108 needed. Boxes 13.1–13.5: **40; £60,000; £58,000; £2,500; £500**. Do not deduct AEA in those boxes. [2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf), [notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf).

### Historical cases retained with original inputs and years

**H1 - old v2 example 1, four dates.** Higher-rate taxpayer, 1 BTC/£20,000, sale £45,000, fee £75, no other gains. Gain £24,925, taxable £21,925. Ordinary completed spot sales with no straddling contract: **15 October 2024: £4,385** at 20%; **1 December 2024, 1 December 2025, 1 December 2026: £5,262 each** at 24%. Difference £877. No assumption that CARF begins in April 2026. [Historic rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances).

**H2 - old v2 example 2, 2024/25.** Higher-rate taxpayer: 1 BTC sold 15 October 2024, gain £10,000; 1 BTC sold 15 November 2024, gain £15,000; total £25,000; AEA £3,000. With no losses/other reliefs or straddling contracts, allocate AEA against 24% gains: £10,000×20% + (£15,000−£3,000)×24%=**£4,880**. Withdraw the old compulsory pro-rata £4,928 result. [TCGA s.1K(5)](https://www.legislation.gov.uk/ukpga/1992/12/section/1K).

**H3 - v1 example 1 / v2 example 3, 2025/26.** Bought 2 BTC at £20,000 each in January 2024, acquisition fee £50; sold 1 for £45,000 in August 2025, disposal fee £75, no other disposals. Pool £40,050; matched cost £20,025; net proceeds £44,925; gain **£24,900**, taxable **£21,900**, remaining pool 1 BTC/£20,025. “Basic-rate taxpayer” does not establish unused band. **£3,942** at 18% is usable only if the entire £21,900 fits the remaining band; otherwise compute 18%/24% from actual taxable income. The actual tax is held pending that input. Check this point with one of our partner accountants. [CGT rates](https://www.gov.uk/capital-gains-tax/rates).

**H4 - v1 example 2 / v2 example 4, 2025/26.** Pool 5 ETH/£10,000; sell 5 for £7,500 on 1 November 2025, rebuy 5 for £8,000 on 20 November, same capacity and UK residence. No same-day/competing transactions: loss **£500**, matched to £8,000 reacquisition. Original pool remains **5 ETH/£10,000**, not a new £8,000-plus-arithmetic pool. The counterfactual pool loss would be £2,500; £2,000 is the difference, not a separately deductible deferred loss. [Matching](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200).

**H5 - v1 example 3 (2025/26) and v2 example 5 (2026/27).** Preserve both: 0.5 ETH receipts worth £1,800, sales £2,200 in **March 2026** and **March 2027**, respectively; higher-rate taxpayer. CGT illustration with no other ETH/matches: gain **£400**, within unused AEA. The old **£720** income tax is only the £1,800×40% arithmetic if the entire receipt is taxable without allowance/expense relief and remains in that band; where C's added eligibility/election assumptions apply, income tax is **£320**. Original facts do not settle relief or other income: actual liability held. Check this point with one of our partner accountants. CARF follows calendar year: relevant **2026** transactions report by May **2027**, and relevant **2027** transactions by May **2028**; the whole 2026/27 tax year is not first reported in 2028. [Staking](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200), [allowance law](https://www.legislation.gov.uk/ukpga/2005/5/part/6A/chapter/1), [CARF deadline](https://www.legislation.gov.uk/uksi/2025/744/regulation/6/made).

### Checked examples

The original basic-rate block assumes sufficient unused band for its whole taxable gain; the higher-rate block assumes all taxable gains at 24%. Both assume the £3,000 AEA is available and no losses/other gains.

```oa-check
name: Crypto gain GBP 12,000, basic rate taxpayer (2026/27)
inputs:
  gain: 12000
  aea: 3000
steps:
  - taxable: gain - aea
  - tax: pct(taxable, 18)
expected:
  taxable: 9000
  tax: 1620
```

```oa-check
name: Crypto gain GBP 12,000, higher rate taxpayer (2026/27)
inputs:
  gain: 12000
  aea: 3000
steps:
  - taxable: gain - aea
  - tax: pct(taxable, 24)
expected:
  taxable: 9000
  tax: 2160
```


## When to refuse or refer

Unclear trading or token rights; specialist taxpayer/residence/FIG cases; separated spouses; income losses/NIC/payments on account; NFT royalties/VAT; uncertain DeFi rights, unascertainable consideration, collateral or impermanent loss; unsupported acquisition cost; and claims lacking ownership/value evidence: **do not use an unproved tax conclusion. Check this point with one of our partner accountants.**

Do not assist hiding or backdating transactions, omitting exchanges or inventing costs. The old spouse/ISA “workaround” is withdrawn; no crypto ISA eligibility or avoidance safe harbour is asserted. GAAR and anti-forestalling analysis is a specialist hold. Check this point with one of our partner accountants.

## Filing and payment

### SA108 for 2025/26

Fill the pages if chargeable disposal proceeds exceed **£50,000**, gains before losses exceed **£3,000**, an allowable loss/CGT claim or election is made, or earlier-year gains are taxable now. Other triggers include remitted earlier foreign gains, FIG/TRF claims and specified non-resident/split-year UK-land disposals: route those specialist cases rather than claiming exemption. Merely disposing of crypto is not an independent filing trigger. The 2025/26 form has crypto **boxes**, not a universal crypto tick box; do not carry their numbers forward to an unverified 2026/27 form. ([2026 notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf))

| Box | 2025/26 entry |
| --- | --- |
| 13.1 | Number of disposals, excluding another capacity such as trustee |
| 13.2 | Disposal proceeds |
| 13.3 | Allowable costs including purchase price |
| 13.4 | Gains before losses |
| 13.5 | Losses |
| 13.6 | Relevant claim/election code, e.g. NVC for negligible value; multiple codes MUL |
| 13.7 | Gains/losses already reported on real-time transaction returns |
| 13.8 | Tax on box 13.7 gains already paid |

Source for this table: [SA108 2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf) and [notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf). Send computations/valuations/claim forms; no AEA deduction in asset boxes. Explain estimates/valuations and real-time references in box 54 and mark box 53 where required. Income receipts go through the appropriate income pages, not these capital disposal boxes; use an accountant to settle the income classification/form mapping.

### Deadlines and submission

| Tax year | Notify if required to register | Ordinary paper filing | Ordinary online filing and balancing tax | Official source |
| --- | --- | --- | --- | --- |
| 2024/25 (historic; deadlines passed) | 5 October 2025 | 31 October 2025 | 31 January 2026 | [TMA ss.7–8](https://www.legislation.gov.uk/ukpga/1970/9/section/8); [s.59B](https://www.legislation.gov.uk/ukpga/1970/9/section/59B) |
| 2025/26 | 5 October 2026 | 31 October 2026 | 31 January 2027 | [HMRC deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines) |
| 2026/27 | 5 October 2027 | 31 October 2027 | 31 January 2028 | [TMA s.7](https://www.legislation.gov.uk/ukpga/1970/9/section/7), [s.8](https://www.legislation.gov.uk/ukpga/1970/9/section/8), [s.59B](https://www.legislation.gov.uk/ukpga/1970/9/section/59B) |

These are ordinary individual deadlines. Where notification was on time but HMRC issues the return notice after 31 October, s.59B(3) can also move the balancing-payment date to three months after that notice; do not apply the ordinary date blindly. Late 2025/26 registration after 5 October: HMRC's notice gives three months to file, but tax remains due 31 January 2027. To request eligible collection through a tax code, submit online by 30 December 2026; eligibility is separate. Payments on account are not automatic extra CGT instalments. Check this point with one of our partner accountants. ([HMRC deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines))

Use [Self Assessment](https://www.gov.uk/log-in-file-self-assessment-tax-return), add the applicable capital-gains supplement in compatible software or use the paper form, attach the computation, reconcile the liability, submit and save the acknowledgement; use [HMRC payment instructions](https://www.gov.uk/pay-self-assessment-tax-bill) and retain payment confirmation. Check a missing acknowledgement/payment rather than assuming completion.

A UK resident can use the real-time CGT service for eligible own gains: report by **31 December in the next tax year**, pay by **31 January**. Thus 2025/26→31 December 2026/31 January 2027 and 2026/27→31 December 2027/31 January 2028. If already registered for Self Assessment, include the sale there too. The service cannot report for a client/trust/estate, UK residential property gains, overseas-property foreign tax credit relief or life-policy chargeable-event gains. ([HMRC real-time service](https://www.gov.uk/report-and-pay-your-capital-gains-tax/print))

### Earlier years, penalties and records

Use HMRC's [crypto disclosure service](https://www.gov.uk/guidance/tell-hmrc-about-unpaid-tax-on-cryptoassets) for eligible earlier unpaid tax; current and previous tax years go on Self Assessment. The page distinguishes four years with reasonable care, up to six if careless, up to twenty if deliberate. Those are not universal periods regardless of the facts. **Actual look-back, interest and penalty computations, including offshore issues and the former generic “100%” figure, are held. Check this point with one of our partner accountants.** Do not delay correcting a return until CARF reports arrive.

Keep token type, dates, quantities, sterling values, transaction fees, wallet/exchange evidence, bank statements, receipt income and pooled costs before/after disposals. HMRC's ordinary non-business guidance says at least **22 months after the tax year ends** for an on-time return or **15 months after sending** a late return; keep acquisition/pool evidence needed for assets still held and unresolved claims/enquiries. Business retention rules are longer and require separate application. ([Receiving crypto](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets), [HMRC retention](https://www.gov.uk/keeping-your-pay-tax-records/how-long-to-keep-your-records))

## Completion checklist

- [ ] Scope, ownership, capacity and trade/income classification settled; held conclusions not used.
- [ ] All activity reconstructed in sterling, including fees, swaps and subsequent matching purchases.
- [ ] Pool, fork, reward, loss and allowance conditions applied; no guessed basis or double expense.
- [ ] Cases use their original year and inputs; conditional tax figures remain conditional.
- [ ] Correct year's form and all reporting triggers checked; computations attached, filing and payment confirmations saved.
- [ ] CARF calendar years and correct user details reconciled; earlier unpaid tax addressed.

## Sources

Read 2026-11-27 unless described as reused below. Each entry identifies the passage read, not merely a successful URL response. Operative legislation takes priority over summaries.

- [TCGA ss.1A,1H–1K](https://www.legislation.gov.uk/ukpga/1992/12/section/1K): scope, ordinary rates, AEA and loss ordering; reuse of the same-day UK capital-gains proof, applicability checked for these individual crypto cases. (read 2026-11-27).
- [HMRC CGT rates/allowances](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances), [calculation](https://www.gov.uk/capital-gains-tax/rates), [2024/25 adjustment](https://www.gov.uk/guidance/work-out-your-capital-gains-tax-adjustment-for-the-2024-to-2025-tax-year): current/historical rate matrix, £37,700 band and adjustment; same-day proven passages reused. (read 2026-11-27).
- [ITA ss.10,35](https://www.legislation.gov.uk/ukpga/2007/3/section/10), [FA 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2), [HMRC income rates](https://www.gov.uk/income-tax-rates): taxable bands, allowance/taper and 2026/27 main rates. (read 2026-11-27).
- [TCGA ss.17,22,24,37,38,43,48,52](https://www.legislation.gov.uk/ukpga/1992/12/section/17): XML operative text read for market value, capital sums, negligible value, income overlap, cost, derived assets and deferred consideration/apportionment. (read 2026-11-27).
- [TCGA ss.18,58](https://www.legislation.gov.uk/ukpga/1992/12/section/58): connected loss and spouse transfer conditions; same-day capital-gains proof reused, not a new separation opinion. (read 2026-11-27).
- [TCGA ss.104–106A](https://www.legislation.gov.uk/ukpga/1992/12/section/104): pooling scope read directly; same-day proven identification/residence/later-acquisition passages reused. (read 2026-11-27).
- [TCGA s.16](https://www.legislation.gov.uk/ukpga/1992/12/section/16), [TMA s.43](https://www.legislation.gov.uk/ukpga/1970/9/section/43), [HMRC losses](https://www.gov.uk/capital-gains-tax/losses): notification, ordinary time limit and ordering; same-day proof reused. (read 2026-11-27).
- [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100), [22150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22150), [22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200), [22280](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22280): disposal exceptions, costs, matching and fee-token example. (read 2026-11-27).
- [CRYPTO22300](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22300), [22350](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22350), [21250](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21250): fork apportionment and airdrop conditions/pooling. (read 2026-11-27).
- [CRYPTO22400](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22400), [22450](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22450), [22500](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22500): lost keys, theft/fraud and whole-pool negligible value. (read 2026-11-27).
- [CRYPTO21100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21100), [21150](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21150), [21200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200), [receiving tokens](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets): employment, mining, staking, registration instructions and records. (read 2026-11-27).
- [ITTOIA s.687](https://www.legislation.gov.uk/ukpga/2005/5/section/687), [Part 6A Ch.1](https://www.legislation.gov.uk/ukpga/2005/5/part/6A/chapter/1): income charge, allowance aggregation, full/partial relief, elections and exclusions; operative ss.783A,AB,AC,AD,AE,AG,AH,AJ,AK,AL,AM,AN–AQ read. (read 2026-11-27).
- [CRYPTO61110](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61110), [61212](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61212), [61214](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61214), [61620](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61620), [61650](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61650): income/capital factors, ownership, ascertainable debt and LP entry/exit. (read 2026-11-27).
- [SI 2025/744](https://www.legislation.gov.uk/uksi/2025/744/made), [FA 2026 s.275](https://www.legislation.gov.uk/ukpga/2026/11/section/275): operative commencement, provider definition, duties, domestic extension, report/notification dates, self-certification and reasonable excuse. (read 2026-11-27).
- [HMRC CARF reporting](https://www.gov.uk/guidance/reporting-cryptoasset-user-and-transaction-data), [user details](https://www.gov.uk/guidance/information-youll-need-to-give-to-uk-cryptoasset-service-providers): first-year window correction dated 2 November 2026 and identity/TIN exception. (read 2026-11-27).
- [SA108 2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf), [2026 notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf): same-day proven 2025/26 trigger, crypto-box, computation, estimates and NVC passages reused; no later form represented as read. (read 2026-11-27).
- [HMRC deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines), [TMA s.7](https://www.legislation.gov.uk/ukpga/1970/9/section/7), [s.8](https://www.legislation.gov.uk/ukpga/1970/9/section/8), [s.59B](https://www.legislation.gov.uk/ukpga/1970/9/section/59B): current deadlines read; year-relative statutory deadlines read for historic/following-year dates. (read 2026-11-27).
- [HMRC real-time CGT](https://www.gov.uk/report-and-pay-your-capital-gains-tax/print): same-day proven service eligibility, exclusions and dates reused. (read 2026-11-27).
- [HMRC crypto disclosure](https://www.gov.uk/guidance/tell-hmrc-about-unpaid-tax-on-cryptoassets), [record retention](https://www.gov.uk/keeping-your-pay-tax-records/how-long-to-keep-your-records): return/disclosure boundary, behaviour branches and non-business retention passages. (read 2026-11-27).

Not yet confirmed: no usable conclusion is supplied for the explicit specialist holds above, historical H3/H5 actual tax without missing income/relief inputs, no-income airdrop basis, unascertainable DeFi rights/elections, proposed DeFi relief, or the 2026/27 SA108 fields. Check this point with one of our partner accountants.
