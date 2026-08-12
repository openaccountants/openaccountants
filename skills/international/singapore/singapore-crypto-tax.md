---
name: singapore-crypto-tax
description: Use this skill whenever asked about Singapore cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Singapore", "Bitcoin Singapore", "digital tokens Singapore", "cryptocurrency gains Singapore", "IRAS crypto", "GST crypto Singapore", "staking Singapore", "mining income Singapore", "NFT tax Singapore", "Coinbase Singapore", "Binance Singapore", "payment tokens", "digital payment tokens", "capital gains Singapore crypto", "crypto business income Singapore", or any question about the income tax, GST, or reporting obligations for cryptocurrency, tokens, or digital assets for Singapore tax residents or Singapore-source crypto income. Covers IRAS e-Tax Guide on Digital Tokens (income tax and GST), trader vs investor distinction, badges of trade, and GST exemption for digital payment tokens. ALWAYS read this skill before touching any Singapore crypto work.
version: 1.0
jurisdiction: SG
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - singapore-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Singapore Crypto Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Singapore (Republic of Singapore) |
| Tax | Income Tax (no capital gains tax) |
| Currency | SGD (values must be converted to SGD at transaction date) |
| Tax year | Preceding year basis — income earned 1 Jan -- 31 Dec 2024 is assessed in Year of Assessment (YA) 2025 |
| Primary authority | IRAS e-Tax Guide: Income Tax Treatment of Digital Tokens (9 October 2020) |
| GST authority | IRAS e-Tax Guide: GST — Digital Payment Tokens (17 November 2019, effective 1 January 2020) |
| Tax authority | Inland Revenue Authority of Singapore (IRAS) |
| Filing portal | myTax Portal (mytax.iras.gov.sg) |
| Filing deadline | 15 April (paper) / 18 April (e-filing) of the YA |
| Corporate tax rate | Flat 17% on chargeable income |
| Top personal rate | 24% (on income above S$1,000,000, from YA 2024) |
| Capital gains tax | **None** — Singapore does not impose capital gains tax |
| Validated by | Pending — requires sign-off by a Singapore-accredited tax agent |
| Skill version | 1.0 |

### Key Principle

Singapore has **no capital gains tax**. Gains from disposal of crypto assets held as **long-term investments** are capital in nature and **not taxable**. However, if crypto activities constitute a **trade or business**, profits are taxable as ordinary **income** under the Income Tax Act 1947 (ITA).

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether trading or investment | Assess against badges of trade; if unclear, treat as potentially taxable (trading) and seek IRAS ruling |
| Unknown token classification | Treat as payment token (most common) |
| Unknown cost basis | STOP — cannot compute gain without acquisition cost |
| Unknown residency | STOP — affects Singapore-source income determination |
| Unknown whether mining is hobby or business | Companies → presumed business; individuals → evaluate frequency and scale |

## Section 2 -- Classification Rules

### 2.1 IRAS Digital Token Classification

**IRAS Digital Token Classification**  _(IRAS e-Tax Guide (October 2020))_

| Token Type | Definition | Examples | Tax Treatment on Disposal |
| --- | --- | --- | --- |
| **Payment tokens** | Tokens that function or are intended to function as a medium of exchange | BTC, ETH, LTC, XRP, SOL, stablecoins (USDT, USDC) | Capital gain (not taxable) if investment; income if trading business |
| **Utility tokens** | Tokens that provide access to a current or prospective product/service on a DLT platform | Filecoin (FIL), BAT, service access tokens | Capital gain (not taxable) if investment; income if trading business |
| **Security tokens** | Tokens that represent ownership rights (equity, debt, units in a fund) | Tokenised shares, tokenised bonds, fund tokens | May attract withholding tax if dividend-like distributions; capital gain (not taxable) if investment disposal |

IRAS classifies digital tokens into three categories for tax purposes (per the e-Tax Guide, October 2020):

### 2.2 Taxable vs Non-Taxable Events

**Taxable vs Non-Taxable Events**

| Event | Taxable? | Condition |
| --- | --- | --- |
| Disposal of crypto investment (capital gain) | **No** | Held as long-term investment; no capital gains tax in Singapore |
| Disposal of crypto trading stock (revenue gain) | **Yes** | Part of a trading business; taxed as income |
| Receiving crypto as payment for goods/services | **Yes** | Revenue of the business at FMV when received |
| Mining rewards (company) | **Yes** | Presumed business income for companies |
| Mining rewards (individual, habitual) | **Yes** | If habitual and systematic → vocation income |
| Mining rewards (individual, hobby) | **No** | Prima facie hobby; capital gain on disposal not taxable |
| Staking / DeFi yields (business) | **Yes** | Business income at FMV when received |
| Staking / DeFi yields (individual, occasional) | **No** | Capital in nature if not part of a business |
| Airdrop (no service provided) | **No** | Windfall gain; not taxable; cost basis = S$0 |
| Airdrop (in exchange for a service) | **Yes** | Income at FMV when received |
| Crypto-to-crypto swap (investor) | **No** | Capital transaction; no CGT |
| Crypto-to-crypto swap (trader) | **Yes** | Revenue transaction; gain/loss is taxable |
| Transfer between own wallets | **No** | No change in beneficial ownership |

