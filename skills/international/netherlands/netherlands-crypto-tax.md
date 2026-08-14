---
name: netherlands-crypto-tax
description: Use this skill whenever asked about Netherlands cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Netherlands", "Bitcoin Netherlands", "crypto belasting", "Box 3 crypto", "vermogensrendementsheffing crypto", "cryptocurrency Netherlands", "crypto income Netherlands", "staking Netherlands", "mining income Netherlands", "NFT tax Netherlands", "Belastingdienst crypto", "Dutch crypto tax", "fictief rendement crypto", "heffingsvrij vermogen", "Overbruggingswet box 3", "Binance Netherlands tax", "Coinbase Netherlands tax", "aangifte crypto", or any question about the income tax, wealth tax, or VAT treatment of cryptocurrency, tokens, or digital assets for Dutch tax residents or Netherlands-source crypto income. Covers Box 3 wealth taxation, fictional return system, actual return counter-evidence, Box 1 business classification, and DAC8 reporting. ALWAYS read this skill before touching any Netherlands crypto work.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - netherlands-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands Crypto Tax

## Netherlands Crypto / Digital Assets Tax Skill v1.0

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Tax | Inkomstenbelasting — Box 3 (Inkomen uit sparen en beleggen) |
| Currency | EUR (all values must be in EUR) |
| Tax year | Calendar year (1 January – 31 December) |
| Primary authority | Wet inkomstenbelasting 2001 (Wet IB 2001), Articles 5.1–5.3; Overbruggingswet box 3 (2023–2027 transitional legislation); Wet tegenbewijsregeling box 3 (enacted 8 July 2025) |
| Future reform | Wet werkelijk rendement box 3 — planned effective 1 January 2028 (actual-return system) |
| Tax authority | Belastingdienst (Dutch Tax and Customs Administration) |
| Filing portal | Mijn Belastingdienst (mijn.belastingdienst.nl) |
| Filing deadline | 1 May of the following year (extensions possible until 1 September) |
| EU reporting | DAC8 / CARF — from 2026 |
| Validated by | Pending — requires sign-off by a Dutch belastingadviseur or registeraccountant |
| Skill version | 1.0 |

### Key Principle: Box 3 Wealth Tax — NOT Capital Gains Tax

The Netherlands does **not** tax crypto capital gains for private investors. Instead, crypto is taxed as an asset under Box 3 based on its **value on 1 January** of the tax year. A fictional (notional) return is applied to this value, and tax is levied on that fictional return — regardless of whether the taxpayer actually made or lost money during the year.

### Box 3 Categories and Crypto Classification

**Box 3 Categories and Crypto Classification**

| Asset Category | 2025 Notional Return | Examples |
| --- | --- | --- |
| Banktegoeden (bank balances) | 1.37% | Savings, current accounts, cash above threshold |
| Beleggingen en overige bezittingen (investments and other assets) | **5.88%** | **Cryptocurrency**, shares, bonds, real estate (not primary home), NFTs |
| Schulden (deductible debts) | 2.70% | Loans, mortgages not in Box 1 |

- **Crypto classification** — Crypto falls under "beleggingen en overige bezittingen" at 5.88% notional return.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether trading is hobby or business | Treat as Box 3 (private investment) unless clear business indicators |
| Unknown January 1 valuation | STOP — cannot compute Box 3 without peildatum value |
| Unknown residency status | STOP — affects worldwide vs limited tax obligation |
| DeFi positions with unclear valuation | Estimate fair market value on 1 January; flag for review |
| Staking rewards received during year | Add to Box 3 value on next 1 January; if habitual business, escalate |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — total market value of all crypto holdings in EUR as of 1 January 2025, confirmation of Dutch tax residency, and indication of whether activity is passive holding or active business.

**Recommended** — portfolio snapshots on 1 January from all exchanges (Binance, Coinbase, Kraken, Bitvavo, etc.), wallet balances on 1 January, DeFi position values, and overview of all other Box 3 assets and debts.

**Ideal** — complete Mijn Belastingdienst pre-populated data, portfolio tracker export with January 1 snapshots, full transaction history (to evaluate actual return option), and records of staking/mining activity frequency.

### Refusal Catalogue

