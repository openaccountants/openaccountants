---
name: de-capital-gains
description: "German tax on private investment income and gains for a resident individual, tax year 2026. Covers the 25% flat tax (Abgeltungsteuer) with the 5.5% solidarity surcharge and the church-tax formula, bank withholding (Kapitalertragsteuer), the Sparer-Pauschbetrag of EUR 1,000 or EUR 2,000, the share-loss pot and the general pot, loss certificates, funds and ETFs (Teilfreistellung, Vorabpauschale, Basiszins), large holdings of 1% or more under § 17 with the partial-income method, private sales under § 23 (one-year and ten-year rules, the EUR 1,000 Freigrenze), the Günstigerprüfung and Anlage KAP. Trigger on: Abgeltungsteuer, Kapitalertragsteuer, Sparer-Pauschbetrag, Freistellungsauftrag, Verlustbescheinigung, Teilfreistellung, Vorabpauschale, Spekulationsfrist, sell shares Germany, German capital gains. Out of scope: crypto detail (de-crypto-tax), the exit tax (leaving-germany-exit-tax), non-residents (de-non-resident-tax), treaty withholding (de-treaty-withholding-rates), assets in a business (de-einkommensteuer-freelancer)."
version: 1.2
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-28
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - de-self-employed-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Capital gains tax in Germany (Abgeltungsteuer and private sales), 2026

## Who this applies to

An individual fully liable to German tax (home or habitual abode in Germany) who holds investments privately, not in a business. Tax year 2026 is the calendar year. Figures are read from the consolidated federal law on gesetze-im-internet.de and from finance ministry (BMF) letters.

Sort every asset into one of three regimes first. They do not mix: flat-tax losses cannot offset private-sales gains, and the other way round.

