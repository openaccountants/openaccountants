---
name: de-crypto-tax
description: Use this skill whenever asked about German cryptocurrency taxation. Trigger on phrases like "Krypto Steuer", "crypto tax Germany", "Haltefrist", "§23 EStG", "private Veräußerungsgeschäfte", "Freigrenze", "staking tax Germany", "mining income Germany", "BMF Schreiben", "DeFi tax Germany", "FIFO crypto", or any question about buying, selling, staking, mining, or lending crypto as a German tax resident. This skill covers the 1-year holding period, €1,000 Freigrenze, staking/mining classification, DeFi treatment, and the BMF guidance of 10.05.2022. ALWAYS read this skill before advising on German crypto taxation.
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DE Crypto Tax

## German Crypto Tax -- Skill v1.0

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Germany (Bundesrepublik Deutschland) |
| Tax | Einkommensteuer (Income Tax) on crypto gains |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Einkommensteuergesetz (EStG) §23, §22 Nr. 3, §15 |
| Key guidance | BMF-Schreiben vom 10.05.2022 (Gz. IV C 1 - S 2256/19/10003 :001) |
| Supporting legislation | Jahressteuergesetz 2022 (Freigrenze-Erhöhung ab VZ 2024) |
| Tax authority | Bundeszentralamt für Steuern (BZSt) / local Finanzamt |
| Filing portal | ELSTER (elster.de) |
| Filing deadline | July 31 following year (without Steuerberater); Feb 28 of second following year (with Steuerberater) |
| Validated by | Pending — requires sign-off by a German Steuerberater |
| Skill version | 1.0 |

### Core Rules Summary

**Core Rules Summary**

| Rule | Detail |
| --- | --- |
| Legal classification | "Anderes Wirtschaftsgut" (other economic asset) per BMF 2022 |
| Taxable event | Sale, exchange, or use of crypto within 1-year Haltefrist |
| Holding period (Haltefrist) | >1 year → completely tax-free (§23 Abs. 1 S. 1 Nr. 2 EStG) |
| Freigrenze (§23 Abs. 3 S. 5) | €1,000/year total from ALL private sales (since VZ 2024; previously €600) |
| Freigrenze behavior | If exceeded, ENTIRE gain is taxable (not just excess) |
| Tax rate | Personal income tax rate (0%--45%) + Solidaritätszuschlag (5.5% of tax) + Kirchensteuer (8%/9%) |
| Method | FIFO (First In, First Out) -- per BMF Schreiben |
| Staking/Lending income | Sonstige Einkünfte §22 Nr. 3 EStG |
| Mining (commercial) | Gewerbliche Einkünfte §15 EStG |
| NO Abgeltungsteuer | Crypto is NOT subject to 25% flat capital gains tax |
| Holding period extension | NOT extended by staking/lending (BMF 2022 confirmed) |

### German Income Tax Rates 2025

**German Income Tax Rates 2025**

| Taxable Income (EUR) | Rate |
| --- | --- |
| 0 -- 12,096 | 0% (Grundfreibetrag) |
| 12,097 -- 17,443 | 14% -- 23.97% (progressive zone 1) |
| 17,444 -- 66,760 | 23.97% -- 42% (progressive zone 2) |
| 66,761 -- 277,825 | 42% |
| 277,826+ | 45% (Reichensteuer) |

- **Solidaritätszuschlag threshold** — Plus: Solidaritätszuschlag 5.5% on income tax (if tax > Freigrenze of €18,130/€36,260)
- **Kirchensteuer rate** — Plus: Kirchensteuer 8% (Bayern, Baden-Württemberg) or 9% (all other Länder) if church member

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown acquisition date | Assume <1 year (taxable) |
| Unknown acquisition cost | Use €0 (maximises gain -- conservative) |
| Unknown wallet attribution | STOP -- cannot determine Haltefrist without wallet history |
| FIFO vs LIFO | FIFO mandatory per BMF Schreiben |
| Mixed wallet (staked + unstaked) | Separate tracking required |
| Airdrop cost basis | €0 at receipt (income = FMV at receipt under §22) |

## Section 2 -- Rules and Classification

### 2.1 Private Veräußerungsgeschäfte (§23 EStG)

- **Definition of private sale and gain formula** — Crypto sold/exchanged within 1 year of acquisition is a private sale. Gain = sale price - acquisition cost - directly related expenses (Werbungskosten).  _(§23 EStG)_

