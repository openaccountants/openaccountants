---
name: be-capital-gains
description: "Belgium capital gains tax for individuals from 1 January 2026 (income year 2026, assessment year 2027), under the law of 6 April 2026 and Circular 2026/C/74: the 10% tax on gains on shares, bonds, funds, ETFs, derivatives, crypto, investment gold and life insurance; the EUR 10,000 exemption and its carry-forward; the 31 December 2025 value step-up and the cost option to 2030; the 20% substantial interest scale (1.25% to 10%); internal gains (33%); speculation (33%); bank withholding and opt-out; losses; real estate gains. Trigger on: Belgium capital gains tax, meerwaardebelasting, plus-values Belgique, solidariteitsbijdrage, aanmerkelijk belang, Belgian shares gain, fotomoment."
version: 2.0
jurisdiction: BE
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium capital gains tax for individuals (income year 2026)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Belgium.

**What changed.** Until 31 December 2025, a Belgian resident who sold shares, bonds or funds in the normal management of private wealth paid no income tax on the gain. That is no longer the rule. The law of 6 April 2026 introducing a tax on capital gains on financial assets (Belgian Official Gazette 21 April 2026, Numac 2026002780) taxes gains realised from 1 January 2026. Gains that built up before that date are exempt through a value step-up to 31 December 2025.

**Tax year.** Belgium taxes the calendar income year. Income year 2026 is assessment year (aanslagjaar) 2027. Figures below are for income year 2026 unless the row says otherwise.

**Where this skill sits.**

- Leaving Belgium (exit tax on financial assets, deferral, the 24-month rule): `be-cross-border`. This skill does not repeat it.
- Crypto classification (normal management, speculation, professional activity): `belgium-crypto-tax`. Crypto gains in normal management fall under this skill's 10% regime from 2026.
- Ordinary personal income tax, the scale and municipal surcharges: `be-income-tax`.
- Gains inside a company: corporate income tax, `be-corporate-tax`. The new tax does not change corporate tax (Circular 2026/C/74, no. 4).

## 1. Who this applies to

**Residents only.** The tax applies in the personal income tax of Belgian residents (art. 2, §1, 1° WIB 92). It also applies to non-profit legal entities taxed under the legal entities tax (art. 222/1 WIB 92); those are out of scope here. It does not apply in the non-resident tax (BNI): art. 228 and 232 WIB 92 were changed so that non-residents are not taxed on these gains, including gains on Belgian shares from speculation (Circular 2026/C/74, no. 5).

**Private wealth only.** The gain must be realised outside a professional activity and in the normal management of private wealth (art. 90, first paragraph, 9° WIB 92). Gains on assets used in a business stay professional income. Gains from speculation or abnormal management are taxed at 33% under art. 90, first paragraph, 1° instead (section 3).

**Who is the taxpayer.** The owner, or the bare owner where the asset is split. A usufructuary is never taxed on these gains, and selling only the usufruct triggers no gain for the bare owner (art. 92, §3, a) WIB 92; Circular 2026/C/74, no. 12). For life insurance, the beneficiary is taxed (no. 14). For married people, common property is reported half by each spouse (art. 127 WIB 92; no. 15). A minor is taxed in their own name and has their own exemption (no. 16).

**Realisation, not gifts or death.** Only a transfer for value (onder bezwarende titel) realises a gain. Gifts and inheritances do not; the heir or donee takes over the donor's or deceased's acquisition value (art. 102, §1, second paragraph; no. 127). Treated as a transfer for value (art. 92, §2 WIB 92): payment of a life insurance capital or surrender value during life, and leaving Belgium (the exit tax, see `be-cross-border`). Every crypto-to-crypto swap and every payment with crypto is a realisation; a move between your own wallets is not (nos. 85 to 87). The trade date, not the settlement date, fixes the year (no. 18).

**The three types.** A transfer falls under one type only, the most specific (no. 9):

| Type | Article | What it covers |
|---|---|---|
| A. Internal gain | Art. 90, 9°, a) | Sale of shares or profit-sharing certificates to a company the seller controls (art. 1:14 Companies Code), alone or with close family (spouse or legal cohabitant, descendants, ascendants, relatives to the second degree, and theirs of the spouse) |
| B. Substantial interest | Art. 90, 9°, b) | Sale of shares where the seller directly holds at least 20% of the rights in the company at the moment of the sale |
| C. General regime | Art. 90, 9°, c) | Every other financial asset |

