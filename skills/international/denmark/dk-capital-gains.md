---
name: dk-capital-gains
description: "Danish capital gains for individuals, income year 2026. Covers share gains and dividends as share income (27% up to DKK 79,400, 42% above; DKK 158,800 for married couples living together), the average-cost method, listed and unlisted share losses and the 1 July purchase-reporting condition, investment funds and ETFs (mark-to-market lagerbeskatning for investment companies, realisation for minimum-tax funds), the aktiesparekonto at 17% with the DKK 174,200 deposit ceiling, bonds and currency gains with the DKK 2,000 threshold, property gains and the parcelhusreglen (1,400 m2), property losses, holiday homes, cooperative flats, crypto routing, exit tax on shares and return fields. Trigger on: Denmark capital gains, aktieindkomst, aktieavance, sell shares Denmark, ETF Denmark lager, aktiesparekonto, parcelhusreglen, sell house Denmark tax, Danish crypto tax. Out of scope: companies (dk-corporate-tax), self-employed business income (dk-income-tax), moving in or out of Denmark in depth (dk-cross-border)."
version: 1.1
jurisdiction: DK
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark capital gains: individual investors and home sales, 2026

Tax year: 2026 (calendar income year).

## Who this applies to

This skill is for an individual fully liable to Danish tax who sells or holds shares, funds, ETFs, bonds, crypto or property privately, outside a pension scheme. It works out the gain or loss for each asset, puts it in the right income category, applies the loss rules and names the return field.

Danish gains do not share one rate. Sort each item first:

- **Share income (aktieindkomst):** gains and dividends on shares, share-based funds and share-based investment companies. Taxed at 27% and 42% (Personskatteloven § 8 a).
- **Capital income (kapitalindkomst):** taxable property gains, bond and currency gains, bond-based funds and bond-based investment companies. Taxed with the taxpayer's other income under the ordinary rates in dk-income-tax.
- **Personal income:** private crypto gains (SKAT practice).
- **Separate 17% tax:** returns inside an aktiesparekonto, outside both share income and the annual return.

Out of scope: companies (dk-corporate-tax), business assets and depreciated property, trading as a business, employee shares and options, derivatives, pension wrappers, gifts and inheritance, reorganisations, and the detailed rules for arrival and departure (dk-cross-border). Refer these.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Share income up to the band | 27% on the first DKK 79,400 | 2026 | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier |
| Share income above the band | 42% | 2026 | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier |
| Band for spouses married and living together at year end | DKK 158,800 combined | 2026 | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier |
| Statutory base of the band (indexed each year) | DKK 48,300 at 2010 level | 2026 | https://www.retsinformation.dk/eli/lta/2021/1284 (PSL § 8 a) |
| Aktiesparekonto tax on the return | 17% | 2026 | https://www.retsinformation.dk/eli/lta/2025/281 (§ 14) |
| Aktiesparekonto deposit ceiling (net deposits) | DKK 174,200 | 2026 | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/aktiesparekonto |
| Charge on deposits over the ceiling | 3% a year | 2026 | https://www.retsinformation.dk/eli/lta/2025/281 |
| Bond, debt and currency gains: threshold for individuals | Taxed only if the net yearly total exceeds DKK 2,000 | 2026 | https://www.retsinformation.dk/eli/lta/2025/1176 (KGL §§ 14, 23) |
| Home exemption land-area test | Under 1,400 m2 | 2026 | https://www.retsinformation.dk/eli/lta/2019/132 (EBL § 8) |
| Property cost: annual addition | DKK 10,000 a year owned (not the sale year, unless bought and sold in the same year) | 2026 | https://www.retsinformation.dk/eli/lta/2019/132 (EBL § 5) |
| Property improvements added to cost | Amount above DKK 10,000 per calendar year | 2026 | https://www.retsinformation.dk/eli/lta/2019/132 (EBL § 5, stk. 2) |
| Exit tax on shares: holding threshold | Share holding worth DKK 100,000 or more | 2026 | https://www.retsinformation.dk/eli/lta/2026/849 (ABL § 38) |
| Private crypto | Personal income, up to 53% on gains; loss deduction worth 26% | 2026 | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-paa-krypto-kend-reglerne-saa-du-undgaar-et-skattesmaek/beregn-og-oplys-gevinst-og-tab-paa-krypto |

