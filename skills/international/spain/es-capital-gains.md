---
name: es-capital-gains
description: "Spain capital gains tax: savings income rates (19%–28%), holding period, main residence exemption, reinvestment relief. Trigger on: \"Spain CGT\", \"capital gains Spain\", \"Spain savings tax rate\", \"sell shares Spain\", \"IRPF capital gains\", \"Spain property CGT\", \"Spain investment gains\", \"Spain 19% capital gains\"."
version: 1.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain capital gains tax (ganancias y pérdidas patrimoniales)

Figures are for tax year 2026. The rates, bands, ceilings and coefficients below come from the consolidated texts of Ley 35/2006 (IRPF), Real Decreto 439/2007 (Reglamento IRPF) and Real Decreto Legislativo 5/2004 (IRNR) on boe.es, which carry the law in force. Two Agencia Tributaria pages are also linked. One of them sits in the "Manual práctico de Renta 2025", the return for 2025 that is filed during 2026, and it is used here only for the conditions of the over 65 main home exemption and for the filing window of that return, never for a rate. This Guide covers common territory Spain. The Basque provinces and Navarre run their own income tax and no page on an allowed host carries their capital gains rules.

## Quick reference

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| What a gain is | A change in the value of the taxpayer's assets shown up by any alteration in their composition, unless the law calls it a rendimiento | art. 33.1 Ley 35/2006 |
| Which base | Gains and losses on a TRANSMISSION of an asset are savings income. A gain that does not come from a transmission is general income and bears the general scale, not the savings scale | art. 46.b and art. 45 |
| Holding period | Irrelevant to the rate. The savings scale is charged on the size of the savings base, not on how long the asset was held | art. 66 |
| Annual exemption | None. Spanish law gives no yearly tax free amount for gains | see the savings scale below |
| Legislation | Ley 35/2006 arts. 33 to 39, 45, 46, 48, 49, 66, 68.4 and 76; disposición transitoria novena; Reglamento IRPF arts. 41, 41 bis and 42 | consolidated text |
| Form | Modelo 100 for residents, Modelo 210 for non residents with no permanent establishment | see the method below |

## Savings income tax rates (2026)

The savings scale is charged on the savings taxable base (base liquidable del ahorro) above the personal and family minimum. It is NOT the general scale, and it is not the payroll withholding table either. These are the rates a resident bears in total.

| Band of the savings base | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Up to EUR 6,000 | 19% | art. 66.2: "0 0 6.000 19" |
| EUR 6,000 to EUR 50,000 | 21% | "6.000,00 1.140 44.000 21" |
| EUR 50,000 to EUR 200,000 | 23% | "50.000,00 10.380 150.000 23" |
| EUR 200,000 to EUR 300,000 | 27% | "200.000,00 44.880 100.000 27" |
| Above EUR 300,000 | 30% | "300.000,00 71.880 En adelante 30" |

The last band was added with effect from 1 January 2025 by Ley 7/2024. A Guide whose savings scale stops at the fourth band in the table above, or whose top rate is lower than the top rate in the table above, is describing the law before that change. The scale has been extended more than once, so check the band boundaries as well as the rates.

### The scale is really two halves, and state law fixes both

The tax has a state half and an autonomous community half. For the GENERAL scale the community sets its own half (art. 74 Ley 35/2006), so there is no single Spanish general rate. For the SAVINGS scale the community sets nothing: art. 66.1 fixes the state half and art. 76 fixes the autonomous half at the same rates. That is why the savings scale is the same across common territory Spain. Art. 66.2, written for contributors who keep Spanish contributor status while habitually resident abroad, prints the two halves already added, which is the combined table above.

| Band of the savings base | State half (art. 66.1) | Autonomous half (art. 76) |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Up to EUR 6,000 | 9.5% | 9.5% |
| EUR 6,000 to EUR 50,000 | 10.5% | 10.5% |
| EUR 50,000 to EUR 200,000 | 11.5% | 11.5% |
| EUR 200,000 to EUR 300,000 | 13.5% | 13.5% |
| Above EUR 300,000 | 15% | 15% |