**What is a financial asset (art. 92, §1 WIB 92; nos. 61 to 82).** The list is closed:

- **Financial instruments** under art. 2, 1° of the law of 2 August 2002: listed and unlisted shares, bonds, money market instruments, units in collective investment schemes (funds, ETFs, ETNs), options, futures, swaps, CFDs and other derivatives, emission allowances. Belgian and foreign. Units in a partnership without legal personality (maatschap) count.
- **Insurance and capitalisation contracts** with a savings or investment component: branch 21, 22, 23, 26 and 44, Luxembourg "branch 6" and comparable foreign contracts. Pure credit-cover and funeral branch 21 policies are out (no. 75).
- **Crypto-assets** as defined in MiCA (Regulation 2023/1114), and NFTs that can be used for payment or investment. Security tokens are financial instruments.
- **Money and investment gold**: scriptural and electronic money not held on a payment account, investment gold (bars of at least 995/1000, coins of at least 900/1000 struck after 1800), and central bank digital currency.

Out of scope: money on a payment account (so no tax on everyday currency gains), jewellery, art, wine, collectables (no. 81).

## 2. Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| General regime (type C) rate | 10% on the net gain after the exemption, unless taxing it at the progressive scale gives less tax. No municipal surcharge | Gains from 1 January 2026 | [Art. 171, 2°, e) WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c67e2c6d-c7b0-4fef-bf88-70e579734c21); [art. 466, second paragraph](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/81bf3101-a837-4d89-8b97-713e080f00ac) |
| Basic exemption (type C) | EUR 10,000 per taxpayer (statutory base EUR 4,855, coefficient 2.0592) | Assessment year 2027 | [Art. 96/2, first paragraph, 2° WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/75fb5224-4701-4169-ac6b-26c51dfdf737); [indexation table AY 2027](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e3a471be-e270-4962-9fbf-67ce0d7571f0) |
| Supplementary exemption (carry-forward of unused basic exemption) | EUR 1,000 less the part of the basic exemption actually used the year before, if that part was under EUR 1,000 (statutory base EUR 480, to be reset by royal decree so it indexes to exactly EUR 1,000). The first one comes from income year 2026 and is usable in income year 2027 | First usable in assessment year 2028 | [Art. 96/2, first paragraph, 3° WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/75fb5224-4701-4169-ac6b-26c51dfdf737); [Circular 2026/C/74, nos. 93 to 96](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7f6b62c6-1baa-487a-8f59-c883dd5485c4) |
| Cap on supplementary exemptions used in one year | Statutory base EUR 2,426, indexed yearly; oldest used first | From assessment year 2028 | Art. 96/2, third paragraph WIB 92 |
| Substantial interest (type B) exemption | First EUR 1,000,000 of gains, one "backpack" over 5 consecutive taxable periods; not indexed | Gains from 1 January 2026 | Art. 96/2, first paragraph, 1° and second paragraph WIB 92; Circular 2026/C/74, no. 51 |
| Substantial interest scale (type B), on the gain after the exemption | 1.25% to EUR 2,500,000; 2.5% from EUR 2,500,000 to EUR 5,000,000; 5% from EUR 5,000,000 to EUR 10,000,000; 10% above EUR 10,000,000. Not indexed. No municipal surcharge | Gains from 1 January 2026 | [Art. 171, 9° to 11° and 2°, f) WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c67e2c6d-c7b0-4fef-bf88-70e579734c21) |
| Substantial interest in a Belgian company sold to a legal person established outside the EEA | 16.5% on the gain after the EUR 1,000,000 exemption, instead of the scale | Gains from 1 January 2026 | Art. 171, 4°, l) WIB 92; Circular 2026/C/74, no. 55 |
| Internal gain (type A) | 33%, no municipal surcharge | Gains from 1 January 2026 | Art. 171, 1°, a) WIB 92; Circular 2026/C/74, no. 31 |
| Speculation or abnormal management of private wealth | 33% plus municipal surcharge | Income year 2026 | Art. 90, first paragraph, 1° and art. 171, 1°, a) WIB 92; Circular 2026/C/74, no. 191 |
| Withholding tax (roerende voorheffing) by a Belgian intermediary | 10% of the gross gain on financial instruments and insurance contracts, for resident recipients, unless the client opts out | Gains paid or attributed from 1 June 2026 | [Art. 261, first paragraph, 5° and 269, §1, 5° WIB 92; Circular 2026/C/94](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a64fb047-7cc0-4c60-81ca-35a4ab745e55) |
| Undeveloped land in Belgium, sold within 5 years of acquisition | 33% plus municipal surcharge | Income year 2026 | [Art. 90, first paragraph, 8° WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5e4a1456-519a-415a-942b-060dbf9e842d); art. 171, 1°, b) |
| Undeveloped land in Belgium, sold after 5 but within 8 years | 16.5% plus municipal surcharge | Income year 2026 | Art. 90, first paragraph, 8° and art. 171, 4°, d) WIB 92 |
| Built property in Belgium, sold within 5 years of acquisition | 16.5% plus municipal surcharge; own home exempt | Income year 2026 | Art. 90, first paragraph, 10° and art. 171, 4°, e) WIB 92; [art. 93bis](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/91a62944-b475-4fae-84a6-8986bda09d36) |
| Stock exchange tax (TOB), per transaction, not deductible from the gain | 0.12% capped at EUR 1,300 (bonds, distribution fund units, regulated real estate companies); 0.35% capped at EUR 1,600 (shares and other securities); 1.32% capped at EUR 4,000 (accumulating fund units) | 2026 | [Art. 121 Code of miscellaneous duties and taxes](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d80a8f94-bc90-45c8-9306-1df94b621018); [art. 124](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d8d56231-7ed6-494e-bcce-e5ad1a49eae7) |