The 2025 band was DKK 67,500 (DKK 135,000 for couples). The 2025 aktiesparekonto ceiling was DKK 166,200.

## The taxable base

### Shares

Ordinary shares are taxed when sold (realisation principle, Aktieavancebeskatningsloven § 23). Gain is sale proceeds less the average cost of the shares sold (§ 26). Pool every share in the same company across all Danish and foreign accounts. Adjust for splits and other corporate actions. Do not use a broker's first-in cost. Remove tax-exempt legacy holdings from the pool before calculating; mixed pre-reform holdings need the transitional rules.

"Admitted to trading" means a regulated market or a multilateral trading facility. The trading-facility part applies from 1 January 2024. Check the share's actual status for each year of ownership, not the broker's label. A share that was admitted at any time while owned keeps the admitted-share loss rules.

Dividends and gains are added together as share income. For couples married and living together at year end the band doubles. Unmarried partners and spouses living apart each use their own DKK 79,400.

### Share losses

- **Admitted (listed) shares** (ABL § 13 A): a loss reduces only dividends and gains on admitted shares and gains on share-based investment companies. Any excess goes to a spouse married to and living with the taxpayer, after the spouse's own losses, and then forward to later years. Never against salary.
- **Purchase reporting condition:** a listed-share loss is deductible only if SKAT had the purchase details by 1 July of the year after the purchase (next working day at 09:00 if 1 July is a weekend). Danish banks report this. Foreign brokers usually do not, so the taxpayer reports via TastSelv (ISIN, quantity, date, cost with charges). A foreign broker can agree to report by 20 January after the purchase year. Other deadlines: gifts, 1 July after the transfer; shares from an estate, 1 July after distribution; shares held on becoming Danish taxable, before 1 July of the year after liability starts. Purchases before 1 July 2012 follow SKAT's transitional table. There is no dispensation for a missed deadline, and reopening a year does not cure it.
- **Unlisted shares:** the loss reduces other share income. Negative share income gives a tax value (27% or 42% of the negative amount) set against the taxpayer's other taxes, then the spouse's, then carried forward. Keep this tax-value balance separate from a restricted listed-share loss balance.
- The same ring-fence as listed shares applies to share-based minimum-tax fund units and accumulating funds that are not investment companies. A loss on a share-based investment company admitted to trading is deducted in share income without that restriction.

### Funds and ETFs (lagerbeskatning)

Get the fund's Danish classification for the year before calculating:

- **Investment company (investeringsselskab, ABL § 19):** taxed every year on the change in value, sold or not (lagerprincippet). Gain = closing value less opening value; use cost for units bought in the year and proceeds for units sold in the year. It is share income only if the company is on SKAT's list of share-based investment companies for that year. If not on the list, treat it as bond-based: capital income. Most foreign ETFs fall here; never assume.
- **Minimum-tax investment institution (udloddende):** taxed on sale with the average method. Share-based: share income. Bond-based: capital income, inside the DKK 2,000 test below.
- **Accumulating Danish association that is not an investment company:** taxed on sale, share income.

Listed or centrally registered units use the taxpayer's income year. An unlisted, unregistered investment-company share uses the company's income year.

### Aktiesparekonto

Only a person fully liable to Danish tax may open one. One account per person, never joint. The bank computes the yearly change in value (mark-to-market) and pays 17% tax (Aktiesparekontoloven § 14). The return is left out of share income and the annual return (§ 22). For 2026 a person can deposit up to DKK 174,200 less the account's market value on 31 December 2025; the ceiling is on net deposits, so a withdrawal can be re-deposited within the year. A spouse cannot use the other's unused room. Over-deposits must be withdrawn when found, and 3% a year is charged on the excess. A loss becomes a negative tax carried forward only on the same account and is lost if the account closes. Allowed assets: shares admitted to a regulated market or trading facility, minimum-tax fund units with at least 50% in shares, and listed share-based investment companies. An ineligible asset is treated as never in the account. A foreign "savings account" is an ordinary account under Danish rules.

