---
name: italy-crypto-tax
description: Use this skill whenever asked about Italy cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Italy", "tasse crypto Italia", "Bitcoin Italy", "cripto-attività", "cryptocurrency gains Italy", "imposta sostitutiva crypto", "staking Italy", "mining income Italy", "NFT tax Italy", "Quadro RT crypto", "Quadro RW crypto", "IVCA crypto", "Modello Redditi PF crypto", "Coinbase Italy tax", "Binance Italy", "Revolut crypto Italy", "DAC8 Italy", "Legge di Bilancio crypto", or any question about the income tax, capital gains, wealth tax, or reporting obligations for cryptocurrency, tokens, or digital assets for Italian tax residents. Covers Legge di Bilancio 2023 (L. 197/2022) classification, Legge di Bilancio 2025 (L. 207/2024) rate changes, IVCA wealth tax, Quadro RW monitoring, and Quadro RT Section V reporting. ALWAYS read this skill before touching any Italy crypto work.
version: 1.1
jurisdiction: IT
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - it-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Crypto-asset tax in Italy (cripto-attività) v1.1

Tax year **2026**, private holdings of Italian resident individuals. This Guide computes ordinary crypto gains/income and the annual crypto-value tax, identifies the special euro e-money-token rate, and distinguishes income, monitoring and wealth-tax duties. Outputs are working papers for a commercialista; they do not carry accountant attestation.

**Year boundary:** Redditi PF **2026** instructions report **2025** income. Their form coordinates below are historical reference points, not published 2027 fields. The current statutory **2026** rates override older rates and thresholds in Circolare 30/E/2023 or a return instruction. D.Lgs. 117/2026, annex article 377, applies the new income-tax code from **1 January 2027**; use the provisions in force for the relevant income period ([annex art.377](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117:1~art377!vig=2026-10-29)).

## Who this applies to

Confirm residence, private/business capacity, token rights, contracts and tax arrangements before computing. This Guide covers private crypto within TUIR article 67(1)(c-sexies), not company/business income, PE attribution, financial instruments or residence/exit-tax analysis. It does not assume that an unclassified token is an ordinary coin merely because it uses a blockchain.

- **cripto-attività.** "Una rappresentazione digitale di valore o di diritti che possono essere trasferiti e memorizzati elettronicamente, utilizzando la tecnologia di registro distribuito o una tecnologia analoga" (art. 67(1)(c-sexies) TUIR): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art67!vig=2026-06-30
- Agenzia Circolare 30/E of 27 October 2023 says security tokens that are MiFID II financial instruments are NOT under letter c-sexies; they follow the ordinary rules for capital income and financial "redditi diversi". Tokenised shares stay shares. Derivatives on crypto (CFDs, futures) fall under letter c-quater: https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf

**Asset Classification Table** (rates: the tables in Rates, bands and thresholds)

| Asset Type | Classification | Tax Treatment |
| --- | --- | --- |
| Cryptocurrencies (BTC, ETH, SOL, etc.) | Cripto-attività | Ordinary crypto rate |
| Utility tokens | Cripto-attività | Ordinary crypto rate on sale. Using the right to buy the product at a discount is not income (Circolare 30/E) |
| Security / financial tokens | Financial instrument if it meets the MiFID II definition, otherwise cripto-attività | Financial instrument: ordinary rules for financial income, not this Guide |
| Stablecoins that do not satisfy the euro e-money-token exception | Cripto-attività | Ordinary crypto rate |
| Euro e-money tokens (MiCA art. 3(1)(7)) | Cripto-attività with its own rate, but only tokens whose value is stably pegged to the euro and whose reserve funds are held entirely in euro assets with entities authorised in the EU (Legge 199/2025 comma 28) | The euro e-money token rate. Converting euro to these tokens, or redeeming them in euro at face value, is not a gain or loss (Legge 199/2025 comma 28) |
| NFTs | Cripto-attività when sold by a holder | Ordinary crypto rate. Sale by the author of the work: see Staking, NFTs and excluded activities |

