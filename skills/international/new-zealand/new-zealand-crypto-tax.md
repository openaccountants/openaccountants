---
name: new-zealand-crypto-tax
description: Use this skill whenever asked about New Zealand cryptocurrency or cryptoasset taxation. Trigger on phrases like "crypto tax New Zealand", "crypto tax NZ", "Bitcoin NZ tax", "IRD crypto", "cryptoassets NZ", "cryptocurrency gains NZ", "crypto income NZ", "staking NZ", "mining income NZ", "NFT tax NZ", "DeFi NZ tax", "IR3 crypto", "purpose of disposal crypto", "intention test crypto NZ", "GST crypto NZ", or any question about the income tax or GST treatment of cryptocurrency, tokens, or digital assets for New Zealand tax residents or NZ-source crypto income. Covers IRD cryptoasset guidance, the purpose-of-disposal test under s CB 4, GST exemption, cost basis, DeFi/staking/mining, and IR3 reporting. ALWAYS read this skill before touching any New Zealand crypto work.
version: 1.0
jurisdiction: NZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - new-zealand-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand Crypto Tax

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | New Zealand (Aotearoa) |
| Tax | Income Tax on Cryptoassets |
| Currency | NZD — all values must be converted to NZD at the transaction date |
| Tax year | 1 April -- 31 March (e.g., 2025 tax year = 1 April 2024 -- 31 March 2025) |
| Primary authority | Income Tax Act 2007 (ITA 2007), ss CA 1, CB 3, CB 4, CB 5; Goods and Services Tax Act 1985 (GST Act), ss 2(1), 3, 20H |
| Supporting guidance | IRD Cryptoassets guidance (ird.govt.nz/cryptoassets); Tax Information Bulletin Vol 34 No 5 (Jun 2022); TDS 25/23 (Oct 2025) |
| Tax authority | Inland Revenue (Te Tari Taake, IRD) |
| Filing portal | myIR (myir.ird.govt.nz) |
| Filing deadline | 7 July following the tax year end (or 31 March of the following year if using a tax agent) |
| Capital gains tax | **New Zealand has NO general capital gains tax** — crypto taxation depends on the PURPOSE of acquisition |
| Validated by | Pending — requires sign-off by a New Zealand Chartered Accountant (CA) or tax advisor |
| Skill version | 1.0 |

### The Central Rule

**New Zealand does not have a capital gains tax.** Whether crypto profits are taxable depends on the taxpayer's **dominant purpose at the time of acquisition**. If you acquired crypto with the purpose of disposing of it (selling, exchanging, spending), profits on disposal are taxable income. If acquired purely as a long-term investment with no intention to sell, profits may not be taxable — but the burden of proof is on the taxpayer.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown purpose at acquisition | Treat as acquired for purpose of disposal (taxable) — conservative |
| Trading vs investment unclear | Treat as taxable until taxpayer provides clear evidence of investment intent |
| Unknown cost basis method | Use FIFO unless taxpayer has documented another method |
| Staking rewards — income or capital? | Treat as income (taxable at receipt) — per IRD guidance and TDS 25/23 |
| DeFi transaction classification | Treat token deposits to protocols as potential disposals unless clearly not |
| GST on crypto | Crypto sales are EXEMPT from GST; do NOT charge GST on crypto-for-fiat |
| Unknown tax residency | STOP — NZ residents taxed on worldwide income; non-residents on NZ-source only |

## Section 2 -- Classification Rules

**Section 2 header**

### 2.1 Legal Classification

**2.1 Legal Classification**

| Term | Definition | Authority |
| --- | --- | --- |
| Cryptoasset | A form of property for tax purposes; not legal tender | IRD guidance; ITA 2007 |
| Property | Includes any real or personal property, estate or interest in property, and any right or interest | ITA 2007 s YA 1 |
| Excepted financial arrangement | Cryptoassets are excluded from the financial arrangements rules | ITA 2007 s EW 5(22B) |
| Not money | Crypto is not "money" for tax purposes | IRD guidance |

### 2.2 The Purpose-of-Disposal Test (s CB 4)

This is the **key provision** for NZ crypto taxation:

> Under s CB 4 of the ITA 2007, an amount derived from disposing of personal property is income if the property was acquired for the **purpose of disposing of it**.

**Purpose-of-Disposal Test factors table**

| Factor | Indicates Purpose of Disposal (Taxable) | Indicates NOT Purpose of Disposal |
| --- | --- | --- |
| Stated intent at purchase | "I'll sell when it goes up" | "I'm holding for 10+ years regardless" |
| Holding period | Short (days to months) | Long (years) |
| Frequency of transactions | Many trades, frequent portfolio changes | Rare, infrequent transactions |
| Source of expected return | Price appreciation via trading | Passive income (staking) with no plan to sell underlying |
| Evidence | Trading history, stop-loss orders, leverage | Long-term wallet with no outflows |
| Profit expectation | Expected to profit more from disposal than passive income | Expected to earn more from staking/passive than from selling |

### 2.3 Other Income Provisions

Even if s CB 4 does not apply (no purpose of disposal), crypto profits may still be taxable under:

**Other Income Provisions table**

| Provision | Description |
| --- | --- |
| s CB 3 — Profit-making scheme | If the taxpayer carries on a profit-making undertaking or scheme |
| s CB 5 — Amount from business | If the crypto activity constitutes a business |
| s CA 1(2) — Income under ordinary concepts | Catch-all: regular, expected returns with the character of income |

### 2.4 Burden of Proof

- **Burden of proof** — Per TDS 25/23 (Oct 2025): the onus is on the taxpayer to show they did NOT acquire crypto for the purpose of disposal. The Commissioner does not need to prove intent — the taxpayer must provide "clear and compelling evidence" of non-disposal purpose.  _(TDS 25/23 (Oct 2025))_

## Section 3 -- Rate Tables

**Section 3 header**

### 3.1 Individual Income Tax Rates (2025/26 Tax Year — 1 April 2025 to 31 March 2026)

**Individual Income Tax Rates 2025/26**  _(ITA 2007 Schedule 1; rates confirmed by Taxation (Annual Rates for 2025–26) Act 2026.)_

| Taxable Income (NZD) | Marginal Rate |
| --- | --- |
| $0 – $15,600 | 10.5% |
| $15,601 – $53,500 | 17.5% |
| $53,501 – $78,100 | 30% |
| $78,101 – $180,000 | 33% |
| $180,001 and over | 39% |

- **No tax-free threshold** — There is no tax-free threshold in New Zealand — tax applies from the first dollar of income at 10.5%.  _(ITA 2007 Schedule 1)_
- **Crypto income aggregation** — Crypto income is added to all other income to determine the applicable marginal rate.

### 3.2 Prior Year Rates (2024/25 Tax Year — 1 April 2024 to 31 March 2025)

**Prior Year Rates 2024/25**

| Taxable Income (NZD) | Marginal Rate |
| --- | --- |
| $0 – $15,600 | 10.5% |
| $15,601 – $53,500 | 17.5% |
| $53,501 – $78,100 | 30% |
| $78,101 – $180,000 | 33% |
| $180,001 and over | 39% |

Note: The 2024/25 year had transitional composite rates due to mid-year threshold changes (effective 31 July 2024). For simplicity, use the full-year 2025/26 rates for the current year.

### 3.3 Company Tax Rate

**Company Tax Rate table**

| Entity | Rate |
| --- | --- |
| Companies | 28% |
| Trusts (trustee income) | 39% |

### 3.4 GST

**GST treatment table**

| Transaction | GST Treatment | Authority |
| --- | --- | --- |
| Sale/purchase of cryptocurrency | **EXEMPT** — not subject to GST | GST Act s 2(1), as amended; TIB Vol 34 No 5 |
| Payment for goods/services using crypto | GST applies to the underlying supply, not to the crypto | Standard GST rules |
| NFT sales | **Subject to GST** — NFTs are NOT excluded from GST | GST Act (NFTs not covered by cryptocurrency exemption) |
| Mining as a service | Subject to GST at 15% if provided as a taxable supply | Standard GST rules |

