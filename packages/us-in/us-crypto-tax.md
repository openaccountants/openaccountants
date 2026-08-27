---
name: us-crypto-tax
description: ALWAYS USE THIS SKILL when a user asks about cryptocurrency taxation, digital asset reporting, or mentions any of these trigger phrases — crypto, bitcoin, ethereum, Form 8949, digital assets, staking, mining, NFT, DeFi, airdrop, token swap, liquidity pool, yield farming, cost basis crypto, wash sale crypto, Form 1099-DA, Coinbase taxes, Kraken taxes, crypto capital gains, virtual currency, blockchain income. Covers IRS treatment of cryptocurrency and digital assets as property under Notice 2014-21, Form 8949 and Schedule D reporting, cost basis methods, staking and mining income, airdrops, hard forks, DeFi transactions, NFT collectibles treatment, wash sale inapplicability, Form 1099-DA requirements, FBAR/Form 8938 for foreign exchanges, and transaction pattern recognition from major exchanges. US federal only; state-specific crypto rules require separate state skills.
version: 1.0
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
category: federal
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Crypto Tax

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **a licensed accountant** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Crypto Tax (US)

- **Treatment** — Treated as property  _(IRS Notice 2014-21; IRS digital-asset FAQs.)_
- **Default** — FIFO is the default; specific identification permitted with adequate records  _(Treas. Reg. 1.1012-1(j); Rev. Proc. 2024-28.)_
- **Avg cost** — Averaging is not allowed for digital assets (only FIFO or specific ID)  _(Rev. Proc. 2024-28; Treas. Reg. 1.1012-1(c)/(j).)_
- **NIIT** — 3.8% NIIT applies to crypto investment gains above MAGI thresholds  _(IRC 1411.)_
- **FBAR** — The $10,000 aggregate threshold is correct for foreign financial accounts generally, but a foreign account holding ONLY virtual currency is not currently FBAR-reportable (FinCEN Notice 2020-2 proposed to add virtual currency but the rule is not finalized). As applied to crypto, this is premature/misleading.  _(31 CFR 1010.350; FinCEN Notice 2020-2.)_

### IRS Notice 2014-21: Crypto as property

- **Property treatment** — Virtual currency is treated as property for federal tax purposes. General tax principles applicable to property transactions apply to transactions using virtual currency. Virtual currency is not treated as currency for purposes of determining foreign currency gain or loss under §988.  _(IRS Notice 2014-21)_
- **Key consequences of property treatment** — Every disposition is a taxable event requiring gain/loss calculation; Holding period determines short-term vs long-term treatment; Basis must be tracked for every lot acquired; Like-kind exchange under §1031 does NOT apply to crypto (confirmed by TCJA 2017 limiting §1031 to real property); Constructive receipt rules apply when crypto is credited to wallet  _(IRS Notice 2014-21; TCJA 2017)_

### IRS digital asset question on Form 1040

- **Digital asset question text** — For tax year 2025, every taxpayer must answer the digital asset question on Form 1040 page 1: "At any time during 2025, did you: (a) receive (as a reward, award, or payment for property or services); or (b) sell, exchange, or otherwise dispose of a digital asset (or a financial interest in a digital asset)?"  _(Form 1040 (2025))_
- **Answer Yes if taxpayer** — Received crypto as payment for services (including mining/staking rewards); Sold crypto for fiat; Exchanged one crypto for another; Received an airdrop; Received crypto from a hard fork and disposed of it; Used crypto to pay for goods or services  _(Form 1040 instructions)_
- **Answer No only if taxpayer** — Held crypto without any transactions; Transferred between own wallets (same owner); Purchased crypto with fiat and took no other action  _(Form 1040 instructions)_

### Taxable events requiring Form 8949 reporting

