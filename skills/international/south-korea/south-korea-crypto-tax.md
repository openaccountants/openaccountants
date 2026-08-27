---
name: south-korea-crypto-tax
description: Use this skill whenever asked about South Korea cryptocurrency or virtual asset taxation. Trigger on phrases like "crypto tax Korea", "Bitcoin Korea tax", "가상자산 과세", "virtual asset tax Korea", "cryptocurrency gains Korea", "crypto income Korea", "Upbit tax", "Bithumb tax", "staking Korea", "mining income Korea", "NFT tax Korea", "NTS crypto", "종합소득세 crypto", "Korean crypto regulation", "virtual asset users protection act", or any question about the income tax treatment of cryptocurrency, tokens, or digital assets for Korean tax residents. Covers the Income Tax Act provisions on virtual asset income, NTS reporting requirements, exchange obligations, cost basis rules, and CARF implementation. ALWAYS read this skill before touching any South Korea crypto work.
version: 1.0
jurisdiction: KR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Yeong Min Lee
review_status: current
depends_on:
  - south-korea-income-tax
category: crypto
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# South Korea Crypto Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Korea (대한민국) |
| Tax | Income Tax on Virtual Asset Income (가상자산소득세) |
| Currency | KRW (₩) — all values must be in KRW at transaction date |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary authority | Income Tax Act (소득세법), as amended by Act No. 17757 (Dec 2020), further amended Dec 2022 and Dec 2024 |
| Supporting legislation | Virtual Asset Users Protection Act (가상자산이용자보호법, effective Jul 2024); Enforcement Decree of the Income Tax Act |
| Tax authority | National Tax Service (국세청, NTS) |
| Filing portal | HomeTax (hometax.go.kr) |
| Filing deadline | May 1–31 of the following year (종합소득세 신고) |
| International reporting | CARF (Crypto-Asset Reporting Framework) — Korea begins receiving exchange data 2027; US joins CARF 2029 |
| Validated by | Pending — requires sign-off by a Korean licensed tax accountant (세무사) |
| Skill version | 1.0 |

### CRITICAL STATUS NOTE — Tax Year 2025

**Virtual asset income tax is NOT in effect for 2025.** The tax was originally legislated in December 2020 for a January 2022 start, but has been postponed three times:
- 2022 → deferred to 2023
- 2023 → deferred to 2025
- 2025 → deferred to **1 January 2027**

As of May 2026, the Ministry of Economy and Finance has officially confirmed that the tax **will proceed as scheduled from 1 January 2027**, rejecting further postponement. The NTS is actively coordinating with the five major exchanges (Upbit/Dunamu, Bithumb, Coinone, Korbit, Gopax) to build the filing and reporting infrastructure.

**For tax year 2025: crypto gains are NOT taxable as virtual asset income.** This skill documents the framework that will apply from 2027 onwards, plus the rules that currently apply (gift tax, foreign asset reporting).

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Whether tax is in effect for a given year | Check implementation date — NOT in effect before 1 January 2027 |
| Unknown cost basis method | Use moving average for exchange transactions, FIFO for all others |
| Unknown whether gains exceed ₩2.5M threshold | Compute precisely — do not estimate |
| Pre-2027 holdings cost basis | Use higher of market price on 31 December 2026 or actual acquisition cost |
| Unknown residency status | STOP — Korean tax obligations depend on residency |
| Gift of crypto between related parties | Treat as subject to gift tax NOW (gift tax applies regardless of income tax deferral) |

## Section 2 -- Classification Rules

### 2.1 Legal Classification

- **Virtual asset (가상자산)** — Electronically tradable digital representation of economic value; excludes e-money, prepaid means, securities, and in-game items  _(VAUPA Art. 2)_
- **Virtual asset income (가상자산소득)** — Income from transfer or lending of virtual assets  _(Income Tax Act Art. 21(1)(27))_
- **Classification for tax** — "Other income" (기타소득)  _(Income Tax Act Art. 21)_

### 2.2 Taxable Events (from 2027)

**Taxable Events (from 2027)**