- **R-NLC-1** — Residency unknown. "Dutch tax residents are subject to Box 3 on worldwide assets. Non-residents may only be taxed on Dutch-source assets. Cannot proceed without confirming tax residency."
- **R-NLC-2** — No January 1 valuation. "Box 3 tax is based entirely on the value of crypto holdings on 1 January. Without this valuation, the tax cannot be computed. Cannot proceed."
- **R-NLC-3** — Corporate crypto holdings. "Companies (BVs, NVs) holding crypto pay vennootschapsbelasting (corporate income tax) on realised and unrealised gains. This skill covers individuals (inkomstenbelasting) only. Escalate to a belastingadviseur."
- **R-NLC-4** — Box 1 business classification. "If crypto activity constitutes a business (onderneming) or work (resultaat uit overige werkzaamheden), it falls under Box 1 with different rules. This requires professional assessment. Escalate."
- **R-NLC-5** — Complex international structures. "Non-resident taxpayers with Dutch crypto assets, or Dutch residents with foreign structures holding crypto, require specialist international tax advice. Escalate."

## Section 3 — Rate Tables and Computation

### 3.1 Box 3 Parameters for 2025

**Box 3 Parameters for 2025**  _(Belastingdienst official calculation page (belastingdienst.nl/box-3); Overbruggingswet box 3; Belastingplan 2025.)_

| Parameter | 2025 Value |
| --- | --- |
| Tax rate | **36%** |
| Heffingsvrij vermogen (tax-free allowance) — single | **€57,684** |
| Heffingsvrij vermogen — fiscal partners (combined) | **€115,368** |
| Notional return: bank balances | 1.37% |
| Notional return: investments & other assets (incl. crypto) | **5.88%** |
| Notional return: debts | 2.70% |
| Debt threshold — single | €3,800 |
| Debt threshold — fiscal partners | €7,600 |

### 3.2 Box 3 Computation Steps

1. **Determine asset values on 1 January 2025** — total banktegoeden, total beleggingen en overige bezittingen (including all crypto), total schulden
2. **Calculate notional return per category:**
   - Bank balances × 1.37%
   - Investments & other assets × 5.88%
   - Debts (above threshold) × 2.70%
3. **Taxable return** = (return on banks + return on investments) − return on debts
4. **Capital yield tax base** = total assets − total debts (but debts reduced by threshold)
5. **Effective return %** = taxable return ÷ capital yield tax base
6. **Box 3 income** = (capital yield tax base − heffingsvrij vermogen) × effective return %
7. **Tax** = Box 3 income × 36%

### 3.3 Actual Return Option (Tegenbewijsregeling) — Available from 2025

Since the Hoge Raad (Supreme Court) Kerstarrest (24 December 2021) and subsequent rulings (June 2024), taxpayers can claim their **actual return** if it is lower than the notional return. The Wet tegenbewijsregeling box 3 was enacted on 8 July 2025.

**Actual Return Option table**

| Element | Detail |
| --- | --- |
| How to claim | Via the "Opgaaf Werkelijk Rendement" (OWR) form in Mijn Belastingdienst (available since 10 July 2025) |
| What counts as actual return | Received income (interest, dividends, rent) PLUS realised and unrealised value changes of all Box 3 assets over the calendar year |
| For crypto | Must include both realised gains/losses AND unrealised appreciation/depreciation (1 Jan value vs 31 Dec value) |
| Tax treatment | Belastingdienst automatically applies the more favourable of notional vs actual return |
| Available years | 2017 onwards (for years with open assessments) |

**Key insight:** If crypto prices fell during 2025 but you held a large position on 1 January, the actual return method may produce a lower (or negative) return, reducing your tax liability.

### 3.4 Future: Wet Werkelijk Rendement Box 3 (from 2028)

From 1 January 2028, the system is planned to change fundamentally:
- Tax based on **actual** income: received interest, dividends, rental income, and realised + unrealised value changes
- Heffingsvrij **inkomen** (income exemption) of approximately €1,800 per person replaces heffingsvrij vermogen
- Tax rate expected to remain 36%
- Crypto unrealised gains/losses will be part of the taxable base

## Section 4 — Cost Basis Methods

### 4.1 Box 3 — No Cost Basis Needed for Standard Computation

- **Cost basis irrelevance** — Under the standard Box 3 notional return system, **cost basis is irrelevant** — only the market value on 1 January matters.

**Cost basis methods table**

| Method | Relevance |
| --- | --- |
| FIFO | Not required for Box 3 notional return |
| Average cost | Not required for Box 3 notional return |
| Specific identification | Not required for Box 3 notional return |

