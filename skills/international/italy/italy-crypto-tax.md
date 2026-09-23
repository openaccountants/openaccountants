---
name: italy-crypto-tax
description: Use this skill whenever asked about Italy cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Italy", "tasse crypto Italia", "Bitcoin Italy", "cripto-attività", "cryptocurrency gains Italy", "imposta sostitutiva crypto", "staking Italy", "mining income Italy", "NFT tax Italy", "Quadro RT crypto", "Quadro RW crypto", "IVCA crypto", "Modello Redditi PF crypto", "Coinbase Italy tax", "Binance Italy", "Revolut crypto Italy", "DAC8 Italy", "Legge di Bilancio crypto", or any question about the income tax, capital gains, wealth tax, or reporting obligations for cryptocurrency, tokens, or digital assets for Italian tax residents. Covers Legge di Bilancio 2023 (L. 197/2022) classification, Legge di Bilancio 2025 (L. 207/2024) rate changes, IVCA wealth tax, Quadro RW monitoring, and Quadro RT Section V reporting. ALWAYS read this skill before touching any Italy crypto work.
version: 1.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - italy-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Crypto-asset tax in Italy (cripto-attività)

How Italy taxes an individual resident on crypto-assets held privately: the substitute tax on gains and other income, the end of the old yearly threshold, the 2025 step-up of cost, the yearly tax on the value of crypto held (reported in Quadro RW), reporting in the Modello Redditi PF, staking and mining. It is not for crypto held in a business. Figures are for tax year 2026. The rates are read from the Budget Laws on Normattiva, with Legge 207/2024 read as in force on 30 June 2026. The return instructions used are the Redditi PF 2026 instructions (Fascicolo 2), which cover tax year 2025, the latest published; the 2027 edition for tax year 2026 was not yet out.

## Italy Crypto / Digital Assets Tax Guide

## Section 1: Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Tax | Imposta sostitutiva on crypto gains and other crypto income, plus the yearly imposta sul valore delle cripto-attività |
| Currency | EUR |
| Tax year | Calendar year (1 January to 31 December) |
| Primary legislation | Art. 67(1)(c-sexies) and art. 68(9-bis) TUIR (D.P.R. 917/1986), inserted by Legge 197/2022 art. 1 commi 126 to 147 |
| Later changes | Legge 207/2024 art. 1 commi 23 to 29 (threshold removed from 2025, rate change from 2026, step-up at 1 January 2025); Legge 199/2025 art. 1 comma 28 (euro e-money tokens) |
| New TUIR | D.Lgs. 117/2026 applies only from 1 January 2027. For 2026 income the rules below still apply, even where Normattiva's current view marks them "abrogato" |
| Tax authority | Agenzia delle Entrate |
| Filing form | Modello Redditi PF: Quadro RT (gains), Quadro RW (holdings and the yearly value tax) |
| Filing deadline | Online by 31 October of the following year (D.P.R. 322/1998 art. 2), see Section 7.2 |
| Validated by | Pending. Requires sign-off by an Italian commercialista |

### Tax Rate Summary (2026)

**Rates on crypto income (Legge 199/2025 art. 1 comma 28)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199 |
| Ordinary substitute tax on crypto gains and other crypto income realised from 1 January 2026 | 33% | "in luogo di quella ordinaria del 33 per cento" |
| Rate kept for euro-denominated e-money tokens (held, sold or used) | 26% | "si applicano con l'aliquota del 26 per cento" |

**Rate up to 2025, threshold removed, step-up (Legge 207/2024 art. 1 commi 23 to 28)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207 |
| General substitute tax on financial "redditi diversi" (it applied to crypto until 2025, and still applies to other financial gains) | 26% | "è pari al 26 per cento" |
| Old yearly minimum below which crypto gains were not taxed. Deleted from 2025: there is no threshold in 2026 | EUR 2,000 | "non inferiori complessivamente a 2.000 euro nel periodo d'imposta" |
| One-off substitute tax to step up the cost of crypto held on 1 January 2025 | 18% | "nella misura del 18 per cento" |
| Interest on the second and third instalments of that step-up tax | 3% | "nella misura del 3 per cento annuo" |

