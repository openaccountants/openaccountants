---
name: netherlands-crypto-tax
description: Use this skill whenever asked about Netherlands cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Netherlands", "Bitcoin Netherlands", "crypto belasting", "Box 3 crypto", "vermogensrendementsheffing crypto", "cryptocurrency Netherlands", "crypto income Netherlands", "staking Netherlands", "mining income Netherlands", "NFT tax Netherlands", "Belastingdienst crypto", "Dutch crypto tax", "fictief rendement crypto", "heffingsvrij vermogen", "Overbruggingswet box 3", "Binance Netherlands tax", "Coinbase Netherlands tax", "aangifte crypto", or any question about the income tax, wealth tax, or VAT treatment of cryptocurrency, tokens, or digital assets for Dutch tax residents or Netherlands-source crypto income. Covers Box 3 wealth taxation, the deemed-return system, the actual-return counter-evidence route, Box 1 business classification, and DAC8 reporting. ALWAYS read this skill before touching any Netherlands crypto work.
version: 2.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-14
type: situation-rules
depends_on:
  - nl-income-tax
category: crypto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
---

# Netherlands crypto and digital assets: classification, valuation and income tax

Tax year 2026, with the 2025 return (being filed now) shown beside it.

## Scope

Use this method for an individual's Dutch crypto tax classification and the crypto component of a complete income-tax return. It covers tax year 2026 (provisional assessment and planning) and the 2025 return, each labelled. It also identifies payroll, business, VAT and company branches that require their own return method. Establish residence, ownership and the tax year before calculating. Migration, non-residence, trusts, companies and treaty questions require a specific scope decision; a Dutch exchange account alone does not establish Dutch taxing rights.

Private investment crypto normally belongs to Box 3. The ordinary method uses prescribed returns on reference-date assets (Wet IB 2001 art. 5.2), but the actual-return route (tegenbewijsregeling, Wet IB 2001 art. 5.25 to 5.36) includes annual income and value changes, including unrealised changes. Therefore neither "all gains are exempt" nor "only the January value ever matters" is an adequate instruction. Do not apply announced future Box 3 legislation to these years (the Belastingdienst expects new Box 3 law probably from 1 January 2028). Recheck enacted rules before extending this method to another year.

Sibling skills: the full income-tax computation (Box 1 bands, credits) lives in `nl-income-tax`; business profit and entrepreneur relief in `nl-zzp-deductions`; VAT in `nl-vat-return`.

## Ask the client first

Collect the following before producing a filing-ready result:

- Tax year, residence periods, age, fiscal-partner status and allocation, beneficial owner, minor-child holdings, employment and business connections.
- Every exchange, wallet, custodian and protocol; token quantities, legal rights and obligations, euro values on the reference date, and evidence of the pricing source and time. Include locked, lent, wrapped and collateralised positions, debts and bankruptcy claims.
- All other Box 3 assets and debts, exemptions and debt classification. A crypto-only total cannot calculate the taxpayer's overall Box 3 liability.
- For actual return: opening and closing values, purchases, sales, swaps, rewards, income, gifts and inheritances, transfers and debt interest throughout the year. Reconcile external cash movements and remove transfers between the same owner's wallets from purchases and sales.
- For mining, trading services, validators or NFT creation: what work was done, its economic purpose, expected and actual benefits, costs, organisation, contracts and whether the activity exceeds ordinary investment management. For employment or business receipts, record euro value at the relevant receipt or revenue recognition point.
- Existing return, assessment, actual-return request and any applicable filing deadline or extension.

## Rates, bands and thresholds

