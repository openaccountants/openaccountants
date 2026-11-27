---
name: de-capital-gains
description: "German tax on private investment income and gains for a resident individual, tax year 2026. Covers the 25% flat tax (Abgeltungsteuer) with the 5.5% solidarity surcharge and the church-tax formula, bank withholding (Kapitalertragsteuer), the Sparer-Pauschbetrag of EUR 1,000 or EUR 2,000, the share-loss pot and the general pot, loss certificates, funds and ETFs (Teilfreistellung, Vorabpauschale, Basiszins), large holdings of 1% or more under § 17 with the partial-income method, private sales under § 23 (one-year and ten-year rules, the EUR 1,000 Freigrenze), the Günstigerprüfung and Anlage KAP. Trigger on: Abgeltungsteuer, Kapitalertragsteuer, Sparer-Pauschbetrag, Freistellungsauftrag, Verlustbescheinigung, Teilfreistellung, Vorabpauschale, Spekulationsfrist, sell shares Germany, German capital gains. Out of scope: crypto detail (de-crypto-tax), the exit tax (leaving-germany-exit-tax), non-residents (de-non-resident-tax), treaty withholding (de-treaty-withholding-rates), assets in a business (de-einkommensteuer-freelancer)."
version: 1.6
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - de-einkommensteuer-freelancer
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Capital gains tax in Germany (Abgeltungsteuer and private sales), 2026

## Who this applies to