- **Taxable events** — 1. Sale of crypto for fiat currency (USD, EUR, etc.); 2. Exchange of one crypto for another (BTC → ETH is a taxable disposition of BTC); 3. Using crypto to purchase goods or services; 4. Receiving crypto as payment (ordinary income at FMV, then basis established); 5. Liquidating a DeFi position; 6. Selling an NFT  _(Form 8949 instructions)_

### Form 8949 columns

- **Columns** — Column (a): Description of property — e.g., "2.5 BTC" or "1,000 ETH"; Column (b): Date acquired; Column (c): Date sold or disposed; Column (d): Proceeds (FMV in USD at time of disposition); Column (e): Cost or other basis; Column (f): Adjustment code (if any); Column (g): Adjustment amount; Column (h): Gain or loss (d minus e, plus or minus g)  _(Form 8949 instructions)_

### Box checking on Form 8949

- **Box definitions** — For 2025 digital assets, use the dedicated digital-asset boxes: Box G (short-term, 1099-DA with basis reported), Box H (short-term, 1099-DA, basis not reported), Box I (short-term, no 1099-DA received); Boxes J, K, L are the long-term counterparts. Do not use Box C for digital assets.  _(2025 Instructions for Form 8949)_

### Schedule D summary

- **Schedule D structure** — Part I: Short-term capital gains and losses (holding period ≤ 1 year); Part II: Long-term capital gains and losses (holding period > 1 year); Schedule D totals flow to Form 1040 Line 7 (or Schedule D Tax Worksheet if needed)  _(Schedule D instructions)_

### Capital gains rates (2025)

**Short-term capital gains rates (2025, ordinary income brackets)**  _(IRC (2025 brackets))_

| Rate | Single | MFJ |
| --- | --- | --- |
| 10% | $0–$11,925 | $0–$23,850 |
| 12% | $11,926–$48,475 | $23,851–$96,950 |
| 22% | $48,476–$103,350 | $96,951–$206,700 |
| 24% | $103,351–$197,300 | $206,701–$394,600 |
| 32% | $197,301–$250,525 | $394,601–$501,050 |
| 35% | $250,526–$626,350 | $501,051–$751,600 |
| 37% | Over $626,350 | Over $751,600 |

**Long-term capital gains rates (2025)**  _(IRC (2025 brackets))_

| Rate | Single | MFJ |
| --- | --- | --- |
| 0% | $0–$48,350 | $0–$96,700 |
| 15% | $48,351–$533,400 | $96,701–$600,050 |
| 20% | Over $533,400 | Over $600,050 |

- **Net Investment Income Tax (NIIT)** — Additional 3.8% on net investment income for AGI above $200,000 (single) / $250,000 (MFJ) percent  _(§1411)_

### Specific identification (recommended)

- **Requirements** — The taxpayer identifies exactly which lots are being sold. Requires contemporaneous records showing: Date and time of acquisition for each lot; Amount of crypto acquired; FMV at acquisition (cost basis); Transaction ID or wallet address for identification. Specific identification allows tax-loss harvesting and holding period optimization. Per Rev. Proc. 2024-28, specific identification requires adequate records designating the specific unit sold at the time of the transaction. If the taxpayer cannot adequately identify the units sold, FIFO applies by default.  _(Rev. Proc. 2024-28; Treas. Reg. §1.1012-1(j))_

### FIFO (First In, First Out)

- **FIFO default method** — Default method if specific identification records are inadequate. The earliest-acquired units are deemed sold first. Generally results in more long-term gains if the taxpayer has been accumulating over time.  _(Treas. Reg. 1.1012-1(j))_

### HIFO (Highest In, First Out)

- **HIFO method** — A subset of specific identification where the taxpayer deliberately selects the highest-basis lots to minimize current gain. Legal if specific identification requirements are met.  _(Rev. Proc. 2024-28)_

### Average cost basis

