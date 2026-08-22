---
name: spain-crypto-tax
description: Use this skill whenever asked about Spain cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Spain", "Bitcoin Spain", "criptomonedas IRPF", "cryptocurrency gains Spain", "crypto income Spain", "staking Spain", "mining income Spain", "NFT tax Spain", "Modelo 721", "Modelo 100 crypto", "rentas del ahorro crypto", "base del ahorro", "AEAT crypto", "Binance Spain tax", "Coinbase Spain tax", "Revolut crypto Spain", "DeFi tax Spain", "Hacienda crypto", "declaración renta criptomonedas", or any question about the income tax, capital gains, or VAT treatment of cryptocurrency, tokens, or digital assets for Spanish tax residents or Spain-source crypto income. Covers IRPF savings base taxation, Modelo 721 foreign crypto reporting, FIFO cost basis, Ley 11/2021 anti-fraud provisions, and DAC8 reporting. ALWAYS read this skill before touching any Spain crypto work.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - spain-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Crypto Tax

## Section 1 — Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Tax | IRPF — Impuesto sobre la Renta de las Personas Físicas |
| Currency | EUR (all values must be in EUR at transaction date) |
| Tax year | Calendar year (1 January – 31 December) |
| Primary authority | Ley 35/2006 del IRPF; Ley 11/2021 de medidas de prevención y lucha contra el fraude fiscal; Ley 7/2024 (savings base rate update) |
| Regulatory framework | Real Decreto 249/2023 (Modelos 172, 173); Orden HFP/886/2023 (Modelo 721) |
| Tax authority | Agencia Estatal de Administración Tributaria (AEAT / Hacienda) |
| Filing portal | Sede Electrónica AEAT (sede.agenciatributaria.gob.es), Renta WEB |
| IRPF filing deadline | 1 April – 30 June of the following year |
| Modelo 721 filing deadline | 1 January – 31 March of the following year |
| EU reporting | DAC8 / CARF — crypto platforms report user data from 2026; Spanish exchanges already report via Modelos 172/173 since 2024 |
| Validated by | Pending — requires sign-off by a Spanish asesor fiscal or economista |
| Skill version | 1.0 |

### Crypto Classification Under IRPF

**Crypto Classification Under IRPF**

| Activity | IRPF Classification | Tax Base |
| --- | --- | --- |
| Buying/selling crypto for fiat | Ganancia/pérdida patrimonial (capital gain/loss) | Base del ahorro (savings) |
| Crypto-to-crypto swap (permuta) | Ganancia/pérdida patrimonial | Base del ahorro (savings) |
| Staking / lending / yield farming rewards | Rendimiento del capital mobiliario | Base del ahorro (savings) |
| Airdrops (no service rendered) | Ganancia patrimonial no derivada de transmisión | Base general (general base) |
| Mining — occasional | Ganancia patrimonial | Base general (general base) |
| Mining / trading — habitual (actividad económica) | Rendimiento de actividades económicas | Base general (general base) |
| Payment for goods/services in crypto | Disposal at market value — ganancia patrimonial | Base del ahorro (savings) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether habitual trading or occasional | Treat as occasional (savings base) unless clear business indicators |
| Unknown cost basis | STOP — cannot compute gain without acquisition cost |
| Unknown whether foreign or Spanish exchange | Assume foreign — check Modelo 721 obligation |
| Unknown residency status | STOP — affects worldwide vs source taxation |
| Unknown whether staking reward or airdrop | Treat as staking reward (savings base — rendimiento del capital mobiliario) |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — transaction history from exchange(s) or wallet(s), confirmation of Spanish tax residency, and indication of whether activity is occasional investment or habitual trading.

**Recommended** — full CSV exports from all exchanges used (Binance, Coinbase, Kraken, Bit2Me, Revolut, etc.), wallet addresses with on-chain history, cost basis records for each acquisition, record of staking/lending/mining activity, and Modelo 721 filing history.

**Ideal** — complete portfolio tracker export (e.g. CoinTracking, Koinly, TaxDown), DeFi protocol interaction history, NFT purchase/sale records, AEAT borrador pre-populated data for cross-checking, and documentation of any token airdrops received.

### Refusal Catalogue