### 4.2 Actual Return (Tegenbewijsregeling) — Cost Basis Required

If claiming actual return, you need:
- Value of all crypto on 1 January and 31 December
- All acquisition costs and disposal proceeds during the year
- The Belastingdienst does not prescribe a specific method for calculating individual trade gains in the actual-return context; the total portfolio return over the year is what matters

### 4.3 Box 1 Business — Cost Basis Required

- **Box 1 cost basis** — If crypto activity is classified as Box 1 business income, standard accounting methods apply (typically FIFO or weighted average under good bookkeeping practice — goed koopmansgebruik under Article 3.25 Wet IB 2001).  _(Article 3.25 Wet IB 2001)_

## Section 5 — DeFi, Staking, Mining, and Airdrop Treatment

### 5.1 General Principle

For private investors, all crypto assets and DeFi positions are simply part of Box 3 — valued on 1 January. The nature of the holding (staking, lending, LP tokens) doesn't change the Box 3 treatment; it only matters for valuation.

**Activity classification table**

| Activity | Private Investor (Box 3) | Business/Professional (Box 1) |
| --- | --- | --- |
| Passive holding | Box 3 — value on 1 Jan | N/A |
| Staking (passive, via exchange) | Box 3 — include staking position value on 1 Jan | Box 1 if habitual business activity |
| Mining (occasional) | Box 3 — include mined coins value on 1 Jan | Box 1 if habitual/organised |
| Mining (systematic, with infrastructure) | Likely Box 1 — resultaat uit overige werkzaamheden or winst uit onderneming | Box 1 business income |
| DeFi lending (e.g. Aave) | Box 3 — value of deposited crypto + accrued interest on 1 Jan | Box 1 if part of active trading business |
| Liquidity provision (e.g. Uniswap) | Box 3 — value of LP tokens on 1 Jan | Box 1 if part of active business |
| Active DeFi trading (frequent, systematic) | May be reclassified to Box 1 | Box 1 — resultaat uit overige werkzaamheden |
| Airdrops | Box 3 — value on next 1 Jan if still held | Box 1 if received as part of business activity |

### 5.2 Box 1 Indicators (When Does Crypto Become Business?)

The Belastingdienst applies general income tax principles. There is no specific crypto threshold. Indicators for Box 1 classification:

**Box 1 Indicators table**

| Factor | Indicates Box 1 |
| --- | --- |
| Volume and frequency | Hundreds/thousands of trades, daily activity |
| Specialist knowledge | Use of bots, algorithms, technical analysis |
| Organisation | Dedicated infrastructure, office, employees |
| Time investment | Significant hours spent on trading |
| Leverage and borrowing | Trading with borrowed funds |
| Source of income | Crypto trading is primary income source |

- **Box 1 consequences** — Income taxed at progressive rates (up to 49.50% in 2025), but business deductions and losses are available.

### 5.3 Valuation of DeFi Positions on 1 January

**Valuation of DeFi Positions table**

| Position Type | Valuation Method |
| --- | --- |
| Tokens on exchange | Exchange balance × price on 1 Jan |
| Tokens in hardware wallet | Balance × price on 1 Jan (use CoinGecko/CoinMarketCap closing price) |
| Staked tokens (locked) | Market value of underlying tokens on 1 Jan (not the staking derivative) |
| LP tokens (Uniswap, etc.) | Fair market value of the LP position on 1 Jan (underlying tokens × prices) |
| Lending deposits (Aave, Compound) | Principal + accrued interest in crypto × price on 1 Jan |
| Wrapped tokens (WETH, WBTC) | Same as underlying token value |
| Governance tokens (UNI, AAVE, etc.) | Market price on 1 Jan |

## Section 6 — NFT Treatment

NFTs are treated as "overige bezittingen" (other assets) in Box 3.

**NFT Treatment table**

| Activity | Treatment |
| --- | --- |
| Holding NFTs | Box 3 — fair market value on 1 January |
| Buying NFTs with crypto | Crypto position decreases, NFT position increases — both valued on next 1 Jan |
| Selling NFTs | Proceeds are part of your overall assets; capital gain is not separately taxed (Box 3 only) |
| Creating and selling NFTs (artist) | If habitual/professional → Box 1 business income |
| NFT valuation challenge | Use last sale price, floor price of collection, or best available fair market estimate |