A community can still change what the client finally pays, through its own deductions in the quota. Those are not in this Guide and no single official page carries them for every community. See `es-irpf-deductions`.

## Main residence exemption (reinvestment relief)

Three different reliefs are often run together. They are separate, each with its own condition and its own ceiling.

**1. Reinvestment in a new main home (art. 38.1 Ley 35/2006, art. 41 Reglamento IRPF).** The gain on selling the taxpayer's own main home is left out of charge if the WHOLE amount obtained on the transfer is reinvested in acquiring a new main home. Where only part is reinvested, only the proportional part of the gain that matches the reinvested amount is excluded. There is no cash ceiling and no age condition. Points that decide real cases:

- The reinvestment must be made, in one go or in successive steps, in a period of not more than two years from the date of the transfer. Buying the new main home in the two years BEFORE the sale also counts.
- Where the home being sold was bought with borrowed money, the "total amount obtained" is the transfer value reduced by the principal of the loan still outstanding at the moment of the transfer. This is the commonest reason a claimed full exemption turns out to be partial.
- Rehabilitating a home is treated as acquiring one. Art. 41.1 Reglamento IRPF gives two separate routes: works subsidised under the state housing plan, or works that meet both the object test and the cost test in the table below.
- Where the reinvestment does not happen in the same year as the sale, the taxpayer must state the intention to reinvest in the return for the year the gain arises.
- Main home means the building that has been the taxpayer's residence for a continuous period of at least three years, occupied within twelve months of acquisition or of the works finishing (art. 41 bis Reglamento IRPF). Death, marriage, marital separation, a job move, a first job or a change of job can excuse the three years.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Rehabilitation counts as acquisition where the works have as their main object rebuilding the home by consolidating and treating its structure, facade, roof or the like, AND their global cost exceeds this share of the purchase price, where the home was bought in the two years before the works began, or of market value in any other case, the land share being taken out of either figure | 25% | art. 41.1.b: "exceda del 25 por ciento del precio de adquisición" |

**2. Selling the main home after 65 (art. 33.4.b Ley 35/2006).** The gain is not brought into the taxable base at all. No reinvestment is needed and there is no cash ceiling. The Agencia Tributaria states the conditions on https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c11-ganancias-perdidas-patrimoniales/ganancias-perdidas-patrimoniales-que-no-bi/ganancias-patrimoniales-exentas.html : the home transferred must have been the taxpayer's habitual residence for a continuous period of at least three years, and the taxpayer must have held the full ownership (pleno dominio) of it throughout that period, even if shared. Where full ownership is split between a bare owner and a usufructuary, neither of them gets the exemption. Art. 33.4.b itself states neither condition. The three continuous years come from art. 41 bis.1 Reglamento IRPF, which applies the main home definition expressly to art. 33.4.b. The pleno dominio point is the administration's reading: the Agencia Tributaria calls it an interpretative criterion set by the Supreme Court in judgment number 1858/2018 of 20 December. Treat it as settled practice rather than as words in the statute, and say so to a client who is a bare owner or a usufructuary. The relief applies whether the home is sold for a capital sum or for a temporary or life annuity, and to a sale of the bare ownership with the life usufruct kept back. It also applies to people in a situation of severe dependency or great dependency.

A home still counts as the main home if it had that character on any day of the two years before the date of transfer (art. 41 bis.3 Reglamento IRPF). That is what lets someone who moved out shortly before selling still qualify.

**3. Over 65 reinvesting ANY asset in a life annuity (art. 38.3 Ley 35/2006, art. 42 Reglamento IRPF).** This one is not about the home. A taxpayer over 65 who sells any asset can leave the gain out of charge by putting the whole amount obtained into an insured life annuity in their own favour within six months of the transfer. Unlike the two reliefs above, this one HAS a cash ceiling, and it is a lifetime total across all such reinvestments, not a yearly allowance. Once earlier reinvestments have used the ceiling up, only the difference counts as reinvested. Where less than the whole amount goes in, only the matching share of the gain is exempt.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Maximum total that may be put into life annuities under art. 38.3, counting every earlier reinvestment | EUR 240,000 | "La cantidad máxima total que a tal efecto podrá destinarse a constituir rentas vitalicias será de 240.000 euros" |