- **R-ESC-1 — Residency unknown** — Spain taxes worldwide income of tax residents. Non-residents are only taxed on Spain-source income. Cannot proceed without confirming tax residency status.
- **R-ESC-2 — No transaction records** — Crypto tax computations require detailed transaction records with dates, amounts, and counterparties. AEAT applies FIFO method across ALL exchanges — without complete records, gains cannot be calculated. Cannot proceed.
- **R-ESC-3 — Corporate crypto holdings** — Companies holding crypto (Impuesto sobre Sociedades) have different accounting and tax treatment. This skill covers individuals (IRPF) only. Escalate to an asesor fiscal.
- **R-ESC-4 — Actividad económica classification disputes** — Whether crypto activity constitutes a business (actividad económica) under Article 27 LIRPF has complex indicators including regularity, infrastructure, and intent. Escalate to a qualified professional.
- **R-ESC-5 — Cross-border DeFi/DAO structures** — Complex DeFi arrangements involving multiple jurisdictions, DAOs, or governance tokens require specialist international tax advice. Escalate.

## Section 3 — Rate Tables

### 3.1 Savings Base (Base del Ahorro) — Rates for 2025

Crypto capital gains and investment income are taxed at progressive rates on the savings base. Rates updated by Ley 7/2024 effective 1 January 2025.

**Savings Base rate table 2025**  _(Ley 7/2024, disposición final séptima, modifying Article 66 LIRPF. Confirmed by AEAT Manual de Renta 2025.)_

| Taxable Savings Income | Rate | Cumulative Tax |
| --- | --- | --- |
| First €6,000 | 19% | €1,140 |
| €6,001 – €50,000 | 21% | €10,380 |
| €50,001 – €200,000 | 23% | €44,880 |
| €200,001 – €300,000 | 27% | €71,880 |
| Over €300,000 | 30% | — |

- **Top rate increase note** — The top rate was increased from 28% to 30% by Ley 7/2024 effective 1 January 2025. The combined rate includes both the state portion (cuota íntegra estatal) and the autonomous community portion (cuota íntegra autonómica).  _(Ley 7/2024, disposición final séptima, modifying Article 66 LIRPF)_

### 3.2 General Base (Base General) — Progressive Rates for 2025

Applies to airdrops (not derived from a transfer), mining income if occasional, and habitual trading classified as actividad económica.

**General Base progressive rates 2025**

| Taxable General Income | Marginal Rate (approx. combined) |
| --- | --- |
| Up to €12,450 | 19% |
| €12,451 – €20,200 | 24% |
| €20,201 – €35,200 | 30% |
| €35,201 – €60,000 | 37% |
| €60,001 – €300,000 | 45% |
| Over €300,000 | 47% |

Exact rates vary by autonomous community. Rates shown are approximate combined state + CCAA.

### 3.3 Wealth Tax (Impuesto sobre el Patrimonio)

- **National exemption threshold** — €700,000 exemption (plus €300,000 for primary residence) EUR
- **Wealth tax rates by CCAA** — 0.2% to 3.5% depending on CCAA. Madrid and Andalusia effectively exempt via 99-100% bonification. Catalonia and Valencia apply full rates.
- **Impuesto Temporal de Solidaridad de Grandes Fortunas (ITSGF)** — Net wealth > €3 million taxed at 1.7%–3.5% regardless of CCAA bonifications. Applies 2022–2024; check status for 2025.

## Section 4 — Cost Basis Methods

### 4.1 FIFO — Mandatory

**FIFO method status table**

| Method | Status |
| --- | --- |
| FIFO (First In, First Out) | **Mandatory** — required by AEAT per DGT consulta V1604-18 |
| LIFO | NOT permitted |
| Average cost | NOT permitted |
| Specific identification | NOT permitted |

- **Critical rule — global FIFO per coin** — FIFO must be applied per type of homogeneous cryptocurrency (e.g. all BTC, all ETH) and consolidated across all exchanges and wallets. You cannot apply FIFO per exchange — it must be a single global FIFO queue per coin.

### 4.2 Cost Basis Components

- **Acquisition cost (valor de adquisición)** — Includes: purchase price in EUR (converted at exchange rate on acquisition date); exchange fees, commissions, and spreads paid on acquisition; network/gas fees directly attributable to the acquisition.
- **Disposal value (valor de transmisión)** — Includes: sale proceeds in EUR (or market value of asset received in a swap); less exchange fees, commissions paid on disposal.