| Event | Tax Treatment |
| --- | --- |
| Sale of crypto for KRW/fiat | Taxable — transfer of virtual asset |
| Crypto-to-crypto exchange | Taxable — transfer; value determined by exchange ratio × underlying asset value |
| Lending crypto and receiving interest | Taxable — lending income |
| Mining rewards | Treatment remains ambiguous; NTS guidance pending; likely "other income" or business income depending on scale |
| Staking rewards | Treatment remains ambiguous; NTS guidance pending; likely taxable as income |
| Airdrops | Unclear; NTS has not issued specific guidance; conservative: taxable at FMV |
| Payment for goods/services with crypto | Taxable — transfer of virtual asset (disposal at FMV) |
| Transfer between own wallets | NOT taxable — no transfer of economic ownership |
| Gift of crypto | NOT virtual asset income tax — but subject to GIFT TAX (see Section 9) |

### 2.3 Current Status (Pre-2027)

**Current Status (Pre-2027)**

| Tax Type | Applies to Crypto Now? | Notes |
| --- | --- | --- |
| Virtual asset income tax (22%) | **NO** — deferred to 2027 | No filing obligation for crypto gains in 2025 or 2026 |
| Gift tax (증여세) | **YES** — applies now | Crypto gifts between related parties are subject to gift tax at 10%–50% |
| Inheritance tax (상속세) | **YES** — applies now | Crypto held at death is part of the estate |
| Foreign asset reporting | **YES** — applies now | Overseas financial accounts > ₩500M must be reported |
| Corporate income tax | **YES** | Corporations already pay corporate tax on crypto investment gains |

## Section 3 -- Rate Tables

### 3.1 Virtual Asset Income Tax (from 1 January 2027)

**Virtual Asset Income Tax (from 1 January 2027)**

| Component | Rate |
| --- | --- |
| National other income tax | 20% |
| Local income tax (지방소득세) | 2% (10% surtax on national tax) |
| **Combined effective rate** | **22%** |
| Annual basic deduction | ₩2,500,000 (approx. USD 1,800) |

- **Virtual asset income tax formula** — Taxable income = (Total gains from transfers + lending income) − (Total necessary expenses) − ₩2,500,000 Tax = Taxable income × 22%  _(Income Tax Act Art. 21(1)(27), Art. 64(1); Enforcement Decree Art. 41(13).)_
- **Flat-rate separate taxation** — This is a flat-rate separate taxation — virtual asset income is NOT aggregated with other income types for progressive rate purposes.  _(Income Tax Act Art. 21(1)(27), Art. 64(1); Enforcement Decree Art. 41(13).)_

### 3.2 Gift Tax Rates (Applies NOW)

**Gift Tax Rates (Applies NOW)**  _(Inheritance and Gift Tax Act Arts. 26, 53.)_

| Taxable Amount (₩) | Rate | Cumulative Deduction |
| --- | --- | --- |
| Up to 100M | 10% | — |
| 100M – 500M | 20% | ₩10M |
| 500M – 1B | 30% | ₩60M |
| 1B – 3B | 40% | ₩160M |
| Over 3B | 50% | ₩460M |

- **Gift tax exemptions for crypto** — Gift tax exemptions for crypto: ₩50M from spouse, ₩50M from lineal ascendants (adult children), ₩20M from other relatives over 10-year aggregation periods.  _(Inheritance and Gift Tax Act Arts. 26, 53.)_

### 3.3 Korean Progressive Income Tax Rates (for reference — mining/business income)

**Korean Progressive Income Tax Rates**

| Taxable Income (₩) | Rate | Cumulative Deduction |
| --- | --- | --- |
| Up to 14M | 6% | — |
| 14M – 50M | 15% | ₩1.26M |
| 50M – 88M | 24% | ₩5.76M |
| 88M – 150M | 35% | ₩15.44M |
| 150M – 300M | 38% | ₩19.94M |
| 300M – 500M | 40% | ₩25.94M |
| 500M – 1B | 42% | ₩35.94M |
| Over 1B | 45% | ₩65.94M |

- **Local income tax surtax** — Plus 10% local income tax surtax on each bracket.

## Section 4 -- Cost Basis Methods

### 4.1 Acquisition Cost Rules

**Acquisition Cost Rules**  _(Enforcement Decree Art. 89)_

| Transaction Type | Valuation Method | Authority |
| --- | --- | --- |
| Exchange transactions (via registered exchange) | **Moving average method** (이동평균법) | Enforcement Decree Art. 89 |
| All other transactions (P2P, DeFi, OTC) | **FIFO (First In, First Out)** (선입선출법) | Enforcement Decree Art. 89 |

- **Consistency requirement** — Once a method is applied by transaction type, it must be consistently maintained.  _(Enforcement Decree Art. 89)_

