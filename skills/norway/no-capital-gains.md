---
name: no-capital-gains
description: "Norway capital gains tax: 22% rate, shield deduction (skjermingsfradrag) on shares, shareholder model, exit tax. Trigger on: \"Norway CGT\", \"capital gains Norway\", \"Norway 22% capital gains\", \"skjermingsfradrag\", \"shareholder model Norway\", \"sell shares Norway\", \"Norway aksjer skatt\", \"Norway exit tax shares\"."
version: 1.1
jurisdiction: "NO"
tax_year: 2026
last_updated: 2026-11-15
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Norway capital gains: individual investment method

## Scope

Income year 2026. Use this method for an individual who is tax resident in Norway with ordinary shares, fund units, investment accounts, private property or virtual assets. Confirm treaty residence and asset classification first. Corporate exemption, business asset disposals, employee option benefits and complex reorganisations need their own method. The name of a brokerage product does not determine its tax treatment. [Model](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/the-shareholder-model/) [Crypto](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/tax-regulations-virtual-currency/)

## Ask the client first

- Obtain residence and relocation dates, treaty position, ownership proportions and whether trading is a business.
- Obtain account contracts distinguishing ordinary custody, ASK and endowment insurance; holdings, all transactions, fees, currencies, distributions and year-end statements.
- Obtain lot-level purchase records, gifts/inheritances, capital repayments, splits and mergers, and documented unused shielding after dividend use.
- For property obtain contracts (including the date the sale was agreed), exact ownership/use dates, rental and holiday use, improvements, acquisition/sale costs and donor history where relevant.
- Ask about assets transferred abroad, prior exit-tax assessments, the exact date of any move or transfer (before or after 20 March 2024), payment elections, distributions, deaths and changes of residence. Missing records remain unresolved inputs, never an invented zero basis.

## Rates, bands and thresholds

