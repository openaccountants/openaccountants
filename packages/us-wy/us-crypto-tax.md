---
name: us-crypto-tax
description: ALWAYS USE THIS SKILL when a user asks about cryptocurrency taxation, digital asset reporting, or mentions any of these trigger phrases — crypto, bitcoin, ethereum, Form 8949, digital assets, staking, mining, NFT, DeFi, airdrop, token swap, liquidity pool, yield farming, cost basis crypto, wash sale crypto, Form 1099-DA, Coinbase taxes, Kraken taxes, crypto capital gains, virtual currency, blockchain income. Covers IRS treatment of cryptocurrency and digital assets as property under Notice 2014-21, Form 8949 and Schedule D reporting, cost basis methods, staking and mining income, airdrops, hard forks, DeFi transactions, NFT collectibles treatment, wash sale inapplicability, Form 1099-DA requirements, FBAR/Form 8938 for foreign exchanges, and transaction pattern recognition from major exchanges. US federal only; state-specific crypto rules require separate state skills.
version: 1.0
jurisdiction: US
tax_year: 2025
category: federal
---

# US Crypto Tax Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

> This block is generated from the verified facts database at openaccountants.com —
> edit the facts there, not this prose. Items under clarification are excluded.

### Crypto Tax (US)

- **Treatment** — Treated as property  _(IRS Notice 2014-21; IRS digital-asset FAQs.)_
- **Default** — FIFO is the default; specific identification permitted with adequate records  _(Treas. Reg. 1.1012-1(j); Rev. Proc. 2024-28.)_
- **Avg cost** — Averaging is not allowed for digital assets (only FIFO or specific ID)  _(Rev. Proc. 2024-28; Treas. Reg. 1.1012-1(c)/(j).)_
- **NIIT** — 3.8% NIIT applies to crypto investment gains above MAGI thresholds  _(IRC 1411.)_
- **FBAR** — The $10,000 aggregate threshold is correct for foreign financial accounts generally, but a foreign account holding ONLY virtual currency is not currently FBAR-reportable (FinCEN Notice 2020-2 proposed to add virtual currency but the rule is not finalized). As applied to crypto, this is premature/misleading.  _(31 CFR 1010.350; FinCEN Notice 2020-2.)_

## Section 1 — Foundational framework

### IRS Notice 2014-21: Crypto as property

Virtual currency is treated as property for federal tax purposes. General tax principles applicable to property transactions apply to transactions using virtual currency. Virtual currency is not treated as currency for purposes of determining foreign currency gain or loss under §988.

Key consequences of property treatment:
- Every disposition is a taxable event requiring gain/loss calculation
- Holding period determines short-term vs long-term treatment
- Basis must be tracked for every lot acquired
- Like-kind exchange under §1031 does NOT apply to crypto (confirmed by TCJA 2017 limiting §1031 to real property)
- Constructive receipt rules apply when crypto is credited to wallet

### IRS digital asset question on Form 1040

For tax year 2025, every taxpayer must answer the digital asset question on Form 1040 page 1: "At any time during 2025, did you: (a) receive (as a reward, award, or payment for property or services); or (b) sell, exchange, gift, or otherwise dispose of a digital asset (or a financial interest in a digital asset)?"

Answer "Yes" if the taxpayer:
- Received crypto as payment for services (including mining/staking rewards)
- Sold crypto for fiat
- Exchanged one crypto for another
- Received an airdrop
- Received crypto from a hard fork and disposed of it
- Used crypto to pay for goods or services
- Gifted crypto

Answer "No" only if the taxpayer:
- Held crypto without any transactions
- Transferred between own wallets (same owner)
- Purchased crypto with fiat and took no other action

---

## Section 2 — Capital gains reporting: Form 8949 and Schedule D

### Taxable events requiring Form 8949 reporting

1. Sale of crypto for fiat currency (USD, EUR, etc.)
2. Exchange of one crypto for another (BTC → ETH is a taxable disposition of BTC)
3. Using crypto to purchase goods or services
4. Receiving crypto as payment (ordinary income at FMV, then basis established)
5. Liquidating a DeFi position
6. Selling an NFT

### Form 8949 columns