### 4.2 Deemed Acquisition Cost (Transitional Rule)

- **Deemed acquisition cost formula** — Deemed acquisition cost = MAX(market price on 31 December 2026, actual acquisition cost)

For virtual assets held **before** the tax takes effect (i.e., acquired before 1 January 2027):

This protects existing holders from being taxed on pre-implementation gains. The market price will be determined by reference to exchange closing prices on 31 December 2026.

### 4.3 Necessary Expenses (Deductible Costs)

**Necessary Expenses (Deductible Costs)**

| Expense | Deductible? |
| --- | --- |
| Acquisition cost (purchase price) | Yes |
| Exchange/trading fees on acquisition | Yes |
| Exchange/trading fees on disposal | Yes |
| Network/gas fees | Yes — if directly attributable |
| Transfer fees between wallets | Generally no — not a disposal |
| Hardware wallet cost | No — personal expense |

### 4.4 Unverifiable Cost Basis

- **Unverifiable cost basis ceiling** — If the actual acquisition cost cannot be verified, the taxpayer may claim up to **50% of the transfer (sale) price** as necessary expenses. This is a ceiling, not an entitlement — the NTS may challenge claimed amounts.

## Section 5 -- DeFi / Staking / Mining / Airdrop Treatment

> **WARNING:** The NTS has NOT issued detailed guidance on DeFi, staking, mining, or airdrops as of May 2026. The tax authorities have acknowledged these are "ambiguous criteria for taxing new income types." The following represents conservative interpretations based on the statutory framework.

### 5.1 Mining

**Mining**

| Aspect | Treatment |
| --- | --- |
| Occasional/hobby mining | Likely "other income" (기타소득) at progressive rates when virtual asset income tax takes effect |
| Commercial-scale mining | Business income (사업소득) at progressive rates — applies now for corporations |
| Valuation | Market value at time of receipt |
| Cost basis of mined coins | Market value at receipt (for future disposal calculations) |

### 5.2 Staking

**Staking**

| Aspect | Treatment |
| --- | --- |
| Staking rewards received | Likely taxable as income at FMV when received (once 2027 framework applies) |
| Cost basis of staked rewards | FMV at receipt date |
| Staking-as-a-service | Lending income — taxable at 22% |
| Loss of staked assets (slashing) | Treatment unclear; likely not deductible absent NTS guidance |

### 5.3 Airdrops

**Airdrops**

| Aspect | Treatment |
| --- | --- |
| Airdrop from existing holding (fork-based) | Cost basis of ₩0; taxable on disposal |
| Promotional/gratuitous airdrop | Potentially taxable at FMV on receipt — NTS guidance pending |
| Airdrop in exchange for a service | Income at FMV |

### 5.4 DeFi Lending and Liquidity Provision

**DeFi Lending and Liquidity Provision**

| Activity | Treatment |
| --- | --- |
| DeFi lending interest | Lending income — taxable at 22% under virtual asset framework |
| Liquidity provision (LP) | Adding to pool may constitute transfer — LP token received has new cost basis |
| Yield farming rewards | Likely income at FMV |
| Impermanent loss | Not addressed by NTS; likely NOT deductible |

## Section 6 -- NFT Treatment

**NFT Treatment**  _(VAUPA Art. 2(3) exclusions; NTS classification criteria pending.)_

| Aspect | Treatment |
| --- | --- |
| NFTs generally | Excluded from virtual asset definition under VAUPA if they cannot be divided, used as payment, or exchanged for other virtual assets on a marketplace |
| Fungible or tradeable NFTs | May be classified as virtual assets — case-by-case |
| NFT sale profit (if classified as virtual asset) | Taxable at 22% under virtual asset income framework (from 2027) |
| NFT creation and sale (artist/creator) | Business income — taxed at progressive rates |
| NFT art collection (non-tradeable) | May fall outside the virtual asset tax scope |
| Gaming NFTs | Excluded if they meet the in-game item exception |

NFT taxation in Korea is partially carved out:

## Section 7 -- Reporting Requirements

### 7.1 Individual Filing (from 2027 income onwards)

**Individual Filing (from 2027 income onwards)**

| Requirement | Detail |
| --- | --- |
| Return type | 종합소득세 신고 (Comprehensive Income Tax Return) |
| Filing period | 1–31 May of following year (first filing: May 2028 for 2027 income) |
| Filing portal | HomeTax (hometax.go.kr) |
| Payment deadline | 31 May (same as filing) |
| Estimated/provisional payments | Not required for virtual asset income |