| Item | 2026 | 2025 return | Condition | Source |
|---|---:|---:|---|---|
| Deemed return, bank balances | 1.28% (provisional) | 1.37% (final) | 2026 figure is the provisional-assessment percentage; the final 2026 bank percentage is set after the year | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 |
| Deemed return, investments and other assets (crypto is here) | 6.00% | 5.88% | Wet IB 2001 art. 5.2(2); crypto counts as "beleggingen en andere bezittingen", not as a bank balance | https://wetten.overheid.nl/BWBR0011353/2026-01-01 |
| 2025 other-assets percentage | | 5.88% | Wet IB 2001 art. 5.2(2), version in force in 2025 | https://wetten.overheid.nl/BWBR0011353/2025-07-01 |
| Deemed return, debts | 2.70% (provisional) | 2.70% (final) | Wet IB 2001 art. 5.2(2) as amended by Stcrt. 2026, 3708, retroactive to 1 January 2025 | https://wetten.overheid.nl/BWBR0011353/2026-02-21 |
| 2025 final bank and debt percentages | | 1.37% and 2.70% | Belastingdienst table of final percentages per year | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/ |
| Tax-free assets (heffingvrij vermogen), individual | EUR 59,357 | EUR 57,684 | Wet IB 2001 art. 5.5 | https://wetten.overheid.nl/BWBR0011353/2026-01-01 |
| 2025 tax-free assets | | EUR 57,684 | Wet IB 2001 art. 5.5, 2025 version | https://wetten.overheid.nl/BWBR0011353/2025-07-01 |
| Tax-free assets, fiscal partners together | EUR 118,714 | EUR 115,368 | Whole-year partners (or the whole-year election); art. 5.2(5) adds both allowances | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 |
| Debt threshold, individual | EUR 3,800 | EUR 3,800 | Wet IB 2001 art. 5.3(3); only debts above the threshold count | https://wetten.overheid.nl/BWBR0011353/2026-01-01 |
| Debt threshold, fiscal partners together | EUR 7,600 | EUR 7,600 | Whole-year partners; art. 5.3(3) | same |
| Box 3 tax rate | 36% | 36% | Wet IB 2001 art. 2.13 | same |
| Assets reporting limit for income-dependent schemes (toeslagen), no partner | EUR 38,479 | EUR 37,395 | Assets above this must be reported in the return even when no Box 3 tax is due | https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/aangifte-doen-en-belasting-betalen-met-cryptos |
| Same limit, with fiscal partner | EUR 76,958 | EUR 74,790 | Same | same |
| Box 1 first band (below AOW age), combined tax and national insurance | 35.75% up to EUR 38,883 | 35.82% up to EUR 38,441 | Used only in the mining illustration; full bands in `nl-income-tax` | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/ |
| Reference-date arbitrage window | 3 months | 3 months | Wet IB 2001 art. 5.24; sale before and repurchase after 1 January within a 3-month period | https://wetten.overheid.nl/BWBR0011353/2026-01-01 |
| Box 1 loss carry-back and carry-forward | 3 years back, 9 years forward | same | Mandatory order: oldest preceding year first; not against Box 2 or Box 3 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/verlies_uit_onderneming |

The pooled fiscal-partner allowance, debt threshold and allocation apply only to qualifying whole-year partners or partners eligible for and making the whole-year election. Establish that status before pooling; otherwise use the individual and part-year rules (art. 5.2(6) time-apportions the advantage where Dutch residence starts or ends during the year).

The 2026 bank and debt percentages are provisional-assessment parameters, not final annual rates. The statute text in force from 21 February 2026 still reads 1.37% and 2.70% (the 2025 finals); the Belastingdienst uses 1.28% and 2.70% for provisional 2026 assessments. Preserve that status in every estimate.

## The method, step by step

### Step 1: Classify before calculating

| Situation | Method and decision |
|---|---|
| Private investment and speculative trading | Normally Box 3. Frequency, a trading bot, leverage or time spent does not by itself establish Box 1. The Belastingdienst compares crypto trading to trading ordinary currencies; it changes only where extra work beyond investment activities regularly produces additional income. |
| Mining or other remunerated work | Determine whether a taxable source exists and whether it is other-work income or enterprise profit. The authority notes mining costs often prevent a benefit; proceeds exceeding costs can require Box 1 reporting. Do not classify solely by hardware count. |
| Salary paid in crypto | Employer converts to euros at receipt; this is wage in kind. Subsequent private holdings require their own Box 3 assessment. |
| Individual enterprise paid in crypto | Convert the consideration into euro turnover; later exchange results enter profit and loss. Crypto retained as business assets is valued at cost or lower market value. Purchases belong to enterprise assets only within normal business operations; permanently surplus funds invested privately can belong in Box 3. |
| BV crypto | The BV conducts an enterprise with its whole capital, so mining and trading results sit in its profit and loss. Use corporate accounting and tax, not an individual's Box 3 allowance. Authority guidance uses cost or lower market value for crypto on the balance sheet; it does not require taxing every unrealised appreciation. |
| VAT on supplies paid in crypto | Convert payment to euros for the VAT return; payment medium does not decide the underlying supply's VAT treatment. Mining, token issuance, exchange services and complex protocols require separate VAT analysis (see `nl-vat-return`). |

