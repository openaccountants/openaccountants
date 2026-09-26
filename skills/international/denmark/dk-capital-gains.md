---
name: dk-capital-gains
description: "Denmark capital gains tax: 27%/42% on share gains, progression threshold, inventory taxation for certain shares, real property gains. Trigger on: \"Denmark CGT\", \"capital gains Denmark\", \"Denmark aktieindkomst\", \"sell shares Denmark\", \"Denmark 27% 42% capital gains\", \"Denmark aktieavance\", \"Danish share gains tax\"."
version: 1.0
jurisdiction: DK
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark capital gains — individual investors and home sales, 2026

Tax year: 2026.

## Scope and outcome

Use this method for a Danish-resident individual’s ordinary shares held outside special savings or pension arrangements, and ordinary owner-occupied or privately held property. Produce an asset-by-asset calculation, loss schedule and filing instructions. Identify the income category before applying a rate: share income and capital income are different categories. Do not use the share rate on a property gain.

## Ask the client first

- Obtain tax residence and arrival/departure dates, marital/cohabitation status at year end, asset identity and legal type, trading-market status throughout ownership, account wrapper, all acquisition/disposal dates, costs and corporate actions. Obtain holdings across every broker, dividend and foreign-tax statements, prior losses and proof of acquisition reporting. For property obtain the deed, binding contract, ownership share, actual occupancy, parcel area, use/classification, subdivision decisions, acquisition/sale costs and improvements by year. Missing cost, classification or residence evidence means a provisional result with the missing inputs named, not an invented basis.

## Current figures

| Rule | 2026 amount | Authority |
|---|---|---|
| Individual share-income lower band | DKK 79,400 at 27% | [SKAT share rates](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier) |
| Share income above that band | 42% | [SKAT share rates](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier) |
| Married spouses living together at the end of the income year: combined lower band | DKK 158,800 | [SKAT share rates](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier) |
| Ordinary home land-area screen | Below 1,400 square metres; 1,400 square metres or more needs an exception | [SKAT property conditions](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig) |
| Property basis annual addition | DKK 10,000 per eligible ownership year | [SKAT adjusted basis](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig) |

## The method, step by step

1. Route the asset and confirm the applicable tax year before calculation.
2. Reconcile all holdings, transaction evidence and cost pools; calculate each disposal or annual taxable movement using its own regime.
3. Apply the correct loss restrictions, combine relevant income and compute a provisional tax result where this Guide supplies the applicable rates.
4. Reconcile the return with SKAT’s records, enter missing figures in the correct fields and retain the approved calculation and submission receipt.

## Classify shares and funds

For this Guide, “admitted to trading” includes regulated markets and multilateral trading facilities. The multilateral-trading-facility part applies from 1 January 2024; before that date, shares traded only on a multilateral trading facility were not treated as admitted, so check the rule for the year in which a historic gain or loss arose. Check the instrument’s actual status, rather than the broker’s informal “listed” label. A holding not admitted now may still have been admitted earlier during ownership, affecting loss treatment. [Trading status](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/aktier-optaget-til-handel)