**The 16.5% non-EEA rule.** The old rule (art. 90, first paragraph, 9°, second dash, to income year 2025) taxed at 16.5% a sale of shares in a Belgian company to a non-EEA legal person where the seller's family held more than 25% in the previous five years. It was repealed together with its anti-abuse rule in art. 94 (Circular 2026/C/74, nos. 39 to 41). A narrower 16.5% rule replaces it inside type B: it applies only to a seller who personally holds at least 20%, after the EUR 1,000,000 exemption (no. 55).

## 3. The base

### Type C (general regime): the default for investors

**Gain = price received minus acquisition value (art. 102, §1 WIB 92).** Costs and taxes on the purchase or sale (brokerage fees, TOB, valuation fees) are not deducted (no. 130). Foreign currency amounts are converted at the rate on the purchase date and on the sale date (no. 129). Identical assets are matched first in, first out, applied per securities account (no. 144). If the acquisition value cannot be shown, the whole price is the gain (art. 102, §1, sixth paragraph); for assets held before 2026 the 31 December 2025 value is the fallback, and possession before 2026 can be proved by any means except an oath (no. 149).

**The 31 December 2025 step-up (art. 102, §4 WIB 92).** For assets acquired before 1 January 2026, the acquisition value is their value on 31 December 2025 (the "snapshot", fotomoment):

- **Listed** on a regulated market or another regularly operating public market (including MTFs such as Euronext Growth and Euronext Access): the last closing price of 2025. Your own bank's closing exchange rate may be used (no. 166).
- **Unlisted:** the highest of (a) the price in an arm's length transfer, or at incorporation or the last capital increase, between 1 January and 31 December 2025; (b) the value under a valuation formula in a contract or put option offer in force on 1 January 2026; (c) for shares, equity plus four times EBITDA of the last financial year closed before 1 January 2026 (equity alone if EBITDA is negative). Instead of (c), or where none of the methods works, a company auditor or certified accountant who is not the company's usual practitioner may value the asset at 31 December 2025, no later than 31 December 2027 (nos. 158 to 160).
- **Investment gold:** reference value of EUR 117,910 per kg of 24-carat gold on 31 December 2025, with a list in annex I to the circular (no. 163).
- **Crypto:** the price at the snapshot, proven by any means; a screenshot of the trading app is enough (no. 164).
- **Arriving residents:** assets are taken at their value on the first day of Belgian residence, not the snapshot (art. 102, §3; no. 150).