### 4.3 Crypto-to-Crypto Swaps (Permutas)

- **Taxable event on swap** — Every crypto-to-crypto swap is a taxable event (permuta under Article 37.1.h LIRPF). AEAT treats it as a simultaneous disposal of the outgoing crypto and acquisition of the incoming crypto.  _(Article 37.1.h LIRPF)_
- **Swap gain/loss formula** — Disposal value = market value of the crypto received at the time of the swap. Acquisition cost of new crypto = same market value (plus any fees). Gain/loss = disposal value minus FIFO cost basis of the outgoing crypto.  _(Article 37.1.h LIRPF)_

## Section 5 — DeFi, Staking, Mining, and Airdrop Treatment

### 5.1 Staking and Lending Rewards

**Staking and Lending Rewards table**

| Type | Treatment | Tax Base |
| --- | --- | --- |
| Staking rewards (PoS validation) | Rendimiento del capital mobiliario | Base del ahorro — 19%–30% |
| Lending interest (Aave, Compound, etc.) | Rendimiento del capital mobiliario | Base del ahorro — 19%–30% |
| Yield farming rewards | Rendimiento del capital mobiliario | Base del ahorro — 19%–30% |
| Liquidity mining tokens | Rendimiento del capital mobiliario (if passive) or ganancia patrimonial | Context-dependent |

- **Taxable timing and cost basis** — Taxable at market value in EUR on receipt date. Cost basis of received tokens = market value at receipt (for future disposals).

### 5.2 Mining

**Mining treatment table**

| Scenario | Treatment | Tax Base |
| --- | --- | --- |
| Occasional / hobby mining | Ganancia patrimonial no derivada de transmisión | Base general — progressive rates 19%–47% |
| Habitual / commercial mining (actividad económica) | Rendimiento de actividades económicas | Base general — progressive rates, plus alta en Modelo 036, epígrafe IAE 831.9, and RETA registration |

- **Indicators of actividad económica** — Indicators of actividad económica: regular mining operation, dedicated hardware, systematic approach, intent to generate ongoing income (per Article 27 LIRPF).  _(Article 27 LIRPF)_

### 5.3 Airdrops

**Airdrops table**

| Type | Treatment |
| --- | --- |
| Gratuitous airdrop (no action required) | Ganancia patrimonial no derivada de transmisión — base general at progressive rates |
| Airdrop for service (sign-up, referral, task) | Ganancia patrimonial no derivada de transmisión — base general |

- **Taxable timing and cost basis** — Taxable at market value on receipt. Cost basis for future disposal = market value at receipt.

### 5.4 Hard Forks

- **Conservative treatment of hard forks** — No specific AEAT guidance. Conservative treatment: Cost basis of original coin: unchanged. Cost basis of forked coin: €0. Subsequent disposal: full proceeds treated as gain.

## Section 6 — NFT Treatment

NFTs are treated as crypto-assets under Spanish tax law. No separate regime exists.

**NFT Treatment table**

| Activity | Treatment |
| --- | --- |
| Purchase of NFT with crypto | Disposal of crypto (taxable event) + acquisition of NFT |
| Sale of NFT for fiat | Capital gain/loss on savings base |
| Sale of NFT for crypto | Permuta — taxable at market value |
| Creation and sale of NFT (artist) | Actividad económica if habitual — base general |
| NFT royalties | Rendimiento del capital mobiliario or actividad económica depending on regularity |

- **FIFO applies to identical NFTs** — FIFO applies if you hold multiple identical NFTs (e.g. editions from the same collection).

## Section 7 — Reporting Requirements

### 7.1 Modelo 100 — Annual IRPF Return

**Modelo 100 table**

| Section | Content |
| --- | --- |
| Casillas 1800–1814 | Ganancias y pérdidas patrimoniales por transmisión de monedas virtuales — detail each transaction: acquisition date, disposal date, acquisition value, disposal value |
| Casilla 0031 | Rendimientos del capital mobiliario (staking, lending rewards) |
| Casilla 0304/0305 | Pérdidas patrimoniales to offset (if applicable) |

- **Filing** — Filing: 1 April – 30 June of the following year via Renta WEB.

### 7.2 Modelo 721 — Foreign Crypto Declaration