- **GST Act amendment citation** — Taxation (Annual Rates for 2024–25, Emergency Response, and Remedial Matters) Act — amended GST Act to exclude cryptocurrency from both "goods" and "services" definitions. NFTs remain GST-able.  _(Taxation (Annual Rates for 2024–25, Emergency Response, and Remedial Matters) Act)_

## Section 4 -- Cost Basis Methods

**Section 4 header**

### 4.1 Accepted Methods

**Accepted Methods table**

| Method | Status |
| --- | --- |
| FIFO (First In, First Out) | Accepted; widely used |
| Weighted average cost | Accepted |
| Specific identification | Accepted if clearly documented |
| LIFO | Not standard; not recommended |

- **Consistency requirement** — The taxpayer must choose a method and apply it consistently.

### 4.2 Cost Basis Components

**Cost Basis Components table**

| Component | Included? |
| --- | --- |
| Purchase price in NZD (converted at transaction-date exchange rate) | Yes |
| Exchange fees and commissions on acquisition | Yes |
| Network/gas fees on acquisition | Yes |
| Exchange fees and commissions on disposal | Yes — deductible from proceeds |
| NZD conversion: use mid-market rate on transaction date | Yes |

### 4.3 Trading Stock Rules

- **Trading stock valuation** — If cryptoassets are trading stock (held as part of a business of trading crypto), they must be valued at cost at the end of the tax year. Cryptoassets are excepted financial arrangements, so market-to-market valuation under the financial arrangements rules does NOT apply.  _(ITA 2007 s EW 5(22B); TIB Vol 34 No 5.)_

### 4.4 NZD Conversion

- **NZD conversion method** — All transactions must be converted to NZD. Use the mid-market exchange rate on the date of each transaction. For crypto-to-crypto trades, determine the NZD value of the crypto disposed of at the time of the exchange.

## Section 5 -- DeFi / Staking / Mining / Airdrop Treatment

**Section 5 header**

### 5.1 Mining

**Mining table**

| Aspect | Treatment |
| --- | --- |
| Mining rewards received | Taxable income at FMV (NZD) on date of receipt |
| Classification | Income under ordinary concepts (s CA 1(2)) or business income (s CB 5) |
| Cost basis of mined coins | FMV at receipt (for future disposal calculation) |
| Expenses | Deductible if mining constitutes a business (electricity, equipment depreciation, etc.) |
| Hobby mining | Still taxable — income character depends on regularity and amount |

### 5.2 Staking

**Staking table**

| Aspect | Treatment |
| --- | --- |
| Staking rewards received | **Taxable as income** at FMV on date of receipt — per IRD guidance and TDS 25/23 |
| Rationale | Regular receipt of staking rewards = "return on investment" = income under ordinary concepts |
| Cost basis of staking rewards | FMV at receipt date (for future disposal) |
| Disposal of staking rewards | Separately taxable event — gain/loss computed using receipt-date FMV as cost basis |
| Dominant purpose analysis | Even if underlying crypto was acquired for staking income (not disposal), staking rewards themselves are income; but the underlying crypto's disposal may NOT be taxable if staking was the dominant purpose |

**Key distinction (per TDS 25/23):** If you bought crypto primarily to earn staking income, the staking rewards are income when received. But the profit on selling the **original** crypto may not be taxable if you can show your dominant purpose was passive income, not disposal. However, the burden of proof is on you, and IRD has taken aggressive positions.

### 5.3 Airdrops

**Airdrops table**

| Aspect | Treatment |
| --- | --- |
| Airdrop from existing holding (fork/snapshot) | Income at FMV if received because of existing holdings; cost basis of NZD 0 if FMV unclear |
| Promotional airdrop (unsolicited) | Taxable at FMV when received — income under ordinary concepts |
| Airdrop for performing a service | Income at FMV — clearly taxable |
| Subsequent disposal of airdropped tokens | Taxable if acquired for purpose of disposal; cost basis = FMV at receipt |

- **Airdrop citation** — IRD Issues Paper — "Income tax treatment of cryptoassets received from blockchain forks and airdrops" (Dec 2020, updated Jan 2026).  _(IRD Issues Paper — "Income tax treatment of cryptoassets received from blockchain forks and airdrops" (Dec 2020, updated Jan 2026))_

### 5.4 DeFi

**DeFi table**