## Rates, bands and thresholds

Figures apply to **2026** unless explicitly labelled as historical election/return information.

| What | Value | Note | Official source |
| --- | --- | --- | --- |
| Ordinary substitute tax on crypto gains and other crypto income realised from 1 January 2026 | 33% | "in luogo di quella ordinaria del 33 per cento" | [Law 199/2025 art. 1(28)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-10-29) |
| Rate kept for euro-denominated e-money tokens (held, sold or used) | 26% | "si applicano con l'aliquota del 26 per cento" | [Law 199/2025 art. 1(28)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-10-29) |

| What | Value | Note | Official source |
| --- | --- | --- | --- |
| General substitute tax on financial "redditi diversi" (it applied to crypto until 2025, and still applies to other financial gains) | 26% | "è pari al 26 per cento" | [Law 207/2024 art. 1(23)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |
| Old yearly minimum below which crypto gains were not taxed. Deleted from 2025: there is no threshold in 2026 | EUR 2,000 | "non inferiori complessivamente a 2.000 euro nel periodo d'imposta" | [Law 207/2024 art. 1(25)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |
| One-off substitute tax to step up the cost of crypto held on 1 January 2025 | 18% | "nella misura del 18 per cento" | [Law 207/2024 art. 1(26)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |
| Interest on the second and third instalments of that step-up tax | 3% | "nella misura del 3 per cento annuo" | [Law 207/2024 art. 1(28)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |

The **33%** ordinary rate applies to income realised from **1 January 2026**. The **26%** exception requires a token stably pegged to the euro with reserves entirely in euro-denominated assets at EU-authorised entities. Mere conversion between euro and such tokens, and redemption in euro at face value, is not a gain/loss. This does not exempt a crypto-to-e-money-token disposal ([Law 207/2024 art.1(24), as amended by Law 199/2025 art.1(28)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29)). The old **EUR 2,000** threshold was deleted from 2025; it is not a 2026 allowance. For 2023–2024 disposals or loss origins, retain the historical-year evidence rather than applying 2026 rules retrospectively.

**Annual crypto-value tax** (DL 201/2011 art.19; PF2 Quadro RW; form coordinates are for 2025 income)

| Parameter | Value | Note | Official source |
| --- | --- | --- | --- |
| Rate | 2 per mille a year of the value | "nella medesima misura (prevista per l’imposta di bollo) del 2 per mille" | [PF2 Quadro RW](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) |
| Taxable base | Value at 31 December on the exchange where the crypto was bought; else a comparable platform or specialist price site; failing that, cost. If sold during the year, the value at the end of the holding | "La base imponibile è costituita dal valore delle cripto-attività al termine di ciascun anno solare" | [PF2 Quadro RW](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) |
| Part-year or joint holding | In proportion to days held and to the share owned | "in proporzione ai giorni di detenzione e alla quota di possesso" | [PF2 Quadro RW](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) |
| Who pays | Every resident holding crypto on which stamp duty was not applied, not only those with Quadro RW monitoring duties | "sulle quali non è stata applicata l’imposta di bollo" | [PF2 Quadro RW](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) |
| Foreign wealth tax | Credit for a wealth tax paid finally abroad on the same crypto | "versata a titolo definitivo nello Stato estero" | [PF2 Quadro RW](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) |
| Not paid if the amount due is not above | EUR 12 | "non supera 12 euro" | [PF2 Quadro RW](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) |
| Payment | Modello F24, code 1727 (balance); acconti with codes 1728 (first) and 1729 (second), on the IRPEF dates | "codici tributo 1728 (primo acconto) e 1729 (secondo acconto)" | [PF2 Quadro RW](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) |

**Closed 2025 step-up election** (Law 207/2024 art.1(26)–(29))

| Parameter | Value | Note | Official source |
| --- | --- | --- | --- |
| Reference date | 1 January 2025 | "alla data del 1° gennaio 2025" | [Law 207/2024 art. 1(26)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |
| Substitute tax | 18% of the value at that date | "nella misura del 18 per cento" | [Law 207/2024 art. 1(26)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |
| Payment | 30 November 2025, or up to three equal yearly instalments from that date | "entro il 30 novembre 2025" | [Law 207/2024 art. 1(27)–(28)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |
| Interest on later instalments | 3% a year | "nella misura del 3 per cento annuo" | [Law 207/2024 art. 1(28)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |
| Effect | The value at 1 January 2025 becomes the cost. It does NOT allow usable losses | "non consente il realizzo di minusvalenze utilizzabili" | [Law 207/2024 art. 1(29)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29) |

## The base

### Taxable events and gains

Apply TUIR article 67(1)(c-sexies) and Circolare 30/E sections 3–3.1. Unresolved events are listed under Sources, not given a default tax result.

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

**Swap example from Circolare 30/E** (the figures are the Agenzia's own example)

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf |
| Cost of 20 BTC held; 5 of them are swapped for 10 ETH | EUR 2,000 | "valore di acquisto di euro 2.000" |
| Cost given to the 10 ETH (equal to the cost of the 5 BTC given up); no tax on the swap | EUR 500 | "un valore di acquisto di euro 500" |

Gain is proceeds received (or the normal value of crypto received in a taxable swap) less documented acquisition cost. For the current year, add **crypto gains and other crypto proceeds**, including holding income measured gross, and algebraically net the relative crypto losses. Measuring staking gross prevents a deduction for platform fees/retention; it does not prohibit this current-year category-level loss netting. Excess losses carry forward for at most **four** subsequent periods, against subsequent crypto gains, only if declared for their origin year. **Do not offset c-sexies crypto income against the financial-income categories c through c-quinquies** (Circolare 30/E section 3.2.1, pp. 54–55). No carry-back is established here. Inherited cost is the succession-tax value; gifted cost is the donor's cost. Undocumented cost is **zero**, so request records first ([TUIR art.68(9-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art68!vig=2026-10-29); [PF2 section V-A](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026)).

### Historical losses: keep three periods separate

- **2023–2024 c-sexies origins:** the historical EUR 2,000 excess limit applies to the eligible carried loss, as described in PF2 section V-A. Do not apply it to a 2025 or 2026 origin.
- **From 2025:** the EUR 2,000 gain/loss threshold is removed by Law 207/2024 article 1(25); the current crypto loss/carry-forward conditions above apply.
- **Operations before 1 January 2023:** Circolare 30/E's transitional section 3.2, printed pages 51–52, applies article 68(5)/(6) and its separate financial-income loss bucket, with the stated four-year carry and origin-return condition. This Guide does not compute those transitional balances. Obtain the origin records and refer the classification; do not treat a 2022 transitional loss as a 2023–2024 c-sexies loss subject to the EUR 2,000 excess rule.

### Acquisition-cost records and fees

Do **not** add exchange fees, gas fees or other acquisition/disposal costs to the statutory crypto basis. AdE expressly distinguishes article 68(9-bis) from the financial-asset rule allowing incidental costs. It also taxes income from holding, including staking, **gross**, without deductions, including amounts retained by the platform ([Circolare 30/E pp.50–51](https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf)).

For multiple crypto-assets **of the same denomination in the private declarative regime**, use **LIFO**: the most recently acquired units are disposed of first. This is the express instruction in Circolare 30/E section 3.2.1, printed pages 54–55. It is not an assumption imported from the financial-asset wording of article 67(1-bis). The **administered regime** has a separate weighted-average rule in section 3.2.2. Confirm the actual regime, denomination, acquisition dates and quantities before assigning cost. The official swap illustration above preserves the transferred cost; later disposals follow the applicable regime's matching rule.

### Staking, NFTs and excluded activities

Staking is income from holding within letter c-sexies and is taxed gross on receipt. Circolare 30/E treats an issued NFT sold by its holder within the crypto rules; its example of an NFT/NFT swap falls under same-characteristics/functions treatment, while crypto/NFT swaps are taxable. For an author's own work, the circular distinguishes professional self-employment, occasional activity and business income. **Refer creators and NFT royalties/VAT** for their own classification; do not apply this holder computation to them ([Circolare 30/E pp.44–51 and section3.7.1.3](https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf)).

### Annual crypto-value tax and stamp duty

The official name is **imposta sul valore delle cripto-attività**; “IVCA” is shorthand and the tax is distinct from IVAFE, although reported in Quadro RW. It substitutes for stamp duty where no Italian intermediary applied that duty. Confirm actual stamp-duty treatment. It can be due even if the holder has no separate monitoring duty ([DL 201/2011 art.19(18)–(22)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art19!vig=2026-10-29); [PF2 Quadro RW](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026)).

Use year-end value on the purchase exchange; if unavailable use a comparable platform or specialist market-price source, otherwise cost. For assets no longer held at 31 December, use end-of-holding value. Prorate by days and ownership, then deduct the final foreign wealth tax on the same assets, capped at the Italian tax. The 2026 year has 365 days. The crypto rate printed by the instructions is **2 per mille**; the application of the separate increased tax-haven financial-product rate to crypto is not resolved here.

### Existing step-up elections

- **Legal basis and rule.** Legge 207/2024 art. 1 commi 26 to 29. For each cripto-attività held on 1 January 2025, the value on that date (art. 9 TUIR) could replace the cost, if that value bore the one-off substitute tax in the Legge 207/2024 table. An earlier option at 1 January 2023 (Legge 197/2022 comma 133) used a lower rate; Circolare 30/E describes it.
- **It is closed for new elections.** The payment date has passed. For 2026 disposals it matters only if the client elected it.

The statutory 2025 election date was 30 November 2025, subject to applicable non-working-day rules; no new 2026 election is created by that provision. Existing instalments continue under the elected schedule with **3% annual interest** on later instalments. The increased basis cannot generate usable losses. The earlier 1 January 2023 election is retained as a prior-cost-record question, not a new election. In PF 2026/2025-income, the 2025 step-up is shown in section XI, rows RT118/RT119; check successor fields at filing ([Law 207/2024 art.1(26)–(29)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29); [PF2 section XI](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026)).

## Deadlines and filing

### Modello Redditi PF: Annual Tax Return

Source for this section: the Redditi PF 2026 instructions, Fascicolo 2 (link in Annual crypto-value tax and stamp duty), and D.L. 167/1990 art. 4: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1990-06-28;167~art4!vig=2026-06-30

**Modello Redditi PF Reporting Table**

| Form Section | Purpose | Who Must File |
| --- | --- | --- |
| **Quadro RT, Section V-A (rows RT41 to RT45)** | Gains and other income from cripto-attività, including income from holding (staking). In the Redditi PF 2026 instructions this section covers income realised by 31 December 2025 at the old rate; the rows for 2026 income will be set by the 2027 edition | Anyone who realised crypto income in the year, where no intermediary taxed it |
| **Quadro RT, Section XI** | The 1 January 2025 step-up | Those who elected it |
| **Quadro RW** | Monitoring: residents who hold crypto-attività in the year must report them (D.L. 167/1990 art. 4(1)). Not required for assets kept with, or contracts made through, Italian resident intermediaries, if the intermediary applied withholding or substitute tax to the income from them (art. 4(3)) | Residents, including beneficial owners |
| **Quadro RW: code 21, row RW8** | Compute the imposta sul valore delle cripto-attività | Residents holding crypto on which no stamp duty was applied, even if not otherwise required to monitor |
| **Quadro RL** | Do not automatically put staking here: published PF 2026 instructions place letter c-sexies income in Quadro RT. A different income classification requires its own review | Mining/other categories not settled here |

### Filing Deadlines

Source: D.P.R. 322/1998 art. 2: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30

**Filing Deadlines Table**

| Filing Method | Deadline |
| --- | --- |
| Online | Statutory 15 April–31 October of the following year, with applicable non-working-day extensions; do not treat 31 October 2027 as an unadjusted final date |
| Paper, at a post office (only where allowed) | 15 April to **30 June** of the following year |
| Late filing (within 90 days) | Valid, with penalties for the delay |
| Late filing (over 90 days) | Treated as omitted, but still a basis for collecting the tax |

### IVCA Payment

**IVCA Payment Table**

| Method | Detail |
| --- | --- |
| Payment vehicle | Modello F24 |
| Codes | 1727 (balance), 1728 (first acconto), 1729 (second acconto). The live Guide said 1728 and 1729 were interest and penalties; the instructions say they are the acconti |
| Deadline | Same dates and acconto rules as IRPEF (instructions, link in Annual crypto-value tax and stamp duty). For the IRPEF dates and the late-payment surcharge see `it-income-tax` |

**All RT/RW section, row, column and code references above describe the published PF 2026 form for 2025 income.** They are not confirmed fields of the future PF 2027 form for 2026. The law still requires annual reporting; verify the actual successor form before filing. The bank-account monitoring exemption does not create a crypto de-minimis exemption (DL 167/1990 art.4). Monitoring concerns holdings during the year, not only 31 December balances.

## Penalties and interest

Keep monitoring and tax violations separate. Under the legislation applicable through 2026, **DL 167/1990 art.5(2)** sets an ordinary monitoring penalty of **3%–15% of undeclared amounts**, **6%–30%** for the specifically listed tax-haven foreign-investment/foreign-financial-asset cases, and **EUR 258** for the monitoring declaration filed within **90 days**. Do not apply the doubled territorial range to every crypto wallet without checking the statutory classification and location ([DL 167/1990 art.5(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1990-06-28;167~art5!vig=2026-10-29)).

For tax payments, **D.Lgs. 471/1997 art.13(1)** starts at **25%** of unpaid tax, halved within **90 days**, with further **1/15 per day** reduction of the halved amount within **15 days**, before voluntary-correction relief. Ordinary unfaithful income declarations start at **70%**, minimum **EUR 150**, subject to special conditions and adjustments. The penalty-code transition begins **1 January 2027**. These are through 2026 provisions, not a conclusion about a 2026-income return violation committed in 2027. Detailed filing omissions, voluntary correction, interest and any applicable successor rules require the actual violation facts; use `it-income-tax` and `it-estimated-tax` and obtain the specialist calculation ([D.Lgs. 471/1997 art.13](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-29); [art.1](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-29); [D.Lgs. 173/2024 annex art.102](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig=2026-10-29)).

## Cross-border points

Italian-resident monitoring duties include beneficial owners under DL 167/1990 article4(1). The resident-intermediary exemption requires the statutory management/intervention and tax-withholding/substitute-tax conditions in article4(3); the fact that an exchange has an Italian name or registration does not prove the exemption. A foreign platform/self-custody position requires its own monitoring and value-tax review. A resident's final foreign wealth tax on the same crypto can credit the value tax only up to that tax. Do not net unrelated foreign income tax against it.

Non-residents, residence changes, entities, CFC attribution, tax-treaty treatment and business exit/transfer-pricing rules need separate analysis. The scope limits of `it-cross-border` and `it-income-tax` apply. DAC8/CARF implementation is not used here to change the taxpayer's own reporting duty.

## Two worked examples that recompute

### Example 1: ordinary private disposal

Assume a resident in the **private declarative regime** owns two same-denomination units: one older unit with documented cost **EUR 6,000**, and one newer unit costing **EUR 7,000**. The resident sells **one unit for EUR 10,000** in 2026, with no eligible losses or step-up. LIFO assigns the newer EUR 7,000 cost, giving **EUR 3,000 gain** and **EUR 990** tax at 33%. Assume exchange fees are EUR 100; they are not deducted from the gain. The retained older unit keeps its own cost. Check monitoring/value tax separately for the actual holdings.

```oa-check
name: Italy 2026 declarative crypto LIFO, no fee deduction
inputs:
  proceeds: 10000
  newest_lot_documented_cost: 7000
steps:
  gain: proceeds - newest_lot_documented_cost
  substitute_tax: gain * 0.33
expected:
  gain: 3000
  substitute_tax: 990
```

### Example 2: part-year joint holding and foreign wealth-tax credit

Assume the relevant platform value is **EUR 40,000**, the resident owns **50%** for **183 days of 2026**, no stamp duty was applied, and **EUR 5** final foreign wealth tax on these same assets qualifies for credit. Gross value tax is EUR 40,000×0.002×183/365×50%=EUR 20.05479. The credit is capped at that amount; net tax rounded to cents is **EUR 15.05**, above the EUR 12 non-payment amount. This example excludes prior payments/credits and tests time, share and credit; the eventual F24 balance must also account for actual advances and return credits.

```oa-check
name: Italy2026 crypto-value tax, part-year share and capped foreign credit
inputs:
  platform_value: 40000
  holding_days: 183
  ownership_share: 0.5
  qualifying_foreign_wealth_tax: 5
steps:
  gross_value_tax: platform_value * 0.002 * holding_days / 365 * ownership_share
  credit: min(qualifying_foreign_wealth_tax, gross_value_tax)
  net_value_tax: round(max(0, gross_value_tax - credit), 2)
expected:
  gross_value_tax: 20.05479
  credit: 5
  net_value_tax: 15.05
```

### Preserved qualitative scenarios

#### Legacy scenario 1: Simple buy and sell (2026)

A resident buys 1 BTC in February 2026 and sells it for euro in September 2026.

1. Gain = sale price less the documented purchase price. Do NOT add exchange fees (Acquisition-cost records and fees).
2. There is no threshold, so the whole gain is taxed.
3. Apply the ordinary 2026 rate in the Legge 199/2025 table (Rates, bands and thresholds).
4. Report in the applicable 2026-income return fields; PF 2026/2025-income uses Quadro RT section V-A. Nothing is held at 31 December, but the BTC was held during the year: the value tax is due for the days held unless stamp duty was applied, and Quadro RW monitoring applies unless it was kept with an Italian intermediary that taxed the income (Deadlines and filing).

#### Legacy scenario 2: Multiple Trades with Loss Carry-Forward

In 2026 a resident sells some ETH at a loss in April and more ETH at a gain in November, and swaps BTC for ETH in June.

1. The June BTC to ETH swap is not taxed; the ETH takes the BTC's cost (the Circolare 30/E example in Taxable events and gains).
2. Net the April loss and the November gain.
3. If the result is a gain, apply the 2026 rate. If a loss, report it in Quadro RT for 2026 to carry it forward up to the fourth later year.
4. In the private declarative regime, assign the cost of same-denomination ETH disposed of using LIFO under Circolare 30/E section 3.2.1. If an intermediary applies the administered regime, use that regime's separate matching rule.

#### Legacy scenario 3: IVCA Calculation

A resident holds 2 BTC on a foreign exchange all year.

1. Base: value at 31 December on the exchange where the BTC was bought (Annual crypto-value tax and stamp duty).
2. Tax = base times 2 per mille, times the days held over the year, times the share owned.
3. Less any foreign wealth tax paid finally on the same crypto.
4. Report in the applicable 2026-income return fields; PF 2026/2025-income uses Quadro RW code 21,row RW8. Pay by F24 with code 1727 if the amount due is above the minimum in the Annual crypto-value tax and stamp duty table.

## Ask the client first

- Were you an Italian tax resident for 2026, and did you hold the crypto privately or through a business, company or trust?
- Which of your crypto is kept with an Italian intermediary (bank, broker or exchange that applies stamp duty or withholds tax), and which is on foreign platforms or in your own wallet?
- Do you have documents proving what you paid for each coin? Did you inherit or receive any as a gift?
- Did you step up your cost at 1 January 2025 (or at 1 January 2023), and are instalments still due?
- Which tokens are euro e-money tokens, and which swaps were into stablecoins, NFTs or other tokens with different functions?
- Do you have losses from 2022 to 2025 shown in earlier returns?

### Referral gates

- Crypto held in a business, by a company, or mining as an activity: business income rules, not this Guide.
- Security tokens and derivatives on crypto (CFDs, futures): financial income rules.
- Non-residents, people moving in or out of Italy in the year, or exit tax questions.
- DeFi, liquidity pools, airdrops, hard forks and wrapping where no official guidance settles the treatment: refer to a commercialista.
- Crypto never declared in earlier years (the regularisation of Legge 197/2022 is closed; penalties need a professional).
- NFT creators and VAT on NFT or crypto services.
- Any income realised from 2027, when the new TUIR (D.Lgs. 117/2026) applies.

### Self-checks

Before finalising any Italy crypto tax computation:

- [ ] Confirmed taxpayer is an Italian tax resident
- [ ] All taxable events identified, and same-characteristics swaps left out
- [ ] Cost documented for each disposal; no fees added; private declarative same-denomination lots matched by LIFO
- [ ] No threshold applied for 2025 or 2026
- [ ] 2026 rate from the Legge 199/2025 table; euro e-money tokens separated
- [ ] Staking measured gross; current-year c-sexies gains/proceeds/losses netted without financial-category offset
- [ ] Value tax computed for crypto without stamp duty, by days held
- [ ] Quadro RW completed where monitoring applies
- [ ] Correct income-year return fields used for gains, losses and holding income; PF 2026 coordinates are for 2025 only
- [ ] Loss origins separated: pre-2023 transition, 2023–2024 threshold, and from-2025 crypto losses; eligible carry applied within four years
- [ ] Step-up at 1 January 2025 checked if the client elected it

## Sources

| Source and provision | Official URL | Read on |
| --- | --- | --- |
| Law 199/2025 art.1(28), euro e-money tokens | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-10-29 | 2026-10-29 |
| Law 207/2024 art.1(23)–(29), current consolidated text | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-29 | 2026-10-29 |
| TUIR art.67(1)(c-sexies),2026 text | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art67!vig=2026-10-29 | 2026-10-29 |
| TUIR art.68(9-bis),2026 text | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art68!vig=2026-10-29 | 2026-10-29 |
| DL 201/2011 art.19(18)–(22) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art19!vig=2026-10-29 | 2026-10-29 |
| DL 167/1990 art.4, monitoring | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1990-06-28;167~art4!vig=2026-10-29 | 2026-10-29 |
| DL 167/1990 art.5(2), monitoring penalties | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1990-06-28;167~art5!vig=2026-10-29 | 2026-10-29 |
| DPR 322/1998 art.2, filing/90 days | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art2!vig=2026-10-29 | 2026-10-29 |
| AdE Circolare 30/E/2023 pp.44–51, administered-regime discussion, monitoring/value-tax and NFT VAT sections; historical rates overridden | https://www.agenziaentrate.gov.it/portale/documents/20143/5589638/Circolare+criptoattivita+del+27+ottobre+2023.pdf | 2026-10-29 |
| AdE Redditi PF 2026 Fascicolo 2,RTV-A,XI,RW (2025-income form only) | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026 | 2026-10-29 |
| D.Lgs. 117/2026 annex art.377 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117:1~art377!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 173/2024 annex art.102 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 471/1997 art.1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 471/1997 art.13 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-29 | 2026-10-29 |

**Not yet confirmed:** transfers between own wallets, wrapping/unwrapping, hard-fork receipt/disposal, private/business mining income classification, DeFi lending, liquidity provision/LP tokens, airdrops and yield farming (their former proposed timing/treatments are not applied); NFT smart-contract royalties and current creator/VAT computations; exact application of the increased tax-haven value-tax rate to crypto; carry-back and computation of the separate pre-2023 transitional financial-loss bucket; crypto-specific application of general abuse-of-law, CFC, transfer-pricing, private-holder exit and wash-sale rules; Italian DAC8/CARF implementing provisions/operational dates; successor 2027 form fields, penalty provisions, interest and income-code cross-references. Prior undeclared holdings and the closed 2022 regularisation need specialist correction advice. These are explicit referrals, not default tax assumptions.

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