Entrepreneur relief is not available merely because an activity is taxed in Box 1. Confirm income-tax entrepreneur status and each relief's conditions separately (`nl-zzp-deductions`). Genuine business assets are not also included as the same taxpayer's private Box 3 assets.

### Step 2: Value the rights actually held

For ordinary crypto holdings use economic value at **1 January, 00:00**, in euros, using the reference-date quotation of the exchange used. Retain quantity, price, euro conversion and timestamp. For self-custody, document a relevant market quotation consistently; an unrelated closing price chosen because it is lower is not a justified reference-date valuation.

For DeFi, staking, lending, liquidity pools, wrapped tokens and NFTs, first identify the asset or enforceable claim actually owned. Do not count both a receipt token and the underlying assets when they represent one economic position. Conversely, do not omit separately owned rewards or claims. A locked staking claim or a depegged wrapper is not automatically worth the unrestricted underlying token. Examine transfer restrictions, redemption terms, market transactions, recoverability and counterparty insolvency. Refer material illiquid or unique positions for a supported valuation instead of inventing a universal discount or floor-price rule.

Passive staking or lending does not automatically become a business; paid validator services, professional creation and other work may change classification. An airdrop is not automatically either tax-free or enterprise income: establish why it was received and any work or consideration. Investment NFTs, NFTs linked to services and personal-use rights may need different legal classification. This guide provides the intake and valuation process; it does not assert a tax ruling for every protocol or NFT.

Under the ordinary Box 3 method an individual trading cost-basis convention is not the tax base. Actual return needs annual flows and values. Business cost and recognition policies must follow the applicable accounting rules; do not impose a universal FIFO or average-cost election from this guide.

### Step 3: Ordinary Box 3 method (Wet IB 2001 art. 5.2)

The method concerns ordinary taxable categories, after checking ownership, exemptions and classification. Crypto is an investment or other asset, including a stablecoin merely intended to track a currency; do not label a token as a bank deposit without establishing the legal nature of the holding (art. 5.2(3) lists what counts as a bank balance).

Let B be bank balances, O investments and other taxable assets, D qualifying debts, T the debt threshold and H the appropriate tax-free allowance. Apply any reference-date anti-arbitrage adjustment first (Step 5).

1. Deductible debt A = max(D minus T, nil).
2. Net asset base R = max(B + O minus A, nil).
3. Taxable base G = max(R minus H, nil).
4. Aggregate deemed return F = max(B x bank rate + O x investment rate minus A x debt rate, nil). Article 5.2(2) requires this nil floor even if R is positive.
5. If R or G is nil, ordinary Box 3 income is nil. Otherwise ordinary income = F x G / R. Keep precision through this ratio and reconcile the return's rounding (the Belastingdienst's own examples round the G / R percentage to two decimals).
6. Allocate a fiscal partnership's taxable base consistently with the return (any split that totals 100% is allowed), calculate each person's income and apply the 36% rate. The actual-return allocation must follow the same allocation (art. 5.25(4)); do not independently assign losses for a better result.

The tax-free allowance is not a universal threshold below which assets never need reporting. The return asks for assets for income-dependent schemes at the lower reporting limits in the table. Follow the return questions and filing notice even if the calculation yields no Box 3 tax.

### Step 4: Actual-return comparison (tegenbewijsregeling, art. 5.25 to 5.36)

Compute the entire relevant Box 3 portfolio, including assets acquired during the year, not just the losing crypto position. Actual return is the total of regular benefits (interest, rent, dividends and similar, art. 5.27) and value changes (vermogensaanwas, art. 5.28) of all Box 3 assets and debts (art. 5.26). The basic crypto reconciliation for ordinary purchases and sales, as the Belastingdienst gives it:

**Closing value minus opening value minus purchases plus sales**, with all values in euros.

Record swaps as a disposal and acquisition at supported euro values, so the portfolio reconciliation remains complete. Own-wallet transfers do not generate an external purchase or sale. Check rewards, gifts, inheritances, service receipts and other non-purchase movements separately so that income and capital movements are neither omitted nor double counted. Complex protocol rewards or transfers require a documented classification before finalising the formula.

Add the return on other Box 3 assets and subtract interest paid on Box 3 debts (negative regular benefits). Costs such as trading fees are not deductible under the actual-return method; the Belastingdienst names two exceptions only (debt interest, and an investment in a second home that raised its WOZ value). Do not net fees silently into purchases or sales. There is no tax-free asset allowance or debt threshold in this actual-return calculation, no inflation adjustment and no carry-forward of a negative annual return. A negative overall annual result is floored at nil (art. 5.25(2)).