Conditions the Reglamento adds for the annuity (art. 42): the contract is between the taxpayer, as beneficiary, and an insurance undertaking; the annuity is paid at intervals of a year or less; it must start being received within one year of being set up; the yearly amount may not fall by more than five per cent against the year before, which the Reglamento prints in words and not in digits; and the taxpayer must tell the insurer that the annuity is the reinvestment. Where the gain bore withholding and the transfer value less the withholding is put into the annuity within the six months, the deadline for the withheld part runs to the end of the following year. Taking the economic rights of the annuity early, in whole or in part, brings the gain back into charge.

## Assets bought before 31 December 1994: the abatement coefficients

The transitional rule in disposición transitoria novena Ley 35/2006 still exists. It applies to assets NOT used in a business that were acquired before 31 December 1994. It does not reduce the whole gain, and it is capped for the taxpayer's lifetime. Work it in this order:

1. Compute the gain in the ordinary way, then split off the part accrued before 20 January 2006. That part is the share of the gain matching the days between the date of acquisition and 19 January 2006, both included, over the total days the asset was held.
2. Count the holding period as the number of years between acquisition and 31 December 1996, rounded up.
3. Add up the transfer value of every asset on which these coefficients have already been used, from 1 January 2015 to the date of this transfer, and add the transfer value of this asset.
4. Apply the coefficient for each year of holding under step 2 that exceeds two, but only while the running total in step 3 stays under the ceiling.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Immovable property, rights over it, and securities of the entities in art. 108 Ley 24/1988, but NOT shares or units representing the capital or assets of a Sociedad or Fondo de Inversión Inmobiliaria, per year of holding beyond two | 11.11% | "con excepción de las acciones o participaciones representativas del capital social o patrimonio de las Sociedades o Fondos de Inversión Inmobiliaria, un 11,11 por ciento" |
| Shares admitted to trading on an official secondary market, but NOT shares representing the capital of a Sociedad de Inversión Mobiliaria or Inmobiliaria, per year of holding beyond two | 25% | "con excepción de las acciones representativas del capital social de Sociedades de Inversión Mobiliaria e Inmobiliaria, un 25 por ciento" |
| All other gains accrued before 20 January 2006, per year of holding beyond two | 14.28% | "con anterioridad a 20 de enero de 2006, un 14,28 por ciento" |
| Lifetime ceiling on the CUMULATIVE transfer value, counting every asset abated since 1 January 2015 plus this one | EUR 400,000 | "Cuando sea inferior a 400.000 euros la suma del valor de transmisión del elemento patrimonial" |

How the ceiling bites, from letters c), d) and e) of the same rule: below it, the reduction is given in full; where this transfer takes the running total past it but the earlier total on its own is still below it, the reduction is given only on the slice of the transfer value that keeps the running total inside it; once the earlier total on its own is above it, no reduction at all. Guides routinely print the three coefficients and leave the ceiling out. Without the ceiling the answer is wrong for anyone who has sold more than one old asset since 1 January 2015. The ceiling counts TRANSFER VALUE, not gain. Shares and units in the investment vehicles the first two rows exclude are not left out of the rule: they fall into the third row, the residual 3.º of the same rule, which names no asset class and carves nothing out.

Where the running total is inside the ceiling, the part of the gain accrued before 20 January 2006 is not subject to tax at all if the holding period at 31 December 1996, counted as above, was more than ten years for immovable property, five years for listed shares and eight years for everything else. That sentence sits inside letter c), so it does not survive letter e).

## Capital losses

Losses are set off in a fixed order, and only a capped share can cross between the two parts of the savings base.

Within the savings base (art. 49.1 Ley 35/2006):

1. Investment income (rendimientos del capital mobiliario) is netted only against itself.
2. Gains and losses on transmissions are netted only against each other.
3. If one of those two balances is negative, it is set against the positive balance of the other, but only up to the capped share in the table below.
4. Anything still negative is carried to the four following years, in that same order, and must be used in the largest amount each of those years allows. It cannot be pushed past the four years by rolling it into a later year's losses.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Share of the other savings balance that a negative balance may be set against, in each direction (art. 49.1.a and 49.1.b) | 25% | "con el límite del 25 por ciento de dicho saldo positivo" |
| Share of the positive general income balance that a negative general gains balance may be set against (art. 48.b) | 25% | same wording in art. 48.b |