Ordinary share disposals use realization treatment. Funds need a separate classification: an investment company uses annual mark-to-market treatment, including unrealized movements; an investment institution with minimum taxation, and an accumulating investment association that is not an investment company, are taxed on disposal (average method), with share-based units in field 66 as share income. Establish share-based versus bond-based status and the income-year classification from the issuer/custodian. Investment-company gains can be share income or capital income; distributing versus accumulating alone is insufficient. An investment company is share-based only if it has notified SKAT and appears on SKAT’s published list of share-based investment companies for that year; if it is not share-based it is treated as bond-based, so its annual gain or loss is capital income (field 38 Danish, 422 foreign), not share income. Check the list for the actual year before choosing field 345 or 375. [Share-based investment companies](https://info.skat.dk/data.aspx?oid=2292808); [SKAT list page](https://skat.dk/erhverv/ekapital/vaerdipapirer/beviser-og-aktier-i-investeringsforeninger-og-selskaber-ifpa). Use SKAT’s fund-specific fields and guidance rather than the ordinary-share table below. With an unclassified ETF, stop the calculation and obtain its Danish classification. [Fund rules](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber)

For a straightforward investment-company holding unchanged throughout the year, the unrealized movement is closing value minus opening value. For units purchased during the relevant year substitute acquisition price for opening value; for units sold substitute disposal proceeds for closing value. Calculate held and disposed quantities separately and sum their movements, avoiding duplicate proceeds or costs. Listed/centrally registered shares and fund units use the taxpayer’s income year; an investment-company share neither admitted on a regulated market nor centrally registered uses the investment company’s income year. Status changes need separate review. Hypothetical unchanged holding: opening DKK 100,000, closing DKK 110,000, no distributions or trades; annual gain DKK 10,000 even without a sale. The verified fund classification determines the income category. [Annual valuation](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber)

For a hypothetical ordinary investment-company lot bought during the year for DKK 40,000 and sold during that year for net DKK 50,000, with no distributions or other movements, the annual taxable gain is DKK 10,000. A purchase retained at year-end uses closing value instead of sale proceeds. [Fund method](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber)

| Core fund gain/loss route | Danish field | Foreign field | Source |
|---|---|---|---|
| Share-based minimum-tax institution: disposal gain/loss, share income | 66 | 454 | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber) |
| Bond-based minimum-tax institution: disposal gain/loss, capital income | 30 | 434 | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber) |
| Accumulating investment association that is not an investment company: disposal gain/loss, share income | 66 | Not listed separately; confirm with SKAT | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber) |
| Share-based investment company: annual gain/loss, share income | 345 | 375 | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber) |
| Bond-based investment company: annual gain/loss, capital income | 38 | 422 | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber) |

For bond-based minimum-tax units, combine the relevant annual net gain/loss with qualifying debt-claim and foreign-currency debt gains/losses. The per-spouse aggregate must exceed DKK 2,000 in magnitude: exactly DKK 2,000 is outside taxation/deduction; DKK 2,001 is included in full. This is a threshold, not a deduction from the included gain. Do not apply it to every fund category. Preserve purchase-notification evidence for loss relief. [Fund threshold](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber)

## Calculate ordinary share gains

Pool the acquisition cost of taxable shares in the same company across Danish and foreign custody accounts. Use the average cost attributable to shares sold, taking account of splits and other corporate actions. Remove qualifying tax-exempt legacy holdings from the taxable pool; mixed pre-reform holdings need the transitional rules and disposal-order analysis before this calculation. Reconcile fees to the transaction documentation and acquisition-cost record. [Average method](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier/gevinst-og-tab-opgoeres-efter-gennemsnitsmetoden)

Hypothetical simple pool, all costs already included: buy 100 shares for DKK 20,000 and another 100 for DKK 40,000. The pool is DKK 60,000 for 200 shares; average cost DKK 300 each. Sell 50 for net DKK 20,000: allocated basis DKK 15,000; gain DKK 5,000. Remaining basis DKK 45,000 for 150 shares. Do not use a broker’s first-purchase cost as the gain calculation merely because those shares are deemed disposed of first. [Average method](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier/gevinst-og-tab-opgoeres-efter-gennemsnitsmetoden)

Combine taxable dividends and realized gains after relevant loss adjustments. For a single taxpayer with hypothetical positive net share income DKK 100,000 and no credits, the lower-band charge is DKK 21,438 and excess-band charge DKK 8,652, total DKK 30,090. Exactly at DKK 79,400, the charge is DKK 21,438. The doubled DKK 158,800 band applies only to spouses who are married and living together at the end of the income year; unmarried cohabiting partners, and spouses separated at year end, each use their own DKK 79,400 band. For qualifying spouses with combined positive income DKK 100,000 and no other share income/losses, the combined charge is DKK 27,000. Hypothetical unmarried cohabitants where one partner has DKK 100,000 share income and the other has none: the DKK 100,000 is taxed alone at DKK 30,090, not DKK 27,000. These are arithmetic illustrations before withholding/credits, not balances payable. [Rates](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier)

## Apply share losses correctly