Compare this whole-portfolio actual income, allocated correctly for partners, with **ordinary Box 3 income after the allowance ratio** (the "voordeel uit sparen en beleggen"), not with the gross deemed return F. The lower one applies, and only if the taxpayer makes the actual return plausible (art. 5.25(1)). A large crypto loss cannot be used selectively while excluding gains on other assets.

From the 2025 return the income-tax return itself asks whether to give the actual return; for crypto it asks for the 1 January and 31 December values and total purchases and sales for the year. The separate "Opgaaf werkelijk rendement" form is the route for 2024 and earlier. Older-year eligibility, assessment finality and deadlines must be checked for that taxpayer; do not promise reopening every year from 2017. For 2026 the provisional assessment always uses the deemed return; the actual return is only taken into account in the 2026 return. Keep submission evidence and reconcile the resulting assessment.

### Step 5: Reference-date transactions and losses

A temporary conversion of investments into bank balances around the reference date can be disregarded under peildatumarbitrage (art. 5.24). The rule covers a sale in the three months immediately before 1 January followed by a purchase after it, with no more than three months between sale and purchase, and temporary borrowing repaid within three months. Evidence that the transactions had business reasons (zakelijke overwegingen) switches it off. Where the rule applies, report the affected assets and debts as though the temporary transactions had not occurred, and make the matching actual-return adjustment (the Belastingdienst reduces the recorded purchases by the amount sold just before 1 January). Do not recommend a December sale and January repurchase as automatically effective planning. Transfers between tax boxes require their own anti-abuse assessment.

Selling all crypto does not remove the proceeds from wealth: retained bank balances or other assets still enter the next relevant calculation. An exchange bankruptcy does not automatically make a recoverable claim worthless. Determine economic value, evidence and timing.

A negative overall Box 3 actual return gives no cross-year loss carry-forward. For a Box 1 enterprise loss, first offset positive Box 1 income in the same year. A remaining assessed Box 1 loss is offset against the **three preceding years**, then the **nine following years**, in the mandatory order. It cannot offset Box 2 or Box 3 income. Obtain and reconcile the loss determination; corporate loss rules do not apply to this individual calculation.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Deductible debt exceeds assets | Stop at the nil net or taxable base without dividing by it. |
| Aggregate deemed return negative but taxable base positive | Apply the statutory deemed-return nil floor (art. 5.2(2)). |
| Actual-return records cover only one wallet | Do not claim that its loss eliminates the household's complete Box 3 liability. |
| Minor child holds crypto | The child's assets are added to the parent's or carer's Box 3 (art. 2.15); the parents report them. |
| Stablecoin pegged to a currency | Investment or other asset at 6.00% (2026), not a bank balance, unless the legal nature of the holding is a deposit. |
| Trading fees in the actual-return route | Not deductible. |
| Crypto held by a BV | Corporate tax; outside Box 3. |
| Dutch residence starts or ends in the year | Reference-date base, advantage time-apportioned by whole months (art. 5.2(6)); refer treaty and migration points. |
| DAC8 reports from 2026 | Crypto service providers report client and transaction data from 1 January 2026; the taxpayer's return stays the same and the report does not decide classification. |

## Worked cases

These are isolated calculations, not a complete personal tax assessment. Keep the assumptions visible.

### Case A: ordinary private holdings in 2026

Single resident, no debts or other assets: bank EUR 20,000 and crypto EUR 150,000 at 1 January 2026. Deemed return is EUR 256 + EUR 9,000 = EUR 9,256 (provisional bank rate 1.28%). Net base EUR 170,000; taxable base EUR 110,643. Ordinary income is EUR 9,256 x 110,643 / 170,000 = **EUR 6,024.19**, giving Box 3 tax of **EUR 2,168.71** before filing-system rounding. Rounding the effective return rate early would distort this result.

For the 2025 return the same holdings give EUR 274 + EUR 8,820 = EUR 9,094, taxable base EUR 112,316, income EUR 6,008.25 and tax EUR 2,162.97.

```oa-check
name: Box 3 deemed return, bank 20000 and crypto 150000, single, 2026 provisional
inputs:
  bank: 20000
  crypto: 150000
  allowance: 59357
steps:
  - deemed: bank * 0.0128 + crypto * 0.06
  - base: bank + crypto
  - taxable_base: max(base - allowance, 0)
  - income: deemed * taxable_base / base
  - tax: income * 0.36
expected:
  deemed: 9256.00
  taxable_base: 110643
  income: 6024.19
  tax: 2168.71
```

