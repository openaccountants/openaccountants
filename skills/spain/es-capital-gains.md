---
name: es-capital-gains
description: Use this Guide to compute Spanish common-territory individual capital gains and losses for 2026. It covers transfer versus non-transfer classification, acquisition and disposal values, fees, improvements, depreciation, homogeneous-security identification, main-home reinvestment, over-65 relief, insured life annuities, pre-1994 abatement, repurchase-deferred losses, annual savings-pool integration and the current savings scale. Trigger phrases include capital gains Spain, ganancia patrimonial, sell shares, property gain, reinversión vivienda habitual, coeficientes de abatimiento, pérdida por recompra and compensación de pérdidas. Obtain the actual residence, asset and lot records, prices, eligible costs, prior-loss and repurchase history and relief evidence. The computation uses the taxpayer’s whole annual savings position and minimum allocation rather than taxing each sale through fresh first bands. Non-resident and special incoming-worker cases follow their companion routes.
version: 1.6
jurisdiction: ES
tax_year: 2026
last_updated: 2026-11-27
drafted_by: OpenAccountants
approved_by: pending
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Spain: individual capital gains and losses v1.6

Compute common-territory resident gains for 2026 using actual asset records, then integrate reliefs, losses and the whole annual savings position. All amounts below are EUR.

## Who this applies to

A gain or loss is a value change revealed by an alteration in asset composition unless classified as another income category. Transfer gains/losses normally enter savings income; non-transfer gains/losses enter the general base ([LIRPF arts. 33, 45–46](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a33)). Holding period alone does not change the savings rate. Disposing of a business fixed asset can remain a capital gain under [art. 28.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a28); distinguish it from trading stock.

For gifts, inheritances, succession agreements, qualifying business gifts, partitions and co-ownership or matrimonial-property changes, this Guide supplies no transaction-specific exemption or basis conclusion. Check this point with one of our partner accountants.

Use [es-income-tax](es-income-tax.md) for general taxation and minima, [es-irpf-deductions](es-irpf-deductions.md) for regional credits, [spain-crypto-tax](spain-crypto-tax.md) for crypto, [es-rental-income](es-rental-income.md) for rental income, [es-beckham](es-beckham.md) for the incoming-worker regime, [es-foral-income-tax](es-foral-income-tax.md) for foral IRPF and [the cross-border Guide](es-non-resident-income-tax-irnr-and.md) for residence, PE, treaty, departure and non-resident procedures. Inheritance/gift tax, municipal urban-land tax and wealth tax need separate work.

## Rates, bands and thresholds

| 2026 resident savings-base slice | Combined marginal rate | Quota at lower boundary | Source |
|---|---:|---:|---|
| 0–6,000 | 19% | 0 | [LIRPF arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a66) |
| >6,000–50,000 | 21% | 1,140 | [Arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a76) |
| >50,000–200,000 | 23% | 10,380 | [Arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a66) |
| >200,000–300,000 | 27% | 44,880 | [Arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a76) |
| >300,000 | 30% | 71,880 | [Arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a66) |

These combine the state and autonomous halves, each 9.5/10.5/11.5/13.5/15%. There is no separate annual capital-gains allowance. Allocate the available personal/family minimum under [arts. 56/66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a56): general income uses it first; any available remainder enters the savings calculation. Apply the statutory tax-on-minimum reduction in each half, rather than taxing `(gain − whole minimum)` or giving every sale new first bands.

## The base

### Ordinary sale and securities

Under [LIRPF arts. 34–35](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a35):

`acquisition_value = acquisition_price + eligible_acquisition_costs/taxes + improvements − required_depreciation`.

`transfer_value = max(actual_sale_price, required_normal_market_value) − eligible_seller_transfer_costs/taxes`.

`gain_or_loss = transfer_value − acquisition_value`.

Exclude acquisition interest. Separate improvements from repairs already deducted and do not deduct a cost twice. For depreciable assets, deduct at least minimum depreciation even if it was not claimed ([RIRPF art. 40](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a40)).

For ordinary listed equity within the regulated-market population in [art. 37.1(a)](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a37), the transfer reference is the higher of quotation at disposal and agreed price, before eligible seller expenses. Identify the statutory market; a platform's “listed” label is insufficient. Homogeneous securities use FIFO under art. 37.2.

