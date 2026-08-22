---
name: au-crypto-tax
description: Use this skill whenever asked about Australian cryptocurrency taxation. Trigger on phrases like "crypto tax Australia", "Bitcoin CGT", "ATO crypto", "crypto capital gains", "personal use asset crypto", "staking income", "airdrop tax", "DeFi tax Australia", "crypto cost base", "crypto trading tax", "Coinbase tax", "Swyftx tax", "CoinSpot tax", "NFT tax Australia", or any question about how cryptocurrency is taxed by the ATO. This skill covers CGT treatment of crypto assets, the personal use asset exemption, trading vs investing distinction, staking and airdrop income, DeFi events, record-keeping requirements, and exchange-specific transaction patterns. ALWAYS read this skill before touching any Australian crypto tax work.
version: "1.1"
jurisdiction: AU
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Crypto Tax

## Australia Crypto Tax -- CGT & Income Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax | Income Tax -- Cryptocurrency / Digital Assets |
| Currency | AUD (all gains/income must be reported in AUD) |
| Tax year | 1 July 2024 -- 30 June 2025 |
| Primary legislation | Income Tax Assessment Act 1997, Div 104 (CGT events), Div 118 (exemptions) |
| Supporting guidance | ATO Cryptocurrency guidance (updated 2024); TD 2014/26 (Bitcoin as CGT asset); PCG 2023/1 (DeFi) |
| Tax authority | Australian Taxation Office (ATO) |
| Filing portal | myTax / tax agent lodgement |
| Filing deadline | 31 October (self-lodgement); agent-managed deadlines vary |
| Skill version | 1.0 |

### Core Principle

The ATO treats cryptocurrency (including Bitcoin, Ethereum, stablecoins, NFTs, and DeFi tokens) as a **CGT asset**, not as foreign currency. Each disposal triggers a CGT event.

### Individual Marginal Tax Rates (2024-25)

**Individual Marginal Tax Rates (2024-25)**

| Taxable Income (AUD) | Rate |
| --- | --- |
| 0 -- 18,200 | 0% |
| 18,201 -- 45,000 | 16% |
| 45,001 -- 135,000 | 30% |
| 135,001 -- 190,000 | 37% |
| 190,001+ | 45% |

### Key Thresholds

**Key Thresholds**

| Item | Value |
| --- | --- |
| Personal use asset exemption | Acquisition cost < $10,000 |
| CGT discount (held 12+ months) | 50% for individuals and trusts |
| CGT discount -- companies | Not available |
| Capital loss carry forward | Indefinite (offset against future capital gains only) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown acquisition date | No 50% discount available |
| Unknown cost base | $0 (maximum gain) -- obtain records |
| Unknown whether personal use or investment | Treat as investment (CGT applies) |
| Unknown whether trading or investing | Treat as investor (CGT, not ordinary income) |
| DeFi event -- unknown character | Treat as disposal (CGT event) |

## Section 2 -- Classification Rules

### 2.1 CGT Events (Disposals)

**CGT Events (Disposals)**

| Event | CGT Triggered? |
| --- | --- |
| Sell crypto for AUD (or fiat) | Yes |
| Trade one crypto for another (e.g., BTC → ETH) | Yes -- disposal of BTC at market value |
| Use crypto to purchase goods/services | Yes -- disposal at market value |
| Gift crypto to another person | Yes -- market value at time of gift |
| Send crypto to an exchange for sale | No (transfer to own wallet is not disposal) |
| Transfer between own wallets | No -- same beneficial ownership |
| Lost/stolen crypto (no private key) | Possible CGT event -- must demonstrate irrecoverability |

A CGT event occurs when you:

### 2.2 Cost Base Calculation

**Cost Base Calculation**

| Element | Included in Cost Base |
| --- | --- |
| Purchase price in AUD | Yes |
| Exchange fees / commission on acquisition | Yes |
| Gas fees on acquisition transaction | Yes |
| Exchange fees / commission on disposal | Reduces capital proceeds (or included in cost base of new asset in swap) |
| Wallet transfer fees (own wallets) | Included in cost base of the asset |
| Subscription to portfolio tracking tool | Included (third element -- ownership costs) |