- Column (a): Description of property — e.g., "2.5 BTC" or "1,000 ETH"
- Column (b): Date acquired
- Column (c): Date sold or disposed
- Column (d): Proceeds (FMV in USD at time of disposition)
- Column (e): Cost or other basis
- Column (f): Adjustment code (if any)
- Column (g): Adjustment amount
- Column (h): Gain or loss (d minus e, plus or minus g)

### Box checking on Form 8949

- **Box A**: Transactions reported on Form 1099-B (or 1099-DA) showing basis was reported to IRS
- **Box B**: Transactions reported on Form 1099-B (or 1099-DA) where basis was NOT reported to IRS
- **Box C**: Transactions not reported on any Form 1099

Most crypto transactions for 2025 fall into Box C unless the exchange provided Form 1099-DA with basis.

### Schedule D summary

- Part I: Short-term capital gains and losses (holding period ≤ 1 year)
- Part II: Long-term capital gains and losses (holding period > 1 year)
- Schedule D totals flow to Form 1040 Line 7 (or Schedule D Tax Worksheet if needed)

### Capital gains rates (2025)

**Short-term (held ≤ 1 year):** Taxed as ordinary income at the taxpayer's marginal rate:
- 10%: $0–$11,925 (single) / $0–$23,850 (MFJ)
- 12%: $11,926–$48,475 (single) / $23,851–$96,950 (MFJ)
- 22%: $48,476–$103,350 (single) / $96,951–$206,700 (MFJ)
- 24%: $103,351–$197,300 (single) / $206,701–$394,600 (MFJ)
- 32%: $197,301–$250,525 (single) / $394,601–$501,050 (MFJ)
- 35%: $250,526–$626,350 (single) / $501,051–$751,600 (MFJ)
- 37%: Over $626,350 (single) / Over $751,600 (MFJ)

**Long-term (held > 1 year):**
- 0%: $0–$48,350 (single) / $0–$96,700 (MFJ)
- 15%: $48,351–$533,400 (single) / $96,701–$600,050 (MFJ)
- 20%: Over $533,400 (single) / Over $600,050 (MFJ)

**Net Investment Income Tax (NIIT):** Additional 3.8% on net investment income for AGI above $200,000 (single) / $250,000 (MFJ) under §1411.

---

## Section 3 — Cost basis methods

### Specific identification (recommended)

The taxpayer identifies exactly which lots are being sold. Requires contemporaneous records showing:
- Date and time of acquisition for each lot
- Amount of crypto acquired
- FMV at acquisition (cost basis)
- Transaction ID or wallet address for identification

Specific identification allows tax-loss harvesting and holding period optimization.

Per Rev. Rul. 2024-14, specific identification requires adequate records designating the specific unit sold at the time of the transaction. If the taxpayer cannot adequately identify the units sold, FIFO applies by default.

### FIFO (First In, First Out)

Default method if specific identification records are inadequate. The earliest-acquired units are deemed sold first. Generally results in more long-term gains if the taxpayer has been accumulating over time.

### HIFO (Highest In, First Out)

A subset of specific identification where the taxpayer deliberately selects the highest-basis lots to minimize current gain. Legal if specific identification requirements are met.

### Average cost basis

**NOT permitted for cryptocurrency.** Average cost is only available for mutual fund shares and dividend reinvestment plan shares under Reg. §1.1012-1(e). Crypto does not qualify. Taxpayers who used average cost on prior returns may need to file amended returns.

### Universal basis tracking requirement (new for 2025+)

Under the broker reporting regulations (TD 9877), beginning January 1, 2025, brokers must track and report cost basis. Taxpayers using exchanges that are now classified as brokers will receive Form 1099-DA with basis information. For transactions on non-broker platforms (DeFi protocols, peer-to-peer), the taxpayer must maintain their own basis records.

---

## Section 4 — Staking income

### Tax treatment

Staking rewards are ordinary income at the fair market value (FMV) at the time the taxpayer gains dominion and control over the rewards. This means:

- Income recognized when rewards are credited to the staking wallet and freely transferable
- If rewards are locked during an unbonding period, income is recognized when the unbonding completes and tokens become available
- Reported on Schedule 1 Line 8z (Other income) or Schedule C if staking constitutes a trade or business

### Basis in staked tokens received

The taxpayer's basis in tokens received as staking rewards equals the FMV reported as income. The holding period for these tokens begins the day after receipt.

### When staking is a trade or business (Schedule C)