**Taxable events:**
- Selling crypto for EUR/fiat
- Exchanging crypto for another crypto (e.g., BTC → ETH)
- Paying for goods/services with crypto
- Providing crypto as collateral that is liquidated

**Non-taxable events:**
- Transferring between own wallets
- Buying crypto with fiat (acquisition, not disposal)
- Holding >1 year then selling (steuerfrei)
- Gift (but recipient inherits acquisition date + cost)

### 2.2 Staking as Sonstige Einkünfte (§22 Nr. 3 EStG)

**Staking treatment table**

| Aspect | Treatment |
| --- | --- |
| Classification | Sonstige Einkünfte (miscellaneous income) |
| Taxable event | Receipt of staking rewards |
| Taxable amount | Fair market value (EUR) at time of receipt (Zufluss) |
| Freigrenze | €256/year for ALL sonstige Einkünfte combined (§22 Nr. 3 S. 2) |
| Freigrenze behavior | If exceeded, entire amount taxable |
| Holding period of rewards | Starts fresh from receipt date -- 1 year to tax-free sale |
| Haltefrist extension | NO extension for staked coins (BMF 2022, Rz. 87) |

### 2.3 Mining

**Mining classification table**

| Scenario | Classification |
| --- | --- |
| Hobby mining (occasional, small scale) | §22 Nr. 3 EStG (sonstige Einkünfte) |
| Commercial mining (sustained, profit intent, significant hardware) | §15 EStG (Gewerbebetrieb) |
| Pool mining | Same rules -- proportional share of block reward |

**Commercial mining triggers:**
- Gewerbesteuer obligation (municipal trade tax)
- Gewerbeanmeldung required
- IHK membership
- Full income tax on mining income at progressive rates
- Depreciation (AfA) allowed on mining hardware

**Hobby mining (§22 Nr. 3):**
- €256 Freigrenze applies
- Hardware costs deductible as Werbungskosten
- No Gewerbesteuer

### 2.4 Lending (Crypto Lending / DeFi Lending)

**Lending treatment table**

| Aspect | Treatment |
| --- | --- |
| Interest received | §22 Nr. 3 EStG (sonstige Einkünfte) |
| Taxable amount | FMV in EUR at receipt |
| Freigrenze | €256/year (shared with staking and other §22 Nr. 3 income) |
| Holding period of original coins | NOT extended by lending (BMF 2022) |
| Return of lent coins | Not a taxable event |

### 2.5 DeFi Specific Treatments

**DeFi activity classification table**

| DeFi Activity | Classification | Notes |
| --- | --- | --- |
| Token swap on DEX | §23 EStG disposal + acquisition | Same as centralised exchange trade |
| Liquidity provision (LP) | Disposal of tokens into pool = §23 event | Acquisition of LP tokens |
| LP token removal | Disposal of LP token = §23 event | Reacquisition of underlying |
| Yield farming rewards | §22 Nr. 3 (sonstige Einkünfte) | FMV at receipt |
| Airdrops | §22 Nr. 3 at FMV on receipt | Cost basis = FMV at receipt for future sale |
| Hard forks (new coins) | Cost basis €0; acquisition date = fork date | Taxable on sale within 1 year |
| Wrapped tokens (e.g., WETH) | Potentially §23 event (exchange) | Conservative: treat as disposal |
| NFT sale | §23 EStG (same as any crypto asset) | 1-year Haltefrist applies |
| Governance token rewards | §22 Nr. 3 at FMV | Same as staking rewards |

### 2.6 FIFO Method (Mandatory)

- **FIFO application rules** — FIFO applies per wallet/exchange account (walletbezogen). Alternatively, taxpayer may apply FIFO across ALL wallets (universal FIFO) if consistently applied. Once chosen, method must be maintained consistently. LIFO, HIFO, and other methods are NOT permitted.  _(BMF-Schreiben Rz. 59--63)_

**Per-wallet FIFO example:**
- Wallet A: bought 1 BTC on 01.01.2024, bought 1 BTC on 01.06.2024
- Wallet A: sold 1 BTC on 15.03.2025
- FIFO: the 01.01.2024 BTC is sold → held >1 year → tax-free

## Section 3 -- Computation

### 3.1 Gain Calculation (§23)

- **Veräußerungsgewinn formula** — Veräußerungsgewinn = Veräußerungspreis - Anschaffungskosten - Werbungskosten (directly attributable costs) Where: - Veräußerungspreis = EUR value at time of sale/exchange - Anschaffungskosten = EUR value at time of acquisition (FIFO) - Werbungskosten = exchange fees, network fees (gas), directly related costs  _(§23 EStG)_