### Bonds, debt and currency (Kursgevinstloven)

Gains and losses on bonds and other debt claims (KGL § 14) and on foreign-currency debt (§ 23) are capital income. For an individual they count only if the year's net total, together with bond-based minimum-tax fund units, exceeds DKK 2,000 in magnitude. Exactly DKK 2,000 is out; above it the whole amount counts. This is a threshold, not an allowance. Bond-based investment companies sit outside this test and are taxed in full on the mark-to-market basis.

### Crypto

SKAT treats privately held crypto as bought for speculation. Gains are personal income; losses give a deduction worth 26%. Use FIFO across all wallets and exchanges as one holding. Swapping one crypto-asset for another is a disposal. Report total gains in field 20 and total losses in field 58 separately. The Tax Law Council's October 2024 proposals for a new regime have not been enacted; check before filing. Staking, mining, stablecoins and NFTs: refer.

### Property (Ejendomsavancebeskatningsloven)

**Parcelhusreglen (EBL § 8).** A gain on a one- or two-family house or an owner-occupied flat is exempt if the owner or household lived there as a real home at some point while owning it, and the total land is under 1,400 m2. With 1,400 m2 or more it is still exempt if the municipality confirms the land cannot be subdivided for separate building, or a Vurderingsstyrelsen statement shows subdivision would cut the value of the rest by more than 20%. A loss on an exempt sale is not deductible. The same Danish conditions apply to a home abroad.

The gain is taxable where the home was bought to resell at a profit, nobody in the household ever lived there (such as a pure rental), or it is business property. A property with more than two independent dwellings cannot be sold exempt as a whole. After a two-family house is split into flats, only the flat lived in after the split qualifies. Only the land-register parcel carrying the home qualifies; a vacant building plot does not. A small farm valued as a one-family house can qualify.

Home with a business in it (such as a clinic or salon): a sale on or after 1 July 2025 is normally exempt if the property is valued as an owner-occupied home at the sale date and the residence and area tests are met. For a sale before 1 July 2025, the older test applies: it must look like a one-family house, and the home part must be at least 50% of value and 50% of area.

Holiday homes are exempt if used privately and under 1,400 m2 (same subdivision exceptions); purely let-out holiday homes are taxable. A cooperative flat (andelsbolig) is taxed under the share-gains act as share income in field 67, but the gain is exempt if the owner lived there and the land belonging to the flat is under 1,400 m2.

**Taxable property gain.** Use the year of the binding sale agreement. Proceeds less sale costs, minus adjusted cost: purchase price plus purchase costs, plus DKK 10,000 for the purchase year and each later calendar year owned except the sale year (one addition if bought and sold in the same year; pro rata for part-owners), plus maintenance and improvement spend above DKK 10,000 in each calendar year (EBL § 5). Never add spend already deducted. The gain is capital income. A property loss can only be set against property gains, the same year or later, and against a cohabiting spouse's property gains (EBL § 6).

## Deadlines and filing

- **Annual return:** employees and investors check and complete the annual assessment (årsopgørelse) in TastSelv by 1 May of the year after the income year (1 May 2027 for 2026). Taxpayers with business income use 1 July (see dk-income-tax). Confirm the date shown in TastSelv for the person.
- **Share fields:** listed shares in Danish custody and Danish listed shares abroad: field 66 (often prefilled). Foreign listed shares abroad: 454, own calculation. Danish unlisted shares: 67. Foreign unlisted shares: 451. Foreign custody also needs the year-end value in DKK.
- **Fund fields:** share-based minimum-tax fund: 66 (foreign 454). Bond-based minimum-tax fund: 30 (foreign 434). Share-based investment company: 345 (foreign 375). Bond-based investment company: 38 (foreign 422).
- **Property:** Danish taxable gain field 39; loss field 84; foreign property gain 425 with eligible foreign tax in 495K. Update the preliminary assessment after a sale.
- **Crypto:** gains 20, losses 58.
- **Purchase reporting for loss relief:** 1 July of the year after purchase (see above).
- **Aktiesparekonto:** nothing to file; the bank pays the 17% tax.
- **Corrections:** the 2025 return can be changed until 1 May 2029 and the 2024 return until 1 May 2028. Later changes need special circumstances, asked for within 6 months.