**The historical cost option to 2030 (art. 102, §4, fourth paragraph).** For sales up to 31 December 2030 of assets acquired before 2026, the taxpayer may ask that the gain be computed on the real acquisition value instead of the snapshot. It only helps when the real cost is higher than the snapshot. The cost is the average purchase price of the identical assets held before 31 December 2025 (not FIFO), and the taxpayer must prove it. A higher real cost can reduce the gain to zero but never creates a loss (nos. 167 and 168). The statute says sales "up to" (tot) 31 December 2030; the circular reads it as up to and including that date.

**Exemption.** Each taxpayer has one EUR 10,000 basic exemption for assessment year 2027, across all type C gains, own accounts and any accounts managed for an association without legal personality (no. 102). It is reduced by months when the taxable period is not a full calendar year (arrival, departure; not death), counting each month whose 15th day falls in the period, rounded to a multiple of EUR 10 (art. 129/1 WIB 92). Unused basic exemption builds the supplementary exemption from 2027 (see section 2). Supplementary exemptions are used before the basic exemption (no. 98). Choosing when to sell to use the exemptions is not abuse (no. 101).

**Losses (art. 102, §5 WIB 92).** A loss reduces gains only if it is realised (1) in the same taxable period, (2) by the same taxpayer and (3) in the same type (A, B or C). There is no carry-forward or carry-back. Within type C, all asset classes mix: a loss on crypto or on an insurance product offsets a gain on listed shares in the same year (no. 174). For assets acquired before 2026, the loss is measured from the 31 December 2025 value, not from cost (art. 102, §5, third paragraph). Within type B, a loss may be set against the gain taxed at the highest rate, such as a non-EEA sale at 16.5% (no. 175).

**Specific exemptions (art. 96/2 WIB 92).** Contribution of shares to a company or to a partnership without legal personality: exempt, the original acquisition value carries over to the new shares (4°; nos. 32 and 139). Assets of a pension savings or long-term savings product that got a tax reduction: out (5°). Income already taxed as movable income or professional income, or subject to the long-term savings tax: out (6°), for example life insurance paid within 8 years (no. 108). For fund units caught by the Reynders tax (art. 19bis), the art. 19bis taxable amount is taxed at 30% as movable income and deducted from the capital gain; only the rest is taxed at 10% (nos. 201 to 203). Look-through income already taxed under the Cayman tax: out (7°). Division of jointly held assets within three years of a death, divorce or end of cohabitation: exempt, the original acquisition value carries over (8°; nos. 111 to 114). Reorganisations of investment funds (mergers, splits) are tax neutral (art. 95/1 and 96/1; no. 115).

### Type B (substantial interest)

- The seller must directly hold at least 20% of the rights in the capital at the moment of each sale, counting all share classes together whatever their votes; family holdings are not added (nos. 45 to 49). Profit-sharing certificates, options and warrants do not count toward the 20%, and only "shares" qualify for type B.
- Married couple with the shares in common property: 40% is needed (no. 48). Full ownership and bare ownership add up; usufruct does not.
- The test is per sale: selling 10% and then 15% out of 25% in the same year gives type B for the first sale only.
- Who the buyer is does not matter, except the 16.5% non-EEA rule.
- The EUR 1,000,000 exemption is reduced by what was exempted under the same rule in the four previous taxable periods, and pro rata for a short period other than by death (no. 51).

### Type A (internal gain)

Selling shares or profit-sharing certificates to a company you control, alone or with close family, is taxed at 33% on the full gain, with no exemption. A contribution of shares in exchange for new shares is exempt instead (art. 96/2, 4°), but a contribution of profit-sharing certificates is not (nos. 24 to 35). A sale to a buyer you control jointly with a private equity fund is not an internal gain (no. 30). Type A always takes priority over type B.

### Speculation and abnormal management (art. 90, first paragraph, 1° WIB 92)

A gain the taxpayer reports under the 10% regime is presumed correct; the administration carries the burden of proving speculation or abnormal management (no. 192). The test is what a normally prudent person would do with private wealth. For crypto, the circular lists the share of wealth invested in crypto, borrowing to buy it, and the use of automated trading software, weighed together, not one alone (no. 192). Gains on assets outside art. 92 (art, collectables, NFTs that are not for payment or investment) are taxed only under this rule (nos. 193 and 194). The "no tax below EUR 2,000 gross" presumption in art. 90, 1° does not cover financial assets. If the activity is professional, the gain is professional income at the progressive scale.