### Case B: falling portfolio, which route should she choose? (decision)

Same person and opening balances as Case A, tax year 2026. No crypto purchases, sales or rewards; closing crypto EUR 90,000 and bank interest EUR 250. Actual return is EUR 90,000 minus EUR 150,000 + EUR 250 = **minus EUR 59,750**, floored to nil. Deemed route: EUR 6,024.19 income. Actual route: EUR 0. With no other Box 3 return, she should give the actual return in the 2026 return: Box 3 income EUR 0 and tax EUR 0, against EUR 2,168.71 on the deemed route. Had the portfolio risen so that actual return exceeded EUR 6,024.19, the deemed route would stay and giving the actual return would change nothing (the lower one applies).

```oa-check
name: Actual return against deemed return, crypto fell from 150000 to 90000, 2026
inputs:
  opening_crypto: 150000
  closing_crypto: 90000
  bank_interest: 250
  deemed_income: 6024.19
steps:
  - actual_raw: closing_crypto - opening_crypto + bank_interest
  - actual: max(actual_raw, 0)
  - income_used: min(deemed_income, actual)
  - tax: income_used * 0.36
expected:
  actual_raw: -59750
  actual: 0
  income_used: 0
  tax: 0
```

### Case C: purchases and sales (the Belastingdienst's own 2025 example)

Private portfolio: 1 January value EUR 80,000, 31 December 2025 value EUR 90,000, purchases EUR 5,000, sales EUR 17,000, no other flows. Actual crypto return is EUR 90,000 minus EUR 80,000 minus EUR 5,000 + EUR 17,000 = **EUR 22,000**. This is not merely the EUR 10,000 change in the wallet balance. Combine it with all other relevant Box 3 returns before comparing methods.

### Case D: mining work, limited Box 1 rate illustration, 2026

Assume a supported taxable other-work classification, full Dutch national-insurance coverage and below AOW age throughout 2026. Revenue EUR 40,000 less **established current deductible expenses** EUR 15,000 leaves EUR 25,000 taxable Box 1 income; no other Box 1 items. This expense assumption does not authorise immediate deduction of mining equipment: capital assets require the appropriate depreciation analysis. The whole EUR 25,000 sits in the first band, so gross income tax and national insurance is EUR 25,000 x **35.75%** = **EUR 8,937.50** (2025: 35.82%, EUR 8,955), before credits and the separate income-related healthcare contribution (`nl-social-contributions`). Other-work income does not receive entrepreneur or MKB deductions. If instead the facts establish enterprise profit, determine eligible deductions before applying tax bands; use `nl-income-tax` for the final liability.

## When to refuse or refer

- Missing residence or ownership prevents a final scope conclusion.
- Missing reference-date values prevents ordinary Box 3 computation.
- Missing whole-portfolio annual records prevents a reliable actual-return comparison. Return a bounded calculation only when its assumptions are explicit; identify the exact missing evidence and its effect. Never silently value an unavailable or disputed position at nil.
- Material illiquid, locked or unique positions (NFTs, staking claims, bankrupt-exchange claims) without a supported valuation: refer for valuation.
- Mining, validator, token issuance or NFT creation at a scale that may be an enterprise: refer the Box 1 classification and the VAT analysis.
- Migration, non-residence, trusts, companies and treaty questions: refer.
- Service-provider DAC8 reporting implementation, AFM or DNB authorisation: out of scope.

## Filing and payment

In the 2025 and later return tick "Cryptobezittingen" under "Bankrekeningen en andere bezittingen" and enter the 1 January value; for 2024 and earlier returns crypto went under "Overige bezittingen", then "Andere bezittingen". Follow the annual asset, income and actual-return questions. A return's ordinary summary figures do not remove the need to retain transaction evidence. Do not substitute a generic deadline for the date on the filing invitation or an approved extension. Review the submitted return and assessment together; use the proper correction or objection route if an earlier return used the wrong method.

Keep wallet ownership and reconciliation records, exchange exports, valuations, token rights, receipts, rewards, debt agreements, interest, source versions, calculation assumptions and submission confirmations. Individuals have no legal retention duty for private records, but the Belastingdienst can raise additional assessments up to 5 years back, so government guidance recommends keeping them at least 5 years; retain relevant older evidence where assessments, foreign matters or a dispute require it. Businesses and self-employed people must keep their administration 7 years, with some records 10 years.