**Special issue:** Illiquid or unique NFTs with no clear market value — use conservative best estimate and document your methodology. The Belastingdienst may challenge valuations.

## Section 7 — Reporting Requirements

### 7.1 Aangifte Inkomstenbelasting (Income Tax Return)

**Aangifte Inkomstenbelasting table**

| Section | Content |
| --- | --- |
| Box 3, "beleggingen en andere bezittingen" | Total value of all crypto holdings as of 1 January 2025 in EUR |
| "cryptovaluta" subcategory | Specifically listed in the Box 3 form — enter total EUR value |
| Schulden (debts) | If you have crypto-related debts (margin loans, etc.) above the threshold |
| Werkelijk rendement (if applicable) | Complete the Opgaaf Werkelijk Rendement (OWR) form if actual return < notional return |

- **Filing deadline** — 1 May of the following year (extended to 1 September upon request).

### 7.2 What You Do NOT Report

- Individual transactions (buys, sells, swaps)
- Capital gains or losses on individual trades
- Cost basis or FIFO calculations
- Staking/mining reward details

You only report the **total value on 1 January**.

### 7.3 DAC8 / CARF (from 2026)

Crypto exchanges will report Dutch users' transaction data to the Belastingdienst automatically. This will enable cross-referencing of reported Box 3 values against actual holdings.

### 7.4 Record-Keeping

**Record-Keeping table**

| Requirement | Detail |
| --- | --- |
| Retention period | 7 years (algemene bewaarplicht under Article 52 AWR) |
| Records to maintain | Portfolio snapshots on 1 January of each year, exchange statements, wallet balances, transaction history (especially if claiming actual return or for Box 1 classification) |
| Format | Exchange exports, portfolio tracker screenshots, on-chain records |

## Section 8 — Loss Offset and Carry-Forward

### 8.1 Box 3 — No Loss Offset in Standard System

- **No loss concept** — Under the standard notional return system, there is **no concept of losses**. Tax is based on the fictional return, not actual results.

**Loss scenarios table**

| Scenario | Treatment |
| --- | --- |
| Crypto lost 50% value during 2025 | Irrelevant under notional return — tax based on 1 Jan value |
| Crypto exchange went bankrupt | If holdings are worthless on next 1 Jan, Box 3 value = €0 for that year |
| Sold all crypto at a loss | No Box 3 liability in following year (no assets on 1 Jan) |

**This means Dutch crypto holders can pay tax even when they lost money — a major source of controversy and the reason for the Kerstarrest reform.**

### 8.2 Actual Return — Negative Return Possible

- **Negative actual return rules** — If using the tegenbewijsregeling (actual return): - A negative actual return (losses exceed income) results in **€0 Box 3 income** for that year - Negative returns can NOT be carried forward to offset future years' Box 3 income - The Belastingdienst applies the more favourable of notional vs actual return

### 8.3 Box 1 — Standard Loss Rules

- **Box 1 loss rules** — If classified as Box 1 business income: - Losses from crypto business can offset other Box 1 income in the same year - Carry-back: 1 year - Carry-forward: indefinite (but limited to €1,000,000 + 50% of profits exceeding €1,000,000 per year)

## Section 9 — Anti-Avoidance Rules

### 9.1 General Anti-Abuse (Fraus Legis)

- **Fraus legis doctrine** — Dutch tax law includes the doctrine of fraus legis — the Belastingdienst can disregard arrangements entered into primarily for tax avoidance purposes that conflict with the purpose and intent of the law.

### 9.2 Peildatumarbitrage (Reference Date Manipulation)

**Peildatumarbitrage table**

| Risk | Detail |
| --- | --- |
| Selling crypto before 31 December and rebuying after 1 January | Legitimate tax planning (Box 3 value on 1 Jan is zero), but must be genuine — if considered artificial, fraus legis may apply |
| Moving crypto to non-reportable structures around 1 January | High audit risk — Belastingdienst is aware of this practice |
| Using stablecoins to "park" value before 1 January | Stablecoins are also crypto — still counted as "overige bezittingen" |

### 9.3 Box Hopping

- **Box hopping anti-avoidance** — Moving assets between Box 1, Box 2, and Box 3 to minimise tax is subject to anti-avoidance scrutiny. The Belastingdienst can reclassify.

### 9.4 DAC8 Cross-Referencing (from 2026)

Automatic data exchange will make it much harder to underreport Box 3 crypto values. Exchanges report:
- Account balances
- Transaction volumes
- User identity