If the taxpayer operates a validator node with:
- Continuity and regularity of activity
- Primary purpose of income or profit
- Significant personal effort (maintaining uptime, software updates, hardware)

Then staking income is reported on Schedule C and subject to self-employment tax (15.3% on first $176,100 of net earnings for 2025, 2.9% thereafter).

### When staking is passive (Schedule 1)

If the taxpayer delegates to a staking pool or exchange-managed staking (e.g., Coinbase staking, Kraken staking):
- Income reported on Schedule 1 Line 8z
- NOT subject to self-employment tax
- Subject to NIIT (3.8%) if AGI exceeds threshold

### Ethereum-specific: post-Merge staking

ETH staking rewards from the Beacon Chain are recognized as income at FMV when withdrawn (post-Shanghai upgrade, April 2023). For 2025, all ETH staking rewards are freely withdrawable and taxable upon receipt.

---

## Section 5 — Mining income

### Tax treatment

Mining rewards (block rewards + transaction fees) are ordinary income at FMV when the miner gains dominion and control (typically when the block is confirmed and coins are spendable).

### Individual miner (hobby vs. business)

**Trade or business (Schedule C):**
- Mining is conducted with continuity and regularity
- Primary purpose is profit
- Equipment costs, electricity, and facility costs are deductible against mining income
- Net mining income subject to self-employment tax
- Equipment depreciable under MACRS (5-year property for computer equipment) or §179 expensing

**Hobby (Schedule 1):**
- Mining is sporadic or incidental
- Hobby loss rules under §183 apply: no deduction for expenses exceeding income (post-TCJA, hobby expenses are not deductible at all)
- Income still taxable, reported on Schedule 1 Line 8z

### Pool mining

When mining through a pool:
- Income recognized when the pool distributes the miner's share
- Pool fees are deductible if mining is a trade or business
- Report gross mining income before pool fees on Schedule C Line 1, pool fees on Line 10 (Commissions and fees)

### Mining equipment depreciation

- MACRS 5-year property (computers and peripherals)
- §179 expensing available up to $1,250,000 for 2025
- Bonus depreciation: 40% for property placed in service in 2025 (phasing down from 100% in 2022)
- If equipment becomes worthless or is scrapped, remaining basis is deductible as a loss in that year

---

## Section 6 — Airdrops

### Tax treatment

Airdrops are ordinary income at FMV at the time of receipt, provided:
- The taxpayer has dominion and control (tokens are in the wallet and freely transferable)
- The airdrop has ascertainable FMV (listed on an exchange with trading volume)

Per Rev. Rul. 2019-24 (as applied to airdrops): taxpayer receiving new cryptocurrency has ordinary income equal to FMV at time of receipt.

### Unsolicited airdrops

Even if the taxpayer did not request the airdrop, it is still taxable upon receipt if it has FMV. The taxpayer cannot avoid income by ignoring tokens in their wallet.

### Airdrops with no ascertainable FMV

If the airdropped token has no trading market and no ascertainable FMV at receipt:
- Some practitioners take the position that income is $0 at receipt, with $0 basis
- This position is aggressive and should be flagged for reviewer
- Conservative position: use any available pricing data (DEX pools, OTC markets) to establish FMV

### Basis in airdropped tokens

Basis equals the FMV reported as income. Holding period begins the day after receipt.

---

## Section 7 — Hard forks

### Tax treatment per Rev. Rul. 2019-24

A hard fork that does not result in an airdrop (i.e., the taxpayer does not receive new tokens on the new chain) does NOT create a taxable event.

A hard fork followed by an airdrop (taxpayer receives new tokens): ordinary income at FMV when taxpayer has dominion and control over the new tokens.

### Dominion and control for fork tokens

The taxpayer has dominion and control when:
- The new chain is live and the tokens are accessible
- The taxpayer's wallet or exchange supports the new chain
- The tokens can be transferred or sold

If the exchange does not support the fork and the taxpayer cannot access the new tokens: no income until access is established.

### Basis allocation

No basis from the original token is allocated to the forked token. The forked token's basis equals the amount of ordinary income recognized (FMV at receipt). The original token retains its original basis.

---

## Section 8 — DeFi transactions

### Token swaps on DEXs (Uniswap, SushiSwap, etc.)

A token swap is a taxable exchange. Selling Token A for Token B:
- Proceeds = FMV of Token B received
- Basis = cost basis of Token A disposed
- Gain/loss recognized on Form 8949