The carry forward period is four years, which the statute prints in words ("los cuatro años siguientes") and not as a digit. Gains and losses in the GENERAL base (art. 48.b) follow the same shape, with the same capped share and the same four years, but they are a separate pool: a general loss never reduces savings income and a savings loss never reduces general income.

The legacy split of "financial assets" against "other assets" is not the statutory rule. What the law separates is investment income from gains on transmissions, both inside the savings base. A loss on shares and a loss on a flat sit in the SAME pool.

### A loss you cannot take yet: the repurchase rules

Three separate windows in art. 33.5 Ley 35/2006 stop a loss being counted when the taxpayer buys the same thing back. The loss is not lost: it is brought in when the securities or the asset that stayed in the taxpayer's hands are later transferred.

- Assets other than securities (art. 33.5.e): the loss is not counted where the taxpayer acquires the asset again within the year following the transfer.
- Securities admitted to trading on an official secondary market (art. 33.5.f): the loss is not counted where the taxpayer acquired homogeneous securities within the two months before or the two months after the transfer.
- Securities not admitted to trading (art. 33.5.g): the loss is not counted where the taxpayer acquired homogeneous securities within the year before or the year after the transfer.

Other losses art. 33.5 refuses outright: unjustified losses, losses from consumption, losses on lifetime gifts and liberalities, and gambling losses beyond the gambling winnings of the same period.

## Non-residents

A non resident with no permanent establishment is taxed under Real Decreto Legislativo 5/2004, separately on each gain, not on a yearly aggregate, and files Modelo 210 rather than Modelo 100.

| Item | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527 |
| Capital gains on a disposal, whatever the seller's country of residence and subject to any treaty (art. 25.1.f.3.º) | 19% | "El 19 por ciento cuando se trate de: 1.º Dividendos y otros rendimientos derivados de la participación en los fondos propios de una entidad. 2.º Intereses y otros rendimientos obtenidos por la cesión a terceros de capitales propios. 3.º Ganancias patrimoniales que se pongan de manifiesto con ocasión de transmisiones de elementos patrimoniales" |
| Residents of another EU member state, or of an EEA state with effective exchange of tax information, on income other than the art. 25.1.f items (art. 25.1.a) | 19% | "el tipo de gravamen será el 19 por ciento cuando se trate de contribuyentes residentes en otro Estado miembro" |
| General rate on income obtained with no permanent establishment, other than the art. 25.1.f items (art. 25.1.a). The exception for residents of another member state is the row above | 24% | "Con carácter general el 24 por 100" |
| Withholding the buyer of Spanish property from a non resident must pay over (art. 25.2) | 3% | "el adquirente estará obligado a retener e ingresar el 3 por ciento" |

The legacy statement that other non residents pay 24 per cent on capital gains was wrong. The 24 per cent rate in art. 25.1.a is the general rate on Spain source income. Gains on a disposal fall in art. 25.1.f and bear 19 per cent whatever the seller's country, subject to any treaty.

Selling Spanish property as a non resident, on the Agencia Tributaria's own page:

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/cuestiones-especificas-sobre-tributacion-inmuebles/ganancia-patrimonial-derivada-transmision.html |
| Rate on the gain | 19% | "El tipo de gravamen aplicable es el 19%" |
| The buyer, resident or not, must withhold and pay to the Treasury this share of the agreed consideration, on Modelo 211, within one month of the date of transfer, and give the non resident seller a copy so it can be credited | 3% | "el 3% de la contraprestación acordada" |
| Partial exemption for urban property situated in Spain that was acquired from 12 May 2012 to 31 December 2012 (disposición adicional cuarta Ley IRNR), with exclusions set out on the page | 50% | "Están exentas en un 50% las ganancias patrimoniales derivadas de la venta de inmuebles urbanos" |

