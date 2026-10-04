---
name: netherlands-crypto-tax
description: Use this skill whenever asked about Netherlands cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Netherlands", "Bitcoin Netherlands", "crypto belasting", "Box 3 crypto", "vermogensrendementsheffing crypto", "cryptocurrency Netherlands", "crypto income Netherlands", "staking Netherlands", "mining income Netherlands", "NFT tax Netherlands", "Belastingdienst crypto", "Dutch crypto tax", "fictief rendement crypto", "heffingsvrij vermogen", "Overbruggingswet box 3", "Binance Netherlands tax", "Coinbase Netherlands tax", "aangifte crypto", or any question about the income tax, wealth tax, or VAT treatment of cryptocurrency, tokens, or digital assets for Dutch tax residents or Netherlands-source crypto income. Covers Box 3 wealth taxation, fictional return system, actual return counter-evidence, Box 1 business classification, and DAC8 reporting. ALWAYS read this skill before touching any Netherlands crypto work.
version: 1.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-09-28
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - netherlands-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands crypto and digital assets: classification, valuation and income tax

Tax year: 2026 estimates; 2025 returns.

## Scope and period

Use this method for an individual's Dutch crypto tax classification and the crypto component of a complete income-tax return. It covers the 2025 return and separately labelled 2026 estimates. It also identifies payroll, business, VAT and company branches that require their own return method. Establish residence, ownership and the tax year before calculating. Migration, non-residence, trusts, companies and treaty questions require a specific scope decision; a Dutch exchange account alone does not establish Dutch taxing rights.

Private investment crypto normally belongs to Box 3. The ordinary method uses prescribed returns on reference-date assets, but the actual-return alternative includes annual income and value changes, including unrealised changes. Therefore neither “all gains are exempt” nor “only the January value ever matters” is an adequate instruction. Do not apply announced future Box 3 legislation to these years. Recheck enacted rules before extending this method to another year.

Sources: [crypto classifications](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/cryptovaluta), [2025 tax calculation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening), [2026 tax calculation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening).

## Ask the client first

Collect the following before producing a filing-ready result:

- Tax year, residence periods, age, fiscal-partner status and allocation, beneficial owner, minor-child holdings, employment and business connections.
- Every exchange, wallet, custodian and protocol; token quantities, legal rights and obligations, euro values on the reference date, and evidence of the pricing source and time. Include locked, lent, wrapped and collateralised positions, debts and bankruptcy claims.
- All other Box 3 assets and debts, exemptions and debt classification. A crypto-only total cannot calculate the taxpayer's overall Box 3 liability.
- For actual return: opening and closing values, purchases, sales, swaps, rewards, income, gifts/inheritances, transfers and debt interest throughout the year. Reconcile external cash movements and remove transfers between the same owner's wallets from purchases and sales.
- For mining, trading services, validators or NFT creation: what work was done, its economic purpose, expected and actual benefits, costs, organisation, contracts and whether the activity exceeds ordinary investment management. For employment or business receipts, record euro value at the relevant receipt or revenue recognition point.
- Existing return, assessment, actual-return request and any applicable filing deadline or extension.

## When to refuse or refer

- Missing residence/ownership prevents a final scope conclusion. 
- Missing reference-date values prevents ordinary Box 3 computation. 
- Missing whole-portfolio annual records prevents a reliable actual-return comparison. Return a bounded calculation only when its assumptions are explicit; identify the exact missing evidence and its effect. Never silently value an unavailable or disputed position at nil.

Source: [crypto return instructions](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/aangifte-doen-en-belasting-betalen-met-cryptos).

## Classify before calculating