### Liquidity pool (LP) positions

**Providing liquidity:**
- Depositing tokens into an LP may constitute a taxable exchange (position uncertain)
- Conservative position: treat deposit as a taxable disposition of both tokens for the LP token received
- Aggressive position: treat LP deposit as a non-taxable open transaction until withdrawal
- Flag for reviewer: IRS has not issued definitive guidance on LP deposits

**LP fee income:**
- Trading fees earned by LPs are ordinary income when received/accrued
- Report on Schedule 1 Line 8z or Schedule C if LP activity constitutes a trade or business

**Impermanent loss:**
- Not deductible as a separate loss
- Reflected in the reduced value of tokens withdrawn from the pool
- Capital loss recognized only upon actual disposition of the LP position

**Withdrawing from LP:**
- Taxable event: recognize gain/loss based on difference between value received and basis in LP position

### Lending (Aave, Compound, etc.)

**Interest earned from lending:**
- Ordinary income at FMV when received
- Similar treatment to staking (Schedule 1 or Schedule C depending on trade or business determination)
- Report as interest income on Schedule B if > $1,500 in crypto interest

**Depositing collateral:**
- Not a taxable event (similar to pledging securities for a margin loan)
- The taxpayer retains ownership; tokens are returned upon repayment

**Borrowing:**
- Not a taxable event (receiving loan proceeds is not income)
- Interest paid on crypto loans: potentially deductible as investment interest under §163(d) if proceeds used for investment
- If collateral is liquidated: taxable disposition of the collateral tokens

### Yield farming / liquidity mining

- Governance tokens or reward tokens received for providing liquidity: ordinary income at FMV when received
- Same treatment as staking/mining rewards
- Basis in tokens received = FMV recognized as income

### Wrapped tokens (WBTC, wETH)

- Wrapping: exchanging BTC for WBTC or ETH for wETH
- Position uncertain: arguably not a taxable event if economically equivalent
- Conservative position: taxable exchange (recognize gain/loss)
- Aggressive position: non-taxable (same underlying asset, just a representation change)
- Flag for reviewer

---

## Section 9 — NFTs

### General treatment

NFTs are digital assets treated as property. Buying, selling, and exchanging NFTs follows the same capital gains framework as other crypto.

### Collectibles rate (28%)

Under §408(m), long-term capital gains on "collectibles" are taxed at a maximum rate of 28% instead of the standard 20% maximum rate.

An NFT may qualify as a collectible if it represents:
- A work of art
- A rug or antique
- A metal or gem
- A stamp or coin
- An alcoholic beverage
- Any other tangible personal property specified by the IRS

**IRS Notice 2023-27** provides a look-through framework: if the NFT represents a right to a collectible (e.g., digital art), it may be taxed at the 28% collectibles rate. If it represents a non-collectible asset (e.g., event tickets, in-game items with utility), the standard long-term rates apply.

### NFT creator income

Artists/creators who mint and sell NFTs:
- Sale proceeds are ordinary income (self-employment income) if the creator is in the trade or business of creating NFTs
- Report on Schedule C
- Subject to SE tax
- Minting costs (gas fees) are deductible business expenses

### Royalties on secondary sales

- Smart contract royalties received by NFT creators on secondary sales: ordinary income
- Report on Schedule C or Schedule E depending on whether the creator is actively involved

---

## Section 10 — Wash sale rule

### Current law: NOT applicable to crypto

IRC §1091 (wash sale rule) applies only to "stock or securities." Cryptocurrency is classified as property, not stock or securities. Therefore, the wash sale rule does NOT currently apply to crypto.

This means a taxpayer can:
- Sell crypto at a loss
- Immediately repurchase the same crypto
- Claim the capital loss without the 30-day waiting period required for stocks

### Proposed legislation (not yet enacted)

Multiple proposals have been introduced to extend wash sale rules to digital assets:
- Build Back Better Act (2021) — did not pass
- Lummis-Gillibrand Responsible Financial Innovation Act — introduced but not enacted
- Various 2024-2025 proposals

**For 2025 tax year:** Wash sale rule does NOT apply. Crypto tax-loss harvesting is fully permitted.

**Flag for reviewer:** If legislation passes retroactively or effective for 2025, positions may need amendment. Monitor legislative developments.

---

## Section 11 — Form 1099-DA (new reporting)

