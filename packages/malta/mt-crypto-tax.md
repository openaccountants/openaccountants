---
name: mt-crypto-tax
description: Use this skill whenever asked about Malta cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Malta", "Bitcoin Malta", "DLT assets", "cryptocurrency gains", "crypto income Malta", "Binance Malta tax", "staking Malta", "mining income Malta", "NFT tax Malta", "Coinbase Malta", "Revolut crypto Malta", "token tax", "distributed ledger", "MFSA crypto", "DAC8", or any question about the income tax, capital gains, or VAT treatment of cryptocurrency, tokens, or digital assets for Malta tax residents or Malta-source crypto income. Covers the CfR DLT asset guidelines, classification of coins/tokens, trading vs investment distinction, VAT treatment, and DAC8 reporting. ALWAYS read this skill before touching any Malta crypto work.
version: 1.0
jurisdiction: MT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - malta-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MT Crypto Tax

## Malta Crypto / Digital Assets Tax Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Tax | Income Tax on DLT Assets (Crypto) |
| Currency | EUR (values must be converted to EUR at transaction date) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary authority | CfR Guidelines on Income Tax Treatment of DLT Assets (1 November 2018), issued under Article 96(2) ITA |
| Supporting legislation | Income Tax Act, Chapter 123 (Articles 4, 5, 5A, 14, 27); Virtual Financial Assets Act, Chapter 590 (MFSA regulatory — not tax); Innovative Technology Arrangements and Services Act, Chapter 592 |
| Tax authority | Commissioner for Revenue (CFR) |
| Filing portal | CFR MyTax (mytax.cfr.gov.mt) |
| Filing deadline | 30 June of the following year |
| EU reporting | DAC8 / CARF — crypto exchanges report user data to CfR from 2026 |
| Validated by | Pending — requires sign-off by a Maltese warranted accountant |
| Skill version | 1.0 |

### DLT Asset Classification (CfR Guidelines)

**DLT Asset Classification**  _(CfR Guidelines)_

| Asset Type | CfR Definition | Capital Gains Tax (Art. 5) | Income Tax |
| --- | --- | --- | --- |
| Coins (cryptocurrencies) | Medium of exchange / store of value (e.g. BTC, ETH, LTC) | NOT subject to CGT | Trading profits = ordinary income; investment gains generally not taxed |
| Utility Tokens | Access to a product/service on a DLT platform | NOT subject to CGT | Trading profits = ordinary income |
| Financial Tokens (securities) | Participate in profits, mimic shares/bonds/units in CIS | Subject to CGT if they meet "securities" definition under Art. 5 | Trading profits = ordinary income |
| Hybrid / Convertible Tokens | Start as utility, convert to financial token | Outside CGT until converted to securities | Trading profits = ordinary income |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether trading or investment | Treat as trading (taxable as ordinary income) |
| Unknown token classification | Treat as coin (not subject to CGT, but trading profits taxable) |
| Unknown cost basis | STOP — cannot compute gain without acquisition cost |
| Unknown residency / domicile | STOP — affects source and remittance rules |
| Unknown whether activity is commercial mining | Treat as commercial (taxable) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- transaction history from exchange(s) or wallet(s), confirmation of residency and domicile status, and indication of whether activity is trading or long-term investment.

**Recommended** -- full CSV exports from all exchanges used (Binance, Coinbase, Kraken, Revolut, etc.), wallet addresses with on-chain history, cost basis records for each acquisition, and record of any staking/lending/mining activity.

**Ideal** -- complete portfolio tracker export (e.g. CoinTracking, Koinly, Accointing), DeFi protocol interaction history, NFT purchase/sale records, and documentation of any token airdrops received.

### Refusal Catalogue

- **R-MTC-1 -- Residency/domicile unknown** — "Malta's crypto tax treatment depends critically on residency and domicile status. Non-domiciled residents are only taxed on foreign-source income remitted to Malta. Cannot proceed without this information."
- **R-MTC-2 -- No transaction records** — "Crypto tax computations require detailed transaction records with dates, amounts, and counterparties. Without exchange/wallet records, gains cannot be calculated. Cannot proceed."
- **R-MTC-3 -- ICO/STO issuance** — "Token issuance (ICOs, STOs, IEOs) has complex tax implications for the issuer including potential VAT, income tax, and regulatory obligations. Escalate to a warranted accountant with MFSA expertise."
- **R-MTC-4 -- Corporate crypto holdings** — "Companies holding crypto on their balance sheet have different accounting and tax treatment. This skill covers individuals only. Escalate to a warranted accountant."
- **R-MTC-5 -- Cross-border DeFi structures** — "Complex DeFi arrangements involving multiple jurisdictions, DAOs, or liquidity pool governance tokens require specialist international tax advice. Escalate."