Admitted-to-trading losses are ring-fenced: SKAT offsets them only against share dividends, gains on other admitted shares and mark-to-market gains on share-based investment companies. Do not set them against gains on shares not admitted to trading. Excess passes to the corresponding income of a spouse the taxpayer is married to and living with, after that spouse’s own losses, then forward to later years (the taxpayer’s first, then the spouse’s). The same ring-fence applies to losses on share-based minimum-tax institution units and on accumulating investment associations that are not investment companies. By contrast, a loss on a share-based investment company whose units are admitted to trading is deducted in share income without that restriction. Never deduct this loss directly from salary. Report the loss by the taxpayer’s information deadline to preserve carryforward. Unlisted-share losses instead reduce other share income; negative share income produces a tax value against other taxes, subject to spouse ordering and carryforward of unused tax value. Shares formerly admitted during ownership retain the admitted-share loss rules. [Loss categories](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier)

Before allowing an admitted-share loss, verify acquisition notification. For current ordinary purchases the taxpayer must notify SKAT by 1 July following the purchase year, with weekend extension to the next working day under SKAT’s published deadline. Supply identity/ISIN, quantity, purchase date, cost including transaction charges and price through TastSelv Contact → Write to us → Income and deductions → Annual assessment → Questions and changes → Shares and securities. Keep proof. A reporting-obliged institution can correct its reporting later; do not confuse that exception with permission for a taxpayer to report an unreported foreign purchase late. Other deadlines: shares received as a gift, 1 July the year after the transfer; shares distributed from an estate, 1 July the year after distribution (later if the estate statement is filed after 1 July); shares acquired before becoming liable to Danish tax, before 1 July of the year after the year in which liability starts. A foreign broker can agree to report for the taxpayer by 20 January the year after purchase. Older purchases (before 1 July 2012) follow SKAT’s transitional table. There is no dispensation for a missed deadline. [Acquisition reporting and exceptions](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier/betingelser-for-fradrag-for-tab-paa-aktier-og-investeringsbeviser)

Hypothetical unlisted-loss example: never-admitted shares produce a DKK 50,000 loss; the taxpayer has DKK 10,000 other positive share income, leaving negative DKK 40,000. A spouse the taxpayer is married to and living with at year end has DKK 20,000 positive share income: offset that first, leaving negative DKK 20,000. The negative balance is within the lower share-income band, so its tax value is DKK 5,400 at 27%. Apply against the taxpayer’s other taxes first; assuming DKK 3,000 available there, DKK 2,400 remains for the spouse’s other taxes. With DKK 1,000 available there, unused tax value DKK 1,400 carries forward to the taxpayer’s and then the spouse’s taxes in later years. Record tax-value carryforward separately from a restricted listed-share loss balance. Larger negative balances use the applicable share-income bands; reconcile the assessment’s calculation and spouse allocation. [Unlisted losses and tax-value ordering](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier)

## File ordinary shares

In TastSelv, inspect Skatteoplysninger → Aktieoplysninger and the Securities System; repair missing transaction data and reconcile the resulting assessment. Use the field for the actual combination of issuer country, market status and custody. The following are gain/loss fields, not dividend fields. [SKAT filing instructions](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier)

| Ordinary share route | Annual assessment field | Source |
|---|---|---|
| Admitted shares in Danish custody; Danish admitted shares in foreign custody | 66 | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier) |
| Foreign admitted shares in foreign custody | 454 | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier) |
| Danish shares not admitted | 67 | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier) |
| Foreign shares not admitted | 451 | [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier) |

Unlisted shares need the taxpayer’s own calculation. Foreign custody also requires the year-end portfolio value in Danish kroner. Reconcile gross dividends and foreign tax separately; foreign tax credit cannot automatically equal everything the broker withheld. Check SKAT’s country/treaty-specific dividend instructions before entering relief. [SKAT](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier)

## Decide whether a home sale is exempt

SKAT treats the sale of a home as normally exempt only when all three conditions hold: (1) the property is a one-family or two-family house, an owner-occupied condominium or a house on leased land; (2) the owner or the owner’s spouse/partner lived there as their genuine home at some point during ownership (a temporary stay does not count, and they need not live there at the sale date); and (3) the total land area is under 1,400 square metres. With 1,400 square metres or more the sale is exempt only if the land cannot be subdivided for separate building, backed by a declaration from the municipality, or subdivision would reduce the value of the remaining land or the existing building by more than 20% (a Vurderingsstyrelsen declaration, obtainable only after the municipality confirms subdivision is possible). Losses on a sale that meets the exemption are not deductible. Danish conditions also govern a foreign home; foreign exemption alone is insufficient. [Home conditions](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig); [foreign-home conditions](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-bolig-i-udlandet)