- **Average cost basis not permitted** — NOT permitted for cryptocurrency. Average cost is only available for mutual fund shares and dividend reinvestment plan shares under Reg. §1.1012-1(e). Crypto does not qualify. Taxpayers who used average cost on prior returns may need to file amended returns.  _(Reg. §1.1012-1(e))_

### Universal basis tracking requirement (new for 2025+)

- **Broker basis reporting** — Under the broker reporting regulations (TD 10000), beginning January 1, 2025, brokers must track and report cost basis. Taxpayers using exchanges that are now classified as brokers will receive Form 1099-DA (gross proceeds only for 2025; basis reporting begins with 2026 acquisitions). For transactions on non-broker platforms (DeFi protocols, peer-to-peer), the taxpayer must maintain their own basis records.  _(TD 10000; Treas. Reg. §1.6045-1)_

### Tax treatment

- **Staking income timing and recognition** — Staking rewards are ordinary income at the fair market value (FMV) at the time the taxpayer gains dominion and control over the rewards. Income recognized when rewards are credited to the staking wallet and freely transferable; If rewards are locked during an unbonding period, income is recognized when the unbonding completes and tokens become available; Reported on Schedule 1 Line 8z (Other income) or Schedule C if staking constitutes a trade or business.  _(IRS guidance on staking (dominion and control))_

### Basis in staked tokens received

- **Basis and holding period** — The taxpayer's basis in tokens received as staking rewards equals the FMV reported as income. The holding period for these tokens begins the day after receipt.  _(IRS guidance on staking)_

### When staking is a trade or business (Schedule C)

- **Trade or business criteria and SE tax** — If the taxpayer operates a validator node with: Continuity and regularity of activity; Primary purpose of income or profit; Significant personal effort (maintaining uptime, software updates, hardware). Then staking income is reported on Schedule C and subject to self-employment tax (15.3% on first $176,100 of net earnings for 2025, 2.9% thereafter).  _(IRC self-employment tax provisions)_

### When staking is passive (Schedule 1)

- **Passive staking treatment** — If the taxpayer delegates to a staking pool or exchange-managed staking (e.g., Coinbase staking, Kraken staking): Income reported on Schedule 1 Line 8z; NOT subject to self-employment tax; Subject to NIIT (3.8%) if AGI exceeds threshold.  _(IRC §1411)_

### Ethereum-specific: post-Merge staking

- **ETH staking rewards recognition** — ETH staking rewards from the Beacon Chain are recognized as income at FMV when withdrawn (post-Shanghai upgrade, April 2023). For 2025, all ETH staking rewards are freely withdrawable and taxable upon receipt.  _(IRS guidance on staking; Shanghai upgrade April 2023)_

### Tax treatment

- **Mining income recognition** — Mining rewards (block rewards + transaction fees) are ordinary income at FMV when the miner gains dominion and control (typically when the block is confirmed and coins are spendable).  _(IRS guidance on mining)_

### Individual miner (hobby vs. business)

- **Trade or business (Schedule C)** — Mining is conducted with continuity and regularity; Primary purpose is profit; Equipment costs, electricity, and facility costs are deductible against mining income; Net mining income subject to self-employment tax; Equipment depreciable under MACRS (5-year property for computer equipment) or §179 expensing  _(MACRS; §179)_
- **Hobby (Schedule 1)** — Mining is sporadic or incidental; Hobby loss rules under §183 apply: no deduction for expenses exceeding income (post-TCJA, hobby expenses are not deductible at all); Income still taxable, reported on Schedule 1 Line 8z  _(§183; TCJA)_

### Pool mining

- **Pool mining treatment** — Income recognized when the pool distributes the miner's share; Pool fees are deductible if mining is a trade or business; Report gross mining income before pool fees on Schedule C Line 1, pool fees on Line 10 (Commissions and fees)  _(Schedule C instructions)_

### Mining equipment depreciation