| Activity | Treatment |
| --- | --- |
| DeFi lending (depositing crypto to earn interest) | Interest income taxable at FMV when received |
| Liquidity provision (AMM pools) | Depositing tokens to pool = potential disposal if different tokens received (LP tokens); gain/loss on the "sold" tokens |
| Receiving LP tokens | New asset with cost basis = FMV of tokens deposited |
| Removing liquidity | Potential disposal of LP tokens; acquisition of underlying tokens at FMV |
| Yield farming rewards | Income at FMV when received |
| Wrapping (e.g., ETH → WETH) | IRD position evolving — conservative: treat as disposal, though gain is typically nominal |
| Bridging to another chain | Similar to wrapping — conservative: potential disposal |
| Impermanent loss | Not specifically addressed; likely NOT deductible as a standalone loss |
| Borrowing against crypto (collateralized loan) | Generally NOT a disposal (you retain ownership); but if liquidated, that is a disposal |

- **DeFi citation** — IRD Issues Paper — "Wrapping, bridging, lending, borrowing and staking cryptoassets" (ongoing).  _(IRD Issues Paper — "Wrapping, bridging, lending, borrowing and staking cryptoassets" (ongoing))_

## Section 6 -- NFT Treatment

**NFT Treatment table**

| Aspect | Treatment |
| --- | --- |
| Purchase of NFT | Acquisition cost for future disposal |
| Sale of NFT at profit | Taxable if acquired for purpose of disposal (s CB 4) |
| Creation and sale (artist/creator) | Business income — fully taxable |
| NFT royalties (ongoing) | Income when received |
| NFT-to-NFT swap | Disposal of both NFTs — compute gain/loss on each |
| GST on NFT sales | **Subject to GST at 15%** — NFTs are NOT covered by the crypto GST exemption |
| NFT as trading stock | If held in a business, trading stock rules apply |

- **NFT GST exemption note** — **Important:** The GST exemption for cryptocurrency explicitly does NOT extend to NFTs. A business selling NFTs must charge 15% GST on B2C sales to NZ customers.  _(GST Act s 2(1) as amended; TIB Vol 34 No 5.)_

## Section 7 -- Reporting Requirements

**Section 7 header**

### 7.1 Individual Filing

**Individual Filing table**

| Requirement | Detail |
| --- | --- |
| Return type | IR3 — Individual Income Tax Return |
| Filing deadline | 7 July following the tax year end (e.g., 7 July 2025 for 2024/25 tax year) |
| Extended deadline (tax agent) | 31 March of the following year (e.g., 31 March 2026 for 2024/25 year) |
| Filing portal | myIR (myir.ird.govt.nz) |
| Crypto section | No dedicated crypto schedule — include net income (or loss) in the "Other income" section of the IR3 |
| Income to declare | Net crypto income after deducting cost basis and allowable expenses |
| Loss to claim | If you made a taxable loss, declare it (must show profit would have been taxable) |

### 7.2 When Must You File an IR3?

You must file an IR3 if you have taxable income from cryptoasset activity that is not already accounted for in your income tax assessment. This includes:

- Profits from selling/exchanging crypto (if taxable under s CB 4 or other provisions)
- Mining income
- Staking rewards
- Airdrop income
- DeFi lending/yield income
- NFT trading profits

### 7.3 Provisional Tax

**Provisional Tax table**

| Who | Obligation |
| --- | --- |
| Residual income tax > $5,000 | Must register as a provisional taxpayer and make provisional tax payments |
| Payment dates | Standard: 3 installments (28 Aug, 15 Jan, 7 May) — or use AIM (Accounting Income Method) for monthly payments |

### 7.4 Record-Keeping

**Record-Keeping table**

| Requirement | Detail |
| --- | --- |
| Retention period | 7 years |
| Records to maintain | Full transaction logs, exchange records, wallet addresses, cost basis calculations, evidence of acquisition purpose, staking/mining logs |
| NZD conversion records | Exchange rates used for each transaction |
| Purpose documentation | Written record of intent at time of acquisition (emails, notes, investment strategy documents) |
| Burden of proof | On the taxpayer — must demonstrate acquisition purpose |