SKAT treats the gain as taxable where the home was bought solely to resell at a profit (speculation), the owner or household never lived there (for example a pure rental property), or it is purely business property. A property with more than two independent dwellings (each with its own kitchen and toilet as actually fitted out) cannot be sold exempt as a whole, even if the owner lived in one of them. When a two-family house is split into two condominiums, only the unit the owner or household lived in after the split can be sold exempt. Where a property has several land-register parcels that may be sold separately (not jointly registered), only the parcel carrying the home can qualify; a vacant building plot cannot be sold exempt. A small farm with an agricultural obligation can still qualify if it is valued as a one-family house (01/residential) and the other conditions are met. [Property categories](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig)

Home combined with a business (for example a dental clinic or hair salon in the same building): for a sale agreed on or after 1 July 2025 it can normally be exempt if the property is correctly valued as an owner-occupied home property at the sale date and the residence and area conditions are met. For a sale before 1 July 2025 the older test applies: it must look like a one-family house, the home’s value must be at least 50% of the total property value, and at least 50% of the area must be used as the home. Inherited/gifted property, trading or depreciation history need their own computation before asserting exemption. [Mixed use](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig)

Holiday homes and cooperative flats sit outside the ordinary home rule but have their own exemption. A holiday home is exempt if the owner used it privately and the plot is under 1,400 square metres (larger plots need the same subdivision exception); if it was only let out commercially, the gain is taxable. A cooperative-flat share (andelsbolig) is taxed under the share-gains act as share income in field 67, but the gain is exempt if the owner lived there and the land belonging to the flat is under 1,400 square metres. [Holiday home](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-sommerhus); [cooperative flat](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-andelsbolig)

## Compute a taxable ordinary property disposal

Use the binding agreement year. Adjust cash-equivalent sale proceeds for permitted sale expenses. Adjust purchase price for acquisition expenses, the annual addition for ownership years excluding the sale year (same-year purchase/sale gets one addition), and documented eligible maintenance/improvements exceeding DKK 10,000 in each year. Avoid adding previously deducted expenditure; obtain specialist adjustment where business use or depreciation occurred. Taxable gain is capital income, not a universal flat tax. [SKAT computation](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig)

Hypothetical ordinary property bought at the start of the previous year, sold this year, no deductible-business expenditure: proceeds DKK 2,000,000 less sale costs DKK 100,000 give DKK 1,900,000. Purchase DKK 1,500,000 plus buying costs DKK 50,000, one annual addition DKK 10,000 and eligible sale-year improvements DKK 30,000 less annual threshold DKK 10,000 give adjusted basis DKK 1,580,000. Gain DKK 320,000. This is taxable income, not the tax bill. [Basis method](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig)

Domestic taxable gain goes to annual field 39; a qualifying property loss goes to field 84 and can offset other taxable property gains, including later years, rather than salary/share income. Foreign property gain uses field 425 and eligible foreign capital-income tax field 495K; foreign property loss also uses field 84. Update the property sale and preliminary assessment so ongoing property taxes and borrowing deductions are correct. [Domestic filing](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig); [foreign filing](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-bolig-i-udlandet)

## Corrections, evidence and delivery