### 7.2 Exchange Reporting Obligations

**Exchange Reporting Obligations**

| Requirement | Detail |
| --- | --- |
| Domestic exchanges (Upbit, Bithumb, etc.) | Must report user transaction data to NTS |
| Data submission deadline | By end of January of the filing year (tentative: January 2028 for 2027 data) |
| Data collected | Transaction history, gains/losses, user identification |
| Customer self-certification | Since 1 January 2026, top 5 exchanges collect CARF self-certification forms for overseas tax obligations |

### 7.3 Foreign Asset Reporting (Applies NOW)

**Foreign Asset Reporting (Applies NOW)**

| Requirement | Detail |
| --- | --- |
| Overseas financial account reporting | If total balance of all overseas financial accounts exceeds ₩500M at any point during the year, must file report |
| Includes crypto on foreign exchanges | Yes — crypto held on Binance, Bybit, etc. counts toward ₩500M threshold |
| Filing deadline | June of the following year |
| Penalty for non-reporting | Up to 20% of unreported amount |
| CARF data sharing | Korea begins receiving data from CARF-signatory countries in 2027; US joins 2029 |

### 7.4 Record-Keeping

**Record-Keeping**

| Requirement | Detail |
| --- | --- |
| Retention period | 5 years from filing deadline |
| Records to maintain | Full transaction logs, exchange records, wallet addresses, cost basis calculations, lending records |
| Burden of proof | On the taxpayer for claimed deductions and cost basis |

## Section 8 -- Loss Offset and Carry-Forward

### 8.1 Loss Offset Rules (from 2027)

**Loss Offset Rules (from 2027)**

| Rule | Detail |
| --- | --- |
| Netting within year | Gains and losses from virtual asset transactions are netted within the calendar year |
| Cross-asset netting | Losses on one virtual asset can offset gains on another within the same year |
| Basic deduction | ₩2,500,000 applied after netting |
| Loss carry-forward | **NOT permitted** — losses cannot be carried to future years |
| Loss carry-back | NOT permitted |

### 8.2 Key Limitation

- **No loss carry-forward for virtual asset income** — South Korea does **not** allow loss carry-forward for virtual asset income. If an investor loses ₩4.4M in 2027 and gains ₩4.4M in 2028, they owe ₩418,000 tax in 2028 (after ₩2.5M deduction) despite being net flat over two years. The Ministry of Economy and Finance has stated this aligns with the treatment of domestic stock investment income, which also does not allow loss carry-forward.  _(Income Tax Act Art. 21; confirmed by Ministry of Economy and Finance at May 2026 National Assembly forum.)_

## Section 9 -- Anti-Avoidance Rules

### 9.1 Gift Tax on Crypto Transfers (IN EFFECT NOW)

**Gift Tax on Crypto Transfers (IN EFFECT NOW)**

| Rule | Detail |
| --- | --- |
| Applies | Gift of virtual assets between related parties |
| Effective | NOW — regardless of virtual asset income tax deferral |
| Valuation | Average of daily closing prices on registered exchanges for 1 month before and 1 month after the gift date |
| Rates | 10%–50% progressive (see Section 3.2) |
| Exemptions | Spouse: ₩600M (lifetime); Lineal ascendants/descendants: ₩50M (adults), ₩20M (minors) per 10 years |
| NTS enforcement | NTS has actively investigated crypto gift tax evasion |

This is the most important current anti-avoidance provision:

### 9.2 Wash Sale Rules

- **Wash sale rules** — No specific wash sale rule has been enacted for virtual assets. However, the NTS may invoke general anti-avoidance provisions if transactions lack economic substance.

### 9.3 Overseas Exchange Enforcement

**Overseas Exchange Enforcement**

| Measure | Detail |
| --- | --- |
| CARF | Korea joins CARF; exchanges data with signatory countries from 2027 |
| US gap | US does not join CARF until 2029 — enforcement gap for US-based exchange transactions in 2027–2028 |
| Statute of limitations | 10 years — NTS can retroactively assess 2027–2028 income once US data is available |
| Deliberate non-reporting | NTS acknowledges tracking difficulty for hidden wallets; penalties apply for intentional evasion |

### 9.4 Corporate vs Individual Disparity