| Situation | Method and decision |
|---|---|
| Private investment and speculative trading | Normally Box 3. Frequency, a trading bot, leverage or time spent does not by itself establish Box 1. Investigate whether extra work beyond investment activities regularly produces additional income. |
| Mining or other remunerated work | Determine whether a taxable source exists and whether it is other-work income or enterprise profit. The authority notes mining costs often prevent a benefit; proceeds exceeding costs can require Box 1 reporting. Do not classify solely by hardware count. |
| Salary paid in crypto | Employer converts to euros at receipt; this is wage in kind. Subsequent private holdings require their own Box 3 assessment. |
| Individual enterprise paid in crypto | Convert the consideration into euro turnover; later exchange results enter profit and loss. Crypto retained as business assets is valued at cost or lower market value. Purchases belong to enterprise assets only within normal business operations; permanently surplus funds invested privately can belong in Box 3. |
| BV crypto | The BV conducts an enterprise with its assets. Use corporate accounting and tax, not an individual's Box 3 allowance. Authority guidance uses cost or lower market value for crypto on the balance sheet; it does not require taxing every unrealised appreciation. |
| VAT on supplies paid in crypto | Convert payment to euros for the VAT return; payment medium does not decide the underlying supply's VAT treatment. Mining, token issuance, exchange services and complex protocols require separate VAT analysis. |

Entrepreneur relief is not available merely because an activity is taxed in Box 1. Confirm income-tax entrepreneur status and each relief's conditions separately. Genuine business assets are not also included as the same taxpayer's private Box 3 assets.

Source: [Belastingdienst crypto situation guide](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/cryptovaluta).

## Value the rights actually held

For ordinary crypto holdings use economic value at **1 January, 00:00**, in euros, using the reference-date quotation of the exchange used. Retain quantity, price, euro conversion and timestamp. For self-custody, document a relevant market quotation consistently; an unrelated closing price chosen because it is lower is not a justified reference-date valuation.

For DeFi, staking, lending, liquidity pools, wrapped tokens and NFTs, first identify the asset or enforceable claim actually owned. Do not count both a receipt token and the underlying assets when they represent one economic position. Conversely, do not omit separately owned rewards or claims. A locked staking claim or a depegged wrapper is not automatically worth the unrestricted underlying token. Examine transfer restrictions, redemption terms, market transactions, recoverability and counterparty insolvency. Refer material illiquid or unique positions for a supported valuation instead of inventing a universal discount or floor-price rule.

Passive staking or lending does not automatically become a business; paid validator services, professional creation and other work may change classification. An airdrop is not automatically either tax-free or enterprise income: establish why it was received and any work or consideration. Investment NFTs, NFTs linked to services and personal-use rights may need different legal classification. This guide provides the intake and valuation process; it does not assert a tax ruling for every protocol or NFT.

Under the ordinary Box 3 method an individual trading cost-basis convention is not the tax base. Actual return needs annual flows and values. Business cost and recognition policies must follow the applicable accounting rules; do not impose a universal FIFO or average-cost election from this guide.

Sources: [valuation and classification](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/cryptovaluta), [reference-date instructions](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/aangifte-doen-en-belasting-betalen-met-cryptos).

## The method, step by step

### Ordinary Box 3 method

The table concerns ordinary taxable categories, after checking ownership, exemptions and classification. Crypto is an investment/other asset, including a stablecoin merely intended to track a currency; do not label a token as a bank deposit without establishing the legal nature of the holding.

| Parameter | 2025 return | 2026 estimate |
|---|---:|---:|
| Bank return | 1.37% | 1.28% provisional |
| Investments/other assets return | 5.88% | 6.00% |
| Debt return | 2.70% | 2.70% provisional |
| Tax-free assets, individual | €57,684 | €59,357 |
| Tax-free assets, fiscal partners together | €115,368 | €118,714 |
| Debt threshold, individual | €3,800 | €3,800 |
| Debt threshold, fiscal partners together | €7,600 | €7,600 |
| Box 3 tax rate | 36% | 36% |
| Official sources | [2025 parameters](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/bezittingen_en_schulden_box_3_) and [final rates](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/) | [2026 parameters](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026) |

The pooled fiscal-partner allowance, debt threshold and allocation below apply only to qualifying whole-year partners or partners eligible for and making the whole-year election. Establish that status before pooling; otherwise use the applicable individual/part-year rules.

The 2026 bank/debt percentages are provisional-assessment parameters, not final annual rates. Preserve that status in every estimate.

Let B be bank balances, O investments/other taxable assets, D qualifying debts, T the debt threshold and H the appropriate tax-free allowance. Apply any reference-date anti-arbitrage adjustment first.

