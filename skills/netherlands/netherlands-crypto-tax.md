---
name: netherlands-crypto-tax
description: Use this skill whenever asked about Netherlands cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Netherlands", "Bitcoin Netherlands", "crypto belasting", "Box 3 crypto", "vermogensrendementsheffing crypto", "cryptocurrency Netherlands", "crypto income Netherlands", "staking Netherlands", "mining income Netherlands", "NFT tax Netherlands", "Belastingdienst crypto", "Dutch crypto tax", "fictief rendement crypto", "heffingsvrij vermogen", "Overbruggingswet box 3", "Binance Netherlands tax", "Coinbase Netherlands tax", "aangifte crypto", or any question about the income tax, wealth tax, or VAT treatment of cryptocurrency, tokens, or digital assets for Dutch tax residents or Netherlands-source crypto income. Covers Box 3 wealth taxation, the deemed-return system, the actual-return counter-evidence route, Box 1 business classification, and DAC8 reporting. ALWAYS read this skill before touching any Netherlands crypto work.
version: 2.1
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-27
type: situation-rules
depends_on:
  - nl-income-tax
category: crypto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
---

# Netherlands crypto and digital assets: classification, valuation and income tax

Tax year 2026 estimates, with the 2025 return shown separately. The 2026 bank and debt percentages remain provisional.

## Scope

Use this method for an individual's Dutch crypto tax classification and the crypto component of a complete income-tax return. It covers tax year 2026 (provisional assessment and planning) and the 2025 return, each labelled. It also identifies payroll, business, VAT and company branches that require their own return method. Establish residence, ownership and the tax year before calculating. Migration, non-residence, trusts, companies and treaty questions require a specific scope decision; a Dutch exchange account alone does not establish Dutch taxing rights.

Private investment crypto normally belongs to Box 3. The ordinary method uses prescribed returns on reference-date assets (Wet IB 2001 art. 5.2), but the actual-return route (tegenbewijsregeling, Wet IB 2001 art. 5.25 to 5.36) includes annual income and value changes, including unrealised changes. Therefore neither "all gains are exempt" nor "only the January value ever matters" is an adequate instruction. Do not apply announced future Box 3 legislation to these years. Recheck enacted rules before extending this method to another year.

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
| Deemed return, bank balances | 1.28% provisional | 1.37% final | 2026 bank percentage is for provisional assessments only; 2025 final amendment applies retrospectively | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 ; https://zoek.officielebekendmakingen.nl/stcrt-2026-3708.html |
| Deemed return, investments and other assets | 6.00% | 5.88% | Crypto belongs here; Wet IB 2001 art. 5.2(2) | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml |
| Deemed return, debts | 2.70% provisional | 2.70% final | Apply only to deductible Box 3 debts after the threshold; final 2026 percentage set after year-end | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 ; https://zoek.officielebekendmakingen.nl/stcrt-2026-3708.html |
| Tax-free assets, individual | EUR 59,357 | EUR 57,684 | Wet IB 2001 art. 5.5; ordinary method only | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml |
| Tax-free assets, qualifying fiscal partners together | EUR 118,714 | EUR 115,368 | Computed: twice individual allowance; whole-year partnership/election, art. 5.2(5) | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml |
| Debt threshold, individual | EUR 3,800 | EUR 3,800 | Only otherwise eligible debts above threshold, art. 5.3(3)(f) | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml |
| Debt threshold, qualifying fiscal partners together | EUR 7,600 | EUR 7,600 | Whole-year partnership/election, art. 5.3(3)(f) | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml |
| Box 3 tax rate | 36% | 36% | On taxable Box 3 income; art. 2.13 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml |
| Assets reporting limit for income-dependent schemes, no partner | EUR 38,479 | EUR 37,395 | Net Box 3 wealth above this must be reported, even if no Box 3 tax is due | https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/aangifte-doen-en-belasting-betalen-met-cryptos |
| Same reporting limit, with fiscal partner | EUR 76,958 | EUR 74,790 | Reporting limit, not a tax-free allowance | same |
| Box 1 first band, below AOW age and fully insured | 35.75% to EUR 38,883 | 35.82% to EUR 38,441 | Combined tax and national insurance; mining illustration only | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1 |
| Reference-date arbitrage window | 3 months | 3 months | A continuous period straddling 1 January; statutory asset/debt movements and business-reasons exception, art. 5.24 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml |
| Ordinary Box 1 loss carry-back / forward | 3 / 9 years | 3 / 9 years | Oldest first; special cases require the referral below, art. 3.150 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml |

The pooled fiscal-partner allowance, debt threshold and allocation apply only to qualifying whole-year partners or partners eligible for and making the whole-year election. Establish that status before pooling; otherwise use the individual and part-year rules (art. 5.2(6) time-apportions the advantage where Dutch residence starts or ends during the year).

The 2026 bank and debt percentages are provisional-assessment parameters, not final annual rates. The current 2026 statute reads 1.37% and 2.70% following the retrospective 2025 amendment in Stcrt. 2026, 3708; the Belastingdienst uses 1.28% and 2.70% for provisional 2026 assessments. Preserve that status in every estimate.

## The method, step by step

### Step 1: Classify before calculating

| Situation | Method and decision |
|---|---|
| Private investment and speculative trading | Normally Box 3. The Belastingdienst compares crypto trading to trading ordinary currencies; it changes only where extra work beyond investment activities regularly produces additional income. |
| Mining or other remunerated work | Determine whether a taxable source exists and whether it is other-work income or enterprise profit. The authority notes mining costs often prevent a benefit; proceeds exceeding costs can require Box 1 reporting. Do not classify solely by hardware count. |
| Salary paid in crypto | Employer converts to euros at receipt; this is wage in kind. Subsequent private holdings require their own Box 3 assessment. |
| Individual enterprise paid in crypto | Convert the consideration into euro turnover; later exchange results enter profit and loss. Crypto retained as business assets is valued at cost or lower market value. Purchases belong to enterprise assets only within normal business operations; permanently surplus funds invested privately can belong in Box 3. |
| BV crypto | The BV conducts an enterprise with its whole capital, so mining and trading results sit in its profit and loss. Use corporate accounting and tax, not an individual's Box 3 allowance. Authority guidance uses cost or lower market value for crypto on the balance sheet; it does not require taxing every unrealised appreciation. |
| VAT on supplies paid in crypto | Convert payment to euros for the VAT return; payment medium does not decide the underlying supply's VAT treatment. Mining, token issuance, exchange services and complex protocols require separate VAT analysis (see `nl-vat-return`). |

Entrepreneur relief is not available merely because an activity is taxed in Box 1. Confirm income-tax entrepreneur status and each relief's conditions separately (`nl-zzp-deductions`). Assets generating Box 1 or Box 2 income are normally excluded from Box 3 (art. 2.14(2)); temporary transfers between boxes, non-reportable structures and the general fraus-legis doctrine require separate anti-abuse analysis. Check this point with one of our partner accountants.

### Step 2: Value the rights actually held

For ordinary crypto holdings use economic value at **1 January, 00:00**, in euros, using the reference-date quotation of the exchange used. Retain quantity, price, euro conversion and timestamp. For self-custody, document a relevant market quotation consistently; an unrelated closing price chosen because it is lower is not a justified reference-date valuation.

For DeFi, staking, lending, liquidity pools, wrapped tokens, airdrops, NFTs and validator or creator rewards, identify the legal rights, consideration and work performed before classifying. Reconcile receipt tokens and underlying rights to prevent duplicate or omitted positions. Obtain terms, transfer restrictions, redemption rights, market transactions, recoverability and counterparty-insolvency evidence. Article 5.19 requires economic value, treats an economic unit as a unit and, if reference-date value cannot be determined, uses the nearest time at which it can. It does not supply a universal lock-up discount, NFT floor price or bankruptcy nil value.

Protocol-specific tax classification and unsupported valuations are non-usable holds. Check this point with one of our partner accountants. Do not finalise a return using a guessed value or classify all passive rewards as exempt or all validator work as enterprise income.

Under the ordinary Box 3 method an individual trading cost-basis convention is not the tax base. Actual return needs annual flows and values. Business cost and recognition policies must follow the applicable accounting rules; do not impose a universal FIFO or average-cost election from this guide.

### Step 3: Ordinary Box 3 method (Wet IB 2001 art. 5.2)