## Section 8 -- Loss Offset and Carry-Forward

**Section 8 header**

### 8.1 Loss Offset Rules

**Loss Offset Rules table**

| Rule | Detail |
| --- | --- |
| Losses from crypto disposal | Claimable ONLY if the gain would have been taxable (i.e., acquired for purpose of disposal) |
| Offset against other income | Crypto losses can offset other income types within the same year (including employment income) — for individuals |
| Loss carry-forward | Available — excess losses can be carried forward to future years |
| Company loss carry-forward | Subject to shareholder continuity rules |
| Loss carry-back | NOT available for individuals |

### 8.2 Key Principle

- **Key principle for claiming loss** — To claim a crypto loss, the taxpayer must demonstrate that if they had made a profit, it would have been taxable. This means showing that the crypto was acquired for the purpose of disposal (or under another income provision). You cannot claim a loss on crypto that was held as a non-taxable long-term investment.

### 8.3 Trading Stock Losses

- **Trading stock losses** — If crypto is trading stock in a business, losses on disposal are deductible business expenses. Year-end valuation at cost (not market) means unrealized losses are NOT deductible.

## Section 9 -- Anti-Avoidance Rules

**Section 9 header**

### 9.1 General Anti-Avoidance (s BG 1)

- **General anti-avoidance rule** — The ITA 2007 contains a broad general anti-avoidance rule. Any arrangement that has a purpose or effect of tax avoidance may be voided by the Commissioner. This applies to crypto structures designed to avoid the purpose-of-disposal test.  _(ITA 2007 s BG 1)_

### 9.2 Aggressive Position — "Clear and Compelling Evidence"

Per TDS 25/23, the IRD takes an aggressive view on crypto: if you claim your crypto was NOT acquired for the purpose of disposal, you need "clear and compelling evidence." Factors IRD will scrutinize:

- Subsequent trading history (even if you initially intended to hold)
- Whether you expected more return from disposal than from passive income
- Whether you used exchanges with easy sell functionality
- Pattern of behavior across multiple cryptoassets

### 9.3 Transitional Residents

Non-residents and transitional residents (new arrivals to NZ) may have different obligations:

**Transitional Residents table**

| Status | Treatment |
| --- | --- |
| NZ tax resident | Worldwide crypto income taxable |
| Non-resident | Only NZ-source crypto income taxable (sourcing rules complex for crypto) |
| Transitional resident (first 4 years) | Exempt from tax on most foreign-source income, but NZ-source crypto income still taxable |

- **Transitional resident citation** — ITA 2007 s HR 8; TDS discussed transitional resident crypto cases.  _(ITA 2007 s HR 8)_

### 9.4 Information Sharing

**Information Sharing table**

| Measure | Detail |
| --- | --- |
| CRS (Common Reporting Standard) | NZ participates; financial account data shared with other jurisdictions |
| CARF (when implemented) | Crypto-specific exchange-of-information framework — NZ expected to adopt |
| Domestic exchange cooperation | NZ-based exchanges cooperate with IRD on data requests |

## Section 10 -- Worked Examples

### Example 1 -- Crypto Acquired for Purpose of Disposal (Taxable)

**Input:** NZ tax resident, employed full-time (salary $85,000). Bought 2 ETH on Easy Crypto NZ in July 2024 for NZD $6,000 total. Sold 2 ETH in January 2025 for NZD $10,000. Exchange fees: NZD $100. Bought with explicit intention to "sell when ETH hits $5,000 per coin."

**Computation:**
```
Tax year:                2024/25 (1 Apr 2024 – 31 Mar 2025)

Disposal proceeds:       $10,000
Less exchange fees:        -$100
Net proceeds:             $9,900

Cost basis (FIFO):        $6,000
Gain:                     $3,900

Purpose test:            Acquired to sell at target price → purpose of disposal → TAXABLE

Total income:            $85,000 salary + $3,900 crypto = $88,900

Tax on crypto gain:      Marginal rate at $85,001–$88,900 = 33%
Additional tax:          $3,900 × 33% = $1,287
```

Reported in IR3 filed by 7 July 2025 (or 31 March 2026 via tax agent).

### Example 2 -- Staking Rewards with Non-Disposal Purpose on Underlying

