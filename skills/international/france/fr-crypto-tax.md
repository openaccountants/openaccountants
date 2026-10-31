---
name: fr-crypto-tax
description: French cryptocurrency and digital asset taxation for individuals. Trigger on phrases like "crypto France impôt", "fiscalité crypto", "bitcoin impôt France", "ethereum déclaration France", "plus-value crypto", "PAMC crypto", "prix d'acquisition moyen pondéré", "formulaire 2086", "déclaration 2086", "cession crypto-actifs", "staking impôt France", "mining fiscalité", "airdrop fiscalité", "exonération 305 euros", "crypto flat tax France", "échange crypto-to-crypto", "stablecoin fiscalité", "Koinly France", "Waltio", "déclaration crypto France", "BNC staking". Covers the PAMC method, the EUR 305 exemption threshold, PFU 31.4%, barème option, form 2086, staking/mining/airdrops, and documentation obligations.
version: 1.3
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Crypto-asset tax in France (actifs numériques)

How France taxes an individual on digital assets: the flat tax on occasional disposals, the option for the progressive scale, the exemption for small yearly proceeds, what counts as a disposal, the habitual and professional cases, mining and staking, foreign account declarations, and the gain formula. Figures are for tax year 2026, meaning disposals made in 2025 and declared in 2026, and disposals made in 2026. The rates, the exemption and the micro-BNC allowance come from the tax administration's own page, modified 17 July 2026. BOI-RPPM-PVBMC-30-10 and -30-20 are in force since 2 September 2019. BOI-RPPM-PVBMC-30-30, in force since 23 April 2024, still prints an older combined rate because it was not rewritten for the 2026 social levy rise, so every rate here comes from impots.gouv.fr.

> Based on work by Romain Simon (@romainsimon), licensed under MIT. Adapted for the OpenAccountants format.

## France: Crypto-Asset Taxation (Particuliers) v1.3

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | France |
| Tax | Income tax plus social levies on gains from disposing of digital assets |
| Currency | EUR. Another currency is converted at the exchange rate on the day of the operation |
| Tax year | Calendar year, over the whole foyer fiscal |
| Primary legislation | CGI, art. 150 VH bis. Rate and scale option in CGI, art. 200 C. Foreign accounts in CGI, art. 1649 bis C |
| What a digital asset is | For 2025 disposals: the historical CoMoFi art. L. 54-10-1 definition. For 2026 disposals: the MiCA scope in current CGI art. 150 VH bis, I; see the dated source note below. Unique/nonfungible assets follow art. 150 VH ter and are outside the computation here |
| Key forms | Annexe n° 2086 (per disposal), déclaration n° 2042-C (boxes 3AN, 3BN, 3CN), imprimé n° 3916-3916 bis (foreign accounts) |
| Exemption and default rate | See the tables in Section 6 and Section 5 |
| Tax authority | Direction générale des Finances publiques |
| Verified by | Pending. A French expert-comptable or avocat fiscaliste must sign off |

## Section 2: Scope: Occasional vs Professional

Three regimes. The first question in any crypto engagement is which the client is in.

- **Occasional disposals in private wealth management: CGI, art. 150 VH bis.** The regime the rest of this Guide describes. It covers individuals tax-resident in France within CGI, art. 4 B, managing their private wealth, directly or through an interposed person. Disposals of every member of the foyer fiscal are added together. See https://bofip.impots.gouv.fr/bofip/11967-PGP.html
- **Habitual buying for resale: BIC.** Gains from "l'exercice habituel d'une activité d'achat en vue de la revente d'actifs numériques" stay in industrial and commercial profits. The administration ties this to a commercial activity within Code de commerce, art. L. 110-1.
- **Professional-like conditions: BNC, not BIC.** Since 1 January 2023 a third case sits between the two: buying, selling or exchanging digital assets "dans des conditions analogues à celles qui caractérisent une activité professionnelle", without it being the client's profession, is taxed as non-commercial profits. The case named is investors making "des opérations nombreuses et sophistiquées" all year with professional traders' tools. They pay the progressive scale plus social levies, with either the micro-BNC allowance in Section 8 or actual expenses under the déclaration contrôlée. Source: the page linked in Section 8.
- **Partnerships.** A société within CGI, art. 8, art. 8 bis or art. 8 ter, seated in France with a non-professional activity such as holding a portfolio, is an interposed person and each partner is taxed on their share. One with an industrial, commercial, artisanal, agricultural or non-commercial object falls under the professional gains regime instead, whether its disposals are habitual or occasional.