The method concerns ordinary taxable categories, after checking ownership, exemptions and classification. Crypto is an investment or other asset, including a stablecoin merely intended to track a currency; do not label a token as a bank deposit without establishing the legal nature of the holding (art. 5.2(3) lists what counts as a bank balance).

Let B be bank balances, O investments and other taxable assets, D qualifying debts, T the debt threshold and H the appropriate tax-free allowance. Apply any reference-date anti-arbitrage adjustment first (Step 5).

1. Deductible debt A = max(D minus T, nil).
2. Net asset base R = max(B + O minus A, nil).
3. Taxable base G = max(R minus H, nil).
4. Aggregate deemed return F = max(B x bank rate + O x investment rate minus A x debt rate, nil). Article 5.2(2) requires this nil floor even if R is positive.
5. If R or G is nil, ordinary Box 3 income is nil. Otherwise ordinary income = F x G / R. Keep precision through this statutory ratio; the annual return controls its rounding. The authority’s 2026 page gives differing rounding instructions, so the unrounded examples below are estimates rather than a filing-system result.
6. Allocate a fiscal partnership's taxable base consistently with the return (any split that totals 100% is allowed), calculate each person's benefit, then deduct any remaining eligible personal deductions (arts. 5.1 and 6.2), floored at nil, before applying the 36% rate. The actual-return allocation must follow the same allocation (art. 5.25(4)); do not independently assign losses for a better result.

The tax-free allowance is not a universal threshold below which assets never need reporting. The return asks for assets for income-dependent schemes at the lower reporting limits in the table. Follow the return questions and filing notice even if the calculation yields no Box 3 tax.

### Step 4: Actual-return comparison (tegenbewijsregeling, art. 5.25 to 5.36)

Compute the entire relevant Box 3 portfolio, including assets acquired during the year, not just the losing crypto position. Actual return is the total of regular benefits (interest, rent, dividends and similar, art. 5.27) and value changes (vermogensaanwas, art. 5.28) of the relevant Box 3 assets and debts (art. 5.26). Do not copy the ordinary exemption list mechanically: art. 5.26(3) disapplies the debt threshold and specified exemptions, while art. 5.32 separately regulates green investments. For portfolios with property, green investments, usufruct rights, exempt family claims, net pensions or net annuities, this crypto reconciliation is insufficient: Check this point with one of our partner accountants. Hold the whole-portfolio comparison until those components are resolved. For plain investment crypto with ordinary purchases and sales and no rewards or other flows, the Belastingdienst reconciliation is:

**Closing value minus opening value minus purchases plus sales**, with all values in euros.

Reconcile euro-valued swaps on both sides; transfers between the same owner’s wallets are internal movements, not external purchases or sales. Identify gifts, inheritances, rewards and service receipts separately as income or capital movements (arts. 5.27 to 5.30). For unresolved protocol rewards or non-purchase transfers: Check this point with one of our partner accountants. Do not use the purchases-and-sales formula as a complete answer for those unresolved events.

Add regular income not already counted in value changes. Recognise regular benefits when received, set off, made available, interest-bearing, or due and collectible; negative regular benefits when paid, set off, made available or interest-bearing (art. 5.34). Deduct qualifying Box 3 debt interest as a negative regular benefit (art. 5.27(2)); do not deduct loan principal as an expense. Non-arm’s-length contracts require arm’s-length regular benefits under art. 5.27(3); unresolved contracts hold the complete comparison. Check this point with one of our partner accountants. Costs such as trading fees are not deductible under the actual-return method; debt interest is treated separately, and housing improvements have their own valuation adjustment under art. 5.31, requiring the property referral above. Do not net fees silently into purchases or sales. There is no tax-free asset allowance or debt threshold in this actual-return calculation, no inflation adjustment and no carry-forward of a negative annual return. A negative overall annual result is floored at nil (art. 5.25(2)). These are nominal euro returns; do not deduct inflation from the statutory calculation.

Compare this whole-portfolio actual income, allocated correctly for partners, with **ordinary Box 3 income after the allowance ratio** (the "voordeel uit sparen en beleggen"), not with the gross deemed return F. The lower one applies only if the taxpayer makes the actual return plausible; then deduct any remaining personal deduction, floored at nil (art. 5.25(1), art. 6.2). A large crypto loss cannot be used selectively while excluding gains on other assets.