### Background

The Infrastructure Investment and Jobs Act (2021) expanded the definition of "broker" to include digital asset exchanges and certain DeFi platforms, effective January 1, 2025.

### What Form 1099-DA reports

- Gross proceeds from sales or exchanges of digital assets
- Cost basis (if the broker has the information)
- Date of acquisition
- Date of sale
- Type of digital asset
- Whether the gain is short-term or long-term

### Who receives Form 1099-DA

Taxpayers who used:
- Centralized exchanges (Coinbase, Kraken, Gemini, Binance.US)
- Certain payment processors handling crypto
- Hosted wallet providers that facilitate dispositions

### Who does NOT receive Form 1099-DA

- Self-custodied wallet transactions (hardware wallets, MetaMask)
- Peer-to-peer transactions
- Certain DeFi protocols (IRS implementation of DeFi broker rules delayed to 2026+)

### Reconciliation

Taxpayers must reconcile Form 1099-DA against their own records:
- 1099-DA may not reflect correct basis (especially for transferred-in tokens)
- 1099-DA may report gross proceeds without netting fees
- If basis on 1099-DA is incorrect, report on Form 8949 Box B with adjustment in column (f)/(g)

---

## Section 12 — De minimis safe harbor

### Current law

There is no statutory de minimis exemption for crypto transactions. Every transaction, regardless of size, is technically a taxable event requiring reporting.

### Proposed safe harbor

Multiple legislative proposals have included a de minimis exclusion ($200 or $600 gain per transaction) for using crypto as a medium of exchange. None have been enacted as of 2025.

### Practical guidance

- All transactions must be reported regardless of size
- For very small transactions (coffee purchases with Bitcoin), the gain/loss must still be computed
- Aggregate reporting on Form 8949 is permitted: multiple small transactions can be combined into a single line if same exchange, same asset, same holding period category
- Reference: Form 8949 instructions allow summary reporting per broker statement

---

## Section 13 — Foreign exchange reporting

### FBAR (FinCEN Form 114)

**Requirement:** US persons with financial interest in or signature authority over foreign financial accounts must file FBAR if the aggregate value exceeds $10,000 at any time during the calendar year.

**Application to crypto:** If the taxpayer holds crypto on a foreign exchange (Binance international, KuCoin, Bybit, OKX, etc.), the account is reportable on FBAR.

- Filing deadline: April 15 (automatic extension to October 15)
- Filed electronically through FinCEN BSA E-Filing
- Penalties for non-filing: up to $12,886 per account per year (non-willful), or greater of $129,210 or 50% of account balance (willful)

### Form 8938 (FATCA)

**Requirement:** US persons with specified foreign financial assets exceeding threshold must file Form 8938.

**Thresholds (end of year / any time during year):**
- Single, living in US: $50,000 / $75,000
- MFJ, living in US: $100,000 / $150,000
- Single, living abroad: $200,000 / $300,000
- MFJ, living abroad: $400,000 / $600,000

**Application to crypto:** Accounts on foreign exchanges holding digital assets may be reportable as specified foreign financial assets.

### Domestic exchanges — no FBAR/8938

Coinbase, Kraken, Gemini, Binance.US are US-based. Accounts on these exchanges are NOT reported on FBAR or Form 8938.

---

## Section 14 — Exchange transaction patterns

### Coinbase

- Provides annual tax report and Form 1099-MISC (for staking/rewards over $600)
- Beginning 2025: Form 1099-DA for sales
- Transaction history downloadable as CSV
- Fields: timestamp, transaction type, asset, quantity, spot price, subtotal, total (including fees), notes
- Coinbase Pro (now Advanced Trade): separate transaction history
- Coinbase Wallet (self-custody): not reported by Coinbase

### Kraken

- Provides transaction history and ledger export
- Beginning 2025: Form 1099-DA for US customers
- CSV fields: txid, refid, time, type, subtype, aclass, asset, amount, fee, balance
- Staking rewards itemized in ledger
- Kraken has historically provided Form 1099-MISC for staking income > $600

### Gemini

- Provides transaction history export
- Beginning 2025: Form 1099-DA
- CSV fields: date, time, type, symbol, specification, liquidity indicator, trading fee, quantity, price, amount, trade ID
- Gemini Earn interest reported on Form 1099-MISC (program discontinued, but legacy reporting may apply)