- **Depreciation rules** — MACRS 5-year property (computers and peripherals); §179 expensing available up to $2,500,000 for 2025 (OBBBA); Bonus depreciation: 100% for property acquired and placed in service after January 19, 2025 (OBBBA restored; 40% applies only to property acquired before January 20, 2025); If equipment becomes worthless or is scrapped, remaining basis is deductible as a loss in that year  _(MACRS; OBBBA (P.L. 119-21): §179 2025 limit $2,500,000; IRC §168(k))_

### Tax treatment

- **Airdrop income recognition** — Airdrops are ordinary income at FMV at the time of receipt, provided: The taxpayer has dominion and control (tokens are in the wallet and freely transferable); The airdrop has ascertainable FMV (listed on an exchange with trading volume). Per Rev. Rul. 2019-24 (as applied to airdrops): taxpayer receiving new cryptocurrency has ordinary income equal to FMV at time of receipt.  _(Rev. Rul. 2019-24)_

### Unsolicited airdrops

- **Unsolicited airdrops still taxable** — Even if the taxpayer did not request the airdrop, it is still taxable upon receipt if it has FMV. The taxpayer cannot avoid income by ignoring tokens in their wallet.  _(Rev. Rul. 2019-24)_

### Airdrops with no ascertainable FMV

- **No ascertainable FMV positions** — If the airdropped token has no trading market and no ascertainable FMV at receipt: Some practitioners take the position that income is $0 at receipt, with $0 basis; This position is aggressive and should be flagged for reviewer; Conservative position: use any available pricing data (DEX pools, OTC markets) to establish FMV  _(Practitioner guidance (aggressive position — flag for reviewer))_

### Basis in airdropped tokens

- **Basis and holding period** — Basis equals the FMV reported as income. Holding period begins the day after receipt.  _(Rev. Rul. 2019-24)_

### Tax treatment per Rev. Rul. 2019-24

- **Hard fork taxability** — A hard fork that does not result in an airdrop (i.e., the taxpayer does not receive new tokens on the new chain) does NOT create a taxable event. A hard fork followed by an airdrop (taxpayer receives new tokens): ordinary income at FMV when taxpayer has dominion and control over the new tokens.  _(Rev. Rul. 2019-24)_

### Dominion and control for fork tokens

- **Dominion and control criteria** — The taxpayer has dominion and control when: The new chain is live and the tokens are accessible; The taxpayer's wallet or exchange supports the new chain; The tokens can be transferred or sold. If the exchange does not support the fork and the taxpayer cannot access the new tokens: no income until access is established.  _(Rev. Rul. 2019-24)_

### Basis allocation

- **Basis allocation for forked tokens** — No basis from the original token is allocated to the forked token. The forked token's basis equals the amount of ordinary income recognized (FMV at receipt). The original token retains its original basis.  _(Rev. Rul. 2019-24)_

### Token swaps on DEXs (Uniswap, SushiSwap, etc.)

- **Token swap taxability** — A token swap is a taxable exchange. Selling Token A for Token B: Proceeds = FMV of Token B received; Basis = cost basis of Token A disposed; Gain/loss recognized on Form 8949  _(Form 8949 instructions; general property tax principles)_

### Liquidity pool (LP) positions

- **Providing liquidity** — Depositing tokens into an LP may constitute a taxable exchange (position uncertain); Conservative position: treat deposit as a taxable disposition of both tokens for the LP token received; Aggressive position: treat LP deposit as a non-taxable open transaction until withdrawal; Flag for reviewer: IRS has not issued definitive guidance on LP deposits  _(No definitive IRS guidance — flag for reviewer)_
- **LP fee income** — Trading fees earned by LPs are ordinary income when received/accrued; Report on Schedule 1 Line 8z or Schedule C if LP activity constitutes a trade or business  _(IRS guidance on ordinary income)_
- **Impermanent loss** — Not deductible as a separate loss; Reflected in the reduced value of tokens withdrawn from the pool; Capital loss recognized only upon actual disposition of the LP position  _(General property tax principles)_
- **Withdrawing from LP** — Taxable event: recognize gain/loss based on difference between value received and basis in LP position  _(General property tax principles)_