From the 2025 return the income-tax return itself asks whether to give the actual return; for crypto it asks for the 1 January and 31 December values and total purchases and sales for the year. The separate "Opgaaf werkelijk rendement" form is the route for 2024 and earlier. Older-year eligibility, assessment finality and deadlines are non-usable holds: Check this point with one of our partner accountants. Do not promise reopening every year from 2017. For 2026 the provisional assessment always uses the deemed return; the actual return is only taken into account in the 2026 return. Under art. 5.25(6) to (8), use the inspector’s form unless the data is requested within the return invitation; the separate form allows further documents within six weeks after sending. Keep submission evidence and reconcile the resulting assessment.

### Step 5: Reference-date transactions and losses

Under art. 5.24, transactions can be disregarded where, within a continuous three-month period starting before and ending after 1 January, the taxpayer’s actions temporarily reduce other assets and increase bank balances at the reference date, followed by the corresponding reversal after it. Temporary increases in debts followed by a decrease within such a period are also covered. Evidence that the transactions had business reasons (zakelijke overwegingen) switches it off. Where the rule applies, report the affected assets and debts as though the temporary transactions had not occurred, and make the matching actual-return adjustment (the Belastingdienst’s 2025 instructions reduce recorded purchases by the smaller affected sale/repurchase amount). Do not recommend a December sale and January repurchase as automatically effective planning. Transfers between tax boxes require their own anti-abuse assessment.

Selling all crypto does not remove the proceeds from wealth: retained bank balances or other assets still enter the next relevant calculation. An exchange bankruptcy does not automatically make a recoverable claim worthless. Determine economic value, evidence and timing.

A negative overall Box 3 actual return gives no cross-year loss carry-forward. For a Box 1 enterprise loss, first offset positive Box 1 income in the same year. For the ordinary individual case, a remaining assessed Box 1 loss is offset against the **three preceding years**, then the **nine following years**, in the mandatory order. It cannot offset Box 2 or Box 3 income. Obtain and reconcile the loss determination. Special conscientious-objection, death/partner and corporate-conversion loss rules under art. 3.150(3) to (7): Check this point with one of our partner accountants. Corporate loss rules do not apply to this individual calculation.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Deductible debt exceeds assets | Stop at the nil net or taxable base without dividing by it. |
| Aggregate deemed return negative but taxable base positive | Apply the statutory deemed-return nil floor (art. 5.2(2)). |
| Actual-return records cover only one wallet | Do not claim that its loss eliminates the household's complete Box 3 liability. |
| Minor child holds crypto | Attribute to the parent exercising authority; where multiple parents exercise authority, equal shares. Art. 2.15(3) additionally equates the specified sole parent whose authority was terminated under BW1:266; actual return follows the same attribution (art. 5.25(3)). Other guardianship cases: Check this point with one of our partner accountants. |
| Stablecoin pegged to a currency | Investment or other asset at 6.00% (2026), not a bank balance, unless the legal nature of the holding is a deposit. |
| Crypto falls 50% during 2025 | The ordinary reference-date calculation is unchanged; include the annual fall in the complete actual-return comparison. |
| Trading fees in the actual-return route | Not deductible. |
| Crypto held by a BV | Corporate tax; outside Box 3. |
| Dutch residence starts or ends in the year | Reference-date base, advantage time-apportioned by whole months (art. 5.2(6)); refer treaty and migration points. |
| DAC8 data collection from 2026 | Covered providers collect data from 1 January 2026 and first report it by 31 January 2027; the taxpayer’s tax treatment does not change. See filing below. |

## Worked cases

These are isolated calculations, not a complete personal tax assessment. Keep the assumptions visible.

### Case A: ordinary private holdings in 2026

Single whole-year resident, no remaining personal deduction, debts or other assets: bank EUR 20,000 and crypto EUR 150,000 at 1 January 2026. Deemed return is EUR 256 + EUR 9,000 = EUR 9,256 (provisional bank rate 1.28%). Net base EUR 170,000; taxable base EUR 110,643. Ordinary income is EUR 9,256 x 110,643 / 170,000 = **EUR 6,024.19**, giving Box 3 tax of **EUR 2,168.71** before filing-system rounding. Rounding the effective return rate early would distort this result.

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