### Binance.US

- Provides transaction history and tax reports
- Beginning 2025: Form 1099-DA
- CSV fields: date, pair, type, order price, order amount, average trading price, filled, total, trigger condition, status
- Note: Binance.US has limited trading pairs compared to international Binance

### General reconciliation approach

1. Download complete transaction history from each exchange
2. Identify all deposits (trace origin: purchased on exchange, transferred from wallet, received as payment)
3. Identify all withdrawals (trace destination: transferred to wallet, sent as payment, sold for fiat)
4. Match deposits/withdrawals between exchanges to avoid double-counting
5. Compute basis for each lot using chosen method (specific ID or FIFO)
6. Generate Form 8949 entries for all dispositions
7. Separate short-term from long-term based on holding period
8. Cross-check against any 1099-DA received

---

## Section 15 — Special situations

### Lost or stolen crypto

- Theft loss: Under TCJA (2018-2025), personal theft losses are only deductible if attributable to a federally declared disaster. Crypto theft generally does NOT qualify.
- Exception: If the crypto was held in a trade or business, the loss may be deductible under §165(c)(1)
- Worthless tokens: Capital loss in the year the token becomes worthless (must demonstrate complete worthlessness)
- Lost keys/inaccessible wallet: No deduction until the taxpayer can demonstrate the crypto is permanently inaccessible (abandonment loss requires affirmative act)

### Gifts of crypto

