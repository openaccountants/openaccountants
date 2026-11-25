---
name: au-crypto-tax
description: Use this skill whenever asked about Australian cryptocurrency taxation. Trigger on phrases like "crypto tax Australia", "Bitcoin CGT", "ATO crypto", "crypto capital gains", "personal use asset crypto", "staking income", "airdrop tax", "DeFi tax Australia", "crypto cost base", "crypto trading tax", "Coinbase tax", "Swyftx tax", "CoinSpot tax", "NFT tax Australia", or any question about how cryptocurrency is taxed by the ATO. This skill covers CGT treatment of crypto assets, the personal use asset exemption, trading vs investing distinction, staking and airdrop income, DeFi events, record-keeping requirements, and exchange-specific transaction patterns. ALWAYS read this skill before touching any Australian crypto tax work.
version: "1.4"
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-22
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
---

# AU Crypto Tax

## Australia Crypto Tax -- CGT & Income Skill v1.4

## Section 1 -- Quick Reference

**Quick Reference**

**Quick Reference**

| Field | Detail |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax | Income Tax -- Cryptocurrency / Digital Assets |
| Currency | AUD (all gains/income must be reported in AUD) |
| Tax year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Primary legislation | Income Tax Assessment Act 1997, Div 104 (CGT events), Div 118 (exemptions) |
| Supporting guidance | ATO crypto asset investments guidance; TD 2014/26 (Bitcoin as a CGT asset); TR 2026/D1 (airdrops, draft); TD 2026/D2 (wrapping, draft); ATO DeFi and wrapping guidance |
| Tax authority | Australian Taxation Office (ATO) |
| Filing portal | myTax / tax agent lodgement |
| Filing deadline | Generally 31 October for self-lodgement, or the next business day when it falls on a weekend. Agent deadlines vary. |
| Skill version | 1.4 |

### Core Principle

Bitcoin and similar investment crypto assets are generally CGT assets. Identify the property or rights represented by stablecoins, NFTs and DeFi tokens. Ordinary income and trading stock rules can apply in business and other income-producing activities. A mere transfer with unchanged beneficial ownership does not trigger CGT event A1.

### Individual Marginal Tax Rates (2026-27)

**Individual Marginal Tax Rates (2026-27)**

| Taxable Income (AUD) | Rate |
| --- | --- |
| 0 -- 18,200 | 0% |
| 18,201 -- 45,000 | 15% |
| 45,001 -- 135,000 | 30% |
| 135,001 -- 190,000 | 37% |
| 190,001+ | 45% |

- **Rate scale by year** — The second resident bracket is 15 cents from 1 July 2026 and was 16 cents in 2024-25 and 2025-26. The ordinary Medicare levy rate is 2%, subject to reductions and exemptions. A full-year foreign resident generally has no tax-free threshold. Check taxable Australian property and discount apportionment for foreign and temporary residence. See section 2.3 for the changes from 1 July 2027. _([ATO, Tax rates: Australian resident](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents))_

### Key Thresholds

**Key Thresholds**

| Item | Value |
| --- | --- |
| Personal use asset exemption | First element of cost base is $10,000 or less and the asset qualifies as a personal use asset ([ATO crypto personal use asset](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-asset-as-a-personal-use-asset)) |
| CGT discount (held 12+ months) | 50% for individuals and trusts |
| CGT discount -- companies | Not available |
| Capital loss carry forward | Indefinite (offset against future capital gains only) |

### Evidence required

| Ambiguity | Evidence required before finalising |
| --- | --- |
| Unknown acquisition date | Establish the acquisition and event dates before applying the discount |
| Unknown cost base | Reconstruct the acquisition and consider any applicable market-value substitution |
| Unknown whether personal use or investment | Establish how the taxpayer mainly used or kept the asset |
| Unknown whether trading or investing | Document purpose, commercial activity and the nature of receipts |
| DeFi event with unknown character | Establish the legal and beneficial rights before and after the transaction |

## Section 2 -- Classification Rules

### 2.1 CGT Events (Disposals)

**CGT Events (Disposals)**

| Event | CGT Triggered? |
| --- | --- |
| Sell crypto for AUD (or fiat) | Yes |
| Trade one crypto for another (e.g., BTC → ETH) | Yes -- disposal of BTC at market value |
| Use crypto to purchase goods/services | Yes -- disposal at market value |
| Gift crypto to another person | Yes -- market value at time of gift |
| Send crypto to an exchange for sale | Check whether beneficial ownership changes under the custody terms |
| Transfer between own wallets | No -- same beneficial ownership |
| Lost/stolen crypto (no private key) | Possible CGT event -- must demonstrate irrecoverability |