**Modelo 721 table**

| Requirement | Detail |
| --- | --- |
| Obligation | Mandatory when the aggregate value of crypto held on foreign exchanges/custodians exceeds €50,000 as of 31 December |
| Who must file | Spanish tax residents (individuals and entities) |
| Deadline | 1 January – 31 March of the following year |
| Subsequent years | Required again only if there is an increase > €20,000 over the last declared value |
| Penalties | €5,000 per datum omitted or incorrectly reported (minimum €10,000) |
| Legal basis | Ley 11/2021 (disposición adicional 13ª LGT); Orden HFP/886/2023 |

### 7.3 Modelos 172 and 173 — Exchange Reporting

- **Exchange reporting since 2024** — Since 2024, Spanish-registered crypto exchanges (Bit2Me, Bitnovo, Criptan, etc.) must file: Modelo 172: Annual report of client crypto balances. Modelo 173: Annual report of client crypto operations. This means AEAT has independent data to cross-reference against your Modelo 100.

### 7.4 Record-Keeping

**Record-Keeping table**

| Requirement | Detail |
| --- | --- |
| Retention period | 4 years from end of relevant tax year (general prescription period under Article 66 LGT) |
| Records to maintain | Full transaction logs from all exchanges, wallet addresses, global FIFO ledger per coin, staking/mining logs, Modelo 721 copies |
| Burden of proof | On the taxpayer — AEAT can request supporting documentation in an inspection |

## Section 8 — Loss Offset and Carry-Forward

### 8.1 Savings Base Losses

**Savings Base Losses table**

| Rule | Detail |
| --- | --- |
| Same-year offset | Pérdidas patrimoniales on the savings base can offset ganancias patrimoniales on the savings base |
| Cross-category offset (same base) | Up to 25% of rendimientos del capital mobiliario can be offset by capital losses (and vice versa) |
| Carry-forward | Uncompensated losses carry forward for **4 years** |
| Cross-base offset | Savings base losses CANNOT offset general base income |

### 8.2 General Base Losses

**General Base Losses table**

| Rule | Detail |
| --- | --- |
| Same-year offset | Losses on the general base can offset general base income |
| Carry-forward | 4 years |

### 8.3 Anti-Abuse Rule (Norma Antirecompra) — Article 33.5.f LIRPF

- **Re-acquisition rule (2 months)** — Spain has a re-acquisition rule similar to (but distinct from) the US wash sale rule: If you sell a crypto asset at a loss and reacquire the same asset (homogeneous) within 2 months (before or after the sale), the loss is suspended — it cannot be recognised until the replacement asset is itself disposed of outside the 2-month window. For assets traded on a regulated market, the period extends to 1 year (before or after). Most crypto is NOT on a regulated market, so the 2-month rule applies. The suspended loss is not lost — it is added to the cost basis of the replacement asset.  _(Article 33.5.f Ley 35/2006 LIRPF; DGT consulta V1604-18)_

## Section 9 — Anti-Avoidance Rules

### 9.1 General Anti-Abuse Provision (Norma General Antielusión)

- **Article 15 LGT general anti-abuse** — Article 15 of the Ley General Tributaria (LGT) empowers AEAT to disregard arrangements that are: wholly or partly artificial; entered into with the main purpose of obtaining a tax advantage; contrary to the spirit of the legislation. AEAT can recharacterise transactions to reflect their economic substance.  _(Article 15 LGT)_

### 9.2 Specific Crypto Anti-Avoidance

**Specific Crypto Anti-Avoidance table**

| Measure | Detail |
| --- | --- |
| Modelo 721 (foreign holdings) | Failure to declare → €5,000 per datum penalty; unjustified capital gains may be imputed |
| Modelos 172/173 (exchange data) | AEAT receives automatic data from Spanish exchanges since 2024 |
| DAC8 / CARF (from 2026) | Cross-border automatic exchange of crypto data from EU and partner jurisdictions |
| Exit taxation | If you cease to be a Spanish tax resident, unrealised gains on crypto > €4 million may be taxable under exit tax rules (Article 95 bis LIRPF) |
| Impuesto de Solidaridad | Prevents circumventing wealth tax via CCAA bonifications for net wealth > €3 million |

### 9.3 Penalties for Non-Compliance