| Item | Income-year rule | Official source |
| --- | --- | --- |
| Share gain/dividend after eligible shield, and share-loss tax effect | 37.84%; underlying amount uplifted by 1.72 and taxed at 22% | [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) |
| Other ordinary capital income, including virtual-asset gains and losses | 22%; classify first | [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) [Crypto](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/tax-regulations-virtual-currency/) |
| Ordinary personal return | 30 April following the income year. A 30-day extension is available if applied for by 30 April. Sole proprietors file by 31 May | [Return](https://www.skatteetaten.no/en/person/taxes/tax-return/tax-return-person/) [Tax Administration Regulation § 8-2-3](https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/*) |
| Own-home sale exemption | Sale made or agreed more than 1 year after acquisition, and the owner lived in the home for at least 12 months of the last 2 years (year counts in words on the page) | [Home](https://www.skatteetaten.no/ordbok/skatt-pa-gevinst-ved-realisasjon-av-fast-eiendom/) |
| Own holiday-home exemption | Sale made or agreed more than 5 years after acquisition and more than 5 years after first use or completion certification; used as own holiday home for at least 5 of the last 8 years (the year counts are in words on the page) | [Tax Act § 9-3(4)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/*) [Exempt](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/bolig-og-eiendeler/bolig-eiendom-tomt/salg/) |
| Fund share proportion | Above 80% treated as 100%; below 20% treated as zero; boundaries remain actual proportions | [Fund](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/taxation-of-units-in-mutual-funds/) |
| Exit tax on moving abroad on or after 20 March 2024 | NOK 3,000,000 deducted from the net (EEA/Svalbard) or gross (outside EEA) latent gain | [Exit](https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/) |
| Exit tax on transfer of assets to someone abroad on or after 20 March 2024 | Whole latent gain taxed when it exceeds NOK 100,000; no NOK 3,000,000 deduction | [Exit](https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/) |
| Exit tax on a move or transfer on or before 19 March 2024 | Older regime: tax applies when the net latent gain exceeds NOK 500,000 | [Exit](https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/) |

The annual shield rate is published in January after the income year. Do not insert an estimated 2026 rate into a final calculation prepared before publication. Prior unused shielding can be established from existing records. [Model](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/the-shareholder-model/)

## The method, step by step

1. **Route each asset and event.** Identify legal owner, security, account wrapper, acquisition and disposal dates, units, currencies and whether an actual or deemed disposal occurred. Keep dividends, gains, withdrawals and wealth separate.
2. **Build the evidence schedule.** Reconcile opening units plus purchases less disposals to closing units. Match each disposal to the appropriate lots and supporting statements. Resolve missing cost or wrapper data before calculating that item.
3. **Calculate using the applicable branch below.** Preserve gross proceeds, costs, input value, shield movements and underlying gain/loss. Do not uplift an amount twice or apply the share rate to all investments.
4. **Reconcile to reporting.** Compare the shareholder report, provider statement and tax return. Add missing assets; correct both the report and return where necessary. Reconcile total income, losses, wealth and foreign-tax claims separately.
5. **Deliver the working paper and submission record.** Show completed amounts, unresolved items, assumptions, source dates, return locations and final assessment comparison. Preserve evidence and re-submit any corrected return. [Report](https://www.skatteetaten.no/en/forms/the-shareholders-tax-report/) [Return](https://www.skatteetaten.no/en/person/taxes/tax-return/tax-return-person/)

### Ordinary shares: lots and currency

For shares of the same class in the same company, use the earliest acquired lots first (FIFO); historical/unknown acquisition records require the statutory special ordering rules. [Tax Act § 10-36](https://lovdata.no/dokument/NL/lov/1999-03-26-14/*). Allocate acquisition/disposal expenses once. Translate purchase value at the purchase-date exchange rate, sale proceeds at the sale-date rate, and expenses at their payment-date rates. A foreign broker's foreign-currency net profit is not the NOK result. Record exchange-rate evidence and reconcile fractional disposals. [Foreign](https://www.skatteetaten.no/en/person/to-from-norway/assets/income-wealth/report/)

Use net disposal proceeds minus established input value, including acquisition expenses. Gift/inheritance continuity, historical shares and reorganisations can change the input value; establish those positions before applying the ordinary formula. The default purchase rule is not permission to reset inherited cost to market value. [Model](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/the-shareholder-model/)

### Share shielding and estimated tax

The annual shield goes to whoever owns the share on 31 December. Available unused shield belongs to the particular share/lot after prior use against dividends. A dividend is taxed only on the part that exceeds the year's shield plus unused shield on that share, and the shield applies only to a lawfully distributed dividend. Apply unused shield against a positive gain, capped at that gain. It cannot create or enlarge a loss; the remainder expires on disposal. No disposal-year annual shield accrues to the seller of a share sold before year-end. Do not pool across unrelated lots. [Shield](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/tax-rules-for-gainslosses-from-realisations-and-share-dividends/find-your-deductible-risk-free-return/) [Model](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/the-shareholder-model/)

Record the underlying taxable gain or actual deductible loss; the tax service applies the uplift automatically. Check the uplift in the tax calculation rather than entering an already uplifted amount as the gain. A deduction's illustrated tax effect is not a guaranteed immediate refund: reconcile with the whole assessment. [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/)

### ASK share savings account

Only an individual can hold ASK, and it cannot be co-owned. It may hold only shares listed on a stock exchange in companies domiciled in the EEA, and units in EEA-domiciled equity funds whose share component exceeds 80% at the start of the income year. Money market funds are not allowed, and several companies listed on the Oslo Stock Exchange are not domiciled in the EEA, so they do not qualify. Cash in the account earns no interest. A holding that qualified when bought may stay in the account after the company moves outside the EEA or the fund's share component falls. [Ask](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/share-savings-account-ask/)

Internal sales and dividends retained inside ASK do not trigger ordinary immediate gain taxation; an internal loss is not deductible until the account is closed. Withdrawals first recover remaining deposited capital, then become taxable after available account shield. Maintain an account-level deposit/withdrawal/shield schedule and reconcile provider data. The annual shield base is the lowest deposit balance during the year plus prior unused shield; multiply by the published annual rate, without forecasting the final rate. On account termination, the shortfall of the closing value against remaining contributed capital establishes the deductible loss; unused shielding cannot increase it. Ordinary shares transferred into ASK are treated as sold, with FIFO applied, and any gain or loss is taxed then; qualifying transfers between ASK accounts follow continuity rules. Do not use the per-share ordinary-account shield schedule inside ASK. Check the provider's contract status before treating an account as ASK. [Ask](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/share-savings-account-ask/)

### Mutual funds

For distributions use the share proportion at the start of the income year. For disposal gains/losses use the average of the adjusted proportions in acquisition and disposal years, applying the table's high/low thresholds to each year's proportion before averaging. Allocate the gain/loss into share and interest parts; shield reduces the share gain, then the appropriate rates apply. Obtain provider history; older acquisitions and fund mergers have transition rules, so do not reconstruct historical proportions from today's portfolio. No second threshold rounding of the calculated average. [Fund](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/taxation-of-units-in-mutual-funds/)

### Endowment-insurance securities account

This branch requires endowment insurance without guaranteed yield and a secondary insurance element: death/disability supplement below 50% of remaining savings, or a fixed payment below 100% of invested savings. For qualifying accounts, every withdrawal realises a proportional part of capital and gain/loss. Capital returned equals withdrawal multiplied by remaining contributed capital divided by account market value immediately before withdrawal. Subtract that capital from the withdrawal for gain/loss and reduce the remaining capital accordingly. Allocate using the average adjusted annual equity proportions over the ownership period, not the fund acquisition/disposal average. Apply all usable shield against the whole gain: it may reduce the share part first, then the interest part; do not retain shield against a later share withdrawal while leaving current interest gain unrelieved. Check provider records and the contract's insurance conditions. [Insurance](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/tax-rules-for-investing-in-shares-and-other-securities-through-endowment-insurance-securities-account/)

### Private property

Establish exact ownership and use periods before deciding exemption. The own-home ownership test is met only if the sale is made or agreed more than one year after acquisition, so a sale agreed within the first year fails even if completion comes later. For a home the owner built, the ownership period runs from taking it into use or completion certification. The use test needs at least 12 months living in the home during the last 2 years; statutory use-obstacle and family-breakup exceptions, and mixed-use allocation, need the actual facts. [Tax Act § 9-3(2)-(3)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/*). [Home](https://www.skatteetaten.no/ordbok/skatt-pa-gevinst-ved-realisasjon-av-fast-eiendom/) The same ownership and use periods apply to property abroad. [Ordinary ownership/use tests](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/property-and-belongings/houses-property-and-plots-of-land/sale2/) A qualifying holiday home is not automatically taxable merely because it is not the main home. A loss is deductible only where a corresponding gain would be taxable. Giving a property away without payment, transfers between spouses, division of spouses' community property, inheritance and division of an estate are not realisations; a sale at an undervalue, a forced sale, an exchange or destruction is. Mixed residence/rental use, use obstacles, plots and inherited property require the official property's fact-specific decision path. [Exempt](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/bolig-og-eiendeler/bolig-eiendom-tomt/salg/)

For a taxable ordinary sale: output value includes cash and debt assumed by the buyer, less sale costs. Input value includes purchase/acquisition cost, relevant acquisition charges and qualifying improvements. Distinguish improvements from maintenance; do not add ordinary repairs to basis. Moving costs are not sale costs. Apply ownership share consistently. An estate sale is reported by the estate; obtain the proper acquisition value rather than using an heir's personal exemption. [Property](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/property-and-belongings/houses-property-and-plots-of-land/sale2/)

### Virtual assets

A sale, exchange into another token or payment using crypto normally realises the disposed asset. A gift transfer is not a realisation. Calculate NOK proceeds less documented NOK input value and transaction costs. A gain is taxed at 22% and a loss is deductible at 22%. There is no share uplift or shareholder shield. Mining/staking receipts and later disposal are separate events; business activity and unusual DeFi/NFT arrangements require separate classification. Do not claim an exchange insolvency loss solely because withdrawals are frozen: the provider must be declared bankrupt and it must be confirmed that you will get nothing back. A fraud loss is deductible only when documented as finally lost after attempts to recover it. [Crypto](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/tax-regulations-virtual-currency/)

FIFO does not apply to virtual currency. When several units of the same currency are held, identify which units were actually sold and use those units' input values; record the choice. Currency effects from converting to NOK are part of the gain or loss; do not calculate a separate currency gain. [Selling](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/selling/)

Keep dated units, market prices, fees and exchange-rate evidence. Report under Finance, Virtual assets/cryptocurrency; separate cards or an aggregate card with an asset breakdown are available. Crypto-linked exchange-traded financial products belong in their financial-product route, not automatically in the direct-token card. Retain purchase cost until disposal and report year-end wealth separately. [Purchase](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/purchases/)

### Exit tax: route before any disposal calculation

First fix the date of the move or transfer: the rules differ for events on or before 19 March 2024 and on or after 20 March 2024. For a move or transfer on or after 20 March 2024, covered latent investments include shares, funds, ASK and endowment-insurance accounts, employment options, partnership interests, share derivatives, foreign ETFs, and investment-type foreign pension accounts such as IRA and 401k. Real property and virtual assets are not on the official list. Residence under treaty rules, tax emigration or becoming resident on Svalbard can trigger exit tax. Use the return for the day before relocation/transfer, disclose the event, asset valuations/bases and payment election. The relocation deduction is in the table; current-year transfers followed by relocation require the aggregation rule in § 10-70(4), so do not apply a second independent deduction. [Tax Act § 10-70(4)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/*). Transfers use the whole relevant gain after any deductible losses once the net gain or loss exceeds NOK 100,000 in the income year; losses outside the EEA are not deductible. EEA/Svalbard netting differs from outside-EEA gross gains without losses. Only value built up while tax resident in Norway is taxed; returning residents with gains from an earlier untaxed Norwegian-residence period need the entry-value adjustment in § 10-70(6), rather than an automatic clean market-value reset. [Tax Act § 10-70(6)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/*). [Exit](https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/)

Current payment choices include immediate payment, instalments or full deferral over 12 years. The tax and accrued interest fall away for assets still held if you become resident in Norway again within 12 years after the end of the year the exit tax is timed to; assets already disposed of do not qualify. [Tax Act § 10-70(9)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/*). A latent loss deduction is given at once, cannot be deferred, and can be reversed within 12 years if you move out of the EEA or back to Norway. EEA security can still be required for collection risk. For the regime applying to moves/transfers from 7 October 2024, distributions can require repayment of 70% subject to the combined-tax cap; any transfer of the asset, including a sale, and death can accelerate liability, with inheritance exceptions. Later value falls/foreign tax do not automatically reduce current exit tax. If exit tax was not assessed, the ordinary reopening limit is 15 years after the end of the tax period, subject to the death/estate and prior-decision conditions in [Tax Administration Act § 12-6(1), (3)-(4)](https://lovdata.no/dokument/NL/lov/2016-05-27-14). Earlier departure regimes differ. Obtain specialist calculation for immigration basis, treaty issues, mixed assets, inherited liability and ongoing reporting; keep the authority updated while the liability lasts, and preserve a diary of notifications and annual obligations using the authority's event-specific instructions. [Exit](https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/)

## Return completion and corrections

Check the Shareholder's tax report against transaction records. Incorrect acquisition value or sale consideration requires changing/submitting that report, then transferring the recalculated gain/loss to the return. Dividend and wealth corrections are made directly in the return. Shares absent from the report and return go under Finance; reconcile domestic and foreign holdings without duplication. ASK is outside the shareholder report. [Report](https://www.skatteetaten.no/en/forms/the-shareholders-tax-report/)

For other assets use the asset's relevant return card and its current help text; retain a schedule linking each total to transactions. Do not invent legacy box numbers. Report foreign dividends gross and document any separately claimed foreign-tax credit. [Foreign](https://www.skatteetaten.no/en/person/to-from-norway/assets/income-wealth/report/)

The ordinary individual deadline and the sole-proprietor deadline are in the table. If the return is not submitted by the deadline, it is treated as submitted with the pre-filled information. Corrections require re-submission, including after a corrected provider report arrives. Previous-year self-amendments are generally available for the last three years; check the current amendment/appeal route for the affected year. Retain the submission acknowledgement and compare the resulting assessment. [Return](https://www.skatteetaten.no/en/person/taxes/tax-return/tax-return-person/)

## Worked cases

These examples use assumed complete records and illustrative final rounding. They are calculation aids, not taxpayer assessments. The annual shield is not estimated: example shields are established unused balances.

| Case | Assumed inputs | Expected result | Rule |
| --- | --- | --- | --- |
| Share gain | Basis 100,000; net proceeds 130,000; unused shield 2,000 | Raw gain 30,000; taxable 28,000; estimated tax 10,595.20 | [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) [Shield](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/tax-rules-for-gainslosses-from-realisations-and-share-dividends/find-your-deductible-risk-free-return/) |
| Shield exceeds gain | Basis 100,000; net proceeds 101,000; shield 2,000 | No taxable gain or deductible loss; unused remainder expires | [Shield](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/tax-rules-for-gainslosses-from-realisations-and-share-dividends/find-your-deductible-risk-free-return/) |
| Actual share loss | Basis 100,000; net proceeds 90,000; shield 2,000 | Deductible loss 10,000; tax effect 3,784; no shield enlargement | [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) [Shield](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/tax-rules-for-gainslosses-from-realisations-and-share-dividends/find-your-deductible-risk-free-return/) |
| Currency effect | USD 10,000 purchase at NOK 10/USD; same USD sale at NOK 11/USD; no costs/shield | NOK gain 10,000; tax effect 3,784 | [Foreign](https://www.skatteetaten.no/en/person/to-from-norway/assets/income-wealth/report/) [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) |
| ASK withdrawal | Remaining deposits 100,000; withdrawal 120,000; account shield 2,000 | Taxable withdrawal 18,000; tax effect 6,811.20 | [Ask](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/share-savings-account-ask/) [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) |
| Fund disposal | Gain 20,000; adjusted acquisition proportion 40%; disposal proportion 50%; no shield | Share gain 9,000; interest gain 11,000; total tax 5,825.60 | [Fund](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/taxation-of-units-in-mutual-funds/) [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) |
| Insurance withdrawal | Capital 100,000; value 200,000; withdrawal 40,000; adjusted average equity 60%; shield 15,000 | Capital returned 20,000; gain 20,000; share gain 12,000 fully shielded, remaining shield 3,000 reduces interest gain 8,000 to 5,000; tax 1,100 | [Insurance](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/tax-rules-for-investing-in-shares-and-other-securities-through-endowment-insurance-securities-account/) [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) |
| Taxable property | Cash/debt proceeds 3,000,000; sale costs 100,000; established basis including improvements 2,400,000 | Gain 500,000; estimated tax 110,000; no maintenance added | [Property](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/property-and-belongings/houses-property-and-plots-of-land/sale2/) [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/) |
| Crypto exchange | NOK value received 50,000; transaction costs 1,000; documented basis 30,000 | Gain 19,000; tax 4,180; record new asset separately | [Crypto](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/tax-regulations-virtual-currency/) |
| Crypto loss | Documented basis of the identified units 40,000; net NOK proceeds 30,000 | Deductible loss 10,000; tax effect 2,200; no share uplift | [Crypto](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/tax-regulations-virtual-currency/) [Selling](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/selling/) |
| Home boundary | Assessed realisation date exactly one year after acquisition; no exception | Exemption ownership test fails; assess taxable result | [Home](https://www.skatteetaten.no/ordbok/skatt-pa-gevinst-ved-realisasjon-av-fast-eiendom/) |
| Home sale agreed early | Owner lived in the home throughout; sale agreed 11 months after purchase; completion 13 months after purchase | Ownership test fails because the sale was agreed within one year; gain taxable, loss deductible | [Home](https://www.skatteetaten.no/ordbok/skatt-pa-gevinst-ved-realisasjon-av-fast-eiendom/) |
| Property gift | Parent gives a rental flat to a child with no payment | Not a realisation for the parent; no gain or loss now; child's later sale needs the gift-continuity path | [Exempt](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/bolig-og-eiendeler/bolig-eiendom-tomt/salg/) |
| ASK capital return | Remaining deposits 100,000; withdrawal 40,000 | No taxable withdrawal; remaining deposits 60,000 | [ASK](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/share-savings-account-ask/) |
| ASK closure loss | Remaining deposits 100,000; final account value 90,000; account closed | Deductible loss 10,000; unused shield does not enlarge the loss | [ASK](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/share-savings-account-ask/) |
| ASK ineligible holding | Client wants to buy, inside ASK, shares of a company listed in Oslo but domiciled outside the EEA, or a money market fund | Not permitted in ASK; hold and tax it in an ordinary account | [ASK](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/share-savings-account-ask/) |
| Missing basis | Sale confirmed; purchase or continuity records absent | Obtain records; no invented gain or tax amount | [Model](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/the-shareholder-model/) |
| Exit event | Treaty residence changes during current year, assets remain unsold | Assess exit tax and disclosure; do not wait for a market sale | [Exit](https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/) |
| Pre-2024 departure | Treaty residence changed in 2023; net latent share gain 400,000 | Below the older NOK 500,000 threshold: no exit tax under that regime; do not apply the post-March-2024 rules | [Exit](https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/) |

### Recomputing the numerical cases above

The following blocks use the same hypothetical records as the table. They preserve full calculations and show derived outputs; they do not supply a missing annual shield or decide a real exemption. The share/crypto losses illustrate an assessment effect, not an automatic cash refund.

```oa-check
name: Norway 2026 Share gain and shield cap
inputs:
  basis: 100000
  net_proceeds: 130000
  unused_shield: 2000
  small_proceeds: 101000
steps:
  - raw_gain: net_proceeds - basis
  - taxable: max(raw_gain - unused_shield, 0)
  - tax: taxable * 1.72 * 0.22
  - small_raw_gain: small_proceeds - basis
  - small_taxable: max(small_raw_gain - unused_shield, 0)
  - small_unused_expired: unused_shield - min(unused_shield, max(small_raw_gain, 0))
expected:
  raw_gain: 30000
  taxable: 28000
  tax: 10595.2
  small_raw_gain: 1000
  small_taxable: 0
  small_unused_expired: 1000
```

```oa-check
name: Norway 2026 Actual share loss does not use shielding
inputs:
  basis: 100000
  net_proceeds: 90000
  unused_shield: 2000
steps:
  - actual_loss: basis - net_proceeds
  - tax_effect: actual_loss * 1.72 * 0.22
expected:
  actual_loss: 10000
  tax_effect: 3784
```

```oa-check
name: Norway 2026 NOK currency effect on an unchanged USD share price
inputs:
  usd_price: 10000
  purchase_rate: 10
  sale_rate: 11
steps:
  - basis: usd_price * purchase_rate
  - proceeds: usd_price * sale_rate
  - gain: proceeds - basis
  - tax_effect: gain * 1.72 * 0.22
expected:
  basis: 100000
  proceeds: 110000
  gain: 10000
  tax_effect: 3784
```

```oa-check
name: Norway 2026 ASK withdrawal after capital and established shield
inputs:
  deposits: 100000
  withdrawal: 120000
  shield: 2000
steps:
  - taxable_withdrawal: max(withdrawal - deposits - shield, 0)
  - tax_effect: taxable_withdrawal * 1.72 * 0.22
expected:
  taxable_withdrawal: 18000
  tax_effect: 6811.2
```

```oa-check
name: Norway 2026 Fund disposal allocates the adjusted average once
inputs:
  gain: 20000
  acquisition_equity: 0.4
  disposal_equity: 0.5
steps:
  - average_equity: (acquisition_equity + disposal_equity) / 2
  - share_gain: gain * average_equity
  - interest_gain: gain - share_gain
  - tax: share_gain * 1.72 * 0.22 + interest_gain * 0.22
expected:
  average_equity: 0.45
  share_gain: 9000
  interest_gain: 11000
  tax: 5825.6
```

```oa-check
name: Norway 2026 Insurance withdrawal uses remaining shield on interest component
inputs:
  capital: 100000
  value: 200000
  withdrawal: 40000
  equity_fraction: 0.6
  shield: 15000
steps:
  - capital_return: withdrawal * capital / value
  - gain: withdrawal - capital_return
  - share_gain: gain * equity_fraction
  - interest_gain: gain - share_gain
  - share_shield: min(shield, share_gain)
  - interest_shield: min(shield - share_shield, interest_gain)
  - tax: (share_gain - share_shield) * 1.72 * 0.22 + (interest_gain - interest_shield) * 0.22
expected:
  capital_return: 20000
  gain: 20000
  share_gain: 12000
  interest_gain: 8000
  share_shield: 12000
  interest_shield: 3000
  tax: 1100
```

```oa-check
name: Norway 2026 Taxable property gain excludes selling costs once
inputs:
  cash_and_debt_proceeds: 3000000
  sale_costs: 100000
  established_basis: 2400000
steps:
  - gain: cash_and_debt_proceeds - sale_costs - established_basis
  - tax: gain * 0.22
expected:
  gain: 500000
  tax: 110000
```

```oa-check
name: Norway 2026 Crypto exchange and separately identified loss
inputs:
  received_value: 50000
  costs: 1000
  basis: 30000
  loss_basis: 40000
  loss_net_proceeds: 30000
steps:
  - exchange_gain: received_value - costs - basis
  - exchange_tax: exchange_gain * 0.22
  - loss: loss_basis - loss_net_proceeds
  - loss_tax_effect: loss * 0.22
expected:
  exchange_gain: 19000
  exchange_tax: 4180
  loss: 10000
  loss_tax_effect: 2200
```

```oa-check
name: Norway 2026 ASK capital recovery and closure loss are separate events
inputs:
  deposits: 100000
  withdrawal: 40000
  closing_value: 90000
steps:
  - taxable_withdrawal: max(withdrawal - deposits, 0)
  - remaining_deposits: deposits - withdrawal
  - separate_closure_loss: deposits - closing_value
  - closure_tax_effect: separate_closure_loss * 1.72 * 0.22
expected:
  taxable_withdrawal: 0
  remaining_deposits: 60000
  separate_closure_loss: 10000
  closure_tax_effect: 3784
```

### Ordinary custody or ASK: retain versus withdraw

Assume the same eligible investment costs NOK 100,000, is sold for net NOK 130,000, and has an established usable shield of NOK 2,000 under the applicable account rules. In ordinary custody the sale gives taxable gain NOK 28,000 and estimated tax NOK 10,595.20. If the sale proceeds stay inside ASK, current sale tax is NOK 0. If all NOK 130,000 is immediately withdrawn from ASK, taxable withdrawal is NOK 28,000 and the same estimated NOK 10,595.20 arises. Keeping eligible reinvestment funds inside ASK therefore defers this tax; withdrawing everything removes that timing benefit. ASK eligibility, shield and loss timing must still be checked, and transferring an existing ordinary holding into ASK itself realises it. [ASK](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/share-savings-account-ask/) [Rate](https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/)

```oa-check
name: Norway 2026 ordinary sale versus ASK retained or fully withdrawn
inputs:
  capital: 100000
  net_sale: 130000
  established_shield: 2000
steps:
  - ordinary_taxable: max(net_sale - capital - established_shield, 0)
  - ordinary_tax: ordinary_taxable * 1.72 * 0.22
  - ask_retained_tax: 0
  - ask_full_withdrawal_taxable: max(net_sale - capital - established_shield, 0)
  - ask_full_withdrawal_tax: ask_full_withdrawal_taxable * 1.72 * 0.22
  - current_tax_deferred: ordinary_tax - ask_retained_tax
expected:
  ordinary_taxable: 28000
  ordinary_tax: 10595.20
  ask_retained_tax: 0
  ask_full_withdrawal_taxable: 28000
  ask_full_withdrawal_tax: 10595.20
  current_tax_deferred: 10595.20
```

## When to refuse or refer

- Stop the affected calculation if input value, lot identity, wrapper, residence, shielding or material transaction data cannot be established.
- Refer reorganisations, unusual derivatives, historic transition values, treaty conflicts, inheritance/estate complications and business disposals to the relevant method or qualified adviser.
- Refer exit-tax liability and payment monitoring when the full residence/valuation/history record is not available. Apply the regime that matches the date of the move or transfer: never apply the older NOK 500,000 threshold to an event on or after 20 March 2024, and never apply the newer rules to an earlier event.
- Distinguish estimates from filing-ready amounts and unresolved items from checked totals. Revisit the final annual shield and filing instructions when published.

## Sources

| Actual scope read | Official URL | Read on |
|---|---|---|
| Read for scope, input value/continuity, per-share annual and unused shield, disposal cap/expiry; exclude its stale exit-tax footer | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/the-shareholder-model/ | 2026-11-15 |
| Read for crypto realisations, 22% capital treatment, documentary expenses, fraud and bankruptcy | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/tax-regulations-virtual-currency/ | 2026-11-15 |
| Read for 2026 share uplift/rates and ordinary capital rate | https://www.skatteetaten.no/en/rates/factor-for-upward-adjustment-of-gainloss-or-dividend-on-shares/ | 2026-11-15 |
| Read for current return workflow, extension, resubmission, amendment and personal/ENK deadlines | https://www.skatteetaten.no/en/person/taxes/tax-return/tax-return-person/ | 2026-11-15 |
| Read for Tax Administration Regulation §§ 8-2-3 and 8-2-5: deadline categories and extension conditions | https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/* | 2026-11-15 |
| Read for ordinary own-home ownership/use boundary | https://www.skatteetaten.no/ordbok/skatt-pa-gevinst-ved-realisasjon-av-fast-eiendom/ | 2026-11-15 |
| Read for Tax Act §§ 9-3, 10-31, 10-36 and 10-70: home/holiday boundaries, share shield/uplift, FIFO special cases, current exit rules and adjacent exceptions | https://lovdata.no/dokument/NL/lov/1999-03-26-14/* | 2026-11-15 |
| Read for Norwegian property sale guidance and non-realisations | https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/bolig-og-eiendeler/bolig-eiendom-tomt/salg/ | 2026-11-15 |
| Read for fund allocation, strict 80/20 tests, adjusted acquisition/disposal averaging and historical routes; use the separate 2026 rate page | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/taxation-of-units-in-mutual-funds/ | 2026-11-15 |
| Read for both historical and current exit regimes, asset list, thresholds/netting, elections, distribution dates, loss/security/return exceptions and reporting | https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/exit-tax/ | 2026-11-15 |
| Read for shareholder report corrections, absent shares, direct dividend/wealth corrections and transfer to return | https://www.skatteetaten.no/en/forms/the-shareholders-tax-report/ | 2026-11-15 |
| Read for foreign shares/securities, gross dividends, purchase/sale/cost exchange dates and foreign-tax evidence | https://www.skatteetaten.no/en/person/to-from-norway/assets/income-wealth/report/ | 2026-11-15 |
| Read for per-share shield and no pooling | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/tax-rules-for-gainslosses-from-realisations-and-share-dividends/find-your-deductible-risk-free-return/ | 2026-11-15 |
| Read for ASK eligibility, grandfathered holdings, transfers, deposits, shield, withdrawals, closure loss and reporting | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/share-savings-account-ask/ | 2026-11-15 |
| Read for secondary insurance tests, proportional capital, annual averaging and whole-gain shield; use the separate 2026 rate page | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/tax-rules-for-investing-in-shares-and-other-securities-through-endowment-insurance-securities-account/ | 2026-11-15 |
| Read for property basis/costs, maintenance, estate and gift routes, Norway/abroad scope | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/property-and-belongings/houses-property-and-plots-of-land/sale2/ | 2026-11-15 |
| Read for identified units, no FIFO, integrated currency effect and return cards; illustrative authority arithmetic not relied on | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/selling/ | 2026-11-15 |
| Read for purchase-date NOK basis/costs and year-end reporting | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/digital-currency/purchases/ | 2026-11-15 |

| Read for exit-tax reopening and adjacent death/estate and prior-decision limits, Tax Administration Act § 12-6 | https://lovdata.no/dokument/NL/lov/2016-05-27-14 | 2026-11-15 |

Not yet confirmed: the final annual shielding rate for income year 2026, published after year end; the final income-year-2026 live return fields; client-specific residence, wrapper eligibility, lot/basis/continuity and foreign-tax evidence. Complex reorganisations, historic transitions, business disposals and exit-tax monitoring require the specific method and records described above. The earlier foreign-income and property-abroad URLs now redirect to general hubs, so they have been replaced by operative current guidance. The shareholder-model page’s older exit-tax footer is not used for current departures.