**Input:** NZ tax resident. Bought 100 SOL in May 2024 for NZD $20,000. Primary purpose: stake for passive income. No intention to sell the underlying SOL. Earned 5 SOL in staking rewards over 2024/25 tax year, FMV of NZD $1,000 at receipt dates. In February 2025, sold all 5 staking reward SOL for NZD $1,200.

**Computation:**
```
Step 1 — Staking rewards received:
  Income at receipt:     $1,000 (taxable as income under ordinary concepts per TDS 25/23)

Step 2 — Disposal of staking rewards:
  Proceeds:              $1,200
  Cost basis:            $1,000 (FMV at receipt)
  Gain:                  $200

  Purpose test on staking rewards: acquired through staking, subsequently sold
  → likely purpose of disposal → gain of $200 is TAXABLE

Step 3 — Original 100 SOL:
  NOT sold — no disposal event
  If sold later: taxpayer would argue dominant purpose was passive income (staking),
  not disposal → potentially NOT taxable. But burden of proof on taxpayer.

Total crypto income for year:  $1,000 (staking) + $200 (gain on reward disposal) = $1,200
Added to other income for progressive rate computation.
```

### Example 3 -- Long-Term Holder (NOT Taxable)

**Input:** NZ tax resident. Bought 1 BTC in 2019 for NZD $8,000. Documented investment strategy: "long-term store of value, part of retirement savings, no plan to sell for at least 15 years." Sold in 2025 for NZD $95,000 due to unexpected medical emergency. Has written investment policy, no trading history, 6-year hold, single transaction.

**Computation:**
```
Proceeds:              $95,000
Cost basis:             $8,000
Gain:                  $87,000

Purpose test:          NOT acquired for purpose of disposal — compelling evidence:
  - Written investment policy
  - 6-year holding period
  - No other crypto trades
  - Sale triggered by unforeseen emergency
  - Employed full-time separately

Tax:                   Likely NOT TAXABLE — investor, not trader

CAUTION: IRD could challenge this. Taxpayer should retain all evidence.
Flag for reviewer: confirm purpose-of-disposal analysis.
```

## Self-Checks

Before finalising any New Zealand crypto tax computation, verify:

- [ ] Has the taxpayer confirmed NZ tax residency (or transitional resident status)?
- [ ] What was the **dominant purpose at the time of acquisition**? Is there evidence?
- [ ] Are all values converted to NZD at the transaction-date mid-market rate?
- [ ] Has the correct cost basis method been applied consistently (FIFO or weighted average)?
- [ ] Have staking/mining/airdrop receipts been included as income at FMV?
- [ ] Is crypto treated as trading stock if part of a business?
- [ ] GST: confirmed crypto sales are EXEMPT; confirmed NFT sales are subject to GST?
- [ ] If claiming a loss: would the gain have been taxable? (Required to claim the loss)
- [ ] Provisional tax: does residual tax exceed $5,000?
- [ ] Filing deadline: 7 July (or 31 March via tax agent)?
- [ ] Are DeFi transactions analyzed individually for disposal/income events?
- [ ] Flag for reviewer: has IRD issued any updated guidance since this skill was written?

## PROHIBITIONS

- NEVER state that NZ has a capital gains tax — it does not; crypto taxation is based on purpose of acquisition
- NEVER assume all crypto profits are tax-free — the purpose-of-disposal test makes most active trading taxable
- NEVER ignore the burden of proof — taxpayer must prove non-disposal intent, not the other way around
- NEVER charge GST on crypto-for-fiat sales — cryptocurrency is exempt from GST
- NEVER treat NFTs the same as crypto for GST — NFTs ARE subject to GST
- NEVER ignore staking rewards as income — IRD and TDS 25/23 confirm they are taxable
- NEVER allow a loss claim on crypto that was held as a non-taxable investment
- NEVER use market value for trading stock year-end — must use cost (excepted financial arrangement)
- NEVER treat transfers between own wallets as disposals
- NEVER ignore the transitional resident exemption for new NZ arrivals
- NEVER present crypto tax positions as definitive — the purpose test is fact-specific; always flag for professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant (CA), tax advisor, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