For ordinary unlisted equity, absent proof of the price independent parties would agree under normal market conditions, art. 37.1(b) sets a floor: the greater of attributable net assets in the last financial year closed before tax accrual and attributable average results of the three financial years closed before tax accrual divided by 20%. The results measure includes dividends distributed and allocations to reserves, excluding regularisation/revaluation reserves. Use the actual price if higher; valid independent-price proof permits the actual-price route. The statutory transfer value also determines the buyer's acquisition value. Deduct eligible seller expenses and the established acquisition value.

Original unlisted-share case, with ordinary nonemployee shares, no special transaction/expenses and basis 5,000: sale 7,000, attributable net assets 10,000 and three-year average results 3,000 give capitalised results `3,000 / 20% = 15,000`, hence gain 10,000. With valid independent-price proof, gain is 2,000; with actual price 18,000 and no such proof, gain is 13,000.

For partially paid bonus shares, basis is the amount paid. For fully paid bonus shares, spread total cost across old and new shares; art. 37.2 retains the old shares' seniority. Subscription-right proceeds under art. 37.1(a)/(b) are a gain in the disposal year. For listed shares' earlier rights, [DT 29](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtvigesimanovena) deducts proceeds from rights sold before 1 January 2017 from share basis, excluding amounts already taxed as gains; partial rights sales attach to the earliest securities.

Original rights cases: basis 10,000, untaxed 2016 rights proceeds 2,000, ordinary 2026 sale 15,000 give adjusted basis 8,000 and gain 7,000. If the 2,000 was already taxed as a gain, basis stays 10,000 and gain is 5,000.

Fund valuation/transfer deferral, tax-neutral exchanges, employee-share reliefs and startup-share reinvestment under art. 38.2 are non-usable here until their separate eligibility and valuation records are checked. Check this point with one of our partner accountants.

### Main-home relief

Keep home reinvestment and the over-65/dependency exemption separate.

For [home reinvestment, RIRPF art. 41](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a41), the required amount is transfer value less principal still outstanding on the loan used to acquire the old home. On a positive required amount, `exempt_gain = positive_gain × min(qualifying_reinvestment / required_amount, 1)`. There is no general 240,000 ceiling or age test for this relief. The replacement must qualify as the taxpayer's main home. Reinvestment is within two years before/after disposal; where it occurs after the disposal year, state the intention in that year's return. Instalment sales, rehabilitation and any zero/negative required-amount case need separate application of the article; no automatic full exemption is supplied here. Check this point with one of our partner accountants.

Under [LIRPF art. 33.4(b)](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a33), a qualifying main-home gain of someone over 65 or with severe/great dependency is exempt without reinvestment or a cash ceiling. [AEAT's ownership explanation](https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/que-ocurre-cuando-vendo-inmueble/transmision-vivienda-habitual-mayores-65-anos.html) distinguishes a full owner transferring bare ownership while reserving life usufruct, which can qualify, from full ownership already split between bare owner and usufructuary, where neither holder qualifies merely by transferring their existing right. For the ordinary case, [AEAT's full-ownership criterion](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c11-ganancias-perdidas-patrimoniales/ganancias-perdidas-patrimoniales-que-no-bi/ganancias-patrimoniales-exentas.html) requires full ownership, which may be shared, throughout the continuous period of at least three years. This ownership criterion is administrative interpretation, not express wording in art. 33.4(b). Cases relying on an exception to the ordinary period need individual review. Check this point with one of our partner accountants.

[RIRPF art. 41 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a41bis) generally requires three continuous years of residence and effective permanent occupation within twelve months of acquisition/completion. Death or justified circumstances necessarily requiring a move can excuse the three-year period; death/necessary impediments and the specified employment-provided-home case can excuse or postpone occupation. Mere convenience is insufficient.

Normally the property must be the main home at disposal or have had that status on any day in the preceding two years. Under the wording effective **8 October 2026**, an over-65 or severely/greatly dependent transferor's qualifying former main home can also retain status where they moved because of age/dependency to a specialised centre or a relative's home within the third degree of blood/affinity. Other ownership and relief conditions still apply. For separation, divorce or annulment causing a spouse to leave, the departing spouse meets the occupation-at-disposal/two-year condition when the spouse remaining meets it. Informal separation evidence needs individual review. Check this point with one of our partner accountants.