Same person and opening balances as Case A, tax year 2026. No crypto purchases, sales or rewards; closing crypto EUR 90,000 and bank interest EUR 250. Actual return is EUR 90,000 minus EUR 150,000 + EUR 250 = **minus EUR 59,750**, floored to nil. Deemed route: EUR 6,024.19 income. The original 2025 case has the same EUR 59,750 loss, nil actual income and tax, versus EUR 6,008.25 deemed income and EUR 2,162.97 tax. Actual route: EUR 0. With no other Box 3 return, she should give the actual return in the 2026 return: Box 3 income EUR 0 and tax EUR 0, against EUR 2,168.71 on the deemed route. Had the portfolio risen so that actual return exceeded EUR 6,024.19, the deemed route would stay and giving the actual return would change nothing (the lower one applies).

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

The historical 2025 mining case specified **20 GPUs, dedicated premises, regular mining income, EUR 40,000 revenue, EUR 15,000 electricity and hardware costs, and no other employment**. Those facts alone do not establish enterprise status or immediate deduction of all hardware expenditure. Check this point with one of our partner accountants. Preserve the EUR 15,000 as reported costs pending classification and depreciation; the EUR 25,000 taxable illustration and EUR 8,955 gross 2025 levy apply only if the whole EUR 15,000 is established as currently deductible. The former 36.97% / EUR 9,242.50 result used the wrong year’s rate. Full higher-band computations, credits and any relief remain with `nl-income-tax`.

## When to refuse or refer

- Missing residence or ownership prevents a final scope conclusion.
- Missing reference-date values prevents ordinary Box 3 computation.
- Missing whole-portfolio annual records prevents a reliable actual-return comparison. Return a bounded calculation only when its assumptions are explicit; identify the exact missing evidence and its effect. Never silently value an unavailable or disputed position at nil.
- Material illiquid, locked or unique positions without supported valuation: Check this point with one of our partner accountants.
- Unresolved mining/validator/creator enterprise classification and VAT on mining, token issuance, exchange services or protocols: Check this point with one of our partner accountants.
- Migration, non-residence, trusts, companies and treaty questions beyond the basic classification table: Check this point with one of our partner accountants.
- Service-provider DAC8 implementation, nexus and authorisation: Check this point with one of our partner accountants.

## Filing and payment

In the 2025 and later return tick "Cryptobezittingen" under "Bankrekeningen en andere bezittingen" and enter the 1 January value; for 2024 and earlier returns crypto went under "Overige bezittingen", then "Andere bezittingen". Follow the annual asset, income and actual-return questions. A return's ordinary summary figures do not remove the need to retain transaction evidence. Do not substitute a generic deadline for the date on the filing invitation or an approved extension. Review the submitted return and assessment together; use the proper correction or objection route if an earlier return used the wrong method.

Keep wallet ownership and reconciliation records, exchange exports, valuations, token rights, receipts, rewards, debt agreements, interest, source versions, calculation assumptions and submission confirmations. Individuals have no legal retention duty for private records; government guidance recommends keeping them at least 5 years for possible additional assessments; retain relevant older evidence where assessments, foreign matters or a dispute require it. Businesses and self-employed people must keep their administration 7 years, with some records 10 years.

DAC8 providers and reportable users are defined in WIB art. 2f. Dutch reporting depends on arts. 10ob to 10oc, including AFM-licensed or Article 60-notified providers, other Dutch nexus and branch cases, with reporting-elsewhere exceptions. The rules can reach relevant transfers and controlling persons as well as exchanges. Covered providers collect client and transaction data from 1 January 2026 and first report by 31 January 2027, then annually by 31 January (Stb. 2026, 79, art. I and V; WIB art. 10ob(12)). For users the tax treatment is unchanged: reporting does not itself establish tax due or replace their return. Provider implementation, registration, detailed user/asset exclusions, CARF treaties and AFM/DNB authorisation are non-usable holds. Check this point with one of our partner accountants.