The 33% applies from 1 January 2026 under comma 24 of Legge 207/2024, read as in force on 30 June 2026: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207!vig=2026-06-30 ("realizzati a decorrere dal 1° gennaio 2026"). The yearly value tax is 2 per mille of the value, see Section 3.2.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown cost | The law says the cost must be documented "con elementi certi e precisi"; without it the cost is zero (art. 68(9-bis) TUIR). Ask for records before computing |
| Unknown residency | STOP. These rules are for Italian tax residents |
| Token classification unclear | Treat as a cripto-attività under art. 67(1)(c-sexies) TUIR, unless it is a financial instrument (security token), see Section 2.1 |
| Unsure whether gains are small enough to ignore | There is no threshold from 2025. Every gain counts |
| Unsure about the value tax | Assume it is due for crypto on which no Italian intermediary applied stamp duty (imposta di bollo) |

## Section 2: Classification Rules

### 2.1 Cripto-Attività Under Italian Law

- **cripto-attività.** "Una rappresentazione digitale di valore o di diritti che possono essere trasferiti e memorizzati elettronicamente, utilizzando la tecnologia di registro distribuito o una tecnologia analoga" (art. 67(1)(c-sexies) TUIR): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art67!vig=2026-06-30
- Agenzia Circolare 30/E of 27 October 2023 says security tokens that are MiFID II financial instruments are NOT under letter c-sexies; they follow the ordinary rules for capital income and financial "redditi diversi". Tokenised shares stay shares. Derivatives on crypto (CFDs, futures) fall under letter c-quater: https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf

**Asset Classification Table** (rates: the tables in Section 1)

| Asset Type | Classification | Tax Treatment |
| --- | --- | --- |
| Cryptocurrencies (BTC, ETH, SOL, etc.) | Cripto-attività | Ordinary crypto rate |
| Utility tokens | Cripto-attività | Ordinary crypto rate on sale. Using the right to buy the product at a discount is not income (Circolare 30/E) |
| Security / financial tokens | Financial instrument if it meets the MiFID II definition, otherwise cripto-attività | Financial instrument: ordinary rules for financial income, not this Guide |
| Stablecoins that are not euro e-money tokens (for example USDT, USDC) | Cripto-attività | Ordinary crypto rate |
| Euro e-money tokens (MiCA art. 3(1)(7)) | Cripto-attività with its own rate, but only tokens whose value is stably pegged to the euro and whose reserve funds are held entirely in euro assets with entities authorised in the EU (Legge 199/2025 comma 28) | The euro e-money token rate. Converting euro to these tokens, or redeeming them in euro at face value, is not a gain or loss (Legge 199/2025 comma 28) |
| NFTs | Cripto-attività when sold by a holder | Ordinary crypto rate. Sale by the author of the work: see Section 6 |

### 2.2 Taxable Events

The law and Circolare 30/E (links in Section 2.1) settle the swap rules. Other rows are legacy practice that no allowed page confirms; they are marked.

**Taxable Events Table**

| Event | Taxable? | Notes |
| --- | --- | --- |
| Crypto to euro (sell) | Yes | Gain = amount received less cost (art. 68(9-bis) TUIR) |
| Crypto to crypto with the same characteristics and functions (for example BTC to ETH, NFT to NFT) | No | "Non costituisce una fattispecie fiscalmente rilevante". The cost of the old coin carries over to the new one (Circolare 30/E) |
| Crypto to crypto with different characteristics and functions (for example crypto to NFT) | Yes | Disposal at the normal value of what is received, read on the platform where the swap happened (Circolare 30/E) |
| Crypto to an e-money token | Yes | Circolare 30/E: a swap into an e-money token is taxable |
| Crypto to an asset-referenced token | No | Circolare 30/E: not a taxable swap |
| Crypto to goods or services | Yes | A disposal ("cessione a titolo oneroso") |
| Loss or theft of private keys | No | Circolare 30/E: not a tax event, so no deductible loss |
| Transfer between own wallets | No | Legacy, not confirmed on an allowed page |
| Wrapping or unwrapping (ETH to WETH) | Unclear | Legacy view. Test it against the same-characteristics rule; no official page read addresses it |
| Hard fork (receiving a new coin) | Unclear | Legacy view: not taxed on receipt, taxed on sale. No official page read addresses it |