## Section 3 -- Rate Tables

### 3.1 Personal Income Tax Rates (YA 2025, Resident Individuals)

**Personal Income Tax Rates (YA 2025, Resident Individuals)**  _(IRAS, Individual Income Tax rates, effective from YA 2024 onwards.)_

| Chargeable Income (S$) | Rate | Cumulative Tax (S$) |
| --- | --- | --- |
| First 20,000 | 0% | 0 |
| Next 10,000 | 2% | 200 |
| Next 10,000 | 3.5% | 550 |
| Next 40,000 | 7% | 3,350 |
| Next 40,000 | 11.5% | 7,950 |
| Next 40,000 | 15% | 13,950 |
| Next 40,000 | 18% | 21,150 |
| Next 40,000 | 19% | 28,750 |
| Next 40,000 | 19.5% | 36,550 |
| Next 40,000 | 20% | 44,550 |
| Next 180,000 | 22% | 84,150 |
| Next 500,000 | 23% | 199,150 |
| Above 1,000,000 | 24% | — |

- **YA 2025 rebate** — 60% personal income tax rebate, capped at S$200  _(IRAS, Individual Income Tax rates, effective from YA 2024 onwards.)_

### 3.2 Corporate Income Tax Rate

**Corporate Income Tax Rate**  _(Income Tax Act 1947 (ITA), Section 43; IRAS corporate tax guide.)_

| Parameter | Value |
| --- | --- |
| Headline rate | 17% |
| First S$10,000 chargeable income | 75% exemption → effective 4.25% |
| Next S$190,000 chargeable income | 50% exemption → effective 8.5% |

### 3.3 Non-Resident Rates

**Non-Resident Rates**

| Income Type | Rate |
| --- | --- |
| Employment income | Higher of 15% flat or progressive resident rates |
| Director's fees / consultant fees | 24% flat (from YA 2024) |
| Business income (PE in Singapore) | 17% corporate rate or progressive personal rates |

## Section 4 -- Cost Basis Methods

### 4.1 Accepted Methods

**Accepted Methods**

| Method | Status | Notes |
| --- | --- | --- |
| Specific identification | Acceptable | Must be clearly documented |
| FIFO (First In, First Out) | Acceptable | Commonly used; IRAS does not mandate a specific method |
| Weighted average cost | Acceptable | Particularly for fungible tokens traded in volume |
| LIFO | Not commonly used | Not prohibited but may be questioned |

- **Consistent application** — Once a method is chosen, apply it consistently across the tax year and across years.

### 4.2 Cost Basis Components

- Purchase price in SGD (convert foreign currency at exchange rate on acquisition date)
- Exchange/trading fees and commissions on acquisition
- Network/gas fees directly attributable to the acquisition
- Any other directly incurred acquisition costs

### 4.3 For Businesses (Revenue Assets)

- Cost basis = purchase price + incidental acquisition costs
- Standard accounting principles (FRS 102 / SFRS(I)) apply
- Inventory valuation: lower of cost or net realisable value at year-end

## Section 5 -- DeFi, Staking, Mining, and Airdrops

### 5.1 Mining

**Mining**  _(IRAS e-Tax Guide (Digital Tokens, paras 3.1--3.5))_

| Scenario | Tax Treatment |
| --- | --- |
| Company mining | Business income — taxed at point of **disposal**, not at mining receipt. Company can claim mining expenses (electricity, hardware, etc.) as deductions. |
| Individual mining (habitual, systematic) | Vocation income — profits from sale of mined tokens are taxable |
| Individual mining (hobby) | Not taxable — gains on sale are capital gains (no CGT) |

- **Key nuance** — For miners, IRAS taxes at the point of disposal, not at receipt. The miner holds the token at cost (incurred mining costs) until sold.  _(IRAS e-Tax Guide (Digital Tokens, paras 3.1--3.5))_

### 5.2 Staking and DeFi

**Staking and DeFi**