Select the affected year in TastSelv and correct the transaction or return entry, preserving old and new workings and the reason. For prior years use SKAT’s published reopening deadlines: the 2025 return can be corrected until 1 May 2029 and the 2024 return until 1 May 2028. After that, correction needs special circumstances outside the taxpayer’s and adviser’s control (a forgotten deduction or misunderstood rule does not qualify), requested within 6 months of learning of them; if an online field cannot be edited, contact SKAT with the calculation. Ordinary reopening does not cure a missed acquisition-reporting condition for loss relief. The ordinary information deadline for an individual’s annual return is 1 May of the following year; confirm the deadline shown for the actual taxpayer in TastSelv, and do not reuse a prior year’s exceptional deadline. [Information deadline](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-paa-krypto-kend-reglerne-saa-du-undgaar-et-skattesmaek/beregn-og-oplys-gevinst-og-tab-paa-krypto); [Corrections](https://skat.dk/borger/aarsopgoerelse/se-og-ret-dine-gamle-aarsopgoerelser); [loss notification](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier/betingelser-for-fradrag-for-tab-paa-aktier-og-investeringsbeviser)

Deliver the classification decision, ownership/cost reconciliation, realized or annual movement calculation, loss utilisation/carryforward, fields, withheld-tax reconciliation and filing receipt. Label unconfirmed evidence and unresolved credit questions. Retain source retrieval dates with the workpaper.

## Share savings account and crypto: route, do not compute here

Share savings account (aktiesparekonto): only a person fully liable to Danish tax can open one, each person may own only one, and it cannot be held jointly, even with a spouse. The return is taxed at 17% on the mark-to-market basis at year end, calculated and paid by the bank, and it does not go on the annual return or into share income. The 2026 deposit ceiling is DKK 174,200 of net deposits, measured against the account’s market value on 31 December 2025, and it is personal: a spouse cannot use the other spouse’s unused room. Over-deposits must be withdrawn as soon as the error is found, and a 3% charge applies each year to the excess. A loss gives a negative tax that carries forward only against later tax on the same account and is lost if the account is closed. Only shares admitted to a regulated market or multilateral trading facility, units in minimum-tax institutions with at least 50% in shares, and share-based investment companies on SKAT’s list (if their shares are admitted to trading or their units are negotiable) may be held; an ineligible asset is treated as never having been in the account and goes on the ordinary return. A foreign “savings account” wrapper is an ordinary custody account under Danish rules. [Aktiesparekonto](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/aktiesparekonto)

Crypto held privately is normally treated as bought for speculation. Gains are personal income (not share income), which SKAT says can mean tax of up to 53%; losses give a deduction worth 26%. Use FIFO across all wallets and exchanges as one holding, and report total gains in field 20 and total losses in field 58 separately; a loss on one trade generally cannot be netted against a gain on another. Paying for one crypto-asset with another is a disposal. SKAT says its pages describe practice under current rules and that the Tax Law Council’s October 2024 recommendations for new legislation have not been dealt with by Parliament, so check for a change before filing. [Crypto](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-paa-krypto-kend-reglerne-saa-du-undgaar-et-skattesmaek/beregn-og-oplys-gevinst-og-tab-paa-krypto); [crypto practice note](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-paa-krypto-kend-reglerne-saa-du-undgaar-et-skattesmaek)

## When to refuse or refer

- Refer corporate investors, pension wrappers, share savings account disputes, derivatives, crypto staking/mining/stablecoins/NFTs or a crypto question beyond the routing above, bonds/currency debt, employee-option charging, departure/arrival and exit tax, tax-exempt legacy holdings, reorganisations, gifts/inheritance, non-arm’s-length valuations, uncertain fund status, business property/depreciation and treaty-credit disputes. These need their own governing method. Do not silently broaden this ordinary individual-investor method to cover them.

## Sources

Official SKAT guidance retrieved 24–25 September 2026. Recheck rates, fund classification and filing fields for the actual income year.
- [shares](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier)
- [average](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier/gevinst-og-tab-opgoeres-efter-gennemsnitsmetoden)
- [loss](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier/betingelser-for-fradrag-for-tab-paa-aktier-og-investeringsbeviser)
- [market](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/aktier-optaget-til-handel)
- [fund](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber)
- [home](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig)
- [foreign](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-bolig-i-udlandet)
- [correction](https://skat.dk/borger/aarsopgoerelse/se-og-ret-dine-gamle-aarsopgoerelser)
- [share-based investment companies](https://info.skat.dk/data.aspx?oid=2292808)
- [share-based list](https://skat.dk/erhverv/ekapital/vaerdipapirer/beviser-og-aktier-i-investeringsforeninger-og-selskaber-ifpa)
- [holiday home](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-sommerhus)
- [cooperative flat](https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-andelsbolig)
- [share savings account](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/aktiesparekonto)
- [crypto](https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-paa-krypto-kend-reglerne-saa-du-undgaar-et-skattesmaek/beregn-og-oplys-gevinst-og-tab-paa-krypto)

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