### Real estate gains

- **Undeveloped land in Belgium (art. 90, first paragraph, 8°):** taxed if bought for value and sold within 8 years of the authentic deed, or received by gift and sold within 3 years of the gift and within 8 years of the donor's purchase. 33% within 5 years, 16.5% after 5 years.
- **Built property in Belgium (art. 90, first paragraph, 10°):** taxed at 16.5% if bought for value and sold within 5 years, received by gift and sold within 3 years of the gift and 5 years of the donor's purchase, or if the taxpayer built on land and sold within 5 years of first use or letting where building started within 5 years of buying the land.
- **Own home exempt (art. 93bis, 1°):** no tax if the property was the taxpayer's own home for an uninterrupted period of at least 12 months before the month of sale. Up to 6 months of non-use may separate that period from the month of sale.
- Real estate gains carry municipal surcharges (art. 466 excludes only 9°). Foreign real estate is not caught by art. 90, 8° or 10°.

## 4. Deadlines and filing

| Event | What to do | When | Source |
|---|---|---|---|
| Type C gain on financial instruments or insurance at a Belgian bank, insurer or broker, no opt-out | The intermediary withholds 10% on the gross gain (snapshot value for pre-2026 assets; no exemption, no losses, no historical cost option) | From 1 June 2026, on each sale | Art. 261, first paragraph, 5° WIB 92; Circular 2026/C/94 |
| Same, with withholding | Reporting in the return is optional. Report to use the exemption, losses or a higher historical cost; the withholding is then credited against the tax and any excess is refunded | Income year 2026 return | Circular 2026/C/74, nos. 121 and 122; art. 307, §1/1, fourth paragraph WIB 92 (inserted by art. 28 law of 6 April 2026); Circular 2026/C/94 |
| Opt-out of withholding, per account or contract | All account holders tell the intermediary in writing, at account opening or before the first sale on that account; a later choice applies from the next year. Revocation: once a year, effective the next year | Before the first sale | Art. 265/1 WIB 92; art. 85/1 KB/WIB 92; Circular 2026/C/94 |
| Opt-out for income year 2026 (transitional) | Tell the intermediary by 31 August 2026; applies to the whole of 2026 | 31 August 2026 | Art. 34 law of 6 April 2026; Circular 2026/C/94 |
| Sales from 1 January to 31 May 2026 | All account holders could ask the intermediary to pay an amount equal to 10%, treated as withholding; asked by 31 August 2026, paid by 30 November 2026. Asking excludes the opt-out for 2026 | 31 August 2026 / 30 November 2026 | Art. 35 law of 6 April 2026; Circular 2026/C/74, no. 124; Circular 2026/C/94 |
| Opted-out accounts | Intermediary files a yearly BELCOTAX form 281.08 (accounts) or 281.09 (insurance) with the total gains | Before 1 March of the following year | Art. 85/1, §1 KB/WIB 92 |
| Opted-out gains, crypto, money, gold, foreign accounts, types A and B, exit tax | Must be reported in the personal income tax return | Income year 2026 return (assessment year 2027), filed in 2027 | Art. 313 WIB 92; Circular 2026/C/74, nos. 38, 59 and 120 |
| Types A and B sales | Every Belgian-linked intermediary that designs, offers or manages the sale must report it to the administration once carried out | When the transaction is carried out | Art. 326bis WIB 92; Circular 2026/C/74, nos. 211 to 215 |
| Unlisted assets: valuation at 31 December 2025 by auditor or certified accountant | Have it done by someone who is not the usual practitioner | By 31 December 2027 | Art. 102, §4, third paragraph WIB 92 |

## 5. Penalties and interest

- **Tax increase (art. 444 WIB 92).** Not filing, filing late or under-declaring adds 10% to 200% of the tax on the missing income, on a royal decree scale. No increase for a first offence in good faith. Only if the undeclared income reaches EUR 2,500. ([Art. 444 WIB 92, income 2026](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0))
- **Administrative fine (art. 445, §1 WIB 92).** EUR 50 to EUR 1,250 per breach. ([Art. 445 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f))
- **Late payment interest (art. 414 WIB 92).** 4% a year for calendar year 2026, charged per calendar month. ([Law of 5 May 1865, art. 2, §2/1, rates](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/da7e0caf-3428-43aa-ab80-30410a15beca))
- **Reclassification.** If the administration proves speculation, the gain moves from 10% to 33% plus municipal surcharge, and the exemption is lost for that gain.