- **Method for identical assets** — FIFO, LIFO, or specific identification -- must be consistent and documented. ATO does not mandate a method but requires consistency.

### 2.3 50% CGT Discount

Available if:
- The asset was held for at least 12 months (acquisition to disposal)
- The taxpayer is an individual or trust (not a company or super fund at 1/3 discount)
- The taxpayer is an Australian tax resident at the time of the CGT event

### 2.4 Personal Use Asset Exemption

**Personal Use Asset Exemption Conditions**

| Condition | All Must Be Met |
| --- | --- |
| Acquired for personal use (e.g., to purchase goods) | Yes |
| Acquisition cost < $10,000 | Yes |
| Used within a short time of acquisition | Yes |
| NOT held as an investment | Yes |
| NOT held for exchange/trading purposes | Yes |

- **Exemption failure conditions** — If ANY acquisition cost ≥ $10,000, the personal use asset exemption does NOT apply. If crypto is kept on an exchange or held for extended periods, the ATO considers it an investment -- NOT personal use.

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
| Losses | Capital losses only | Business losses (offset all income) |

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
| Airdrop with no action required | Ordinary income at market value on receipt (if established market value exists) |
| Airdrop requiring action (e.g., claim transaction) | Ordinary income when claimed |
| Airdrop of worthless/no-market token | $0 income; cost base = $0 |
| Subsequent disposal | CGT event -- cost base is value at receipt |

### 2.8 DeFi Specific Events

**DeFi Specific Events**

| DeFi Action | Tax Treatment |
| --- | --- |
| Wrapping (e.g., ETH → WETH) | ATO view: likely a disposal (CGT event). Conservative: treat as disposal at market value |
| Unwrapping (WETH → ETH) | Disposal of WETH, acquisition of ETH |
| Providing liquidity (LP tokens) | Disposal of deposited tokens; acquisition of LP token at combined market value |
| Removing liquidity | Disposal of LP token; acquisition of underlying tokens |
| Yield farming rewards | Ordinary income at market value when received |
| Borrowing against crypto (collateral) | Not a disposal (no change of beneficial ownership). BUT if liquidated -- CGT event |
| Bridge transactions (cross-chain) | Conservative: treat as disposal + acquisition |
| Token migration/hard fork | New token acquired at $0 cost base; not assessable until disposed |

### 2.9 NFTs

Treated identically to other crypto assets. Purchase = acquisition (CGT asset). Sale = disposal (CGT event). Creating and selling an NFT = ordinary income if in the business of creating them, otherwise CGT.

## Section 3 -- Transaction Pattern Library

### 3.1 Exchange Patterns -- Coinbase

**Exchange Patterns -- Coinbase**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BUY [CRYPTO] | Acquisition | Cost base = AUD amount + fee |
| SELL [CRYPTO] | Disposal (CGT event) | Proceeds = AUD received |
| CONVERT [CRYPTO A] TO [CRYPTO B] | Disposal of A + acquisition of B | Market value at time of convert |
| COINBASE EARN / LEARN REWARD | Ordinary income | Market value at receipt |
| STAKING REWARD | Ordinary income | Market value at receipt |
| SEND / RECEIVE (own wallet) | Not a CGT event | Transfer -- no gain/loss |
| WITHDRAWAL TO BANK | Not a CGT event | Fiat transfer (already sold) |

### 3.2 Exchange Patterns -- Swyftx

**Exchange Patterns -- Swyftx**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BUY ORDER | Acquisition | Cost base = AUD equivalent + spread/fee |
| SELL ORDER | Disposal (CGT event) | Proceeds = AUD credited |
| SWAP [A] FOR [B] | Disposal of A + acquisition of B | Market value at execution |
| STAKING REWARD | Ordinary income | Market value at receipt |
| DEPOSIT AUD | Not taxable | Fiat deposit |
| WITHDRAWAL AUD | Not taxable | Fiat withdrawal |

### 3.3 Exchange Patterns -- CoinSpot

**Exchange Patterns -- CoinSpot**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MARKET BUY | Acquisition | Cost = AUD paid + 0.1% fee |
| MARKET SELL | Disposal (CGT event) | Proceeds = AUD received (net of 0.1% fee) |
| SWAP | Disposal + acquisition | Two CGT events |
| AFFILIATE PAYMENT | Ordinary income |  |
| REFERRAL REWARD | Ordinary income | Market value at receipt |
| AIRDROP | Ordinary income (if value > $0) |  |
| SEND TO EXTERNAL WALLET | Not a CGT event | Own-wallet transfer |