The gain itself is worked out on IRPF rules: transfer value less acquisition value, the acquisition value including improvements and the costs and taxes inherent to the acquisition paid by the seller, and reduced by the depreciation allowed, with the minimum depreciation always counted for a property that was let.

The transitional regime for assets bought before 31 December 1994 reaches a non resident individual as well, through disposición transitoria única Ley IRNR. The coefficients, the cumulative transfer value ceiling and the order of the steps are the same as in the abatement section above, and the Agencia Tributaria works the calculation on the page linked in this section.

Deadlines for the non resident, from the Agencia Tributaria: Modelo 210 for income from transfers of immovable property is filed in the three months that begin once one month has passed from the date of the transfer. See https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/declaracion-irnr-sin-establecimiento-permanente/modelo-plazo-declaracion.html

Reinvestment relief on a main home is not shut to non residents. Disposición adicional séptima Ley IRNR extends it to residents of an EU member state, and of Iceland, Norway and, since 11 July 2021, Liechtenstein, on the same condition that the whole amount obtained is reinvested in a new main home, with a proportional exclusion where less is reinvested.

## Ceuta and Melilla

Ceuta and Melilla do not get a different rate on a gain. They get a credit against the tax already worked out.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Credit against the share of the combined state and autonomous gross tax that the Ceuta or Melilla income represents (art. 68.4 Ley 35/2006) | 60% | "se deducirán el 60 por ciento de la parte de la suma de las cuotas íntegras" |

Gains from immovable property situated in Ceuta or Melilla, and from movable property situated there, count as income obtained in those cities (art. 68.4.3.º letters d and e). Someone habitually and effectively resident in Ceuta or Melilla claims the credit on income obtained there. Someone who is not resident there claims it only on income obtained there, and only where the taxable bases are positive. Art. 68.4.2.º shuts income out of the credit for a taxpayer who is not resident in the cities: income from collective investment undertakings unless every asset is invested in Ceuta or Melilla, and the income in letters a), e) and i) of art. 68.4.3.º, which are employment income, gains on movable property situated there, and income from deposits and accounts with financial institutions there. So someone who does not live in the cities keeps the credit on a gain on immovable property situated there under letter d), but loses it on a gain on movable property situated there under letter e).

## The method, step by step

1. Settle residence and territory first. A Spanish resident is taxed on worldwide gains through Modelo 100; a non resident with no permanent establishment is taxed gain by gain through Modelo 210 under Real Decreto Legislativo 5/2004 (https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527). Common territory, the Basque provinces and Navarre are different tax systems, and this Guide is common territory only.
2. Decide whether there is an alteration at all. Art. 33.2 and 33.3 Ley 35/2006 treat some events as producing no gain or loss: dividing a common asset, dissolving the matrimonial property regime, separating co-owners, and transfers on the death of the taxpayer (https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764).
3. Put the item in the right base. A gain or loss on a TRANSMISSION is savings income (art. 46.b Ley 35/2006). A gain that is not on a transmission is general income (art. 45) and bears the general scale, which has an autonomous half this Guide does not carry (https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764).
4. Compute the gain. Use art. 35 for a sale, art. 36 for a gift or an inheritance, and art. 37 for listed securities, unlisted securities, collective investment funds and the other special cases. Where homogeneous securities exist, art. 37.2 treats the ones sold as the ones acquired first (https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764).
5. Apply any exemption before anything else: art. 33.4.b for the over 65 main home, art. 38.1 for reinvestment in a new main home, art. 38.2 for shares that carried the new company deduction, art. 38.3 for the over 65 life annuity. Check each one's own condition and its own ceiling in the sections above (https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764).
6. Apply the abatement coefficients only if the asset was acquired before 31 December 1994 and is not used in a business, and only after checking the cumulative ceiling in the table above (disposición transitoria novena, https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764).
7. Integrate and compensate. Net inside each pool, then cross between the two savings pools up to the capped share in the losses table, then carry any remainder to the four following years (art. 49, https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764).
8. Charge the savings scale in the table above (art. 66 Ley 35/2006), then apply the Ceuta and Melilla credit if it is in point (art. 68.4, https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764). Read the exclusions in art. 68.4.2 first: a taxpayer who does not live in the cities loses the credit on some of the income listed there, including a gain on movable property situated there.
9. File. A resident files Modelo 100 in the Renta campaign. The window for the 2025 return runs from 8 April to 30 June 2026, with bank direct debit to 25 June 2026; the Agencia Tributaria has not yet published the window for the 2026 return, which falls in 2027 (https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c01-campana-declaracion-renta/confirmacion-borrador-presentacion-declaraciones/plazo-forma-presentacion.html). A non resident selling property files Modelo 210 in the three months that begin one month after the transfer, and the buyer files Modelo 211 within one month of it (https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/declaracion-irnr-sin-establecimiento-permanente/modelo-plazo-declaracion.html).