## Penalties and interest

- Missing the 1 July purchase-reporting date loses the listed-share loss permanently. This is the costliest mistake in this area.
- Unpaid tax after the annual assessment (restskat) carries a surcharge and, above an indexed amount, is collected in three instalments in August to October. The figures and the late-filing rules sit in dk-income-tax; use those.
- Aktiesparekonto over-deposits: 3% a year on the excess until withdrawn.
- Deliberate or grossly negligent under-reporting can lead to fines under Skattekontrolloven. Refer.

## Cross-border points

- **Exit tax on shares (ABL § 38):** when Danish tax liability ends, other than by death, gains on shares are treated as realised if the person's share holding is worth DKK 100,000 or more. Payment can be deferred (henstand). See dk-cross-border for the method.
- **Arrival:** shares held on becoming Danish taxable must be reported before 1 July of the year after liability starts to keep listed-share loss relief.
- **Foreign brokers and dividends:** foreign custody is the taxpayer's own calculation. Reconcile gross dividends and foreign tax separately; credit for foreign tax is not automatically everything the broker withheld.
- **Foreign homes:** Danish parcelhus conditions decide the Danish exemption, whatever the other country does.

## Worked examples

**Example 1: single investor with DKK 100,000 share income.** A single person sells listed shares in Danish custody for a gain of DKK 85,000 and receives DKK 15,000 of dividends. Share income is DKK 100,000. The first DKK 79,400 is taxed at 27% (DKK 21,438). The remaining DKK 20,600 is taxed at 42% (DKK 8,652). Share-income tax is DKK 30,090, before credit for dividend tax withheld. If the person were married and living with a spouse with no share income at year end, the couple's band would be DKK 158,800 and all DKK 100,000 would be taxed at 27% (DKK 27,000).

```oa-check
name: Single investor, share income DKK 100,000 (2026 band)
inputs:
  gains: 85000
  dividends: 15000
  band: 79400
  couple_band: 158800
steps:
  - share_income: gains + dividends
  - low: min(share_income, band) * 0.27
  - high: max(share_income - band, 0) * 0.42
  - tax_single: low + high
  - tax_couple: min(share_income, couple_band) * 0.27 + max(share_income - couple_band, 0) * 0.42
expected:
  share_income: 100000
  low: 21438.00
  high: 8652.00
  tax_single: 30090.00
  tax_couple: 27000.00
```

**Example 2: rental flat sold in the year (sale-year addition excluded).** A person bought a flat in January 2024 for DKK 1,500,000 plus DKK 50,000 purchase costs and let it out; nobody in the household lived there, so the parcelhusreglen does not apply. In 2025 they spent DKK 30,000 on improvements. They sell in 2026 for DKK 2,000,000 with DKK 100,000 sale costs. The annual addition is given for 2024 and 2025 but not 2026, the sale year: DKK 20,000. Only the 2025 spend above DKK 10,000 counts: DKK 20,000. Adjusted cost is DKK 1,590,000. Net proceeds are DKK 1,900,000. The taxable gain is DKK 310,000, capital income for field 39. It is taxed with the person's other income, not at the share rates.

```oa-check
name: Rental flat, bought 2024, sold 2026 (EBL section 5)
inputs:
  price: 2000000
  sale_costs: 100000
  purchase: 1500000
  purchase_costs: 50000
  years_with_addition: 2
  improvements_2025: 30000
steps:
  - net_proceeds: price - sale_costs
  - additions: years_with_addition * 10000
  - improvements_counted: max(improvements_2025 - 10000, 0)
  - adjusted_cost: purchase + purchase_costs + additions + improvements_counted
  - gain: net_proceeds - adjusted_cost
expected:
  net_proceeds: 1900000
  additions: 20000
  improvements_counted: 20000
  adjusted_cost: 1590000
  gain: 310000
```