| Regime | What falls in it | How it is taxed | Law |
| --- | --- | --- | --- |
| Flat tax (Abgeltungsteuer) | Interest, dividends, gains on shares, bonds, funds and ETFs, derivatives | 25% plus solidarity surcharge and church tax, normally withheld by the German bank | [§ 20](https://www.gesetze-im-internet.de/estg/__20.html), [§ 32d EStG](https://www.gesetze-im-internet.de/estg/__32d.html) |
| Large shareholding | Shares in a company where the seller held at least 1% at any time in the last five years | Partial-income method at the normal progressive rate | [§ 17 EStG](https://www.gesetze-im-internet.de/estg/__17.html) |
| Private sales | Crypto and other assets sold within one year; land and buildings sold within ten years | Normal progressive rate, nothing withheld | [§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html) |

Out of scope here: assets held in a business or company (de-einkommensteuer-freelancer, de-corporate-tax), non-residents (de-non-resident-tax), crypto staking, lending, mining and DeFi (de-crypto-tax), and the exit tax in detail (leaving-germany-exit-tax).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Flat tax on private investment income | 25% | 2026 | https://www.gesetze-im-internet.de/estg/__32d.html |
| Bank withholding (Kapitalertragsteuer) | 25% of the income | 2026 | https://www.gesetze-im-internet.de/estg/__43a.html |
| Solidarity surcharge, on the tax | 5.5% | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Church tax: flat tax becomes (e - 4q) / (4 + k), k = state church-tax rate | formula | 2026 | https://www.gesetze-im-internet.de/estg/__32d.html |
| Sparer-Pauschbetrag, single | EUR 1,000 | 2026 | https://www.gesetze-im-internet.de/estg/__20.html |
| Sparer-Pauschbetrag, jointly assessed couple | EUR 2,000 | 2026 | https://www.gesetze-im-internet.de/estg/__20.html |
| Large-holding threshold, any time in the last five years | 1% | 2026 | https://www.gesetze-im-internet.de/estg/__17.html |
| § 17: tax-free share of sale price (partial-income method) | 40% | 2026 | https://www.gesetze-im-internet.de/estg/__3.html |
| § 17: deductible share of cost and selling costs | 60% | 2026 | https://www.gesetze-im-internet.de/estg/__3c.html |
| § 17 allowance, scaled to the share sold | EUR 9,060 | 2026 | https://www.gesetze-im-internet.de/estg/__17.html |
| § 17 allowance falls by the gain above (scaled) | EUR 36,100 | 2026 | https://www.gesetze-im-internet.de/estg/__17.html |
| Private sales of other assets taxable if held | one year or less | 2026 | https://www.gesetze-im-internet.de/estg/__23.html |
| Private sales of land taxable if held | ten years or less | 2026 | https://www.gesetze-im-internet.de/estg/__23.html |
| Private sales Freigrenze (total yearly gain tax-free if below) | EUR 1,000 | 2026 | https://www.gesetze-im-internet.de/estg/__23.html |
| Teilfreistellung: equity fund / mixed fund | 30% / 15% | 2026 | https://www.gesetze-im-internet.de/invstg_2018/__20.html |
| Teilfreistellung: property fund / foreign property fund | 60% / 80% | 2026 | https://www.gesetze-im-internet.de/invstg_2018/__20.html |
| Vorabpauschale base return: start price x 70% of Basiszins | 70% | 2026 | https://www.gesetze-im-internet.de/invstg_2018/__18.html |
| Basiszins 2026 / 2025 | 3.20% / 2.53% | 2026, 2025 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2026-01-13-basiszins-berechnung-vorabpauschale.pdf?__blob=publicationFile&v=3 |
| Fund units bought before 2009: allowance on post-2017 growth | EUR 100,000 | 2026 | https://www.gesetze-im-internet.de/invstg_2018/__56.html |

## The taxable base

**Flat-tax income.** Interest, dividends and gains on shares, bonds, funds and derivatives ([§ 20(1) and (2) EStG](https://www.gesetze-im-internet.de/estg/__20.html)). Gain = sale proceeds, less costs directly tied to the sale, less purchase cost. Foreign-currency amounts are converted at the date of each transaction. For securities of one kind in one custody account, the first bought count as the first sold (§ 20(4) EStG).

- **Sparer-Pauschbetrag.** EUR 1,000, or EUR 2,000 for a jointly assessed couple, deducted from all investment income together. It replaces actual costs: "der Abzug der tatsächlichen Werbungskosten ist ausgeschlossen" (§ 20(9)). Custody fees and loan interest are not deductible; purchase and sale costs still reduce the gain. A couple's allowance is split half each, and an unused half moves to the other spouse. It cannot create a loss and lapses at year end.
- **Freistellungsauftrag.** The client tells each German bank how much of the allowance to use there. It needs the client's tax identification number ([§ 44a EStG](https://www.gesetze-im-internet.de/estg/__44a.html)).
- **Church tax.** For a church member the flat tax is reduced by 25% of the church tax, which gives tax = (e - 4q) / (4 + k), where e is the income, q the creditable foreign tax and k the church-tax rate ([§ 32d(1) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)). The rate k is set by state law; confirm it for the client's state. Banks withhold church tax unless the client blocked the data transfer, in which case the client declares it ([§ 51a EStG](https://www.gesetze-im-internet.de/estg/__51a.html)).
- **Solidarity surcharge.** 5.5% of the flat tax. The exemption threshold that frees most salary earners does not help: on bank withholding the threshold test in [§ 3(3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) leaves out tax under § 32d(3) and (4) EStG, so the 5.5% ([§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html)) is charged on the flat tax in full.
- **Foreign withholding tax** is credited against the flat tax, capped per item of income (§ 32d(5) EStG). Treaty refund cases go to de-treaty-withholding-rates.
- **Bought before 2009.** Gains on shares bought before 1 January 2009 are outside the flat tax unless § 17 applies ([§ 52(28) EStG](https://www.gesetze-im-internet.de/estg/__52.html)). Derivatives and other securities have their own start dates in the same paragraph: for a Termingeschäft the right must have been acquired after 31 December 2008 (§ 52(28) sentence 12 EStG). Fund units bought before 2009 and held privately: growth to 31 December 2017 is tax-free; later growth is taxable only above a one-time EUR 100,000 allowance ([§ 56(6) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__56.html)).

**Loss pots** ([§ 20(6) EStG](https://www.gesetze-im-internet.de/estg/__20.html)).

- Investment losses never offset salary, business or rental income, and are not carried back. They carry forward without time limit.
- **Share pot.** Losses from selling shares only offset gains from selling shares (§ 20(6) sentence 4).
- **General pot.** Other investment losses (bonds, funds, derivatives, worthless securities, bad debts) offset any investment income.
- **Derivative and bad-debt caps removed.** A 2020 law capped yearly offsets of losses from Termingeschäfte and from worthless assets. Both caps are no longer in § 20(6), and the repeal applies to all open years (§ 52(28) sentences 25 and 26 EStG). Older material still quotes the caps. If an open assessment applied them, ask for a correction.
- **Loss certificate (Verlustbescheinigung).** A bank offsets losses inside the bank and carries the rest forward there. To use them at another bank, the client asks for a certificate; the irrevocable request must reach the bank "bis zum 15. Dezember des laufenden Jahres" ([§ 43a(3) EStG](https://www.gesetze-im-internet.de/estg/__43a.html)). Withheld-tax losses can only be used in the return with that certificate (§ 20(6) sentence 5).

**Funds and ETFs.** Fund income has three parts: distributions, the Vorabpauschale and the gain on sale ([§ 16 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__16.html)). The partial-income method never applies to funds. The Teilfreistellung makes a share tax-free: 30% for an equity fund (fund terms require over 50% of assets continuously in equities, [§ 2(6) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__2.html)), 15% for a mixed fund (at least 25%, § 2(7) InvStG; half the equity-fund rate), 60% for a property fund and 80% for a foreign property fund ([§ 20 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__20.html)). The same share of costs and losses is not deductible ([§ 21 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__21.html)). A fund that in fact stayed above the equity quota can get the share on proof in the return (§ 20(4) InvStG).

**Vorabpauschale** ([§ 18 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__18.html)):

1. Base return = redemption price at the start of the year x 70% of the Basiszins.
2. Capped at the year's price rise plus distributions. No rise, no lump sum.
3. Lump sum = base return less the year's distributions, never below zero.
4. In the year of purchase, cut by one twelfth for each full month before the month of purchase.
5. It counts as received on the first working day of the next year. The 2026 lump sum (Basiszins 3.20%) is taxed in 2027; the 2025 lump sum (2.53%) was taxed in 2026.
6. The fund's Teilfreistellung applies to the lump sum, as it is part of the fund's income ([§ 16(1) no. 2](https://www.gesetze-im-internet.de/invstg_2018/__16.html) and [§ 20(1) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__20.html)). A German bank that holds the units collects the tax from the client's account or sets it against the allowance ([§ 44(1) and (1b) EStG](https://www.gesetze-im-internet.de/estg/__44.html)).
7. On a sale, lump sums already taxed are deducted from the gain ([§ 19(1) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__19.html)). With a foreign broker the client tracks them.

**Large holdings (§ 17 EStG).** A sale of shares in any company, German or foreign, is business income if the seller held at least 1%, directly or indirectly, at any time in the five years before the sale ([§ 17(1)](https://www.gesetze-im-internet.de/estg/__17.html): "zu mindestens 1 Prozent beteiligt war"). A holding cut below 1% still counts, and gifted shares count if the giver met the test. Liquidation and capital repayments count as a sale (§ 17(4)). Under the partial-income method (Teileinkünfteverfahren), 60% of the price less 60% of cost and selling costs is taxable ([§ 3 no. 40 c](https://www.gesetze-im-internet.de/estg/__3.html), [§ 3c(2)](https://www.gesetze-im-internet.de/estg/__3c.html)), less the allowance: the share sold of EUR 9,060, cut by the gain above the same share of EUR 36,100. The result joins other income at the normal rate. A loss is 60% deductible and can offset other income, but is barred in part for shares received free or not in a qualifying holding for the full five years (§ 17(2)).

- **Dividends from a large holding** stay in the flat tax by default. On application, a holder of at least 25%, or of at least 1% who works for the company with significant influence, can use the partial-income method instead ([§ 32d(2) no. 3 EStG](https://www.gesetze-im-internet.de/estg/__32d.html)). The application is made with the return at the latest, runs for four more years unless revoked, and cannot be made again for that holding after revocation. Financing costs then become 60% deductible.

**Private sales (§ 23 EStG).**

- Land and buildings sold "nicht mehr als zehn Jahre" after purchase; other assets (crypto, gold, foreign currency, collectibles) sold "nicht mehr als ein Jahr" after purchase ([§ 23(1)](https://www.gesetze-im-internet.de/estg/__23.html)). Exactly one year is still taxable.
- Property is outside § 23 if the owner lived in it exclusively between purchase and sale, or in the year of sale and the two years before (§ 23(1) no. 1 sentence 3: "ausschließlich zu eigenen Wohnzwecken oder im Jahr der Veräußerung und in den beiden vorangegangenen Jahren"). Letting it out at any point breaks the first test; the second test looks only at the three calendar years ending with the sale. Everyday objects ("Gegenstände des täglichen Gebrauchs") are outside § 23 (§ 23(1) no. 2 sentence 2).
- Gain = price less cost and sale costs; for a let property, cost is reduced by depreciation claimed (§ 23(3)).
- **Freigrenze.** Gains stay tax-free if the total private-sales gain in the calendar year is "weniger als 1 000 Euro" (§ 23(3) sentence 5). It is a cliff: at EUR 1,000 or more the whole gain is taxed. The EUR 1,000 limit applies from 2024 ([Wachstumschancengesetz, BGBl. 2024 I Nr. 108](https://www.recht.bund.de/bgbl/1/2024/108/VO.html), Art. 2 no. 5, in force from 1 January 2024 under Art. 35(4)); for 2023 and earlier the gain had to be below EUR 600.
- Losses only offset private-sales gains of the same year, the year before or later years.
- **Crypto pointer.** The [BMF ruling of 6 March 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2) treats a coin-to-coin swap as a sale and new purchase (new one-year period), does not extend the period to ten years for lent or staked currency tokens, and sets lot rules per wallet and coin (paragraphs 61 and 62: where lots cannot be identified one by one, first in, first out for the holding period, and average cost or, as a simplification, FIFO for the value). Detail is in de-crypto-tax.

**Günstigerprüfung.** On request, investment income is added to other income and taxed at the normal rate "wenn dies zu einer niedrigeren Einkommensteuer einschließlich Zuschlagsteuern führt" ([§ 32d(6) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)). It covers all investment income for the year, and both spouses if jointly assessed. The allowance still applies; actual costs are still not deductible. It pays where the client's marginal rate is below 25%.

## Deadlines and filing

- **Bank withholding settles the tax** where all income was taxed by German banks correctly. The bank pays withheld tax to its tax office by the tenth of the following month ([§ 44(1) EStG](https://www.gesetze-im-internet.de/estg/__44.html)).
- **A return is required** for investment income with no German withholding, such as a foreign broker account ([§ 32d(3) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)), and for any § 17 or § 23 gain. A return is worth filing to use an unused allowance, offset losses across banks, credit foreign tax, settle church tax or apply the Günstigerprüfung (§ 32d(4) and (6)).
- **Forms.** Anlage KAP for investment income (Anlage KAP-INV for funds at a foreign broker), Anlage SO for private sales, Anlage G for a § 17 sale. Filed through ELSTER; use the form version for the year.
- **With the bank, not the tax office:** the Freistellungsauftrag before income arrives; the loss certificate request by 15 December ([§ 43a(3) EStG](https://www.gesetze-im-internet.de/estg/__43a.html)).
- **Guidance on bank withholding:** [BMF letter "Einzelfragen zur Abgeltungsteuer" of 14 May 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Abgeltungsteuer/2025-05-14-einzelfragen-zur-abgeltungsteuer.html).

| Return | Deadline | Source |
| --- | --- | --- |
| 2025 return, filed by the client | 31 July 2026, passed. File now | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| 2025 return, prepared by a Steuerberater | 28 February 2027 is a Sunday, so Monday 1 March 2027 | § 149(3) AO; [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| 2026 return, filed by the client | 31 July 2027 is a Saturday, so Monday 2 August 2027 | § 149(2) AO; § 108(3) AO |
| 2026 return, prepared by a Steuerberater | Tuesday 29 February 2028 | § 149(3) AO |

The tax office can ask for an adviser-prepared return earlier (§ 149(4) AO). For the 2025 return the rules are the same, except that the 2025 Vorabpauschale (2.53%) belongs in the 2026 return, and the lump sum on the 2025 bank certificate is the one for 2024.

## Penalties and interest

| Item | Figure | Source |
| --- | --- | --- |
| Late-filing surcharge (Verspätungszuschlag) | 0.25% of the assessed tax less prepayments and withheld tax, per started month, at least EUR 25 per month | [§ 152(5) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Interest on back tax or refunds (§ 233a) | 0.15% per month (1.8% a year), starting 15 months after the end of the tax year | [§ 233a AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html), [§ 238(1a) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html) |
| Late-payment surcharge (Säumniszuschlag) | 1% per started month of the unpaid tax, rounded down to EUR 50 | [§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html) |

Failing to declare foreign-broker income is under-declaration; the back tax carries § 233a interest.

## Cross-border points

- **Foreign brokers** withhold no German tax. The client declares the income on Anlage KAP and tracks Vorabpauschalen and loss pots.
- **Foreign withholding** is credited per item against the 25%, capped at the German tax on that item (§ 32d(5) EStG). Reclaims above the treaty rate are made in the source country.
- **Non-residents** are taxed in Germany only on German-source income: see de-non-resident-tax. Dividends paid abroad: de-treaty-withholding-rates.
- **Exit tax.** A client fully liable for at least seven of the last twelve years who holds § 17 shares faces a deemed sale on moving abroad, or on giving the shares to someone not liable in Germany ([§ 6 AStG](https://www.gesetze-im-internet.de/astg/__6.html)). Payment can be spread over seven yearly instalments on application; there is no open-ended EU/EEA deferral for triggers from 2022, and the tax falls away on return within seven years if conditions are met. Fund units are caught at 1% of a fund or a cost of EUR 500,000 ([§ 19(3) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__19.html)). Full detail: leaving-germany-exit-tax.

## Worked examples

Round numbers chosen for illustration. They are not official examples.

**Example 1: single investor, German bank, no church tax.** In 2026 the client received dividends of EUR 1,500 and sold shares bought in 2020 for a gain of EUR 2,500. The Freistellungsauftrag covers the full EUR 1,000. Taxable: EUR 4,000 less EUR 1,000 = EUR 3,000. Flat tax at 25% = EUR 750. Surcharge at 5.5% of EUR 750 = EUR 41.25. The bank withholds EUR 791.25 in total. No return is needed for this income unless the client wants the Günstigerprüfung.

```oa-check
name: DE 2026 flat tax, single, no church tax
inputs:
  dividends: 1500
  share_gain: 2500
  allowance: 1000
steps:
  - taxable: dividends + share_gain - allowance
  - flat_tax: taxable * 0.25
  - soli: flat_tax * 0.055
  - total: flat_tax + soli
expected:
  taxable: 3000
  flat_tax: 750
  soli: 41.25
  total: 791.25
```

**Example 2: church member, share losses and a foreign broker.** The client is single, a church member in a state with a church-tax rate of 8% (assumed for the example; confirm the state rate). In 2026: interest of EUR 1,200 and dividends of EUR 2,800 at a foreign broker (no German tax withheld, no foreign tax), plus a share gain of EUR 2,000 and a share loss of EUR 2,500 at a German bank that issued a loss certificate. The share loss can only offset the share gain, so EUR 500 of loss carries forward to future share gains; it does not reduce the interest or dividends. Taxable: EUR 4,000 less the EUR 1,000 allowance = EUR 3,000. Flat tax = 3,000 / (4 + 0.08) = EUR 735.29. Church tax = 8% of that = EUR 58.82. Surcharge = 5.5% = EUR 40.44. Total EUR 834.55, against EUR 791.25 without church tax.

```oa-check
name: DE 2026 church-tax formula with share-loss pot
inputs:
  interest: 1200
  dividends: 2800
  share_gain: 2000
  share_loss: 2500
  allowance: 1000
  k: 0.08
steps:
  - share_net: max(share_gain - share_loss, 0)
  - loss_carried: max(share_loss - share_gain, 0)
  - taxable: interest + dividends + share_net - allowance
  - flat_tax: round(taxable / (4 + k), 2)
  - church: round(flat_tax * k, 2)
  - soli: round(flat_tax * 0.055, 2)
  - total: flat_tax + church + soli
expected:
  share_net: 0
  loss_carried: 500
  taxable: 3000
  flat_tax: 735.29
  church: 58.82
  soli: 40.44
  total: 834.55
```

**Example 3: losses at two banks.** In 2026 the client lost EUR 3,000 selling shares at bank A and gained EUR 5,000 selling shares at bank B. Bank B withholds on the EUR 5,000 (less any allowance used there). The client asks bank A for a loss certificate by 15 December 2026 and files Anlage KAP; the tax office sets the EUR 3,000 against the share gain at bank B and refunds the excess tax ([§ 43a(3) EStG](https://www.gesetze-im-internet.de/estg/__43a.html), § 20(6) sentence 5). Without the certificate the loss stays at bank A and is carried into 2027 there.

**Example 4: Vorabpauschale on an equity ETF.** An accumulating equity ETF was worth EUR 50,000 on 1 January 2026 and rose by more than EUR 1,120 over 2026, with no distributions. Base return: EUR 50,000 x 70% x 3.20% = EUR 1,120. Teilfreistellung 30%, so EUR 784 is taxable. It counts as received on the first working day of 2027 ([§ 18 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__18.html), [§ 20 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__20.html)). The same holding for 2025 gave EUR 50,000 x 70% x 2.53% = EUR 885.50, received early in 2026.

```oa-check
name: DE Vorabpauschale 2026 and 2025, equity ETF
inputs:
  start_value: 50000
  basiszins_2026: 0.032
  basiszins_2025: 0.0253
  teilfreistellung: 0.30
steps:
  - base_2026: start_value * 0.70 * basiszins_2026
  - taxable_2026: base_2026 * (1 - teilfreistellung)
  - base_2025: start_value * 0.70 * basiszins_2025
expected:
  base_2026: 1120
  taxable_2026: 784
  base_2025: 885.50
```

**Example 5: crypto and the Freigrenze cliff.** Bitcoin bought 1 March 2025 for EUR 10,000 and sold 15 February 2026 for EUR 10,900: a gain of EUR 900 within one year. With no other private sales the total is below EUR 1,000, so it is tax-free. If the client also sold gold within a year at a EUR 200 gain, the total is EUR 1,100 and the whole EUR 1,100 is taxed at the normal rate. Sold on 2 March 2026, more than one year after purchase, the Bitcoin would be outside § 23 ([§ 23(1) no. 2 and (3) EStG](https://www.gesetze-im-internet.de/estg/__23.html)).

**Example 6: selling a 2% stake.** The client sells a whole 2% holding in a GmbH for EUR 100,000; cost EUR 40,000, no selling costs. Taxable: 60% of EUR 100,000 less 60% of EUR 40,000 = EUR 36,000. The allowance for 2% is 2% of EUR 9,060 = EUR 181.20, cut by the amount the gain exceeds 2% of EUR 36,100 (EUR 722), so it is nil. EUR 36,000 joins the client's other income ([§ 17(3) EStG](https://www.gesetze-im-internet.de/estg/__17.html), [§ 3 no. 40 c](https://www.gesetze-im-internet.de/estg/__3.html), [§ 3c(2)](https://www.gesetze-im-internet.de/estg/__3c.html)).

```oa-check
name: DE § 17 sale of a 2% stake, allowance fully cut
inputs:
  price: 100000
  cost: 40000
  share: 0.02
steps:
  - gain: price * 0.60 - cost * 0.60
  - allowance_start: 9060 * share
  - cut_threshold: 36100 * share
  - allowance: max(allowance_start - max(gain - cut_threshold, 0), 0)
  - taxable: gain - allowance
expected:
  gain: 36000
  allowance_start: 181.20
  cut_threshold: 722
  allowance: 0
  taxable: 36000
```

**Example 7: selling a flat.** A flat bought in 2018 was let until 2023 and lived in by the owner from January 2024 until its sale in June 2026. It was the owner's home in the year of sale and the two years before, so the gain is outside § 23 even though the sale is within ten years. Had it still been let at the sale, the whole gain would be taxed at the normal rate (§ 23(1) no. 1 sentence 3 EStG).

## When to refer

Refer to a German Steuerberater when:

- The client is leaving Germany, or giving shares to someone abroad, with a holding of 1% or more or large fund holdings ([§ 6 AStG](https://www.gesetze-im-internet.de/astg/__6.html)); the exit tax needs a valuation and the holding history.
- Assets are held in a business, a partnership or a company.
- The case turns on a tax treaty, or on crediting foreign tax beyond the per-item cap.
- Crypto goes beyond buying, selling and swapping: staking, lending, mining, DeFi, NFTs, or tokens that work like securities.
- A § 17 sale involves a loss, shares received as a gift, a capital reduction or a liquidation.
- The client wants the § 32d(2) no. 3 option, which runs for four more years unless revoked and cannot be made again after revocation.

Do not state a combined flat-tax rate with church tax without the client's state church-tax rate, and do not estimate a Vorabpauschale without the fund's actual prices.

## Ask the client first

- Are the assets held privately or in a business, and are you married and assessed jointly?
- Which banks and brokers hold them, is any outside Germany, and how is the Freistellungsauftrag split?
- Are you a church member, and in which federal state do you live?
- Do you hold, or did you hold in the last five years, 1% or more of any company? Do you work for it?
- For each fund: its type and the price on 1 January. For crypto, gold and property: purchase and sale dates, and whether you lived in the property.
- Do you have losses carried forward or bank loss certificates, and are you planning to leave Germany?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| EStG § 3 (no. 40) | https://www.gesetze-im-internet.de/estg/__3.html | 2026-10-24 |
| EStG § 3c | https://www.gesetze-im-internet.de/estg/__3c.html | 2026-10-24 |
| EStG § 17 | https://www.gesetze-im-internet.de/estg/__17.html | 2026-10-26 |
| EStG § 20 | https://www.gesetze-im-internet.de/estg/__20.html | 2026-10-26 |
| EStG § 23 | https://www.gesetze-im-internet.de/estg/__23.html | 2026-10-24 |
| EStG § 32d | https://www.gesetze-im-internet.de/estg/__32d.html | 2026-10-26 |
| EStG § 43a | https://www.gesetze-im-internet.de/estg/__43a.html | 2026-10-26 |
| EStG § 44 | https://www.gesetze-im-internet.de/estg/__44.html | 2026-10-26 |
| EStG § 44a, § 51a | https://www.gesetze-im-internet.de/estg/__44a.html | 2026-10-26 |
| EStG § 52 | https://www.gesetze-im-internet.de/estg/__52.html | 2026-10-24 |
| SolzG § 3 and § 4 | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-10-24 |
| InvStG § 2, § 16, § 18, § 19, § 20, § 21, § 56 | https://www.gesetze-im-internet.de/invstg_2018/__20.html | 2026-10-26 |
| AStG § 6 | https://www.gesetze-im-internet.de/astg/__6.html | 2026-10-26 |
| AO § 108, § 149, § 152, § 233a, § 238, § 240 | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-10-24 |
| BMF letter, Einzelfragen zur Abgeltungsteuer, 14 May 2025 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Abgeltungsteuer/2025-05-14-einzelfragen-zur-abgeltungsteuer.html | 2026-10-26 |
| BMF letter, Basiszins 2026, 13 January 2026 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2026-01-13-basiszins-berechnung-vorabpauschale.pdf?__blob=publicationFile&v=3 | 2026-10-26 |
| BMF letter, Basiszins 2025, 10 January 2025 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2025-01-10-basiszins-vorabpauschale-zum-2-1-2025.pdf?__blob=publicationFile&v=6 | 2026-10-26 |
| BMF letter, crypto assets, 6 March 2025 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2 | 2026-10-26 |
| Wachstumschancengesetz, BGBl. 2024 I Nr. 108 (Art. 2 no. 5, Art. 35(4)) | https://www.recht.bund.de/bgbl/1/2024/108/VO.html | 2026-10-26 |

Not yet confirmed: the state church-tax rates (8% or 9%, set by state law, not on the federal pages); the body of the 14 May 2025 BMF letter was located but not read line by line.

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