**Penalties table**

| Violation | Penalty Range |
| --- | --- |
| Failure to file Modelo 100 with crypto | 50%–150% of unpaid tax (sanción grave/muy grave) |
| Failure to file Modelo 721 | €5,000 per datum omitted (minimum €10,000) |
| Late filing | Recargo (surcharge) 1%–20% depending on delay, plus interest |

## Section 10 — Worked Examples

### Example 1 — Buy-and-Sell BTC, Savings Base

**Input:** Spanish tax resident. Bought 1 BTC at €25,000 in February 2025. Sold 1 BTC at €55,000 in October 2025. Exchange fees: €150 on purchase, €200 on sale. No other savings income.

**Computation:**
```
Disposal value:    €55,000 − €200 (sale fee) = €54,800
Acquisition cost:  €25,000 + €150 (purchase fee) = €25,150
Gain:              €54,800 − €25,150 = €29,650

Tax (savings base):
  First €6,000 × 19% =  €1,140
  Next €23,650 × 21% =  €4,966.50
  Total:                 €6,106.50
```

### Example 2 — Crypto-to-Crypto Swap (Permuta)

**Input:** Spanish tax resident. Acquired 10 ETH at €1,200 each in March 2024 (total cost: €12,000). In June 2025, swapped 10 ETH for 0.5 BTC when ETH market price = €3,800 each.

**Computation:**
```
Disposal value of ETH:    10 × €3,800 = €38,000
Acquisition cost (FIFO):  10 × €1,200 = €12,000
Gain on ETH disposal:     €38,000 − €12,000 = €26,000

Tax on €26,000 (savings base):
  First €6,000 × 19% =  €1,140
  Next €20,000 × 21% =  €4,200
  Total:                 €5,340

New cost basis of 0.5 BTC: €38,000 (for future disposal FIFO)
```

### Example 3 — Loss with Re-Acquisition (Anti-Abuse Rule)

**Input:** Spanish tax resident. Sold 2 BTC at €40,000 each on 1 August 2025. FIFO cost basis: €50,000 each. Loss: €20,000. Repurchased 2 BTC at €39,000 each on 15 August 2025 (within 2 months).

**Computation:**
```
Loss on sale:     (€40,000 − €50,000) × 2 = −€20,000
Re-acquisition:   Within 2 months → Article 33.5.f applies
Loss status:      SUSPENDED — cannot be recognised in 2025
New cost basis:   €39,000 + €10,000 (suspended loss per BTC) = €49,000 per BTC

The suspended loss is effectively preserved in the increased
cost basis and will be recognised when the replacement BTC
is disposed of (outside the 2-month window).
```

## Self-Checks

Before delivering any Spain crypto tax computation, verify:

- [ ] Residency confirmed — Spanish tax resident (worldwide income) or non-resident (source only)?
- [ ] FIFO applied globally per coin across ALL exchanges and wallets
- [ ] Every crypto-to-crypto swap treated as a taxable permuta
- [ ] Staking/lending classified as rendimiento del capital mobiliario (savings base)
- [ ] Airdrops classified on general base (not savings base)
- [ ] 2-month anti-abuse rule checked for any loss + re-acquisition
- [ ] Modelo 721 obligation checked (foreign crypto > €50,000 at 31 Dec)
- [ ] Rates reflect Ley 7/2024 update (30% top bracket, not 28%)
- [ ] Wealth tax exposure checked (especially for Catalonia/Valencia residents)
- [ ] Output labelled as estimated — flag for professional review

## PROHIBITIONS

- NEVER use the old top savings rate of 28% — it is 30% from 2025 per Ley 7/2024
- NEVER apply FIFO per-exchange — it must be a single global FIFO queue per coin type
- NEVER ignore crypto-to-crypto swaps — they are ALL taxable events in Spain
- NEVER classify staking rewards on the general base — they go on the savings base as rendimiento del capital mobiliario
- NEVER forget the 2-month re-acquisition anti-abuse rule for losses
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review
- NEVER omit Modelo 721 analysis for clients with foreign exchange holdings
- NEVER advise on CNMV regulatory matters — this skill covers tax only
- NEVER compute gains without verified cost basis and complete FIFO records

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, economista colegiado, or abogado tributarista in Spain) before filing or acting upon.

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
