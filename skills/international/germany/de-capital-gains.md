---
name: de-capital-gains
description: "Use this skill for any German capital gains tax question. Trigger on: \"Abgeltungsteuer\", \"capital gains Germany\", \"CGT Germany\", \"Kapitalertragsteuer\", \"Sparer-Pauschbetrag\", \"sell shares Germany\", \"German exit tax\", \"Wegzugsbesteuerung\", \"leaving Germany tax shares\", \"crypto Germany CGT\", \"German investment gains\", \"German shareholder 1% rule\". Covers Abgeltungsteuer flat rate, annual exemption, offsetting losses, exit tax on departure."
version: 1.0
jurisdiction: DE
tax_year: 2026
last_updated: 2026-09-26
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - de-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Capital gains tax in Germany (Abgeltungsteuer and private sales)

## Scope

How Germany taxes an individual who is fully liable to German tax on gains from assets held privately, not in a business. It covers shares, bonds, funds and ETFs, derivatives, large shareholdings, crypto, property sold within ten years, and the exit tax on leaving Germany with shares. Primary year: 2026 (calendar year). A dated section covers the 2025 return being filed now. Figures are read from the consolidated federal law on gesetze-im-internet.de and from finance ministry (BMF) letters.

Not covered: assets held in a business or by a company, non-residents, treaty relief and foreign tax credits in detail, and crypto staking, lending or mining.

There are three regimes. Sort every asset into one of them before doing anything else:

| Regime | What falls in it | How it is taxed | Law |
| --- | --- | --- | --- |
| Flat tax (Abgeltungsteuer) | Interest, dividends, sale gains on shares, bonds, funds and ETFs, derivatives | 25% plus solidarity surcharge and church tax, usually withheld by the German bank | [§ 20](https://www.gesetze-im-internet.de/estg/__20.html) and [§ 32d EStG](https://www.gesetze-im-internet.de/estg/__32d.html) |
| Large shareholding | Sale of shares in a company where the seller held at least 1% at any time in the last five years | Partial-income method at the normal progressive rate | [§ 17 EStG](https://www.gesetze-im-internet.de/estg/__17.html) |
| Private sales | Crypto and other assets sold within one year; land and buildings sold within ten years | Normal progressive rate, nothing withheld | [§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html) |

## Ask the client first

- Are the assets held privately or in a business?
- Which banks and brokers hold them? Is any account outside Germany, so that no German tax was withheld?
- Is there a Freistellungsauftrag (allowance order) at each German bank, and how is the allowance split?
- Are you married or in a civil partnership and assessed jointly?
- Are you a member of a church that levies church tax, and in which federal state do you live?
- When was each holding bought? Was any of it bought before 2009?
- Do you hold, or did you hold at any time in the last five years, 1% or more of any company's capital? Do you work for that company? ([source](https://www.gesetze-im-internet.de/estg/__17.html))
- For funds: is each fund an equity fund, a mixed fund, a property fund or another fund? What was the price on 1 January?
- For crypto and other private sales: purchase and sale dates of each lot, swaps between coins, and any other private sales in the same year.
- For property: when was it bought, and did you live in it yourself? In which years?
- Do you have losses carried forward, or loss certificates from a bank?
- Are you planning to leave Germany, or to give shares to someone who lives abroad?

## The method, step by step

1. **Sort each asset into its regime** using the table above. The regimes do not mix: flat-tax losses cannot offset private-sales gains, and the other way round.
2. **Collect the bank tax certificates.** Each German bank withholds the flat tax, applies the allowance under the Freistellungsauftrag, and offsets losses inside the bank. The certificate shows what was withheld.
3. **List income with no German withholding.** Income paid by a foreign bank or broker must be declared in the return, and the tax office then assesses it at the flat rate ([§ 32d(3) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)).
4. **Check whether the return can fix something.** A return is worth filing where the allowance was not fully used, losses sit at one bank and gains at another, foreign tax was not credited, or church tax was not withheld ([§ 32d(4) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)).
5. **Test the normal rate (Günstigerprüfung).** On request, investment income is taxed at the client's normal rate instead, if that gives lower income tax including surcharges. The request covers all investment income for the year, and for a jointly assessed couple the income of both spouses ([§ 32d(6) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)). The allowance still applies and actual costs are still not deductible.
6. **Funds:** apply the tax-free share (Teilfreistellung) to distributions, the advance lump sum (Vorabpauschale) and sale gains. On a sale, deduct the advance lump sums already taxed.
7. **Large shareholding:** apply the partial-income method and the § 17 allowance, then add the result to the client's other income.
8. **Private sales:** check each holding period, total the year's gains and losses, and test the total against the limit.
9. **Leaving Germany:** test the exit tax before the move, not after.
10. **File** the return with Anlage KAP (investment income) and Anlage SO (private sales), and Anlage G for a § 17 sale, by the deadline in the filing section.

## Figures and rules, 2026 (unchanged from 2025 unless stated)

### Flat tax: rate and surcharges

| What | Value | Source and wording |
| --- | --- | --- |
| Income tax on private investment income | 25% | [§ 32d(1) EStG](https://www.gesetze-im-internet.de/estg/__32d.html): "beträgt 25 Prozent" |
| Solidarity surcharge, charged on the tax, not on the income | 5.5% | [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html): "5,5 Prozent der Bemessungsgrundlage" |

- **The surcharge always applies to flat-tax income.** The exemption threshold that frees most salary earners from the surcharge does not help here: on tax withheld by a bank the surcharge is charged on the withholding tax itself ([§ 3(1) no. 5 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html)), and on flat tax assessed in the return it is 5.5% regardless of the threshold (last sentence of § 4 SolzG).
- **Church tax.** For a church member the flat tax is first reduced, by a formula in § 32d(1) EStG: tax = income ÷ (4 + church tax rate). The church tax rate is set by state law and is not on the federal pages; confirm it for the client's state. Banks withhold church tax automatically unless the client has blocked the data transfer, in which case the client must declare it ([§ 51a EStG](https://www.gesetze-im-internet.de/estg/__51a.html)).
- **Foreign withholding tax** is credited against the German flat tax, capped per item of income (§ 32d(5) EStG). Treaty cases are referred out.

### Allowance (Sparer-Pauschbetrag)

| Status | Allowance | Source and wording |
| --- | --- | --- |
| Single person | EUR 1,000 | [§ 20(9) EStG](https://www.gesetze-im-internet.de/estg/__20.html): "ein Betrag von 1 000 Euro abzuziehen (Sparer-Pauschbetrag)" |
| Jointly assessed couple | EUR 2,000 | § 20(9) EStG: "ein gemeinsamer Sparer-Pauschbetrag von 2 000 Euro" |

- The allowance covers all investment income together (interest, dividends, gains). It replaces actual costs: custody fees, advice fees and interest on loans to buy investments cannot be deducted. Purchase costs and the costs of the sale itself still reduce the gain under § 20(4) EStG.
- A couple's allowance is split half each; if one spouse's income is below their half, the unused part goes to the other.
- It cannot exceed the investment income after loss offset, and an unused allowance is lost at year end. An allowance the banks did not use can be claimed in that year's return.
- **Freistellungsauftrag.** The client tells each German bank how much of the allowance to apply there, up to the total. The order only works if the client gives their tax identification number, and the spouse's for a joint order ([§ 44a(2a) EStG](https://www.gesetze-im-internet.de/estg/__44a.html)).

### Working out a gain

- Gain = sale proceeds, less costs directly tied to the sale, less the purchase cost. Foreign-currency amounts are converted into euro at the date of each transaction. For securities of the same kind in one custody account, the first bought count as the first sold ([§ 20(4) EStG](https://www.gesetze-im-internet.de/estg/__20.html)).
- **Bought before 2009.** Gains on shares are only within the flat tax if the shares were bought after 31 December 2008. A gain on older shares is not taxed, unless the holding is a large shareholding under § 17 ([§ 52(28) EStG](https://www.gesetze-im-internet.de/estg/__52.html)). Derivatives and other securities have their own start rules in the same paragraph.
- **Fund units bought before 2009** and never held in a business: growth up to 31 December 2017 is tax-free; later growth is taxable only above a one-time allowance of EUR 100,000, which the tax office tracks until it is used up ([§ 56(6) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__56.html): "100 000 Euro übersteigt").

### Losses: the offset pots

- Investment losses can only be set against investment income, never against salary, business or rental income. They cannot be carried back. Unused losses carry forward without time limit ([§ 20(6) EStG](https://www.gesetze-im-internet.de/estg/__20.html)).
- **Share pot.** Losses from selling shares can only be set against gains from selling shares.
- **General pot.** All other investment losses (bonds, funds, derivatives, worthless securities, bad debts) can be set against any investment income, including dividends and interest.
- **The old cap on derivative and bad-debt losses is gone.** A law of 21 December 2020 capped the yearly offset of losses from derivatives (Termingeschäfte) and from worthless or written-off assets and debts. Older material still quotes that cap. Both rules have since been removed from § 20(6), and they are no longer applied "auf alle offenen Fälle", that is to every year whose assessment is still open ([§ 52(28) sentences 25 and 26 EStG](https://www.gesetze-im-internet.de/estg/__52.html)). If an older assessment applied the cap and is still open, ask for it to be corrected.
- **Loss certificate (Verlustbescheinigung).** A bank offsets losses within the year and carries any rest forward inside the bank. To use them against gains at another bank, the client asks for a loss certificate. The request cannot be withdrawn and must reach the bank by 15 December of the current year; the bank then stops carrying the loss forward ([§ 43a(3) EStG](https://www.gesetze-im-internet.de/estg/__43a.html)). Losses that were subject to withholding can only be used in the return with that certificate (§ 20(6) sentence 5 EStG).

### Funds and ETFs (InvStG)

Fund income has three parts: distributions, the advance lump sum (Vorabpauschale) and the gain on sale ([§ 16 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__16.html)). The partial-income method never applies to funds. A share of each part is tax-free, depending on the fund type:

| Fund type | Test in the fund's terms | Tax-free share for a private investor | Source |
| --- | --- | --- | --- |
| Equity fund (Aktienfonds) | More than 50% of its assets continuously in equities | 30% | [§ 2(6) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__2.html); [§ 20(1) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__20.html): "Steuerfrei sind bei Aktienfonds 30 Prozent der Erträge" |
| Mixed fund (Mischfonds) | At least 25% continuously in equities | 15% (half the equity-fund share: the law says "die Hälfte") | § 2(7) and § 20(2) InvStG |
| Property fund | More than 50% continuously in property (§ 2(9) InvStG) | 60% | § 20(3) InvStG: "Bei Immobilienfonds sind 60 Prozent der Erträge steuerfrei" |
| Foreign property fund | More than 50% continuously in foreign property (§ 2(9) InvStG) | 80% | § 20(3) InvStG: "80 Prozent der Erträge steuerfrei" |
| Other funds (bond funds, money market) | None of the above | None | § 20 InvStG |

- The same share of related costs and of a loss is not deductible ([§ 21 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__21.html)).
- If a fund in fact stayed above the equity quota all year without its terms saying so, the client can apply for the tax-free share in the return with proof (§ 20(4) InvStG).

**Advance lump sum (Vorabpauschale).** Accumulating funds, and funds that distribute little, are taxed each year on a minimum return ([§ 18 InvStG](https://www.gesetze-im-internet.de/invstg_2018/__18.html)):

1. Base return = the redemption price at the start of the year × 70% of the Basiszins. ([source](https://www.gesetze-im-internet.de/invstg_2018/__18.html))
2. The base return is capped at the actual rise in price over the year plus distributions. If the fund fell in value, there is no lump sum.
3. Advance lump sum = base return less the year's distributions, never below zero.
4. In the year of purchase, cut it by one twelfth for each full month before the month of purchase.
5. It counts as received on the first working day of the next year. So the 2026 lump sum is taxed in 2027 and uses the 2026 Basiszins; the lump sum for 2025 was taxed in 2026.
6. The tax-free share from the table applies. A German bank collects the tax from the client's account or uses the allowance. On a sale, the lump sums already taxed are deducted from the gain ([§ 19(1) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__19.html)); with a foreign broker the client must track them.

| Year | Basiszins | Source and wording |
| --- | --- | --- |
| 2026 | 3.20% | [BMF letter of 13 January 2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2026-01-13-basiszins-berechnung-vorabpauschale.pdf?__blob=publicationFile&v=3): "einen Wert von 3,20 Prozent" |
| 2025 | 2.53% | [BMF letter of 10 January 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2025-01-10-basiszins-vorabpauschale-zum-2-1-2025.pdf?__blob=publicationFile&v=6): "einen Wert von 2,53 Prozent" |

### Large shareholdings (§ 17 EStG)

A sale of shares in a company, German or foreign, is taxed as business income, not under the flat tax, if the seller held at least 1% of its capital, directly or indirectly, at any time in the five years before the sale ([§ 17(1) EStG](https://www.gesetze-im-internet.de/estg/__17.html): "zu mindestens 1 Prozent beteiligt war"). The five-year look-back means a holding reduced below 1% still counts. Shares received as a gift count if the giver met the test in that period.

| What | Value | Source and wording |
| --- | --- | --- |
| Share of the sale price that is tax-free (partial-income method) | 40% | [§ 3 no. 40 letter c EStG](https://www.gesetze-im-internet.de/estg/__3.html): "40 Prozent ... des Veräußerungspreises" |
| Share of purchase cost and selling costs that may be deducted | 60% | [§ 3c(2) EStG](https://www.gesetze-im-internet.de/estg/__3c.html): "nur zu 60 Prozent abgezogen werden" |
| Allowance, scaled to the share of the company sold | EUR 9,060 | § 17(3) EStG: "soweit er den Teil von 9 060 Euro übersteigt" |
| The allowance falls by the amount the gain exceeds this, scaled the same way | EUR 36,100 | § 17(3) EStG: "den Teil von 36 100 Euro übersteigt" |

- The taxable result is added to the client's other income and taxed at the normal progressive rate. A loss is 60% deductible and can offset other income, but is barred in part where the shares were received free within five years or did not belong to a qualifying holding for the whole five years (§ 17(2) EStG). ([source](https://www.gesetze-im-internet.de/estg/__17.html))
- The allowance is small and disappears for any sizeable gain; see worked case 5.
- **Dividends from a large holding** stay under the flat tax by default. On application, the client can have them taxed under the partial-income method instead if they hold at least 25%, or at least 1% and work for the company with significant influence over its business ([§ 32d(2) no. 3 EStG](https://www.gesetze-im-internet.de/estg/__32d.html)). The application must be made with the return at the latest and, unless revoked, also applies for the following four years. It can be revoked (with the return for the first year it should no longer apply), but after revoking it the client cannot apply again for that holding. It lets financing costs be deducted at 60%.

### Private sales (§ 23 EStG): crypto, other assets and property

| Asset | Taxable if sold within | Source and wording |
| --- | --- | --- |
| Land and buildings, including flats | Ten years of purchase | [§ 23(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__23.html): "nicht mehr als zehn Jahre" |
| Other assets: crypto such as Bitcoin and Ether, gold, foreign currency, collectibles | One year of purchase | § 23(1) no. 2 EStG: "nicht mehr als ein Jahr" |

- **Owner-occupation exception.** A property is outside § 23 if the owner lived in it exclusively between purchase and sale, or in the year of sale and the two years before. Renting it out in the period breaks the first test; the second test only looks at the three calendar years ending with the sale.
- **Everyday objects** (Gegenstände des täglichen Gebrauchs) are outside § 23.
- **Gain** = sale price less purchase or building cost and costs of sale; for a rented property the cost is reduced by depreciation already claimed (§ 23(3) EStG).
- **Yearly limit (Freigrenze).** Gains are tax-free only if the client's total gain from all private sales in the calendar year is less than EUR 1,000 (§ 23(3) EStG: "weniger als 1 000 Euro"). It is a cliff, not an allowance: at EUR 1,000 or more the whole gain is taxed. Reportedly the EUR 1,000 limit applies from 2024 and a lower limit applied to 2023 and earlier years; neither the start year nor the earlier limit could be confirmed on an official page for this Guide: **check** before relying on the limit for any year before 2025. ([source](https://www.gesetze-im-internet.de/estg/__23.html))
- **Losses** from private sales can only offset private-sales gains of the same year, then of the previous year or of later years. They never offset other income (§ 23(3) EStG).
- **Crypto.** The [BMF ruling on crypto assets of 6 March 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2) says: a swap of one coin for another is a sale of the coin given up, valued at the market price of the coin received, and a new purchase, so a new one-year period starts; and the one-year period is not extended to ten years for currency tokens even if they were lent or staked. Staking, lending and mining income are referred out.
- **Which crypto lot was sold** (same ruling, paragraphs 61 and 62): identify each lot individually where possible. Where that is not possible, treat the first-bought units of that coin as sold first for the holding period, and value the sale with the average-cost method; as a simplification, first in, first out may also be used for the value. The method applies per wallet and per coin, and must be kept for that coin in that wallet until all of it has been sold.

### Exit tax (§ 6 AStG)

- **Who.** An individual who was fully liable to German tax for at least seven of the last twelve years and holds shares within § 17 (at least 1%), German or foreign ([§ 6 AStG](https://www.gesetze-im-internet.de/astg/__6.html)).
- **Triggers.** Moving the home or habitual abode out of Germany; a gift or inheritance of the shares to a person not fully liable in Germany; any other loss or limitation of Germany's right to tax the gain.
- **What happens.** A deemed sale at market value on the trigger date, taxed under the partial-income method as above.
- **Payment.** On application, seven equal yearly instalments without interest, normally only against security. The first is due within one month of the tax notice, the others on 31 July of each following year. The unpaid tax falls due within one month if an instalment is missed, the client becomes insolvent or ignores the reporting duties; on a sale or transfer of shares, or distributions worth more than a quarter of the value taxed, only the matching part falls due.
- **No open-ended deferral for moves in the EU or EEA.** That rule ended for triggers from 1 January 2022; older cases stay under the old law with changes: an old deferral is also withdrawn to the extent that distributions or capital repayments exceed a quarter of the value of the shares at the trigger ([§ 21(3) AStG](https://www.gesetze-im-internet.de/astg/__21.html)).
- **Return within seven years.** If the departure was only a temporary absence and the client becomes fully liable again within seven years, the tax falls away to the extent that: the shares were not sold, transferred or put into a business in the meantime; distributions and capital repayments were not worth more than a quarter of the value taxed; and Germany's right to tax the gain is restored at least as it stood on leaving (§ 6(3) AStG). The tax office can extend the seven years by up to five more on application, if the intention to return continues. In such a case the client can ask to pay no instalments meanwhile; if the tax then does not fall away, interest is charged for the deferral period.
- **Fund units** are also caught if the client held at least 1% of a fund's issued units at any time in the last five years, or at the time of the trigger holds units in the fund that cost at least EUR 500,000 ([§ 19(3) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__19.html): "mindestens 500 000 Euro"). Either test only applies if the client's taxable gains on the fund units are positive overall ("insgesamt positiv"). The deemed gain is flat-tax income with the fund's tax-free share.

## Boundaries and exceptions

| Situation | Treatment | Source |
| --- | --- | --- |
| Held 0.9% of a company throughout the five years | Flat tax on the sale gain (below 1%) | [§ 17(1) EStG](https://www.gesetze-im-internet.de/estg/__17.html) |
| Held exactly 1% at some point in the five years, 0.5% at sale | § 17 applies: the test is "at least" 1% at any time in the five years | § 17(1) EStG |
| Crypto held exactly one year | Taxable: the period must be more than one year ("nicht mehr als ein Jahr" is taxable) | [§ 23(1) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__23.html) |
| Total private-sales gain of EUR 999 in the year | Tax-free (less than EUR 1,000) | § 23(3) EStG |
| Total private-sales gain of EUR 1,000 in the year | Fully taxable: the limit is "weniger als" (less than) EUR 1,000 | § 23(3) EStG |
| Flat let for part of the ownership, then lived in by the owner in the year of sale and the two years before | Outside § 23 under the second owner-occupation test | § 23(1) no. 1 EStG |
| Günstigerprüfung wanted for dividends only | Not possible: all investment income, both spouses if joint | [§ 32d(6) EStG](https://www.gesetze-im-internet.de/estg/__32d.html) |
| Share losses and bond interest in one year | Share losses cannot offset the interest; they carry forward to share gains | [§ 20(6) EStG](https://www.gesetze-im-internet.de/estg/__20.html) |
| Loss certificate asked for on 16 December | Too late for that year; the bank carries the loss forward internally | [§ 43a(3) EStG](https://www.gesetze-im-internet.de/estg/__43a.html) |
| Accumulating equity ETF that fell in value in the year | No advance lump sum for that year | [§ 18(1) InvStG](https://www.gesetze-im-internet.de/invstg_2018/__18.html) |

## Worked cases

Examples use round numbers chosen for illustration. They are not official examples.

**Case 1: single investor, German bank, 2026.** Dividends EUR 1,500 and a share gain of EUR 2,500 bought after 2008; no church tax; Freistellungsauftrag for the full EUR 1,000. Taxable: EUR 4,000 less EUR 1,000 = EUR 3,000. Flat tax 25% = EUR 750. Surcharge 5.5% of EUR 750 = EUR 41.25. Total withheld EUR 791.25. No return is needed for this income unless the client wants the Günstigerprüfung. ([source](https://www.gesetze-im-internet.de/estg/__20.html))

**Case 2: losses at two banks.** In 2026 the client lost EUR 3,000 selling shares at bank A and gained EUR 5,000 selling shares at bank B. Bank B withholds on EUR 5,000 (less any allowance). The client asks bank A for a loss certificate by 15 December 2026 and files Anlage KAP; the tax office offsets the EUR 3,000 against the share gain at bank B and refunds the excess tax. Without the certificate the loss stays at bank A for 2027. ([source](https://www.gesetze-im-internet.de/estg/__43a.html))

**Case 3: advance lump sum on an equity ETF.** An accumulating equity ETF was worth EUR 50,000 on 1 January 2026 and rose by more than EUR 1,120 over 2026, with no distributions. Base return: EUR 50,000 × 70% × 3.20% = EUR 1,120 (Basiszins 2026). Tax-free share 30%, so EUR 784 is taxable. It counts as received on the first working day of 2027. For comparison, the same holding in 2025 gave EUR 50,000 × 70% × 2.53% = EUR 885.50, received early in 2026. ([source](https://www.gesetze-im-internet.de/invstg_2018/__18.html))

**Case 4: crypto and the cliff.** Bitcoin bought 1 March 2025 for EUR 10,000, sold 15 February 2026 for EUR 10,900: gain EUR 900 within one year. No other private sales: under EUR 1,000, tax-free. If the client also sold gold within a year at a EUR 200 gain, the total is EUR 1,100, and the whole EUR 1,100 is taxed at the normal rate. If the Bitcoin had been sold on 2 March 2026, more than one year after purchase, it would be outside § 23. ([source](https://www.gesetze-im-internet.de/estg/__23.html))

**Case 5: selling a 2% stake.** The client sells their whole 2% holding in a GmbH for EUR 100,000; purchase cost EUR 40,000, no selling costs. Taxable: 60% of EUR 100,000 = EUR 60,000, less 60% of EUR 40,000 = EUR 24,000, giving EUR 36,000. The allowance for a 2% stake is 2% of EUR 9,060 = EUR 181.20, and it is cut by the amount the gain exceeds 2% of EUR 36,100 = EUR 722, so it is nil. EUR 36,000 is added to the client's other income. ([source](https://www.gesetze-im-internet.de/estg/__17.html))

**Case 6: selling a flat.** A flat bought in 2018 was let until 2023 and lived in by the owner from January 2024 until its sale in June 2026. It was used as the owner's home in the year of sale and in the two years before, so the gain is outside § 23 even though the sale is within ten years. Had it still been let at sale, the whole gain would be taxed at the normal rate. ([source](https://www.gesetze-im-internet.de/estg/__23.html))

## When to refuse or refer

Refer to a German Steuerberater (tax adviser) when:

- The client is leaving Germany, or giving shares to someone abroad, with a holding of 1% or more or large fund holdings: the exit tax needs a valuation and the holding history. ([source](https://www.gesetze-im-internet.de/astg/__6.html))
- Assets are held in a business, a partnership or a company.
- The case turns on a tax treaty or on crediting foreign tax beyond the simple per-item cap.
- Crypto activity goes beyond buying, selling and swapping: staking, lending, mining, DeFi, NFTs, or tokens that work like securities.
- The § 17 sale involves a loss, shares received as a gift, a capital reduction or a liquidation.
- The client wants the § 32d(2) no. 3 option; it runs on for four more years unless revoked, and cannot be re-made after revocation.
- The exact church tax rate or church tax on a blocked data transfer matters.
- A tax year before 2024 is still open for private sales and the old limit matters.

Refuse to state a combined flat-tax rate with church tax without the client's state rate, and refuse to estimate a Vorabpauschale without the fund's actual prices.

## Filing and payment

- **No return needed** where all investment income was taxed by German banks at the right amount and nothing else requires a return. The bank's withholding settles the tax.
- **Return required** for investment income with no German withholding, such as a foreign broker account ([§ 32d(3) EStG](https://www.gesetze-im-internet.de/estg/__32d.html)), and for any private-sales or § 17 gain.
- **Forms.** Investment income goes on Anlage KAP (with Anlage KAP-INV for funds held at foreign brokers), private sales on Anlage SO, a § 17 sale on Anlage G. Returns are filed electronically through ELSTER. Form versions change each year; use the one for the tax year concerned.
- **Freistellungsauftrag and loss certificate** are handled with the bank, not the tax office: the allowance order before income arrives, the loss certificate request by 15 December.

| Return | Deadline | Source |
| --- | --- | --- |
| 2025 return, filed by the client | 31 July 2026, already passed. File now | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| 2025 return, prepared by a Steuerberater | Last day of February 2027: 28 February 2027 is a Sunday, so Monday 1 March 2027 | § 149(3) AO; [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| 2026 return, filed by the client | 31 July 2027 is a Saturday, so Monday 2 August 2027 | § 149(2) AO; § 108(3) AO |
| 2026 return, prepared by a Steuerberater | Tuesday 29 February 2028 | § 149(3) AO |

The tax office can ask for an adviser-prepared return earlier (§ 149(4) AO).

## The 2025 return (being filed now)

The rules and figures for 2025 are the same as for 2026 above, except:

- **Advance lump sum:** the lump sum for 2025 used the 2025 Basiszins of 2.53% and counted as received on the first working day of 2026, so it belongs in the 2026 return, not the 2025 one. The lump sum shown in the 2025 bank certificate is the one for 2024. ([source](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2025-01-10-basiszins-vorabpauschale-zum-2-1-2025.pdf?__blob=publicationFile&v=6))
- **Loss cap:** a 2025 assessment must not apply the old cap on derivative or bad-debt losses; the repeal covers all open years.
- **Deadlines:** see the filing table.

## Completion checklist

- [ ] Every asset sorted into flat tax, § 17 or § 23.
- [ ] Bank tax certificates collected; allowance use checked against EUR 1,000 or EUR 2,000. ([source](https://www.gesetze-im-internet.de/estg/__20.html))
- [ ] Foreign-broker income declared on Anlage KAP; foreign tax credit capped per item.
- [ ] Share losses kept in the share pot; loss certificates requested by 15 December where needed.
- [ ] Günstigerprüfung tested for all income (both spouses if joint).
- [ ] Fund type, tax-free share and advance lump sum checked for each fund, with the right Basiszins year.
- [ ] § 17 holdings tested against 1% over five years; partial-income method and allowance applied. ([source](https://www.gesetze-im-internet.de/estg/__17.html))
- [ ] Private sales: holding periods, the property owner-occupation tests, and the yearly total against the EUR 1,000 limit. ([source](https://www.gesetze-im-internet.de/estg/__23.html))
- [ ] Exit tax tested if the client is moving abroad or giving shares abroad.
- [ ] Return filed by the deadline for the year.

## Sources

- EStG [§ 3](https://www.gesetze-im-internet.de/estg/__3.html), [§ 3c](https://www.gesetze-im-internet.de/estg/__3c.html), [§ 17](https://www.gesetze-im-internet.de/estg/__17.html), [§ 20](https://www.gesetze-im-internet.de/estg/__20.html), [§ 23](https://www.gesetze-im-internet.de/estg/__23.html), [§ 32d](https://www.gesetze-im-internet.de/estg/__32d.html), [§ 43a](https://www.gesetze-im-internet.de/estg/__43a.html), [§ 44a](https://www.gesetze-im-internet.de/estg/__44a.html), [§ 51a](https://www.gesetze-im-internet.de/estg/__51a.html), [§ 52](https://www.gesetze-im-internet.de/estg/__52.html)
- SolzG [§ 3](https://www.gesetze-im-internet.de/solzg_1995/__3.html) and [§ 4](https://www.gesetze-im-internet.de/solzg_1995/__4.html)
- InvStG [§ 2](https://www.gesetze-im-internet.de/invstg_2018/__2.html), [§ 16](https://www.gesetze-im-internet.de/invstg_2018/__16.html), [§ 18](https://www.gesetze-im-internet.de/invstg_2018/__18.html), [§ 19](https://www.gesetze-im-internet.de/invstg_2018/__19.html), [§ 20](https://www.gesetze-im-internet.de/invstg_2018/__20.html), [§ 21](https://www.gesetze-im-internet.de/invstg_2018/__21.html), [§ 56](https://www.gesetze-im-internet.de/invstg_2018/__56.html)
- AStG [§ 6](https://www.gesetze-im-internet.de/astg/__6.html) and [§ 21](https://www.gesetze-im-internet.de/astg/__21.html); AO [§ 108](https://www.gesetze-im-internet.de/ao_1977/__108.html) and [§ 149](https://www.gesetze-im-internet.de/ao_1977/__149.html)
- BMF letters on the Basiszins of 10 January 2025 and 13 January 2026 (linked in the fund section); BMF ruling on crypto assets of 6 March 2025 (linked in the private-sales section); BMF ruling on the flat tax (Einzelfragen zur Abgeltungsteuer) of 14 May 2025, for bank withholding questions.

This Guide is a working aid, not advice. Exit tax, business holdings and treaty cases need a German Steuerberater.

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