### Lending (Aave, Compound, etc.)

- **Interest earned from lending** — Ordinary income at FMV when received; similar treatment to staking (Schedule 1 or Schedule C depending on the trade-or-business determination). Crypto lending rewards are NOT statutory interest from a bank or bond payor, so Schedule B does not apply; report as other income at FMV. No crypto-specific interest guidance exists.  _(IRC §61(a); Notice 2014-21)_
- **Depositing collateral** — Not a taxable event (similar to pledging securities for a margin loan). The taxpayer retains ownership; tokens are returned upon repayment.  _(General property tax principles)_
- **Borrowing** — Not a taxable event (receiving loan proceeds is not income); Interest paid on crypto loans: potentially deductible as investment interest under §163(d) if proceeds used for investment; If collateral is liquidated: taxable disposition of the collateral tokens  _(§163(d))_

### Yield farming / liquidity mining

- **Yield farming income** — Governance tokens or reward tokens received for providing liquidity: ordinary income at FMV when received; Same treatment as staking/mining rewards; Basis in tokens received = FMV recognized as income  _(IRS guidance on ordinary income for rewards)_

### Wrapped tokens (WBTC, wETH)

- **Wrapping treatment** — Wrapping: exchanging BTC for WBTC or ETH for wETH; Position uncertain: arguably not a taxable event if economically equivalent; Conservative position: taxable exchange (recognize gain/loss); Aggressive position: non-taxable (same underlying asset, just a representation change); Flag for reviewer  _(No definitive IRS guidance — flag for reviewer)_

### General treatment

- **NFT property treatment** — NFTs are digital assets treated as property. Buying, selling, and exchanging NFTs follows the same capital gains framework as other crypto.  _(IRS Notice 2014-21 general property principles)_

### Collectibles rate (28%)

- **Collectibles maximum rate** — 28% percent (Under §408(m), long-term capital gains on "collectibles" are taxed at a maximum rate of 28% instead of the standard 20% maximum rate. An NFT may qualify as a collectible if it represents: A work of art; A rug or antique; A metal or gem; A stamp or coin; An alcoholic beverage; Any other tangible personal property specified by the IRS. IRS Notice 2023-27 provides a look-through framework: if the NFT represents a right to a collectible (e.g., digital art), it may be taxed at the 28% collectibles rate. If it represents a non-collectible asset (e.g., event tickets, in-game items with utility), the standard long-term rates apply.)  _(§408(m); IRS Notice 2023-27)_

### NFT creator income

- **Creator income treatment** — Artists/creators who mint and sell NFTs: Sale proceeds are ordinary income (self-employment income) if the creator is in the trade or business of creating NFTs; Report on Schedule C; Subject to SE tax; Minting costs (gas fees) are deductible business expenses  _(Schedule C instructions)_

### Royalties on secondary sales

- **Royalty income treatment** — Smart contract royalties received by NFT creators on secondary sales: ordinary income; Report on Schedule C or Schedule E depending on whether the creator is actively involved  _(Schedule C/E instructions)_

### Current law: NOT applicable to crypto

- **Wash sale inapplicability** — IRC §1091 (wash sale rule) applies only to "stock or securities." Cryptocurrency is classified as property, not stock or securities. Therefore, the wash sale rule does NOT currently apply to crypto. This means a taxpayer can: Sell crypto at a loss; Immediately repurchase the same crypto; Claim the capital loss without the 30-day waiting period required for stocks  _(IRC §1091)_

### Proposed legislation (not yet enacted)