## Ask the client first

- Were you a Spanish tax resident for the whole year, and in which autonomous community, or in Ceuta or Melilla? Residence decides Modelo 100 against Modelo 210, and Ceuta or Melilla brings in the credit, subject to the art. 68.4.2 exclusions for someone who does not live there.
- When did you acquire the asset? Anything acquired before 31 December 1994 opens the abatement coefficients, and the next question is which other old assets you have already sold since 1 January 2015, because the ceiling counts them all.
- Is the property your main home, and was it your residence for at least three years? Ask separately whether you held the full ownership, not a usufruct or the bare ownership on its own, and whether you were over 65 at the date of the transfer.
- If you are reinvesting in a new home, is the entire amount obtained going in, and was there a mortgage still outstanding on the old home? The outstanding principal comes off the amount you must reinvest.
- Have you bought the same shares, or homogeneous ones, in the two months either side of the sale, or the same asset within the following year? If so the loss is deferred, not denied.
- Do you have unused losses from the four previous years, and from which pool did they come?

## When to refuse or refer

- The Basque provinces (Álava, Bizkaia, Gipuzkoa) and Navarre. They run their own income tax and no page on an allowed host carries their capital gains rules.
- Autonomous community deductions and any question about a community's own reliefs on a gain. Route to `es-irpf-deductions`.
- Gains inside a business or a profession, which follow the business income rules rather than these, and the transfer of a whole business or of shares under art. 20.6 of the inheritance and gift tax law.
- Crypto assets. The savings base treatment is the same shape, but the valuation, the exchange rules and Modelo 721 are not in this Guide. Route to `spain-crypto-tax`.
- Anyone inside the inbound worker regime of art. 93 Ley 35/2006. They stay an IRPF contributor but are taxed under the non resident rules. Route to `es-beckham`.
- Rental income, imputed property income and the deductions a landlord may take. Route to `es-rental-income`. The general scale, the personal and family minimums and the filing thresholds are in `es-income-tax`.
- Any case where a double tax treaty may cut the Spanish charge. The treaty, not this Guide, decides.
- Working out a non resident's whole Spanish position, the 183 day residence test, or a Modelo 210 that is not about a gain. Route to `es-non-resident-income-tax-irnr-and`.
- Inheritance and gift tax, the municipal plusvalía on urban land, and wealth tax. All three can fall due on the same disposal and none of them is covered here.

## Sources

- Ley 35/2006, IRPF, consolidated text: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
- Real Decreto 439/2007, Reglamento IRPF, consolidated text: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- Real Decreto Legislativo 5/2004, IRNR, consolidated text: https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527
- Agencia Tributaria, exempt capital gains, Manual práctico de Renta 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c11-ganancias-perdidas-patrimoniales/ganancias-perdidas-patrimoniales-que-no-bi/ganancias-patrimoniales-exentas.html
- Agencia Tributaria, capital gain on transferring property as a non resident: https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/cuestiones-especificas-sobre-tributacion-inmuebles/ganancia-patrimonial-derivada-transmision.html
- Agencia Tributaria, Modelo 210 form and filing periods: https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/declaracion-irnr-sin-establecimiento-permanente/modelo-plazo-declaracion.html
- Agencia Tributaria, filing period for the Renta return: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c01-campana-declaracion-renta/confirmacion-borrador-presentacion-declaraciones/plazo-forma-presentacion.html

> Working paper only. Have a qualified Spanish tax adviser review before filing.

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