- **Corporate vs individual disparity rationale** — Corporations already pay corporate income tax on virtual asset gains. The government has stated that exempting individuals while taxing corporations would be unfair — this is a key rationale for proceeding with the 2027 implementation.

## Section 10 -- Worked Examples

### Example 1 -- Basic Trading Gain (2027 Scenario)

**Input:** Korean tax resident. Bought 1 BTC on Upbit at ₩40,000,000 in February 2027. Sold 1 BTC on Upbit at ₩55,000,000 in August 2027. Exchange fees: ₩150,000 total.

**Computation:**
```
Disposal proceeds:    ₩55,000,000
Cost basis (moving avg): ₩40,000,000 + ₩150,000 fees = ₩40,150,000
Gain:                 ₩14,850,000
Basic deduction:      ₩2,500,000
Taxable income:       ₩12,350,000
Tax (22%):            ₩2,717,000
  - National (20%):   ₩2,470,000
  - Local (2%):       ₩247,000
```

Filed via 종합소득세 신고 on HomeTax by 31 May 2028.

### Example 2 -- Pre-2027 Holdings with Deemed Cost Basis

**Input:** Korean tax resident. Bought 10 ETH at ₩500,000 each in 2021 (actual cost: ₩5,000,000). Market price on 31 Dec 2026: ₩4,000,000 per ETH (total: ₩40,000,000). Sold all 10 ETH at ₩5,000,000 each in March 2027 (total proceeds: ₩50,000,000).

**Computation:**
```
Deemed acquisition cost = MAX(actual cost, 31 Dec 2026 price)
  Actual cost:            ₩5,000,000
  31 Dec 2026 value:      ₩40,000,000
  Deemed cost:            ₩40,000,000

Disposal proceeds:        ₩50,000,000
Cost basis:               ₩40,000,000
Gain:                     ₩10,000,000
Basic deduction:          ₩2,500,000
Taxable income:           ₩7,500,000
Tax (22%):                ₩1,650,000
```

The pre-2027 appreciation (₩35,000,000) is shielded by the deemed cost basis rule.

### Example 3 -- Gift Tax (Applies NOW — 2025)

**Input:** Parent gifts 2 BTC to adult child. Average exchange price over the 2-month valuation window: ₩50,000,000 per BTC. Total gift value: ₩100,000,000.

**Computation:**
```
Gift value:                ₩100,000,000
Exemption (adult child):   ₩50,000,000
Taxable gift:              ₩50,000,000
Gift tax (10%):            ₩5,000,000
```

This applies in 2025 — gift tax on crypto is already in force regardless of the virtual asset income tax deferral.

## Self-Checks

Before finalising any South Korea crypto tax computation, verify:

- [ ] Is the income year 2027 or later? If before 2027, virtual asset income tax does NOT apply (but gift tax and foreign reporting do)
- [ ] Has the taxpayer confirmed Korean tax residency?
- [ ] Are all transaction values converted to KRW at the transaction date?
- [ ] Has the correct cost basis method been applied (moving average for exchange, FIFO for other)?
- [ ] For pre-2027 holdings, has the deemed acquisition cost been computed using MAX(31 Dec 2026 price, actual cost)?
- [ ] Has the ₩2,500,000 basic deduction been applied (once per year, not per transaction)?
- [ ] Have any crypto gifts been checked for gift tax liability?
- [ ] Has the ₩500M overseas financial account threshold been checked?
- [ ] Are exchange fees included in cost basis?
- [ ] Has the loss netting been done correctly within the year (no carry-forward)?
- [ ] Flag for reviewer: has NTS issued any updated guidance since this skill was written?

## PROHIBITIONS

- NEVER state that crypto gains are taxable income in Korea for years before 2027 — the income tax is deferred
- NEVER ignore gift tax — it applies NOW to crypto transfers between related parties
- NEVER allow loss carry-forward — Korea does not permit this for virtual asset income
- NEVER assume progressive rates apply to virtual asset income — it is a flat 22% separate tax
- NEVER forget the deemed acquisition cost rule for pre-2027 holdings
- NEVER ignore overseas exchange holdings for the ₩500M foreign account reporting threshold
- NEVER compute gain without verified cost basis and correct method (moving average vs FIFO)
- NEVER treat wallet-to-wallet transfers as taxable disposals
- NEVER present crypto tax positions as definitive — NTS guidance is still evolving; always flag for professional review
- NEVER advise on VAUPA regulatory compliance — this skill covers tax only

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Korean licensed tax accountant (세무사), CPA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