- **Proposed wash sale legislation** — Multiple proposals have been introduced to extend wash sale rules to digital assets: Build Back Better Act (2021) — did not pass; Lummis-Gillibrand Responsible Financial Innovation Act — introduced but not enacted; Various 2024-2025 proposals. For 2025 tax year: Wash sale rule does NOT apply. Crypto tax-loss harvesting is fully permitted. Flag for reviewer: If legislation passes retroactively or effective for 2025, positions may need amendment. Monitor legislative developments.  _(Build Back Better Act (2021); Lummis-Gillibrand Responsible Financial Innovation Act)_

### Background

- **Form 1099-DA background** — The Infrastructure Investment and Jobs Act (2021) expanded the definition of "broker" to include digital asset exchanges and certain DeFi platforms, effective January 1, 2025.  _(Infrastructure Investment and Jobs Act (2021))_

### What Form 1099-DA reports

- **Reported fields** — Gross proceeds from sales or exchanges of digital assets; Cost basis (if the broker has the information); Date of acquisition; Date of sale; Type of digital asset; Whether the gain is short-term or long-term  _(Form 1099-DA)_

### Who receives Form 1099-DA

- **Recipients** — Taxpayers who used: Centralized exchanges (Coinbase, Kraken, Gemini, Binance.US); Certain payment processors handling crypto; Hosted wallet providers that facilitate dispositions  _(Form 1099-DA)_

### Who does NOT receive Form 1099-DA

- **Non-recipients** — Self-custodied wallet transactions (hardware wallets, MetaMask); Peer-to-peer transactions; Certain DeFi protocols (the DeFi broker rule, TD 10021, was REPEALED under the Congressional Review Act by P.L. 119-5 on April 10, 2025, and the regulations were removed at 90 FR 31136; non-custodial DeFi front-ends are not brokers and will not issue Form 1099-DA, and the CRA bars a substantially similar rule absent new legislation)  _(P.L. 119-5; 90 FR 31136)_

### Reconciliation

- **Reconciliation guidance** — Taxpayers must reconcile Form 1099-DA against their own records: 1099-DA may not reflect correct basis (especially for transferred-in tokens); 1099-DA may report gross proceeds without netting fees; If basis on 1099-DA is incorrect, report on Form 8949 Box B with adjustment in column (f)/(g)  _(Form 8949 instructions)_

### Current law

- **No de minimis exemption** — There is no statutory de minimis exemption for crypto transactions. Every transaction, regardless of size, is technically a taxable event requiring reporting.  _(General property tax principles)_

### Proposed safe harbor

- **Proposed de minimis exclusion** — Multiple legislative proposals have included a de minimis exclusion ($200 or $600 gain per transaction) for using crypto as a medium of exchange. None have been enacted as of 2025.  _(Legislative proposals (not enacted))_

### Practical guidance

- **Practical guidance for small transactions** — All transactions must be reported regardless of size; For very small transactions (coffee purchases with Bitcoin), the gain/loss must still be computed; Aggregate reporting on Form 8949 is permitted: multiple small transactions can be combined into a single line if same exchange, same asset, same holding period category; Reference: Form 8949 instructions allow summary reporting per broker statement  _(Form 8949 instructions)_

### FBAR (FinCEN Form 114)

- **FBAR requirement and application to crypto** — Requirement: US persons with financial interest in or signature authority over foreign financial accounts must file FBAR if the aggregate value exceeds $10,000 at any time during the calendar year. Application to crypto: a foreign account holding ONLY virtual currency is not currently FBAR-reportable (FinCEN Notice 2020-2 announced an intent to change this; the rule remains unfinalized), but an account that also holds or can hold fiat or other reportable assets counts in full toward the $10,000 threshold. Filing deadline: April 15 (automatic extension to October 15); filed electronically through FinCEN BSA E-Filing. Penalties for non-filing (2025 inflation-adjusted): up to $16,536 per violation (non-willful), or the greater of $165,353 or 50% of the account balance (willful); amounts re-adjust each January.  _(31 CFR 1010.350; FinCEN Notice 2020-2)_
- **FBAR aggregate threshold** — 10000 USD  _(31 CFR 1010.350)_