## 6. Cross-border points

- **Arrival.** Assets are stepped up to their value on the first day of residence (art. 102, §3). The basic exemption is cut pro rata by months: arrival on 12 December 2026 gives EUR 830; arrival on 6 October 2026 gives EUR 2,500 (Circular 2026/C/74, no. 100, examples 5 and 6). A person who left and returns within 24 months keeps the original cost, increased by a foreign exit tax base actually taxed (art. 102, §3, second and third paragraphs; nos. 151 and 152).
- **Departure.** Leaving Belgium is a deemed sale (exit tax). See `be-cross-border`. Taxpayers whose residence ended before 1 May 2026 are outside the new rules (no. 235).
- **Non-residents.** Not taxed on these gains, and no withholding applies to them (art. 228 and 232 WIB 92; Circular 2026/C/94).
- **Foreign accounts and foreign assets.** Residents are taxed on gains on foreign accounts, foreign shares and foreign insurance contracts the same way. No Belgian withholding applies, so the gain must be reported. Read the applicable treaty's capital gains article before computing: some treaties give the source state the right to tax gains on shares of companies rich in real estate.
- **Belgian company shares sold to a non-EEA buyer.** Type B sellers pay 16.5% instead of the scale (section 2).

## 7. Worked examples

### Example 1: an investor with a step-up, a loss and the exemption

Facts: a Belgian resident, single, holds one Belgian securities account and has not opted out. She bought 1,000 units of an accumulating world equity ETF with no bond holdings (so the Reynders tax does not apply) in 2019 for EUR 40,000. The 2025 closing price was EUR 52, so the snapshot value is EUR 52,000. On 15 September 2026 she sells all units for EUR 70,000. On 20 October 2026 she sells 200 shares of a listed company bought in 2024 for EUR 12,000; the 2025 closing price was EUR 50 (EUR 10,000) and she sells at EUR 45 (EUR 9,000). No other sales in 2026, no speculation indicators.

1. ETF gain: EUR 70,000 - EUR 52,000 = EUR 18,000. Her real cost (EUR 40,000) is lower than the snapshot, so the 2030 historical cost option does not help.
2. Share loss: measured from the snapshot, EUR 9,000 - EUR 10,000 = EUR 1,000 loss (art. 102, §5, third paragraph). Her higher 2024 cost does not enlarge the loss.
3. Same year, same taxpayer, same type C: net gain EUR 17,000.
4. Basic exemption for assessment year 2027: EUR 10,000. Taxable: EUR 7,000.
5. Tax at 10%: EUR 700. No municipal surcharge.
6. The bank withheld 10% of the gross ETF gain, EUR 1,800, on 15 September 2026. It ignored the exemption and the loss. She reports both sales in her 2027 return so the exemption and the loss apply; she asks in that return for the EUR 1,800 to be credited against the EUR 700 and the EUR 1,100 excess to be refunded (art. 307, §1/1, fourth paragraph WIB 92, inserted by art. 28 of the law of 6 April 2026). She must keep the bank statements showing the withholding and the 31 December 2025 values.

```oa-check
name: Type C investor, ETF gain with step-up, share loss and EUR 10,000 exemption (income 2026)
inputs:
  etf_price: 70000
  etf_snapshot: 52000
  etf_cost: 40000
  share_price: 9000
  share_snapshot: 10000
  exemption: 10000
  rate: 0.10
steps:
  - etf_gain: etf_price - max(etf_snapshot, etf_cost)
  - share_result: share_price - share_snapshot
  - net_gain: etf_gain + share_result
  - taxable: max(net_gain - exemption, 0)
  - tax: taxable * rate
  - withheld: etf_gain * rate
  - withholding_above_tax: withheld - tax
expected:
  etf_gain: 18000
  share_result: -1000
  net_gain: 17000
  taxable: 7000
  tax: 700
  withheld: 1800
  withholding_above_tax: 1100
```

Edge case: had she opted out of withholding by 31 August 2026, nothing would have been withheld and the gain would have to be reported. If the share loss had been on crypto instead, it would still offset the ETF gain, because both are type C.