### 2.2 Cost Base Calculation

**Cost Base Calculation**

| Element | Included in Cost Base |
| --- | --- |
| Purchase price in AUD | Yes |
| Exchange fees / commission on acquisition | Yes |
| Gas fees on acquisition transaction | Yes |
| Exchange fees / commission on disposal | Eligible incidental costs go into the cost base or reduced cost base of the disposed asset. Use gross capital proceeds. |
| Wallet transfer fees (own wallets) | Check whether the fee falls within a statutory cost base element. Consider the disposal of any crypto used to pay it. |
| Subscription to portfolio tracking tool | Check whether the cost qualifies under the statutory rules and whether it is deductible. |

- Identify the units disposed of and keep records that support any parcel allocation.
- Match eligible fees to the relevant acquisition or disposal and avoid counting any fee twice. Where an acquisition record is missing, obtain exchange exports, wallet history and bank transfers to reconstruct the cost and consider statutory valuation rules. _([ATO, Transactions: acquiring and disposing of crypto assets](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets))_

### 2.3 50% CGT Discount

- A qualifying discount gain generally requires acquisition at least 12 months before the CGT event. Exclude both the acquisition and event days from the count.
- For eligible gains, the usual discount is 50% for individuals and trusts and 33⅓% for complying superannuation entities. Companies have no discount for crypto investments.
- Foreign or temporary residence can reduce the individual discount. For a foreign resident, first check whether the asset is taxable Australian property or another inclusion rule applies.
- For crypto assets disposed of from 1 July 2027, apply the enacted transition rules to separate pre-reform gains from later gains. Eligible pre-reform gains can still qualify for the discount. Check the 12-month requirement for cost base indexation and the 30% minimum income tax provisions for eligible later gains, including the statutory exceptions. See `au-capital-gains.md`. _([Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/asmade/text))_

### 2.4 Personal Use Asset Exemption

**Personal Use Asset Exemption Conditions**

- The taxpayer must use or keep the asset mainly for personal use or enjoyment, determined at the CGT event. Prompt spending on personal goods supports that conclusion. Holding period and how the asset was stored are evidence of its purpose.
- Disregard the gain if the first element of the cost base is $10,000 or less. Check the rules for sets of personal use assets. Spending an asset kept mainly as an investment on personal goods does not satisfy the test. Disregard a capital loss on a personal use asset. _([ATO, Crypto asset as a personal use asset](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-asset-as-a-personal-use-asset))_

### 2.5 Trading vs Investing

**Trading vs Investing**

| Factor | Investor (CGT) | Trader (Business Income) |
| --- | --- | --- |
| Volume of transactions | Low to moderate | High frequency, systematic |
| Holding period | Weeks/months/years | Minutes/hours/days |
| Purpose | Long-term growth | Profit from short-term price movements |
| Organisation | Casual / part-time | Business-like, significant time commitment |
| Capital employed | Personal savings | Significant working capital |
| Tax treatment | Capital gains (50% discount available) | Ordinary income (no CGT discount, no capital loss restrictions) |
| Losses | Capital losses offset capital gains | Check the non-commercial loss rules before offsetting an individual's business loss against other income |