An individual fully liable to German tax (home or habitual abode in Germany) who holds investments privately, not in a business. Tax year 2026 is the calendar year ([§ 1(1)](https://www.gesetze-im-internet.de/estg/__1.html), [§ 25(1) EStG](https://www.gesetze-im-internet.de/estg/__25.html)). Use ordinary private investment accounts; pension/insurance wrappers, tax-shelter schemes and special investment funds need separate classification. Check this point with one of our partner accountants.

Sort every asset into one of three regimes first. They do not mix: flat-tax losses cannot offset private-sales gains, and the other way round.

| Regime | What falls in it | How it is taxed | Law |
| --- | --- | --- | --- |
| Flat tax (Abgeltungsteuer) | Interest, dividends, gains on shares, bonds, funds and ETFs, derivatives, subject to the mandatory § 32d(2) exceptions below | 25% plus solidarity surcharge and church tax, normally withheld by the German bank | [§ 20](https://www.gesetze-im-internet.de/estg/__20.html), [§ 32d EStG](https://www.gesetze-im-internet.de/estg/__32d.html) |
| Large shareholding | Shares personally meeting the 1%/five-year test, or a qualifying recent free acquisition under § 17(1) sentence 4 with the actual predecessor/chain holding test | Partial-income method at the normal progressive rate | [§ 17 EStG](https://www.gesetze-im-internet.de/estg/__17.html) |
| Private sales | Other private assets within one year, extended to ten years for the statutory income-producing use; Currency/Payment Tokens retain the specific BMF exception. Land/buildings: ten years | Normal progressive rate, nothing withheld | [§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html) |

Out of scope here: assets held in a business or company (de-einkommensteuer-freelancer, de-corporate-tax), non-residents (de-non-resident-tax), crypto staking, lending, mining and DeFi (de-crypto-tax), and the exit tax in detail (leaving-germany-exit-tax).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Flat tax on private investment income | 25% | 2026 | https://www.gesetze-im-internet.de/estg/__32d.html |
| Bank withholding on the ordinary private income covered here, after applicable loss/allowance/partial-exemption rules | 25%, reduced for church tax under the formula below | 2026 | https://www.gesetze-im-internet.de/estg/__43a.html |
| Solidarity surcharge, on the tax | 5.5% | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Church tax: flat tax becomes (e - 4q) / (4 + k), k = state church-tax rate | formula | 2026 | https://www.gesetze-im-internet.de/estg/__32d.html |
| Sparer-Pauschbetrag, single | EUR 1,000 | 2026 | https://www.gesetze-im-internet.de/estg/__20.html |
| Sparer-Pauschbetrag, jointly assessed couple | EUR 2,000 | 2026 | https://www.gesetze-im-internet.de/estg/__20.html |
| Personal large-holding threshold, any time in the last five years; recent free acquisitions also test the predecessor/chain rule below | 1% | 2026 | https://www.gesetze-im-internet.de/estg/__17.html |
| § 17: tax-free share of sale price (partial-income method) | 40% | 2026 | https://www.gesetze-im-internet.de/estg/__3.html |
| § 17: deductible share of cost and selling costs | 60% | 2026 | https://www.gesetze-im-internet.de/estg/__3c.html |
| § 17 allowance, scaled to the share sold | EUR 9,060 | 2026 | https://www.gesetze-im-internet.de/estg/__17.html |
| § 17 allowance falls by the gain above (scaled) | EUR 36,100 | 2026 | https://www.gesetze-im-internet.de/estg/__17.html |
| Other private assets: ordinary disposal period, subject to the statutory ten-year income-producing branch and specific Currency/Payment Token exception | one year or less; qualifying income-producing assets ten years or less | 2026 | https://www.gesetze-im-internet.de/estg/__23.html |
| Private sales of land taxable if held | ten years or less | 2026 | https://www.gesetze-im-internet.de/estg/__23.html |
| Private sales Freigrenze (total yearly gain tax-free if below) | EUR 1,000 | 2026 | https://www.gesetze-im-internet.de/estg/__23.html |
| Teilfreistellung: qualifying equity fund / mixed fund, private investor | 30% / 15% (mixed rate derived: half the equity rate) | 2026 | https://www.gesetze-im-internet.de/invstg_2018/__20.html |
| Teilfreistellung: property fund / foreign property fund | 60% / 80% | 2026 | https://www.gesetze-im-internet.de/invstg_2018/__20.html |
| Vorabpauschale base return: start price x 70% of Basiszins | 70% | 2026 | https://www.gesetze-im-internet.de/invstg_2018/__18.html |
| Basiszins for the 2026 Vorabpauschale, received in 2027 | 3.20% | 2026 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2026-01-13-basiszins-berechnung-vorabpauschale.pdf?__blob=publicationFile&v=3 |
| Basiszins for the 2025 Vorabpauschale, received in 2026 | 2.53% | 2025 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2025-01-10-basiszins-vorabpauschale-zum-2-1-2025.pdf?__blob=publicationFile&v=6 |
| Fund units bought before 2009: allowance on post-2017 growth | EUR 100,000 | 2026 | https://www.gesetze-im-internet.de/invstg_2018/__56.html |

## The taxable base

**Flat-tax income.** Interest, dividends and gains on shares, bonds, funds and derivatives ([§ 20(1) and (2) EStG](https://www.gesetze-im-internet.de/estg/__20.html)). Gain = sale proceeds, less costs directly tied to the sale, less purchase cost. Foreign-currency sale proceeds are converted at disposal and purchase costs at acquisition. For fungible securities in collective custody, the first bought count as the first sold. On a gift or inheritance, § 20(4) sentence 6 attributes the predecessor's acquisition history to the successor; do not reset cost to market value. Corporate actions, removals from business assets and disputed acquisition data: Check this point with one of our partner accountants.

**Mandatory financing exceptions (§ 32d(2) no. 1).** Before applying 25%, test income within § 20(1) nos. 4 and 7 and § 20(2) sentence 1 nos. 4 and 7. Under (a), creditor and debtor must be related within the statutory test, and the corresponding debtor expenses must be business expenses or income-related costs connected with income subject to German tax, without the § 20(9) sentence 1 second-half expense bar applying. Under (b), the same debtor-expense/German-tax conditions apply to payments by a corporation or cooperative to a shareholder holding at least 10%, or to a person related to that shareholder. Exactly 10% meets the ownership limb; 9.99% does not meet that limb alone, and (a)/(c) still require testing. Do not establish statutory relatedness from family membership alone.

Under (c), test third-party capital income connected with capital made available to the creditor's business; the stated extension covers a related person, a partnership in which the creditor/related person is a co-entrepreneur, or a corporation/cooperative in which either holds at least 10%, subject to the third party's recourse condition. A common plan, particularly close timing or linked interest agreements, is relevant; the statutory connection is absent where interest terms are market-standard or the flat-tax treatment gives no tax-burden advantage. The clauses apply correspondingly where the capital finances income under § 2(1) sentence 1 nos. 4, 6 or 7. Establish those actual financing/recourse/terms facts rather than treating every owner or family loan alike.

For an actually qualifying no. 1 case, the ordinary tariff applies and § 20(6)/(9) does not apply: use eligible actual costs rather than the Sparer-Pauschbetrag method. Stipulated qualifying interest of EUR 10,000 less EUR 2,000 eligible actual costs gives EUR 8,000 ordinary-rate income, rather than EUR 9,000 from an assumed EUR 1,000 allowance; final tax depends on the other tariff inputs. This mandatory route is distinct from the optional dividend partial-income election.

- **Sparer-Pauschbetrag.** EUR 1,000, or EUR 2,000 for a jointly assessed couple, deducted from all investment income together. It replaces actual costs: "der Abzug der tatsächlichen Werbungskosten ist ausgeschlossen" (§ 20(9)). Custody fees and loan interest are not deductible; purchase and sale costs still reduce the gain. A couple's allowance is split half each, and an unused half moves to the other spouse. It cannot create a loss and lapses at year end.
- **Freistellungsauftrag.** Allocate the allowance across banks without exceeding the total. The prescribed order needs the client's tax identification number and, for a joint order, the spouse's too ([§ 44a(2), (2a) EStG](https://www.gesetze-im-internet.de/estg/__44a.html)).
- **Church tax.** For a church member the flat tax is reduced by 25% of the church tax, which gives tax = (e - 4q) / (4 + k), where e is the income, q the creditable foreign tax and k the church-tax rate ([§ 32d(1) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)). The rate k is set by state law; confirm it for the client's state. Banks withhold church tax unless the client blocked the data transfer, in which case the client declares it ([§ 51a EStG](https://www.gesetze-im-internet.de/estg/__51a.html)).
- **Solidarity surcharge.** 5.5% of the flat tax. The exemption threshold that frees most salary earners does not help: on bank withholding the threshold test in [§ 3(3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) leaves out tax under § 32d(3) and (4) EStG, so the 5.5% ([§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html)) is charged on the flat tax in full.
- **Foreign withholding tax** under [§ 32d(5) EStG](https://www.gesetze-im-internet.de/estg/__32d.html) must be assessed and paid and reduced by an accrued relief entitlement; the per-item ceiling is 25% of the taxable foreign income, and the credit cannot exceed the German tax attributable to that year's foreign income. Apply the treaty rule where relevant. Treaty refund cases: use de-treaty-withholding-rates. Check this point with one of our partner accountants.
- **Bought before 2009.** Gains on shares bought before 1 January 2009 are outside the flat-tax sale rule unless § 17 applies ([§ 52(28) EStG](https://www.gesetze-im-internet.de/estg/__52.html)). Derivatives and other securities have their own start dates in that paragraph: for a Termingeschäft the right must have been acquired after 31 December 2008. Do not generalise the share rule to every security. For protected fund units acquired before 2009 and never held in business assets, growth through 31 December 2017 is exempt; post-2017 sale growth uses the remaining EUR 100,000 personal allowance. The tax office separately determines the remaining allowance annually until used up. Former § 21(2a)/(2b) InvStG units are excluded ([§ 56(6) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__56.html)). Obtain the actual allowance determination and legacy-unit classification.

**Loss pots** ([§ 20(6) EStG](https://www.gesetze-im-internet.de/estg/__20.html)).

- Investment losses never offset salary, business or rental income, and are not carried back. They carry forward without time limit.
- **Share pot.** Losses from selling shares only offset gains from selling shares (§ 20(6) sentence 4).
- **General pot.** Other eligible § 20 losses (for example bonds, funds and derivatives) can offset investment income. Classify worthless assets and bad debts by the underlying instrument; a worthless share does not become a general-pot loss merely because it is worthless. Tax-shelter losses are held for separate review.
- **Derivative and bad-debt caps removed.** A 2020 law capped yearly offsets of losses from Termingeschäfte and from worthless assets. Both caps are no longer in § 20(6), and the repeal applies to all open years (§ 52(28) sentences 25 and 26 EStG). Older material still quotes the caps. If an open assessment applied them, ask for a correction.
- **Loss certificate (Verlustbescheinigung).** A bank offsets losses inside the bank and carries the rest forward there. To use them at another bank, the client asks for a certificate; the irrevocable request must reach the bank "bis zum 15. Dezember des laufenden Jahres" ([§ 43a(3) EStG](https://www.gesetze-im-internet.de/estg/__43a.html)). Withheld-tax losses can only be used in the return with that certificate (§ 20(6) sentence 5).

**Funds and ETFs.** Fund income has three parts: distributions, the Vorabpauschale and the gain on sale ([§ 16 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__16.html)). The § 3 no. 40 partial-income method does not apply to these fund returns (§ 16(3) InvStG). The Teilfreistellung makes a share tax-free: 30% for an equity fund (fund terms require over 50% of assets continuously in equities, [§ 2(6) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__2.html)), 15% for a mixed fund (at least 25%, § 2(7) InvStG; half the equity-fund rate), 60% for a property fund and 80% for a foreign property fund ([§ 20 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__20.html)). The same share of costs and losses is not deductible ([§ 21 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__21.html)). Under § 20(4) InvStG the investor can request the exemption in assessment on proof that the relevant quota was actually exceeded continuously throughout the year. If a later disposal loss exceeds EUR 500 (or a qualifying write-down is claimed) for units previously proved this way, obtain the required quota information and year-end redemption prices for the whole ownership period and submit them with the return; bank-custodied sale losses also require the prescribed tax/loss certificate. Assessment is mandatory in that follow-up case; failure to provide the information permits the highest proved exemption rate for the ownership-period loss. A property fund must, under its investment terms, continuously invest more than 50% of its assets in property and property companies; for a foreign property fund, more than 50% must be in foreign property and foreign property companies. Apply the classification, exclusions and asset-value rules in [§ 2(9)–(9b) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__2.html).

**Vorabpauschale** ([§ 18 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__18.html)):

1. Base return = redemption price at the start of the year x 70% of the Basiszins.
2. Cap the base return at the difference between the first and last redemption prices fixed in the year, plus distributions; use exchange/market prices where no redemption price is fixed. An accumulating fund with no distributions and a price fall has no Vorabpauschale.
3. Lump sum = base return less the year's distributions, never below zero.
4. In the year of purchase, cut by one twelfth for each full month before the month of purchase.
5. It counts as received on the first working day of the next year. The 2026 lump sum (Basiszins 3.20%) is taxed in 2027; the 2025 lump sum (2.53%) was taxed in 2026.
6. The fund's Teilfreistellung applies to the lump sum, as it is part of the fund's income ([§ 16(1) no. 2](https://www.gesetze-im-internet.de/invstg_2018/__16.html) and [§ 20(1) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__20.html)). For a German custodian, supply any cash shortfall for the tax after applicable allowances; § 44(1) sentences 7–11 and (1b) permit collection from a same-name account under their conditions. If collection fails, the bank reports it and the residence tax office assesses the unpaid tax ([§ 44 EStG](https://www.gesetze-im-internet.de/estg/__44.html)).
7. On a sale, deduct the full Vorabpauschalen assessed during ownership from the gain before applying the actual partial exemption ([§ 19(1) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__19.html)). Use the full assessed amount regardless of partial exemption or whether allowances prevented cash withholding, not merely its taxable fraction; do not deduct unassessed estimates. A stipulated gain of EUR 10,000 less EUR 1,120 full prior assessed Vorabpauschalen leaves EUR 8,880; a 30% equity-fund exemption then leaves EUR 6,216. Deducting only EUR 784 would wrongly leave EUR 6,451.20. Obtain actual broker history, including with a foreign broker.

**Large holdings (§ 17 EStG).** A sale of shares in any company, German or foreign, is business income if the seller held at least 1%, directly or indirectly, at any time in the five years before the sale ([§ 17(1)](https://www.gesetze-im-internet.de/estg/__17.html): "zu mindestens 1 Prozent beteiligt war"). A holding cut below 1% still counts. If the seller acquired the disposed share free within the five years before disposal, § 17(1) sentence 4 applies sentence 1 correspondingly where the seller did not personally meet the test but a predecessor, or an earlier predecessor in a chain of free transfers, held the statutory participation within the relevant five-year period. Record the actual acquisition and predecessor holding dates; a free acquisition outside that recent-acquisition window does not enter this exception solely because its giver currently owns 1%. This share test is separate from AStG residence aggregation. Qualifying liquidation and capital repayments can count as sales under § 17(4), except to the extent the receipts are § 20(1) no. 1 or 2 capital income. Under the partial-income method (Teileinkünfteverfahren), 60% of the price less 60% of cost and selling costs is taxable ([§ 3 no. 40 c](https://www.gesetze-im-internet.de/estg/__3.html), [§ 3c(2)](https://www.gesetze-im-internet.de/estg/__3c.html)), less the allowance: the share sold of EUR 9,060, cut by the gain above the same share of EUR 36,100. The result joins other income at the normal rate. Do not apply a blanket loss allowance: § 17(2) sentence 6 has separate gift and holding-history restrictions and exceptions. Losses, liquidations, capital reductions/repayments and reorganisation shares under § 17(6), including sub-1% holdings: Check this point with one of our partner accountants.

- **Dividends from a large holding** stay in the flat tax by default. On application, a holder of at least 25%, or of at least 1% who works for the company with significant influence, can use the partial-income method instead ([§ 32d(2) no. 3 EStG](https://www.gesetze-im-internet.de/estg/__32d.html)). Test the direct/indirect holding and qualifying influence in the initial application year. The application is made with the return at the latest, runs for four more years unless revoked, and cannot be made again for that holding after revocation. Revocation must reach the tax office by the return for the first affected year. Financing costs then become 60% deductible subject to § 3c(2). Deductible-payer distributions under § 32d(2) no. 4 or any uncertainty about this election: Check this point with one of our partner accountants.

**Private sales (§ 23 EStG).**

- Land and buildings sold "nicht mehr als zehn Jahre" after purchase; other assets (crypto, gold, foreign currency, collectibles) sold "nicht mehr als ein Jahr" after purchase ([§ 23(1)](https://www.gesetze-im-internet.de/estg/__23.html)). Exactly one year is still taxable. For other private assets used as an income source with income in at least one calendar year, § 23(1) no. 2 sentence 4 extends the period to ten years. The BMF's 6 March 2025 letter, paragraph 63, specifically does not apply that extension to Currency or Payment Tokens; do not extend that administrative exception to every other private asset or token classification. An independently qualifying income-producing non-token asset sold after two years is not exempt merely because one year passed.
- Property is outside § 23 if the owner lived in it exclusively between purchase and sale, or in the year of sale and the two years before (§ 23(1) no. 1 sentence 3: "ausschließlich zu eigenen Wohnzwecken oder im Jahr der Veräußerung und in den beiden vorangegangenen Jahren"). Letting it out at any point breaks the first test; the second test looks only at the three calendar years ending with the sale. Everyday objects ("Gegenstände des täglichen Gebrauchs") are outside § 23 (§ 23(1) no. 2 sentence 2).
- Gain = price less cost and sale costs; for a let property, cost is reduced by depreciation claimed (§ 23(3)).
- **Freigrenze.** Gains stay tax-free if the total private-sales gain in the calendar year is "weniger als 1 000 Euro" (§ 23(3) sentence 5). It is a cliff: at EUR 1,000 or more the whole gain is taxed. For the preserved 2023 comparison the limit was EUR 600; from 2024 it is EUR 1,000 ([BMF 6 March 2025, paragraph 53](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2)).
- Losses only offset private-sales gains of the same year, the year before or later years.
- **Crypto pointer.** The [BMF ruling of 6 March 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2) treats a coin-to-coin swap as a sale and new purchase (new one-year period), does not extend the period to ten years for lent or staked currency tokens, and sets lot rules per wallet and coin (paragraphs 61 and 62: individual identification first; where that is impossible, FIFO for the holding period, and average cost or, as a simplification, FIFO for value. Keep the chosen value method for each denomination in each wallet until that denomination is fully sold; a subsequent new acquisition permits a fresh choice). Detail is in de-crypto-tax.

**Günstigerprüfung.** On request, investment income is added to other income and taxed at the normal rate "wenn dies zu einer niedrigeren Einkommensteuer einschließlich Zuschlagsteuern führt" ([§ 32d(6) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)). It covers all investment income for the year, and both spouses if jointly assessed. The allowance still applies; actual costs are still not deductible. Compare actual total income tax including surcharges; a marginal-rate shortcut does not determine the result.

## Deadlines and filing

- **Bank withholding settles the tax** where the final-withholding conditions hold and no § 32d(2) or business-income exception under § 43(5) applies; correct bank withholding alone does not make a mandatory exception final. The ordinary remittance deadline is the tenth of the following month; for § 43(1) sentence 1 no. 1 income, remittance is due when the income flows to the creditor ([§ 44(1) EStG](https://www.gesetze-im-internet.de/estg/__44.html)).
- **A return is required** for investment income with no German withholding, such as a foreign broker account ([§ 32d(3) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)), for the mandatory § 32d(2) no. 1 assessment route above even where tax was withheld; § 17 and § 23 gains enter the ordinary assessment, but do not by themselves prove that every person must file. Test § 56 EStDV and, for wage earners, § 46 EStG; also honour any tax-office demand. Check this point with one of our partner accountants. A return is worth filing to use an unused allowance, offset losses across banks, credit foreign tax, settle church tax or apply the Günstigerprüfung (§ 32d(4) and (6)).
- **Forms.** In ELSTER, use Anlage KAP for investment income, KAP-INV for investment income not subject to domestic withholding, SO for private sales and G for a § 17 sale. Use the actual year's [official form help](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2026); do not copy box numbers between years. Retain the submission receipt and reconcile certificates, allowances, loss pots and foreign tax before filing.
- **With the bank, not the tax office:** the Freistellungsauftrag before income arrives; the loss certificate request by 15 December ([§ 43a(3) EStG](https://www.gesetze-im-internet.de/estg/__43a.html)).
- Special bank-withholding interpretations, insurance benefits, relatedness disputes and non-assessment certificates: Check this point with one of our partner accountants.

| Return | Deadline | Source |
| --- | --- | --- |
| 2025 return, filed by the client | 31 July 2026, passed. File now | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| 2025 return, prepared by a Steuerberater | 28 February 2027 is a Sunday, so Monday 1 March 2027 | [§ 149(3) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html); [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| 2026 return, filed by the client | 31 July 2027 is a Saturday, so Monday 2 August 2027 | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html); [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| 2026 return, prepared by a Steuerberater | Tuesday 29 February 2028 | [§ 149(3) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |

These are ordinary mandatory calendar-year return deadlines, subject to a valid extension, an earlier tax-office demand under § 149(4) AO and local public holidays under § 108(3) AO; voluntary and agricultural returns need their own deadline check. For the 2025 return, use the 2025 receipt year: its Vorabpauschale is for 2024. The 2025 Vorabpauschale (2.53%) is received in 2026; the 2026 amount (3.20%) is received in 2027. The repealed derivative/bad-debt caps do not apply to an open 2025 assessment.

## Penalties and interest

| Item | Figure | Source |
| --- | --- | --- |
| Late-filing surcharge on an annual return, if imposed | 0.25% of assessed tax less prepayments/creditable withholding per started late month, minimum EUR 25; whole-euro floor, maximum EUR 25,000. Discretion/excusable delay under (1); ordinarily mandatory after 14 months or the earlier-demand deadline under (2), except an extended deadline, zero/negative tax, or assessed tax no greater than prepayments/creditable withholding under (3). First-demand relief under (5) needs separate review | [§ 152(1)–(5), (10) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Ordinary annual assessment interest under § 233a, excluding advance/withholding assessments | 0.15% per full month (1.8% yearly); ordinarily starts 15 months after the tax year, so 1 April 2028 for 2026. Round the interest base down to EUR 50; refunds are limited to the repayment and do not run before payment | [§ 233a(1)–(3) AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html), [§ 238(1), (1a), (2) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html) |
| Late-payment surcharge on assessed/declared overdue tax | 1% per started month, unpaid tax rounded down to EUR 50; three-day grace except payments under § 224(2) no. 1. No surcharge on ancillary tax charges | [§ 240(1)–(3) AO](https://www.gesetze-im-internet.de/ao_1977/__240.html) |

Do not assume a surcharge is automatic merely because a deadline passed. Extensions, zero/refund assessments, agricultural income, retrospective events/loss carrybacks, disputed notices, disclosure and penalty mitigation: Check this point with one of our partner accountants.

## Cross-border points

- Check actual German withholding on a foreign-broker account; undeclared taxable income without German withholding follows § 32d(3), and the credit follows § 32d(5), not an assumed treaty refund. Track actual fund history and loss certificates.
- Non-residence and treaty relief: use de-non-resident-tax and de-treaty-withholding-rates. These are routing pointers, not a determination. Check this point with one of our partner accountants.
- **Exit tax hold.** Before a departure, gift abroad or restriction of German taxing rights, obtain residence, acquisition/predecessor and participation history, current values and fund acquisition costs. The historical § 6 AStG residence test, deemed sale, instalments/security, reporting/acceleration, conditional return relief, pre-2022 EU/EEA deferral and the § 19(3) InvStG fund thresholds are not usable conclusions here. Use leaving-germany-exit-tax for the actual case. Check this point with one of our partner accountants.

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

**Example 4: Vorabpauschale on an equity ETF.** An accumulating equity ETF was worth EUR 50,000 on 1 January 2026 and rose by more than EUR 1,120 over 2026, with no distributions. Base return: EUR 50,000 x 70% x 3.20% = EUR 1,120. Teilfreistellung 30%, so EUR 784 is taxable. It counts as received on the first working day of 2027 ([§ 18 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__18.html), [§ 20 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__20.html)). For the preserved 2025 comparison, assume the same EUR 50,000 start value, full-year ownership, no distributions and sufficient price growth: EUR 50,000 x 70% x 2.53% = EUR 885.50, received early in 2026. The 2026 case also assumes full-year ownership.

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

**Example 7: selling a flat.** A flat bought in 2018 was let until 2023 and lived in by the owner from January 2024 until its sale in June 2026. It was the owner's home in the year of sale and the two years before, so the gain is outside § 23 even though the sale is within ten years. Had it remained let throughout instead, test the gain and the annual Freigrenze at the ordinary rate; a final tax cannot be computed without the sale price, cost, depreciation and other income (§ 23(1) no. 1 sentence 3 EStG).

## When to refer

Refer to a German Steuerberater when:

- The client is leaving Germany or giving assets abroad: apply the exit-tax hold above. Check this point with one of our partner accountants.
- Assets are held in a business, a partnership or a company.
- The case turns on a tax treaty, or on crediting foreign tax beyond the per-item cap.
- Crypto goes beyond buying, selling and swapping: staking, lending, mining, DeFi, NFTs, or tokens that work like securities.
- A § 17 sale involves a loss, shares received as a gift, a capital reduction, a liquidation or reorganisation shares; property involves mixed use or uncertain occupation. Check this point with one of our partner accountants.
- The client wants the § 32d(2) no. 3 option, which runs for four more years unless revoked and cannot be made again after revocation.

Do not state a combined flat-tax rate with church tax without the client's state church-tax rate, and do not estimate a Vorabpauschale without the fund's actual prices.

### Preserved boundary cases

These retain the original inputs; apply the conditions above before using an outcome.

| Original facts | Treatment | Source |
| --- | --- | --- |
| 0.9% throughout the five years (computed comparison with the statutory threshold) | Below the personal § 17(1) threshold; test gifts and § 17(6) reorganisation shares before treating it as flat-tax income | https://www.gesetze-im-internet.de/estg/__17.html |
| Exactly 1% during the five years, 0.5% at sale (computed comparison) | Personal § 17(1) threshold met | https://www.gesetze-im-internet.de/estg/__17.html |
| Crypto held exactly one year | Still within the ordinary § 23 period; not automatically exempt | https://www.gesetze-im-internet.de/estg/__23.html |
| Total private-sales gain EUR 999 / EUR 1,000 | Below the cliff / whole gain enters ordinary assessment, subject to the actual assessment conditions | https://www.gesetze-im-internet.de/estg/__23.html |
| Flat let earlier, then own use in sale year and two preceding years | Test the second owner-occupation exception, as in Example 7 | https://www.gesetze-im-internet.de/estg/__23.html |
| Günstigerprüfung for dividends only | Election must cover all investment income, both spouses if joint | https://www.gesetze-im-internet.de/estg/__32d.html |
| Share loss with bond interest | Share-loss pot cannot offset the interest | https://www.gesetze-im-internet.de/estg/__20.html |
| Loss-certificate request reaches bank on 16 December | After the statutory receipt deadline; ordinary bank carryforward applies | https://www.gesetze-im-internet.de/estg/__43a.html |
| Accumulating equity ETF falls in value, no distributions | No Vorabpauschale | https://www.gesetze-im-internet.de/invstg_2018/__18.html |

## Ask the client first

- Are the assets held privately or in a business, and are you married and assessed jointly?
- Which banks and brokers hold them, is any outside Germany, and how is the Freistellungsauftrag split?
- Are you a church member, and in which federal state do you live?
- Do you hold, or did you hold in the last five years, 1% or more of any company? Any free acquisition within the five years before disposal, including a chain: actual acquisition dates and each predecessor's participation/holding dates? Do you work for the company?
- For each fund: its type, price on 1 January and full assessed Vorabpauschalen during ownership, including amounts with no cash withholding. For crypto, gold and property: actual asset/token classification, purchase/sale dates, any income-producing use in a calendar year, and whether you lived in the property.
- Do you have losses carried forward or bank loss certificates, and are you planning to leave Germany?
- For financing income: actual borrower/shareholder/related-person relationships and percentages, domestic-tax/expense use, linked deposits/loans and common plan, recourse and market interest terms, plus eligible actual costs.

## Sources

Read dates below identify operative units actually read; unchanged AO proof is reused from the completed Germany employee-income and tax-optimization ledgers (26 November), after checking that it covers these ordinary calendar-year assessments. These are source checks, not accountant approval.

| Source and unit read | URL | Read on |
| --- | --- | --- |
| EStG § 1(1), resident condition | https://www.gesetze-im-internet.de/estg/__1.html | 2026-11-27 |
| EStG § 25(1), calendar assessment | https://www.gesetze-im-internet.de/estg/__25.html | 2026-11-27 |
| EStG § 20(1), (2), (4), (6)–(9), income, gain/history, pots, allowance | https://www.gesetze-im-internet.de/estg/__20.html | 2026-11-27 |
| EStG § 32d(1)–(6), flat tax, exceptions, elections, credits | https://www.gesetze-im-internet.de/estg/__32d.html | 2026-11-27 |
| EStG § 17(1)–(4), (6), holding, gain, allowance and exceptions | https://www.gesetze-im-internet.de/estg/__17.html | 2026-11-27 |
| EStG § 3 no. 40(c), partial exemption | https://www.gesetze-im-internet.de/estg/__3.html | 2026-11-27 |
| EStG § 3c(2), related deductions | https://www.gesetze-im-internet.de/estg/__3c.html | 2026-11-27 |
| EStG § 23(1)–(3), periods, exclusions, base, cliff, losses | https://www.gesetze-im-internet.de/estg/__23.html | 2026-11-27 |
| EStG § 43a(1)–(3), withholding base and loss certificates | https://www.gesetze-im-internet.de/estg/__43a.html | 2026-11-27 |
| EStG § 43(5), finality and exceptions | https://www.gesetze-im-internet.de/estg/__43.html | 2026-11-27 |
| EStG § 44(1), (1b), custodian collection, remittance and failure | https://www.gesetze-im-internet.de/estg/__44.html | 2026-11-27 |
| EStG § 44a(2), (2a), prescribed allowance order and both IDs | https://www.gesetze-im-internet.de/estg/__44a.html | 2026-11-27 |
| EStG § 51a(2c), (2d), church-tax collection and declaration | https://www.gesetze-im-internet.de/estg/__51a.html | 2026-11-27 |
| EStG § 52(28), acquisition dates and loss-cap repeal | https://www.gesetze-im-internet.de/estg/__52.html | 2026-11-27 |
| SolzG § 3(1), (3), flat-tax surcharge base/exemption exclusion | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-11-27 |
| SolzG § 4, rate and rounding | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-11-27 |
| InvStG § 2(6)–(9b), classifications, exclusions and valuation | https://www.gesetze-im-internet.de/invstg_2018/__2.html | 2026-11-27 |
| InvStG § 16(1)–(3), income and wrapper exclusions | https://www.gesetze-im-internet.de/invstg_2018/__16.html | 2026-11-27 |
| InvStG § 18(1)–(4), prepayment computation and timing | https://www.gesetze-im-internet.de/invstg_2018/__18.html | 2026-11-27 |
| InvStG § 19(1), full assessed prepayment deduction | https://www.gesetze-im-internet.de/invstg_2018/__19.html | 2026-11-27 |
| InvStG § 20(1)–(4), exemption rates and actual-quota follow-up | https://www.gesetze-im-internet.de/invstg_2018/__20.html | 2026-11-27 |
| InvStG § 21, related deductions | https://www.gesetze-im-internet.de/invstg_2018/__21.html | 2026-11-27 |
| InvStG § 56(6), protected old units and remaining allowance | https://www.gesetze-im-internet.de/invstg_2018/__56.html | 2026-11-27 |
| EStDV § 56, ordinary filing-condition reference | https://www.gesetze-im-internet.de/estdv_1955/__56.html | 2026-11-27 |
| AO § 149(1)–(4), mandatory-return deadlines; reused applicable proof | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-11-26 |
| AO § 108(3), weekend/public-holiday shift; reused proof | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-11-26 |
| AO § 152(1)–(5), (10), surcharge and exceptions; reused proof | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-11-26 |
| AO § 233a(1)–(3), ordinary interest; reused proof | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-11-26 |
| AO § 238(1), (1a), (2), rate/rounding; reused proof | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-11-26 |
| AO § 240(1)–(3), payment surcharge/grace; reused proof | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-11-26 |
| BMF 13 January 2026, one-page Basiszins/receipt letter | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2026-01-13-basiszins-berechnung-vorabpauschale.pdf?__blob=publicationFile&v=3 | 2026-11-27 |
| BMF 10 January 2025, Basiszins/receipt letter, PDF text read | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2025-01-10-basiszins-vorabpauschale-zum-2-1-2025.pdf?__blob=publicationFile&v=6 | 2026-11-27 |
| BMF 6 March 2025, crypto paragraphs 53–63 only | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2 | 2026-11-27 |
| ELSTER 2026, Anlage G/KAP/KAP-INV/SO routing only | https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2026 | 2026-11-27 |

Not yet confirmed: actual state/religious-community church-tax rate (the 8% in Example 2 is stipulated, not a state-rate conclusion); the held exit/non-resident/treaty/wrapper/complex-loss and relatedness cases, special bank interpretations and notice-specific penalty relief. None is a usable determination from this Guide. Check this point with one of our partner accountants.