### Example 2: a founder sells a 30% holding

Facts: a Belgian resident founded a Belgian BV in 2012 and holds 30% of the shares in full ownership, in his own name (not common property). His shares cost EUR 18,600. There was no arm's length sale, capital increase or contractual formula in 2025. For 2025 the company's equity plus four times EBITDA is EUR 7,000,000, so his 30% is worth EUR 2,100,000 at 31 December 2025. On 10 November 2026 he sells all his shares to an unrelated German GmbH for EUR 6,100,000. He does not control the buyer. He has made no earlier type B sale.

1. Type: not internal (he does not control the buyer); he holds at least 20% directly at the sale, so type B.
2. Gain: EUR 6,100,000 - EUR 2,100,000 = EUR 4,000,000. The 2030 cost option does not help (cost EUR 18,600).
3. Exemption: EUR 1,000,000, none used in the four previous periods. Taxable: EUR 3,000,000.
4. Scale: EUR 2,500,000 at 1.25% = EUR 31,250; EUR 500,000 at 2.5% = EUR 12,500. Tax EUR 43,750. No municipal surcharge.
5. No withholding applies to type B. He must report the gain in his 2027 return, and the advisers on the deal must report the transaction (art. 326bis).

```oa-check
name: Type B substantial interest sale to an EEA buyer, EUR 6.1m price (income 2026)
inputs:
  price: 6100000
  snapshot_value: 2100000
  exemption: 1000000
  band1_top: 2500000
  band2_top: 5000000
  band3_top: 10000000
  non_eea_rate: 0.165
steps:
  - gain: price - snapshot_value
  - taxable: max(gain - exemption, 0)
  - tax_band1: min(taxable, band1_top) * 0.0125
  - tax_band2: max(min(taxable, band2_top) - band1_top, 0) * 0.025
  - tax_band3: max(min(taxable, band3_top) - band2_top, 0) * 0.05
  - tax_band4: max(taxable - band3_top, 0) * 0.10
  - tax: tax_band1 + tax_band2 + tax_band3 + tax_band4
  - tax_if_non_eea_buyer: taxable * non_eea_rate
expected:
  gain: 4000000
  taxable: 3000000
  tax_band1: 31250
  tax_band2: 12500
  tax_band3: 0
  tax_band4: 0
  tax: 43750
  tax_if_non_eea_buyer: 495000
```

Edge cases: had he sold to a US corporation (a legal person established outside the EEA), the rate would be a flat 16.5%, EUR 495,000. Had he sold to his own holding company that he controls, the whole EUR 4,000,000 gain would be an internal gain at 33% with no exemption. Had the shares been common property of a married couple, the couple would need 40% together for type B. A valuation by an independent auditor or certified accountant, done by 31 December 2027, can replace the EBITDA value if it is higher.

## 8. Ask the client first

1. Were you a Belgian resident for the whole of 2026? If you arrived or left, on what date?
2. What did you sell or swap in 2026 (shares, funds, ETFs, bonds, derivatives, crypto, gold, life insurance payouts), on which dates, and through which accounts (Belgian or foreign)? Did you opt out of withholding on any Belgian account?
3. For anything held before 2026: the 31 December 2025 value (year-end statement or closing price), and the real purchase cost if it was higher.
4. Do you hold at least 20% of any company you sold shares in, and did you sell to a company you or your family control, or to a buyer outside the EEA?
5. How do you trade: share of your wealth in crypto or leveraged products, borrowing to invest, trading bots, frequency?
6. Any sale of Belgian land or a building within 8 or 5 years of buying or receiving it, and was it your own home for 12 months?

## Sources

All read on 2026-10-22.