### 3.2 Annual Aggregation

- **Annual aggregation steps** — Step 1: Calculate gain/loss on each individual disposal within Haltefrist Step 2: Sum all gains and losses from §23 transactions for the year Step 3: Check net result against €1,000 Freigrenze - Net gain < €1,000 → entirely tax-free - Net gain ≥ €1,000 → entire net gain is taxable Step 4: If taxable, add to other taxable income in Einkommensteuererklärung Step 5: Apply personal income tax rate (Anlage SO)

### 3.3 Loss Treatment (§23 Abs. 3)

**Loss treatment table**

| Rule | Detail |
| --- | --- |
| Offsetting within year | §23 losses offset §23 gains in same year |
| Cannot offset against other income | §23 losses ONLY offset §23 gains (horizontal Verlustausgleich prohibited) |
| Carry-back | 1 year carry-back to prior year §23 gains (§10d Abs. 1) |
| Carry-forward | Unlimited carry-forward to future §23 gains |
| Verlustvortrag application | Automatically applied by Finanzamt if declared |

### 3.4 Staking/Mining Income Computation

- **Staking/Mining income steps** — Staking/Mining Income (§22 Nr. 3): Step 1: Record FMV in EUR of each reward at time of receipt Step 2: Sum all §22 Nr. 3 income for the year (includes staking, lending interest, mining hobby, airdrops) Step 3: Check against €256 Freigrenze - Total < €256 → entirely tax-free - Total ≥ €256 → entire amount taxable Step 4: Deduct directly related Werbungskosten (e.g., validator costs) Step 5: Net amount added to taxable income

## Section 4 -- Filing

### 4.1 ELSTER Forms

**ELSTER forms table**

| Form | Purpose |
| --- | --- |
| Anlage SO (Sonstige Einkünfte) | Report §23 gains and §22 Nr. 3 income |
| Zeile 41--48 (Anlage SO) | Private Veräußerungsgeschäfte |
| Zeile 8--15 (Anlage SO) | Sonstige Einkünfte (staking, lending) |
| Anlage G (Gewerbeeinkünfte) | Commercial mining only |
| Anlage EÜR | Einnahmen-Überschussrechnung for Gewerbe |

### 4.2 Documentation Requirements

**Documentation requirements table**  _(§147 AO)_

| Document | Retention Period |
| --- | --- |
| Trade history (all exchanges) | 10 years (§147 AO) |
| Wallet transaction records | 10 years |
| Cost basis calculations | 10 years |
| Staking reward records with timestamps | 10 years |
| Exchange confirmations / screenshots | 10 years |
| FIFO calculation spreadsheet | 10 years |

### 4.3 Filing Deadlines

**Filing deadlines table**

| Scenario | Deadline |
| --- | --- |
| Without Steuerberater | July 31 of following year |
| With Steuerberater | Last day of February, second following year |
| Voluntary filing (Antragsveranlagung) | Up to 4 years |
| Amended return (Berichtigung) | Before Steuerbescheid becomes bestandskräftig |

## Section 5 -- Edge Cases

### 5.1 Crypto-to-Crypto Exchanges

- **Crypto-to-crypto exchange treatment** — Every crypto-to-crypto exchange (e.g., BTC → ETH) is TWO events: 1. Disposal of BTC (realises gain/loss under §23 if <1 year held) 2. Acquisition of ETH (new Anschaffungskosten = FMV at time of exchange) The exchange rate used must be documented (e.g., CoinMarketCap, exchange order fill price).  _(§23 EStG)_

### 5.2 Gifts and Inheritance

**Gifts and inheritance table**

| Scenario | Rule |
| --- | --- |
| Gift (Schenkung) | Recipient inherits acquisition date AND cost basis of donor |
| Inheritance (Erbschaft) | Heir inherits acquisition date AND cost basis of deceased |
| Implication | If donor held >1 year, recipient can sell immediately tax-free |
| Schenkungsteuer | Separate gift tax may apply (Freibeträge: €500,000 spouse, €400,000 child) |

### 5.3 Stablecoins

- **Stablecoin treatment** — Stablecoins (USDT, USDC, DAI) are "andere Wirtschaftsgüter" -- same rules apply. Exchange gains from EUR→stablecoin→EUR within 1 year are taxable. FX movement on stablecoin denominated in USD is a §23 event.

### 5.4 Lost/Stolen Crypto