## Section 3 -- Computation Rules

### 3.1 Coins (BTC, ETH, etc.) -- Tax Treatment

**Key principle:** Coins are treated analogously to foreign currency. They are NOT securities under Article 5 ITA.

**Coins Tax Treatment**

| Scenario | Tax Treatment |
| --- | --- |
| Held as trading stock (frequent buy/sell for profit) | Profits are **ordinary income**, taxed at progressive rates (0%--35%) |
| Held as long-term investment (buy and hold) | Gains on disposal generally **NOT taxable** (not within CGT scope, not trading income) |
| Mining — private scale | Income at market value when received; if sold within short period, practical approach: taxable as other income |
| Mining — commercial scale | Business income, taxed as self-employment |
| Staking rewards | Income at market value when received (sonstige Einkünfte equivalent) |
| Airdrops | Taxable as income if received in exchange for a service; gratuitous airdrops may not be taxable |
| Payment for goods/services | Disposal at market value — gain is trading income or not taxable depending on classification |

### 3.2 Trading vs Investment -- The Critical Distinction

The CfR applies general income tax principles. There is no statutory bright-line test. Factors indicating **trading**:

**Factors indicating Trading**

| Factor | Indicates Trading |
| --- | --- |
| Frequency of transactions | High volume, multiple trades per day/week |
| Holding period | Short (days to weeks) |
| Intent | Profit from short-term price movements |
| Sophistication | Use of leverage, derivatives, automated bots |
| Funding | Borrowed money to fund purchases |
| Organisation | Systematic, business-like approach |

Factors indicating **investment**:

**Factors indicating Investment**

| Factor | Indicates Investment |
| --- | --- |
| Frequency | Infrequent, buy-and-hold |
| Holding period | Long (months to years) |
| Intent | Long-term capital appreciation |
| Funding | Own savings |
| Other income | Has separate primary employment |

**Conservative default:** If classification is unclear, treat as trading (fully taxable).

### 3.3 Financial Tokens (Security Tokens)

- **Financial Tokens treatment** — If a token meets the definition of "securities" under Article 5 ITA (participates in company profits, return not limited to fixed rate, or units in a CIS), then: - Transfer is subject to **capital gains tax** under Article 5 - Capital gains rate: generally 0% for transfers of securities listed on a recognised exchange, or taxed at progressive rates for unlisted securities depending on the nature of the underlying - Losses on securities within the CGT regime can only offset gains within that regime  _(Article 5 ITA)_

### 3.4 Cost Basis and Methods

**Cost Basis Methods**

| Method | Status |
| --- | --- |
| FIFO (First In, First Out) | Accepted by CfR; recommended |
| Specific identification | Acceptable if clearly documented |
| Average cost | May be accepted; less common |
| LIFO | Not standard practice in Malta |

- **Cost basis includes** — The cost basis includes: - Purchase price in EUR (convert at exchange rate on date of acquisition) - Exchange fees and commissions paid on acquisition - Network/gas fees directly attributable to the transaction

### 3.5 Non-Domiciled Residents (Special Rules)

Malta's remittance basis for non-domiciled residents is critical for crypto:

**Non-Dom Rules**

| Scenario | Tax Treatment |
| --- | --- |
| Malta-domiciled resident | Worldwide crypto income taxable |
| Malta-resident but NOT Malta-domiciled | Foreign-source crypto income taxable ONLY if remitted to Malta |
| Crypto gains kept on foreign exchange (not remitted) | NOT taxable for non-doms (if source is foreign) |
| Proceeds transferred to Malta bank account | Taxable for non-doms (remittance) |
| Minimum tax for non-doms | EUR 5,000 per year (regardless of actual remittance) |

## Section 4 -- VAT Treatment

### 4.1 Crypto and VAT

**Crypto and VAT**  _(CJEU C-264/14 Hedqvist; EU VAT rules)_

