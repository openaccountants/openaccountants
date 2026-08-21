---
name: italy-crypto-tax
description: Use this skill whenever asked about Italy cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Italy", "tasse crypto Italia", "Bitcoin Italy", "cripto-attività", "cryptocurrency gains Italy", "imposta sostitutiva crypto", "staking Italy", "mining income Italy", "NFT tax Italy", "Quadro RT crypto", "Quadro RW crypto", "IVCA crypto", "Modello Redditi PF crypto", "Coinbase Italy tax", "Binance Italy", "Revolut crypto Italy", "DAC8 Italy", "Legge di Bilancio crypto", or any question about the income tax, capital gains, wealth tax, or reporting obligations for cryptocurrency, tokens, or digital assets for Italian tax residents. Covers Legge di Bilancio 2023 (L. 197/2022) classification, Legge di Bilancio 2025 (L. 207/2024) rate changes, IVCA wealth tax, Quadro RW monitoring, and Quadro RT Section V reporting. ALWAYS read this skill before touching any Italy crypto work.
version: 1.0
jurisdiction: IT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - italy-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italy Crypto Tax

## Italy Crypto / Digital Assets Tax Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Tax | Imposta Sostitutiva on Crypto-Asset Gains + IVCA Wealth Tax |
| Currency | EUR (all values must be in EUR at transaction date) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Art. 67(1)(c-sexies) TUIR (D.P.R. 917/1986), as introduced by Legge di Bilancio 2023 (L. 197/2022, Art. 1 cc. 126--147) |
| 2025 amendments | Legge di Bilancio 2025 (L. 207/2024, Art. 1 cc. 23--29): 26% rate confirmed for 2025, €2,000 exemption abolished, 33% from 2026, revaluation at 18% |
| Tax authority | Agenzia delle Entrate (Revenue Agency) |
| Filing form | Modello Redditi PF (Persone Fisiche) |
| Filing portal | Agenzia delle Entrate online (agenziaentrate.gov.it) |
| Filing deadline | 31 October of the following year (electronic); 30 June (paper via Poste Italiane) |
| EU reporting | DAC8 / CARF — crypto exchanges report user data to Agenzia delle Entrate from 2026 |
| Validated by | Pending — requires sign-off by an Italian commercialista |
| Skill version | 1.0 |

### Tax Rate Summary (2025)

**Tax Rate Summary (2025)**

| Item | Rate / Threshold |
| --- | --- |
| Capital gains flat tax (imposta sostitutiva) | **26%** on all net crypto gains |
| De minimis exemption | **None** — abolished from 1 January 2025 (was €2,000 until 31 December 2024) |
| IVCA (crypto wealth tax) | **0.2%** per annum on value at 31 December (pro-rata if held part-year) |
| Cost basis revaluation option | FMV at 1 January 2025 with **18%** substitute tax |
| From 2026 | Rate rises to **33%** (except 26% for MiCAR-compliant euro e-money tokens) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown cost basis | STOP — cannot compute gain without acquisition cost |
| Unknown residency | STOP — Italy taxes worldwide income only for tax residents |
| Token classification unclear | Treat as cripto-attività under Art. 67(1)(c-sexies) TUIR (taxable) |
| Unsure whether gains exceed thresholds | Compute precisely — no de minimis exemption from 2025 |
| Unsure about IVCA | Assume IVCA due unless held via Italian intermediary that withholds |

## Section 2 -- Classification Rules

### 2.1 Cripto-Attività Under Italian Law

- **cripto-attività** — A digital representation of value or rights that can be transferred and stored electronically using distributed ledger technology, per EU MiCA Regulation (EU) 2023/1114, Art. 3(1)(5).  _(Legge di Bilancio 2023 (L. 197/2022); EU MiCA Regulation (EU) 2023/1114, Art. 3(1)(5))_

**Asset Classification Table**

| Asset Type | Classification | Tax Treatment |
| --- | --- | --- |
| Cryptocurrencies (BTC, ETH, SOL, etc.) | Cripto-attività | 26% imposta sostitutiva on gains |
| Utility tokens | Cripto-attività | 26% imposta sostitutiva on gains |
| Security / financial tokens | Cripto-attività (unless qualifying as traditional securities) | 26% imposta sostitutiva; if traditional security, standard financial income rules |
| Stablecoins (non-euro, e.g. USDT, USDC) | Cripto-attività | 26% imposta sostitutiva on gains |
| Euro e-money tokens (MiCAR-compliant) | Cripto-attività (special sub-class) | 26% from 2025; remains 26% from 2026 (exempted from 33% increase per L. 199/2025) |
| NFTs | Cripto-attività | Same 26% regime; creation and sale by artist = business income |

