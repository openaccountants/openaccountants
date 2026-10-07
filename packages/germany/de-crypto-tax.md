---
name: de-crypto-tax
description: Use this skill whenever asked about German cryptocurrency taxation. Trigger on phrases like "Krypto Steuer", "crypto tax Germany", "Haltefrist", "§23 EStG", "private Veräußerungsgeschäfte", "Freigrenze", "staking tax Germany", "mining income Germany", "BMF Schreiben", "DeFi tax Germany", "FIFO crypto", or any question about buying, selling, staking, mining, or lending crypto as a German tax resident. This skill covers the 1-year holding period, €1,000 Freigrenze, staking/mining classification, DeFi treatment, and the BMF guidance of 10.05.2022. ALWAYS read this skill before advising on German crypto taxation.
version: 1.0
jurisdiction: DE
tax_year: 2026
last_updated: 2026-09-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Crypto tax in Germany

How Germany taxes an individual who is fully liable to German income tax and holds crypto assets (Kryptowerte) privately, not in a business. It covers selling and swapping (private sales under § 23 EStG), which units count as sold, staking and lending income (§ 22 Nr. 3 EStG), mining and forging, airdrops, hard forks, NFTs, the records the tax office expects, and the new platform reporting (DAC8 / CARF) that starts with 2026.

**Primary year: 2026 (calendar year).** A dated section covers the 2025 return being filed now. The statute figures come from the consolidated federal law on gesetze-im-internet.de. The rules on how to apply them come from the finance ministry's letter of 6 March 2025, "Einzelfragen zur ertragsteuerrechtlichen Behandlung bestimmter Kryptowerte" (GZ IV C 1 - S 2256/00042/064/043), which replaced the letter of 10 May 2022. Paragraph numbers (Rn) below all point into that letter: [BMF letter of 6 March 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2). Do not use the paragraph numbers of the 2022 letter.

**Not covered:** business holdings, wages in crypto, non-residents, treaties, VAT, gift and inheritance tax.

**How the letter sorts tokens (Rn 2 to 4)**, by function whatever the name: currency or payment tokens (means of exchange or speculation; the letter names Bitcoin and Ether), utility tokens (a right to use a network or obtain a product), security tokens (work like securities), and hybrids. A utility token used as a means of exchange is treated like a currency token when used that way.

## Ask the client first

- Held privately, or in a business or company? Any wages paid in crypto? Fully liable to German tax all year?
- Which wallets and platforms (any foreign or decentralised)? Complete exports for every year you held coins?
- For each sale, swap or crypto payment: coin, units, wallet, date bought, date sold, and for what? Can you show which units were sold, and which lot method did you use before for that coin in that wallet?
- Any staking, lending, mining, forging, airdrops or forks? For an airdrop: did you have to post, upload or hand over personal data?
- Did you stake or lend a token that is NOT a currency token?
- Any NFTs, derivatives, leveraged trading, liquidity pools or security tokens?
- Which tax report tool, price source and settings?
- Wages, other private sales in the same year, joint assessment, losses carried forward? Were earlier returns complete?

## The method, step by step