### 3.4 On-Chain Patterns

**On-Chain Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UNISWAP / SUSHISWAP SWAP | Disposal + acquisition | Two CGT events at market value |
| LP DEPOSIT (ADD LIQUIDITY) | Disposal of tokens, acquisition of LP token |  |
| LP WITHDRAWAL (REMOVE LIQUIDITY) | Disposal of LP token, acquisition of tokens |  |
| CLAIM REWARDS | Ordinary income | Market value at time of claim |
| BRIDGE [TOKEN] TO [CHAIN] | Conservative: disposal + acquisition |  |
| MINT NFT | Acquisition | Cost base = mint price + gas |
| APPROVE / REVOKE (no transfer) | Not a CGT event | Gas fee adds to cost of next related transaction |

## Section 4 -- Computation Method

### Step 1: Identify All CGT Events

- **Identify All CGT Events** — List every disposal in the financial year (sells, swaps, spends, gifts, DeFi events).

### Step 2: Calculate Gain/Loss per Event

- **Calculate Gain/Loss per Event** — Capital proceeds − cost base = capital gain (or capital loss).

### Step 3: Apply 50% Discount (if eligible)

- **Apply 50% Discount (if eligible)** — For each gain where asset held ≥ 12 months: net capital gain = gain × 50%.

### Step 4: Offset Capital Losses

- **Offset Capital Losses** — Apply current and prior year capital losses against gross capital gains BEFORE applying the 50% discount. **Correct order:** Gross gains − capital losses = net gain. Then apply 50% discount to remaining gains eligible.

### Step 5: Add Ordinary Income

- **Add Ordinary Income** — Staking rewards + airdrops + mining income reported as other income (not in CGT schedule).

### Step 6: Report on Tax Return

- **Report on Tax Return** — Capital gains: Item 18 (Capital gains); Ordinary crypto income: Item 24 (Other income)

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

- **Retention period** — Retention period: 5 years from the date of lodgement of the return in which the gain/loss is reported. For assets still held: records must be kept until 5 years after eventual disposal.

## Section 6 -- Edge Cases

### 6.1 Hard Forks

- **Hard Forks** — Tokens received from a hard fork (e.g., Bitcoin Cash from Bitcoin) have a cost base of $0. No income at receipt. CGT event occurs on subsequent disposal with cost base = $0.

### 6.2 Lost or Stolen Crypto

- **Lost or Stolen Crypto** — A capital loss may be claimed if the crypto is demonstrably lost (e.g., lost private keys with no possibility of recovery, scam/hack with no recovery). The taxpayer must demonstrate the loss is permanent. ATO may require evidence.

### 6.3 Mining

**Mining**

| Scenario | Treatment |
| --- | --- |
| Hobby miner (small scale) | Mined coins acquired at $0 cost base; CGT on disposal |
| Business miner (significant scale) | Ordinary income at market value when mined; trading stock rules may apply |

### 6.4 Crypto Received as Payment for Services

- **Crypto Received as Payment for Services** — Assessable as ordinary income (PSI or business income) at market value in AUD at time of receipt. Cost base for future CGT = that market value.

### 6.5 Margin Trading / Futures

- **Margin Trading / Futures** — Profits and losses from crypto derivatives and margin trading are generally on revenue account (ordinary income/loss) unless clearly a one-off speculative punt.

## Section 7 -- Prohibitions

- **Prohibitions** — NEVER claim the personal use asset exemption for crypto held on an exchange for extended periods; NEVER apply the 50% CGT discount without verifying 12+ months holding period; NEVER apply the 50% CGT discount for companies or non-residents; NEVER offset capital losses against ordinary income (only against capital gains); NEVER apply capital losses before gross gains (apply losses first, THEN discount); NEVER ignore crypto-to-crypto swaps as non-events -- each swap is a disposal; NEVER assume DeFi events are non-taxable -- conservative approach is to treat as disposals; NEVER omit staking/airdrop income -- it is ordinary income when received; NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