| Activity | Business Context | Tax Treatment |
| --- | --- | --- |
| Staking rewards | Part of business operations | Business income at FMV when received; or at disposal depending on accounting |
| Staking rewards | Individual, passive | Likely capital in nature; not taxable |
| DeFi lending interest | Business | Taxable income |
| DeFi lending interest | Individual, passive | Likely capital; not taxable (but grey area — conservative: taxable) |
| Liquidity provision | Business | Revenue activity; gains taxable |
| Liquidity provision | Individual | Capital activity if passive; no specific IRAS guidance |
| Yield farming | Business | Taxable income at FMV |

### 5.3 Airdrops and Hard Forks

**Airdrops and Hard Forks**

| Event | Tax Treatment |
| --- | --- |
| Airdrop (no consideration given) | Not income; cost basis = S$0; gain on disposal is capital (not taxable for investors) |
| Airdrop (in return for service, e.g. referral) | Taxable income at FMV |
| Hard fork (new coin received) | Not a taxable event; cost basis of new coin = S$0; original coin cost basis unchanged |

## Section 6 -- NFT Treatment

**NFT Treatment**

| Scenario | Treatment |
| --- | --- |
| Purchase of NFT | Acquisition at cost — cost basis for future disposal |
| Sale of NFT (investor) | Capital gain — not taxable (no CGT) |
| Sale of NFT (trader/business) | Taxable business income |
| Creation and sale of NFT (artist/creator) | Business income if habitual; hobby income if occasional |
| NFT → NFT swap (investor) | Capital transaction — not taxable |
| NFT → NFT swap (trader) | Revenue transaction — taxable |
| NFT royalties | Income when received; taxable if part of business or vocation |
| GST on NFT sales | If NFT is not a digital payment token → standard GST rules may apply (9% from 1 January 2024) |

## Section 7 -- Reporting Requirements

### 7.1 Badges of Trade (Trader vs Investor Determination)

**Badges of Trade (Trader vs Investor Determination)**

| Badge | Indicates Trading | Indicates Investment |
| --- | --- | --- |
| Subject matter | Commodities or items typically traded | Assets typically held for long-term appreciation |
| Frequency of transactions | High volume, repeated transactions | Infrequent, isolated transactions |
| Holding period | Short (days to weeks) | Long (months to years) |
| Supplementary work | Value-added activities (market making, arbitrage) | No additional work beyond buy-and-hold |
| Circumstances of sale | Systematic selling pattern | Sold only when needed or at opportune time |
| Motive/intention | Profit from short-term price movements | Long-term capital appreciation |
| Financing | Borrowed funds to trade | Own savings |
| Organisation | Business-like structure, dedicated accounts | Casual, alongside primary employment |

IRAS applies the common law "badges of trade" to distinguish trading (taxable) from investment (not taxable):

### 7.2 Filing Forms

**Filing Forms**

| Form | Who Files | Deadline |
| --- | --- | --- |
| Form B (individuals with self-employment / business income) | Individuals with crypto trading business income | 15 April (paper) / 18 April (e-filing) |
| Form B1 (individuals with employment income only) | Individuals with crypto employment payment only | 15 April (paper) / 18 April (e-filing) |
| Form C-S / Form C (companies) | Companies with crypto business income | 30 November of YA |
| ECI (Estimated Chargeable Income) | Companies | Within 3 months of financial year-end |

### 7.3 GST Reporting

**GST Reporting**  _(IRAS e-Tax Guide: GST — Digital Payment Tokens (effective 1 January 2020))_

| Transaction | GST Treatment |
| --- | --- |
| Exchange of digital payment tokens for fiat (or vice versa) | **Exempt supply** (no GST) |
| Exchange of digital payment tokens for other digital payment tokens | **Exempt supply** |
| Use of digital payment tokens to pay for goods/services | GST on the goods/services; **not** on the token itself |
| ICO (issuance of payment tokens) | **Exempt supply** |
| Supply of utility tokens | Depends on underlying supply — may be standard-rated (9%) or exempt |
| Mining services (identifiable recipient) | Standard-rated supply (9%) |
| NFT sale | Not a digital payment token — standard GST rules apply |

- **GST registration threshold** — S$1 million in taxable supplies in past 12 months (or expected next 12 months). Exempt supplies (including payment token exchanges) count towards the threshold for registration purposes.  _(IRAS e-Tax Guide: GST — Digital Payment Tokens (effective 1 January 2020))_

### 7.4 No FBAR Equivalent

Singapore does not have an FBAR-like foreign asset reporting obligation for individuals. However:
- Businesses holding significant crypto may have reporting obligations under MAS (Monetary Authority of Singapore) regulations
- Licensed payment service providers under the Payment Services Act 2019 have AML/CFT reporting requirements

## Section 8 -- Loss Offset and Carry-Forward

**Loss Offset and Carry-Forward**