1. **Sort each asset** by function (Rn 2 to 4). Security tokens, NFTs and anything held in a business leave this Guide.
2. **Sort each event.** Sale, swap or paying with crypto: private sale, § 23 EStG (Rn 54). Passive staking and lending: § 22 Nr. 3 EStG (Rn 48, 65). Mining or forging: test [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html) first (Rn 35 to 39). Moving coins between own wallets: no sale (Rn 54).
3. **Fix the dates.** Central platform: the times it recorded. Direct trades, for example on a decentralised platform: as a rule the wallet times. A client who wants the contract date to count must prove it (Rn 55).
4. **Pick the units sold** under Rn 61 and 62 (below), per wallet and per coin, and write the method down.
5. **Test the holding period.** A sale is taxable only if the time between purchase and sale is "nicht mehr als ein Jahr", not more than one year ([§ 23(1) sentence 1 no. 2 EStG](https://www.gesetze-im-internet.de/estg/__23.html)). Each swap starts a new period for the coin received (Rn 55).
6. **Compute each taxable gain or loss:** sale price less purchase cost less costs of the sale (§ 23(3) sentence 1 EStG; Rn 57 to 60).
7. **Add up all private sales of the year per person**, crypto and non-crypto together, and test the total against the Freigrenze. A total below the limit is tax-free; at or above it, the whole total is taxed.
8. **Compute § 22 Nr. 3 income:** every reward at its euro market price when received, less the related costs, added to all other income from services of the year. Test the result against its own Freigrenze.
9. **Keep losses in their box:** § 23 losses only against § 23 gains, § 22 Nr. 3 losses only against § 22 Nr. 3 income, one year back and later years forward.
10. **Report** in Anlage SO of the income tax return through ELSTER (business mining: Anlage G and the profit statement). File on time (Filing and payment below), and keep the records listed in "Records and duties to cooperate".

## Figures for 2026 and 2025

| Figure | 2026 | 2025 | Source |
| --- | --- | --- | --- |
| Freigrenze for all private sales of the year (a cliff: the total must be BELOW it) | EUR 1,000 | EUR 1,000 | [§ 23(3) sentence 5 EStG](https://www.gesetze-im-internet.de/estg/__23.html): "weniger als 1 000 Euro"; Rn 53 |
| Same limit for years up to and including 2023 (late or corrected returns only) | n/a | n/a | Rn 53: "bis Veranlagungszeitraum 2023: 600 €" |
| Freigrenze for all income from services (§ 22 Nr. 3), tested after costs; a cliff | EUR 256 | EUR 256 | [§ 22 Nr. 3 sentence 2 EStG](https://www.gesetze-im-internet.de/estg/__22.html): "weniger als 256 Euro im Kalenderjahr" |
| Employees: untaxed side income that forces an assessment if MORE than | EUR 410 | EUR 410 | [§ 46(2) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__46.html) |
| Employees who are assessed: side income is deducted again if NOT MORE than | EUR 410 | EUR 410 | § 46(3) EStG |
| Record retention of six years applies if positive surplus income is MORE than | EUR 500,000 | EUR 500,000 | [§ 147a AO](https://www.gesetze-im-internet.de/ao_1977/__147a.html); Rn 105 |
| The same threshold from 1 January 2027 | EUR 750,000 from 2027 | n/a | § 147a AO footnote; Rn 105 |
| Late-filing surcharge per started month (tax less prepayments and withholding) | 0.25%, at least EUR 25 | same | [§ 152(5) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Flat tax on investment income, for contrast only: it does NOT apply to currency-token gains | 25% | 25% | [§ 32d(1) EStG](https://www.gesetze-im-internet.de/estg/__32d.html) |

The two Freigrenzen are separate tests. They are never added together, and using one does not use up the other. Taxable crypto gains and income are added to the client's other income and taxed at the personal progressive rate, plus solidarity surcharge and, for members, church tax. The tariff is in [§ 32a EStG](https://www.gesetze-im-internet.de/estg/__32a.html) and in the German income tax Guide, `de-einkommensteuer-freelancer`; this Guide does not compute a rate.

## Private sales: selling, swapping and paying with crypto (§ 23 EStG)

- **What is taxed.** Crypto held privately is an "anderes Wirtschaftsgut". A gain on a sale is taxable income from a private sale if not more than one year lies between purchase and sale (Rn 53, citing the Federal Fiscal Court judgment of 14 February 2023, IX R 3/22). The intention to make a profit is not tested (Rn 53).
- **A purchase and a sale are both needed (Rn 54).** A purchase is getting the coin from a third party for something in return: for euro, goods, services or other coins, and also coins received from mining or forging, lending, passive staking, and, where it applies, an ICO or an airdrop. A sale is the mirror image: a swap into euro, goods, services or other coins.
- **Swaps.** Coin for coin is a sale of the coin given up and a purchase of the coin received. The sale price is the market price of the coin RECEIVED at the time of the swap; if that cannot be found, the market price of the coin given up is accepted (Rn 58). That market price, plus incidental purchase costs, is also the purchase cost of the coin received (Rn 59). "Die Veräußerungsfristen ... beginnen nach jedem Tausch neu" (Rn 55).
- **Paying for goods or services.** The sale price is the euro price agreed; if none was stated, the market price of the coin given up (Rn 60). This includes a crypto card that sells coins at the till; the card statement is normally enough as a record (Rn 103).
- **Costs.** Transaction fees on the sale are deductible (Rn 59). Costs must be split between taxable sales and sales that are not taxable, such as sales after more than one year (Rn 57).
- **Change outputs.** For coins on the UTXO model, the "change" that flows back to the client's own key keeps the original purchase data (Rn 56).
- **Gifts.** A gift is not a sale by the giver. The recipient takes over the giver's purchase ([§ 23(1) sentence 3 EStG](https://www.gesetze-im-internet.de/estg/__23.html); Rn 75), so the giver's purchase date counts for the one-year test.
- **Market price.** The price on a trading platform or a web price list (Rn 43). A documented daily price is accepted "bis auf Weiteres" if applied evenly: one source and one method for cost and sale price (Rn 91).

### Which units were sold (Rn 61 and 62)

This matches de-capital-gains.

- **Individual identification first (Einzelbetrachtung).** Where the client can show which units were sold, those units count.
- **If that is not possible:** for the HOLDING PERIOD, the first-bought units of that coin (for example Bitcoin or Ether) count as sold first; for the VALUE, the average-cost method (Durchschnittsmethode) applies. As a simplification, first in, first out may be used for the value as well.
- **Per wallet:** "Es gilt eine walletbezogene Betrachtung." There is no single queue across all wallets.
- **Per coin:** each coin name in a wallet carries its own choice.
- **Keep it.** Inside a wallet, the chosen method stays until every unit of that coin in that wallet has been sold. After a full sale and a new purchase, the method may be changed.
- **Document it:** the method per wallet and coin, and reallocations within wallets (Rn 103).
- LIFO and "highest in, first out" are not among the methods the letter offers.

### Losses from private sales

- Losses from private sales offset only gains from private sales of the same year, up to those gains. They cannot be set against wages, business income, investment income or § 22 Nr. 3 income ([§ 23(3) sentence 7 EStG](https://www.gesetze-im-internet.de/estg/__23.html)).
- What is left reduces private-sales gains of the year before or of later years, under the rules of § 10d EStG; the remaining loss is formally determined (§ 23(3) sentence 8 EStG). On application the carry-back is waived altogether; the law allows no partial waiver ("insgesamt abzusehen", [§ 10d(1) sentence 6 EStG](https://www.gesetze-im-internet.de/estg/__10d.html)). Declare losses even in a year with no tax, so the loss is recorded.
- Is the Freigrenze tested before or after losses carried in from other years? The law tests the "Gesamtgewinn" of the year; how carried-in losses interact with the limit is a "check" point for a Steuerberater.

## Staking, lending, mining, airdrops, forks and NFTs

### Staking and lending (§ 22 Nr. 3 EStG)

- **Passive staking** (a staking pool or platform staking, without creating blocks oneself) is "in der Regel" income from services under § 22 Nr. 3 EStG (Rn 48). Running a masternode or creating blocks oneself (forging) follows the mining rules below (Rn 50).
- **Lending** income is § 22 Nr. 3 income (Rn 65): coins are let out for a time for a fee.
- **Value.** Each reward is taken at its euro market price when received (Rn 48, 65), or at a consistent daily price (Rn 91). Simplification: during the year the time the reward is booked into the wallet on claiming may be used; rewards not yet claimed count at the latest at the end of the calendar year (Rn 48a).
- **Freigrenze.** Income from services is untaxed if it is "weniger als 256 Euro im Kalenderjahr" (§ 22 Nr. 3 sentence 2 EStG). It covers ALL § 22 Nr. 3 income of the person together: staking, lending, private mining, airdrops received for a service, and non-crypto income such as occasional commissions. It is tested on income after costs (receipts less Werbungskosten), and at or above the limit the whole amount is taxed.
- **Losses** from services cannot be set against other income; they reduce § 22 Nr. 3 income of the year before or of later years under § 10d EStG (§ 22 Nr. 3 sentences 3 and 4).
- **The rewards themselves.** Each reward counts as purchased (Rn 54, 65), so each starts its own one-year period, and a later sale within that period is a private sale.
- **The staked or lent coins.** For currency tokens the one-year period is NOT extended to ten years (Rn 63). The statute extends the period to ten years for other assets "aus deren Nutzung als Einkunftsquelle zumindest in einem Kalenderjahr Einkünfte erzielt werden" ([§ 23(1) sentence 1 no. 2 sentence 4 EStG](https://www.gesetze-im-internet.de/estg/__23.html)). The letter excludes only currency tokens from that rule, so a staked or lent utility token or other non-currency token can fall under the ten-year period. Refer.
- **Lent coins coming back.** The letter does not say whether the return of lent coins is a sale (Rn 26, 65). "Check".

### Mining and forging (block creation)

- **Mining and forging are purchases**: block reward and transaction fees are both received in exchange for a service (Rn 33, 34, 42).
- **Business or not.** Block creation is a business under [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html) when independent, lasting (set up to be repeated, Rn 36), able to make a profit over time (Rn 37) and taking part in general trade, which offering computing power to the network already is (Rn 38). It is not private asset management (Rn 39). A mining pool can be a partnership depending on the contract; a staking pool is as a rule not one (Rn 40).
- **As a business:** coins received are valued at market price when received (Rn 43). With a cash-basis profit statement the receipt is business income, and the coins' cost is deducted only when they are sold or withdrawn (Rn 44). Trade tax and bookkeeping follow; refer to a business Guide.
- **Not a business**, for example because it is not lasting: § 22 Nr. 3 income ([Rn 45](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2)), valued at market price when received. Hardware and software (by depreciation where needed) and electricity are deductible costs (Rn 47). The EUR 256 limit above applies together with all other income from services (Rn 45).

### Airdrops (Rn 70 to 75)

- **Income only for a service.** An airdrop is § 22 Nr. 3 income where the client has to do something for it: for example naming the airdrop or the project in social media posts, uploading own pictures or videos (Rn 70), or handing over personal data beyond what the technical transfer needs; the public key alone is enough for a transfer (Rn 71).
- **Chance.** Where chance also decides who receives, the link between service and reward is broken or overlaid (Rn 72).
- **No service at all:** a gift may be possible, and the gift tax rules must be considered (Rn 74). Refer.
- **Value:** market price when received; if no market price can be found yet, a value of zero is accepted (Rn 73).
- **Cost for a later sale.** An airdrop received for a service is also a purchase. Its cost is the value of the data or action given, presumed (rebuttably) to equal the market price of the tokens (Rn 75).

### Hard forks (Rn 67 and 68)

- A hard fork does NOT create § 22 Nr. 3 income (Rn 68).
- Buying coins always includes a purchase of the coins a later fork creates. The cost of the original coins is split between old and new coins in the ratio of their market prices at the time of the fork. If the new coins have no value, all the cost stays with the old coins (Rn 67).
- The new coins take the purchase date of the original coins. A sale of the new coins is a private sale only if not more than one year lies between the purchase of the ORIGINAL coins and the sale (Rn 68). New coins from long-held originals can therefore be sold outside § 23 at once.

### Utility tokens, security tokens and ICOs

- **Utility tokens.** Redeeming a token for the product or service it stands for is not a sale (Rn 79). Selling a purchased utility token can be a private sale, also where it is used as a means of exchange (Rn 80).
- **Security tokens** can be securities or other financial instruments; current income and gains can then be investment income under § 20 EStG at the flat rate, depending on the token's terms (Rn 81 to 86). Refer; see de-capital-gains.
- **ICO.** Tokens bought in an ICO for euro or other coins are purchased (Rn 54); cost is what was given (Rn 59). The issuer's side is outside this Guide (Rn 76).

### NFTs

The letter says: "Auf die Besonderheiten nicht-fungibler Kryptowerte (sog. Non-Fungible-Token, NFT) wird in der vorliegenden Fassung des BMF-Schreibens nicht eingegangen" (Rn 5). The ministry's notice page for the letter also says NFTs and liquidity mining are not yet covered and that the letter will be added to over time. The law is therefore unsettled: the private-sales rule for "other assets" in § 23 EStG is the obvious starting point for an NFT bought and sold privately, but the ministry has not confirmed it, and income from creating or licensing NFTs may be business or other income. Refer, and check the ministry's site for a newer version of the letter.

### Other points the letter does not settle

Liquidity pools and liquidity mining, yield farming, wrapped tokens, governance rewards, stablecoins as such, derivatives and leveraged trading, and lost, stolen or scammed coins have no rule in the letter. A § 23 loss needs a sale, a transfer to a third party for something in return (Rn 54, 57); the letter mentions hacks only as a records risk that falls on the client (Rn 89). Do not tell a client that a lost key, a hack or a scam gives a deductible loss. Refer all of these.

## Records and duties to cooperate (Rn 87 to 105)

For crypto held privately the general duties of Rn 87 to 92 apply (Rn 100).

- **Truth and cooperation.** Returns must be made truthfully to the best of the client's knowledge ([§ 150(2) AO](https://www.gesetze-im-internet.de/ao_1977/__150.html)); the client must help establish the facts ([§ 90 AO](https://www.gesetze-im-internet.de/ao_1977/__90.html)) (Rn 88).
- **Blockchain data is the client's burden:** a public key alone is not evidence (Rn 87).
- **Extended duty for foreign and decentralised platforms.** Trading on a central platform run from abroad triggers the extended duty of § 90(2) AO: the client must clear up the facts and obtain the evidence, in particular by downloading the platforms' transaction overviews regularly and in full. Missing records and lost data, for example after a platform's insolvency or a hack, count against the client. The same applies as a rule to decentralised platforms (Rn 89).
- **Tax reports.** A report from a private provider can be the basis of the assessment if it looks plausible: nothing obviously missing (costs, wallets, platforms), consistent in itself, and not at odds with what the office knows. As a rule the report settings (prices, lot method such as first in, first out) and the tax reasoning must be shown; manual changes must be marked and explained (Rn 90). The office can ask for the files behind the report (Rn 101).
- **Minimum per sale.** Records should let each private sale be traced on its own: coin name or ticker, number of units, the gain with cost and sale price (or times and prices of purchase and sale), and the holding period (Rn 102). For lending and other services: start, end, object, fee and terms (Rn 102).
- **What the office may ask for (Rn 101, 103, 104):** for each purchase and sale the time, amount, type, platform, euro values and price source; the lot method per wallet and coin and reallocations within wallets; records of reward income (for an airdrop, its conditions); and in a single case the source of funds, wallet balances at 31 December of the year and the year before, wallet addresses, transaction hashes, platform account details, and screenshots once the office has used its own means such as a block explorer.
- **Estimation.** Where the office cannot work out the figures it estimates them under [§ 162 AO](https://www.gesetze-im-internet.de/ao_1977/__162.html). The estimate must aim at the real facts and must not be used as a penalty (Rn 92).
- **How long to keep records.** A private investor whose positive surplus income (wages, investment income, letting and § 22 income, which includes private sales) is more than the § 147a AO threshold in the figures table in a calendar year must keep the records on those receipts and costs for six years ([§ 147a AO](https://www.gesetze-im-internet.de/ao_1977/__147a.html); Rn 105). For spouses assessed jointly, each spouse's own sum counts. Below the threshold no fixed period is printed, but the purchase record is needed whenever a unit is sold, however long ago it was bought (Rn 102), and assessments stay open for four years as a rule, ten where tax was evaded and five where it was reduced through gross negligence ([§ 169(2) AO](https://www.gesetze-im-internet.de/ao_1977/__169.html)).

## Platform reporting from 2026 (DAC8 / CARF)

The enacted Kryptowerte-Steuertransparenz-Gesetz (KStTG) implements DAC8 and the OECD's CARF.

- **From 2026.** Providers' duties to identify and report users apply "erstmals für das Kalenderjahr 2026" ([§ 21 KStTG](https://www.gesetze-im-internet.de/ksttg/__21.html)). The reporting period is the calendar year ([§ 10 KStTG](https://www.gesetze-im-internet.de/ksttg/__10.html)).
- **When.** Providers report to the Federal Central Tax Office (BZSt) by 31 July for the previous reporting period ([§ 9 KStTG](https://www.gesetze-im-internet.de/ksttg/__9.html)), so the first reports for 2026 are due by 31 July 2027.
- **What.** Identity data, and per crypto asset the aggregated amounts, units and number of transactions by type, such as sales for fiat money and swaps ([§ 11 KStTG](https://www.gesetze-im-internet.de/ksttg/__11.html)).
- **Customers who do not cooperate.** A provider must remind, then warn, a user who does not supply the requested information. For a customer relationship begun by 31 December 2025, the provider must then block reportable transactions at the latest 90 days, but not before 60 days, after the original request ([§ 8 KStTG](https://www.gesetze-im-internet.de/ksttg/__8.html)).
- The client must still declare every taxable sale and reward (Rn 88).

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Currency token sold after MORE than one year | Outside § 23, not taxed | § 23(1) s. 1 no. 2 EStG; Rn 53 |
| Sold on the same calendar date one year after purchase | Still "nicht mehr als ein Jahr": taxable. The day after that date is outside | § 23 EStG; [§ 108(1) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) (periods follow the Civil Code) |
| Private-sales total, or § 22 Nr. 3 income after costs, exactly at its limit | The WHOLE amount is taxed ("weniger als") | § 23(3) s. 5; § 22 Nr. 3 s. 2 EStG |
| Currency token staked or lent | No ten-year extension | Rn 63 |
| Non-currency token staked or lent | Ten-year period may apply. Refer | § 23(1) s. 1 no. 2 s. 4 EStG |
| Move between own wallets | Not a sale; document it | Rn 54, 62, 104 |
| Swap coin for coin | Sale and new purchase; new one-year period | Rn 54, 55, 58, 59 |
| Lot cannot be identified | First in, first out for holding period; average cost for value (or first in, first out) | Rn 61 |
| Same coin in two wallets | Separate lots and methods per wallet | Rn 62 |
| Gift received | Giver's purchase date and cost carry over | § 23(1) s. 3 EStG; Rn 75 |
| Inherited coins | "Check" as a whole: § 23(1) s. 3 names only the single successor (Einzelrechtsnachfolger, a gift), not an heir. Refer | § 23(1) s. 3 EStG |
| Hard fork coins | No income; cost split by market prices; original purchase date | Rn 67, 68 |
| Airdrop with no service | No § 22 Nr. 3 income; gift tax may apply. Refer | Rn 74 |
| Airdrop with no market price at receipt | Value zero accepted | Rn 73 |
| Unclaimed staking rewards at 31 December | Count at the latest at year end | Rn 48a |
| Redeeming a utility token for its product | Not a sale | Rn 79 |
| Spouses assessed jointly | Each spouse's own sales and services are tested against the limits; the allowed official sources for this Guide do not print that sentence. "Check" | § 23(3) s. 5; § 22 Nr. 3 EStG |

## Worked cases (rules: [BMF letter](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2), [§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html))

Amounts below are example inputs, not official figures. Fees are ignored unless stated.

**Case 1: two lots in one wallet, lot not identifiable (2026).** Wallet A holds two Bitcoin: one bought 10 January 2025 for EUR 40,000, one bought 1 September 2025 for EUR 60,000. The client sells one Bitcoin on 5 March 2026 for EUR 70,000 and cannot show which unit it was.
- Holding period: first in, first out, so the January 2025 unit counts as sold. Held more than one year: outside § 23, not taxed (Rn 61).
- The client sells the second Bitcoin on 1 August 2026 for EUR 65,000. The unit left for the holding period is the September 2025 one: held not more than one year, so the sale is taxable.
- Value with the average method: cost is the average of both units, EUR 50,000, so the gain is EUR 15,000. With the first-in-first-out simplification for value, the cost is EUR 60,000 and the gain is EUR 5,000. The client must use the same method throughout for Bitcoin in Wallet A until it is empty (Rn 62), and document it (Rn 103).
- Either gain is at or above the private-sales limit, so the whole gain is taxed at the personal rate.

**Case 2: the cliff (2026).** The client's only private sale in 2026 is a coin held eight months, gain EUR 999: below EUR 1,000, tax-free. If the client also sold gold within a year at a gain of EUR 200, the total is EUR 1,199 and the whole EUR 1,199 is taxed, not just the part above the limit ([§ 23(3) sentence 5 EStG](https://www.gesetze-im-internet.de/estg/__23.html)). Losses from other private sales of the same year are set off first (§ 23(3) sentence 7).

**Case 3: staking rewards and the EUR 256 limit (2026).** Passive staking rewards worth EUR 300 at receipt; platform fees for the staking of EUR 60; no other § 22 Nr. 3 income. Income after costs is EUR 240: below the limit, not taxed. If the fees had been EUR 40, income would be EUR 260 and all EUR 260 is taxed. Each reward still starts its own one-year period for a later sale (Rn 48, 54; [§ 22 Nr. 3 EStG](https://www.gesetze-im-internet.de/estg/__22.html)).

**Case 4: an airdrop for personal data plus staking (2026).** The client had to give an email address and date of birth to receive airdropped tokens worth EUR 150 at receipt, and also received staking rewards worth EUR 200, with no costs. The airdrop is § 22 Nr. 3 income (Rn 71). Total income from services EUR 350: at or above the limit, all EUR 350 is taxed. The airdropped tokens have a cost of EUR 150 for a later sale (Rn 75).

**Case 5: hard fork (2026).** Coins bought 1 February 2026 for EUR 10,000. A hard fork on 1 May 2026 creates new coins. At the fork, the old coins are worth EUR 18,000 and the new coins EUR 2,000, together EUR 20,000. Cost split: old coins EUR 9,000, new coins EUR 1,000 (Rn 67). No income at the fork (Rn 68). The new coins are sold on 1 July 2026 for EUR 2,500: not more than one year after the purchase of the ORIGINAL coins, so a private sale with a gain of EUR 1,500. At or above the limit: taxed. Had the original coins been bought in 2024, the sale would be outside § 23.

**Case 6: late 2025 return with crypto gains.** A client filing without an adviser has taxable 2025 crypto gains and has not filed. The deadline was 31 July 2026: file now. A surcharge of 0.25% of the tax less prepayments and withheld tax per started month, at least EUR 25 per month, may be charged; it is compulsory after 14 months from the year end unless the deadline was extended, the tax is zero or negative, or the tax does not exceed the prepayments and withheld tax ([§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)).

## Tax year 2025 (returns being filed now)

- **Same rules.** The Freigrenze was EUR 1,000 and the § 22 Nr. 3 limit EUR 256 in 2025 as in 2026 ([§ 23](https://www.gesetze-im-internet.de/estg/__23.html), [§ 22](https://www.gesetze-im-internet.de/estg/__22.html)). The one-year period, the lot rules and the staking, lending, mining, airdrop and fork rules above apply to 2025.
- **Which letter.** The letter of 6 March 2025 applies from its publication in the Federal Tax Gazette to all open cases. Price determinations under the rules of the 2022 letter, and records that do not follow Rn 87 and following, are not objected to for assessment periods up to and including 2024 (Rn 106). So for 2025 returns the new record and price rules apply in full.
- **Forms and deadlines.** Use the 2025 Anlage SO; deadlines are in "Filing and payment".

## When to refuse or refer

- Crypto held in a business or a company, commercial mining or forging, or trading so frequent it may be a business (Rn 35 to 44, 52). Token issuers (Rn 76).
- Wages or bonuses paid in crypto; the letter leaves employment income out.
- NFTs, liquidity pools and liquidity mining, yield farming, wrapped tokens, governance rewards, stablecoin questions: no rule in the letter.
- Security tokens (Rn 81 to 86). Derivatives, futures, contracts for difference and leveraged trading, which the letter does not cover. See de-capital-gains.
- A non-currency token that was staked or lent (possible ten-year period).
- Lost, stolen or scammed coins, and worthless tokens.
- Airdrops with no service (possible gift tax), gifts and inheritances beyond the carry-over of purchase data.
- Clients not fully liable to German tax for the whole year, moves into or out of Germany, and treaty questions.
- Past years with undeclared crypto income. A client who finds before the assessment period ends that a return was wrong or incomplete and that tax was or may be underpaid must report it without delay and correct it ([§ 153(1) AO](https://www.gesetze-im-internet.de/ao_1977/__153.html)). Voluntary disclosure and any penalty question go to a Steuerberater or lawyer.
- No usable records: the office may estimate (§ 162 AO; Rn 92).

## Filing and payment

- **Who must file.** A person with no wages must file if total income is above the basic allowance (twice that for spouses assessed jointly) ([§ 56 EStDV](https://www.gesetze-im-internet.de/estdv_1955/__56.html)). A return is also compulsory if a remaining loss deduction was formally determined at the end of the previous year, for example a private-sales loss carried forward (§ 56 sentence 2 EStDV). An employee must be assessed if untaxed side income, such as taxable crypto gains or staking income, is more than the § 46(2) no. 1 EStG amount in the figures table; for an employee who is assessed, such income is deducted again if it is not more than that amount in total, and above it a regulation softens the step up to full taxation (§ 46(3) and (5), [§ 46 EStG](https://www.gesetze-im-internet.de/estg/__46.html)).
- **Where.** Anlage SO of the income tax return, filed through ELSTER: the "Leistungen" block for staking, lending, private mining and airdrops, the private-sales block for sales and swaps. Business mining goes on Anlage G with the profit statement. Follow the labels of the form for the year.
- **Gains below the limits and losses.** Declare losses from private sales so they can be carried; whether gains below the limits must be entered is set by the form instructions for each year ("check" on the current form).
- **Payment.** The tax on private crypto sales and rewards is set in the income tax assessment notice and paid as that notice says.

| Return | Deadline | Source |
| --- | --- | --- |
| 2025 return, filed by the client | 31 July 2026, already passed. File now | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| 2025 return, prepared by a Steuerberater | Last day of February 2027: 28 February 2027 is a Sunday, so Monday 1 March 2027 | § 149(3) AO; [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| 2026 return, filed by the client | 31 July 2027 is a Saturday, so Monday 2 August 2027 | § 149(2) AO; § 108(3) AO |
| 2026 return, prepared by a Steuerberater | Tuesday 29 February 2028 | § 149(3) AO |

The office can ask for an adviser-prepared return earlier (§ 149(4) AO). Late filing: surcharge of 0.25% of the tax less prepayments and withheld tax per started month, at least EUR 25 per month; compulsory if the return is not in within 14 months of the year end, unless the deadline was extended, the tax is zero or negative, or the tax "die Summe der festgesetzten Vorauszahlungen und der anzurechnenden Steuerabzugsbeträge nicht übersteigt" (§ 152(3) nos. 1 to 3, [§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)).

## Completion checklist

- [ ] Assets sorted by function; NFTs, security tokens and business holdings referred.
- [ ] Complete exports from every platform and wallet (Rn 89); every sale, swap and payment listed with coin, units, dates, euro values and price source (Rn 102, 103).
- [ ] Lot method recorded per wallet and coin and kept (Rn 61, 62); holding period tested per lot.
- [ ] Private-sales total per person tested against the EUR 1,000 limit ([§ 23](https://www.gesetze-im-internet.de/estg/__23.html)); losses set off within the box.
- [ ] § 22 Nr. 3 income after costs per person tested against the EUR 256 limit ([§ 22](https://www.gesetze-im-internet.de/estg/__22.html)), with all non-crypto income from services included.
- [ ] Staked or lent non-currency tokens flagged for the ten-year rule.
- [ ] Forks and airdrops handled under Rn 67 to 75.
- [ ] Tax report settings and manual changes documented (Rn 90).
- [ ] Filing duty and deadline checked; late-filing surcharge considered; earlier years checked for § 153 AO corrections.
- [ ] § 147a AO retention checked; records kept for as long as any unit bought is still held.

## Sources

- BMF letter of 6 March 2025 on crypto assets ([PDF](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf?__blob=publicationFile&v=2)).- EStG, EStDV, AO and KStTG sections on gesetze-im-internet.de, each linked where it is used above.

This Guide is general information, not tax advice. Have a Steuerberater check a return before it is filed.

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