| Transaction | VAT Treatment | Authority |
| --- | --- | --- |
| Exchange of crypto for fiat (and vice versa) | Exempt financial service (no VAT) | CJEU C-264/14 Hedqvist |
| Payment for goods/services using crypto | VAT applies to the underlying supply (not the crypto itself) | Standard EU VAT rules |
| Crypto exchange platform services | Exempt financial service | CJEU Hedqvist |
| Mining rewards (no identifiable recipient) | Outside scope of VAT (no supply) | General VAT principles |
| Mining as a service (identifiable recipient) | Subject to VAT at 18% | Service supply |
| NFT sale (digital art/collectible) | Subject to VAT at 18% (electronically supplied service) | EU VAT rules on digital services |
| Staking-as-a-service | Likely exempt financial service; case-by-case | CfR position evolving |

## Section 5 -- Transaction Pattern Library

### 5.1 Income Patterns (Credits)

**Income Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BINANCE WITHDRAWAL, BINANCE DEPOSIT (to bank) | Potential disposal proceeds | Convert EUR amount on date; match to cost basis |
| COINBASE PAYOUT, COINBASE EUR | Potential disposal proceeds | Match to trades on Coinbase |
| REVOLUT CRYPTO SELL, REVOLUT EXCHANGE | Disposal proceeds | Revolut provides transaction history in-app |
| KRAKEN WITHDRAWAL | Potential disposal proceeds | Match to Kraken trade history |
| MINING REWARD, POOL PAYOUT, ETHERMINE | Mining income | Taxable at market value on receipt date |
| STAKING REWARD, VALIDATOR REWARD | Staking income | Taxable at market value on receipt date |
| AIRDROP, TOKEN DISTRIBUTION | Possible income | Taxable if received for a service; potentially not if gratuitous |
| P2P TRANSFER, BISQ, LOCALBITCOINS | Potential disposal | Verify whether sale or transfer between own wallets |

### 5.2 Expense Patterns (Debits)

**Expense Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BINANCE DEPOSIT, COINBASE BUY, REVOLUT CRYPTO BUY | Acquisition cost | Record as cost basis for FIFO |
| GAS FEE, NETWORK FEE, TRANSACTION FEE | Part of cost basis | Add to acquisition cost of the asset obtained |
| EXCHANGE FEE, TRADING FEE, COMMISSION | Part of cost basis or disposal cost | Deductible from gain computation |
| HARDWARE WALLET, LEDGER, TREZOR | Business expense if trading | Capital item if trading business; not deductible if personal investment |

### 5.3 Exclusions

**Exclusions**

| Pattern | Treatment |
| --- | --- |
| TRANSFER BETWEEN OWN WALLETS | EXCLUDE — not a disposal |
| EXCHANGE TO EXCHANGE TRANSFER (same owner) | EXCLUDE — not a disposal |
| WRAPPING/UNWRAPPING (e.g. ETH → WETH) | Generally EXCLUDE — no change in economic ownership |
| STABLECOIN CONVERSION (EUR equivalent) | Technically a disposal — but gain is typically zero or negligible |

## Section 6 -- MFSA Regulatory Framework (Non-Tax)

The MFSA regulatory framework is distinct from tax but relevant for context:

**MFSA Regulatory Framework**

| Framework | Scope | Tax Relevance |
| --- | --- | --- |
| Virtual Financial Assets Act (VFAA, Chapter 590) | Licensing of VFA service providers, ICO rules | Regulatory compliance does not affect tax classification |
| Innovative Technology Arrangements Act (ITAA, Chapter 592) | Certification of DLT platforms | No direct tax impact |
| MiCA (EU Markets in Crypto-Assets Regulation) | EU-wide crypto regulation from 2024/2025 | Standardises classification; may influence future CfR guidance |
| DAC8 / CARF | Automatic exchange of crypto transaction data | Exchanges report to CfR from 2026; foreign holdings >EUR 5,000 must be declared |

## Section 7 -- Record-Keeping Requirements

**Record-Keeping Requirements**

| Requirement | Detail |
| --- | --- |
| Retention period | 6 years from end of relevant tax year |
| Records to maintain | Full transaction logs from all exchanges, wallet addresses, cost basis calculations, FIFO ledger, staking/mining logs |
| Format | CSV exports preferred; screenshots acceptable as backup; on-chain records (block explorer links) recommended |
| Burden of proof | On the taxpayer — CfR can request records; DAC8 data will allow cross-referencing |