**Swap example from Circolare 30/E** (the figures are the Agenzia's own example)

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf |
| Cost of 20 BTC held; 5 of them are swapped for 10 ETH | EUR 2,000 | "valore di acquisto di euro 2.000" |
| Cost given to the 10 ETH (equal to the cost of the 5 BTC given up); no tax on the swap | EUR 500 | "un valore di acquisto di euro 500" |

## Section 3: Rate Tables and Computation

### 3.1 Capital Gains (Plusvalenze): Imposta Sostitutiva

- **Legal basis.** Art. 67(1)(c-sexies) and art. 68(9-bis) TUIR; the substitute tax of D.Lgs. 461/1997 arts. 5 to 7 applies at the rate set by Legge 207/2024 comma 24 (tables in Section 1).
- **Computation.** Gain = amount received (or the normal value of the crypto received in a taxable swap) less the cost. Gains and losses of the year are added together. Income from simply holding crypto (for example staking) is taxed in full "senza alcuna deduzione" (art. 68(9-bis) TUIR, link in Section 2.1).
- **No threshold.** From 2025 every gain is taxed; the old threshold in the Legge 207/2024 table applied only to disposals up to 31 December 2024.
- **Net loss result.** No tax. The loss is carried forward (Section 8).

**Rate Table**

| Tax Year | Rate | Threshold | Citation |
| --- | --- | --- | --- |
| 2023 to 2024 | 26% | Gains not taxed if the year's total was below EUR 2,000 | Legge 197/2022; see the Legge 207/2024 table |
| 2025 | 26% | None | Legge 207/2024 commi 23 and 25 |
| 2026 | 33% (ordinary); 26% (euro e-money tokens) | None | Legge 207/2024 comma 24; Legge 199/2025 comma 28 |

### 3.2 IVCA: Crypto Wealth Tax

The official name is the **imposta sul valore delle cripto-attività** ("imposta sulle cripto-attività" in the return). "IVCA" is an informal label. It is not IVAFE: it sits in the same Quadro RW, with its own code (21) and columns.

- **Legal basis.** D.L. 201/2011 art. 19 commi 18 to 22, as amended by Legge 197/2022 art. 1 comma 146: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art19!vig=2026-06-30
- It replaces the stamp duty (imposta di bollo) for crypto on which no Italian intermediary applied it. Crypto kept with an Italian intermediary bears stamp duty instead, applied by the intermediary.
- D.L. 201/2011 art. 19 comma 20-bis sets a higher yearly rate from 2024 for financial products held in tax havens. The return instructions give only the 2 per mille rate for crypto; whether the higher rate reaches crypto held in a tax haven is not settled here. Refer.

**IVCA Parameters Table** (Redditi PF 2026 instructions, Fascicolo 2, Quadro RW)

| Parameter | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026 |
| Rate | 2 per mille a year of the value | "nella medesima misura (prevista per l’imposta di bollo) del 2 per mille" |
| Taxable base | Value at 31 December on the exchange where the crypto was bought; else a comparable platform or specialist price site; failing that, cost. If sold during the year, the value at the end of the holding | "La base imponibile è costituita dal valore delle cripto-attività al termine di ciascun anno solare" |
| Part-year or joint holding | In proportion to days held and to the share owned | "in proporzione ai giorni di detenzione e alla quota di possesso" |
| Who pays | Every resident holding crypto on which stamp duty was not applied, not only those with Quadro RW monitoring duties | "sulle quali non è stata applicata l’imposta di bollo" |
| Foreign wealth tax | Credit for a wealth tax paid finally abroad on the same crypto | "versata a titolo definitivo nello Stato estero" |
| Not paid if the amount due is not above | EUR 12 | "non supera 12 euro" |
| Payment | Modello F24, code 1727 (balance); acconti with codes 1728 (first) and 1729 (second), on the IRPEF dates | "codici tributo 1728 (primo acconto) e 1729 (secondo acconto)" |

### 3.3 Cost Basis Revaluation (Rivalutazione)

- **Legal basis and rule.** Legge 207/2024 art. 1 commi 26 to 29. For each cripto-attività held on 1 January 2025, the value on that date (art. 9 TUIR) could replace the cost, if that value bore the one-off substitute tax in the Legge 207/2024 table. An earlier option at 1 January 2023 (Legge 197/2022 comma 133) used a lower rate; Circolare 30/E describes it.
- **It is closed for new elections.** The payment date has passed. For 2026 disposals it matters only if the client elected it.

**Revaluation Parameters Table**

| Parameter | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207 |
| Reference date | 1 January 2025 | "alla data del 1° gennaio 2025" |
| Substitute tax | 18% of the value at that date | "nella misura del 18 per cento" |
| Payment | 30 November 2025, or up to three equal yearly instalments from that date | "entro il 30 novembre 2025" |
| Interest on later instalments | 3% a year | "nella misura del 3 per cento annuo" |
| Effect | The value at 1 January 2025 becomes the cost. It does NOT allow usable losses | "non consente il realizzo di minusvalenze utilizzabili" |

The step-up is declared in Quadro RT, Section XI (rows RT118 and RT119) of the Redditi PF 2026 instructions.

## Section 4: Cost Basis Methods

No allowed page read sets a matching method (LIFO, FIFO or average) for crypto. The live Guide said LIFO is the default under art. 67(1-bis) TUIR; that paragraph concerns foreign currencies, not crypto, so the claim is removed. Circolare 30/E's own swap example (Section 2.2) gives the swapped coins a proportional share of the cost. The adopting accountant must settle the method.

**Cost Basis Methods Table**

| Method | Status | Notes |
| --- | --- | --- |
| LIFO (Last In, First Out) | Not confirmed for crypto | Art. 67(1-bis) TUIR is about foreign currencies |
| Specific identification | Not confirmed | Document it and apply it consistently |
| Average cost | Not confirmed | Circolare 30/E's swap example allocates cost proportionally |
| FIFO | Not confirmed | Document it and apply it consistently |

- **Cost includes.** The purchase price in euro, documented "con elementi certi e precisi"; without documents the cost is zero. Inherited crypto: the value for inheritance tax. Gifted crypto: the donor's cost (art. 68(9-bis) TUIR).
- **Fees are NOT added.** The law is silent, but Circolare 30/E says art. 68(9-bis), unlike the rule for financial assets (art. 68(6)), does not let the costs of buying and selling crypto be counted. The live Guide added fees and gas to the cost; that is against the Agenzia's position.

## Section 5: DeFi, Staking, Mining, and Airdrops

**DeFi/Staking/Mining/Airdrops Table**

| Activity | Tax Treatment | Timing | Notes |
| --- | --- | --- | --- |
| Staking rewards | "Proventi derivanti dalla detenzione" under letter c-sexies, at the crypto rate | When received | Taxed on the GROSS reward, before the platform's cut, with no deduction (art. 68(9-bis) TUIR; Circolare 30/E) |
| Mining (private) | Not settled on an allowed page | Unclear | Circolare 30/E covers mining only for VAT (outside VAT when the network pays automatically). The income tax treatment needs the accountant |
| Mining (business) | Business income, legacy view | Not confirmed | Legacy: VAT number, IRPEF, IRAP and contributions. Not confirmed on an allowed page |
| DeFi lending interest | Probably income from holding crypto, legacy view | When received | Not confirmed on an allowed page |
| Liquidity provision | Legacy view: adding to a pool may be a disposal; LP tokens are a new asset | At each event | Test against the same-characteristics swap rule. No official guidance read |
| Airdrops | Not settled on an allowed page | Unclear | Legacy said taxable when linked to an activity; no page read confirms it |
| Yield farming | Legacy view: income when received | When received | Not confirmed on an allowed page |

## Section 6: NFT Treatment

**NFT Treatment Table** (Circolare 30/E, link in Section 2.1, unless marked)

| Scenario | Treatment |
| --- | --- |
| Purchase of NFT | Acquisition. The price is the cost for a later sale |
| Sale of NFT already issued, by a holder | Letter c-sexies gain at the crypto rate (Section 1) |
| Sale by the author of the work | Not letter c-sexies. Self-employment income (art. 53(2)(b) TUIR) if done as a profession, or art. 67(1)(l) TUIR if occasional, unless it is business income |
| NFT to NFT swap | Not taxable (same characteristics and functions) |
| Crypto to NFT | Taxable swap |
| NFT royalties (smart contract) | Legacy view: income when received. Not confirmed on an allowed page |
| VAT on NFT sales | Circolare 30/E section 3.7.1.3 deals with it case by case. Refer; see `italy-vat-return` |

## Section 7: Reporting Requirements

### 7.1 Modello Redditi PF: Annual Tax Return

Source for this section: the Redditi PF 2026 instructions, Fascicolo 2 (link in Section 3.2), and D.L. 167/1990 art. 4: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1990-06-28;167~art4!vig=2026-06-30

**Modello Redditi PF Reporting Table**

| Form Section | Purpose | Who Must File |
| --- | --- | --- |
| **Quadro RT, Section V-A (rows RT41 to RT45)** | Gains and other income from cripto-attività, including income from holding (staking). In the Redditi PF 2026 instructions this section covers income realised by 31 December 2025 at the old rate; the rows for 2026 income will be set by the 2027 edition | Anyone who realised crypto income in the year, where no intermediary taxed it |
| **Quadro RT, Section XI** | The 1 January 2025 step-up | Those who elected it |
| **Quadro RW** | Monitoring: residents who hold crypto-attività in the year must report them (D.L. 167/1990 art. 4(1)). Not required for assets kept with, or contracts made through, Italian resident intermediaries, if the intermediary applied withholding or substitute tax to the income from them (art. 4(3)) | Residents, including beneficial owners |
| **Quadro RW: code 21, row RW8** | Compute the imposta sul valore delle cripto-attività | Residents holding crypto on which no stamp duty was applied, even if not otherwise required to monitor |
| **Quadro RL** | Legacy said staking and mining go here. The instructions put staking in Quadro RT. Use Quadro RL only if the accountant decides an item is not letter c-sexies income | Confirm with the accountant |

### 7.2 Filing Deadlines

Source: D.P.R. 322/1998 art. 2: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30

**Filing Deadlines Table**

| Filing Method | Deadline |
| --- | --- |
| Online | 15 April to **31 October** of the following year |
| Paper, at a post office (only where allowed) | 15 April to **30 June** of the following year |
| Late filing (within 90 days) | Valid, with penalties for the delay |
| Late filing (over 90 days) | Treated as omitted, but still a basis for collecting the tax |

### 7.3 IVCA Payment

**IVCA Payment Table**

| Method | Detail |
| --- | --- |
| Payment vehicle | Modello F24 |
| Codes | 1727 (balance), 1728 (first acconto), 1729 (second acconto). The live Guide said 1728 and 1729 were interest and penalties; the instructions say they are the acconti |
| Deadline | Same dates and acconto rules as IRPEF (instructions, link in Section 3.2). For the IRPEF dates and the late-payment surcharge see `it-income-tax` |

### 7.4 DAC8 / CARF (from 2026)

- **DAC8/CARF reporting.** The EU directive on crypto reporting (DAC8, Directive (EU) 2023/2226) makes crypto-asset service providers report their clients' transactions for automatic exchange between tax authorities, mirroring the OECD's Crypto-Asset Reporting Framework. Circolare 30/E says Member States had to transpose it by 31 December 2025. The Italian implementing rules and start date were not read on an allowed page. Expect the Agenzia to hold independent data to match against returns.

## Section 8: Loss Offset and Carry-Forward

- **Legal basis.** Art. 68(9-bis) TUIR (link in Section 2.1).

**Loss Offset and Carry-Forward Table**

| Rule | Detail |
| --- | --- |
| Netting within year | Letter c-sexies gains and losses of the year are added together |
| Cross-asset netting | Not supported by the pages read. Art. 68(9-bis) nets crypto gains with crypto losses ("relative minusvalenze"). The live Guide's claim that crypto losses offset other financial gains from 2025 is removed |
| Carry-forward | An excess of losses is deducted from crypto gains of later years, "ma non oltre il quarto", only if it is shown in the return for the year of the loss |
| Old threshold and losses | For losses on disposals up to 31 December 2024, only the part above the old threshold could be carried; from 2025 the whole loss counts (instructions, Quadro RT Section V-A) |
| Carry-back | Not provided for |
| Losses after the step-up | The step-up does not allow usable losses (Legge 207/2024 comma 29, Section 3.3) |
| Lost or stolen keys | Not a deductible loss (Circolare 30/E) |

## Section 9: Anti-Avoidance Rules

Legacy content. None of these rows was checked on an allowed page for crypto.

**Anti-Avoidance Rules Table**

| Rule | Description |
| --- | --- |
| Abuse of law (Art. 10-bis L. 212/2000) | General anti-avoidance principle applies to crypto transactions lacking economic substance |
| Controlled Foreign Company (CFC) | If crypto is held through a CFC in a low-tax jurisdiction, CFC rules may attribute income to the Italian resident |
| Transfer pricing | Applicable if crypto transactions occur between related parties or entities |
| Exit tax | Legacy cited art. 166 TUIR; that article covers business assets. Whether a private holder faces exit tax on crypto was not confirmed. Refer |
| Beneficial ownership | Quadro RW duties extend to beneficial owners (D.L. 167/1990 art. 4(1)) |
| Wash sale | No specific anti-wash-sale rule found, but the abuse of law principle could apply to artificial losses |

## Section 10: Worked Examples

The live Guide's examples used invented amounts and added fees to cost. They are replaced by worked steps; take every rate from the linked tables.

### Example 1: Simple Buy and Sell (2026)

A resident buys 1 BTC in February 2026 and sells it for euro in September 2026.

1. Gain = sale price less the documented purchase price. Do NOT add exchange fees (Section 4).
2. There is no threshold, so the whole gain is taxed.
3. Apply the ordinary 2026 rate in the Legge 199/2025 table (Section 1).
4. Report in Quadro RT, Section V-A. Nothing is held at 31 December, but the BTC was held during the year: the value tax is due for the days held unless stamp duty was applied, and Quadro RW monitoring applies unless it was kept with an Italian intermediary that taxed the income (Section 7.1).

### Example 2: Multiple Trades with Loss Carry-Forward

In 2026 a resident sells some ETH at a loss in April and more ETH at a gain in November, and swaps BTC for ETH in June.

1. The June BTC to ETH swap is not taxed; the ETH takes the BTC's cost (the Circolare 30/E example in Section 2.2).
2. Net the April loss and the November gain.
3. If the result is a gain, apply the 2026 rate. If a loss, report it in Quadro RT for 2026 to carry it forward up to the fourth later year.
4. The matching method for which ETH was sold is not settled (Section 4). Record the method used.

### Example 3: IVCA Calculation

A resident holds 2 BTC on a foreign exchange all year.

1. Base: value at 31 December on the exchange where the BTC was bought (Section 3.2).
2. Tax = base times 2 per mille, times the days held over the year, times the share owned.
3. Less any foreign wealth tax paid finally on the same crypto.
4. Report in Quadro RW (code 21, row RW8). Pay by F24 with code 1727 if the amount due is above the minimum in the Section 3.2 table.

## The method, step by step

1. **Confirm residence and scope.** These rules cover residents holding crypto privately (art. 67(1)(c-sexies) TUIR): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art67!vig=2026-06-30
2. **List every event of 2026.** Sales for euro, taxable swaps (different characteristics and functions, or into euro e-money tokens), payments in crypto, staking and other income from holding. Drop same-characteristics swaps (Circolare 30/E): https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf
3. **Compute gains and losses** under art. 68(9-bis) TUIR, with documented cost, no fees, the 1 January 2025 step-up where elected, and prior losses carried forward: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art68!vig=2026-06-30
4. **Apply the rate.** Ordinary 2026 rate, or the euro e-money token rate, per Legge 199/2025 comma 28: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199
5. **Fill Quadro RT and Quadro RW** of the Modello Redditi PF, including the value tax (code 21, row RW8), following the instructions: https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026 (tax year 2025 edition; use the 2027 edition for tax year 2026 when it is published).
6. **File online by 31 October 2027** (D.P.R. 322/1998 art. 2): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30 and pay by F24 on the IRPEF dates (codes in Section 7.3).

## Ask the client first

- Were you an Italian tax resident for 2026, and did you hold the crypto privately or through a business, company or trust?
- Which of your crypto is kept with an Italian intermediary (bank, broker or exchange that applies stamp duty or withholds tax), and which is on foreign platforms or in your own wallet?
- Do you have documents proving what you paid for each coin? Did you inherit or receive any as a gift?
- Did you step up your cost at 1 January 2025 (or at 1 January 2023), and are instalments still due?
- Which tokens are euro e-money tokens, and which swaps were into stablecoins, NFTs or other tokens with different functions?
- Do you have losses from 2022 to 2025 shown in earlier returns?

## When to refuse or refer

- Crypto held in a business, by a company, or mining as an activity: business income rules, not this Guide.
- Security tokens and derivatives on crypto (CFDs, futures): financial income rules.
- Non-residents, people moving in or out of Italy in the year, or exit tax questions.
- DeFi, liquidity pools, airdrops, hard forks and wrapping where no official guidance settles the treatment: refer to a commercialista.
- Crypto never declared in earlier years (the regularisation of Legge 197/2022 is closed; penalties need a professional).
- NFT creators and VAT on NFT or crypto services.
- Any income realised from 2027, when the new TUIR (D.Lgs. 117/2026) applies.

## Self-Checks

Before finalising any Italy crypto tax computation:

- [ ] Confirmed taxpayer is an Italian tax resident
- [ ] All taxable events identified, and same-characteristics swaps left out
- [ ] Cost documented for each disposal; no fees added
- [ ] No threshold applied for 2025 or 2026
- [ ] 2026 rate from the Legge 199/2025 table; euro e-money tokens separated
- [ ] Staking income taxed gross
- [ ] Value tax computed for crypto without stamp duty, by days held
- [ ] Quadro RW completed where monitoring applies
- [ ] Quadro RT Section V-A completed for all gains, losses and income from holding
- [ ] Carried-forward losses applied, within four years
- [ ] Step-up at 1 January 2025 checked if the client elected it

## Sources

- Legge 199/2025: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199
- Legge 207/2024: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207
- Legge 207/2024 as in force on 30 June 2026: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207!vig=2026-06-30
- TUIR art. 67: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art67!vig=2026-06-30
- TUIR art. 68: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art68!vig=2026-06-30
- D.L. 201/2011 art. 19: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art19!vig=2026-06-30
- D.L. 167/1990 art. 4: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1990-06-28;167~art4!vig=2026-06-30
- D.P.R. 322/1998 art. 2: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30
- Agenzia delle Entrate, Circolare 30/E of 27 October 2023: https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf
- Agenzia delle Entrate, Redditi PF 2026 instructions, Fascicolo 2: https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista, consulente del lavoro, or equivalent licensed practitioner in Italy) before filing or acting upon.

> Contributed by OpenAccountants.

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