## Section 10 — Worked Examples

### Example 1 — Standard Box 3 Computation

**Input:** Dutch tax resident (single, no fiscal partner). On 1 January 2025:
- Bank balances: €20,000
- Crypto portfolio: €150,000 (BTC, ETH, various altcoins)
- No debts, no other Box 3 assets

**Computation:**
```
Step 1 — Notional return:
  Bank balances:  €20,000 × 1.37%  =   €274.00
  Crypto:        €150,000 × 5.88%  = €8,820.00
  Total return:                       €9,094.00

Step 2 — Capital yield tax base:
  Total assets:  €20,000 + €150,000 = €170,000
  Less debts:    €0
  Tax base:      €170,000

Step 3 — Effective return percentage:
  €9,094 ÷ €170,000 = 5.3494%

Step 4 — Box 3 income:
  (€170,000 − €57,684) × 5.3494% = €112,316 × 5.3494% = €6,008.53

Step 5 — Tax:
  €6,008.53 × 36% = €2,163.07
```

### Example 2 — Actual Return Lower Than Notional

**Input:** Same taxpayer as Example 1. During 2025, crypto portfolio fell from €150,000 (1 Jan) to €90,000 (31 Dec). No crypto was sold. Bank interest earned: €250.

**Actual return computation:**
```
Actual return:
  Bank interest:        €250.00
  Crypto value change:  €90,000 − €150,000 = −€60,000.00
  Total actual return:  €250 + (−€60,000) = −€59,750.00

Since actual return (−€59,750) < notional return (€9,094),
the Belastingdienst uses the actual return.

Actual return is negative → Box 3 income = €0
Tax = €0

Savings compared to notional method: €2,163.07
```

The taxpayer should file the Opgaaf Werkelijk Rendement (OWR) to claim this benefit.

### Example 3 — Crypto Miner (Box 1)

**Input:** Dutch tax resident operates a mining farm with 20 GPUs, dedicated premises, and regular income from mining. Total mining revenue in 2025: €40,000. Electricity and hardware costs: €15,000. No other employment.

**Computation:**
```
Classification: Box 1 — winst uit onderneming (business profits)

Revenue:        €40,000
Expenses:       €15,000
Taxable profit: €25,000

Box 1 tax (2025 rates, approximate):
  Up to €38,441: 36.97%
  €25,000 × 36.97% = €9,242.50

Less: small business deduction (zelfstandigenaftrek) 
  and other Box 1 deductions if applicable.

Mined crypto still held on 1 January: NOT counted in
Box 3 (already in Box 1 as business assets).
```

## Self-Checks

Before delivering any Netherlands crypto tax computation, verify:

- [ ] Residency confirmed — Dutch tax resident (worldwide) or non-resident?
- [ ] 1 January valuation obtained for ALL crypto holdings across ALL platforms and wallets
- [ ] Correct category: crypto is "beleggingen en overige bezittingen" at 5.88% (2025)
- [ ] Heffingsvrij vermogen correctly applied (€57,684 single / €115,368 partners)
- [ ] Fiscal partner status checked — can allocate Box 3 assets optimally
- [ ] Actual return option evaluated — is actual return lower than notional?
- [ ] Box 1 indicators assessed — is activity hobby or business?
- [ ] DeFi positions included in Box 3 at fair market value on 1 Jan
- [ ] Peildatumarbitrage risk flagged if large sales occurred near year-end
- [ ] Output labelled as estimated — flag for professional review

## PROHIBITIONS

- NEVER apply capital gains tax to crypto for Dutch private investors — there is no CGT in the Netherlands for Box 3 assets
- NEVER confuse Box 3 notional return with actual gains — the tax is based on fictional return, not real profits (unless actual return option is used)
- NEVER forget that crypto holders pay tax even in loss years under the standard system
- NEVER use mid-year or year-end values — Box 3 is based strictly on 1 January values (peildatum)
- NEVER assume staking/mining is automatically Box 1 — only habitual, organised, business-like activity qualifies
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review
- NEVER ignore the actual return option — it can save significant tax in down markets
- NEVER advise on AFM/DNB regulatory matters — this skill covers tax only
- NEVER assume the system will continue unchanged — Box 3 reform (werkelijk rendement) is planned for 2028

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a belastingadviseur, registeraccountant, or fiscalist in the Netherlands) before filing or acting upon.

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