### 2.2 Taxable Events

**Taxable Events Table**

| Event | Taxable? | Notes |
| --- | --- | --- |
| Crypto → fiat (sell) | Yes | Gain = proceeds − cost basis |
| Crypto → crypto (swap) | Yes | Each swap is a disposal at FMV |
| Crypto → goods/services | Yes | Disposal at FMV of goods/services received |
| Receiving crypto as payment | Yes | Income at FMV when received |
| Transfer between own wallets | No | No change in beneficial ownership |
| Wrapping/unwrapping (ETH → WETH) | Depends | Generally not taxable if no economic change; conservative: taxable |
| Hard fork (receiving new coin) | Not a taxable event on receipt | Cost basis = €0; taxable on disposal |

## Section 3 -- Rate Tables and Computation

### 3.1 Capital Gains (Plusvalenze) — Imposta Sostitutiva

- **Legal basis** — D.Lgs. 461/1997, Arts. 5--7, applied to Art. 67(1)(c-sexies) TUIR.  _(D.Lgs. 461/1997, Arts. 5--7)_

**Rate Table**

| Tax Year | Rate | De Minimis Exemption | Citation |
| --- | --- | --- | --- |
| 2023--2024 | 26% | First €2,000 of gains exempt | L. 197/2022, Art. 1 c. 126 |
| **2025** | **26%** | **None (abolished)** | L. 207/2024, Art. 1 c. 23 |
| 2026 onwards | 33% (general); 26% (euro e-money tokens) | None | L. 207/2024, Art. 1 c. 24; L. 199/2025 |

- **Computation formula** — Net gain = Σ(disposal proceeds − cost basis) for all crypto disposals in the year Tax due = Net gain × 26%  _(L. 207/2024, Art. 1 c. 23)_
- **Net loss result** — If net result is a loss, no tax is due and the loss can be carried forward (see Section 8).

### 3.2 IVCA — Crypto Wealth Tax

- **Legal basis** — D.L. 201/2011, Art. 19 c. 18, as amended by L. 197/2022, Art. 1 c. 146.  _(D.L. 201/2011, Art. 19 c. 18; L. 197/2022, Art. 1 c. 146)_

**IVCA Parameters Table**

| Parameter | Value |
| --- | --- |
| Rate | 0.2% per annum (2 per mille) |
| Taxable base | Market value of all crypto holdings as at 31 December |
| Pro-rata | If held for part of year, proportional to days held / 365 |
| Minimum threshold | IVCA not due if calculated amount < €12 |
| Who pays | Italian tax residents holding crypto anywhere (self-custody, foreign exchanges, etc.) |
| Exemption | Not due if held via Italian intermediary that applies and withholds the equivalent stamp duty (imposta di bollo) |
| Payment | Via Modello F24, codes 1727 (tax), 1728 (interest), 1729 (penalties) |

### 3.3 Cost Basis Revaluation (Rivalutazione)

- **Legal basis and revaluation rule** — L. 207/2024, Art. 1 cc. 26--29. Taxpayers may elect to revalue the cost basis of crypto held as at 1 January 2025 to fair market value on that date, by paying an 18% substitute tax on the revalued amount. This replaces the previous 14% revaluation option for holdings at 1 January 2023 (L. 197/2022).  _(L. 207/2024, Art. 1 cc. 26--29)_

**Revaluation Parameters Table**

| Parameter | Value |
| --- | --- |
| Reference date | 1 January 2025 |
| Substitute tax rate | 18% of FMV at reference date |
| Payment deadline | 30 November 2025 (or in up to 3 equal annual instalments from 30 November 2025) |
| Interest on instalments | 3% per annum on 2nd and 3rd instalments |
| Effect | New cost basis = FMV at 1 January 2025 for future disposals |

## Section 4 -- Cost Basis Methods

**Cost Basis Methods Table**

| Method | Status | Notes |
| --- | --- | --- |
| LIFO (Last In, First Out) | **Default** under Art. 67(1-bis) TUIR for financial assets | Standard method for Italian tax purposes |
| Specific identification | Acceptable if clearly documented | Must be consistently applied |
| Average cost | Not standard for Italian tax purposes | Not recommended |
| FIFO | Not the default | May be used if declared and consistently applied |