| Source | URL | Read on |
|---|---|---|
| FPS Finance, Circular 2026/C/74 on the tax on capital gains on financial assets in the personal income tax (22 July 2026), with the law of 6 April 2026 | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7f6b62c6-1baa-487a-8f59-c883dd5485c4 | 2026-10-22 |
| Art. 307, §1/1, fourth paragraph WIB 92 as inserted by art. 28 of the law of 6 April 2026 (credit and refund of withholding), reproduced in the annex to Circular 2026/C/74 | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7f6b62c6-1baa-487a-8f59-c883dd5485c4 | 2026-10-22 |
| FPS Finance, Circular 2026/C/94 on withholding tax on capital gains on financial assets (20 October 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a64fb047-7cc0-4c60-81ca-35a4ab745e55 | 2026-10-22 |
| Fisconetplus, art. 90 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5e4a1456-519a-415a-942b-060dbf9e842d | 2026-10-22 |
| Fisconetplus, art. 92 WIB 92 (income 2026), definition of financial assets and deemed transfers | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6bfef6a8-8c6a-4b8b-a3ee-709ae06564c4 | 2026-10-22 |
| Fisconetplus, art. 93bis WIB 92 (income 2026), own home exemption | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/91a62944-b475-4fae-84a6-8986bda09d36 | 2026-10-22 |
| Fisconetplus, art. 96/2 WIB 92 (income 2026), exemptions | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/75fb5224-4701-4169-ac6b-26c51dfdf737 | 2026-10-22 |
| Fisconetplus, art. 102 WIB 92 (income 2026), computation, snapshot, losses | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1ef83a30-bcb0-4b29-9ca9-0c8347f87f9e | 2026-10-22 |
| Fisconetplus, art. 102/1 WIB 92 (income 2026), life insurance | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e23bb84b-3ab0-4482-9e65-de7b47cbbecd | 2026-10-22 |
| Fisconetplus, art. 129/1 WIB 92 (income 2026), pro rata for short periods | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a2d5f204-9fa6-45ce-8be8-de5aba995b8f | 2026-10-22 |
| Fisconetplus, art. 171 WIB 92 (income 2026), separate rates | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c67e2c6d-c7b0-4fef-bf88-70e579734c21 | 2026-10-22 |
| Fisconetplus, art. 466 WIB 92 (income 2026), municipal surcharge base | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/81bf3101-a837-4d89-8b97-713e080f00ac | 2026-10-22 |
| Fisconetplus, art. 261 WIB 92 (income 2026), withholding debtor | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1b5988c0-f042-4847-a806-edb0e4b0f7c5 | 2026-10-22 |
| Fisconetplus, art. 265/1 WIB 92 (income 2026), opt-out | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7fa2393d-0a67-4746-b5d8-c25f2c551c84 | 2026-10-22 |
| Fisconetplus, automatic indexation, income 2026, assessment year 2027 (EUR 4,855 to EUR 10,000; coefficient 2.0592) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e3a471be-e270-4962-9fbf-67ce0d7571f0 | 2026-10-22 |
| Fisconetplus, art. 121 Code of miscellaneous duties and taxes, TOB rates | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d80a8f94-bc90-45c8-9306-1df94b621018 | 2026-10-22 |
| Fisconetplus, art. 124 Code of miscellaneous duties and taxes, TOB caps | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d8d56231-7ed6-494e-bcce-e5ad1a49eae7 | 2026-10-22 |
| Fisconetplus, art. 444 WIB 92 (income 2026), tax increases | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0 | 2026-10-22 |
| Fisconetplus, art. 445 WIB 92 (income 2026), administrative fines | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f | 2026-10-22 |
| Fisconetplus, law of 5 May 1865, art. 2, §2/1, late payment interest rates | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/da7e0caf-3428-43aa-ab80-30410a15beca | 2026-10-22 |
| Justel, list of laws amending the WIB 92 (law of 6 April 2026, Numac 2026002780) | https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&cn=1992041032&table_name=wet | 2026-10-22 |

Not yet confirmed:

- The filing deadline for the 2027 personal income tax return (income year 2026). It is set on the return form and was not published on 22 October 2026.
- The exact indexed cap on supplementary exemptions for assessment year 2028 (statutory base EUR 2,426) and the royal decree that resets the EUR 480 base so the supplementary exemption is EUR 1,000; the circular's figures for later years are hypothetical.
- Where the line between a sale "up to" 31 December 2030 (statute) and "up to and including" (circular) matters, rely on the circular only with the risk named.
- The rules for life insurance contracts (art. 102/1: premiums paid, value at 31 December 2025, the 8-year and 130% tests) are summarised, not worked through; read Circular 2026/C/74, nos. 177 to 189, before advising on a policy.
- Penalties for an intermediary that misses the art. 326bis report were not checked.

> Contributed by Ryan Duguid.

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