- **Lost/stolen crypto treatment** — If provably lost (e.g., lost private key, verified hack), may claim as Verlust under §23. Finanzamt may require proof (police report, blockchain evidence). Scam losses: deductible as §23 Verlust if disposal can be demonstrated.

### 5.5 ICO / Token Sales

- **ICO/token sale treatment** — Acquisition of ICO tokens: Anschaffungskosten = EUR paid. Sale within 1 year: §23 gain/loss. Worthless tokens: may realise loss by provable abandonment or sell for minimal amount.

### 5.6 Fork Coins

- **Fork coin treatment** — New coins received from hard fork: Anschaffungskosten = €0. Acquisition date = date of fork. Sale within 1 year of fork: gain = full proceeds (minus fees). Sale after 1 year from fork: tax-free.

### 5.7 Margin/Futures Trading

- **Margin/futures trading treatment** — Gains from crypto futures/CFDs: typically §20 EStG (Kapitalerträge) -- 25% Abgeltungsteuer. Gains from leveraged spot trading: §23 EStG (same as normal trading). BFH case law developing -- document approach taken.

## Section 6 -- Worked Examples

### Example 1 -- Simple Sale Within Haltefrist

Bought 2 BTC on 15.03.2025 for €50,000 total (€25,000 each).
Sold 1 BTC on 01.08.2025 for €35,000. Exchange fee: €50.

Gain = €35,000 - €25,000 - €50 = €9,950
Held < 1 year → taxable under §23.
€9,950 > €1,000 Freigrenze → entire €9,950 is taxable income.

### Example 2 -- Sale After Haltefrist

Bought 1 ETH on 01.01.2024 for €2,000.
Sold 1 ETH on 15.01.2025 for €4,000.

Held > 1 year → completely tax-free. No reporting obligation.

### Example 3 -- Staking Rewards

Received 0.5 ETH staking rewards throughout 2025.
Total FMV at each receipt: €1,800.
No other §22 Nr. 3 income.

€1,800 > €256 Freigrenze → entire €1,800 is taxable as sonstige Einkünfte.
Added to personal income; taxed at marginal rate.

### Example 4 -- Under Freigrenze

Total §23 gains in 2025: €900.
Total §22 Nr. 3 income (staking): €200.

§23: €900 < €1,000 → tax-free.
§22 Nr. 3: €200 < €256 → tax-free.
No tax obligation and no reporting required.

## Section 7 -- Common Mistakes

**Common mistakes table**

| Mistake | Correction |
| --- | --- |
| Applying 25% Abgeltungsteuer | WRONG -- crypto is §23, not §20. Personal rate applies. |
| Using LIFO instead of FIFO | WRONG -- only FIFO allowed per BMF Schreiben |
| Ignoring crypto-to-crypto trades | Each swap is a taxable disposal + new acquisition |
| Not tracking staking rewards separately | Each reward has its own acquisition date and cost basis |
| Assuming Haltefrist extends with staking | WRONG -- BMF 2022 confirmed NO extension |
| Treating Freigrenze as Freibetrag | WRONG -- Freigrenze means if exceeded, ALL is taxable |
| Not reporting because "exchange didn't report" | Doesn't matter -- taxpayer has Erklärungspflicht |

## Section 8 -- Reference Material

**Reference material table**

| Topic | Reference |
| --- | --- |
| Private sales | §23 Abs. 1 S. 1 Nr. 2 EStG |
| Freigrenze (€1,000) | §23 Abs. 3 S. 5 EStG (amended by JStG 2022, effective VZ 2024) |
| Miscellaneous income | §22 Nr. 3 EStG |
| Commercial income | §15 EStG |
| BMF crypto guidance | BMF-Schreiben 10.05.2022, IV C 1 - S 2256/19/10003 :001 |
| FIFO requirement | BMF-Schreiben Rz. 59--63 |
| No Haltefrist extension | BMF-Schreiben Rz. 87 |
| Staking classification | BMF-Schreiben Rz. 78--92 |
| Loss offsetting | §23 Abs. 3 S. 7, 8 EStG; §10d EStG |
| Filing obligation | §25 Abs. 3 EStG; §46 EStG |
| Record retention | §147 AO (10 years) |
| Grundfreibetrag 2025 | €12,096 (Inflationsausgleichsgesetz) |
| Solidaritätszuschlag | §3 SolZG |
| BFH case law | BFH IX R 3/22 (crypto as Wirtschaftsgut confirmed) |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