- **Frequency alone does not decide** — Establish whether the taxpayer invests, carries on a trading or mining business, is paid for services, or undertook an isolated profit-making transaction. An isolated commercial transaction can produce ordinary income without a business, and business trading stock and revenue gains use different calculations from capital investments.  _([TR 92/3](https://www.ato.gov.au/law/view/document?docid=TXR/TR923/NAT/ATO/00001))_

### 2.6 Staking Rewards

**Staking Rewards**

| Treatment | Detail |
| --- | --- |
| Classification | Ordinary income at market value when received |
| Timing | Assessable in the income year the reward is received/controlled |
| Cost base for future CGT | Market value at date of receipt becomes cost base |
| Holding period for CGT discount | Starts from date of receipt |

### 2.7 Airdrops

**Airdrops**

| Type | Treatment |
| --- | --- |
| Airdrop with or without a claim transaction | Determine whether the receipt is income and when it was derived. A claim transaction may help establish when the taxpayer obtained the token. |
| Airdrop with no quoted price | Establish whether the asset has market value. The absence of a price feed does not establish nil value. |
| Subsequent disposal | Apply CGT for an investment holding and determine the cost base under the ordinary rules, including applicable market-value substitution |

- **Airdrops are not automatically ordinary income** — Establish whether the airdrop was received in a crypto trading business, for goods or services, through another income-producing activity, or as a hobby receipt, gift or windfall; current ATO guidance distinguishes these. Where it is not ordinary income the token is still a CGT asset, so record its acquisition and support its value; an unavailable price feed is not evidence that a token had no value.  _([ATO, Staking rewards and airdrops](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops))_
- **TR 2026/D1 is a draft** — TR 2026/D1 sets out the Commissioner's preliminary view on airdrops, with stated scope exclusions and proposed application arrangements. Do not cite it as a final ruling; record which view was applied.  _([TR 2026/D1](https://www.ato.gov.au/law/view/document?docid=DTR/TR2026D1/NAT/ATO/00001))_

### 2.8 DeFi Specific Events

**DeFi Specific Events**

| DeFi Action | Tax Treatment |
| --- | --- |
| Wrapping or unwrapping | Test for a change or ending of rights. The draft determination proposes C2 for specified smart-contract arrangements. |
| Providing or removing liquidity | Identify the assets and rights transferred, ended or acquired. If there is a disposal, value the consideration and identify eligible incidental costs. |
| Yield farming rewards | Ordinary income at market value when received |
| Borrowing against crypto | Check if the borrower retains beneficial ownership when posting collateral. Identify any disposal on liquidation. |
| Bridge transactions (cross-chain) | Examine the bridge mechanics and determine whether rights change or end |
| Token migration or chain split | Check for a disposal or ending of rights on migration. Apply the separate ATO chain split rules to qualifying investment assets. |

- **Read the mechanics before choosing the event** — Depositing into a liquidity pool, receiving a replacement token, lending, borrowing, wrapping or unwrapping can change or end rights even where the economic exposure looks unchanged. Record the assets and rights held before and after the transaction; the CGT event can be A1, C2, E2 or H2 depending on the arrangement.  _([ATO, Decentralised finance and wrapping crypto](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto))_
- **TD 2026/D2 on wrapping and unwrapping** — TD 2026/D2 proposes CGT event C2 treatment for specified smart-contract wrapping and unwrapping arrangements. It is a draft with exclusions, so do not apply it to every bridge or custodial transfer; keep a record of the arrangement and the interpretation used.  _([TD 2026/D2](https://www.ato.gov.au/law/view/document?docid=DXT/TD2026D2/NAT/ATO/00001))_

### 2.9 NFTs

Buying and selling an investment NFT generally involves acquiring and disposing of a CGT asset. Creation and sale can generate ordinary income in a business or in an isolated commercial profit-making transaction. Identify the rights the NFT represents.

- **What the NFT represents decides the treatment** — Business receipts, investment disposals, personal use assets and collectables each have their own rules. Neither the label NFT nor an exchange's tax category settles the result.

## Section 3 -- Transaction Pattern Library

### 3.1 Exchange Patterns -- Coinbase

**Exchange Patterns -- Coinbase**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BUY [CRYPTO] | Acquisition | Cost base = AUD amount + fee |
| SELL [CRYPTO] | Disposal (CGT event) | Use gross sale consideration and record eligible fees separately |
| CONVERT [CRYPTO A] TO [CRYPTO B] | Disposal of A + acquisition of B | Market value at time of convert |
| COINBASE EARN / LEARN REWARD | Ordinary income | Market value at receipt |
| STAKING REWARD | Ordinary income | Market value at receipt |
| SEND / RECEIVE (own wallet) | Not a CGT event | Transfer -- no gain/loss |
| WITHDRAWAL TO BANK | Not a CGT event | Fiat transfer (already sold) |

### 3.2 Exchange Patterns -- Swyftx

**Exchange Patterns -- Swyftx**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BUY ORDER | Acquisition | Use the executed price plus eligible separately charged fees. The price already includes any embedded spread. |
| SELL ORDER | Disposal (CGT event) | Use gross sale consideration and record eligible fees separately |
| SWAP [A] FOR [B] | Disposal of A + acquisition of B | Market value at execution |
| STAKING REWARD | Ordinary income | Market value at receipt |
| DEPOSIT AUD | Not taxable | Fiat deposit |
| WITHDRAWAL AUD | Not taxable | Fiat withdrawal |

### 3.3 Exchange Patterns -- CoinSpot

**Exchange Patterns -- CoinSpot**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MARKET BUY | Acquisition | Use the executed price and the actual eligible acquisition fee |
| MARKET SELL | Disposal (CGT event) | Use gross sale consideration and record the eligible disposal fee separately |
| SWAP | Disposal of old asset and acquisition of new asset | The acquisition itself is not a second CGT event for the taxpayer |
| AFFILIATE PAYMENT | Ordinary income |  |
| REFERRAL REWARD | Ordinary income | Market value at receipt |
| AIRDROP | Apply section 2.7 | Market value alone does not determine whether the receipt is income |
| SEND TO EXTERNAL WALLET | Check beneficial ownership | An own-wallet transfer does not dispose of the transferred asset |

### 3.4 On-Chain Patterns

**On-Chain Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UNISWAP / SUSHISWAP SWAP | Disposal of old asset and acquisition of new asset | Check separately for any crypto disposed of to pay a fee |
| LP DEPOSIT (ADD LIQUIDITY) | Check the transfer and acquisition of rights | See section 2.8 |
| LP WITHDRAWAL (REMOVE LIQUIDITY) | Check the transfer or ending of rights | See section 2.8 |
| CLAIM REWARDS | If ordinary income, value it when derived | Check when the taxpayer received or had the reward applied for their benefit |
| BRIDGE [TOKEN] TO [CHAIN] | Check whether rights change or end | See section 2.8 |
| MINT NFT | Acquisition | Cost base = mint price + gas |
| APPROVE / REVOKE (no transfer) | Check for any disposal of fee tokens | Include gas in a cost base only if it qualifies under the statutory rules |

## Section 4 -- Computation Method

### Step 1: Identify All CGT Events

- **Identify All CGT Events** — List every disposal in the financial year (sells, swaps, spends, gifts, DeFi events).

### Step 2: Calculate Gain/Loss per Event

- Subtract the cost base from capital proceeds to calculate a gain if proceeds exceed cost base. Subtract capital proceeds from the reduced cost base to calculate a loss if proceeds are below reduced cost base.

### Step 3: Offset Capital Losses

- Reduce capital gains by this year's eligible capital losses, then by unapplied net capital losses from earlier years.

### Step 4: Apply the CGT Discount

- Reduce remaining eligible gains by the applicable discount. Add the remaining amounts after any other applicable concessions to calculate the net capital gain.

### Step 5: Add Ordinary Income

- Include taxable rewards and airdrops in the relevant ordinary income calculation. Separate business income and trading stock adjustments from non-business receipts.

### Step 6: Report on Tax Return

- Use the relevant year's return instructions for capital gains, taxable non-business rewards and business income or loss. Capital gains and other income have separate labels.

## Section 5 -- Record-Keeping Requirements

The ATO requires the following records for each transaction:

**Record-Keeping Requirements**

| Record | Required |
| --- | --- |
| Date of acquisition | Yes |
| Date of disposal | Yes |
| Amount in AUD at time of transaction | Yes |
| Purpose of the transaction | Yes |
| Exchange/wallet records | Yes |
| Counterparty details (if applicable) | Yes |
| Exchange rate used (AUD conversion) | Yes |
| Agent/exchange fees | Yes |

- Keep CGT records until 5 years after it becomes certain that no further CGT event can arise for which they could be relevant. Keep records supporting carried-forward losses and check any longer applicable retention period. _([Income Tax Assessment Act 1997, section 121-25](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html))_
- **Reconcile before calculating** — Collect exchange exports, wallet addresses, transaction identifiers, timestamps, token quantities, fees and Australian dollar valuations. Match transfers between the taxpayer's own wallets so they are not recorded as sales, and check that beneficial ownership really stayed unchanged for exchange, lending and custody arrangements. Reconcile opening holdings plus receipts less disposals and fees to closing holdings, and investigate any gap.  _([ATO, Keeping crypto records](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records))_

## Section 6 -- Edge Cases

### 6.1 Hard Forks

- For an investment holding, an additional token from a qualifying chain split generally has a zero initial cost base. Receipt is not income and a CGT event normally occurs on disposal. Identify which chain continued the original asset. Use trading stock rules where the assets are held as trading stock. _([ATO, Chain splits](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/chain-splits))_

### 6.2 Lost or Stolen Crypto

- **Lost or Stolen Crypto** — A capital loss may be claimed if the crypto is demonstrably lost (e.g., lost private keys with no possibility of recovery, scam/hack with no recovery). The taxpayer must demonstrate the loss is permanent. ATO may require evidence.
- **Exchange collapse and suspended withdrawals** — An exchange entering administration, or suspending withdrawals, needs evidence of what asset or enforceable right remains and whether a CGT event has happened. Do not write off an account because withdrawals are suspended. Keep unresolved transactions outside the final calculation until the facts and treatment are documented, then reconcile income, gains, losses and holdings to the workpapers.

### 6.3 Mining

**Mining**

| Scenario | Treatment |
| --- | --- |
| Hobby miner | Check whether there is a business or other income-producing arrangement. If held on capital account, establish any eligible cost base and disposal proceeds. |
| Business miner | Apply ordinary income and trading stock rules according to the business arrangements. Include any taxable fees for supplying mining services. Treat tokens produced and held for sale or exchange as trading stock. |

### 6.4 Crypto Received as Payment for Services

- Include the AUD value of taxable payment for services when derived, applying the relevant employment, personal services income or business rules. Establish the treatment and cost of the crypto received for any later disposal.

### 6.5 Margin Trading / Futures

- Identify the product and the purpose of the transaction. A commercial profit-making derivative transaction can be on revenue account even when isolated. Check the rules for the particular instrument before classifying a gain or loss. _([ATO, TR 2005/15](https://www.ato.gov.au/law/view/document?DocID=TXR%2FTR200515%2FNAT%2FATO%2F00001))_

## Section 7 -- Prohibitions

- Confirm the personal use test and discount eligibility before applying a concession. Apply eligible capital losses against capital gains before discounting. Include taxable swap disposals, staking and airdrop income. Resolve uncertain DeFi and other transactions before finalising, and label provisional figures as estimates.

## Worked examples

**Example 1. Long-term investment disposal with current-year capital loss.** An investor sells crypto held more than 12 months for AUD 15,000 (cost base AUD 8,000 including brokerage), and has a current-year capital loss of AUD 1,000 from another disposal before 1 July 2027. Apply the loss before the 50% discount: (15,000 - 8,000 - 1,000) x 50% = AUD 3,000.

```oa-check
name: AU crypto long-term CGT disposal with capital loss before 50% discount
inputs:
  proceeds: 15000
  cost_base: 8000
  capital_loss: 1000
steps:
  - gross_gain: proceeds - cost_base
  - after_losses: gross_gain - capital_loss
  - net_capital_gain: pct(after_losses, 50)
expected:
  gross_gain: 7000
  after_losses: 6000
  net_capital_gain: 3000
```

**Example 2. Crypto-to-crypto swap within 12 months.** Swapping one token for another is a CGT disposal at market value in AUD. Proceeds AUD 12,000, acquisition cost AUD 9,200 plus AUD 50 acquisition fee and AUD 50 disposal fee gives cost base AUD 9,300 and a short-term net capital gain of AUD 2,700 (no discount).

```oa-check
name: AU crypto short-term swap with brokerage fees in cost base
inputs:
  swap_market_value: 12000
  purchase_price: 9200
  buy_fee: 50
  sell_fee: 50
steps:
  - cost_base: purchase_price + buy_fee + sell_fee
  - net_capital_gain: swap_market_value - cost_base
expected:
  cost_base: 9300
  net_capital_gain: 2700
```

## Sources

- [ATO, Tax rates: Australian resident](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents) (read 2026-11-22)
- [ATO, Transactions: acquiring and disposing of crypto assets](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets) (read 2026-11-22)
- [ATO, Crypto asset as a personal use asset](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-asset-as-a-personal-use-asset) (read 2026-11-22)
- [ATO, Staking rewards and airdrops](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops) (read 2026-11-22)
- [ATO, Decentralised finance and wrapping crypto](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto) (read 2026-11-22)
- [ATO, Keeping crypto records](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records) (read 2026-11-22)
- [ATO, Chain splits](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/chain-splits) (read 2026-11-22)
- [ITAA 1997, section 121-25](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) and [Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/asmade/text) (read 2026-11-22)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