| Rule | Detail |
| --- | --- |
| Trading losses | Can offset against other income in the same YA (Section 37 ITA) |
| Carry-forward of unabsorbed losses | Indefinite carry-forward, subject to shareholding test (Section 37 ITA) |
| Carry-back | Up to 3 preceding YAs, capped at S$100,000 per YA (Section 37E ITA) — for companies only |
| Capital losses | Not deductible — there is no capital gains tax regime to offset against |
| Investment losses (individual) | Not deductible — capital in nature |

## Section 9 -- Anti-Avoidance Rules

**Anti-Avoidance Rules**

| Rule | Description |
| --- | --- |
| General anti-avoidance (Section 33 ITA) | IRAS can disregard or vary any arrangement that has the purpose of tax avoidance |
| Transfer pricing (Section 34D ITA) | Arm's length standard applies to related-party crypto transactions |
| Substance over form | IRAS may recharacterise transactions based on economic substance |
| Recharacterisation of capital as revenue | If IRAS determines activity is trading despite taxpayer's claim of investment, gains become taxable |
| MAS compliance | Unlicensed crypto activities may attract regulatory scrutiny and affect tax positions |

## Section 10 -- Worked Examples

### Example 1 -- Long-Term Investor (Not Taxable)

**Input:** Singapore tax resident individual. Employed full-time as a software engineer. Bought 2 BTC at S$40,000 each in 2022. Sold 2 BTC at S$75,000 each in 2024. Total 2 transactions in 2 years. Used personal savings.

**Analysis:**
```
Proceeds:           2 × S$75,000 = S$150,000
Cost basis:         2 × S$40,000 = S$80,000
Gain:               S$70,000

Badges of trade assessment:
  Frequency:        Low (1 buy, 1 sell over 2 years)
  Holding period:   Long (~2 years)
  Motive:           Long-term appreciation
  Financing:        Own savings
  Organisation:     Casual, alongside employment

Classification:     INVESTMENT (capital gain)
Tax:                NOT TAXABLE — no capital gains tax in Singapore
```

**Reporting:** No reporting required for YA 2025 (income earned 2024). Gain is capital in nature.

### Example 2 -- Active Trader (Taxable)

**Input:** Singapore tax resident individual. No other employment. Traded crypto full-time on Binance in 2024. Made 500+ trades, average holding period 3 days. Used leverage. Total revenue: S$200,000 from cost basis of S$120,000. Net trading gain: S$80,000.

**Analysis:**
```
Revenue:            S$200,000
Cost of tokens:     S$120,000
Net gain:           S$80,000

Badges of trade assessment:
  Frequency:        Very high (500+ trades)
  Holding period:   Very short (3 days average)
  Motive:           Short-term profit
  Financing:        Used leverage
  Organisation:     Full-time, sole activity

Classification:     TRADING (business income)
Tax computation:    Chargeable income S$80,000
  First S$20,000 @ 0%    = S$0
  Next S$10,000 @ 2%     = S$200
  Next S$10,000 @ 3.5%   = S$350
  Next S$40,000 @ 7%     = S$2,800
  Total tax:              = S$3,350
  Less YA 2025 rebate (60%, max S$200): -S$200
  Net tax payable:        = S$3,150
```

**Reporting:** File Form B by 18 April 2025. Declare as trade/business income.

### Example 3 -- Company Mining Operation

**Input:** Singapore-incorporated company. Mines ETH using dedicated hardware. Revenue in 2024: 50 ETH sold at average S$4,000 each = S$200,000. Mining costs (electricity, hardware depreciation, hosting): S$80,000.

**Analysis:**
```
Revenue:            S$200,000
Expenses:           S$80,000
Chargeable income:  S$120,000

Corporate tax (17%):
  First S$10,000:   75% exempt → taxable S$2,500 @ 17% = S$425
  Next S$110,000:   → S$190,000 bracket, 50% exempt → taxable S$55,000 @ 17% = S$9,350
  Total tax:        S$9,775
```

**Reporting:** File ECI within 3 months of year-end. File Form C-S/C by 30 November 2025.

## Self-Checks

Before finalising any Singapore crypto tax computation:

- [ ] Assessed badges of trade to determine capital vs revenue nature
- [ ] Confirmed Singapore tax residency status
- [ ] Verified whether individual or corporate taxpayer
- [ ] For companies: confirmed whether mining/trading income is Singapore-sourced
- [ ] Applied correct cost basis method consistently
- [ ] GST implications assessed (digital payment token exemption vs standard supply)
- [ ] Ensured no double-counting of exempt supply in GST returns
- [ ] Trading losses properly offset or carried forward
- [ ] YA 2025 personal income tax rebate applied where applicable

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an IRAS-accredited tax agent, Singapore chartered accountant, or equivalent licensed practitioner) before filing or acting upon.

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