DAC8 requires crypto service providers to report client and transaction data to the Belastingdienst from 1 January 2026. It does not replace the taxpayer's return or automatically establish the correct tax classification. This guide does not provide a service provider's regulatory reporting implementation or AFM or DNB authorisation advice.

Return the tax year, ownership and residence scope, classification reasoning, complete asset inventory, ordinary calculation, actual-return comparison or missing evidence, partner allocation, rounding, assumptions, source URLs and required referrals. Label a partial calculation as partial and keep any provisional 2026 parameters visible. Do not present a source review as an accountant's attestation.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet inkomstenbelasting 2001, version 1 January 2026 | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-11-14. Read for art. 2.13 (36%), 5.2 (6% other assets, nil floor, partner pooling, part-year rule), 5.3(3) (EUR 3,800 / 7,600 debt threshold), 5.5 (EUR 59,357), 5.24 (reference-date arbitrage) and 5.25 to 5.34 (actual return) |
| Wet inkomstenbelasting 2001, version from 21 February 2026 | https://wetten.overheid.nl/BWBR0011353/2026-02-21 | 2026-11-14. Read for art. 5.2(2) as amended by Stcrt. 2026, 3708 (1.37% and 2.70%, retroactive to 1 January 2025) |
| Wet inkomstenbelasting 2001, 2025 version | https://wetten.overheid.nl/BWBR0011353/2025-07-01 | 2026-11-14. Read for the 2025 art. 5.2 (5.88% other assets), art. 5.5 (EUR 57,684) and the EUR 3,800 debt threshold |
| Belastingdienst, Box 3 calculation 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 | 2026-11-14. Read for the provisional 2026 percentages (1.28%, 6.00%, 2.70%), crypto as other assets, EUR 59,357 and EUR 118,714, and that the provisional assessment ignores actual return |
| Belastingdienst, Box 3 final percentages per year | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/ | 2026-11-14. Read for the 2025 percentages 1.37%, 5.88% and 2.70% and the Overbruggingswet history |
| Belastingdienst, crypto in the return | https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/aangifte-doen-en-belasting-betalen-met-cryptos | 2026-11-14. Read for the 1 January 00:00 exchange-rate valuation, the return field, the 2026 and 2025 reporting limits (EUR 38,479 / 76,958 and EUR 37,395 / 74,790), the crypto actual-return inputs and minors |
| Belastingdienst, cryptovaluta situations | https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/cryptovaluta | 2026-11-14. Read for the classification of private holding, mining, wages in crypto, enterprise and BV receipts, VAT conversion and DAC8 from 1 January 2026 |
| Belastingdienst, actual-return examples | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/rekenvoorbeelden-berekening-werkelijk-rendement | 2026-11-14. Read for the crypto-only example (EUR 80,000 to 90,000, EUR 22,000) and the debt-interest treatment |
| Belastingdienst, 2025 tax calculation (fiscal information) | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening | 2026-11-14. Read for the actual-return rules: no allowance, nil floor, no carry-forward, costs not deductible with two exceptions, new Box 3 law probably 2028 |
| Belastingdienst, 2026 tax calculation (fiscal information) | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening | 2026-11-14. Read for the 2026 actual-return section |
| Belastingdienst, temporary moves around the reference date (2025) | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/regels_voor_het_tijdelijk_verplaatsen_van_bezittingen_en_schulden | 2026-11-14. Read for the 3-month peildatumarbitrage conditions and the actual-return purchase adjustment |
| Belastingdienst, loss from an enterprise | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/verlies_uit_onderneming | 2026-11-14. Read for Box 1 loss relief 3 years back and 9 forward, mandatory order, no Box 2 or 3 offset |
| Belastingdienst, Box 1 rates | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/ | 2026-11-14. Read for the 2026 first band 35.75% to EUR 38,883 and the 2025 first band 35.82% to EUR 38,441 |
| Rijksoverheid, how long to keep records | https://www.rijksoverheid.nl/vraag-en-antwoord/inkomstenbelasting/hoe-lang-moet-ik-mijn-financiele-administratie-bewaren | 2026-11-14. Read for no private retention duty, 5-year advice, 7 to 10 years for businesses |

Not yet confirmed: the final 2026 bank-balance percentage (published after the year; 1.28% is provisional) and whether the final 2026 debt percentage stays at 2.70%; protocol-specific treatment of staking rewards, airdrops, wrapped tokens and NFTs (no official page read sets a rule for each).