**What the official pages do NOT print.** No page read here gives a transaction count, a frequency or a share of household income that turns an occasional investor into a habitual or professional one. The only wording given is the "opérations nombreuses et sophistiquées" test above. Treat any rule of thumb as untested.

## Section 3: Taxable Events (Fait Générateur)

The taxable event is a disposal for consideration. The doctrine lists four kinds: legal tender money, a good that is not a digital asset, a digital asset exchanged with a soulte, and a service.

| Operation | Taxable? | Notes |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11967-PGP.html |
| Buy digital assets with legal tender money | No | Acquisition only |
| Sell digital assets for legal tender money | Yes | "de monnaie ayant cours légal" |
| Pay for a service with digital assets | Yes | "d'un service" |
| Exchange digital assets for a good that is not a digital asset | Yes | "de l'échange d'un bien autre qu'un actif numérique" |
| Exchange digital assets for other digital assets, no soulte | No | Sursis d'imposition, CGI art. 150 VH bis, II-A. Intercalary: no taxable event, not declared |
| Exchange digital assets for other digital assets WITH a soulte | Yes | "l'échange avec soulte entre actifs numériques est une opération imposable" |
| Digital asset to stablecoin, no soulte | No, if both units qualify within the applicable dated definition | The unit must meet the Section 1 definition; the commercial label stablecoin does not replace that test |
| Stablecoin to legal tender money | Yes | A disposal for legal tender money |
| Mining, staking | Not this regime | See Section 8 |

- **Crypto-to-crypto is a deferral, not an exemption.** An exchange without soulte gets a sursis d'imposition: the gain is not cancelled, it is carried in the portfolio and taxed when the client sells for money, a good or a service. The reference is CGI, art. 150 VH bis, II-A, not the paragraph the earlier version cited.
- **A soulte breaks the deferral.** A cash balancing payment received or paid makes the exchange taxable. A soulte received is added to the disposal price, one paid is deducted.
- **Fees paid in crypto.** Paying a platform or miner fee in digital assets is consideration for a service, so a taxable operation. As a simplification the disposal and its fees count as one operation with one gain; on a sursis exchange the fees get the same sursis.

## Section 4: PAMC Method (Prix d'Acquisition Moyen Pondéré en Continu)

### Official formula

CGI, art. 150 VH bis, III sets the gross gain as the disposal price less the product of the total acquisition price of the whole portfolio by the ratio of the disposal price to the total value of that portfolio. The doctrine prints it:

~~~
Plus ou moins-value brute = Prix de cession - [Prix total d'acquisition x Prix de cession / Valeur globale du portefeuille]
~~~

In English: gain = disposal price, less (total acquisition price x disposal price / portfolio value just before the disposal). See https://bofip.impots.gouv.fr/bofip/11968-PGP.html

### The three inputs

- **Disposal price.** The price received, plus a soulte received, less a soulte paid, then reduced on evidence by the seller's costs of that disposal. Those costs come off the first term only: not off the disposal price used inside the ratio.
- **Total acquisition price.** Everything paid or given for the portfolio, including consideration in kind and soultes paid. An asset received by inheritance or gift takes the value used for the droits de mutation à titre gratuit, or failing that its real value when it entered the client's estate. Where the client cannot produce the supporting documents for a price or value of acquisition, those assets are deemed acquired for a nil value. The total is then reduced by the fractions of initial capital contained in the price or value of each earlier disposal, whether for consideration or by gift, leaving out exchanges that got the sursis, and by soultes received on earlier exchanges. That stops one cost being counted twice. For holdings predating 2019, first establish the separate opening record below; do not include every historical acquisition indiscriminately.

**Opening on 1 January 2019.** BOI-RPPM-PVBMC-30-20, I-B-4, includes only acquisition prices of assets still held on that date. Exclude the cost of assets disposed of before 2019, whether the old disposal was taxed, exempt or wrongly undeclared. For a crypto-to-crypto exchange before 2019, even without soulte, the opening acquisition price of the assets received and still held is the value of the asset surrendered at that historical exchange; exclude the surrendered asset's earlier acquisition cost. Then apply the subsequent pooled additions, capital-fraction reductions and soultes above. For example, an asset bought for EUR 1,000 and exchanged in 2018 when the surrendered asset was worth EUR 3,000 gives EUR 3,000 opening cost for the received holding still held on 1 January 2019. With no other holdings, additions or costs, its later full sale for EUR 5,000 gives EUR 2,000 gain, not EUR 4,000. Keep the original acquisition, exchange-date valuation and opening-holding evidence. Source: https://bofip.impots.gouv.fr/bofip/11968-PGP.html
- **Portfolio value.** Every digital asset held by the foyer fiscal before the disposal, valued at that moment, whatever the storage: exchange platforms including foreign ones, personal servers, offline devices. Re-measured at every taxable disposal.

### A worked example from the doctrine

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11968-PGP.html |
| January: acquisition price, the client held nothing before | EUR 1,000 | "acquiert pour 1 000 € d'actifs numériques" |
| March: portfolio value before the disposal | EUR 1,200 | "la valeur globale de son portefeuille est de 1 200 €" |
| March: disposal price | EUR 450 | "Il réalise alors une cession pour un prix de 450 €" |
| March: fraction of the acquisition price used against this disposal | EUR 375 | The doctrine works 1000 x 450 / 1200 |
| March: the gain | EUR 75 | 450 less 375 |

At the next disposal the acquisition price is reduced by the fraction already used, so that figure is carried forward for the life of the portfolio.

### Practical consequences

- Each disposal draws on the whole portfolio, not on a chosen lot. It is not FIFO and it is not LIFO.
- It needs the complete history from the first acquisition for a post-2018 starting portfolio, or the supported 1 January 2019 opening record above and subsequent history for older holdings, and a portfolio valuation at every taxable disposal. Untaxed crypto-to-crypto exchanges still have to be traced, because they move both.

### Recommended tools

Koinly, CoinTracking, Waltio and Cryptio are commercial products, not official ones, and no page read here endorses any of them. If one is used, check it applies the formula above, including the reduction for fractions of initial capital, and keep its working.

## Section 5: Tax Rates

### Default: the prélèvement forfaitaire unique

| Component | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques |
| Total flat rate on an occasional disposal | 31.4% | "prélèvement forfaitaire unique (PFU) de 31,4 %" |
| Income tax part | 12.8% | "12,8 % d'impôt" |
| Social levies part | 18.6% | "18,6 % de prélèvements sociaux" |

The total rate above is the one the administration itself prints, whatever the number of transactions. It is charged on the net gain for the year, after this year's crypto losses (Section 7). Do not add the two parts together yourself elsewhere: BOI-RPPM-PVBMC-30-30 still prints an older combined figure.

**Which income years the rate above covers.** An occasional crypto gain bears the social levies on revenus du patrimoine, not those on produits de placement. The rise in the contribution sociale généralisée brought in by the social security financing law for 2026 applies to revenus du patrimoine from the income of 2025 declared in 2026, and only from 1 January 2026 to produits de placement such as dividends and interest. So the total above is the rate for a disposal made in 2025 and declared in 2026, and for a disposal made in 2026. A lower social levy figure quoted for investment income of 2025 belongs to produits de placement and must not be carried across to a crypto gain. Basis: loi n° 2025-1403, art. 12, and CSS, art. L136-8. See https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf

### Option barème (since revenus 2023)

- **How it is made.** Tick box 3CN. The option must be made expressly on the déclaration d'ensemble des revenus (déclaration n° 2042-C), at the latest before the filing deadline. Made late it does not exist and the flat income tax rate applies. It may still be changed before that deadline. The box is on https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques and the conditions are on https://bofip.impots.gouv.fr/bofip/11969-PGP.html
- **What it covers.** It is global for all gains of the same year within the flat rate of the first paragraph of CGI, art. 200 C, and irrevocable once the deadline passes. It is NOT the option for investment income: "Cette option est définitive et indépendante de celle qui concerne les revenus de capitaux mobiliers". The earlier version of this Guide said it was shared with dividends and interest. That is wrong.
- **Effect.** The gains join the net global income taxed on the progressive scale. No page read here prints a marginal rate below which the option always wins, so model it on the client's figures. Basis: loi n° 2021-1900, art. 79.

## Section 6: EUR 305 Exemption Threshold

| Annual total of disposal prices | Treatment | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques |
| Not more than EUR 305 | Exempt for the year | "n'excède pas 305 € au cours de l'année d'imposition" |
| More than EUR 305 | Every taxable disposal of the year is taxed, the small ones included | See the cliff example below |

- **Measured on statutory disposal prices, not on the gain.** CGI art. 150 VH bis, II-B, expressly uses the prices defined in III-A: actual consideration, including a soulte received or less one paid, reduced by evidenced seller disposal fees. The official agency page also says "montant annuel brut des cessions". This worksheet follows the statute's express III-A incorporation for the threshold, while retaining that contrary administrative gross wording. It does not reduce the price by acquisition cost. The gross disposal price remains the numerator of the portfolio quotient under the separate BOFiP fee rule in Section 4. Thus EUR 310 consideration less EUR 10 evidenced seller fees gives EUR 300 for this threshold interpretation, while the quotient numerator remains EUR 310. Without fees, EUR 305 is within the exemption and EUR 306 is over it. This is a source-combined statutory interpretation, not a printed agency example resolving its gross wording.
- **A yearly cliff, not an allowance.** Pass it by one euro and the whole year's gain is taxed, not the excess only.
- **Measured per foyer fiscal**, adding disposals made directly and through an interposed person, counting every consideration: money, a good, a service. For a disposal through an interposed person, count the client's share of the disposal price. Crypto-to-crypto exchanges without soulte are left out.
- **Exempt does not mean nothing to file.** Each disposal price still goes on the annexe. Only the gain calculation is dropped.

**The cliff, as the doctrine's own examples show it**

| Case | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11967-PGP.html |
| Three disposals, each of | EUR 100 | "un montant de 100 € chacune" |
| Those three added up, under the limit, so exempt | EUR 300 | "est de 300 € (3 x 100 €)" |
| Their gain, not taxed | EUR 90 | "s'élève à 90 €. Ainsi, le contribuable est exonéré" |
| Four disposals of the same size, added up, over the limit | EUR 400 | "est de 400 € (4 x 100 €)" |
| Their gain, taxed in full | EUR 120 | "s'élève à 120 €. Ainsi, le contribuable est imposé" |

## Section 7: Loss Offsetting

- **Within the year, yes.** Losses on taxable disposals of digital assets are set against gains on such disposals in the same year. The net figure is taxed.
- **Against other assets, no.** A crypto loss "n'est pas imputable sur les plus-values de cession d'autres biens", securities included.
- **Carry forward, no.** A net loss for the year is lost: "elle ne se reporte pas sur les années suivantes". Source: the page linked in the rate table in Section 5.
- **Losses before 2019 are dead.** Losses on disposals before 1 January 2019 cannot be set against any later gain. See https://bofip.impots.gouv.fr/bofip/11968-PGP.html

## Section 8: Staking, Mining, Airdrops

Mining and staking are NOT capital gains. They are taxed on the nature of the activity, and the administration puts both in non-commercial profits.

| Activity | Category | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques |
| Mining (minage) | BNC | "Les bénéfices issus des activités de minage ou de staking sont imposés dans la catégorie des bénéfices non commerciaux (BNC)" |
| Staking | BNC | Same sentence |
| Micro-BNC allowance, printed for the professional-conditions case in Section 2 | 34% | "un abattement de 34 % (régime micro‑BNC)" |
| Actual expenses instead, same case | Déclaration contrôlée | "soit la déduction des frais réels" |
| Habitual buying to resell, as a commercial activity | BIC | Section 2 |
| Professional-like conditions | BNC | Section 2 |

- **Why BNC and not BIC for mining.** The doctrine applies the non-commercial category, by exception, where the gains are not a capital return on an investment but the consideration for taking part in the creation or operation of the virtual unit-of-account system. See https://bofip.impots.gouv.fr/bofip/11967-PGP.html The earlier version of this Guide put mining in BIC. That is wrong.
- **These receipts are taxed on the progressive scale** plus social levies, not at the flat rate in Section 5. Value them in euro at each receipt date. A later sale of a mined or staked coin is a separate event, under Section 4.
- **Airdrops: no position here.** No page read here states how an airdrop is taxed on receipt, or whether a task performed changes that. Do not state a rule.

**Where the allowance above comes from.** The page prints it for the professional-conditions case, in the sentence before the one that puts mining and staking in non-commercial profits. It does not say in terms that a miner or a staker takes the same allowance. Micro-BNC is the ordinary regime for small non-commercial receipts, so it will usually be open to them, but that last step is an inference and not the page's words.

**The micro-BNC regime has a ceiling**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23267 |
| Receipts ceiling for the micro-BNC regime, income received in 2026, tested on 2025 or on 2024, so the regime is lost only where both years are over | EUR 83,600 | "Activité libérale (BNC) … n’a pas dépassé 83 600 €" |

## Section 9: Form 2086 (Mandatory Disclosure)

- **What goes where.** Online, fill annexe n° 2086 at step 3 under "Déclarations annexes"; the total carries itself into box 3AN for a gain or 3BN for a loss. On paper, enter it in box 3AN of the déclaration n° 2042-C, or 3BN for a loss, and attach the annexe. See https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques
- **One line per taxable disposal.** Each line carries the disposal price with any costs and any soulte received or paid, the acquisition price split into acquisition prices and fractions of initial capital, soultes received on earlier exchanges, the portfolio value at the moment of the disposal, and that disposal's gain or loss. The annexe then shows the year's gains and losses added together. Basis: CGI, ann. III, art. 41 duovicies J. See https://bofip.impots.gouv.fr/bofip/11969-PGP.html
- **Exempt year, reduced filing.** Where Section 6 exempts the year, only the price of each disposal, with its costs and any soulte, goes on the annexe. Sursis exchanges are not declared at all. Through a partnership, the interposed person files its own annexe plus the split between partners, and the individual reports only their share and that person's identity.
- **Foreign accounts and portfolios must be declared.** The 2025 version of CGI art. 1649 bis C already covers digital-asset portfolios opened, held, used or closed with an enterprise, legal person, institution or organisation established abroad. The current text from 1 July 2026 uses MiCA crypto-asset portfolios and also expressly covers unique/nonfungible crypto-assets held or used abroad. Do not reduce that statutory population to a platform-account label or apply it to every self-custody wallet without checking the statutory foreign-provider or asset limb. The administration’s 2026 filing instructions use the online procedure or imprimé n° 3916-3916 bis; the specific 2027 procedure for the enlarged population is not yet confirmed here.

**Fines for an undeclared foreign digital-asset account or portfolio**

The table retains the BOFiP account wording for historical returns. Current CGI art. 1736, X, from 1 July 2026, applies EUR 750 per undeclared portfolio or unique/nonfungible crypto-asset and EUR 125 per omission or inaccuracy, within EUR 10,000 per declaration. It doubles those two amounts to EUR 1,500 and EUR 250 if the specified foreign assets or portfolios exceed EUR 50,000 at any moment in the year. Use that current statutory unit, not a universal per-platform count; exact enlarged-population filing mechanics remain reserved.

| Case | Fine | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11969-PGP.html |
| Per account not declared | EUR 750 | "amende de 750 € par compte non déclaré" |
| Per omission or inaccuracy | EUR 125 | "125 € par omission ou inexactitude" |
| Cap per declaration | EUR 10,000 | "dans la limite de 10 000 € par déclaration" |
| Accounts worth more than this at any moment in the year: fines double | EUR 50,000 | "est supérieure à 50 000 € à un moment quelconque de l'année" |
| Then, per account not declared | EUR 1,500 | "1 500 € par compte non déclaré (au lieu de 750 €)" |
| Then, per omission or inaccuracy | EUR 250 | "250 € par omission ou inexactitude (au lieu de 125 €)" |

The doubling test is market value at any moment in the year, not value at 31 December and not the gain.

## Section 10: Documentation Requirements

The client must be able to rebuild the whole portfolio history: the formula in Section 4 needs the acquisition price and the portfolio value at every taxable disposal. Keep:

- The complete transaction history from every platform and wallet, exported.
- Proof of the date and price of every acquisition, including gifts and inheritances and the value used for the droits de mutation à titre gratuit.
- Crypto-to-crypto exchanges, untaxed though they are, because they move the acquisition price and the portfolio value, and wallet-to-wallet transfers, showing a movement was not a disposal.
- A portfolio valuation at each taxable disposal, covering every holding of the foyer fiscal on every platform, server and offline device.
- Mining and staking receipts valued in euro at each receipt date, and the exchange rate used for anything not in euro.

No page read for this Guide prints a retention period. The earlier version stated one. It has been removed rather than guessed at.

## Section 11: Conservative Defaults

| Ambiguity | Default |
| --- | --- |
| Activity classification unclear | Establish the Section 2 facts before choosing the regime. Use CGI art. 150 VH bis only for qualifying private wealth management; do not presume that an unclear activity is occasional |
| Flat rate or scale unclear | The flat rate in Section 5: the scale option is irrevocable after the deadline |
| Stablecoin to stablecoin, no soulte | Apply the dated definition in Sections 1 and 3 to both assets or rights. Only an exchange between qualifying units without soulte gets the Section 3 sursis; a stablecoin label alone does not establish either unit's statutory scope |
| A fee paid in crypto | Treat the sale and its fees as one operation, as the doctrine allows |
| Whether a foreign account, portfolio or unique/nonfungible asset must be declared | Apply the actual dated Section 9 population: foreign-provider portfolios and, under the current text, unique/nonfungible crypto-assets held or used abroad. The current Section 9 fine is per undeclared portfolio or unique/nonfungible asset, not automatically per platform account. Establish those facts before deciding the obligation; the specific enlarged-population 2027 form procedure remains reserved |
| Acquisition price cannot be evidenced | Treat only the unsupported acquisition amounts as nil, retain the documented acquisition price of the household portfolio, and apply Section 4. The whole price before selling costs is gain only if the remaining total acquisition price is zero. Keep looking for the missing evidence |
| Airdrop received | No official page read here sets a rule. Refer |

## Section 12: Key Legal References

| Rule | Reference |
| --- | --- |
| Occasional disposals by individuals; residence | CGI, art. 150 VH bis; CGI, art. 4 B |
| Sursis; exemption; gain formula; portfolio value | CGI, art. 150 VH bis, II-A; II-B; III; III-C |
| Flat income tax rate and the option for the scale | CGI, art. 200 C |
| What a digital asset is | Historical CoMoFi art. L. 54-10-1/L. 552-2 for 2025; current CGI art. 150 VH bis, I, MiCA scope for 2026; unique/nonfungible assets separately in art. 150 VH ter |
| Content of the annexe to the return | CGI, ann. III, art. 41 duovicies J and K |
| Foreign digital-asset accounts, and the fines | CGI, art. 1649 bis C and art. 1736, X |
| Commercial activity, for the BIC case | Code de commerce, art. L. 110-1 |
| Statutes: the regime, then the scale option | loi n° 2018-1317, art. 41; loi n° 2021-1900, art. 79 |
| Doctrine: scope, tax base, charge and filing | BOI-RPPM-PVBMC-30-10, -30-20, -30-30 |
| Social levies on revenus du patrimoine, and the rate rise | CSS, art. L136-8; loi n° 2025-1403, art. 12 |
| Doctrine: mining and staking in non-commercial profits | BOI-BNC-CHAMP-10-10-20-40 |

## The method, step by step

1. **Place the client in one of the three regimes in Section 2.** Habitual buying for resale as a commercial activity within Code de commerce, art. L. 110-1 is BIC. Conditions analogous to a professional activity are BNC. Everything else in private wealth management is CGI, art. 150 VH bis, at https://bofip.impots.gouv.fr/bofip/11967-PGP.html If BIC or BNC, stop: Sections 4 to 7 do not apply.
2. **List every operation of the year for the whole foyer fiscal and mark each taxable or not,** using Section 3. Sales for money, payments for goods or services and exchanges with a soulte are taxable. Exchanges between digital assets without a soulte are not, and are not declared. Then add up the statutory III-A disposal prices with the evidenced-fee/soulte treatment and express contrary agency wording in Section 6, and test the exemption in Section 6: at or under the limit the year is exempt and only the prices are filed; over it, every taxable disposal is taxed. Same page as step 1.
3. **Build the running portfolio record and compute each disposal with the formula in Section 4,** then add the year's gains and losses to one net figure. Use the supported 1 January 2019 opening record in Section 4 for older holdings; for a portfolio first acquired after 2018 start with its first acquisition. Apply subsequent additions, less fractions of initial capital already used and soultes received. The portfolio value is taken at each taxable disposal across every platform and wallet of the foyer fiscal. See https://bofip.impots.gouv.fr/bofip/11968-PGP.html
4. **Choose the rate.** The flat rate in Section 5 applies by default. Model the progressive scale on the client's numbers, and if it wins tick box 3CN on the déclaration n° 2042-C before the deadline. It is irrevocable afterwards and separate from the option for investment income. The box is on https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques and the conditions are on https://bofip.impots.gouv.fr/bofip/11969-PGP.html
5. **File** annexe n° 2086, one line per taxable disposal, total carried to box 3AN or 3BN of the déclaration n° 2042-C. See https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques
6. **Declare the foreign accounts, portfolios and assets within the applicable dated scope** in Section 9. For the historical account filing route use imprimé n° 3916-3916 bis or the online annex; check the reserved 2027 procedure before extending that route to the enlarged population. Fines and their statutory unit are in Section 9.

## Worked examples that recompute

**Example 1: the existing doctrine portfolio example, at the default rate.** For a qualifying private disposal, acquisition cost EUR 1,000, portfolio value EUR 1,200 and gross proceeds EUR 450 with no fees give capital used EUR 375 and gain EUR 75. The annual proceeds exceed EUR 305. At the stated 31.4% default rate the derived tax is EUR 23.55, assuming no other disposals, losses or scale election. The gain inputs and formula are the existing BOFiP11968 example; the tax is computed from the current agency rate.

```oa-check
name: FR crypto pooled gain, existing doctrine example
inputs:
  cost: 1000
  portfolio: 1200
  proceeds: 450
steps:
  - capital_used: cost * proceeds / portfolio
  - gain: proceeds - capital_used
  - remaining_cost: cost - capital_used
  - tax: gain * 0.314
expected:
  capital_used: 375
  gain: 75
  remaining_cost: 625
  tax: 23.55
```

**Example 2: the existing annual cliff examples.** Three EUR 100 disposals, gain EUR 90, produce EUR 300 proceeds and no tax. Four EUR 100 disposals, gain EUR 120, produce EUR 400 proceeds, so the whole EUR 120 gain is taxable. At 31.4% the derived tax is EUR 37.68, assuming the private regime, no other disposals or losses and no scale election. This is the existing BOFiP11967 three-versus-four-disposal example, not a EUR 305 allowance.

```oa-check
name: FR crypto annual proceeds cliff, existing doctrine cases
inputs:
  disposal_price: 100
  exempt_count: 3
  taxable_count: 4
  taxable_gain: 120
steps:
  - exempt_proceeds: disposal_price * exempt_count
  - taxable_proceeds: disposal_price * taxable_count
  - taxable_tax: taxable_gain * 0.314
expected:
  exempt_proceeds: 300
  taxable_proceeds: 400
  taxable_tax: 37.68
```

## Ask the client first

- How do you actually trade: bots, arbitrage, professional traders' tools, and how often? This decides between CGI art. 150 VH bis, BIC and BNC, and changes the rate, the forms and the social charges.
- Did anyone else in your household sell, spend or exchange digital assets this year? The exemption and the portfolio value cover the whole foyer fiscal.
- Did you pay for anything with crypto, swap crypto for a physical item, or take cash on top of a swap? Each is a taxable disposal clients rarely report.
- Do you have every platform and wallet export back to your first purchase, including swaps you never cashed out? Without them the acquisition price cannot be built.
- Do you hold an account with a platform established outside France, including one opened and closed this year? A separate declaration, with its own fines.
- Did you receive coins from mining, staking, a gift or an inheritance? Mining and staking are BNC income at receipt; a gift or inheritance has its own acquisition value.

## When to refuse or refer

- The client is habitual or professional (BIC or BNC). This Guide covers the occasional regime only: profits, expenses, VAT and social contributions are all outside it.
- The acquisition history cannot be rebuilt. The doctrine treats unsupported acquisitions as made for a nil value; it does not erase other documented acquisition cost in the household portfolio. Apply Section 4 with the supported remaining total, deduct evidenced selling costs as stated there, and refer where the missing history prevents a reliable calculation.
- Airdrops, hard forks, lending rewards, liquidity pool rewards and other DeFi positions: no complete treatment is supplied here. For unique/nonfungible crypto-assets, CGI art. 150 VH ter expressly routes gains to the regime of the underlying assets or rights, with art. 150 VI for the listed precious objects; it applies to disposals from 1 January 2026 (loi n° 2026-534, art. 91, II). Those underlying-asset computations remain outside this Guide, while the foreign-declaration scope in Section 9 still needs checking.
- The client is not tax-resident in France within CGI, art. 4 B, or moved in or out during the year. Residence and any treaty come first.
- Digital assets held through a company, or a partnership with a commercial object: professional gains regime. Tokens that are financial instruments within CoMoFi, art. L. 211-1 are outside the digital-asset definition.
- Past years not declared, or any question turning on a figure this Guide does not print, such as a retention period or a professional-activity test.

## Sources

- https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/11967-PGP.html Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/11968-PGP.html Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/11969-PGP.html Selected cited scope read 2026-10-29.
- Source checks on 29 October 2026: the four preceding official pages were read in their selected operative scopes. Current [CGI art. 150 VH bis and 150 VH ter](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000037943229/2026-10-29), the [2025 version](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000037943229/2025-12-31), and [loi n° 2026-534 art. 91](https://www.legifrance.gouv.fr/loda/id/LEGIARTI000054312191/2026-06-27) distinguish the dated definitions. Article 91, II, applies its 2° and 3° gain changes to disposals from 1 January 2026; the ordinance terminology text is in force from 1 July 2026. The unchanged pooled formula is not an asset-specific FIFO method.
- The foreign-reporting wording was checked in [CGI art. 1649 bis C, 2025 version](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162758/2025-12-31) and its [current version](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054339286/2026-10-29); the current fine unit is in [CGI art. 1736, X](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373979/2026-10-29). Direct HTTP requests were blocked; the rendered official provisions were actually read in a normal browser. The earlier BOFiP is retained for its historical wording, not substituted for a later statute.
- Selected repair reads, 31 October 2026: BOI-RPPM-PVBMC-30-20 I-B-4 supplies the pre-2019 opening transition; current CGI art. 150 VH bis II-B/III-A supplies the fee-adjusted threshold incorporation, with the agency's gross wording expressly retained in Section 6. The dated foreign population/fine sources above also govern the conservative defaults. These were selected retained official-source reads, not a fresh acquisition or whole-body reading claim.
- Not yet confirmed: the specific 2027 return/form implementation for the enlarged foreign-portfolio and unique/nonfungible-asset population, and a complete professional-asset versus private-asset basis transition for mining/staking receipts. This Guide does not award a receipt-value basis automatically in every later disposal. The other expressly reserved tokens and professional computations remain reserved.

> **Disclaimer:** This Guide is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable or avocat fiscaliste before filing.

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