Original relocation case: a 73-year-old full owner sells on 15 October 2026 for a positive gain 90,000 after moving in 2022 to their granddaughter's home because of age. With the prior main-home status and all other art. 33.4(b) conditions proved, that gain is exempt without reinvestment. This does not cover an unrelated person's home or an unexplained voluntary move.

The dated chain is [RDL 26/2026 DF3.1/DF11.1](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-20266), effective 1 October; [repeal on 2 October](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-20526); and [RDL 29/2026 DF3.1/DF11.1](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-20823), effective 8 October. Do not apply the current extension retrospectively to every 2026 disposal. Outcomes during 2–7 October or depending on an entitlement accrued before repeal are non-usable here. Check this point with one of our partner accountants.

### Over-65 insured-annuity reinvestment

For qualifying asset disposals by taxpayers over 65, [LIRPF art. 38.3/RIRPF art. 42](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a42) provide a separate relief. For positive proceeds:

`eligible_reinvestment = min(total_amount_obtained, qualifying_reinvestment, max(240,000 − prior_eligible_reinvestment, 0))`.

`exempt_gain = positive_gain × eligible_reinvestment / total_amount_obtained`.

This uses disposal proceeds, not the gain or the home-relief loan-net denominator. Unrelated overfunding does not increase exemption or consume more qualifying allowance. Original cases: 30,000 proceeds, 10,000 gain and 60,000 annuity funding exempt at most 10,000; qualifying reinvestment of 15,000 against the same proceeds exempts 5,000. No negative-gain or zero-denominator exemption is asserted.

Constitute the annuity within six months. If the gain bears withholding and all proceeds net of withholding fund it within six months, only the withheld part's deadline extends to the end of the next year: 31 December 2027 for a 2026 disposal. Notify the insurer of the qualifying reinvestment; if investment is after the gain year, state the intention in that year's return.

The contract must be with an insurer, name the taxpayer as beneficiary, pay at least annually, start within one year and decrease annual payment by no more than 5% against the previous year. Contracts with reversion, guaranteed payment periods or death-refund cover require the separate safeguards in RIRPF DA 9 and the pre-1 April 2019 transition in DT 18 before using this relief. This Guide supplies no approval of such contract terms. Check this point with one of our partner accountants.

For home/annuity relief failure, including full/partial anticipation of annuity economic rights, attribute the corresponding nonexempt gain to its original year and file a supplementary return with late-payment interest from breach until the end of the ordinary filing period for the breach year ([RIRPF arts. 41.5/42.5](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a42)).

### Pre-1994 abatement

Apply [LIRPF DT 9](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtnovena) only to qualifying assets acquired **before 31 December 1994**, outside business use; de-affection must precede disposal by more than three years. Separate improvements and their disposal-value/holding components.

For the general asset method, calculate the ordinary gain, then pre-20 January 2006 gain as `gain × days_from_acquisition_through_19_January_2006_inclusive / total_holding_days`. Count holding years to 31 December 1996, rounded up; apply the reduction for each year beyond two to the eligible pre-2006 part.

| DT 9 asset class | Reduction per qualifying year beyond two | Complete pre-2006 exclusion, subject to cap | Source |
|---|---:|---|---|
| Real estate/rights and specified property-rich securities, excluding real-estate investment companies/funds | 11.11% | Holding period over ten years | [DT 9.1.1(c)(1)](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtnovena) |
| Qualifying listed equity, excluding investment-company shares named in the provision | 25% | Holding period over five years | [DT 9.1.1(c)(2)](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtnovena) |
| Residual assets | 14.28% | Holding period over eight years | [DT 9.1.1(c)(3)](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtnovena) |

Listed securities and relevant fund units instead use DT 9.1.2's **2005 wealth-tax value** split: if sale value is at least that value, the pre-2006 part is the gain calculated substituting the 2005 value; if sale value is below it, the whole positive gain is pre-2006. Then apply the relevant reduction and cap.