Return the tax year, ownership and residence scope, classification reasoning, complete asset inventory, ordinary calculation, actual-return comparison or missing evidence, partner allocation, rounding, assumptions, source URLs and required referrals. Label a partial calculation as partial and keep any provisional 2026 parameters visible. Do not present a source review as an accountant's attestation.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet IB 2001, current 2026 edition | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml | 2026-11-27. Read for arts. 2.13 to 2.15, 3.30, 3.79a, 3.90, 3.94, 3.95, 3.150, 5.1, 5.2, 5.3, 5.5, 5.19, 5.24 to 5.34 and 6.2; operative conditions and adjacent exceptions |
| Wet IB 2001, 2025 edition with later retrospective amendments | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2025-08-25_2/xml/BWBR0011353_2025-08-25_2.xml | 2026-11-27. Read for arts. 2.10, 2.13, 5.2, 5.3, 5.5, 5.25 and comparison with 2026 actual-return rules; original bank/debt figures require the final amendment below |
| Final 2025 percentages, Stcrt. 2026, 3708 | https://zoek.officielebekendmakingen.nl/stcrt-2026-3708.html | 2026-11-27. Read for arts. I and V(a), 1.37% and 2.70% retrospective to 1 January 2025 |
| Belastingdienst, 2026 provisional calculation | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 | 2026-11-27. Read for provisional percentages, allowances, asset categories, rounding and actual-return adjustment in annual return |
| Belastingdienst, 2025 calculation | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2025 | 2026-11-27. Read for final parameters, partner allocation, annual return and rounding |
| Belastingdienst, crypto reporting and valuation | https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/aangifte-doen-en-belasting-betalen-met-cryptos | 2026-11-27. Read for reporting limits, fields, 1 January 00:00 value, annual actual-return data; minors qualified by statute above |
| Belastingdienst, crypto classifications | https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/cryptovaluta | 2026-11-27. Read for private trading/mining, wages, individual enterprise, BV and VAT conversion |
| Belastingdienst, actual-return examples | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/rekenvoorbeelden-berekening-werkelijk-rendement | 2026-11-27. Read for crypto EUR 80,000 / 90,000 / 5,000 / 17,000 example and partner comparison |
| Belastingdienst, actual-return filing routes | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/wat-is-mijn-werkelijk-rendement | 2026-11-27. Read for annual-return route from 2025, older OWR route, complete annual return and costs |
| Belastingdienst, 2026 fiscal information | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening | 2026-11-27. Read for actual-return whole-portfolio rules, nil floor, no carry-forward, costs and personal deduction |
| Belastingdienst, 2025 reference-date arbitrage | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/regels_voor_het_tijdelijk_verplaatsen_van_bezittingen_en_schulden | 2026-11-27. Read for sale/repurchase, temporary borrowing and actual-return purchase adjustment |
| Belastingdienst, Box 1 rates | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1 | 2026-11-27. Read for fully insured below-AOW 2025 and 2026 first bands |
| Rijksoverheid, records retention | https://www.rijksoverheid.nl/vraag-en-antwoord/inkomstenbelasting/hoe-lang-moet-ik-mijn-financiele-administratie-bewaren | 2026-11-27. Read for no private duty, 5-year recommendation and business 7/10-year guidance |
| Enacted DAC8 implementation | https://zoek.officielebekendmakingen.nl/stb-2026-79.html | 2026-11-27. Read for art. I definitions (WIB art. 2f), reporting/nexus and exceptions (10ob to 10oc), annual 31 January deadline (10ob(12)), and art. V retrospective effect |
| Belastingdienst, DAC8/CARF | https://www.belastingdienst.nl/wps/wcm/connect/nl/ondernemers/content/wet-implementatie-eu-richtlijn-gegevensuitwisseling-cryptoactiva | 2026-11-27. Read for covered providers/users, 2026 collection, first reporting 31 January 2027, licensing/nexus and unchanged user taxation |

Not yet confirmed: final 2026 bank/debt percentages are not available for final-return use here; protocol-specific staking, airdrops, wrapped tokens, DeFi and NFT outcomes or illiquid valuations; property/green-investment/usufruct/net-pension components of a complete actual-return portfolio; older-year reopening; historical 2028 reform forecasts (approximately EUR 1,800 income exemption and a 36% rate) are not usable as enacted law; full higher-band calculations (historical 2025 top-rate reference: 49.50%) require the income-tax method; unusual loss/guardianship/migration/treaty cases; provider DAC8/authorisation implementation. These are non-usable holds: Check this point with one of our partner accountants. Preserve the original facts and year while obtaining that determination.