- Donor: No taxable event upon gifting
- Recipient basis: Carryover basis from donor (for gains); FMV at time of gift (for losses, if FMV < donor's basis)
- Gift tax: Form 709 required if gift exceeds $18,000 annual exclusion (2025) per recipient
- Holding period: Tacks (recipient includes donor's holding period) if using carryover basis

### Charitable donations of crypto

- Held > 1 year: Deduct FMV, no capital gains recognized (§170(e) long-term capital gain property)
- Held ≤ 1 year: Deduct lesser of FMV or basis
- Qualified appraisal required for donations > $5,000 (Form 8283 Section B)
- Donations > $500: Form 8283 Section A required

### Crypto received as compensation

- W-2 employees receiving crypto: FMV included in Box 1 of W-2, subject to withholding
- Independent contractors receiving crypto: Ordinary income at FMV, reported on Schedule C
- Basis = FMV at time of receipt (amount included in income)

### Margin trading and futures

- Crypto margin trades: Same as regular trades, gain/loss on disposition
- Crypto futures on regulated exchanges (CME Bitcoin futures): Subject to §1256 (60% long-term / 40% short-term, marked-to-market)
- Crypto perpetual futures on unregulated exchanges: Standard capital gain/loss treatment (not §1256)

---

## Section 16 — Record-keeping requirements

### What records to maintain

Per IRS guidance (FAQ Q39-Q41):
- Date and time of each transaction
- Quantity of digital asset received or transferred
- FMV at time of transaction (with source of valuation)
- Purpose of the transaction
- Counterparty information (if available)
- Wallet addresses involved
- Transaction IDs (hash)
- Exchange records

### Valuation sources

Acceptable FMV sources:
- Exchange where the transaction occurred (best evidence)
- CoinMarketCap, CoinGecko (widely accepted)
- Exchange APIs with timestamp-level pricing
- Block explorer data (for on-chain transactions)

Use consistent valuation methodology. Document the source used.

### Retention period

- Standard: 3 years from filing date (§6501 statute of limitations)
- If income understated by >25%: 6 years
- If no return filed or fraudulent return: unlimited
- Recommendation: retain crypto records indefinitely (basis tracking requires historical data)

---

## Section 17 — Self-checks

**Check CRYPTO-1 — Every disposition reported.** All sales, exchanges, and uses of crypto are reported on Form 8949.

**Check CRYPTO-2 — Basis method consistent.** The same basis method (specific ID or FIFO) is applied consistently within each exchange/wallet for the tax year.

**Check CRYPTO-3 — Income recognition complete.** All staking rewards, mining income, airdrops, and DeFi income are reported as ordinary income.

**Check CRYPTO-4 — Holding period correct.** Short-term vs long-term classification matches actual holding periods with documentation.

**Check CRYPTO-5 — NIIT computed if applicable.** 3.8% NIIT applied to crypto gains if AGI exceeds threshold.

**Check CRYPTO-6 — Foreign exchange reporting evaluated.** FBAR and Form 8938 obligations assessed for foreign exchange accounts.

**Check CRYPTO-7 — Form 1040 digital asset question answered correctly.**

**Check CRYPTO-8 — 1099-DA reconciled.** Any Form 1099-DA received is reconciled against taxpayer records with adjustments noted on Form 8949.

**Check CRYPTO-9 — NFT collectibles rate evaluated.** If NFTs sold, determination made whether 28% collectibles rate applies.

**Check CRYPTO-10 — No average cost basis used.** Average cost is not permitted for crypto.

---

## Section 18 — Refusals

**R-CRYPTO-1 — Insufficient records.** If the taxpayer cannot provide transaction history or wallet records for material positions, refuse to prepare Form 8949. Recommend engaging a crypto tax specialist with forensic blockchain analysis capability (Chainalysis, CoinTracker integration).

**R-CRYPTO-2 — Foreign exchange non-compliance.** If the taxpayer held material amounts on foreign exchanges and has not previously filed FBAR, this requires voluntary disclosure analysis. Refuse and refer to tax attorney specializing in offshore compliance (Streamlined Filing Compliance Procedures or VDP).

**R-CRYPTO-3 — Active DeFi trading without records.** If the taxpayer interacted with multiple DeFi protocols without maintaining records (common with dozens of yield farming positions), refuse to estimate. Recommend CoinTracker, Koinly, or TokenTax for reconstruction.

**R-CRYPTO-4 — §1256 contract classification dispute.** If the taxpayer traded crypto futures and the classification as §1256 contracts is disputed, flag for reviewer. Do not take a position without CPA signoff.

---

## Section 19 — Cross-skill references

**Inputs:**
- Taxpayer intake data (filing status, income level for bracket/NIIT determination)
- Transaction history from exchanges (CSV or 1099-DA)
- Staking/mining/DeFi activity records

**Outputs consumed by:**
- `us-federal-return-assembly` — Form 8949, Schedule D totals, ordinary income items
- `us-quarterly-estimated-tax` — crypto income affects estimated tax calculations
- State skills — some states have crypto-specific adjustments

---

## Section 20 — Computational examples

### Example 1: Simple sale

Purchased 1.0 BTC on March 15, 2024 for $65,000. Sold 1.0 BTC on July 20, 2025 for $98,000.
- Holding period: > 1 year (long-term)
- Proceeds: $98,000
- Basis: $65,000
- Long-term capital gain: $33,000
- Report on Form 8949 Part II, Box C (no 1099 received)

### Example 2: Staking income

Staked 32 ETH on Coinbase. Received 1.2 ETH in staking rewards throughout 2025. Monthly FMV at receipt: average $3,500/ETH.
- Ordinary income: 1.2 × $3,500 = $4,200 (actual computation uses per-receipt FMV)
- Report on Schedule 1 Line 8z (delegated staking, not trade or business)
- Basis in 1.2 ETH received = $4,200
- Subject to NIIT if AGI > $200,000 (single)

### Example 3: Token swap on Uniswap

Swapped 10 ETH (basis $25,000, acquired February 2025) for 50,000 USDC on August 10, 2025.
- Holding period: < 1 year (short-term)
- Proceeds: $50,000 (FMV of USDC received)
- Basis: $25,000
- Short-term capital gain: $25,000
- Report on Form 8949 Part I, Box C

### Example 4: Airdrop

Received 1,000 ARB tokens via airdrop on March 23, 2025. FMV at receipt: $1.15/token.
- Ordinary income: 1,000 × $1.15 = $1,150
- Report on Schedule 1 Line 8z
- Basis in 1,000 ARB = $1,150
- If later sold for $2.00/token: gain = ($2,000 − $1,150) = $850

---

## End of Skill

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

---

<!-- openaccountants-cta-block -->

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://www.openaccountants.com/network).

<!-- openaccountants-mcp-cta -->

## The accountant-verified version lives in the connector

This file is the open, **research-grade draft**. The **accountant-verified**
version of this skill is **not published to GitHub** — it is delivered free
through the OpenAccountants MCP connector, where your AI agent loads the
verified rules together with the name of the accountant who signed them off.

**→ Install the free connector:** <https://www.openaccountants.com/connect>
**MCP endpoint:** `https://www.openaccountants.com/api/mcp`