Track cumulative qualifying **transfer values**, not gains, from 1 January 2015. Where prior plus current transfer value is below 400,000, apply the reduction; where it crosses 400,000 with prior value below it, apply it only to the pre-2006-gain fraction matching remaining transfer-value capacity. Prior value above the cap permits no reduction. This is not a fresh annual/per-asset cap. The statute uses strict “inferior”/“superior” wording: where prior or cumulative value equals exactly 400,000 and the boundary decides the answer, no outcome is usable here. Check this point with one of our partner accountants.

### Loss pools and annual tax

First net investment-income items separately from admitted transfer gains/losses. If one pool is negative, cross-offset against the positive other pool only up to **25% of that positive balance** ([LIRPF art. 49](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a49)). Carry admitted unused losses for four following years, in statutory order and maximum amounts; retain origin year/type and do not restart expiry by combining with newer losses.

Apply [art. 33.5](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a33) repurchase deferral before pooling:

- Specified listed homogeneous securities: acquisitions within two months before/after disposal.
- Unlisted homogeneous securities: acquisitions within one year before/after disposal.
- Other sold assets reacquired within the following year: defer until that asset is later transferred.

For the securities, release the deferred loss as the retained securities are transferred. This is distinct from the four-year admitted-loss carryforward. Exclude unproved, consumption and lifetime-gift/liberality losses, gambling losses exceeding same-year winnings, and losses in the specially excluded DA 33 games. Non-transfer gains/losses stay in the separate [art. 48](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a48) general pool: its negative gain balance can offset at most 25% of positive general income, with four-year maximum-use carryforward.

Integrate all savings items and available minima, charge the annual scale, then apply actual credits/payments on account. Where other items use the bands, incremental tax from a gain is annual tax with that item less annual tax without it.

Ceuta/Melilla's conditional art. 68.4 quota credit, the 2012 urban-property partial exemptions (LIRPF DA 37/TRLIRNR DA 4), and non-resident pre-1994 or EU/EEA former-home reinvestment outcomes are non-usable here until the actual territorial, acquisition, connection and residence conditions are checked. No automatic exclusion, exemption or withholding reduction is supplied. Check this point with one of our partner accountants.

## Deadlines and filing

Residents report the accrual year's gain and relief details in Modelo 100 where obliged to file, using [LIRPF arts. 14/96](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a14). Obtain the operative 2026-return campaign order for filing in 2027; this Guide supplies no fixed future campaign dates. Retain basis, lots, depreciation, loss and reinvestment records.

## Penalties and interest

Voluntary late filing, assessed under-declaration, collection enforcement, information failures and relief-recapture supplements have distinct rules (LGT arts. 26–28/191 and RIRPF arts. 41–42). No case-specific surcharge, penalty or interest calculation is usable here. Check this point with one of our partner accountants.

## Cross-border points

Ordinary non-resident transfer gains use **19%**, subject to domestic exemption/treaty; residence outside the EU does not itself change that to 24% ([TRLIRNR arts. 24.4/25.1(f)](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a25)). A foreign broker does not remove a resident's worldwide gain ([LIRPF art. 2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a2)).

For a non-resident's Spanish-property sale, the purchaser's **Modelo 211/3%** payment on agreed consideration is due within one month; the seller's Modelo 210 window is the next three months after that first month, including nil/refund outcomes ([IRNR regulation art. 14](https://www.boe.es/buscar/act.php?id=BOE-A-2004-14532#a14); [210 order art. 5](https://www.boe.es/buscar/act.php?id=BOE-A-2010-19707#a5)). The withholding is a credit, not final gain tax. Use the cross-border Guide for the full non-resident basis, return, exemption and treaty analysis.

## Two worked examples that recompute

### 1. Ordinary disposal with costs

A hypothetical common-territory resident sells an asset in 2026 for **20,000**, pays eligible selling costs 100, and has acquisition price 10,000 plus eligible acquisition costs 50. No exemption, depreciation, earlier losses or other savings income applies; their minimum is already fully allocated to general income. Transfer value 19,900 less acquisition value 10,050 gives gain **9,850**. Savings tax is `6,000 ×19% +3,850 ×21% =1,948.50` ([LIRPF arts. 35/66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a35)).