## Ask the client first

1. Were you fully liable to Danish tax all year, and are you married and living with your spouse on 31 December?
2. For each holding: what is it (share, fund, ETF, bond, crypto), is it admitted to trading, where is it held, and is it in an aktiesparekonto?
3. For any fund or ETF: is it on SKAT's list of share-based investment companies for 2026?
4. For loss-making listed shares bought through a foreign broker: did SKAT receive the purchase details by 1 July of the following year? Do you have proof?
5. For a property: did you or your household ever live there, what is the land area, what did it cost with costs and improvements by year, and when was the sale agreement signed?
6. Are you planning to leave Denmark, and is your share holding worth DKK 100,000 or more?

## Sources

| Source | URL | Read on |
|---|---|---|
| Aktieavancebeskatningsloven, LBK nr. 849 of 21 September 2026 (§§ 13 A, 19, 23, 26, 38) | https://www.retsinformation.dk/eli/lta/2026/849 | 2026-10-26 |
| Personskatteloven, LBK nr. 1284 of 14 June 2021 (§ 8 a) | https://www.retsinformation.dk/eli/lta/2021/1284 | 2026-10-26 |
| Kursgevinstloven, LBK nr. 1176 of 19 September 2025 (§§ 14, 23) | https://www.retsinformation.dk/eli/lta/2025/1176 | 2026-10-26 |
| Ejendomsavancebeskatningsloven, LBK nr. 132 of 25 January 2019 (§§ 5, 6, 8) | https://www.retsinformation.dk/eli/lta/2019/132 | 2026-10-26 |
| Aktiesparekontoloven, LBK nr. 281 of 13 March 2025 (§§ 14, 22) | https://www.retsinformation.dk/eli/lta/2025/281 | 2026-10-26 |
| SKAT, tax on shares (2026 bands, loss rules, fields) | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier | 2026-10-26 |
| SKAT, aktiesparekonto (2026 ceiling) | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/aktiesparekonto | 2026-10-26 |
| SKAT, investment funds (lagerprincippet, fields) | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-investeringsbeviser-udstedt-af-investeringsforeninger-og-investeringsselskaber | 2026-10-26 |
| SKAT, selling an owner-occupied home | https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-ejerbolig | 2026-10-26 |
| SKAT, crypto gains and losses | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-paa-krypto-kend-reglerne-saa-du-undgaar-et-skattesmaek/beregn-og-oplys-gevinst-og-tab-paa-krypto | 2026-10-26 |
| SKAT, purchase reporting for loss relief | https://skat.dk/borger/aktier-og-andre-vaerdipapirer/skat-af-aktier/betingelser-for-fradrag-for-tab-paa-aktier-og-investeringsbeviser | 2026-09-25 |
| SKAT, share-based investment companies list | https://skat.dk/erhverv/ekapital/vaerdipapirer/beviser-og-aktier-i-investeringsforeninger-og-selskaber-ifpa | 2026-09-25 |
| SKAT, holiday home sale | https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-sommerhus | 2026-09-25 |
| SKAT, cooperative flat sale | https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-andelsbolig | 2026-09-25 |
| SKAT, foreign home sale | https://skat.dk/borger/bolig-og-ejendomme/salg-af-bolig/salg-af-bolig-i-udlandet | 2026-09-25 |
| SKAT, correcting old returns | https://skat.dk/borger/aarsopgoerelse/se-og-ret-dine-gamle-aarsopgoerelser | 2026-09-25 |

Not yet confirmed: the latest consolidations of Personskatteloven (2021) and Ejendomsavancebeskatningsloven (2019) predate later amendments, so the 2026 band and the 1 July 2025 mixed-use home rule come from skat.dk, not the consolidated text; the 1 May 2026 filing date for non-business taxpayers, the correction cut-off dates, the fund and property field numbers (30, 434, 345, 375, 38, 422, 425, 495K) and the holiday-home, cooperative-flat and transitional purchase-reporting rules were carried from the September 2026 reading of skat.dk and not re-read today; the 2026 interest and surcharge rates on restskat are not stated here.

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