1. Deductible debt A = max(D − T, nil).
2. Net asset base R = max(B + O − A, nil).
3. Taxable base G = max(R − H, nil).
4. Aggregate deemed return F = max(B × bank rate + O × investment rate − A × debt rate, nil). Article 5.2 requires this nil floor even if R is positive.
5. If R or G is nil, ordinary Box 3 income is nil. Otherwise ordinary income = F × G / R. Keep precision through this ratio and reconcile the return's rounding.
6. Allocate a fiscal partnership's taxable base consistently with the return, calculate each person's income and apply the tax rate. The actual-return allocation must follow the applicable same allocation; do not independently assign losses for a better result.

The tax-free allowance is not a universal threshold below which assets never need reporting. The return asks for assets for income-dependent schemes at lower limits. Follow the return questions and filing notice even if the calculation yields no Box 3 tax.

Sources: [historical final rates](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/), [2025 assets/debts](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/bezittingen_en_schulden_box_3_), [2026 calculation and provisional status](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026), [Wet IB article 5.2](https://wetten.overheid.nl/BWBR0011353).

## Actual-return comparison

Compute the entire relevant Box 3 portfolio, including assets acquired during the year, not just the losing crypto position. Include direct income and realised and unrealised value changes. The basic crypto reconciliation for ordinary purchases and sales is:

**Closing value − opening value − purchases + sales**, with all values in euros.

Record swaps as a disposal and acquisition at supported euro values, so the portfolio reconciliation remains complete. Own-wallet transfers do not generate an external purchase or sale. Check rewards, gifts, inheritances, service receipts and other non-purchase movements separately so that income and capital movements are neither omitted nor double counted. Complex protocol rewards or transfers require a documented classification before finalising the formula.

Add the return on other Box 3 assets and subtract allowable debt interest. Ordinary expenses such as trading fees are not a general deduction under this actual-return method; do not net them silently into purchases or sales. Follow the official treatment for any specific exception. There is no tax-free asset allowance or debt threshold in this actual-return calculation, no inflation adjustment and no carryforward of a negative annual return. A negative overall annual result is floored at nil.

Compare this whole-portfolio actual income, allocated correctly for partners, with **ordinary taxable Box 3 income after the allowance ratio**, not with the gross deemed return F. Use the more favourable permitted result. A large crypto loss cannot be used selectively while excluding gains on other assets.

From 2025 the income-tax return offers the actual-return questions. The separate Opgaaf werkelijk rendement form is the route for 2024 and earlier where applicable. Older-year eligibility, assessment finality and deadlines must be checked for that taxpayer; do not promise reopening every year from 2017. Keep submission evidence and reconcile the resulting assessment.

Sources: [official crypto and other portfolio examples](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/rekenvoorbeelden-berekening-werkelijk-rendement), [2025 calculation and actual-return rules](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening).

## Reference-date transactions and losses

A temporary conversion of investments into bank balances around the reference date can be disregarded under peildatumarbitrage. The official rule covers a sale in the three months immediately before January followed by a purchase after January, with no more than three months between sale and purchase, and relevant temporary borrowing. Evidence that the transactions were not undertaken to save tax matters. Where the rule applies, report the affected assets/debts as though the temporary transactions had not occurred, and follow the official corresponding actual-return transaction adjustment. Do not recommend a December sale/January repurchase as automatically effective planning. Transfers between tax boxes require their own anti-abuse assessment.

Selling all crypto does not remove the proceeds from wealth: retained bank balances or other assets still enter the next relevant calculation. An exchange bankruptcy does not automatically make a recoverable claim worthless. Determine economic value, evidence and timing.

A negative overall Box 3 actual return gives no cross-year loss carryforward. For a Box 1 enterprise loss, first offset positive Box 1 income in the same year. A remaining assessed Box 1 loss is offset against the **three preceding years**, then the **nine following years**, in the mandatory order. It cannot offset Box 2 or Box 3 income. Obtain and reconcile the loss determination; corporate loss rules do not apply to this individual calculation.

Sources: [peildatumarbitrage and actual-return adjustment](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/regels_voor_het_tijdelijk_verplaatsen_van_bezittingen_en_schulden), [individual enterprise losses](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/verlies_uit_onderneming).

## Worked checks

These are isolated calculations, not a complete personal tax assessment. Keep the assumptions visible.

### A — Ordinary private holdings in 2025

Single resident, no debts or other assets: bank €20,000 and crypto €150,000 at the reference date. Deemed return is €274 + €8,820 = €9,094. Net base is €170,000; taxable base €112,316. Ordinary income is €9,094 × €112,316 / €170,000 = **€6,008.245318**, giving **€2,162.968314** before filing-system rounding. Rounding the effective return rate early would distort this result. [Calculation basis](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening).

### B — Falling portfolio, actual-return route

Same person and opening balances as A. No crypto purchases, sales or rewards; closing crypto €90,000 and bank interest €250. Actual return is €90,000 − €150,000 + €250 = **−€59,750**, floored to nil. With no other Box 3 return, the actual-return comparison produces nil Box 3 income. For 2025 provide it through the annual return questions. [Calculation basis](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/rekenvoorbeelden-berekening-werkelijk-rendement).

### C — Purchases and sales

Assumed private portfolio: opening €80,000, closing €90,000, purchases €5,000, sales €17,000, no other flows. Actual crypto return is **€22,000**. This is not merely the €10,000 change in the wallet balance. Combine it with all other relevant Box 3 returns before comparing methods. [Calculation basis](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/rekenvoorbeelden-berekening-werkelijk-rendement).

### D — Mining work: limited Box 1 rate illustration

Assume a supported taxable other-work classification, full Dutch national-insurance coverage and below AOW age throughout 2025. Revenue €40,000 less **established current deductible expenses** €15,000 leaves €25,000 taxable Box 1 income; no other Box 1 items. This expense assumption does not authorise immediate deduction of mining equipment: capital assets require the appropriate depreciation analysis. Gross income tax/national insurance is €25,000 × **35.82%** = **€8,955**, before credits and separate healthcare contribution. Other-work income does not receive entrepreneur/MKB deductions. If instead the facts establish enterprise profit, determine eligible deductions before applying tax bands; use the full income-tax method for the final liability. [Calculation basis](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/).

### E — Nil-floor and missing-data decisions

If deductible debt exceeds assets, stop at the nil net/taxable base without dividing by it. If the aggregate deemed return is negative but the taxable asset base is positive, apply the statutory deemed-return nil floor. If actual-return records cover only one wallet, do not claim that its loss eliminates the household's complete Box 3 liability.

Sources: [Box 1 annual tables](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/), [official portfolio examples](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/rekenvoorbeelden-berekening-werkelijk-rendement), [2025 computation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening).

## Filing, records and output

In the 2025 and later return select cryptobezittingen under bank accounts and other assets; follow its annual asset, income and actual-return questions. A return's ordinary summary figures do not remove the need to retain transaction evidence. Do not substitute a generic deadline for the date on the filing invitation or an approved extension. Review the submitted return and assessment together; use the proper correction/objection route if an earlier return used the wrong method.

Keep wallet ownership and reconciliation records, exchange exports, valuations, token rights, receipts, rewards, debt agreements, interest, source versions, calculation assumptions and submission confirmations. Individuals do not have the blanket business bookkeeping retention duty merely for privately owning crypto. Government guidance recommends retaining private tax records for at least five years; retain relevant older evidence where assessments, foreign matters or a dispute require it. Businesses normally retain core administration for seven years, with longer categories where applicable.

DAC8 requires crypto service providers to report client and transaction data from 2026. It does not replace the taxpayer's return or automatically establish the correct tax classification. This guide does not provide a service provider's regulatory reporting implementation or AFM/DNB authorisation advice.

Return the tax year, ownership/residence scope, classification reasoning, complete asset inventory, ordinary calculation, actual-return comparison or missing evidence, partner allocation, rounding, assumptions, source URLs and required referrals. Label a partial calculation as partial and keep any provisional 2026 parameters visible. Do not present a source review as an accountant's attestation.

Sources: [crypto return fields](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/aangifte-doen-en-belasting-betalen-met-cryptos), [DAC8 summary](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/cryptovaluta), [retention guidance](https://www.rijksoverheid.nl/vraag-en-antwoord/inkomstenbelasting/hoe-lang-moet-ik-mijn-financiele-administratie-bewaren).

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