### Form 8938 (FATCA)

**Form 8938 thresholds (end of year / any time during year)**  _(FATCA Form 8938 instructions)_

| Filing status | End of year | Any time during year |
| --- | --- | --- |
| Single, living in US | $50,000 | $75,000 |
| MFJ, living in US | $100,000 | $150,000 |
| Single, living abroad | $200,000 | $300,000 |
| MFJ, living abroad | $400,000 | $600,000 |

- **Application to crypto** — Accounts on foreign exchanges holding digital assets may be reportable as specified foreign financial assets.  _(FATCA Form 8938 instructions)_

### Domestic exchanges — no FBAR/8938

- **Domestic exchange exclusion** — Coinbase, Kraken, Gemini, Binance.US are US-based. Accounts on these exchanges are NOT reported on FBAR or Form 8938.  _(FBAR/FATCA guidance)_

### Coinbase

- **Coinbase reporting patterns** — Provides annual tax report and Form 1099-MISC (for staking/rewards over $600); Beginning 2025: Form 1099-DA for sales; Transaction history downloadable as CSV; Fields: timestamp, transaction type, asset, quantity, spot price, subtotal, total (including fees), notes; Coinbase Pro (now Advanced Trade): separate transaction history; Coinbase Wallet (self-custody): not reported by Coinbase

### Kraken

- **Kraken reporting patterns** — Provides transaction history and ledger export; Beginning 2025: Form 1099-DA for US customers; CSV fields: txid, refid, time, type, subtype, aclass, asset, amount, fee, balance; Staking rewards itemized in ledger; Kraken has historically provided Form 1099-MISC for staking income > $600

### Gemini

- **Gemini reporting patterns** — Provides transaction history export; Beginning 2025: Form 1099-DA; CSV fields: date, time, type, symbol, specification, liquidity indicator, trading fee, quantity, price, amount, trade ID; Gemini Earn interest reported on Form 1099-MISC (program discontinued, but legacy reporting may apply)

### Binance.US

- **Binance.US reporting patterns** — Provides transaction history and tax reports; Beginning 2025: Form 1099-DA; CSV fields: date, pair, type, order price, order amount, average trading price, filled, total, trigger condition, status; Note: Binance.US has limited trading pairs compared to international Binance

### General reconciliation approach

- **Reconciliation steps** — 1. Download complete transaction history from each exchange; 2. Identify all deposits (trace origin: purchased on exchange, transferred from wallet, received as payment); 3. Identify all withdrawals (trace destination: transferred to wallet, sent as payment, sold for fiat); 4. Match deposits/withdrawals between exchanges to avoid double-counting; 5. Compute basis for each lot using chosen method (specific ID or FIFO); 6. Generate Form 8949 entries for all dispositions; 7. Separate short-term from long-term based on holding period; 8. Cross-check against any 1099-DA received

### Lost or stolen crypto

- **Theft, worthlessness, and lost keys** — Theft loss: Under TCJA (2018-2025), personal theft losses are only deductible if attributable to a federally declared disaster. Crypto theft generally does NOT qualify. Exception: If the crypto was held in a trade or business, the loss may be deductible under §165(c)(1). Worthless tokens: Capital loss in the year the token becomes worthless (must demonstrate complete worthlessness). Lost keys/inaccessible wallet: No deduction until the taxpayer can demonstrate the crypto is permanently inaccessible (abandonment loss requires affirmative act).  _(TCJA (2018-2025); §165(c)(1))_

### Gifts of crypto

- **Gift tax treatment** — Donor: No taxable event upon gifting. Recipient basis: Carryover basis from donor (for gains); FMV at time of gift (for losses, if FMV < donor's basis). Gift tax: Form 709 required if gift exceeds $19,000 annual exclusion (2025) per recipient. Holding period: Tacks (recipient includes donor's holding period) if using carryover basis.  _(Form 709; Rev. Proc. 2024-40: 2025 annual exclusion $19,000)_