## Section 8 -- Worked Examples

### Example 1 -- Trader, Coins, Ordinary Income

**Input:** Malta-domiciled resident. Bought 1 BTC at EUR 25,000 in January 2025. Sold 1 BTC at EUR 45,000 in March 2025. Traded frequently (50+ trades in year). Exchange fees: EUR 100 total.

**Computation:**
```
Disposal proceeds:  EUR 45,000
Cost basis:         EUR 25,000 + EUR 100 fees = EUR 25,100
Gain:               EUR 19,900
Classification:     Trading income (frequent trader)
Tax:                Ordinary income at progressive rates
```
If single, no other income: tax on EUR 19,900 = EUR 0 (first 9,100) + EUR 810 (9,101-14,500 @ 15%) + EUR 1,350 (14,501-19,500 @ 25%) + EUR 100 (19,501-19,900 @ 25%) = EUR 2,260.

### Example 2 -- Investor, Coins, Not Taxable

**Input:** Malta-domiciled resident. Bought 2 ETH at EUR 1,500 each in 2021. Sold 2 ETH at EUR 3,500 each in 2025. Total 3 trades in 4 years. Employed full-time separately.

**Computation:**
```
Gain: (EUR 3,500 - EUR 1,500) × 2 = EUR 4,000
Classification: Investment (infrequent, long hold, employed elsewhere)
Tax: NOT taxable — coins held as investment are outside CGT scope
```
Flag for reviewer: confirm investment classification based on full trading history.

### Example 3 -- Non-Dom, Foreign Exchange, Not Remitted

**Input:** Malta-resident, non-domiciled individual. Traded crypto on Binance (non-Malta platform). EUR 30,000 gain. Proceeds remain on Binance, not transferred to Malta bank.

**Computation:**
```
Gain: EUR 30,000
Source: Foreign (traded on foreign platform)
Remitted to Malta: No
Tax: NOT taxable (remittance basis — foreign gains not remitted)
Minimum tax: EUR 5,000 still applies regardless
```

### Example 4 -- Staking Income

**Input:** Malta-domiciled resident. Staked ETH via Coinbase. Received 0.5 ETH in staking rewards over 2025. Market value at receipt: EUR 1,750 total.

**Computation:**
```
Staking income: EUR 1,750 (market value at each receipt date)
Classification: Other income (income at receipt)
Tax: Taxable at progressive rates, added to other income
Cost basis of staked ETH received: EUR 1,750 (for future disposal)
```

## Section 9 -- Edge Cases

### 9.1 Hard Forks

When a blockchain forks and the holder receives new coins (e.g. BTC → BCH), the CfR has not issued specific guidance. Conservative treatment:
- Cost basis of original coin: unchanged
- Cost basis of forked coin: EUR 0 (no acquisition cost)
- If sold: full proceeds are gain; classify as trading or investment per normal rules

### 9.2 DeFi Lending / Liquidity Providing

- Interest received from lending (e.g. Aave, Compound): taxable as income at market value when received
- Liquidity provision (e.g. Uniswap): adding to a pool may constitute a disposal; LP tokens received have a new cost basis
- Impermanent loss: not currently a recognised deductible loss under CfR guidance
- Flag for reviewer — DeFi treatment is evolving

### 9.3 NFTs

- Purchase of NFT: acquisition cost for future disposal
- Sale of NFT: disposal — gain taxed as trading income or not taxable depending on frequency
- Creation and sale of NFT (artist/creator): business income
- VAT: electronically supplied service — 18% VAT may apply on B2C sales to EU customers

## PROHIBITIONS

- NEVER assume all crypto gains are tax-free in Malta — trading profits are taxable as ordinary income
- NEVER classify coins as securities — they fall outside Article 5 CGT
- NEVER ignore the trading vs investment distinction — it determines taxability
- NEVER forget the non-dom remittance basis — it can eliminate Malta tax on unrepatriated foreign gains
- NEVER treat transfers between own wallets as disposals
- NEVER compute gains without verified cost basis and FIFO records
- NEVER advise on MFSA regulatory licensing — this skill covers tax only
- NEVER ignore DAC8 reporting obligations from 2026
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