- **Cost basis includes** — Purchase price in EUR (converted at ECB rate on transaction date); Exchange/trading fees and commissions; Network/gas fees directly attributable to the acquisition; Any substitute tax paid for revaluation (added to revalued basis)

## Section 5 -- DeFi, Staking, Mining, and Airdrops

**DeFi/Staking/Mining/Airdrops Table**

| Activity | Tax Treatment | Timing | Notes |
| --- | --- | --- | --- |
| Mining (private, occasional) | Income at FMV when received (redditi diversi) | At receipt | If habitual → business income (reddito d'impresa) |
| Mining (business/commercial) | Business income (partita IVA required) | At receipt | Subject to IRPEF + IRAP + social contributions |
| Staking rewards | Income at FMV when received | At receipt | Cost basis of received tokens = FMV at receipt |
| DeFi lending interest | Income at FMV when received | At receipt | Treated as redditi diversi |
| Liquidity provision | Adding to pool = potential disposal; LP tokens = new acquisition | At each event | Impermanent loss: no specific guidance; conservative = non-deductible |
| Airdrops (gratuitous) | Taxable at FMV when received if linked to any economic activity | At receipt | Purely unsolicited airdrops may have €0 cost basis → full gain on disposal |
| Airdrops (service-related) | Income at FMV when received | At receipt | E.g. rewards for testing, referrals |
| Yield farming | Income at FMV when received | At receipt | Each token receipt is a taxable moment |

## Section 6 -- NFT Treatment

**NFT Treatment Table**

| Scenario | Treatment |
| --- | --- |
| Purchase of NFT | Acquisition at cost — cost basis for future disposal |
| Sale of NFT for profit | Capital gain taxed at 26% (2025); same regime as other cripto-attività |
| Creation and sale (artist/creator) | Business income if habitual (reddito d'impresa or reddito di lavoro autonomo); occasional = redditi diversi |
| NFT → NFT swap | Taxable event — each side valued at FMV |
| NFT royalties (smart contract) | Income at FMV when received |
| VAT on NFT sales | Electronically supplied service — standard VAT rate (22%) may apply on B2C within EU |

## Section 7 -- Reporting Requirements

### 7.1 Modello Redditi PF — Annual Tax Return

**Modello Redditi PF Reporting Table**

| Form Section | Purpose | Who Must File |
| --- | --- | --- |
| **Quadro RT, Sezione V** | Report capital gains and losses from cripto-attività | Anyone who disposed of crypto during the year |
| **Quadro RW** | Monitor all crypto holdings (foreign and domestic, including self-custody wallets) | All Italian residents holding crypto at any point during the year |
| **Quadro RW — IVCA section** | Calculate and declare IVCA (0.2% wealth tax) | All Italian residents with crypto holdings as at 31 December |
| **Quadro RL** | Report other crypto income (staking, mining, airdrops) if classified as redditi diversi | Those receiving crypto income not classified as capital gains |

### 7.2 Filing Deadlines

**Filing Deadlines Table**

| Filing Method | Deadline |
| --- | --- |
| Electronic (via Agenzia delle Entrate) | **31 October** of the following year |
| Paper (via Poste Italiane, limited eligibility) | **30 June** of the following year |
| Late filing (within 90 days) | Valid but subject to penalties |
| Late filing (>90 days) | Considered omitted — penalties + tax collection |

### 7.3 IVCA Payment

**IVCA Payment Table**

| Method | Detail |
| --- | --- |
| Payment vehicle | Modello F24 |
| Code | 1727 (IVCA tax), 1728 (interest), 1729 (penalties) |
| Deadline | Same as balance due for Modello Redditi PF (30 June, or 31 July with 0.4% surcharge) |

### 7.4 DAC8 / CARF (from 2026)

- **DAC8/CARF reporting** — From 1 January 2026, crypto-asset service providers (CASPs) licensed under MiCA operating in the EU are required to automatically report Italian clients' transaction data to the Agenzia delle Entrate under the DAC8 Directive (EU) 2023/2226 and the OECD CARF framework. This means the Italian tax authority will receive independent data to cross-reference against taxpayer declarations.  _(DAC8 Directive (EU) 2023/2226; OECD CARF framework)_

## Section 8 -- Loss Offset and Carry-Forward

- **Legal basis** — D.Lgs. 461/1997, Art. 68(5), applied to cripto-attività.  _(D.Lgs. 461/1997, Art. 68(5))_

**Loss Offset and Carry-Forward Table**

| Rule | Detail |
| --- | --- |
| Netting within year | Crypto losses offset crypto gains within the same tax year |
| Cross-asset netting | From 2025 (Redditi PF 2025), crypto losses can offset gains from other financial assets in the same imposta sostitutiva regime (Art. 67 TUIR) |
| Carry-forward | Net crypto losses can be carried forward for **4 years** |
| Carry-back | Not permitted |
| Documentation | Losses must be properly declared in Quadro RT to be carried forward |
| Losses from revaluation | If revaluation substitute tax was paid and asset is subsequently sold at a loss, the revalued amount is the cost basis |

## Section 9 -- Anti-Avoidance Rules

**Anti-Avoidance Rules Table**

| Rule | Description |
| --- | --- |
| Abuse of law (Art. 10-bis L. 212/2000) | General anti-avoidance principle applies to crypto transactions lacking economic substance |
| Controlled Foreign Company (CFC) | If crypto is held through a CFC in a low-tax jurisdiction, CFC rules may attribute income to the Italian resident |
| Transfer pricing | Applicable if crypto transactions occur between related parties or entities |
| Exit tax | Italian residents moving abroad may trigger exit taxation on unrealised crypto gains (Art. 166 TUIR) |
| Beneficial ownership | Agenzia delle Entrate may look through nominee arrangements |
| Wash sale | No specific anti-wash-sale rule, but abuse of law principle could apply to artificial loss generation |

## Section 10 -- Worked Examples

### Example 1 -- Simple Buy and Sell (2025)

**Input:** Italian tax resident. Bought 1 BTC at €30,000 in February 2025. Sold 1 BTC at €55,000 in September 2025. Exchange fees: €150 total.

**Computation:**
```
Disposal proceeds:          EUR 55,000
Cost basis:                 EUR 30,000 + EUR 150 fees = EUR 30,150
Capital gain:               EUR 24,850
De minimis exemption:       None (abolished from 2025)
Imposta sostitutiva (26%):  EUR 24,850 × 0.26 = EUR 6,461
IVCA:                       Not due (no crypto held at 31 December)
```

**Reporting:** Quadro RT, Sezione V. Tax paid via Modello F24 by 30 June 2026.

### Example 2 -- Multiple Trades with Loss Carry-Forward

**Input:** Italian tax resident. In 2025:
- Bought 5 ETH at €2,000 each in January (total €10,000).
- Sold 3 ETH at €1,500 each in April (total €4,500 — loss).
- Sold 2 ETH at €3,500 each in November (total €7,000 — gain).

**Computation (LIFO):**
```
Trade 1 (April disposal of 3 ETH):
  Proceeds: 3 × EUR 1,500 = EUR 4,500
  Cost basis (LIFO): 3 × EUR 2,000 = EUR 6,000
  Loss: EUR -1,500

Trade 2 (November disposal of 2 ETH):
  Proceeds: 2 × EUR 3,500 = EUR 7,000
  Cost basis (LIFO): 2 × EUR 2,000 = EUR 4,000
  Gain: EUR 3,000

Net position 2025:   EUR 3,000 - EUR 1,500 = EUR 1,500 net gain
Imposta sostitutiva:  EUR 1,500 × 0.26 = EUR 390
```

### Example 3 -- IVCA Calculation

**Input:** Italian tax resident holds 2 BTC on Binance (foreign exchange) throughout 2025. Value at 31 December 2025: €100,000.

**Computation:**
```
IVCA base:       EUR 100,000
Rate:            0.2%
IVCA due:        EUR 100,000 × 0.002 = EUR 200
```

**Reporting:** Quadro RW (monitoring + IVCA). Paid via Modello F24.

## Self-Checks

Before finalising any Italy crypto tax computation:

- [ ] Confirmed taxpayer is Italian tax resident (worldwide income obligation)
- [ ] All disposals identified (including crypto-to-crypto swaps)
- [ ] Cost basis verified with transaction records (LIFO applied unless otherwise declared)
- [ ] No de minimis exemption applied for 2025 (abolished)
- [ ] IVCA computed on 31 December holdings (including self-custody wallets)
- [ ] Staking/mining/airdrop income included as redditi diversi
- [ ] Quadro RW completed for all crypto holdings (domestic and foreign)
- [ ] Quadro RT Sezione V completed for all capital gains/losses
- [ ] Any carried-forward losses from prior years applied correctly
- [ ] Revaluation election evaluated if pre-2025 holdings exist

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista, consulente del lavoro, or equivalent licensed practitioner in Italy) before filing or acting upon.

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