### Charitable donations of crypto

- **Charitable donation treatment** — Held > 1 year: Deduct FMV, no capital gains recognized (§170(e) long-term capital gain property). Held ≤ 1 year: Deduct lesser of FMV or basis. Qualified appraisal required for donations > $5,000 (Form 8283 Section B). Donations > $500: Form 8283 Section A required.  _(§170(e); Form 8283)_

### Crypto received as compensation

- **Compensation treatment** — W-2 employees receiving crypto: FMV included in Box 1 of W-2, subject to withholding. Independent contractors receiving crypto: Ordinary income at FMV, reported on Schedule C. Basis = FMV at time of receipt (amount included in income).  _(W-2/Schedule C reporting rules)_

### Margin trading and futures

- **Margin and futures treatment** — Crypto margin trades: Same as regular trades, gain/loss on disposition. Crypto futures on regulated exchanges (CME Bitcoin futures): Subject to §1256 (60% long-term / 40% short-term, marked-to-market). Crypto perpetual futures on unregulated exchanges: Standard capital gain/loss treatment (not §1256).  _(§1256)_

### What records to maintain

- **Recordkeeping requirements** — Per IRS guidance (FAQ Q39-Q41): Date and time of each transaction; Quantity of digital asset received or transferred; FMV at time of transaction (with source of valuation); Purpose of the transaction; Counterparty information (if available); Wallet addresses involved; Transaction IDs (hash); Exchange records  _(IRS FAQ Q39-Q41)_

### Valuation sources

- **Acceptable FMV sources** — Exchange where the transaction occurred (best evidence); CoinMarketCap, CoinGecko (widely accepted); Exchange APIs with timestamp-level pricing; Block explorer data (for on-chain transactions). Use consistent valuation methodology. Document the source used.

### Retention period

- **Record retention periods** — Standard: 3 years from filing date (§6501 statute of limitations); If income understated by >25%: 6 years; If no return filed or fraudulent return: unlimited; Recommendation: retain crypto records indefinitely (basis tracking requires historical data)  _(§6501)_

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

## Section 18 — Refusals

- **R-CRYPTO-1 — Insufficient records** — If the taxpayer cannot provide transaction history or wallet records for material positions, refuse to prepare Form 8949. Recommend engaging a crypto tax specialist with forensic blockchain analysis capability (Chainalysis, CoinTracker integration).  _(R-CRYPTO-1)_
- **R-CRYPTO-2 — Foreign exchange non-compliance** — If the taxpayer held material amounts on foreign exchanges and has not previously filed FBAR, this requires voluntary disclosure analysis. Refuse and refer to tax attorney specializing in offshore compliance (Streamlined Filing Compliance Procedures or VDP).  _(R-CRYPTO-2)_
- **R-CRYPTO-3 — Active DeFi trading without records** — If the taxpayer interacted with multiple DeFi protocols without maintaining records (common with dozens of yield farming positions), refuse to estimate. Recommend CoinTracker, Koinly, or TokenTax for reconstruction.  _(R-CRYPTO-3)_
- **R-CRYPTO-4 — §1256 contract classification dispute** — If the taxpayer traded crypto futures and the classification as §1256 contracts is disputed, flag for reviewer. Do not take a position without CPA signoff.  _(R-CRYPTO-4)_

## Section 19 — Cross-skill references

**Inputs:**
- Taxpayer intake data (filing status, income level for bracket/NIIT determination)
- Transaction history from exchanges (CSV or 1099-DA)
- Staking/mining/DeFi activity records

**Outputs consumed by:**
- `us-federal-return-assembly` — Form 8949, Schedule D totals, ordinary income items
- `us-quarterly-estimated-tax` — crypto income affects estimated tax calculations
- State skills — some states have crypto-specific adjustments

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

## End of Skill

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