```oa-check
name: Spain 2026 resident sale with acquisition and transfer costs
inputs:
  sale_price: 20000
  selling_costs: 100
  purchase_price: 10000
  purchase_costs: 50
steps:
  transfer_value: sale_price - selling_costs
  acquisition_value: purchase_price + purchase_costs
  gain: transfer_value - acquisition_value
  tax: min(gain, 6000) * 0.19 + max(gain - 6000, 0) * 0.21
expected:
  transfer_value: 19900
  acquisition_value: 10050
  gain: 9850
  tax: 1948.50
```

### 2. Repurchase deferral and capped loss offset are different ledgers

A hypothetical resident has realised transfer losses **10,000**, of which **2,000** is correctly allocated to homogeneous repurchased shares and deferred under art. 33.5. Thus current admitted transfer loss is 8,000. Positive investment income is 10,000, with no other items or prior losses and no remaining personal minimum. Cross-offset is at most 25% ×10,000 =**2,500**. Savings base is **7,500**, tax **1,455**. Carry **5,500 admitted loss** to the four following years and separately retain **2,000 deferred repurchase loss** until its release event ([LIRPF arts. 33.5/49](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a49)).

```oa-check
name: Spain 2026 repurchase-blocked loss and savings-pool cross-offset
inputs:
  realised_transfer_loss: 10000
  deferred_repurchase_loss: 2000
  positive_investment_income: 10000
steps:
  admitted_loss: realised_transfer_loss - deferred_repurchase_loss
  cross_offset: min(admitted_loss, positive_investment_income * 0.25)
  admitted_loss_carryforward: admitted_loss - cross_offset
  savings_base: positive_investment_income - cross_offset
  savings_tax: min(savings_base, 6000) * 0.19 + max(savings_base - 6000, 0) * 0.21
expected:
  admitted_loss: 8000
  cross_offset: 2500
  admitted_loss_carryforward: 5500
  savings_base: 7500
  savings_tax: 1455
```

## Ask the client first

1. What residence, territory, special regime and disposal year apply?
2. What asset, lot, dates, actual values, eligible costs, improvements and depreciation establish the gain?
3. What home ownership/use, age/dependency, loan, move and actual reinvestment/annuity records support relief?
4. What pre-1994 holding/improvement history, 2005 securities values and qualifying disposals since 2015 affect abatement?
5. What current/prior pool balances, repurchases, deferred releases, withholding and foreign tax affect annual tax?
6. What prior returns, relief conditions and breach dates determine filing or a supplementary return?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [LIRPF, Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Arts. 2/14/28/33–38/45–49/56/66/76/96, DT 9/29: classification, basis, shares, reliefs, pools, minima, annual rates and abatement | 2026-10-28; applicability checked 2026-11-27 |
| [RIRPF, RD 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Arts. 40–42: depreciation, habitual home, reinvestment, annuity and recapture; DA 9/DT 18 contract terms are referred | 2026-10-28; applicability checked 2026-11-27 |
| [AEAT main-home ownership](https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/que-ocurre-cuando-vendo-inmueble/transmision-vivienda-habitual-mayores-65-anos.html) | Full owner reserving usufruct versus already split rights | 2026-10-28; applicability checked 2026-11-27 |
| [AEAT 2025 manual, full ownership](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c11-ganancias-perdidas-patrimoniales/ganancias-perdidas-patrimoniales-que-no-bi/ganancias-patrimoniales-exentas.html) | Ordinary continuous full-ownership criterion only; current 2026 lookback comes from RIRPF | 2026-11-27 |
| [RDL 29/2026](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-20823), [RDL 26/2026](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-20266), [repeal](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-20526) | Operative home-status amendment, commencement and repeal chain | 2026-10-28 |
| [TRLIRNR](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527), [IRNR regulation](https://www.boe.es/buscar/act.php?id=BOE-A-2004-14532), [Modelo 210 order](https://www.boe.es/buscar/act.php?id=BOE-A-2010-19707) | Transfer-gain rate and property withholding/filing gateway | 2026-10-28; applicability checked 2026-11-27 |

Not yet confirmed: no usable outcome is asserted for the explicit partner-accountant holds above; obtain the future 2026-return campaign order before giving 2027 filing dates.

> Contributed by OpenAccountants.
